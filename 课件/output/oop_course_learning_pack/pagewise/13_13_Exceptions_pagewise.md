# Lecture 13: 13 Exceptions

- Source: `13 Exceptions.pdf`
- Pages: 60
- Rendered page images: 60
- Contact sheet: [open](../contact_sheets/13_13_Exceptions_contact.jpg)
- Raw extracted text: [open](../raw_texts/13-13 Exceptions.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 13 page 1](../page_images/13_13_Exceptions/page_001.png)

Extracted text:

```text
Exceptions
Object-Oriented Programming with C++
```

## Page 2

![Lecture 13 page 2](../page_images/13_13_Exceptions/page_002.png)

Extracted text:

```text
Run-time error

•The basic philosophy of C++ is that "badly
  formed code will not be run."
•There's always something happens in run-time.
•It is very important to deal with all possible
  situation in the future running.
```

## Page 3

![Lecture 13 page 3](../page_images/13_13_Exceptions/page_003.png)

Extracted text:

```text
Read a file

open the file;
determine its size;
allocate that much memory;
read the file into memory;
close the file;
```

## Page 4

![Lecture 13 page 4](../page_images/13_13_Exceptions/page_004.png)

Extracted text:

```text
errorCodeType readFile {
       initialize errorCode = 0;
       open the file;
       if ( theFilesOpen ) {
                 determine its size;
                 if ( gotTheFileLength ) {
                          allocate that much memory;
                          if ( gotEnoughMemory ) {
                                   read the file into memory;
                                   if ( readFailed ) {
                                            errorCode = -1;
                                   }
                          } else {
                                   errorCode = -2;
                          }
                 } else {
                          errorCode = -3;
                 }
                 close the file;
                 if ( theFILEDidntClose && errorCode == 0 ) {
                          errorCode = -4;
                 }
       } else {
                 errorCode = -5;
       }
       return errorCode;
}
```

## Page 5

![Lecture 13 page 5](../page_images/13_13_Exceptions/page_005.png)

Extracted text:

```text
Working with exception
    try {
           open the file;
           determine its size;
           allocate that much memory;
           read the file into memory;
           close the file;
    } catch ( fileOpenFailed ) {
           doSomething;
    } catch ( sizeDeterminationFailed ) {
           doSomething;
    } catch ( memoryAllocationFailed ) {
           doSomething;
    } catch ( readFailed ) {
           doSomething;
    } catch ( fileCloseFailed ) {
           doSomething;
    }
```

## Page 6

![Lecture 13 page 6](../page_images/13_13_Exceptions/page_006.png)

Extracted text:

```text
Why exception?

• The significant benefit of exceptions is that
  they clean up error handling code.
• It separates the code that describes what you
  want to do from the code that is executed.
```

## Page 7

![Lecture 13 page 7](../page_images/13_13_Exceptions/page_007.png)

Extracted text:

```text
Example: Vector
template <class T> class Vector {
private:
    T* m_elements;
    int m_size;
public:
    Vector (int size = 0) : m_size(size)
    { ... }
    ~Vector () { delete [] m_elements; }
    void length(int);
    int length() { return m_size; }
    T& operator[](int);
};
```

## Page 8

![Lecture 13 page 8](../page_images/13_13_Exceptions/page_008.png)

Extracted text:

```text
Problem
template <class T>
T& Vector<T>::operator[](int idx) {
```

## Page 9

![Lecture 13 page 9](../page_images/13_13_Exceptions/page_009.png)

Extracted text:

```text
Problem
template <class T>
T& Vector<T>::operator[](int idx) {


   What should the [] operator do if the index is
                 not valid?
```

## Page 10

![Lecture 13 page 10](../page_images/13_13_Exceptions/page_010.png)

Extracted text:

```text
Problem
template <class T>
T& Vector<T>::operator[](int idx) {


   What should the [] operator do if the index is
                 not valid?

1.) Return random memory object
  return m_elements[idx];
```

## Page 11

![Lecture 13 page 11](../page_images/13_13_Exceptions/page_011.png)

Extracted text:

```text
More choices
2.) Return a special error value
if (idx < 0 || idx >= m_size) {
  T error_marker("some magic value");
  return error_marker;
}
return m_elements[idx];

This throws the baby out with the bath water!
x = v[2] + v[4]; // not safe code!
```

## Page 12

![Lecture 13 page 12](../page_images/13_13_Exceptions/page_012.png)

Extracted text:

```text
More choices …
```

## Page 13

![Lecture 13 page 13](../page_images/13_13_Exceptions/page_013.png)

Extracted text:

```text
More choices …
3.) Just die!
if (idx < 0 || idx >= m_size){
  exit(22);
}
return m_elements[idx];

4.) Die gracefully (with autopsy!)
assert(idx >= 0 && idx < m_size);
return m_elements[idx];
```

## Page 14

![Lecture 13 page 14](../page_images/13_13_Exceptions/page_014.png)

Extracted text:

```text
When to use exceptions
• Many times, you don't know what should be
  done
• If you do anything you’ll be wrong


• Solution: expose the problem


 Make your caller (or its caller ...) responsible
```

## Page 15

![Lecture 13 page 15](../page_images/13_13_Exceptions/page_015.png)

Extracted text:

```text
How to raise an exception
template <class T>
T& Vector<T>::operator[](int idx) {
    if (idx < 0 || idx >= m_size) {
        // throw is a keyword
        // exception is raised at this point
        throw <<something>>;
    }
    return m_elements[idx];
}
```

## Page 16

![Lecture 13 page 16](../page_images/13_13_Exceptions/page_016.png)

Extracted text:

```text
What do you throw?
// What do you have? Data!
// Define a class to represent the error
class VectorIndexError {
public:
    VectorIndexError(int v) : m_badValue(v) { }
    ~VectorIndexError() { }
    void diagnostic() {
        cerr << "index " << m_ badValue
        << "out of range!"; }
private:
    int m_badValue;
};
```

## Page 17

![Lecture 13 page 17](../page_images/13_13_Exceptions/page_017.png)

Extracted text:

```text
How to raise an exception
template <class T>
T& Vector<T>::operator[](int idx){
  if (idx < 0 || idx >= m_size) {
    throw VectorIndexError(idx);
  }
  return m_elements[idx];
}
```

## Page 18

![Lecture 13 page 18](../page_images/13_13_Exceptions/page_018.png)

Extracted text:

```text
What about your caller?
Case 1) Doesn’t care
 –Code never even suspects a problem
  int func() {
      Vector<int> v(12);
      v[3] = 5;
      int i = v[42]; // out of range
      // control never gets here!
      return i * 5;
  }
```

## Page 19

![Lecture 13 page 19](../page_images/13_13_Exceptions/page_019.png)

Extracted text:

```text
What about your caller?
Case 2) Cares deeply
void outer() {
    try {
        func();
        func2();
    } catch (VectorIndexError& e) {
        e.diagnostic();
        // This exception does not propagate
    }
    cout << "Control is here after exception";
}
```

## Page 20

![Lecture 13 page 20](../page_images/13_13_Exceptions/page_020.png)

Extracted text:

```text
What about your caller?
Case 3) Mildly interested

  void outer2() {
    String err("exception caught");
    try {
        func();
    } catch (VectorIndexError) {
      cout << err;
      throw; // propagate the exception
    }
  }
```

## Page 21

![Lecture 13 page 21](../page_images/13_13_Exceptions/page_021.png)

Extracted text:

```text
What about your caller?
Case 4) Doesn’t care about the particulars

  void outer3() {
    try {
        outer2();
    } catch (...) {
      // ... catches ALL exceptions!
      cout << "The exception stops here!";
    }
  }
```

## Page 22

![Lecture 13 page 22](../page_images/13_13_Exceptions/page_022.png)

Extracted text:

```text
What happened?
```

## Page 23

![Lecture 13 page 23](../page_images/13_13_Exceptions/page_023.png)

Extracted text:

```text
Review
• Throw statement raises the exception
  – Control propagates back to first handler for that
    exception
  – Propagation follows the call chain
  – Objects on stack are properly destroyed
•throw exp;
  – throws value for matching
•throw;
  – re-raises the exception being handled
  – valid only within a handler
```

## Page 24

![Lecture 13 page 24](../page_images/13_13_Exceptions/page_024.png)

Extracted text:

```text
Try blocks
• Try block
   try { ... }
   catch ...
   catch ...
• Establishes any number of handlers
• Not needed if you don’t use any handlers
• Shows where you expect to handle exceptions
• Costs cycles
```

## Page 25

![Lecture 13 page 25](../page_images/13_13_Exceptions/page_025.png)

Extracted text:

```text
Exception handlers
•Select exception by type
•Can re-raise exceptions
•Two forms
   catch (SomeType v) { // handler code
   }
   catch (...) { // handler code
   }

•Take a single argument (like a formal parameter)
```

## Page 26

![Lecture 13 page 26](../page_images/13_13_Exceptions/page_026.png)

Extracted text:

```text
Selecting a handler
• Can have any number of handlers
• Handlers are checked in order of appearance

   1. Check for exact match
   2. Apply base class conversions
       Reference and pointer types, only
   3. Catch-all handler (...)


   Inheritance can be used to structure exceptions
```

## Page 27

![Lecture 13 page 27](../page_images/13_13_Exceptions/page_027.png)

Extracted text:

```text
Example: using inheritance
• Hierarchy of exception types
class MathErr {
   ...
   virtual void diagnostic();
};

class OverflowErr : public MathErr { ... }

class UnderflowErr : public MathErr { ... }

class ZeroDivideErr : public MathErr { ... }
```

## Page 28

![Lecture 13 page 28](../page_images/13_13_Exceptions/page_028.png)

Extracted text:

```text
Using handlers
try {
   // code to exercise math options
   throw UnderFlowErr();
} catch (ZeroDivideErr& e) {
   // handle zero divide case
} catch (MathErr& e) {
   // handle other math errors
} catch (UnderFlowErr& e) {
   // handle underflow errors
} catch (...) {
   // any other exceptions
}
```

## Page 29

![Lecture 13 page 29](../page_images/13_13_Exceptions/page_029.png)

Extracted text:

```text
Standard library exceptions
                  (Synopsis)
```

## Page 30

![Lecture 13 page 30](../page_images/13_13_Exceptions/page_030.png)

Extracted text:

```text
Exceptions and new
•new does NOT returned 0 on failure
•new raises a bad_alloc() exception
 void func() {
     try {
         while(1) {
             char *p = new char[10000];
         }
     } catch (std::bad_alloc& e) {
         // ...
     }
 }
```

## Page 31

![Lecture 13 page 31](../page_images/13_13_Exceptions/page_031.png)

Extracted text:

```text
Exception specifications
• Specifies whether a function could throw exceptions.
• Part of function type, but not part of signature.
   void abc(int a) noexcept {
     ...
   }
• May not be checked at compile time, but utilized by
  the compiler to enable certain optimizations.
• At run time,
 –if an exception is thrown out, the std::terminate is
 called.
```

## Page 32

![Lecture 13 page 32](../page_images/13_13_Exceptions/page_032.png)

Extracted text:

```text
Design considerations
• Exceptions should indicate errors
• Here is an inappropriate use:
   try {
       for (;;) {
           p = list.next()
       // ...
   } catch (List::end_of_list) {
       // handle end of list here
   }
```

## Page 33

![Lecture 13 page 33](../page_images/13_13_Exceptions/page_033.png)

Extracted text:

```text
Design considerations…
•Don’t use exceptions in place of good design
 void func() {
   File f;
   if (f.open("somefile")) {
     try {
       // work with f
     } catch (...) {
        f.close()
     }
   }
 }
•This is a good place to use the destructor
```

## Page 34

![Lecture 13 page 34](../page_images/13_13_Exceptions/page_034.png)

Extracted text:

```text
void func() {
  File f("some file");
  // assume destructor closes f
  // will still be closed if exception
  // is raised!
  if (f.ok()) {
  }
}
```

## Page 35

![Lecture 13 page 35](../page_images/13_13_Exceptions/page_035.png)

Extracted text:

```text
Summary
```

## Page 36

![Lecture 13 page 36](../page_images/13_13_Exceptions/page_036.png)

Extracted text:

```text
Summary
• Error recovery is a hard design problem
• All subsystems need help from their clients to
  handle exceptional cases
```

## Page 37

![Lecture 13 page 37](../page_images/13_13_Exceptions/page_037.png)

Extracted text:

```text
Summary
• Error recovery is a hard design problem
• All subsystems need help from their clients to
  handle exceptional cases
• Exceptions provide the mechanism
  –Propagated dynamically
  –Objects on stack destroyed properly
```

## Page 38

![Lecture 13 page 38](../page_images/13_13_Exceptions/page_038.png)

Extracted text:

```text
More exceptions
• Exceptions and constructors
• Exceptions and destructors
• Design and usage with exceptions
• Handlers
```

## Page 39

![Lecture 13 page 39](../page_images/13_13_Exceptions/page_039.png)

Extracted text:

```text
Failure in constructors
• No return value is possible
• Use an “uninitialized flag”
• Defer work to an init() function

Better: Throw an exception
```

## Page 40

![Lecture 13 page 40](../page_images/13_13_Exceptions/page_040.png)

Extracted text:

```text
Failure in constructors…
If your constructor throws an exception:
• Dtors for the object won’t be called.
• Manually clean up allocated resources before
   throwing, otherwise memory leak happens.




  demo
```

## Page 41

![Lecture 13 page 41](../page_images/13_13_Exceptions/page_041.png)

Extracted text:

```text
Two stages construction
• Do normal work in ctor
  –Initialize all member objects
  –Initialize all primitive members
  –Initialize all pointers to 0
  –NEVER request any resource
    •File
    •Network connection
    •Memory
• Do additional initialization work in Init()
```

## Page 42

![Lecture 13 page 42](../page_images/13_13_Exceptions/page_042.png)

Extracted text:

```text
Using smart pointers
•std::unique_ptr
•std::shared_ptr
•…

• The destructor will delete the native pointer
  when it dies.
```

## Page 43

![Lecture 13 page 43](../page_images/13_13_Exceptions/page_043.png)

Extracted text:

```text
Exceptions and destructors
Destructors are called when:
•Normal call ended: object exits from scope
•Exceptions throwed: “stack unwinding” invokes
dtors on objects as they exit from scope.

What happens if an exception is thrown in a
destructor?
```

## Page 44

![Lecture 13 page 44](../page_images/13_13_Exceptions/page_044.png)

Extracted text:

```text
Exceptions and destructors…
Throwing an exception in a destructor that is itself
being called as the result of an exception will invoke
std::terminate().
• Allowing exceptions to escape from destructors
  should be avoided, never throw it!
```

## Page 45

![Lecture 13 page 45](../page_images/13_13_Exceptions/page_045.png)

Extracted text:

```text
Programming with exceptions
Prefer catching exceptions by reference
• throwing/catching by value involves slicing:

   struct X {};
   struct Y : public X {};
   try {
       throw Y();
   } catch(X x) {
       // was it X or Y?
   }
```

## Page 46

![Lecture 13 page 46](../page_images/13_13_Exceptions/page_046.png)

Extracted text:

```text
Programming with exceptions…
• throwing/catching by pointer introduces
  coupling between normal and handler code:
  try {
      throw new Y();
  } catch(Y* p) {
      // whoops, forgot to delete..
  }
```

## Page 47

![Lecture 13 page 47](../page_images/13_13_Exceptions/page_047.png)

Extracted text:

```text
Catch exceptions by reference:
struct B {
    virtual void print() { /* … */ }
};
struct D : public B { /* … */ };

try {
    throw D("D error");
}
catch(B& b) {
    b.print(); // print D's error.
}
```

## Page 48

![Lecture 13 page 48](../page_images/13_13_Exceptions/page_048.png)

Extracted text:

```text
Exceptions wrap-up
```

## Page 49

![Lecture 13 page 49](../page_images/13_13_Exceptions/page_049.png)

Extracted text:

```text
Exceptions wrap-up
• Develop an error-handling strategy early in
  design.
```

## Page 50

![Lecture 13 page 50](../page_images/13_13_Exceptions/page_050.png)

Extracted text:

```text
Exceptions wrap-up
• Develop an error-handling strategy early in
  design.
• Avoid over-use of try/catch blocks. Use objects
  to acquire/release resources.
```

## Page 51

![Lecture 13 page 51](../page_images/13_13_Exceptions/page_051.png)

Extracted text:

```text
Exceptions wrap-up
• Develop an error-handling strategy early in
  design.
• Avoid over-use of try/catch blocks. Use objects
  to acquire/release resources.
• Don’t use exceptions where local control
  structures would suffice.
```

## Page 52

![Lecture 13 page 52](../page_images/13_13_Exceptions/page_052.png)

Extracted text:

```text
Exceptions wrap-up
• Develop an error-handling strategy early in
  design.
• Avoid over-use of try/catch blocks. Use objects
  to acquire/release resources.
• Don’t use exceptions where local control
  structures would suffice.
• Not every function can handle every error.
```

## Page 53

![Lecture 13 page 53](../page_images/13_13_Exceptions/page_053.png)

Extracted text:

```text
Exceptions wrap-up…
```

## Page 54

![Lecture 13 page 54](../page_images/13_13_Exceptions/page_054.png)

Extracted text:

```text
Exceptions wrap-up…
• Use exception-specifications for major
  interfaces.
```

## Page 55

![Lecture 13 page 55](../page_images/13_13_Exceptions/page_055.png)

Extracted text:

```text
Exceptions wrap-up…
• Use exception-specifications for major
  interfaces.
• Library code should not decide to terminate
  a program. Throw exceptions and let the
  caller decide.
```

## Page 56

![Lecture 13 page 56](../page_images/13_13_Exceptions/page_056.png)

Extracted text:

```text
Uncaught exceptions
• If an exception is thrown but not caught
  std::terminate() will be called.
• The std::terminate() can also be
  intercepted.
 void my_terminate() {
     /* … */
 }
 set_terminate(my_terminate);
```

## Page 57

![Lecture 13 page 57](../page_images/13_13_Exceptions/page_057.png)

Extracted text:

```text
Write exception-safe code
```

## Page 58

![Lecture 13 page 58](../page_images/13_13_Exceptions/page_058.png)

Extracted text:

```text
Write exception-safe code
class BankAccount {
  // …

 void withdrawMoney(int amount) {
   // …

     reduceBalance(amount);
     prepareCash();
     releaseCash();

     // …
 }

  // …
};
```

## Page 59

![Lecture 13 page 59](../page_images/13_13_Exceptions/page_059.png)

Extracted text:

```text
Write exception-safe code
class BankAccount {
  // …

 void withdrawMoney(int amount) {
   // …

     reduceBalance(amount);
     prepareCash();        Throws an exception
     releaseCash();

     // …
 }

  // …
};
```

## Page 60

![Lecture 13 page 60](../page_images/13_13_Exceptions/page_060.png)

Extracted text:

```text
Write exception-safe code
class BankAccount {
  // …

 void withdrawMoney(int amount) {
   // …

     reduceBalance(amount);       Balance already reduced…
     prepareCash();        Throws an exception
     releaseCash();

     // …
 }

  // …
};
```
