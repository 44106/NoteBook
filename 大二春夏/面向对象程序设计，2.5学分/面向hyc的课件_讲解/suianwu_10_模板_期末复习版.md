# 模板 (Template) — 期末考试复习版

> 面向"会用 + 能考试"的讲解。课件原版的 CRTP、非类型参数、模板与继承的各种组合属于进阶内容，期末大概率不考。

---

## 1. 为什么需要模板？

假设你要写一个取较大值的函数：

```cpp
// 为 int 写一个
int max_int(int a, int b) {
    return a > b ? a : b;
}

// 为 double 再写一个
double max_double(double a, double b) {
    return a > b ? a : b;
}

// 为 string 又写一个
string max_string(string a, string b) {
    return a > b ? a : b;
}
```

**问题**：代码一模一样，只是类型不同。能不能只写一遍？

### 三种方案对比

| 方案 | 代码量 | 类型安全 | 性能 |
|------|--------|---------|------|
| 复制粘贴 N 份 | N 份 | ✅ | ✅ |
| 用 `void*`（无类型） | 1 份 | ❌ 不知道存的是什么 | ✅ |
| 用公共基类 | 1 份 | ✅ | ❌ 虚函数开销 |
| **用模板** | **1 份** | **✅ 编译时检查** | **✅ 无运行时开销** |

---

## 2. 函数模板

### 基本语法

```cpp
template <class T>       // 或 template <typename T>，完全等价
T my_max(T a, T b) {
    return a > b ? a : b;
}
```

拆解：
- `template <class T>` — 声明这是一个模板，`T` 是**类型参数**（占位符）
- `T my_max(T a, T b)` — 用 `T` 来代替具体的类型
- `T` 在同一个调用中必须是**同一种类型**

### 使用

```cpp
int    x = my_max(3, 5);           // T = int
double y = my_max(3.14, 2.72);    // T = double
string s = my_max(string("ab"), string("cd"));  // T = string
```

**编译器做的事**：看到 `my_max(3, 5)`，推导出 `T = int`，自动生成一份 `int` 版本。这个过程叫**模板实例化**。

### ❌ 常见错误

```cpp
my_max(3, 5.0);  // 错误！
// T 是 int 还是 double？编译器无法推导
// 因为参数 (int, double) 类型不一致

// 解决：
my_max<double>(3, 5.0);  // 显式指定 T = double
my_max(3.0, 5.0);         // 参数类型一致
```

### 重载：普通函数和模板函数怎么选？

```cpp
void f(float i, float k) {}         // 普通函数

template <class T>
void f(T t, T u) {}                 // 模板函数

f(1.0f, 2.0f);   // → 普通函数（精确匹配优先）
f(1.0, 2.0);     // → 模板 f<double>
f(1, 2);         // → 模板 f<int>
f(1, 2.0);       // → 普通函数（模板要求 T 一致，这里 int≠double，不匹配）
```

**优先级**：普通函数（精确匹配） > 模板函数 > 普通函数（隐式转换后匹配）

---

## 3. 类模板

### 基本语法

```cpp
template <class T>
class Box {
private:
    T data;          // T 类型的成员变量
public:
    Box(T val) : data(val) {}
    T get() { return data; }
    void set(T val) { data = val; }
};

// 使用：必须指定类型！
Box<int>    b1(42);       // 装 int 的盒子
Box<string> b2("hello");  // 装 string 的盒子
Box<double> b3(3.14);     // 装 double 的盒子
```

**注意**：`Box<int>` 和 `Box<string>` 是**两个完全不同的类**，会各自生成一份代码。

### 类模板的成员函数定义在类外部

```cpp
template <class T>
class Box {
    T data;
public:
    Box(T val);     // 声明
    T get();
};

// 类外部定义：必须重复 template <class T>
// 类名必须带 <T>
template <class T>
Box<T>::Box(T val) : data(val) {}

template <class T>
T Box<T>::get() { return data; }
```

### 类模板的声明和定义都放在头文件

普通类的 `.h` 声明 + `.cpp` 定义可以分开。但**模板不行**——编译器需要看到完整的模板定义才能实例化，所以通常全部放在 `.h` 中。

---

## 4. 必考示例：自己实现一个 Vector

```cpp
template <class T>
class Vector {
private:
    T*    m_data;     // 动态数组
    int   m_size;
public:
    // 构造
    Vector(int size) : m_size(size) {
        m_data = new T[size];
    }

    // 析构
    ~Vector() { delete[] m_data; }

    // 拷贝构造（深拷贝！）
    Vector(const Vector& v) : m_size(v.m_size) {
        m_data = new T[m_size];
        for (int i = 0; i < m_size; i++)
            m_data[i] = v.m_data[i];
    }

    // [] 运算符
    T& operator[](int i) { return m_data[i]; }

    // 获取大小
    int size() const { return m_size; }
};

// 使用
Vector<int>    vi(100);
Vector<string> vs(50);
Vector<double> vd(200);

vi[0] = 42;
vs[0] = "hello";
```

---

## 5. 多个类型参数

```cpp
template <class Key, class Value>
class Pair {
    Key   first;
    Value second;
public:
    Pair(Key k, Value v) : first(k), second(v) {}
    Key   getKey()   { return first; }
    Value getValue() { return second; }
};

Pair<string, int> p1("Alice", 95);
Pair<int, double> p2(1, 3.14);
```

### 嵌套使用

```cpp
// 二维 vector
Vector<Vector<int>> matrix(10);  // 10行，每行是一个 Vector<int>

// map 的值是 list
map<string, list<int>> data;
```

---

## 6. 常见考试误区

### ❌ 误区1：模板参数类型不匹配

```cpp
template <class T>
void swap(T& a, T& b) {
    T tmp = a;
    a = b;
    b = tmp;
}

int   i = 1;
float f = 2.5;
swap(i, f);  // ❌ T 是 int 还是 float？编译失败
```

### ❌ 误区2：忘了类模板名后面的 `<T>`

```cpp
// 类外部定义成员函数
template <class T>
Vector Vector<T>::f() {}  // ❌ Vector 没有 <T>！

template <class T>
Vector<T> Vector<T>::f() {}  // ✅
```

### ❌ 误区3：模板和普通类的分离编译

```cpp
// ❌ 模板的声明在 .h，定义在 .cpp → 链接错误！
// ✅ 类模板的声明和定义都放在 .h
```

### ❌ 误区4：试图用模板"省掉所有类型"

```cpp
template <class T>
void print(T x) {
    cout << x.length();  // ❌ 如果 T 是 int，没有 .length()！
}
// 模板不是万能的——你用的操作必须是 T 类型支持的
```

---

## 7. `typename` 关键字的两种用法

```cpp
// 用法1：声明模板参数（和 class 完全等价）
template <typename T>   // 等价于 template <class T>
void f(T t) {}

// 用法2：告诉编译器"这是一个类型"（在模板内部）
template <class Container>
void f(Container& c) {
    typename Container::iterator it = c.begin();
    //  ↑ 必须写！不然编译器不知道 iterator 是类型还是变量
}
```

期末通常只考用法1。

---

## 8. 模板的特化（了解即可）

有时候对**特定类型**需要特殊处理：

```cpp
// 通用模板
template <class T>
class Compare {
public:
    bool equal(T a, T b) { return a == b; }
};

// 对 const char* 的特化
template <>
class Compare<const char*> {
public:
    bool equal(const char* a, const char* b) {
        return strcmp(a, b) == 0;
    }
};
```

---

## 9. 期末常见考题类型

### 写代码：写出 swap 函数模板

```cpp
template <class T>
void my_swap(T& a, T& b) {
    T tmp = a;
    a = b;
    b = tmp;
}
```

### 看代码写结果

```cpp
template <class T>
T add(T a, T b) { return a + b; }

int  x = add(3, 5);        // x = 8
double y = add(3.5, 2.0);  // y = 5.5
string s = add(string("ab"), string("cd"));  // s = "abcd"
```

### 判断对错

1. 模板函数可以和普通函数重载。（✅）
2. 模板的声明和定义必须放在同一个文件中。（✅ 通常如此）
3. `template <class T>` 中的 `class` 只能是类类型。（❌ 内置类型也可以）
4. `template <class T>` 和 `template <typename T>` 完全等价。（✅）
5. 类模板的成员函数定义时不需要写 `template <class T>`。（❌ 必须写）

### 找出错误

```cpp
template <class T>
T max(T a, T b) {
    if (a > b) return a;
    return b;
}

int main() {
    cout << max(3, 4.5);  // ❌ T 无法确定：int 还是 double？
}
```

---

## 10. 和"普通类 + 继承 + 多态"的对比（常考简答）

| | 模板 | 继承+虚函数 |
|------|------|------------|
| 绑定时机 | **编译时** | **运行时** |
| 性能 | ✅ 无虚函数开销 | ❌ vtable 有开销 |
| 灵活性 | ❌ 编译后类型就固定了 | ✅ 运行时动态改变 |
| 代码量 | ❌ 每种类型生成一份代码（代码膨胀） | ✅ 共用一个函数体 |
| 何时用 | 只要类型不同但操作相同 | 需要不同派生类做不同的事 |

**例子**：`vector<int>`、`vector<string>` 操作完全一样 → 用模板。  
**例子**：Shape 的 render，圆和矩形画法不同 → 用虚函数。

---

## 11. 速记表

| 考点 | 答案 |
|------|------|
| 模板本质 | 编译时生成代码（代码生成器） |
| 函数模板 | `template<class T> T f(T a);` |
| 类模板 | `template<class T> class C {};` |
| 调用时类型推导 | 自动推导（参数一致）或显式指定 `f<int>(3)` |
| 类模板声明/定义放哪 | 都放 `.h` |
| 类外定义成员 | 写两遍：`template<class T>` + `类名<T>::` |
| 模板 + 普通函数优先级 | 普通函数（精确匹配）> 模板 > 普通函数（隐式转换） |
| 最常考错误 | 类型不一致、忘了 `<T>`、声明定义分离编译 |
