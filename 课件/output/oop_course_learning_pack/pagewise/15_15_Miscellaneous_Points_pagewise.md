# Lecture 15: 15 Miscellaneous Points

- Source: `15 Miscellaneous Points.pdf`
- Pages: 46
- Rendered page images: 46
- Contact sheet: [open](../contact_sheets/15_15_Miscellaneous_Points_contact.jpg)
- Raw extracted text: [open](../raw_texts/15-15 Miscellaneous Points.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 15 page 1](../page_images/15_15_Miscellaneous_Points/page_001.png)

Extracted text:

```text
Miscellaneous Points
  Object-Oriented Programming with C++
```

## Page 2

![Lecture 15 page 2](../page_images/15_15_Miscellaneous_Points/page_002.png)

Extracted text:

```text
Named casts
• The C-style cast is:
  • dangerous because it can do (logically different)
    conversion.
  • not search-friendly
• If you must cast things, use a named cast:
  • static_cast (less likely to make mistakes)
  • dynamic_cast
  • reinterpret_cast
  • const_cast
  •…
```

## Page 3

![Lecture 15 page 3](../page_images/15_15_Miscellaneous_Points/page_003.png)

Extracted text:

```text
Named casts
double d = 7.1;
int a;

a = d;                   // implicit

a = (int) d;             // explicit

a = static_cast<int>(d); // exact meaning
```

## Page 4

![Lecture 15 page 4](../page_images/15_15_Miscellaneous_Points/page_004.png)

Extracted text:

```text
Named casts
int a = 7;
double* p;

p = (double*) &a; // ok (but a is not a double)

p = static_cast<double*>(&a); // error

p = reinterpret_cast<double*>(&a); // ok: I really
                                   // mean it
```

## Page 5

![Lecture 15 page 5](../page_images/15_15_Miscellaneous_Points/page_005.png)

Extracted text:

```text
Named casts
const int c = 7;
int* q;

q = &c; // error

q = (int*)&c; // ok (but is *q=2 really allowed?)

q = static_cast<int*>(&c); // error

q = const_cast<int*>(&c); // I really mean it
```

## Page 6

![Lecture 15 page 6](../page_images/15_15_Miscellaneous_Points/page_006.png)

Extracted text:

```text
Named casts
struct A {
   virtual void f() {}
};
struct B : public A {};
struct C : public A {};

int main()
{
  A *pa = new B;
  C *pc = static_cast<C*>(pa);   // OK: but *pa is B!
}
```

## Page 7

![Lecture 15 page 7](../page_images/15_15_Miscellaneous_Points/page_007.png)

Extracted text:

```text
Named casts
struct A {
   virtual void f() {}
};
struct B : public A {};
struct C : public A {};

int main()
{
  A *pa = new B;
  C *pc = static_cast<C*>(pa); // OK: but *pa is B!
  C *pc = dynamic_cast<C*>(pa); // return nullptr
}
```

## Page 8

![Lecture 15 page 8](../page_images/15_15_Miscellaneous_Points/page_008.png)

Extracted text:

```text
Named casts
struct A {
   // virtual void f() {}
};
struct B : public A {};
struct C : public A {};

int main()
{
  A *pa = new B;
  C *pc = static_cast<C*>(pa); // OK: but *pa is B!
  C *pc = dynamic_cast<C*>(pa); // Error!
}
```

## Page 9

![Lecture 15 page 9](../page_images/15_15_Miscellaneous_Points/page_009.png)

Extracted text:

```text
Named casts
struct A {
   // virtual void f() {}
};
struct B : public A {};
struct C : public A {};

int main()
{
  A *pa = new B;
  C *pc = static_cast<C*>(pa);   // OK: but *pa is B!
}
```

## Page 10

![Lecture 15 page 10](../page_images/15_15_Miscellaneous_Points/page_010.png)

Extracted text:

```text
Named casts
struct A {
   // virtual void f() {}
};
struct B : public A {};
struct C : public A {};
struct D {};

int main()
{
  A *pa = new B;
  D *pd = static_cast<D*>(pa);   // Error!

    return 0;
}
```

## Page 11

![Lecture 15 page 11](../page_images/15_15_Miscellaneous_Points/page_011.png)

Extracted text:

```text
Multiple inheritance
                          Employee
Temporary


              Secretary     MTS       Administrator

        TempSec
                              Supervisor

                                           President
 Consultant
```

## Page 12

![Lecture 15 page 12](../page_images/15_15_Miscellaneous_Points/page_012.png)

Extracted text:

```text
Mix and match
class Employee {                 class Consultant:
protected:                          public MTS,
    String name;                    public Temporary {
    EmpID id;                    …
};                               };

class MTS : public Employee {
protected:
    Degrees degree_info;        • Consultant picks up the
};                                attributes of both MTS and
                                  Temporary.
class Temporary {                 – name
protected:                        – id
    Company employer;             – degree_info
};                                – employer
```

## Page 13

![Lecture 15 page 13](../page_images/15_15_Miscellaneous_Points/page_013.png)

Extracted text:

```text
MI complicates data layouts

        Employee
         Employee

           MTS

         Temporary
           Consultant
```

## Page 14

![Lecture 15 page 14](../page_images/15_15_Miscellaneous_Points/page_014.png)

Extracted text:

```text
iostream package
```

## Page 15

![Lecture 15 page 15](../page_images/15_15_Miscellaneous_Points/page_015.png)

Extracted text:

```text
Vanilla MI
• Members are duplicated                     IOS



• Derived class has access                         streambuf


  to full copies of each base   istream                                ostream

  class
                                   streambuf                   streambuf
• This can be useful!
  –Multiple links for lists       iostream

  –Multiple streambufs for
   input and output                                streambuf




                                                   streambuf
```

## Page 16

![Lecture 15 page 16](../page_images/15_15_Miscellaneous_Points/page_016.png)

Extracted text:

```text
More on MI …
struct B1 { int m_i; };
struct D1 : public B1 {};
struct D2 : public B1 {};
struct M : public D1, public D2 {};

int main() {
  M m; // OK
  B1* p = &m; // ERROR: which B1???
  B1* p1 = static_cast<D1*>(&m); // OK
  B1* p2 = static_cast<D2*>(&m); // OK
}
B1 is a replicated sub-object of M.
```

## Page 17

![Lecture 15 page 17](../page_images/15_15_Miscellaneous_Points/page_017.png)

Extracted text:

```text
Replicated bases
• Normally replicated bases aren’t a problem
  (usage of B1 by D1 and D2 is an implementation
  detail).
• Replication becomes a problem if replicated data
  makes for confusing logic:

M m;
m.m_i++; // ERROR: D1::B1.m_i or D2::B1.m_i?
```

## Page 18

![Lecture 15 page 18](../page_images/15_15_Miscellaneous_Points/page_018.png)

Extracted text:

```text
Safe uses
• Protocol classes
```

## Page 19

![Lecture 15 page 19](../page_images/15_15_Miscellaneous_Points/page_019.png)

Extracted text:

```text
Protocol / Interface classes
• Abstract base class with
  – All non-static member functions are pure virtual except
    destructor
  – Virtual destructor with empty body
  – No non-static member variables, inherited or
    otherwise
    •May contain static members
```

## Page 20

![Lecture 15 page 20](../page_images/15_15_Miscellaneous_Points/page_020.png)

Extracted text:

```text
Example interface
• Unix character device
   class CDevice {
   public:
       virtual ~CDevice() {}

        virtual int read(...) = 0;
        virtual int write(...) = 0;
        virtual int open(...) = 0;
        virtual int close(...) = 0;
        virtual int ioctl(...) = 0;
   };
```

## Page 21

![Lecture 15 page 21](../page_images/15_15_Miscellaneous_Points/page_021.png)

Extracted text:

```text
What about sharing?
```

## Page 22

![Lecture 15 page 22](../page_images/15_15_Miscellaneous_Points/page_022.png)

Extracted text:

```text
What about sharing?
• How do you avoid having two streambufs?
```

## Page 23

![Lecture 15 page 23](../page_images/15_15_Miscellaneous_Points/page_023.png)

Extracted text:

```text
What about sharing?
• How do you avoid having two streambufs?
• Base classes can be virtual
  –To C++ people, “virtual” means “indirect”
```

## Page 24

![Lecture 15 page 24](../page_images/15_15_Miscellaneous_Points/page_024.png)

Extracted text:

```text
What about sharing?
• How do you avoid having two streambufs?
• Base classes can be virtual
  –To C++ people, “virtual” means “indirect”
• Virtual member functions have dynamic binding
  –They use pointer indirection
```

## Page 25

![Lecture 15 page 25](../page_images/15_15_Miscellaneous_Points/page_025.png)

Extracted text:

```text
What about sharing?
• How do you avoid having two streambufs?
• Base classes can be virtual
  –To C++ people, “virtual” means “indirect”
• Virtual member functions have dynamic binding
  –They use pointer indirection
• Virtual base classes are represented indirectly
  –They use pointer indirection
```

## Page 26

![Lecture 15 page 26](../page_images/15_15_Miscellaneous_Points/page_026.png)

Extracted text:

```text
Using virtual base classes
• Virtual base classes are                            IOS

  shared                                                     streambuf


• Derived classes have a
                                                  istream                ostream
  single copy of the virtual
  base                         streambuf                                              streambuf
                                                  iostream

• Full control over sharing
  –Up to you to choose
                                                                                   streambuf

• Cost is in complications
                                       has-a
                                           is-a
```

## Page 27

![Lecture 15 page 27](../page_images/15_15_Miscellaneous_Points/page_027.png)

Extracted text:

```text
Virtual bases
struct B1 { int m_i; };
struct D1 : virtual public B1 {};
struct D2 : virtual public B1 {};
struct M : public D1, public D2 {};
int main() {
    M m;   // OK
    m.m_i++; // OK, there is only one B1 in m
    B1* p = new M; // OK
}
```

## Page 28

![Lecture 15 page 28](../page_images/15_15_Miscellaneous_Points/page_028.png)

Extracted text:

```text
Complications of MI
• Name conflicts                  • Code in virtual bases
  –Dominance rule                   called more than once
• Order of construction           • Compilers are still iffy
  –Who constructs virtual base?
• Virtual bases not declared
                                  • Moral:
  when you need them                – Use sparingly
                                    – Avoid diamond patterns
              A                        • expensive
                                       • hard
         B          C


              D
```

## Page 29

![Lecture 15 page 29](../page_images/15_15_Miscellaneous_Points/page_029.png)

Extracted text:

```text
Virtual bases
• Use of virtual base imposes some runtime and
  space overhead.
• If replication isn’t a problem then you don’t
  need to make bases virtual.
• Abstract base classes (that hold no data except
  for a vptr) can be replicated with no problem –
  virtual base can be eliminated.
```

## Page 30

![Lecture 15 page 30](../page_images/15_15_Miscellaneous_Points/page_030.png)

Extracted text:

```text
TIPS for MI
• In general, SAY



                    NO
```

## Page 31

![Lecture 15 page 31](../page_images/15_15_Miscellaneous_Points/page_031.png)

Extracted text:

```text
Avoiding name clashes
• Including duplicate names at global scope is a problem:

// old1.h
   void f();
   void g();

// old2.h
   void f();
   void g();
```

## Page 32

![Lecture 15 page 32](../page_images/15_15_Miscellaneous_Points/page_032.png)

Extracted text:

```text
Avoiding name clashes (cont)
• Wrap declarations in namespaces.

// old1.h
namespace old1 {
   void f();
   void g();
}

// old2.h
namespace old2 {
   void f();
   void g();
}
```

## Page 33

![Lecture 15 page 33](../page_images/15_15_Miscellaneous_Points/page_033.png)

Extracted text:

```text
Namespace
• Expresses a logical grouping of classes, functions,
  variables, etc.
• A namespace is a scope just like a class
• Preferred when name encapsulation is needed
   namespace Math {
     double abs(double);
     double sqrt(double);
     int trunc(double);
     ...
   } // Note: No terminating end colon!
```

## Page 34

![Lecture 15 page 34](../page_images/15_15_Miscellaneous_Points/page_034.png)

Extracted text:

```text
Defining namespaces
• Place namespaces in include files:
```

## Page 35

![Lecture 15 page 35](../page_images/15_15_Miscellaneous_Points/page_035.png)

Extracted text:

```text
Defining namespaces
• Place namespaces in include files:
  // Mylib.h
  namespace MyLib {
      void foo();
      class Cat {
      public:
          void Meow();
      };
  }
```

## Page 36

![Lecture 15 page 36](../page_images/15_15_Miscellaneous_Points/page_036.png)

Extracted text:

```text
Defining namespace functions
 • Use normal scoping to implement functions in
   namespaces.
 // MyLib.cpp
 #include "MyLib.h"

 void MyLib::foo() { cout << "foo\n"; }
 void MyLib::Cat::Meow() {
     cout << "meow\n";
 }
```

## Page 37

![Lecture 15 page 37](../page_images/15_15_Miscellaneous_Points/page_037.png)

Extracted text:

```text
Using names from a namespace
• Use scope resolution to qualify names from a
  namespace.
• Can be tedious and distracting.
#include "MyLib.h"
int main()
{
   MyLib::foo();
   MyLib::Cat c;
   c.Meow();
}
```

## Page 38

![Lecture 15 page 38](../page_images/15_15_Miscellaneous_Points/page_038.png)

Extracted text:

```text
using-declarations
• Introduces a local synonym for name
• States in one place where a name comes from.
• Eliminates redundant scope qualification:

 int main() {
     using MyLib::foo;
     using MyLib::Cat;
     foo();
     Cat c;
     c.Meow();
 }
```

## Page 39

![Lecture 15 page 39](../page_images/15_15_Miscellaneous_Points/page_039.png)

Extracted text:

```text
using-directives
• Makes all names from a namespace available.
•Can be used as a notational convenience.
 int main() {
    using namespace std;
    using namespace MyLib;
    foo();
    Cat c;
    c.Meow();
    cout << "hello" << endl;
 }
```

## Page 40

![Lecture 15 page 40](../page_images/15_15_Miscellaneous_Points/page_040.png)

Extracted text:

```text
Ambiguities
• Using-directives may create potential ambiguities.
• Consider:
  // Mylib.h
 namespace XLib {
     void x();
     void y();
 }

 namespace YLib {
     void y();
     void z();
 }
```

## Page 41

![Lecture 15 page 41](../page_images/15_15_Miscellaneous_Points/page_041.png)

Extracted text:

```text
Ambiguities (cont)
• Using-directives only make the names available.
• Ambiguities arise only when you make calls.
• Use scope resolution to resolve.
 int main() {
   using namespace XLib;
   using namespace YLib;
   x();       // OK
   y();       // Error: ambiguous
   XLib::y(); // OK, resolves to XLib
   z();       // OK
 }
```

## Page 42

![Lecture 15 page 42](../page_images/15_15_Miscellaneous_Points/page_042.png)

Extracted text:

```text
Namespace aliases
• Namespace names that are too short may clash
• Names that are too long are hard to work with
• Use aliasing to create workable names
• Aliasing can be used to version libraries.
 namespace supercalifragilistic {
     void f();
 }
 namespace short_ns = supercalifragilistic;
 short_ns::f();
```

## Page 43

![Lecture 15 page 43](../page_images/15_15_Miscellaneous_Points/page_043.png)

Extracted text:

```text
Namespace composition
• Compose new namespaces using names from other ones.
• Using-declarations can resolve potential clashes.
• Explicitly defined functions take precedence.
 namespace first {
   void x();
   void y();
 }
 namespace second {
   void y();
   void z();
 }
```

## Page 44

![Lecture 15 page 44](../page_images/15_15_Miscellaneous_Points/page_044.png)

Extracted text:

```text
Namespace composition (cont)
namespace mine {
    using namespace first;
    using namespace second;
    using first::y; // resolve clashes
    void mystuff();
    ...
}
int main() {
    mine::x();
    mine::y(); // call first::y()
    mine::mystuff();
}
```

## Page 45

![Lecture 15 page 45](../page_images/15_15_Miscellaneous_Points/page_045.png)

Extracted text:

```text
Namespace selection
• Compose namespaces by selecting a few features
  from other namespaces.
• Choose only the names you want rather than all.
• Changes to “orig” declaration become reflected in
  “mine”.
 namespace mine {
   using orig::Cat; // use Cat class from orig
   void x();
   void y();
 }
```

## Page 46

![Lecture 15 page 46](../page_images/15_15_Miscellaneous_Points/page_046.png)

Extracted text:

```text
Namespaces are open
• Multiple namespace declarations add to the
  same namespace.
 – Namespace can be distributed across multiple files.

 //header1.h
 namespace X {
     void f();
 }

 // header2.h
 namespace X {
     void g(); // X how has f() and g();
 }
```
