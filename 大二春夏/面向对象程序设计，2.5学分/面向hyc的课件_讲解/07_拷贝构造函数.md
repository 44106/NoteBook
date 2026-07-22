# 第7章 拷贝构造函数与 static

## 1. 引用作为类成员

### 1.1 为什么必须使用初始化列表

引用在声明时必须初始化，不能"先声明后赋值"。因此，如果类成员是引用类型，必须在构造函数初始化列表中进行初始化。

```cpp
class X {
public:
    int& m_y;
    X(int& a);       // 不能在函数体内初始化引用成员
};

X::X(int& a) : m_y(a) { }  // 必须在初始化列表中绑定
```

**为什么**：引用没有空状态，它必须在诞生的那一刻就指向某个对象。构造函数体执行时，成员已经构造完毕，所以初始化列表是唯一的机会。

### 1.2 返回引用

函数可以返回引用，但必须确保引用的对象在函数返回后仍然存活：

```cpp
const int SIZE = 32;
double myarray[SIZE];

double& subscript(const int i) {
    return myarray[i];    // OK: myarray 是全局数组，函数返回后仍然存在
}
```

**铁律**：返回的引用必须指向**非局部变量**（全局变量、静态变量、或调用者传入的引用）。永远不要返回局部变量的引用。

```cpp
// 危险!
int& dangerous() {
    int x = 42;
    return x;  // x 在函数返回后被销毁，引用变成"悬空引用"
}
```

### 1.3 const 在函数参数中的应用

```cpp
// 不好的做法: 按 const 值传递 (const 没有意义，多此一举)
void bad(const int x);

// 好的做法: 按 const 引用传递
void good(const string& name, int weight);
```

**为什么用 const 引用**：
- 避免复制开销（对于 string 等大型对象尤为重要）
- const 保证参数不被修改
- 可以接受临时值（见下文）

### 1.4 临时值是 const — 关键理解

```cpp
void func(int&);
func(i * 3);  // 错误或警告!
```

编译器实际生成：

```cpp
void func(int&);
const int _tmp_ = i * 3;  // 编译器创建临时变量
func(_tmp_);  // 错误: 非 const 引用不能绑定到 const 临时变量
```

**本质原因**：`i * 3` 产生的是一个临时值，你没有变量名来访问它，所以编译器视其为 const。将非 const 引用绑定到它是不允许的（否则你修改了它，却无法从外部看到修改结果）。

**解决方案**：将参数声明为 `const int&`。

---

## 2. 拷贝构造函数

### 2.1 为什么需要拷贝构造函数

当需要从已有对象创建一个新对象时：

```cpp
Currency bucks(100, 0);
func(bucks);  // bucks 被复制到函数的参数 p (按值传递)
```

**编译器自动生成的拷贝构造函数**执行"逐成员复制"：
- 对于普通类型（int、double 等），直接复制值 —— 没问题
- 对于指针，只复制地址 —— 这会导致**多个对象共享同一块动态内存**

### 2.2 浅拷贝的陷阱

以 `Person` 类为例，`name` 是 `char*`：

```
浅拷贝 (编译器生成的):
+-------+       +----------+
| name  | ----> | "Alice\0" |  <---- 只有一份字符串数据
+-------+       +----------+
|  ...  |
+-------+
+-------+
| name  | ----/
+-------+
```

**问题**：
- 一个对象析构时 `delete[] name`，释放了字符串内存
- 另一个对象仍然持有指向已释放内存的指针 —— **悬空指针**
- 修改字符串会影响"两个"对象 —— 逻辑上不合理

### 2.3 深拷贝 — 正确的解决方案

```
深拷贝:
+-------+       +----------+
| name  | ----> | "Alice\0" |
+-------+       +----------+
|  ...  |
+-------+
+-------+       +----------+
| name  | ----> | "Alice\0" |  <---- 独立的副本
+-------+       +----------+
```

### 2.4 拷贝构造函数签名

```cpp
T::T(const T&);
```

- 参数是 `const T&`（**为什么是引用？** 如果是值传递，调用拷贝构造函数本身又需要拷贝 —— 无限递归）
- 如果你不提供，编译器自动生成（逐成员复制）
- 无返回值

### 2.5 Person (char*) 完整实现

```cpp
#include <cstring>

class Person {
public:
    Person(const char* s);
    Person(const Person& w);  // 拷贝构造函数
    ~Person();
private:
    char* name;
};

// 普通构造函数
Person::Person(const char* s) {
    name = new char[::strlen(s) + 1];  // +1 给 '\0'
    ::strcpy(name, s);
}

// 拷贝构造函数 —— 深拷贝
Person::Person(const Person& w) {
    name = new char[::strlen(w.name) + 1];
    ::strcpy(name, w.name);
    // 每个 Person 拥有独立的 name 拷贝
}

Person::~Person() {
    delete[] name;  // 数组 delete，与 new[] 对应
}
```

**注意**：
- 可以访问 `w.name`，尽管 name 是 private —— 这是同一类的成员函数，可以访问同类其他对象的私有成员
- 拷贝构造函数初始化的是**尚未初始化的内存**，与赋值运算符不同

### 2.6 Person (string) — 编译器生成的就够了

```cpp
class Person {
public:
    Person(const string&);
    ~Person();
private:
    string name;
};
```

此时不需要自己写拷贝构造函数。编译器生成的会将每个成员的拷贝构造函数逐一调用。`string` 自己实现了深拷贝，因此 Person 的默认拷贝构造就是正确的。

**关键在于**：默认拷贝构造是逐成员递归的。只要每个成员自身正确处理了拷贝，组合起来的对象就不需要自定义拷贝构造。

### 2.7 拷贝构造函数何时被调用

| 场景 | 示例 | 说明 |
|------|------|------|
| **按值传递参数** | `func(bucks)` | 实参被复制到形参 |
| **初始化新对象** | `Person b = a;` 或 `Person b(a);` | 注意这是初始化，不是赋值 |
| **函数返回对象** | `return player;` | 返回的对象是原始对象的副本 |

**函数返回时的拷贝**：

```cpp
Person captain() {
    Person player("George");
    return player;   // 拷贝发生在这里
}
Person who = captain();  // who 是返回值的副本
```

编译器可能会优化掉返回值拷贝（**复制省略 / Copy Elision**），但程序员不应依赖优化：始终为"不太聪明的编译器"写好正确的拷贝构造。

### 2.8 构造 vs. 赋值

每个对象**构造一次**，可以被**赋值多次**：

```cpp
Person a("Alice");       // 构造
Person b = a;            // 拷贝构造（不是赋值！注意有等号但不一定是赋值）
a = b;                   // 赋值（两个已存在的对象）
```

- 构造：初始化之前未初始化的内存
- 赋值：覆盖已有对象的值

### 2.9 拷贝构造函数指南

| 场景 | 做法 |
|------|------|
| 只需逐成员复制（无指针/资源） | 不写，用编译器默认的 |
| 有动态内存/文件句柄等资源 | 自己写深拷贝 |
| 不想让对象被复制 | `T(const T&) = delete;` (C++11) 或声明为 private |
| 有虚析构但资源简单 | 可能不需要自定义拷贝 |

---

## 3. static 关键字深度解析

### 3.1 两个基本含义

- **静态存储**：在固定地址分配一次，值在程序运行期间持续存在
- **名称可见性**：控制标识符的链接属性

### 3.2 全局 static — 文件作用域隐藏

```cpp
// file1.cpp
int g_global;           // 外部链接（其他文件可以 extern）
static int s_local;     // 内部链接（仅本文件可见）
static void helper() {} // 内部链接

// file2.cpp
extern int g_global;    // OK, 引用 file1 中的 g_global
extern int s_local;     // 链接错误! s_local 仅 file1 可见
```

**为什么用**：避免全局命名冲突。将只在本文件使用的函数/变量声明为 static。

### 3.3 函数内部的 static — 持久值

```cpp
void f() {
    static int num_calls = 0;  // 只初始化一次
    num_calls++;
    // num_calls 在 f() 多次调用间保持值
}
```

- 值在程序运行期间被记住（持久性）
- 初始化只发生一次，在第一次调用时（C++11 起线程安全）
- 适用于：统计调用次数、缓存、单例模式等

### 3.4 static 应用于对象

```cpp
class X {
    X(int, int);
    ~X();
};

void f() {
    static X my_X(10, 20);  // 只构造一次
}
```

- **构造**：第一次遇到定义时调用构造函数（最多一次）
- **析构**：程序退出时，按 **LIFO**（后进先出/栈序）顺序析构

**条件构造**：

```cpp
void f(int x) {
    if (x > 10) {
        static X my_X(x, x * 21);  // 只在 x>10 时构造
    }
}
// my_X 只在 f() 以 x>10 首次被调用时构造
// 只有被构造了才会被析构
```

### 3.5 全局对象

```cpp
static X global_x(12, 34);   // 构造函数在 main() 之前调用
static X global_x2(8, 16);   // global_x 先于 global_x2
```

- 构造函数在 `main()` **之前**调用（同一文件中按出现顺序）
- 析构函数在 `main()` 退出或 `exit()` 调用时执行
- `main()` 不再是第一个执行的函数

### 3.6 静态成员变量

```cpp
// StatMem.h
class StatMem {
public:
    static int count;  // 声明（不是定义！）
};

// StatMem.cpp
int StatMem::count = 0;  // 定义（在 .cpp 中，没有 static 关键字）
```

- 独立于任何实例存在（**类级别**的变量）
- 所有实例共享同一个值
- 必须在 .cpp 文件中**定义**（分配存储空间）
- 遵守通常的访问控制（private / public）

### 3.7 静态成员函数

```cpp
class StatFun {
public:
    static void printCount();
    static int total;
};

StatFun::printCount();         // 通过类名调用
StatFun obj;
obj.printCount();              // 也可以通过对象调用
```

- **没有 `this` 指针** —— 因此不能访问非静态成员
- 只能访问静态成员变量、静态成员函数，或全局变量
- 不能被声明为 virtual（没有对象，无法通过 vptr 分派）

**为什么没有 this**：静态成员函数属于类本身，不属于任何对象。调用时不需要对象。

### 3.9 使用方法

| 访问方式 | 示例 |
|---------|------|
| 通过类名 | `ClassName::staticMember` |
| 通过对象 | `object.staticMember` |

推荐使用类名访问，因为这样可以一眼看出是静态成员。

---

## 本章小结

- 引用成员必须用初始化列表，返回引用必须指向非局部变量
- 临时值是 const，非 const 引用不能绑定
- 拷贝构造函数是深拷贝的必要机制：签名 `T(const T&)`，按值传递 / 初始化 / 函数返回 时调用
- `string` 等 RAII 类型让默认拷贝构造自动正确
- `static` 在 C++ 中有多重含义：文件内隐藏、函数内持久、全局对象提前构造、类级别共享
- 静态成员函数没有 this，只能访问静态数据
