# c++练习题目三：派生和继承

## Questions

### Inheritance and Derivation

**2-1**. Which type of members can’t be accessed in derived classes of a base class?
- A. All can be accessed
- B. Protected
- C. Private
- D. Public

**2-2**. Which among the following can restrict class members to get inherited?
- A. Private
- B. Protected
- C. Public
- D. All three

**2-3**. Which specifier allows a programmer to make the private members which can be inherited?
- A. Private
- B. Default
- C. Protected
- D. Protected and default

**2-5**. If class A has add() function with protected access, and few other members in public. Then class B inherits class A privately. Will the user will not be able to call _________ from the object of class B.
- A. Any function of class A
- B. The add() function of class A
- C. Any member of class A
- D. Private, protected and public members of class A

**2-6**. If class B inherits class A privately. And class B has a friend function. Will the friend function be able to access the private member of class A?
- A. Yes, because friend function can access all the members
- B. Yes, because friend function is of class B
- C. No, because friend function can only access private members of friend class
- D. No, because friend function can access private member of class A also

**2-7**. Which access specifier should be used so that all the parent class members can be inherited and accessed from outside the class?
- A. Private
- B. Default or public
- C. Protected or private
- D. Public

**2-8**. Which access specifier is/are most secure during inheritance?
- A. Private
- B. Default
- C. Protected
- D. Private and default

**2-9**. If the protected members are to be made accessible only to the nearest subclass and no further subclasses, which access specifier should be used in inheritance?
- A. The sub class should inherit the parent class privately
- B. The sub class should inherit the parent class as protected
- C. The sub class should inherit the parent class as public
- D. The sub class can use any access modifier

**2-11**. If protected inheritance is used then _____
- A. Public members become public in subclass
- B. Protected members become public in subclass
- C. Protected members become protected in subclass
- D. Protected and Public members become protected in subclass

**2-16**. A class has its default constructor defined as public. Class B inherits class A privately. The class ___________
- A. B will not be able to have instances
- B. Only A can have instances
- C. Only B can have instances
- D. Both classes can have instances

**2-17**. Which specifier can be used to inherit protected members as protected in subclass but public as public in subclass?
- A. Private
- B. Default
- C. Public
- D. Protected

**2-18**. In multi-level inheritance(all public), the public members of parent/superclass will ________
- A. Will continue to get inherited subsequently
- B. Will not be inherited after one subclass inheritance
- C. Will not be available to be called outside class
- D. Will not be able to allocated with any memory space

**2-19**. Which specifier allows to secure the public members of base class in inherited classes?
- A. Private
- B. Protected
- C. Public
- D. Private and Protected

**2-21**. If a base class is inherited in protected access mode then which among the following is true?
- A. Public and Protected members of base class becomes protected members of derived class
- B. Only protected members become protected members of derived class
- C. Private, Protected and Public all members of base, become private of derived class
- D. Only private members of base, become private of derived class

**2-22**. Members which are not intended to be inherited are declared as ________________
- A. Public members
- B. Protected members
- C. Private members
- D. Private or Protected members

**2-23**. While inheriting a class, if no access mode is specified, then which among the following is true? (in C++)
- A. It gets inherited publicly by default
- B. It gets inherited protected by default
- C. It gets inherited privately by default
- D. It is not possible

**2-24**. How can you make the private members inheritable?
- A. By making their visibility mode as public only
- B. By making their visibility mode as protected only
- C. By making their visibility mode as private in derived class
- D. It can be done both by making the visibility mode public or protected

**2-25**. Which type of inheritance is illustrated by the following code?

class student{ public: int marks; };

class topper: public student { public: char grade; };

class average{ public: int makrs_needed; };

class section: public average{ public: char name[10];  };

class overall: public average{  public: int students;  };
- A. Single level
- B. Multilevel and single level
- C. Hierarchical
- D. Hierarchical and single level

**2-26**. Which among the following best describes multiple inheritance?
- A. Two classes being parent of any other classes
- B. Three classes being parent of other classes
- C. More than one class being parent of other child classes
- D. More than one class being parent of single child

**2-27**. Which type of inheritance results in the diamond problem?
- A. Single level
- B. Hybrid
- C. Hierarchical**
- D. Multilevel

**2-29**. If class A has two nested classes B and C. Class D has one nested class E, and have inherited class A. If E inherits B and C, then ________________
- A. It shows multiple inheritance
- B. It shows hierarchical inheritance
- C. It shows multiple inheritance
- D. Multiple inheritance among nested classes, and single level for enclosing classes

**2-30**. Which among the following defines single level inheritance?
- A. One base class derives another class
- B. One derived class inherits from one base class
- C. One base class inherits from one derived class
- D. One derived class derives from another derived class

**2-31**. If class A and class B are derived from class C and class D, then ________________
- A. Those are 2 pairs of single inheritance
- B. That is multilevel inheritance
- C. Those is enclosing class
- D. Those are all independent classes

**2-32**. Single level inheritance supports _____________ inheritance.
- A. Runtime
- B. Compile time
- C. Multiple inheritance
- D. Language independency

**2-34**. Which among the following is false for single level inheritance?
- A. There can be more than 2 classes in program to implement single inheritance
- B. There can be exactly 2 classes to implement single inheritance in a program**
- C. There can be more than 2 independent classes involved in single inheritance
- D. The derived class must implement all the abstract method if single inheritance is used

**2-35**. Which among the following best defines multilevel inheritance?
- A. A class derived from another derived class
- B. Classes being derived from other derived classes
- C. Continuing single level inheritance
- D. Class which have more than one parent

**2-36**. If all the classes use private inheritance in multilevel inheritance then ______________
- A. It will not be called multilevel inheritance
- B. Each class can access only non-private members of its parent
- C. Each subsequent class can access all members of previous level parent classes
- D. None of the members will be available to any other class

**2-37**. In multilevel inheritance one class inherits _______________
- A. Only one class
- B. More than one class
- C. At least one class
- D. As many classes as required

**2-39**. If class A inherits class B and class C as “class A: public class B, public class C {// class body ;}; ”, which class constructor will be called first?
- A. Class A
- B. Class B
- C. Class C
- D. All together

**2-40**. Why does diamond problem arise due to multiple inheritance?
- A. Methods with same name creates ambiguity and conflict
- B. Methods inherited from the superclass may conflict
- C. Derived class gets overloaded with more than two class methods
- D. Derived class can’t distinguish the owner class of any derived method

**2-42**. Which member can never be accessed by inherited classes?
- A. Private member function
- B. Public member function
- C. Protected member function替换为正确项
- D. All can be accessed

**2-43**. If public members are to be restricted from getting inherited from the subclass of the class containing that function, which alternative is best?
- A. Make the function private
- B. Use private inheritance
- C. Use public inheritance
- D. Use protected inheritance

**2-44**. Pointer to a base class can be initialized with the address of derived class, because of _________
- A. derived-to-base implicit conversion for pointers
- B. base-to-derived implicit conversion for pointers
- C. base-to-base implicit conversion for pointers
- D. derived-to-derived implicit conversion for pointers

**2-45**. If in multiple inheritance, class C inherits class B, and Class B inherits class A. In which sequence are their destructors called if an object of class C was declared?
- A. ~A() then ~B() then ~C()
- B. ~C() then ~A() then ~B()
- C. ~C() then ~B() then ~A()
- D. ~B() then ~C() then ~A()

**2-46**. In multiple inheritance, if class C inherits two classes A and B as follows, which class constructor will be called first?

class A{ };

class B{ };

class C: public A, public B{  };
- A. A()
- B. B()
- C. C()
- D. Can’t be determined

**2-47**. Can constructors be overloaded in derived class?
- A. Yes, always
- B. Yes, if derived class has no constructor
- C. No, programmer can’t do it
- D. No, never

**2-48**. If in multiple inheritance, class C inherits class B, and Class B inherits class A. In which sequence are their destructors called if an object of class C was declared?
- A. ~C() then ~B() then ~A()
- B. ~B() then ~C() then ~A()
- C. ~A() then ~B() then ~C()
- D. ~C() then ~A() then ~B()

**2-53**. If there are 5 classes, E is derived from D, D from C, C from B and B from A. Which class constructor will be called first if the object of E or D is created?
- A. A
- B. B
- C. C
- D. A and B

**2-54**. If there are 3 classes. Class C is derived from class B and B is derived from A, Which class destructor will be called at last if object of C is destroyed.
- A. A
- B. B
- C. C
- D. All together

**2-55**. Is it compulsory for all the classes in multilevel inheritance to have constructors defined explicitly if only last derived class object is created?
- A. Yes, always
- B. Yes, to initialize the members
- C. No, it not necessary
- D. No, Constructor must not be defined

### Miscellaneous

**2-4**. Which among the following is false?
- A. Private members can be accessed using friend functions
- B. Member functions can be made private
- C. Default members can’t be inherited
- D. Public members are accessible from other classes also

### Classes and Objects

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

**2-12**. If protected members are to be accessed from outside the class then__________
- A. Members must be inherited publicly in subclass
- B. Members must accessed using class pointers
- C. Members must be accessed as usual
- D. Members must be made public

**2-13**. Which among the following can use protected access specifier?
- A. Members which may be used in other packages
- B. Members which have to be secure and should be used by other packages/subclass
- C. Members which have to be accessed from anywhere in the program
- D. Members which have to be as secure as private but can be used by main() function

**2-15**. If members of a super class are public, then_______
- A. All those will be available in subclasses
- B. None of those will be available in subclasses
- C. Only data members will be available in subclass
- D. Only member functions will be available in subclass

**2-20**. Which among the following is not possible for member function?
- A. Access protected members of parent class
- B. Definition without return type
- C. Access public members of subclass
- D. Access static members of class

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

**2-51**. When an object is passed to a function, its copy is made in the function and then ______________
- A. The destructor of the copy is called when function is returned
- B. The destructor is never called in this case
- C. The destructor is called but it is always implicit
- D. The destructor must be user defined

**2-52**. What happens when an object is passed by reference?
- A. Destructor is not called
- B. Destructor is called at end of function
- C. Destructor is called when function is out of scope
- D. Destructor is called when called explicitly

### Constructors and Destructors

**2-14**. If a class have default constructor defined in private access, and one parameter constructor in protected mode, how will it be possible to create instance of object?
- A. Define a constructor in public access with different signature
- B. Directly create the object in the subclass
- C. Directly create the object in main() function
- D. Not possible

**2-49**. Choose the correct sequence of destructors being called for the following code.

class A{   };

class B{   };

class C: public A, public B{   };
- A. ~A(), ~B(), ~C()
- B. ~B(), ~C(), ~A()
- C. ~A(), ~C(), ~B()
- D. ~C(), ~B(), ~A()

**2-50**. Which class destructor will be called first, when following code go out of scope?

```C++
class A{  };

class B{  };

class C: public B{  };

A a;

B b;

C c;
```

- A. ~A()
- B. ~B()
- C. ~C()
- D. ~B() and ~C()

## Answers

### Inheritance and Derivation

- **2-1**: C. Private 中文解释/结论：派生类不能直接访问基类的 `private` 成员。 易错点：`protected` 可以被派生类访问。
- **2-2**: A. Private 中文解释/结论：private 成员最能限制派生类直接访问。 易错点：私有成员仍存在于基类子对象中，只是派生类不可直接访问。
- **2-3**: C. Protected 中文解释/结论：想让成员可被派生类访问，应使用 `protected`。 易错点：`private` 不能被派生类直接访问。
- **2-5**: C. Any member of class A 中文解释/结论：私有继承后，类外不能通过子类对象访问基类成员。 易错点：派生类内部仍可访问基类的非私有成员。
- **2-6**: C. No, because friend function can only access private members of friend class 中文解释/结论：友元函数只能访问它作为友元的那个类的私有成员。 易错点：成为 B 的友元，不等于能访问 A 的私有成员。
- **2-7**: D. Public 中文解释/结论：要让父类成员继承后仍可从类外访问，应使用 `public` 继承。 易错点：`private/protected` 继承会收紧访问权限。
- **2-8**: A. Private 中文解释/结论：private 继承最严格，最能隐藏基类接口。 易错点：protected 仍对子类开放。
- **2-9**: A. The sub class should inherit the parent class privately 中文解释/结论：私有继承可阻止成员继续作为 protected/public 向后暴露。 易错点：实际还要结合成员访问权限与继承方式一起判断。
- **2-11**: D. Protected and Public members become protected in subclass 中文解释/结论：保护继承会把基类 public 和 protected 成员都变为派生类 protected 成员。 易错点：public 不再保持 public。
- **2-16**: D. Both classes can have instances 中文解释/结论：私有继承不影响基类和派生类各自创建实例。 易错点：继承访问权限不是对象能否创建的直接条件。
- **2-17**: C. Public 中文解释/结论：public 继承保持 public 为 public、protected 为 protected。 易错点：protected 继承会把 public 变 protected。
- **2-18**: A. Will continue to get inherited subsequently 中文解释/结论：多级 public 继承中 public 成员会继续向下继承。 易错点：不会只继承一层就消失。
- **2-19**: D. Private and Protected 中文解释/结论：private/protected 继承都会降低基类 public 成员对外可见性。 易错点：public 继承不会保护 public 接口。
- **2-21**: A. Public and Protected members of base class becomes protected members of derived class 中文解释/结论：protected 继承时，基类 public/protected 成员在派生类中都变 protected。 易错点：private 成员仍不能被派生类直接访问。
- **2-22**: C. Private members 中文解释/结论：不希望被继承类直接访问的成员应设为 private。 易错点：protected 是专门给派生类访问的。
- **2-23**: C. It gets inherited privately by default 中文解释/结论：C++ 中 class 继承默认是 private。 易错点：struct 默认 public，class 默认 private。
- **2-24**: B. By making their visibility mode as protected only 中文解释/结论：若想让派生类继承并访问，应把 private 改成 protected。 易错点：改成 public 也可访问但破坏封装，题目更应选 protected。
- **2-25**: D. Hierarchical and single level 中文解释/结论：示例同时体现层次继承和单继承。 易错点：一个基类派生多个子类是 hierarchical inheritance。
- **2-26**: D. More than one class being parent of single child 中文解释/结论：多个父类派生一个子类是多继承。 易错点：不是“多个类各自当父类”就一定是多继承。
- **2-27**: B. Hybrid 中文解释/结论：菱形继承通常是混合继承结构导致的。 易错点：多继承参与其中，但选项里 hybrid 更贴切。
- **2-29**: D. Multiple inheritance among nested classes, and single level for enclosing classes 中文解释/结论：题中嵌套类体现多继承，外围类体现单继承。 易错点：同名选项有重复，按更完整描述选。
- **2-30**: B. One derived class inherits from one base class 中文解释/结论：一个派生类继承一个基类是单继承。 易错点：方向是 derived class inherits base class。
- **2-31**: A. Those are 2 pairs of single inheritance 中文解释/结论：A 从 C、B 从 D 派生，是两组单继承。 易错点：不是多级继承。
- **2-32**: B. Compile time 中文解释/结论：单继承关系在编译期确定。 易错点：不要和虚函数运行期多态混淆。
- **2-34**: D. The derived class must implement all the abstract method if single inheritance is used 中文解释/结论：这是抽象类规则，不是单继承的一般规则。 易错点：单继承不要求必须实现抽象方法，除非要实例化具体类。
- **2-35**: A. A class derived from another derived class 中文解释/结论：多级继承是一个类从另一个派生类继续派生。 易错点：多个父类是多继承，不是多级继承。
- **2-36**: B. Each class can access only non-private members of its parent 中文解释/结论：多级私有继承中，每级只能访问直接父类的非私有成员。 易错点：不能跨级访问所有祖先成员。
- **2-37**: A. Only one class 中文解释/结论：多级继承中每一层直接继承一个类。 易错点：不是一个类同时继承多个类。
- **2-39**: B. Class B 中文解释/结论：多继承构造按继承列表顺序，先构造 B。 易错点：不是先构造派生类 A。
- **2-40**: A. Methods with same name creates ambiguity and conflict 中文解释/结论：菱形问题常因同名或重复继承成员造成歧义。 易错点：根源是继承路径造成的不明确。
- **2-42**: A. Private member function 中文解释/结论：private 成员函数不能被继承类直接访问。 易错点：public/protected 才能按规则被派生类访问。
- **2-43**: B. Use private inheritance 中文解释/结论：要限制 public 成员继续对外暴露，可使用 private 继承。 易错点：把函数改 private 会影响基类自身接口。
- **2-44**: A. derived-to-base implicit conversion for pointers 中文解释/结论：基类指针可指向派生类对象，靠派生到基类的隐式转换。 易错点：反向转换不自动安全成立。
- **2-45**: C. ~C() then ~B() then ~A() 中文解释/结论：析构顺序与构造相反，C -> B -> A。 易错点：先析构最派生类。
- **2-46**: A. A() 中文解释/结论：`class C: public A, public B` 先构造 A。 易错点：构造顺序按继承列表，不按初始化列表。
- **2-47**: A. Yes, always 中文解释/结论：派生类构造函数可以重载。 易错点：构造函数没有返回类型，但可按参数列表重载。
- **2-48**: A. ~C() then ~B() then ~A() 中文解释/结论：多级继承析构仍是 C -> B -> A。 易错点：和构造顺序正好相反。
- **2-53**: A. A 中文解释/结论：多级继承构造从最顶层基类 A 开始。 易错点：创建 E 或 D 都要先构造 A。
- **2-54**: A. A 中文解释/结论：多级继承析构最后调用最顶层基类 A 的析构。 易错点：构造先 A，析构最后 A。
- **2-55**: C. No, it is not necessary 中文解释/结论：不是每个类都必须显式定义构造函数。 易错点：编译器可生成默认构造函数，前提是可用。

### Miscellaneous

- **2-4**: C. Default members can't be inherited 中文解释/结论：C++ 没有所谓独立的 default 成员不能继承这一规则。 易错点：class 默认 private，但不是“default members”。

### Classes and Objects

- **2-10**: A. Object b can't access disp() function 中文解释/结论：`protected` 继承后，类外对象不能访问原 public 成员。 易错点：`b.disp()` 在类外不可调用。
- **2-12**: D. Members must be made public 中文解释/结论：要从类外访问 protected 成员，必须通过 public 接口暴露。 易错点：protected 本身不能被类外直接访问。
- **2-13**: B. Members which have to be secure and should be used by other subclasses 中文解释/结论：`protected` 适合对子类开放、对外部隐藏的成员。 易错点：它不是给 `main()` 直接访问用的。
- **2-15**: A. All those will be available in subclasses 中文解释/结论：父类 public 成员会在子类中可用。 易错点：继承方式会影响类外可见性。
- **2-20**: C. Access public members of subclass 中文解释/结论：成员函数不能随意访问子类 public 成员。 易错点：基类不知道未来派生类的成员。
- **2-28**: D. Single level inheritance is used, with both enclosing and nested classes 中文解释/结论：示例同时有外围类单继承和嵌套类单继承。 易错点：嵌套类继承也要单独看。
- **2-51**: A. The destructor of the copy is called when function is returned 中文解释/结论：对象按值传参会产生副本，函数返回时副本析构。 易错点：析构的是副本，不是原对象。
- **2-52**: A. Destructor is not called 中文解释/结论：对象按引用传参不产生副本，因此函数结束不额外析构。 易错点：引用不是新对象。

### Constructors and Destructors

- **2-14**: B. Directly create the object in the subclass 中文解释/结论：默认构造私有、带参构造 protected 时，可在子类中创建对象。 易错点：类外 main 不能直接调用 protected 构造。
- **2-49**: D. ~C(), ~B(), ~A() 中文解释/结论：多继承析构先派生类，再按基类构造反序析构。 易错点：`class C: public A, public B` 构造 A 后 B，析构 B 后 A。
- **2-50**: C. ~C() 中文解释/结论：局部对象按创建的反序析构，先析构 `c`，即 `~C()`。 易错点：不是按类定义顺序。
