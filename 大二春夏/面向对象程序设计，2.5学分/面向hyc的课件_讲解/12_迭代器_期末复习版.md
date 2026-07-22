# 迭代器 (Iterator) — 期末考试复习版

> 面向"会用 + 能考试"的讲解。课件原版的 traits / 偏特化 / 标签分派属于模板元编程，期末大概率不考。

---

## 1. 迭代器是什么？

**一句话：迭代器就是"泛化的指针"。**

它提供了一个**统一的遍历方式**，不管底层是数组、链表还是树，遍历代码都一样。

```cpp
// 指针版本 — 只能遍历数组
int arr[] = {1, 2, 3, 4, 5};
for (int* p = arr; p != arr + 5; ++p) {
    cout << *p << endl;
}

// 迭代器版本 — 同样的写法，什么容器都能遍历
vector<int> v = {1, 2, 3, 4, 5};
for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
    cout << *it << endl;
}
```

对比指针 `int*` 和迭代器 `vector<int>::iterator`：

| 指针操作 | 迭代器操作 | 含义 |
|---------|-----------|------|
| `p = arr` | `it = v.begin()` | 指向第一个元素 |
| `p != arr + 5` | `it != v.end()` | 判断是否到达末尾 |
| `*p` | `*it` | 访问当前元素 |
| `++p` | `++it` | 移动到下一个元素 |

---

## 2. 为什么要用迭代器？

**把算法和容器分离开。**

```cpp
// 同一个 find 函数，适用于所有容器
list<int>   L;
vector<int> V;
string      S;

find(L.begin(), L.end(), 3);  // 在 list 中找
find(V.begin(), V.end(), 3);  // 在 vector 中找
find(S.begin(), S.end(), 'a'); // 在 string 中找

// find 的实现：
template <class Iterator, class T>
Iterator find(Iterator first, Iterator last, const T& value) {
    while (first != last) {
        if (*first == value) return first;
        ++first;
    }
    return last;  // 没找到，返回 end()
}
```

如果**没有迭代器**：N 种容器 × M 种算法 = 要写 N×M 份代码。  
**有了迭代器**：只用写 M 份算法 + N 套迭代器 = N+M 份代码。

---

## 3. 迭代器的基本操作（必考）

每个容器都提供：

| 方法 | 返回 | 含义 |
|------|------|------|
| `c.begin()` | 迭代器 | 指向第一个元素 |
| `c.end()` | 迭代器 | 指向**最后一个元素的下一个位置**（哨兵） |
| `c.rbegin()` | 反向迭代器 | 指向最后一个元素 |
| `c.rend()` | 反向迭代器 | 指向第一个元素的前一个位置 |

```cpp
vector<int> v = {10, 20, 30, 40};

// begin 和 end
v.begin()  // → 指向 10
v.end()    // → 指向 40 之后的位置（不能解引用！）

// 正向遍历
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";  // 输出：10 20 30 40
}

// 反向遍历
for (auto it = v.rbegin(); it != v.rend(); ++it) {
    cout << *it << " ";  // 输出：40 30 20 10
}
```

### ⚠️ end() 不能解引用！

```cpp
auto it = v.end();
cout << *it;  // ❌ 未定义行为！end() 不指向任何元素
```

---

## 4. 五种迭代器类别（常考选择题）

不同容器提供的迭代器**能力不同**，按能力从弱到强：

```
输入迭代器 (Input)
    ↓ 能 ++，只能读，单遍遍历
前向迭代器 (Forward)  
    ↓ 能 ++，可读写，多遍遍历
双向迭代器 (Bidirectional)
    ↓ 能 ++ 和 --
随机访问迭代器 (Random Access)
    ↓ 能 ++, --, +n, -n, []
```

| 容器 | 迭代器类别 | 支持的操作 |
|------|-----------|-----------|
| `vector`, `deque`, `array`, `string` | **随机访问** | `++`, `--`, `+n`, `-n`, `[]`, `<`, `>`, `<=`, `>=` |
| `list`, `set`, `map`, `multiset`, `multimap` | **双向** | `++`, `--` |
| `forward_list`, `unordered_set`, `unordered_map` | **前向** | 只能 `++` |

### 这意味着什么？

```cpp
vector<int> v = {1, 2, 3, 4, 5};
auto vit = v.begin();
vit = vit + 3;   // ✅ vector 是随机访问，可以直接跳
cout << vit[0];  // ✅ 等价于 *vit

list<int> l = {1, 2, 3, 4, 5};
auto lit = l.begin();
lit = lit + 3;   // ❌ list 是双向迭代器，不支持 +n！
lit++; lit++; lit++;  // ✅ 只能一步步走
```

---

## 5. 遍历容器的四种写法（必考）

```cpp
vector<int> v = {1, 2, 3, 4, 5};

// 写法1：传统迭代器
for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}

// 写法2：auto 简化
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}

// 写法3：范围 for 循环（C++11，最推荐）
for (int x : v) {
    cout << x << " ";
}
// 本质就是写法2的语法糖

// 写法4：用引用修改元素
for (int& x : v) {
    x *= 2;  // 修改 v 中的每个元素
}
```

### 什么时候不能用范围 for？

当你需要在遍历中**删除元素**时：

```cpp
// ❌ 范围 for 中删除元素 — 未定义行为
for (int x : v) {
    if (x == 3) v.erase(???);  // 没有迭代器，无法安全删除
}

// ✅ 用迭代器
for (auto it = v.begin(); it != v.end(); ) {
    if (*it == 3)
        it = v.erase(it);  // erase 返回下一个有效迭代器
    else
        ++it;
}
```

---

## 6. map 的迭代器（特殊，常考）

`map` 的迭代器指向的是 `pair<const Key, Value>`：

```cpp
map<string, int> scores;
scores["Alice"] = 95;
scores["Bob"] = 87;

for (auto it = scores.begin(); it != scores.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
    //       ↑ 键              ↑ 值
}

// 范围 for 版本
for (const auto& p : scores) {
    cout << p.first << ": " << p.second << endl;
}

// C++17 结构化绑定
for (const auto& [name, score] : scores) {
    cout << name << ": " << score << endl;
}
```

---

## 7. 迭代器失效（期末高频考点！）

**在遍历容器的同时修改容器，迭代器可能失效。**

### vector 的迭代器失效

```cpp
vector<int> v = {1, 2, 3, 4, 5};

// ❌ 错误示范
for (auto it = v.begin(); it != v.end(); ++it) {
    if (*it == 3) {
        v.erase(it);  // it 失效了！后面的 ++it 是未定义行为
    }
}

// ✅ 正确示范：用 erase 的返回值更新 it
for (auto it = v.begin(); it != v.end(); ) {
    if (*it == 3) {
        it = v.erase(it);  // erase 返回被删元素之后的有效迭代器
    } else {
        ++it;
    }
}
```

### 什么操作会导致 vector 迭代器失效？

| 操作 | 后果 |
|------|------|
| `push_back` | 如果触发了扩容（capacity 不够），**所有**迭代器失效 |
| `pop_back` | 只有指向最后一个元素的迭代器失效 |
| `erase` | 被删元素及之后**所有**迭代器失效 |
| `insert` | 插入点及之后**所有**迭代器失效（可能触发扩容） |
| `clear` | 所有迭代器失效 |

### list 的迭代器比较稳定

```cpp
list<int> l = {1, 2, 3, 4, 5};
auto it = l.begin();
++it; ++it;  // it 指向 3

l.push_front(0);  // it 仍然有效！list 不会整体移动
l.erase(l.begin());  // it 仍然有效！list 只影响被删的那个节点
```

`list` 只在**删除 it 指向的那个节点本身**时才导致 it 失效。

---

## 8. 常用 STL 算法 + 迭代器

```cpp
vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

// 查找
auto it = find(v.begin(), v.end(), 5);
if (it != v.end()) cout << "找到了：" << *it;

// 排序
sort(v.begin(), v.end());  // 要求随机访问迭代器！
// sort(l.begin(), l.end());  // ❌ list 是双向迭代器，不能用 sort！

// 正确：list 有自己的 sort
list<int> l = {3, 1, 4, 1, 5};
l.sort();  // ✅

// 计数
int cnt = count(v.begin(), v.end(), 1);  // 数有多少个 1

// 反转
reverse(v.begin(), v.end());

// 查找最大值
auto maxIt = max_element(v.begin(), v.end());
```

---

## 9. begin() 和 end() 的惯用写法

```cpp
vector<int> v = {1, 2, 3};

// 老式写法
vector<int>::iterator it = v.begin();

// 现代写法
auto it = v.begin();

// 如果需要只读，用 const_iterator
auto cit = v.cbegin();  // const_iterator
auto cend = v.cend();

// 对 const 容器，begin() 返回 const_iterator
const vector<int>& cv = v;
auto it2 = cv.begin();  // 类型是 const_iterator
```

---

## 10. 期末常见考题类型

### 判断对错

1. `v.end()` 指向最后一个元素。（❌ 指向最后一个元素的**下一个位置**）
2. 所有容器的迭代器都支持 `it + n`。（❌ 只有随机访问迭代器支持）
3. `list<int>::iterator` 可以执行 `--it`。（✅ list 是双向迭代器）
4. 在 `vector` 的 `push_back` 后，之前获取的迭代器一定有效。（❌ 扩容时会失效）
5. 范围 for 循环内部不能删除元素。（✅ 没有迭代器来安全定位）

### 看代码写结果

```cpp
vector<int> v = {10, 20, 30, 40};
auto it = v.begin();
++it; ++it;
v.insert(it, 25);
// v 现在是什么？ [10, 20, 25, 30, 40]
// 此时 it 是什么状态？ 失效了！
```

```cpp
list<int> l = {1, 2, 3, 4};
auto it = l.begin();
++it;  // 指向 2
l.erase(it);
++it;  // ❌ it 失效了！
```

---

## 11. 速记表

| 考点 | 答案 |
|------|------|
| 迭代器本质 | 泛化的指针 |
| `begin()` | 第一个元素 |
| `end()` | 最后一个元素的下一个位置 |
| `vector` 迭代器类型 | 随机访问 |
| `list` 迭代器类型 | 双向 |
| vector 什么时候迭代器全失效 | 扩容（push_back 触发）或 realloc |
| list erase 后其他迭代器 | 只有被删的那个失效，其他都有效 |
| map 迭代器指向什么 | `pair<const Key, Value>` |
| 遍历时删除元素 | `it = c.erase(it);` |
| 范围 for 的本质 | 迭代器的语法糖 |
| `auto` 推导迭代器 | ✅ 可以，`auto it = v.begin()` |
