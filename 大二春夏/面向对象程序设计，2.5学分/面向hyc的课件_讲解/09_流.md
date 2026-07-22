# 第9章 流

## 1. 为什么用流而不是 printf/scanf

### 1.1 C 风格 I/O 的问题

```c
int i = 42;
double d = 3.14;
printf("%d %f", i, d);  // 格式符必须与类型匹配
```

- **类型不安全**：`%d` 配 `double` 编译不报错，运行时行为未定义
- **不可扩展**：无法让 `printf` 直接输出你自定义的 `Person` 对象
- **不是面向对象**：函数式接口，无法利用多态

### 1.2 C++ 流的优势

```cpp
cout << i << " " << d;  // 编译器自动根据类型选择正确输出方式
```

- **类型安全**：编译器在编译期确定调用哪个 `operator<<`
- **可扩展**：你可以为自己的类重载 `operator<<`
- **面向对象**：输入输出流通过继承层次组织

### 1.3 流的缺点

- 语法更冗长（C++20 `std::format` 有所改善）
- 可能更慢（可通过 `ios::sync_with_stdio(false)` 优化）
- 格式化需要操纵符配合，不如 `printf` 格式串简洁

**建议**：将 C 代码转为 C++ 时，保留原有 I/O 不变通常是合理的选择。

---

## 2. 什么是流

流是一个**通用的逻辑接口**，连接程序和外部设备（控制台、文件、字符串等）。

- **一维的**：数据按顺序流动
- **单向的**：输入流只读，输出流只写
- 文件支持随机访问，但 `cin` / `cout` 不支持

### 2.1 命名约定

| 类别 | 输入 | 输出 | 头文件 |
|------|------|------|--------|
| 通用（控制台） | `istream` | `ostream` | `<iostream>` |
| 文件 | `ifstream` | `ofstream` | `<fstream>` |
| C 字符串（旧式） | `istrstream` | `ostrstream` | `<strstream>` |
| C++ 字符串 | `istringstream` | `ostringstream` | `<sstream>` |

**命名规律**：`i` 前缀 = 输入，`o` 前缀 = 输出，"string" 字样 = 字符串流，"f" 字样 = 文件流。

### 2.2 预定义流对象

| 对象 | 用途 |
|------|------|
| `cin` | 标准输入（键盘） |
| `cout` | 标准输出（屏幕） |
| `cerr` | 无缓冲错误输出（立即显示） |
| `clog` | 有缓冲错误输出（攒够再输出，性能更好） |

---

## 3. 流的核心操作

### 3.1 提取器 (Extractor, >>)

从流中读取数据：

```cpp
cin >> c;        // 读取一个字符
cin >> i;        // 读取整数（自动跳过前导空白）
cin >> f >> buffer;  // 链式读取
```

**预定义提取器参考表**：

| 目标类型 | 输入格式 | C 等价 |
|---------|---------|--------|
| `char` | 单个字符 | `%c` |
| `short, int` | 十进制整数 | `%d` |
| `long` | 长整数 | `%ld` |
| `float` | 浮点数 | `%g` |
| `double` | 双精度 | `%lg` |
| `char[]` | 字符串（遇空白停止） | `%s` |
| `void*` | 指针地址 | `%p` |

**提取器默认跳过前导空白字符**。

### 3.2 插入器 (Inserter, <<)

向流中写入数据：

```cpp
cout << "Hello" << 42 << endl;
```

**预定义插入器参考表**：

| 表达式类型 | 输出格式 | C 等价 |
|-----------|---------|--------|
| `char` | 单个字符 | `%c` |
| `short, int` | 十进制整数 | `%d` |
| `long` | 长整数 | `%ld` |
| `float` | 浮点数 | `%g` |
| `double` | 双精度 | `%lg` |
| `char[]` | 字符串 | `%s` |
| `void*` | 指针地址 | `%p` |

### 3.3 链式调用原理

```cpp
cin >> a >> b >> c;
// 等价于 ((cin >> a) >> b) >> c;
// 每次 operator>> 返回 istream&，然后继续 >> 下一位
```

---

## 4. 文本流 vs. 二进制流

| 属性 | 文本流 | 二进制流 |
|------|--------|---------|
| 数据格式 | ASCII / 可读文本 | 原始二进制数据 |
| 字符转换 | 如 `\n` → OS实际换行 | 无转换 |
| 可读性 | 人可读 | 人不可读 |
| 精度 | 浮点数可能有精度损失 | 精确保持 |

---

## 5. 自定义提取器和插入器

### 5.1 自定义提取器模板

```cpp
istream& operator>>(istream& is, T& obj) {
    // 从 is 读取 obj 的成员
    return is;  // 返回 istream& 支持链式调用
}
```

**必须满足的条件**：
- 必须是全局自由函数（两个参数）
- 第一个参数是 `istream&`
- 第二个参数是被读取对象的**引用**
- 返回 `istream&`

### 5.2 自定义插入器模板

```cpp
ostream& operator<<(ostream& os, const T& obj) {
    // 将 obj 的成员写入 os
    return os;  // 返回 ostream& 支持链式调用
}
```

**注意**：
- 第二个参数通常是 `const T&`（不修改被输出的对象）
- 必须返回 `ostream&`

---

## 6. 其他输入操作

| 操作 | 签名 | 说明 |
|------|------|------|
| `get()` | `int get()` | 读取下一个字符，返回 EOF 表示结束 |
| `get(char&)` | `istream& get(char& ch)` | 将下一个字符读入 ch |
| `get()` | `get(char* buf, int limit, char delim='\n')` | 读取最多 limit-1 字符，或遇到 delim，**不消耗分隔符** |
| `getline()` | `getline(char* buf, int limit, char delim='\n')` | 同上，但**会消耗分隔符** |
| `ignore()` | `ignore(int limit=1, int delim=EOF)` | 跳过最多 limit 个字符或直到分隔符 |
| `gcount()` | `int gcount()` | 返回上一次非格式化输入读取的字符数 |
| `putback()` | `void putback(char c)` | 将一个字符放回流中（最多回退一个） |
| `peek()` | `char peek()` | 查看下一个字符，不移除 |

**get() vs getline() 的关键区别**：分隔符是否被消耗。如果 `get()` 后紧接另一个 `get()`，第二个会立即遇到上次的分隔符。

### 6.1 代码示例

```cpp
// 复制输入到输出，字符级
int ch;
while ((ch = cin.get()) != EOF)
    cout.put(ch);

// 逐行读取
char buffer[100];
cin.getline(buffer, sizeof(buffer));
cout << "read " << cin.gcount() << " characters";

// 查看下一个字符
switch(cin.peek()) {
    case '#': /* 处理注释 */ break;
    default:  /* 正常处理 */ break;
}
```

---

## 7. 其他输出操作

| 操作 | 说明 |
|------|------|
| `put(char)` | 输出单个字符 |
| `flush()` | 强制刷新缓冲区 |

```cpp
cout.put('a');
cerr.put('!');

cout << "Enter a number: ";
cout.flush();  // 确保提示在输入前显示
```

---

## 8. 操纵符 (Manipulators)

操纵符是修改流状态的特殊函数。

### 8.1 常用操纵符

| 操纵符 | 效果 | 适用范围 |
|--------|------|---------|
| `endl` | 插入换行 + 刷新 | O |
| `flush` | 刷新流 | O |
| `dec` | 切换为十进制 | I, O |
| `hex` | 切换为十六进制 | I, O |
| `oct` | 切换为八进制 | I, O |
| `setw(int)` | 设置字段宽度（仅下一次） | I, O |
| `setfill(char)` | 设置填充字符（持久） | I, O |
| `setprecision(int)` | 设置浮点精度（持久） | O |
| `setbase(int)` | 设置进制 | O |
| `ws` | 跳过空白字符 | I |
| `setiosflags(long)` | 打开指定标志 | I, O |
| `resetiosflags(long)` | 关闭指定标志 | I, O |

**注意**：`setw` 只对下一次操作有效，其他操纵符的效果会持续。这是常见的混淆点。

```cpp
cout << setprecision(2) << 1230.243 << endl;  // 输出: 1.2e+03
cout << setw(20) << "OK!";                     // 输出: "                 OK!"
```

### 8.2 流标志

| 标志 | 设置时的效果 |
|------|------------|
| `ios::skipws` | 跳过前导空白（默认打开） |
| `ios::left` | 左对齐 |
| `ios::right` | 右对齐 |
| `ios::internal` | 符号和数值之间填充 |
| `ios::dec` `ios::oct` `ios::hex` | 控制进制 |
| `ios::showbase` | 显示进制前缀（0x, 0） |
| `ios::showpoint` | 始终显示小数点 |
| `ios::uppercase` | 十六进制前缀大写（0X） |
| `ios::showpos` | 正数前显示 `+` |
| `ios::scientific` | 科学计数法 |
| `ios::fixed` | 定点表示 |
| `ios::unitbuf` | 每次写入后刷新 |

**设置方法**：

```cpp
// 方法1: 操纵符
cout << setiosflags(ios::showbase | ios::uppercase);

// 方法2: 成员函数
cout.setf(ios::showbase);
cout.unsetf(ios::showbase);
```

---

## 9. 自定义操纵符

### 9.1 无参数操纵符

```cpp
// 框架
ostream& manip(ostream& out) {
    // 修改 out 的状态
    return out;
}

// 示例: tab 操纵符
ostream& tab(ostream& out) {
    return out << '\t';
}

cout << "Hello" << tab << "World!" << endl;
// 输出: Hello    World!
```

**为什么能工作**：流类重载了 `operator<<`，接受 `ostream& (*)(ostream&)` 类型的函数指针，当传入这种函数时自动调用。

---

## 10. 常见模式与陷阱

| 模式/陷阱 | 说明 |
|----------|------|
| `cin >> n` 残留换行 | 之后用 `cin.getline()` 会读到空行，用 `cin.ignore()` 清除 |
| 类型不匹配 | `cin >> i` 输入 "abc"，流进入错误状态，后续所有读取失败 |
| 检查输入成功 | `if (cin >> i)` —— 流对象可隐式转换为 bool |
| 混合 C/C++ I/O | 需要 `sync_with_stdio` 或可能乱序 |

---

## 本章小结

流是 C++ 面向对象 I/O 的核心概念。它通过运算符重载实现了类型安全和可扩展的输入输出。提取器 (`>>`) 和插入器 (`<<`) 可以为你自己的类型自定义。操纵符让你灵活控制格式化。理解 `get()`/`getline()` 的区别、标志的持久性、以及 `setw` 的一次性特征，能帮你避免常见的 I/O 陷阱。
