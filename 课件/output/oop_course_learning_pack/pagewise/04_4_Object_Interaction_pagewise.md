# Lecture 04: 4 Object Interaction

- Source: `4 Object Interaction.pdf`
- Pages: 104
- Rendered page images: 104
- Contact sheet: [open](../contact_sheets/04_4_Object_Interaction_contact.jpg)
- Raw extracted text: [open](../raw_texts/04-4 Object Interaction.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 4 page 1](../page_images/04_4_Object_Interaction/page_001.png)

Extracted text:

```text
Object Interaction
 Object-Oriented Programming with C++
```

## Page 2

![Lecture 4 page 2](../page_images/04_4_Object_Interaction/page_002.png)

Extracted text:

```text
Object oriented programming
• Objects send and receive messages (object do things!)

        Data                            Data

      Methods                          Methods


                        Data

                      Methods
```

## Page 3

![Lecture 4 page 3](../page_images/04_4_Object_Interaction/page_003.png)

Extracted text:

```text
Object send messages
• Messages are
 - Composed by the sender
 - Interpreted by the receiver
 - Implemented by methods

• Messages
 - May return results
 - May cause receiver to change state, i.e., side effects
```

## Page 4

![Lecture 4 page 4](../page_images/04_4_Object_Interaction/page_004.png)

Extracted text:

```text
Encapsulation
• Bundle data and methods dealing with these
  data together in an object
• Hide the details of the data and the action
• Restrict access only to the publicized
  methods
```

## Page 5

![Lecture 4 page 5](../page_images/04_4_Object_Interaction/page_005.png)

Extracted text:

```text
Abstract
• Abstraction is the ability to ignore details of
 parts to focus attention on a higher level of a
 problem.

• Modularization is the process of dividing a
 whole into well-defined parts, which can be
 built and examined separately, and which
 interact in well-defined ways.
```

## Page 6

![Lecture 4 page 6](../page_images/04_4_Object_Interaction/page_006.png)

Extracted text:

```text
Clock display
```

## Page 7

![Lecture 4 page 7](../page_images/04_4_Object_Interaction/page_007.png)

Extracted text:

```text
Modularizing the clock display

                    One 4-digits display?




  Or two 2-digits
  displays?
```

## Page 8

![Lecture 4 page 8](../page_images/04_4_Object_Interaction/page_008.png)

Extracted text:

```text
Object & Classes
            myDisplay:                           ClockDisplay
           ClockDisplay

                          :NumberDisplay

       hours

       minutes
                             11
                                                                NumberDisplay



                          :NumberDisplay
(a)                                        (b)

                             03
  a)
```

## Page 9

![Lecture 4 page 9](../page_images/04_4_Object_Interaction/page_009.png)

Extracted text:

```text
Class diagram
       ClockDisplay
-hours : NumberDisplay
-minutes : NumberDisplay
+start()




       NumberDisplay
    -limit : int
    -value : int
    +increase() : boolean
```

## Page 10

![Lecture 4 page 10](../page_images/04_4_Object_Interaction/page_010.png)

Extracted text:

```text
Implementation - ClockDisplay

 class ClockDisplay {
     NumberDisplay hours;
     NumberDisplay minutes;

     Constructor and methods omitted.


 }
```

## Page 11

![Lecture 4 page 11](../page_images/04_4_Object_Interaction/page_011.png)

Extracted text:

```text
Implementation - ClockDisplay

    class NumberDisplay {
        int limit;
        int value;

        Constructor and methods omitted.


    }
```

## Page 12

![Lecture 4 page 12](../page_images/04_4_Object_Interaction/page_012.png)

Extracted text:

```text
C'tor and D'tor
```

## Page 13

![Lecture 4 page 13](../page_images/04_4_Object_Interaction/page_013.png)

Extracted text:

```text
Point::init()
class Point {
public:
     void init(int x, int y);
     void print() const;
     void move(int dx, int dy);
private:
     int x;
     int y;
};

Point a;
a.init(1,2);
a.move(2,2);
a.print();
```

## Page 14

![Lecture 4 page 14](../page_images/04_4_Object_Interaction/page_014.png)

Extracted text:

```text
[No extractable text]
```

## Page 15

![Lecture 4 page 15](../page_images/04_4_Object_Interaction/page_015.png)

Extracted text:

```text
Guaranteed initialization with
      the constructor
 • If a class has a constructor, the compiler
    automatically calls that constructor at the point
    an object is created, before client programmers
    can get their hands on the object.
 • The name of the constructor is the same as the
    name of the class.
```

## Page 16

![Lecture 4 page 16](../page_images/04_4_Object_Interaction/page_016.png)

Extracted text:

```text
How does a constructor work?
      class X {
        int i;
      public:
        X();
      };
```

## Page 17

![Lecture 4 page 17](../page_images/04_4_Object_Interaction/page_017.png)

Extracted text:

```text
How does a constructor work?
      class X {
        int i;
      public:     constructor
        X();
      };
```

## Page 18

![Lecture 4 page 18](../page_images/04_4_Object_Interaction/page_018.png)

Extracted text:

```text
How does a constructor work?
      class X {
        int i;
      public:      constructor
        X();
      };

      void f() {
        X a;
        // ...
      }
```

## Page 19

![Lecture 4 page 19](../page_images/04_4_Object_Interaction/page_019.png)

Extracted text:

```text
How does a constructor work?
      class X {
        int i;
      public:         constructor
        X();
      };

      void f() {
        X a;
        // ...     a.X();
      }
```

## Page 20

![Lecture 4 page 20](../page_images/04_4_Object_Interaction/page_020.png)

Extracted text:

```text
Constructors with arguments

  • The constructor can have arguments to allow
     you to specify how an object is created, give it
     initialization values, and so on.


  Tree(int i) {…}
  Tree t(12);

  • Constructor1.cpp
```

## Page 21

![Lecture 4 page 21](../page_images/04_4_Object_Interaction/page_021.png)

Extracted text:

```text
The destructor
• In C++, cleanup is as important as initialization and is
 therefore guaranteed with the destructor.
• The destructor is named after the name of the class
 with a leading tilde (~). The destructor never has any
 arguments.
```

## Page 22

![Lecture 4 page 22](../page_images/04_4_Object_Interaction/page_022.png)

Extracted text:

```text
The destructor
• In C++, cleanup is as important as initialization and is
 therefore guaranteed with the destructor.
• The destructor is named after the name of the class
 with a leading tilde (~). The destructor never has any
 arguments.
                   class Y {
                   public:
                     ~Y();
                   };
```

## Page 23

![Lecture 4 page 23](../page_images/04_4_Object_Interaction/page_023.png)

Extracted text:

```text
When is a destructor called?
  • The destructor is called automatically by the
   compiler when the object goes out of scope.
```

## Page 24

![Lecture 4 page 24](../page_images/04_4_Object_Interaction/page_024.png)

Extracted text:

```text
Storage allocation
```

## Page 25

![Lecture 4 page 25](../page_images/04_4_Object_Interaction/page_025.png)

Extracted text:

```text
Storage allocation
• The compiler allocates all the storage for a
 scope at the opening brace of that scope.
```

## Page 26

![Lecture 4 page 26](../page_images/04_4_Object_Interaction/page_026.png)

Extracted text:

```text
Storage allocation
• The compiler allocates all the storage for a
 scope at the opening brace of that scope.

• The constructor call doesn’t happen until the
  sequence point where the object is deﬁned.

• Example: Nojump.cpp
```

## Page 27

![Lecture 4 page 27](../page_images/04_4_Object_Interaction/page_027.png)

Extracted text:

```text
Aggregate initialization
```

## Page 28

![Lecture 4 page 28](../page_images/04_4_Object_Interaction/page_028.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
```

## Page 29

![Lecture 4 page 29](../page_images/04_4_Object_Interaction/page_029.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
```

## Page 30

![Lecture 4 page 30](../page_images/04_4_Object_Interaction/page_030.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
```

## Page 31

![Lecture 4 page 31](../page_images/04_4_Object_Interaction/page_031.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
```

## Page 32

![Lecture 4 page 32](../page_images/04_4_Object_Interaction/page_032.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
• X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }
```

## Page 33

![Lecture 4 page 33](../page_images/04_4_Object_Interaction/page_033.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
• X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }
• struct Y { float f; int i; Y(int a); };
```

## Page 34

![Lecture 4 page 34](../page_images/04_4_Object_Interaction/page_034.png)

Extracted text:

```text
Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
• X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }
• struct Y { float f; int i; Y(int a); };
• Y y1[] = { Y(1), Y(2), Y(3) };
```

## Page 35

![Lecture 4 page 35](../page_images/04_4_Object_Interaction/page_035.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.
```

## Page 36

![Lecture 4 page 36](../page_images/04_4_Object_Interaction/page_036.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {
    float f;
    int i;
    Y(int a);
};
```

## Page 37

![Lecture 4 page 37](../page_images/04_4_Object_Interaction/page_037.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
    int i;
    Y(int a);
};
```

## Page 38

![Lecture 4 page 38](../page_images/04_4_Object_Interaction/page_038.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);
};
```

## Page 39

![Lecture 4 page 39](../page_images/04_4_Object_Interaction/page_039.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);                 Y y3[7];
};
```

## Page 40

![Lecture 4 page 40](../page_images/04_4_Object_Interaction/page_040.png)

Extracted text:

```text
The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);                 Y y3[7];
};                              Y y4;
```

## Page 41

![Lecture 4 page 41](../page_images/04_4_Object_Interaction/page_041.png)

Extracted text:

```text
“auto” default constructor
```

## Page 42

![Lecture 4 page 42](../page_images/04_4_Object_Interaction/page_042.png)

Extracted text:

```text
“auto” default constructor
• If you have a constructor, the compiler ensures
  that construction always happens.
```

## Page 43

![Lecture 4 page 43](../page_images/04_4_Object_Interaction/page_043.png)

Extracted text:

```text
“auto” default constructor
• If you have a constructor, the compiler ensures
  that construction always happens.

• If (and only if) there are no constructors for a
  class (struct or class), the compiler will
  automatically create one for you.
```

## Page 44

![Lecture 4 page 44](../page_images/04_4_Object_Interaction/page_044.png)

Extracted text:

```text
Local variable vs. Field
 •  TicketMachine::refundBalance()
int Local
    int
                                              {
          variables are defined inside a method,
          amountToRefund;
    have a scope limited to the method to which
    amountToRefund
    they belong.         = balance;
    balance = 0;
    return amountToRefund;
}
```

## Page 45

![Lecture 4 page 45](../page_images/04_4_Object_Interaction/page_045.png)

Extracted text:

```text
Local variable vs. Field
 •  TicketMachine::refundBalance()
int Local
    int
                                              {
          variables are defined inside a method,
          amountToRefund;
    have a scope limited to the method to which
    amountToRefund
    they belong.         = balance;
    balance = 0;
    return amountToRefund;
}

Lifetime:
• amountToRefund is with the function call
• balance is with the object, i.e., object state
```

## Page 46

![Lecture 4 page 46](../page_images/04_4_Object_Interaction/page_046.png)

Extracted text:

```text
Local variable vs. Field
 •  TicketMachine::refundBalance()
int Local
    int
                                              {
          variables are defined inside a method,
          amountToRefund;
    have a scope limited to the method to which
    amountToRefund
    they belong.         = balance;
    balance = 0;
    return amountToRefund;
}


But how is the access to balance achieved?
```

## Page 47

![Lecture 4 page 47](../page_images/04_4_Object_Interaction/page_047.png)

Extracted text:

```text
Local variable vs. Field
    •  TicketMachine::refundBalance()
   int Local
       int
                                                 {
             variables are defined inside a method,
             amountToRefund;
       have a scope limited to the method to which
       amountToRefund
       they belong.         = balance;
       balance = 0;
       return amountToRefund;
   }


A local variable of the same name as a field will prevent
the field from being accessed within a method.
```

## Page 48

![Lecture 4 page 48](../page_images/04_4_Object_Interaction/page_048.png)

Extracted text:

```text
Fields, parameters, local variables
•All three kinds of variable are able to store a value that is
 appropriate to their defined type.
•Fields are defined outside constructors and methods
•Fields are used to store data that persists throughout
    the life of an object. As such, they maintain the current
    state of an object. They have a lifetime that lasts as long
    as their object lasts.
•   Fields have class scope: their accessibility extends
    throughout the whole class, and so they can be used
    within any of the constructors or methods of the class
    in which they are defined.
```

## Page 49

![Lecture 4 page 49](../page_images/04_4_Object_Interaction/page_049.png)

Extracted text:

```text
Call the functions in a class
 Point a;
 a.print();

  There is a relationship with the function be
   called and the variable to call it.

  The function itself knows it is doing something
   w/ the variable.
```

## Page 50

![Lecture 4 page 50](../page_images/04_4_Object_Interaction/page_050.png)

Extracted text:

```text
this: the hidden parameter
 this is a hidden parameter for all member functions,
  with the type of the class

    void Point::print()
     ➔ (can be regarded as)
    void Point::print(Point *this)
```

## Page 51

![Lecture 4 page 51](../page_images/04_4_Object_Interaction/page_051.png)

Extracted text:

```text
this: the hidden parameter
 To call the function, you must specify a variable

    Point a;
    a.print();
     ➔ (can be regarded as)
    Point::print(&a);
```

## Page 52

![Lecture 4 page 52](../page_images/04_4_Object_Interaction/page_052.png)

Extracted text:

```text
this: the pointer to the caller
 Inside member functions, you can use this as the
  pointer to the variable that calls the function.

 this is a natural parameter of all class member
  functions that you cannot define, but can use directly.
```

## Page 53

![Lecture 4 page 53](../page_images/04_4_Object_Interaction/page_053.png)

Extracted text:

```text
Initialization
```

## Page 54

![Lecture 4 page 54](../page_images/04_4_Object_Interaction/page_054.png)

Extracted text:

```text
Initializer list
    Class Point {
    private:
      const float x, y;
    public:
      Point(float xa, float ya)
        : y(ya), x(xa) {}
    };
•   Can initialize any type of data
    – pseudo-constructor calls for built-ins
    – No need to perform assignment within body of ctor
•   Order of initialization is order of declaration
    – Not the order in the initializer list!
    – Destroyed in the reverse order.
```

## Page 55

![Lecture 4 page 55](../page_images/04_4_Object_Interaction/page_055.png)

Extracted text:

```text
Initialization vs. assignment
```

## Page 56

![Lecture 4 page 56](../page_images/04_4_Object_Interaction/page_056.png)

Extracted text:

```text
Initialization vs. assignment
 Student::Student(string s):name(s) {}




 Student::Student(string s) {name=s;}
```

## Page 57

![Lecture 4 page 57](../page_images/04_4_Object_Interaction/page_057.png)

Extracted text:

```text
Initialization vs. assignment
 Student::Student(string s):name(s) {}
  initialization
  before constructor body


 Student::Student(string s) {name=s;}
```

## Page 58

![Lecture 4 page 58](../page_images/04_4_Object_Interaction/page_058.png)

Extracted text:

```text
Initialization vs. assignment
 Student::Student(string s):name(s) {}
  initialization
  before constructor body


 Student::Student(string s) {name=s;}
  assignment
  inside constructor body
  string must have a default constructor
```

## Page 59

![Lecture 4 page 59](../page_images/04_4_Object_Interaction/page_059.png)

Extracted text:

```text
Function overloading
• Same functions with different arguments list.
void print(char * str, int width); // #1
void print(double d, int width); // #2
void print(long l, int width); // #3
void print(int i, int width); // #4
void print(char *str); // #5

print("Pancakes", 15);
print("Syrup");
print(1999.0, 10);
print(1999, 12);
print(1999L, 15);
```

## Page 60

![Lecture 4 page 60](../page_images/04_4_Object_Interaction/page_060.png)

Extracted text:

```text
Function overloading
• Same functions with different arguments list.
void print(char * str, int width); // #1
void print(double d, int width); // #2
void print(long l, int width); // #3
void print(int i, int width); // #4
void print(char *str); // #5

print("Pancakes", 15); // #1
print("Syrup");        // #5
print(1999.0, 10);     // #2
print(1999, 12);       // #4
print(1999L, 15);      // #3
```

## Page 61

![Lecture 4 page 61](../page_images/04_4_Object_Interaction/page_061.png)

Extracted text:

```text
Overload and auto-cast
void f(int i);
void f(double d);

f('a'); //ambiguous
f(2);
f(2L); // ambiguous
f(3.2f);
```

## Page 62

![Lecture 4 page 62](../page_images/04_4_Object_Interaction/page_062.png)

Extracted text:

```text
Default arguments

•   A default argument is a value given in the
    declaration that the compiler automatically
    inserts if you don’t provide a value in the
    function call.
Stash(int size, int initQuantity = 0);
```

## Page 63

![Lecture 4 page 63](../page_images/04_4_Object_Interaction/page_063.png)

Extracted text:

```text
• Todefine a function with an argument list, defaults
  must be added from right to left.
   int harpo(int n, int m = 4, int j = 5);
   int chico(int n, int m = 6, int j); //illegal
   int groucho(int k = 1, int m = 2, int n = 3);

   beeps = harpo(2);
   beeps = harpo(1,8);
   beeps = harpo(8,7,6);
```

## Page 64

![Lecture 4 page 64](../page_images/04_4_Object_Interaction/page_064.png)

Extracted text:

```text
Constant objects
```

## Page 65

![Lecture 4 page 65](../page_images/04_4_Object_Interaction/page_065.png)

Extracted text:

```text
Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?
```

## Page 66

![Lecture 4 page 66](../page_images/04_4_Object_Interaction/page_066.png)

Extracted text:

```text
Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?

•   How can the object be protected from change?
```

## Page 67

![Lecture 4 page 67](../page_images/04_4_Object_Interaction/page_067.png)

Extracted text:

```text
Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?

•   How can the object be protected from change?

•   Solution: declare member functions const
    –   Programmer declares member functions to be safe
```

## Page 68

![Lecture 4 page 68](../page_images/04_4_Object_Interaction/page_068.png)

Extracted text:

```text
Const member functions
•Cannot modify their objects
int Date::set_day(int d) {
    //...error check d here...
    day = d; // ok, non-const so can modify
}

int Date::get_day() const {

     return day; // ok
}
```

## Page 69

![Lecture 4 page 69](../page_images/04_4_Object_Interaction/page_069.png)

Extracted text:

```text
Const member functions
•Cannot modify their objects
int Date::set_day(int d) {
    //...error check d here...
    day = d; // ok, non-const so can modify
}

int Date::get_day() const {
    day++; //ERROR modifies data member
    set_day(12); // ERROR calls non-const member
    return day; // ok
}
```

## Page 70

![Lecture 4 page 70](../page_images/04_4_Object_Interaction/page_070.png)

Extracted text:

```text
Const member function usage
 •   Repeat the const keyword in the definition as well as
     the declaration

     int get_day() const;

     int get_day() const { return day };

 •   Function members that do not modify data should be
     declared const

 •   const member functions are safe for const objects
```

## Page 71

![Lecture 4 page 71](../page_images/04_4_Object_Interaction/page_071.png)

Extracted text:

```text
Const objects
```

## Page 72

![Lecture 4 page 72](../page_images/04_4_Object_Interaction/page_072.png)

Extracted text:

```text
Const objects
• Const and non-const objects
 // non-const object
 Date when(1,1,2001); // not a const
 int day = when.get_day(); // OK
 when.set_day(13); // OK


 // const object
 const Date birthday(12,25,1994); // const
 int day = birthday.get_day(); // OK
 birthday.set_day(14); // ERROR
```

## Page 73

![Lecture 4 page 73](../page_images/04_4_Object_Interaction/page_073.png)

Extracted text:

```text
Constant in class
  class A {

     const int i;

  };



• has to be initialized in initializer list of the constructor
```

## Page 74

![Lecture 4 page 74](../page_images/04_4_Object_Interaction/page_074.png)

Extracted text:

```text
Compile-time constants in classes
```

## Page 75

![Lecture 4 page 75](../page_images/04_4_Object_Interaction/page_075.png)

Extracted text:

```text
Compile-time constants in classes
  class HasArray {
     const int size;
     int array[size]; // ERROR!
     ...
  };
```

## Page 76

![Lecture 4 page 76](../page_images/04_4_Object_Interaction/page_076.png)

Extracted text:

```text
Compile-time constants in classes
  class HasArray {
     const int size;
     int array[size]; // ERROR!
     ...
  };

• Make the const value static:
  - static const int size = 100;
  - static indicates only one per class (not one per object)
```

## Page 77

![Lecture 4 page 77](../page_images/04_4_Object_Interaction/page_077.png)

Extracted text:

```text
Compile-time constants in classes
  class HasArray {
     const int size;
     int array[size]; // ERROR!
     ...
  };

• Make the const value static:
  - static const int size = 100;
  - static indicates only one per class (not one per object)

• Or use “anonymous enum” hack :
  class HasArray{
      enum { size = 100 };
      int array[size]; // OK!
      …
  }
```

## Page 78

![Lecture 4 page 78](../page_images/04_4_Object_Interaction/page_078.png)

Extracted text:

```text
Inline function
```

## Page 79

![Lecture 4 page 79](../page_images/04_4_Object_Interaction/page_079.png)

Extracted text:

```text
Overhead for a function call
  • The processing time required by a
     device prior to the execution of a
     command

    • Push parameters
    • Push return address
    • Prepare return values
    • Pop all pushed
```

## Page 80

![Lecture 4 page 80](../page_images/04_4_Object_Interaction/page_080.png)

Extracted text:

```text
Inline
int f(int i) {
  return i*2;
}
main() {
  int a = 4;
  int b = f(a);
}
```

## Page 81

![Lecture 4 page 81](../page_images/04_4_Object_Interaction/page_081.png)

Extracted text:

```text
Inline Functions

• An inline function is expanded in place, like
   a preprocessor macro, so the overhead of
   the function call is eliminated.
```

## Page 82

![Lecture 4 page 82](../page_images/04_4_Object_Interaction/page_082.png)

Extracted text:

```text
Inline
int f(int i) {       inline int f(int i) {
  return i*2;          return i*2;
}                    }
int main() {
                     int main() {
  int a = 4;
  int b = f(a);        int a = 4;
}                      int b = f(a);
                     }
```

## Page 83

![Lecture 4 page 83](../page_images/04_4_Object_Interaction/page_083.png)

Extracted text:

```text
inline int f(int i) {
  return i * 2;
}
int main() {
  int a = 4;
  int b = f(a);
}
```

## Page 84

![Lecture 4 page 84](../page_images/04_4_Object_Interaction/page_084.png)

Extracted text:

```text
inline int f(int i) {
  return i * 2;
}
int main() {          int main() {
  int a = 4;            int a = 4;
  int b = f(a);         int b = a + a;
}                     }
```

## Page 85

![Lecture 4 page 85](../page_images/04_4_Object_Interaction/page_085.png)

Extracted text:

```text
Inline Functions
inline int plusOne(int x) { return ++x; };

• The “definition” of an inline function should be
    put in a header file.
• An inline function definition may not generate
    any code in .obj file.
• It is declaration rather than definition.
```

## Page 86

![Lecture 4 page 86](../page_images/04_4_Object_Interaction/page_086.png)

Extracted text:

```text
Inline functions in header file
   • So you can put inline functions’ bodies in
      header file. Then #include it where the
      function is needed.
   • Never be afraid of multi-definition of
      inline functions.
   • Definitions of inline functions are just
      declarations.
```

## Page 87

![Lecture 4 page 87](../page_images/04_4_Object_Interaction/page_087.png)

Extracted text:

```text
Tradeoff of inline functions
  •  Body of the called function is to be inserted into
     the caller.
  • This may expand the code size
  • but deduces the overhead of calling time.
  • So it gains speed at the expenses of space.
  • Ittypes
        is much better than macro in C. It checks the
            of the parameters, and has no dangerous
     side effect.
```

## Page 88

![Lecture 4 page 88](../page_images/04_4_Object_Interaction/page_088.png)

Extracted text:

```text
#define unsafe(i) \    inline int safe(int i)
 ((i)>=0?(i):-(i))     {
                         return i>=0 ? i:-i;
int f();               }

int main() {           int f();
  ans = unsafe(x++);
  ans = unsafe(f());   int main() {
}                        ans = safe(x++);
                         ans = safe(f());
                       }
```

## Page 89

![Lecture 4 page 89](../page_images/04_4_Object_Interaction/page_089.png)

Extracted text:

```text
Inline inside classes
• Any  function you define inside a
  class declaration is automatically an
   inline.
   •    Example:
        Inline.cpp
```

## Page 90

![Lecture 4 page 90](../page_images/04_4_Object_Interaction/page_090.png)

Extracted text:

```text
Access functions
 • They are small functions that allow you to read or
    change part of the state of an object – that is, an
    internal variable or variables.
class Cup {
  int color;
public:
  int getColor() { return color; }
  void setColor(int color) {
     this->color = color;
  }
};
```

## Page 91

![Lecture 4 page 91](../page_images/04_4_Object_Interaction/page_091.png)

Extracted text:

```text
Reducing clutter
• Member functions defined within classes
   use the Latin in situ (in place) and maintains
   that all definitions should be placed outside
   the class to keep the interface clean.


• Example: Noinsitu.cpp
```

## Page 92

![Lecture 4 page 92](../page_images/04_4_Object_Interaction/page_092.png)

Extracted text:

```text
Inline or not?
```

## Page 93

![Lecture 4 page 93](../page_images/04_4_Object_Interaction/page_093.png)

Extracted text:

```text
Inline or not?
• Inline:
 • Small functions, 2 or 3lines
 • Frequently called functions, e.g. inside loops
```

## Page 94

![Lecture 4 page 94](../page_images/04_4_Object_Interaction/page_094.png)

Extracted text:

```text
Inline or not?
• Inline:
 • Small functions, 2 or 3lines
 • Frequently called functions, e.g. inside loops
• Not inline?
  • Very large functions, say, more than 20 lines
  • Recursive functions
```

## Page 95

![Lecture 4 page 95](../page_images/04_4_Object_Interaction/page_095.png)

Extracted text:

```text
Inline may not in-line
• The compiler does not have to honor your
  request to make a function inline. It might
  decide the function is too large or notice
  that it calls itself (recursion is not allowed or
  indeed possible for inline functions), or the
  feature might not be implemented for your
  particular compiler.
```

## Page 96

![Lecture 4 page 96](../page_images/04_4_Object_Interaction/page_096.png)

Extracted text:

```text
Inline may not in-line
• Nowadays, the keyword inline for functions
  comes to mean "multiple definitions are
  permitted" rather than "inlining is preferred".
```

## Page 97

![Lecture 4 page 97](../page_images/04_4_Object_Interaction/page_097.png)

Extracted text:

```text
[No extractable text]
```

## Page 98

![Lecture 4 page 98](../page_images/04_4_Object_Interaction/page_098.png)

Extracted text:

```text
[No extractable text]
```

## Page 99

![Lecture 4 page 99](../page_images/04_4_Object_Interaction/page_099.png)

Extracted text:

```text
[No extractable text]
```

## Page 100

![Lecture 4 page 100](../page_images/04_4_Object_Interaction/page_100.png)

Extracted text:

```text
[No extractable text]
```

## Page 101

![Lecture 4 page 101](../page_images/04_4_Object_Interaction/page_101.png)

Extracted text:

```text
[No extractable text]
```

## Page 102

![Lecture 4 page 102](../page_images/04_4_Object_Interaction/page_102.png)

Extracted text:

```text
[No extractable text]
```

## Page 103

![Lecture 4 page 103](../page_images/04_4_Object_Interaction/page_103.png)

Extracted text:

```text
[No extractable text]
```

## Page 104

![Lecture 4 page 104](../page_images/04_4_Object_Interaction/page_104.png)

Extracted text:

```text
[No extractable text]
```
