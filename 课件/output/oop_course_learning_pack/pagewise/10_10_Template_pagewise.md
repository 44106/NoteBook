# Lecture 10: 10 Template

- Source: `10 Template.pdf`
- Pages: 47
- Rendered page images: 47
- Contact sheet: [open](../contact_sheets/10_10_Template_contact.jpg)
- Raw extracted text: [open](../raw_texts/10-10 Template.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 10 page 1](../page_images/10_10_Template/page_001.png)

Extracted text:

```text
Templates
Object-Oriented Programming with C++
```

## Page 2

![Lecture 10 page 2](../page_images/10_10_Template/page_002.png)

Extracted text:

```text
Why templates?
```

## Page 3

![Lecture 10 page 3](../page_images/10_10_Template/page_003.png)

Extracted text:

```text
Why templates?
• Suppose you need a list of X and a list of Y
  –The lists would use similar code
  –They differ by the type stored in the list
```

## Page 4

![Lecture 10 page 4](../page_images/10_10_Template/page_004.png)

Extracted text:

```text
Why templates?
• Suppose you need a list of X and a list of Y
  –The lists would use similar code
  –They differ by the type stored in the list
• Choices
  –Clone code
    •preserves type-safety
    •hard to manage
```

## Page 5

![Lecture 10 page 5](../page_images/10_10_Template/page_005.png)

Extracted text:

```text
Why templates?
• Suppose you need a list of X and a list of Y
  –The lists would use similar code
  –They differ by the type stored in the list
• Choices
  –Clone code
    •preserves type-safety
    •hard to manage
  –Make a common base class
    •May not be desirable
```

## Page 6

![Lecture 10 page 6](../page_images/10_10_Template/page_006.png)

Extracted text:

```text
Why templates?
• Suppose you need a list of X and a list of Y
  –The lists would use similar code
  –They differ by the type stored in the list
• Choices
  –Clone code
    •preserves type-safety
    •hard to manage
  –Make a common base class
    •May not be desirable
  –Untyped lists
    •type unsafe
```

## Page 7

![Lecture 10 page 7](../page_images/10_10_Template/page_007.png)

Extracted text:

```text
Templates
• Reuse source code
 –generic programming
 –use types as parameters in class or function definitions
```

## Page 8

![Lecture 10 page 8](../page_images/10_10_Template/page_008.png)

Extracted text:

```text
Templates
• Reuse source code
 –generic programming
 –use types as parameters in class or function definitions
• Function Template
 –Example: sort function
```

## Page 9

![Lecture 10 page 9](../page_images/10_10_Template/page_009.png)

Extracted text:

```text
Templates
• Reuse source code
 –generic programming
 –use types as parameters in class or function definitions
• Function Template
 –Example: sort function
• Class Template
 –Example: containers such as stack,list,queue...
    •stack operations are independent of the type of items in the
     stack
 –template member functions
```

## Page 10

![Lecture 10 page 10](../page_images/10_10_Template/page_010.png)

Extracted text:

```text
Function templates
• Perform similar operations on different types of
  data.
• Swap function for two int arguments:
    void swap ( int& x, int& y ) {
        int temp = x;
        x = y;
        y = temp;
    }
• What if we want to swap floats, strings, Currency,
  Person?
```

## Page 11

![Lecture 10 page 11](../page_images/10_10_Template/page_011.png)

Extracted text:

```text
Example: swap function templates
  template < class T >
  void swap( T& x, T& y ){
      T temp = x;
      x = y;
      y = temp;
  }

  •The template keyword introduces the template
  •The class T specifies a parameterized type name
      •class means any built-in type or user-defined type
  •Inside the template, use T as a type name
```

## Page 12

![Lecture 10 page 12](../page_images/10_10_Template/page_012.png)

Extracted text:

```text
Function templates syntax
• Type parameters represent:
 –types of arguments to the function
 –return type of the function
 –define variables within the function
```

## Page 13

![Lecture 10 page 13](../page_images/10_10_Template/page_013.png)

Extracted text:

```text
Template instantiation
• Generating a definition from a template
  class/function and template arguments:
 –Types are substituted into template
 –New body of function or class definition is created
    •syntax errors, type checking
 –Specialization -- a version of a template for a
 particular argument(s)
```

## Page 14

![Lecture 10 page 14](../page_images/10_10_Template/page_014.png)

Extracted text:

```text
Example: using swap
 int i = 3; int j = 4;
 swap(i, j); // use explicit int swap

 float k = 4.5; float m = 3.7;
 swap(k, m); // instantiate float swap

 std::string s("Hello");
 std::string t("World");
 swap(s, t); // instantiate std::string swap

• A template function is an instantiation of a function
  template
```

## Page 15

![Lecture 10 page 15](../page_images/10_10_Template/page_015.png)

Extracted text:

```text
Interactions
• Only exact match on types is used
```

## Page 16

![Lecture 10 page 16](../page_images/10_10_Template/page_016.png)

Extracted text:

```text
Interactions
• Only exact match on types is used
• No conversion operations are applied
 –swap(int, int);    // ok
 –swap(double, double); // ok
 –swap(int, double);     // error!
```

## Page 17

![Lecture 10 page 17](../page_images/10_10_Template/page_017.png)

Extracted text:

```text
Interactions
• Only exact match on types is used
• No conversion operations are applied
  –swap(int, int);    // ok
  –swap(double, double); // ok
  –swap(int, double);     // error!
• Even implicit conversions are ignored
```

## Page 18

![Lecture 10 page 18](../page_images/10_10_Template/page_018.png)

Extracted text:

```text
Interactions
• Only exact match on types is used
• No conversion operations are applied
  –swap(int, int);    // ok
  –swap(double, double); // ok
  –swap(int, double);     // error!
• Even implicit conversions are ignored
• Template functions and regular
  functions coexist
```

## Page 19

![Lecture 10 page 19](../page_images/10_10_Template/page_019.png)

Extracted text:

```text
Overloading rules
• Check first for unique function match
• Then check for unique function template match
• Then implicit conversions on regular functions
 void f(float i, float k) {};

 template <class T>
 void f(T t, T u) {};

 f(1.0f, 2.0f);
 f(1.0, 2.0);
 f(1, 2);
 f(1, 2.0);
```

## Page 20

![Lecture 10 page 20](../page_images/10_10_Template/page_020.png)

Extracted text:

```text
Function instantiation
• The compiler deduces the template type from the
  actual arguments passed into the function.
• Can be explicit:
 – for example, if the parameter is not in the function
 signature (older compilers won't allow this...)

 template <class T>
 void foo() { /* … */ }
```

## Page 21

![Lecture 10 page 21](../page_images/10_10_Template/page_021.png)

Extracted text:

```text
Function instantiation
• The compiler deduces the template type from the
  actual arguments passed into the function.
• Can be explicit:
 – for example, if the parameter is not in the function
 signature (older compilers won't allow this...)

 template <class T>
 void foo() { /* … */ }

 foo<int>();           // type T is int
 foo<float>();         // type T is float
```

## Page 22

![Lecture 10 page 22](../page_images/10_10_Template/page_022.png)

Extracted text:

```text
Class templates
```

## Page 23

![Lecture 10 page 23](../page_images/10_10_Template/page_023.png)

Extracted text:

```text
Class templates
• Classes parameterized by types
  –Abstract operations from the types being operated upon
  –Define potentially infinite set of classes
  –Another step towards reuse!
```

## Page 24

![Lecture 10 page 24](../page_images/10_10_Template/page_024.png)

Extracted text:

```text
Class templates
• Classes parameterized by types
  –Abstract operations from the types being operated upon
  –Define potentially infinite set of classes
  –Another step towards reuse!

• Typical use: container classes
   •stack <int>
    • is a stack that is parameterized over int
  •list <Person*>
  •queue <Job>
```

## Page 25

![Lecture 10 page 25](../page_images/10_10_Template/page_025.png)

Extracted text:

```text
Example: Vector
template <class T>
class Vector{
public:
    Vector(int);
    ~Vector();
    Vector(const Vector&);
    Vector& operator=(const Vector&);
    T& operator[](int);
private:
    T* m_elements;
    int m_size;
}
```

## Page 26

![Lecture 10 page 26](../page_images/10_10_Template/page_026.png)

Extracted text:

```text
Usage
Vector<int> v1(100);
Vector<Complex> v2(256);

v1[20] = 10;
v2[20] = v1[20];   // ok if int->Complex defined
```

## Page 27

![Lecture 10 page 27](../page_images/10_10_Template/page_027.png)

Extracted text:

```text
Vector members
template <class T>
Vector<T>::Vector(int size): m_size(size) {
    m_elements = new T[m_size];
}
template <class T>
T& Vector<T>::operator[](int index)
{
    if(index < m_size && index >= 0) {
        return m_elements[index];
    } else {
        …
    }
}
```

## Page 28

![Lecture 10 page 28](../page_images/10_10_Template/page_028.png)

Extracted text:

```text
A simple sort function
// bubble sort – don't use it!
template <class T>
void sort(Vector<T>& arr) {
    const size_t last = arr.size() - 1;
    for(int i=0; i<last; i++)
    for(int j = last; j>i; j--) {
        if(arr[j] < arr[j-1]) {
            // which swap?
            swap(arr[j], arr[j-1]);
        }
    }
}
```

## Page 29

![Lecture 10 page 29](../page_images/10_10_Template/page_029.png)

Extracted text:

```text
Sorting the Vector
Vector<int> vi(4);
vi[0] = 4; vi[1] = 3; vi[2] = 7; vi[3] = 1;
sort(vi); // sort(Vector<int>&)

Vector<string> vs(5);
vs[0] = "Fred";
vs[1] = "Wilma";
vs[2] = "Barney";
vs[3] = "Dino";
vs[4] = "Prince";
sort(vs); // sort(Vector<string>&);
//NOTE: sort use operator< for comparison
```

## Page 30

![Lecture 10 page 30](../page_images/10_10_Template/page_030.png)

Extracted text:

```text
Templates
• Templates can use multiple types
  template < class Key, class Value >
  class HashTable {
      const Value& lookup (const Key&) const;
      void insert (const Key&, const Value&);
      …
  }
```

## Page 31

![Lecture 10 page 31](../page_images/10_10_Template/page_031.png)

Extracted text:

```text
Templates
• Templates can use multiple types
  template < class Key, class Value >
  class HashTable {
      const Value& lookup (const Key&) const;
      void insert (const Key&, const Value&);
      …
  }
• Templates nest – they’re just new types!
   Vector< Vector<double*> >
```

## Page 32

![Lecture 10 page 32](../page_images/10_10_Template/page_032.png)

Extracted text:

```text
Templates
• Templates can use multiple types
  template < class Key, class Value >
  class HashTable {
      const Value& lookup (const Key&) const;
      void insert (const Key&, const Value&);
      …
  }
• Templates nest – they’re just new types!
   Vector< Vector<double*> >
• Type arguments can be complicated
   Vector< int (*) (Vector<double>&, int) >
```

## Page 33

![Lecture 10 page 33](../page_images/10_10_Template/page_033.png)

Extracted text:

```text
Expression parameters
• Template arguments can be constant expressions
• Non-Type parameters
  – can have a default argument

 template <class T, int bounds = 100>
 class FixedVector {
 public:
     FixedVector();
     T& operator[](int);
 private:
     T elements[bounds];   // fixed-size array!
 }
```

## Page 34

![Lecture 10 page 34](../page_images/10_10_Template/page_034.png)

Extracted text:

```text
Non-Type parameters
template <class T, int bounds>
T& FixedVector<T, bounds>::operator[] (int i){
    return elements[i];   //no error checking
}
```

## Page 35

![Lecture 10 page 35](../page_images/10_10_Template/page_035.png)

Extracted text:

```text
Usage: non-type parameters
•Usage
 - FixedVector<int, 50> v1;
 - FixedVector<int, 10*5> v2;
 - FixedVector<int> v3; // uses default
•Summary
 –Embedding sizes not necessarily a good idea
 –Can make code faster
 –Makes code more complicated
   •size argument appears everywhere!
 –Can lead to (even more) code bloat
```

## Page 36

![Lecture 10 page 36](../page_images/10_10_Template/page_036.png)

Extracted text:

```text
Templates and inheritance
• Templates can inherit from non-template classes
  template <class A>
  class Derived : public Base {…}
```

## Page 37

![Lecture 10 page 37](../page_images/10_10_Template/page_037.png)

Extracted text:

```text
Templates and inheritance
• Templates can inherit from non-template classes
  template <class A>
  class Derived : public Base {…}
• Templates can inherit from template classes
  template <class A>
  class Derived : public List<A> {…}
```

## Page 38

![Lecture 10 page 38](../page_images/10_10_Template/page_038.png)

Extracted text:

```text
Templates and inheritance
• Templates can inherit from non-template classes
  template <class A>
  class Derived : public Base {…}
• Templates can inherit from template classes
  template <class A>
  class Derived : public List<A> {…}

• Non-template classes can inherit from templates
  class SupervisorGroup : public
    List<Employee*> {…}
```

## Page 39

![Lecture 10 page 39](../page_images/10_10_Template/page_039.png)

Extracted text:

```text
Recurring template pattern
• General form
   // The Curiously Recurring Template Pattern (CRTP)
   template <class T>
   class Base
   {
       // ...
   };
   class Derived : public Base<Derived>
   {
       // ...
   };
```

## Page 40

![Lecture 10 page 40](../page_images/10_10_Template/page_040.png)

Extracted text:

```text
Recurring template pattern
• Simulate virtual function in generic programming
    template <class T>
    class Base {
      void interface() {
          static_cast<T*>(this)->implementation(); // ...
      }
      static void static_func() {
          T::static_sub_func(); // ...
      }
    };
    class Derived : public Base<Derived> {
      void implementation();
      static void static_sub_func();
    };
```

## Page 41

![Lecture 10 page 41](../page_images/10_10_Template/page_041.png)

Extracted text:

```text
Notes
• Friends
• Static Members
• In general put the definition and the declaration
  for the template in the header file
 – won't allocate storage for the class at that point
 – compiler/linker has mechanism for removing multiple
 definitions
```

## Page 42

![Lecture 10 page 42](../page_images/10_10_Template/page_042.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
```

## Page 43

![Lecture 10 page 43](../page_images/10_10_Template/page_043.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
•Establish a good set of test cases
```

## Page 44

![Lecture 10 page 44](../page_images/10_10_Template/page_044.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
•Establish a good set of test cases
•Measure performance and tune
```

## Page 45

![Lecture 10 page 45](../page_images/10_10_Template/page_045.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
•Establish a good set of test cases
•Measure performance and tune

•Review implementation
  –Which types should be parameterized?
```

## Page 46

![Lecture 10 page 46](../page_images/10_10_Template/page_046.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
•Establish a good set of test cases
•Measure performance and tune

•Review implementation
  –Which types should be parameterized?
•Convert non-parameterized version into template
```

## Page 47

![Lecture 10 page 47](../page_images/10_10_Template/page_047.png)

Extracted text:

```text
Writing templates
•Get a non-template version working first
•Establish a good set of test cases
•Measure performance and tune

•Review implementation
  –Which types should be parameterized?
•Convert non-parameterized version into template
•Test against established test cases
```
