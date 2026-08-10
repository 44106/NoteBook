# Lecture 7: 7 Copy Constructor

Source: `7 Copy Constructor.pdf`
Pages: 96

## Page 1

References as class members
• Declared without initial value

## Page 2

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

## Page 3

       Returning references
• Functions can return references
  – But they should refer to non-local variables!

   #include <cassert>
   const int SIZE = 32;
   double myarray[SIZE];
   double& subscript(const int i) {
      return myarray[i];
   }

## Page 4

           Example
main() {
   for (int i = 0; i < SIZE; i++) {
      myarray[i] = i * 0.5;
   }
   double value = subscript(12);
   subscript(3) = 34.5;
}

## Page 5

const in functions arguments
• Passing by const value – don’t do it
• Passing by const reference
      Person(const string& name, int weight);
 – won’t change the string object
 – more efficient than pass by value (copy)
 – const qualifier protects from change

## Page 6

 const reference parameters
• What if you don’t want to change the argument
• Use const modifier
   // y is a constant! Can’t be modified
   void func(const int& y, int& z) {
      z = z * 5; // ok
      y += 8; // error!
   };

## Page 7

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

## Page 8

   const in function returns
• return by const value
   – basically it means nothing
• return by const pointer or reference
   – depends on what you want your client to do
     with the return value


 code & demo

## Page 9

      Copy Ctor
Object-Oriented Programming with C++

## Page 10

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

## Page 11

The copy constructor

## Page 12

       The copy constructor
• Copying is implemented by the copy constructor

## Page 13

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

## Page 14

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

## Page 15

                Choices
Copy pointer

        Some Text




code & demo

## Page 16

                Choices
Copy pointer        Copy entire block

        Some Text          Some Text




                           Some Text



code & demo

## Page 17

Character strings




     C   +         +   '\0'
             /50

## Page 18

          Character strings
• In C++, a character string is
  – An array of characters
  – With a special terminator — ‘\0’ or ASCII null
• The string “C++” is represented, in memory,
  by an array of four (4, count’em) characters




                      C   +         +   '\0'
                              /50

## Page 19

 Standard C library String fxns
• Declared in <cstring>

## Page 20

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

## Page 21

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

## Page 22

Person copy constructor

## Page 23

    Person copy constructor
• To Person declaration add copy ctor prototype:
 Person( const Person& w );          // copy ctor
• To Person .cpp add copy ctor defintion:
 Person::Person( const Person& w ) {
     name = new char[::strlen(w.name) + 1];
     ::strcpy(name, w.name);
 }

## Page 24

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

## Page 25

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

## Page 26

Person: string name…

## Page 27

     Person: string name…
• In the default copy ctor, the compiler recursively
  calls the copy ctors for all member objects (and
  base classes).

## Page 28

     Person: string name…
• In the default copy ctor, the compiler recursively
  calls the copy ctors for all member objects (and
  base classes).
• default is memberwise initialization

## Page 29

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

## Page 30

  When are copy ctors called?
• During initialization
   Person baby_a("Fred");
   // these use the copy ctor
   Person baby_b = baby_a;    // not an assignment
   Person baby_c( baby_a ); // not an assignment


          baby_a          baby_b       baby_c


           Fred             Fred         Fred

## Page 31

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

## Page 32

Copies and overhead

## Page 33

      Copies and overhead
• Compilers can "optimize out" copies when
  safe!

## Page 34

      Copies and overhead
• Compilers can "optimize out" copies when
  safe!
• Programmers need to
 – Program for “dumb” compilers
 – Be ready to look for optimizations

## Page 35

              Example
Person copy_func( Person p ) {
    p.print();
    return p; // copy ctor called!
}

Person nocopy_func( char *who ) {
    return Person( who );
} // no copy needed!


code & demo

## Page 36

Constructions vs. assignment
• Every object is constructed once
• Every object should be destroyed once
   •Forget to invoke delete
   •Invoke delete more than once
• Once an object is constructed, it can be the
  target of many assignment operations

## Page 37

Copy ctor guidelines

## Page 38

        Copy ctor guidelines
• In most cases, you don’t have to write.
• Be explicit when necessary, e.g., managing raw
  pointers.
  - create your own copy ctor
• If you don't need one declare a private copy ctor (no
  need to define the body).
  - prevents creation of a default copy constructor
  - generates a compiler error for copy

## Page 39

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

## Page 40

static

## Page 41

                Static in C++
Two basic meanings
• Static storage
 – allocated once at a fixed address
• Visibility of a name
 – internal linkage

## Page 42

Uses of “static” in C++

## Page 43

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

## Page 44

Static inside functions

## Page 45

      Static inside functions
• Value is remembered for entire program

## Page 46

      Static inside functions
• Value is remembered for entire program
• Initialization occurs only once

## Page 47

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

## Page 48

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

## Page 49

Static applied to objects…

## Page 50

  Static applied to objects…
• Construction occurs when definition is
  encountered
 – Constructor called at-most once
 – The constructor arguments must be satisfied
• Destruction takes place on exit from program
 – Compiler assures LIFO order of destructors

## Page 51

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

## Page 52

Global objects

## Page 53

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

## Page 54

Can we apply static to members?

## Page 55

Can we apply static to members?
 • Static means
   –Hidden
   –Persistent
 • Hidden: A static member is a member
   – Obeys usual access rules
 • Persistent: Independent of instances

## Page 56

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

## Page 57

Static members

## Page 58

            Static members
• Static member variables
 –Global to all class member functions
 –Initialized once, at file scope
 –provide a place for this variable and init it in .cpp
 –No ‘static’ in .cpp

• Example: StatMem.h, StatMem.cpp

## Page 59

             Static members
• Static member functions
 –Have no implicit receiver ("this")
   •(why?)
 –Can access only static member variables
   •(or other globals)
 –Can’t be dynamically overridden

• Example: StatFun.h, StatFun.cpp

## Page 60

     To use static members
• <class name>::<static member>
• <object variable>.<static member>

## Page 61

Container & STL
Object-Oriented Programming with C++

## Page 62

[No extractable text]

## Page 63

[No extractable text]

## Page 64

[No extractable text]

## Page 65

[No extractable text]

## Page 66

[No extractable text]

## Page 67

[No extractable text]

## Page 68

[No extractable text]

## Page 69

[No extractable text]

## Page 70

[No extractable text]

## Page 71

[No extractable text]

## Page 72

[No extractable text]

## Page 73

[No extractable text]

## Page 74

[No extractable text]

## Page 75

[No extractable text]

## Page 76

[No extractable text]

## Page 77

[No extractable text]

## Page 78

[No extractable text]

## Page 79

[No extractable text]

## Page 80

[No extractable text]

## Page 81

[No extractable text]

## Page 82

[No extractable text]

## Page 83

[No extractable text]

## Page 84

[No extractable text]

## Page 85

[No extractable text]

## Page 86

[No extractable text]

## Page 87

[No extractable text]

## Page 88

[No extractable text]

## Page 89

[No extractable text]

## Page 90

[No extractable text]

## Page 91

[No extractable text]

## Page 92

[No extractable text]

## Page 93

[No extractable text]

## Page 94

[No extractable text]

## Page 95

[No extractable text]

## Page 96

[No extractable text]
