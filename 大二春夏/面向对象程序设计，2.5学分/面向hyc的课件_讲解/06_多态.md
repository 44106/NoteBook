# 第6章 多态

## 1. 绘图程序问题 — 为什么需要多态

假设我们要写一个绘图程序，需要绘制多种形状：Rectangle（矩形）、Circle（圆）、Ellipse（椭圆）。每种形状都有 `render()`、`move()`、`resize()` 等操作，但它们的具体实现各不相同。

**不用多态的方法**（错误示范）：

```cpp
void renderShape(void* shape, int type) {
    switch(type) {
        case RECTANGLE: /* 绘制矩形 */ break;
        case CIRCLE:    /* 绘制圆 */   break;
        case ELLIPSE:   /* 绘制椭圆 */ break;
    }
}
```

问题：
- 每添加一种新形状，就要修改所有 `switch` 语句
- 类型不安全（用 `void*` 丢失类型信息）
- 代码难以维护

**多态的解决方案**：通过基类指针/引用，统一调用派生类的方法。添加新形状时，只需要写新类，不需要修改旧代码。这体现了**开闭原则**（对扩展开放，对修改关闭）。

---

## 2. virtual 的工作原理 — vtable 与 vptr

### 2.1 概念模型

```
        Shape（形状）
        center  // 中心点
        move()
        render()    <-- virtual
        resize()    <-- virtual
           |
    +------+------+
    |             |
Rectangle     Ellipse
render()      render()
                 |
              Circle
              render()
```

**注意**：从 Ellipse 派生 Circle 可能是一个有问题的设计（一个圆是特殊的椭圆，但椭圆不是圆的一般化），课程在此仅用作教学示例。

### 2.2 内存布局：vptr 与 vtable

当一个类声明了虚函数，编译器为该类生成一个**虚函数表（vtable）**——一个函数指针数组。该类的每个对象内部会包含一个隐藏指针 **vptr**，指向本类的 vtable。

**Shape 对象的内存布局：**

```
一个 Shape 对象
+------------------+
|       vptr       | --> Shape vtable
|      center      |     [0] Shape::~Shape()
|                  |     [1] Shape::render()
|                  |     [2] Shape::resize()
+------------------+
```

**Ellipse 对象覆盖了 render()：**

```
一个 Ellipse 对象
+------------------+
|       vptr       | --> Ellipse vtable
|      center      |     [0] Ellipse::~Ellipse()
|    major_axis    |     [1] Ellipse::render()    <-- 自己的版本!
|    minor_axis    |     [2] Shape::resize()      <-- 继承的版本
+------------------+
```

**Circle 对象：**

```
一个 Circle 对象
+------------------+
|       vptr       | --> Circle vtable
|      center      |     [0] Circle::~Circle()
|    major_axis    |     [1] Circle::render()
|    minor_axis    |     [2] Circle::resize()
|      area        |     [3] Circle::radius()
+------------------+
```

**为什么这样设计？** vtable 只存一份（每个类一份），对象只存指针。这样：
- 派生类对象可以在布局上与基类兼容（基类部分在前）
- 调用虚函数时，通过 `vptr -> vtable[offset]` 实现，无论指针的静态类型是什么，调用的都是实际对象的函数

### 2.3 三个类的 vtable 对比

| 虚函数槽位 | Shape vtable | Ellipse vtable | Circle vtable |
|-----------|-------------|---------------|---------------|
| [0] dtor  | `Shape::~Shape()` | `Ellipse::~Ellipse()` | `Circle::~Circle()` |
| [1] render | `Shape::render()` | `Ellipse::render()` | `Circle::render()` |
| [2] resize | `Shape::resize()` | `Shape::resize()` | `Circle::resize()` |
| [3] radius | （不存在） | （不存在） | `Circle::radius()` |

---

## 3. 多态的两个要素

### 3.1 向上转型（Upcasting）

将派生类对象当作基类对象来使用。

```cpp
Ellipse ell(10, 20);
Shape* p = &ell;   // Ellipse* 隐式转换为 Shape*
Shape& r = ell;    // 引用同理
```

- 向上转型是安全的（派生类 "is-a" 基类）
- 不需要显式类型转换
- **但是**，通过 `p` 只能看到基类部分的接口

### 3.2 动态绑定（Dynamic Binding）

- **静态绑定**：编译器根据变量的**声明类型**决定调用哪个函数
- **动态绑定**：运行时根据对象的**实际类型**决定调用哪个函数

```cpp
void render(Shape* p) {
    p->render();  // 动态绑定: 根据 p 实际指向的对象调用对应的 render
}

Circle circ(40);
render(&circ);    // 调用 Circle::render()
```

两者缺一不可：**没有向上转型，无法用统一接口操作不同对象；没有动态绑定，调用的永远是基类版本。**

---

## 4. 对象切片（Object Slicing）

### 4.1 值赋值的危险

```cpp
Ellipse elly(20F, 40F);
Circle circ(60F);
elly = circ;        // 对象切片!
elly.render();      // Ellipse::render() 被调用!
```

发生了什么：
- `circ` 中只有属于 Ellipse 部分的数据被复制到 `elly`
- `circ` 的 `area` 成员（Circle 特有的）被**切掉（sliced off）**
- `circ` 的 vptr **不会被复制**，`elly` 的 vptr 仍然指向 Ellipse 的 vtable
- 因此 `elly.render()` 调用的是 `Ellipse::render()`，不是 `Circle::render()`

### 4.2 指针赋值的不同行为

```cpp
Ellipse* elly = new Ellipse(20F, 40F);
Circle* circ = new Circle(60F);
elly = circ;            // 指针赋值！没有切片
elly->render();          // Circle::render() 被调用!
```

- 只复制了**指针**，对象完整无缺
- `elly` 和 `circ` 指向同一 Circle 对象
- `elly->render()` 通过 vptr 找到 Circle 的 vtable，调用 `Circle::render()`
- **注意**：原来的 Ellipse 对象丢失了（内存泄漏！）

### 4.3 总结

| 操作 | 行为 | render() 调用 |
|------|------|--------------|
| `elly = circ` (值) | 切片，复制部分数据 | `Ellipse::render()` |
| `elly = circ` (指针) | 指向同一对象 | `Circle::render()` |
| `Elly& ref = circ` (引用) | 引用原对象 | `Circle::render()` |

**记忆要点**：只有通过指针或引用，多态才能正常工作。值传递会触发切片。

---

## 5. 虚析构函数 — 为什么必不可少

```cpp
Shape* p = new Ellipse(100.0F, 200.0F);
delete p;    // 如果 ~Shape() 不是 virtual，只调用 Shape::~Shape()!
```

**如果析构函数不是虚函数**：
- `delete p` 只会调用 `Shape::~Shape()`
- `Ellipse` 特有的资源（如 major_axis、minor_axis 可能关联的动态内存）不会被释放
- 造成资源泄漏，甚至是严重的内存错误

**正确的做法**：

```cpp
class Shape {
public:
    virtual ~Shape() {}  // 虚析构函数
};
```

当析构函数被声明为 virtual：
- `delete p` 时，通过 vptr 找到实际类型的析构函数
- 派生类的析构函数执行完毕后，**自动调用**基类的析构函数（析构链）
- 所有资源被正确释放

**规则**：如果一个类可能被继承，就应该将析构函数声明为 virtual。

---

## 6. 重写（Overriding）

### 6.1 基本概念

重写是指在派生类中重新定义虚函数的函数体：

```cpp
class Base {
public:
    virtual void func();
};

class Derived : public Base {
public:
    void func() override;  // 重写 Base::func()
    // C++11 的 override 关键字让编译器帮你检查是否真的重写了
};
```

### 6.2 调用基类版本

重写时可以调用基类的实现，避免代码重复：

```cpp
void Derived::func() {
    cout << "In Derived::func!";
    Base::func();  // 显式调用基类版本
}
```

这是添加新功能的常见模式：先执行扩展逻辑，再调用基类逻辑（或反过来）。

---

## 7. 协变返回类型（Covariant Return Types）

派生类重写虚函数时，可以让返回类型更具体：

```cpp
class Expr {
public:
    virtual Expr* newExpr();   // 返回 Expr*
    virtual Expr& clone();     // 返回 Expr&
    virtual Expr self();       // 返回 Expr（值类型不可以协变!）
};

class BinaryExpr : public Expr {
public:
    BinaryExpr* newExpr(); // OK: 返回指针可以协变
    BinaryExpr& clone();   // OK: 返回引用可以协变
    // BinaryExpr self();   // 错误! 值类型不能协变
};
```

**规则**：只有当返回类型是指针或引用，并且派生类的返回类型是基类返回类型的公有派生类时，协变才有效。

---

## 8. 重载与 virtual

```cpp
class Base {
public:
    virtual void func();
    virtual void func(int);
};
```

**关键规则**：如果你在派生类中重写了其中一个重载版本，**必须重写所有变体**，否则未被重写的变体会被隐藏。

```cpp
class Derived : public Base {
public:
    void func() override {   // 重写无参版本
        Base::func();
    }
    // func(int) 被隐藏了！derived.func(5) 会编译错误
};
```

**正确做法**：

```cpp
class Derived : public Base {
public:
    void func() override { Base::func(); }
    void func(int) override { /* ... */ }  // 也重写有参版本
};
```

---

## 9. 两条铁律

### 9.1 永远不要重新定义继承的非虚函数

非虚函数是**静态绑定**的。如果重新定义了，通过基类指针调用时会调用基类版本，通过派生类指针调用时会调用派生类版本——行为取决于指针类型，而不是对象类型。这会造成混乱。

```cpp
// 反例
class Base {
public:
    void show() { cout << "Base"; }   // 非虚函数
};
class Derived : public Base {
public:
    void show() { cout << "Derived"; } // 重新定义
};

Base* p = new Derived();
p->show();  // 输出 "Base"——与直觉相反!
```

### 9.2 永远不要重新定义继承的默认参数值

默认参数值也是**静态绑定**的。虚函数的动态绑定只绑定函数体，不绑定默认参数。

```cpp
class Base {
public:
    virtual void func(int x = 10) { cout << x; }
};
class Derived : public Base {
public:
    void func(int x = 20) override { cout << x; }
};

Base* p = new Derived();
p->func();  // 输出 10！默认值来自 Base，函数体来自 Derived
```

**教训**：同一个虚函数在所有派生类中使用相同的默认参数值。

---

## 10. 抽象类

### 10.1 为什么需要抽象类

- **建模**：有些概念天然是抽象的（比如"形状"），不应该被实例化
- **强制正确行为**：要求每个派生类必须实现某些方法
- **定义接口**：只规定"能做什么"，不规定"怎么做"

### 10.2 纯虚函数

```cpp
class Shape {
public:
    virtual void render() = 0;   // 纯虚函数
    virtual void resize() = 0;   // 纯虚函数
};
```

- `= 0` 表示此函数没有实现，派生类**必须**重写它
- 包含纯虚函数的类是**抽象类**，不能实例化
- 纯虚函数可以有默认实现（少见但允许），派生类仍需显式重写

### 10.3 接口 / 协议类

接口类是一种特殊的抽象类：

- 所有非静态成员函数都是纯虚函数
- 虚析构函数有空的函数体（`virtual ~CDevice() {}`）
- 没有非静态成员变量
- 可以包含静态成员

示例 —— Unix 字符设备接口：

```cpp
class CDevice {
public:
    virtual ~CDevice() {}        // 虚析构，空函数体
    virtual int read(...) = 0;   // 纯虚
    virtual int write(...) = 0;  // 纯虚
    virtual int open(...) = 0;   // 纯虚
    virtual int close(...) = 0;  // 纯虚
    virtual int ioctl(...) = 0;  // 纯虚
};
```

任何实现了这些方法的类都可以作为 CDevice 使用——这就是面向接口编程。

---

## 11. 常见错误与记忆口诀

| 常见错误 | 后果 | 正确做法 |
|---------|------|---------|
| 析构函数非 virtual | 资源泄漏 | 基类析构函数加 virtual |
| 值传递对象 | 对象切片 | 用指针或引用传递 |
| 重写非虚函数 | 行为不一致 | 不重写，或改为 virtual |
| 派生类改默认参数 | 结果与预期不符 | 保持默认参数一致 |
| 只重写部分重载函数 | 其他版本被隐藏 | 全部重写 |

**记忆口诀**：
- "指针引用才多态，值传对象会切片"
- "析构加 virtual，delete 才安全"
- "纯虚 = 0，抽象不能 new"
- "重写加 override，编译器帮你查"

---

## 本章小结

多态是面向对象编程的三大支柱之一（封装、继承、多态）。它的本质是通过基类接口操作不同的派生类对象。理解 vtable/vptr 机制能帮助你写出正确的代码：知道什么时候用指针/引用，什么时候需要虚析构函数，以及避免对象切片等常见陷阱。
