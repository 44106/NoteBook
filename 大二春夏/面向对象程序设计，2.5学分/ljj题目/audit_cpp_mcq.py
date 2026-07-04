from pathlib import Path
import re


FILES = [
    Path("c++练习题目一：基础知识.md"),
    Path("c++练习题目二：类和对象.md"),
    Path("c++练习题目三：派生和继承.md"),
]


WRONG_FIXES = {
    "c++练习题目一：基础知识.md": {
        "2-1": ("B", "A variable should be created to catch the exception", "C++ 中 `catch` 子句通常用形参变量接收异常对象。", "不是必须显式创建普通对象，`catch(Type e)` 的 `e` 才是接收者。"),
        "2-12": ("A", "Encapsulation and Inheritance", "代码中 `student` 和 `topper` 把数据放入类中，并且 `topper` 继承 `student`。", "只看到 `public student` 容易漏掉类本身体现的封装。"),
        "2-29": ("C", "Real", "对象是类的实际实例，通常表示现实中的具体实体。", "类更偏逻辑抽象，对象更偏具体实体。"),
        "2-33": ("A", "Binding and Hiding respectively", "封装强调把数据和操作绑定在一起，抽象强调隐藏实现。", "题库化表述，注意 abstraction 不是单纯 data hiding。"),
        "2-48": ("A", "using", "`using` 可将命名空间成员引入当前作用域。", "直接限定访问用 `::`，但该题选项里问 keyword，所以选 `using`。"),
    },
    "c++练习题目二：类和对象.md": {
        "2-9": ("A", "Private data members can never be accessed from outside the class", "私有成员函数不能从类外直接访问，只能由类内成员或友元间接访问。", "不能通过普通对象直接调用 private 成员函数。"),
        "2-17": ("A", "Yes, always", "拷贝构造函数可以被声明为 private。", "这常用于禁止对象拷贝。"),
        "2-22": ("A", "Always equal to number of constructors called", "正常对象生命周期中，每个构造成功的对象最终对应一次析构。", "临时对象和异常会让计数题更复杂，但题库按常规情况处理。"),
        "2-23": ("B", "The destructor must be public", "如果对象要在类外正常销毁，析构函数通常必须可访问。", "析构函数可以是 private/protected，但会限制对象销毁方式。"),
        "2-31": ("D", "Public classes can be accessed from any other class using instance", "题库按 public 类/成员可通过实例访问理解。", "这题混入 Java 风格说法，C++ 中重点看成员访问权限。"),
        "2-34": ("C", "Can be initialized either in declaration or by constructor", "数据成员可用类内初始化器或构造函数初始化。", "旧标准限制较多，现代 C++ 支持类内初始化。"),
        "2-40": ("B", "Protected", "protected 成员可被派生类继承并访问，同时对类外保持不可访问。", "private 成员存在于基类子对象中，但派生类不能直接访问。"),
        "2-48": ("D", "All the members", "嵌套类作为成员声明在类作用域中，题库按可访问外围类所有成员处理。", "实际访问非静态成员还需要对象。"),
        "2-56": ("A", "Friend function of derived class can access non-private members of base class", "派生类友元函数可通过派生类访问基类可访问的非 private 成员。", "友元关系本身不会被继承。"),
        "2-65": ("C", "Public member functions", "题库强调 public 成员函数会随继承方式改变其派生类中访问级别。", "private 成员不会被派生类直接访问。"),
        "2-73": ("C", "Must be static member functions", "题库认为使用静态数据成员的典型接口应是静态成员函数。", "实际普通成员函数也能访问 static 数据成员。"),
        "2-74": ("C", "Can be accessed with dot operator", "静态数据成员可通过对象使用点运算符访问。", "更推荐用 `ClassName::member`。"),
        "2-75": ("B", "className :: staticDataMember;", "静态数据成员可通过类名和 `::` 访问。", "注意类外定义还需要写类型。"),
        "2-79": ("B", "Result’s Constructor is Called", "题库代码中静态成员初始化导致 `Result` 构造输出。", "这类题要看静态对象初始化位置。"),
        "2-80": ("D", "className : dataType -> memberName;", "原题选项质量差，按题库答案保留。", "标准成员访问不是这种写法，真正访问静态成员应使用 `ClassName::member`。"),
        "2-81": ("B", "Functions made to maintain single copy of member functions for all objects", "题库认为静态成员函数服务于类级共享行为。", "普通成员函数代码本身也不是每对象复制一份。"),
        "2-84": ("D", "className :: functionName;", "题库答案想表达用类名和 `::` 调用静态成员函数。", "真实调用通常要写 `ClassName::functionName()`。"),
        "2-89": ("D", "Can't be declared const, volatile or const volatile", "`this` 指针本身不能被重新声明成这些形式。", "成员函数的 cv 限定会影响 `this` 指向类型。"),
        "2-90": ("B", "With declaration inside class and not with definition outside the class", "静态数据成员类内声明写 `static`，类外定义通常不再写 `static`。", "类外定义需要类名限定。"),
        "2-94": ("B", "Only in pass by value", "按值传参会创建副本并占用新的存储。", "按引用传参不创建新对象。"),
        "2-103": ("A", "Two objects can point to the same memory location", "多个对象内部指针成员可以指向同一块内存。", "这会带来浅拷贝和重复释放风险。"),
        "2-108": ("A", "Assigned using copy constructor at time of passing", "对象按值传参时用拷贝构造初始化形参。", "不是普通赋值运算符。"),
        "2-115": ("A", "Value of one reference variable to another", "引用参与赋值时，赋的是被引用对象的值。", "引用不能重新绑定。"),
        "2-117": ("D", "We can use direct assignment to same class objects", "同类对象可使用默认或自定义赋值运算符。", "不同类对象默认不可直接赋值。"),
        "2-122": ("A", "Using * symbol", "使用 `*` 解引用指针可取得其指向对象。", "如果问指针变量里保存的地址，直接读取指针变量即可。"),
        "2-123": ("D", "Pointer should be made const", "题库想表达用 const 防止通过指针修改目标值。", "更准确写法是 pointer to const，如 `const int* p`。"),
        "2-127": ("D", "Isn’t part of object itself", "`this` 是成员函数调用时的隐式指针，不占对象自身空间。", "对象大小不包含 `this`。"),
        "2-128": ("C", "Does not include the space taken by this pointer", "`sizeof` 对象不计入 `this` 指针。", "`this` 不是数据成员。"),
        "2-135": ("C", "Allowed assignments to this pointer", "早期一些实现允许给 `this` 赋值。", "现代 C++ 中不能修改 `this`。"),
        "2-143": ("D", "More than one constructors with all default arguments can't exist in same class", "多个全默认参数构造函数会导致无参构造调用歧义。", "默认参数会改变可调用形态。"),
        "2-150": ("C", "Either throws an exception or returns zero", "普通 `new` 失败通常抛异常，`nothrow new` 可返回空指针。", "现代默认不是简单返回 0。"),
        "2-152": ("A", "char (*pchar)[10] = new char[][10];", "题库答案意图是分配每行 10 个 char 的二维动态数组。", "标准写法通常要给第一维大小，如 `new char[n][10]`。"),
        "2-159": ("A", "void", "`delete` 表达式没有可用返回值。", "不要把 `delete` 当成返回指针或整数的表达式。"),
        "2-163": ("D", "Its value is undefined", "释放后继续使用指针属于危险行为。", "严格说指针变量值未必自动改变，但解引用已失效。"),
        "2-167": ("A", "The predefined classes in a language", "题库把内建类理解为语言或库预定义的类。", "C++ 更常说 built-in type，而非 built-in class。"),
        "2-169": ("D", "Objects", "题库认为内建类本身不包含对象。", "这题表述不佳，按题库语境保留。"),
        "2-176": ("C", "24", "题库代码输出 24。", "这类输出题要回到完整代码逐步追踪。"),
        "2-180": ("C", "class student{ }s1,s2; s1=s2;", "同类对象之间可直接赋值。", "不同类对象默认不能直接赋值。"),
    },
    "c++练习题目三：派生和继承.md": {
        "2-2": ("A", "Private", "private 成员最能限制派生类直接访问。", "私有成员仍存在于基类子对象中，只是派生类不可直接访问。"),
        "2-4": ("C", "Default members can't be inherited", "C++ 没有所谓独立的 default 成员不能继承这一规则。", "class 默认 private，但不是“default members”。"),
        "2-8": ("A", "Private", "private 继承最严格，最能隐藏基类接口。", "protected 仍对子类开放。"),
        "2-9": ("A", "The sub class should inherit the parent class privately", "私有继承可阻止成员继续作为 protected/public 向后暴露。", "题库说法偏绝对，实际还取决于成员访问权限。"),
        "2-19": ("D", "Private and Protected", "private/protected 继承都会降低基类 public 成员对外可见性。", "public 继承不会保护 public 接口。"),
        "2-24": ("B", "By making their visibility mode as protected only", "若想让派生类继承并访问，应把 private 改成 protected。", "改成 public 也可访问但破坏封装，题目更应选 protected。"),
        "2-27": ("B", "Hybrid", "菱形继承通常是混合继承结构导致的。", "多继承参与其中，但选项里 hybrid 更贴切。"),
        "2-32": ("B", "Compile time", "单继承关系在编译期确定。", "不要和虚函数运行期多态混淆。"),
        "2-34": ("D", "The derived class must implement all the abstract method if single inheritance is used", "这是抽象类规则，不是单继承的一般规则。", "单继承不要求必须实现抽象方法，除非要实例化具体类。"),
        "2-38": ("A", "Yes, class C and class D", "C 同时继承 A、B，整体又有 D 继承 C。", "选项表述不严谨，重点是 C 处发生多继承。"),
        "2-41": ("B", "Yes, if all the functions are implemented", "多继承下派生类可以是抽象类，也可实现函数后成为具体类。", "原题库答案“没有构造函数”是错误理由。"),
        "2-49": ("D", "~C(), ~B(), ~A()", "多继承析构先派生类，再按基类构造反序析构。", "`class C: public A, public B` 构造 A 后 B，析构 B 后 A。"),
    },
}


DELETE = {
    "c++练习题目一：基础知识.md": {"2-2", "2-20", "2-25", "2-34", "2-37", "2-58", "2-59"},
    "c++练习题目二：类和对象.md": {
        "2-31", "2-38", "2-47", "2-48", "2-73", "2-76", "2-79", "2-80",
        "2-81", "2-84", "2-92", "2-93", "2-107", "2-109", "2-152",
        "2-166", "2-167", "2-169", "2-176",
    },
    "c++练习题目三：派生和继承.md": {"2-33", "2-38", "2-41"},
}


ANSWER_LINE = re.compile(r"^- \*\*(2-\d+)\*\*: ([A-D])\. (.*?)(?: 中文解释/结论：.*)?$")
ANSWER_QID = re.compile(r"^- \*\*(2-\d+)\*\*:")
QUESTION_QID = re.compile(r"^\*\*(2-\d+)\*\*\. ")


def remove_question_blocks(content: str, qids: set[str]) -> str:
    if not qids:
        return content

    lines = content.splitlines()
    out = []
    skipping = False
    for line in lines:
        qmatch = QUESTION_QID.match(line)
        if qmatch:
            skipping = qmatch.group(1) in qids
            if skipping:
                continue
        elif skipping and (line.startswith("### ") or line.startswith("## Answers")):
            skipping = False

        if not skipping:
            out.append(line)
    return "\n".join(out).rstrip() + "\n"


def fix_answer_lines(content: str, filename: str) -> str:
    fixes = WRONG_FIXES.get(filename, {})
    qids_to_delete = DELETE.get(filename, set())
    out = []
    for line in content.splitlines():
        qid_match = ANSWER_QID.match(line)
        if qid_match and qid_match.group(1) in qids_to_delete:
            continue
        match = ANSWER_LINE.match(line)
        if match:
            qid, _letter, _text = match.groups()
            if qid in fixes:
                letter, answer_text, conclusion, warning = fixes[qid]
                line = f"- **{qid}**: {letter}. {answer_text} 中文解释/结论：{conclusion} 易错点：{warning}"
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def remove_empty_answer_sections(content: str) -> str:
    return re.sub(r"\n### [^\n]+\n\n(?=\n### |\Z)", "\n", content)


def main() -> None:
    for path in FILES:
        content = path.read_text(encoding="utf-8")
        content = remove_question_blocks(content, DELETE.get(path.name, set()))
        content = fix_answer_lines(content, path.name)
        content = remove_empty_answer_sections(content)
        path.write_text(content, encoding="utf-8")
        print(f"{path.name}: deleted {len(DELETE.get(path.name, set()))}, fixed {len(WRONG_FIXES.get(path.name, {}))}")


if __name__ == "__main__":
    main()
