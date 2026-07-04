# c++练习题目一：基础知识

## Questions

### Miscellaneous

**2-1**. To catch the exceptions ___________________
- A. An object must be created to catch the exception
- B. A variable should be created to catch the exception
- C. An array should be created to catch all the exceptions
- D. A string have to be created to store the exception

**2-7**. Which Feature of OOP illustrated the code reusability?
- A. Polymorphism
- B. Abstraction
- C. Encapsulation
- D. Inheritance

**2-8**. Which concept of OOP is false for C++?
- A. Code can be written without using classes
- B. Code must contain at least one class
- C. A class must have member functions
- D. At least one object should be declared in code

**2-9**. Which of the two features match each other?
- A. Inheritance and Encapsulation
- B. Encapsulation and Polymorphism
- C. Encapsulation and Abstraction
- D. Abstraction and Polymorphism

**2-11**. Which among the following doesn’t come under OOP concept?
- A. Data hiding
- B. Message passing
- C. Platform independent
- D. Data binding

**2-14**. Which among the following, for a pure OOP language, is true?
- A. The language should follow at least 1 feature of OOP
- B. The language must follow only 3 features of OOP
- C. The language must follow all the rules of OOP
- D. The language should follow 3 or more features of OOP

**2-17**. Which is not feature of OOP in general definitions?
- A. Code reusability
- B. Modularity
- C. Duplicate/Redundant data
- D. Efficient Code

**2-18**. Which feature allows open recursion, among the following?
- A. Use of this pointer
- B. Use of pointers
- C. Use of pass by value
- D. Use of parameterized constructor

**2-22**. Which of the following pairs are similar?
- A. Class and object
- B. Class and structure
- C. Structure and object
- D. Structure and functions

**2-23**. If a function can perform more than 1 type of tasks, where the function name remains same, which feature of OOP is used here?
- A. Encapsulation
- B. Inheritance
- C. Polymorphism
- D. Abstraction

**2-24**. If different properties and functions of a real world entity is grouped or embedded into a single element, what is it called in OOP language?
- A. Inheritance
- B. Polymorphism
- C. Abstraction
- D. Encapsulation

**2-27**. Which among the following best defines abstraction?
- A. Hiding the implementation
- B. Showing the important data
- C. Hiding the important data
- D. Hiding the implementation and showing only the features

**2-30**. Abstraction gives higher degree of ________
- A. Class usage
- B. Program complexity
- C. Idealized interface
- D. Unstable interface

**2-31**. Which among the following can be viewed as combination of abstraction of data and code.
- A. Class
- B. Object
- C. Inheritance
- D. Interfaces

**2-32**. Abstraction principle includes___________
- A. Use abstraction at its minimum
- B. Use abstraction to avoid longer codes
- C. Use abstraction whenever possible to avoid duplication
- D. Use abstraction whenever possible to achieve OOP

**2-33**. Encapsulation and abstraction differ as ____________
- A. Binding and Hiding respectively
- B. Hiding and Binding respectively
- C. Can be used any way
- D. Hiding and hiding respectively

**2-36**. A phone is made up of many components like motherboard, camera, sensors and etc. If the processor represents all the functioning of phone, display shows the display only, and the phone is represented as a whole. Which among the following have highest level of abstraction?
- A. Motherboard
- B. Display
- C. Camera
- D. Phone

**2-38**. Using higher degree of abstraction __________
- A. May get unsafe
- B. May reduce readability
- C. Can be safer
- D. Can increase vulnerability

**2-40**. Identify the correct statement.
- A. Namespace is used to group class, objects and functions
- B. Namespace is used to mark the beginning of the program
- C. A namespace is used to separate the class, objects
- D. Namespace is used to mark the beginning & end of the program

### Operators and Object Semantics

**2-39**. Which operator is used to signify the namespace?
- A. conditional operator
- B. ternary operator
- C. scope operator
- D. bitwise operator

### Classes and Objects

**2-3**. The static member functions __________________
- A. Have access to all the members of a class
- B. Have access to only constant members of a class
- C. Have access to only the static members of a class
- D. Have direct access to all other class members also

**2-6**. Which of the following best defines a class?
- A. Parent of an object
- B. Instance of an object
- C. Blueprint of an object
- D. Scope of an object

**2-12**. Which feature of OOP is indicated by the following code?
class student{  int marks;  };
class topper:public student{  int age;  topper(int age){ this.age=age; } };
- A. Encapsulation and Inheritance
- B. Inheritance and polymorphism
- C. Polymorphism
- D. Inheritance

**2-13**. The feature by which one object can interact with another object is _____________
- A. Message reading
- B. Message Passing
- C. Data transfer
- D. Data Binding

**2-16**. What is an abstraction in object-oriented programming?
- A. Hiding the implementation and showing only the features
- B. Hiding the important data
- C. Hiding the implementation
- D. Showing the important data

**2-19**. Which is most appropriate comment on following class definition?

class Student

{

```cpp
int a;
public : float a;
```

};
- A. Error : same variable name can’t be used twice
- B. Error : Public must come first
- C. Error : data types are different for same variable
- D. It is correct

**2-21**. Which among the following is false, for a member function of a class?
- A. All member functions must be defined
- B. Member functions can be defined inside or outside the class body
- C. Member functions need not be declared inside the class definition
- D. Member functions can be made friend to another class using the friend keyword

**2-26**. The feature by which one object can interact with another object is _____________
- A. Data transfer
- B. Data Binding
- C. Message Passing
- D. Message reading

**2-28**. Class is _________ abstraction.
- A. Object
- B. Logical
- C. Real
- D. Hypothetical

**2-29**. Object is ________ abstraction.
- A. Object
- B. Logical
- C. Real
- D. Hypothetical

**2-35**. If two classes combine some private data members and provides public member functions to access and manipulate those data members. Where is abstraction used?
- A. Using private access specifier for data members
- B. Using class concept with both data members and member functions
- C. Using public member functions to access and manipulate the data members
- D. Data is not sufficient to decide what is being used

### Namespace and Scope

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
        cout << "I'm a Mammal
";
    }

    ~Mammal() {}
};

class Human : public Mammal
{
public:
    Human()
    {
        cout << "I'm a Human
";
    }
};

class Male : public Human
{
public:
    Male()
    {
        cout << "I'm a Male
";
    }
};

class Female : public Human
{
public:
    Female()
    {
        cout << "I'm a Female
";
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

**2-10**. Which header file is required in C++ to use OOP?
- A. OOP can be used without using any header file
- B. stdlib.h
- C. iostream.h
- D. stdio.h

**2-41**. What is the use of Namespace?
- A. To encapsulate the data
- B. To structure a program into logical units
- C. Encapsulate the data & structure a program into logical units
- D. It is used to mark the beginning of the program

**2-42**. What is the general syntax for accessing the namespace variable?
- A. namespace::operator
- B. namespace,operator
- C. namespace#operator
- D. namespace$operator

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

**2-44**. What will be the output of the following C++ code?

#include <iostream.h>

```cpp
using namespace std;

namespace first
{
int x = 5;
int y = 10;
}
namespace second
{
double x = 3.1416;
double y = 2.7183;
}
int main ()
{
using first::x;
using second::y;
bool a, b;
a = x > y;
b = first::y < second::x;
cout << a << b;
return 0;
}
```
- A. 11
- B. 01
- C. 00
- D. 10

**2-45**. What will be the output of the following C++ code?

#include <iostream.h>

```cpp
using namespace std;
namespace Box1
{
int a = 4;
}
namespace Box2
{
int a = 13;
}
int main ()
{
int a = 16;
Box1::a;
Box2::a;
cout << a;
return 0;
}
```
- A. 4
- B. 13
- C. 16
- D. compile time error

**2-46**. What will be the output of the following C++ code?

#include <iostream.h>

```cpp
using namespace std;
namespace space
{
int x = 10;
}
namespace space
{
int y = 15;
}
int main(int argc, char * argv[])
{
space::x = space::y =5;
cout << space::x << space::y;
}
```
- A. 1015
- B. 1510
- C. 55
- D. compile time error

**2-47**. What will be the output of the following C++ code?

#include <iostream.h>

```cpp
using namespace std;
namespace extra
{
int i;
}
void i()
{
using namespace extra;
int i;
i = 9;
cout << i;
}
int main()
{
enum  letter { i, j};
class i { letter j; };
::i();
return 0;
}
```
- A. 9
- B. 10
- C. compile time error
- D. 11

**2-48**. Which keyword is used to access the variable in the namespace?
- A. using
- B. dynamic
- C. const
- D. static

**2-49**. Pick the incorrect statement for namespaces in C++.
- A. Namespace declarations are always global scope
- B. Keyword namespace is used at the starting of a namespace definition
- C. Namespace has access specifiers like private or public
- D. Namespace definitions can be nested

**2-50**. Which is the correct syntax of declaring a namespace?
- A. namespace A{
    int i
}
- B. namespace B{
    int i;
};
- C. namespace C{
    int i;
}
- D. Namespace D{
    int i
}

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

**2-55**. What is the correct syntax of defining a namespace?
- A. namespace name{}
- B. Namespace name{};
- C. namespace name{};
- D. typedef namespace name{} NAME

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

### Inheritance and Derivation

**2-15**. In multilevel inheritance, which is the most significant feature of OOP used?
- A. Code efficiency
- B. Code readability
- C. Flexibility
- D. Code reusability

## Answers

### Miscellaneous

- **2-1**: B. A variable should be created to catch the exception 中文解释/结论：C++ 中 `catch` 子句通常用形参变量接收异常对象。 易错点：不是必须显式创建普通对象，`catch(Type e)` 的 `e` 才是接收者。
- **2-7**: D. Inheritance 中文解释/结论：代码复用最典型靠继承。 易错点：封装和抽象不直接等同于“复用”。
- **2-8**: B. Code must contain at least one class 中文解释/结论：C++ 不要求程序必须包含类。 易错点：C++ 不是纯 OOP 语言。
- **2-9**: C. Encapsulation and Abstraction 中文解释/结论：封装和抽象关系最紧密。 易错点：多态常和继承配合，但这里不是最佳对应。
- **2-11**: C. Platform independent 中文解释/结论：平台无关不属于 OOP 核心概念。 易错点：别把语言特性和面向对象特性混在一起。
- **2-14**: C. The language must follow all the rules of OOP 中文解释/结论：所谓纯 OOP 语言应满足完整 OOP 规则。 易错点：这里按“纯面向对象语言”的严格定义理解。
- **2-17**: C. Duplicate/Redundant data 中文解释/结论：冗余数据不是 OOP 特征。 易错点：模块化、复用性才是正向特征。
- **2-18**: A. Use of this pointer 中文解释/结论：开放递归和 `this` 指针联系最紧。 易错点：普通指针和传值不是这里的核心。
- **2-22**: B. Class and structure 中文解释/结论：类和结构体最相似。 易错点：两者差别主要是默认访问权限，不是本质模型差别。
- **2-23**: C. Polymorphism 中文解释/结论：同名函数完成不同任务体现多态。 易错点：这里通常考函数重载。
- **2-24**: D. Encapsulation 中文解释/结论：把属性和行为装进一个单元是封装。 易错点：不要误判成抽象。
- **2-27**: D. Hiding the implementation and showing only the features 中文解释/结论：抽象最完整的定义是“隐藏实现，只展示功能”。 易错点：只选“隐藏实现”不够完整。
- **2-30**: C. Idealized interface 中文解释/结论：抽象提供理想化接口。 易错点：抽象通常降低复杂度，不会提高复杂度。
- **2-31**: A. Class 中文解释/结论：类可以看成数据抽象和代码抽象的结合。 易错点：对象是实例，不是抽象定义本体。
- **2-32**: C. Use abstraction whenever possible to avoid duplication 中文解释/结论：抽象应尽量用于提炼共性、减少重复。 易错点：不是为了“写更长代码”。
- **2-33**: A. Binding and Hiding respectively 中文解释/结论：封装强调把数据和操作绑定在一起，抽象强调隐藏实现。 易错点：这是常见教材表述；注意 abstraction 不只是 data hiding。
- **2-36**: D. Phone 中文解释/结论：手机整体的抽象层次高于主板、摄像头、显示屏。 易错点：抽象层次越高，表示越整体。
- **2-38**: C. Can be safer 中文解释/结论：更高层抽象通常更安全。 易错点：抽象不是降低可读性，而是减少不必要暴露。
- **2-40**: A. Namespace is used to group class, objects and functions 中文解释/结论：命名空间用于给类、对象、函数等分组。 易错点：它不是程序起止标记。

### Operators and Object Semantics

- **2-39**: C. scope operator 中文解释/结论：命名空间使用作用域解析运算符 `::`。 易错点：不是三目运算符，也不是条件运算符。

### Classes and Objects

- **2-3**: C. Have access to only the static members of a class 中文解释/结论：静态成员函数只能直接访问静态成员。 易错点：静态成员函数没有 `this` 指针。
- **2-6**: C. Blueprint of an object 中文解释/结论：类是对象的蓝图。 易错点：对象才是实例，类不是实例。
- **2-12**: A. Encapsulation and Inheritance 中文解释/结论：代码中 `student` 和 `topper` 把数据放入类中，并且 `topper` 继承 `student`。 易错点：只看到 `public student` 容易漏掉类本身体现的封装。
- **2-13**: B. Message Passing 中文解释/结论：对象之间交互叫消息传递。 易错点：不是 data binding。
- **2-16**: A. Hiding the implementation and showing only the features 中文解释/结论：抽象是隐藏实现、暴露接口。 易错点：单纯“隐藏重要数据”更像信息隐藏，不够完整。
- **2-19**: A. Error : same variable name can't be used twice 中文解释/结论：同一类里不能定义两个同名数据成员。 易错点：即使类型不同也不行。
- **2-21**: C. Member functions need not be declared inside the class definition 中文解释/结论：成员函数必须先在类里声明。 易错点：可以在类外定义，但不能完全不在类定义中声明。
- **2-26**: C. Message Passing 中文解释/结论：对象交互仍然叫消息传递。 易错点：和 2-13 是重复考点。
- **2-28**: B. Logical 中文解释/结论：类是逻辑抽象。 易错点：类不是现实实体本身。
- **2-29**: C. Real 中文解释/结论：对象是类的实际实例，通常表示现实中的具体实体。 易错点：类更偏逻辑抽象，对象更偏具体实体。
- **2-35**: C. Using public member functions to access and manipulate the data members 中文解释/结论：通过公有成员函数操作私有数据体现抽象。 易错点：私有数据本身更像封装/隐藏，公有接口才是抽象入口。

### Namespace and Scope

- **2-4**: A. I'm a Mammal 中文解释/结论：创建派生类对象时，构造顺序是基类到派生类。 易错点：不是先执行最底层类的构造函数。

I'm a Human

I'm a Male
- **2-10**: A. OOP can be used without using any header file 中文解释/结论：OOP 不依赖某个专门头文件。 易错点：`iostream` 只是输入输出库，不是 “OOP 头文件”。
- **2-41**: B. To structure a program into logical units 中文解释/结论：命名空间用于把程序组织成逻辑单元。 易错点：它不负责数据封装。
- **2-42**: A. namespace::operator 中文解释/结论：访问命名空间成员的形式是 `namespace::name`。 易错点：符号必须是双冒号。
- **2-43**: B. 8 中文解释/结论：`int` 接收 `5 + 3.1416` 会截断成 `8`。 易错点：不是四舍五入。
- **2-44**: D. 10 中文解释/结论：布尔值输出为 `1` 和 `0`，所以结果是 `10`。 易错点：`true/false` 默认不会直接打印英文。
- **2-45**: C. 16 中文解释/结论：未限定名 `a` 取局部变量 `16`。 易错点：写了 `Box1::a;` 不等于输出了它。
- **2-46**: C. 55 中文解释/结论：同名命名空间可分开定义，最后合并。 易错点：这不是重定义错误。
- **2-47**: A. 9 中文解释/结论：局部变量 `i=9` 屏蔽了其他同名实体，输出 `9`。 易错点：函数内最近作用域优先。
- **2-48**: A. using 中文解释/结论：`using` 可将命名空间成员引入当前作用域。 易错点：直接限定访问用 `::`，但该题选项里问 keyword，所以选 `using`。
- **2-49**: C. Namespace has access specifiers like private or public 中文解释/结论：命名空间没有 `public/private` 访问说明符。 易错点：类有访问控制，命名空间没有。
- **2-50**: C. namespace C{ 中文解释/结论：命名空间定义语法是 `namespace Name { ... }`。 易错点：`Namespace` 大写不对，末尾分号也不是必须。
 int i;
  }
- **2-51**: C. Error 中文解释/结论：`B::cout` 和标准库 `cout` 同名会引发冲突。 易错点：`using namespace` 很容易制造名字污染。
- **2-52**: A. 5 中文解释/结论：引入 `B` 后，未限定名 `var` 绑定到 `B::var`，输出 `5`。 易错点：不是优先找前面定义的 `A::var`。
- **2-53**: C. 20 中文解释/结论：局部变量 `var=20` 屏蔽命名空间同名变量，输出 `20`。 易错点：局部作用域优先级最高。
- **2-54**: A. 10 中文解释/结论：匿名命名空间成员在当前翻译单元可直接用，输出 `10`。 易错点：匿名命名空间不是“不可访问”。
- **2-55**: A. namespace name{} 中文解释/结论：定义命名空间的基本写法是 `namespace name {}`。 易错点：关键字必须小写。
- **2-56**: C. cout<<A::B::i; 中文解释/结论：嵌套命名空间成员要写全路径 `A::B::i`。 易错点：不能直接写 `B::i`，因为 `B` 在 `A` 内部。
using namespace B20
using namespace A20
- **2-60**: B. Declare both functions inside different namespaces 中文解释/结论：避免同名同参函数重定义的直接办法是放入不同命名空间。 易错点：改头文件名不能解决符号冲突。

### Inheritance and Derivation

- **2-15**: D. Code reusability 中文解释/结论：多级继承最突出的是代码复用。 易错点：不要把“可读性”当核心收益。
