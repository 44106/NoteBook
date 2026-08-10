# Lecture 1: 1 Introduction

Source: `1 Introduction.pptx`
Pages: 43

## Page 1

Object-Oriented  Programming
with C++
Yuchi Huo @ CAD&CG Lab

Speaker notes:
System hierarchy & abstraction, modulization, interface…

## Page 2

Course contents
Introduction to	object-oriented programming…
…with	a	solid software engineering  foundation…
…aimed at producing and maintaining large, high-quality software systems.

## Page 3

Ranked 4th on TIOBE Index

Speaker notes:
Danish, ACM/IEEE fellow

## Page 4

C++ Applications

Speaker notes:
Adobe公司首席科学家Alexander Stepanov

## Page 5

C++ Applications

## Page 6

C++ Applications

## Page 7

C++ Applications「卡脖子问题」

## Page 8

C++ Applications「卡脖子问题」

## Page 9

C++ Applications「卡脖子问题」

## Page 10

template
encapsulation
coupling
interface
cohesion
polymorphic method calls
inheritance
mutator methods
collection classes
overriding
iterators
responsibility-driven design
Buzzwords

## Page 11

Textbooks

## Page 12

[No extractable text]

## Page 13

Thinking in C++,  Vol.1&2
C++ Primer
References:
• The C++ Programming Language
• A Tour of C++
• Essential C++
• Effective C++
• Inside the C++ Object Model
• ……
Textbooks

## Page 14

C++编程思想 机械工业出版社

## Page 15

BRUCE ECKEL is the author of “Thinking in C++”, which won the Software Development Jolt Award for best book of 1995.  He's been professionally programming	for 20 years and has been teaching people throughout the world	how to program with objects since 1986. He was a voting member of the C++ Standards	Committee.
http://mindview.net
6
Bruce Eckel

## Page 16

Online Resources for C++
https://cppreference.com
https://isocpp.org/
https://www.youtube.com/user/CppCon

## Page 17

Lab (50%, including the in-class quiz)
Announced in week 1, 3, 5, 7, 9, 11, and 13
Submit on-line (manually judged by TA)
The deadline is truly DEAD
Per day delay cost: 10% of the full score
Final exam (50%, on PTA)
Assessment

## Page 18

Resources
Courseware (学在浙大)
Assignments (PTA)

## Page 19

作业 (Homework Assignments)
Register and login at https://pintia.cn/
Bind your student ID with bind key
Enter

## Page 20

PTA绑定码：850585

## Page 21

Course policy
Academic honesty:
Students are fully responsible for their actions.
During homework, students can help each other through hints and explanations.
Copying code from anybody else is strictly forbidden.
https://conduct.berkeley.edu/integrity/

## Page 22

Course policy

## Page 23

Contact info:
[ TA 胡崇浩] chonghao@zju.edu.cn
[ TA 孙川] 22421279@zju.edu.cn
[ me ] eehyc0@zju.edu.cn
Title starts	with  "[OOP]"
State your name and	id in the text
E-mail rule

## Page 24

Introduction to C++
The	trip begins…

## Page 25

#include <iostream>  using namespace std;
int main()
{
cout << "Hello, World! I am " << 18 << " Today!" << endl;
return 0;
}
The first C++ program

## Page 26

Development environment
Windows:
visual studio community
Linux, macOS:
g++, clang
visual studio code
Any compiler supports C++ standard well…

## Page 27

#include <iostream>  using namespace std;
int main() {
int number;
cout << "Enter a decimal number: ";  cin >> number;
cout << "The number you entered is " << number <<"." << endl;
return 0;
}
Read input

## Page 28

Strengths
Efficient programs
Direct access to machine, suitable for OS and ES
Flexible
Weakness
Insufficient type checking
Unsuitable for high-level applications
No direct support for oop
The	C language

## Page 29

C++ was first designed and implemented by Bjarne Stroustrup,  AT&T, early 1980’s
http://www.stroustrup.com/
Bjarne Stroustrup

## Page 30

Oct. 2002,  Stroustrup  visited Zhejiang Univ.

## Page 31

[No extractable text]

## Page 32

[No extractable text]

## Page 33

Stroustrup visited zju in 2005

## Page 34

C++ 之父：爱吃辣子鸡，C++20 会非常出色
https://www.infoq.cn/article/rv3SX2V8rtRaJj9B17xZ

## Page 35

The Design and Evolution of C++
Bjarne Stroustrup, Addison-Wesley, ISBN 0-201-54330-3

## Page 36

1978: BS at Cambridge, UK. Simulation program  in Simula
Supports classes, inheritance, and type check
Poor performance
http://www.engin.umd.umich.edu/CIS/course.des/cis400/simula/simula.html
Brief history of C++ (1)

## Page 37

1979: BS at AT&T Labs, Cpre,  C w/classes
1980: most C++ features but virtual functions
1983: C++ w/virtual functions, named C++ by Rick Mascitti
1985: “The C++ Programming Language”
1990: ANSI C++ Committee ISO/ANSI
Standard C++ in 1998: ISO/IEC 14882 (http://www.open-std.org/jtc1/sc22/wg21/)
Brief history of C++ (2)

## Page 38

C++03, C++11, c++14, c++17, c++20
To be continued …
Brief history of C++ (3)

## Page 39

To	combine:
Flexibility and efficiency of C
Support for object-oriented programming (from  Simula and SmallTalk)
Goal for C++

## Page 40

C++	builds on C
Knowledge of C helps you in C++
C++	support more styles of programming
C++	provides	more features
C++
C
C and C++

## Page 41

C++ improvements
Data abstraction
Access control
Initialization & cleanup
Function overloading
Streams for I/O
Constants (C99)
Name control
Inline functions(C99)
References
Operator overloading
Memory management
Support for OOP
Templates
Exception handling
Extensive libraries, STL

## Page 42

C++ can be viewed as a “better” C
C++  C=C+1
But...
C++ is not C
Focus on C++ as a language in its own right
C++	is	a	hybrid language, supports
Procedure-oriented programming
Object-oriented programming
Generic programming
C++

## Page 43

C++
https://en.wikipedia.org/wiki/C%2B%2B#Criticism
OOP
https://en.wikipedia.org/wiki/Object-oriented_programming#Criticism
Criticism of …
