# C++常用核心中英文词汇对照表

## 基础语法

| English | 中文 | 备注 |
|---|---|---|
| program | 程序 | 完整可运行代码 |
| source code | 源代码 | `.cpp` 文件中的代码 |
| statement | 语句 | 以分号结尾的执行单位 |
| expression | 表达式 | 能产生值的代码片段 |
| declaration | 声明 | 告诉编译器名字和类型 |
| definition | 定义 | 真正分配实体或给出实现 |
| identifier | 标识符 | 变量名、函数名、类名等 |
| keyword | 关键字 | `class`, `int`, `return` 等 |
| variable | 变量 | 可存储数据的命名对象 |
| constant | 常量 | 值不可改变 |
| literal | 字面量 | `10`, `'a'`, `"hello"` |
| data type / type | 数据类型 / 类型 | `int`, `double`, class 类型等 |
| built-in type | 内置类型 | `int`, `char`, `bool` 等 |
| user-defined type | 用户自定义类型 | 类、结构体、枚举等 |
| initialization | 初始化 | 创建对象时给初值 |
| assignment | 赋值 | 对已有对象重新赋值 |
| scope | 作用域 | 名字可见的范围 |
| lifetime | 生命周期 | 对象从创建到销毁的时间 |
| compile time | 编译期 | 编译代码时 |
| run time | 运行期 | 程序运行时 |
| compile-time error | 编译错误 | 编译阶段报错 |
| runtime error | 运行时错误 | 程序运行时出错 |

## 运算符与表达式

| English | 中文 | 备注 |
|---|---|---|
| operator | 运算符 | `+`, `=`, `::`, `->` 等 |
| operand | 操作数 | 运算符作用的对象 |
| arithmetic operator | 算术运算符 | `+ - * / %` |
| relational operator | 关系运算符 | `<`, `>`, `==` 等 |
| logical operator | 逻辑运算符 | `&&`, `||`, `!` |
| assignment operator | 赋值运算符 | `=` |
| compound assignment | 复合赋值 | `+=`, `-=`, `*=` |
| increment operator | 自增运算符 | `++` |
| decrement operator | 自减运算符 | `--` |
| scope resolution operator | 作用域解析运算符 | `::` |
| member access operator | 成员访问运算符 | `.`, `->` |
| conditional operator / ternary operator | 条件运算符 / 三目运算符 | `?:` |
| operator precedence | 运算符优先级 | 决定先算哪个 |
| associativity | 结合性 | 同优先级时从左或从右结合 |
| type conversion | 类型转换 | 隐式或显式转换 |
| implicit conversion | 隐式转换 | 编译器自动转换 |
| explicit conversion / cast | 显式转换 / 强制类型转换 | `static_cast<int>(x)` |

## 函数

| English | 中文 | 备注 |
|---|---|---|
| function | 函数 | 可调用的代码块 |
| function declaration | 函数声明 | 说明函数接口 |
| function definition | 函数定义 | 给出函数体 |
| function call | 函数调用 | 执行函数 |
| parameter | 形参 | 函数定义里的参数 |
| argument | 实参 | 调用函数时传入的值 |
| return value | 返回值 | 函数返回的结果 |
| return type | 返回类型 | 函数返回值类型 |
| void | 空类型 | 常用于无返回值函数 |
| pass by value | 值传递 | 复制实参 |
| pass by reference | 引用传递 | 传入原对象别名 |
| pass by pointer | 指针传递 | 传入地址 |
| function overloading | 函数重载 | 同名函数，不同参数列表 |
| signature | 函数签名 | 通常指函数名和参数列表 |
| inline function | 内联函数 | 建议编译器展开调用 |
| recursive function | 递归函数 | 函数调用自身 |
| default argument | 默认参数 | 调用时可省略的参数 |
| const function / const member function | 常成员函数 | 不修改对象状态的成员函数 |

## 类与对象

| English | 中文 | 备注 |
|---|---|---|
| object-oriented programming / OOP | 面向对象编程 | C++ 核心思想之一 |
| class | 类 | 对象的蓝图 |
| object | 对象 | 类的实例 |
| instance | 实例 | 通常等同于对象 |
| member | 成员 | 类中的数据或函数 |
| data member | 数据成员 | 类中的变量 |
| member function | 成员函数 | 类中的函数 |
| method | 方法 | 常指成员函数 |
| access specifier | 访问说明符 | `public`, `private`, `protected` |
| public | 公有的 | 类外可访问 |
| private | 私有的 | 只能类内或友元访问 |
| protected | 受保护的 | 类内、友元、派生类可访问 |
| encapsulation | 封装 | 数据和操作绑定，并控制访问 |
| abstraction | 抽象 | 隐藏实现，只暴露接口 |
| data hiding | 数据隐藏 | 隐藏内部数据 |
| interface | 接口 | 对外暴露的使用方式 |
| implementation | 实现 | 内部具体代码 |
| blueprint | 蓝图 | 类常被称为对象蓝图 |
| this pointer | `this` 指针 | 指向当前对象 |
| static data member | 静态数据成员 | 类共享一份数据 |
| static member function | 静态成员函数 | 无 `this` 指针 |
| friend function | 友元函数 | 可访问类的非公有成员 |
| nested class | 嵌套类 | 类中定义的类 |

## 构造、析构与对象语义

| English | 中文 | 备注 |
|---|---|---|
| constructor | 构造函数 | 对象创建时调用 |
| default constructor | 默认构造函数 | 可无实参调用 |
| parameterized constructor | 带参构造函数 | 带参数初始化对象 |
| copy constructor | 拷贝构造函数 | 用同类对象初始化新对象 |
| move constructor | 移动构造函数 | 转移资源所有权 |
| destructor | 析构函数 | 对象销毁时调用 |
| constructor overloading | 构造函数重载 | 多个不同参数构造函数 |
| initialization list | 初始化列表 | 构造函数冒号后的初始化部分 |
| object lifetime | 对象生命周期 | 创建到销毁 |
| temporary object | 临时对象 | 表达式中短暂存在的对象 |
| shallow copy | 浅拷贝 | 只复制指针等表面值 |
| deep copy | 深拷贝 | 复制资源本身 |
| copy assignment operator | 拷贝赋值运算符 | `operator=` |
| self-assignment | 自赋值 | `a = a` |
| resource management | 资源管理 | 内存、文件句柄等管理 |
| RAII | 资源获取即初始化 | 构造获取资源，析构释放资源 |

## 继承与多态

| English | 中文 | 备注 |
|---|---|---|
| inheritance | 继承 | 子类复用父类 |
| base class | 基类 / 父类 | 被继承的类 |
| derived class | 派生类 / 子类 | 继承得到的类 |
| superclass | 超类 / 父类 | 常见英文题用词 |
| subclass | 子类 | 常见英文题用词 |
| single inheritance | 单继承 | 一个直接基类 |
| multiple inheritance | 多继承 | 多个直接基类 |
| multilevel inheritance | 多级继承 | A -> B -> C |
| hierarchical inheritance | 层次继承 | 一个基类派生多个子类 |
| hybrid inheritance | 混合继承 | 多种继承组合 |
| access mode | 继承访问方式 | `public`, `private`, `protected` 继承 |
| public inheritance | 公有继承 | 常表示 is-a 关系 |
| private inheritance | 私有继承 | 对外隐藏基类接口 |
| protected inheritance | 保护继承 | 基类 public/protected 在子类中变 protected |
| polymorphism | 多态 | 同一接口不同表现 |
| compile-time polymorphism | 编译期多态 | 重载、模板 |
| runtime polymorphism | 运行期多态 | 虚函数 |
| virtual function | 虚函数 | 支持动态绑定 |
| pure virtual function | 纯虚函数 | `= 0` |
| abstract class | 抽象类 | 含纯虚函数，通常不能实例化 |
| overriding | 重写 / 覆盖 | 派生类重新实现虚函数 |
| dynamic binding / late binding | 动态绑定 / 后期绑定 | 运行时决定调用版本 |
| static binding / early binding | 静态绑定 / 前期绑定 | 编译期决定调用版本 |
| virtual destructor | 虚析构函数 | 多态删除对象时常需要 |
| diamond problem | 菱形继承问题 | 多继承中基类重复 |
| virtual inheritance | 虚继承 | 解决共享基类重复问题 |

## 指针、引用与内存

| English | 中文 | 备注 |
|---|---|---|
| pointer | 指针 | 保存地址 |
| reference | 引用 | 对象别名 |
| address | 地址 | 内存位置 |
| dereference | 解引用 | `*p` |
| null pointer | 空指针 | `nullptr` |
| dangling pointer | 悬空指针 | 指向已失效对象 |
| memory allocation | 内存分配 | 申请内存 |
| deallocation | 内存释放 | 归还内存 |
| dynamic allocation | 动态分配 | 运行时申请内存 |
| stack | 栈 | 自动存储区 |
| heap / free store | 堆 / 自由存储区 | 动态内存区域 |
| new operator | `new` 运算符 | 分配并构造对象 |
| delete operator | `delete` 运算符 | 析构并释放对象 |
| memory leak | 内存泄漏 | 申请后未释放 |
| array | 数组 | 连续同类型元素 |
| dynamic array | 动态数组 | `new[]` 或容器实现 |
| smart pointer | 智能指针 | 自动管理资源 |
| unique_ptr | 独占智能指针 | 独占所有权 |
| shared_ptr | 共享智能指针 | 引用计数共享所有权 |
| weak_ptr | 弱引用智能指针 | 不增加引用计数 |

## 命名空间与作用域

| English | 中文 | 备注 |
|---|---|---|
| namespace | 命名空间 | 组织名字，避免冲突 |
| using declaration | using 声明 | `using std::cout;` |
| using directive | using 指示 | `using namespace std;` |
| global scope | 全局作用域 | 文件最外层作用域 |
| local scope | 局部作用域 | 函数或代码块内部 |
| block scope | 块作用域 | `{}` 内 |
| class scope | 类作用域 | 类内部 |
| name lookup | 名字查找 | 编译器寻找名字含义 |
| name conflict / name clash | 名字冲突 | 同名导致歧义 |
| qualified name | 限定名 | `std::cout` |
| unqualified name | 非限定名 | `cout` |
| anonymous namespace | 匿名命名空间 | 当前翻译单元内可见 |
| nested namespace | 嵌套命名空间 | 命名空间中再定义命名空间 |

## 模板与泛型

| English | 中文 | 备注 |
|---|---|---|
| template | 模板 | 泛型编程工具 |
| function template | 函数模板 | 生成函数 |
| class template | 类模板 | 生成类 |
| type parameter | 类型参数 | `typename T` |
| template argument | 模板实参 | 实际传入模板的类型或值 |
| instantiation | 实例化 | 根据模板生成具体代码 |
| specialization | 特化 | 为特定类型提供特殊实现 |
| partial specialization | 偏特化 | 类模板部分特化 |
| generic programming | 泛型编程 | 面向类型参数写通用代码 |
| typename | 类型名关键字 | 模板中常用 |

## 异常处理

| English | 中文 | 备注 |
|---|---|---|
| exception | 异常 | 程序中的异常情况 |
| exception handling | 异常处理 | 处理异常机制 |
| try block | `try` 块 | 包围可能抛异常的代码 |
| catch block | `catch` 块 | 捕获异常 |
| throw | 抛出异常 | `throw expr;` |
| rethrow | 重新抛出 | `throw;` |
| handler | 处理器 | 匹配异常的 `catch` |
| stack unwinding | 栈展开 | 异常传播时销毁局部对象 |
| standard exception | 标准异常 | `std::exception` 等 |
| noexcept | 不抛异常说明 | 表示函数不应抛出异常 |

## STL 与常用库

| English | 中文 | 备注 |
|---|---|---|
| Standard Template Library / STL | 标准模板库 | 容器、算法、迭代器 |
| container | 容器 | 存储元素的数据结构 |
| sequence container | 顺序容器 | `vector`, `list`, `deque` |
| associative container | 关联容器 | `map`, `set` |
| unordered container | 无序容器 | `unordered_map`, `unordered_set` |
| vector | 动态数组容器 | `std::vector` |
| list | 双向链表容器 | `std::list` |
| deque | 双端队列 | `std::deque` |
| map | 映射 | 键值对，按键排序 |
| set | 集合 | 唯一键集合 |
| queue | 队列 | 先进先出 |
| stack | 栈容器适配器 | 后进先出 |
| priority queue | 优先队列 | 按优先级取元素 |
| iterator | 迭代器 | 类似指针，用于遍历容器 |
| algorithm | 算法 | `sort`, `find`, `count` 等 |
| string | 字符串 | `std::string` |
| stream | 流 | 输入输出抽象 |
| input stream | 输入流 | `cin`, `ifstream` |
| output stream | 输出流 | `cout`, `ofstream` |
| header file | 头文件 | `#include` 引入 |

## 编译与文件组织

| English | 中文 | 备注 |
|---|---|---|
| preprocessor | 预处理器 | 处理 `#include`, `#define` |
| include directive | 包含指令 | `#include` |
| macro | 宏 | `#define` 定义 |
| header guard | 头文件保护 | 防止重复包含 |
| translation unit | 翻译单元 | 一个源文件加包含内容 |
| compiler | 编译器 | 把源码编译成目标文件 |
| linker | 链接器 | 合并目标文件和库 |
| object file | 目标文件 | 编译后未最终链接的文件 |
| executable | 可执行文件 | 最终可运行程序 |
| library | 库 | 可复用代码集合 |
| static library | 静态库 | 链接进可执行文件 |
| dynamic library / shared library | 动态库 / 共享库 | 运行时加载 |

## 英文选择题常见动词

| English | 中文 | 做题提示 |
|---|---|---|
| define | 定义 | 给出实体或实现 |
| declare | 声明 | 告诉编译器存在 |
| initialize | 初始化 | 创建时赋初值 |
| assign | 赋值 | 已存在对象重新赋值 |
| access | 访问 | 读写变量或调用成员 |
| invoke / call | 调用 | 调用函数 |
| inherit | 继承 | 从基类获得成员 |
| override | 重写 | 派生类改写虚函数 |
| overload | 重载 | 同名不同参数 |
| allocate | 分配 | 申请内存 |
| deallocate | 释放 | 归还内存 |
| destroy | 销毁 | 调用析构、结束生命周期 |
| construct | 构造 | 调用构造函数 |
| instantiate | 实例化 | 创建对象或模板生成实体 |
| encapsulate | 封装 | 绑定数据与操作 |
| hide | 隐藏 | 不暴露实现或数据 |
| expose | 暴露 | 对外提供接口 |
| resolve | 解析 | 确定名字或调用目标 |
| bind | 绑定 | 将调用与实现关联 |

## 易混词速记

| 易混词 | 区别 |
|---|---|
| declaration vs definition | 声明只说明“有什么”，定义真正创建或实现。 |
| initialization vs assignment | 初始化发生在对象创建时，赋值发生在对象已存在后。 |
| parameter vs argument | 形参在函数定义中，实参在函数调用中。 |
| class vs object | 类是蓝图，对象是实例。 |
| private vs protected | `private` 派生类不能直接访问，`protected` 派生类可以访问。 |
| overloading vs overriding | 重载是同名不同参数，重写是派生类改写虚函数。 |
| static member function vs normal member function | 静态成员函数没有 `this` 指针，普通成员函数有。 |
| pointer vs reference | 指针保存地址，可为空；引用是别名，通常必须初始化。 |
| shallow copy vs deep copy | 浅拷贝复制指针值，深拷贝复制资源本身。 |
| compile-time polymorphism vs runtime polymorphism | 编译期多态靠重载/模板，运行期多态靠虚函数。 |
| namespace vs class | 命名空间组织名字，没有访问权限控制；类组织对象数据和行为，有访问控制。 |
