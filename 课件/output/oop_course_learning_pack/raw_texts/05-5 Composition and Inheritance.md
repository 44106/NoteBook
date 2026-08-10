# Lecture 5: 5 Composition and Inheritance

Source: `5 Composition and Inheritance.pdf`
Pages: 60

## Page 1

Composition & Inheritance
    Object-Oriented Programming with C++

## Page 2

Reusing the implementation
• Composition: construct new object with existing
  objects
• It is the relationship of has-a

   car


         engine             tyre

## Page 3

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

## Page 4

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

## Page 5

[No extractable text]

## Page 6

[No extractable text]

## Page 7

[No extractable text]

## Page 8

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

## Page 9

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

## Page 10

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

## Page 11

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

## Page 12

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

## Page 13

Inheritance

## Page 14

       Reusing the interface
• Inheritance is to take the existing class, clone it, and
  then make additions and modifications to the clone.

## Page 15

              Inheritance
• Language implementation technique
• Also an important component of the OO
  design methodology
• Allows sharing of design for
  – Member data
  – Member functions
  – Interfaces
• Key technology in C++

## Page 16

            Inheritance
•The ability to define the behavior or
  implementation of one class as a derived
  one of another base class




              Person       Studen
                           t

## Page 17

[No extractable text]

## Page 18

[No extractable text]

## Page 19

[No extractable text]

## Page 20

[No extractable text]

## Page 21

[No extractable text]

## Page 22

[No extractable text]

## Page 23

[No extractable text]

## Page 24

[No extractable text]

## Page 25

[No extractable text]

## Page 26

[No extractable text]

## Page 27

[No extractable text]

## Page 28

[No extractable text]

## Page 29

[No extractable text]

## Page 30

[No extractable text]

## Page 31

[No extractable text]

## Page 32

[No extractable text]

## Page 33

[No extractable text]

## Page 34

[No extractable text]

## Page 35

[No extractable text]

## Page 36

[No extractable text]

## Page 37

[No extractable text]

## Page 38

[No extractable text]

## Page 39

[No extractable text]

## Page 40

             Inheritance
• Class relationship: is-a

                       Base Class
       Employee        Super Parent



                       Derived Class
       Manager         Sub
                       Child

## Page 41

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

## Page 42

   Constructor for Employee
Employee::Employee(const string& name,
                   const string& ssn)
    : m_name(name), m_ssn(ssn)
{
     // initializer list sets up the values!
}

## Page 43

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

## Page 44

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

## Page 45

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

## Page 46

      More on constructors
• Base class is always constructed first
• If no explicit arguments are passed to base class
  – Default constructor will be called
• Destructors are called in exactly the reverse
  order of the constructors.

## Page 47

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

## Page 48

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

## Page 49

             Name Hiding
• If you redefine a member function in the
  derived class, all other overloaded functions
  in the base class are inaccessible.
• We'll see how the keyword virtual affects
  function overloading next time.

## Page 50

Access protection

## Page 51

           Access protection
• Members
  - Public: visible to all clients
  - Protected: visible to classes derived from self (and to
  friends)
  - Private: visible only to self and to friends!

## Page 52

                      Friends
• To explicitly grant access to a function that isn’t
  a member of the structure.
• The class itself controls which code has access
  to its members.
• Can declare a global function as a friend, as
  well as a member function of another class, or
  even an entire class, as a friend.
   – Example: Friend.cpp

## Page 53

              class vs. struct

• class defaults to private
• struct defaults to public

## Page 54

          Access protection
• Inheritance
   – Public:    class Derived : public Base ...
   – Protected: class Derived : protected Base ...
   – Private:   class Derived : private Base ...

## Page 55

How inheritance affects access
 Suppose class B is derived from A. Then:
                    Base class member access specifier
  Inheritance          public        protected      private
  Type ( B is )
  :public A          public in B   protected in B private

  :private A        private in B     private in B   private

  :protected A     protected in B protected in B private

## Page 56

Scopes and access in C++

## Page 57

                  Conversions
• Public Inheritance should imply substitution
  – If B is-a A, you can use a B anywhere an A can
    be used.
     • if B is-a A, then everything that is true for A is also
       true of B.
  – Be careful if the substitution is not valid!

## Page 58

               Up-casting
• Upcasting is the act of converting from a
  derived reference or pointer to a base class
  reference or pointer.

                     Base


                     Derived

## Page 59

                  Up-casting
• Is to regard an object of the derived class as an
  object of the base class.
• It is to say: Students are human beings. You are
  students. So you are human being.

                        Human
                         being



                        Students

## Page 60

       Up-casting examples
Manager pete("Pete", "444-55-6666", "Bakery");
Employee* ep = &pete; // Upcast
Employee& er = pete; // Upcast


• Lose type information about the object:
ep->print(cout);      // prints base class version
