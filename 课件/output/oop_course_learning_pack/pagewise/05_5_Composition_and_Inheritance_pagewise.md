# Lecture 05: 5 Composition and Inheritance

- Source: `5 Composition and Inheritance.pdf`
- Pages: 60
- Rendered page images: 60
- Contact sheet: [open](../contact_sheets/05_5_Composition_and_Inheritance_contact.jpg)
- Raw extracted text: [open](../raw_texts/05-5 Composition and Inheritance.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 5 page 1](../page_images/05_5_Composition_and_Inheritance/page_001.png)

Extracted text:

```text
Composition & Inheritance
    Object-Oriented Programming with C++
```

## Page 2

![Lecture 5 page 2](../page_images/05_5_Composition_and_Inheritance/page_002.png)

Extracted text:

```text
Reusing the implementation
• Composition: construct new object with existing
  objects
• It is the relationship of has-a

   car


         engine             tyre
```

## Page 3

![Lecture 5 page 3](../page_images/05_5_Composition_and_Inheritance/page_003.png)

Extracted text:

```text
Composition
• Objects can be used to   • For example, an
  build up other objects     Employee has a
• Ways of inclusion          – Name
   – Fully                   – Address
   – By reference            – Health Plan
                             – Salary History
• Inclusion by reference
                                • Collection of Raise
  allows sharing                  objects
                             – Supervisor
                                • Another Employee
                                  object!
```

## Page 4

![Lecture 5 page 4](../page_images/05_5_Composition_and_Inheritance/page_004.png)

Extracted text:

```text
Composition in action
Classes                            Instances
      Employee
         Name                 Henry Higgins
         Address
         Health Plan                            home
         Salary History                        address
                                 raises
         Supervisor

                                          YAHMO
                    Bill C.
```

## Page 5

![Lecture 5 page 5](../page_images/05_5_Composition_and_Inheritance/page_005.png)

Extracted text:

```text
[No extractable text]
```

## Page 6

![Lecture 5 page 6](../page_images/05_5_Composition_and_Inheritance/page_006.png)

Extracted text:

```text
[No extractable text]
```

## Page 7

![Lecture 5 page 7](../page_images/05_5_Composition_and_Inheritance/page_007.png)

Extracted text:

```text
[No extractable text]
```

## Page 8

![Lecture 5 page 8](../page_images/05_5_Composition_and_Inheritance/page_008.png)

Extracted text:

```text
Embedded objects
• All embedded objects must be initialized
   – The default constructor is called if
      • you don’t supply the arguments, and there is a default
        constructor (or one can be built)
• Initializer list on Constructor
   – any number of objects separated by commas
   – is optional
   – Provide arguments to sub-constructors
• Syntax:
      name( args ) [':' init-list] '{'
```

## Page 9

![Lecture 5 page 9](../page_images/05_5_Composition_and_Inheritance/page_009.png)

Extracted text:

```text
Example 2
class Person { … };
class Currency { … };
class SavingsAccount {
public:
    SavingsAccount( const char* name,
               const char* address, int cents);
    ~SavingsAccount();
    void print();
private:
    Person m_saver;
    Currency m_balance;
};
```

## Page 10

![Lecture 5 page 10](../page_images/05_5_Composition_and_Inheritance/page_010.png)

Extracted text:

```text
Example 2…
SavingsAccount::SavingsAccount(
 const char* name, const char* address, int cents)
 : m_saver(name, address),
   m_balance(0, cents)
{}

void SavingsAccount::print()
{
    m_saver.print();
    m_balance.print();
}
```

## Page 11

![Lecture 5 page 11](../page_images/05_5_Composition_and_Inheritance/page_011.png)

Extracted text:

```text
Question
• If we wrote the constructor as (assuming we
  have the set accessors for the sub-objects):
SavingsAccount::SavingsAccount(
  const char* name, const char* address, int cents)
{
   m_saver.set_name( name );
   m_saver.set_address( address );
   m_balance.set_cents( cents );
}

• Default constructors would be called
```

## Page 12

![Lecture 5 page 12](../page_images/05_5_Composition_and_Inheritance/page_012.png)

Extracted text:

```text
Public vs. Private
• It is common to make embedded objects private:
   – they are part of the underlying implementation
   – the new class only has part of the public interface of
     the old class
• Can embed as a public object if you want to have
  the entire public interface of the sub-object
  available in the new object:
  class SavingsAccount{
  public:
      Person m_saver;
      ...
  }； // assume Person class has set_name()
  SavingsAccount account;
  account.m_saver.set_name("Fred");
```

## Page 13

![Lecture 5 page 13](../page_images/05_5_Composition_and_Inheritance/page_013.png)

Extracted text:

```text
Inheritance
```

## Page 14

![Lecture 5 page 14](../page_images/05_5_Composition_and_Inheritance/page_014.png)

Extracted text:

```text
Reusing the interface
• Inheritance is to take the existing class, clone it, and
  then make additions and modifications to the clone.
```

## Page 15

![Lecture 5 page 15](../page_images/05_5_Composition_and_Inheritance/page_015.png)

Extracted text:

```text
Inheritance
• Language implementation technique
• Also an important component of the OO
  design methodology
• Allows sharing of design for
  – Member data
  – Member functions
  – Interfaces
• Key technology in C++
```

## Page 16

![Lecture 5 page 16](../page_images/05_5_Composition_and_Inheritance/page_016.png)

Extracted text:

```text
Inheritance
•The ability to define the behavior or
  implementation of one class as a derived
  one of another base class




              Person       Studen
                           t
```

## Page 17

![Lecture 5 page 17](../page_images/05_5_Composition_and_Inheritance/page_017.png)

Extracted text:

```text
[No extractable text]
```

## Page 18

![Lecture 5 page 18](../page_images/05_5_Composition_and_Inheritance/page_018.png)

Extracted text:

```text
[No extractable text]
```

## Page 19

![Lecture 5 page 19](../page_images/05_5_Composition_and_Inheritance/page_019.png)

Extracted text:

```text
[No extractable text]
```

## Page 20

![Lecture 5 page 20](../page_images/05_5_Composition_and_Inheritance/page_020.png)

Extracted text:

```text
[No extractable text]
```

## Page 21

![Lecture 5 page 21](../page_images/05_5_Composition_and_Inheritance/page_021.png)

Extracted text:

```text
[No extractable text]
```

## Page 22

![Lecture 5 page 22](../page_images/05_5_Composition_and_Inheritance/page_022.png)

Extracted text:

```text
[No extractable text]
```

## Page 23

![Lecture 5 page 23](../page_images/05_5_Composition_and_Inheritance/page_023.png)

Extracted text:

```text
[No extractable text]
```

## Page 24

![Lecture 5 page 24](../page_images/05_5_Composition_and_Inheritance/page_024.png)

Extracted text:

```text
[No extractable text]
```

## Page 25

![Lecture 5 page 25](../page_images/05_5_Composition_and_Inheritance/page_025.png)

Extracted text:

```text
[No extractable text]
```

## Page 26

![Lecture 5 page 26](../page_images/05_5_Composition_and_Inheritance/page_026.png)

Extracted text:

```text
[No extractable text]
```

## Page 27

![Lecture 5 page 27](../page_images/05_5_Composition_and_Inheritance/page_027.png)

Extracted text:

```text
[No extractable text]
```

## Page 28

![Lecture 5 page 28](../page_images/05_5_Composition_and_Inheritance/page_028.png)

Extracted text:

```text
[No extractable text]
```

## Page 29

![Lecture 5 page 29](../page_images/05_5_Composition_and_Inheritance/page_029.png)

Extracted text:

```text
[No extractable text]
```

## Page 30

![Lecture 5 page 30](../page_images/05_5_Composition_and_Inheritance/page_030.png)

Extracted text:

```text
[No extractable text]
```

## Page 31

![Lecture 5 page 31](../page_images/05_5_Composition_and_Inheritance/page_031.png)

Extracted text:

```text
[No extractable text]
```

## Page 32

![Lecture 5 page 32](../page_images/05_5_Composition_and_Inheritance/page_032.png)

Extracted text:

```text
[No extractable text]
```

## Page 33

![Lecture 5 page 33](../page_images/05_5_Composition_and_Inheritance/page_033.png)

Extracted text:

```text
[No extractable text]
```

## Page 34

![Lecture 5 page 34](../page_images/05_5_Composition_and_Inheritance/page_034.png)

Extracted text:

```text
[No extractable text]
```

## Page 35

![Lecture 5 page 35](../page_images/05_5_Composition_and_Inheritance/page_035.png)

Extracted text:

```text
[No extractable text]
```

## Page 36

![Lecture 5 page 36](../page_images/05_5_Composition_and_Inheritance/page_036.png)

Extracted text:

```text
[No extractable text]
```

## Page 37

![Lecture 5 page 37](../page_images/05_5_Composition_and_Inheritance/page_037.png)

Extracted text:

```text
[No extractable text]
```

## Page 38

![Lecture 5 page 38](../page_images/05_5_Composition_and_Inheritance/page_038.png)

Extracted text:

```text
[No extractable text]
```

## Page 39

![Lecture 5 page 39](../page_images/05_5_Composition_and_Inheritance/page_039.png)

Extracted text:

```text
[No extractable text]
```

## Page 40

![Lecture 5 page 40](../page_images/05_5_Composition_and_Inheritance/page_040.png)

Extracted text:

```text
Inheritance
• Class relationship: is-a

                       Base Class
       Employee        Super Parent



                       Derived Class
       Manager         Sub
                       Child
```

## Page 41

![Lecture 5 page 41](../page_images/05_5_Composition_and_Inheritance/page_041.png)

Extracted text:

```text
Declare an Employee class
class Employee {
public:
     Employee(const std::string& name,
         const std::string& ssn);
     const std::string& get_name() const;
     void print(std::ostream& out) const;
     void print(std::ostream& out,
         const std::string& msg) const;
protected:
     std::string m_name;
     std::string m_ssn;
};
```

## Page 42

![Lecture 5 page 42](../page_images/05_5_Composition_and_Inheritance/page_042.png)

Extracted text:

```text
Constructor for Employee
Employee::Employee(const string& name,
                   const string& ssn)
    : m_name(name), m_ssn(ssn)
{
     // initializer list sets up the values!
}
```

## Page 43

![Lecture 5 page 43](../page_images/05_5_Composition_and_Inheritance/page_043.png)

Extracted text:

```text
Employee member functions
inline const std::string& Employee::get_name() const
{
      return m_name;
}
inline void Employee::print(std::ostream& out) const
{
      out << m_name << endl;
      out << m_ssn << endl;
}
inline void Employee::print(std::ostream& out,
      const std::string& msg) const
{
      out << msg << endl;
      print(out);
}
```

## Page 44

![Lecture 5 page 44](../page_images/05_5_Composition_and_Inheritance/page_044.png)

Extracted text:

```text
Now add Manager
class Manager : public Employee {
public:
    Manager(const std::string& name,
            const std::string& ssn,
            const std::string& title);
    const std::string title_name() const;
    const std::string& get_title() const;
    void print(std::ostream& out) const;
private:
    std::string m_title;
};
```

## Page 45

![Lecture 5 page 45](../page_images/05_5_Composition_and_Inheritance/page_045.png)

Extracted text:

```text
Inheritance and constructors
• Think of inherited traits as an embedded
  object
• Base class is mentioned by class name

  Manager::Manager( const string& name,
                    const string& ssn,
                    const string& title = "" )
      : Employee(name, ssn), m_title( title )
  {
  }
```

## Page 46

![Lecture 5 page 46](../page_images/05_5_Composition_and_Inheritance/page_046.png)

Extracted text:

```text
More on constructors
• Base class is always constructed first
• If no explicit arguments are passed to base class
  – Default constructor will be called
• Destructors are called in exactly the reverse
  order of the constructors.
```

## Page 47

![Lecture 5 page 47](../page_images/05_5_Composition_and_Inheritance/page_047.png)

Extracted text:

```text
Manager member functions
inline void Manager::print( std::ostream& out ) const
{
      Employee::print( out ); //call the base class print
      out << m_title << endl;
}

inline const std::string& Manager::get_title() const
{
      return m_title;
}

inline const std::string Manager::title_name() const
{
      return string( m_title + ": " + m_name );
      // access base m_name
}
```

## Page 48

![Lecture 5 page 48](../page_images/05_5_Composition_and_Inheritance/page_048.png)

Extracted text:

```text
Uses
int main () {
    Employee bob( "Bob Jones", "555-44-0000" );
    Manager bill( "Bill Smith", "666-55-1234",
                  "ImportantPerson" );

    string name = bill.get_name(); // okay Manager
      inherits Employee
    string title = bob.get_title(); // Error --
      bob is an Employee!
    cout << bill.title_name() << '\n' << endl;
    bob.print(cout);
    bob.print(cout, "Employee:");
    bill.print(cout);
    bill.print(cout, "Employee:"); // Error -- hidden!
}
```

## Page 49

![Lecture 5 page 49](../page_images/05_5_Composition_and_Inheritance/page_049.png)

Extracted text:

```text
Name Hiding
• If you redefine a member function in the
  derived class, all other overloaded functions
  in the base class are inaccessible.
• We'll see how the keyword virtual affects
  function overloading next time.
```

## Page 50

![Lecture 5 page 50](../page_images/05_5_Composition_and_Inheritance/page_050.png)

Extracted text:

```text
Access protection
```

## Page 51

![Lecture 5 page 51](../page_images/05_5_Composition_and_Inheritance/page_051.png)

Extracted text:

```text
Access protection
• Members
  - Public: visible to all clients
  - Protected: visible to classes derived from self (and to
  friends)
  - Private: visible only to self and to friends!
```

## Page 52

![Lecture 5 page 52](../page_images/05_5_Composition_and_Inheritance/page_052.png)

Extracted text:

```text
Friends
• To explicitly grant access to a function that isn’t
  a member of the structure.
• The class itself controls which code has access
  to its members.
• Can declare a global function as a friend, as
  well as a member function of another class, or
  even an entire class, as a friend.
   – Example: Friend.cpp
```

## Page 53

![Lecture 5 page 53](../page_images/05_5_Composition_and_Inheritance/page_053.png)

Extracted text:

```text
class vs. struct

• class defaults to private
• struct defaults to public
```

## Page 54

![Lecture 5 page 54](../page_images/05_5_Composition_and_Inheritance/page_054.png)

Extracted text:

```text
Access protection
• Inheritance
   – Public:    class Derived : public Base ...
   – Protected: class Derived : protected Base ...
   – Private:   class Derived : private Base ...
```

## Page 55

![Lecture 5 page 55](../page_images/05_5_Composition_and_Inheritance/page_055.png)

Extracted text:

```text
How inheritance affects access
 Suppose class B is derived from A. Then:
                    Base class member access specifier
  Inheritance          public        protected      private
  Type ( B is )
  :public A          public in B   protected in B private

  :private A        private in B     private in B   private

  :protected A     protected in B protected in B private
```

## Page 56

![Lecture 5 page 56](../page_images/05_5_Composition_and_Inheritance/page_056.png)

Extracted text:

```text
Scopes and access in C++
```

## Page 57

![Lecture 5 page 57](../page_images/05_5_Composition_and_Inheritance/page_057.png)

Extracted text:

```text
Conversions
• Public Inheritance should imply substitution
  – If B is-a A, you can use a B anywhere an A can
    be used.
     • if B is-a A, then everything that is true for A is also
       true of B.
  – Be careful if the substitution is not valid!
```

## Page 58

![Lecture 5 page 58](../page_images/05_5_Composition_and_Inheritance/page_058.png)

Extracted text:

```text
Up-casting
• Upcasting is the act of converting from a
  derived reference or pointer to a base class
  reference or pointer.

                     Base


                     Derived
```

## Page 59

![Lecture 5 page 59](../page_images/05_5_Composition_and_Inheritance/page_059.png)

Extracted text:

```text
Up-casting
• Is to regard an object of the derived class as an
  object of the base class.
• It is to say: Students are human beings. You are
  students. So you are human being.

                        Human
                         being



                        Students
```

## Page 60

![Lecture 5 page 60](../page_images/05_5_Composition_and_Inheritance/page_060.png)

Extracted text:

```text
Up-casting examples
Manager pete("Pete", "444-55-6666", "Bakery");
Employee* ep = &pete; // Upcast
Employee& er = pete; // Upcast


• Lose type information about the object:
ep->print(cout);      // prints base class version
```
