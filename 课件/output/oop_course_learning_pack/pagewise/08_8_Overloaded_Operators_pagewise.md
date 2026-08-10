# Lecture 08: 8 Overloaded Operators

- Source: `8 Overloaded Operators.pdf`
- Pages: 73
- Rendered page images: 73
- Contact sheet: [open](../contact_sheets/08_8_Overloaded_Operators_contact.jpg)
- Raw extracted text: [open](../raw_texts/08-8 Overloaded Operators.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 8 page 1](../page_images/08_8_Overloaded_Operators/page_001.png)

Extracted text:

```text
Overloaded operators
   Object-Oriented Programming with C++
```

## Page 2

![Lecture 8 page 2](../page_images/08_8_Overloaded_Operators/page_002.png)

Extracted text:

```text
Overloading operators
• Allows user-defined types to act like built-in
  types
• Another way to make a function call.
```

## Page 3

![Lecture 8 page 3](../page_images/08_8_Overloaded_Operators/page_003.png)

Extracted text:

```text
Overloaded operators
Unary and binary operators can be overloaded:
     + - * / % ^ & | ~
     = < > += -= *= /= %=
     ^= &= |= << >> >>= <<= ==
     != <= >= ! && ||          ++ --
     , ->* -> () []
    operator new      operator delete
    operator new[] operator delete[]
```

## Page 4

![Lecture 8 page 4](../page_images/08_8_Overloaded_Operators/page_004.png)

Extracted text:

```text
Operators you can't overload
.        .*      ::      ?:
sizeof typeid
static_cast dynamic_cast const_cast
reinterpret_cast
```

## Page 5

![Lecture 8 page 5](../page_images/08_8_Overloaded_Operators/page_005.png)

Extracted text:

```text
[No extractable text]
```

## Page 6

![Lecture 8 page 6](../page_images/08_8_Overloaded_Operators/page_006.png)

Extracted text:

```text
Restrictions
• Only existing operators can be overloaded (you
  can't create a ** operator for exponentiation)
• Overloaded operators must
 –Preserve number of operands
 –Preserve precedence
```

## Page 7

![Lecture 8 page 7](../page_images/08_8_Overloaded_Operators/page_007.png)

Extracted text:

```text
C++ overloaded operator
• Just a function with an operator name!
 –Use the operator keyword as a prefix to name
  operator *(…)
```

## Page 8

![Lecture 8 page 8](../page_images/08_8_Overloaded_Operators/page_008.png)

Extracted text:

```text
C++ overloaded operator
• Just a function with an operator name!
 –Use the operator keyword as a prefix to name
  operator *(…)
• Can be a member function
 –Implicit first argument
  String String::operator+(const String& that);
```

## Page 9

![Lecture 8 page 9](../page_images/08_8_Overloaded_Operators/page_009.png)

Extracted text:

```text
C++ overloaded operator
• Just a function with an operator name!
  –Use the operator keyword as a prefix to name
   operator *(…)
• Can be a member function
  –Implicit first argument
   String String::operator+(const String& that);

• Can be a global (free) function
  –Both arguments explicit
   String operator+(const String& l, const String& r);
```

## Page 10

![Lecture 8 page 10](../page_images/08_8_Overloaded_Operators/page_010.png)

Extracted text:

```text
How to overload
• As member function
 –Implicit first argument
 –No type conversion performed on receiver
```

## Page 11

![Lecture 8 page 11](../page_images/08_8_Overloaded_Operators/page_011.png)

Extracted text:

```text
Operators as member functions
 class Integer
 {
  public:
   Integer( int n = 0 ) : i(n) {}
   Integer operator+(const Integer& n) const {
       return Integer(i + n.i);
   }
   ...
  private:
   int i;
 };
```

## Page 12

![Lecture 8 page 12](../page_images/08_8_Overloaded_Operators/page_012.png)

Extracted text:

```text
Member functions
Integer x(1), y(5), z;
x + y; ====> x.operator+(y);
• Implicit first argument
• Developer must have access to class definition
• Members have full access to all data in class
• No type conversion performed on receiver
    z = x + y;
    z = x + 3;
    z = 3 + y;
```

## Page 13

![Lecture 8 page 13](../page_images/08_8_Overloaded_Operators/page_013.png)

Extracted text:

```text
Member functions
Integer x(1), y(5), z;
x + y; ====> x.operator+(y);
• Implicit first argument
• Developer must have access to class definition
• Members have full access to all data in class
• No type conversion performed on receiver
    z = x + y; √
    z = x + 3;
    z = 3 + y;
```

## Page 14

![Lecture 8 page 14](../page_images/08_8_Overloaded_Operators/page_014.png)

Extracted text:

```text
Member functions
Integer x(1), y(5), z;
x + y; ====> x.operator+(y);
• Implicit first argument
• Developer must have access to class definition
• Members have full access to all data in class
• No type conversion performed on receiver
    z = x + y; √
    z = x + 3; √
    z = 3 + y;
```

## Page 15

![Lecture 8 page 15](../page_images/08_8_Overloaded_Operators/page_015.png)

Extracted text:

```text
Member functions
Integer x(1), y(5), z;
x + y; ====> x.operator+(y);
• Implicit first argument
• Developer must have access to class definition
• Members have full access to all data in class
• No type conversion performed on receiver
    z = x + y; √
    z = x + 3; √
    z = 3 + y;
```

## Page 16

![Lecture 8 page 16](../page_images/08_8_Overloaded_Operators/page_016.png)

Extracted text:

```text
Member functions…
• For binary operators (+, -, *, etc) member
  functions require one argument.
• For unary operators (unary -, !, etc) member
  functions require no arguments:
  Integer operator-() const {
    return Integer(-i);
  }
  ...
  z = -x;
```

## Page 17

![Lecture 8 page 17](../page_images/08_8_Overloaded_Operators/page_017.png)

Extracted text:

```text
Member functions…
• For binary operators (+, -, *, etc) member
  functions require one argument.
• For unary operators (unary -, !, etc) member
  functions require no arguments:
  Integer operator-() const {
    return Integer(-i);
  }
  ...
  z = -x; // ???
```

## Page 18

![Lecture 8 page 18](../page_images/08_8_Overloaded_Operators/page_018.png)

Extracted text:

```text
Member functions…
• For binary operators (+, -, *, etc) member
  functions require one argument.
• For unary operators (unary -, !, etc) member
  functions require no arguments:
  Integer operator-() const {
    return Integer(-i);
  }
  ...
  z = -x; // z.operator=(x.operator-());
```

## Page 19

![Lecture 8 page 19](../page_images/08_8_Overloaded_Operators/page_019.png)

Extracted text:

```text
How to overload
• As a global function
  –Explicit first argument
  –Type conversions performed on both arguments
  –Can be made a friend
```

## Page 20

![Lecture 8 page 20](../page_images/08_8_Overloaded_Operators/page_020.png)

Extracted text:

```text
Operator as a global function
Integer operator+(
    const Integer& lhs,
    const Integer& rhs);
Integer x, y;
x + y     ====> operator+(x, y);

• Explicit first argument
• Developer does not need special access to classes
• May need to be a friend
• Type conversions performed on both arguments
```

## Page 21

![Lecture 8 page 21](../page_images/08_8_Overloaded_Operators/page_021.png)

Extracted text:

```text
Global operators (friend)
class Integer
{
  public:
   friend Integer operator+(const Integer&,
                            const Integer&);
   ...
  private:
   int i;
};

Integer operator+(const Integer& lhs, const Integer& rhs)
{
  return Integer( lhs.i + rhs.i );
}
```

## Page 22

![Lecture 8 page 22](../page_images/08_8_Overloaded_Operators/page_022.png)

Extracted text:

```text
Global operators
• Binary operators require two arguments
• Unary operators require one argument
• Conversion:
  z = x +   y;
  z = x +   3;
  z = 3 +   y;
  z = 3 +   7;
• If you don't have access to private data members,
  then the global function must use the public
  interface (e.g. accessors)
```

## Page 23

![Lecture 8 page 23](../page_images/08_8_Overloaded_Operators/page_023.png)

Extracted text:

```text
Global operators
• Binary operators require two arguments
• Unary operators require one argument
• Conversion:
  z = x +   y; // operator+(x, y)
  z = x +   3;
  z = 3 +   y;
  z = 3 +   7;
• If you don't have access to private data members,
  then the global function must use the public
  interface (e.g. accessors)
```

## Page 24

![Lecture 8 page 24](../page_images/08_8_Overloaded_Operators/page_024.png)

Extracted text:

```text
Global operators
• Binary operators require two arguments
• Unary operators require one argument
• Conversion:
  z = x +   y; // operator+(x, y)
  z = x +   3; // operator+(x, Integer(3))
  z = 3 +   y;
  z = 3 +   7;
• If you don't have access to private data members,
  then the global function must use the public
  interface (e.g. accessors)
```

## Page 25

![Lecture 8 page 25](../page_images/08_8_Overloaded_Operators/page_025.png)

Extracted text:

```text
Global operators
• Binary operators require two arguments
• Unary operators require one argument
• Conversion:
  z = x +   y; // operator+(x, y)
  z = x +   3; // operator+(x, Integer(3))
  z = 3 +   y; // operator+(Integer(3), y)
  z = 3 +   7;
• If you don't have access to private data members,
  then the global function must use the public
  interface (e.g. accessors)
```

## Page 26

![Lecture 8 page 26](../page_images/08_8_Overloaded_Operators/page_026.png)

Extracted text:

```text
Global operators
• Binary operators require two arguments
• Unary operators require one argument
• Conversion:
  z = x +   y;   // operator+(x, y)
  z = x +   3;   // operator+(x, Integer(3))
  z = 3 +   y;   // operator+(Integer(3), y)
  z = 3 +   7;   // Integer(10)
• If you don't have access to private data members,
  then the global function must use the public
  interface (e.g. accessors)
```

## Page 27

![Lecture 8 page 27](../page_images/08_8_Overloaded_Operators/page_027.png)

Extracted text:

```text
Tips: Members vs. Free functions
• Unary operators should be members
• = () [] -> ->* must be members
• All other binary operators as non-members
```

## Page 28

![Lecture 8 page 28](../page_images/08_8_Overloaded_Operators/page_028.png)

Extracted text:

```text
Argument passing
• If it is read-only pass it in as a const reference
  (except built-ins)
• Make member functions const that don't change
  the class (boolean operators, +, -, etc)
• For global functions, if the left-hand side changes
  pass as a reference (stream inserters)
```

## Page 29

![Lecture 8 page 29](../page_images/08_8_Overloaded_Operators/page_029.png)

Extracted text:

```text
Return values
• Select the return type depending on the expected
  meaning of the operator. For example,
 – For operator+ you need to generate a new object.
 Return the created object.
 – Logical operators should return bool (or int for older
 compilers).
```

## Page 30

![Lecture 8 page 30](../page_images/08_8_Overloaded_Operators/page_030.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
```

## Page 31

![Lecture 8 page 31](../page_images/08_8_Overloaded_Operators/page_031.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
 – T operator X(const T& l, const T& r);
```

## Page 32

![Lecture 8 page 32](../page_images/08_8_Overloaded_Operators/page_032.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
 – T operator X(const T& l, const T& r);
• ! && || <      <= == >= >
```

## Page 33

![Lecture 8 page 33](../page_images/08_8_Overloaded_Operators/page_033.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
 – T operator X(const T& l, const T& r);
• ! && || <      <= == >= >
 – bool operator X(const T& l, const T& r);
```

## Page 34

![Lecture 8 page 34](../page_images/08_8_Overloaded_Operators/page_034.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
  – T operator X(const T& l, const T& r);
• ! && || <       <= == >= >
  – bool operator X(const T& l, const T& r);
• []
```

## Page 35

![Lecture 8 page 35](../page_images/08_8_Overloaded_Operators/page_035.png)

Extracted text:

```text
The prototypes of operators
• +-*/%^&|~
  – T operator X(const T& l, const T& r);
• ! && || <        <= == >= >
  – bool operator X(const T& l, const T& r);
• []
  – E& T::operator [](int index);
```

## Page 36

![Lecture 8 page 36](../page_images/08_8_Overloaded_Operators/page_036.png)

Extracted text:

```text
Operators ++ and --
• How to distinguish postfix from prefix?
  •i++ or ++i
```

## Page 37

![Lecture 8 page 37](../page_images/08_8_Overloaded_Operators/page_037.png)

Extracted text:

```text
Operators ++ and --
• How to distinguish postfix from prefix?
  •i++ or ++i
• Postfix forms take an int argument -- compiler will
  pass in 0 as that int
 class Integer {
 public:
     ...
     Integer& operator++();   //prefix++
     Integer operator++(int); //postfix++
     Integer& operator--();   //prefix--
     Integer operator--(int); //postfix--
     ...
 };
```

## Page 38

![Lecture 8 page 38](../page_images/08_8_Overloaded_Operators/page_038.png)

Extracted text:

```text
Operators ++ and --
Integer& Integer::operator++() {
    this->i += 1;      // increment
    return *this;      // fetch
}
// int argument not used so leave unnamed so
// won't get compiler warnings
Integer Integer::operator++( int ){
    Integer old( *this );   // fetch
    ++(*this);              // increment
    return old;             // return
}
```

## Page 39

![Lecture 8 page 39](../page_images/08_8_Overloaded_Operators/page_039.png)

Extracted text:

```text
Operators ++ and --
Integer& Integer::operator++() {
    this->i += 1;      // increment
    return *this;      // fetch
}
// int argument not used so leave unnamed so
// won't get compiler warnings
Integer Integer::operator++( int ){
    Integer old( *this );   // fetch
    ++(*this);              // increment
    return old;             // return
}
```

## Page 40

![Lecture 8 page 40](../page_images/08_8_Overloaded_Operators/page_040.png)

Extracted text:

```text
Operators ++ and --
Integer& Integer::operator++() {
    *this += 1;        // increment
    return *this;      // fetch
}
// int argument not used so leave unnamed so
// won't get compiler warnings
Integer Integer::operator++( int ){
    Integer old( *this );   // fetch
    ++(*this);              // increment
    return old;             // return
}
```

## Page 41

![Lecture 8 page 41](../page_images/08_8_Overloaded_Operators/page_041.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
```

## Page 42

![Lecture 8 page 42](../page_images/08_8_Overloaded_Operators/page_042.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
```

## Page 43

![Lecture 8 page 43](../page_images/08_8_Overloaded_Operators/page_043.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
```

## Page 44

![Lecture 8 page 44](../page_images/08_8_Overloaded_Operators/page_044.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
```

## Page 45

![Lecture 8 page 45](../page_images/08_8_Overloaded_Operators/page_045.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
      // calls x.operator++(0);
```

## Page 46

![Lecture 8 page 46](../page_images/08_8_Overloaded_Operators/page_046.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
      // calls x.operator++(0);
   --x;
```

## Page 47

![Lecture 8 page 47](../page_images/08_8_Overloaded_Operators/page_047.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
      // calls x.operator++(0);
   --x;
      // calls x.operator--();
```

## Page 48

![Lecture 8 page 48](../page_images/08_8_Overloaded_Operators/page_048.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
      // calls x.operator++(0);
   --x;
      // calls x.operator--();
   x--;
```

## Page 49

![Lecture 8 page 49](../page_images/08_8_Overloaded_Operators/page_049.png)

Extracted text:

```text
Using the overloaded ++ and --
// decrement operators similar to increment

   Integer x(5);
   ++x;
      // calls x.operator++();
   x++;
      // calls x.operator++(0);
   --x;
      // calls x.operator--();
   x--;
      // calls x.operator--(0);
```

## Page 50

![Lecture 8 page 50](../page_images/08_8_Overloaded_Operators/page_050.png)

Extracted text:

```text
Using the overloaded ++ and --
 // decrement operators similar to increment

    Integer x(5);
    ++x;
       // calls x.operator++();
    x++;
       // calls x.operator++(0);
    --x;
       // calls x.operator--();
    x--;
       // calls x.operator--(0);


• User-defined prefix is more efficient than postfix.
```

## Page 51

![Lecture 8 page 51](../page_images/08_8_Overloaded_Operators/page_051.png)

Extracted text:

```text
Relational operators
• implement != in terms of ==
• implement >, >=, <= in terms of <
class Integer {
public:
    ...
    bool operator==( const Integer& rhs ) const;
    bool operator!=( const Integer& rhs ) const;

    bool operator<( const Integer& rhs ) const;
    bool operator>( const Integer& rhs ) const;
    bool operator<=( const Integer& rhs ) const;
    bool operator>=( const Integer& rhs ) const;
}
```

## Page 52

![Lecture 8 page 52](../page_images/08_8_Overloaded_Operators/page_052.png)

Extracted text:

```text
Relational operators
bool Integer::operator==( const Integer& rhs ) const {
    return i == rhs.i;
}
// implement lhs != rhs in terms of !(lhs == rhs)
bool Integer::operator!=( const Integer& rhs ) const {
    return !(*this == rhs);
}


bool Integer::operator<( const Integer& rhs ) const {
    return i < rhs.i;
}
```

## Page 53

![Lecture 8 page 53](../page_images/08_8_Overloaded_Operators/page_053.png)

Extracted text:

```text
Relational operators…
// implement lhs > rhs in terms of lhs < rhs
bool Integer::operator>( const Integer& rhs ) const {
    return rhs < *this;
}
// implement lhs <= rhs in terms of !(rhs < lhs)
bool Integer::operator<=( const Integer& rhs ) const {
    return !(rhs < *this);
}
// implement lhs >= rhs in terms of !(lhs < rhs)
bool Integer::operator>=( const Integer& rhs ) const {
    return !(*this < rhs);
}
```

## Page 54

![Lecture 8 page 54](../page_images/08_8_Overloaded_Operators/page_054.png)

Extracted text:

```text
Operator []
• Must be a member function
• Single argument
• Implies that the object acts like an array, so it
  should return a reference
   Vector v(100);    // create a vector of size 100
   v[10] = 45;
   Note: if returned a pointer you would need to do:
   *v[10] = 45;
   See: vector.h, vector.cpp
```

## Page 55

![Lecture 8 page 55](../page_images/08_8_Overloaded_Operators/page_055.png)

Extracted text:

```text
Copying vs. Initialization
MyType b;
MyType a = b;
a = b;


Example: CopyingVsInitialization.cpp
```

## Page 56

![Lecture 8 page 56](../page_images/08_8_Overloaded_Operators/page_056.png)

Extracted text:

```text
Automatic operator= creation
• The compiler will automatically create one
  if it’s not explicitly provided.
• memberwise assignment

• Example: AutomaticOperatorEquals.cpp
```

## Page 57

![Lecture 8 page 57](../page_images/08_8_Overloaded_Operators/page_057.png)

Extracted text:

```text
Assignment operator
• Must be a member function
• Return a reference to *this
   A = B = C;
   // executed as A = (B = C);
```

## Page 58

![Lecture 8 page 58](../page_images/08_8_Overloaded_Operators/page_058.png)

Extracted text:

```text
Assignment operator
• Must be a member function
• Return a reference to *this
   A = B = C;
   // executed as A = (B = C);
• Be sure to assign to all data members: pointers…
```

## Page 59

![Lecture 8 page 59](../page_images/08_8_Overloaded_Operators/page_059.png)

Extracted text:

```text
Assignment operator
• Must be a member function
• Return a reference to *this
   A = B = C;
   // executed as A = (B = C);
• Be sure to assign to all data members: pointers…
• Check for self-assignment
```

## Page 60

![Lecture 8 page 60](../page_images/08_8_Overloaded_Operators/page_060.png)

Extracted text:

```text
Assignment operator skeleton
T& T::operator=( const T& rhs ) {
    // check for self assignment
    if ( this != &rhs ) {
        // perform assignment
    }
    return *this;
}


//This checks address, not value (*this != rhs)
```

## Page 61

![Lecture 8 page 61](../page_images/08_8_Overloaded_Operators/page_061.png)

Extracted text:

```text
Assignment operator
• For classes with dynamically allocated
  memory declare an assignment operator
  (and a copy constructor)
• To prevent assignment, explicitly declare
  operator= as private, or use =delete;
```

## Page 62

![Lecture 8 page 62](../page_images/08_8_Overloaded_Operators/page_062.png)

Extracted text:

```text
Operator ( )
• A functor, which overloads the function call
  operator, is an object that acts like a function.
 struct F {
   void operator()(int x) const {
     std::cout << x << "\n";
   }
 }; // F is a functor

 F f;
 f(2); // calls f.operator()
```

## Page 63

![Lecture 8 page 63](../page_images/08_8_Overloaded_Operators/page_063.png)

Extracted text:

```text
User-defined type conversions
 • A conversion operator can be used to convert
   an object of one class into
  – an object of another class
  – a built-in type
 • Compilers perform implicit conversions using:
  – Single-argument constructors
  – implicit type conversion operators
```

## Page 64

![Lecture 8 page 64](../page_images/08_8_Overloaded_Operators/page_064.png)

Extracted text:

```text
Single argument constructors
 class PathName {
    string name;
 public:
    // or could be multi-argument with defaults
    PathName(const string&);
    ~ PathName();
 };
 ...
 string abc("abc");
 PathName xyz(abc); // OK!
 xyz = abc;          // OK abc => PathName

 Example: AutomaticTypeConversion.cpp
```

## Page 65

![Lecture 8 page 65](../page_images/08_8_Overloaded_Operators/page_065.png)

Extracted text:

```text
Prevent implicit conversions
• New keyword: explicit
class PathName {
   string name;
public:
   explicit PathName(const string&);
   ~ PathName();
};
...
string abc("abc");
PathName xyz(abc); // OK!
xyz = abc;          // error!

Example: ExplicitKeyword.cpp
```

## Page 66

![Lecture 8 page 66](../page_images/08_8_Overloaded_Operators/page_066.png)

Extracted text:

```text
Conversion operations
• Operator conversion
  – Function will be called automatically
  – Return type is same as function name
class Rational {
public:
   ...
   // Rational to double
   operator double() const {
     return numerator_/(double)denominator_;
   }
}
Rational r(1,3); double d = 1.3 * r; // r=>double
```

## Page 67

![Lecture 8 page 67](../page_images/08_8_Overloaded_Operators/page_067.png)

Extracted text:

```text
General form of conversion ops
• X::operator T()
  –Operator name is any type descriptor
  –No explicit arguments
  –No return type
  –Compiler will use it as a type conversion from X T
```

## Page 68

![Lecture 8 page 68](../page_images/08_8_Overloaded_Operators/page_068.png)

Extracted text:

```text
C++ type conversions
• Built-in conversions
  –Primitive
      char  short  int  float  double
                    int  long
  – Any type T
          T T&          T& T     T* void*
          T[] T*        T* T[]   T const T
```

## Page 69

![Lecture 8 page 69](../page_images/08_8_Overloaded_Operators/page_069.png)

Extracted text:

```text
C++ type conversions
• Built-in conversions
  –Primitive
       char  short  int  float  double
                     int  long
  – Any type T
           T T&             T& T              T* void*
           T[] T*           T* T[]            T const T
• User-defined T  C
  – if C(T) is a valid constructor call for C
  –if operator C() is defined for T
```

## Page 70

![Lecture 8 page 70](../page_images/08_8_Overloaded_Operators/page_070.png)

Extracted text:

```text
C++ type conversions
• Built-in conversions
  –Primitive
        char  short  int  float  double
                      int  long
  – Any type T
            T T&            T& T              T* void*
            T[] T*          T* T[]            T const T
• User-defined T  C
  – if C(T) is a valid constructor call for C
  –if operator C() is defined for T
• BUT
  – See: TypeConversionAmbiguity.cpp
```

## Page 71

![Lecture 8 page 71](../page_images/08_8_Overloaded_Operators/page_071.png)

Extracted text:

```text
Do you want to use them?
• In general, be careful!
 – Cause lots of problems when functions are called
 unexpectedly.
• Use explicit conversion functions. Instead of using
  the conversion operator, declare a member
  function in class Rational:
    double to_double() const;
```

## Page 72

![Lecture 8 page 72](../page_images/08_8_Overloaded_Operators/page_072.png)

Extracted text:

```text
Overloading and type conversion
• C++ checks each argument for a "best match"
• Best match means cheapest
 – Exact match is cost-free
 – Matches involving built-in conversions
 – User-defined type conversions
```

## Page 73

![Lecture 8 page 73](../page_images/08_8_Overloaded_Operators/page_073.png)

Extracted text:

```text
Overloading
• Just because you can overload an operator
  doesn't mean you should.
• Overload operators when it makes the code
  easier to read and maintain.
```
