import html
import re
from pathlib import Path


PAIRS = [
    ("单选题 - 题目列表 - c++练习题目一：基础知识.html", "c++练习题目一：基础知识.md"),
    ("单选题 - 题目列表 - c++练习题目二：类和对象.html", "c++练习题目二：类和对象.md"),
    ("单选题 - 题目列表 - c++练习题目三：派生和继承.html", "c++练习题目三：派生和继承.md"),
]


question_re = re.compile(r"^\*\*(2-\d+)\*\*\. ")
answer_re = re.compile(r"^- \*\*(2-\d+)\*\*: ")


def strip_tags(text: str) -> str:
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    text = re.sub(r"</p>\s*<p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def code_from_block(block: str) -> str:
    lines = []
    for raw_line in re.findall(r'<div class="cm-line[^"]*">(.*?)</div>', block, flags=re.S):
        line = strip_tags(raw_line)
        lines.append(line)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def clean_fragment(raw: str) -> str:
    def repl(match: re.Match[str]) -> str:
        code = code_from_block(match.group(0))
        return f"\n\n```cpp\n{code}\n```\n\n" if code else ""

    raw = re.sub(r'<div data-code="">.*?</div></div></div></div></div></div>', repl, raw, flags=re.S)
    text = strip_tags(raw)
    text = text.replace("复制内容", "").replace("格式", "").replace("全屏", "").replace("收起", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_html_questions(html_path: Path) -> dict[str, dict]:
    content = html_path.read_text(encoding="utf-8")
    start_pat = re.compile(r'<div class="pc-x pt-2 pl-4 scroll-mt-0" id="(\d+)">')
    matches = list(start_pat.finditer(content))
    parsed = {}
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else content.find('<div class="flex justify-center items-center p-3 bg-bg-base', start)
        block = content[start:end]
        label_match = re.search(r'<div class="pc-text-raw text-xs ellipsis"[^>]*>([^<]+)</div>', block)
        q_match = re.search(
            r'<div class="hyphens-auto flex-1 min-w-0 break-words" lang="en"><div class="rendered-markdown dark:rendered-markdown-invert">(.*?)</div></div><span class="flex flex-wrap -m-0\.5">',
            block,
            flags=re.S,
        )
        if not label_match or not q_match:
            continue
        label = strip_tags(label_match.group(1))
        question = clean_fragment(q_match.group(1))
        options = []
        for opt in re.finditer(
            r'<span>([A-D])\.</span>.*?<div class="rendered-markdown dark:rendered-markdown-invert">(.*?)</div>',
            block,
            flags=re.S,
        ):
            options.append((opt.group(1), clean_fragment(opt.group(2))))
        if len(options) == 4:
            parsed[label] = {"question": question, "options": options}
    return parsed


def kept_qids(md: str) -> list[str]:
    qids = []
    for line in md.splitlines():
        m = question_re.match(line)
        if m:
            qids.append(m.group(1))
    return qids


def extract_answers(md: str) -> str:
    idx = md.index("## Answers")
    return md[idx:].rstrip()


def extract_question_categories(md: str) -> dict[str, str]:
    categories = {}
    current = "Miscellaneous"
    in_questions = False
    for line in md.splitlines():
        if line == "## Questions":
            in_questions = True
            continue
        if line == "## Answers":
            break
        if in_questions and line.startswith("### "):
            current = line[4:]
        m = question_re.match(line)
        if m:
            categories[m.group(1)] = current
    return categories


def render_question(qid: str, item: dict) -> list[str]:
    out = [f"**{qid}**. {item['question']}"]
    for key, value in item["options"]:
        out.append(f"- {key}. {value}")
    out.append("")
    return out


def regenerate(html_file: str, md_file: str) -> None:
    html_questions = parse_html_questions(Path(html_file))
    old_md = Path(md_file).read_text(encoding="utf-8")
    qids = kept_qids(old_md)
    categories = extract_question_categories(old_md)
    answers = extract_answers(old_md)

    title = old_md.splitlines()[0]
    out = [title, "", "## Questions", ""]
    current = None
    for qid in qids:
        cat = categories.get(qid, "Miscellaneous")
        if cat != current:
            current = cat
            out.append(f"### {current}")
            out.append("")
        item = html_questions.get(qid)
        if not item:
            continue
        out.extend(render_question(qid, item))
    out.append(answers)
    Path(md_file).write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for html_file, md_file in PAIRS:
        regenerate(html_file, md_file)
        print(f"regenerated {md_file}")


if __name__ == "__main__":
    main()
