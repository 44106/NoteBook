from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / "output" / "oop_course_learning_pack"
RAW_TEXT_SRC = ROOT / "tmp" / "extracted_course" / "texts"
EXTRACT_MANIFEST = ROOT / "tmp" / "extracted_course" / "manifest.json"
RENDER_MANIFEST = PACK_DIR / "render_manifest.json"
PAGEWISE_DIR = PACK_DIR / "pagewise"
RAW_TEXT_DEST = PACK_DIR / "raw_texts"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def slug(text: str) -> str:
    return re.sub(r"[^0-9A-Za-z._-]+", "_", text).strip("_")


def parse_pages(markdown_path: Path) -> list[dict]:
    text = markdown_path.read_text(encoding="utf-8")
    chunks = re.split(r"\n## Page (\d+)\n\n", text)
    pages: list[dict] = []
    for idx in range(1, len(chunks), 2):
        page = int(chunks[idx])
        page_text = chunks[idx + 1].strip()
        pages.append({"page": page, "text": page_text})
    return pages


def relative_from_pagewise(path: Path) -> str:
    return path.relative_to(PAGEWISE_DIR).as_posix()


def relative_from_pack(path: Path) -> str:
    return path.relative_to(PACK_DIR).as_posix()


def write_pagewise_notes(extract_items: list[dict], render_items: list[dict]) -> list[dict]:
    PAGEWISE_DIR.mkdir(parents=True, exist_ok=True)
    written: list[dict] = []
    render_by_source = {item["source"]: item for item in render_items}
    for item in extract_items:
        render = render_by_source[item["source"]]
        contact_sheet = render["contact_sheet"].replace("\\", "/")
        raw_md = ROOT / item["markdown"]
        pages = parse_pages(raw_md)
        out_path = PAGEWISE_DIR / f"{item['lecture']:02d}_{slug(Path(item['source']).stem)}_pagewise.md"
        lines = [
            f"# Lecture {item['lecture']:02d}: {Path(item['source']).stem}",
            "",
            f"- Source: `{item['source']}`",
            f"- Pages: {item['page_count']}",
            f"- Rendered page images: {render['image_count']}",
            f"- Contact sheet: [open](../{contact_sheet})",
            f"- Raw extracted text: [open](../raw_texts/{Path(item['markdown']).name})",
            "",
            "> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。",
            "",
        ]
        for page in pages:
            image_rel_pack = render["page_images"][page["page"] - 1]
            image_path = PACK_DIR / image_rel_pack
            image_rel = Path("..") / image_path.relative_to(PACK_DIR)
            lines.extend(
                [
                    f"## Page {page['page']}",
                    "",
                    f"![Lecture {item['lecture']} page {page['page']}]({image_rel.as_posix()})",
                    "",
                    "Extracted text:",
                    "",
                    "```text",
                    page["text"] if page["text"] else "[No extractable text]",
                    "```",
                    "",
                ]
            )
        out_path.write_text("\n".join(lines), encoding="utf-8")
        written.append(
            {
                "lecture": item["lecture"],
                "source": item["source"],
                "path": out_path.relative_to(PACK_DIR).as_posix(),
                "pages": item["page_count"],
            }
        )
    return written


def copy_raw_texts() -> None:
    RAW_TEXT_DEST.mkdir(parents=True, exist_ok=True)
    for source in RAW_TEXT_SRC.glob("*.md"):
        shutil.copy2(source, RAW_TEXT_DEST / source.name)


def write_readme(extract_items: list[dict], render_items: list[dict], pagewise: list[dict]) -> None:
    pagewise_by_source = {item["source"]: item for item in pagewise}
    render_by_source = {item["source"]: item for item in render_items}
    total_pages = sum(item["page_count"] for item in extract_items)
    total_chars = sum(item["total_chars"] for item in extract_items)
    total_low = sum(len(item["low_text_pages"]) for item in extract_items)
    lines = [
        "# 面向对象程序设计课程学习包",
        "",
        "这个目录保留了 15 讲课件的完整学习底稿：逐页图片、逐页文字抽取、每讲缩略图总览，以及后续整理出的中文讲义。",
        "",
        "## 覆盖情况",
        "",
        f"- 课件文件：{len(extract_items)} 个",
        f"- 页面/幻灯片总数：{total_pages}",
        f"- 渲染页面图片：{sum(item['image_count'] for item in render_items)} 张",
        f"- 自动抽取文字量：{total_chars} 字符",
        f"- 低文本页：{total_low} 页；这些页面通常包含图、类图、对象图、代码截图或示意图，请以页面图片为准。",
        "",
        "## 建议阅读顺序",
        "",
        "1. 先读 [完整零基础讲义](完整零基础讲义.md)，建立整门课的知识结构。",
        "2. 再打开对应讲次的逐页底稿，对照原始图片和抽取文字复习细节。",
        "3. 图示、类图、对象图、内存图、代码截图以 `page_images/` 和 `pagewise/` 中的页面图片为准。",
        "",
        "## 逐讲入口",
        "",
        "| 讲次 | 课件 | 页数 | 逐页原文与图片 | 缩略图总览 | 原始抽取文本 |",
        "|---:|---|---:|---|---|---|",
    ]
    for item in extract_items:
        pagewise_item = pagewise_by_source[item["source"]]
        render = render_by_source[item["source"]]
        contact_sheet = render["contact_sheet"].replace("\\", "/")
        lines.append(
            f"| {item['lecture']:02d} | {item['source']} | {item['page_count']} | "
            f"[打开]({pagewise_item['path']}) | [打开]({contact_sheet}) | "
            f"[打开](raw_texts/{Path(item['markdown']).name}) |"
        )
    lines.extend(
        [
            "",
            "## 文件说明",
            "",
            "- `page_images/`：每一页课件的完整渲染图片，用来保留所有图示和版面信息。",
            "- `contact_sheets/`：每讲缩略图总览，便于快速检查图示和知识分布。",
            "- `pagewise/`：逐页图片 + 逐页自动抽取文字，是讲义整理的可追溯底稿。",
            "- `raw_texts/`：从 PPTX/PDF 直接抽取出的逐页文本。",
            "- `render_manifest.json`：图片渲染清单。",
            "",
        ]
    )
    (PACK_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    PACK_DIR.mkdir(parents=True, exist_ok=True)
    extract_items = read_json(EXTRACT_MANIFEST)
    render_items = read_json(RENDER_MANIFEST)
    copy_raw_texts()
    pagewise = write_pagewise_notes(extract_items, render_items)
    write_readme(extract_items, render_items, pagewise)
    print(f"Wrote pack README: {PACK_DIR / 'README.md'}")
    print(f"Wrote pagewise notes: {len(pagewise)}")


if __name__ == "__main__":
    main()
