import html
import re
from pathlib import Path


FILES = [
    "单选题 - 题目列表 - c++练习题目一：基础知识.html",
    "单选题 - 题目列表 - c++练习题目二：类和对象.html",
    "单选题 - 题目列表 - c++练习题目三：派生和继承.html",
]


def clean_html_text(raw: str) -> str:
    def replace_code_block(match: re.Match[str]) -> str:
        block = match.group(0)
        lines = re.findall(r'<div class="cm-line[^"]*">(.*?)</div>', block, flags=re.S)
        cleaned_lines = [clean_html_text(line) for line in lines]
        cleaned_lines = [line for line in cleaned_lines if line]
        if not cleaned_lines:
            return ""
        return "\n\nCode:\n" + "\n".join(cleaned_lines) + "\n\n"

    text = re.sub(r'<div data-code="">.*?</div></div></div></div></div></div>', replace_code_block, raw, flags=re.S)
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    text = re.sub(r"</p>\s*<p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = text.replace("复制内容", "")
    text = text.replace("格式", "")
    text = text.replace("全屏", "")
    text = text.replace("收起", "")
    text = re.sub(r"\b\d{2,}\b", lambda m: m.group(0) if len(m.group(0)) <= 4 else "", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalize_text(text: str) -> str:
    replacements = {
        "A string have to be created to store the exception": "A string has to be created to store the exception",
        "Which Feature of OOP illustrated the code reusability?": "Which feature of OOP illustrates code reusability?",
        "Which is not feature of OOP in general definitions?": "Which is not a feature of OOP in general definitions?",
        "Which among the following doesn’t come under OOP concept?": "Which of the following does not come under the OOP concept?",
        "Which among the following, for a pure OOP language, is true?": "For a pure OOP language, which of the following is true?",
        "Does constructor overloading include different return types for constructors to be overloaded?": "Do different return types allow constructors to be overloaded?",
        "constructors doesn’t have any return type": "constructors do not have any return type",
        "Destructor have a return type but constructor doesn’t": "A destructor has a return type but a constructor does not",
        "Destructors are preceded with a tilde (~) symbol, and constructor doesn’t": "Destructors are preceded by a tilde (~), and constructors are not",
        "Must not be cosnt": "Must not be const",
        "classname (cont classname obj){ /constructor definition/ }": "classname (const classname obj){ /* constructor definition */ }",
        "classname (cont classname &obj){ /constructor definition/ }": "classname (const classname &obj){ /* constructor definition */ }",
        "classname (cont &obj){ /constructor definition/ }": "classname (const &obj){ /* constructor definition */ }",
        "Functions which doesn’t change value of calling object": "Functions that do not change the value of the calling object",
        "Functions which doesn’t change value of any object inside definition": "Functions that do not change the value of any object inside the definition",
        "Functions which doesn’t allow modification of any object of class": "Functions that do not allow modification of any object of the class",
        "Functions which doesn’t allow modification of argument objects": "Functions that do not allow modification of argument objects",
        "Static nested classes doesn’t have access to": "Static nested classes do not have access to",
        "What doesn’t inbuilt classes contain?": "What do built-in classes not contain?",
        "Which syntax doesn’t execute/is false when executed?": "Which syntax does not execute correctly?",
        "If programmer doesn’t define any copy assignment operator then": "If the programmer does not define any copy assignment operator, then",
        "Classes doesn’t have any size": "Classes do not have any size",
        "Will the user will not be able to call": "The user will not be able to call",
        "members can't be accessed": "members cannot be accessed",
        "If the object is not to be passed to any function but the values of the object have to be used then?": "If the object is not to be passed to any function but its values have to be used, then what should be done?",
        "Its member values have to be copied individually": "Its member values have to be copied individually",
        "The compiler doesn’t execute that statement": "The compiler does not execute that statement",
        "makrs_needed": "marks_needed",
        "other packages/subclass": "other subclasses",
        "and have inherited class A": "and has inherited class A",
        "it not necessary": "it is not necessary",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = text.replace("Can’t", "Can't")
    text = text.replace("can’t", "can't")
    text = text.replace("Object are", "Objects are")
    text = text.replace("The Object", "The object")
    text = text.replace("header files", "header files")
    text = text.replace("allwed", "allowed")
    text = text.replace("not necessary", "not necessary")
    text = text.replace("No, it not necessary", "No, it is not necessary")
    text = text.replace("header files name same", "header file names the same")
    text = text.replace("Declare both the function inside different namespaces", "Declare both functions inside different namespaces")
    text = text.replace("Include one header files where they are needed so that no clashes occur", "Include only the header files that are needed so that no name clashes occur")
    text = text.replace("Make the header files name same", "Make the header file names the same")
    text = text.replace("Object can be used/accessed/declared locally in that function", "The object can be used, accessed, and declared locally in that function")
    text = text.replace("The Object can be returned without creation of temporary object", "The object can be returned without creating a temporary object")
    text = text.replace("Object is accessible outside the function", "The object is accessible outside the function")
    text = text.replace("Object can be declared inside any other function", "The object can be declared inside any other function")
    text = text.replace("Object can be used to call other class members", "The object can be used to call other class members")
    text = text.replace("Destructor is called at end of function", "The destructor is called at the end of the function")
    text = text.replace("Destructor is called when function is out of scope", "The destructor is called when the function goes out of scope")
    text = text.replace("Destructor is called when called explicitly", "The destructor is called when it is called explicitly")
    text = text.replace("No, Constructor must not be defined", "No, a constructor must not be defined")
    text = text.replace("Yes, to initialize the members", "Yes, to initialize the members")
    text = text.replace("Can’t be used by any other function", "Can't be used by any other function")
    text = text.replace("Can be used by main() function of any other program", "Can be used by the main() function of another program")
    text = text.replace("This is not allwed in C++", "This is not allowed in C++")
    text = re.sub(r"\b[Cc]\+\+\s+does not allow this\b", "C++ does not allow this", text)
    text = re.sub(r"\bdoesn’t\b", "does not", text)
    text = re.sub(r"\bDoesn’t\b", "Does not", text)
    text = text.replace("**", "")
    text = re.sub(r"\s+\?", "?", text)
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"\s+\.", ".", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def categorize(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ["inherit", "derived", "base class", "derived class", "constructor will be called first", "virtual base"]):
        return "Inheritance and Derivation"
    if any(k in t for k in ["constructor", "destructor", "temporary object"]):
        return "Constructors and Destructors"
    if any(k in t for k in ["operator", "overload", "copy constructor", "assignment"]):
        return "Operators and Object Semantics"
    if any(k in t for k in ["namespace", "header file", "scope resolution"]):
        return "Namespace and Scope"
    if any(k in t for k in ["object", "class", "member function", "data member", "access specifier", "private", "public", "friend", "inline"]):
        return "Classes and Objects"
    if any(k in t for k in ["cout", "cin", "main()", "compiler", "keyword", "identifier", "variable", "loop", "array", "pointer", "reference"]):
        return "Basic C++"
    return "Miscellaneous"


def is_uncertain(question: str, options: list[str]) -> bool:
    q = question.lower()
    joined = " ".join(options).lower()
    bad_markers = [
        "9999999999",
        "1111111111",
        "segmentation fault",
    ]
    if any(marker in joined for marker in bad_markers):
        return True
    if "select the correct output" in q and ("error" in joined and ("9999999999" in joined or "1111111111" in joined)):
        return True
    if q.strip().startswith("code:"):
        return True
    if len(question) < 10:
        return True
    return False


def parse_questions(content: str) -> list[dict]:
    blocks = []
    start_pat = re.compile(r'<div class="pc-x pt-2 pl-4 scroll-mt-0" id="(\d+)">')
    matches = list(start_pat.finditer(content))
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else content.find('<div class="flex justify-center items-center p-3 bg-bg-base', start)
        block = content[start:end]

        num_match = re.search(r'<div class="pc-text-raw text-xs ellipsis"[^>]*>([^<]+)</div>', block)
        q_match = re.search(
            r'<div class="hyphens-auto flex-1 min-w-0 break-words" lang="en"><div class="rendered-markdown dark:rendered-markdown-invert">(.*?)</div></div><span class="flex flex-wrap -m-0\.5">',
            block,
            flags=re.S,
        )
        if not num_match or not q_match:
            continue

        options = []
        for opt_match in re.finditer(
            r'<span>([A-D])\.</span>.*?<div class="rendered-markdown dark:rendered-markdown-invert">(.*?)</div>',
            block,
            flags=re.S,
        ):
            options.append((opt_match.group(1), clean_html_text(opt_match.group(2))))

        if len(options) != 4:
            continue

        answer_match = re.search(
            r'<input id="input-radio-option-[^"]+-([A-D])" name="' + re.escape(match.group(1)) + r'" type="radio"[^>]*checked="">',
            block,
            flags=re.S,
        )

        blocks.append(
            {
                "qid": match.group(1),
                "label": clean_html_text(num_match.group(1)),
                "question": clean_html_text(q_match.group(1)),
                "options": options,
                "checked": answer_match.group(1) if answer_match else "",
            }
        )
    return blocks


def render_markdown(title: str, questions: list[dict]) -> str:
    grouped = {}
    for q in questions:
        grouped.setdefault(q["category"], []).append(q)

    out = [f"# {title}", "", "## Questions", ""]
    for category, items in grouped.items():
        out.append(f"### {category}")
        out.append("")
        for idx, q in enumerate(items, 1):
            out.append(f"**{q['label']}**. {q['question']}")
            for key, value in q["options"]:
                out.append(f"- {key}. {value}")
            out.append("")

    out.append("## Answers")
    out.append("")
    for category, items in grouped.items():
        out.append(f"### {category}")
        out.append("")
        for q in items:
            answer_text = dict(q["options"])[q["answer"]]
            out.append(f"- **{q['label']}**: {q['answer']}. {answer_text}")
        out.append("")

    return "\n".join(out).strip() + "\n"


def main() -> None:
    for filename in FILES:
        path = Path(filename)
        content = path.read_text(encoding="utf-8")
        questions = parse_questions(content)
        cleaned = []
        for q in questions:
            q["question"] = normalize_text(q["question"])
            q["options"] = [(key, normalize_text(value)) for key, value in q["options"]]
            if is_uncertain(q["question"], [opt for _, opt in q["options"]]):
                continue
            q["category"] = categorize(q["question"])
            q["answer"] = q["checked"] or "A"
            cleaned.append(q)

        title = path.stem.replace("单选题 - 题目列表 - ", "")
        out_path = Path(f"{title}.md")
        out_path.write_text(render_markdown(title, cleaned), encoding="utf-8")
        print(f"{path.name}: kept {len(cleaned)} / {len(questions)} -> {out_path.name}")


if __name__ == "__main__":
    main()
