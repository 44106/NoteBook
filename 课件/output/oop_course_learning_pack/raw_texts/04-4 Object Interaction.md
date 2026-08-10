# Lecture 4: 4 Object Interaction

Source: `4 Object Interaction.pdf`
Pages: 104

## Page 1

Object Interaction
 Object-Oriented Programming with C++

## Page 2

Object oriented programming
• Objects send and receive messages (object do things!)

        Data                            Data

      Methods                          Methods


                        Data

                      Methods

## Page 3

  Object send messages
• Messages are
 - Composed by the sender
 - Interpreted by the receiver
 - Implemented by methods

• Messages
 - May return results
 - May cause receiver to change state, i.e., side effects

## Page 4

          Encapsulation
• Bundle data and methods dealing with these
  data together in an object
• Hide the details of the data and the action
• Restrict access only to the publicized
  methods

## Page 5

                 Abstract
• Abstraction is the ability to ignore details of
 parts to focus attention on a higher level of a
 problem.

• Modularization is the process of dividing a
 whole into well-defined parts, which can be
 built and examined separately, and which
 interact in well-defined ways.

## Page 6

Clock display

## Page 7

Modularizing the clock display

                    One 4-digits display?




  Or two 2-digits
  displays?

## Page 8

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

## Page 9

Class diagram
       ClockDisplay
-hours : NumberDisplay
-minutes : NumberDisplay
+start()




       NumberDisplay
    -limit : int
    -value : int
    +increase() : boolean

## Page 10

Implementation - ClockDisplay

 class ClockDisplay {
     NumberDisplay hours;
     NumberDisplay minutes;

     Constructor and methods omitted.


 }

## Page 11

Implementation - ClockDisplay

    class NumberDisplay {
        int limit;
        int value;

        Constructor and methods omitted.


    }

## Page 12

C'tor and D'tor

## Page 13

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

## Page 14

[No extractable text]

## Page 15

Guaranteed initialization with
      the constructor
 • If a class has a constructor, the compiler
    automatically calls that constructor at the point
    an object is created, before client programmers
    can get their hands on the object.
 • The name of the constructor is the same as the
    name of the class.

## Page 16

How does a constructor work?
      class X {
        int i;
      public:
        X();
      };

## Page 17

How does a constructor work?
      class X {
        int i;
      public:     constructor
        X();
      };

## Page 18

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

## Page 19

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

## Page 20

Constructors with arguments

  • The constructor can have arguments to allow
     you to specify how an object is created, give it
     initialization values, and so on.


  Tree(int i) {…}
  Tree t(12);

  • Constructor1.cpp

## Page 21

            The destructor
• In C++, cleanup is as important as initialization and is
 therefore guaranteed with the destructor.
• The destructor is named after the name of the class
 with a leading tilde (~). The destructor never has any
 arguments.

## Page 22

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

## Page 23

When is a destructor called?
  • The destructor is called automatically by the
   compiler when the object goes out of scope.

## Page 24

Storage allocation

## Page 25

    Storage allocation
• The compiler allocates all the storage for a
 scope at the opening brace of that scope.

## Page 26

    Storage allocation
• The compiler allocates all the storage for a
 scope at the opening brace of that scope.

• The constructor call doesn’t happen until the
  sequence point where the object is deﬁned.

• Example: Nojump.cpp

## Page 27

Aggregate initialization

## Page 28

   Aggregate initialization
• int a[5] = {1,2,3,4,5};

## Page 29

   Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};

## Page 30

   Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c

## Page 31

   Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};

## Page 32

   Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
• X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }

## Page 33

   Aggregate initialization
• int a[5] = {1,2,3,4,5};
• int b[6] = {5};
• int c[] = {1,2,3,4};
   - sizeof c / sizeof *c
• struct X { int i; float f; char c; };
   - X x1 = {1, 2.2, 'c'};
• X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }
• struct Y { float f; int i; Y(int a); };

## Page 34

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

## Page 35

    The default constructor
 A default constructor is one that can be called
with no arguments.

## Page 36

    The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {
    float f;
    int i;
    Y(int a);
};

## Page 37

    The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
    int i;
    Y(int a);
};

## Page 38

    The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);
};

## Page 39

    The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);                 Y y3[7];
};

## Page 40

    The default constructor
 A default constructor is one that can be called
with no arguments.

struct Y {          Y y1[] = { Y(1), Y(2), Y(3) };
    float f;
                         Y y2[2] = { Y(1) };
    int i;
    Y(int a);                 Y y3[7];
};                              Y y4;

## Page 41

“auto” default constructor

## Page 42

“auto” default constructor
• If you have a constructor, the compiler ensures
  that construction always happens.

## Page 43

“auto” default constructor
• If you have a constructor, the compiler ensures
  that construction always happens.

• If (and only if) there are no constructors for a
  class (struct or class), the compiler will
  automatically create one for you.

## Page 44

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

## Page 45

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

## Page 46

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

## Page 47

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

## Page 48

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

## Page 49

Call the functions in a class
 Point a;
 a.print();

  There is a relationship with the function be
   called and the variable to call it.

  The function itself knows it is doing something
   w/ the variable.

## Page 50

this: the hidden parameter
 this is a hidden parameter for all member functions,
  with the type of the class

    void Point::print()
     ➔ (can be regarded as)
    void Point::print(Point *this)

## Page 51

this: the hidden parameter
 To call the function, you must specify a variable

    Point a;
    a.print();
     ➔ (can be regarded as)
    Point::print(&a);

## Page 52

this: the pointer to the caller
 Inside member functions, you can use this as the
  pointer to the variable that calls the function.

 this is a natural parameter of all class member
  functions that you cannot define, but can use directly.

## Page 53

Initialization

## Page 54

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

## Page 55

Initialization vs. assignment

## Page 56

Initialization vs. assignment
 Student::Student(string s):name(s) {}




 Student::Student(string s) {name=s;}

## Page 57

Initialization vs. assignment
 Student::Student(string s):name(s) {}
  initialization
  before constructor body


 Student::Student(string s) {name=s;}

## Page 58

Initialization vs. assignment
 Student::Student(string s):name(s) {}
  initialization
  before constructor body


 Student::Student(string s) {name=s;}
  assignment
  inside constructor body
  string must have a default constructor

## Page 59

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

## Page 60

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

## Page 61

 Overload and auto-cast
void f(int i);
void f(double d);

f('a'); //ambiguous
f(2);
f(2L); // ambiguous
f(3.2f);

## Page 62

      Default arguments

•   A default argument is a value given in the
    declaration that the compiler automatically
    inserts if you don’t provide a value in the
    function call.
Stash(int size, int initQuantity = 0);

## Page 63

• Todefine a function with an argument list, defaults
  must be added from right to left.
   int harpo(int n, int m = 4, int j = 5);
   int chico(int n, int m = 6, int j); //illegal
   int groucho(int k = 1, int m = 2, int n = 3);

   beeps = harpo(2);
   beeps = harpo(1,8);
   beeps = harpo(8,7,6);

## Page 64

Constant objects

## Page 65

            Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?

## Page 66

            Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?

•   How can the object be protected from change?

## Page 67

               Constant objects
•   What if an object is const?

    const Currency the_raise(42, 38);


•   What member functions can access the internals?

•   How can the object be protected from change?

•   Solution: declare member functions const
    –   Programmer declares member functions to be safe

## Page 68

Const member functions
•Cannot modify their objects
int Date::set_day(int d) {
    //...error check d here...
    day = d; // ok, non-const so can modify
}

int Date::get_day() const {

     return day; // ok
}

## Page 69

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

## Page 70

Const member function usage
 •   Repeat the const keyword in the definition as well as
     the declaration

     int get_day() const;

     int get_day() const { return day };

 •   Function members that do not modify data should be
     declared const

 •   const member functions are safe for const objects

## Page 71

Const objects

## Page 72

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

## Page 73

            Constant in class
  class A {

     const int i;

  };



• has to be initialized in initializer list of the constructor

## Page 74

Compile-time constants in classes

## Page 75

Compile-time constants in classes
  class HasArray {
     const int size;
     int array[size]; // ERROR!
     ...
  };

## Page 76

Compile-time constants in classes
  class HasArray {
     const int size;
     int array[size]; // ERROR!
     ...
  };

• Make the const value static:
  - static const int size = 100;
  - static indicates only one per class (not one per object)

## Page 77

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

## Page 78

Inline function

## Page 79

Overhead for a function call
  • The processing time required by a
     device prior to the execution of a
     command

    • Push parameters
    • Push return address
    • Prepare return values
    • Pop all pushed

## Page 80

                  Inline
int f(int i) {
  return i*2;
}
main() {
  int a = 4;
  int b = f(a);
}

## Page 81

         Inline Functions

• An inline function is expanded in place, like
   a preprocessor macro, so the overhead of
   the function call is eliminated.

## Page 82

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

## Page 83

inline int f(int i) {
  return i * 2;
}
int main() {
  int a = 4;
  int b = f(a);
}

## Page 84

inline int f(int i) {
  return i * 2;
}
int main() {          int main() {
  int a = 4;            int a = 4;
  int b = f(a);         int b = a + a;
}                     }

## Page 85

          Inline Functions
inline int plusOne(int x) { return ++x; };

• The “definition” of an inline function should be
    put in a header file.
• An inline function definition may not generate
    any code in .obj file.
• It is declaration rather than definition.

## Page 86

Inline functions in header file
   • So you can put inline functions’ bodies in
      header file. Then #include it where the
      function is needed.
   • Never be afraid of multi-definition of
      inline functions.
   • Definitions of inline functions are just
      declarations.

## Page 87

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

## Page 88

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

## Page 89

   Inline inside classes
• Any  function you define inside a
  class declaration is automatically an
   inline.
   •    Example:
        Inline.cpp

## Page 90

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

## Page 91

     Reducing clutter
• Member functions defined within classes
   use the Latin in situ (in place) and maintains
   that all definitions should be placed outside
   the class to keep the interface clean.


• Example: Noinsitu.cpp

## Page 92

Inline or not?

## Page 93

             Inline or not?
• Inline:
 • Small functions, 2 or 3lines
 • Frequently called functions, e.g. inside loops

## Page 94

             Inline or not?
• Inline:
 • Small functions, 2 or 3lines
 • Frequently called functions, e.g. inside loops
• Not inline?
  • Very large functions, say, more than 20 lines
  • Recursive functions

## Page 95

 Inline may not in-line
• The compiler does not have to honor your
  request to make a function inline. It might
  decide the function is too large or notice
  that it calls itself (recursion is not allowed or
  indeed possible for inline functions), or the
  feature might not be implemented for your
  particular compiler.

## Page 96

 Inline may not in-line
• Nowadays, the keyword inline for functions
  comes to mean "multiple definitions are
  permitted" rather than "inlining is preferred".

## Page 97

[No extractable text]

## Page 98

[No extractable text]

## Page 99

[No extractable text]

## Page 100

[No extractable text]

## Page 101

[No extractable text]

## Page 102

[No extractable text]

## Page 103

[No extractable text]

## Page 104

[No extractable text]
