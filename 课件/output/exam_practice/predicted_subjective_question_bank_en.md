# Predicted C++ OOP Final Subjective Question Bank

> Practice version. No reference answers are included. The questions are written in an exam-like English style and are designed from the underlying logic of previous final questions, not by copying their surface scenarios.

---

# Subjective Question 1: Equipment Risk Alert System

**Score: 25**

An engineering laboratory monitors several kinds of equipment. There are three types of devices:

- `NormalDevice`: a normal device, with a temperature value and a voltage value.
- `CriticalDevice`: a critical device, with a temperature value, a voltage value, and a risk level. The level can be `A`, `B`, or `C`.
- `CompositeDevice`: a composite device, with four sensor readings.

The risk value is defined as follows:

- For `NormalDevice`, risk = `(temperature + voltage) / 2`.
- For `CriticalDevice`, risk = `(temperature + voltage) / 2`.
- For `CompositeDevice`, risk = the average of the four sensor readings.

The alert rules are:

1. Among all `NormalDevice` and `CriticalDevice` objects, the devices with the highest risk value must be alerted. This highest risk value is called the **alert line**. If there is a tie, all tied devices must be alerted.
2. A `CompositeDevice` must be alerted if its risk value is greater than or equal to 85% of the alert line.
3. A `CriticalDevice` must also be alerted if its risk value is greater than or equal to 65% of the alert line and its level is `A`.

The output order must be the same as the input order.

## Function Interface

Use `Device` as the base class, and implement `NormalDevice`, `CriticalDevice`, and `CompositeDevice`.

## Judge Program

```cpp
#include <iostream>
#include <string>
using namespace std;

/* Please write your answer here */

int main()
{
    const int Size = 50;
    int type;
    string id, name;
    double a, b, c, d;
    char level;
    Device* devices[Size];
    int count = 0;

    for (int i = 0; i < Size; i++) {
        cin >> type;
        if (type == 0) break;

        cin >> id >> name;
        switch (type) {
            case 1:
                cin >> a >> b;
                devices[count++] = new NormalDevice(id, name, a, b);
                break;
            case 2:
                cin >> a >> b >> level;
                devices[count++] = new CriticalDevice(id, name, a, b, level);
                break;
            case 3:
                cin >> a >> b >> c >> d;
                devices[count++] = new CompositeDevice(id, name, a, b, c, d);
                break;
        }
    }

    for (int i = 0; i < count; i++) {
        devices[i]->alert();
        delete devices[i];
    }

    return 0;
}
```

## Sample Input

```text
1 D01 Pump 80 70
2 D02 Core 90 90 B
3 D03 Filter 78 77 76 75
2 D04 Valve 60 57 A
1 D05 Fan 89 91
2 D06 Backup 60 57 B
0
```

## Sample Output

```text
D02 Core
D03 Filter
D04 Valve
D05 Fan
```

## Requirements

- `Device` must provide a virtual member function `alert()`.
- The judge program must not be modified.
- The alert line is computed only from `NormalDevice` and `CriticalDevice`.
- Use floating point calculation for average values and percentage comparisons.
- A device that satisfies multiple alert rules must be printed only once.

---

# Subjective Question 2: Order Processing Document

**Score: 25**

A company stores order information in a text file. Each line describes one order. There are three types of orders:

- `BookOrder`
- `FoodOrder`
- `ElectronicOrder`

The format of each line is:

```text
Book id B001 price 80 pages 300
Food id F002 price 40 expire 3
Electronic id E003 price 1200 warranty 24
```

The first word is the order type. The remaining words describe the attributes of the order.

You are given the implementation of `OrderDocument` and the `main()` function. Implement the required order classes so that the orders can be parsed and printed correctly.

## Given Code

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Order {
public:
    virtual ~Order() {}
    virtual bool parse(istream& is) = 0;
    virtual void print() const = 0;
};

class BookOrder : public Order {
    // TODO
};

class FoodOrder : public Order {
    // TODO
};

class ElectronicOrder : public Order {
    // TODO
};

class OrderDocument {
public:
    ~OrderDocument();
    void parse(istream& is);
    void print() const;
private:
    vector<Order*> orders;
};

OrderDocument::~OrderDocument()
{
    for (auto p : orders) {
        delete p;
    }
}

template <class T>
void parseOrder(istream& is, vector<Order*>& orders)
{
    Order* p = new T();
    if (!p->parse(is)) {
        delete p;
        return;
    }
    orders.push_back(p);
}

void OrderDocument::parse(istream& is)
{
    string type;
    while (is >> type) {
        if (type == "Book") {
            parseOrder<BookOrder>(is, orders);
        } else if (type == "Food") {
            parseOrder<FoodOrder>(is, orders);
        } else if (type == "Electronic") {
            parseOrder<ElectronicOrder>(is, orders);
        } else {
            break;
        }
    }
}

void OrderDocument::print() const
{
    for (auto p : orders) {
        p->print();
    }
}

int main()
{
    stringstream ss;
    ss << "Book id B001 price 80 pages 300\n";
    ss << "Food id F002 price 40 expire 3\n";
    ss << "Electronic id E003 price 1200 warranty 24\n";
    ss << "Unknown id X000 price 0\n";

    OrderDocument doc;
    doc.parse(ss);
    doc.print();
    return 0;
}
```

## Expected Output

```text
Book B001 price 80 pages 300
Food F002 price 40 expire 3
Electronic E003 price 1200 warranty 24
```

## Requirements

- `BookOrder::parse()` must read the tokens `id`, `price`, and `pages`.
- `FoodOrder::parse()` must read the tokens `id`, `price`, and `expire`.
- `ElectronicOrder::parse()` must read the tokens `id`, `price`, and `warranty`.
- If the input format is not correct, `parse()` should return `false`.
- The signatures of the virtual functions must exactly match the base class.

---

# Subjective Question 3: Generic Task Buffer

**Score: 35**

Design a template class `TaskBuffer<T>`. It stores elements in a fixed-capacity circular buffer. The buffer supports insertion at the back, removal from the front, random access by logical index, and deep copy.

When the buffer is full, `push()` must throw:

```cpp
overflow_error("buffer full")
```

When the buffer is empty, `pop()` must throw:

```cpp
underflow_error("buffer empty")
```

When `operator[]` receives an invalid index, it must throw:

```cpp
out_of_range("invalid index")
```

## Class Interface

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

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

    void push(const T& value);
    T pop();
    T& operator[](int index);
    const T& operator[](int index) const;
    int size() const;
    bool empty() const;
    bool full() const;
    void show() const;
};
```

## Test Program

```cpp
int main()
{
    try {
        TaskBuffer<string> tasks(3);
        tasks.push("A");
        tasks.push("B");
        tasks.push("C");
        tasks.show();

        cout << tasks.pop() << endl;
        tasks.push("D");
        tasks.show();

        TaskBuffer<string> copy = tasks;
        copy[1] = "X";

        tasks.show();
        copy.show();

        tasks.push("E");
    } catch (exception& e) {
        cout << e.what() << endl;
    }

    try {
        TaskBuffer<int> nums(2);
        nums.pop();
    } catch (exception& e) {
        cout << e.what() << endl;
    }

    return 0;
}
```

## Expected Output

```text
A B C
A
B C D
B C D
B X D
buffer full
buffer empty
```

## Requirements

- `first` points to the first valid element.
- `last` points to the next insertion position.
- The physical array index for logical index `i` is `(first + i) % capacity`.
- `show()` prints elements in logical order, separated by one space, then prints a newline.
- Implement the copy constructor, assignment operator, and destructor correctly.
- The assignment operator must handle self-assignment.

---

# Subjective Question 4: Expense Approval System

**Score: 20**

An enterprise uses an approval chain for expense requests. Each approver handles requests up to a certain amount. If an approver cannot handle a request, the request is passed to the next approver in the chain.

There are five classes in total:

- `ExpenseRequest`: stores a request number and an amount.
- `Approver`: abstract base class of all approvers.
- `BaseApprover`: implements the default chaining behavior.
- `Supervisor`: handles requests whose amount is not greater than 1000.
- `Manager`: handles requests whose amount is not greater than 5000.
- `Director`: handles requests whose amount is not greater than 20000.

The implementation of `BaseApprover` and `Supervisor` is given below.

```cpp
class BaseApprover : public Approver {
private:
    Approver* next = nullptr;
public:
    Approver* SetNext(Approver* approver) override {
        next = approver;
        return approver;
    }

    string Approve(ExpenseRequest& request) override {
        if (next) {
            return next->Approve(request);
        }
        return {};
    }
};

class Supervisor : public BaseApprover {
public:
    string Approve(ExpenseRequest& request) override {
        if (request.getAmount() <= 1000) {
            return "Supervisor approved " + request.getNumber() + ".\n";
        }
        return BaseApprover::Approve(request);
    }
};
```

Implement `ExpenseRequest`, `Approver`, `Manager`, and `Director` so that the following program works correctly.

## Client Code

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/* Please write your answer here */

void ClientCode(Approver& approver, vector<ExpenseRequest>& requests)
{
    for (auto& request : requests) {
        cout << "Request " << request.getNumber()
             << " amount " << request.getAmount() << endl;

        string result = approver.Approve(request);
        if (!result.empty()) {
            cout << "  " << result;
        } else {
            cout << "  " << request.getNumber() << " was rejected.\n";
        }
    }
}

int main()
{
    Supervisor* supervisor = new Supervisor;
    Manager* manager = new Manager;
    Director* director = new Director;

    supervisor->SetNext(manager)->SetNext(director);

    vector<ExpenseRequest> requests = {
        ExpenseRequest("R001", 800),
        ExpenseRequest("R002", 4000),
        ExpenseRequest("R003", 16000),
        ExpenseRequest("R004", 25000)
    };

    cout << "Chain: Supervisor > Manager > Director" << endl;
    ClientCode(*supervisor, requests);
    cout << endl;

    cout << "Subchain: Manager > Director" << endl;
    ClientCode(*manager, requests);

    delete supervisor;
    delete manager;
    delete director;
    return 0;
}
```

## Expected Output

```text
Chain: Supervisor > Manager > Director
Request R001 amount 800
  Supervisor approved R001.
Request R002 amount 4000
  Manager approved R002.
Request R003 amount 16000
  Director approved R003.
Request R004 amount 25000
  R004 was rejected.

Subchain: Manager > Director
Request R001 amount 800
  Manager approved R001.
Request R002 amount 4000
  Manager approved R002.
Request R003 amount 16000
  Director approved R003.
Request R004 amount 25000
  R004 was rejected.
```

## Requirements

- `Approver` must be an abstract class.
- `SetNext()` must support chained calls.
- If a concrete approver cannot handle a request, it must call `BaseApprover::Approve()`.
- The base class should have a virtual destructor.
- The output string must exactly match the expected output.

---

# Subjective Question 5: File Tree Composite

**Score: 25**

Implement a small file tree system. A file tree node can be either:

- `FileItem`: a file with a name and a size.
- `Folder`: a folder with a name and a list of child nodes.

Both files and folders must be handled uniformly through the abstract base class `FileNode`.

The total size of a file is its own size. The total size of a folder is the sum of the total sizes of all its children.

## Required Classes

There are three classes:

- `FileNode`
  - abstract base class
  - virtual destructor
  - `virtual int getSize() const = 0`
  - `virtual void print(int indent = 0) const = 0`
- `FileItem`
- `Folder`

`Folder` must provide:

```cpp
void add(FileNode* node);
```

`Folder` owns its child nodes and must delete them in its destructor.

## Test Program

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/* Please write your answer here */

int main()
{
    Folder* root = new Folder("root");
    Folder* src = new Folder("src");
    Folder* test = new Folder("test");

    root->add(new FileItem("README.md", 2));
    src->add(new FileItem("main.cpp", 10));
    src->add(new FileItem("util.cpp", 6));
    test->add(new FileItem("sample.in", 1));
    test->add(new FileItem("sample.out", 1));
    root->add(src);
    root->add(test);

    root->print();
    cout << "Total size: " << root->getSize() << endl;

    delete root;
    return 0;
}
```

## Expected Output

```text
Folder root
  File README.md 2
  Folder src
    File main.cpp 10
    File util.cpp 6
  Folder test
    File sample.in 1
    File sample.out 1
Total size: 20
```

## Requirements

- Each indentation level consists of two spaces.
- `FileNode` must have a virtual destructor.
- `Folder::getSize()` must compute the recursive total size.
- Deleting `root` must delete every child node exactly once.
- Do not use global variables.

---

# Subjective Question 6: Packet Filtering Rules

**Score: 25**

A network monitor processes packets using a list of filtering rules. Each packet has:

- a source address,
- a priority,
- a size.

There are three filtering rules:

- `HighPriorityRule`: matches packets whose priority is greater than or equal to 8.
- `LargePacketRule`: matches packets whose size is greater than 1000.
- `SourceRule`: matches packets from a specified source address.

The monitor checks rules in the order they are added. For each packet, only the first matching rule prints a message. If no rule matches, the packet is accepted.

## Given Interfaces

Implement the following classes:

- `Packet`
- `Rule`
- `HighPriorityRule`
- `LargePacketRule`
- `SourceRule`
- `PacketMonitor`

`Rule` is an abstract base class:

```cpp
class Rule {
public:
    virtual ~Rule() {}
    virtual bool match(const Packet& packet) const = 0;
    virtual string message(const Packet& packet) const = 0;
};
```

`PacketMonitor` owns all rules added to it.

## Test Program

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/* Please write your answer here */

int main()
{
    PacketMonitor monitor;

    monitor.addRule(new SourceRule("10.0.0.1"));
    monitor.addRule(new HighPriorityRule);
    monitor.addRule(new LargePacketRule);

    vector<Packet> packets = {
        Packet("10.0.0.1", 3, 200),
        Packet("10.0.0.2", 9, 300),
        Packet("10.0.0.3", 4, 1500),
        Packet("10.0.0.4", 2, 100),
        Packet("10.0.0.1", 10, 2000)
    };

    for (auto& packet : packets) {
        monitor.process(packet);
    }

    return 0;
}
```

## Expected Output

```text
Blocked source 10.0.0.1
High priority packet from 10.0.0.2
Large packet from 10.0.0.3
Accepted packet from 10.0.0.4
Blocked source 10.0.0.1
```

## Requirements

- `Packet` must provide getter functions for source, priority, and size.
- `PacketMonitor::addRule()` stores a rule pointer.
- `PacketMonitor::process()` checks rules in insertion order.
- Only the first matching rule should print a message.
- `PacketMonitor` must delete all stored rules in its destructor.

