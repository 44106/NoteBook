# Lecture 11: 11 STL

- Source: `11 STL.pdf`
- Pages: 29
- Rendered page images: 29
- Contact sheet: [open](../contact_sheets/11_11_STL_contact.jpg)
- Raw extracted text: [open](../raw_texts/11-11 STL.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 11 page 1](../page_images/11_11_STL/page_001.png)

Extracted text:

```text
STL
Object-Oriented Programming with C++
```

## Page 2

![Lecture 11 page 2](../page_images/11_11_STL/page_002.png)

Extracted text:

```text
What is STL
• STL = Standard Template Library
• Part of the ISO Standard C++ Library
• Data Structures and algorithms for C++.

               Alexander Stepanov
               Алекса́ндр Алекса́ндрович Степа́нов


               Book:
               From Mathematics to Generic Programming
```

## Page 3

![Lecture 11 page 3](../page_images/11_11_STL/page_003.png)

Extracted text:

```text
Why should I use STL?
• Reduce development time.
  – Data-structures already written and debugged.
• Code readability
  – Fit more meaningful stuff on one page.
• Robustness
  – STL data structures grow automatically.
• Portable code.
• Maintainable code
• Easy
```

## Page 4

![Lecture 11 page 4](../page_images/11_11_STL/page_004.png)

Extracted text:

```text
C++ Standard Library
• Library includes:
  – A pair class (pairs of anything, int/int, int/char, etc)
  – Containers
    •vector (expandable array)
    •deque (expandable array, expands at both ends)
    •list (double-linked)
    •set and map
  – Basic Algorithms (sort, search, etc)
• All identifiers in library are in std namespace
           using namespace std;
```

## Page 5

![Lecture 11 page 5](../page_images/11_11_STL/page_005.png)

Extracted text:

```text
The three parts of STL
• Containers
• Algorithms
• Iterators
```

## Page 6

![Lecture 11 page 6](../page_images/11_11_STL/page_006.png)

Extracted text:

```text
The ‘Top 3’ data structures
• map
  –Any key type, any value type.
  –Sorted.
• vector
  –Like c array, but auto-extending.
• list
  –doubly-linked list
```

## Page 7

![Lecture 11 page 7](../page_images/11_11_STL/page_007.png)

Extracted text:

```text
All sequential containers
• vector: variable array
• deque: dual-end queue
• list: double-linked-list
• forward_list: as it
• array: as “array”
• string: char array
```

## Page 8

![Lecture 11 page 8](../page_images/11_11_STL/page_008.png)

Extracted text:

```text
Example using the vector class
• Use “namespace std” so        #include <iostream>
                                #include <vector>
  that you can refer to
                                using namespace std;
  vectors in C++ library
• Just declare a vector of      int main( ) {
  ints (no need to worry             vector<int> x;
  about size)                        for (int a=0; a<1000; a++)
                                           x.push_back(a);
• Add elements                       vector<int>::iterator p;
• Have a pre-defined                 for (p=x.begin();
  iterator for vector class,                     p<x.end(); p++)
                                           cout << *p << " ";
  can use it to print out the
                                     return 0;
  items in vector
                                }
```

## Page 9

![Lecture 11 page 9](../page_images/11_11_STL/page_009.png)

Extracted text:

```text
Basic vector operations
• Constructors                       • Element access
   vector<Elem> c;                     V.at(index)
   vector<Elem> c1(c2);                V[index]
                                        V.front( )       // first item
• Simple methods
                                        V.back( )        // last item
   V.size( )        // num items
   V.empty( )      // empty?         • Add/Remove/Find
                                        V.push_back(e)
   ==, !=, <, >, <=, >=
                                        V.pop_back( )
   v1.swap(v2) // swap
                                        V.insert(pos, e)
• Iterators                             V.erase(pos)
   I.begin( )    // first position      V.clear( )
   I.end( )      // last position       V.find(first, last, item)
```

## Page 10

![Lecture 11 page 10](../page_images/11_11_STL/page_010.png)

Extracted text:

```text
Pay attention to efficiency
• Estimate and preserve the memory
• Avoid extra copies



code & demo
```

## Page 11

![Lecture 11 page 11](../page_images/11_11_STL/page_011.png)

Extracted text:

```text
List class
• Same basic concepts as vector
 – Constructors
 – Ability to compare lists (==, !=, <, <=, >, >=)
 – Ability to access front and back of list
     x.front(), x.back()
 – Ability to assign items to a list, remove items
     x.push_back(item), x.push_front(item)
     x.pop_back(), x.pop_front()
     x.remove(item)
```

## Page 12

![Lecture 11 page 12](../page_images/11_11_STL/page_012.png)

Extracted text:

```text
Sample list application
• Declare a list of strings     #include <iostream>
                                using namespace std;
• Add elements                  #include <list>
                                #include <string>
  –Some to the back
                                int main( ) {
  –Some to the front                list<string> s;
• Iterate through the list          s.push_back("hello");
                                    s.push_back("world");
  –Note the termination             s.push_front("tide");
   condition for our iterator       s.push_front("crimson");
                                    s.push_front("alabama");
            p != s.end( )           list<string>::iterator p;
  –Cannot use p < s.end( ) as       for (p=s.begin(); p!=s.end(); p++)
   with vectors, as the list                  cout << *p << " ";
                                    cout << endl;
   elements may not be stored   }
   in order
```

## Page 13

![Lecture 11 page 13](../page_images/11_11_STL/page_013.png)

Extracted text:

```text
maps
• Maps are collections that contain pairs of
  values.

• Pairs consist of a key and a value.

• Lookup works by supplying a key, and
  retrieving a value.

• An example: a telephone book.
```

## Page 14

![Lecture 11 page 14](../page_images/11_11_STL/page_014.png)

Extracted text:

```text
Using maps
• A map with strings as keys and values
              :map<string, string>
           "Charles Nguyen"    "(531) 9392 4587"

             "Lisa Jones"      "(402) 4536 4674"

          "William H. Smith"   "(998) 5488 0123"
```

## Page 15

![Lecture 11 page 15](../page_images/11_11_STL/page_015.png)

Extracted text:

```text
Example program
#include <map>
#include <string>
map<string, float> price;
price[“snapple”] = 0.75;
price[“coke”] = 0.50;
string item;
double total=0;
while ( cin >> item )
      total += price[item];
```

## Page 16

![Lecture 11 page 16](../page_images/11_11_STL/page_016.png)

Extracted text:

```text
Example program
#include <map>
#include <string>
map<string, float> price;
price[“snapple”] = 0.75;
price[“coke”] = 0.50;
string item;
double total=0;
while ( cin >> item )
      total += price[item];
```

## Page 17

![Lecture 11 page 17](../page_images/11_11_STL/page_017.png)

Extracted text:

```text
Example program
#include <map>
#include <string>
map<string, float> price;
price[“snapple”] = 0.75;
price[“coke”] = 0.50;
string item;
double total=0;
while ( cin >> item )
      total += price[item];
```

## Page 18

![Lecture 11 page 18](../page_images/11_11_STL/page_018.png)

Extracted text:

```text
Example program
#include <map>
#include <string>
map<string, float> price;
price[“snapple”] = 0.75;
price[“coke”] = 0.50;
string item;
double total=0;
while ( cin >> item )
      total += price[item];
```

## Page 19

![Lecture 11 page 19](../page_images/11_11_STL/page_019.png)

Extracted text:

```text
Algorithms
• Take iterators as arguments
list<int> L;
vector<int> V;
// put list in vector
copy (L.begin(),
      L.end(),
      V.begin());

code & demo
```

## Page 20

![Lecture 11 page 20](../page_images/11_11_STL/page_020.png)

Extracted text:

```text
The World Map of C++ STL Algorithms




   https://www.fluentcpp.com/getthemap/
```

## Page 21

![Lecture 11 page 21](../page_images/11_11_STL/page_021.png)

Extracted text:

```text
Typedefs
• Annoying to type long names
  – map<Name,list<PhoneNum>> phonebook;
  – map<Name,list<PhoneNum>>::iterator finger;
• Simplify with typedef
  – typedef PB map<Name,list<PhoneNum>>;
                           –

  – PB phonebook;
  – PB::iterator finger;
• Easy to change implementation.
```

## Page 22

![Lecture 11 page 22](../page_images/11_11_STL/page_022.png)

Extracted text:

```text
Typedefs
• Annoying to type long names
  – map<Name,list<PhoneNum>> phonebook;
  – map<Name,list<PhoneNum>>::iterator finger;
• Simplify with typedef
  – typedef PB map<Name,list<PhoneNum>>;
                           ––

  – PB phonebook;
  – PB::iterator finger;
• Easy to change implementation.
• C++ 11: auto, using
```

## Page 23

![Lecture 11 page 23](../page_images/11_11_STL/page_023.png)

Extracted text:

```text
Using your own classes
• Might need:
  –Assignment Operator, operator=()
  –Default Constructor
• For sorted types, like set,map,…
  –Need less-than operator: operator<()
    •Some types have this by default:
      –int, char, string
    •Some do not:
      –char *
```

## Page 24

![Lecture 11 page 24](../page_images/11_11_STL/page_024.png)

Extracted text:

```text
Example of user-defined type
• Sorted container needs sort function.
  struct full_name {
      char * first;
      char * last;
      bool operator<(full_name & a) {
        return strcmp(first, a.first) < 0;
      }
  }
  map<full_name,int> phonebook;
```

## Page 25

![Lecture 11 page 25](../page_images/11_11_STL/page_025.png)

Extracted text:

```text
Pitfalls
• Accessing an invalid vector<> element.
   vector<int> v;
   v[100]=1; // Whoops!


 Solutions:
  – use push_back()
  – Preallocate withconstructor.
  – Reallocate with resize()
  – Check size()
```

## Page 26

![Lecture 11 page 26](../page_images/11_11_STL/page_026.png)

Extracted text:

```text
Pitfalls
• Inadvertently inserting into map<>
   if (foo["bob"]==1)
   // silently created entry "bob"

Use count() to check for a key without creating a
new entry.
   if (foo.count("bob"))

Or contains() introduced in C++20
   if (foo.contains("bob"))
```

## Page 27

![Lecture 11 page 27](../page_images/11_11_STL/page_027.png)

Extracted text:

```text
Pitfalls
• Using empty() on list<>
 –Slow
     if (my_list.size()== 0)   {...}
 –Fast
     if (my_list.empty())   {...}
```

## Page 28

![Lecture 11 page 28](../page_images/11_11_STL/page_028.png)

Extracted text:

```text
Pitfalls
• Using invalid iterator
   list<int> L;
   list<int>::iterator li;
   li = L.begin();
   L.erase(li);
   ++li; // WRONG
• Use return value of erase to advance
   li = L.erase(li); // RIGHT
```

## Page 29

![Lecture 11 page 29](../page_images/11_11_STL/page_029.png)

Extracted text:

```text
Other data structures
• set, multiset, multimap
• queue, priority_queue
• stack, deque
• slist, bitset, valarray
```
