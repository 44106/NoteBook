# Lecture 14: 14 Smart Pointers

Source: `14 Smart Pointers.pdf`
Pages: 31

## Page 1

Smart Pointers
Object-Oriented Programming with C++

## Page 2

        std smart pointers
• Standard library holder for raw pointers on
  stack
  − std::unique_ptr
  − std::shared_ptr
  − std::weak_ptr
  − std::auto_ptr (deprecated in C++11)
  − …

## Page 3

    Putting it all together
                     Templates
                    Inheritance
                Reference Counting
                  Smart Pointers



Reference: C++ Strategies and Tactics, Robert Murray, 1993

## Page 4

                         Goals
• Introduce the code for maintaining reference
  counts
 – A reference count is a count of the number of times an
 object is shared
 – Pointer manipulations have to maintain the count
• Class UCObject holds the count
 –"Use-counted object"
• UCPointer is a smart pointer to a UCObject
 – A smart pointer is an object defined by a class
 – Implemented using a template
 – Overloads operator-> and unary operator*

## Page 5

 Reference counts in action
String x("abcdef");



        x
                        1    abcdef



        Shared memory maintains a count of
        how many times it is shared

## Page 6

 Reference counts in action
String x("abcdef");
String y = x; // shallow copy of x


        x
                   2   abcdef




        y

## Page 7

 Reference counts in action
String x("abcdef");
String y = x; // shallow copy of x
x = "Hello world"; // copy on write

                   1   Hello world
       x
                   1   abcdef




        y

## Page 8

Reference counting
                     3

## Page 9

       Reference counting
• Each shareable object has a counter
                                        3

## Page 10

       Reference counting
• Each shareable object has a counter
• Initial value is 0                    3

## Page 11

         Reference counting
• Each shareable object has a counter
• Initial value is 0                    3
• Whenever a pointer is assigned:
p = q;

## Page 12

         Reference counting
• Each shareable object has a counter
• Initial value is 0                           3
• Whenever a pointer is assigned:
p = q;
• Have to do the following
p->decrement(); // p's count will decrease
  p = q;
p->increment(); // q/p's count will increase

## Page 13

    The four classes involved
Smart pointer                           2
to UCObject,          UCPointer
a template                                     1
                                                          Implements
                                            UC Object     the reference
                                                          count
              has-a             has-a              is-a



Public interface                                          Details of string
to clients             String               String Rep    representation,
                                                          is sharable

                       4                        3

## Page 14

Reusing reference counting
#include <assert.h>
class UCObject {
public:
    UCObject() : m_refCount(0) { }
    virtual ~UCObject() { assert(m_refCount == 0); }
    UCObject(const UCObject&) : m_refCount(0) { }
    void incr() { m_refCount++; }
    void decr();
    int references() { return m_refCount; }
private:
    int m_refCount;
};

## Page 15

    UCObject continued
inline void UCObject::decr(){
  m_refCount -= 1;
  if (m_refCount == 0) {
    delete this;
  }
}
• “delete this” is legal on heap object
–But don't use it on stack!

## Page 16

           Class UCPointer
template <class T>
class UCPointer {
private:
    T* m_pObj;
    void increment() { if (m_pObj) m_pObj->incr(); }
    void decrement() { if (m_pObj) m_pObj->decr(); }
public:
    UCPointer(T* r = 0): m_pObj(r) { increment(); }
    ~UCPointer() { decrement(); };
    UCPointer(const UCPointer<T> & p);
    UCPointer& operator=(const UCPointer<T> &);
    T* operator->() const;
    T& operator*() const { return *m_pObj; }
};

## Page 17

         UCPointer copy ctor
template <class T>
UCPointer<T>::UCPointer(const UCPointer<T> & p) {
    m_pObj = p.m_pObj;
    increment();
}

## Page 18

        UCPointer assignment
template <class T>
UCPointer<T>&
UCPointer<T>::operator=(const UCPointer<T>& p) {
    if (m_pObj != p.m_pObj) {
        decrement();
        m_pObj = p.m_pObj;
        increment();
    }
    return *this;
}

## Page 19

         Envelope and Letter
• Envelope provides protection
• Letter contains the contents
                                        UCObject
                                             is a
                           m_refCount
String                                  StringRep
                            m_pChars

   UCPointer<StringRep>

## Page 20

           Class String
class String {
public:
    String(const char *);
    ~String();
    String(const String&);
    String& operator=(const String&);
    int operator==(const String&) const;
    String operator+(const String&) const;
    int length() const;
    operator const char*() const;
private:
    UCPointer<StringRep> m_rep;
};

## Page 21

            Class StringRep
class StringRep : public UCObject {
public:
    StringRep(const char *);
    ~StringRep();
    StringRep(const StringRep&);
    int length() const{ return strlen(m_pChars); }
    int equal(const StringRep&) const;
private:
    char *m_pChars;
};

## Page 22

StringRep implementation
StringRep::StringRep(const char *s) {
    if (s) {
        int len = strlen(s) + 1;
        m_pChars = new char[len];
        strcpy(m_pChars , s);
    } else {
        m_pChars = new char[1];
        *m_pChars = '\0';
    }
}
StringRep::~StringRep() {
    delete [] m_pChars ;
}

## Page 23

 StringRep implementation
StringRep::StringRep(const StringRep& sr) {
  int len = sr.length();
  m_pChars = new char[len + 1];
  strcpy(m_pChars , sr.m_pChars );
}

int StringRep::equal(const StringRep& sp)
const {
  return (strcmp(m_pChars, sp.m_pChars) == 0);
}

## Page 24

    String implementation
String::String(const char *s)
    : m_rep(new StringRep(s)) {}

String::~String() {}

// Again, note constructor for rep in list.
String::String(const String& s) : m_rep(s.m_rep) {}

String&
String::operator=(const String& s) {
    m_rep = s.m_rep; // let smart pointer do work!
    return *this;
}

In such case, the implementation of ctor and operator= can be igno

## Page 25

   String implementation
int
String::operator==(const String& s) const {
    // overloaded -> forwards to StringRep
    return m_rep->equal(*s.m_rep); // smart ptr *
}

int
String::length() const {
    return m_rep->length();
}


Dispatch to the real meat StringRep…

## Page 26

                 Critique
• UCPointer maintains reference counts

## Page 27

                  Critique
• UCPointer maintains reference counts
• UCObject hides the details of the count, String
  is very clean

## Page 28

                  Critique
• UCPointer maintains reference counts
• UCObject hides the details of the count, String
  is very clean
• StringRep deals only with string storage and
  manipulation

## Page 29

                  Critique
• UCPointer maintains reference counts
• UCObject hides the details of the count, String
  is very clean
• StringRep deals only with string storage and
  manipulation
• UCObject and UCPointer are reusable

## Page 30

                  Critique
• UCPointer maintains reference counts
• UCObject hides the details of the count, String
  is very clean
• StringRep deals only with string storage and
  manipulation
• UCObject and UCPointer are reusable
• Slower than raw pointers

## Page 31

                  Critique
• UCPointer maintains reference counts
• UCObject hides the details of the count, String
  is very clean
• StringRep deals only with string storage and
  manipulation
• UCObject and UCPointer are reusable
• Slower than raw pointers
• Invasive design
  •see std::shared_ptr for non-intrusive design
