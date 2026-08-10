from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    Image as RLImage,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "期末复习资料"
RENDERED = ROOT / "rendered_slides"
EXTRACTED = ROOT / "extracted"
OUT = ROOT / "output" / "pdf"


MAIN_MD = [
    "00_使用说明与知识地图.md",
    "07_第16讲总复习到前15讲重点映射.md",
    "01_完整零基础讲义.md",
    "04_逐讲图示与细节补充讲义.md",
    "02_重点题型与例题详解.md",
    "03_自测题与闪卡.md",
    "06_覆盖自查报告.md",
]


DECKS = [
    ("1_intro_course-neuman_isa-single-multi-cycle-pipeline", "第1讲 Introduction / ISA / CPU"),
    ("2-pipelining-reorder-buffer", "第2讲 Pipeline Hazard / ROB"),
    ("3-tomasula", "第3讲 Tomasula"),
    ("4-superscalar-cores-SIMD", "第4讲 Superscalar / SIMD / Multicore"),
    ("5_memory", "第5讲 Memory"),
    ("6-gpus-architecture", "第6讲 GPU Architecture"),
    ("7-gpus-optimization", "第7讲 GPU Optimization"),
    ("8-cache", "第8讲 Cache"),
    ("9-cache-coherence", "第9讲 Cache Coherence"),
    ("10-cache-coherence-consistency", "第10讲 Coherence / Consistency"),
    ("11--accelerator_motivation", "第11讲 Accelerator Motivation"),
    ("12-davinci-tpu_自动保存的_", "第12讲 DaVinci / TPU"),
    ("13-hwj-cann-mindspore", "第13讲 Runtime / Framework"),
    ("14-parallel-training", "第14讲 Parallel Training"),
    ("15-flashattention43", "第15讲 ZeRO / FlashAttention"),
    ("16_overview_DESKTOP-H8IOQ49_s_conflicted_copy_2025-06-11_", "第16讲 Overview"),
]


FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/msyh.ttc"),
    Path("C:/Windows/Fonts/simhei.ttf"),
    Path("C:/Windows/Fonts/simsun.ttc"),
]


def register_fonts() -> str:
    for path in FONT_CANDIDATES:
        if path.exists():
            pdfmetrics.registerFont(TTFont("CN", str(path)))
            pdfmetrics.registerFont(TTFont("CN-Bold", str(path)))
            return "CN"
    return "Helvetica"


BASE_FONT = register_fonts()
BOLD_FONT = "CN-Bold" if BASE_FONT == "CN" else "Helvetica-Bold"
MONO_FONT = "Courier"


def styles():
    ss = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=ss["Title"],
            fontName=BOLD_FONT,
            fontSize=24,
            leading=32,
            alignment=TA_CENTER,
            spaceAfter=18,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=ss["Heading1"],
            fontName=BOLD_FONT,
            fontSize=18,
            leading=24,
            spaceBefore=14,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=ss["Heading2"],
            fontName=BOLD_FONT,
            fontSize=14,
            leading=19,
            spaceBefore=10,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=ss["Heading3"],
            fontName=BOLD_FONT,
            fontSize=12,
            leading=17,
            spaceBefore=8,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body",
            parent=ss["BodyText"],
            fontName=BASE_FONT,
            fontSize=9.6,
            leading=14,
            alignment=TA_LEFT,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "small",
            parent=ss["BodyText"],
            fontName=BASE_FONT,
            fontSize=8,
            leading=11,
            spaceAfter=3,
        ),
        "caption": ParagraphStyle(
            "caption",
            parent=ss["BodyText"],
            fontName=BASE_FONT,
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#555555"),
            alignment=TA_CENTER,
            spaceBefore=3,
            spaceAfter=6,
        ),
        "code": ParagraphStyle(
            "code",
            parent=ss["Code"],
            fontName=BASE_FONT,
            fontSize=7.2,
            leading=9,
            leftIndent=4,
            rightIndent=4,
            backColor=colors.HexColor("#F5F5F5"),
        ),
        "toc": ParagraphStyle(
            "toc",
            parent=ss["BodyText"],
            fontName=BASE_FONT,
            fontSize=9,
            leading=13,
            leftIndent=8,
        ),
    }


STY = styles()


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def inline_code_font(match: re.Match[str]) -> str:
    content = match.group(1)
    font = BASE_FONT if has_cjk(content) else MONO_FONT
    return f"<font name='{font}'>{content}</font>"


def esc(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", inline_code_font, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    return text


def clean_line(line: str) -> str:
    return line.replace("\uf0e0", "->").replace("\u2192", "->").replace("\u2011", "-")


def resolve_link(link: str) -> Path | None:
    if not link.startswith("../"):
        return None
    p = (NOTES / link).resolve()
    if p.exists() and p.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        return p
    return None


def image_flowable(path: Path, max_w: float, max_h: float) -> list[Flowable]:
    with Image.open(path) as im:
        w, h = im.size
    scale = min(max_w / w, max_h / h)
    width, height = w * scale, h * scale
    return [
        RLImage(str(path), width=width, height=height),
        Paragraph(path.parent.name + "/" + path.name, STY["caption"]),
    ]


def parse_table(lines: list[str], max_w: float) -> Table:
    rows: list[list[str]] = []
    for line in lines:
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", p or "") for p in parts):
            continue
        rows.append(parts)
    if not rows:
        rows = [[""]]
    cols = max(len(r) for r in rows)
    rows = [r + [""] * (cols - len(r)) for r in rows]
    col_w = max_w / cols
    data = [[Paragraph(esc(c), STY["small"]) for c in r] for r in rows]
    tbl = Table(data, colWidths=[col_w] * cols, repeatRows=1)
    tbl.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), BASE_FONT),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EDEDED")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BBBBBB")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return tbl


@dataclass
class ParseState:
    in_code: bool = False
    code_lines: list[str] | None = None
    table_lines: list[str] | None = None
    list_items: list[str] | None = None
    inserted_images: set[str] | None = None


def flush_table(story: list[Flowable], state: ParseState, max_w: float) -> None:
    if state.table_lines:
        story.append(parse_table(state.table_lines, max_w))
        story.append(Spacer(1, 4))
        state.table_lines = None


def flush_list(story: list[Flowable], state: ParseState) -> None:
    if state.list_items:
        items = [ListItem(Paragraph(esc(i), STY["body"]), leftIndent=10) for i in state.list_items]
        story.append(ListFlowable(items, bulletType="bullet", leftIndent=14, bulletFontName=BASE_FONT))
        state.list_items = None


def flush_code(story: list[Flowable], state: ParseState) -> None:
    if state.code_lines is not None:
        text = "\n".join(state.code_lines)
        story.append(Preformatted(text[:6000], STY["code"]))
        story.append(Spacer(1, 5))
        state.code_lines = None


def add_images_from_line(story: list[Flowable], line: str, state: ParseState, max_w: float) -> bool:
    inserted = False
    for label, link in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line):
        path = resolve_link(link)
        if not path:
            continue
        key = str(path)
        if key in state.inserted_images:
            continue
        state.inserted_images.add(key)
        story.extend(image_flowable(path, max_w, 10.5 * cm))
        inserted = True
    return inserted


def markdown_to_flowables(markdown: str, max_w: float, source_name: str) -> list[Flowable]:
    story: list[Flowable] = []
    state = ParseState(inserted_images=set())
    story.append(PageBreak())
    story.append(Paragraph(source_name, STY["h1"]))

    skip_mermaid = False
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
            continue

        if re.match(r"^\|.*\|$", line):
            flush_list(story, state)
            state.table_lines = state.table_lines or []
            state.table_lines.append(line)
            continue

        flush_table(story, state, max_w)

        if line.startswith("# "):
            flush_list(story, state)
            story.append(PageBreak())
            story.append(Paragraph(esc(line[2:].strip()), STY["h1"]))
            continue
        if line.startswith("## "):
            flush_list(story, state)
            story.append(Paragraph(esc(line[3:].strip()), STY["h2"]))
            continue
        if line.startswith("### "):
            flush_list(story, state)
            story.append(Paragraph(esc(line[4:].strip()), STY["h3"]))
            continue

        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            item = m.group(1).strip()
            add_images_from_line(story, item, state, max_w)
            text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", item)
            state.list_items = state.list_items or []
            state.list_items.append(text)
            continue

        flush_list(story, state)
        add_images_from_line(story, line, state, max_w)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
        if text.strip():
            story.append(Paragraph(esc(text), STY["body"]))

    flush_table(story, state, max_w)
    flush_list(story, state)
    flush_code(story, state)
    return story


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(BASE_FONT, 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(doc.leftMargin, 12 * mm, "人工智能芯片与系统期末复习资料")
    canvas.drawRightString(A4[0] - doc.rightMargin, 12 * mm, f"第 {doc.page} 页")
    canvas.restoreState()


def build_main_pdf() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / "人工智能芯片与系统_完整期末复习讲义_含关键图.pdf"
    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=16 * mm,
        bottomMargin=18 * mm,
        title="人工智能芯片与系统完整期末复习讲义",
        author="Codex",
    )
    max_w = A4[0] - doc.leftMargin - doc.rightMargin
    story: list[Flowable] = [
        Paragraph("人工智能芯片与系统", STY["title"]),
        Paragraph("完整期末复习讲义（含关键 PPT 图）", STY["title"]),
        Spacer(1, 12),
        Paragraph(
            "本 PDF 由期末复习资料整合生成。第 15 讲 FlashAttention 主体按老师说明不列为考试重点；第 16 讲总复习中出现的知识点已回指前 1-15 讲并按重点处理。",
            STY["body"],
        ),
        Spacer(1, 16),
        Paragraph("目录", STY["h1"]),
    ]
    for name in MAIN_MD:
        story.append(Paragraph(name, STY["toc"]))

    for name in MAIN_MD:
        text = (NOTES / name).read_text(encoding="utf-8")
        story.extend(markdown_to_flowables(text, max_w, name))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return out


def deck_data(stem: str) -> dict:
    return json.loads((EXTRACTED / f"{stem}.json").read_text(encoding="utf-8"))


def build_slide_appendix_pdf() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / "人工智能芯片与系统_全PPT截图附录_1708页.pdf"
    page_size = landscape(A4)
    doc = SimpleDocTemplate(
        str(out),
        pagesize=page_size,
        rightMargin=10 * mm,
        leftMargin=10 * mm,
        topMargin=10 * mm,
        bottomMargin=12 * mm,
        title="人工智能芯片与系统全PPT截图附录",
        author="Codex",
    )
    max_w = page_size[0] - doc.leftMargin - doc.rightMargin
    max_h = page_size[1] - doc.topMargin - doc.bottomMargin - 18 * mm
    story: list[Flowable] = [
        Paragraph("人工智能芯片与系统 全 PPT 截图附录", STY["title"]),
        Paragraph("共 16 份 PPT，1708 页截图。用于在 PDF 内直接查原图，不需要回到 Markdown 链接。", STY["body"]),
        PageBreak(),
    ]

    for stem, title in DECKS:
        data = deck_data(stem)
        story.append(Paragraph(f"{title}（{len(data['slides'])} 页）", STY["h1"]))
        for s in data["slides"]:
            n = int(s["number"])
            path = RENDERED / stem / f"slide_{n:03d}.png"
            if not path.exists():
                continue
            marker = ""
            if stem == S15_STEM and n >= 11:
                marker = "（FlashAttention 主体，按老师说明不考）"
            title_line = f"{title} - Slide {n:03d}: {s.get('title','')}{marker}"
            with Image.open(path) as im:
                w, h = im.size
            scale = min(max_w / w, max_h / h)
            img = RLImage(str(path), width=w * scale, height=h * scale)
            story.append(KeepTogether([Paragraph(esc(title_line), STY["h2"]), img]))
            story.append(PageBreak())
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return out


S15_STEM = "15-flashattention43"


def main() -> int:
    main_pdf = build_main_pdf()
    print(main_pdf)
    appendix_pdf = build_slide_appendix_pdf()
    print(appendix_pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
