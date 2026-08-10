# Lecture 12: 12 Iterators

- Source: `12 Iterators.pdf`
- Pages: 48
- Rendered page images: 48
- Contact sheet: [open](../contact_sheets/12_12_Iterators_contact.jpg)
- Raw extracted text: [open](../raw_texts/12-12 Iterators.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 12 page 1](../page_images/12_12_Iterators/page_001.png)

Extracted text:

```text
Iterators
Object-Oriented Programming with C++
```

## Page 2

![Lecture 12 page 2](../page_images/12_12_Iterators/page_002.png)

Extracted text:

```text
Iterators
•Provide a way to visit the elements in order,
  without knowing the details of the container.
  •Generalization of pointers
```

## Page 3

![Lecture 12 page 3](../page_images/12_12_Iterators/page_003.png)

Extracted text:

```text
Iterators
•Provide a way to visit the elements in order,
  without knowing the details of the container.
  •Generalization of pointers
•Separate container and algorithms with standard
  iterator interface functions.
  •The glue between algorithms and data structures
  •Without iterators, with N algorithms and M data
   structures, you need N*M implementations
```

## Page 4

![Lecture 12 page 4](../page_images/12_12_Iterators/page_004.png)

Extracted text:

```text
Iterators
•One of design patterns (Gang of Four):
  “Provide a way to access the elements of an aggregate object
  sequentially without exposing its underlying representation.”
```

## Page 5

![Lecture 12 page 5](../page_images/12_12_Iterators/page_005.png)

Extracted text:

```text
Iterators
template <class InputIterator, class T>
InputIterator find(InputIterator first,
                   InputIterator last,
                   const T &value)
{
  while (first!=last && *first!=value)
    ++first;
  return first;
}
```

## Page 6

![Lecture 12 page 6](../page_images/12_12_Iterators/page_006.png)

Extracted text:

```text
Iterators
template <class InputIterator, class T>
InputIterator find(InputIterator first,
                   InputIterator last,
                   const T &value)
{
  while (first!=last && *first!=value)
    ++first;
  return first;
}
```

## Page 7

![Lecture 12 page 7](../page_images/12_12_Iterators/page_007.png)

Extracted text:

```text
Iterators
vector<int> vecTemp;
list<double> listTemp;


if (find(vecTemp.begin(),vecTemp.end(),3) == vecTemp.end())
  cout << "3 not found in vecTemp" << endl;


if (find(listTemp.begin(),listTemp.end(),4) == listTemp.end())
  cout << "4 not found in listTemp" << endl;
```

## Page 8

![Lecture 12 page 8](../page_images/12_12_Iterators/page_008.png)

Extracted text:

```text
Iterators

•A unified interface used in algorithms
•Work like a pointer to the elements in a container
•Have ++ operator to visit elements in order
•Have * operator to visit the content of an element
```

## Page 9

![Lecture 12 page 9](../page_images/12_12_Iterators/page_009.png)

Extracted text:

```text
auto_ptr
•An example of overloading * and -> operator
  template<class T>
  class auto_ptr {
  private:
    T *pointee;
  public:
    …
    T& operator *() { return *pointee; }
    T* operator ->() { return pointee; }
    …
  };
```

## Page 10

![Lecture 12 page 10](../page_images/12_12_Iterators/page_010.png)

Extracted text:

```text
Iterators
Example code:
template<class T>           template<class T>
class List {                class ListItem {
public:                     public:
     void insert_front();        T& val() { return _value; }
     void insert_end();          ListItem *next() { return
…                                 _next};
private:                    …
     ListItem<T> *front;    private:
     ListItem<T> *end;           T _value;
     long _size;                 ListItem<T> *_next;
};                          };
```

## Page 11

![Lecture 12 page 11](../page_images/12_12_Iterators/page_011.png)

Extracted text:

```text
Iterators
template<class T>
class ListIter {
     ListItem<T> *ptr;
public:
     ListIter(ListItem<T> *p=0) : ptr(p) {}
     ListIter<Item>& operator++()
         { ptr = ptr->next(); return *this; }
     bool operator==(const ListIter& i) const
         { return ptr == i.ptr; }
     …
     T& operator*() { return ptr->val(); }
     T* operator->() { return &(**this);}
};
```

## Page 12

![Lecture 12 page 12](../page_images/12_12_Iterators/page_012.png)

Extracted text:

```text
Iterators
How to use ListIter:
List<int> myList;
… // insert elements

ListIter<int> begin = myList.begin();
ListIter<int> end = myList.end();
ListIter<int> iter;

iter = find(begin, end, 3);
if (iter == end)
  cout << "not found" << endl;
```

## Page 13

![Lecture 12 page 13](../page_images/12_12_Iterators/page_013.png)

Extracted text:

```text
Iterators
The associated type of an iterator:
// we do NOT know the data type of iter,
// so we need another variable v to infer T
template <class I, class T>
void func_impl(I iter, T& v)
{
  T tmp;
  tmp = *iter;
  // processing code here
}
```

## Page 14

![Lecture 12 page 14](../page_images/12_12_Iterators/page_014.png)

Extracted text:

```text
Iterators
The associated type of an iterator:
// a wrapper to extract the associated
// data type T
template <class I>
void func(I iter)
{
  func_impl(iter, *iter);
  // processing code here
}
```

## Page 15

![Lecture 12 page 15](../page_images/12_12_Iterators/page_015.png)

Extracted text:

```text
Iterators
The associated type of an iterator:
// a wrapper to extract the associated
// data type T
template <class I>
void func(I iter)
{
  func_impl(iter, *iter);
  // processing code here
}

However, we might need more type information that
associated to iterators
```

## Page 16

![Lecture 12 page 16](../page_images/12_12_Iterators/page_016.png)

Extracted text:

```text
Iterators
Define the type information for an iterator:
template <class T>
struct myIter {
     typedef T value_type;
     T* ptr;
     myIter(T *p = 0):ptr(p)
     {}
     T& operator*()
     { return *ptr; }
};
```

## Page 17

![Lecture 12 page 17](../page_images/12_12_Iterators/page_017.png)

Extracted text:

```text
Iterators
Define the type information for an iterator:
template <class T>             template <class I>
struct myIter {                typename I::value_type
     typedef T value_type;     func(I iter) {
     T* ptr;                       return *iter;
     myIter(T *p = 0):ptr(p)   }
     {}
     T& operator*()            // code
     { return *ptr; }          myIter<int> iter(new int(8));
};                             cout << func(iter);
```

## Page 18

![Lecture 12 page 18](../page_images/12_12_Iterators/page_018.png)

Extracted text:

```text
Iterators
The problem of the typedef trick:
  It cannot support pointer-type iterators, e.g.,
  int*,double*,Complex*, which cripples the
  STL programming.
```

## Page 19

![Lecture 12 page 19](../page_images/12_12_Iterators/page_019.png)

Extracted text:

```text
Iterators
The problem of the typedef trick:
    It cannot support pointer-type iterators, e.g.,
    int*,double*,Complex*, which cripples the
    STL programming.


Use iterator_traits trick:
template <class I>
struct iterator_traits {
    typedef typename I::value_type value_type;
}
```

## Page 20

![Lecture 12 page 20](../page_images/12_12_Iterators/page_020.png)

Extracted text:

```text
Iterators
How to use:
template <class I>
typename iterator_traits<I>::value_type
func(I iter) {
    return *iter;
}


// code
myIter<int> iter(new int(8));
cout << func(*iter);
```

## Page 21

![Lecture 12 page 21](../page_images/12_12_Iterators/page_021.png)

Extracted text:

```text
Template specialization
Primary template:
template<class T1, class T2, int I>
class A { … };
```

## Page 22

![Lecture 12 page 22](../page_images/12_12_Iterators/page_022.png)

Extracted text:

```text
Template specialization
Primary template:
template<class T1, class T2, int I>
class A { … };

Explicit (full) template specialization:
template<>
class A<int, double, 5> { … };
```

## Page 23

![Lecture 12 page 23](../page_images/12_12_Iterators/page_023.png)

Extracted text:

```text
Template specialization
Primary template:
template<class T1, class T2, int I>
class A { … };

Explicit (full) template specialization:
template<>
class A<int, double, 5> { … };

Partial template specialization:
template<class T2>
class A<int, T2, 3> { … };
```

## Page 24

![Lecture 12 page 24](../page_images/12_12_Iterators/page_024.png)

Extracted text:

```text
Iterators
The traits technique with template specialization:


template<class T>
class C
{
public:
  C() {
    cout<<"template
      T"<<endl;
  }
};
```

## Page 25

![Lecture 12 page 25](../page_images/12_12_Iterators/page_025.png)

Extracted text:

```text
Iterators
The traits technique with template specialization:


template<class T>            template<class T>
class C                      class C<T*>
{                            {
public:                      public:
  C() {                        C() {
    cout<<"template              cout<<"template
      T"<<endl;                   T*"<<endl;
  }                            }
};                           };
```

## Page 26

![Lecture 12 page 26](../page_images/12_12_Iterators/page_026.png)

Extracted text:

```text
Iterators
  The traits technique with template specialization:

template<class I>
class iterator_traits
{
public:
  typedef typename I::value_type value_type;
  typedef typename I::pointer_type pointer_type;
  ……
};
```

## Page 27

![Lecture 12 page 27](../page_images/12_12_Iterators/page_027.png)

Extracted text:

```text
Iterators
         The traits technique with template specialization:
template<class I>                      template<class T>
class iterator_traits                  class iterator_traits
{                                      <T*>
public:                                {
    typedef typename                   public:
     I::value_type value_type;             typedef T value_type;
    typedef typename                       typedef T* pointer_type;
     I:pointer_type pointer_type;          ……
    ……                                 };
};
```

## Page 28

![Lecture 12 page 28](../page_images/12_12_Iterators/page_028.png)

Extracted text:

```text
Iterators
         The traits technique with template specialization:
template<class I>                      template<class T>
class iterator_traits                  class iterator_traits
{                                      <const T*>
public:                                {
    typedef typename                   public:
     I::value_type value_type;             typedef T value_type;
    typedef typename                       typedef const T*
     I:pointer_type pointer_type;           pointer_type;
    ……                                     ……
};                                     };
```

## Page 29

![Lecture 12 page 29](../page_images/12_12_Iterators/page_029.png)

Extracted text:

```text
Iterators
     The standard traits technique in STL:
template<class I>
class iterator_traits
{
public:
    typedef typename I::iterator_category iterator_category;
    typedef typename I::value_type value_type;
    typedef typename I::difference_type differece_type;
    typedef typename I::pointer pointer;
    typedef typename I::reference reference;
    ……
}
```

## Page 30

![Lecture 12 page 30](../page_images/12_12_Iterators/page_030.png)

Extracted text:

```text
Iterators
The standard traits technique in STL:

                                   int *
   iterator_traits                 const int*
                                   list<int>::iterator
                                   deque<int>::iterator
                                   vector<int>::iterator
                                   MyIter
                                   …
      value_type
      difference_type
      pointer
      reference
      iterator_category
      …
```

## Page 31

![Lecture 12 page 31](../page_images/12_12_Iterators/page_031.png)

Extracted text:

```text
Iterators
Iterator category (types):
• InputIterator
• OutputIterator
• ForwardIterator
• BidirectionalIterator
• RandomAccessIterator
```

## Page 32

![Lecture 12 page 32](../page_images/12_12_Iterators/page_032.png)

Extracted text:

```text
Iterators
Iterator category (types):


     InputIterator           OutputIterator

                ForwardIterator

            BidirectionalIterator

             RandomAccessIterator
```

## Page 33

![Lecture 12 page 33](../page_images/12_12_Iterators/page_033.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class InputIterator, class Distance>
void advance_II(InputIterator &i, Distance n)
{
    while (n--) ++i;
}
```

## Page 34

![Lecture 12 page 34](../page_images/12_12_Iterators/page_034.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class BidirectionalIterator, class Distance>
void advance_BI(BidirectionalIterator &i, Distance n)
{
    if (n >= 0)
     while (n--) ++i;
    else
     while (n++) --i;
}
```

## Page 35

![Lecture 12 page 35](../page_images/12_12_Iterators/page_035.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class RandomAccessIterator, class Distance>
void advance_RAI(RandomAccessIterator &i, Distance n)
{
    i += n;
}
```

## Page 36

![Lecture 12 page 36](../page_images/12_12_Iterators/page_036.png)

Extracted text:

```text
Iterators
Iterator methods: advance()


But how to call them according to iterator types?
```

## Page 37

![Lecture 12 page 37](../page_images/12_12_Iterators/page_037.png)

Extracted text:

```text
Iterators
Use iterator category information:

struct input_iterator_tag {};
struct output_iterator_tag {};
struct forward_iterator_tag : public
  input_iterator_tag {};
struct bidirectional_iterator_tag : public
  forward_iterator_tag {};
struct random_access_iterator_tag : public
  bidirectional_iterator_tag {};
```

## Page 38

![Lecture 12 page 38](../page_images/12_12_Iterators/page_038.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class InputIterator, class Distance>
inline void __advance(InputIterator &i, Distance n,
                       input_iterator_tag)
{
    while (n--) ++i;
}
```

## Page 39

![Lecture 12 page 39](../page_images/12_12_Iterators/page_039.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class BidirectionalIterator, class Distance>
inline void __advance(BidirectionalIterator &i,
                          Distance n,
                          bidirectional_iterator_tag)
{
    if (n >= 0)
       while (n--) ++i;
     else
       while (n++) --i;
}
```

## Page 40

![Lecture 12 page 40](../page_images/12_12_Iterators/page_040.png)

Extracted text:

```text
Iterators
Iterator methods: advance()

template <class RandomAccessIterator, class Distance>
inline void __advance(RandomAccessIterator &i,
                      Distance n,
                      random_access_iterator_tag)
{
    i += n;
}
```

## Page 41

![Lecture 12 page 41](../page_images/12_12_Iterators/page_041.png)

Extracted text:

```text
Iterators
Use traits again!

template <class Iterator, class Distance>
inline void advance(Iterator &i, Distance n)
{
    __advance(i, n,
     iterator_traits<Iterator>::iterator_category());
}
```

## Page 42

![Lecture 12 page 42](../page_images/12_12_Iterators/page_042.png)

Extracted text:

```text
Iterators
Use traits again!

template <class Iterator, class Distance>
inline void advance(Iterator &i, Distance n)
{
    __advance(i, n,
     iterator_traits<Iterator>::iterator_category());
}

                                   Temporary object
```

## Page 43

![Lecture 12 page 43](../page_images/12_12_Iterators/page_043.png)

Extracted text:

```text
Iterators
Partial specialization for raw pointers
template <class I>
struct iterator_traits {
     …
     typedef typename I::iterator_category iterator_category;
};


template <class T>
struct iterator_traits<T*> {
     …
     typedef random_access_iterator_tag iterator_category;
};
```

## Page 44

![Lecture 12 page 44](../page_images/12_12_Iterators/page_044.png)

Extracted text:

```text
Iterators
Pure transfer can be removed due to inheritance

template <class ForwardIterator, class Distance>
inline void __advance(ForwardIterator &i, Distance n,
                       forward_iterator_tag)
{                                    Implicit conversion
    __advance(i, n, input_iterator_tag());
}
```

## Page 45

![Lecture 12 page 45](../page_images/12_12_Iterators/page_045.png)

Extracted text:

```text
Iterators
    Iterator methods: distance()
template <class InputIterator>
inline iterator_traits<InputIterator>::difference_type
__distance(InputIterator first, InputIterator last,
                input_iterator_tag)
{
    iterator_traits<InputIterator>::difference_type n=0;
    while (first != last) {
        ++first; ++n;
    }
    return n;
}
```

## Page 46

![Lecture 12 page 46](../page_images/12_12_Iterators/page_046.png)

Extracted text:

```text
Iterators
    Iterator methods: distance()
template <class RandomAccessIterator>
inline iterator_traits<InputIterator >::difference_type
__distance(RandomAccessIterator first,
             RandomAccessIterator last,
             random_access_iterator_tag)
{
    return last – first;
}
```

## Page 47

![Lecture 12 page 47](../page_images/12_12_Iterators/page_047.png)

Extracted text:

```text
Iterators
Iterator methods: distance()
template <class Iterator>
inline iterator_traits<Iterator>::difference_type
distance(Iterator first, Iterator last)
{
    return __distance(first, last,
     iterator_traits<Iterator>::iterator_category());
}
```

## Page 48

![Lecture 12 page 48](../page_images/12_12_Iterators/page_048.png)

Extracted text:

```text
Iterators
• Container knows how to design its own iterator.
• Traits trick extracts type information embedded in
  different iterators, including raw pointers.
• Algorithms are independent to containers
  through the design philosophy of iterators.
```
