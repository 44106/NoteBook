# 11 STL —— 标准模板库

## 目录

1. [什么是 STL](#什么是-stl)
2. [为什么要使用 STL](#为什么要使用-stl)
3. [STL 三大组成部分](#stl-三大组成部分)
4. [三大核心数据结构](#三大核心数据结构)
5. [所有顺序容器概览](#所有顺序容器概览)
6. [vector 深度解析](#vector-深度解析)
7. [list 深度解析](#list-深度解析)
8. [map 深度解析](#map-深度解析)
9. [算法 (Algorithms)](#算法-algorithms)
10. [typedef 与类型简化](#typedef-与类型简化)
11. [自定义类与 STL](#自定义类与-stl)
12. [常见陷阱与解决方案](#常见陷阱与解决方案)
13. [其他数据结构](#其他数据结构)
14. [总结](#总结)

---

## 什么是 STL

STL（Standard Template Library，标准模板库）是 ISO C++ 标准库的核心组成部分。它由 Alexander Stepanov 等人设计，为 C++ 提供了一套通用、高效的数据结构和算法。

**核心思想：泛型编程 (Generic Programming)**

STL 的设计哲学是"将数据与操作分离"——容器负责存储数据，算法负责处理数据，迭代器负责连接二者。这样，一个算法就可以应用于多种容器，一种容器也可以使用多种算法。

> Alexander Stepanov 的著作《从数学到泛型编程》(*From Mathematics to Generic Programming*) 深入阐述了 STL 背后的数学思想和设计理念。STL 不是简单的"工具集"，而是有着深厚理论基础的编程范式。

---

## 为什么要使用 STL

| 优势 | 说明 |
|------|------|
| **减少开发时间** | 数据结构已经编写、测试、优化完毕。你不需要自己实现 `vector`、`list`、`map` 等基础结构 |
| **代码可读性** | 使用 `std::vector<int>` 比手写动态数组更能表达意图；一页代码能容纳更有意义的内容 |
| **健壮性** | STL 容器能自动管理内存和容量增长，避免了许多手动内存管理的陷阱 |
| **可移植性** | STL 是 C++ 标准的一部分，代码可以在任何符合标准的编译器上编译运行 |
| **可维护性** | 标准化的接口意味着团队中的每个人都理解代码 |
| **性能可靠** | STL 的实现经过了数十年的优化，性能通常优于你手写的替代方案 |

**为什么标准库中的代码通常比自己写的更好？**

因为标准库的实现者需要考虑：所有可能的模板参数类型、异常安全、内存分配策略、不同平台下的行为一致性。这些问题自己实现时很容易忽略。

---

## STL 三大组成部分

```
┌──────────────────────────────────────────────────┐
│                     STL                          │
│                                                  │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│   │ 容器      │◄──►│ 迭代器    │◄──►│ 算法      │  │
│   │Containers│    │Iterators │    │Algorithms│  │
│   └──────────┘    └──────────┘    └──────────┘  │
│   存储数据         连接容器与算法   处理数据       │
└──────────────────────────────────────────────────┘
```

1. **容器 (Containers)**：存储数据的对象。如 `vector`、`list`、`map`、`set` 等。每种容器有自己的内存布局和访问特性。
2. **算法 (Algorithms)**：操作数据的函数模板。如 `sort`、`find`、`copy`、`for_each` 等。算法不直接操作容器，而是通过迭代器间接操作。
3. **迭代器 (Iterators)**：泛化的指针，提供统一的方式遍历容器元素，屏蔽容器的内部实现差异。

这三个组件相互配合，使得 STL 极其灵活——你可以用同一种算法处理完全不同的容器，也可以为自定义容器提供迭代器从而使用 STL 算法。

---

## 三大核心数据结构

### map —— 关联数组

- 存储"键-值对"（key-value pair）
- 键是唯一的，值通过键来查找
- 内部通常用红黑树实现，元素按 key 排序
- 应用场景：电话簿（姓名→号码）、词典（单词→释义）、缓存（请求→响应）

### vector —— 动态数组

- 像 C 数组一样连续存储，但可以自动扩展
- 支持随机访问（通过下标，O(1)）
- 在末尾添加/删除元素最高效（均摊 O(1)）
- 在中间插入/删除较慢（需要移动元素，O(n)）
- 应用场景：数值列表、待办事项、序列数据

### list —— 双向链表

- 元素在内存中不连续，每个元素有指向前后元素的指针
- 不支持随机访问，但任意位置的插入/删除是 O(1)
- 可以从两端高效操作
- 应用场景：频繁插入/删除的场景、需要双向遍历的场景

**如何选择？**

| 需求 | 选择 |
|------|------|
| 通过下标随机访问 | `vector` |
| 频繁在末尾添加/删除 | `vector` |
| 频繁在头部添加/删除 | `list` 或 `deque` |
| 频繁在中间插入/删除 | `list` |
| 按键查找 | `map` |
| 只关心是否"存在"某个元素 | `set` |

---

## 所有顺序容器概览

| 容器 | 底层结构 | 特点 |
|------|---------|------|
| `vector` | 动态数组 | 连续存储，支持随机访问，末尾操作快 |
| `deque` | 分段数组 | 连续存储的"块"，两端都可以快速操作 |
| `list` | 双向链表 | 不连续存储，任意位置插入/删除 O(1) |
| `forward_list` | 单向链表 | 只能向前遍历，内存开销更小 |
| `array` | 固定大小数组 | 大小在编译时确定，无动态内存分配 |
| `string` | 字符数组 | 本质是 `basic_string<char>`，专为字符操作优化 |

**为什么需要不同类型的容器？**

不同类型的容器代表不同的"时空权衡"：`vector` 用连续内存换取高效的随机访问；`list` 用额外的指针开销换取高效的插入/删除。没有一种容器在所有场景下都是最优的——选择容器就是在选择适合当前场景的权衡方案。

---

## vector 深度解析

### 构造函数

```cpp
vector<int> v1;           // 空 vector，大小为 0
vector<int> v2(10);       // 10 个元素，值默认初始化为 0
vector<int> v3(10, 42);   // 10 个元素，每个值为 42
vector<int> v4(v3);       // 拷贝构造，v4 是 v3 的副本
vector<int> v5 = {1,2,3}; // 初始化列表（C++11）
```

**底层发生了什么？**当你创建 `vector<int>(10)` 时，`vector` 会调用 `new` 分配一块连续内存（至少能容纳 10 个 `int`），然后在这块内存上构造 10 个 `int`（值为 0）。

### 大小与容量

```cpp
v.size();      // 当前元素个数
v.capacity();  // 当前分配的内存能容纳多少个元素
v.empty();     // 相当于 v.size() == 0，但语义更清晰
v.resize(20);  // 改变元素个数，可能触发内存重新分配
v.reserve(50); // 预留容量，避免将来添加元素时重新分配
```

**size vs capacity 的重要区别**：

- `size()` 是实际存了多少元素
- `capacity()` 是已经分配了多大空间

当 `push_back` 时如果 `size() == capacity()`，vector 会分配一块更大的内存（通常是原来的 2 倍），将旧元素拷贝过去，然后释放旧内存。这就是为什么 `reserve()` 可以优化性能——如果提前知道会有 1000 个元素，调用 `reserve(1000)` 可以避免多次重新分配。

### 迭代器

```cpp
vector<int> v = {10, 20, 30, 40, 50};

v.begin();   // 指向第一个元素的迭代器
v.end();     // 指向最后一个元素之后的位置（不是最后一个元素！）

// 遍历
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";   // 解引用获取元素值
}

// vector 的迭代器是"随机访问迭代器"，支持算术运算
auto it = v.begin();
it += 3;      // 前进 3 个位置，指向 40
cout << *it;  // 输出 40
```

**记忆技巧**：`end()` 不是最后一个元素——它像一个"哨兵"，标记遍历的终点。区间 `[begin(), end())` 是"左闭右开"的，这是 STL 中的通用约定。

### 元素访问

```cpp
vector<int> v = {10, 20, 30};

v[1];       // 返回第 2 个元素：20。不检查边界！
v.at(1);    // 返回第 2 个元素：20。如果越界抛出 std::out_of_range 异常
v.front();  // 返回第 1 个元素：10
v.back();   // 返回第 3 个元素：30
```

**`operator[]` vs `at()`**：`[]` 不检查边界（速度更快但危险），`at()` 会检查边界（安全但有微小开销）。在已经确认索引合法的情况下用 `[]`，在索引来自用户输入或计算时用 `at()`。

### 添加与删除

```cpp
vector<int> v;

v.push_back(10);   // 在末尾添加元素
v.push_back(20);
v.pop_back();      // 删除末尾元素，v 变为 [10]

v.insert(v.begin(), 5);       // 在开头插入 5，v 变为 [5, 10]
v.insert(v.begin() + 1, 7);  // 在第二个位置插入 7，v 变为 [5, 7, 10]

v.erase(v.begin());           // 删除第一个元素，v 变为 [7, 10]
v.erase(v.begin(), v.end());  // 删除全部，等价于 v.clear()
v.clear();                    // 删除所有元素
```

**注意**：`insert` 和 `erase` 在 vector 中开销较大——除了末尾的操作，其他位置都需要移动元素。

---

## list 深度解析

`list` 是双向链表，与 `vector` 的根本区别在于内存布局：

```
vector 的内存布局（连续）：
[10][20][30][40][50]  ← 一块连续内存

list 的内存布局（链式）：
[prev|10|next] → [prev|20|next] → [prev|30|next] → ...
```

### list 独有的操作

```cpp
list<int> L;

L.push_front(5);    // vector 没有这个方法！在头部添加
L.pop_front();      // vector 没有这个方法！删除头部

L.remove(10);       // 删除所有值为 10 的元素（vector 需要 find + erase）
L.sort();           // list 有自己的 sort（因为算法 std::sort 需要随机访问迭代器）

// list 的迭代器是"双向迭代器"，不能做 it += 3 这样的操作
// 只能 it++ 或 it--，每次移动一步
```

### vector 和 list 的迭代器差异

```cpp
vector<int> v = {1, 2, 3, 4, 5};
list<int>   L = {1, 2, 3, 4, 5};

// vector：随机访问迭代器
auto vit = v.begin();
vit = vit + 3;    // OK，一次跳 3 步
if (vit < v.end()) // OK，可以比较大小

// list：双向迭代器
auto lit = L.begin();
// lit = lit + 3;  // 错误！不支持随机访问
++lit; ++lit; ++lit;  // OK，每次走一步
if (lit != L.end())   // OK，可以判等
// if (lit < L.end()) // 错误！不能比较大小（因为元素不连续，内存无顺序关系）
```

**重要区别总结**：

| 特性 | vector | list |
|------|--------|------|
| 随机访问 | O(1) | 不支持 |
| 头插/头删 | O(n) | O(1) |
| 尾插/尾删 | O(1) 均摊 | O(1) |
| 中间插入 | O(n) | O(1) |
| 内存连续性 | 连续 | 分散 |
| 迭代器失效 | 重新分配时全部失效 | 只失效被删除的元素 |
| 缓存友好 | 是 | 否 |

---

## map 深度解析

### 基本用法

```cpp
#include <map>
#include <string>
using namespace std;

map<string, float> price;      // 键类型：string，值类型：float

price["snapple"] = 0.75;       // 如果 "snapple" 不存在，创建并赋值为 0.75
price["coke"] = 0.50;
price["water"] = 1.00;

cout << price["coke"];         // 输出 0.50

// 遍历 map
for (auto& pair : price) {
    cout << pair.first << " costs $" << pair.second << endl;
}
// 注意：map 中的元素按键排序，输出顺序是 "coke" → "snapple" → "water"
```

**map 为什么是排序的？**因为 map 内部通常用红黑树（一种自平衡二叉搜索树）实现，插入时自动按 key 排序。这保证了查找、插入、删除都是 O(log n)。

### operator[] 的陷阱

```cpp
map<string, int> m;
m["bob"] = 42;     // 插入键 "bob"，值 42

// 危险操作：
if (m["alice"] == 1) {   // "alice" 不存在！
    // operator[] 会自动创建 "alice" 并赋默认值 0
    // 这个条件不成立，但 m 中已经多了一个条目！
}

// 安全操作：
if (m.count("alice")) {          // C++98：返回 0 或 1
    // 只有键存在时才进入
}
if (m.contains("alice")) {       // C++20：返回 bool，语义更清晰
    // 只有键存在时才进入
}

// 查找而不插入：
auto it = m.find("alice");
if (it != m.end()) {
    cout << it->second;  // 找到了，安全使用
}
```

**为什么 `operator[]` 有这样的行为？**因为 `operator[]` 返回的是值的引用。如果键不存在，它必须创建一个默认值才能返回有效引用。想要只查询不插入时，请使用 `find()`、`count()` 或 `contains()`。

### map 的遍历

```cpp
map<string, int> m = {{"a", 1}, {"c", 3}, {"b", 2}};

// 方法一：C++11 范围 for
for (const auto& [key, value] : m) {  // 结构化绑定 C++17
    cout << key << ": " << value << endl;
}

// 方法二：传统迭代器
for (auto it = m.begin(); it != m.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
}
// 输出顺序：a:1, b:2, c:3（按 key 排序）
```

---

## 算法 (Algorithms)

STL 算法是与容器无关的函数模板，通过迭代器间接操作数据。

```cpp
#include <algorithm>
#include <vector>
#include <list>

// find：在任意容器中查找值
list<int> L = {1, 2, 3, 4, 5};
auto it = find(L.begin(), L.end(), 3);  // 返回指向 3 的迭代器
if (it != L.end()) {
    cout << "找到: " << *it;
}

// copy：在容器之间复制元素
vector<int> v(5);                        // 目标容器必须有足够的空间！
copy(L.begin(), L.end(), v.begin());

// sort：排序（需要随机访问迭代器，所以不能直接用于 list）
vector<int> nums = {3, 1, 4, 1, 5, 9};
sort(nums.begin(), nums.end());          // 升序：[1, 1, 3, 4, 5, 9]
sort(nums.begin(), nums.end(), greater<int>()); // 降序

// for_each：对每个元素执行操作
for_each(nums.begin(), nums.end(), [](int n) { cout << n << " "; });

// count：计数
int ones = count(nums.begin(), nums.end(), 1);  // 统计 1 的个数
```

**注意 copy 的要点**：`copy` 不会自动扩展目标容器，目标必须有足够的空间。如果目标是空的 vector，可以用 `back_inserter`：

```cpp
vector<int> v;
copy(L.begin(), L.end(), back_inserter(v));  // 自动在 v 末尾追加
```

---

## typedef 与类型简化

STL 类型名可能非常长，尤其是在嵌套容器中：

```cpp
// 难读、难写
map<string, list<pair<int, double>>> complexType;
map<string, list<pair<int, double>>>::iterator it;

// 使用 typedef 简化
typedef map<string, list<pair<int, double>>> MyMap;
MyMap complexType;
MyMap::iterator it;

// C++11 提供了更强大的工具
using MyMap = map<string, list<pair<int, double>>>;  // using 别名（推荐）
auto it = complexType.begin();  // auto 自动推导类型
```

**为什么推荐 `using` 而不是 `typedef`？**因为 `using` 语法更直观（`新名 = 旧类型`），而且 `using` 支持模板别名：

```cpp
template<typename T>
using StringMap = map<string, T>;  // typedef 做不到这一点！

StringMap<int> m1;     // 等价于 map<string, int>
StringMap<double> m2;  // 等价于 map<string, double>
```

---

## 自定义类与 STL

### 放入容器的最低要求

STL 容器需要对其元素进行复制和赋值操作，所以你的类至少需要：

1. **默认构造函数**——容器初始化元素时需要
2. **拷贝构造函数**——元素被复制时需要
3. **赋值运算符** `operator=`——重新赋值时需要

对于 vector 等还需要**可析构性**（通常编译器会自动生成）。

```cpp
class Person {
public:
    Person() : name(""), age(0) {}          // 默认构造（必须）
    Person(const Person&) = default;         // 拷贝构造（编译器生成即可）
    Person& operator=(const Person&) = default; // 赋值运算符
private:
    string name;
    int age;
};
vector<Person> people;  // OK
```

### 有序容器的额外要求

`map`、`set`、`multimap`、`multiset` 等有序容器需要对元素进行排序比较，所以还需要：

**`operator<`（小于运算符）**

```cpp
class Student {
public:
    string name;
    int id;

    // map<Student, ...> 需要这个
    bool operator<(const Student& other) const {
        return id < other.id;  // 按 id 排序
        // 或者：return name < other.name;  // 按姓名排序
    }
};

map<Student, double> grades;  // OK，现在 Student 可以排序了
```

**注意**：`int`、`char`、`string` 等内置类型有默认的比较运算符，但 `char*` 没有——它比较的是指针地址，不是字符串内容。如果你用 `char*` 作为 key，需要提供自定义比较器：

```cpp
struct CStringLess {
    bool operator()(const char* a, const char* b) const {
        return strcmp(a, b) < 0;
    }
};
map<const char*, int, CStringLess> phonebook;  // 第三个模板参数指定比较器
```

---

## 常见陷阱与解决方案

### 陷阱 1：访问无效的 vector 元素

```cpp
vector<int> v;
v[100] = 1;   // ❌ v 是空的，v[100] 访问的是垃圾内存！
```

**原因**：`operator[]` 不检查边界，也不自动扩展 vector——它假设你访问的元素已经存在。

**解决方案**：

```cpp
// 方法 1：用 push_back 添加
v.push_back(1);

// 方法 2：预先分配大小
vector<int> v(101);
v[100] = 1;  // OK

// 方法 3：用 resize 改变大小
vector<int> v;
v.resize(101);
v[100] = 1;  // OK

// 方法 4：用 at() 自动检测越界
v.at(100) = 1;  // 抛出 std::out_of_range 异常，提醒你 bug 存在
```

### 陷阱 2：不经意地向 map 中插入元素

```cpp
map<string, int> foo;
if (foo["bob"] == 1) { ... }  // ❌ "bob" 被悄然插入，值为 0！
```

**正确做法**：

```cpp
// C++98/03：使用 count()
if (foo.count("bob")) { ... }

// C++20：使用 contains()（语义更清晰）
if (foo.contains("bob")) { ... }

// 需要同时检查存在性和获取值：使用 find()
auto it = foo.find("bob");
if (it != foo.end()) {
    int val = it->second;  // 使用值
}
```

### 陷阱 3：在 list 上用 size() 而不是 empty()

```cpp
if (my_list.size() == 0) { ... }  // ❌ 在某些实现中可能很慢

if (my_list.empty()) { ... }      // ✓ 总是 O(1)
```

**原因**：在 C++11 之前，`list::size()` 在某些编译器中是 O(n) 的（需要遍历整个链表来计数）。C++11 标准要求 `size()` 为 O(1)，但 `empty()` 的语义更清晰——它表达的是"检查是否为空"，而不是"获取大小再比较"。

### 陷阱 4：使用已失效的迭代器

```cpp
list<int> L = {1, 2, 3, 4, 5};
auto it = L.begin();

L.erase(it);  // it 指向的元素已被删除，it 已经"失效"
++it;         // ❌ 未定义行为！
```

**正确做法**：使用 `erase` 的返回值，它指向被删除元素的下一个元素：

```cpp
auto it = L.begin();
it = L.erase(it);  // it 现在指向原来的第二个元素（现在的第一个）
// 安全地继续使用 it
```

**迭代器失效规则概览**：

| 容器 | 操作 | 失效的迭代器 |
|------|------|-------------|
| vector | push_back（导致重新分配）| 全部失效 |
| vector | insert / erase | 插入/删除点及之后的迭代器 |
| list | insert | 无迭代器失效 |
| list | erase | 仅被删除元素的迭代器失效 |
| map | insert | 无迭代器失效 |
| map | erase | 仅被删除元素的迭代器失效 |

---

## 其他数据结构

除了三大核心容器，STL 还提供了丰富的其他数据结构：

| 数据结构 | 用途 | 特点 |
|----------|------|------|
| `set` | 不重复元素的集合 | 元素自动排序，插入/查找 O(log n) |
| `multiset` | 可重复元素的集合 | 允许重复元素，自动排序 |
| `multimap` | 键可重复的 map | 一个 key 可以对应多个 value |
| `stack` | LIFO 栈 | push/pop/top，底层默认用 deque |
| `queue` | FIFO 队列 | push/pop/front/back，底层默认用 deque |
| `priority_queue` | 优先队列 | 每次取最大/最小元素，底层用堆 |
| `deque` | 双端队列 | 两端都可以快速插入/删除 |
| `bitset` | 位集合 | 固定大小，位操作高效 |
| `valarray` | 数值数组 | 面向数值计算优化，支持元素级数学运算 |

**选择指南速查**：

- 需要键值映射且键唯一 → `map`
- 需要键值映射但键可重复 → `multimap`
- 需要元素唯一且自动排序 → `set`
- 需要元素自动排序但可重复 → `multiset`
- 需要后进先出 → `stack`
- 需要先进先出 → `queue`
- 需要按优先级出队 → `priority_queue`

---

## 总结

STL 是 C++ 最强大的特性之一。它的核心思想——将容器、算法、迭代器三者解耦——极大地提高了代码的复用性和表达力。

记住这几点：

1. **选用合适的容器**：根据访问模式（随机访问 vs 顺序访问）、插入/删除频率和位置来选择
2. **理解迭代器语义**：不同容器提供不同能力的迭代器，算法也对迭代器有不同要求
3. **警惕常见陷阱**：map 的 `operator[]` 会插入元素、list 用 `empty()` 而不是 `size()==0`、操作删除后迭代器会失效
4. **善用现代 C++**：用 `auto` 简化类型、用 `using` 代替 `typedef`、用 `contains()` 检查键存在性
