# Lecture 03: 3 Class

- Source: `3 Class.pdf`
- Pages: 48
- Rendered page images: 48
- Contact sheet: [open](../contact_sheets/03_3_Class_contact.jpg)
- Raw extracted text: [open](../raw_texts/03-3 Class.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 3 page 1](../page_images/03_3_Class/page_001.png)

Extracted text:

```text
Class
Object-Oriented Programming with C++
```

## Page 2

![Lecture 3 page 2](../page_images/03_3_Class/page_002.png)

Extracted text:

```text
p'




𝑦       p




    𝑥
```

## Page 3

![Lecture 3 page 3](../page_images/03_3_Class/page_003.png)

Extracted text:

```text
Point
typedef struct point {
    int x;
    int y;
} Point;
```

## Page 4

![Lecture 3 page 4](../page_images/03_3_Class/page_004.png)

Extracted text:

```text
Point
typedef struct point {
    int x;
    int y;
} Point;

Point a;
a.x = 1;a.y = 2;
```

## Page 5

![Lecture 3 page 5](../page_images/03_3_Class/page_005.png)

Extracted text:

```text
Point
typedef struct point {
    int x;
    int y;
} Point;

Point a;
a.x = 1;a.y = 2;
void print(const Point* p) {
    printf("%d %d\n", p->x, p->y);
}
```

## Page 6

![Lecture 3 page 6](../page_images/03_3_Class/page_006.png)

Extracted text:

```text
Point
typedef struct point {
    int x;
    int y;
} Point;

Point a;
a.x = 1;a.y = 2;
void print(const Point* p) {
    printf("%d %d\n", p->x, p->y);
}
print(&a);
```

## Page 7

![Lecture 3 page 7](../page_images/03_3_Class/page_007.png)

Extracted text:

```text
move (dx, dy)?
```

## Page 8

![Lecture 3 page 8](../page_images/03_3_Class/page_008.png)

Extracted text:

```text
move (dx, dy)?


void move(Point* p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}
```

## Page 9

![Lecture 3 page 9](../page_images/03_3_Class/page_009.png)

Extracted text:

```text
Prototypes

typedef struct point {
    int x;
    int y;
} Point;

void print(const Point* p);
void move(Point* p, int dx, int dy);
```

## Page 10

![Lecture 3 page 10](../page_images/03_3_Class/page_010.png)

Extracted text:

```text
Usage

Point a;
Point b;
a.x = b.x = 1; a.y = b.y = 1;
move(&a,2,2);
print(&a);
print(&b);
```

## Page 11

![Lecture 3 page 11](../page_images/03_3_Class/page_011.png)

Extracted text:

```text
C++ version
class Point {
public:
    void init(int x, int y);
    void move(int dx, int dy);
    void print() const;

private:
    int x;
    int y;
} ;
```

## Page 12

![Lecture 3 page 12](../page_images/03_3_Class/page_012.png)

Extracted text:

```text
Implementations
void Point::init(int ix, int iy) {
    x = ix; y = iy;
}
void Point::move(int dx, int dy) {
    x+= dx; y+= dy;
}
void Point::print() const {
    cout << x << ' ' << y << endl;
}
```

## Page 13

![Lecture 3 page 13](../page_images/03_3_Class/page_013.png)

Extracted text:

```text
C vs. C++
typedef struct point {        class Point {
    int x;                    public:
    int y;                        void init(int x, int y);
} Point;                          void print() const;
                                  void move(int dx, int dy);
void print(const Point* p);
void move(Point* p,           private:
          int dx,                 int x;
          int dy);                int y;
                              };
Point a;
a.x = 1;                      Point a;
a.y = 2;                      a.init(1, 2);
move(&a, 2, 2);               a.move(2, 2);
print(&a);                    a.print();
```

## Page 14

![Lecture 3 page 14](../page_images/03_3_Class/page_014.png)

Extracted text:

```text
Objects = Attributes + Services
•   Data: the properties or status

•   Operations: the functions



                           Data

                       Operations
```

## Page 15

![Lecture 3 page 15](../page_images/03_3_Class/page_015.png)

Extracted text:

```text
this: the hidden parameter
•   this is a hidden parameter for all member
    functions, with the type of the struct
    void Stash::initialize(int sz)
    ➔ (can be regarded as)
    void Stash::initialize(Stash*this, int
     sz)
•   To call the function, you must specify a variable
    Stash a;
    a.initialize(10);
    ➔ (can be regarded as)
    Stash::initialize(&a,10);
```

## Page 16

![Lecture 3 page 16](../page_images/03_3_Class/page_016.png)

Extracted text:

```text
this: the pointer to the variable
•   Inside member functions, you can use this as the
    pointer to the variable that calls the function.

•   this is a natural local variable of all structs member
    functions that you can not define, but can use it
    directly.
```

## Page 17

![Lecture 3 page 17](../page_images/03_3_Class/page_017.png)

Extracted text:

```text
Objects

•   In C++, an object is just a variable, and the purest
    definition is “a region of storage”.

•   The struct variables mentioned before are just
    objects in C++.
```

## Page 18

![Lecture 3 page 18](../page_images/03_3_Class/page_018.png)

Extracted text:

```text
Ticket Machine
• Ticket machines print a ticket
  when a customer inserts the
  correct money for their fare.
• Our ticket machines work by
  customers' inserting money into
  them, and then requesting a
  ticket to be printed. A machine
  keeps a running total of the
  amount of money it has collected
  throughout its operation.
```

## Page 19

![Lecture 3 page 19](../page_images/03_3_Class/page_019.png)

Extracted text:

```text
Procedure-Oriented
• Step to the machine
• Insert money into the
  machine
• The machine prints a
  ticket
• Take the ticket and leave
```

## Page 20

![Lecture 3 page 20](../page_images/03_3_Class/page_020.png)

Extracted text:

```text
Procedure-Oriented
• Step to the machine
• Insert money into the
    machine
•WeThe machine
    make       prints
         a program       a
                    simulate
theticket
     procedure of buying tickets.
•
It works. But  there is no such
   Take the ticket and leave
machine. There's nothing left
for the further development.
```

## Page 21

![Lecture 3 page 21](../page_images/03_3_Class/page_021.png)

Extracted text:

```text
Something is there
```

## Page 22

![Lecture 3 page 22](../page_images/03_3_Class/page_022.png)

Extracted text:

```text
Something is there
PRICE


balance


 total
```

## Page 23

![Lecture 3 page 23](../page_images/03_3_Class/page_023.png)

Extracted text:

```text
Something is there
PRICE
                         show prompt

balance                   print balance


                         insert money
 total
                         print ticket
```

## Page 24

![Lecture 3 page 24](../page_images/03_3_Class/page_024.png)

Extracted text:

```text
Something is there
   TicketMachine
  PRICE
  balance
  total
  showPrompt
  getMoney
  printTicket
  showBalance
  printError
```

## Page 25

![Lecture 3 page 25](../page_images/03_3_Class/page_025.png)

Extracted text:

```text
Something is there
 TicketMachine
PRICE                ticketMachine 1:
balance               TicketMachine

total
showPrompt        PRICE

getMoney          balance

printTicket       total
showBalance
printError
```

## Page 26

![Lecture 3 page 26](../page_images/03_3_Class/page_026.png)

Extracted text:

```text
Turn it into code
  TicketMachine
PRICE                         ticketMachine 1:
  a l aTicketMachine
b class  nce           {
                               TicketMachine

total
    private:
showPrompt
        const int PRICE;   price
        int balance;
getMoneyint total;
                           balance

printTicket
  };                       total
showBalance
printError
```

## Page 27

![Lecture 3 page 27](../page_images/03_3_Class/page_027.png)

Extracted text:

```text
Turn it into code
      class TicketMachine {
  TicketMachine
      public:
PRICE void showPrompt();
            c e getMoney();
b a l a nvoid
total      void    printTicket();
           void showBalance();
showPrompt
           void printError();
getMoney
      private:
printTicketconst int PRICE;
                  lance
s h o w Bintabalance;
                   or
p r i n t Eintr rtotal;
      };
```

## Page 28

![Lecture 3 page 28](../page_images/03_3_Class/page_028.png)

Extracted text:

```text
Objects = Attributes + Services
•   Data: the properties or status

•   Operations: the functions



                           Data

                       Operations
```

## Page 29

![Lecture 3 page 29](../page_images/03_3_Class/page_029.png)

Extracted text:

```text
Object vs. Class

                                              Class
•Objects (cat)
 •Represent things, events
 •Respond to messages at run-time   defines           instantiates
•Classes (cat class)                          Object
 •Define properties of instances
 •Act like types in C++
```

## Page 30

![Lecture 3 page 30](../page_images/03_3_Class/page_030.png)

Extracted text:

```text
OOP Characteristics
1. Everything is an object.
2. A program is a bunch of objects telling each
   other what to do by sending messages.
3. Each object has its own memory made up of
   other objects.
4. Every object has a type.
5. All objects of a particular type can receive
   the same messages.
```

## Page 31

![Lecture 3 page 31](../page_images/03_3_Class/page_031.png)

Extracted text:

```text
Definition of a Class

• In C++, separated .h and .cpp files are used to
  define one class.
• Class declaration and member function prototypes
  are in the header file (.h).
• All the bodies of these functions are in the source
  file (.cpp).
• PImpl technique: debatable, hides private
  members and removes compilation dependency.
```

## Page 32

![Lecture 3 page 32](../page_images/03_3_Class/page_032.png)

Extracted text:

```text
:: resolver
 •   <Class Name>::<function name>

 •   ::<function name>


void S::f() {
   ::f(); // Would be recursive otherwise!
   ::a++; // Select the global 'a'
   a--;   // The 'a' at class scope
}
```

## Page 33

![Lecture 3 page 33](../page_images/03_3_Class/page_033.png)

Extracted text:

```text
Compilation unit

• The compiler sees only one .cpp file, and
  generates one .obj file.
• The linker links all .obj files into one executable
  file.
• To provide information about functions in
  other .cpp files, use.h file.
```

## Page 34

![Lecture 3 page 34](../page_images/03_3_Class/page_034.png)

Extracted text:

```text
The header files

• If a function is declared in a header file, you
    must include the header file everywhere the
    function is used and where the function is
    defined.
•   If a class is declared in a header file, you must
    include the header file everywhere the class
    is used and where class member functions
    are defined.


                         54
```

## Page 35

![Lecture 3 page 35](../page_images/03_3_Class/page_035.png)

Extracted text:

```text
Header = interface

• The header is a contract between you and the
   user of your code.
• The compiler enforces the contract by
   requiring you to declare all structures and
   functions before they are used.
```

## Page 36

![Lecture 3 page 36](../page_images/03_3_Class/page_036.png)

Extracted text:

```text
Structure of C++ program
.h
```

## Page 37

![Lecture 3 page 37](../page_images/03_3_Class/page_037.png)

Extracted text:

```text
Structure of C++ program
declarations

     .h
```

## Page 38

![Lecture 3 page 38](../page_images/03_3_Class/page_038.png)

Extracted text:

```text
Structure of C++ program
declarations   definitions

     .h
                  .cpp
```

## Page 39

![Lecture 3 page 39](../page_images/03_3_Class/page_039.png)

Extracted text:

```text
Structure of C++ program
declarations   definitions
                #include
     .h
                  .cpp
```

## Page 40

![Lecture 3 page 40](../page_images/03_3_Class/page_040.png)

Extracted text:

```text
Structure of C++ program
declarations   definitions   after pre-compiler
                #include
     .h
                  .cpp
```

## Page 41

![Lecture 3 page 41](../page_images/03_3_Class/page_041.png)

Extracted text:

```text
Structure of C++ program
declarations          definitions          after pre-compiler
                        #include
     .h
                         .cpp




               .cpp


    Other modules that use the functions
```

## Page 42

![Lecture 3 page 42](../page_images/03_3_Class/page_042.png)

Extracted text:

```text
Structure of C++ program
declarations              definitions       after pre-compiler
                           #include
      .h
                             .cpp




               #include

                 .cpp


     Other modules that use the functions
```

## Page 43

![Lecture 3 page 43](../page_images/03_3_Class/page_043.png)

Extracted text:

```text
Declarations vs. Definitions

 •A .cpp file is a compile unit
 •Only declarations are allowed to be in .h
  •extern variables
  •function prototypes
  • class/struct  declaration
```

## Page 44

![Lecture 3 page 44](../page_images/03_3_Class/page_044.png)

Extracted text:

```text
#include
```

## Page 45

![Lecture 3 page 45](../page_images/03_3_Class/page_045.png)

Extracted text:

```text
#include
• #include is to insert the included file into the .cpp
   file at where the #include statement is.
  • #include "xx.h": usually search in the
      current directory, implementation defined
  • #include <xx.h>: search in the specified
      directories
```

## Page 46

![Lecture 3 page 46](../page_images/03_3_Class/page_046.png)

Extracted text:

```text
Standard header file structure

  #ifndef HEADER_FLAG
  #define HEADER_FLAG
  // Type declaration here...
  #endif // HEADER_FLAG
```

## Page 47

![Lecture 3 page 47](../page_images/03_3_Class/page_047.png)

Extracted text:

```text
Tips for header

1. One class declaration per header file
2. Same name with .cpp file.
3. The contents of a header file is surrounded with
   #ifndef #define … #endif
```

## Page 48

![Lecture 3 page 48](../page_images/03_3_Class/page_048.png)

Extracted text:

```text
The CMake utility
```
