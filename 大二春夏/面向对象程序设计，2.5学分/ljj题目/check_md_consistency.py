from pathlib import Path
import re


FILES = [
    "c++练习题目一：基础知识.md",
    "c++练习题目二：类和对象.md",
    "c++练习题目三：派生和继承.md",
]

question_re = re.compile(r"^\*\*(2-\d+)\*\*\. ")
answer_re = re.compile(r"^- \*\*(2-\d+)\*\*: ")


for filename in FILES:
    path = Path(filename)
    questions = []
    answers = []
    for line in path.read_text(encoding="utf-8").splitlines():
        qm = question_re.match(line)
        if qm:
            questions.append(qm.group(1))
        am = answer_re.match(line)
        if am:
            answers.append(am.group(1))
    qset = set(questions)
    aset = set(answers)
    notes = path.read_text(encoding="utf-8").count("中文解释/结论")
    print(filename)
    print(f"  questions={len(questions)} answers={len(answers)} notes={notes}")
    print(f"  missing_answers={sorted(qset - aset)}")
    print(f"  orphan_answers={sorted(aset - qset)}")
