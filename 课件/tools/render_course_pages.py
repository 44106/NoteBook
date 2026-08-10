from __future__ import annotations

import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / "output" / "oop_course_learning_pack"
IMAGE_DIR = PACK_DIR / "page_images"
THUMB_DIR = PACK_DIR / "contact_sheets"
MANIFEST_PATH = ROOT / "tmp" / "extracted_course" / "manifest.json"


def leading_number(path: Path) -> int:
    match = re.match(r"^(\d+)\b", path.name)
    if not match:
        return 10_000
    return int(match.group(1))


def safe_stem(path: Path) -> str:
    return re.sub(r"[^0-9A-Za-z._-]+", "_", path.stem).strip("_")


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def export_pptx_with_powerpoint(path: Path, dest: Path, width: int = 1600, height: int = 1200) -> None:
    ps_script = f"""
$ErrorActionPreference = 'Stop'
$ppt = New-Object -ComObject PowerPoint.Application
$presentation = $ppt.Presentations.Open('{str(path)}', $true, $false, $false)
$presentation.Export('{str(dest)}', 'JPG', {width}, {height})
$presentation.Close()
$ppt.Quit()
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def normalize_ppt_export_names(dest: Path) -> list[Path]:
    candidate_map = {path.resolve(): path for path in list(dest.glob("*.JPG")) + list(dest.glob("*.jpg"))}
    exported_candidates = list(candidate_map.values())
    exported = sorted(exported_candidates, key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)))
    normalized: list[Path] = []
    for index, source in enumerate(exported, start=1):
        target = dest / f"page_{index:03d}.jpg"
        if target.exists():
            target.unlink()
        source.rename(target)
        normalized.append(target)
    return normalized


def render_pdf(path: Path, dest: Path) -> list[Path]:
    prefix = dest / "page"
    run(["pdftoppm", "-png", "-r", "150", str(path), str(prefix)])
    generated = sorted(dest.glob("page-*.png"), key=lambda p: int(re.search(r"-(\d+)\.png$", p.name).group(1)))
    normalized: list[Path] = []
    for index, source in enumerate(generated, start=1):
        target = dest / f"page_{index:03d}.png"
        if target.exists():
            target.unlink()
        source.rename(target)
        normalized.append(target)
    return normalized


def thumb(image: Image.Image, width: int) -> Image.Image:
    ratio = width / image.width
    height = max(1, int(image.height * ratio))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def create_contact_sheet(images: list[Path], dest: Path, title: str, cols: int = 4, thumb_width: int = 280) -> None:
    if not images:
        return
    font = ImageFont.load_default()
    header_h = 34
    label_h = 20
    gap = 12
    thumbs: list[Image.Image] = []
    for image_path in images:
        with Image.open(image_path) as image:
            thumbs.append(thumb(image.convert("RGB"), thumb_width))
    max_thumb_h = max(image.height for image in thumbs)
    rows = math.ceil(len(thumbs) / cols)
    sheet_w = cols * thumb_width + (cols + 1) * gap
    sheet_h = header_h + rows * (max_thumb_h + label_h + gap) + gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((gap, 10), title, fill=(0, 0, 0), font=font)
    for idx, image in enumerate(thumbs):
        row, col = divmod(idx, cols)
        x = gap + col * (thumb_width + gap)
        y = header_h + row * (max_thumb_h + label_h + gap)
        sheet.paste(image, (x, y))
        draw.text((x, y + image.height + 3), f"Page {idx + 1}", fill=(0, 0, 0), font=font)
    sheet.save(dest, quality=90)


def main() -> None:
    PACK_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    source_files = sorted(
        [p for p in ROOT.iterdir() if p.is_file() and p.suffix.lower() in {".pptx", ".pdf"}],
        key=lambda p: (leading_number(p), p.name.lower()),
    )
    extraction_manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")) if MANIFEST_PATH.exists() else []
    extraction_by_source = {item["source"]: item for item in extraction_manifest}

    render_manifest: list[dict] = []
    for path in source_files:
        lecture = leading_number(path)
        dest = IMAGE_DIR / f"{lecture:02d}_{safe_stem(path)}"
        dest.mkdir(parents=True, exist_ok=True)
        old_images = {old.resolve(): old for old in list(dest.glob("*.jpg")) + list(dest.glob("*.JPG")) + list(dest.glob("*.png"))}
        for old in old_images.values():
            old.unlink()

        if path.suffix.lower() == ".pptx":
            export_pptx_with_powerpoint(path.resolve(), dest.resolve())
            images = normalize_ppt_export_names(dest)
        else:
            images = render_pdf(path.resolve(), dest.resolve())

        contact_sheet = THUMB_DIR / f"{lecture:02d}_{safe_stem(path)}_contact.jpg"
        create_contact_sheet(images, contact_sheet, f"Lecture {lecture}: {path.name}")
        expected_pages = extraction_by_source.get(path.name, {}).get("page_count")
        render_manifest.append(
            {
                "lecture": lecture,
                "source": path.name,
                "image_dir": str(dest.relative_to(PACK_DIR)),
                "image_count": len(images),
                "expected_pages": expected_pages,
                "contact_sheet": str(contact_sheet.relative_to(PACK_DIR)),
                "page_images": [str(image.relative_to(PACK_DIR)) for image in images],
            }
        )
        status = "OK" if expected_pages in (None, len(images)) else f"MISMATCH expected {expected_pages}"
        print(f"{lecture:02d}. {path.name}: rendered {len(images)} images ({status})")

    (PACK_DIR / "render_manifest.json").write_text(json.dumps(render_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Render manifest: {PACK_DIR / 'render_manifest.json'}")


if __name__ == "__main__":
    main()
