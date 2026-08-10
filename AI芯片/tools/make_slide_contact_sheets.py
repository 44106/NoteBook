from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rendered_slides")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("slide_contact_sheets")
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    thumb_w = int(sys.argv[4]) if len(sys.argv) > 4 else 320
    out.mkdir(parents=True, exist_ok=True)

    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()

    for deck in sorted([p for p in root.iterdir() if p.is_dir()]):
        imgs = sorted(deck.glob("slide_*.png"))
        if not imgs:
            continue
        first = Image.open(imgs[0])
        aspect = first.height / first.width
        thumb_h = int(thumb_w * aspect)
        label_h = 28
        rows = math.ceil(len(imgs) / cols)
        sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
        draw = ImageDraw.Draw(sheet)
        for i, img_path in enumerate(imgs):
            img = Image.open(img_path).convert("RGB")
            img.thumbnail((thumb_w, thumb_h))
            x = (i % cols) * thumb_w
            y = (i // cols) * (thumb_h + label_h)
            sheet.paste(img, (x, y))
            draw.rectangle([x, y + thumb_h, x + thumb_w, y + thumb_h + label_h], fill=(245, 245, 245))
            draw.text((x + 6, y + thumb_h + 5), img_path.stem.replace("slide_", "Slide "), fill=(0, 0, 0), font=font)
        target = out / f"{deck.name}_contact.jpg"
        sheet.save(target, quality=90)
        print(f"wrote {target} ({len(imgs)} slides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
