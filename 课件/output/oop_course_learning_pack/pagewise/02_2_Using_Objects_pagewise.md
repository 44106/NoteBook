# Lecture 02: 2 Using Objects

- Source: `2 Using Objects.pdf`
- Pages: 87
- Rendered page images: 87
- Contact sheet: [open](../contact_sheets/02_2_Using_Objects_contact.jpg)
- Raw extracted text: [open](../raw_texts/02-2 Using Objects.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 2 page 1](../page_images/02_2_Using_Objects/page_001.png)

Extracted text:

```text
Using Objects
Object-Oriented Programming with C++
```

## Page 2

![Lecture 2 page 2](../page_images/02_2_Using_Objects/page_002.png)

Extracted text:

```text
Safe way to read a
     string in?
```

## Page 3

![Lecture 2 page 3](../page_images/02_2_Using_Objects/page_003.png)

Extracted text:

```text
std::string
```

## Page 4

![Lecture 2 page 4](../page_images/02_2_Using_Objects/page_004.png)

Extracted text:

```text
The string class
•   You must add this at the head of you code
    • #include <string>


•   Define variable of string like other types
    • string str;


•   Initialize it w/ string contant
    • string str = "Hello";


•   Read and write string w/ cin/cout
    • cin >> str;
    • cout << str;
```

## Page 5

![Lecture 2 page 5](../page_images/02_2_Using_Objects/page_005.png)

Extracted text:

```text
Assignment for string
char cstr1[20];
char cstr2[20] = "jaguar";


string str1;
string str2 = "panther";

cstr1 = cstr2; // illegal
str1 = str2;   // legal
```

## Page 6

![Lecture 2 page 6](../page_images/02_2_Using_Objects/page_006.png)

Extracted text:

```text
Concatenation for string

• string   str3;

• str3   = str1 + str2;

• str1   += str2;

• str1   += "lalala";
```

## Page 7

![Lecture 2 page 7](../page_images/02_2_Using_Objects/page_007.png)

Extracted text:

```text
Ctors

•   string (const char *cp, int len);

•   string (const string& s2, int pos);

•   string (const string& s2, int pos, int len);
```

## Page 8

![Lecture 2 page 8](../page_images/02_2_Using_Objects/page_008.png)

Extracted text:

```text
Sub-string


•   substr (int pos, int len);
```

## Page 9

![Lecture 2 page 9](../page_images/02_2_Using_Objects/page_009.png)

Extracted text:

```text
Alter string
•   assign (…);

•   insert (…);

•   insert (int pos, const string& s);

•   erase (…);

•   append (…);

•   replace (int pos, int len, const string& s);
```

## Page 10

![Lecture 2 page 10](../page_images/02_2_Using_Objects/page_010.png)

Extracted text:

```text
Search string


•   find (const string& s);
```

## Page 11

![Lecture 2 page 11](../page_images/02_2_Using_Objects/page_011.png)

Extracted text:

```text
File I/O
•   #include <ifstream>   // read from file
•   #include <ofstream>   // write to file



    ofstream File1("C:\\test.txt");
    File1 << "Hello world" << std::endl;


    ifstream File2("C:\\test.txt");
    std::string str;
    File2 >> str;
```

## Page 12

![Lecture 2 page 12](../page_images/02_2_Using_Objects/page_012.png)

Extracted text:

```text
• Assignment 001 on PTA
 • due in 2 weeks
```

## Page 13

![Lecture 2 page 13](../page_images/02_2_Using_Objects/page_013.png)

Extracted text:

```text
Memory Model
```

## Page 14

![Lecture 2 page 14](../page_images/02_2_Using_Objects/page_014.png)

Extracted text:

```text
What are they?
int i;              // global vars.

static int j;       // static global vars.

void f() {

    int k;          // local vars.

    static int l;   // static local vars.

    int *p = malloc(sizeof(int)); // allocated vars.

}
```

## Page 15

![Lecture 2 page 15](../page_images/02_2_Using_Objects/page_015.png)

Extracted text:

```text
Where are they?
Global data     stack        heap


Global vars.
Static global            dynamically
vars.           Local   allocated vars.
                vars.
Static local
vars.
```

## Page 16

![Lecture 2 page 16](../page_images/02_2_Using_Objects/page_016.png)

Extracted text:

```text
Global vars

•   vars defined outside any functions

•   can be shared btw .cpp files

•   extern
```

## Page 17

![Lecture 2 page 17](../page_images/02_2_Using_Objects/page_017.png)

Extracted text:

```text
Extern

•   extern is a declaration says there will be such a
    variable somewhere in the whole program

•   “such a” means the type and the name of the
    variable

•   global variable is a definition, the place for that
    variable
```

## Page 18

![Lecture 2 page 18](../page_images/02_2_Using_Objects/page_018.png)

Extracted text:

```text
Static


•   static global variable inhibits access from outside the
    .cpp file

•   so as the static function
```

## Page 19

![Lecture 2 page 19](../page_images/02_2_Using_Objects/page_019.png)

Extracted text:

```text
Static local vars


•   static local variable keeps value in between visits
    to the same function

•   is initialized at its first access
```

## Page 20

![Lecture 2 page 20](../page_images/02_2_Using_Objects/page_020.png)

Extracted text:

```text
Static


•   for global stuff: access restriction

•   for local stuff: persistence
```

## Page 21

![Lecture 2 page 21](../page_images/02_2_Using_Objects/page_021.png)

Extracted text:

```text
Pointers to Objects
```

## Page 22

![Lecture 2 page 22](../page_images/02_2_Using_Objects/page_022.png)

Extracted text:

```text
Pointers to Objects


•   string s = “hello”;

•   string* ps = &s;
```

## Page 23

![Lecture 2 page 23](../page_images/02_2_Using_Objects/page_023.png)

Extracted text:

```text
Operators with Pointers
•   &: get address

    •   ps = &s;

•   *: get the object

    •   (*ps).length()

•   ->: call the function

    •   ps->length()
```

## Page 24

![Lecture 2 page 24](../page_images/02_2_Using_Objects/page_024.png)

Extracted text:

```text
Two Ways to Access

•   string s;

    •   s is the object itself

•   string *ps;

    •   ps is a pointer to an object
```

## Page 25

![Lecture 2 page 25](../page_images/02_2_Using_Objects/page_025.png)

Extracted text:

```text
•   string s;

    •   At this line, object s is created and initialized

•   string *ps;

    •   At this line, the object ps points to is not known
        yet.
```

## Page 26

![Lecture 2 page 26](../page_images/02_2_Using_Objects/page_026.png)

Extracted text:

```text
Assignment

•   string s1, s2;

    •   s1 = s2;

•   string *ps1, *ps2;

    •   ps1 = ps2;
```

## Page 27

![Lecture 2 page 27](../page_images/02_2_Using_Objects/page_027.png)

Extracted text:

```text
Dynamically Allocated
     Memory
```

## Page 28

![Lecture 2 page 28](../page_images/02_2_Using_Objects/page_028.png)

Extracted text:

```text
Dynamic memory allocation
• new

  •   new int;

  •   new Stash;

  •   new int[10]

• delete

  •   delete p;

  •   delete[] p;
```

## Page 29

![Lecture 2 page 29](../page_images/02_2_Using_Objects/page_029.png)

Extracted text:

```text
new and delete
•   new is the way to allocate memory as a program
    runs. Pointers become the only access to that
    memory.

•   delete enables you to return memory to the
    memory pool when you are finished with it.
```

## Page 30

![Lecture 2 page 30](../page_images/02_2_Using_Objects/page_030.png)

Extracted text:

```text
Dynamic arrays
int *psome = new int[10];

•   The new operator returns the address of the first element of
    the block.

delete[] psome;

•   The presence of the brackets tells the program that it
    should free the whole array, not just the element
```

## Page 31

![Lecture 2 page 31](../page_images/02_2_Using_Objects/page_031.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];




Student *q=new Student();

Student *r=new Student[10];
```

## Page 32

![Lecture 2 page 32](../page_images/02_2_Using_Objects/page_032.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];




Student *q=new Student();

Student *r=new Student[10];
```

## Page 33

![Lecture 2 page 33](../page_images/02_2_Using_Objects/page_033.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];




Student *q=new Student();

Student *r=new Student[10];
```

## Page 34

![Lecture 2 page 34](../page_images/02_2_Using_Objects/page_034.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                       4
int *a=new int[10];




Student *q=new Student();

Student *r=new Student[10];
```

## Page 35

![Lecture 2 page 35](../page_images/02_2_Using_Objects/page_035.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                       4
int *a=new int[10];




Student *q=new Student();

Student *r=new Student[10];
```

## Page 36

![Lecture 2 page 36](../page_images/02_2_Using_Objects/page_036.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                      4
int *a=new int[10];
                      40




Student *q=new Student();

Student *r=new Student[10];
```

## Page 37

![Lecture 2 page 37](../page_images/02_2_Using_Objects/page_037.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                      4
int *a=new int[10];
                      40

                      16




Student *q=new Student();

Student *r=new Student[10];
```

## Page 38

![Lecture 2 page 38](../page_images/02_2_Using_Objects/page_038.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                      4
int *a=new int[10];
                      40

                      16

                      160


Student *q=new Student();

Student *r=new Student[10];
```

## Page 39

![Lecture 2 page 39](../page_images/02_2_Using_Objects/page_039.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                              4
int *a=new int[10];
                              40
Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 40

![Lecture 2 page 40](../page_images/02_2_Using_Objects/page_040.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;
                              4
int *a=new int[10];
                              40
Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 41

![Lecture 2 page 41](../page_images/02_2_Using_Objects/page_041.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];
                              40
Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 42

![Lecture 2 page 42](../page_images/02_2_Using_Objects/page_042.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];
                              40
Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 43

![Lecture 2 page 43](../page_images/02_2_Using_Objects/page_043.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 44

![Lecture 2 page 44](../page_images/02_2_Using_Objects/page_044.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 45

![Lecture 2 page 45](../page_images/02_2_Using_Objects/page_045.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];
                              16

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 46

![Lecture 2 page 46](../page_images/02_2_Using_Objects/page_046.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 47

![Lecture 2 page 47](../page_images/02_2_Using_Objects/page_047.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 48

![Lecture 2 page 48](../page_images/02_2_Using_Objects/page_048.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 49

![Lecture 2 page 49](../page_images/02_2_Using_Objects/page_049.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;

delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 50

![Lecture 2 page 50](../page_images/02_2_Using_Objects/page_050.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 51

![Lecture 2 page 51](../page_images/02_2_Using_Objects/page_051.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 52

![Lecture 2 page 52](../page_images/02_2_Using_Objects/page_052.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 53

![Lecture 2 page 53](../page_images/02_2_Using_Objects/page_053.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 54

![Lecture 2 page 54](../page_images/02_2_Using_Objects/page_054.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 55

![Lecture 2 page 55](../page_images/02_2_Using_Objects/page_055.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;
                              160
delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 56

![Lecture 2 page 56](../page_images/02_2_Using_Objects/page_056.png)

Extracted text:

```text
The new-delete mech.
int *p=new int;

int *a=new int[10];


Student *q=new Student();

Student *r=new Student[10];

delete p;

delete[] a;

delete q;

delete r;

delete[] r;
```

## Page 57

![Lecture 2 page 57](../page_images/02_2_Using_Objects/page_057.png)

Extracted text:

```text
Tips for new and delete
•   Don't use delete to free memory that new didn't allocate.

•   Don't use delete to free the same block of memory twice in
    succession.

•   Use delete [] if you used new [] to allocate anarray.

•   Use delete (no brackets) if you used new to allocate a
    single entity.

•   It's safe to apply delete to the null pointer (nothing
    happens).
```

## Page 58

![Lecture 2 page 58](../page_images/02_2_Using_Objects/page_058.png)

Extracted text:

```text
Reference
```

## Page 59

![Lecture 2 page 59](../page_images/02_2_Using_Objects/page_059.png)

Extracted text:

```text
Defining references
```

## Page 60

![Lecture 2 page 60](../page_images/02_2_Using_Objects/page_060.png)

Extracted text:

```text
Defining references
•   References are a new data type in C++
    –   char c;          // a character

    –   char* p = &c; // a pointer to a character

    –   char& r = c;     // a reference to a character

•   Local or global variables
    – type&    refname = name;
    – For ordinary variables, the initial value is required


•   In parameter lists and member variables
    – type& refname
    –   Binding defined by caller or constructor
```

## Page 61

![Lecture 2 page 61](../page_images/02_2_Using_Objects/page_061.png)

Extracted text:

```text
References
•   Declares a new name for an existing object
    int    X = 47;
    int& Y = X; // Y is a reference to X



    // X and Y now refer to the same variable

    cout << "Y = " << Y;        // prints Y = 47

    Y = 18;

    cout << "X = " << X;        // prints X = 18
```

## Page 62

![Lecture 2 page 62](../page_images/02_2_Using_Objects/page_062.png)

Extracted text:

```text
Rules of references
•   References must be initialized when defined
•   Initialization establishes a binding
    •
        In definition
         int x = 3;
         int& y = x;
         const int& z = x;

    •
        As a function argument
         void f ( int& x );
         f(y); // initialized when function is called
```

## Page 63

![Lecture 2 page 63](../page_images/02_2_Using_Objects/page_063.png)

Extracted text:

```text
Rules of references
```

## Page 64

![Lecture 2 page 64](../page_images/02_2_Using_Objects/page_064.png)

Extracted text:

```text
Rules of references
•   Bindings don’t change at run time, unlike pointers
```

## Page 65

![Lecture 2 page 65](../page_images/02_2_Using_Objects/page_065.png)

Extracted text:

```text
Rules of references
•   Bindings don’t change at run time, unlike pointers
•   Assignment changes the object referred-to
    int& y = x;

    y = 12; // Changes value of x

•   The target of a reference must have a location!
      void func(int &);

      func (i * 3);     // Warning or error!
```

## Page 66

![Lecture 2 page 66](../page_images/02_2_Using_Objects/page_066.png)

Extracted text:

```text
Pointers vs. References
• References                      • Pointers
  – can't be null                   – can be set to null
  – can't change to a new           – can change to point to a
    "address" location                different address
  – are dependent on an             – pointer is independent of
    existing variable, they are       existing objects
    an alias for an variable
```

## Page 67

![Lecture 2 page 67](../page_images/02_2_Using_Objects/page_067.png)

Extracted text:

```text
Restrictions
```

## Page 68

![Lecture 2 page 68](../page_images/02_2_Using_Objects/page_068.png)

Extracted text:

```text
Restrictions
• No references to references
```

## Page 69

![Lecture 2 page 69](../page_images/02_2_Using_Objects/page_069.png)

Extracted text:

```text
Restrictions
•   No references to references

•   No pointers to references

    int&* p;                  // illegal

    – Reference to pointer is ok

      void f(int*& p);

•   No arrays of references
```

## Page 70

![Lecture 2 page 70](../page_images/02_2_Using_Objects/page_070.png)

Extracted text:

```text
const
```

## Page 71

![Lecture 2 page 71](../page_images/02_2_Using_Objects/page_071.png)

Extracted text:

```text
const
• declares a variable to have a constant value
  const int x = 123;
  x = 27; // illegal!
  x++; // illegal!

  int y = x; // Ok, copy const to non-const

  y = x;         // Ok, same thing

  const int z = y; // ok, const is safer
```

## Page 72

![Lecture 2 page 72](../page_images/02_2_Using_Objects/page_072.png)

Extracted text:

```text
Constants
```

## Page 73

![Lecture 2 page 73](../page_images/02_2_Using_Objects/page_073.png)

Extracted text:

```text
Constants
• Constants are like variables

  – Observe scoping rules

  – Declared with “const” type modifier
```

## Page 74

![Lecture 2 page 74](../page_images/02_2_Using_Objects/page_074.png)

Extracted text:

```text
Constants
• Constants are like variables

  – Observe scoping rules

  – Declared with “const” type modifier

• A const in C++ defaults to internal linkage

  – the compiler tries to avoid creating storage for a const
    -- holds the value in its symbol table.

  – extern forces storage to be allocated.
```

## Page 75

![Lecture 2 page 75](../page_images/02_2_Using_Objects/page_075.png)

Extracted text:

```text
Compile time constants
    const int bufsize = 1024;

    •   Value must be initialized

    •   Unless you make an explicit extern declaration:

    extern const int bufsize = 1024;

    •   Compiler won't let you change it

•   Compile time constants are entries in compiler symbol
    table, not really variables.
```

## Page 76

![Lecture 2 page 76](../page_images/02_2_Using_Objects/page_076.png)

Extracted text:

```text
Run-time constants
•   const value can be exploited
    const int class_size = 12;
    int finalGrade[class_size]; // ok

    int x;
    cin >> x;
    const int size = x;
    double classAverage[size]; // error!
```

## Page 77

![Lecture 2 page 77](../page_images/02_2_Using_Objects/page_077.png)

Extracted text:

```text
Run-time constants
•   const value can be exploited
    const int class_size = 12;
    int finalGrade[class_size]; // ok

    int x;
    cin >> x;
    const int size = x;
    double classAverage[size]; // error! ok
```

## Page 78

![Lecture 2 page 78](../page_images/02_2_Using_Objects/page_078.png)

Extracted text:

```text
Pointers and const
  aPointer -- may be const
0xaffefado
                             aValue -- may be const
                                54
```

## Page 79

![Lecture 2 page 79](../page_images/02_2_Using_Objects/page_079.png)

Extracted text:

```text
Pointers and const
   aPointer -- may be const
 0xaffefado
                                 aValue -- may be const
                                    54
char s[] = "abc";

• char * const q = s; // q is const
   *q = 'c';    // OK
   q++;         // ERROR

• const char *p = s;          // (*p) is const
   *p = 'b';    // ERROR!
```

## Page 80

![Lecture 2 page 80](../page_images/02_2_Using_Objects/page_080.png)

Extracted text:

```text
Quiz: What are these?


string s( "Fred" );
const string* p = &s;
string const* p = &s;
string *const p = &s;
```

## Page 81

![Lecture 2 page 81](../page_images/02_2_Using_Objects/page_081.png)

Extracted text:

```text
Pointers and constants
                    int i;      const int ci = 3;




Remember:
*ip = 54;    // always legal since ip points to int
*cip = 54;   // never legal since cip points to const int
```

## Page 82

![Lecture 2 page 82](../page_images/02_2_Using_Objects/page_082.png)

Extracted text:

```text
String Literals
        char* s = "Hello, world!";

    •    s is a pointer initialized to point to a string constant

    •    This is actually a const char* s but compiler
         accepts it without the const

    •    Don't try to change the character values
         (undefined behavior)

•   If you want to change the string, put it in an array:

        char s[] = "Hello, world!";
```

## Page 83

![Lecture 2 page 83](../page_images/02_2_Using_Objects/page_083.png)

Extracted text:

```text
Conversions
```

## Page 84

![Lecture 2 page 84](../page_images/02_2_Using_Objects/page_084.png)

Extracted text:

```text
Conversions
•
    Can always treat a non-const value as const
    void f(const int* x);

    int a = 15;

    f(&a); // ok

    const int b = a;


    f(&b); // ok

    b = a + 1; // Error!


You cannot treat a constant object as non-constant without an
  explicit cast (const_cast)
```

## Page 85

![Lecture 2 page 85](../page_images/02_2_Using_Objects/page_085.png)

Extracted text:

```text
Passing by const value?


void f1(const int i) {

    i++; // Illegal -- compile-time error

}
```

## Page 86

![Lecture 2 page 86](../page_images/02_2_Using_Objects/page_086.png)

Extracted text:

```text
Returning by const value?
int f3() { return 1; }

const int f4() { return 1; }

int main() {

    const int j = f3(); // Works fine

    int k = f4(); // But this works fine too!

}
```

## Page 87

![Lecture 2 page 87](../page_images/02_2_Using_Objects/page_087.png)

Extracted text:

```text
Passing addresses
•   Passing a whole object may cost you a lot. It is better to
    pass a large object by a pointer. But it’s possible for the
    programmer to take it and modify the original value.

•   In fact, whenever you’re passing an address into a
    function, you should make it a const if at all possible.
```
