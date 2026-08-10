from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)

from build_course_pdfs import (
    BASE_FONT,
    NOTES,
    OUT,
    STY,
    ParseState,
    clean_line,
    esc,
    flush_code,
    flush_list,
    flush_table,
    header_footer,
    parse_table,
)


SOURCE_MD = OUT.parent.parent / "期末复习资料" / "08_完整知识点讲解版.md"
OUTPUT_PDF = OUT / "人工智能芯片与系统_完整知识点讲解版.pdf"


def read_note(name: str) -> str:
    return (NOTES / name).read_text(encoding="utf-8")


def strip_link_noise(text: str) -> str:
    """Keep explanations, remove navigation-only slide links and file references."""
    kept: list[str] = []
    skip_table = False
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()

        if "../rendered_slides/" in line or "../slide_contact_sheets/" in line:
            continue
        if "contact sheet" in line.lower():
            continue
        if stripped.startswith("| 讲次 ") or stripped.startswith("| 文件 "):
            skip_table = True
            continue
        if skip_table:
            if stripped.startswith("|"):
                continue
            skip_table = False
        if stripped.startswith("关键图页") or stripped.startswith("典型页"):
            continue
        if stripped.startswith("- 第16讲页") or stripped.startswith("- 对应前面课程页"):
            continue
        if stripped.startswith("使用方法"):
            continue
        if "05_逐页图文索引" in line or "04_逐讲图示" in line or "01_完整零基础讲义" in line:
            continue
        if stripped.startswith("阅读顺序建议"):
            continue

        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
        kept.append(line)

    cleaned = "\n".join(kept)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def section_from(text: str, heading: str) -> str:
    idx = text.find(heading)
    return text[idx:] if idx >= 0 else text


def drop_sections(text: str, headings: list[str]) -> str:
    lines = text.splitlines()
    out: list[str] = []
    dropping = False
    drop_level = 0
    for line in lines:
        m = re.match(r"^(#+)\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if any(title.startswith(h) for h in headings):
                dropping = True
                drop_level = level
                continue
            if dropping and level <= drop_level:
                dropping = False
        if not dropping:
            out.append(line)
    return "\n".join(out)


def compact_overview_focus(text: str) -> str:
    """Turn the Lecture 16 mapping into a readable priority checklist."""
    text = strip_link_noise(text)
    text = drop_sections(text, ["总复习页优先级", "与现有资料的对应"])
    lines = text.splitlines()
    out: list[str] = ["# 第三部分：第16讲总复习重点回灌清单"]
    keep = False
    for line in lines:
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            if title.startswith("14. 课程行政页"):
                break
            out.append("")
            out.append(line)
            keep = True
            continue
        stripped = line.strip()
        if not keep:
            continue
        if stripped.startswith("- 必须掌握") or stripped.startswith("- 常见考法"):
            out.append(line)
            continue
        if stripped.startswith("- ") and not any(
            bad in stripped for bad in ["第16讲页", "对应前面课程页"]
        ):
            out.append(line)
            continue
        if stripped.startswith("  - "):
            out.append(line)
    return "\n".join(out).strip()


def build_single_markdown() -> str:
    intro = """# 人工智能芯片与系统：完整知识点讲解版

这是一份单文件讲义。它不要求你再去翻 Markdown 链接，也不把原 PPT 截图当作主要内容。正文按“从零理解 -> 期末重点 -> 图表含义 -> 例题方法”的顺序组织，目标是让你能直接从头读到尾完成复习。

考试边界按老师说明处理：第 1-16 讲 PPT 都纳入复习；第 15 讲 FlashAttention 主体部分不作为考试重点；明显前沿研究介绍只保留“它想解决什么瓶颈”的直觉，不作为公式、状态表或主背内容。

阅读方法很简单：先读第一部分建立完整知识体系；再读第二部分理解 PPT 图和表背后的含义；第三部分按第 16 讲总复习检查重点；最后用第四部分掌握老师点名的题型。
"""

    core = read_note("01_完整零基础讲义.md")
    core = core.replace("# 人工智能芯片与系统完整零基础讲义", "# 第一部分：完整知识点讲解")

    visual = read_note("04_逐讲图示与细节补充讲义.md")
    visual = section_from(visual, "## 1. 读图总方法")
    visual = "# 第二部分：PPT 图表与细节的文字解释\n\n" + strip_link_noise(visual)

    overview = compact_overview_focus(read_note("07_第16讲总复习到前15讲重点映射.md"))

    examples = read_note("02_重点题型与例题详解.md")
    examples = examples.replace("# 重点题型与例题详解", "# 第四部分：重点题型与例题详解")

    final_check = """
# 第五部分：考前最后一遍怎么背

不要把这门课当成纯背诵课。闭卷复习时，优先保证自己能主动写出以下内容：性能模型公式、流水线和乱序执行状态更新、cache 地址拆分、coherence 状态含义、GPU 优化瓶颈、AI 加速器为什么用 buffer/dataflow/systolic array、并行训练每种切法对应什么通信。

最容易丢分的地方通常不是“完全没见过”，而是概念混在一起：ISA 和 microarchitecture 混淆，latency 和 throughput 混淆，RAW 和 WAR/WAW 混淆，ROB 和 RS 混淆，coherence 和 consistency 混淆，row-wise 和 column-wise tensor parallel 的通信混淆。每遇到一道题，先写清对象、状态、时间和通信，再代公式或更新表格。
"""

    text = "\n\n".join([intro, core, visual, overview, examples, final_check])
    text = strip_link_noise(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def markdown_to_flowables_text(markdown: str, max_w: float) -> list:
    story: list = []
    state = ParseState(inserted_images=set())
    skip_mermaid = False

    def flush_numbered() -> None:
        numbered = getattr(state, "numbered_items", None)
        if numbered:
            for item in numbered:
                story.append(Paragraph(esc(item), STY["body"]))
            state.numbered_items = None

    for raw in markdown.splitlines():
        line = clean_line(raw.rstrip())

        if line.startswith("```"):
            if state.in_code:
                flush_code(story, state)
                state.in_code = False
                skip_mermaid = False
            else:
                flush_table(story, state, max_w)
                flush_list(story, state)
                flush_numbered()
                lang = line.strip("`").strip().lower()
                skip_mermaid = lang == "mermaid"
                state.in_code = True
                state.code_lines = [] if not skip_mermaid else None
            continue

        if state.in_code:
            if not skip_mermaid and state.code_lines is not None:
                state.code_lines.append(line)
            continue

        if not line.strip():
            flush_table(story, state, max_w)
            flush_list(story, state)
            flush_numbered()
            continue

        if re.match(r"^\|.*\|$", line):
            flush_list(story, state)
            flush_numbered()
            state.table_lines = state.table_lines or []
            state.table_lines.append(line)
            continue

        flush_table(story, state, max_w)

        if line.startswith("# "):
            flush_list(story, state)
            flush_numbered()
            if story:
                story.append(PageBreak())
            story.append(Paragraph(esc(line[2:].strip()), STY["h1"]))
            continue
        if line.startswith("## "):
            flush_list(story, state)
            flush_numbered()
            story.append(Paragraph(esc(line[3:].strip()), STY["h2"]))
            continue
        if line.startswith("### "):
            flush_list(story, state)
            flush_numbered()
            story.append(Paragraph(esc(line[4:].strip()), STY["h3"]))
            continue
        if line.startswith("#### "):
            flush_list(story, state)
            flush_numbered()
            story.append(Paragraph(esc(line[5:].strip()), STY["h3"]))
            continue

        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            flush_numbered()
            state.list_items = state.list_items or []
            state.list_items.append(bullet.group(1).strip())
            continue

        numbered = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if numbered:
            flush_list(story, state)
            state.numbered_items = getattr(state, "numbered_items", None) or []
            state.numbered_items.append(f"{numbered.group(1)}. {numbered.group(2).strip()}")
            continue

        flush_list(story, state)
        flush_numbered()
        story.append(Paragraph(esc(line), STY["body"]))

    flush_table(story, state, max_w)
    flush_list(story, state)
    flush_numbered()
    flush_code(story, state)
    return story


def build_pdf(markdown: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=16 * mm,
        bottomMargin=18 * mm,
        title="人工智能芯片与系统完整知识点讲解版",
        author="Codex",
    )
    max_w = A4[0] - doc.leftMargin - doc.rightMargin
    story = [
        Paragraph("人工智能芯片与系统", STY["title"]),
        Paragraph("完整知识点讲解版", STY["title"]),
        Spacer(1, 10),
        Paragraph(
            "单文件正文讲义：不依赖跳转链接，不以截图附录代替讲解。覆盖第 1-16 讲可考知识点，按老师说明排除第 15 讲 FlashAttention 主体细节。",
            STY["body"],
        ),
        Spacer(1, 12),
    ]
    story.extend(markdown_to_flowables_text(markdown, max_w))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return OUTPUT_PDF


def main() -> int:
    markdown = build_single_markdown()
    SOURCE_MD.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_MD.write_text(markdown, encoding="utf-8")
    print(SOURCE_MD)
    print(build_pdf(markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
