# 05 组合与继承

> has-a 与 is-a —— 代码复用的两种基本方式（第五篇自学笔记）

---

## 1. 代码复用的两种哲学

写程序不可能从零开始。C++ 提供两种复用已有代码的方式：

| 方式 | 关系 | 含义 | 类比 |
|------|------|------|------|
| 组合 (Composition) | **has-a** | 新类中包含已有类的对象作为成员 | 汽车**有**引擎 |
| 继承 (Inheritance) | **is-a** | 新类是已有类的特殊化 | 经理**是**员工 |

选择组合还是继承，是 OOP 设计中最基本的决策之一。**判断标准很简单**：问自己"新类和旧类之间的关系是 has-a 还是 is-a？"

---

## 2. 组合 (Composition)：用零件组装新对象

### 2.1 什么是组合？

```cpp
class Person { ... };
class Currency { ... };

class SavingsAccount {
public:
    SavingsAccount(const char* name, const char* address, int cents);
    ~SavingsAccount();
    void print();
private:
    Person m_saver;      // SavingsAccount "有一个" Person
    Currency m_balance;  // SavingsAccount "有一个" Currency
};
```

`SavingsAccount` 通过包含 `Person` 和 `Currency` 对象来复用它们的功能。这不是在说"储蓄账户是一种人"，而是在说"储蓄账户有一个人作为持有者"。

### 2.2 两种包含方式

| 方式 | 图示 | 存储位置 | 生命周期 | 共享性 |
|------|------|----------|----------|--------|
| **完全包含** (by value) | `Person m_saver;` | 直接存储在对象内部 | 与包含者一致 | 不可共享 |
| **按引用包含** (by reference) | `Person* m_saver;` 或 `Person& m_saver;` | 存储的是指针/引用 | 独立于包含者 | 可以共享 |

```cpp
// 完全包含
class Car {
    Engine engine;     // Engine 对象直接嵌入在 Car 中
    Tyre tyres[4];
};

// 按引用包含
class Employee {
    Person* supervisor; // supervisor 指向另一个 Employee 对象的 Person 部分
    // 多个 Employee 可能共享同一个 supervisor
};
```

### 2.3 内嵌对象的初始化：必须用初始化列表

这是组合使用中最重要的技术细节：

```cpp
SavingsAccount::SavingsAccount(
    const char* name, const char* address, int cents)
    : m_saver(name, address),    // 这里调用 Person 的构造函数
      m_balance(0, cents)         // 这里调用 Currency 的构造函数
{
    // 构造函数体为空——所有工作都在初始化列表中完成
}
```

**如果你不在初始化列表中提供参数会怎样？**

```cpp
// BAD —— 低效的做法
SavingsAccount::SavingsAccount(
    const char* name, const char* address, int cents)
{
    m_saver.set_name(name);       // set_name 不是构造函数
    m_saver.set_address(address);
    m_balance.set_cents(cents);
}
```

这段代码的**真实执行顺序**：
1. 进入构造函数体之前，`m_saver` 被默认构造（调用 `Person()`）
2. 进入构造函数体之前，`m_balance` 被默认构造（调用 `Currency()`）
3. 在构造函数体内，调用 `set_name`、`set_address`、`set_cents` 重新设置

如果 `Person` 没有默认构造函数，这段代码直接编译失败。即使有，也多做了无意义的默认构造 → 赋值的过程。

**正确做法**：始终在初始化列表中直接构造内嵌对象。

### 2.4 public vs private 内嵌对象

```cpp
// 通常：private —— 内嵌对象是实现细节
class SavingsAccount {
private:
    Person m_saver;  // 外部代码不能直接访问 m_saver
    // 只能通过 SavingsAccount 的方法间接操作
};

// 偶尔：public —— 希望把内嵌对象的接口暴露出去
class SavingsAccount {
public:
    Person m_saver;  // 外部可以直接访问
};

SavingsAccount account;
account.m_saver.set_name("Fred");  // 跨过 SavingsAccount 直接操作 Person
```

**为什么通常用 private？** 封装原则。`m_saver` 作为实现细节，其接口可能不适合直接暴露。如果以后 `SavingsAccount` 的内部实现变了（比如不再用 `Person` 而改用 `CustomerProfile`），public 嵌入会导致大量外部代码需要修改。

---

## 3. 继承 (Inheritance)：克隆并增强

### 3.1 什么是继承？

用课件的话：**继承是将现有类克隆，然后在克隆体上添加和修改。**

```cpp
// 基类：Employee
class Employee {
public:
    Employee(const std::string& name, const std::string& ssn);
    const std::string& get_name() const;
    void print(std::ostream& out) const;
    void print(std::ostream& out, const std::string& msg) const;
protected:
    std::string m_name;
    std::string m_ssn;
};

// 派生类：Manager —— "是一种" Employee，但增加了 title
class Manager : public Employee {
public:
    Manager(const std::string& name,
            const std::string& ssn,
            const std::string& title);
    const std::string title_name() const;
    const std::string& get_title() const;
    void print(std::ostream& out) const;  // 重写了基类的 print
private:
    std::string m_title;  // Manager 专属的额外数据
};
```

Manager **继承了** Employee 的所有成员（数据和方法），然后添加了自己的 `m_title` 和几个新方法。

### 3.2 术语对照

课件中列出了继承关系的多种称呼：

| 被继承的类 | 继承得到的类 |
|-----------|-------------|
| Base class 基类 | Derived class 派生类 |
| Super class 父类 | Sub class 子类 |
| Parent class 父类 | Child class 子类 |

本课程主要使用 **基类 (Base)** 和 **派生类 (Derived)**。

### 3.3 Employee → Manager 完整示例

**构造函数**：

```cpp
Manager::Manager(const string& name,
                 const string& ssn,
                 const string& title = "")
    : Employee(name, ssn),    // 在初始化列表中调用基类构造函数
      m_title(title)           // 初始化自己的成员
{
}
```

注意：基类的构造由基类名（而非成员名）在初始化列表中调用。这和处理内嵌对象的方式非常相似——**将继承的特征视为一个内嵌对象**。

**成员函数**：

```cpp
// 重写基类的 print
inline void Manager::print(std::ostream& out) const
{
    Employee::print(out);     // 调用基类的 print
    out << m_title << endl;   // 打印 Manager 独有的信息
}

// 新功能
inline const std::string& Manager::get_title() const
{
    return m_title;
}

inline const std::string Manager::title_name() const
{
    return string(m_title + ": " + m_name);  // 可以访问基类的 m_name
}
```

**使用**：

```cpp
int main() {
    Employee bob("Bob Jones", "555-44-0000");
    Manager bill("Bill Smith", "666-55-1234", "ImportantPerson");

    string name = bill.get_name();    // OK：Manager 继承了 Employee 的 get_name()
    // string title = bob.get_title(); // 错误！bob 是 Employee，没有 get_title()

    bob.print(cout);                  // 调用 Employee::print
    bill.print(cout);                 // 调用 Manager::print（重写版本）

    bob.print(cout, "Employee:");     // OK：两个参数的 print
    // bill.print(cout, "Employee:"); // 错误！被隐藏了（见下一节）
}
```

---

## 4. 构造与析构顺序

**构造函数调用顺序**：**基类总是在派生类之前被构造。**

```cpp
Manager bill("Bill", "666-55", "VIP");

// 实际的构造顺序：
// 1. Employee 部分先构造（基类）
// 2. m_title 构造（派生类的成员）
// 3. Manager 构造函数体执行
```

**析构函数调用顺序**：**与构造函数严格相反。**

```cpp
// 当 bill 离开作用域时：
// 1. Manager 析构函数体执行
// 2. m_title 析构
// 3. Employee 部分析构（基类）
```

**为什么是这个顺序？** 派生类依赖基类——Manager 的方法可能使用 Employee 的数据。如果基类先析构，派生类的方法还在运行时基类的数据已经不存在了——灾难。所以基类必须后析构。

如果不在初始化列表中显式调用基类构造函数，编译器会尝试调用基类的默认构造函数：

```cpp
Manager::Manager(...)    // 如果没写 : Employee(...)
// 编译器会尝试调用 Employee() —— 如果不存在则编译错误
```

---

## 5. 名称隐藏 (Name Hiding)

这是 C++ 中一个微妙但重要的规则：

**如果在派生类中重新定义了一个成员函数，基类中同名的所有重载函数都将不可访问。**

```cpp
class Employee {
public:
    void print(ostream& out) const;                      // 版本 1
    void print(ostream& out, const string& msg) const;   // 版本 2（重载）
};

class Manager : public Employee {
public:
    void print(ostream& out) const;  // 重新定义了 print
};

Manager bill(...);
bill.print(cout);                     // OK，调用 Manager::print
bill.print(cout, "Employee:");        // 错误！Employee::print(out, msg) 被隐藏了！
```

**为什么 C++ 这样设计？** 这是为了防止派生类意外地继承到不合适的重载版本。如果你觉得基类的某个函数不适合派生类，你只需要重写同名函数，所有重载版本全部消失。这让你可以完全控制派生类的接口。

**如何恢复被隐藏的函数？** 用 `using` 声明：

```cpp
class Manager : public Employee {
public:
    using Employee::print;            // 将基类所有 print 重载引入派生类
    void print(ostream& out) const;   // 然后覆盖你需要的那个版本
};
```

---

## 6. 访问保护：三道防线

### 6.1 成员访问级别

| 访问级别 | 谁能访问 | 典型用途 |
|----------|----------|----------|
| `public` | 所有人 | 类的公开接口 |
| `protected` | 本类、派生类、友元 | "对子类公开，对外界隐藏" |
| `private` | 仅本类和友元 | 实现细节，连子类都不让看 |

```cpp
class Employee {
public:
    const string& get_name() const;   // 任何人都能获取姓名
protected:
    string m_name;                     // 派生类（如 Manager）可以直接访问
private:
    string m_ssn;                      // 连 Manager 都不能直接访问！只能通过公共接口
};
```

### 6.2 继承类型：双重控制

继承时指定的访问修饰符（`public`/`protected`/`private`）会**降级**基类成员在派生类中的访问级别：

| 基类成员是... | `:public A` | `:protected A` | `:private A` |
|--------------|-------------|----------------|--------------|
| `public` | → public | → protected | → private |
| `protected` | → protected | → protected | → private |
| `private` | → private (不可访问) | → private (不可访问) | → private (不可访问) |

**解读这张表**：

- **public 继承**（最常用）：基类的 public 成员在派生类中仍然是 public，protected 仍然是 protected ——"is-a"关系的最自然表达。
- **protected 继承**：基类的 public 成员在派生类中降级为 protected。外部不能通过派生类访问这些成员，但派生类的子类可以。
- **private 继承**：基类的一切在派生类中都变成 private。外部不能访问，派生类的子类也不能。这实际上是用继承实现了"has-a"关系（一种比组合更隐晦的方式，不推荐）。

### 6.3 默认访问级别：class vs struct

| | `class` | `struct` |
|------|---------|----------|
| 成员默认访问 | `private` | `public` |
| 继承默认访问 | `private` | `public` |

```cpp
class A { int x; };     // x 是 private
struct B { int x; };    // x 是 public

class D1 : A { };       // private 继承（等同于 : private A）
struct D2 : A { };      // public 继承（等同于 : public A）
```

> **约定**：`struct` 通常只用于纯数据聚合（类似 C 的 struct），有行为的类型用 `class`。

---

## 7. friend：访问控制的特例

```cpp
class MyClass {
private:
    int secret;
    friend void globalFunc(MyClass& m);   // 全局函数是友元
    friend class OtherClass;              // OtherClass 的所有成员函数都是友元
    friend void OtherClass::oneMethod();  // 只授权 OtherClass 的一个特定方法
};

void globalFunc(MyClass& m) {
    cout << m.secret;  // OK——友元可以访问 private 成员
}
```

**关于 friend 的原则**：
- "友元"是**被授予的**，不是索取的——类自己声明谁是它的朋友，外部代码不能单方面宣称自己是某类的朋友。
- friend 打破了封装，应当谨慎使用。最常见的合理场景是运算符重载（如 `operator<<` 需要访问私有成员）。

---

## 8. 向上转型 (Upcasting) 与里氏替换原则

### 8.1 什么是向上转型？

**向上转型**是将派生类的指针或引用转换为基类的指针或引用。

```cpp
Manager pete("Pete", "444-55-6666", "Bakery");
Employee* ep = &pete;   // Manager* → Employee*：向上转型（安全，隐式）
Employee& er = pete;     // Manager& → Employee&：向上转型（安全，隐式）
```

"向上"是因为在继承图中，基类在顶部，派生类在底部：

```
      Employee   (基类，上方)
         ^
         |
      Manager    (派生类，下方)
```

**向上转型总是安全和隐式的**——每个 Manager 都是一个 Employee，编译器确认这一点。`ep` 可以用来访问 `Employee` 中定义的所有接口（`get_name()`, `print()`）。

### 8.2 类型信息的丢失

```cpp
ep->print(cout);  // 调用的是 Employee::print()，不是 Manager::print()！
```

通过基类指针调用非虚函数时，调用的是**基类的版本**——即使指针实际指向的是 Manager 对象。调用哪个函数由**指针的静态类型**决定，而不是由指向的对象的实际类型。

这引出一个问题：如何在基类指针上调用派生类特有的方法？

```cpp
string title = bill.get_title();        // OK，bill 是 Manager 类型
// string title = ep->get_title();      // 错误！ep 是 Employee*，看不到 get_title()
```

关于虚函数（`virtual`）和多态的解决方案——这是第 6 章《多态》的内容。

### 8.3 里氏替换原则 (Liskov Substitution Principle)

> **如果 S 是 T 的子类型，那么程序中所有使用 T 类型对象的地方，都可以用 S 类型的对象替换，而不改变程序的正确性。**

简单说：**如果 B is-a A，那么在任何需要 A 的地方，你都可以使用 B。**

这是 OOP 设计的基石原则。如果某个"is-a"关系不满足这个原则，说明这个继承关系是错的。

```
"正方形是一种矩形" —— 对吗？
数学上对，但编程中可能有陷阱：
- Rectangle::setWidth(w) 和 Rectangle::setHeight(h) 对矩形是独立的
- 但对正方形，设置宽度必须同时改变高度
- 如果 Rectangle 的用户调用 setWidth 后期待高度不变，用 Square 替换就会出问题
- 这说明"Square is-a Rectangle"在编程中需要仔细设计（或者根本不是 is-a）
```

---

## 9. 组合 vs 继承：选择指南

| 考量 | 组合 | 继承 |
|------|------|------|
| 关系 | "has-a" | "is-a" |
| 耦合度 | 较低（只通过接口交互） | 较高（派生类依赖基类实现） |
| 灵活性 | 高（可以在运行时更换组件） | 低（编译期就固定了继承关系） |
| 代码量 | 需要写转发函数 | 自动获得基类的接口 |
| 访问控制 | 可以完全控制暴露哪些接口 | 基类的 public 接口自动成为派生类的一部分 |
| 何时用 | "X 有 Y"、"X 使用 Y" | "X 是 Y 的一种" |

> **优先使用组合而非继承** —— 这是 OOP 设计中的常见建议。继承是强大的工具，但也是"最紧密的耦合"。除非确实存在清晰的 is-a 关系，否则考虑用组合。

---

## 10. 本章要点总结

1. **组合**表达 has-a 关系（用已有对象构建新对象），**继承**表达 is-a 关系（克隆并增强已有的类）。
2. **内嵌对象必须在初始化列表中构造**，否则编译器会尝试调用默认构造函数（低效甚至不可能）。
3. **构造顺序**：基类 → 派生类成员 → 派生类构造函数体。析构严格相反。
4. **名称隐藏**：派生类重定义同名函数会隐藏基类中该名字的**所有重载版本**。可用 `using` 恢复。
5. **访问保护**在成员级别（public/protected/private）和继承级别（public/protected/private 继承）都有作用。
6. **`class` 默认 private，`struct` 默认 public** —— 这是两者唯一的语法区别。
7. **friend** 由类主动授予，允许特定外部函数/类访问私有成员。
8. **向上转型**（派生类 → 基类）总是安全且隐式的。通过基类指针调用非虚函数时调用的是基类版本。
9. **里氏替换原则**：如果 B is-a A，那么任何使用 A 的地方都可以使用 B。

---

*上一篇：[04 对象交互](04_对象交互.md)*
*下一篇：[06 多态](06_多态.md) —— virtual 关键字、虚函数表与运行时多态*
