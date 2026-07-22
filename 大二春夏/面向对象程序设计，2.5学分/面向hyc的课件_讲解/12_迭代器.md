# 12 迭代器 —— 算法与容器的桥梁

## 目录

1. [什么是迭代器](#什么是迭代器)
2. [为什么需要迭代器](#为什么需要迭代器)
3. [迭代器作为设计模式](#迭代器作为设计模式)
4. [find 模板函数解析](#find-模板函数解析)
5. [手把手实现一个 List 迭代器](#手把手实现一个-list-迭代器)
6. [关联类型问题与解决方案](#关联类型问题与解决方案)
7. [模板特化技术](#模板特化技术)
8. [iterator_traits 完整剖析](#iterator_traits-完整剖析)
9. [迭代器类别体系](#迭代器类别体系)
10. [标签分派技术](#标签分派技术)
11. [advance 和 distance 深入分析](#advance-和-distance-深入分析)
12. [总结](#总结)

---

## 什么是迭代器

**定义**：迭代器是一个对象，提供按顺序访问容器中元素的能力，同时隐藏容器的内部实现细节。

**核心类比**：迭代器是**指针的泛化**。你像使用指针一样使用迭代器（`*` 取值，`++` 前进），但迭代器可以适配各种不同的数据结构——数组、链表、树——而不需要关心它们内部是怎么组织的。

```cpp
// 用原生指针遍历数组
int arr[] = {1, 2, 3, 4, 5};
for (int* p = arr; p != arr + 5; ++p) {
    cout << *p << " ";
}

// 用迭代器遍历 list——写法几乎一样！
list<int> L = {1, 2, 3, 4, 5};
for (auto it = L.begin(); it != L.end(); ++it) {
    cout << *it << " ";
}
```

---

## 为什么需要迭代器

**核心问题**：如果有 N 种算法和 M 种数据结构，没有迭代器就意味着需要写 N x M 个实现。

```
没有迭代器：
  find_in_vector   find_in_list   find_in_deque   find_in_map   ...
  sort_in_vector   sort_in_list   sort_in_deque   sort_in_map   ...
  ...

有迭代器：
  find(迭代器)    ← 一份实现，适用所有容器
  sort(迭代器)    ← 一份实现，适用所有容器
  ...

实现数量：N + M（每种算法一份 + 每种容器提供迭代器）
```

**迭代器 = 一组约定好的接口**

迭代器规定了容器必须提供的操作：`*` 解引用、`++` 前进、`==` 判等。只要你的数据结构提供了这些操作，STL 的所有算法都可以直接使用它。

这是软件工程中"关注点分离"原则的经典体现：容器负责存储和组织数据，算法负责数据处理逻辑，迭代器负责让二者对话。

---

## 迭代器作为设计模式

迭代器是 GoF（Gang of Four，四人帮）23 种经典设计模式之一。

> **正式定义**："提供一种方法，可以顺序访问一个聚合对象中的各个元素，而又不需要暴露该对象的内部表示。"

**为什么需要"不暴露内部表示"？**

考虑 `list` 内部是一个链表，元素通过指针相连。如果让外部直接操作这些指针，一旦有人写错了指针赋值，整个链表结构可能被破坏。迭代器封装了遍历逻辑，用户只需要"移动到下一个"而不知道"下一个"是怎么找到的。

---

## find 模板函数解析

STL 的 `find` 算法是最能体现迭代器设计理念的例子：

```cpp
template <class InputIterator, class T>
InputIterator find(InputIterator first,
                   InputIterator last,
                   const T &value)
{
    while (first != last && *first != value)
        ++first;
    return first;
}
```

**这短短几行代码为什么强大？**

1. `first` 和 `last` 定义了查找范围（用迭代器表示，不依赖具体容器类型）
2. `*first` 解引用迭代器获取元素值
3. `++first` 将迭代器移到下一个位置
4. `first != last` 判断是否到达终点
5. 返回的仍然是迭代器——如果找到指向目标元素，如果没找到则等于 `last`

**使用示例**：

```cpp
vector<int> v = {1, 2, 3, 4, 5};
list<double> L = {1.1, 2.2, 3.3, 4.4};

// 同一个 find 模板，处理完全不同的容器类型！
auto it1 = find(v.begin(), v.end(), 3);
auto it2 = find(L.begin(), L.end(), 4.4);
```

注意迭代器的比较方式：
- 对于 `vector` 的随机访问迭代器，可以用 `<` 或 `!=`
- 对于 `list` 的双向迭代器，只能用 `!=`（因为链表元素在内存中不连续，无法比较地址大小）
- `find` 用 `!=` 正是为了兼容所有迭代器类型

---

## 手把手实现一个 List 迭代器

### 第一步：定义链表节点

```cpp
template<class T>
class ListItem {
public:
    ListItem(T val) : _value(val), _next(nullptr) {}
    T& val() { return _value; }
    ListItem* next() { return _next; }
private:
    T _value;
    ListItem<T> *_next;
};
```

### 第二步：定义链表容器（简化版）

```cpp
template<class T>
class List {
public:
    void insert_front(T val) { /* ... */ }
    void insert_end(T val) { /* ... */ }
    // 提供迭代器的入口
    ListIter<T> begin() { return ListIter<T>(_front); }
    ListIter<T> end()   { return ListIter<T>(nullptr); }
private:
    ListItem<T> *_front;
    ListItem<T> *_end;
    long _size;
};
```

### 第三步：实现迭代器类

```cpp
template<class T>
class ListIter {
    ListItem<T> *ptr;  // 内部维护一个指向节点的指针
public:
    ListIter(ListItem<T> *p = 0) : ptr(p) {}

    // 前向移动到下一个节点
    ListIter& operator++() {
        ptr = ptr->next();  // 利用链表节点的 next 指针
        return *this;
    }

    // 判断两个迭代器是否指向同一个节点
    bool operator==(const ListIter& i) const {
        return ptr == i.ptr;
    }
    bool operator!=(const ListIter& i) const {
        return ptr != i.ptr;
    }

    // 解引用：获取节点中存储的值
    T& operator*() { return ptr->val(); }

    // 箭头运算符：直接访问值的成员
    T* operator->() { return &(**this); }
};
```

**设计要点**：
- 迭代器不拥有数据——它只是数据的一个"视图"（view）
- 迭代器可以复制，复制出的迭代器独立使用
- 迭代器的 `end()` 通常用 `nullptr` 表示——这是"遍历终点"标记
- `operator->()` 的实现利用了 `operator*()`："先解引用自己，再取地址"

---

## 关联类型问题与解决方案

### 问题：我们想知道迭代器指向的类型是什么

假设要写一个函数，接受迭代器并处理其指向的值：

```cpp
template <class I>
??? func(I iter) {        // 返回类型应该是什么？
    ??? tmp = *iter;       // 局部变量应该是什么类型？
    // ...
}
```

"迭代器指向什么类型"这个信息是隐藏的——`I` 可能是 `int*`（指向 int），也可能是 `list<string>::iterator`（指向 string）。

### 第一次尝试：typedef 技巧

在迭代器类中定义一个 `value_type` typedef：

```cpp
template <class T>
struct myIter {
    typedef T value_type;  // 声明：这个迭代器指向的类型是 T
    T* ptr;
    myIter(T *p = 0) : ptr(p) {}
    T& operator*() { return *ptr; }
};

template <class I>
typename I::value_type func(I iter) {  // 从迭代器中提取类型
    return *iter;
}
```

**但这有一个致命缺陷**：原生指针（如 `int*`、`double*`）没有 `value_type` 这种内嵌类型。而原生指针也是一种合法的迭代器（用于数组遍历）。

---

## 模板特化技术

在解决上面的问题之前，需要先理解模板特化。模板特化允许为特定的模板参数提供"定制版本"的实现。

### 三种模板形式

```cpp
// 1. 主模板 (Primary Template)：通用定义
template<class T1, class T2, int I>
class A {
    // 适用于大部分情况的通用实现
};

// 2. 显式（全）特化 (Full Specialization)：为精确参数组合定制
template<>
class A<int, double, 5> {
    // 仅当 T1=int, T2=double, I=5 时使用
};

// 3. 偏特化 (Partial Specialization)：为部分参数模式定制
template<class T2>
class A<int, T2, 3> {
    // 当 T1=int, I=3，T2 为任意类型时使用
};
```

**匹配规则**：编译器优先选择最特化的版本。全特化 > 偏特化 > 主模板。

### 用偏特化解决指针问题

```cpp
// 主模板：处理一般情况（类迭代器）
template<class T>
class C {
public:
    C() { cout << "普通模板 T" << endl; }
};

// 偏特化：专门处理指针类型（T*）
template<class T>
class C<T*> {
public:
    C() { cout << "指针模板 T*" << endl; }
};

C<int>  c1;   // 输出："普通模板 T"
C<int*> c2;   // 输出："指针模板 T*"（匹配了偏特化版本）
```

---

## iterator_traits 完整剖析

**Traits 技术**是解决迭代器关联类型问题的标准方案。它的核心思想是：用一个中间层（traits 类）来提取类型信息，并通过偏特化来适配原生指针。

### 标准 iterator_traits 定义

```cpp
template<class I>
struct iterator_traits {
    // 从迭代器类内部提取类型信息
    typedef typename I::value_type        value_type;        // 指向的元素类型
    typedef typename I::difference_type   difference_type;   // 两个迭代器之间的距离类型
    typedef typename I::pointer           pointer;           // 指向元素的指针类型
    typedef typename I::reference         reference;         // 指向元素的引用类型
    typedef typename I::iterator_category iterator_category; // 迭代器类别
};
```

### 针对原生指针的偏特化

```cpp
// 非 const 指针的偏特化
template<class T>
struct iterator_traits<T*> {
    typedef T                          value_type;
    typedef ptrdiff_t                  difference_type;  // C++ 标准定义的类型
    typedef T*                         pointer;
    typedef T&                         reference;
    typedef random_access_iterator_tag iterator_category;  // 原生指针就是随机访问
};

// const 指针的偏特化
template<class T>
struct iterator_traits<const T*> {
    typedef T                          value_type;        // 注意：value_type 不是 const T！
    typedef ptrdiff_t                  difference_type;
    typedef const T*                   pointer;
    typedef const T&                   reference;
    typedef random_access_iterator_tag iterator_category;
};
```

**关键点**：`const T*` 的 `value_type` 是 `T`（不是 `const T`）。这是因为 `value_type` 表示迭代器指向的"元素的类型"，const 描述的是"通过这个迭代器能否修改元素"，而不是元素本身的类型。

### 使用 iterator_traits

```cpp
template <class I>
typename iterator_traits<I>::value_type    // 返回类型：从 traits 中提取
func(I iter) {
    typename iterator_traits<I>::value_type tmp = *iter;  // 局部变量类型
    return tmp;
}
```

现在这个函数可以处理：
- `int*`（原生指针）
- `const int*`（const 指针）
- `list<int>::iterator`（类迭代器）
- `vector<double>::iterator`（类迭代器）
- 任何定义了内嵌类型的自定义迭代器

**traits 技术的本质**：用编译时多态（模板特化）在不修改原始类型的前提下"询问"它的属性。

---

## 迭代器类别体系

不是所有迭代器的能力都相同。STL 定义了五个迭代器类别，从弱到强：

```
InputIterator  ←── 只读，单向，只能遍历一次
    |
ForwardIterator ←── 可读可写，单向，可以多次遍历
    |
BidirectionalIterator ←── 可以向前和向后移动
    |
RandomAccessIterator ←── 可以任意跳转（像指针一样）
```

另外还有 `OutputIterator`（只写，单向，只能遍历一次），通常用于输出结果。

```
    InputIterator       OutputIterator
          \                 /
        ForwardIterator
              |
      BidirectionalIterator
              |
     RandomAccessIterator
```

**继承关系也是一个层次约束**：`ForwardIterator` 满足 `InputIterator` 的所有要求（plus more），`RandomAccessIterator` 满足上面所有类别的所有要求。

**各迭代器类别支持的操作**：

| 操作 | Input | Forward | Bidi | Random |
|------|-------|---------|------|--------|
| `*it` 读 | YES | YES | YES | YES |
| `++it` | YES | YES | YES | YES |
| `it++` | YES | YES | YES | YES |
| `*it` 写 | - | YES | YES | YES |
| 多次遍历 | - | YES | YES | YES |
| `--it` | - | - | YES | YES |
| `it += n` | - | - | - | YES |
| `it - it` | - | - | - | YES |
| `it < it` | - | - | - | YES |
| `it[n]` | - | - | - | YES |

**各容器提供的迭代器**：

| 容器 | 迭代器类别 |
|------|-----------|
| `vector`, `deque`, `array` | RandomAccessIterator |
| `list`, `map`, `set` | BidirectionalIterator |
| `forward_list` | ForwardIterator |
| `istream_iterator` | InputIterator |
| `ostream_iterator` | OutputIterator |

---

## 标签分派技术

**问题**：如何让同一个函数（如 `advance`）根据不同的迭代器类型选择不同的实现？

**方案**：利用函数重载 + 类型标签（tag dispatch）。

### 第一步：定义标签类型

```cpp
struct input_iterator_tag {};
struct output_iterator_tag {};
struct forward_iterator_tag       : public input_iterator_tag {};   // 继承！
struct bidirectional_iterator_tag : public forward_iterator_tag {};
struct random_access_iterator_tag : public bidirectional_iterator_tag {};
```

**为什么用继承？**因为继承可以让"强迭代器"的标签隐式转换为"弱迭代器"的标签。例如 `random_access_iterator_tag` 可以隐式转为 `input_iterator_tag`（因为继承链）。这意味着如果一个算法只实现了 `InputIterator` 版本，`RandomAccessIterator` 也可以使用它。

### 第二步：为不同迭代器类型实现不同版本

```cpp
// 输入迭代器版本：最通用，每次走一步
template <class InputIterator, class Distance>
void __advance(InputIterator& i, Distance n, input_iterator_tag) {
    while (n--) ++i;          // 只能往前走
}

// 双向迭代器版本：可以向前或向后
template <class BidirectionalIterator, class Distance>
void __advance(BidirectionalIterator& i, Distance n,
               bidirectional_iterator_tag) {
    if (n >= 0) while (n--) ++i;
    else        while (n++) --i;
}

// 随机访问迭代器版本：最快，O(1)
template <class RandomAccessIterator, class Distance>
void __advance(RandomAccessIterator& i, Distance n,
               random_access_iterator_tag) {
    i += n;                    // 直接跳跃！
}
```

### 第三步：公共接口进行分派

```cpp
template <class Iterator, class Distance>
void advance(Iterator& i, Distance n) {
    // 创建一个临时的标签对象进行重载解析
    __advance(i, n,
        typename iterator_traits<Iterator>::iterator_category());
    //                                       ^^ 临时对象，用于选择重载版本
}
```

**工作流程**：
1. `advance(vit, 5)` 被调用，`vit` 是 `vector::iterator`
2. `iterator_traits<vector::iterator>::iterator_category` 得到 `random_access_iterator_tag`
3. 创建一个临时的 `random_access_iterator_tag()` 对象
4. 编译器选择匹配最佳的重载：`__advance(..., random_access_iterator_tag)`
5. 执行 `i += n`，一步到位

---

## advance 和 distance 深入分析

### advance：移动迭代器

三个版本的对比清楚地展示了"不同迭代器 → 不同效率"的设计：

| 迭代器类别 | 实现 | 时间复杂度 |
|-----------|------|-----------|
| InputIterator | `while (n--) ++i` | O(n) |
| BidirectionalIterator | 同上但支持负数 | O(abs(n)) |
| RandomAccessIterator | `i += n` | O(1) |

利用继承减少代码：

```cpp
// 只需要为 InputIterator 和 BidirectionalIterator 写实现
// RandomAccessIterator 另写
// ForwardIterator 怎么办？利用继承！
template <class ForwardIterator, class Distance>
void __advance(ForwardIterator& i, Distance n, forward_iterator_tag) {
    // forward_iterator_tag 继承自 input_iterator_tag
    // 所以可以隐式转换为 input_iterator_tag
    // 从而复用 InputIterator 的实现！
    __advance(i, n, input_iterator_tag());
}
```

### distance：计算两个迭代器之间的距离

```cpp
// 输入迭代器版本：只能线性扫描
template <class InputIterator>
typename iterator_traits<InputIterator>::difference_type
__distance(InputIterator first, InputIterator last, input_iterator_tag) {
    typename iterator_traits<InputIterator>::difference_type n = 0;
    while (first != last) {
        ++first; ++n;     // 一步一步走，边数边记
    }
    return n;
}

// 随机访问迭代器版本：直接做减法
template <class RandomAccessIterator>
typename iterator_traits<RandomAccessIterator>::difference_type
__distance(RandomAccessIterator first, RandomAccessIterator last,
           random_access_iterator_tag) {
    return last - first;  // O(1)，因为是连续内存
}

// 公共接口
template <class Iterator>
typename iterator_traits<Iterator>::difference_type
distance(Iterator first, Iterator last) {
    return __distance(first, last,
        typename iterator_traits<Iterator>::iterator_category());
}
```

**为什么 distance 只有两个版本？**因为 `InputIterator` 的实现已经适用于 `ForwardIterator` 和 `BidirectionalIterator`（它们都"至少"可以一步一步走）。只有 `RandomAccessIterator` 有更高效的实现。"继承链 + 只实现需要差异化的级别"是这个设计模式的核心。

---

## 总结

迭代器体系是 STL 中最精妙的设计之一。它涉及的技术栈：

```
┌──────────────────────────────────────────┐
│              算法 (Algorithms)            │
│   独立于容器，通过迭代器操作数据            │
└──────────────────┬───────────────────────┘
                   │ 使用
┌──────────────────▼───────────────────────┐
│          迭代器 (Iterators)               │
│   泛化的指针，提供统一接口                 │
└──────────────────┬───────────────────────┘
                   │ 提供迭代器类型
┌──────────────────▼───────────────────────┐
│         iterator_traits                  │
│   提取类型信息（value_type 等）           │
│   通过偏特化适配原生指针                   │
└──────────────────┬───────────────────────┘
                   │ 提取
┌──────────────────▼───────────────────────┐
│        iterator_category                 │
│   迭代器能力标签（input/bidi/random）     │
│   通过标签分派选择最优算法                  │
└──────────────────────────────────────────┘
```

**关键要点**：

1. **迭代器是泛化的指针**：用 `*` 取值，用 `++` 前进，用 `==` / `!=` 比较。任何一个支持这些操作的类型都可以作为迭代器。

2. **iterator_traits 解决"类型提取"问题**：通过模板偏特化，既支持类迭代器（内部有 `value_type` 等 typedef），也支持原生指针（`int*`、`double*` 等）。

3. **iterator_category 解决"算法选择"问题**：通过标签分派（Tag Dispatch），让编译器在编译期选择最优实现——对 `vector` 的迭代器用 O(1) 的 `i += n`，对 `list` 的迭代器用 O(n) 的逐次步进。

4. **继承优化了代码**：`forward_iterator_tag` 继承自 `input_iterator_tag`，意味着 `ForwardIterator` 可以复用 `InputIterator` 的算法实现。

5. **N + M 而非 N x M**：这是迭代器设计的核心价值——每种算法只需写一份，每种容器只需提供迭代器接口，二者通过迭代器互联。
