from pathlib import Path
import re


def replace_block(text: str, qid: str, replacement: str) -> str:
    pattern = re.compile(
        rf"\*\*{re.escape(qid)}\*\*\. .*?(?=\n\*\*2-\d+\*\*\. |\n### |\n## Answers)",
        re.S,
    )
    return pattern.sub(replacement.strip() + "\n", text)


p = Path("c++练习题目一：基础知识.md")
t = p.read_text(encoding="utf-8")

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

t = replace_block(t, "2-60", r'''
**2-60**. What changes can you make in the header files to avoid the redefinition error that the compiler will give when both header files are included in the same program and both functions have the same declaration?

Content of `h1.h`:

```cpp
// h1.h
#include <iostream>
using namespace std;

int func(int a)
{
    cout << a;
    return a;
}
```

Content of `h2.h`:

```cpp
// h2.h
#include <iostream>
using namespace std;

int func(int a)
{
    cout << a;
    return a;
}
```
- A. Cannot be handled because C++ does not allow this
- B. Declare both functions inside different namespaces
- C. Include only the header files that are needed so that no name clashes occur
- D. Make the header file names the same
''')

p.write_text(t, encoding="utf-8")
