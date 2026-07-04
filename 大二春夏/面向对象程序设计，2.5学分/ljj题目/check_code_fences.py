from pathlib import Path

for name in [
    "c++练习题目一：基础知识.md",
    "c++练习题目二：类和对象.md",
    "c++练习题目三：派生和继承.md",
]:
    text = Path(name).read_text(encoding="utf-8")
    count = text.count("```")
    print(f"{name}: fences={count}, balanced={count % 2 == 0}")
