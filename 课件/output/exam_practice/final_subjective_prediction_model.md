# C++ OOP 期末最后主观题预测模型

> 目的：不押原题外壳，而是从历年题和 PTA 复习题中抽出命题者反复考的“内在能力”。题目表面会变，核心考点基本不会变。

## 一句话判断

今年最后一道主观题最可能仍是：

**给定固定主函数或固定框架，让你补全一组类，使程序通过基类指针/引用、虚函数、动态创建对象、输入解析或模板容器逻辑得到指定输出。**

它不会只考“会不会写一个类”。更深层是在考：

- 你能不能从已有 client code 反推类接口；
- 你能不能用多态把不同对象统一放进同一个数组/容器；
- 你能不能处理对象生命周期、动态分配、虚析构；
- 你能不能在构造、解析、输出之间维护正确状态；
- 你能不能在固定裁判程序不能改的条件下完成全局逻辑。

## 不变的命题内核

| 内核 | 历年题里的表现 | 今年可能换成的外壳 | 真正要练的能力 |
|---|---|---|---|
| 固定 client code 反推接口 | `new GroupA(...)`、`pS[i]->display()`、`SetNext()` | 学生评奖、员工工资、订单折扣、设备告警、文件导入 | 读主函数，精确写出构造函数、虚函数、返回类型 |
| 多态统一处理异构对象 | `Student*`、`shape*`、`Handler&` | `Account*`、`Product*`、`Task*`、`Sensor*` | 基类抽象接口、`public` 继承、override、动态绑定 |
| 全局或跨对象判定 | 获奖线、并列第一、比例线 | 排名线、补贴线、报警阈值、折扣等级、合格线 | 静态成员、类级共享状态、两阶段判定 |
| 输入解析到对象状态 | `parseattribute(ifstream&)`、按类型读取字段 | 课程、图形、媒体、交通、商品、日志 | 用流读取 token，校验关键字，保存成员变量 |
| 动态资源和生命周期 | `vector<shape*>`、`new/delete`、循环队列 | 文档管理器、库存管理器、任务队列、自定义数组 | 虚析构、析构释放、深拷贝、异常安全的基本意识 |
| 模板泛型容器 | `CQueue<T>`、`Array<T>`、`inner_product` | RingBuffer、BlockArray、Matrix、Stack、Polynomial | 模板语法、动态数组、边界条件、operator 重载 |
| 设计模式骨架 | 职责链 `Handler` | Chain / Factory / Strategy / Composite 的简化版 | 用抽象类隔离变化，派生类只实现差异点 |

## 高概率题型预测

### 预测 1：固定主函数 + 多态 + 全局规则判定

概率：高。

可能外壳：

- 员工绩效：普通员工、销售、技术专家，按部门最高分/提成/项目分评优。
- 课程选拔：普通学生、竞赛生、体育生，按平均分、特长分、排名线录取。
- 商品促销：普通商品、生鲜、会员商品，按利润率或折扣线输出推荐商品。
- 设备报警：普通传感器、关键传感器、复合传感器，按最高风险线输出报警设备。

题目会给：

```cpp
Base* p[50];
p[count++] = new DerivedA(...);
p[count++] = new DerivedB(...);
...
for (int i = 0; i < count; i++) {
    p[i]->display();
    delete p[i];
}
```

深层考点：

- `display()` 必须虚函数；
- 构造函数参数要完全匹配裁判代码；
- 如果输出条件依赖全体对象，不能只在构造时立即输出；
- 可用静态成员记录最高线、最低线、总人数、全局阈值；
- 输出顺序通常要求保持输入顺序。

最可能卡点：

- 最高线后输入，前面对象也要按最终最高线判定；
- 并列第一全部输出；
- `>= 70%`、`>= 90%` 这种边界；
- 运动员/特长生/特殊类既可能满足普通规则，也可能满足特殊规则，但只能输出一次。

### 预测 2：抽象基类 + 文档/记录解析 + 统一输出

概率：高。

可能外壳：

- 图形脚本：`Line`、`Circle`、`Rectangle`、`Triangle`；
- 媒体库：`Book`、`Movie`、`Song`；
- 交通系统：`Bus`、`Train`、`Flight`；
- 订单系统：`FoodOrder`、`BookOrder`、`ElectronicOrder`；
- 日志系统：`InfoLog`、`WarningLog`、`ErrorLog`。

题目会给：

```cpp
class Base {
public:
    virtual ~Base() {}
    virtual bool parse(istream& is) = 0;
    virtual void print() const = 0;
};

vector<Base*> items;
```

深层考点：

- 纯虚函数定义接口；
- 派生类各自解析不同字段；
- manager/document 类只保存 `Base*`；
- 读取第一个 token 决定创建哪个派生类；
- 析构函数释放所有 `new` 出来的对象。

最可能卡点：

- `parse()` 要读掉关键字，如 `center`、`radius`、`title`；
- 格式错误时要 `delete` 临时对象；
- 输出顺序是文件顺序；
- 基类析构要 virtual；
- 派生类 `print()` 或 `draw()` 签名必须和基类一致，`const` 也要一致。

### 预测 3：模板容器 + 动态数组 + 边界条件

概率：中高，尤其如果最后题分值偏 30-35。

可能外壳：

- 循环队列、栈、动态数组、分块数组；
- 稀疏向量、矩阵、简单多项式；
- 带容量限制的缓存；
- 类似 STL 的简化容器。

深层考点：

- `template <typename T>` 类定义；
- `new[]` / `delete[]`；
- 拷贝构造、赋值运算符、析构，即 Rule of Three；
- `operator[]`、`operator+`、`operator<<`；
- 空、满、越界、下标回绕；
- 抛出 `overflow_error` / `underflow_error` 或返回错误状态。

最可能卡点：

- `head`、`tail`、`count` 三者不一致；
- 满队列和空队列判断混淆；
- 返回引用还是返回值；
- 自赋值；
- 浅拷贝导致 double delete；
- 模板成员函数写在类外时忘记 `template <typename T>` 和 `Class<T>::`。

### 预测 4：简化设计模式，不一定明说模式名

概率：中高。

可能外壳：

- 文件导入器：PDF/CSV/Image；
- 客服路由：Billing/Technical/Service；
- 日志处理：Info/Warning/Error；
- 支付策略：CreditCard/Alipay/Cash；
- 菜单组件：Menu/MenuItem；
- 消息过滤器：Spam/Urgent/Normal。

深层考点：

- 抽象基类声明统一接口；
- 基类实现默认行为；
- 派生类只处理自己负责的情况；
- 处理不了时转发或返回空；
- client code 只依赖基类。

最可能卡点：

- `SetNext()` 返回传入对象以支持链式调用；
- 派生类处理失败时必须调用 `BaseHandler::Handle()`；
- 返回字符串不能多空格、多换行；
- 基类指针删除派生对象，析构函数要 virtual；
- 不要在派生类里复制一份链表指针破坏转发。

## 今年命题最可能的“换皮方式”

如果老师想避开原题，最自然的变化不是换掉考点，而是换掉业务场景：

1. 把“学生评奖”换成“员工绩效/商品推荐/设备报警”。
2. 把“图形文件解析”换成“媒体记录解析/订单记录解析/日志记录解析”。
3. 把“循环队列”换成“固定容量缓存/环形日志/任务队列”。
4. 把“职责链客服”换成“日志级别处理/文件导入处理/审批流程处理”。

所以不要背类名。真正要背的是这几套骨架：

```cpp
class Base {
public:
    virtual ~Base() {}
    virtual void display() = 0;
};
```

```cpp
class Base {
public:
    virtual ~Base() {}
    virtual bool parse(istream& is) = 0;
    virtual void print() const = 0;
};
```

```cpp
template <typename T>
class Container {
public:
    Container();
    Container(const Container& other);
    Container& operator=(const Container& other);
    ~Container();
};
```

```cpp
class Handler {
public:
    virtual ~Handler() {}
    virtual Handler* SetNext(Handler* h) = 0;
    virtual string Handle(Request& r) = 0;
};
```

## 最值得准备的 8 个硬考点

1. **虚函数和动态绑定**
   - 基类指针调用派生类函数。
   - `display()` / `draw()` / `print()` 这种函数几乎一定要 virtual。

2. **虚析构函数**
   - 只要题目里有 `Base* p = new Derived; delete p;`，基类析构就应该 virtual。

3. **构造函数签名反推**
   - 从 `new GroupB(num, name, s1, s2, gs)` 反推出构造函数参数。

4. **静态成员保存全局状态**
   - 最高分、获奖线、对象总数、阈值、编号计数器。

5. **输入流解析**
   - `ifs >> token >> x >> y`。
   - 关键字必须读掉，但可以不保存。

6. **容器保存基类指针**
   - `vector<Base*>` 或 `Base* arr[50]`。
   - 只通过虚函数访问派生对象。

7. **模板类和类外定义**
   - 模板成员函数写法不能错。

8. **Rule of Three**
   - 有裸指针资源，就要考虑析构、拷贝构造、赋值运算符。

## 最可能的一道“今年卷面题”长相

我认为最高概率不是原封不动的学生题，也不是原封不动的 shape 题，而是下面这种组合型：

> 给一个固定主函数，根据输入类型创建三类对象，统一存入基类指针数组或 `vector<Base*>`。每类对象有不同字段。读完全部对象后，通过虚函数输出满足某个全局规则的对象。规则包含一个由部分对象计算出的“标准线/阈值”，另一类对象按该阈值的某个比例判断，还有一类对象有特殊加分或特殊资格。

这类题同时覆盖：

- 多态；
- 构造函数；
- 静态成员；
- 全局判定；
- 输入顺序保持；
- 输出格式；
- 固定裁判程序不可改。

如果分值更高，可能会把它升级成：

> 再加一个 manager/document 类，负责读取输入、创建对象、析构释放，并用 `parse()` / `print()` 多态处理。

如果分值到 30-35，可能会换成：

> 模板容器 + 动态数组 + 异常 + 深拷贝。

## 复习优先级

最高优先级：

- 多态类层次：`Base` + 3 个派生类；
- 固定主函数反推接口；
- 静态成员全局统计；
- 虚析构；
- 输入解析和输出格式。

第二优先级：

- `vector<Base*>` 管理对象；
- 模板类语法；
- 拷贝构造、赋值、析构；
- 运算符重载。

第三优先级：

- 设计模式名字本身。

模式名不重要，重要的是能看出“统一接口 + 不同派生行为 + client 只依赖基类”。

## 三道预测练习题

这些题不照搬原题外壳，但命题骨架和考点高度一致。

### 预测题 A：设备风险报警系统

题型：固定主函数 + 多态 + 全局阈值。

场景：

一个实验室有三类设备：

- `NormalDevice`：普通设备，有温度 `temp` 和电压 `volt`，风险值为 `(temp + volt) / 2`。
- `CriticalDevice`：关键设备，有温度 `temp`、电压 `volt` 和等级 `level`，风险值为 `(temp + volt) / 2`，等级可能是 `A/B/C`。
- `CompositeDevice`：复合设备，有 4 个检测值，风险值为 4 个值的平均。

报警规则：

1. 普通设备和关键设备中，风险值最高者报警；并列最高全部报警。该最高风险值称为报警线。
2. 复合设备风险值达到报警线 85% 及以上，报警。
3. 关键设备风险值达到报警线 65% 及以上，且等级为 `A`，报警。

固定裁判程序会类似：

```cpp
Device* p[50];
p[count++] = new NormalDevice(id, name, temp, volt);
p[count++] = new CriticalDevice(id, name, temp, volt, level);
p[count++] = new CompositeDevice(id, name, a, b, c, d);

for (int i = 0; i < count; i++) {
    p[i]->alarm();
    delete p[i];
}
```

你要补：

- `Device` 基类；
- 三个派生类；
- 全局报警线维护；
- `alarm()` 多态输出。

高分关键：

- 报警线只来自 `NormalDevice` 和 `CriticalDevice`；
- 读完所有对象后才调用 `alarm()`，所以静态成员可行；
- 边界是 `>=`，不是 `>`；
- `CriticalDevice` 可能既是最高风险，又满足等级 A 特判，但只输出一次。

### 预测题 B：订单处理文档

题型：抽象基类 + 输入解析 + manager 析构。

场景：

输入文件每行描述一个订单：

```text
Book id B001 price 80 pages 300
Food id F002 price 40 expire 3
Electronic id E003 price 1200 warranty 24
```

要求实现：

```cpp
class Order {
public:
    virtual ~Order() {}
    virtual bool parse(istream& is) = 0;
    virtual void print() const = 0;
};
```

派生类：

- `BookOrder`
- `FoodOrder`
- `ElectronicOrder`

`OrderDocument` 保存 `vector<Order*>`，读取第一个 token 决定创建哪种订单，调用对应 `parse()`，最后 `print()` 输出。

可能输出：

```text
Book B001 price 80 pages 300
Food F002 price 40 expire 3
Electronic E003 price 1200 warranty 24
```

高分关键：

- `parse()` 里要读掉 `id`、`price`、`pages` 等关键字；
- `print()` 最好声明为 `const`，如果基类是 `const`，派生类必须一致；
- unknown type 时停止或忽略，要看题面；
- `OrderDocument::~OrderDocument()` 必须 `delete` 所有对象。

### 预测题 C：固定容量任务缓存

题型：模板容器 + 动态数组 + 深拷贝。

要求实现：

```cpp
template <typename T>
class TaskBuffer {
private:
    T* data;
    int capacity;
    int first;
    int last;
    int count;
public:
    TaskBuffer(int capacity = 10);
    TaskBuffer(const TaskBuffer& other);
    TaskBuffer& operator=(const TaskBuffer& other);
    ~TaskBuffer();

    void push(const T& x);
    T pop();
    T& operator[](int index);
    int size() const;
    bool empty() const;
    bool full() const;
};
```

规则：

- 满时 `push()` 抛 `overflow_error("buffer full")`；
- 空时 `pop()` 抛 `underflow_error("buffer empty")`；
- `operator[]` 按逻辑顺序访问第 `index` 个元素；
- 拷贝构造和赋值必须深拷贝。

高分关键：

- `operator[]` 的真实下标是 `(first + index) % capacity`；
- `pop()` 要更新 `first` 和 `count`；
- `push()` 要更新 `last` 和 `count`；
- 赋值运算符要处理自赋值；
- 类外定义模板函数时格式要完整。
