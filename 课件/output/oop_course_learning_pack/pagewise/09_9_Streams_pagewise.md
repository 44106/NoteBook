# Lecture 09: 9 Streams

- Source: `9 Streams.pdf`
- Pages: 27
- Rendered page images: 27
- Contact sheet: [open](../contact_sheets/09_9_Streams_contact.jpg)
- Raw extracted text: [open](../raw_texts/09-9 Streams.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 9 page 1](../page_images/09_9_Streams/page_001.png)

Extracted text:

```text
Streams
Object-Oriented Programming with C++
```

## Page 2

![Lecture 9 page 2](../page_images/09_9_Streams/page_002.png)

Extracted text:

```text
Why streams?
• Original C I/O used printf, scanf
```

## Page 3

![Lecture 9 page 3](../page_images/09_9_Streams/page_003.png)

Extracted text:

```text
Why streams?
• Original C I/O used printf, scanf
• Streams introduced in C++
  – C I/O libraries still work
• Advantages of streams
  – Better type safety
  – Extensible
  – More object-oriented
```

## Page 4

![Lecture 9 page 4](../page_images/09_9_Streams/page_004.png)

Extracted text:

```text
Why streams?
• Original C I/O used printf, scanf
• Streams introduced in C++
  – C I/O libraries still work
• Advantages of streams
  – Better type safety
  – Extensible
  – More object-oriented
• Disadvantages
  – More verbose (std::format comes back in C++20)
  – Might be slower
     – Turn off synchronization:
          std::ios::sync_with_stdio(false);
```

## Page 5

![Lecture 9 page 5](../page_images/09_9_Streams/page_005.png)

Extracted text:

```text
C vs. C++
• C stdio operations work
 – No “object-oriented” features
 – No overloadable operators
• C++
 – Can overload inserters and extractors
• Moral
 – When converting C to C++, leave the I/O intact
```

## Page 6

![Lecture 9 page 6](../page_images/09_9_Streams/page_006.png)

Extracted text:

```text
What is a stream?
• Common logical interface to a device
 – One-dimension, unidirectional
 – Random access on file, but not on std::cin/cout
```

## Page 7

![Lecture 9 page 7](../page_images/09_9_Streams/page_007.png)

Extracted text:

```text
Stream naming convections
                 Input           Output          Header
Generic          istream         ostream         <iostream>
File             ifstream        ofstream        <fstream>
C string (legacy) istrstream     ostrstream      <strstream>
C++ string       istringstream   ostringstream   <sstream>
```

## Page 8

![Lecture 9 page 8](../page_images/09_9_Streams/page_008.png)

Extracted text:

```text
Stream operations
• Extractors
  – Read a value from the stream
  – Overload the >> operator
• Inserters
  – Insert a value into a stream
  – Overload the << operator
• Manipulators
  – Change the stream state
```

## Page 9

![Lecture 9 page 9](../page_images/09_9_Streams/page_009.png)

Extracted text:

```text
Kinds of streams
• Text streams
 – Deal with ASCII text
 – Perform some characters translation
   – e.g.: newline -> actual OS file representation
 – Include
   – Files
   – Character buffers
• Binary streams
 – Binary data
 – No translation
```

## Page 10

![Lecture 9 page 10](../page_images/09_9_Streams/page_010.png)

Extracted text:

```text
Predefined streams
• cin
  – standard input
• cout
  – standard output
• cerr
  – unbuffered error (debugging) output
• clog
  – buffered error (debugging) output
```

## Page 11

![Lecture 9 page 11](../page_images/09_9_Streams/page_011.png)

Extracted text:

```text
Examples
#include <iostream>
int i; float f; char c;
char buffer[80];
• Read the next character
  cin >> c;
• Read an integer
  cin >> i; // skips whitespace
• Read a float and a string separated by
  whitespace
  cin >> f >> buffer;
```

## Page 12

![Lecture 9 page 12](../page_images/09_9_Streams/page_012.png)

Extracted text:

```text
Predefined extractors
•istream >> lvalue
    Expression type   input format            C I/O
    char              Character               %c
    short, int        Integer                 %d
    long              Long decimal integer    %ld
    float             Floating point          %g
    double            Double precision flp.   %lg
    char []           String                  %s
    void *            Pointer                 %p


• Extractors skip leading whitespace, in general
```

## Page 13

![Lecture 9 page 13](../page_images/09_9_Streams/page_013.png)

Extracted text:

```text
Defining a stream extractor
• Has to be a 2-argument free function
– First argument is an istream&
 – Second argument is a reference to a value

    istream& operator>>(istream& is, T& obj) {
        // specific code to read obj
        return is;
    }
```

## Page 14

![Lecture 9 page 14](../page_images/09_9_Streams/page_014.png)

Extracted text:

```text
Defining a stream extractor
• Has to be a 2-argument free function
– First argument is an istream&
 – Second argument is a reference to a value

    istream& operator>>(istream& is, T& obj) {
        // specific code to read obj
        return is;
    }

• Return an istream& for chaining
    cin >> a >> b >> c;
    ((cin >> a) >> b) >> c;
```

## Page 15

![Lecture 9 page 15](../page_images/09_9_Streams/page_015.png)

Extracted text:

```text
Other input operators
•int get()
 • Returns the next character in the stream
 • Returns EOF if no characters left
 • Example: copy input to output
    int ch;
    while ((ch = cin.get()) != EOF)
      cout.put(ch);

•istream& get(char& ch)
 • Reads the next character into argument
 • Similar to int get();
```

## Page 16

![Lecture 9 page 16](../page_images/09_9_Streams/page_016.png)

Extracted text:

```text
More input operators
• get(char *buf, int limit, char delim='\n')
  • Read up to limit characters, or to delim
  • Appends a null character to buf
 • Does not consume the delimiter
• getline(char *buf, int limit, char delim='\n')
  • Read up to limit characters, or to delim
  • Appends a null character to buf
 • Does consume the delimiter
• ignore(int limit=1, int delim = EOF)
 • Skip over limit characters or to delimiter
 • Skip over delimiter if found
```

## Page 17

![Lecture 9 page 17](../page_images/09_9_Streams/page_017.png)

Extracted text:

```text
More input operators
• int gcount()
 • Returns number of characters just read
     char buffer[100];
     cin.getline(buffer, sizeof(buffer));
     cout << "read" << cin.gcount()
          << " characters"
• void putback(char c)
 • Pushes a single character back into the stream
• char peek()
 • Examines the next character without consuming it
   switch(cin.peek()) …
```

## Page 18

![Lecture 9 page 18](../page_images/09_9_Streams/page_018.png)

Extracted text:

```text
Predefined inserters
• Usage
 – ostream << expression
    Expression type   Output format           C I/O
    char              Character               %c
    short, int        Integer                 %d
    long              Long decimal integer    %ld
    float             Floating point          %g
    double            Double precision flp.   %lg
    char []           String                  %s
    void *            Pointer                 %p
```

## Page 19

![Lecture 9 page 19](../page_images/09_9_Streams/page_019.png)

Extracted text:

```text
Creating a stream inserter
```

## Page 20

![Lecture 9 page 20](../page_images/09_9_Streams/page_020.png)

Extracted text:

```text
Creating a stream inserter
• Has to be a 2-argument free function
 – First argument is an ostream&
 – Second argument is any value
  ostream& operator<<(ostream& os, const T& obj) {
      // specific code to write obj
      return os;
  }

• Return an ostream& for chaining
   cout << a << b << c;
   ((cout << a) << b) << c;
```

## Page 21

![Lecture 9 page 21](../page_images/09_9_Streams/page_021.png)

Extracted text:

```text
Other output operators
•put(char)
 • Prints a single character
 • Examples
   cout.put('a');
   cerr.put('!');

•flush()
 • Force output of stream contents
 • Example
   cout << "Enter a number";
   cout.flush();
```

## Page 22

![Lecture 9 page 22](../page_images/09_9_Streams/page_022.png)

Extracted text:

```text
Formatting using manipulators
• Manipulators modify the state of the stream
  • #include <iomanip>
  • Effects hold (usually)
• Example
    int n;
    cout << "enter number in hexadecimal"
         << endl;
    cin >> hex >> n;
```

## Page 23

![Lecture 9 page 23](../page_images/09_9_Streams/page_023.png)

Extracted text:

```text
Example
• A simple program
    #include <iostream>
    #include <iomanip>
    int main() {
      cout << setprecision(2) << 1230.243 << endl;
      cout << setw(20) << "OK!";
      return 0;
    }
• Prints
    1.2e+03
                     OK!
```

## Page 24

![Lecture 9 page 24](../page_images/09_9_Streams/page_024.png)

Extracted text:

```text
Manipulators
Manipulator           Effect                         Type
dec, hex, oct         Set numeric conversion         I, O
endl                  Insert newline and flush       O
flush                 Flush stream                   O
setw(int)             Set field width                I, O
setfill(ch)           Change fill character          I, O
setbase(int)          Set number base                O
ws                    Skip whitespace                I
setprecision(int)     Set floating point precision   O
setiosflags(long)     Turn on specified flags        I, O
resetiosflags(long)   Turn off specified flags       I, O
```

## Page 25

![Lecture 9 page 25](../page_images/09_9_Streams/page_025.png)

Extracted text:

```text
Creating manipulators
• You can define your own manipulators!
    // skeleton for an output stream manipulator
    ostream& manip(ostream& out) {
       ...
       return out;
    }
    ostream& tab(ostream& out) {
       return out << '\t';
    }
    cout << "Hello" << tab << "World!" << endl;
```

## Page 26

![Lecture 9 page 26](../page_images/09_9_Streams/page_026.png)

Extracted text:

```text
Stream flags control formatting
    Flag                           Purpose (when set)
    ios::skipws                    Skip leading white space
    ios::left, ios::right          Justification
    ios::internal                  Pad between sign and value
    ios::dec, ios::oct, ios::hex   Format for numbers
    ios::showbase                  Show base of number
    ios::showpoint                 Always show decimal point
    ios::uppercase                 Put base in uppercase
    ios::showpos                   Display + on positive numbers
    ios::scientific, ios::fixed    Floating point format
    ios::unitbuf                   Flush on every write
```

## Page 27

![Lecture 9 page 27](../page_images/09_9_Streams/page_027.png)

Extracted text:

```text
Setting flags
• Using manipulators
  – setiosflags(flags);
  – resetiosflags(flags);
• Using stream member functions
  – setf(flags);
  – unsetf(flags);
```
