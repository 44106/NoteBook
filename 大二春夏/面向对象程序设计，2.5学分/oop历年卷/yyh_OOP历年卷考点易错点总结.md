# OOP 历年卷考点与易错点总结

资料范围：当前文件夹内 `2005-2006.pdf`、`2007-2008.pdf`、`2008-2009.pdf`、`2016-2017.pdf`、`2018-2019.pdf`、`2018-2019-有答案.pdf`、`2019-2020.pdf`、`2023-2024.pdf`、`23-24_wk_midterm.pdf`。其中早年卷多为扫描版，本总结按可读题面和重复题型归纳，重点面向 C++ 语法题、输出题、程序填空题和函数题。

## 老师划重点版

老师明确给出的知识点：`class`、`inheritance`、`casting`、`polymorphism`、`pass by reference`、`static member variable`、`template`、`exception`、`virtual`、`operator overloading`、`constructor and destructor`。题型包括程序输出题、选择题、填空题、函数/类设计题；模板类必须复习。

| 题型 | 可能考法 | 必会知识点 | 易错点 | 复习动作 |
|---|---|---|---|---|
| 程序输出题 | 给一段类/继承/重载代码，写每一行输出 | 构造析构、虚函数、函数隐藏、引用返回、异常流 | 忘记临时对象和局部对象析构；把拷贝构造看成赋值；忽略 `endl` | 按“构造 -> 调用 -> 析构”逐行模拟 |
| 选择题 | 判断概念、选正确/错误说法 | class 默认 private、struct 默认 public、virtual、static、operator、new/delete | 概念题容易被绝对化表述骗，如 “all members”“always”“only” | 背专题速查表，遇到绝对词重点审 |
| 填空题 | 补函数声明、返回类型、模板参数、类成员 | 引用、const、模板、友元、运算符重载 | 返回类型漏 `&`；模板类名漏 `<T>`；成员函数类外定义漏作用域 | 先看调用点，再反推签名 |
| 函数/类设计题 | 按 judge 代码补 `class` 或模板类 | 接口匹配、构造函数、运算符、虚函数、多态删除 | 自己改 judge；函数名/参数 const 不匹配；输出格式多空格/少空格 | 从 `main` 和测试函数逐行列“需要哪些接口” |

| 老师点名知识点 | 重点掌握 | 常见考题信号 | 一句话规则 |
|---|---|---|---|
| `class` | 访问控制、封装、friend、const 成员函数 | `private` 成员能否访问、同类对象互访 | 类成员函数可以访问同类任意对象的 private |
| `inheritance` | public 继承、多继承、对象切片、构造析构顺序 | `class B : public A`、`A a = b` | 派生对象构造先基类后派生，析构反过来 |
| `casting` | `static_cast`、`dynamic_cast`、转换构造、类型转换函数 | 基类指针转派生、`operator B()`、`static_cast<double>` | `dynamic_cast` 用于多态类型，失败指针返回 `nullptr` |
| `polymorphism` | 基类指针/引用调用虚函数 | `Base *p = new Derived; p->f();` | virtual 调用看动态类型，非 virtual 看静态类型 |
| `pass by reference` | 引用传参、引用返回、避免拷贝 | `int& f(int&)`、`A& operator=` | 引用是别名，修改引用就是修改原对象 |
| `static member variable` | 类内声明、类外定义、对象共享 | `static int m; int A::m;` | static 数据成员不属于某个对象，所有对象共享 |
| `template` | 函数模板、类模板、特化、模板类 | `template<class T>`、`Array<T>`、`CQueue<T>` | 模板类类外定义必须写 `template<class T>` 和 `Class<T>::` |
| `exception` | `throw`、`catch`、重抛、catch 顺序 | `catch(...)`、`throw;` | 抛出后跳到匹配 catch，try 后续语句不执行 |
| `virtual` | 虚函数、纯虚函数、虚析构 | `virtual void f()`、`=0`、`delete Base*` | 多态基类析构函数应为 virtual |
| `operator overloading` | `[]`、`++`、`=`, `<<`, 类型转换 | `operator[]`、`operator++(int)` | `[]`、`()`, `->`, `=` 必须是成员函数 |
| `constructor and destructor` | 默认构造、拷贝构造、析构顺序 | `A a; A b=a; delete p;` | 析构函数不能重载，构造函数不能 virtual |

## 高频考点总表

| 模块 | 常见题型 | 核心规则 | 易错点 | 典型判断方法 |
|---|---|---|---|---|
| 构造函数 | 默认构造、带参构造、拷贝构造、`explicit` | 只要用户声明了任意构造函数，编译器不再自动生成默认构造函数；`explicit` 禁止拷贝初始化 | `C c = 7;` 不能调用 `explicit C(int)`，可能转而调用 `C(double)` | 区分 `C c(7)` 直接初始化和 `C c = 7` 拷贝初始化 |
| 拷贝构造 | `A a2 = b;`、函数传参、返回对象 | 拷贝构造一般写 `A(const A&)` | 写成 `A(A&)` 不能绑定 `const` 对象和临时对象 | 看到同类对象初始化新对象，就考虑拷贝构造 |
| 赋值运算符 | `a2 = a1;` | 赋值发生在两个已经存在的对象之间，通常返回 `A&` | 把 `A a = b;` 误判成赋值；实际上是拷贝构造 | “是否已经构造完成”是判断构造/赋值的关键 |
| 析构函数 | 输出顺序、`delete basePtr` | 析构顺序与构造相反；派生类析构先执行，再执行基类析构 | 基类析构非 `virtual` 时用基类指针删除派生对象可能未定义行为 | 先列对象生命周期，再按作用域退出和 `delete` 顺序写输出 |
| 派生类构造 | 初始化基类子对象 | 派生类应在初始化列表中显式调用基类构造函数，如 `B(int x): A(x) {}`；若不写，编译器尝试调用 `A()` | 不能在派生类初始化列表里直接初始化基类成员；基类无默认构造时不写 `A(args)` 会报错 | 构造顺序永远是：基类 -> 派生类成员 -> 派生类构造函数体 |
| 派生类拷贝构造 | 拷贝基类子对象和成员对象 | 自定义 `B(const B& b)` 时，应在初始化列表写 `: A(b), a(b.a), i(b.i)` | 如果不写，基类子对象和成员对象会默认构造，不会自动拷贝构造 | 函数体执行前，所有基类和成员已经构造完 |
| 编译器生成的派生类拷贝构造 | 没有自定义 `B(const B&)` 时 | 编译器生成的拷贝构造会自动拷贝构造基类子对象和成员对象 | 和“自定义但没写初始化列表”不同 | 不写时编译器帮你拷贝；写了就要自己负责 |
| 成员初始化列表 | `A(): y(x), x(1)` | 成员初始化顺序按成员声明顺序，不按初始化列表顺序 | 以为初始化列表书写顺序决定初始化顺序 | 看类中成员声明的先后 |
| 继承 | public/protected/private 继承、访问控制 | public 继承保持 public/protected；private 成员继承但派生类不能直接访问 | “继承了”不等于“能直接访问” | 先判断继承方式，再判断成员原访问级别 |
| 多继承 | 菱形继承、二义性 | 非虚继承下，多个基类子对象会导致成员访问二义性 | 只看函数体里是否显式 `B::fun()`，忽略数据成员是否二义 | 有多个路径继承同一基类时，重点检查 `d.x`、隐式转换 |
| 虚继承 | `class B : virtual public A` | 虚继承让公共基类子对象只保留一份；虚基类由最派生类负责构造 | 以为每条继承路径都有一份虚基类，或以为初始化列表能改变虚基类构造顺序 | 虚基类先构造，顺序看最派生类的继承层次声明顺序 |
| 虚函数 | 基类指针/引用调用派生实现 | 虚函数一旦在基类声明为 `virtual`，派生类同签名覆盖后仍是虚函数 | 构造函数不能是虚函数；析构函数可以且常应为虚函数 | 看调用表达式的静态类型和函数是否 virtual |
| 函数隐藏 | 派生类定义同名函数 | 派生类中的同名函数会隐藏基类所有同名重载 | `B::F(double)` 会隐藏 `A::F(int)`，`b.F(2)` 可能调用 `B::F(double)` | 名字查找先于重载决议；要引入基类重载需 `using A::F;` |
| 函数重载 | 参数类型、`const`、引用 | 只看函数名和参数列表；返回值不能作为重载依据 | 误以为返回类型不同能重载 | 列候选函数，排除不可行，再比较匹配优先级 |
| `const` 成员函数 | `void f() const`、`const A a` | `const` 对象只能调用 `const` 成员函数和静态成员函数 | 静态成员函数没有 `this`，可通过 const 对象调用 | 把成员函数隐含参数写成 `A* this` 或 `const A* this` |
| 静态成员 | `static int m;`、`static void f()` | 静态数据成员属于类，需要类外定义；静态函数无 `this` | 以为每个对象都有一份 static 数据成员 | 静态数据成员由所有对象共享 |
| 运算符重载 | `[]`、`()`, `->`, `<<`, `=`, `++` | `[]`、`()`, `->`, `=` 必须重载为成员函数；`::`、`.`、`.*`、`?:`、`sizeof` 不能重载 | 把 `operator[]` 写成普通友元函数 | 记住“必须成员”和“不可重载”两类清单 |
| 类型转换 | 转换构造、`operator T()` | 单参数构造可做隐式转换；转换函数可把对象转成目标类型 | `*s` 中对象可能先转成指针再解引用 | 先看是否有转换构造或类型转换运算符 |
| 异常 | `try/catch`、重抛、catch 顺序 | `catch` 参数像函数参数；`throw;` 重抛当前异常 | `catch(...)` 应放最后；重抛后不会继续执行 try 后普通语句 | 沿控制流跳到第一个匹配的 catch |
| 模板 | 函数模板、类模板、显式特化 | 模板参数推导要求同一个 `T` 一致；显式特化不是普通重载 | `max(x,y,z)` 中 `x/y/z` 类型不一致会推导失败 | 对每个模板参数列出由实参推导出的类型 |
| STL vector | `push_back`、`size`、`operator[]` | `v[i]` 不检查边界；空 vector 的 `v[0]` 是越界未定义行为 | 误判为编译错误；实际通常是运行时/未定义行为 | `operator[]` 只要求类型可编译，不保证元素存在 |
| `new/delete` | 动态对象、数组、构造析构 | `new` 调构造，返回目标类型指针；`malloc` 不调构造，返回 `void*` | `new[]` 必须配 `delete[]`；不能用 `delete` 释放栈对象 | 看对象是单个还是数组、是否来自 `new` |
| 输入输出 | `<<`、指针、`char*` | `cout << char*` 按 C 字符串输出；其他指针通常输出地址 | `cout << *charPtr` 输出单个字符，不是字符串 | 区分指针值、解引用值、字符串指针特例 |

## 函数调用优先级与重载决议

| 场景 | 优先级/规则 | 易错例子 | 正确理解 |
|---|---|---|---|
| 普通重载 | 精确匹配优先于提升，提升优先于标准转换，标准转换优先于用户自定义转换 | `f(3)` 在 `f(int)` 和 `f(double)` 中选 `f(int)` | 先列可行函数，再比较转换代价 |
| `const` 对象调用成员函数 | `const` 对象不能调用非 `const` 成员函数 | `const A a; a.f(3);` 中 `void f(int)` 不可用 | 如果还有 `static void f(double)`，静态函数可用 |
| 派生类同名函数 | 派生类同名函数隐藏基类所有同名函数 | `B` 定义 `F(double)` 后，`A::F(int)` 被隐藏 | 除非 `B` 中写 `using A::F;` |
| 虚函数调用 | 通过基类指针/引用调用 virtual 函数时按动态类型 | `A* p = new B; p->f();` 调 `B::f()` | 非 virtual 函数按静态类型绑定 |
| 默认参数和虚函数 | 默认参数看静态类型，虚函数体看动态类型 | `A* p = new B; p->foo();` 函数体可能是 `B::foo`，默认参数来自 `A` | 默认实参看指针/引用静态类型，函数体如果 virtual 才看动态类型 |
| 构造/析构中调用虚函数 | 构造/析构期间虚调用不会跨越当前正在构造/析构的类层次 | `Base` 构造/析构中调用 `foo()` 调 `Base::foo()`；`Derived` 构造/析构体中调用 `foo()` 调 `Derived::foo()` | 不要把普通多态规则直接套到构造/析构函数内部 |
| 模板特化 | 显式特化不是普通重载 | `template<class T> f(T&); template<> f(const int&); int i; f(i);` 输出主模板 | `i` 是 `int`，主模板推导成 `int&` 更直接 |
| 转换构造与 `explicit` | 直接初始化可用 explicit，拷贝初始化不可用 explicit | `C c1(7)` 调 `C(int)`；`C c2 = 7` 不调 `explicit C(int)` | 拷贝初始化会排除 explicit 构造 |
| 运算符表达式 | 运算符本质是函数调用，但保留求值语义和返回类型约束 | `a1[0] = a2[1]` 调两个 `operator[]` | 左侧需返回引用才能赋值 |

## 函数返回值类型：什么时候要加引用

| 目标 | 推荐返回类型 | 为什么 | 易错点 |
|---|---|---|---|
| 允许链式赋值 | `A& operator=(const A&)` | 返回当前对象本身，支持 `(a=b)=c`，避免拷贝 | 返回 `A` 会多一次拷贝且语义弱 |
| 前置自增 | `A& operator++()` | `++x` 返回自增后的原对象 | 返回局部变量引用会悬空 |
| 后置自增 | `A operator++(int)` | `x++` 返回修改前的旧值，通常是值返回 | 不能返回局部对象引用 |
| 下标作为左值 | `T& operator[](int)` | 支持 `a[i] = value` | 若返回 `T`，只能读不能改原数组 |
| const 下标只读 | `T operator[](int) const` 或 `const T& operator[](int) const` | const 对象不能返回可修改引用 | 返回 `T&` 会破坏 const |
| 输入输出流运算符 | `ostream& operator<<(ostream&, const T&)` | 支持 `cout << a << b` | 返回 `ostream` 会拷贝流，通常不可行 |
| 返回对象内部成员 | `T&` 或 `const T&` | 需要修改内部成员或避免大对象拷贝时使用 | 不要返回局部变量引用 |
| 算术运算 | `T operator+(...)`、`T operator-(...)` | 结果是新对象 | 返回引用会指向临时或局部，错误 |
| 工厂函数/转换结果 | `T` | 产生新对象 | 不要为了省拷贝返回局部引用；现代 C++ 有返回值优化 |
| 链表/容器访问节点 | 指针或引用视所有权而定 | 指针表达“可能为空”，引用表达“必存在” | 不清楚所有权时容易 double delete |

## 运算符重载参数的 const 规则

| 场景 | 推荐写法 | 原因 | 例子 |
|---|---|---|---|
| 只读取右操作数 | `const A& rhs` | 避免拷贝，不允许修改实参 | `A operator+(const A& rhs) const` |
| 会修改右操作数 | `A& rhs` | 必须允许修改传入对象 | 少见，按题意需要才写 |
| 右操作数是小类型 | `int x`、`double x` | 内置小类型直接传值即可 | `A operator+(int x) const` |
| 接收临时对象并转移资源 | `A&& rhs` | 移动语义 | `A& operator=(A&& rhs) noexcept` |
| 输出流左参数 | `ostream& os` | 输出会改变流状态，不能 const | `friend ostream& operator<<(ostream& os, const A& obj)` |
| 输入流左参数 | `istream& is` | 输入会改变流状态和对象 | `friend istream& operator>>(istream& is, A& obj)` |
| 成员函数不修改左操作数 | 函数末尾加 `const` | 限制 `this`，允许 const 对象调用 | `bool operator<(const A& rhs) const` |
| 赋值运算符 | `A& operator=(const A& rhs)` | 修改左操作数，返回左操作数引用 | 末尾不能加 `const` |

口诀：

```text
只读对象用 const A&；要改对象用 A&；小类型直接传值。
流对象不能 const；成员函数末尾 const 表示不改左操作数。
```

## 左值引用、右值引用和移动语义

| 写法 | 名称 | 能绑定什么 | 典型用途 | 易错点 |
|---|---|---|---|---|
| `A&` | 左值引用 | 有名字的对象，如 `A a;` | 修改原对象、避免拷贝 | 不能绑定普通临时对象 |
| `const A&` | const 左值引用 | 左值和右值都能绑定 | 只读传参、延长临时对象生命周期 | 不能通过引用修改对象 |
| `A&&` | 右值引用 | 临时对象、`std::move(a)` | 移动构造、移动赋值、接管资源 | 右值引用变量有名字后，表达式本身是左值 |
| `A(const A&)` | 拷贝构造 | 左值、const 对象、临时对象 | 复制资源 | 源对象应保持原状态 |
| `A(A&&) noexcept` | 移动构造 | 右值、`std::move` 后的对象 | 转移资源所有权 | 要把源对象置为可析构状态，如指针置 `nullptr` |
| `std::move(a)` | 右值转换 | 把左值强制转成右值表达式 | 允许调用移动构造/移动赋值 | `std::move` 本身不移动，只是类型转换 |
| `noexcept` | 不抛异常承诺 | 常用于移动构造/移动赋值 | 让 STL 容器更愿意移动元素 | `noexcept` 函数若抛异常会 `terminate` |

口诀：

```text
A& 绑定普通对象；A&& 绑定临时对象或准备被搬走的对象。
拷贝构造复制资源，移动构造转移资源。
std::move 不移动，只是把对象转换成右值。
右值引用变量有名字，所以在表达式中仍然是左值。
```

## `*` 的常见用法和判断

| 写法 | 含义 | 典型题点 | 易错点 |
|---|---|---|---|
| `T *p` | 声明指针变量 | `A *p = new B;` | `*` 属于声明符，不是乘法 |
| `*p` | 解引用，取得指针指向的对象 | `cout << *s` 中若 `s` 可转 `char*`，输出首字符 | 和 `cout << p` 输出指针/字符串区分 |
| `p->f()` | 等价于 `(*p).f()` | 多态调用、成员访问 | `p` 为空时解引用未定义 |
| `T& r = *p` | 引用绑定到指针所指对象 | `B &r = b0`、基类引用绑定派生对象 | 引用不是新对象，不调用构造 |
| `delete p` | 删除单个动态对象 | 触发析构 | 基类指针删除派生对象要求基类析构 virtual |
| `delete[] p` | 删除动态数组 | 依次析构数组元素 | `new[]` 和 `delete` 混用是错误 |
| `int A::*pm` | 成员指针 | 早年卷可能出现 | 与普通指针不是一回事 |
| `operator*` | 重载解引用运算符 | 智能指针/迭代器类题 | 返回类型通常是 `T&` |
| `char *s` | C 字符串指针 | `cout << s` 输出字符串 | `cout << *s` 输出第一个字符 |
| `const int* p` / `int* const p` | `const` 指针规则 | `const` 在 `*` 左边：指向的内容不能改；`const` 在 `*` 右边：指针本身不能改 | 把“不能改内容”和“不能改指向”混淆 |

## 输出题通用解题流程

| 步骤 | 要做什么 | 对应考点 | 易错提醒 |
|---|---|---|---|
| 1 | 标出所有对象创建点 | 构造、拷贝构造、转换构造 | `A a = b;` 是初始化，不是赋值 |
| 2 | 标出作用域和 `delete` 点 | 析构顺序 | 局部对象出作用域会自动析构 |
| 3 | 判断静态类型和动态类型 | 虚函数、多态 | virtual 只影响通过指针/引用调用的虚函数 |
| 4 | 列出候选重载函数 | 重载、const、模板 | 先名字查找，再重载决议 |
| 5 | 检查是否有名字隐藏 | 继承中的同名函数 | 派生类同名函数隐藏基类同名重载 |
| 6 | 检查返回值是否为引用 | `++`、`[]`、赋值 | 返回引用会改变原对象，值返回只改临时 |
| 7 | 检查异常路径 | `throw`、`catch`、重抛 | throw 后跳转，try 中后续语句不执行 |
| 8 | 最后处理输出格式 | `endl`、空格、无换行 | 析构函数里没 `endl` 就连续输出 |

## 函数题和程序填空题思路

| 题型 | 常见要求 | 解题模板 | 易错点 |
|---|---|---|---|
| 类接口补全 | 根据 judge 的调用写类 | 先从 `main` 和测试函数反推构造函数、运算符、类型转换 | 不要写多余输出；接口签名必须完全匹配 |
| 指针数组处理 | `vec **arr`、`*val < *minv`、`static_cast<double>(*val)` | 类中实现 `operator<`、`operator double`、`operator<<` | 比较依据和平均值依据可能不是同一个成员 |
| 多态接口 | `Shape* shape = new Rect; shape->area(); delete shape;` | 基类写 `virtual double area() = 0; virtual ~Shape(){}` | 忘记虚析构；派生类函数签名不匹配 |
| 链表填空 | `Node* next`、虚析构、`AppendNode` | 维护头尾指针；析构时先保存 next 再 delete 当前节点 | delete 后再访问 `p->next` 是野指针 |
| 循环队列 | `head`、`rear`、`queueSize` | 空：`head == rear`；满：`(rear+1)%size == head`；数量：`(rear-head+size)%size` | 队列容量是 `queueSize-1`，不是 `queueSize` |
| 分数类 | `Fraction + - print` | `+/-` 返回新对象；友元用于访问 private；不要求约分则不要约分 | 全局运算符不用 friend 就不能访问私有成员 |
| 动态数组 | `new[]`、扩容、析构 | 构造分配，析构 `delete[]`；拷贝要考虑深拷贝 | 默认拷贝会浅拷贝指针，导致 double delete |
| STL 字符串排序 | 多组输入、`stop`、稳定排序 | 读整行用 `getline`；按长度稳定排序 | 混用 `cin >> n` 和 `getline` 要吃掉换行 |
| Map 前缀和 | `insert` 覆盖、`sum(prefix)` | 可用 `map<string,int>` 遍历前缀 | 插入已有键要覆盖，不是累加 |
| 模板函数补全 | `template<class ...>`、迭代器 | 从函数调用反推模板参数和操作符参数 | `++first1` 后别忘 `++first2` |

## 异常对象生命周期和拷贝次数

| 场景 | 会发生什么 | 输出题怎么数 |
|---|---|---|
| `throw 临时对象` | 直接构造异常对象，现代 C++ 可能有拷贝消除 | 重点看题目是否有构造/拷贝构造输出，老题常按“构造异常对象”算 |
| `throw 局部对象` | 通常会从局部对象拷贝构造出异常对象；随后局部对象在栈展开时析构 | 先输出局部对象构造，再输出异常对象拷贝构造，再析构局部对象 |
| 栈展开 | `throw` 后离开当前作用域，已经构造完成的局部对象按逆序析构 | `try` 中 throw 后面的语句不执行，throw 前已经构造的对象要析构 |
| `catch(Exception e)` | 按值捕获，会从异常对象再拷贝构造 catch 参数 `e` | 多一次拷贝构造；catch 结束时先析构 `e` |
| `catch(Exception& e)` | 按引用捕获，不拷贝异常对象 | 没有 catch 参数拷贝；更推荐 |
| `catch(const Exception& e)` | 按 const 引用捕获，不拷贝，且不修改异常对象 | 最常见写法 |
| `catch(...)` | 捕获任意异常，不知道具体类型 | 不会构造具名 catch 参数 |
| catch 结束 | catch 参数先析构，最后异常对象本体销毁 | 按值捕获时通常看到两个析构：catch 参数、异常对象本体 |
| `throw;` | 在 catch 中重抛当前异常对象 | 不重新构造异常对象，只继续传播当前异常 |
| `throw e;` | 抛出表达式 `e`，可能重新拷贝构造新的异常对象 | 和 `throw;` 不同，输出题要多算拷贝 |

分析口诀：

```text
throw 局部对象：局部对象 -> 异常对象 -> 栈展开析构局部对象。
catch 按值：再拷贝一份 catch 参数。
catch 按引用：不拷贝。
throw 后 try 里后续语句不执行。
throw; 是重抛当前异常，throw e; 是重新抛出 e。
```

## 模板类专项

| 考点 | 标准写法 | 常见题目 | 易错点 |
|---|---|---|---|
| 模板类声明 | `template <class T> class Array { ... };` | 动态数组、队列、向量、节点类 | 漏写 `template<class T>` |
| 类外成员函数定义 | `template<class T> T& Array<T>::operator[](int i)` | 程序填空补 `operator[]`、`iterate` | 写成 `Array::operator[]`，漏掉 `<T>` |
| 模板构造函数 | `template<class T> CQueue<T>::CQueue(int s) : queueSize(s) { ... }` | 循环队列模板类 | `const` 数据成员必须在初始化列表中初始化 |
| 模板析构函数 | `template<class T> CQueue<T>::~CQueue(){ delete[] data; }` | 动态内存模板类 | `new[]` 对应 `delete[]` |
| 模板类指针成员 | `Array<T>* next;` | 分块数组、链表 | 写成 `Array* next` 在模板类外通常不完整/不规范 |
| 模板类对象声明 | `Array<int> a;`、`CQueue<double> rq;` | 主函数填空 | 漏写类型参数 |
| 模板类静态成员 | `template<class T> int A<T>::cnt = 0;` | 统计对象个数 | 每个 `T` 都有自己的一份 static 成员 |
| 模板类运算符 | `template<class T> T& Array<T>::operator[](int i)` | `a[i] = i` | 左值下标必须返回引用 |
| 模板类友元输出 | `friend ostream& operator<< <T>(ostream&, const Vec<T>&);` 或类内定义 friend | 输出模板对象 | 友元模板语法复杂，考试可优先类内直接定义 |
| 模板特化 | `template<> class A<int> { ... };` | `A<double>`、`A<char>`、`A<int>` 输出 | 特化版本完全替代主模板对应类型 |
| 模板参数推导 | 函数模板由实参推导，类模板通常要显式写类型 | `inner_product`、`max` | 同一个 `T` 不能同时由 `int` 和 `double` 推出 |
| 模板和继承 | `class Disk : public Shape` 通常不是模板；`CQueue<T>` 才是模板 | 类设计题区分普通多态和模板容器 | 不要把所有类都写成模板，只有数据类型可变才模板化 |

### 模板类程序填空固定套路

| 位置 | 先想什么 | 常见答案形态 |
|---|---|---|
| 类名前一行 | 这是不是模板类 | `template <typename T>` |
| 成员数据类型 | 数据是否随模板参数变化 | `T *data;`、`T value;`、`Node<T>* next;` |
| 类外函数名前 | 是否需要模板头 | `template <typename T>` |
| 作用域限定 | 类名是否要带模板参数 | `Array<T>::`、`CQueue<T>::` |
| 返回类型 | 是否需要作为左值或链式调用 | `T&`、`Class<T>&` |
| 构造函数 | 是否有 `const` 成员或动态内存 | 初始化列表、`new T[size]` |
| 析构函数 | 是否有 `new` 或 `new[]` | `delete`、`delete[]` |

## 重要专题速查

| 专题 | 必背结论 | 例子 |
|---|---|---|
| 不可重载运算符 | `::`、`.`、`.*`、`?:`、`sizeof` | 选择题常问 “which cannot be overloaded” |
| 必须作为成员重载 | `operator=`、`operator[]`、`operator()`、`operator->` | `[]` 不能写成 friend 全局函数 |
| 构造/析构能否 virtual | 构造函数不能 virtual；析构函数可以 virtual | 多态基类通常要 virtual 析构 |
| 析构能否重载 | 析构函数不能重载，一个类最多一个析构函数 | `~A()` 无参数，无返回值 |
| `new` vs `malloc` | `new` 是运算符，调用构造，返回类型化指针；`malloc` 是函数，不调用构造，返回 `void*` | OOP 选择题高频 |
| `delete` 安全性 | `delete nullptr` 安全；重复 delete 同一指针不安全 | “It is safe to delete the same pointer multiple times” 是错 |
| `vector::operator[]` | 不做边界检查 | 空 vector 的 `v[0] = 2.5` 是未定义行为 |
| `const` 数据成员 | 必须在构造函数初始化列表中初始化 | 不能在构造函数体内赋值 |
| static 数据成员 | 类内声明，类外定义；所有对象共享 | `int A::m;` |
| 同类对象访问 private | 类的成员函数可以访问同类任意对象的 private 成员 | `int fun(A& another){ another.x += x; }` 合法 |
| namespace | 同名函数可用命名空间区分 | `A::func(a)`、`B::func(b)` |
| inline | 主要减少函数调用开销，不是减少代码长度 | 判断题常设反向陷阱 |

## 针对历年卷的复习优先级

| 优先级 | 内容 | 原因 | 建议 |
|---|---|---|---|
| 最高 | 构造/拷贝/赋值/析构输出顺序 | 几乎每年都出现输出题 | 每题先画对象生命周期 |
| 最高 | 函数重载、隐藏、const、模板推导 | 选择题和输出题高频，细节多 | 严格按“名字查找 -> 可行函数 -> 最佳匹配” |
| 最高 | 运算符重载返回类型 | 程序填空和函数题常考 | `=`、`++前置`、`[]` 常返回引用；`+/-` 常返回值 |
| 高 | 虚函数、多态、虚析构 | 形状面积、文档图形、Base/Derived 输出题常见 | 基类接口写纯虚函数和虚析构 |
| 高 | 指针、引用、动态内存 | 链表、队列、数组、对象切片都依赖 | 明确所有权：谁 new，谁 delete |
| 高 | 异常处理 | 2018、2023 都出现 | 记住 catch 顺序、重抛、异常后控制流 |
| 中 | STL 容器和算法 | vector、map、string 排序题 | 注意 `getline`、稳定排序、边界 |
| 中 | 模板类/模板函数 | inner_product、Array、vec 类题 | 从调用点反推接口，不要过度设计 |
| 中 | namespace、static、friend | 选择/填空常考 | friend 破访问控制，不是成员函数 |

## 期末冲刺清单

| 顺序 | 复习内容 | 必做题型 | 检查点 |
|---|---|---|---|
| 1 | 构造、拷贝构造、赋值、析构 | 程序输出题 | 能区分 `A a=b`、`a=b`、函数传参、返回对象 |
| 2 | 继承、多态、virtual、对象切片 | 程序输出题、选择题 | 能判断调用基类还是派生类函数，析构是否完整 |
| 3 | 函数重载、隐藏、const、static | 程序输出题、选择题 | 能解释 `b.F(2)`、`const A a; a.f(3)` 这类题 |
| 4 | 运算符重载和返回引用 | 填空题、函数题 | `operator=`、`operator[]`、`operator++`、`operator<<` 返回类型不出错 |
| 5 | 模板类和模板函数 | 填空题、函数/类设计题 | 类外定义能写对 `template<class T>` 和 `Class<T>::` |
| 6 | exception 和 casting | 选择题、输出题 | `catch` 顺序、`throw;`、`dynamic_cast` 条件能判断 |
| 7 | 函数/类设计题 | 大题 | 先从 judge 代码反推接口，再写实现，不改测试代码 |

## 继承和生命周期易错补充

| 易错点 | 正确理解 | 例子 |
|---|---|---|
| `X can be assigned to Y` 的方向 | 英文意思是“X 可以赋值给 Y”，代码方向是 `Y = X` | `Derived can be assigned to Base` 表示 `Base b; Derived d; b = d;` |
| 派生对象赋给基类对象 | 可以，但发生对象切片，只保留基类子对象部分 | `Base b = derived;` 后 `b` 仍然是 `Base` 对象 |
| 基类对象赋给派生对象 | 默认不可以，除非派生类自定义 `operator=(const Base&)` 或转换 | `Derived d; Base b; d = b;` 通常编译错误 |
| 派生类指针赋给基类指针 | 可以，向上转型安全 | `Base* p = new Derived;` |
| 基类指针赋给派生类指针 | 默认不可以；需要 `dynamic_cast` 并检查结果 | `Derived* p = dynamic_cast<Derived*>(basePtr);` |
| 基类指针删除派生对象 | 基类析构函数必须是 `virtual`，否则未定义行为 | `Base* p = new Derived; delete p;` 要求 `virtual ~Base()` |
| 成员对象生命周期 | 成员对象先于所属类构造函数体构造，晚于所属类析构函数体析构 | `Base` 中有 `MyClass m;`：先 `MyClass::Ctor`，再 `Base::Ctor`；先 `Base::Dtor`，再 `MyClass::Dtor` |
| 派生对象完整构造顺序 | 基类子对象 -> 成员对象 -> 派生类构造函数体 | `Derived(int): Base(...), member(...) {}` |
| 虚基类构造顺序 | 虚基类先于普通基类构造；顺序看最派生类的继承层次声明顺序，不看构造函数初始化列表 | `class C : virtual B, virtual A` 中若 `B` 又虚继承 `A`，构造 `C` 时通常先构造共享的 `A`，再构造 `B` |
| 自定义派生类拷贝构造 | 初始化列表不写基类/成员时，它们会默认构造；要拷贝必须显式写 | `B(const B& b): A(b), a(b.a), i(b.i) {}` |
| 未自定义派生类拷贝构造 | 编译器生成的版本会自动拷贝构造基类和成员对象 | 相当于 `B(const B& other): A(other), member(other.member), ... {}` |
| 派生对象完整析构顺序 | 派生类析构函数体 -> 派生成员 -> 基类析构函数体 -> 基类成员 | 与构造顺序反向 |
| 构造/析构中的虚函数 | 构造/析构函数内部调用虚函数时，不会调用“尚未构造完成”或“已经析构掉”的派生层实现 | `Base` 构造中 `foo()` 调 `Base::foo()`；`Derived` 析构体中 `foo()` 调 `Derived::foo()` |

## 最容易丢分的细节清单

| 细节 | 正确写法/结论 | 错误写法/误区 |
|---|---|---|
| 拷贝构造参数 | `A(const A& rhs)` | `A(A& rhs)` 适用范围太窄 |
| 派生类初始化基类 | `B(int x): A(x) {}` | 以为只能由编译器调用基类默认构造，或在派生类初始化列表直接写基类成员名 |
| 派生类拷贝构造 | `B(const B& b): A(b), a(b.a), i(b.i) {}` | 自定义 `B(const B&)` 后，以为基类和成员对象会自动拷贝构造 |
| 默认派生类拷贝构造 | 不自定义 `B(const B&)` 时，编译器会自动拷贝基类和成员对象 | 把它和“自定义但没写初始化列表”的行为混为一谈 |
| 赋值返回 | `A& operator=(const A& rhs)` | 返回 `void` 或 `A` 影响链式赋值 |
| 前置 `++` | `A& operator++()` | 返回值会导致无法连续修改原对象 |
| 后置 `++` | `A operator++(int)` | 返回引用到局部旧值 |
| 下标左值 | `T& operator[](int)` | 返回 `T` 导致 `a[i]=x` 不能改原对象 |
| const 下标 | `T operator[](int) const` 或 `const T&` | 返回非 const 引用破坏只读性 |
| 输出运算符 | `friend ostream& operator<<(ostream&, const A&)` | 返回 `ostream` 或漏掉引用 |
| `operator[]` | 必须成员函数 | 写成非成员 friend |
| 运算符参数 const | 只读右操作数通常写 `const A&`，成员函数末尾 `const` 表示不改左操作数 | 把所有参数都写成 const，导致 `istream&` 或需要修改的参数无法工作 |
| 基类析构 | `virtual ~Base(){}` | 多态删除时基类析构非 virtual |
| 基类指针删除派生对象 | `Base* p = new Derived; delete p;` 要求 `Base` 析构为 virtual | 以为类里有其他虚函数就一定能安全删除；析构函数本身也应 virtual |
| 成员对象生命周期 | 成员先构造，所属类构造函数体后执行；析构时所属类析构函数体先执行，成员后析构 | 把成员对象当成在构造函数体里才开始构造 |
| 虚基类构造 | 虚基类构造顺序看最派生类的继承层次声明顺序，不看构造函数初始化列表 | 以为 `C(): B(), A()` 可以改变虚基类构造顺序 |
| assigned to | `X assigned to Y` 对应代码 `Y = X` | 把赋值方向理解反 |
| 动态数组释放 | `delete[] p` | `delete p` |
| 链表析构 | 先保存 next，再 delete 当前节点 | delete 后访问当前节点成员 |
| 模板参数一致 | `T` 由多个实参推导必须一致 | `max(int, int, float)` 直接推导同一 `T` 会失败 |
| `char*` 输出 | `cout << s` 输出字符串，`cout << *s` 输出首字符 | 把 `*s` 当字符串 |
| `const` 成员 | 函数尾部 `const` 限制 `this` | 以为只限制返回值 |
| 对象切片 | `A a = b;` 只保留 A 子对象 | 以为还能虚调用 B 行为 |
| 默认参数 + virtual | 默认参数看静态类型，虚函数体看动态类型 | 以为虚函数的默认参数也会跟着动态绑定 |
| `const` 指针 | `const` 在 `*` 左边：指向的内容不能改；`const` 在 `*` 右边：指针本身不能改 | 把 `const int* p` 和 `int* const p` 看成一样 |

```cpp
//Matrix.h
#ifndef MATRIX_H
#define MATRIX_H

template<typename T>
class  Matrix{
private:
    int row,col;
    T* data;
public:
    Matrix(int m = 0 ,int n = 0):row(m),col(n){
        if(m*n != 0){
            data = new T[m*n];
        }else data = NULL;
    }
    ~Matrix(){
        delete[] data;
    }

    Matrix(const Matrix& other) : row(other.row), col(other.col){
        int size = row * col;
        data = size ? new T[size] : NULL;
        for (int i = 0; i < size; i++)
            data[i] = other.data[i];
    }

    friend istream& operator>> (istream& in, Matrix& obj){
        for(int i = 0;i<obj.row;i++){
            for(int j = 0;j<obj.col;j++ ){
                in >> obj.data[i*obj.col + j];
            }
        }
        return in;
    }  

    Matrix& operator=(const Matrix& other) {
        if (this == &other)
            return *this;

        delete[] data;

        row = other.row;
        col = other.col;

        int size = row * col;
        data = size ? new T[size] : NULL;
        for (int i = 0; i < size; i++)
            data[i] = other.data[i];

        return *this;
    }
    
    friend ostream& operator<< (ostream& os,const Matrix& obj){
        for(int i = 0;i<obj.row;i++){
            for(int j = 0;j<obj.col;j++ ){
                os << obj.data[i*obj.col + j]<<" ";
            }
            os << endl;
        }
        return os;
    }

    Matrix operator+(const Matrix& rhs){
        Matrix res(row, col);
        for (int i = 0; i < row * col; i++)
            res.data[i] = data[i] + rhs.data[i];
        return res;
    }
};
#endif
```