# C++ OOP 期末最后主观题练习

> 题目版：不含完整参考答案。整体保持略高于常规 PTA 的训练难度。建议先独立写代码，再对照“验收输出”“强化测试”和“评分点”自查。

## 一、真题画像

从 `agvpqnsa.pdf`、`q0kzhai2.pdf`、`tools/c04zkz5a.md` 和 PTA 复习题看，最后一道主观题大致有四种形式：

1. **固定裁判主函数 + 类层次 + 多态判定**
   - 代表：PTA `6-2 表彰优秀学生（多态）`。
   - 常考：基类指针数组、派生类构造、虚函数 `display()`、静态成员保存全局信息、按输入顺序输出。
   - 难度：20 分左右，题面看似只考继承，实际会考“主函数不可改时如何保存全局获奖线”。

2. **类设计 + 模板/资源管理**
   - 代表：泛型循环队列 `CQueue<T>`。
   - 常考：模板类、动态数组、构造/析构、异常 `overflow_error` / `underflow_error`、下标回绕、成员函数补全。
   - 难度：35 分左右，代码量较大，容易在边界条件扣分。

3. **抽象基类 + 多态 + 文件/流解析**
   - 代表：`shape` 抽象基类，`Rectangle` / `Circle` / `Ellipse` 从文件解析属性，`CShapeDocument` 保存 `vector<shape*>` 并统一 `draw()`。
   - 常考：纯虚函数、虚析构、派生类 override、`ifstream` 读取、容器保存基类指针、模板辅助函数。
   - 难度：20 分左右，重点是接口对齐和输出格式。

4. **设计模式骨架补全**
   - 代表：Online Support Chat System，职责链模式。
   - 常考：抽象接口、继承、多态、基类默认转发逻辑、链式 `SetNext()` 返回值、字符串分类处理。
   - 难度：20 分左右，题面会给出部分代码，要求补全缺失类。

公开网络上能找到相近的**设计模式样例和语言点资料**，但没有找到与这些真题在题面、评分和输出上完全同构的公开考试题。因此下面题目主要按真题形式自编，考点参考公开资料与课件。

参考资料：

- Chain of Responsibility pattern: https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
- Composite pattern: https://en.wikipedia.org/wiki/Composite_pattern
- C++ virtual functions: https://learn.microsoft.com/en-us/cpp/cpp/virtual-functions
- C++ templates: https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29

## 二、建议挑战顺序

| 顺序 | 题目 | 训练重点 | 建议用时 |
|---:|---|---|---:|
| 1 | RingBuffer Template | 模板、动态数组、异常、深拷贝 | 40 min |
| 2 | Shape Drawing Script | 多态解析、文件流、输出格式 | 30 min |
| 3 | 表彰优秀学生（强化） | 固定主函数、多态、静态成员、全局判定、边界并列 | 35 min |
| 4 | Document Import System | 职责链模式骨架、抽象接口、转发逻辑 | 25 min |
| 5 | Media Library | 工厂式创建、容器保存基类指针、虚析构 | 30 min |
| 6 | Logger Chain | 职责链复盘、枚举分类、多态转发 | 25 min |

做题策略：按“隐藏测试”标准完成，而不是只过样例。主观题最常见扣分点不是思路不会，而是函数签名、`public` 继承、虚析构、静态成员定义、输出空格换行、临界比例这些小处没对齐。

---

## 练习题 1：表彰优秀学生（多态 + 静态成员，强化版，20 分）

学期结束，班主任决定表彰一批学生。学生分三类：

- `GroupA`：普通生，有 2 门课程成绩。
- `GroupB`：特招运动员，有 2 门课程成绩和 1 次运动会表现分，表现分为 `A`、`B`、`C`、`D`。
- `GroupC`：学科专长生，有 5 门课程成绩，人数不超过 5 人。

表彰人员至少符合以下条件之一：

1. 普通生和特招运动员中，2 门课程平均分名列第一者。该最高平均分称为**获奖线**。如果并列第一，全部表彰。
2. 学科专长生 5 门课程平均分达到或超过获奖线的 90%，给予表彰。
3. 特招运动员 2 门课程平均分达到或超过获奖线的 70%，且运动会表现分为 `A`，给予表彰。

输入格式：

- 每行第 1 项为类型：`1` 普通生，`2` 特招运动员，`3` 学科专长生，`0` 表示结束。
- 第 2 项是学号，第 3 项是姓名。
- 普通生共 5 项：类型、学号、姓名、2 门成绩。
- 特招运动员共 6 项：类型、学号、姓名、2 门成绩、表现等级。
- 学科专长生共 8 项：类型、学号、姓名、5 门成绩。

输出格式：打印要表彰学生的学号和姓名，顺序与输入顺序一致。

函数接口要求：以 `Student` 为基类，构建 `GroupA`、`GroupB`、`GroupC` 三个类。

裁判测试程序：

```cpp
#include<iostream>
#include <string>
using namespace std;

/* 请在这里填写答案 */

int main()
{
    const int Size=50;
    string num, name;
    int i,ty,s1,s2,s3,s4,s5;
    char gs;
    Student *pS[Size];
    int count=0;
    for(i=0;i<Size;i++){
        cin>>ty;
        if(ty==0) break;
        cin>>num>>name>>s1>>s2;
        switch(ty){
             case 1:pS[count++]=new GroupA(num, name, s1, s2); break;
             case 2:cin>>gs; pS[count++]=new GroupB(num, name, s1,s2, gs); break;
             case 3:cin>>s3>>s4>>s5; pS[count++]=new GroupC(num, name, s1,s2,s3,s4,s5); break;
        }
    }
    for(i=0;i<count;i++) {
        pS[i]->display();
        delete pS[i];
    }
    return 0;
}
```

输入样例：

```text
1 001 AAAA 96 80
2 009 BBB 82 75 A
1 007 CC 100 99
3 012 CCCC 97 95 90 99 93
1 003 DDD 62 50
1 022 ABCE 78 92
2 010 FFF 45 40 A
3 019 AAA 93 97 94 82 80
0
```

输出样例：

```text
009 BBB
007 CC
012 CCCC
```

强化测试样例 1：并列第一、恰好 90%、恰好 70%

```text
1 101 A1 90 90
2 102 B1 95 85 B
3 103 C1 81 81 81 81 81
2 104 B2 63 63 A
2 105 B3 63 63 B
1 106 A2 90 89
0
```

输出应为：

```text
101 A1
102 B1
103 C1
104 B2
```

强化测试样例 2：输入顺序乱序，获奖线在后面才出现

```text
3 201 Cearly 80 80 80 80 80
2 202 Bearly 60 60 A
1 203 TopA 100 98
2 204 TopB 99 99 C
3 205 Clate 90 88 91 89 90
0
```

输出应为：

```text
203 TopA
204 TopB
205 Clate
```

评分点：

- `Student` 基类保存学号、姓名，并提供虚函数 `display()`：4 分
- `GroupA`、`GroupB`、`GroupC` 正确继承并实现构造：4 分
- 能在所有对象构造完成后得到普通生/运动员 2 门平均分最高值作为获奖线，即使最高者后输入：4 分
- 三类学生的表彰规则判断正确，含并列第一、恰好 90%、恰好 70%、运动员重复满足规则但只输出一次：5 分
- 输出顺序、格式、内存释放配合裁判程序正确：3 分

易错点：

- `display()` 必须是虚函数，否则 `Student*` 调用不到派生类逻辑。
- 获奖线来自 `GroupA` 和 `GroupB`，不包含 `GroupC`。
- `GroupB` 有两种获奖可能：最高平均分并列第一，或 `avg >= line * 0.7 && grade == 'A'`。
- 主函数先读完所有对象，再统一调用 `display()`，因此可以用静态成员在构造阶段记录最高平均分。
- 如果用静态成员，别忘了在类外定义；这是这题在 PTA 编译环境里最常见的链接错误。
- 平均分建议用 `double`，避免整数除法影响 90% 和 70% 判断。

---

## 练习题 2：Document Import System（职责链模式，20 分）

We aim to design a **Document Import System**. Different importers handle files according to their extension. The system follows the **Chain of Responsibility Design Pattern**.

There are 6 classes in total:

- `ImportRequest`: represents one file import request.
  - attribute: `filename`
  - member function: `getFilename()`
  - member function: `getExtension()`, which returns the substring after the last `'.'`; if no dot exists, return an empty string.
- `Importer`: abstract handler interface.
  - `SetNext(Importer* importer)`
  - `Import(ImportRequest& request)`
- `BaseImporter`: derived from `Importer`; implements default chaining behavior.
- `PdfImporter`: handles `"pdf"`.
- `CsvImporter`: handles `"csv"`.
- `ImageImporter`: handles `"png"` and `"jpg"`.

The implementation for `BaseImporter` and `PdfImporter` is given:

```cpp
class BaseImporter : public Importer {
private:
    Importer* nextImporter = nullptr;
public:
    Importer* SetNext(Importer* importer) override {
        nextImporter = importer;
        return importer;
    }

    string Import(ImportRequest& request) override {
        if (nextImporter) {
            return nextImporter->Import(request);
        }
        return {};
    }
};

class PdfImporter : public BaseImporter {
public:
    string Import(ImportRequest& request) override {
        if (request.getExtension() == "pdf") {
            return "PdfImporter: imported PDF file.\n";
        }
        return BaseImporter::Import(request);
    }
};
```

Complete `ImportRequest`, `Importer`, `CsvImporter`, and `ImageImporter` so that the following code works properly.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void ClientCode(Importer& importer, vector<ImportRequest>& requests) {
    for (auto& request : requests) {
        cout << "Importing " << request.getFilename() << endl;
        string result = importer.Import(request);
        if (!result.empty()) {
            cout << "  " << result;
        } else {
            cout << "  " << request.getFilename() << " was left unhandled.\n";
        }
    }
}

int main() {
    PdfImporter* pdf = new PdfImporter;
    CsvImporter* csv = new CsvImporter;
    ImageImporter* image = new ImageImporter;

    pdf->SetNext(csv)->SetNext(image);

    vector<ImportRequest> requests = {
        ImportRequest("report.pdf"),
        ImportRequest("scores.csv"),
        ImportRequest("logo.png"),
        ImportRequest("photo.jpg"),
        ImportRequest("README")
    };

    cout << "Chain: PDF > CSV > Image" << endl;
    ClientCode(*pdf, requests);
    cout << endl;

    cout << "Subchain: CSV > Image" << endl;
    ClientCode(*csv, requests);

    delete pdf;
    delete csv;
    delete image;
    return 0;
}
```

Expected output:

```text
Chain: PDF > CSV > Image
Importing report.pdf
  PdfImporter: imported PDF file.
Importing scores.csv
  CsvImporter: imported CSV file.
Importing logo.png
  ImageImporter: imported image file.
Importing photo.jpg
  ImageImporter: imported image file.
Importing README
  README was left unhandled.

Subchain: CSV > Image
Importing report.pdf
  report.pdf was left unhandled.
Importing scores.csv
  CsvImporter: imported CSV file.
Importing logo.png
  ImageImporter: imported image file.
Importing photo.jpg
  ImageImporter: imported image file.
Importing README
  README was left unhandled.
```

评分点：

- `Importer` 是抽象类，函数签名与题面完全一致：5 分
- `ImportRequest` 正确保存文件名并提取扩展名：5 分
- `CsvImporter` / `ImageImporter` 正确 override 并在不能处理时转发：6 分
- 链式调用 `SetNext()` 可连续使用，且无多余输出：2 分
- 代码可编译、析构安全意识合理：2 分

---

## 练习题 3：Shape Drawing Script（多态 + 流解析，25 分）

The class hierarchy in this task is as follows:

- `Shape`: abstract base class.
- `Line`, `Rectangle`, and `Circle`: concrete derived classes.
- `DrawingDocument`: owns shapes and calls their `draw()` functions.

The text file describes shapes line by line:

```text
Line from 0 0 to 3 4
Rectangle left-bottom 2 5 W&H 6 8
Circle center 10 10 radius 5
```

The first word is the shape type. The remaining words describe attributes:

- `Line from x1 y1 to x2 y2`
- `Rectangle left-bottom x y W&H width height`
- `Circle center x y radius r`

Read the existing implementation of `DrawingDocument` and `main()`. Implement the required shape classes.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

class Shape {
public:
    virtual ~Shape() {}
    virtual void draw() = 0;
    virtual bool parseAttribute(ifstream& ifs) = 0;
};

class Line : public Shape {
    // TODO
};

class Rectangle : public Shape {
    // TODO
};

class Circle : public Shape {
    // TODO
};

class DrawingDocument {
public:
    ~DrawingDocument();
    void draw();
    void parse(ifstream& ifs);
private:
    vector<Shape*> shapes;
};

DrawingDocument::~DrawingDocument() {
    for (auto p : shapes) {
        delete p;
    }
}

void DrawingDocument::draw() {
    for (auto p : shapes) {
        p->draw();
    }
}

template<class X>
void parseAttribute(ifstream& ifs, vector<Shape*>& shapes) {
    Shape* p = new X();
    if (!p->parseAttribute(ifs)) {
        delete p;
        return;
    }
    shapes.push_back(p);
}

void DrawingDocument::parse(ifstream& ifs) {
    string type;
    while (ifs >> type) {
        if (type == "Line") {
            parseAttribute<Line>(ifs, shapes);
        } else if (type == "Rectangle") {
            parseAttribute<Rectangle>(ifs, shapes);
        } else if (type == "Circle") {
            parseAttribute<Circle>(ifs, shapes);
        } else {
            break;
        }
    }
}

int main() {
    ifstream ifs("D:\\drawing.txt");
    DrawingDocument doc;
    doc.parse(ifs);
    doc.draw();
    return 0;
}
```

Suppose `D:\drawing.txt` contains:

```text
Line from 0 0 to 3 4
Rectangle left-bottom 2 5 W&H 6 8
Circle center 10 10 radius 5
```

Expected output:

```text
Line 0 0 to 3 4
Rectangle 2 5 W&H 6 8
Circle 10 10 radius 5
```

评分点：

- `Shape` 派生关系、`public` 继承、override 签名正确：5 分
- 三个类正确读取关键字和数值：9 分
- `parseAttribute()` 遇到格式错误返回 `false`：3 分
- `draw()` 输出格式完全匹配：5 分
- 不创建临时局部对象地址、不泄漏已分配对象：3 分

---

## 练习题 4：Media Library（抽象接口 + 容器 + 工厂式解析，25 分）

Design a **Media Library**. Each line in a file describes one media item:

```text
Book title CppPrimer pages 970
Movie title Inception duration 148
Song title Yesterday artist Beatles
```

There are four classes:

- `MediaItem`: abstract base class.
  - `virtual ~MediaItem()`
  - `virtual bool load(istream& is) = 0`
  - `virtual void print() const = 0`
- `Book`
- `Movie`
- `Song`

There is also a `MediaLibrary` class that owns all created objects:

```cpp
class MediaLibrary {
public:
    ~MediaLibrary();
    void load(istream& is);
    void print() const;
private:
    vector<MediaItem*> items;
};
```

Complete all classes so that the following main function works.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main() {
    stringstream ss;
    ss << "Book title CppPrimer pages 970\n";
    ss << "Movie title Inception duration 148\n";
    ss << "Song title Yesterday artist Beatles\n";
    ss << "Unknown title Something\n";

    MediaLibrary lib;
    lib.load(ss);
    lib.print();
    return 0;
}
```

Expected output:

```text
Book: CppPrimer, pages 970
Movie: Inception, duration 148
Song: Yesterday, artist Beatles
```

Requirements:

- `MediaLibrary::load()` reads the first word of each item.
- If type is `Book`, `Movie`, or `Song`, create the corresponding object with `new`.
- If the object fails to load, delete it and do not store it.
- If the type is unknown, stop parsing.
- `MediaLibrary::~MediaLibrary()` must release every stored object.

评分点：

- 抽象基类接口设计正确：4 分
- 三个派生类的数据成员和 `load()` 实现正确：9 分
- `MediaLibrary::load()` 选择派生类并保存基类指针：6 分
- `print()` 使用多态，输出格式正确：4 分
- 析构释放资源：2 分

---

## 练习题 5：RingBuffer Template（模板 + 循环数组 + 异常，35 分）

Design a generic circular buffer class `RingBuffer<T>` using C++ standard exceptions:

- throw `overflow_error` when pushing into a full buffer
- throw `underflow_error` when popping from an empty buffer

The buffer has fixed capacity `capacity`. It stores at most `capacity` elements. Use a dynamically allocated array.

Class outline:

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

template <typename T>
class RingBuffer {
private:
    int capacity;
    int head;
    int tail;
    int count;
    T* data;

public:
    RingBuffer(int capacity = 8);
    RingBuffer(const RingBuffer& other);
    RingBuffer& operator=(const RingBuffer& other);
    ~RingBuffer();

    void push(const T& value);
    T pop();
    T front() const;
    int size() const;
    bool empty() const;
    bool full() const;
    void show() const;
};
```

Complete the class so that the following code works.

```cpp
int main() {
    try {
        RingBuffer<string> rb(4);

        rb.push("A");
        rb.push("B");
        rb.push("C");
        rb.show();

        cout << rb.pop() << endl;
        rb.push("D");
        rb.push("E");
        rb.show();

        cout << "front: " << rb.front() << endl;
        cout << "size: " << rb.size() << endl;

        rb.push("F");
    } catch (overflow_error& e) {
        cout << "overflow: " << e.what() << endl;
    } catch (underflow_error& e) {
        cout << "underflow: " << e.what() << endl;
    }

    try {
        RingBuffer<int> nums(2);
        nums.pop();
    } catch (underflow_error& e) {
        cout << "underflow: " << e.what() << endl;
    }

    return 0;
}
```

Expected output:

```text
A B C
A
B C D E
front: B
size: 4
overflow: buffer is full
underflow: buffer is empty
```

Requirements:

- `head` points to the current first element.
- `tail` points to the next insertion position.
- After an index reaches `capacity - 1`, the next index becomes `0`.
- `show()` prints elements from front to back, separated by one space, then prints a newline.
- Implement deep copy in copy constructor and assignment operator.

评分点：

- 构造、析构、动态数组管理：6 分
- `push()` / `pop()` 回绕逻辑正确：10 分
- `front()` / `size()` / `empty()` / `full()` 正确：5 分
- 异常类型和 `what()` 文本符合题目：4 分
- `show()` 按逻辑顺序输出：4 分
- 拷贝构造和赋值深拷贝，处理自赋值：6 分

---

## 练习题 6：Logger Chain（职责链进阶，20 分）

This exercise is inspired by the Chain of Responsibility pattern. Implement a logger chain. Each logger decides whether to handle a message according to its severity level. If it does not handle the message, it forwards the message to the next logger.

Severity levels:

```cpp
enum Level {
    INFO = 1,
    WARNING = 2,
    ERROR = 3
};
```

Classes:

- `LogMessage`
  - attributes: `Level level`, `string text`
  - `getLevel()`, `getText()`
- `Logger`
  - abstract class
  - `virtual Logger* SetNext(Logger* logger) = 0`
  - `virtual string Log(LogMessage& msg) = 0`
  - virtual destructor
- `BaseLogger`
  - stores `Logger* next`
  - default behavior: forward to next logger or return empty string
- `InfoLogger`
- `WarningLogger`
- `ErrorLogger`

Rules:

- `InfoLogger` handles `INFO`
- `WarningLogger` handles `WARNING`
- `ErrorLogger` handles `ERROR`

Test code:

```cpp
int main() {
    InfoLogger* info = new InfoLogger;
    WarningLogger* warning = new WarningLogger;
    ErrorLogger* error = new ErrorLogger;

    info->SetNext(warning)->SetNext(error);

    vector<LogMessage> messages = {
        LogMessage(INFO, "program started"),
        LogMessage(WARNING, "low memory"),
        LogMessage(ERROR, "cannot open file")
    };

    for (auto& msg : messages) {
        cout << info->Log(msg);
    }

    delete info;
    delete warning;
    delete error;
    return 0;
}
```

Expected output:

```text
InfoLogger: program started
WarningLogger: low memory
ErrorLogger: cannot open file
```

评分点：

- 抽象接口和虚析构：4 分
- `SetNext()` 返回传入的 logger，支持链式调用：4 分
- 三个具体 logger 判断条件正确：6 分
- 未处理时调用基类转发逻辑：4 分
- 输出格式正确：2 分
