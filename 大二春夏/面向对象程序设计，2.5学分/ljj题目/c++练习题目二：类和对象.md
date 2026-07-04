# c++练习题目二：类和对象

## Questions

### Constructors and Destructors

**2-1**. The copy constructors can be used to ________
- A. Copy an object so that it can be passed to another primitive type variable
- B. Copy an object for type casting
- C. Copy an object so that it can be passed to a function
- D. Copy an object so that it can be passed to a class

**2-2**. Which constructor will be called from the object obj2 in the following C++ program?



```cpp
class A
{
    int i;
    A()
    {
        i=0;
    }
    A(int x)
    {
        i=x+1;
    }
    A(int y, int x)
    {
        i=x+y;
    }
};
```



A obj1(10);

A obj2(10,20);

A obj3;
- A. A(int y, int x)
- B. A(int y; int x)
- C. A(int y)
- D. A(int x)

**2-3**. Which among the following represents correct constructor?
- A. –classname()
- B. classname()
- C. ()classname
- D. ~classname()

**2-12**. What is the syntax of copy constructor?
- A. classname (classname &obj){ /constructor definition/ }
- B. classname (cont classname obj){ /constructor definition/ }
- C. classname (cont classname &obj){ /constructor definition/ }
- D. classname (cont &obj){ /constructor definition/ }

**2-13**. Object being passed to a copy constructor ___________
- A. Must be passed by reference
- B. Must be passed by value
- C. Must be passed with integer type
- D. Must not be mentioned in parameter list

**2-14**. Out of memory error is given when the object _____________ to the copy constructor.
- A. Is passed with & symbol
- B. Is passed by reference
- C. Is passed as <classname &obj>
- D. Is not passed by reference

**2-15**. Copy constructor will be called whenever the compiler __________
- A. Generates implicit code
- B. Generates member function calls
- C. Generates temporary object
- D. Generates object operations

**2-17**. Can a copy constructor be made private?
- A. Yes, always
- B. Yes, if no other constructor is defined
- C. No, never
- D. No, private members can’t be accessed

**2-18**. The arguments to a copy constructor _____________
- A. Must be const
- B. Must not be cosnt
- C. Must be integer type
- D. Must be static

**2-19**. Which among the following best describes constructor overloading?
- A. Defining one constructor in each class of a program
- B. Defining more than one constructor in single class
- C. Defining more than one constructor in single class with different signature
- D. Defining destructor with each constructor

**2-20**. Does constructor overloading include different return types for constructors to be overloaded?
- A. Yes, if return types are different, signature becomes different
- B. Yes, because return types can differentiate two functions
- C. No, return type can’t differentiate two functions
- D. No, constructors doesn’t have any return type

**2-21**. Destructor calls ________________ (C++)
- A. Are only implicit
- B. Are only explicit
- C. Can be implicit or explicit
- D. Are made at end of program only

**2-22**. Number of destructors called are ____________
- A. Always equal to number of constructors called
- B. Always less than the number of constructors called
- C. Always greater than the number of constructors called
- D. Always less than or equal to number of constructors

**2-24**. Which among the following is true for destructors?
- A. Destructors can be overloaded
- B. Destructors can be define more than one time
- C. Destructors can’t be overloaded
- D. Destructors are overloaded in derived classes

**2-25**. Which among the following describes a destructor?
- A. A special function that is called to free the resources, acquired by the object
- B. A special function that is called to delete the class
- C. A special function that is called anytime to delete an object
- D. A special function that is called to delete all the objects of a class

**2-26**. When a destructor is called?
- A. After the end of object life
- B. Anytime in between object’s lifespan
- C. At end of whole program
- D. Just before the end of object life

**2-27**. When is the destructor of a global object called?
- A. Just before end of program
- B. Just after end of program
- C. With the end of program
- D. Anytime when object is not needed

**2-28**. How the constructors and destructors can be differentiated?
- A. Destructor have a return type but constructor doesn’t
- B. Destructors can’t be defined by the programmer, but constructors can be defined
- C. Destructors are preceded with a tilde (~) symbol, and constructor doesn’t
- D. Destructors are same as constructors in syntax

**2-29**. Global destructors execute in ___________ order after main function is terminated.
- A. Sequential
- B. Random
- C. Reverse
- D. Depending on priority

**2-30**. When is it advised to have user defined destructor?
- A. When class contains some pointer to memory allocated in class
- B. When a class contains static variables
- C. When a class contains static functions
- D. When a class is inheriting another class only

**2-105**. Why temporary object is not created in return by reference?
- A. Because compiler can’t create temporary objects
- B. Because the temporary object is created within the function
- C. Because return by reference just make the objects points to values memory location
- D. Because return by reference just make the object point to null

**2-111**. In copy constructor definition, if non const values are accepted only ________
- A. Only const objects will be accepted
- B. Only non – const objects are accepted
- C. Only const members will not get copied
- D. Compiler generates an error

**2-138**. Which among the following is true for constructors overloading?
- A. Constructors can’t be overloaded
- B. Constructors can be overloaded using different signatures
- C. Constructors can be overloaded with same signatures
- D. Constructors can be overloaded with different return types

**2-139**. If a constructors should be capable of creating objects without argument and with arguments, which is a good alternative for this purpose?
- A. Use zero argument constructor
- B. Use constructor with one parameter
- C. Use constructor with all default arguments
- D. Use default constructor

**2-141**. Which among the following can be used in place of default constructor?
- A. constructorName(int x, int y=0)
- B. constructorName(int x=0, int y=0)
- C. constructorName(int x=0, int y)
- D. constructorName(int x, int y)

**2-142**. If the constructors are overloaded by using the default arguments, which problem may arise?
- A. The constructors might have all the same arguments except the default arguments
- B. The constructors might have same return type
- C. The constructors might have same number of arguments
- D. The constructors can’t be overloaded with respect to default arguments

**2-144**. Which constructor among the following will be called if a call is made like className(5,’a’);?
- A. className(int x=5,char c=’a’);
- B. int className(int x, char c, char d);
- C. className(int x, char c, int y);
- D. char className(char c,int x);

**2-145**. Which constructor definition will produce a compile time error?
- A. className(int x=0);
- B. className(char c);
- C. className(int x=0,char c);
- D. className(char c,int x=0);

**2-146**. If there is a constructor with all the default arguments and arguments are not passed then _________________
- A. The default values given will not be used
- B. Then all the null values will be used
- C. Then all the default values given will be used
- D. Then compiler will produce an error

**2-147**. Which is the correct statement for default constructors?
- A. The constructors with all the default arguments
- B. The constructors with all the null and zero values
- C. The constructors which can’t be defined by programmer
- D. The constructors with zero arguments

**2-148**. Which is a good alternative instead of having one zero argument constructor and one single argument constructor with default argument?
- A. No constructor defined
- B. One default value constructor
- C. Defining the default constructor
- D. Using one constructor with two arguments

**2-151**. In C++, if new operator is used, when is the constructor called?
- A. Before the allocation of memory
- B. After the allocation of memory
- C. Constructor is called to allocate memory
- D. Depends on code

**2-162**. When delete operator is used ___________________ (If object has a destructor)
- A. Object destructor is called after deallocation
- B. Object destructor is called before deallocation
- C. Object destructor is not used
- D. Object destructor can be called anytime during destruction

### Classes and Objects

**2-4**. What happens when an object is passed by reference?
- A. Destructor is called at end of function
- B. Destructor is called when called explicitly
- C. Destructor is not called
- D. Destructor is called when function is out of scope

**2-5**. Which of the following is not a property of an object?
- A. Properties
- B. Names
- C. Identity
- D. Attributes

**2-6**. What happens if non static members are used in static member function?
- A. Executes fine
- B. Compile time error
- C. Executes if that member function is not used
- D. Runtime error

**2-7**. What is friend member functions in C++?
- A. Non-member functions which have access to all the members (including private) of a class
- B. Member function which doesn’t have access to private members
- C. Member function which can modify any data of a class
- D. Member function which can access all the members of a class

**2-9**. How to access the private member function of a class?
- A. Using class address
- B. Using object of class
- C. Using object pointer
- D. Using address of member function

**2-10**. If data members are private, what can we do to access them from the class object?
- A. Private data members can never be accessed from outside the class
- B. Create public member functions to access those data members
- C. Create private member functions to access those data members
- D. Create protected member functions to access those data members

**2-11**. If a class implements some dynamic memory allocations and pointers then _____________
- A. Copy constructor must be defined
- B. Copy constructor must not be defined
- C. Copy constructor can’t be defined
- D. Copy constructor will not be used

**2-32**. If a class doesn’t have public members, then________
- A. None of its members will be able to get inherited
- B. None of its instance creation will be allowed
- C. None of its member function can be called outside the class
- D. None of its data members will be able to get initial value

**2-33**. What is the term used to indicate the variable and constants of a class?
- A. Data members
- B. Variables of class
- C. Data characters
- D. Constants

**2-34**. Data members ________________ (C++)
- A. Can be initialized with declaration in classes
- B. Can be initialized only with help of constructors
- C. Can be initialized either in declaration or by constructor
- D. Can’t be initialized

**2-35**. Which among the following is true for data members?
- A. Private data members can be initialized with declaration in class
- B. Static members are initialized in constructors
- C. Protected data members can be initialized in class directly
- D. Static data members are defined outside class, not in constructor

**2-36**. What should be done for data member to be of user defined structure type?
- A. The structure must have been defined before class.
- B. The structure must have been defined after the class definition
- C. The structure must be predefined
- D. The structure type data members can’t be used

**2-37**. To create a pointer to a private data member of a class, outside the class, which among the following is correct?
- A. Return the address of the private data member using a member function
- B. Access the private member using a pointer outside class
- C. Declare the member as pointer inside the class
- D. Not possible to create pointer to a private member

**2-39**. The static member functions can only use ________
- A. Static data members
- B. Private data members
- C. Protected data members
- D. Constant data members

**2-41**. All the member functions of local classes are __________ by default.
- A. Static
- B. Inline
- C. Abstract
- D. Virtual

**2-42**. Can two different functions have local class with same name?
- A. Yes, since local
- B. No, names must be different
- C. No, scope doesn’t work here
- D. No, ambiguity arises

**2-43**. What is the scope of local class?
- A. Within the class only
- B. Within the function
- C. Within the program
- D. One time creation and live till end of program

**2-44**. Can a function, other than the enclosing function of local class, access the class members?
- A. Yes, using object
- B. Yes, using direct call
- C. Yes, using pointer
- D. No, can’t access

**2-45**. Which among the following is the main advantage of using local classes?
- A. Make program more efficient
- B. Makes program execution faster
- C. Helps to add extra functionality to a function
- D. Helps to add more members to a function

**2-46**. Which among the following best describes a nested class?
- A. Class inside a class
- B. Class inside a function
- C. Class inside a package
- D. Class inside a structure

**2-49**. Static nested classes doesn’t have access to _________________ from enclosing class.
- A. Private members
- B. Protected members
- C. Public members
- D. Any other members

**2-50**. Which among the following is the correct advantage/disadvantage of nested classes?
- A. Makes the code more complex
- B. Makes the code unreadable
- C. Makes the code efficient and readable
- D. Makes the code multithreaded

**2-51**. Objects can be used _____________________
- A. To access any member of a class
- B. To access only public members of a class
- C. To access only protected members of a class
- D. To access only private members of a class

**2-52**. Which among the following is not a use of object?
- A. Defining a member function
- B. Accessing data members
- C. Creating instance of a class
- D. Using class members

**2-53**. Which object can be used to access the standard input?
- A. System.inner
- B. cin
- C. System.stdin
- D. console.input

**2-54**. A single object can be used __________________
- A. As only two class types at a time
- B. As only three class types at a time
- C. As only one class type at a time
- D. As of as many class types as required

**2-55**. If same object name is given to different objects of different class then _____________
- A. Its compile time error
- B. Its runtime error
- C. It’s not an error
- D. Program suns smooth

**2-57**. If a class have two data members and two functions to add those two numbers and to subtract them, which among the following is most efficient if the programmer wants to implement multiplication too?
- A. Define a public function which multiplies two numbers
- B. Define a public function that returns values of two data members
- C. Define a private function which multiplies two numbers
- D. Define a private function that returns values of two data members

**2-58**. Which among the following is a feature of class?
- A. Object orientation
- B. Procedure orientation
- C. Both object and procedure orientation
- D. Neither object nor procedure orientation

**2-59**. In which case the classes can be used to make the more efficient program?
- A. To define a function that is called frequently in a program
- B. To structure data that is most similar
- C. To group the most similar data and operations
- D. To define a blueprint that shows memory location of data

**2-60**. Why do classes use accessor methods?
- A. To make public data accessible to client
- B. To make public data private to client
- C. To make private data public for whole program
- D. To make private data accessible to the client

**2-61**. What are the constant member functions?
- A. Functions which doesn’t change value of calling object
- B. Functions which doesn’t change value of any object inside definition
- C. Functions which doesn’t allow modification of any object of class
- D. Functions which doesn’t allow modification of argument objects

**2-62**. Which is private member functions access scope?
- A. Member functions which can only be used within the class
- B. Member functions which can used outside the class
- C. Member functions which are accessible in derived class
- D. Member functions which can’t be accessed inside the class

**2-64**. What are public member functions?
- A. Functions accessible outside the class but not in derived class
- B. Functions accessible outside the class directly
- C. Functions accessible everywhere using object of class
- D. Functions that can’t be accessed outside the class

**2-66**. If a class have a public member function and is called directly in the main function then ___________________________
- A. Undeclared function error will be produced
- B. Out of memory error is given
- C. Program gives warning only
- D. Program shut down the computer

**2-67**. All the public member functions ___________________
- A. Can’t access the private members of a class
- B. Can’t access the protected members of a class
- C. Can access only public members of a class
- D. Can access all the member of its class

**2-69**. Any changes made to static data member from one member function _____________
- A. Is reflected to only the corresponding object
- B. Is reflected to all the variables in a program
- C. Is reflected to all the objects of that class
- D. Is constant to that function only

**2-70**. Which is the correct syntax for declaring static data member?
- A. static mamberName dataType;
- B. dataType static memberName;
- C. memberName static dataType;
- D. static dataType memberName;

**2-71**. The static data member ______________________
- A. Must be defined inside the class
- B. Must be defined outside the class
- C. Must be defined in main function
- D. Must be defined using constructor

**2-72**. The syntax for defining the static data members is __________
- A. dataType className :: memberName = value;
- B. dataType className : memberName = value;
- C. dataType className . memberName = value;
- D. dataType className -> memberName =value;

**2-74**. The static data member __________________________
- A. Can be accessed directly
- B. Can be accessed with any public class name
- C. Can be accessed with dot operator
- D. Can be accessed using class name if not using static member function

**2-75**. Which among the following is the correct syntax to access static data member without using member function?
- A. className -> staticDataMember;
- B. className :: staticDataMember;
- C. className : staticDataMember;
- D. className . staticDataMember;

**2-77**. Whenever any static data member is declared in a class ______________________
- A. Only one copy of the data is created
- B. New copy for each object is created
- C. New memory location is allocated with each object
- D. Only one object uses the static data

**2-78**. If object of class are created, then the static data members can be accessed ____________
- A. Using dot operator
- B. Using arrow operator
- C. Using colon
- D. Using dot or arrow operator

**2-82**. The static member functions __________________
- A. Have access to all the members of a class
- B. Have access to only constant members of a class
- C. Have access to only the static members of a class
- D. Have direct access to all other class members also

**2-83**. The static member functions ____________________
- A. Can be called using class name
- B. Can be called using program name
- C. Can be called directly
- D. Can’t be called outside the function

**2-85**. Which among the following is not applicable for the static member functions?
- A. Variable pointers
- B. void pointers
- C. this pointer
- D. Function pointers

**2-89**. The static member functions _______________
- A. Can’t be declared const
- B. Can’t be declared volatile
- C. Can’t be declared const or volatile
- D. Can’t be declared const, volatile or const volatile

**2-91**. What exactly is passed when an object is passed by reference?
- A. The original object name
- B. The original object class name
- C. The exact address of the object in memory
- D. The exact address of data members

**2-95**. In which of the following way(s) can the object be returned from a function?
- A. Can only be returned by value
- B. Can only be returned by reference
- C. Can be returned either by value or reference
- D. Can neither be returned by value nor by reference

**2-96**. Whenever an object is returned by value ____________________
- A. A temporary object is created
- B. Temporary object is not created
- C. Temporary object may or may not be created
- D. New permanent object is created

**2-97**. Which is the correct syntax for returning an object by value?
- A. void functionName ( ){ }
- B. object functionName( ) { }
- C. class object functionName( ) { }
- D. ClassName functionName ( ){ }

**2-98**. Which is the correct syntax for defining a function which passes an object by reference?
- A. className& functionName ( )
- B. className* functionName( )
- C. className-> functionName( )
- D. &className functionName()
View Answer

**2-99**. If an object is declared inside the function then ____________________ outside the function.
- A. It can be returned by reference
- B. It can’t be returned by reference
- C. It can be returned by address
- D. It can’t be returned at all

**2-100**. Which error will be produced if a local object is returned by reference outside a function?
- A. Out of memory error
- B. Run time error
- C. Compile time error
- D. No error

**2-101**. If object is passed by reference ____________________
- A. Temporary object is created
- B. Temporary object is created inside the function
- C. Temporary object is created for few seconds
- D. Temporary object is not created

**2-102**. Can we return an array of objects?
- A. Yes, always
- B. Yes, only if objects are having same values
- C. No, because objects contain many other values
- D. No, because objects are single entity

**2-104**. If an object is being returned by value then __________________________
- A. Its member values are made constant
- B. Its member values have to be copied individually
- C. Its member values are not used
- D. Its member values are copied using copy constructor

**2-106**. When value of an object is assigned to another object ________________
- A. It becomes invalid statement
- B. Its values gets copied into another object
- C. Its values gets address of the existing values
- D. The compiler doesn’t execute that statement

**2-113**. If more than one object refer to the same address, any changes made __________
- A. Can be made visible to specific objects
- B. Will be specific to one object only
- C. From any object will be visible in all
- D. Doesn’t changes the values of all objects

**2-114**. How to make more than one object refer to the same object?
- A. Initialize it to null
- B. Initialize the object with another at declaration
- C. Use constructor to create new object
- D. Assign the address directly

**2-116**. Assigning reference to an object _________________
- A. Will create another copy of the object
- B. Will create two different copies of the object
- C. Will not create any other copy of the object
- D. Will not refer to the object

**2-118**. How does compiler decide the intended object to be used, if more than one object are used?
- A. Using object name
- B. Using an integer pointer
- C. Using this pointer
- D. Using void pointer

**2-119**. What is the size of an object pointer?
- A. Equal to size of any usual pointer
- B. Equal to size of sum of all the members of object
- C. Equal to size of maximum sized member of object
- D. Equal to size of void

**2-120**. Which is the correct syntax to call a member function using pointer?
- A. pointer->function()
- B. pointer.function()
- C. pointer::function()
- D. pointer:function()

**2-121**. If a pointer to an object is created and the object gets deleted without using the pointer then __________
- A. It becomes void pointer
- B. It becomes dangling pointer
- C. It becomes null pointer
- D. It becomes zero pointer

**2-124**. Which is the pointer which denotes the object calling the member function?
- A. Variable pointer
- B. This pointer
- C. Null pointer
- D. Zero pointer

**2-127**. An object’s this pointer _____________________
- A. Isn’t part of class
- B. Isn’t part of program
- C. Isn’t part of compiler
- D. Isn’t part of object itself

**2-129**. Whenever non-static member functions are called _______________
- A. Address of the object is passed implicitly as an argument
- B. Address of the object is passed explicitly as an argument
- C. Address is specified globally so that the address is not used again
- D. Address is specified as return type of the function

**2-130**. Which is the correct interpretation of the member function call from an object, object.function(parameter);
- A. object.function(&this, parameter)
- B. object(&function,parameter)
- C. function(&object,&parameter)
- D. function(&object,parameter)

**2-131**. The address of the object _________________
- A. Can’t be accessed from inside the function
- B. Can’t be accessed in the program
- C. Is available inside the member function using this pointer
- D. Can be accessed using the object name inside the member function

**2-137**. Which is the correct syntax for declaring the type of this in a member function?
- A. classType [cv-qualifier-list] *const this;
- B. classType const[cv-qualifier-list] *this;
- C. [cv-qualifier-list]*const classType this;
- D. [cv-qualifier-list] classType *const this;

**2-160**. If delete is used to delete an object which was not allocated using new _______________
- A. Then out of memory error arises
- B. Then unreachable code error arises
- C. Then unpredictable errors may arise
- D. Then undefined variable error arises

**2-163**. If delete is applied to an object whose l-value is modifiable, then _______________ after the object is deleted.
- A. Its value is defined as null
- B. Its value is defined as void
- C. Its value is defined as 0
- D. Its value is undefined

**2-164**. Which is the correct syntax to delete an array of objects?
- A. delete [] objectName;
- B. delete * objectName;
- C. objectName[] delete;
- D. delete objectName[];

**2-168**. Inbuilt class __________________________
- A. Must be included before use
- B. Are not necessary to be included for use
- C. Are used by the compiler only
- D. Can be modified by programmer always

**2-170**. What is the InputStream class meant for?
- A. To handle all input streams
- B. To handle all output streams
- C. To handle all input and output streams
- D. To handle only input from file

**2-171**. What is an array of objects?
- A. An array of instances of class represented by single name
- B. An array of instances of class represented by more than one name
- C. An array of instances which have more than 2 instances
- D. An array of instances which have different types

**2-172**. Which among the following is a mandatory condition for array of objects?
- A. All the objects should be of different class
- B. All the objects should be of same program classes
- C. All the objects should be of same class
- D. All the objects should have different data

**2-173**. What is the type of elements of array of objects?
- A. Class
- B. Void
- C. String
- D. Null

**2-174**. Which definition best describes an object?
- A. Instance of a class
- B. Instance of itself
- C. Child of a class
- D. Overview of a class

**2-175**. The object can’t be __________
- A. Passed by reference
- B. Passed by value
- C. Passed by copy
- D. Passed as function

**2-177**. If a local class is defined in a function, which of the following is true for an object of that class?
- A. Object is accessible outside the function
- B. Object can be declared inside any other function
- C. Object can be used to call other class members
- D. Object can be used/accessed/declared locally in that function

**2-178**. Object declared in main() function _____________
- A. Can be used by any other function
- B. Can be used by main() function of any other program
- C. Can’t be used by any other function
- D. Can be accessed using scope resolution operator

**2-179**. When an object is returned___________
- A. A temporary object is created to return the value
- B. The same object used in function is used to return the value
- C. The Object can be returned without creation of temporary object
- D. Object are returned implicitly, we can’t say how it happens inside program

### Miscellaneous

**2-8**. Encapsulation and abstraction differ as ____________
- A. Hiding and hiding respectively
- B. Binding and Hiding respectively
- C. Hiding and Binding respectively
- D. Can be used any way

**2-16**. The deep copy is possible only with the help of __________
- A. Implicit copy constructor
- B. User defined copy constructor
- C. Parameterized constructor
- D. Default constructor

**2-23**. For explicit call _________________
- A. The destructor must be private
- B. The destructor must be public
- C. The destructor must be protected
- D. The destructor must be defined outside the class

**2-56**. Which among the following is correct?
- A. Friend function of derived class can access non-private members of base class
- B. Friend function of base class can access derived class members
- C. Friend function of derived class can access members of only derived class
- D. Friend function can access private members of base class of a derived class

**2-63**. Which among the following is true?
- A. The private members can’t be accessed by public members of the class
- B. The private members can be accessed by public members of the class
- C. The private members can be accessed only by the private members of the class
- D. The private members can’t be accessed by the protected members of the class

**2-86**. Which among the following is true?
- A. Static member functions can’t be virtual
- B. Static member functions can be virtual
- C. Static member functions can be declared virtual if it is pure virtual class
- D. Static member functions can be used as virtual in Java

**2-87**. The static members are ______________________
- A. Created with each new object
- B. Created twice in a program
- C. Created as many times a class is used
- D. Created and initialized only once

**2-88**. Which among the following is true?
- A. Static member functions can be overloaded
- B. Static member functions can’t be overloaded
- C. Static member functions can be overloaded using derived classes
- D. Static member functions are implicitly overloaded

**2-94**. In which type is new memory location will be allocated?
- A. Only in pass by reference
- B. Only in pass by value
- C. Both in pass by reference and value
- D. Depends on the code

**2-103**. Which among the following is true?
- A. Two objects can point to the same memory location
- B. Two objects can never point to the same memory location
- C. Objects not allowed to point at a location already occupied
- D. Objects can’t point to any address

**2-108**. How the argument passed to a function get initialized?
- A. Assigned using copy constructor at time of passing
- B. Copied directly
- C. Uses addresses always
- D. Doesn’t get initialized

**2-115**. We can assign ______________________
- A. Value of one reference variable to another
- B. Value of any object to another
- C. Value of any type to any object
- D. Value of non – reference to another reference

**2-117**. Which among the following is true?
- A. We can use direct assignment for any object
- B. We can use direct assignment only for different class objects
- C. We must not use direct assignment
- D. We can use direct assignment to same class objects

**2-125**. Which among the following is true?
- A. this pointer is passed implicitly when member functions are called
- B. this pointer is passed explicitly when member functions are called
- C. this pointer is passed with help of pointer member functions are called
- D. this pointer is passed with help of void pointer member functions are called

**2-128**. The result of sizeof() function __________________
- A. Includes space reserved for this pointer
- B. Includes space taken up by the address pointer by this pointer
- C. Doesn’t include the space taken by this pointer
- D. Doesn’t include space for any data member

**2-132**. Which among the following is true?
- A. This pointer can be used to guard against any kind of reference
- B. This pointer can be used to guard against self-reference
- C. This pointer can be used to guard from other pointers
- D. This pointer can be used to guard from parameter referencing

**2-133**. Which syntax doesn’t execute/is false when executed?
- A. if(&object != this)
- B. if(&function !=object)
- C. this.if(!this)
- D. this.function(!this)

**2-135**. Earlier implementations of C++ ___________________
- A. Never allowed assignment to this pointer
- B. Allowed no assignment to this pointer
- C. Allowed assignments to this pointer
- D. Never allowed assignment to any pointer

**2-140**. Which among the following is true?
- A. The constructors overloading can be done by using different names
- B. The constructors overloading can be done by using different return types
- C. The constructors can be overloaded by using only one argument
- D. The constructors must have the same name as that of class

**2-143**. Which among the following is true?
- A. More than one constructors with all default arguments is allowed
- B. More than one constructors with all default arguments can be defined outside the class
- C. More than one constructors can be used with same argument list
- D. More than one constructors with all default arguments can’t exist in same class

**2-150**. What happens when new fails?
- A. Returns zero always
- B. Throws an exception always
- C. Either throws an exception or returns zero
- D. Terminates the program

**2-154**. Which among the following is true?
- A. New operator can’t allocate functions but pointer to functions can be allocated
- B. New operator can allocate functions as well as pointer to functions
- C. New operator can allocate any type of functions
- D. New operator is not applicable with functions allocation

**2-158**. Does delete return any value?
- A. Yes, positive value
- B. Yes, negative value
- C. Yes, zero value
- D. No

**2-180**. Which among the following is correct?
- A. class student{ }s1,s2; s1.student()=s2.student();
- B. class student{ }s1; class topper{ }t1; s1=t1;
- C. class student{ }s1,s2; s1=s2;
- D. class student{ }s1; class topper{ }t1; s1.student()=s2.topper();

### Inheritance and Derivation

**2-40**. Which data members can be inherited but are private to a class?
- A. Private
- B. Protected
- C. Protected and Static
- D. Privately inherited

**2-65**. Which type of member functions get inherited in the same specifier in which the inheritance is done? (If private inheritance is used, those become private and if public used, those become public)
- A. Private member functions
- B. Protected member functions
- C. Public member functions
- D. All member functions

### Basic C++

**2-68**. Which among the following best defines static variables members?
- A. Data which is allocated for each object separately
- B. Data which is common to all the objects of a class
- C. Data which is common to all the classes
- D. Data which is common to a specific method

**2-90**. The keyword static is used _______________
- A. With declaration inside class and with definition outside the class
- B. With declaration inside class and not with definition outside the class
- C. With declaration and definition wherever done
- D. With each call to the member function

**2-122**. How can the address stored in the pointer be retrieved?
- A. Using * symbol
- B. Using $ symbol
- C. Using & symbol
- D. Using @ symbol

**2-123**. What should be done to prevent changes that may be made to the values pointed by the pointer?
- A. Usual pointer can’t change the values pointed
- B. Pointer should be made virtual
- C. Pointer should be made anonymous
- D. Pointer should be made const

**2-126**. The this pointer is accessible __________________
- A. Within all the member functions of the class
- B. Only within functions returning void
- C. Only within non-static functions
- D. Within the member functions with zero arguments

**2-134**. The this pointers _____________________
- A. Are modifiable
- B. Can be assigned any value
- C. Are made variables
- D. Are non-modifiable

**2-136**. This pointer can be used directly to ___________
- A. To manipulate self-referential data structures
- B. To manipulate any reference to pointers to member functions
- C. To manipulate class references
- D. To manipulate and disable any use of pointers

### Operators and Object Semantics

**2-110**. If programmer doesn’t define any copy assignment operator then ____________________
- A. Compiler gives an error
- B. Program fails at run time
- C. Compiler gives an implicit definition
- D. Compiler can’t copy the member values

**2-112**. Use of assignment operator ____________________
- A. Changes its use, when used at declaration and in normal assignment
- B. Doesn’t changes its use, whatever the syntax might be
- C. Assignment takes place in declaration and assignment syntax
- D. Doesn’t work in normal syntax, but only with declaration

**2-149**. What is the new operator?
- A. Allocates memory for an object or array
- B. Allocates memory for an object or array and returns a particular pointer
- C. Used as return type when an object is created
- D. Used to declare any new thing in a program

**2-153**. The new operator _____________
- A. Can allocate reference types too
- B. Doesn’t allocate reference types
- C. Can allocate reference to objects
- D. Doesn’t allocate any data

**2-155**. The objects allocated using new operator ________________
- A. Are destroyed when they go out of scope
- B. Are not destroyed even if they go out of scope
- C. Are destroyed anytime
- D. Are not destroyed throughout the program execution

**2-156**. How does compiler convert “::operator new” implicitly?
- A. ::operator new( sizeof( type ) )
- B. ::operator new( sizeof( ) )
- C. new operator :: type sizeof( type )
- D. new sizeof( type ) operator

**2-157**. What is a delete operator?
- A. Deallocates a block of memory
- B. Deallocates whole program memory
- C. Deallocates only primitive data memory
- D. Deallocates all the data reserved for a class

**2-159**. Which type of value has resulted from the delete operator?
- A. void
- B. void pointer
- C. null pointer
- D. null

**2-161**. Delete operator _________________
- A. Can be used on pointers with null value
- B. Can be used on pointers with void value
- C. Can be used on pointer with value 0
- D. Can be used on pointer with any value

**2-165**. The delete operator __________________
- A. Invokes function operator delete
- B. Invokes function defined by user to delete
- C. Invokes function defined in global scope to delete object
- D. Doesn’t invoke any function

## Answers

### Constructors and Destructors

- **2-1**: C. Copy an object so that it can be passed to a function 中文解释/结论：拷贝构造常用于按值传参时复制对象。 易错点：按值传参会创建副本；不是“传给另一个类”。
- **2-2**: A. A(int y, int x) 中文解释/结论：`obj2(10,20)` 调用两个 `int` 参数的构造函数。 易错点：构造函数匹配看参数个数和类型。
- **2-3**: B. classname() 中文解释/结论：构造函数名必须与类名相同。 易错点：析构函数前面有 `~`，不是构造函数。
- **2-12**: C. classname (const classname &obj){ /* constructor definition */ } 中文解释/结论：标准拷贝构造语法是 `ClassName(const ClassName&)`。 易错点：少了引用会造成递归拷贝问题。
- **2-13**: A. Must be passed by reference 中文解释/结论：拷贝构造参数应按引用传递。 易错点：按值传递会再次调用拷贝构造。
- **2-14**: D. Is not passed by reference 中文解释/结论：拷贝构造若不按引用接收，可能导致无限复制甚至内存问题。 易错点：核心原因是递归调用自身。
- **2-15**: C. Generates temporary object 中文解释/结论：编译器在生成临时对象时会调用拷贝构造。 易错点：按值返回、按值传参都常见。
- **2-17**: A. Yes, always 中文解释/结论：拷贝构造函数可以被声明为 private。 易错点：这常用于禁止对象拷贝。
- **2-18**: A. Must be const 中文解释/结论：拷贝构造参数通常应为 `const` 引用。 易错点：否则无法接收 const 对象和临时对象。
- **2-19**: C. Defining more than one constructor in single class with different signature 中文解释/结论：构造函数重载指同一类中多个不同签名的构造函数。 易错点：返回类型不能区分重载。
- **2-20**: D. No, constructors do not have any return type 中文解释/结论：构造函数没有返回类型，因此不能靠返回类型重载。 易错点：构造函数连 `void` 都不写。
- **2-21**: C. Can be implicit or explicit 中文解释/结论：析构函数既可隐式调用，也可显式调用。 易错点：实际开发中通常依赖隐式调用。
- **2-22**: A. Always equal to number of constructors called 中文解释/结论：正常对象生命周期中，每个构造成功的对象最终对应一次析构。 易错点：这里按构造成功、正常生命周期结束的常规对象计数理解。
- **2-24**: C. Destructors can't be overloaded 中文解释/结论：析构函数不能重载。 易错点：一个类只能有一个析构函数。
- **2-25**: A. A special function that is called to free the resources, acquired by the object 中文解释/结论：析构函数用于释放对象占用的资源。 易错点：不是“删除类”本身。
- **2-26**: D. Just before the end of object life 中文解释/结论：析构函数在对象生命周期结束前自动调用。 易错点：不是程序运行中任意时刻。
- **2-27**: A. Just before end of program 中文解释/结论：全局对象在程序结束前析构。 易错点：顺序通常与构造相反。
- **2-28**: C. Destructors are preceded by a tilde (~), and constructors are not 中文解释/结论：析构函数与构造函数最明显区别是前者有 `~`。 易错点：构造函数没有返回类型，析构函数也没有。
- **2-29**: C. Reverse 中文解释/结论：全局对象析构顺序通常与构造顺序相反。 易错点：记住“后构造先析构”。
- **2-30**: A. When class contains some pointer to memory allocated in class 中文解释/结论：类中若管理动态资源，通常应自定义析构函数。 易错点：否则可能泄漏内存。
- **2-105**: C. Because return by reference just make the objects points to values memory location 中文解释/结论：按引用返回不创建临时对象，因为只是返回已有对象的别名。 易错点：原英文表述不自然，核心是引用返回已有对象。
- **2-111**: B. Only non – const objects are accepted 中文解释/结论：若拷贝构造只接收非常量引用，则只能拷贝非常量对象。 易错点：不能接收 const 对象和临时对象。
- **2-138**: B. Constructors can be overloaded using different signatures 中文解释/结论：构造函数可通过不同参数列表重载。 易错点：不能靠返回类型区分。
- **2-139**: C. Use constructor with all default arguments 中文解释/结论：若希望既可无参又可带参构造，可用全默认参数构造函数。 易错点：这样一个构造函数覆盖两种场景。
- **2-141**: B. constructorName(int x=0, int y=0) 中文解释/结论：所有参数都有默认值的构造函数可充当默认构造函数。 易错点：可无参调用。
- **2-142**: A. The constructors might have all the same arguments except the default arguments 中文解释/结论：默认参数参与重载时，容易让多个构造函数调用产生歧义。 易错点：重载设计要避免冲突。
- **2-144**: A. className(int x=5,char c=’a’); 中文解释/结论：调用 `className(5,'a')` 会匹配 `className(int x=5, char c='a')`。 易错点：参数类型和顺序都匹配。
- **2-145**: C. className(int x=0,char c); 中文解释/结论：`className(int x=0, char c)` 会编译报错。 易错点：默认参数后面不能跟无默认参数。
- **2-146**: C. Then all the default values given will be used 中文解释/结论：全默认参数构造函数在不传参时会使用全部默认值。 易错点：这正是它代替默认构造的原因。
- **2-147**: D. The constructors with zero arguments 中文解释/结论：零参数构造函数是默认构造函数的一种典型形式。 易错点：更广义地说，可无参调用的也算。
- **2-148**: B. One default value constructor 中文解释/结论：与其写一个无参和一个单参默认值构造，不如直接写一个默认值构造。 易错点：可减少歧义。
- **2-151**: B. After the allocation of memory 中文解释/结论：`new` 先分配内存，再调用构造函数。 易错点：分配和构造是两个步骤。
- **2-162**: B. Object destructor is called before deallocation 中文解释/结论：`delete` 时先调用析构，再释放内存。 易错点：析构顺序早于 deallocation。

### Classes and Objects

- **2-4**: C. Destructor is not called 中文解释/结论：对象按引用传参不会生成副本，因此不会多出一个局部副本析构。 易错点：引用不是新对象。
- **2-5**: B. Names 中文解释/结论：对象通常有属性、状态、行为，名字不是对象本质属性。 易错点：名字只是程序员给的标识。
- **2-6**: B. Compile time error 中文解释/结论：静态成员函数中直接使用非静态成员会编译报错。 易错点：静态成员函数没有 `this`。
- **2-7**: A. Non-member functions which have access to all the members (including private) of a class 中文解释/结论：友元函数是非成员函数，但可访问类的私有成员。 易错点：它不是成员函数。
- **2-9**: A. Private data members can never be accessed from outside the class 中文解释/结论：私有成员函数不能从类外直接访问，只能由类内成员或友元间接访问。 易错点：不能通过普通对象直接调用 private 成员函数。
- **2-10**: B. Create public member functions to access those data members 中文解释/结论：访问私有数据应提供公有成员函数。 易错点：不要直接把数据成员改成 public。
- **2-11**: A. Copy constructor must be defined 中文解释/结论：涉及动态内存的类通常应自定义拷贝构造。 易错点：否则可能发生浅拷贝问题。
- **2-32**: C. None of its member function can be called outside the class 中文解释/结论：类没有 public 成员时，类外不能调用其成员函数。 易错点：不是不能创建对象。
- **2-33**: A. Data members 中文解释/结论：类中的变量和常量统称数据成员。 易错点：member variables 常对应 data members。
- **2-34**: C. Can be initialized either in declaration or by constructor 中文解释/结论：数据成员可用类内初始化器或构造函数初始化。 易错点：旧标准限制较多，现代 C++ 支持类内初始化。
- **2-35**: D. Static data members are defined outside class, not in constructor 中文解释/结论：静态数据成员通常在类外定义，而不是在构造函数中定义。 易错点：构造函数可修改值，但不是“定义”。
- **2-36**: A. The structure must have been defined before class. 中文解释/结论：类中使用结构体类型成员前，结构体必须先定义。 易错点：编译器要先知道类型。
- **2-37**: A. Return the address of the private data member using a member function 中文解释/结论：想在类外拿到私有成员地址，通常通过公有成员函数返回。 易错点：类外不能直接取私有成员地址。
- **2-39**: A. Static data members 中文解释/结论：静态成员函数只能直接使用静态数据成员。 易错点：非静态成员需要对象。
- **2-41**: B. Inline 中文解释/结论：局部类的成员函数默认会被当作内联处理。 易错点：局部类只在其定义函数内部可见。
- **2-42**: A. Yes, since local 中文解释/结论：不同函数中的局部类可以同名。 易错点：因为它们处于不同局部作用域。
- **2-43**: B. Within the function 中文解释/结论：局部类的作用域仅限其所在函数。 易错点：类外和其他函数都不可见。
- **2-44**: D. No, can't access 中文解释/结论：除包围它的函数外，其他函数不能访问局部类成员。 易错点：局部类作用域很窄。
- **2-45**: C. Helps to add extra functionality to a function 中文解释/结论：局部类能为特定函数增加局部辅助功能。 易错点：它不是提速工具。
- **2-46**: A. Class inside a class 中文解释/结论：嵌套类就是定义在类内部的类。 易错点：不是定义在函数里。
- **2-49**: D. Any other members 中文解释/结论：静态嵌套类不能直接访问外围类的其他成员。 易错点：尤其不能直接访问非静态上下文。
- **2-50**: C. Makes the code efficient and readable 中文解释/结论：嵌套类可提升代码组织性和可读性。 易错点：不是让代码自动并发。
- **2-51**: B. To access only public members of a class 中文解释/结论：对象在类外通常只能访问 public 成员。 易错点：private/protected 不能直接访问。
- **2-52**: A. Defining a member function 中文解释/结论：对象不是用来定义成员函数的。 易错点：成员函数属于类定义。
- **2-53**: B. cin 中文解释/结论：标准输入对象是 `cin`。 易错点：对应标准输出对象 `cout`。
- **2-54**: C. As only one class type at a time 中文解释/结论：一个对象同一时刻只能是一个类类型的实例。 易错点：不会同时属于多个无关类。
- **2-55**: A. Its compile time error 中文解释/结论：不同类里使用同名对象名在同一作用域会编译报错。 易错点：同一作用域内名字不能重复定义。
- **2-57**: A. Define a public function which multiplies two numbers 中文解释/结论：要扩展功能，最直接做法是再加一个公有乘法函数。 易错点：没必要暴露内部数据。
- **2-58**: A. Object orientation 中文解释/结论：类是面向对象程序设计的核心载体。 易错点：不是过程式特征。
- **2-59**: C. To group the most similar data and operations 中文解释/结论：类适合把相近的数据和操作组织在一起。 易错点：这正是封装。
- **2-60**: D. To make private data accessible to the client 中文解释/结论：访问器方法用于让私有数据可控地被外部访问。 易错点：不是把私有数据直接变 public。
- **2-61**: A. Functions that do not change the value of the calling object 中文解释/结论：常成员函数不会修改调用对象的状态。 易错点：通常声明为函数后缀 `const`。
- **2-62**: A. Member functions which can only be used within the class 中文解释/结论：私有成员函数只能在类内部使用。 易错点：类外对象不能直接调用。
- **2-64**: C. Functions accessible everywhere using object of class 中文解释/结论：公有成员函数可通过对象在类外访问。 易错点：是否能访问看对象和作用域。
- **2-66**: A. Undeclared function error will be produced 中文解释/结论：不能直接在 `main` 里像普通函数一样调用某对象的公有成员函数名。 易错点：需要对象或类作用域。
- **2-67**: D. Can access all the member of its class 中文解释/结论：类的公有成员函数在类内部可访问该类所有成员。 易错点：包括 private/protected。
- **2-69**: C. Is reflected to all the objects of that class 中文解释/结论：修改静态数据成员会影响该类所有对象看到的结果。 易错点：因为它是共享的。
- **2-70**: D. static dataType memberName; 中文解释/结论：静态数据成员声明语法是 `static type name;`。 易错点：顺序不能颠倒。
- **2-71**: B. Must be defined outside the class 中文解释/结论：静态数据成员通常还需在类外定义一次。 易错点：只在类内声明不算完整定义。
- **2-72**: A. dataType className :: memberName = value; 中文解释/结论：静态数据成员定义格式是 `type Class::member = value;`。 易错点：中间必须是 `::`。
- **2-74**: C. Can be accessed with dot operator 中文解释/结论：静态数据成员可通过对象使用点运算符访问。 易错点：更推荐用 `ClassName::member`。
- **2-75**: B. className :: staticDataMember; 中文解释/结论：静态数据成员可通过类名和 `::` 访问。 易错点：注意类外定义还需要写类型。
- **2-77**: A. Only one copy of the data is created 中文解释/结论：静态数据成员在整个类中只保留一份。 易错点：不是每个对象一份副本。
- **2-78**: D. Using dot or arrow operator 中文解释/结论：静态成员函数可通过点或箭头运算符调用。 易错点：也可用类名直接调用。
- **2-82**: C. Have access to only the static members of a class 中文解释/结论：静态成员函数只能直接访问类的静态成员。 易错点：不能直接访问非静态成员。
- **2-83**: A. Can be called using class name 中文解释/结论：静态成员函数可以直接用类名调用。 易错点：无需对象。
- **2-85**: C. this pointer 中文解释/结论：`this` 是指向当前对象的指针。 易错点：只存在于非静态成员函数中。
- **2-89**: D. Can't be declared const, volatile or const volatile 中文解释/结论：`this` 指针本身不能被重新声明成这些形式。 易错点：成员函数的 cv 限定会影响 `this` 指向类型。
- **2-91**: C. The exact address of the object in memory 中文解释/结论：`this` 保存当前对象的实际地址。 易错点：因此可区分不同对象。
- **2-95**: C. Can be returned either by value or reference 中文解释/结论：对象既可按值返回，也可按引用返回。 易错点：要注意引用返回的生命周期。
- **2-96**: A. A temporary object is created 中文解释/结论：对象按值返回通常会产生临时对象。 易错点：现代编译器可做返回值优化，但概念上可理解为按值返回产生结果对象。
- **2-97**: D. ClassName functionName ( ){ } 中文解释/结论：`ClassName functionName(){}` 表示函数返回一个类类型对象。 易错点：函数返回类型是类名。
- **2-98**: A. className& functionName ( ) 中文解释/结论：按引用返回对象的函数写法是 `ClassName& functionName()`。 易错点：返回引用要保证目标对象仍然有效。
- **2-99**: B. It can't be returned by reference 中文解释/结论：局部对象通常不能按引用安全返回。 易错点：函数结束后局部对象已销毁。
- **2-100**: B. Run time error 中文解释/结论：错误返回局部对象引用可能导致运行时错误。 易错点：典型是悬空引用。
- **2-101**: D. Temporary object is not created 中文解释/结论：按引用返回对象时不需要额外创建临时对象。 易错点：因为直接引用已有对象。
- **2-102**: A. Yes, always 中文解释/结论：对象可以作为函数返回值。 易错点：按值返回是允许的。
- **2-104**: D. Its member values are copied using copy constructor 中文解释/结论：对象按值传参时，其成员值通过拷贝构造复制。 易错点：不是简单按地址共享。
- **2-106**: B. Its values gets copied into another object 中文解释/结论：对象赋值的本质是把一个对象的值复制给另一个对象。 易错点：前提是同类或可赋值类型。
- **2-113**: C. From any object will be visible in all 中文解释/结论：静态成员从任一对象修改后，对所有对象可见。 易错点：共享数据的典型特征。
- **2-114**: B. Initialize the object with another at declaration 中文解释/结论：用已有对象在声明时初始化新对象属于拷贝初始化。 易错点：不是普通赋值。
- **2-116**: C. Will not create any other copy of the object 中文解释/结论：按引用传递对象不会再创建副本。 易错点：效率更高。
- **2-118**: A. Using object name 中文解释/结论：访问对象成员最直接用对象名。 易错点：配合点运算符。
- **2-119**: A. Equal to size of any usual pointer 中文解释/结论：`this` 指针大小与普通指针大小相同。 易错点：本质上它就是一个指针。
- **2-120**: A. pointer->function() 中文解释/结论：对象指针调用成员函数用 `pointer->function()`。 易错点：不是 `pointer.function()`。
- **2-121**: B. It becomes dangling pointer 中文解释/结论：释放后未置空的指针会变成悬空指针。 易错点：再使用会有未定义行为。
- **2-124**: B. This pointer 中文解释/结论：当前对象地址由 `this` 指针保存。 易错点：只在非静态成员函数中可用。
- **2-127**: D. Isn’t part of object itself 中文解释/结论：`this` 是成员函数调用时的隐式指针，不占对象自身空间。 易错点：对象大小不包含 `this`。
- **2-129**: A. Address of the object is passed implicitly as an argument 中文解释/结论：调用成员函数时，对象地址会作为隐式参数传入。 易错点：这正是 `this` 的来源。
- **2-130**: D. function(&object,parameter) 中文解释/结论：成员函数调用可近似理解为隐式传入对象地址：`function(&object, parameter)`。 易错点：这是理解编译器转换的一种近似。
- **2-131**: C. Is available inside the member function using this pointer 中文解释/结论：`this` 可在成员函数内部直接使用。 易错点：类外不能直接写 `this`。
- **2-137**: D. [cv-qualifier-list] classType *const this; 中文解释/结论：`this` 可近似理解为指向当前对象的常指针，形式类似 `[cv] classType *const this`。 易错点：重点是它本质是常指针。
- **2-160**: C. Then unpredictable errors may arise 中文解释/结论：释放错误的内存或重复释放会导致不可预测错误。 易错点：典型未定义行为。
- **2-163**: D. Its value is undefined 中文解释/结论：释放后继续使用指针属于危险行为。 易错点：严格说指针变量值未必自动改变，但解引用已失效。
- **2-164**: A. delete [] objectName; 中文解释/结论：释放动态数组要用 `delete[] objectName;`。 易错点：不能用普通 `delete`。
- **2-168**: A. Must be included before use 中文解释/结论：预定义类或库类使用前通常需要先包含相应头文件。 易错点：否则编译器不知道声明。
- **2-170**: A. To handle all input streams 中文解释/结论：处理标准输入流的对象是 `cin`。 易错点：与输入流概念关联。
- **2-171**: A. An array of instances of class represented by single name 中文解释/结论：对象数组是一组同类对象，用一个数组名统一表示。 易错点：数组元素类型必须一致。
- **2-172**: C. All the objects should be of same class 中文解释/结论：对象数组中的所有元素必须属于同一类。 易错点：不能混放不同类对象。
- **2-173**: A. Class 中文解释/结论：类是对象数组元素所属的类型定义。 易错点：对象数组本质上是类实例集合。
- **2-174**: A. Instance of a class 中文解释/结论：对象就是类的实例。 易错点：类是模板，对象是实体。
- **2-175**: D. Passed as function 中文解释/结论：对象可以作为函数参数传递。 易错点：可按值、引用或指针。
- **2-177**: D. The object can be used, accessed, and declared locally in that function 中文解释/结论：局部对象只能在当前函数内声明、访问和使用。 易错点：离开作用域后销毁。
- **2-178**: C. Can't be used by any other function 中文解释/结论：函数内局部对象不能被其他函数直接使用。 易错点：除非以参数/返回值形式传递。
- **2-179**: A. A temporary object is created to return the value 中文解释/结论：对象按值返回时会创建临时对象。 易错点：现代编译器可做返回值优化。

### Miscellaneous

- **2-8**: B. Binding and Hiding respectively 中文解释/结论：封装常强调绑定数据和操作，抽象常强调隐藏实现、暴露接口。 易错点：这是一种教材化说法，不够严格。
- **2-16**: B. User defined copy constructor 中文解释/结论：管理动态内存的类通常需要自定义拷贝构造以实现深拷贝。 易错点：本质是深拷贝需求。
- **2-23**: B. The destructor must be public 中文解释/结论：如果对象要在类外正常销毁，析构函数通常必须可访问。 易错点：析构函数可以是 private/protected，但会限制对象销毁方式。
- **2-56**: A. Friend function of derived class can access non-private members of base class 中文解释/结论：派生类友元函数可通过派生类访问基类可访问的非 private 成员。 易错点：友元关系本身不会被继承。
- **2-63**: B. The private members can be accessed by public members of the class 中文解释/结论：类的公有成员函数可以访问该类的私有成员。 易错点：这是封装的基础。
- **2-86**: A. Static member functions can't be virtual 中文解释/结论：静态成员函数不能是虚函数。 易错点：虚函数依赖对象动态绑定和 `this`。
- **2-87**: D. Created and initialized only once 中文解释/结论：静态成员在程序中只创建并初始化一次。 易错点：不是每建一个对象创建一次。
- **2-88**: A. Static member functions can be overloaded 中文解释/结论：静态成员函数可以重载。 易错点：重载看参数列表，不看是否 static。
- **2-94**: B. Only in pass by value 中文解释/结论：按值传参会创建副本并占用新的存储。 易错点：按引用传参不创建新对象。
- **2-103**: A. Two objects can point to the same memory location 中文解释/结论：多个对象内部指针成员可以指向同一块内存。 易错点：这会带来浅拷贝和重复释放风险。
- **2-108**: A. Assigned using copy constructor at time of passing 中文解释/结论：对象按值传参时用拷贝构造初始化形参。 易错点：不是普通赋值运算符。
- **2-115**: A. Value of one reference variable to another 中文解释/结论：引用参与赋值时，赋的是被引用对象的值。 易错点：引用不能重新绑定。
- **2-117**: D. We can use direct assignment to same class objects 中文解释/结论：同类对象可使用默认或自定义赋值运算符。 易错点：不同类对象默认不可直接赋值。
- **2-125**: A. this pointer is passed implicitly when member functions are called 中文解释/结论：`this` 会在成员函数调用时隐式传入。 易错点：程序员通常不显式写出它。
- **2-128**: C. Does not include the space taken by this pointer 中文解释/结论：`sizeof` 对象不计入 `this` 指针。 易错点：`this` 不是数据成员。
- **2-132**: B. This pointer can be used to guard against self-reference 中文解释/结论：`this` 常用于防止自赋值。 易错点：典型写法是 `if (this == &other)`。
- **2-133**: A. if(&object != this) 中文解释/结论：`if (&object != this)` 是可用于避免自赋值的合法判断式。 易错点：其他选项语法不合法。
- **2-135**: C. Allowed assignments to this pointer 中文解释/结论：早期一些实现允许给 `this` 赋值。 易错点：现代 C++ 中不能修改 `this`。
- **2-140**: D. The constructors must have the same name as that of class 中文解释/结论：构造函数名必须和类名完全相同。 易错点：否则就只是普通函数。
- **2-143**: D. More than one constructors with all default arguments can't exist in same class 中文解释/结论：多个全默认参数构造函数会导致无参构造调用歧义。 易错点：默认参数会改变可调用形态。
- **2-150**: C. Either throws an exception or returns zero 中文解释/结论：普通 `new` 失败通常抛异常，`nothrow new` 可返回空指针。 易错点：现代默认不是简单返回 0。
- **2-154**: A. New operator can't allocate functions but pointer to functions can be allocated 中文解释/结论：`new` 不能直接分配函数，但可分配函数指针。 易错点：函数本身不是普通对象。
- **2-158**: D. No 中文解释/结论：`delete` 没有返回值。 易错点：不是返回 0 或指针。
- **2-180**: C. class student{ }s1,s2; s1=s2; 中文解释/结论：同类对象之间可直接赋值。 易错点：不同类对象默认不能直接赋值。

### Inheritance and Derivation

- **2-40**: B. Protected 中文解释/结论：protected 成员可被派生类继承并访问，同时对类外保持不可访问。 易错点：private 成员存在于基类子对象中，但派生类不能直接访问。
- **2-65**: C. Public member functions 中文解释/结论：public 成员函数在派生类中的访问级别会受继承方式影响。 易错点：private 成员不会被派生类直接访问。

### Basic C++

- **2-68**: B. Data which is common to all the objects of a class 中文解释/结论：静态数据成员是类所有对象共享的一份数据。 易错点：不是每个对象各有一份。
- **2-90**: B. With declaration inside class and not with definition outside the class 中文解释/结论：静态数据成员类内声明写 `static`，类外定义通常不再写 `static`。 易错点：类外定义需要类名限定。
- **2-122**: A. Using * symbol 中文解释/结论：使用 `*` 解引用指针可取得其指向对象。 易错点：如果问指针变量里保存的地址，直接读取指针变量即可。
- **2-123**: D. Pointer should be made const 中文解释/结论：应使用指向 const 的指针来防止通过指针修改目标值。 易错点：更准确写法是 pointer to const，如 `const int* p`。
- **2-126**: C. Only within non-static functions 中文解释/结论：`this` 只存在于非静态成员函数中。 易错点：静态成员函数没有 `this`。
- **2-134**: D. Are non-modifiable 中文解释/结论：`this` 指针本身不可被修改。 易错点：现代标准下 `this` 本身不可重新赋值。
- **2-136**: A. To manipulate self-referential data structures 中文解释/结论：`this` 可用于操作自引用数据结构。 易错点：比如链表、树等对象内部链接。


### Operators and Object Semantics

- **2-110**: C. Compiler gives an implicit definition 中文解释/结论：若未定义拷贝赋值运算符，编译器会隐式生成一个。 易错点：默认是逐成员赋值。
- **2-112**: A. Changes its use, when used at declaration and in normal assignment 中文解释/结论：赋值号在声明初始化和普通赋值里的语义场景不同。 易错点：一个是初始化，一个是赋值。
- **2-149**: B. Allocates memory for an object or array and returns a particular pointer 中文解释/结论：`new` 用于分配内存并返回相应指针。 易错点：通常还会调用构造函数。
- **2-153**: B. Does not allocate reference types 中文解释/结论：`new` 不能分配引用类型。 易错点：引用不是可独立分配的对象。
- **2-155**: B. Are not destroyed even if they go out of scope 中文解释/结论：用 `new` 分配的对象不会因离开作用域自动销毁。 易错点：必须手动 `delete` 或交给智能指针。
- **2-156**: A. ::operator new( sizeof( type ) ) 中文解释/结论：`new T` 的底层分配步骤可理解为调用 `::operator new(sizeof(T))`。 易错点：这是理解底层机制的经典表述。
- **2-157**: A. Deallocates a block of memory 中文解释/结论：`delete` 用于释放动态分配的内存块。 易错点：并在需要时先调用析构函数。
- **2-159**: A. void 中文解释/结论：`delete` 表达式没有可用返回值。 易错点：不要把 `delete` 当成返回指针或整数的表达式。
- **2-161**: A. Can be used on pointers with null value 中文解释/结论：`delete` 可以安全作用于空指针。 易错点：对空指针执行 `delete` 没问题。
- **2-165**: A. Invokes function operator delete 中文解释/结论：`delete` 最终会调用 `operator delete`。 易错点：这是其底层释放机制。
