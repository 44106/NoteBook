from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_course_pdfs import NOTES, OUT, STY, header_footer
from build_single_lecture_pdf import (
    markdown_to_flowables_text,
    strip_link_noise,
)
import build_visual_review_notes as visual


ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / "extracted"
SOURCE_MD = NOTES / "09_完整细节覆盖版.md"
OUTPUT_PDF = OUT / "人工智能芯片与系统_完整细节覆盖版.pdf"


ADMIN_PATTERNS = [
    "Instructor",
    "TA for",
    "TAs for",
    "Submission Policy",
    "Honest Policy",
    "Q&A",
    "Acknowledgement",
    "Office",
    "Email",
    "Mobile",
    "Homepage",
    "Lab assignments",
    "5%:",
]

EXTENSION_TERMS = [
    "RAIDR",
    "MLWeaving",
    "Cerebras",
    "Wafer Scale",
    "Piranha",
    "Niagara",
    "Sun ROCK",
    "POWER4",
    "POWER5",
    "POWER6",
    "Reading for the Really Interested",
]


def read_note(name: str) -> str:
    return (NOTES / name).read_text(encoding="utf-8")


def normalize(text: str) -> str:
    text = str(text)
    text = text.replace("\uf0e0", "->").replace("\u2192", "->")
    text = text.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def table_to_text(table: list[list[Any]]) -> str:
    rows: list[str] = []
    for row in table:
        cells = [normalize(c) for c in row if normalize(c)]
        if cells:
            rows.append(" | ".join(cells))
    return "；".join(rows)


def flatten_item(item: Any) -> list[str]:
    if item is None:
        return []
    if isinstance(item, str):
        return [normalize(item)]
    if isinstance(item, dict):
        if "table" in item:
            return ["表格：" + table_to_text(item["table"])]
        return [normalize(v) for v in item.values()]
    if isinstance(item, list):
        out: list[str] = []
        for x in item:
            out.extend(flatten_item(x))
        return out
    return [normalize(item)]


def visible_slide_text(slide: dict) -> str:
    raw: list[str] = []
    for item in slide.get("shape_items", []):
        raw.extend(flatten_item(item))
    if not raw:
        for item in slide.get("all_text", []):
            raw.extend(flatten_item(item))

    title = normalize(slide.get("title", ""))
    seen: set[str] = set()
    kept: list[str] = []
    for piece in raw:
        piece = normalize(piece)
        if not piece:
            continue
        if piece == title:
            continue
        if re.fullmatch(r"\d{1,3}", piece):
            continue
        key = piece.lower()
        if key in seen:
            continue
        seen.add(key)
        kept.append(piece)

    text = "；".join(kept)
    text = re.sub(r"；{2,}", "；", text)
    return text[:1600]


def is_admin(slide: dict) -> bool:
    title = normalize(slide.get("title", ""))
    text = visible_slide_text(slide)
    blob = title + " " + text
    return any(p.lower() in blob.lower() for p in ADMIN_PATTERNS)


def is_explicitly_excluded(stem: str, slide_no: int) -> bool:
    return stem == "15-flashattention43" and slide_no >= 11


def is_extension(slide: dict) -> bool:
    blob = normalize(slide.get("title", "")) + " " + visible_slide_text(slide)
    return any(term.lower() in blob.lower() for term in EXTENSION_TERMS)


def load_deck(stem: str) -> dict:
    return json.loads((EXTRACTED / f"{stem}.json").read_text(encoding="utf-8"))


def clean_note_for_body(name: str, title: str) -> str:
    text = read_note(name)
    text = strip_link_noise(text)
    lines = []
    for line in text.splitlines():
        if line.startswith("# "):
            lines.append("# " + title)
        else:
            lines.append(line)
    return "\n".join(lines).strip()


def remove_chinese_inline_code_outside_fences(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
        else:
            lines.append(re.sub(r"`([^`]*[\u4e00-\u9fff][^`]*)`", r"\1", line))
    return "\n".join(lines)


def build_slide_detail_section() -> tuple[str, dict[str, int]]:
    lines: list[str] = [
        "# 第五部分：逐讲逐页可考细节清单",
        "",
        "本部分来自 `extracted/*.json` 的 PPT 可见文本和表格抽取，并结合重点图页清单标注。它不是让你背每一页的页码，而是把每页可能承载的概念、表格字段、图中标签和关键词纳入同一个 PDF，防止复习时只看总结而漏掉细节。",
        "",
        "标记说明：`重点` 表示第 16 讲或图示讲义中反复出现；`图`/`表` 表示该页有图形或表格；`拓展边界` 表示明显历史案例或研究扩展，不作为主背内容，只保留解决什么瓶颈。",
    ]
    stats = {
        "slides_total": 0,
        "included": 0,
        "explicit_excluded": 0,
        "admin_skipped": 0,
        "extension_marked": 0,
        "image_pages": 0,
        "table_pages": 0,
        "key_pages": 0,
    }
    skipped_examples: list[str] = []

    for stem, deck_title in visual.DECKS:
        data = load_deck(stem)
        key_pages = set(visual.KEY_SLIDES.get(stem, []))
        lines.extend(["", f"## {deck_title}", ""])
        for slide in data["slides"]:
            n = int(slide["number"])
            stats["slides_total"] += 1
            if is_explicitly_excluded(stem, n):
                stats["explicit_excluded"] += 1
                if len(skipped_examples) < 30:
                    skipped_examples.append(f"{deck_title} 第 {n} 页：FlashAttention 主体，按老师说明不考")
                continue
            if is_admin(slide):
                stats["admin_skipped"] += 1
                continue

            title = normalize(slide.get("title", "")) or f"Slide {n}"
            body = visible_slide_text(slide)
            if not body and n not in key_pages:
                continue

            tags: list[str] = []
            if n in key_pages:
                tags.append("重点")
                stats["key_pages"] += 1
            if int(slide.get("image_count", 0)) > 0:
                tags.append(f"图{slide.get('image_count')}")
                stats["image_pages"] += 1
            if int(slide.get("table_count", 0)) > 0:
                tags.append(f"表{slide.get('table_count')}")
                stats["table_pages"] += 1
            ext = is_extension(slide)
            if ext:
                tags.append("拓展边界")
                stats["extension_marked"] += 1

            tag_text = "，".join(tags) if tags else "普通"
            prefix = f"- 第 {n} 页 [{tag_text}] {title}"
            if ext:
                lines.append(prefix + "：明显偏历史案例/研究扩展，考试一般不要求背具体型号参数或论文细节；保留其核心作用：说明系统瓶颈、存储/通信/低精度/多核设计为什么重要。")
            else:
                if body:
                    lines.append(prefix + "：" + body)
                else:
                    lines.append(prefix + "。")
            stats["included"] += 1

    lines.extend(
        [
            "",
            "## 排除和降级边界记录",
            "",
            f"- 总 PPT 页数：{stats['slides_total']}。",
            f"- 纳入逐页细节清单页数：{stats['included']}。",
            f"- 第 15 讲 FlashAttention 主体按老师说明排除页数：{stats['explicit_excluded']}。",
            f"- 行政/联系方式/评分规则等非知识点页跳过页数：{stats['admin_skipped']}。",
            f"- 标记为拓展边界但保留瓶颈直觉的页数：{stats['extension_marked']}。",
            "",
            "显式排除示例：",
        ]
    )
    lines.extend([f"- {x}" for x in skipped_examples])
    return "\n".join(lines), stats


def build_markdown() -> tuple[str, dict[str, int]]:
    intro = """# 人工智能芯片与系统：完整细节覆盖版

这份文件是在 `08_完整知识点讲解版` 基础上的扩展版。它的目标不是精简，而是尽量把分章节讲义、图示补充、第 16 讲总复习映射、重点例题、以及 PPT 逐页抽取出的可考文本和表格细节放进同一份 PDF。

排除边界按老师说明执行：第 15 讲 FlashAttention 主体不纳入考试主干；明显研究拓展或历史案例不展开为主背内容，只保留其想说明的系统瓶颈。除此之外，课程主线知识、图中标签、表格字段、状态/时序/通信细节都尽量纳入。
"""

    core = clean_note_for_body("01_完整零基础讲义.md", "第一部分：完整知识点讲解")
    visual_notes = clean_note_for_body("04_逐讲图示与细节补充讲义.md", "第二部分：逐讲图示与细节补充")
    mapping = clean_note_for_body("07_第16讲总复习到前15讲重点映射.md", "第三部分：第16讲总复习重点映射")
    examples = clean_note_for_body("02_重点题型与例题详解.md", "第四部分：重点题型与例题详解")
    slide_details, stats = build_slide_detail_section()
    final = """# 第六部分：闭卷复习检查方式

读完整细节版后，不要只问“看过没有”，要用下面方式检查：能否不看答案写出 Roofline/AMAT/AllReduce 公式；能否手动更新 Tomasula 的 RAT、RS、CDB 和 ROB；能否对 cache 地址序列拆 tag/index/offset 并判断 hit/miss；能否解释 MSI/MESI 状态转换；能否说清 GPU coalescing、bank conflict、tiling、occupancy；能否对 data/pipeline/tensor parallel 说出切分对象和通信对象。
"""
    text = "\n\n".join([intro, core, visual_notes, mapping, examples, slide_details, final])
    text = remove_chinese_inline_code_outside_fences(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n", stats


def build_pdf(markdown: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=14 * mm,
        leftMargin=14 * mm,
        topMargin=15 * mm,
        bottomMargin=17 * mm,
        title="人工智能芯片与系统完整细节覆盖版",
        author="Codex",
    )
    max_w = A4[0] - doc.leftMargin - doc.rightMargin
    story = [
        Paragraph("人工智能芯片与系统", STY["title"]),
        Paragraph("完整细节覆盖版", STY["title"]),
        Spacer(1, 10),
        Paragraph("面向期末复习：包含核心讲解、图示细节、第 16 讲映射、例题方法和逐页可考细节清单。", STY["body"]),
        Spacer(1, 12),
    ]
    story.extend(markdown_to_flowables_text(markdown, max_w))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return OUTPUT_PDF


def main() -> int:
    markdown, stats = build_markdown()
    SOURCE_MD.write_text(markdown, encoding="utf-8")
    print(SOURCE_MD)
    print(stats)
    print(build_pdf(markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
