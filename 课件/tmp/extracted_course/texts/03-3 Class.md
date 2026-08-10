# Lecture 3: 3 Class

Source: `3 Class.pdf`
Pages: 48

## Page 1

            Class
Object-Oriented Programming with C++

## Page 2

            p'




𝑦       p




    𝑥

## Page 3

                  Point
typedef struct point {
    int x;
    int y;
} Point;

## Page 4

                   Point
typedef struct point {
    int x;
    int y;
} Point;

Point a;
a.x = 1;a.y = 2;

## Page 5

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

## Page 6

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

## Page 7

move (dx, dy)?

## Page 8

      move (dx, dy)?


void move(Point* p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}

## Page 9

           Prototypes

typedef struct point {
    int x;
    int y;
} Point;

void print(const Point* p);
void move(Point* p, int dx, int dy);

## Page 10

             Usage

Point a;
Point b;
a.x = b.x = 1; a.y = b.y = 1;
move(&a,2,2);
print(&a);
print(&b);

## Page 11

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

## Page 12

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

## Page 13

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

## Page 14

Objects = Attributes + Services
•   Data: the properties or status

•   Operations: the functions



                           Data

                       Operations

## Page 15

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

## Page 16

this: the pointer to the variable
•   Inside member functions, you can use this as the
    pointer to the variable that calls the function.

•   this is a natural local variable of all structs member
    functions that you can not define, but can use it
    directly.

## Page 17

                       Objects

•   In C++, an object is just a variable, and the purest
    definition is “a region of storage”.

•   The struct variables mentioned before are just
    objects in C++.

## Page 18

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

## Page 19

           Procedure-Oriented
• Step to the machine
• Insert money into the
  machine
• The machine prints a
  ticket
• Take the ticket and leave

## Page 20

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

## Page 21

Something is there

## Page 22

         Something is there
PRICE


balance


 total

## Page 23

         Something is there
PRICE
                         show prompt

balance                   print balance


                         insert money
 total
                         print ticket

## Page 24

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

## Page 25

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

## Page 26

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

## Page 27

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

## Page 28

Objects = Attributes + Services
•   Data: the properties or status

•   Operations: the functions



                           Data

                       Operations

## Page 29

              Object vs. Class

                                              Class
•Objects (cat)
 •Represent things, events
 •Respond to messages at run-time   defines           instantiates
•Classes (cat class)                          Object
 •Define properties of instances
 •Act like types in C++

## Page 30

      OOP Characteristics
1. Everything is an object.
2. A program is a bunch of objects telling each
   other what to do by sending messages.
3. Each object has its own memory made up of
   other objects.
4. Every object has a type.
5. All objects of a particular type can receive
   the same messages.

## Page 31

       Definition of a Class

• In C++, separated .h and .cpp files are used to
  define one class.
• Class declaration and member function prototypes
  are in the header file (.h).
• All the bodies of these functions are in the source
  file (.cpp).
• PImpl technique: debatable, hides private
  members and removes compilation dependency.

## Page 32

                  :: resolver
 •   <Class Name>::<function name>

 •   ::<function name>


void S::f() {
   ::f(); // Would be recursive otherwise!
   ::a++; // Select the global 'a'
   a--;   // The 'a' at class scope
}

## Page 33

          Compilation unit

• The compiler sees only one .cpp file, and
  generates one .obj file.
• The linker links all .obj files into one executable
  file.
• To provide information about functions in
  other .cpp files, use.h file.

## Page 34

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

## Page 35

    Header = interface

• The header is a contract between you and the
   user of your code.
• The compiler enforces the contract by
   requiring you to declare all structures and
   functions before they are used.

## Page 36

Structure of C++ program
.h

## Page 37

   Structure of C++ program
declarations

     .h

## Page 38

   Structure of C++ program
declarations   definitions

     .h
                  .cpp

## Page 39

   Structure of C++ program
declarations   definitions
                #include
     .h
                  .cpp

## Page 40

   Structure of C++ program
declarations   definitions   after pre-compiler
                #include
     .h
                  .cpp

## Page 41

   Structure of C++ program
declarations          definitions          after pre-compiler
                        #include
     .h
                         .cpp




               .cpp


    Other modules that use the functions

## Page 42

    Structure of C++ program
declarations              definitions       after pre-compiler
                           #include
      .h
                             .cpp




               #include

                 .cpp


     Other modules that use the functions

## Page 43

Declarations vs. Definitions

 •A .cpp file is a compile unit
 •Only declarations are allowed to be in .h
  •extern variables
  •function prototypes
  • class/struct  declaration

## Page 44

#include

## Page 45

                   #include
• #include is to insert the included file into the .cpp
   file at where the #include statement is.
  • #include "xx.h": usually search in the
      current directory, implementation defined
  • #include <xx.h>: search in the specified
      directories

## Page 46

Standard header file structure

  #ifndef HEADER_FLAG
  #define HEADER_FLAG
  // Type declaration here...
  #endif // HEADER_FLAG

## Page 47

           Tips for header

1. One class declaration per header file
2. Same name with .cpp file.
3. The contents of a header file is surrounded with
   #ifndef #define … #endif

## Page 48

The CMake utility
