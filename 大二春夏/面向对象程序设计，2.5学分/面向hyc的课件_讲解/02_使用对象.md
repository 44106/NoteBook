# 02 使用对象

> std::string、动态内存、指针、引用与 const —— 第二篇自学笔记

---

## 1. std::string：告别 char[] 的痛苦

### 1.1 为什么需要 string 类？

C 语言用 `char[]` 处理字符串，这是无数 bug 的根源：

```cpp
// C 的方式 —— 处处是陷阱
char cstr1[20];
char cstr2[20] = "jaguar";
cstr1 = cstr2;          // 编译错误！数组不能直接赋值
strcpy(cstr1, cstr2);   // 必须用函数，还要担心缓冲区溢出
if (cstr1 == cstr2)     // 比较的是地址，不是内容！
strcat(cstr1, cstr2);   // 拼接——cstr1 容量够大吗？
```

**为什么 char[] 这么麻烦？** 因为它只是一个字符数组，没有"字符串"的概念。长度信息不存在，边界检查不存在，赋值、比较、拼接都需要借助库函数。程序员必须自己管理内存和缓冲区——而人总是会犯错的。

C++ 的 `std::string` 是一个**类**。它把字符数据和所有字符串操作封装在一起，提供了直观、安全的接口：

```cpp
#include <string>
string str1;
string str2 = "panther";
str1 = str2;            // 直接赋值，自动管理内存
str1 += "lalala";       // 直接拼接
if (str1 == str2)       // 比较内容，不是地址
str3 = str1 + str2;     // 用 + 号拼接
cin >> str;             // 输入（自动处理长度）
cout << str;            // 输出
```

**核心区别**：`char[]` 是你自己管理的一块原始内存；`string` 是一个知道自己有多大、能自动扩容的智能对象。

### 1.2 构造 string 的多种方式

```cpp
string s1;                     // 默认构造，空字符串
string s2("hello");            // 从 C 字符串构造
string s3(s2);                 // 拷贝构造
string s4("abcdef", 3);        // 取前 3 个字符 → "abc"
string s5(s2, 1);              // 从下标 1 开始 → "ello"
string s6(s2, 1, 2);           // 从下标 1 开始取 2 个 → "el"
```

**为什么有这么多构造方式？** 因为字符串的来源多样：有时是 C 库返回的 `const char*`，有时只需要取一个子串，有时想从另一个 string 拷贝。提供多种构造函数让你在不同场景下都能用最自然的方式初始化。

### 1.3 常用操作速查

| 操作 | 语法 | 说明 |
|------|------|------|
| 子串 | `s.substr(pos, len)` | 返回从 pos 开始长度为 len 的新字符串 |
| 赋值 | `s.assign(...)` | 重新设置整个字符串的内容 |
| 插入 | `s.insert(pos, str)` | 在 pos 位置插入 str |
| 删除 | `s.erase(pos, len)` | 删除从 pos 开始的 len 个字符 |
| 追加 | `s.append(str)` | 在末尾追加，等价于 `s += str` |
| 替换 | `s.replace(pos, len, str)` | 将 [pos, pos+len) 替换为 str |
| 查找 | `s.find(str)` | 返回 str 首次出现的位置，找不到返回 `string::npos` |

```cpp
string s = "Hello World";
string sub = s.substr(0, 5);           // "Hello"
s.replace(6, 5, "C++");                // "Hello C++"
size_t pos = s.find("C++");            // pos = 6
if (pos != string::npos) {
    cout << "Found at " << pos << endl;
}
```

> **常见错误**：`find` 返回 `size_t`（无符号整数），找不到时返回 `string::npos`（通常是最大的 size_t 值）。如果用 `int` 接收，-1 和 `npos` 的比较会有问题。始终用 `size_t` 或 `auto`。

---

## 2. 文件 I/O 基础

C++ 用流对象处理文件，和 `cin`/`cout` 的用法几乎一样：

```cpp
#include <fstream>   // 注意：是 <fstream> 不是 <ifstream> 或 <ofstream>

// 写文件
ofstream outFile("C:\\test.txt");
outFile << "Hello world" << endl;
outFile.close();     // 虽然不是必须的（析构时会自动关闭），但明确关闭是好习惯

// 读文件
ifstream inFile("C:\\test.txt");
string str;
inFile >> str;       // 读取一个单词（空白字符分隔）
getline(inFile, str); // 读取一整行
```

> **注意**：课件中的 `#include <ifstream>` 和 `#include <ofstream>` 不标准，正确的头文件是 `<fstream>`。大多数编译器提供 `<ifstream>` 和 `<ofstream>` 作为内部包含的辅助头文件，但直接 `#include <fstream>` 最可靠。

---

## 3. 内存模型：变量住在哪里？

理解内存布局是掌握指针、动态分配、引用和 const 的前提。C++ 程序运行时，内存被分为三个主要区域：

| 区域 | 存放内容 | 生命周期 | 特点 |
|------|----------|----------|------|
| **全局数据区** (静态存储区) | 全局变量、static 全局变量、static 局部变量 | 程序启动到结束 | 编译期分配，地址固定 |
| **栈** (Stack) | 局部变量、函数参数 | 进入作用域到离开作用域 | 自动管理，LIFO |
| **堆** (Heap) | `new` / `malloc` 分配的变量 | 手动管理，`delete`/`free` 时归还 | 灵活但容易出错 |

```cpp
int i;                          // 全局数据区 —— 全局变量
static int j;                   // 全局数据区 —— 静态全局变量

void f() {
    int k;                      // 栈 —— 局部变量
    static int l;               // 全局数据区 —— 静态局部变量（持久但局部可见）
    int *p = new int;           // p 在栈上，*p 在堆上
}
```

### 3.1 static 的两个面孔

`static` 在 C++ 中有不同的含义，取决于它修饰的是什么：

| 修饰对象 | 效果 | 通俗理解 |
|----------|------|----------|
| 全局变量 / 全局函数 | 限制作用域在当前 .cpp 文件内 | "这个全局变量别让其他文件看到" |
| 局部变量 | 变量在多次调用间保持值不变 | "虽然是局部变量，但只初始化一次" |

```cpp
// file1.cpp
static int hidden = 42;     // 只能在 file1.cpp 中访问
static void helper() { }    // 只能在 file1.cpp 中调用

// file1.cpp 和 file2.cpp 各有自己的 hidden，互不干扰

void counter() {
    static int count = 0;   // 第一次调用时初始化，之后保持值
    count++;
    cout << count << endl;  // 第 1 次输出 1，第 2 次输出 2...
}
```

**为什么 static 局部变量第一次访问时才初始化？** 这是 C++ 的设计选择——避免"静态初始化顺序问题"。如果所有 static 变量都在程序启动时初始化，它们之间的依赖关系可能导致未定义行为。延迟到第一次访问时初始化更安全。

### 3.2 extern：跨文件共享

```cpp
// file1.cpp
int globalVar = 100;    // 定义（分配了存储空间）

// file2.cpp
extern int globalVar;   // 声明（告诉编译器：这个变量在别的文件里定义过了）
```

`extern` 不分配存储空间，只是一个"引用声明"。

---

## 4. new 和 delete：堆内存的手动管理

### 4.1 基本机制

在 C++ 中，`new` 和 `delete` 替代了 C 的 `malloc` 和 `free`。关键区别：`new` 不仅分配内存，还会**调用构造函数**；`delete` 不仅释放内存，还会**调用析构函数**。这对类对象至关重要。

```cpp
int *p = new int;              // 分配一个 int，未初始化
int *p2 = new int(42);         // 分配一个 int，初始化为 42
int *a = new int[10];          // 分配 10 个 int 的数组
Student *q = new Student();    // 分配一个 Student 对象，调用默认构造函数
Student *r = new Student[10];  // 分配 10 个 Student，每个都调用默认构造函数

delete p;      // 释放单个对象
delete p2;     // 释放单个对象
delete[] a;    // 释放数组 —— 方括号必不可少！
delete q;      // 释放单个 Student（析构函数被调用）
delete[] r;    // 释放 Student 数组（每个元素都调用析构函数）
```

### 4.2 五条铁律 (The 5 Iron Rules)

课件第 57 页列出的规则，每条都有其背后的原因：

1. **不要 delete 不是 new 出来的内存。**
   - 为什么？`delete` 假定内存是从堆上分配的，有特定的内部管理结构。对栈变量或全局变量调用 `delete` 会破坏程序内存管理，结果不可预测。

2. **不要对同一块内存 delete 两次。**
   - 为什么？第一次 delete 后，内存已归还给系统。第二次 delete 可能操作已被重新分配给别的对象的区域，导致"双重释放"崩溃。**防御技巧**：`delete p; p = nullptr;` —— 对空指针 delete 是安全的。

3. **用 `new[]` 分配数组，必须用 `delete[]` 释放。**
4. **用 `new` 分配单个实体，必须用 `delete`（不带括号）释放。**
   - 为什么这两条？编译器在处理 `new[]` 时可能会在数组前面额外存储数组长度的信息。`delete[]` 会读取这个信息，知道要调用多少次析构函数。如果用 `delete` 释放数组，编译器不知道有多少个元素，可能只析构第一个。

5. **delete 空指针是安全的。**
   - 为什么？这是标准明确规定的——`delete` 和 `delete[]` 对空指针什么都不做。所以初始化指针为 `nullptr` 是良好的防御性编程习惯。

### 4.3 动态数组

```cpp
int size;
cin >> size;
int *psome = new int[size];   // C++ 中可以用变量指定数组大小
// ... 使用 psome ...
delete[] psome;
```

> **和 C 的对比**：在 C 中你需要 `malloc(size * sizeof(int))`，并且要自己计算字节数。`new int[size]` 自动计算所需的存储空间。

---

## 5. 指向对象的指针

```cpp
string s = "hello";
string* ps = &s;       // ps 存储 s 的地址
```

### 5.1 三个关键运算符

| 运算符 | 名称 | 作用 | 示例 |
|--------|------|------|------|
| `&` | 取地址 | 获取变量的地址 | `ps = &s;` |
| `*` | 解引用 | 获取指针指向的对象 | `(*ps).length()` |
| `->` | 成员访问 | 解引用 + 访问成员 | `ps->length()` |

`ps->length()` 是 `(*ps).length()` 的语法糖，因为 `(*ps).` 经常使用又写起来很烦。

### 5.2 两种方式：直接对象 vs 指针

```cpp
// 方式一：直接对象
string s;               // s 在栈上，对象在声明时创建并初始化
s = "hello";
cout << s.length();     // 直接用 . 访问

// 方式二：指针
string *ps;             // ps 仅仅是一个指针，还没有指向任何对象
ps = &s;                // 现在 ps 指向 s
cout << ps->length();   // 用 -> 访问
```

**关键认知**：声明一个指针变量本身不一定创建了它指向的对象。`string *ps;` 只是创建了一个可以存储地址的变量，但那个地址指向什么还未确定。这和 Java/C# 不同——在那些语言里，声明引用变量时对象就已经存在（或被初始化为 null）。

---

## 6. 引用：别名机制

```cpp
int X = 47;
int& Y = X;       // Y 是 X 的引用——它们是同一个变量
Y = 18;           // 改变 X 的值
cout << X;        // 输出 18
```

### 6.1 引用的核心特性

- 引用在**定义时必须初始化**（对普通变量而言；作为函数参数时，初始化推迟到调用时）。
- 绑定一旦建立，**永远不能改变**。引用的对象是终身的。
- 对引用赋值，改变的是**被引用的对象**，而不是让引用绑到别的东西上。

```cpp
int a = 1, b = 2;
int& r = a;     // r 绑定到 a
r = b;          // 这不是让 r 绑定到 b！这是把 b 的值赋给 a！
// 现在 a = 2, b = 2, r 仍然绑定到 a
```

**这和指针的对比**：
```cpp
int a = 1, b = 2;
int* p = &a;    // p 指向 a
p = &b;         // 现在 p 指向 b —— 可以改变指向
```

### 6.2 指针 vs 引用对照表

| 特性 | 引用 | 指针 |
|------|------|------|
| 能否为空 | 不能为 null | 可以为 `nullptr` |
| 能否改变绑定 | 不能重新绑定 | 可以重新指向不同地址 |
| 独立性 | 依赖现有变量，是别名 | 独立存在的变量 |
| 语法 | 简洁：`r = 5; r.m();` | 需要 `*p = 5; p->m();` |
| 安全性 | 更高（不能为空，不会悬空） | 更低（需要手动检查 null） |
| 何时使用 | 传递参数、返回引用、for-range 循环 | 需要 null 语义、动态分配、数据结构中的节点链接 |

**使用决策**：
- 函数参数优先用 **const 引用** (`const T&`)——高效且安全。
- 需要修改传入的对象？用**非 const 引用** (`T&`)。
- 需要表示"可能没有对象"？用**指针**并检查 `nullptr`。
- 动态分配和链表/树结构？用**指针**。

---

## 7. 引用的三个"不能"

```cpp
// 1. 没有引用的引用
int&& rr = ...; // 不存在这种语法（C++11 的 && 是右值引用，不同概念）

// 2. 没有指向引用的指针
int&* p;        // 非法！

// 但是有指向指针的引用：
void f(int*& p); // 合法——p 是对指针的引用

// 3. 没有引用数组
int& arr[5];    // 非法！
```

**为什么有这些限制？** 引用本身不是对象，它只是一个别名，不占用独立存储空间。既然不是对象，就不能取它的地址（所以没有指向引用的指针），也不能把它放进数组（数组元素必须是对象）。

---

## 8. const：编译期的安全卫士

### 8.1 基础用法

```cpp
const int x = 123;
x = 27;          // 错误！不能修改常量
x++;             // 错误！
int y = x;       // 可以，const → non-const 没问题
const int z = y; // 可以，non-const → const 更安全的方向

const int class_size = 12;
int finalGrade[class_size];  // 可以，编译期常量可以用作数组大小
```

### 8.2 编译时常量 vs 运行时常量

```cpp
const int bufsize = 1024;       // 编译时常量——值在编译时就确定
int x;
cin >> x;
const int size = x;             // 运行时常量——值到运行时才知道
int array[size];                // C++ 标准不允许（尽管有些编译器支持）
```

**为什么编译器尽量不为 const 分配存储空间？** 对于编译时常量，编译器只需要在符号表中记录它的值即可。每次使用 `bufsize` 的地方直接替换为 `1024`。这既节省内存又提升效率。除非你用了 `extern const` 或取地址操作，编译器才会被迫分配存储空间。

### 8.3 指针与 const：三兄弟辨析

这是最容易混淆的地方。口诀：**const 离谁近就修饰谁。**

```cpp
const char *p = "abc";    // p 指向的内容是常量（不能通过 p 修改）
char const *p = "abc";    // 同上！const 在 * 左边 = 指向的内容是常量
char * const p = "abc";   // p 本身是常量（不能修改 p 指向别处）
const char * const p = ...;// p 和 *p 都是常量
```

图解：
```
const char *p        →    p 可变，*p 不可变
char const *p        →    同上（const 在 * 左边 = 修饰 char）
char * const p       →    p 不可变，*p 可变
const char * const p →    p 不可变，*p 也不可变
```

**小测试解析**：
```cpp
string s("Fred");
const string* p = &s;    // p 可变，*p 不可变（不能通过 p 修改 s）
string const* p = &s;    // 同上
string *const p = &s;    // p 不可变，*p 可变
```

### 8.4 字符串字面量的陷阱

```cpp
char* s = "Hello, world!";   // 危险！s 指向只读内存
s[0] = 'h';                   // 未定义行为——可能崩溃！
```

**为什么编译器不报错？** 历史兼容性。C++ 为了兼容旧的 C 代码，允许 `char*` 指向字符串字面量（尽管字面量是 const）。正确做法：
```cpp
const char* s = "Hello, world!"; // 明确表示这是只读的
// 或者
char s[] = "Hello, world!";      // 可修改的副本，在栈上
s[0] = 'h';                      // 安全，修改的是栈上的数组
```

### 8.5 const 转换规则

```cpp
void f(const int* x);

int a = 15;
f(&a);              // OK：non-const → const 是安全的（承诺"我不会修改"）

const int b = a;
f(&b);              // OK：const → const 没问题
b = a + 1;          // 错误！b 是 const
```

核心原则：**non-const 可以隐式转换为 const（限定得更严格总是安全的），const 不能隐式转换为 non-const。** 必须用 `const_cast` 时，请三思——它通常意味着设计有问题。

### 8.6 按值传递 const 有意义吗？

```cpp
void f1(const int i) { i++; }  // 错误：参数是 const 副本
```

**按值传递时使用 const 没什么意义** ——函数拿到的是参数的副本，修改副本不影响原始值。对外部调用者来说，函数的参数是 const 还是 non-const 没有任何区别。

但是 **const 引用参数** 非常有意义：
```cpp
void print(const BigObject& obj);  // 高效（不拷贝）+ 安全（不会修改）
```

---

## 9. 本章要点总结

1. **`std::string`** 是类，不是原始数组。它能自动管理内存、支持直观的运算符（`+`, `==`, `=`）。
2. **内存分三个区域**：全局数据区（static/global）、栈（局部变量）、堆（new/malloc）。生命周期各不相同。
3. **`new` 和 `delete` 配套使用**：`new` 调构造，`delete` 调析构。`new[]` 必须配 `delete[]`。
4. **指针存储地址，引用是别名**。指针可为 null、可改变指向；引用更安全但不能为空、不能重新绑定。
5. **const** 修饰指针时，`const` 的位置决定它修饰的是指针本身还是指向的内容。
6. **字符串字面量是只读的**，用 `const char*` 或 `char[]`（可修改副本）处理。
7. **参数传递首选 const 引用**：既避免拷贝开销，又保护原始数据不被修改。

---

*上一篇：[01 C++ 入门与课程介绍](01_C++入门与课程介绍.md)*
*下一篇：[03 类](03_类.md) —— 从 C struct 到 C++ class 的关键跨越*
