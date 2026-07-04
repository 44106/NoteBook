# c++练习题目四：运算符重载

说明：已保留带明确答案的题目，少数题干做了规范化；个别原文带有 Java 风格措辞的题目，按原题意保留。

## 题目与答案

### 重载规则与写法

**2-1**. For overloading `()` , `[]` or `->` operators, a class ________.
- A. Must use static member functions
- B. Must use non-static member functions
- C. Must be non-static member and should not be friend of class
- D. Must use static member function or a friend member function
- **答案：** B. Must use non-static member functions
- **解析：** 这三个运算符只能通过非静态成员函数重载。

**2-2**. Which among the following are valid ways of overloading the operators?
- A. Only using friend function
- B. Only using member function
- C. Either member functions or friend functions can be used
- D. perators can’t be overloaded
- **答案：** C. Either member functions or friend functions can be used
- **解析：** 题库考的是运算符重载规则，正确项是“Either member functions or friend functions can be used”。

**2-3**. Which of the following is the intended rule for operator overloading?
- A. Overloaded operator must be member function of the left operand
- B. Overloaded operator must be member function of the right operand
- C. Overloaded operator must be member function of either left or right operand
- D. Overloaded operator must not be dependent on the operands
- **答案：** C. Overloaded operator must be member function of either left or right operand
- **解析：** 题库这里想表达的是：运算符重载要遵守成员函数/友元函数的实现规则。

**2-4**. When the operator to be overloaded becomes the left operand member then ______________
- A. The right operand acts as implicit object represented by *this
- B. The left operand acts as implicit object represented by *this
- C. Either right or left operand acts as implicit object represented by *this
- D. *this pointer is not applicable in that member function
- **答案：** B. The left operand acts as implicit object represented by *this
- **解析：** 题库考的是运算符重载规则，正确项是“The left operand acts as implicit object represented by *this”。

**2-5**. If the left operand is pointed by *this pointer, what happens to other operands?
- A. Other operands are passed as function return type
- B. Other operands are passed to compiler implicitly
- C. Other operands must be passed using another member function
- D. Other operands are passed as function arguments
- **答案：** D. Other operands are passed as function arguments
- **解析：** 按题库对应概念，正确项是“Other operands are passed as function arguments”。

**2-6**. If a friend overloaded operator have to be changed to member overloaded operator, which operator should be used with the class name?
- A. Scope resolution operator
- B. Colon
- C. Arrow operator
- D. Dot operator
- **答案：** A. Scope resolution operator
- **解析：** 题库考的是运算符重载规则，正确项是“Scope resolution operator”。

**2-7**. What is the syntax to overload an operator?
- A. className::operator(parameters)
- B. className:operator(parameters)
- C. className.operator(paramteres)
- D. className->operator(parameters)
- **答案：** A. className::operator(parameters)
- **解析：** 成员运算符重载通常写成 `ClassName::operator<op>(...)`。

**2-8**. Which object’s members can be called directly while overloading operator function is used (In function definition)?
- A. Left operand members
- B. Right operand members
- C. All operand members
- D. None of the members
- **答案：** A. Left operand members
- **解析：** 题库考的是运算符重载规则，正确项是“Left operand members”。

**2-9**. If left operand member is specified directly in the function definition, which is the correct implicit conversion of that syntax?
- A. *this className
- B. *this parameterObject
- C. *this returnedObject
- D. *this object
- **答案：** D. *this object
- **解析：** 按题库对应概念，正确项是“*this object”。

**2-10**. When the friend operator overloading is converted into member operator overloading _______________
- A. Two parameters of friend function remains same parameters in member operator overloading
- B. Two parameters of friend function becomes only one parameter of member function
- C. Two parameters of friend function are removed while using member function
- D. Two parameters of friend function are made 4 in member operator overloading
- **答案：** B. Two parameters of friend function becomes only one parameter of member function
- **解析：** 题库考的是运算符重载规则，正确项是“Two parameters of friend function becomes only one parameter of member function”。

### 可重载运算符与典型结论

**2-11**. Which operator among the following can be overloading using only member function?
- A. Assignment operator
- B. Addition operator
- C. Subtraction operator
- D. Multiplication and division operator
- **答案：** A. Assignment operator
- **解析：** 题库考的是运算符重载规则，正确项是“Assignment operator”。

**2-12**. Which operator among the following can be overloaded using both friend function and member function?
- A. Assignment operator
- B. Subscript
- C. Member selection (arrow operator)
- D. Modulus operator
- **答案：** D. Modulus operator
- **解析：** 题库考的是运算符重载规则，正确项是“Modulus operator”。

**2-13**. Which of the following statements about friend functions in operator overloading is correct?
- A. << operator only
- B. operator only
- C. Both << and >> operators
- D. It’s not mandatory to use friend function in any case
- **答案：** D. It’s not mandatory to use friend function in any case
- **解析：** 并非所有运算符都必须用友元函数，`<<` 和 `>>` 只是常见写法。

**2-14**. Which feature in OOP is used to allocate additional function to a predefined operator in any language?
- A. Operator Overloading
- B. Function Overloading
- C. Operator Overriding
- D. Function Overriding
- **答案：** A. Operator Overloading
- **解析：** 题库考的是运算符重载规则，正确项是“Operator Overloading”。
