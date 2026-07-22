# 第8章 运算符重载

## 1. 为什么重载运算符

C++ 允许用户自定义类型像内置类型一样自然地使用运算符。这实际上是**函数调用的另一种语法形式**：

```cpp
// 不使用运算符重载
z = add(x, y);

// 使用运算符重载
z = x + y;  // 更自然、更易读
```

**好处的本质**：减少认知负担。`x + y` 比 `x.add(y)` 更直观，前提是运算符的含义符合直觉。

---

## 2. 可重载与不可重载的运算符

### 2.1 可重载的运算符

```
算术:   +   -   *   /   %   ^   &   |   ~
比较:   <   >   <=  >=  ==  !=
逻辑:   !   &&  ||
位运算: <<  >>  &=  |=  ^=
赋值:   =   +=  -=  *=  /=  %=  <<= >>=
自增减: ++  --
特殊:   ,   ->* ->  ()  []
内存:   new  delete  new[]  delete[]
```

### 2.2 不可重载的运算符

```
.    .*   ::   ?:
sizeof   typeid
static_cast   dynamic_cast   const_cast   reinterpret_cast
```

### 2.3 限制

- **不能创建新运算符**（例如不能发明 `**` 做幂运算）
- **必须保留操作数数量**（二元运算符始终是二元的）
- **必须保留优先级**（例如 `*` 始终优先于 `+`）

---

## 3. 成员函数 vs. 全局函数

### 3.1 作为成员函数

```cpp
class Integer {
public:
    Integer(int n = 0) : i(n) {}
    Integer operator+(const Integer& n) const {
        return Integer(i + n.i);  // 隐式 this 是左操作数
    }
private:
    int i;
};

Integer x(1), y(5);
x + y;  // 等价于 x.operator+(y)
```

**特点**：
- 隐式的第一个参数（`this`，左操作数）
- 可以完全访问类的私有成员
- **不对左操作数执行类型转换**

```cpp
z = x + y;   // OK: x.operator+(y)
z = x + 3;   // OK: x.operator+(Integer(3)) —— 右操作数被转换了
z = 3 + y;   // 错误！3 是 int，不是 Integer，没有 operator+
             // 编译器不会将 3 转换为 Integer 因为成员函数不对左操作数做强制转换
```

### 3.2 作为全局函数

```cpp
class Integer {
    friend Integer operator+(const Integer&, const Integer&);
private:
    int i;
};

Integer operator+(const Integer& lhs, const Integer& rhs) {
    return Integer(lhs.i + rhs.i);
}
```

**特点**：
- 两个参数都是显式的
- 可能需要对私有成员使用 `friend`（或用公有访问器）
- **对两个操作数都执行类型转换**

```cpp
z = x + y;   // OK: operator+(x, y)
z = x + 3;   // OK: operator+(x, Integer(3))
z = 3 + y;   // OK: operator+(Integer(3), y)
z = 3 + 7;   // OK: Integer(10)
```

### 3.3 选择指南

| 运算符 | 推荐形式 | 原因 |
|--------|---------|------|
| `= () [] -> ->*` | **必须是成员** | C++ 语言要求 |
| 一元运算符 (`- ! ~ ++ --`) | 成员 | 操作对象本身 |
| `+= -= *= /=` 等复合赋值 | 成员 | 修改对象自身 |
| `+ - * /` 等二元算术 | **全局** | 支持左操作数类型转换 |
| `== != < > <= >=` | **全局** | 支持左操作数类型转换 |
| `<< >>` (流) | **全局** | 左操作数是 `ostream` ，你不能修改标准库 |

---

## 4. 一元运算符

### 4.1 一元负号

```cpp
// 成员函数 — 无参数
Integer Integer::operator-() const {
    return Integer(-i);
}

z = -x;  // z.operator=(x.operator-());
```

---

## 5. 自增与自减运算符 — 前缀与后缀的区别

这是一个经典考点。`int` 参数用于区分前后缀：

```cpp
class Integer {
public:
    Integer& operator++();    // 前缀 ++x — 无参数或 int
    Integer  operator++(int); // 后缀 x++ — 有一个 int 参数（编译器传 0）
    Integer& operator--();    // 前缀
    Integer  operator--(int); // 后缀
};
```

**前缀版本**（更高效）：

```cpp
Integer& Integer::operator++() {
    *this += 1;    // 先递增
    return *this;  // 返回递增后的自己的引用
}
```

**后缀版本**（需要创建副本）：

```cpp
Integer Integer::operator++(int) {
    Integer old(*this);  // 先保存旧值（调用拷贝构造）
    ++(*this);           // 再递增（复用前缀版本!）
    return old;          // 返回旧值的副本
}
```

**为什么前缀返回引用、后缀返回值？**

- 前缀：返回递增后的对象自身，可以继续操作 `++x = 5;` 很自然
- 后缀：必须返回递增前的旧值，旧值是一个临时对象，不能返回引用

**性能建议**：用户定义的前缀运算符比后缀更高效（少一次拷贝）。对内置类型，编译器通常会优化到相同。

---

## 6. 关系运算符 — "实现一个，推导全部"

**核心策略**：只需要实现 `==` 和 `<`，其他全部用这两个推导：

```cpp
class Integer {
public:
    bool operator==(const Integer& rhs) const { return i == rhs.i; }
    bool operator<(const Integer& rhs)  const { return i < rhs.i; }

    bool operator!=(const Integer& rhs) const { return !(*this == rhs); }
    bool operator>(const Integer& rhs)  const { return rhs < *this; }
    bool operator<=(const Integer& rhs) const { return !(rhs < *this); }
    bool operator>=(const Integer& rhs) const { return !(*this < rhs); }
};
```

**逻辑关系**：
- `a != b` 等价于 `!(a == b)`
- `a > b` 等价于 `b < a`
- `a <= b` 等价于 `!(b < a)`（即 a 不小于等于 b 意味着 b 不小于 a）
- `a >= b` 等价于 `!(a < b)`

---

## 7. operator[] — 下标访问

```cpp
T& Vector::operator[](int index);
```

- **必须是成员函数**
- 通常应返回**引用**，否则 `v[10] = 45;` 无法编译（你是在给临时变量赋值）
- 如果返回指针，调用者需要写 `*v[10] = 45;`，不自然

---

## 8. 赋值运算符 operator=

```cpp
T& T::operator=(const T& rhs) {
    if (this != &rhs) {       // 1. 自赋值检查（检查地址，不是值）
        // 2. 释放旧资源
        // 3. 分配新资源并复制
    }
    return *this;              // 4. 返回 *this 以支持链式赋值
}
```

**四要素**：
1. **自赋值检查** — 防止 `a = a` 时错误释放资源
2. **必须是成员函数** — 语言要求
3. **返回 `T&`** — 支持 `a = b = c` 链式赋值
4. **参数是 `const T&`** — 避免不必要的拷贝

**拷贝构造函数 vs 赋值运算符**：

```cpp
MyType b;            // 构造
MyType a = b;        // 拷贝构造！（初始化，不是赋值）
a = b;               // 赋值（两个已存在的对象）
```

区分关键：看等号左边的对象是否刚被创建。刚创建时走拷贝构造，否则走赋值。

---

## 9. operator() — 函数对象 (Functor)

```cpp
struct F {
    void operator()(int x) const {
        std::cout << x << "\n";
    }
};

F f;
f(2);  // 调用 f.operator()(2) —— 对象像函数一样被"调用"
```

**用途**：
- 传递给 STL 算法（如 `std::sort` 的比较器）
- 状态化的回调（比普通函数指针更灵活）
- lambda 表达式本质上是语法糖，底层也是 functor

---

## 10. 用户定义的类型转换

### 10.1 单参数构造函数 — 隐式构造

```cpp
class PathName {
    string name;
public:
    PathName(const string&);  // 单参数构造 → 隐式转换
};

string abc("abc");
PathName xyz(abc);  // OK 显式
xyz = abc;          // OK 隐式: abc → PathName(abc)
```

**为什么这是问题**：隐式转换可能在你不知情的情况下发生，导致难以发现的 bug。

### 10.2 explicit 关键字 — 阻止隐式转换

```cpp
class PathName {
    string name;
public:
    explicit PathName(const string&);
};

string abc("abc");
PathName xyz(abc);  // OK 显式构造
xyz = abc;          // 编译错误！不允许隐式转换
```

**建议**：几乎所有单参数构造函数都应该加 `explicit`，除非你明确需要隐式转换。

### 10.3 转换运算符 — operator T()

```cpp
class Rational {
public:
    operator double() const {         // Rational → double
        return numerator_ / (double)denominator_;
    }
};

Rational r(1, 3);
double d = 1.3 * r;  // r 隐式转换为 double
```

- 函数名是目标类型 `T`
- 没有显式参数
- 没有返回类型（目标类型就是"返回类型"）
- 编译器自动调用

**谨慎使用**：转换运算符会导致难以追踪的隐式类型转换。替代方案是显式转换函数：

```cpp
class Rational {
    double to_double() const;  // 显式转换，调用者必须写 r.to_double()
};
```

### 10.4 类型转换歧义

如果同时存在 `C::C(T)` 构造函数和 `T::operator C()`，编译器无法选择——产生歧义错误。这是使用隐式类型转换的风险之一。

---

## 11. 重载 vs. 类型转换 — 最佳匹配规则

编译器为每个参数选择"最便宜的匹配"：

| 优先级 | 匹配类型 | 成本 |
|--------|---------|------|
| 1 | 精确匹配（包括 `T&`、`const T` 等细微调整） | 零 |
| 2 | 内置提升（如 `char→int`） | 低 |
| 3 | 内置转换（如 `int→double`） | 中 |
| 4 | 用户定义的类型转换 | 高 |

---

## 12. 指南 — 什么时候应该（不应该）重载

### 应该重载

- 算术类型（复数、矩阵、货币等）的 `+ - * /`
- 容器类型的 `[]` 下标访问
- 可比较类型的关系运算符 `== <`
- 流的 `<< >>`
- 需要类似指针行为的 `-> *`

### 不应该重载

- 运算符含义不直观（如用 `+` 做减法）
- 仅仅因为"技术上可以"
- 可能导致意外行为的运算符（`&&` `||` 重载会失去短路求值）
- 逗号运算符 `,` 除非非常清楚自己在做什么

### 核心原则

**重载运算符的唯一合理理由是让代码更易读、更易维护。如果它让代码变得令人困惑，就不要重载。**

---

## 13. 参数传递与返回值建议

| 方面 | 建议 |
|------|------|
| 只读参数 | `const T&` (内置类型除外，直接传值即可) |
| 不修改对象的运算符 | 声明为 const 成员函数 |
| 产生新对象的运算符 (`+`) | 返回值（非引用） |
| 修改左操作数的运算符 (`+=`) | 返回 `T&`（`*this`） |
| 逻辑/比较运算符 | 返回 `bool` |

---

## 本章小结

运算符重载本质上是函数调用的语法糖。关键决策是选择成员函数还是全局函数：`= () [] ->` 必须是成员；二元算术/比较推荐全局以支持对称的类型转换。`explicit` 和 `= delete` 让你精确控制什么可以用、什么不能用。重载的原则是"让代码更自然"，而不是炫耀技术。
