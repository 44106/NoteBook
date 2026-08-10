from __future__ import annotations

import re
import sys
from pathlib import Path

import win32com.client


def natural_key(path: Path) -> tuple[int, str]:
    match = re.match(r"^(\d+)", path.name)
    if match:
        return int(match.group(1)), path.name.lower()
    return 999, path.name.lower()


def safe_name(name: str) -> str:
    return re.sub(r"[^\w.-]+", "_", name, flags=re.UNICODE)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "rendered_slides"
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
    out.mkdir(parents=True, exist_ok=True)

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True
    try:
        for pptx in sorted(root.glob("*.pptx"), key=natural_key):
            deck_dir = out / safe_name(pptx.stem)
            deck_dir.mkdir(parents=True, exist_ok=True)
            pres = app.Presentations.Open(str(pptx.resolve()), WithWindow=False)
            try:
                slide_count = pres.Slides.Count
                height = int(width * pres.PageSetup.SlideHeight / pres.PageSetup.SlideWidth)
                for idx in range(1, slide_count + 1):
                    target = deck_dir / f"slide_{idx:03d}.png"
                    if target.exists() and target.stat().st_size > 0:
                        continue
                    pres.Slides(idx).Export(str(target.resolve()), "PNG", width, height)
                print(f"rendered {pptx.name}: {slide_count} slides -> {deck_dir}")
            finally:
                pres.Close()
    finally:
        app.Quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
