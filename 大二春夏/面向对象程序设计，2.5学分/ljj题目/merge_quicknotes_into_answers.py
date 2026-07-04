from pathlib import Path
import re


FILES = [
    "c++练习题目一：基础知识.md",
    "c++练习题目二：类和对象.md",
    "c++练习题目三：派生和继承.md",
]


NOTE_RE = re.compile(
    r"^- \*\*(2-\d+)\*\*：(?:结论：)?(.+?)\s*易错点：(.+)$"
)
ANSWER_RE = re.compile(r"^(- \*\*(2-\d+)\*\*: .+)$")


def split_quicknotes(content: str) -> tuple[str, dict[str, tuple[str, str]]]:
    marker = "\n## 中文速记版\n"
    if marker not in content:
        return content, {}

    before, notes_part = content.split(marker, 1)
    notes: dict[str, tuple[str, str]] = {}
    for line in notes_part.splitlines():
        match = NOTE_RE.match(line.strip())
        if not match:
            continue
        qid, conclusion, warning = match.groups()
        notes[qid] = (conclusion.strip(), warning.strip())
    return before.rstrip() + "\n", notes


def merge_notes(content: str, notes: dict[str, tuple[str, str]]) -> str:
    if not notes:
        return content

    out: list[str] = []
    in_answers = False
    for line in content.splitlines():
        if line == "## Answers":
            in_answers = True
            out.append(line)
            continue

        if in_answers:
            match = ANSWER_RE.match(line)
            if match:
                whole, qid = match.groups()
                if qid in notes:
                    conclusion, warning = notes[qid]
                    line = f"{whole} 中文解释/结论：{conclusion} 易错点：{warning}"
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    for filename in FILES:
        path = Path(filename)
        content = path.read_text(encoding="utf-8")
        without_notes, notes = split_quicknotes(content)
        merged = merge_notes(without_notes, notes)
        path.write_text(merged, encoding="utf-8")
        print(f"{filename}: merged {len(notes)} quick notes")


if __name__ == "__main__":
    main()
