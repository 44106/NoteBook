from pathlib import Path


FILES = [
    "c++练习题目一：基础知识.md",
    "c++练习题目二：类和对象.md",
    "c++练习题目三：派生和继承.md",
]

REPL = {
    "题目说法不严谨，但按题库记结论。": "这里按“纯面向对象语言”的严格定义理解。",
    "题库化表述，注意 abstraction 不是单纯 data hiding。": "这是常见教材表述；注意 abstraction 不是单纯 data hiding。",
    "临时对象和异常会让计数题更复杂，但题库按常规情况处理。": "这里按构造成功且正常生命周期结束的对象计数理解。",
    "题库原句有语法问题，但意思如此。": "原英文表述不自然，核心是引用返回已有对象。",
    "题库把零参数构造函数称为默认构造函数。": "零参数构造函数是默认构造函数的典型形式。",
    "现代编译器可优化，但题库按传统语义考。": "现代编译器可优化，但概念上可理解为按值返回产生结果对象。",
    "题库把 `ClassName functionName(){}` 视为对象返回函数的正确写法。": "`ClassName functionName(){}` 表示函数返回类类型对象。",
    "题库把成员函数调用抽象为 `function(&object, parameter)`。": "成员函数调用可近似理解为隐式传入对象地址：`function(&object, parameter)`。",
    "题库把 `this` 形式记为 `[cv] classType *const this`。": "`this` 可近似理解为指向当前对象的常指针，形式类似 `[cv] classType *const this`。",
    "题库把封装和抽象的区别记为“封装是绑定，抽象是隐藏”。": "封装常强调绑定数据和操作，抽象常强调隐藏实现、暴露接口。",
    "题库认为动态内存类需要用户自定义拷贝构造。": "管理动态内存的类通常需要自定义拷贝构造以实现深拷贝。",
    "题库认为 `if(&object != this)` 是可执行判断式。": "`if (&object != this)` 是可用于避免自赋值的合法判断式。",
    "题库强调 public 成员函数会随继承方式改变其派生类中访问级别。": "public 成员函数在派生类中的访问级别会受继承方式影响。",
    "题库想表达用 const 防止通过指针修改目标值。": "应使用指向 const 的指针来防止通过指针修改目标值。",
    "题库记忆点：`this` 不可被修改。": "`this` 指针本身不可被修改。",
    "题库把 `new T` 视为隐式调用 `::operator new(sizeof(T))`。": "`new T` 的底层分配步骤可理解为调用 `::operator new(sizeof(T))`。",
    "题库说法偏绝对，实际还取决于成员访问权限。": "实际还要结合成员访问权限与继承方式一起判断。",
}


for name in FILES:
    p = Path(name)
    text = p.read_text(encoding="utf-8")
    for old, new in REPL.items():
        text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
