# 03 类

> 从 C struct 到 C++ class 的关键跨越 —— 第三篇自学笔记

---

## 1. 从 C struct 到 C++ class：编程范式的革命

课件第 3-13 页用 Point 的例子展示了整个进化过程。这是理解 OOP 的关键段落。

### 1.1 C 的方式：数据与操作分离

```cpp
// C 风格 —— 数据和操作没有语法上的关联
typedef struct point {
    int x;
    int y;
} Point;

void print(const Point* p) {
    printf("%d %d\n", p->x, p->y);
}

void move(Point* p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}

// 使用
Point a;
a.x = 1; a.y = 2;
move(&a, 2, 2);
print(&a);
```

**问题在哪？**
- `print` 和 `move` 是全局函数，和 `Point` 的关联只体现在命名上（`Point* p` 作为第一个参数）。编译器不知道这些函数"属于" `Point`。
- 任何人都可以绕过函数直接修改 `a.x` 和 `a.y`，没有访问控制。
- 数据和操作分散在不同位置，理解一个"概念"需要查看多个地方。

### 1.2 C++ 的方式：将数据和操作捆绑在一起

```cpp
// C++ 风格 —— 数据和方法在同一个类中
class Point {
public:
    void init(int x, int y);
    void move(int dx, int dy);
    void print() const;
private:
    int x;
    int y;
};

// 实现
void Point::init(int ix, int iy) {
    x = ix; y = iy;
}
void Point::move(int dx, int dy) {
    x += dx; y += dy;
}
void Point::print() const {
    cout << x << ' ' << y << endl;
}

// 使用
Point a;
a.init(1, 2);          // 用 . 调用成员函数（不再是 &a 传指针）
a.move(2, 2);
a.print();
```

### 1.3 并排对比：这场范式转变一览

| 方面 | C (struct) | C++ (class) |
|------|------------|-------------|
| 结构声明 | `typedef struct point { int x; int y; } Point;` | `class Point { public: ... private: int x; int y; };` |
| 函数定义 | 全局函数 `void print(const Point* p);` | 成员函数 `void print() const;` |
| 数据访问 | 公开 `a.x = 1;` | 私有，通过函数 `a.init(1,2);` |
| 函数调用 | `print(&a);` 需要传地址 | `a.print();` 对象在前，自然 |
| 参数传递 | 显式传指针 `Point* p` | 隐式的 `this` 指针 |
| 类型检查 | 弱——任何 `void*` 都可传入 | 强——编译器知道调用者类型 |
| 封装 | 无——数据对所有人开放 | 有——public/private 控制访问 |

**这是整个课程最重要的转变。** 从此之后，你不再思考"我要操作哪些数据"和"调用哪些函数"，而是思考"我有一个什么对象，它能做什么"。

---

## 2. 对象 = 属性 + 服务

```
    数据 (属性/状态)
  操作 (方法/服务)
```

这个简单的等式是 OOP 世界观的基础：
- **属性 (Attributes)**：对象知道什么（内部数据，如 Point 的 x 和 y）
- **服务 (Services)**：对象能做什么（对外接口，如 Point 的 move 和 print）

**为什么要把它们放在一起？** 因为修改数据的方式直接影响数据的一致性。把操作和数据放在一起，你可以在操作内部做校验（比如 x 和 y 不能为负），调用者无法绕过这些校验直接破坏数据。

---

## 3. this 指针：谁在调用我？

`this` 是理解成员函数如何工作的关键。

### 3.1 隐藏的参数

```cpp
class Point {
public:
    void print() const;     // 你看到的声明
};

// 编译器内部的等价理解：
void Point::print(const Point* this);  // this 是一个隐藏参数！
```

当你写 `a.print()` 时，编译器实际上做的是 `Point::print(&a)` —— 把调用者的地址作为隐藏的第一个参数传入。

### 3.2 在成员函数中使用 this

```cpp
class Cup {
    int color;
public:
    void setColor(int color) {
        this->color = color;  // 用 this-> 区分成员变量和参数
    }
};
```

当成员变量和参数同名时，`this->` 用来区分"对象的 color"和"参数的 color"。如果名字不冲突，可以省略 `this->`，直接写 `color`。

**为什么要理解 this？**
- 它解释了为什么成员函数不需要显式接受对象参数——因为 `this` 隐式地传递了。
- 理解 `const` 成员函数的本质：`this` 的类型从 `Point*` 变成 `const Point*`。
- 某些操作（如返回自身引用 `return *this;`）必须用它。

---

## 4. 类的定义：.h 与 .cpp 分离

### 4.1 编译单元的概念

一个 C++ 程序被分成多个**编译单元**（每个 .cpp 文件是一个编译单元）。编译过程分三步：

```
.h (声明)  ---#include--->  .cpp (定义 + 声明)  ---预处理--->  .cpp (完整代码)
                                                               |
                                                               v
                                                           编译器 (每个 .cpp 独立)
                                                               |
                                                               v
                                                           .obj / .o (目标文件)
                                                               |
                                                               v
                                                           链接器 (链接所有 .o)
                                                               |
                                                               v
                                                           可执行文件
```

**关键认知**：编译器一次只看到一个 .cpp 文件。所以如果 `a.cpp` 调用了 `b.cpp` 中定义的函数，编译器需要提前知道这个函数的样子（返回类型、参数列表）。这份"预告"就是 **声明 (declaration)**，放在 .h 文件中。

### 4.2 头文件 = 接口 = 契约

```cpp
// Point.h — 声明（接口/契约）
#ifndef POINT_H
#define POINT_H

class Point {
public:
    void init(int x, int y);    // 只声明，不定义
    void move(int dx, int dy);
    void print() const;
private:
    int x;
    int y;
};

#endif
```

```cpp
// Point.cpp — 定义（实现）
#include "Point.h"
#include <iostream>
using namespace std;

void Point::init(int ix, int iy) {
    x = ix; y = iy;
}
// ...其余实现
```

### 4.3 include guards（包含保护）

```cpp
#ifndef HEADER_FLAG    // 如果 HEADER_FLAG 没有被定义过……
#define HEADER_FLAG    // 定义它
// ...头文件内容...
#endif                 // 结束条件编译块
```

**为什么需要它？** 假设 `a.h` 被 `b.h` 包含，而 `main.cpp` 同时包含了 `a.h` 和 `b.h`。如果没有包含保护，`a.h` 的内容会出现在 `main.cpp` 两次，导致重复定义错误。包含保护确保每个头文件在每个 .cpp 中只被处理一次。

> **约定**：`HEADER_FLAG` 通常命名为 `PROJECT_FILENAME_H`，如 `POINT_H`。

### 4.4 声明 vs 定义：什么该放在 .h 中？

| 放在 .h 中（声明） | 放在 .cpp 中（定义） |
|-------------------|---------------------|
| 类/结构体声明 | 成员函数实现 |
| 函数原型 | 非内联全局函数实现 |
| `extern` 变量声明 | 全局变量定义 |
| 内联函数体 | static 全局变量定义 |
| `const` 编译期常量 | |
| 模板（全部在头文件中） | |

> **黄金法则**：一个头文件中只放一个类的声明，头文件名称与类名相同。

---

## 5. 类 vs 对象：蓝图 vs 实物

课件用"猫"和"猫类"的类比非常精妙：

| 方面 | 类 (Class) | 对象 (Object) |
|------|-----------|---------------|
| 英文对应 | Cat species / 蓝图 | My cat Garfield / 具体的猫 |
| 存在时间 | 编译期 | 运行期 |
| 作用 | 定义属性和操作的结构 | 存储实际的数据值 |
| 在 C++ 中 | 类型 (type) | 变量 (variable) |
| 内存 | 不占用（除了 static 成员） | 占用内存 |

```
类  ————定义/实例化————>  对象
   <——抽象/归纳————
```

### 5.1 OOP 的五个特征（课件第 30 页）

1. **一切皆对象。** 思考问题时，先问"有什么东西在这里"，而不是"第一步做什么"。
2. **程序是一堆对象通过发送消息来告诉彼此做什么。** "发送消息"在 C++ 中就是"调用成员函数"。
3. **每个对象都有自己的内存，由其他对象组成。** 一个对象可以包含其他对象——这是"组合"的基础。
4. **每个对象都有一个类型。** 在 C++ 中，类就是类型。
5. **特定类型的所有对象都可以接收相同的消息。** 所有 `Point` 对象都能 `print()`、`move()`。

---

## 6. `::` 作用域解析运算符

```cpp
void S::f() {      // 这是类 S 的成员函数 f
    ::f();          // 调用全局的 f()（不是 S::f()，避免递归）
    ::a++;          // 访问全局变量 a
    a--;            // 访问类成员 a（等同于 this->a）
}
```

`::` 的三个用途：
- `ClassName::member` —— 指定某个类的成员（最常见）
- `::name` —— 访问全局命名空间中的名字（前面不加类名）
- `std::name` —— 访问 std 命名空间中的名字

---

## 7. 售票机案例：OOP 设计思维全景展示

课件用 TicketMachine 展示了一个完整的设计思维转变。

### 7.1 第一步：只有数据（错误的开始）

```cpp
class TicketMachine {
private:
    const int PRICE;
    int balance;
    int total;
};
```

这只是一个数据容器，和 C struct 没有本质区别。类存在的意义不仅是"把数据放在一起"。

### 7.2 第二步：加入操作（正确的方向）

```cpp
class TicketMachine {
public:
    void showPrompt();
    void getMoney();
    void printTicket();
    void showBalance();
    void printError();
private:
    const int PRICE;
    int balance;
    int total;
};
```

现在，`TicketMachine` 不仅知道自己的状态，还**知道自己能做什么**。`balance` 和 `total` 只能通过这些公开的方法来修改。

### 7.3 第三步：实例化（从类到对象）

```
类 TicketMachine             对象 ticketMachine1 (实例)
├── PRICE                    ├── PRICE = 2
├── balance                  ├── balance = 0
├── total                    ├── total = 0
├── showPrompt()             └── (可以调用所有方法)
├── getMoney()
├── printTicket()
├── showBalance()
└── printError()
```

每个 `TicketMachine` 对象有自己的 `balance` 和 `total`，但共享同一套操作代码。这就是"每个对象有自己的内存"的体现。

### 7.4 设计思维的转变总结

| 过程式思维 | OOP 思维 |
|------------|----------|
| 我要做什么？(步骤、流程) | 有什么东西在这里？(对象、角色) |
| 函数 + 全局数据 | 对象 = 数据 + 方法 |
| `get_money(&tm);` | `tm.getMoney();` |
| 数据暴露在外，谁都可以改 | 数据封装在内，通过接口访问 |

---

## 8. 本章要点总结

1. **C 的 struct 只打包数据**，操作是独立的全局函数；**C++ 的 class 打包数据和方法**，形成逻辑完整的实体。
2. **`this` 指针**是每个非静态成员函数的隐藏参数，指向调用该函数的对象。
3. **头文件 (.h)** 放声明（接口/契约），**.cpp** 放定义（实现）。`#ifndef/#define/#endif` 防止重复包含。
4. **类**是编译期的概念（蓝图/类型），**对象**是运行期的概念（实例/变量）。一个类可以有无数个对象。
5. **`::`** 用于指定名字所在的作用域。
6. **面向对象设计**的第一步不是"写函数"，而是"找对象"——识别系统中存在什么"东西"，它们有什么属性和行为。

---

*上一篇：[02 使用对象](02_使用对象.md)*
*下一篇：[04 对象交互](04_对象交互.md) —— 构造函数、析构函数、函数重载与 const 成员函数*
