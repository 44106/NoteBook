# c++练习题目五：多态与虚函数

说明：已保留带明确答案的题目，少数题干做了规范化；个别原文带有 Java 风格措辞的题目，按原题意保留。

## 题目与答案

### 继承与多态概念

**2-1**. 以下说法正确的是？
- A. 派生类可以和基类有同名成员函数，但是不能有同名成员变量
- B. 派生类的成员函数中，可以调用基类的同名同参数表的成员函数
- C. 派生类和基类的同名成员函数必须参数表不同，否则就是重复定义
- D. 派生类和基类的同名成员变量存放在相同存储空间
- **答案：** B. 派生类的成员函数中，可以调用基类的同名同参数表的成员函数
- **解析：** 按题库对应概念，正确项是“派生类的成员函数中，可以调用基类的同名同参数表的成员函数”。

**2-2**. Which among the following can show polymorphism?
- A. Overloading &&
- B. Overloading <<
- C. Overloading ||
- D. Overloading +=
- **答案：** B. Overloading <<
- **解析：** 按题库对应概念，正确项是“Overloading <<”。

**2-3**. Which feature in OOP is used to allocate additional functions to a predefined operator in any language?
- A. Function Overloading
- B. Function Overriding
- C. Operator Overloading
- D. Operator Overriding
- **答案：** C. Operator Overloading
- **解析：** 题库考的是运算符重载规则，正确项是“Operator Overloading”。

**2-4**. How to overcome the diamond problem?
- A. Using seperate derived class
- B. Using virtual inheritance (virtual base classes)
- C. Can’t be done
- D. Using alias name
- **答案：** B. Using virtual inheritance (virtual base classes)
- **解析：** 菱形继承通常通过虚继承来避免基类重复出现。

**2-5**. ___________ underlines the feature of Polymorphism in a class.
- A. Virtual Function
- B. Inline function
- C. Enclosing class
- D. Nested class
- **答案：** A. Virtual Function
- **解析：** 按题库对应概念，正确项是“Virtual Function”。

### 虚函数与运行时多态

**2-6**. Destructors can be ________
- A. Abstract type
- B. Virtual
- C. Void
- D. Any type depending on situation
- **答案：** B. Virtual
- **解析：** 按题库对应概念，正确项是“Virtual”。

**2-7**. If a virtual member function is defined ___________
- A. It should not contain any body and defined by subclasses
- B. It must contain body and overridden by subclasses
- C. It must contain body and be overloaded
- D. It must not contain any body and should not be derived
- **答案：** A. It should not contain any body and defined by subclasses
- **解析：** 按题库对应概念，正确项是“It should not contain any body and defined by subclasses”。

**2-8**. Member functions of a generic class are _____________
- A. Not generic
- B. Automatically generic
- C. To be made generic explicitly
- D. Given default type as double
- **答案：** B. Automatically generic
- **解析：** 按题库对应概念，正确项是“Automatically generic”。

**2-9**. Virtual function is ______ class function which expected to be redefined in ______ class, so that when reference is made to derived class object using pointer then we can call virtual function to execute ________ class definition version.
- A. Base, derived, derived
- B. Derived, Derived, Derived
- C. Base, derived, base
- D. Base, base, derived
- **答案：** A. Base, derived, derived
- **解析：** 题库考的是虚函数/多态规则，正确项是“Base, derived, derived”。

**2-10**. What does a virtual function ensure for an object, among the following?
- A. Correct method is called, regardless of the class defining it
- B. Correct method is called, regardless of the object being called
- C. Correct method is called, regardless of the type of reference used for function call
- D. Correct method is called, regardless of the type of function being called by objects
- **答案：** C. Correct method is called, regardless of the type of reference used for function call
- **解析：** 按题库对应概念，正确项是“Correct method is called, regardless of the type of reference used for function call”。

**2-11**. Virtual functions are mainly used to achieve _____________
- A. Compile time polymorphism
- B. Interpreter polymorphism
- C. Runtime polymorphism
- D. Functions code polymorphism
- **答案：** C. Runtime polymorphism
- **解析：** 按题库对应概念，正确项是“Runtime polymorphism”。

**2-12**. Where the virtual function should be defined?
- A. Twice in base class
- B. Derived class
- C. Base class and derived class
- D. Base class
- **答案：** D. Base class
- **解析：** 按题库对应概念，正确项是“Base class”。

**2-13**. The resolving of virtual functions is done at ______________
- A. Compile time
- B. Interpret time
- C. Runtime
- D. Writing source code
- **答案：** C. Runtime
- **解析：** 按题库对应概念，正确项是“Runtime”。

**2-14**. In which access specifier should a virtual function be defined?
- A. Private
- B. Public
- C. Protected
- D. Default
- **答案：** B. Public
- **解析：** 按题库对应概念，正确项是“Public”。

**2-15**. Virtual functions can never be made _______________
- A. Static function
- B. Parameterized function
- C. Default argument function
- D. Zero parameter function
- **答案：** A. Static function
- **解析：** 按题库对应概念，正确项是“Static function”。

**2-16**. Which is a must condition for virtual function to achieve runtime polymorphism?
- A. Virtual function must be accessed with direct name
- B. Virtual functions must be accessed using base class object
- C. Virtual function must be accessed using pointer or reference
- D. Virtual function must be accessed using derived class object only
- **答案：** C. Virtual function must be accessed using pointer or reference
- **解析：** 按题库对应概念，正确项是“Virtual function must be accessed using pointer or reference”。

**2-17**. Which among the following is true for virtual functions?
- A. Prototype must be different in base and derived class
- B. Prototype must be same in base class and derived class
- C. Prototype must be given only in base class
- D. Prototype must have different signature in base and derived class
- **答案：** B. Prototype must be same in base class and derived class
- **解析：** 按题库对应概念，正确项是“Prototype must be same in base class and derived class”。

**2-18**. The virtual functions must be declared and defined in _____________ class and overridden in ___________ class.
- A. Base, base
- B. Derived, derived
- C. Derived, base
- D. Base, derived
- **答案：** D. Base, derived
- **解析：** 题库考的是虚函数/多态规则，正确项是“Base, derived”。

**2-19**. It is not necessary to redefine the virtual function in the derived class.
- A. Necessary
- B. Not necessary
- C. Not acceptable
- D. Good practice
- **答案：** B. Not necessary
- **解析：** 虚函数可以在派生类中重写，但不是必须重写。

**2-20**. Which among the following is true?
- A. A class may have virtual destructor but not virtual constructor
- B. A class may have virtual constructor but not virtual destructor
- C. A class may have virtual constructor and virtual constructor
- D. A class may have either virtual destructor or virtual constructor
- **答案：** A. A class may have virtual destructor but not virtual constructor
- **解析：** 按题库对应概念，正确项是“A class may have virtual destructor but not virtual constructor”。

**2-21**. If virtual function of base class is redefined in derived class then ________________
- A. It must be declared virtual in derived class also
- B. It may or may not be declared virtual in derived class
- C. It can must not be declared virtual in derived class
- D. It must be declared normally in derived class
- **答案：** B. It may or may not be declared virtual in derived class
- **解析：** 题库考的是虚函数/多态规则，正确项是“It may or may not be declared virtual in derived class”。

**2-22**. Which among the following is true?
- A. The abstract functions must be only declared in derived classes
- B. The abstract functions must not be defined in derived classes
- C. The abstract functions must be defined in base and derived class
- D. The abstract functions must be defined either in base or derived class
- **答案：** D. The abstract functions must be defined either in base or derived class
- **解析：** 按题库对应概念，正确项是“The abstract functions must be defined either in base or derived class”。

**2-23**. The virtual function overrides ____________
- A. Do not acquire base class declaration of default arguments
- B. Do acquire base class declaration of default arguments
- C. Do not link with the default arguments of base class
- D. Do link with the default argument but only of derived classes
- **答案：** A. Do not acquire base class declaration of default arguments
- **解析：** 按题库对应概念，正确项是“Do not acquire base class declaration of default arguments”。

**2-24**. Which type of function among the following shows polymorphism?
- A. Inline function
- B. Virtual function
- C. Undefined functions
- D. Class member functions
- **答案：** B. Virtual function
- **解析：** 按题库对应概念，正确项是“Virtual function”。

**2-25**. Which one is the characteristic of abstract class?
- A. May have virtual functions
- B. May have constructors overloaded
- C. May have friend function
- D. Can not make instance of this class
- **答案：** D. Can not make instance of this class
- **解析：** 题库考的是抽象类规则，正确项是“Can not make instance of this class”。

### 代码题

**2-26**. Given:

```cpp
class A {
A() {};
virtual f() {};
int i;
};
```

which statement is NOT true:
- A. i is private
- B. f() is an inline function
- C. i is a member of class A
- D. sizeof(A) == sizeof(int)
- **答案：** D. sizeof(A) == sizeof(int)
- **解析：** 题库考的是虚函数/多态规则，正确项是“sizeof(A) == sizeof(int)”。

**2-27**. Given:

```cpp
class A {
A() {}
virtual f() = 0;
int i;
};
```

which statement below is NOT true:
- A. i is private
- B. Objects of class A can not be created
- C. i is a member of class A
- D. sizeof(A) == sizeof(int)
- **答案：** D. sizeof(A) == sizeof(int)
- **解析：** 题库考的是虚函数/多态规则，正确项是“sizeof(A) == sizeof(int)”。

**2-28**. Given:

```cpp
class X {
int i;
virtual void f() {};
};
```

If sizeof(int *) == sizeof(int) == 4, then sizeof(X)==?
- A. 4
- B. 6
- C. 8
- D. Undetermined
- **答案：** C. 8
- **解析：** 题库考的是虚函数/多态规则，正确项是“8”。

**2-29**. Which class/set of classes can illustrate polymorphism in the following C++ code?

class student

{

   public :

```cpp
int marks;
calc_grade();
```

}

class topper:public student

{

```cpp
public : calc_grade()
{
return 10;
}
```

};

class average:public student

{

```cpp
public : calc_grade()
{
return 20;
}
```

};

class failed

{

```cpp
int marks;
```

};
- A. Only class student and topper together can show polymorphism
- B. Only class student can show polymorphism
- C. Class failed should also inherit class student for this code to work for polymorphism
- D. All class student, topper and average together can show polymorphism
- **答案：** D. All class student, topper and average together can show polymorphism
- **解析：** 按题库对应概念，正确项是“All class student, topper and average together can show polymorphism”。

### 抽象类

**2-30**. Instance of which type of class can’t be created?
- A. Parent class
- B. Abstract class
- C. Anonymous class
- D. Nested class
- **答案：** B. Abstract class
- **解析：** 按题库对应概念，正确项是“Abstract class”。

**2-31**. Which class can have member functions without their implementation?
- A. Default class
- B. String class
- C. Template class
- D. Abstract class
- **答案：** D. Abstract class
- **解析：** 按题库对应概念，正确项是“Abstract class”。

**2-32**. Which among the following is wrong?
- A. class student{ }; student s;
- B. abstract class student{ }; student s;
- C. abstract class student{ }s[50000000];
- D. abstract class student{ }; class toppers: public student{ }; topper t;
- **答案：** B. abstract class student{ }; student s;
- **解析：** 按题库对应概念，正确项是“abstract class student{ }; student s;”。

**2-33**. Which among the following is correct about abstract class destructors?
- A. It doesn’t have destructors
- B. It has destructors
- C. It may or may not have destructors
- D. It contains an implicit destructor
- **答案：** B. It has destructors
- **解析：** 抽象类也可以有析构函数，实际工程里经常还会把它设为虚析构。

**2-34**. If an abstract class has all the private members, then _________
- A. No class will be able to implement members of abstract class
- B. Only single inheritance class can implement its members
- C. Only other enclosing classes will be able to implement those members
- D. No class will be able to access those members but can implement.
- **答案：** D. No class will be able to access those members but can implement.
- **解析：** 题库考的是抽象类规则，正确项是“No class will be able to access those members but can implement.”。

**2-35**. Which among the following best describes abstract classes?
- A. If a class has more than one virtual function, it’s abstract class
- B. If a class have only one pure virtual function, it’s abstract class
- C. If a class has at least one pure virtual function, it’s abstract class
- D. If a class has all the pure virtual functions only, then it’s abstract class
- **答案：** C. If a class has at least one pure virtual function, it’s abstract class
- **解析：** 题库考的是抽象类规则，正确项是“If a class has at least one pure virtual function, it’s abstract class”。

**2-36**. Can abstract class have main() function defined inside it?
- A. Yes, depending on return type of main()
- B. Yes, always
- C. No, main must not be defined inside abstract class
- D. No, because main() is not abstract function
- **答案：** B. Yes, always
- **解析：** 题库考的是抽象类规则，正确项是“Yes, always”。

**2-37**. If there is an abstract method in a class then, ________________
- A. Class must be abstract class
- B. Class may or may not be abstract class
- C. Class is generic
- D. Class must be public
- **答案：** A. Class must be abstract class
- **解析：** 题库考的是抽象类规则，正确项是“Class must be abstract class”。

**2-38**. If a class is extending/inheriting another abstract class having abstract method, then _______________________
- A. Either implementation of method or making class abstract is mandatory
- B. Implementation of the method in derived class is mandatory
- C. Making the derived class also abstract is mandatory
- D. It’s not mandatory to implement the abstract method of parent class
- **答案：** A. Either implementation of method or making class abstract is mandatory
- **解析：** 题库考的是抽象类规则，正确项是“Either implementation of method or making class abstract is mandatory”。

**2-39**. Abstract class A has 4 virtual functions. Abstract class B defines only 2 of those member functions as it extends class A. Class C extends class B and implements the other two member functions of class A. Choose the correct option below.
- A. Program won’t run as all the methods are not defined by B
- B. Program won’t run as C is not inheriting A directly
- C. Program won’t run as multiple inheritance is used
- D. Program runs correctly
- **答案：** D. Program runs correctly
- **解析：** 题库考的是抽象类规则，正确项是“Program runs correctly”。

**2-40**. Abstract classes can ____________________ instances.
- A. Never have
- B. Always have
- C. Have array of
- D. Have pointer of
- **答案：** A. Never have
- **解析：** 题库考的是抽象类规则，正确项是“Never have”。

**2-41**. We ___________________ to an abstract class.
- A. Can create pointers
- B. Can create references
- C. Can create pointers or references
- D. Can’t create any reference, pointer or instance
- **答案：** C. Can create pointers or references
- **解析：** 题库考的是抽象类规则，正确项是“Can create pointers or references”。

**2-42**. Which among the following is an important use of abstract classes?
- A. Header files
- B. Class Libraries
- C. Class definitions
- D. Class inheritance
- **答案：** B. Class Libraries
- **解析：** 题库考的是抽象类规则，正确项是“Class Libraries”。

**2-43**. Use of pointers or reference to an abstract class gives rise to which among the following feature?
- A. Static Polymorphism
- B. Runtime polymorphism
- C. Compile time Polymorphism
- D. Polymorphism within methods
- **答案：** B. Runtime polymorphism
- **解析：** 题库考的是抽象类规则，正确项是“Runtime polymorphism”。

**2-44**. The abstract classes in java can _________________
- A. Implement constructors
- B. Can’t implement constructor
- C. Can implement only unimplemented methods
- D. Can’t implement any type of constructor
- **答案：** A. Implement constructors
- **解析：** 题库考的是抽象类规则，正确项是“Implement constructors”。

**2-45**. It is _________________________ to have an abstract method.
- A. Not mandatory for an static class
- B. Not mandatory for a derived class
- C. Not mandatory for an abstract class
- D. Not mandatory for parent class
- **答案：** C. Not mandatory for an abstract class
- **解析：** 题库考的是抽象类规则，正确项是“Not mandatory for an abstract class”。

**2-46**. Is it necessary that all the abstract methods must be defined from an abstract class?
- A. Yes, depending on code
- B. Yes, always
- C. No, never
- D. No, if function is not used, no definition is required
- **答案：** C. No, never
- **解析：** 题库考的是抽象类规则，正确项是“No, never”。

**2-47**. If single level inheritance is used and an abstract class is created with some undefined functions, can its derived class also skip some definitions?
- A. Yes, always possible
- B. Yes, possible if only one undefined function
- C. No, at least 2 undefined functions must be there
- D. No, the derived class must implement those methods
- **答案：** D. No, the derived class must implement those methods
- **解析：** 题库考的是抽象类规则，正确项是“No, the derived class must implement those methods”。

**2-48**. Can abstract classes be used in multilevel inheritance?
- A. Yes, always
- B. Yes, only one abstract class
- C. No, abstract class doesn’t have constructors
- D. No, never
- **答案：** A. Yes, always
- **解析：** 题库考的是抽象类规则，正确项是“Yes, always”。

**2-49**. Is it possible to have all the abstract classes as base classes of a derived class from those?
- A. Yes, always
- B. Yes, only if derived class implements all the methods
- C. No, because abstract classes doesn’t have constructors
- D. No, never
- **答案：** B. Yes, only if derived class implements all the methods
- **解析：** 题库考的是抽象类规则，正确项是“Yes, only if derived class implements all the methods”。

**2-50**. Is it compulsory to have constructor for all the classes involved in multiple inheritance?
- A. Yes, always
- B. Yes, only if no abstract class is involved
- C. No, only classes being used should have a constructor
- D. No, they must not contain constructors
- **答案：** B. Yes, only if no abstract class is involved
- **解析：** 按题库对应概念，正确项是“Yes, only if no abstract class is involved”。

**2-51**. Which among the following best defines the abstract methods?
- A. Functions declared and defined in base class
- B. Functions only declared in base class
- C. Function which may or may not be defined in base class
- D. Function which must be declared in derived class
- **答案：** B. Functions only declared in base class
- **解析：** 题库考的是抽象类规则，正确项是“Functions only declared in base class”。

**2-52**. How are abstract functions different from virtual functions?
- A. Abstract must not be defined in base class whereas virtual function can be defined
- B. Either of those must be defined in base class
- C. Different according to definition
- D. Abstract functions are faster
- **答案：** A. Abstract must not be defined in base class whereas virtual function can be defined
- **解析：** 抽象函数只声明不实现；虚函数可以在基类中直接给出实现。

**2-53**. Which among the following is NOT correct?
- A. Abstract functions should not be defined in all the derived classes
- B. Abstract functions should be defined only in one derived class
- C. Abstract functions must be defined in base class
- D. Abstract functions must be defined in all the derived classes
- **答案：** D. Abstract functions must be defined in all the derived classes
- **解析：** 抽象函数不要求在所有派生类中都显式定义。

**2-54**. It is ____________________ to define the abstract functions.
- A. Mandatory for all the classes in program
- B. Necessary for all the base classes
- C. Necessary for all the derived classes
- D. Not mandatory for all the derived classes
- **答案：** D. Not mandatory for all the derived classes
- **解析：** 题库考的是抽象类规则，正确项是“Not mandatory for all the derived classes”。

**2-55**. The abstract function definitions in derived classes is enforced at _________
- A. Runtime
- B. Compile time
- C. Writing code time
- D. Interpreting time
- **答案：** B. Compile time
- **解析：** 题库考的是抽象类规则，正确项是“Compile time”。

**2-56**. What is this feature of enforcing definitions of abstract function at compile time called?
- A. Static polymorphism
- B. Polymorphism
- C. Dynamic polymorphism
- D. Static or dynamic according to need
- **答案：** A. Static polymorphism
- **解析：** 题库考的是抽象类规则，正确项是“Static polymorphism”。

**2-57**. If a function declared as abstract in base class doesn’t have to be defined in derived class then ______
- A. Derived class must define the function anyhow
- B. Derived class should be made abstract class
- C. Derived class should not derive from that base class
- D. Derived class should not use that function
- **答案：** B. Derived class should be made abstract class
- **解析：** 题库考的是抽象类规则，正确项是“Derived class should be made abstract class”。

**2-58**. Which among the following is true?
- A. Abstract methods can be static
- B. Abstract methods can be defined in derived class
- C. Abstract methods must not be static
- D. Abstract methods can be made static in derived class
- **答案：** C. Abstract methods must not be static
- **解析：** 按题库对应概念，正确项是“Abstract methods must not be static”。

**2-59**. Which among the following is correct for abstract methods?
- A. It must have different prototype in the derived class
- B. It must have same prototype in both base and derived class
- C. It must have different signature in derived class
- D. It must have same return type only
- **答案：** B. It must have same prototype in both base and derived class
- **解析：** 题库考的是抽象类规则，正确项是“It must have same prototype in both base and derived class”。

**2-60**. If a class have all the abstract methods the class will be known as ___________
- A. Abstract class
- B. Anonymous class
- C. Base class
- D. Derived class
- **答案：** A. Abstract class
- **解析：** 题库考的是抽象类规则，正确项是“Abstract class”。

**2-61**. The abstract methods can never be ___________ in a base class.
- A. Private
- B. Protected
- C. Public
- D. Default
- **答案：** A. Private
- **解析：** 题库考的是抽象类规则，正确项是“Private”。

**2-62**. The abstract method definition can be made ___________ in derived class.
- A. Private
- B. Protected
- C. Public
- D. Private, public, or protected
- **答案：** D. Private, public, or protected
- **解析：** 题库考的是抽象类规则，正确项是“Private, public, or protected”。

**2-63**. In case of using abstract class or function overloading, which function is supposed to be called first?
- A. Local function
- B. Function with highest priority in compiler
- C. Global function
- D. Function with lowest priority because it might have been halted since long time, because of low priority
- **答案：** B. Function with highest priority in compiler
- **解析：** 题库考的是抽象类规则，正确项是“Function with highest priority in compiler”。

**2-64**. Which problem may arise if we use abstract class functions for polymorphism?
- A. All classes are converted as abstract class
- B. Derived class must be of abstract type
- C. All the derived classes must implement the undefined functions
- D. Derived classes can’t redefine the function
- **答案：** C. All the derived classes must implement the undefined functions
- **解析：** 题库考的是抽象类规则，正确项是“All the derived classes must implement the undefined functions”。
