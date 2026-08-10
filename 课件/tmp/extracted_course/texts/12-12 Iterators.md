# Lecture 12: 12 Iterators

Source: `12 Iterators.pdf`
Pages: 48

## Page 1

       Iterators
Object-Oriented Programming with C++

## Page 2

                  Iterators
•Provide a way to visit the elements in order,
  without knowing the details of the container.
  •Generalization of pointers

## Page 3

                  Iterators
•Provide a way to visit the elements in order,
  without knowing the details of the container.
  •Generalization of pointers
•Separate container and algorithms with standard
  iterator interface functions.
  •The glue between algorithms and data structures
  •Without iterators, with N algorithms and M data
   structures, you need N*M implementations

## Page 4

                     Iterators
•One of design patterns (Gang of Four):
  “Provide a way to access the elements of an aggregate object
  sequentially without exposing its underlying representation.”

## Page 5

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

## Page 6

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

## Page 7

                         Iterators
vector<int> vecTemp;
list<double> listTemp;


if (find(vecTemp.begin(),vecTemp.end(),3) == vecTemp.end())
  cout << "3 not found in vecTemp" << endl;


if (find(listTemp.begin(),listTemp.end(),4) == listTemp.end())
  cout << "4 not found in listTemp" << endl;

## Page 8

                  Iterators

•A unified interface used in algorithms
•Work like a pointer to the elements in a container
•Have ++ operator to visit elements in order
•Have * operator to visit the content of an element

## Page 9

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

## Page 10

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

## Page 11

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

## Page 12

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

## Page 13

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

## Page 14

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

## Page 15

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

## Page 16

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

## Page 17

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

## Page 18

                 Iterators
The problem of the typedef trick:
  It cannot support pointer-type iterators, e.g.,
  int*,double*,Complex*, which cripples the
  STL programming.

## Page 19

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

## Page 20

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

## Page 21

  Template specialization
Primary template:
template<class T1, class T2, int I>
class A { … };

## Page 22

   Template specialization
Primary template:
template<class T1, class T2, int I>
class A { … };

Explicit (full) template specialization:
template<>
class A<int, double, 5> { … };

## Page 23

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

## Page 24

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

## Page 25

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

## Page 26

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

## Page 27

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

## Page 28

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

## Page 29

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

## Page 30

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

## Page 31

                  Iterators
Iterator category (types):
• InputIterator
• OutputIterator
• ForwardIterator
• BidirectionalIterator
• RandomAccessIterator

## Page 32

                  Iterators
Iterator category (types):


     InputIterator           OutputIterator

                ForwardIterator

            BidirectionalIterator

             RandomAccessIterator

## Page 33

                   Iterators
Iterator methods: advance()

template <class InputIterator, class Distance>
void advance_II(InputIterator &i, Distance n)
{
    while (n--) ++i;
}

## Page 34

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

## Page 35

                 Iterators
Iterator methods: advance()

template <class RandomAccessIterator, class Distance>
void advance_RAI(RandomAccessIterator &i, Distance n)
{
    i += n;
}

## Page 36

                 Iterators
Iterator methods: advance()


But how to call them according to iterator types?

## Page 37

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

## Page 38

                   Iterators
Iterator methods: advance()

template <class InputIterator, class Distance>
inline void __advance(InputIterator &i, Distance n,
                       input_iterator_tag)
{
    while (n--) ++i;
}

## Page 39

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

## Page 40

                 Iterators
Iterator methods: advance()

template <class RandomAccessIterator, class Distance>
inline void __advance(RandomAccessIterator &i,
                      Distance n,
                      random_access_iterator_tag)
{
    i += n;
}

## Page 41

                      Iterators
Use traits again!

template <class Iterator, class Distance>
inline void advance(Iterator &i, Distance n)
{
    __advance(i, n,
     iterator_traits<Iterator>::iterator_category());
}

## Page 42

                      Iterators
Use traits again!

template <class Iterator, class Distance>
inline void advance(Iterator &i, Distance n)
{
    __advance(i, n,
     iterator_traits<Iterator>::iterator_category());
}

                                   Temporary object

## Page 43

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

## Page 44

                   Iterators
Pure transfer can be removed due to inheritance

template <class ForwardIterator, class Distance>
inline void __advance(ForwardIterator &i, Distance n,
                       forward_iterator_tag)
{                                    Implicit conversion
    __advance(i, n, input_iterator_tag());
}

## Page 45

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

## Page 46

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

## Page 47

                   Iterators
Iterator methods: distance()
template <class Iterator>
inline iterator_traits<Iterator>::difference_type
distance(Iterator first, Iterator last)
{
    return __distance(first, last,
     iterator_traits<Iterator>::iterator_category());
}

## Page 48

                 Iterators
• Container knows how to design its own iterator.
• Traits trick extracts type information embedded in
  different iterators, including raw pointers.
• Algorithms are independent to containers
  through the design philosophy of iterators.
