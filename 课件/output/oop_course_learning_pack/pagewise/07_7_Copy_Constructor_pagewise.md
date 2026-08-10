# Lecture 07: 7 Copy Constructor

- Source: `7 Copy Constructor.pdf`
- Pages: 96
- Rendered page images: 96
- Contact sheet: [open](../contact_sheets/07_7_Copy_Constructor_contact.jpg)
- Raw extracted text: [open](../raw_texts/07-7 Copy Constructor.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 7 page 1](../page_images/07_7_Copy_Constructor/page_001.png)

Extracted text:

```text
References as class members
• Declared without initial value
```

## Page 2

![Lecture 7 page 2](../page_images/07_7_Copy_Constructor/page_002.png)

Extracted text:

```text
References as class members
• Declared without initial value
• Must be initialized using constructor initializer list

   class X {
   public:
      int& m_y;
      X(int& a);
   };
   X::X(int& a) : m_y(a) { }

   code & demo
```

## Page 3

![Lecture 7 page 3](../page_images/07_7_Copy_Constructor/page_003.png)

Extracted text:

```text
Returning references
• Functions can return references
  – But they should refer to non-local variables!

   #include <cassert>
   const int SIZE = 32;
   double myarray[SIZE];
   double& subscript(const int i) {
      return myarray[i];
   }
```

## Page 4

![Lecture 7 page 4](../page_images/07_7_Copy_Constructor/page_004.png)

Extracted text:

```text
Example
main() {
   for (int i = 0; i < SIZE; i++) {
      myarray[i] = i * 0.5;
   }
   double value = subscript(12);
   subscript(3) = 34.5;
}
```

## Page 5

![Lecture 7 page 5](../page_images/07_7_Copy_Constructor/page_005.png)

Extracted text:

```text
const in functions arguments
• Passing by const value – don’t do it
• Passing by const reference
      Person(const string& name, int weight);
 – won’t change the string object
 – more efficient than pass by value (copy)
 – const qualifier protects from change
```

## Page 6

![Lecture 7 page 6](../page_images/07_7_Copy_Constructor/page_006.png)

Extracted text:

```text
const reference parameters
• What if you don’t want to change the argument
• Use const modifier
   // y is a constant! Can’t be modified
   void func(const int& y, int& z) {
      z = z * 5; // ok
      y += 8; // error!
   };
```

## Page 7

![Lecture 7 page 7](../page_images/07_7_Copy_Constructor/page_007.png)

Extracted text:

```text
Temporary values are const
• What you type
 void func(int &);
 func(i * 3); // Generates warning or error!


• What the compiler generates
 void func(int &);
 const int _tmp_ = i * 3;
 func(_tmp_); // Problem – binding non-const ref
              // to const argument!

    The temporary is constant, since you can’t access it
```

## Page 8

![Lecture 7 page 8](../page_images/07_7_Copy_Constructor/page_008.png)

Extracted text:

```text
const in function returns
• return by const value
   – basically it means nothing
• return by const pointer or reference
   – depends on what you want your client to do
     with the return value


 code & demo
```

## Page 9

![Lecture 7 page 9](../page_images/07_7_Copy_Constructor/page_009.png)

Extracted text:

```text
Copy Ctor
Object-Oriented Programming with C++
```

## Page 10

![Lecture 7 page 10](../page_images/07_7_Copy_Constructor/page_010.png)

Extracted text:

```text
Copying
• Create a new object from an existing one
  – For example, when calling a function

 // Currency as pass-by-value argument
 void func(Currency p) {
   cout << "X = " << p.dollars();
 }
 ...
 Currency bucks(100, 0);
 func(bucks); // bucks is copied into p

Example: HowMany.cpp
```

## Page 11

![Lecture 7 page 11](../page_images/07_7_Copy_Constructor/page_011.png)

Extracted text:

```text
The copy constructor
```

## Page 12

![Lecture 7 page 12](../page_images/07_7_Copy_Constructor/page_012.png)

Extracted text:

```text
The copy constructor
• Copying is implemented by the copy constructor
```

## Page 13

![Lecture 7 page 13](../page_images/07_7_Copy_Constructor/page_013.png)

Extracted text:

```text
The copy constructor
• Copying is implemented by the copy constructor
• Has the unique signature
     T::T(const T&);
  – Call-by-reference is used for the explicit argument
• C++ builds a copy ctor for you if you don't provide one!
  –Copies each member variable
    • Good for numbers, objects, object arrays
  – Copies each pointer
    • Data may become shared!
```

## Page 14

![Lecture 7 page 14](../page_images/07_7_Copy_Constructor/page_014.png)

Extracted text:

```text
What if class contains pointers?
 class Person {
 public:
      Person(const char *s);
      ~Person();
      void print();
      // ... accessor functions
 private:
      char *name;     // char * instead of string
      //... more info e.g. age, address, phone
 };
```

## Page 15

![Lecture 7 page 15](../page_images/07_7_Copy_Constructor/page_015.png)

Extracted text:

```text
Choices
Copy pointer

        Some Text




code & demo
```

## Page 16

![Lecture 7 page 16](../page_images/07_7_Copy_Constructor/page_016.png)

Extracted text:

```text
Choices
Copy pointer        Copy entire block

        Some Text          Some Text




                           Some Text



code & demo
```

## Page 17

![Lecture 7 page 17](../page_images/07_7_Copy_Constructor/page_017.png)

Extracted text:

```text
Character strings




     C   +         +   '\0'
             /50
```

## Page 18

![Lecture 7 page 18](../page_images/07_7_Copy_Constructor/page_018.png)

Extracted text:

```text
Character strings
• In C++, a character string is
  – An array of characters
  – With a special terminator — ‘\0’ or ASCII null
• The string “C++” is represented, in memory,
  by an array of four (4, count’em) characters




                      C   +         +   '\0'
                              /50
```

## Page 19

![Lecture 7 page 19](../page_images/07_7_Copy_Constructor/page_019.png)

Extracted text:

```text
Standard C library String fxns
• Declared in <cstring>
```

## Page 20

![Lecture 7 page 20](../page_images/07_7_Copy_Constructor/page_020.png)

Extracted text:

```text
Standard C library String fxns
• Declared in <cstring>
size_t strlen(const char *s);
  – s is a null-terminated string
  – returns the length of s
  – length does not include the terminator!
char *strcpy (char *dest, const char *src);
  – Copies src to dest stopping after the terminating null-character is
    copied. (src should be null-terminated!)
  – dest should have enough memory space allocated to contain src
    string.
  – Return Value: returns dest
```

## Page 21

![Lecture 7 page 21](../page_images/07_7_Copy_Constructor/page_021.png)

Extracted text:

```text
Person (char*) implementation
 #include <cstring>      // #include <string.h>
 using namespace std;

 Person::Person( const char *s ) {
  name = new char[::strlen(s) + 1];
   ::strcpy(name, s);
 }

 Person::~Person() {
   delete [] name;      // array delete
 }
```

## Page 22

![Lecture 7 page 22](../page_images/07_7_Copy_Constructor/page_022.png)

Extracted text:

```text
Person copy constructor
```

## Page 23

![Lecture 7 page 23](../page_images/07_7_Copy_Constructor/page_023.png)

Extracted text:

```text
Person copy constructor
• To Person declaration add copy ctor prototype:
 Person( const Person& w );          // copy ctor
• To Person .cpp add copy ctor defintion:
 Person::Person( const Person& w ) {
     name = new char[::strlen(w.name) + 1];
     ::strcpy(name, w.name);
 }
```

## Page 24

![Lecture 7 page 24](../page_images/07_7_Copy_Constructor/page_024.png)

Extracted text:

```text
Person copy constructor
• To Person declaration add copy ctor prototype:
 Person( const Person& w );          // copy ctor
• To Person .cpp add copy ctor defintion:
 Person::Person( const Person& w ) {
     name = new char[::strlen(w.name) + 1];
     ::strcpy(name, w.name);
 }
• No value returned
• Accesses w.name across client boundary
• The copy ctor initializes uninitialized memory
```

## Page 25

![Lecture 7 page 25](../page_images/07_7_Copy_Constructor/page_025.png)

Extracted text:

```text
Person: string name
• What if the name was a string (and not a char*)
 #include <string>
 class Person {
 public:
     Person( const string& );
     ~Person();
     void print();
     // ... other accessor fxns ...
 private:
     string name;    // embedded object (composition)
     // ... other data members...
 };
```

## Page 26

![Lecture 7 page 26](../page_images/07_7_Copy_Constructor/page_026.png)

Extracted text:

```text
Person: string name…
```

## Page 27

![Lecture 7 page 27](../page_images/07_7_Copy_Constructor/page_027.png)

Extracted text:

```text
Person: string name…
• In the default copy ctor, the compiler recursively
  calls the copy ctors for all member objects (and
  base classes).
```

## Page 28

![Lecture 7 page 28](../page_images/07_7_Copy_Constructor/page_028.png)

Extracted text:

```text
Person: string name…
• In the default copy ctor, the compiler recursively
  calls the copy ctors for all member objects (and
  base classes).
• default is memberwise initialization
```

## Page 29

![Lecture 7 page 29](../page_images/07_7_Copy_Constructor/page_029.png)

Extracted text:

```text
When are copy ctors called?
• During call by value
   void roster( Person );          // declare function
   Person child( "Ruby" );         // create object
   roster( child );        // call function
                                  void roster ( Person player );
      child
                                       player

              Ruby
                                            Ruby

        roster( child );
```

## Page 30

![Lecture 7 page 30](../page_images/07_7_Copy_Constructor/page_030.png)

Extracted text:

```text
When are copy ctors called?
• During initialization
   Person baby_a("Fred");
   // these use the copy ctor
   Person baby_b = baby_a;    // not an assignment
   Person baby_c( baby_a ); // not an assignment


          baby_a          baby_b       baby_c


           Fred             Fred         Fred
```

## Page 31

![Lecture 7 page 31](../page_images/07_7_Copy_Constructor/page_031.png)

Extracted text:

```text
When are copy ctors called?
                                         Person captain()
• During function return
    Person captain() {
       Person player("George");
       return player;
                                              George
    }
    ...
    Person who         who                 return player;
        = captain();
    ...                    George


                       who = captain()   copy
```

## Page 32

![Lecture 7 page 32](../page_images/07_7_Copy_Constructor/page_032.png)

Extracted text:

```text
Copies and overhead
```

## Page 33

![Lecture 7 page 33](../page_images/07_7_Copy_Constructor/page_033.png)

Extracted text:

```text
Copies and overhead
• Compilers can "optimize out" copies when
  safe!
```

## Page 34

![Lecture 7 page 34](../page_images/07_7_Copy_Constructor/page_034.png)

Extracted text:

```text
Copies and overhead
• Compilers can "optimize out" copies when
  safe!
• Programmers need to
 – Program for “dumb” compilers
 – Be ready to look for optimizations
```

## Page 35

![Lecture 7 page 35](../page_images/07_7_Copy_Constructor/page_035.png)

Extracted text:

```text
Example
Person copy_func( Person p ) {
    p.print();
    return p; // copy ctor called!
}

Person nocopy_func( char *who ) {
    return Person( who );
} // no copy needed!


code & demo
```

## Page 36

![Lecture 7 page 36](../page_images/07_7_Copy_Constructor/page_036.png)

Extracted text:

```text
Constructions vs. assignment
• Every object is constructed once
• Every object should be destroyed once
   •Forget to invoke delete
   •Invoke delete more than once
• Once an object is constructed, it can be the
  target of many assignment operations
```

## Page 37

![Lecture 7 page 37](../page_images/07_7_Copy_Constructor/page_037.png)

Extracted text:

```text
Copy ctor guidelines
```

## Page 38

![Lecture 7 page 38](../page_images/07_7_Copy_Constructor/page_038.png)

Extracted text:

```text
Copy ctor guidelines
• In most cases, you don’t have to write.
• Be explicit when necessary, e.g., managing raw
  pointers.
  - create your own copy ctor
• If you don't need one declare a private copy ctor (no
  need to define the body).
  - prevents creation of a default copy constructor
  - generates a compiler error for copy
```

## Page 39

![Lecture 7 page 39](../page_images/07_7_Copy_Constructor/page_039.png)

Extracted text:

```text
Copy ctor guidelines
• In most cases, you don’t have to write.
• Be explicit when necessary, e.g., managing raw
  pointers.
  - create your own copy ctor
• If you don't need one declare a private copy ctor (no
  need to define the body).
  - prevents creation of a default copy constructor
  - generates a compiler error for copy
  - use “Person(const Person &rhs) = delete;”
    (since C++11)
```

## Page 40

![Lecture 7 page 40](../page_images/07_7_Copy_Constructor/page_040.png)

Extracted text:

```text
static
```

## Page 41

![Lecture 7 page 41](../page_images/07_7_Copy_Constructor/page_041.png)

Extracted text:

```text
Static in C++
Two basic meanings
• Static storage
 – allocated once at a fixed address
• Visibility of a name
 – internal linkage
```

## Page 42

![Lecture 7 page 42](../page_images/07_7_Copy_Constructor/page_042.png)

Extracted text:

```text
Uses of “static” in C++
```

## Page 43

![Lecture 7 page 43](../page_images/07_7_Copy_Constructor/page_043.png)

Extracted text:

```text
Global static hidden in file
   . cpp file 1                   .cpp file 2

int g_global;             extern int g_global;
static int s_local;       void func();

void                      extern int s_local;
func() {                  int myfunc() {
...
}                             g_global += 2;
                              s_local *= g_global;
static                ?       func();
void                      }
hidden() { ...}
```

## Page 44

![Lecture 7 page 44](../page_images/07_7_Copy_Constructor/page_044.png)

Extracted text:

```text
Static inside functions
```

## Page 45

![Lecture 7 page 45](../page_images/07_7_Copy_Constructor/page_045.png)

Extracted text:

```text
Static inside functions
• Value is remembered for entire program
```

## Page 46

![Lecture 7 page 46](../page_images/07_7_Copy_Constructor/page_046.png)

Extracted text:

```text
Static inside functions
• Value is remembered for entire program
• Initialization occurs only once
```

## Page 47

![Lecture 7 page 47](../page_images/07_7_Copy_Constructor/page_047.png)

Extracted text:

```text
Static inside functions
• Value is remembered for entire program
• Initialization occurs only once
• Example:
  – count the number of times the function has beencalled
  void f() {
      static int num_calls = 0;
      ...
      num_calls++;
  }
```

## Page 48

![Lecture 7 page 48](../page_images/07_7_Copy_Constructor/page_048.png)

Extracted text:

```text
Static applied to objects
• Suppose you have a class
  class X {
      X(int, int);
      ~X();
      ...
  };

• And a function with a static X object
  void f() {
      static X my_X(10, 20);
      ...
  }
```

## Page 49

![Lecture 7 page 49](../page_images/07_7_Copy_Constructor/page_049.png)

Extracted text:

```text
Static applied to objects…
```

## Page 50

![Lecture 7 page 50](../page_images/07_7_Copy_Constructor/page_050.png)

Extracted text:

```text
Static applied to objects…
• Construction occurs when definition is
  encountered
 – Constructor called at-most once
 – The constructor arguments must be satisfied
• Destruction takes place on exit from program
 – Compiler assures LIFO order of destructors
```

## Page 51

![Lecture 7 page 51](../page_images/07_7_Copy_Constructor/page_051.png)

Extracted text:

```text
Conditional construction
• Example: conditional construction
 void f(int x) {
     if (x > 10) {
         static X my_X(x, x * 21);
         ...
     }
 }
•my_X
  – is constructed once, if f() is ever called with x >10
  – retains its value
  – destroyed only if constructed
```

## Page 52

![Lecture 7 page 52](../page_images/07_7_Copy_Constructor/page_052.png)

Extracted text:

```text
Global objects
```

## Page 53

![Lecture 7 page 53](../page_images/07_7_Copy_Constructor/page_053.png)

Extracted text:

```text
Global objects
• Consider
    #include "X.h"
    static X global_x(12, 34);
    static X global_x2(8, 16);
• Constructors are called before main() is entered
  – Order controlled by appearance in file
  – In this case, global_x before global_x2
  – main() is "no longer" the first function being called
• Destructors called when
  – main() exits
  – exit() iscalled
```

## Page 54

![Lecture 7 page 54](../page_images/07_7_Copy_Constructor/page_054.png)

Extracted text:

```text
Can we apply static to members?
```

## Page 55

![Lecture 7 page 55](../page_images/07_7_Copy_Constructor/page_055.png)

Extracted text:

```text
Can we apply static to members?
 • Static means
   –Hidden
   –Persistent
 • Hidden: A static member is a member
   – Obeys usual access rules
 • Persistent: Independent of instances
```

## Page 56

![Lecture 7 page 56](../page_images/07_7_Copy_Constructor/page_056.png)

Extracted text:

```text
Can we apply static to members?
 • Static means
   –Hidden
   –Persistent
 • Hidden: A static member is a member
   – Obeys usual access rules
 • Persistent: Independent of instances
 • Static members are class-wide
   – variables or
   – functions
```

## Page 57

![Lecture 7 page 57](../page_images/07_7_Copy_Constructor/page_057.png)

Extracted text:

```text
Static members
```

## Page 58

![Lecture 7 page 58](../page_images/07_7_Copy_Constructor/page_058.png)

Extracted text:

```text
Static members
• Static member variables
 –Global to all class member functions
 –Initialized once, at file scope
 –provide a place for this variable and init it in .cpp
 –No ‘static’ in .cpp

• Example: StatMem.h, StatMem.cpp
```

## Page 59

![Lecture 7 page 59](../page_images/07_7_Copy_Constructor/page_059.png)

Extracted text:

```text
Static members
• Static member functions
 –Have no implicit receiver ("this")
   •(why?)
 –Can access only static member variables
   •(or other globals)
 –Can’t be dynamically overridden

• Example: StatFun.h, StatFun.cpp
```

## Page 60

![Lecture 7 page 60](../page_images/07_7_Copy_Constructor/page_060.png)

Extracted text:

```text
To use static members
• <class name>::<static member>
• <object variable>.<static member>
```

## Page 61

![Lecture 7 page 61](../page_images/07_7_Copy_Constructor/page_061.png)

Extracted text:

```text
Container & STL
Object-Oriented Programming with C++
```

## Page 62

![Lecture 7 page 62](../page_images/07_7_Copy_Constructor/page_062.png)

Extracted text:

```text
[No extractable text]
```

## Page 63

![Lecture 7 page 63](../page_images/07_7_Copy_Constructor/page_063.png)

Extracted text:

```text
[No extractable text]
```

## Page 64

![Lecture 7 page 64](../page_images/07_7_Copy_Constructor/page_064.png)

Extracted text:

```text
[No extractable text]
```

## Page 65

![Lecture 7 page 65](../page_images/07_7_Copy_Constructor/page_065.png)

Extracted text:

```text
[No extractable text]
```

## Page 66

![Lecture 7 page 66](../page_images/07_7_Copy_Constructor/page_066.png)

Extracted text:

```text
[No extractable text]
```

## Page 67

![Lecture 7 page 67](../page_images/07_7_Copy_Constructor/page_067.png)

Extracted text:

```text
[No extractable text]
```

## Page 68

![Lecture 7 page 68](../page_images/07_7_Copy_Constructor/page_068.png)

Extracted text:

```text
[No extractable text]
```

## Page 69

![Lecture 7 page 69](../page_images/07_7_Copy_Constructor/page_069.png)

Extracted text:

```text
[No extractable text]
```

## Page 70

![Lecture 7 page 70](../page_images/07_7_Copy_Constructor/page_070.png)

Extracted text:

```text
[No extractable text]
```

## Page 71

![Lecture 7 page 71](../page_images/07_7_Copy_Constructor/page_071.png)

Extracted text:

```text
[No extractable text]
```

## Page 72

![Lecture 7 page 72](../page_images/07_7_Copy_Constructor/page_072.png)

Extracted text:

```text
[No extractable text]
```

## Page 73

![Lecture 7 page 73](../page_images/07_7_Copy_Constructor/page_073.png)

Extracted text:

```text
[No extractable text]
```

## Page 74

![Lecture 7 page 74](../page_images/07_7_Copy_Constructor/page_074.png)

Extracted text:

```text
[No extractable text]
```

## Page 75

![Lecture 7 page 75](../page_images/07_7_Copy_Constructor/page_075.png)

Extracted text:

```text
[No extractable text]
```

## Page 76

![Lecture 7 page 76](../page_images/07_7_Copy_Constructor/page_076.png)

Extracted text:

```text
[No extractable text]
```

## Page 77

![Lecture 7 page 77](../page_images/07_7_Copy_Constructor/page_077.png)

Extracted text:

```text
[No extractable text]
```

## Page 78

![Lecture 7 page 78](../page_images/07_7_Copy_Constructor/page_078.png)

Extracted text:

```text
[No extractable text]
```

## Page 79

![Lecture 7 page 79](../page_images/07_7_Copy_Constructor/page_079.png)

Extracted text:

```text
[No extractable text]
```

## Page 80

![Lecture 7 page 80](../page_images/07_7_Copy_Constructor/page_080.png)

Extracted text:

```text
[No extractable text]
```

## Page 81

![Lecture 7 page 81](../page_images/07_7_Copy_Constructor/page_081.png)

Extracted text:

```text
[No extractable text]
```

## Page 82

![Lecture 7 page 82](../page_images/07_7_Copy_Constructor/page_082.png)

Extracted text:

```text
[No extractable text]
```

## Page 83

![Lecture 7 page 83](../page_images/07_7_Copy_Constructor/page_083.png)

Extracted text:

```text
[No extractable text]
```

## Page 84

![Lecture 7 page 84](../page_images/07_7_Copy_Constructor/page_084.png)

Extracted text:

```text
[No extractable text]
```

## Page 85

![Lecture 7 page 85](../page_images/07_7_Copy_Constructor/page_085.png)

Extracted text:

```text
[No extractable text]
```

## Page 86

![Lecture 7 page 86](../page_images/07_7_Copy_Constructor/page_086.png)

Extracted text:

```text
[No extractable text]
```

## Page 87

![Lecture 7 page 87](../page_images/07_7_Copy_Constructor/page_087.png)

Extracted text:

```text
[No extractable text]
```

## Page 88

![Lecture 7 page 88](../page_images/07_7_Copy_Constructor/page_088.png)

Extracted text:

```text
[No extractable text]
```

## Page 89

![Lecture 7 page 89](../page_images/07_7_Copy_Constructor/page_089.png)

Extracted text:

```text
[No extractable text]
```

## Page 90

![Lecture 7 page 90](../page_images/07_7_Copy_Constructor/page_090.png)

Extracted text:

```text
[No extractable text]
```

## Page 91

![Lecture 7 page 91](../page_images/07_7_Copy_Constructor/page_091.png)

Extracted text:

```text
[No extractable text]
```

## Page 92

![Lecture 7 page 92](../page_images/07_7_Copy_Constructor/page_092.png)

Extracted text:

```text
[No extractable text]
```

## Page 93

![Lecture 7 page 93](../page_images/07_7_Copy_Constructor/page_093.png)

Extracted text:

```text
[No extractable text]
```

## Page 94

![Lecture 7 page 94](../page_images/07_7_Copy_Constructor/page_094.png)

Extracted text:

```text
[No extractable text]
```

## Page 95

![Lecture 7 page 95](../page_images/07_7_Copy_Constructor/page_095.png)

Extracted text:

```text
[No extractable text]
```

## Page 96

![Lecture 7 page 96](../page_images/07_7_Copy_Constructor/page_096.png)

Extracted text:

```text
[No extractable text]
```
