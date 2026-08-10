from __future__ import annotations

import json
import re
import subprocess
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tmp" / "extracted_course"
TEXT_DIR = OUT_DIR / "texts"
PAGE_DIR = OUT_DIR / "pages"
MANIFEST_PATH = OUT_DIR / "manifest.json"

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def leading_number(path: Path) -> int:
    match = re.match(r"^(\d+)\b", path.name)
    if not match:
        return 10_000
    return int(match.group(1))


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def extract_pptx_paragraphs_from_xml(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for paragraph in root.findall(".//a:p", NS):
        parts: list[str] = []
        for node in paragraph.iter():
            if node.tag == f"{{{NS['a']}}}t" and node.text:
                parts.append(node.text)
            elif node.tag == f"{{{NS['a']}}}br":
                parts.append("\n")
            elif node.tag == f"{{{NS['a']}}}tab":
                parts.append("\t")
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def extract_pptx(path: Path) -> dict:
    slides: list[dict] = []
    with zipfile.ZipFile(path) as zf:
        slide_names = sorted(
            [name for name in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", name)],
            key=lambda name: int(re.search(r"slide(\d+)\.xml$", name).group(1)),
        )
        notes_by_index: dict[int, list[str]] = {}
        for name in zf.namelist():
            match = re.match(r"ppt/notesSlides/notesSlide(\d+)\.xml$", name)
            if match:
                notes_by_index[int(match.group(1))] = extract_pptx_paragraphs_from_xml(zf.read(name))

        for index, name in enumerate(slide_names, start=1):
            paragraphs = extract_pptx_paragraphs_from_xml(zf.read(name))
            notes = notes_by_index.get(index, [])
            text_parts = []
            if paragraphs:
                text_parts.append("\n".join(paragraphs))
            if notes:
                text_parts.append("Speaker notes:\n" + "\n".join(notes))
            text = clean_text("\n\n".join(text_parts))
            slides.append(
                {
                    "page": index,
                    "text": text,
                    "char_count": len(text),
                    "line_count": len(text.splitlines()) if text else 0,
                }
            )
    return {"kind": "pptx", "page_count": len(slides), "pages": slides}


def run_text_command(args: list[str]) -> str:
    completed = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return completed.stdout.decode("utf-8", errors="replace")


def pdf_page_count(path: Path) -> int:
    output = run_text_command(["pdfinfo", str(path)])
    for line in output.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not determine page count for {path}")


def extract_pdf(path: Path) -> dict:
    count = pdf_page_count(path)
    pages: list[dict] = []
    for page in range(1, count + 1):
        text = run_text_command(
            ["pdftotext", "-layout", "-enc", "UTF-8", "-f", str(page), "-l", str(page), str(path), "-"]
        )
        text = clean_text(text.replace("\x0c", ""))
        pages.append(
            {
                "page": page,
                "text": text,
                "char_count": len(text),
                "line_count": len(text.splitlines()) if text else 0,
            }
        )
    return {"kind": "pdf", "page_count": count, "pages": pages}


def write_markdown_for_file(path: Path, data: dict) -> Path:
    lecture_no = leading_number(path)
    dest = TEXT_DIR / f"{lecture_no:02d}-{path.stem}.md"
    parts = [f"# Lecture {lecture_no}: {path.stem}", "", f"Source: `{path.name}`", f"Pages: {data['page_count']}", ""]
    for page in data["pages"]:
        parts.extend(
            [
                f"## Page {page['page']}",
                "",
                page["text"] if page["text"] else "[No extractable text]",
                "",
            ]
        )
    dest.write_text("\n".join(parts), encoding="utf-8")
    return dest


def main() -> None:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_DIR.mkdir(parents=True, exist_ok=True)

    source_files = sorted(
        [p for p in ROOT.iterdir() if p.is_file() and p.suffix.lower() in {".pptx", ".pdf"}],
        key=lambda p: (leading_number(p), p.name.lower()),
    )

    manifest: list[dict] = []
    for path in source_files:
        if path.suffix.lower() == ".pptx":
            data = extract_pptx(path)
        else:
            data = extract_pdf(path)

        markdown_path = write_markdown_for_file(path, data)
        low_text_pages = [
            {"page": page["page"], "char_count": page["char_count"], "line_count": page["line_count"]}
            for page in data["pages"]
            if page["char_count"] < 20
        ]
        manifest.append(
            {
                "lecture": leading_number(path),
                "source": path.name,
                "kind": data["kind"],
                "page_count": data["page_count"],
                "markdown": str(markdown_path.relative_to(ROOT)),
                "total_chars": sum(page["char_count"] for page in data["pages"]),
                "low_text_pages": low_text_pages,
            }
        )

    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Extracted {len(manifest)} files")
    print(f"Manifest: {MANIFEST_PATH}")
    for item in manifest:
        print(
            f"{item['lecture']:02d}. {item['source']} | {item['kind']} | "
            f"{item['page_count']} pages | {item['total_chars']} chars | "
            f"low-text pages: {len(item['low_text_pages'])}"
        )


if __name__ == "__main__":
    main()
