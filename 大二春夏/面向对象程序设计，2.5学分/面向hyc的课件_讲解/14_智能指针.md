# 14 智能指针 —— 让内存管理自动化

## 目录

1. [标准库智能指针概览](#标准库智能指针概览)
2. [智能指针融合了哪些概念](#智能指针融合了哪些概念)
3. [引用计数机制详解](#引用计数机制详解)
4. [四类架构设计](#四类架构设计)
5. [UCObject —— 引用计数管理](#ucobject--引用计数管理)
6. [UCPointer —— 智能指针模板](#ucpointer--智能指针模板)
7. [StringRep —— 实际数据](#stringrep--实际数据)
8. [String —— 公共接口](#string--公共接口)
9. [Envelope-Letter 模式](#envelope-letter-模式)
10. [设计评价与对比](#设计评价与对比)
11. [与 std::shared_ptr 的对比](#与-stdshared_ptr-的对比)
12. [总结](#总结)

---

## 标准库智能指针概览

C++11 起标准库提供了以下智能指针：

| 智能指针 | 说明 | 引入版本 |
|----------|------|----------|
| `std::unique_ptr` | 独占所有权，不能被拷贝，只能移动 | C++11 |
| `std::shared_ptr` | 共享所有权，引用计数管理 | C++11 |
| `std::weak_ptr` | 不增加引用计数的"观察者"指针 | C++11 |
| `std::auto_ptr` | 已废弃，有缺陷的所有权转移语义 | C++98（C++17 移除） |

**本章重点**：通过自建一个简化版的智能指针系统，深入理解引用计数的工作原理、智能指针与模板和继承的结合方式，以及 Envelope-Letter 设计模式。理解这些原理后，使用 `std::shared_ptr` 等标准库组件会更得心应手。

---

## 智能指针融合了哪些概念

智能指针不是一个单独的 C++ 特性，而是多个概念的综合应用：

```
智能指针 = 模板 + 继承 + 引用计数 + 运算符重载
```

| 概念 | 在智能指针中的作用 |
|------|-------------------|
| **模板** | 让智能指针可以指向任意类型（泛型）|
| **继承** | 让数据类从引用计数基类继承，获得引用计数能力 |
| **引用计数** | 追踪有多少个指针共享同一个对象，决定何时释放 |
| **运算符重载** | 重载 `->` 和 `*`，让智能指针像原生指针一样使用 |

**为什么需要综合运用这些概念？**

- 不使用模板 → 每种类型都要写一个智能指针类
- 不使用继承 → 引用计数逻辑和业务数据混在一起
- 不使用引用计数 → 无法知道何时安全释放共享对象
- 不重载运算符 → 使用智能指针不方便，`ptr->method()` 变成 `ptr.get()->method()`

---

## 引用计数机制详解

### 什么是引用计数

引用计数是一个整数，记录当前有多少个指针指向同一个对象。

**核心规则**：

```
1. 对象创建时，引用计数 = 1（有一个指针指向它）
2. 又有一个指针指向它时，引用计数 + 1
3. 有一个指针不再指向它时，引用计数 - 1
4. 引用计数降到 0 时，释放对象
```

### 状态演变的图解

#### 初始状态

```
String x("abcdef");

   x ──────► +---+---+---+---+---+---+
             | 1 | a | b | c | d | e | f |
             +---+---+---+---+---+---+
               ↑
           引用计数 = 1
```

#### 浅拷贝（两个指针共享同一份数据）

```
String x("abcdef");
String y = x;    // y 是 x 的浅拷贝

   x ──────► +---+---+---+---+---+---+
             | 2 | a | b | c | d | e | f |
   y ──────► +---+---+---+---+---+---+
               ↑
           引用计数 = 2
```

x 和 y 指向同一个字符串数据，引用计数变为 2。没有被复制的是数据本身——只有指针被复制了。

#### 写时复制（Copy on Write）

```
String x("abcdef");
String y = x;            // 浅拷贝，引用计数 = 2
x = "Hello world";       // x 被修改：触发写时复制！

   x ──────► +---+---+---+---+---+---+---+---+---+---+---+
             | 1 | H | e | l | l | o |   | w | o | r | l | d |
   y ──────► +---+---+---+---+---+---+
             | 1 | a | b | c | d | e | f |
             +---+---+---+---+---+---+

   原来的共享数据引用计数降为 1（只有 y 指向它）
   x 指向了新的副本
```

**写时复制的价值**：如果没有人修改，就共享同一份数据（省内存）。一旦有人要修改，就复制一份，修改不影响其他人。这种策略在文本处理等场景中非常有效。

### 引用计数的操作规则

```
p = q;（指针赋值）
需要做：
    1. p->decrement();   // p 不再指向旧对象，旧对象的计数减 1
    2. p = q;             // p 现在指向 q 指向的对象
    3. p->increment();    // 新对象的计数加 1
```

---

## 四类架构设计

本章的智能指针系统由四个类组成：

```
┌─────────────────┐
│    String       │  ← 对外暴露的公共接口（用户使用这个）
│   (envelope)    │
└────────┬────────┘  has-a（持有）
         │
┌────────▼────────┐
│  UCPointer<T>   │  ← 智能指针模板（自动管理引用计数）
│  (smart ptr)    │
└────────┬────────┘  has-a（持有）
         │
┌────────▼────────┐
│   StringRep     │  ← 实际数据存储（字符串的表示）
│   (letter)      │
└────────┬────────┘  is-a（继承）
         │
┌────────▼────────┐
│   UCObject      │  ← 引用计数基类（管理 m_refCount）
└─────────────────┘
```

**职责分离**：

| 类 | 职责 | 关心引用计数吗 |
|----|------|---------------|
| `UCObject` | 维护引用计数，提供 `incr()` / `decr()` | 是，这是它唯一的职责 |
| `UCPointer<T>` | 自动调用引用计数操作，重载 `->` 和 `*` | 是，它确保计数正确 |
| `StringRep` | 存储和操作字符串数据 | 否，它从 UCObject 继承获得了计数能力 |
| `String` | 提供用户友好的接口 | 否，它通过 UCPointer 间接获得 |

---

## UCObject —— 引用计数管理

`UCObject` 是引用计数系统的"引擎"。

```cpp
#include <cassert>

class UCObject {
public:
    UCObject() : m_refCount(0) { }
    virtual ~UCObject() {
        assert(m_refCount == 0);  // 析构时引用计数必须为 0
    }
    UCObject(const UCObject&) : m_refCount(0) {
        // 拷贝构造时，新对象的引用计数从 0 开始
    }

    void incr() { m_refCount++; }

    void decr() {
        m_refCount--;
        if (m_refCount == 0) {
            delete this;  // 我是最后一个指向者，自毁
        }
    }

    int references() { return m_refCount; }

private:
    int m_refCount;
};

UCObject& UCObject::operator=(const UCObject&) {
    // 赋值不影响引用计数（引用计数由 UCPointer 管理）
    return *this;
}
```

### 关键设计决策

**为什么 `m_refCount` 初始化为 0 而不是 1？**

因为 `UCPointer` 的构造函数会自动调用 `incr()`。如果初始值为 1 而 `UCPointer` 又调用 `incr()`，计数就变成了 2——这是错误的。初始值为 0 确保了"指针的计数 = 实际指向该对象的指针数量"。

**`delete this` 安全吗？**

安全的前提是：对象在堆上分配，且没有人在 `delete this` 之后使用该对象。`UCObject` 的设计确保了这一点——只有引用计数降为 0 时才执行 `delete this`，此时没有任何指针指向它。

**为什么析构函数中有 `assert(m_refCount == 0)`？**

这是一个防御性编程措施。如果析构时引用计数不为 0，说明程序设计有 bug——还有指针指向这个对象但它已经被销毁了。`assert` 在 Debug 模式下会捕获这个错误。

---

## UCPointer —— 智能指针模板

`UCPointer` 是智能指针的核心——它像一个"自动扳机"，自动调用引用计数的增减操作。

```cpp
template <class T>
class UCPointer {
private:
    T* m_pObj;

    void increment() { if (m_pObj) m_pObj->incr(); }
    void decrement() { if (m_pObj) m_pObj->decr(); }

public:
    // 构造函数：从原生指针创建智能指针
    UCPointer(T* r = nullptr) : m_pObj(r) {
        increment();  // 创建智能指针 = 开始指向 = 引用计数 +1
    }

    // 析构函数：智能指针销毁 = 不再指向 = 引用计数 -1
    ~UCPointer() {
        decrement();
    }

    // 拷贝构造函数：新指针 = 旧指针的副本 = 引用计数 +1
    UCPointer(const UCPointer<T>& p) : m_pObj(p.m_pObj) {
        increment();
    }

    // 赋值运算符
    UCPointer& operator=(const UCPointer<T>& p) {
        if (m_pObj != p.m_pObj) {       // 防止自赋值
            decrement();                 // 先放弃旧对象
            m_pObj = p.m_pObj;           // 指向新对象
            increment();                 // 新对象引用计数 +1
        }
        return *this;
    }

    // 重载 -> 运算符
    T* operator->() const { return m_pObj; }

    // 重载 * 运算符
    T& operator*() const { return *m_pObj; }
};
```

### 每个方法的设计分析

#### 构造函数

```
触发时机：UCPointer<StringRep> p(new StringRep("hello"));
操作流程：
  1. m_pObj = 指向 "hello" 的 StringRep 对象
  2. increment() → m_pObj->incr() → 引用计数: 0 → 1
```

#### 析构函数

```
触发时机：UCPointer 离开作用域
操作流程：
  1. decrement() → m_pObj->decr()
  2. 如果引用计数变为 0：delete m_pObj → 调用 StringRep 析构 → 调用 UCObject 析构
```

#### 拷贝构造函数

```
触发时机：UCPointer<StringRep> p2 = p1;
操作流程：
  1. m_pObj = p1.m_pObj（指向同一个 StringRep）
  2. increment() → 引用计数: 1 → 2
```

#### 赋值运算符

```
触发时机：p2 = p1;
操作流程（假设 p2 原来指向对象 A，p1 指向对象 B）：
  1. 检查 m_pObj != p.m_pObj（防止 p2 = p2 的问题）
  2. decrement() → A 的引用计数 -1（如果降到 0 则 delete A）
  3. m_pObj = p.m_pObj → 现在指向 B
  4. increment() → B 的引用计数 +1
```

**为什么需要自赋值检查？**考虑 `p = p`——如果没有自赋值检查：
1. `decrement()` 减少引用计数（可能降到 0 → delete 对象）
2. 然后尝试从已删除的对象读取 `m_pObj`——灾难！

### operator-> 和 operator* 的妙用

```cpp
// 不用智能指针：
StringRep* raw = new StringRep("hello");
int len = raw->length();    // 用 -> 调用成员
int len2 = (*raw).length(); // 用 * 解引用再调用成员

// 用智能指针：
UCPointer<StringRep> smart(new StringRep("hello"));
int len = smart->length();    // operator-> 返回 m_pObj，然后调用 length()
int len2 = (*smart).length(); // operator* 返回 *m_pObj，然后调用 length()
```

**一行代码的转换过程**：

```
smart->length()
  → smart.operator->()->length()   // smart.operator->() 返回 m_pObj (StringRep*)
  → (m_pObj)->length()             // 原生指针调用 StringRep::length()
```

`operator*` 的实现：

```cpp
T& operator*() const { return *m_pObj; }
// *smart → smart.operator*() → *(m_pObj) → StringRep 对象的引用
```

---

## StringRep —— 实际数据

`StringRep` 是"干实事"的类——它继承自 `UCObject` 获得了引用计数能力，同时负责实际的字符串存储和操作。

```cpp
class StringRep : public UCObject {
public:
    StringRep(const char *s);
    ~StringRep();
    StringRep(const StringRep&);

    int length() const { return strlen(m_pChars); }
    int equal(const StringRep& sp) const {
        return (strcmp(m_pChars, sp.m_pChars) == 0);
    }

private:
    char *m_pChars;
};
```

**实现细节**：

```cpp
StringRep::StringRep(const char *s) {
    if (s) {
        int len = strlen(s) + 1;      // +1 给 '\0'
        m_pChars = new char[len];
        strcpy(m_pChars, s);
    } else {
        m_pChars = new char[1];
        *m_pChars = '\0';              // 空字符串
    }
}

StringRep::~StringRep() {
    delete[] m_pChars;                 // 释放字符数组
}

StringRep::StringRep(const StringRep& sr) {
    int len = sr.length();
    m_pChars = new char[len + 1];
    strcpy(m_pChars, sr.m_pChars);
}
```

**StringRep 和 UCObject 的关系**：`StringRep` 继承自 `UCObject`，所以"StringRep IS-A UCObject"——这意味着任何需要 `UCObject*` 的地方都可以传入 `StringRep*`。但这不是本章的重点，重要的是 StringRep 继承了引用计数能力，而**不需要写任何引用计数代码**。

---

## String —— 公共接口

`String` 类是对用户暴露的"门面"——用户使用 `String` 类，就像使用普通的字符串一样。用户不需要知道智能指针、引用计数这些底层细节。

```cpp
class String {
public:
    String(const char *s) : m_rep(new StringRep(s)) {}
    ~String() {}
    String(const String& s) : m_rep(s.m_rep) {}
    String& operator=(const String& s) {
        m_rep = s.m_rep;    // UCPointer 的赋值运算符自动处理引用计数
        return *this;
    }

    int operator==(const String& s) const {
        // m_rep-> 调用 UCPointer::operator->
        // *s.m_rep  调用 UCPointer::operator*
        return m_rep->equal(*s.m_rep);
    }

    int length() const {
        return m_rep->length();
    }

    String operator+(const String& s) const { /* ... */ }
    operator const char*() const { /* ... */ }

private:
    UCPointer<StringRep> m_rep;  // String 只持有这一个成员！
};
```

**String 的拷贝构造为什么这么简单？**

```cpp
String::String(const String& s) : m_rep(s.m_rep) {}
//        ↑只是拷贝了 UCPointer          ↑触发 UCPointer 的拷贝构造
//                                        ↑拷贝构造自动 incr()
```

`String` 只需拷贝 `m_rep`，而 `UCPointer` 的拷贝构造函数自动处理引用计数。这就是**职责分离**的威力——每一层只做自己该做的事，把其他事情委托给下层。

**String 的赋值运算符为什么更简单？**

```cpp
String& String::operator=(const String& s) {
    m_rep = s.m_rep;  // 调用 UCPointer::operator=
    return *this;     // 自动 decrement 旧对象，increment 新对象
}
```

`String` 甚至不需要自己写 `operator=`——编译器生成的默认版本就是正确的（因为 `UCPointer` 的 `operator=` 已经正确处理了所有细节）。

### String 各方法如何委托工作

```
String::length()
  → m_rep->length()        // UCPointer::operator-> 返回 StringRep*
    → StringRep::length()  // 实际计算字符串长度

String::operator==
  → m_rep->equal(*s.m_rep) // -> 进入 StringRep, * 解引用另一个 UCPointer
    → strcmp(m_pChars, ...)
```

---

## Envelope-Letter 模式

本章的设计是经典的 **Envelope-Letter**（信封-信纸）模式（也叫 Handle-Body 或 Pimpl 模式）：

```
┌─────────────┐       ┌─────────────┐       ┌──────────┐
│   String     │       │  StringRep  │       │ UCObject │
│  (信封)      │──has-a│  (信纸)     │──is-a │ (计数层) │
│  用户看到的   │       │  真正干活的  │       │          │
│  公共接口     │       │  数据存储    │       │          │
└─────────────┘       └─────────────┘       └──────────┘
```

- **String**（信封）：对用户暴露的轻量级接口，只持有一个指向 `StringRep` 的智能指针
- **StringRep**（信纸）：真正的数据和工作所在，但用户看不到
- **UCPointer**：信封和信纸之间的"自动管理胶水"

**这个模式的好处**：

1. **数据隐藏**：用户通过 `String` 接口操作，不知道 `StringRep` 的存在
2. **共享数据**：拷贝 `String` 只会增加引用计数，不会复制字符串内容（浅拷贝 + 写时复制）
3. **编译隔离**：修改 `StringRep` 不需要重新编译使用 `String` 的代码

---

## 设计评价与对比

### 优点

| 优点 | 说明 |
|------|------|
| **职责分离** | 每个类只管一件事：UCObject 管计数，UCPointer 管指针操作，StringRep 管数据，String 管接口 |
| **可复用** | UCObject 和 UCPointer 是通用的，可以用于任意类型的引用计数管理 |
| **自动化** | 引用计数完全自动，不会忘记 incr/decr |
| **类型安全** | 模板确保编译期类型检查 |

### 缺点

| 缺点 | 说明 |
|------|------|
| **性能开销** | 每次拷贝/赋值/析构都要检查并更新引用计数（虽然通常可以接受） |
| **侵入式设计** | 被管理的类必须继承自 `UCObject`——如果 `StringRep` 已经是某个继承体系的一部分，这很麻烦 |
| **不是线程安全的** | `m_refCount` 的增减没有加锁，多线程环境下会出问题 |

---

## 与 std::shared_ptr 的对比

本章中 `UCObject + UCPointer` 的组合是**侵入式**的引用计数——被管理的对象必须继承自 `UCObject`。

`std::shared_ptr` 采用**非侵入式**设计：

```
侵入式（本章方案）：
  StringRep ──继承──► UCObject (含 m_refCount)

非侵入式（std::shared_ptr）：
  shared_ptr<T> ──指向──► T 对象
         │
         └──指向──► 控制块 (ref_count, weak_count, deleter...)
```

| 对比维度 | UCObject + UCPointer | std::shared_ptr |
|----------|---------------------|-----------------|
| 是否修改被管理对象 | 是（必须继承 UCObject）| 否（对象不需要任何修改）|
| 应用范围 | 只能管理"知道自己是引用计数的"对象 | 可管理任意类型 |
| 内存开销 | 引用计数在对象内部 | 额外的控制块（通常 16 字节）|
| 线程安全 | 否 | 是（引用计数操作线程安全）|
| 支持 weak_ptr | 否 | 是 |
| 适用于 | 教学理解、特定场景优化 | 通用场景 |

**学习意义**：理解 `UCObject + UCPointer` 的设计后，使用 `std::shared_ptr` 时就能理解它背后的工作方式——"增加引用计数"、"减少引用计数"、"引用计数归零时释放"这些概念是完全一致的。

---

## 总结

智能指针的工作原理并不复杂——关键是理解引用计数的三条规则和四个类如何协作：

1. **UCObject** 管理引用计数：一个 `int` + `incr()` + `decr()`（归零时自毁）
2. **UCPointer** 自动触发计数操作：构造时 incr，析构时 decr，拷贝时 incr，赋值时正确处理新旧两个对象
3. **StringRep** 继承自 UCObject，获得"能被引用计数管理"的能力，同时专注自己真正的业务逻辑
4. **String** 持有 UCPointer<StringRep>，提供简洁的用户接口

这个设计体系体现了面向对象编程的精髓：**通过类的组合和继承，将复杂的资源管理分解为若干简单的、内聚的职责，每部分专注于一件事**。
