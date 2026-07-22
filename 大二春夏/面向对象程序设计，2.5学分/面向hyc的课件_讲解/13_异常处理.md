# 13 异常处理 —— 让错误处理回归优雅

## 目录

1. [为什么需要异常](#为什么需要异常)
2. [传统错误码方式的困境](#传统错误码方式的困境)
3. [异常处理的基本语法](#异常处理的基本语法)
4. [Vector operator[] 的四种设计方案](#vector-operator-的四种设计方案)
5. [异常类设计与抛出](#异常类设计与抛出)
6. [捕获异常的四种场景](#捕获异常的四种场景)
7. [异常处理器选择规则](#异常处理器选择规则)
8. [标准库异常](#标准库异常)
9. [异常与构造函数](#异常与构造函数)
10. [异常与析构函数](#异常与析构函数)
11. [最佳实践与设计准则](#最佳实践与设计准则)
12. [异常安全的代码编写](#异常安全的代码编写)
13. [总结](#总结)

---

## 为什么需要异常

C++ 的核心信条之一是"编写不当的代码不应该运行"。但在现实中，运行时错误是不可避免的：文件不存在、内存不足、网络断开、用户输入非法……

**理想的错误处理应该满足**：

1. 正常逻辑和错误处理逻辑**分离**——你阅读代码时先看到"正常情况下做什么"，再看到"出错时怎么办"
2. 错误不能被**忽略**——如果调用者忘了处理，程序应该给出明确的信号
3. 错误信息可以**传播**——一个函数可能不知道如何处理错误，但它可以把错误传给知道如何处理的调用者
4. 资源要正确**释放**——即使发生了错误，已经分配的内存、打开的文件等也应该被释放

异常机制就是为满足这些需求而设计的。

---

## 传统错误码方式的困境

考虑读取一个文件的典型流程：

```
打开文件 → 确定大小 → 分配内存 → 读入内容 → 关闭文件
```

用错误码方式实现：

```cpp
errorCodeType readFile() {
    initialize errorCode = 0;
    open the file;
    if (theFileIsOpen) {
        determine its size;
        if (gotTheFileLength) {
            allocate that much memory;
            if (gotEnoughMemory) {
                read the file into memory;
                if (readFailed) {
                    errorCode = -1;
                }
            } else {
                errorCode = -2;
            }
        } else {
            errorCode = -3;
        }
        close the file;
        if (theFileDidntClose && errorCode == 0) {
            errorCode = -4;
        }
    } else {
        errorCode = -5;
    }
    return errorCode;
}
```

**这种方式的五大问题**：

| 问题 | 说明 |
|------|------|
| 嵌套过深 | 每多一个检查就多一层缩进，逻辑被淹没 |
| 错误码信息少 | `-1` 代表什么？需要查文档 |
| 容易遗忘 | 调用者可以忽略返回值 `readFile(); // 不管成功与否` |
| 返回值被占用 | 函数不能返回"真正的结果" |
| 传播困难 | 如果调用者也不知道怎么办，需要手动向上传播 |

---

## 异常处理的基本语法

用异常机制重写读文件：

```cpp
void readFile() {
    open the file;          // 如果失败，直接 throw
    determine its size;     // 如果失败，直接 throw
    allocate memory;        // 如果失败，直接 throw
    read into memory;       // 如果失败，直接 throw
    close the file;         // 如果失败，直接 throw
}

// 调用者
try {
    readFile();
} catch (FileOpenFailed& e) {
    // 处理打开失败
} catch (SizeDeterminationFailed& e) {
    // 处理确定大小失败
} catch (MemoryAllocationFailed& e) {
    // 处理内存分配失败
} catch (ReadFailed& e) {
    // 处理读取失败
} catch (FileCloseFailed& e) {
    // 处理关闭失败
}
```

**对比**：正常逻辑是一条"直线"，所有错误处理集中在末尾。阅读代码时先看到"要做什么"，再看"失败了怎么办"。

### 三个关键字

| 关键字 | 作用 | 位置 |
|--------|------|------|
| `throw` | 抛出异常对象，将控制权转移给处理器 | 错误发生处 |
| `try` | 标记"监控区域"，其中的 throw 会被捕获 | 调用栈中任何可能有异常的地方 |
| `catch` | 捕获并处理特定类型的异常 | 紧接 try 块之后 |

---

## Vector operator[] 的四种设计方案

假设 `Vector` 是一个自定义的容器类：

```cpp
template <class T> class Vector {
private:
    T* m_elements;
    int m_size;
public:
    Vector(int size = 0) : m_size(size), m_elements(new T[size]) {}
    ~Vector() { delete[] m_elements; }
    T& operator[](int idx);
};
```

当 `idx` 越界时，`operator[]` 有四种选择：

### 选择 1：什么都不做——返回随机内存

```cpp
template <class T>
T& Vector<T>::operator[](int idx) {
    return m_elements[idx];  // 越界时访问非法内存！
}
```

**评价**：最危险。程序可能崩溃，也可能静默地返回错误数据。这是安全漏洞的常见来源。

### 选择 2：返回错误标记值

```cpp
template <class T>
T& Vector<T>::operator[](int idx) {
    if (idx < 0 || idx >= m_size) {
        static T error_marker;  // 返回一个"特殊值"
        return error_marker;
    }
    return m_elements[idx];
}
```

**评价**：问题在于——调用者怎么知道返回的是"错误标记"还是"恰好等于错误标记的正常值"？而且对于泛型 `T`，不一定有"合适的错误标记值"。另外，`error_marker` 是 static 的，多线程访问不安全。

### 选择 3：直接终止程序

```cpp
template <class T>
T& Vector<T>::operator[](int idx) {
    if (idx < 0 || idx >= m_size) {
        exit(22);  // 直接结束程序
    }
    return m_elements[idx];
}
```

**评价**：过于粗暴。`Vector` 类不知道调用者的上下文——也许越界访问是可以容忍的？也许调用者想重试？`Vector` 没有资格替调用者做"终止程序"的决定。

### 选择 4：抛出异常（最佳方案）

```cpp
template <class T>
T& Vector<T>::operator[](int idx) {
    if (idx < 0 || idx >= m_size) {
        throw VectorIndexError(idx);  // 让调用者决定怎么办
    }
    return m_elements[idx];
}
```

**评价**：`Vector` 不替调用者做决定——它只报告"发生了什么"，让调用者决定如何处理。调用者可以选择忽略（让程序终止）、处理、或者重新抛出让更上层的代码处理。

**设计原则**：底层代码（如 `Vector`）负责**检测错误并报告**，高层代码负责**决定如何响应**。异常机制就是为这种"责任分离"而设计的。

---

## 异常类设计与抛出

### 定义异常类

异常类就是一个普通的类，它的目的是携带错误信息：

```cpp
class VectorIndexError {
public:
    VectorIndexError(int v) : m_badValue(v) {}
    void diagnostic() {
        cerr << "Index " << m_badValue << " out of range!";
    }
private:
    int m_badValue;  // 记录哪个索引出错了
};
```

**设计异常类的要点**：
- 尽量简单——通常只有数据和诊断方法
- 命名要以 `Error` 或 `Exception` 结尾——一眼就知道它是异常类
- 携带足够的信息让调用者理解发生了什么

### 抛出异常

```cpp
template <class T>
T& Vector<T>::operator[](int idx) {
    if (idx < 0 || idx >= m_size) {
        throw VectorIndexError(idx);  // 创建临时对象并抛出
    }
    return m_elements[idx];
}
```

**`throw` 做了什么？**
1. 复制（或移动）异常对象到一个"安全区域"（不在栈上，不会被栈展开销毁）
2. 开始"栈展开"（stack unwinding）：沿调用链向上，逐层销毁栈上的局部对象（调用析构函数）
3. 寻找第一个匹配的 `catch` 处理器
4. 找到后将异常对象交给它

---

## 捕获异常的四种场景

### 场景 1：毫不在意（不捕获）

```cpp
int func() {
    Vector<int> v(12);
    v[3] = 5;
    int i = v[42];  // 抛出异常，程序在这里中断
    return i * 5;   // 永远不会执行到这里
}
```

如果异常一路传播到 `main()` 也没有被捕获，`std::terminate()` 会被调用，程序终止。

### 场景 2：非常关心（捕获并处理）

```cpp
void outer() {
    try {
        func();
        func2();
    } catch (VectorIndexError& e) {
        e.diagnostic();  // 打印错误信息
        // 异常到此为止，不再传播
    }
    cout << "Control continues here after exception";
}
```

### 场景 3：稍微关注（捕获后重新抛出）

```cpp
void outer2() {
    try {
        func();
    } catch (VectorIndexError& e) {
        cout << "Logging: index error occurred" << endl;
        throw;  // 重新抛出！注意：没有参数
    }
}
```

**`throw;`（无参数）vs `throw e;`（带参数）**：
- `throw;`：重新抛出**当前正在处理的同一个异常对象**，保留原始类型信息（多态仍有效）
- `throw e;`：复制 `e` 然后抛出副本。如果 `e` 是基类引用而实际对象是派生类，**会发生对象切片**（slicing）！

### 场景 4：不关心细节（捕获所有）

```cpp
void outer3() {
    try {
        outer2();
    } catch (...) {  // 三个点：捕获一切
        cout << "Something went wrong, but I don't care what.";
        // 异常到此为止
    }
}
```

**谨慎使用 `catch(...)`**：你丢失了异常的所有信息，无法判断发生了什么。通常只在"需要做清理工作后无论如何都要终止"的时候使用。

---

## 异常处理器选择规则

当一个 `catch` 块被选择时，按以下顺序匹配：

1. **精确匹配** —— 异常类型与 `catch` 参数类型完全一致
2. **基类匹配** —— 如果异常类型是 `catch` 参数类型的派生类（仅适用于引用和指针捕获）
3. **`catch(...)`** —— 捕获一切

**关键规则**：处理器按**书写顺序**依次检查！先匹配的先用。

```cpp
try {
    throw UnderflowErr();
} catch (ZeroDivideErr& e) {          // 先检查：不匹配
    // ...
} catch (MathErr& e) {                // 再检查：匹配！（UnderflowErr 继承自 MathErr）
    // 这里被执行
} catch (UnderflowErr& e) {           // 永远不会执行！已经被上面的 MathErr 捕获了
    // ...
}
```

**黄金法则**：**把更具体（派生类）的处理器放在更通用（基类）的处理器前面。**

```cpp
// 正确的顺序
try {
    // ...
} catch (UnderflowErr& e) {    // 派生类在前
    // ...
} catch (MathErr& e) {         // 基类在后
    // ...
}
```

---

## 标准库异常

C++ 标准库定义了一个异常层次结构：

```
std::exception
├── std::logic_error      （逻辑错误，可在编译时发现的逻辑问题）
│   ├── std::invalid_argument
│   ├── std::domain_error
│   ├── std::length_error
│   └── std::out_of_range
├── std::runtime_error     （运行时错误）
│   ├── std::range_error
│   ├── std::overflow_error
│   └── std::underflow_error
└── std::bad_alloc         （new 分配失败）
```

**`new` 失败时不会返回 NULL**。在标准 C++ 中，`new` 失败会抛出 `std::bad_alloc` 异常：

```cpp
void func() {
    try {
        while (true) {
            char *p = new char[10000];  // 不断分配直到失败
        }
    } catch (std::bad_alloc& e) {
        cerr << "Memory exhausted: " << e.what() << endl;
    }
}
```

**`noexcept` 规范**（C++11）：声明一个函数不抛出异常：

```cpp
void abc(int a) noexcept {  // 我承诺不抛异常
    // ...
}
```

如果在 `noexcept` 函数中抛出异常，程序会调用 `std::terminate()`。编译器可以据此做优化。

> **注意**：`noexcept` 在 C++11 中取代了旧的 `throw()` 规范。旧式的 `throw(X, Y, Z)`（指定可抛出哪些类型）在 C++17 中被完全移除。

---

## 异常与构造函数

构造函数没有返回值，所以怎么报告构造失败是一个难题。

### 问题

```cpp
class FileHandler {
    FILE* fp;
public:
    FileHandler(const char* name) {
        fp = fopen(name, "r");
        // 如果打开失败？没有返回值可以给调用者！
    }
    ~FileHandler() { if (fp) fclose(fp); }
};
```

### 解决方案：抛出异常

```cpp
class FileHandler {
    FILE* fp;
public:
    FileHandler(const char* name) {
        fp = fopen(name, "r");
        if (!fp) throw FileOpenError(name);  // 构造失败，抛异常
    }
    ~FileHandler() { fclose(fp); }
};
```

### 重要警告

**如果构造函数抛出异常，该对象的析构函数不会被调用！**

```cpp
class Dangerous {
    char* buf1;
    char* buf2;
public:
    Dangerous() {
        buf1 = new char[100];
        buf2 = new char[100];  // 假设这里抛出 bad_alloc
        // buf1 不会被释放！因为析构函数不会被调用！
    }
    ~Dangerous() {
        delete[] buf1;
        delete[] buf2;
    }
};
```

**解决方案 1**：在构造时手动清理

```cpp
Dangerous() {
    buf1 = new char[100];
    try {
        buf2 = new char[100];
    } catch (...) {
        delete[] buf1;  // 手动清理
        throw;          // 重新抛出
    }
}
```

**解决方案 2**：使用智能指针（推荐）

```cpp
class Safe {
    unique_ptr<char[]> buf1;
    unique_ptr<char[]> buf2;
public:
    Safe() : buf1(new char[100]), buf2(new char[100]) {
        // 如果 buf1 构造成功而 buf2 失败
        // buf1 的析构函数会自动被调用（因为它已经是完整构造的对象）
    }
    // 不需要手动写析构函数
};
```

### 两阶段构造（Two-phase Construction）

有时候为了更精细的控制，可以采用两阶段构造：

```cpp
class Resource {
public:
    Resource() : ptr(nullptr) {  // 第 1 阶段：安全初始化
        // 只做绝对不会失败的操作
        // 指针设为 nullptr，基本类型初始化
    }

    bool Init() {  // 第 2 阶段：可能失败的操作
        ptr = allocate();
        return ptr != nullptr;
    }
private:
    void* ptr;
};

// 使用
Resource r;
if (!r.Init()) {
    // 处理初始化失败
}
```

**缺点**：调用者需要记住调用 `Init()`，而且对象在未初始化状态可能被误用。

---

## 异常与析构函数

**绝对不要在析构函数中让异常逃逸出去！**

析构函数会在两种情况下被调用：
1. 正常情况：对象离开作用域
2. 异常情况：栈展开（stack unwinding）

如果在情况 2 中析构函数又抛出异常，C++ 会调用 `std::terminate()` 立即终止程序——因为两个异常不能同时存在。

```cpp
class BadDesign {
    ~BadDesign() {
        // 如果 close_file() 可能抛出异常...
        close_file();  // 危险！
    }
};
```

**安全的做法**：在析构函数中吞掉所有异常：

```cpp
class GoodDesign {
    ~GoodDesign() {
        try {
            close_file();  // 尝试关闭
        } catch (...) {
            // 吞掉异常，记录日志
            // 绝不！让异常从析构函数中逃逸
        }
    }
};
```

---

## 最佳实践与设计准则

### 1. 按引用捕获异常（不是按值，不是按指针）

```cpp
// ❌ 按值捕获——对象切片
catch (MathErr e) {   // 如果抛出 OverflowErr，复制时被切片为 MathErr
    e.diagnostic();   // 调用的是 MathErr::diagnostic()，不是 OverflowErr::diagnostic()！
}

// ❌ 按指针捕获——谁来 delete？
catch (Y* p) {
    // p 是谁分配的？我需要 delete 吗？不知道！
}

// ✓ 按引用捕获
catch (MathErr& e) {  // 多态正常工作，不需要 delete
    e.diagnostic();   // 实际类型的方法被调用
}
```

### 2. RAII 原则（Resource Acquisition Is Initialization）

资源获取即初始化：用对象管理资源，让析构函数自动释放。

```cpp
// ❌ 不好的写法：手动管理资源
void func() {
    File f;
    if (f.open("file.txt")) {
        try {
            // 使用 f
        } catch (...) {
            f.close();  // 容易忘记
        }
        f.close();      // 容易忘记
    }
}

// ✓ 好的写法：让析构函数自动处理
void func() {
    File f("file.txt");  // 构造时打开
    // 不管正常返回还是抛出异常，f 离开作用域时析构函数会关闭文件
    if (f.ok()) {
        // 使用 f
    }
}
```

### 3. 不要用异常做正常流程控制

```cpp
// ❌ 滥用异常
try {
    for (;;) {
        p = list.next();  // 到达末尾时抛出异常
    }
} catch (EndOfList&) { ... }

// ✓ 正常做法
while (list.hasMore()) {
    p = list.next();
}
```

### 4. 异常设计策略总结

| 准则 | 说明 |
|------|------|
| 早定策略 | 在设计初期就制定错误处理策略 |
| 避免过度 try/catch | 用 RAII 自动管理资源，而非到处 try/catch |
| 异常 ≠ 控制流 | 异常只用于真正的"异常"情况，不是 if/else 的替代品 |
| 不替调用者做决定 | 库代码应该 throw，让调用者决定是否终止 |
| 使用 noexcept | 对确定不会抛异常的主要接口加 noexcept 修饰 |
| 先执行危险操作 | 修改状态放在最后——如果危险操作失败了，状态还没改 |

---

## 异常安全的代码编写

### 问题：提款操作

```cpp
class BankAccount {
    void withdrawMoney(int amount) {
        reduceBalance(amount);   // 1. 修改状态：余额减少
        prepareCash();           // 2. 危险操作：可能失败！
        releaseCash();           // 3. 给出现金
    }
};
```

如果 `prepareCash()` 抛出异常，但余额已经扣了——用户的账户少了钱但没拿到现金！

### 解决方案：先做危险的事，再改状态

```cpp
void withdrawMoney(int amount) {
    Cash cash = prepareCash();       // 1. 先做可能失败的操作
    reduceBalance(amount);           // 2. 确认成功了再修改状态
    releaseCash(cash);               // 3. 交付
}
```

### 或使用 RAII 做自动回滚

```cpp
void withdrawMoney(int amount) {
    BalanceGuard guard(this);  // 构造时记录余额，析构时自动恢复
    reduceBalance(amount);
    Cash cash = prepareCash();
    guard.dismiss();           // 一切顺利，取消回滚
    releaseCash(cash);
}
// 如果 prepareCash() 抛异常，guard 析构时自动恢复余额
```

---

## 总结

异常处理是 C++ 中管理错误的成熟机制。它的核心价值在于：

1. **分离关注点**：正常代码和错误处理代码不再混在一起
2. **责任分离**：底层代码检测并报告错误，高层代码决定如何响应
3. **资源安全**：栈展开机制自动调用析构函数，配合 RAII 保证资源不泄漏
4. **不可忽略**：未被捕获的异常会终止程序，错误不会"悄悄溜走"

**记住**：
- 抛出异常用 `throw`，捕获用引用 `catch (T& e)`
- 派生类处理器放在基类处理器之前
- 构造函数抛异常要手动清理（或用智能指针）
- 析构函数绝不抛出异常
- 用 RAII 管理资源，用智能指针管理内存
- 异常是处理错误的，不是替代 if/else 的
