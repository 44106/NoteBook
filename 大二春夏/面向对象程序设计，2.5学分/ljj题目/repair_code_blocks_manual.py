from pathlib import Path
import re


def replace_block(text: str, qid: str, replacement: str) -> str:
    pattern = re.compile(
        rf"\*\*{re.escape(qid)}\*\*\. .*?(?=\n\*\*2-\d+\*\*\. |\n### |\n## Answers)",
        re.S,
    )
    return pattern.sub(replacement.strip() + "\n", text)


p1 = Path("c++练习题目一：基础知识.md")
t = p1.read_text(encoding="utf-8")

t = replace_block(t, "2-4", r'''
**2-4**. What is the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std;

class Mammal
{
public:
    Mammal()
    {
        cout << "I'm a Mammal\n";
    }
    ~Mammal() {}
};

class Human : public Mammal
{
public:
    Human()
    {
        cout << "I'm a Human\n";
    }
};

class Male : public Human
{
public:
    Male()
    {
        cout << "I'm a Male\n";
    }
};

class Female : public Human
{
public:
    Female()
    {
        cout << "I'm a Female\n";
    }
};

int main()
{
    Male M;
    return 0;
}
```
- A. I'm a Mammal

I'm a Human

I'm a Male
- B. I'm a Mammal

I'm a Human

I'm a Female
- C. I'm a Human

I'm a Male
- D. I'm a Mammal

I'm a Male
''')

t = replace_block(t, "2-43", r'''
**2-43**. What will be the output of the following C++ code?

```cpp
#include <iostream>
using namespace std;

namespace first
{
    int var = 5;
}

namespace second
{
    double var = 3.1416;
}

int main()
{
    int a;
    a = first::var + second::var;
    cout << a;
    return 0;
}
```
- A. 8.31416
- B. 8
- C. 9
- D. compile time error
''')

t = replace_block(t, "2-51", r'''
**2-51**. What will be the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std;

namespace A
{
    int var = 10;
}

namespace B
{
    int cout = 5;
}

int main()
{
    using namespace B;
    cout << A::var;
    return 0;
}
```
- A. 10
- B. 5
- C. Error
- D. 105
''')

t = replace_block(t, "2-52", r'''
**2-52**. What will be the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std;

namespace A
{
    int var = 10;
}

namespace B
{
    int var = 5;
}

int main()
{
    using namespace B;
    cout << var;
    return 0;
}
```
- A. 5
- B. 10
- C. Error
- D. Wrong use of namespace
''')

t = replace_block(t, "2-53", r'''
**2-53**. What will be the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std;

namespace A
{
    int var = 10;
}

namespace B
{
    int var = 5;
}

int main()
{
    int var = 20;
    using namespace B;
    cout << var;
    return 0;
}
```
- A. 5
- B. 10
- C. 20
- D. Error
''')

t = replace_block(t, "2-54", r'''
**2-54**. What will be the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std;

namespace
{
    int var = 10;
}

int main()
{
    cout << var;
    return 0;
}
```
- A. 10
- B. Error
- C. Some garbage value
- D. Nothing but program runs perfectly
''')

t = replace_block(t, "2-56", r'''
**2-56**. How to print the value of the i variable inside namespace B?

```cpp
namespace A
{
    int var = 10;

    namespace B
    {
        int i = 15;
    }
}
```
- A. cout<<A::i;
- B. cout<<B::i;
- C. cout<<A::B::i;
- D. cout<<i;
''')

p1.write_text(t, encoding="utf-8")


p3 = Path("c++练习题目三：派生和继承.md")
t3 = p3.read_text(encoding="utf-8")
t3 = replace_block(t3, "2-10", r'''
**2-10**. Which among the following is true for the given code below?

```cpp
class A
{
protected:
    int marks;

public:
    A()
    {
        marks = 100;
    }

    void disp()
    {
        cout << "marks=" << marks;
    }
};

class B : protected A
{
};

B b;
b.disp();
```
- A. Object b can't access disp() function
- B. Object b can access disp() function inside its body
- C. Object b can't access members of class A
- D. Program runs fine
''')

t3 = replace_block(t3, "2-28", r'''
**2-28**. Which among the following is correct for the following code?

```cpp
class A
{
public:
    class B
    {
    public:
        B(int i) : data(i)
        {
        }

        int data;
    };
};

class C : public A
{
    class D : public A::B
    {
    };
};
```
- A. Multi-level inheritance is used, with nested classes
- B. Multiple inheritance is used, with nested classes
- C. Single level inheritance is used, with enclosing classes
- D. Single level inheritance is used, with both enclosing and nested classes
''')

p3.write_text(t3, encoding="utf-8")
