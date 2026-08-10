# Lecture 06: 6 Polymorphism

- Source: `6 Polymorphism.pdf`
- Pages: 40
- Rendered page images: 40
- Contact sheet: [open](../contact_sheets/06_6_Polymorphism_contact.jpg)
- Raw extracted text: [open](../raw_texts/06-6 Polymorphism.md)

> 使用说明：每一页都保留了原始页面图片。图片下方是自动抽取的文字；如果某页文字很少或为空，请以页面图片为准。

## Page 1

![Lecture 6 page 1](../page_images/06_6_Polymorphism/page_001.png)

Extracted text:

```text
Polymorphism
Object-Oriented Programming with C++
```

## Page 2

![Lecture 6 page 2](../page_images/06_6_Polymorphism/page_002.png)

Extracted text:

```text
A drawing program

                             Rectangle
             Circle
                                         Ellipse


Operations
 - render             Data
 - move          + center
 - resize
```

## Page 3

![Lecture 6 page 3](../page_images/06_6_Polymorphism/page_003.png)

Extracted text:

```text
Inheritance in C++
• Can define one class in terms of another                  Ellipse
• Can capture the notion that
  –An ellipse is a shape
                                                         Shap
  –A circle is a special kind of ellipse
                                                         e
  –A rectangle is a different shape
  –Circles, ellipses, and rectangles share common               Circle
    •attributes
    •services
  –Circles, ellipses, and rectangles are not identical
```

## Page 4

![Lecture 6 page 4](../page_images/06_6_Polymorphism/page_004.png)

Extracted text:

```text
Conceptual model
                                       center
                       Shape           move()
                                       render()

Rectangle render()
                                       Ellipse         render()




  Square         render()               Circle         render()


Note: Deriving Circle from Ellipse may be a poor design choice!
```

## Page 5

![Lecture 6 page 5](../page_images/06_6_Polymorphism/page_005.png)

Extracted text:

```text
Shape
• Define the general properties of a Shape
 class Point {...};    // (x,y) point
 class Shape {
 public:
     Shape();
     void move(const Point&);
     virtual void render();
     virtual void resize();
     virtual ~Shape();
 protected:
     Point center;
 }
```

## Page 6

![Lecture 6 page 6](../page_images/06_6_Polymorphism/page_006.png)

Extracted text:

```text
Add new shapes
class Ellipse: public Shape {
public:
    Ellipse(float major, float minor);
    virtual void render(); // will define own
protected:
    float major_axis, minor_axis;
};

class Circle: public Ellipse {
public:
    Circle(float radius) : Ellipse(radius, radius) {}
    virtual void render();
};
```

## Page 7

![Lecture 6 page 7](../page_images/06_6_Polymorphism/page_007.png)

Extracted text:

```text
Example
void render(Shape* p){
    p->render();     // calls correct render function
}                    // for given Shape!

void func(){
    Ellipse ell(10, 20);
    ell.render();
    Circle circ(40);
    circ.render();
    render(&ell);
    render(&circ);
}
```

## Page 8

![Lecture 6 page 8](../page_images/06_6_Polymorphism/page_008.png)

Extracted text:

```text
Example
void render(Shape* p){
    p->render();     // calls correct render function
}                    // for given Shape!

void func(){
    Ellipse ell(10, 20);
    ell.render();
    Circle circ(40);
    circ.render();
    render(&ell);
    render(&circ);
}

code & demo
```

## Page 9

![Lecture 6 page 9](../page_images/06_6_Polymorphism/page_009.png)

Extracted text:

```text
Polymorphism
```

## Page 10

![Lecture 6 page 10](../page_images/06_6_Polymorphism/page_010.png)

Extracted text:

```text
Polymorphism
• Upcast: take an object of the derived class as
  an object of the base one.
  –Ellipse can be treated as a Shape
```

## Page 11

![Lecture 6 page 11](../page_images/06_6_Polymorphism/page_011.png)

Extracted text:

```text
Polymorphism
• Upcast: take an object of the derived class as
  an object of the base one.
  –Ellipse can be treated as a Shape
• Dynamic binding:
  –Binding: which function to be called
    •Static binding: call the function as the declared type
    •Dynamic binding: call the function according to the
     “real” type of the object
```

## Page 12

![Lecture 6 page 12](../page_images/06_6_Polymorphism/page_012.png)

Extracted text:

```text
How virtual works in C++
class Shape {
public:
   Shape();
   virtual ~Shape();
   virtual void render();
   void move(const
     Point&);
   virtual void resize();
protected:
   Point center;
};

code & demo
```

## Page 13

![Lecture 6 page 13](../page_images/06_6_Polymorphism/page_013.png)

Extracted text:

```text
How virtual works in C++
class Shape {               A Shape
public:
   Shape();                    vptr
   virtual ~Shape();
                              center
   virtual void render();
                                       Shape
   void move(const                     vtable
     Point&);
   virtual void resize();              Shape::dtor()
protected:                             Shape::render()
   Point center;
                                       Shape::resize()
};
```

## Page 14

![Lecture 6 page 14](../page_images/06_6_Polymorphism/page_014.png)

Extracted text:

```text
Ellipse
class Ellipse: public Shape{   An Ellipse
public:
    Ellipse(float major,            vptr
            float minor);
                                   center
    virtual void render();
                                 major_axis   Ellipse vtable
protected:
                                 minor_axis
    float major_axis,;
                                               Ellipse::dtor()
    float minor_axis;
};                                            Ellipse::render()

                                              Shape::resize()
```

## Page 15

![Lecture 6 page 15](../page_images/06_6_Polymorphism/page_015.png)

Extracted text:

```text
Shape vs. Ellipse
A Shape                         An Ellipse


   vptr                              vptr

  center                            center

              Shape               major_axis   Ellipse vtable
              vtable
                                  minor_axis
              Shape::dtor()                     Ellipse::dtor()

              Shape::render()                  Ellipse::render()

              Shape::resize()                  Shape::resize()
```

## Page 16

![Lecture 6 page 16](../page_images/06_6_Polymorphism/page_016.png)

Extracted text:

```text
Circle
class Circle: public Ellipse{
                                A Circle
public:
                                    vptr
    Circle(float radius);
    virtual void render();         center
    virtual void resize();
                                major_axis
    virtual float radius();                    Circle vtable
                                minor_axis
protected:                                    Circle::dtor()
    float area;                     area
                                             Circle::render()
};                                           Circle::resize()

                                             Circle::radius()
 code & demo
```

## Page 17

![Lecture 6 page 17](../page_images/06_6_Polymorphism/page_017.png)

Extracted text:

```text
What happens if
```

## Page 18

![Lecture 6 page 18](../page_images/06_6_Polymorphism/page_018.png)

Extracted text:

```text
What happens if
Ellipse elly(20F, 40F);
Circle circ(60F);
elly = circ; // ?

code & demo
```

## Page 19

![Lecture 6 page 19](../page_images/06_6_Polymorphism/page_019.png)

Extracted text:

```text
What happens if
   Ellipse elly(20F, 40F);
   Circle circ(60F);
   elly = circ;


• Area of circ is sliced off
  –(Only the part of circ that fits in elly gets copied)
```

## Page 20

![Lecture 6 page 20](../page_images/06_6_Polymorphism/page_020.png)

Extracted text:

```text
What happens if
   Ellipse elly(20F, 40F);
   Circle circ(60F);
   elly = circ;


• Area of circ is sliced off
  –(Only the part of circ that fits in elly gets copied)
• Vptr from circ is ignored; the vptr in elly points to
  the Ellipse vtable

   (&elly)->render(); // Ellipse::render()
```

## Page 21

![Lecture 6 page 21](../page_images/06_6_Polymorphism/page_021.png)

Extracted text:

```text
What happens with pointers?
```

## Page 22

![Lecture 6 page 22](../page_images/06_6_Polymorphism/page_022.png)

Extracted text:

```text
What happens with pointers?
  Ellipse* elly = new Ellipse(20F, 40F);
  Circle* circ = new Circle(60F);
  elly = circ;
```

## Page 23

![Lecture 6 page 23](../page_images/06_6_Polymorphism/page_023.png)

Extracted text:

```text
What happens with pointers?
   Ellipse* elly = new Ellipse(20F, 40F);
   Circle* circ = new Circle(60F);
   elly = circ;


• Well, the original Ellipse for elly is lost....
```

## Page 24

![Lecture 6 page 24](../page_images/06_6_Polymorphism/page_024.png)

Extracted text:

```text
What happens with pointers?
   Ellipse* elly = new Ellipse(20F, 40F);
   Circle* circ = new Circle(60F);
   elly = circ;


• Well, the original Ellipse for elly is lost....
• elly and circ point to the same Circle object!

   elly->render(); // Circle::render()
```

## Page 25

![Lecture 6 page 25](../page_images/06_6_Polymorphism/page_025.png)

Extracted text:

```text
Virtual and reference arguments
```

## Page 26

![Lecture 6 page 26](../page_images/06_6_Polymorphism/page_026.png)

Extracted text:

```text
Virtual and reference arguments
  void func(Ellipse& elly) {
    elly.render();
  }

  Circle circ(60F);
  func(circ);
```

## Page 27

![Lecture 6 page 27](../page_images/06_6_Polymorphism/page_027.png)

Extracted text:

```text
Virtual and reference arguments
   void func(Ellipse& elly) {
     elly.render();
   }

   Circle circ(60F);
   func(circ);

• References act like pointers
```

## Page 28

![Lecture 6 page 28](../page_images/06_6_Polymorphism/page_028.png)

Extracted text:

```text
Virtual and reference arguments
   void func(Ellipse& elly) {
     elly.render();
   }

   Circle circ(60F);
   func(circ);

• References act like pointers
• Circle::render() is called
```

## Page 29

![Lecture 6 page 29](../page_images/06_6_Polymorphism/page_029.png)

Extracted text:

```text
Virtual destructors
• Make destructors virtual if they might be inherited
   Shape *p = new Ellipse(100.0F, 200.0F);
   ...
   delete p;
• If Shape::~Shape() is not virtual, only
  Shape::~Shape() will be invoked!
• Want Ellipse::~Ellipse() to be called
  – Must declare Shape::~Shape() virtual
  – It will call Shape::~Shape() internally
```

## Page 30

![Lecture 6 page 30](../page_images/06_6_Polymorphism/page_030.png)

Extracted text:

```text
Overriding
• Overriding redefines the body of a virtual function
   class Base {
   public:
      virtual void func();
   }
   class Derived : public Base {
   public:
      void func() override;
      //overrides Base::func()
   }
```

## Page 31

![Lecture 6 page 31](../page_images/06_6_Polymorphism/page_031.png)

Extracted text:

```text
Calls up the chain
• You can still call the overridden function for reuse:

void Derived::func() {

    cout << "In Derived::func!";
    Base::func(); // call to base class
}
• This is a common way to add new functionality
• No need to copy the old stuff!
```

## Page 32

![Lecture 6 page 32](../page_images/06_6_Polymorphism/page_032.png)

Extracted text:

```text
Return types relaxation (current)
• Suppose D is publicly derived from B

• D::f() can return a subclass of the return type
  defined in B::f()

• Applies to pointer and reference types

  – e.g. D&, D*

• In most compilers now
```

## Page 33

![Lecture 6 page 33](../page_images/06_6_Polymorphism/page_033.png)

Extracted text:

```text
Relaxation example
class Expr{
public:
    virtual Expr* newExpr();
    virtual Expr& clone();
    virtual Expr self();
};

class BinaryExpr: public Expr{
public:
    virtual BinaryExpr* newExpr(); // ok
    virtual BinaryExpr& clone();   // ok
    virtual BinaryExpr self();     // Error!
};
```

## Page 34

![Lecture 6 page 34](../page_images/06_6_Polymorphism/page_034.png)

Extracted text:

```text
Overloading and virtual
• Overloading adds multiple signatures
  class Base {
     public:
          virtual void func();
          virtual void func(int);
     };
• If you override an overloaded function, you
  must override all of the variants!
 –Can't override just one
 –If you don't override all, some will be hidden
```

## Page 35

![Lecture 6 page 35](../page_images/06_6_Polymorphism/page_035.png)

Extracted text:

```text
Overloading example
• When you override an overloaded function,
  override all of the variants!

 class Derived: public Base{
 public:
     virtual void func(){
         Base::func();
     }
     virtual void func(int) { ... };
 }
```

## Page 36

![Lecture 6 page 36](../page_images/06_6_Polymorphism/page_036.png)

Extracted text:

```text
Tips
• Never redefine an inherited non-virtual
  function
  –Non-virtuals are statically bound
  –No dynamic dispatch!
• Never redefine an inherited default
  parameter value
  –They’re statically bound too!
  –And what would it mean?
```

## Page 37

![Lecture 6 page 37](../page_images/06_6_Polymorphism/page_037.png)

Extracted text:

```text
[No extractable text]
```

## Page 38

![Lecture 6 page 38](../page_images/06_6_Polymorphism/page_038.png)

Extracted text:

```text
Abstract classes
• Why use them?
 – Modeling
 – Force correct behavior
 – Define interface without defining an implementation
• When to use them?
 – Not enough information is available
 – When designing for interface inheritance
```

## Page 39

![Lecture 6 page 39](../page_images/06_6_Polymorphism/page_039.png)

Extracted text:

```text
Protocol / Interface classes
• Abstract base class with
  – All non-static member functions are pure virtual except
    destructor
  – Virtual destructor with empty body
  – No non-static member variables, inherited or
    otherwise
    •May contain static members
```

## Page 40

![Lecture 6 page 40](../page_images/06_6_Polymorphism/page_040.png)

Extracted text:

```text
Example interface
• Unix character device
   class CDevice {
   public:
       virtual ~CDevice() {}

        virtual int read(...) = 0;
        virtual int write(...) = 0;
        virtual int open(...) = 0;
        virtual int close(...) = 0;
        virtual int ioctl(...) = 0;
   };
```
