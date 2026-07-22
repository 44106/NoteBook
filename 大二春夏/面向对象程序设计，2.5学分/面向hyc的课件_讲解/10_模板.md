# 第10章 模板

## 1. 为什么需要模板

### 1.1 问题场景

假设你需要一个 `int` 列表和一个 `Person` 列表：

```cpp
class IntList {
    int data[100];
    int size;
public:
    void push(int);
    int pop();
};

class PersonList {
    Person data[100];  // 几乎相同的代码!
    int size;
public:
    void push(Person);
    Person pop();
};
```

这两个类唯一的区别是存储的类型不同。直觉上，我们不希望复制粘贴代码。

### 1.2 三种非模板方案及其缺陷

| 方案 | 优点 | 缺陷 |
|------|------|------|
| 复制粘贴代码 | 类型安全 | 难以管理，修改需要同步多份 |
| 公共基类 (`ListOfObject`) | 只有一份代码 | 需要设计基类，可能不自然；存取时需要向下转型 |
| 无类型列表 (`void*`) | 通用 | **类型不安全**，不知道存的是什么 |

**模板的解决方案**：用类型作为参数，让编译器生成类型安全的代码。

```cpp
template <class T>
class List {
    T data[100];
public:
    void push(const T&);
    T pop();
};

List<int> intList;       // 编译器生成 int 版本的 List
List<Person> personList; // 编译器生成 Person 版本的 List
```

---

## 2. 函数模板

### 2.1 swap 示例 — 语法走读

问题：如果想交换 `int`、`float`、`string` 等不同类型的两个值怎么办？

```cpp
template <class T>
void swap(T& x, T& y) {
    T temp = x;
    x = y;
    y = temp;
}
```

**逐行解读**：

- `template <class T>` —— 声明这是一个模板，`T` 是类型参数（`class` 在此处等价于 `typename`，表示"任意类型"）
- `void swap(T& x, T& y)` —— `T` 可以用在参数类型、返回类型、函数体中的变量声明
- `T temp = x;` —— 在模板内部，`T` 就像一个具体的类型名称一样使用

### 2.2 模板实例化

编译器根据实际调用的参数类型，自动生成具体的函数：

```cpp
int i = 3, j = 4;
swap(i, j);             // 实例化 swap<int>，T = int

float k = 4.5, m = 3.7;
swap(k, m);             // 实例化 swap<float>，T = float

std::string s("Hello"), t("World");
swap(s, t);             // 实例化 swap<std::string>，T = std::string
```

每次用新类型调用，编译器生成一份新的函数代码。这个过程叫**隐式实例化**。

---

## 3. 模板的类型匹配规则

### 3.1 精确类型匹配 — 不进行隐式转换

```cpp
swap(int, int);       // OK: T = int
swap(double, double); // OK: T = double
swap(int, double);    // 错误! T 不能同时是 int 和 double
```

**为什么 `swap(int, double)` 失败**：编译器需要为 `T` 推断一个统一的类型。`int` 和 `double` 是两个不同类型，编译器不会自动将 `int` 提升为 `double`。

即使存在从 `int` 到 `double` 的隐式转换，模板实例化也不考虑它。

### 3.2 模板与普通函数的互动 — 重载规则

```cpp
// 普通函数
void f(float i, float k) {}

// 函数模板
template <class T>
void f(T t, T u) {}

f(1.0f, 2.0f);  // 调用普通函数 f(float, float) -- 精确匹配
f(1.0, 2.0);    // 调用模板 f(double, double)
f(1, 2);        // 调用模板 f(int, int)
f(1, 2.0);      // 调用普通函数 f(float, float) -- 隐式转换
```

**选择优先级**：
1. 检查是否有精确匹配的普通函数
2. 检查是否有能精确匹配的函数模板
3. 对普通函数应用隐式类型转换

---

## 4. 显式实例化

当类型无法从参数推断时：

```cpp
template <class T>
void foo() { /* T 不出现在参数列表中 */ }

foo<int>();    // 显式指定 T = int
foo<float>();  // 显式指定 T = float
```

---

## 5. 类模板

### 5.1 Vector 示例

```cpp
template <class T>
class Vector {
public:
    Vector(int);
    ~Vector();
    Vector(const Vector&);
    Vector& operator=(const Vector&);
    T& operator[](int);
private:
    T* m_elements;
    int m_size;
};
```

**用法**：

```cpp
Vector<int> v1(100);       // int 类型的 Vector
Vector<Complex> v2(256);   // Complex 类型的 Vector
v1[20] = 10;
v2[20] = v1[20];           // OK, 如果 int 可转换为 Complex
```

### 5.2 类模板成员函数的定义语法

```cpp
template <class T>
Vector<T>::Vector(int size) : m_size(size) {
    m_elements = new T[m_size];
}

template <class T>
T& Vector<T>::operator[](int index) {
    if (index < m_size && index >= 0) {
        return m_elements[index];
    } else {
        // 越界处理...
    }
}
```

**关键点**：
- 每个成员函数前都要有 `template <class T>`
- 类名后面要跟 `<T>`，即 `Vector<T>::` 而不是 `Vector::`
- 在类内部定义成员时，`Vector` 自动表示 `Vector<T>`

---

## 6. 多类型参数与嵌套

### 6.1 多个类型参数

```cpp
template <class Key, class Value>
class HashTable {
    const Value& lookup(const Key&) const;
    void insert(const Key&, const Value&);
};
```

### 6.2 嵌套模板

模板本身产生的是类型，因此可以嵌套：

```cpp
Vector< Vector<double*> >          // Vector 的 Vector
Vector< int (*)(Vector<double>&, int) >  // 函数指针的 Vector
```

（C++11 起，`>>` 不会被误认为是右移运算符。）

---

## 7. 表达式参数 (非类型参数)

模板参数不仅可以是类型，还可以是编译期常量表达式：

```cpp
template <class T, int bounds = 100>
class FixedVector {
public:
    FixedVector();
    T& operator[](int);
private:
    T elements[bounds];  // 固定大小的数组！大小在编译时确定
};
```

**成员函数定义**：

```cpp
template <class T, int bounds>
T& FixedVector<T, bounds>::operator[](int i) {
    return elements[i];
}
```

**使用**：

```cpp
FixedVector<int, 50> v1;     // 50 个元素
FixedVector<int, 10*5> v2;   // 等价于 50 个元素 (编译器计算)
FixedVector<int> v3;         // 使用默认值 100
```

**注意事项**：
- 非类型参数必须是编译期常量
- 可以带默认值
- 不同的大小会产生不同的类型（`FixedVector<int,50>` 和 `FixedVector<int,100>` 是不同的类型）
- 可能导致代码膨胀（每种大小生成一份代码）

---

## 8. 模板与继承 — 四种组合

### 8.1 模板类继承自非模板类

```cpp
template <class A>
class Derived : public Base { ... };
```

### 8.2 模板类继承自模板类

```cpp
template <class A>
class Derived : public List<A> { ... };
```

### 8.3 非模板类继承自模板类

```cpp
class SupervisorGroup : public List<Employee*> { ... };
```

这里 `List<Employee*>` 是模板的一个具体实例化，是一个完整的类型。

### 8.4 CRTP — 奇异递归模板模式

```cpp
template <class T>
class Base {
    void interface() {
        static_cast<T*>(this)->implementation();  // 静态多态!
    }
    static void static_func() {
        T::static_sub_func();
    }
};

class Derived : public Base<Derived> {
    void implementation();          // 非虚函数
    static void static_sub_func();
};
```

**CRTP 的本质**：派生类将自己的类型传给基类模板。基类通过 `static_cast` 调用派生类的方法——这实现了**编译期多态**，没有任何 vtable 开销。

**与虚函数的对比**：

| 方面 | virtual + 继承 | CRTP |
|------|---------------|------|
| 绑定时间 | 运行时 | 编译时 |
| 开销 | vptr + 间接调用 | 零开销（内联可能） |
| 灵活性 | 可以用基类指针统一操作 | 必须在编译时知道具体类型 |
| 安全 | override 关键字辅助 | static_cast 如果不匹配是未定义行为 |

---

## 9. 模板的最佳实践

### 9.1 开发流程

1. **先写非模板版本并确保正确**
2. **建立完善的测试用例**
3. **测量性能并调优**
4. 审查：**哪些类型应该参数化？**
5. 将非参数化版本转换为模板
6. 用已有的测试用例验证

### 9.2 模板放在头文件中

由于模板在实例化时编译器需要看到完整的定义（不是只有声明），模板的定义通常**全部放在头文件中**。

```cpp
// vector.h — 模板声明和定义都在这里
template <class T>
class Vector {
    // ...
};

template <class T>
Vector<T>::Vector(int size) {
    // 定义也在这里
}
```

**为什么**：编译器在实例化模板时需要看到完整的函数体来替换类型参数。如果定义在 .cpp 中，编译调用方时看不到定义。

**编译器和链接器有处理多重定义的机制**（如 `inline` 关键字被隐式使用）。

---

## 10. 常见陷阱

| 陷阱 | 说明 |
|------|------|
| 模板在 .cpp 中 | 链接错误，找不到实例化 |
| `swap(int, double)` | 类型不精确匹配，编译失败 |
| 忘记 `<T>` | 成员函数定义少了 `Vector<T>::` |
| 代码膨胀 | 每种类型组合生成一份代码，非类型参数加剧膨胀 |
| 错误信息难读 | 模板出错时，编译器输出大量不可读信息（C++20 Concepts 可改善） |
| 循环依赖 | `Derived : public Base<Derived>` 如果写反了顺序 |

---

## 11. 完整示例：参数化排序

```cpp
template <class T>
void sort(Vector<T>& arr) {
    const size_t last = arr.size() - 1;
    for (int i = 0; i < last; i++)
        for (int j = last; j > i; j--) {
            if (arr[j] < arr[j-1]) {
                swap(arr[j], arr[j-1]);  // 调用模板 swap
            }
        }
}

Vector<int> vi(4);
vi[0] = 4; vi[1] = 3; vi[2] = 7; vi[3] = 1;
sort(vi);  // sort(Vector<int>&)

Vector<string> vs(5);
vs[0] = "Fred"; vs[1] = "Wilma"; vs[2] = "Barney";
vs[3] = "Dino"; vs[4] = "Prince";
sort(vs);  // sort(Vector<string>&)
           // 使用 operator< 比较字符串
```

---

## 本章小结

模板是 C++ 泛型编程的基石。它通过类型参数化实现"一次编写，多类型使用"，同时保持编译期类型安全。关键理解：模板实例化是**编译期**行为——编译器为每种使用的类型组合生成一份代码。函数模板强调类型精确匹配（不触发隐式转换），类模板非常适合编写容器。CRTP 提供了一种零开销的静态多态方案。最佳实践是先写非模板版本验证正确性，再转化为模板。
