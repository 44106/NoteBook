# Raw Extract: 12-davinci-tpu [自动保存的].pptx

- Slides: 122

## Slide 1

### Shape 1 Rectangle 4

Computer Arch. & AI SystemsLecture 12: AI Processors

### Alt/Text Metadata 1

Rectangle 4

### Shape 2 Rectangle 5

Prof. Zeke Wang
Zhejiang University
May 21 2026

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- 1

## Slide 2

### Shape 1 Title 1

Recall:深度学习算法计算和访存特性分析

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

2

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

MAC (Multiply–Accumulate)

### Alt/Text Metadata 3

Rectangle 4

### Table 4 Table 5

- Operator | 计算特性 | 访存特性
- Conv | 矩阵相乘 | Burst+stride
- Activation | 单向量操作 | Sequential
- Pooling | 单矩阵Reduce操作 | Burst+stride
- FC | 矩阵相乘 | Sequential

### Alt/Text Metadata 4

Table 5

### Shape 5 Rectangle 9

Fixed Memory Access Pattern

### Alt/Text Metadata 5

Rectangle 9

### Shape 6 Rectangle 10

AI相关计算内，矩阵乘法计算量的占比高于90%。

### Alt/Text Metadata 6

Rectangle 10

### Table 7 表格 17

- Attention | 矩阵相乘 | Burst+stride

### Alt/Text Metadata 7

表格 17

### XML fallback texts

- Operator
- Conv
- 相乘
- B
- urst
- +stride
- Activation
- 单
- 向量
- 操作
- Sequential
- Pooling
- Reduce
- FC
- Attention
- Burst+stride

### Notes XML fallback texts

- 17

### Slide media/diagram relationships

- rId3: image:../media/image2.emf
- rId5: image:../media/image3.emf

## Slide 3

### Shape 1 Title 1

Recall: Five Design Principles of AI Accelerators

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

3

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Five Design Principles:
Global Buffer: 使用专有的存储器来减少数据搬运的距离与开销，比如将复杂的cache设计替换成scratchpad memory (global buffer)。
简化控制模块: 将缩减的高级微架构特性而节省出的面积，用于增加更多的运算单元或者片上存储。
并行计算模块: 使用能够符合特定领域加速需求最简单的并行形式，例如，对于矩阵运算的加速，单条指令直接支持小矩阵运算。
量化: 减少计算数据尺寸与类型来符合特定领域性能要求，例如，深度学习中，推理可以采用int8量化方式进行。
专用编程语言: 使用DSA专用语言进行编程。

### Alt/Text Metadata 3

内容占位符 2

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 38

## Slide 4

### Shape 1 Title 1

Recall: AI Accelerator vs. CPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

4

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 Table 3

-  | CPU | DSA
- On-chip Memory | Cache | Global Buffer
- Instruction Issue | Superscalar | In-order/simple
- Parallelism | Inter-instruction | Intra-instruction
- Fuctionality | Full | Partial
- Optimization Purpose | Low Latency | High Throughput
- Programming Language | General | Domain-specific

### Alt/Text Metadata 3

Table 3

### XML fallback texts

- DSA
- On-chip
- Memory
- Cache
- Global
- Buffer
- Instruction
- Issue
- Superscalar
- In-order
- /simple
- Parallelism
- Inter
- -instruction
- Intra
- Fuctionality
- Full
- Partial
- Optimization
- Purpose
- Low
- Latency
- High
- Throughput
- Programming
- Language
- General
- Domain
- -specific

### Notes XML fallback texts

- Cube
- :
- 矩阵乘运算单元，一拍完成一个
- fp16
- 的
- 16x16
- 与
- 16x16
- 矩阵乘；
- C
- =
- A
- *
- B
- ;
- 如果是
- int8
- 输入
- ,
- 则一拍完成
- 16*32
- 与
- 32*16
- 矩阵乘。
- Accumulator
- :
- 累加器， 把当前矩阵乘的结果与前次计算的中间结果相加， 可以用于完成卷积中加
- bias
- 操作。
- C
- =
- A
- *
- B + C
- L0A/L0B/L0C Buffer
- :  L0A
- 存储矩阵乘的左矩阵数据，
- L0B
- 存储矩阵乘的右矩阵数据，
- L0C
- 存储矩阵乘的结果和中间结果。
- A/B DFF
- :
- 数据寄存器，缓存当前计算的
- 16
- *
- 16
- 左
- /
- 右子矩阵。
- Accum
- DFF
- :
- 数据寄存器，缓存当前计算的
- 16*16
- 结果矩阵。
- 40

## Slide 5

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

5

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

### Notes XML fallback texts

- Vector Unit
- ： 向量运算单元，覆盖各种基本的计算类型和许多定制的计算类型，主要包括
- FP16/FP32/int32/Int8
- 等数据类型的计算，支持连续或者固定间隔寻址；或者
- VA
- 寄存器寻址（不规则向量运算）
- SIMD
- 长度
- ：一条
- Vector
- 指令可以完成两个
- 128
- 长度
- fp16
- 类型的向量相加
- /
- 乘， 或者
- 64
- 个
- fp32/int32
- 类型的向量相加
- /
- 乘
- Unified Buffer(UB)
- ： 保存
- Vector
- 运算的源操作数和目的操作数； 一般要求
- 32Byte
- 对齐；
- 数据从
- L0C->UB
- ，需要以
- Vector Unit
- 作为中转，并可以随数据搬运完成一些
- RELU/
- 数据格式转换等操作
- 41

## Slide 6

### Shape 1 Title 1

Two Main Properties of AI Accelerators

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

6

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 3

访存

### Alt/Text Metadata 3

Rectangle 3

### Alt/Text Metadata 4

Group 14 | Rectangle 2 | TextBox 10

### Shape 4.1 Rectangle 2

计算

### Alt/Text Metadata 4.1

Rectangle 2

### Shape 4.2 TextBox 10

很多矩阵、向量计算

### Alt/Text Metadata 4.2

TextBox 10

### Shape 5 Rectangle 11

当前的主要挑战: 不足的算力, 访存代价太大!

### Alt/Text Metadata 5

Rectangle 11

### Alt/Text Metadata 6

Picture 6

### Relationships 6

- rId2: image:../media/image2.tiff

### Alt/Text Metadata 7

Picture 7

### Relationships 7

- rId3: image:../media/image4.emf

### Shape 8 Rectangle 27

[Sze, MIT, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 8

Rectangle 27

### Shape 9 TextBox 28

很多外存访问

### Alt/Text Metadata 9

TextBox 28

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 43

### Slide media/diagram relationships

- rId3: image:../media/image4.emf
- rId2: image:../media/image2.tiff

## Slide 7

### Shape 1 Title 1

Main Challenges of AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

7

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image5.emf

### Shape 4 内容占位符 2

能耗分析: 32bit的DRAM读比32bit的浮点乘法能耗高出2个数量级!

### Alt/Text Metadata 4

内容占位符 2

### Shape 5 内容占位符 2

Mission: 减少能耗高的操作, DRAM/SRAM Read、32b Multiply。

### Notes XML fallback texts

- Buffer Name
- Size
- 最小访问粒度
- L1 Buffer
- 1MB
- 32B
- L0A/B Buffer
- 64KB
- 512B/128B
- L0C Buffer
- 256KB
- 512B/1024B
- Unified Buffer(UB)
- 256KB
- 32B/2B
- Scalar Buffer(SB)
- 16KB
- 2B
- 44

### Slide media/diagram relationships

- rId2: image:../media/image5.emf

## Slide 8

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

8

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 45

## Slide 9

### Shape 1 Title 1

Why On-chip Buffer?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

9

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

最差情况：所有内存读写都是访问外部内存。
AlexNet: 需要 724M MAC操作和2896M次外部内存访问

### Alt/Text Metadata 3

内容占位符 2

### Shape 4 Rectangle 58

[Sze, MIT, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 4

Rectangle 58

### Alt/Text Metadata 5

矩形 3

### Shape 6 TextBox 31

MAC

### Alt/Text Metadata 6

TextBox 31

### Alt/Text Metadata 7

Rectangle 52

### Alt/Text Metadata 8

Group 27 | 矩形 3 | Group 15 | Oval 4 | Straight Connector 10 | Straight Connector 11 | Group 16 | Oval 17 | Straight Connector 18 | Straight Connector 19 | Elbow Connector 25 | TextBox 26

### Alt/Text Metadata 8.2

Group 15 | Oval 4 | Straight Connector 10 | Straight Connector 11

### Alt/Text Metadata 8.2.1

Oval 4

### Alt/Text Metadata 8.2.2

Straight Connector 10

### Alt/Text Metadata 8.2.3

Straight Connector 11

### Alt/Text Metadata 8.3

Group 16 | Oval 17 | Straight Connector 18 | Straight Connector 19

### Alt/Text Metadata 8.3.1

Oval 17

### Alt/Text Metadata 8.3.2

Straight Connector 18

### Alt/Text Metadata 8.3.3

Straight Connector 19

### Alt/Text Metadata 8.4

Elbow Connector 25

### Shape 8.5 TextBox 26

ALU

### Alt/Text Metadata 8.5

TextBox 26

### Alt/Text Metadata 9

Group 5 | TextBox 41 | TextBox 44 | Straight Arrow Connector 33 | Straight Arrow Connector 34 | Straight Arrow Connector 35 | TextBox 42

### Shape 9.1 TextBox 41

Filter weight

### Alt/Text Metadata 9.1

TextBox 41

### Shape 9.2 TextBox 44

Partial sum

### Alt/Text Metadata 9.2

TextBox 44

### Alt/Text Metadata 9.3

Straight Arrow Connector 33

### Alt/Text Metadata 9.4

Straight Arrow Connector 34

### Alt/Text Metadata 9.5

Straight Arrow Connector 35

### Shape 9.6 TextBox 42

Feature map

### Alt/Text Metadata 9.6

TextBox 42

### Shape 10 TextBox 55

1x

### Alt/Text Metadata 10

TextBox 55

### Alt/Text Metadata 11

Group 2 | Straight Connector 29 | Rectangle 45 | TextBox 49 | TextBox 56

### Alt/Text Metadata 11.1

Straight Connector 29

### Shape 11.2 Rectangle 45

DRAM

### Alt/Text Metadata 11.2

Rectangle 45

### Shape 11.3 TextBox 49

Memory Read

### Alt/Text Metadata 11.3

TextBox 49

### Shape 11.4 TextBox 56

200x

### Alt/Text Metadata 11.4

TextBox 56

### Alt/Text Metadata 12

Group 3 | Straight Connector 30 | Rectangle 48 | TextBox 50 | Straight Arrow Connector 46 | TextBox 57 | TextBox 59

### Alt/Text Metadata 12.1

Straight Connector 30

### Alt/Text Metadata 12.2

Rectangle 48

### Shape 12.3 TextBox 50

Memory Write

### Alt/Text Metadata 12.3

TextBox 50

### Alt/Text Metadata 12.4

Straight Arrow Connector 46

### Alt/Text Metadata 12.5

TextBox 57

### Shape 12.6 TextBox 59

Updated partial sum

### Alt/Text Metadata 12.6

TextBox 59

### Notes XML fallback texts

- I Cache
- :
- AICore
- 内部的指令
- Cache,
- 具有指令预取功能
- Scalar PSQ
- : Scalar
- 指令处理队列
- Instr
- Dispatch
- :
- 指令分发模
- , CUBE/Vector/MTE
- 指令经过
- Scalar PSQ
- 处理之后，地址、参数等要素都已经配置好，之后
- Instr
- Dispatch
- 单元根据指令的类型，将
- CUBE/Vector/MTE
- 指令分别分发到对应的指令队列等待相应的执行单元调度执行
- Cube/Vector/MTE1/MTE2/MTE3 Queue:
- Cube/Vector/MTE1/MTE2/MTE3
- 指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行
- 46

## Slide 10

### Shape 1 文本框 1

Where Are We?

### Alt/Text Metadata 1

文本框 1

### Alt/Text Metadata 2

Picture 2

### Relationships 2

- rId2: image:../media/image6.emf

### Alt/Text Metadata 3

Rectangle 36

### Notes XML fallback texts

- System Control
- :
- 系统控制单元，外部的
- Task Scheduler
- 控制和初始化
- AICore
- 的配置接口， 配置比如
- PC,
- Para_base
- ,
- BlockID
- 等信息
- :
- Block
- 执行控制
- Block
- 执行完之后中断和状态申报
- 执行错误状态申报等
- 47

### Slide media/diagram relationships

- rId2: image:../media/image6.emf

## Slide 11

### Shape 1 Title 1

Cache or Buffer?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

11

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 Table 10

-  | Cache | Buffer
- 能耗 | 高 | 低
- 芯片面积 | 大 | 小
- 管理方式 | 自动 | 手动

### Alt/Text Metadata 3

Table 10

### Alt/Text Metadata 4

Picture 33

### Relationships 4

- rId2: image:../media/image7.tiff

### Alt/Text Metadata 5

Picture 34

### Relationships 5

- rId3: image:../media/image8.tiff

### Alt/Text Metadata 6

Picture 35

### Relationships 6

- rId3: image:../media/image8.tiff

### Alt/Text Metadata 7

Picture 37

### Relationships 7

- rId3: image:../media/image8.tiff

### Alt/Text Metadata 8

Picture 38

### Relationships 8

- rId2: image:../media/image7.tiff

### Alt/Text Metadata 9

Picture 39

### Relationships 9

- rId2: image:../media/image7.tiff

### Shape 10 Can 41

Main memory (DRAM)

### Alt/Text Metadata 10

Can 41

### Alt/Text Metadata 11

Rectangle 42

### Shape 12 TextBox 9

Mat

### Alt/Text Metadata 12

TextBox 9

### Alt/Text Metadata 13

Rectangle 10

### Alt/Text Metadata 14

Straight Arrow Connector 12

### Shape 15 Rectangle 46

Cache or Buffer

### Alt/Text Metadata 15

Rectangle 46

### Shape 17 TextBox 9

Vec

### Shape 19 TextBox 9

Scalar

### Shape 21 TextBox 52

AI加速器

### Alt/Text Metadata 21

TextBox 52

### Shape 22 Rectangle 23

AI加速器的主要目标: 提高算力、降低功耗!

### Alt/Text Metadata 22

Rectangle 23

### Shape 23 Rectangle 26

隐含的意思: 可以牺牲可编程性!

### Alt/Text Metadata 23

Rectangle 26

### XML fallback texts

- 能耗
- 芯片
- 面积
- 大
- 小
- 管理方式
- 自动
- 手动

### Notes XML fallback texts

- I Cache
- :
- AICore
- 内部的指令
- Cache,
- 具有指令预取功能
- Scalar PSQ
- : Scalar
- 指令处理队列
- Instr
- Dispatch
- :
- 指令分发模
- , CUBE/Vector/MTE
- 指令经过
- Scalar PSQ
- 处理之后，地址、参数等要素都已经配置好，之后
- Instr
- Dispatch
- 单元根据指令的类型，将
- CUBE/Vector/MTE
- 指令分别分发到对应的指令队列等待相应的执行单元调度执行
- Cube/Vector/MTE1/MTE2/MTE3 Queue:
- Cube/Vector/MTE1/MTE2/MTE3
- 指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行
- 48

### Slide media/diagram relationships

- rId3: image:../media/image8.tiff
- rId2: image:../media/image7.tiff

## Slide 12

### Shape 1 Title 1

Programming Model: Cache vs. Buffer

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

12

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

文本框 87

### Shape 4 文本框 50

DDR uint32_t a[32] = {0, 1, 2, …, 31};
DDR uint32_t b[32] = {0, 1, 2, …, 31};
DDR uint32_t c[32];
Unified_Buffer uint32_t a_ub[32];
Unified_Buffer uint32_t b_ub[32];
Unified_Buffer uint32_t c_ub[32];
Dma_Mov(a_ub, a);
Dma_Mov(b_ub, b);
Vector_add(c_ub, a_ub, b_ub);
Dma_Mov(c, c_ub);

### Alt/Text Metadata 4

文本框 50

### Shape 5 文本框 51

uint32_t a[32] = {0, 1, 2, …, 31};
uint32_t b[32] = {0, 1, 2, …, 31};
uint32_t c[32];
for(uint i = 0; i < 32; i++){
    c[i] = a[i] + b[i];
}

### Alt/Text Metadata 5

文本框 51

### Alt/Text Metadata 6

直接箭头连接符 2

### Alt/Text Metadata 7

直接箭头连接符 54

### Shape 8 文本框 7

Manual

### Alt/Text Metadata 8

文本框 7

### Alt/Text Metadata 9

组合 9 | Group 188 | Freeform 189 | Freeform 190 | Group 191 | Rectangle 192 | Freeform 193 | Freeform 194 | 矩形 11

### Alt/Text Metadata 9.1

Group 188 | Freeform 189 | Freeform 190 | Group 191 | Rectangle 192 | Freeform 193 | Freeform 194

### Alt/Text Metadata 9.1.1

Freeform 189

### Alt/Text Metadata 9.1.2

Freeform 190

### Alt/Text Metadata 9.1.3

Group 191 | Rectangle 192 | Freeform 193 | Freeform 194

### Alt/Text Metadata 9.1.3.1

Rectangle 192

### Alt/Text Metadata 9.1.3.2

Freeform 193

### Alt/Text Metadata 9.1.3.3

Freeform 194

### Shape 9.2 矩形 11

Cache

### Alt/Text Metadata 9.2

矩形 11

### Shape 11 矩形 11

Buffer

### Shape 12 内容占位符 16

Cache-based Programming Model: Automatic
Buffer-based Programming Model: manual manipulation

### Alt/Text Metadata 12

内容占位符 16

### Notes XML fallback texts

- 54

## Slide 13

### Shape 1 Title 1

How to Use Buffer?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

13

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 2

### Relationships 3

- rId2: image:../media/image9.emf

### Alt/Text Metadata 4

Rectangle 9

### Alt/Text Metadata 5

Rectangle 10

### Alt/Text Metadata 6

Rectangle 11

### Alt/Text Metadata 7

Rectangle 12

### Shape 8 内容占位符 2

Global Buffer: Separate, low unit access cost!
L1: for MTE module
UB: for Vector module
L0A/B/C: for Cube module

### Alt/Text Metadata 8

内容占位符 2

### Shape 9 Rectangle 16

Difficult to program due to awareness of buffer location!

### Alt/Text Metadata 9

Rectangle 16

### Notes XML fallback texts

- 128 x 128
- 67

### Slide media/diagram relationships

- rId2: image:../media/image9.emf

## Slide 14

### Shape 1 Title 1

External Memory Access: Solved!

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

14

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image10.emf

### Shape 4 Rectangle 4

[Sze, MIT, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 4

Rectangle 4

### Shape 5 Rectangle 2

Global Buffer

### Alt/Text Metadata 5

Rectangle 2

### Notes XML fallback texts

- 4
- 个
- MMU
- 74

### Slide media/diagram relationships

- rId2: image:../media/image10.emf

## Slide 15

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

15

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

### Notes XML fallback texts

- 4
- 个
- MMU
- 75

## Slide 16

### Shape 1 Title 1

Recall: Data Movement Energy

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

16

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 Table 6

- 32-bit Operation | Energy (pJ) | ADD (int) Relative Cost
- ADD (int) | 0.1 | 1
- ADD (float) | 0.9 | 9
- Register File | 1 | 10
- MULT (int) | 3.1 | 31
- MULT (float) | 3.7 | 37
- SRAM Cache | 5 | 50
- DRAM | 640 | 6400

### Alt/Text Metadata 3

Table 6

### Shape 4 TextBox 8

Han+, “EIE: Efficient Inference Engine on Compressed Deep Neural Network,” ISCA 2016.

### Alt/Text Metadata 4

TextBox 8

### Shape 5 TextBox 9

A memory access consumes ~6400X
the energy of an integer addition

### Alt/Text Metadata 5

TextBox 9

### XML fallback texts

- 32-bit Operation
- Energy (
- pJ
- )
- ADD (int) Relative Cost
- ADD (int)
- 0.1
- ADD (float)
- 0.9
- Register File
- 10
- MULT (int)
- 3.1
- 31
- MULT (float)
- 3.7
- 37
- SRAM Cache
- 5
- 50
- DRAM

### Notes XML fallback texts

- 4
- 个
- MMU
- 76

## Slide 17

### Shape 1 Rectangle 2

Recall: FF vs. SRAM vs. DRAM vs. Flash

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 Content Placeholder 17

Flip-Flops
Very fast, parallel access
Very expensive (one bit costs tens of transistors)
Static RAM
Relatively fast, only one data word at a time
Expensive (one bit costs 6+ transistors)
Dynamic RAM
Slower, one data word at a time, reading destroys content (refresh), needs special process for manufacturing
Cheap (one bit costs only one transistor plus one capacitor)
Flash Memory
Much slower, access takes a long time, non-volatile
Very cheap (one transistor stores 16 bits or no transistors involved)

### Alt/Text Metadata 2

Content Placeholder 17

### Shape 3 Slide Number Placeholder 1

17

### Alt/Text Metadata 3

Slide Number Placeholder 1

### Notes XML fallback texts

- 4
- 个
- MMU
- 77

## Slide 18

### Shape 1 Title 1

Reducing Global Buffer Accesses

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

18

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image11.emf

### Alt/Text Metadata 4

Group 114 | Group 105 | Straight Arrow Connector 101 | Straight Arrow Connector 104 | Straight Arrow Connector 74 | 矩形 3 | TextBox 30 | Rectangle 41 | Straight Arrow Connector 63 | Straight Arrow Connector 71 | Straight Arrow Connector 76 | Straight Arrow Connector 78 | Straight Connector 81 | Straight Connector 84 | Group 107 | Oval 89 | Straight Connector 90 | Straight Connector 91 | Oval 92 | Straight Connector 93 | Straight Connector 94

### Alt/Text Metadata 4.1

Group 105 | Straight Arrow Connector 101 | Straight Arrow Connector 104 | Straight Arrow Connector 74 | 矩形 3 | TextBox 30 | Rectangle 41 | Straight Arrow Connector 63 | Straight Arrow Connector 71 | Straight Arrow Connector 76 | Straight Arrow Connector 78

### Alt/Text Metadata 4.1.1

Straight Arrow Connector 101

### Alt/Text Metadata 4.1.2

Straight Arrow Connector 104

### Alt/Text Metadata 4.1.3

Straight Arrow Connector 74

### Alt/Text Metadata 4.1.4

矩形 3

### Shape 4.1.5 TextBox 30

AI Core

### Alt/Text Metadata 4.1.5

TextBox 30

### Shape 4.1.6 Rectangle 41

DRAM

### Alt/Text Metadata 4.1.6

Rectangle 41

### Alt/Text Metadata 4.1.7

Straight Arrow Connector 63

### Shape 4.1.8 矩形 3

Global
Buffer

### Alt/Text Metadata 4.1.9

Straight Arrow Connector 71

### Shape 4.1.10 矩形 3

PE

### Alt/Text Metadata 4.1.12

Straight Arrow Connector 76

### Alt/Text Metadata 4.1.13

Straight Arrow Connector 78

### Alt/Text Metadata 4.2

Straight Connector 81

### Alt/Text Metadata 4.3

Straight Connector 84

### Alt/Text Metadata 4.4

Group 107 | 矩形 3 | Oval 89 | Straight Connector 90 | Straight Connector 91 | Oval 92 | Straight Connector 93 | Straight Connector 94

### Alt/Text Metadata 4.4.2

Oval 89

### Alt/Text Metadata 4.4.3

Straight Connector 90

### Alt/Text Metadata 4.4.4

Straight Connector 91

### Alt/Text Metadata 4.4.5

Oval 92

### Alt/Text Metadata 4.4.6

Straight Connector 93

### Alt/Text Metadata 4.4.7

Straight Connector 94

### Shape 4.4.8 矩形 3

Control

### Shape 4.4.9 矩形 3

Reg File

### Shape 6 Rectangle 115

Problem: Global Buffer access is expensive.

### Alt/Text Metadata 6

Rectangle 115

### Shape 7 Rectangle 116

Solution: Increasing Register File utilization.

### Alt/Text Metadata 7

Rectangle 116

### Notes XML fallback texts

- Huawei
- follows NV…
- 78

### Slide media/diagram relationships

- rId2: image:../media/image11.emf

## Slide 19

### Shape 1 Title 1

Weight Stationary (WS)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

19

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image12.emf

### Shape 4 Rectangle 31

[Sze, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 4

Rectangle 31

### Shape 5 内容占位符 16

Key idea (Systolic array):
最大程度地减少从Global Buffer读取Weight (conv),
广播Activations和沿着PE水平方向上累加Psum.

### Alt/Text Metadata 5

内容占位符 16

### Shape 6 内容占位符 16

例子: TPU [Jouppi, ISCA, 2017]

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 79

### Slide media/diagram relationships

- rId2: image:../media/image12.emf

## Slide 20

### Shape 1 Title 1

Output Stationary (OS)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

20

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image13.emf

### Shape 4 内容占位符 16

Key idea:
最大程度地减少从Global Buffer读取和存储Psum, 尽量把Psum留在PE内。
广播Weight和沿着PE水平方向上复用Activation。

### Alt/Text Metadata 4

内容占位符 16

### Shape 5 内容占位符 16

例子: [Moons, VLSI, 2016]

### Shape 6 Rectangle 31

[Sze, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 6

Rectangle 31

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 80

### Slide media/diagram relationships

- rId2: image:../media/image13.emf

## Slide 21

### Shape 1 Title 1

Input Stationary (IS)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

21

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image14.emf

### Shape 4 内容占位符 16

Key idea:
最大程度地减少从Global Buffer读取Activation, 尽量把Activation留在PE内。
并行读Weight, 沿着PE水平方向上累加Psum。

### Alt/Text Metadata 4

内容占位符 16

### Shape 5 内容占位符 16

例子: [SCNN, ISCA, 2017]

### Shape 6 Rectangle 31

[Sze, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 6

Rectangle 31

### Notes XML fallback texts

- 现在的计算世界往三个方向发展
- 81

### Slide media/diagram relationships

- rId2: image:../media/image14.emf

## Slide 22

### Shape 1 Title 1

Row Stationary (RS)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

22

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image15.emf

### Shape 4 内容占位符 16

Key idea:
从Global Buffer读出Filter中的一行和Activation的一个滑窗, 留在PE内。
尽量减少从Global Buffer的整体读出量，而不只是一个维度的。

### Alt/Text Metadata 4

内容占位符 16

### Shape 5 内容占位符 16

例子: [Chen, ISCA, 2016]

### Shape 6 Rectangle 31

[Sze, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 6

Rectangle 31

### Notes XML fallback texts

- In
- a
- 2D
- convolution,
- the
- kernel
- is
- used
- to
- extract
- the
- two-dimensional
- information.
- We
- usually
- use
- 3D
- convolution
- in
- image
- processing
- because we
- also
- need
- to
- extract
- the
- depth
- information.
- Stride
- is
- the
- number
- of
- input
- values
- the
- kernel
- will
- jump
- when
- sliding
- on
- the
- input
- feature
- map.
- When
- stride
- =
- 1,
- the
- kernel
- moves
- to
- the
- adjacent input
- values
- without
- jumping.
- Padding
- is
- the
- number
- of
- zeros
- added
- outside
- the
- input
- feature
- map.
- Padding
- =
- 1
- means
- adding
- a
- circle
- of
- zeros
- outside
- the
- input
- feature
- map.
- The
- size
- of
- output
- can
- be
- calculated:
- Output
- =
- (Input
- +
- 2
- *
- Padding
- –
- Kernel)
- /
- Stride
- +
- 1
- In
- this
- example
- :
- (5
- +
- 2
- *
- 1
- –
- 3)
- /
- 1
- +
- 1
- =
- 5
- 87

### Slide media/diagram relationships

- rId2: image:../media/image15.emf

## Slide 23

### Shape 1 Title 1

Goal of Reducing Global Buffer Accesses

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

23

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image16.emf

### Shape 4 Rectangle 2

Global Buffer

### Alt/Text Metadata 4

Rectangle 2

### Shape 5 Rectangle 5

Data Reuse

### Alt/Text Metadata 5

Rectangle 5

### Shape 6 Rectangle 4

[Sze, MIT, https://tinyurl.com/SzeMITDL2020]

### Alt/Text Metadata 6

Rectangle 4

### Notes XML fallback texts

- Mark which layer is which -> first layer as input, second as kernel and last as output
- 88

### Slide media/diagram relationships

- rId2: image:../media/image16.emf

## Slide 24

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

24

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

## Slide 25

### Shape 1 文本框 1

Where Are We?

### Alt/Text Metadata 1

文本框 1

### Alt/Text Metadata 2

Picture 2

### Relationships 2

- rId2: image:../media/image6.emf

### Alt/Text Metadata 3

Rectangle 36

### Notes XML fallback texts

- 106

### Slide media/diagram relationships

- rId2: image:../media/image6.emf

## Slide 26

### Shape 1 Title 1

深度学习：计算和访存特性

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

26

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

MAC (Multiply–Accumulate)

### Alt/Text Metadata 3

Rectangle 4

### Table 4 Table 5

- Operator | 计算特性 | 访存特性
- Conv | 矩阵相乘 | Burst+stride
- Activation | 单向量操作 | Sequential
- Pooling | 单矩阵Reduce操作 | Burst+stride
- FC | 矩阵相乘 | Sequential
- … | … | …

### Alt/Text Metadata 4

Table 5

### Shape 5 Rectangle 9

Fixed Memory Access Pattern

### Alt/Text Metadata 5

Rectangle 9

### Shape 6 Rectangle 10

AI相关计算量里，矩阵乘法计算量的占比高于90%。

### Alt/Text Metadata 6

Rectangle 10

### XML fallback texts

- Operator
- Conv
- 相乘
- B
- urst
- +stride
- Activation
- 单
- 向量
- 操作
- Sequential
- Pooling
- Reduce
- FC
- …

### Notes XML fallback texts

- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 117

### Slide media/diagram relationships

- rId3: image:../media/image160.emf
- rId5: image:../media/image170.emf

## Slide 27

### Shape 1 Title 1

计算模块的设计原则

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

27

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 7

尽量多定制计算单元，略不择手段！

### Alt/Text Metadata 3

TextBox 7

### Alt/Text Metadata 4

Picture 10

### Relationships 4

- rId2: image:../media/image17.png

### Alt/Text Metadata 5

Picture 12

### Relationships 5

- rId3: image:../media/image18.png

### Alt/Text Metadata 6

Picture 14

### Relationships 6

- rId4: image:../media/image19.png

### Notes XML fallback texts

- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 118

### Slide media/diagram relationships

- rId3: image:../media/image18.png
- rId2: image:../media/image17.png
- rId4: image:../media/image19.png

## Slide 28

### Shape 1 Title 1

Matrix Multiplication Unit

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

28

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 103

Scalar:

### Alt/Text Metadata 3

TextBox 103

### Shape 4 TextBox 104

for (int i = 0; i < 16; i++)
    for (int j = 0; j < 16; j++)
       for (int k = 0; k < 16; k++)
           C[i][j] += A[i][k] * B[k][j]

### Alt/Text Metadata 4

TextBox 104

### Shape 5 TextBox 106

for (int i = 0; i < 16; i++)
    for (int j = 0; j < 16; j++)
       C[i][j] = A[i][:] * B[:][j]

### Alt/Text Metadata 5

TextBox 106

### Shape 6 TextBox 107

C[:][:] = A[:][:] * B[:][:]

### Alt/Text Metadata 6

TextBox 107

### Shape 7 TextBox 108

Vector:

### Alt/Text Metadata 7

TextBox 108

### Shape 8 TextBox 109

Matrix:

### Alt/Text Metadata 8

TextBox 109

### Shape 9 TextBox 111

周期数：16*16*16 = 4096
每周期内存访问量: 2 (rd), 1/16 (wr)

### Alt/Text Metadata 9

TextBox 111

### Shape 10 TextBox 112

周期数：16*16 = 256
每周期内存访问量: 2*16 (rd), 1 (wr)

### Alt/Text Metadata 10

TextBox 112

### Shape 11 TextBox 113

周期数：1
每周期内存访问量: 2*16*16 (rd), 16*16 (wr)

### Alt/Text Metadata 11

TextBox 113

### Alt/Text Metadata 12

Down Arrow 114

### Shape 13 TextBox 115

算力密度高

### Alt/Text Metadata 13

TextBox 115

### Alt/Text Metadata 14

Down Arrow 116

### Shape 15 TextBox 117

灵活

### Alt/Text Metadata 15

TextBox 117

### Alt/Text Metadata 16

Group 105 | Rectangle 34 | TextBox 91 | TextBox 92 | Rectangle 93 | TextBox 95 | TextBox 96 | Rectangle 97 | TextBox 98 | TextBox 100 | TextBox 101

### Shape 16.1 Rectangle 34

A

### Alt/Text Metadata 16.1

Rectangle 34

### Shape 16.2 TextBox 91

16

### Alt/Text Metadata 16.2

TextBox 91

### Alt/Text Metadata 16.3

TextBox 92

### Shape 16.4 Rectangle 93

B

### Alt/Text Metadata 16.4

Rectangle 93

### Alt/Text Metadata 16.5

TextBox 95

### Shape 16.6 TextBox 96

X

### Alt/Text Metadata 16.6

TextBox 96

### Shape 16.7 Rectangle 97

C

### Alt/Text Metadata 16.7

Rectangle 97

### Shape 16.8 TextBox 98

=

### Alt/Text Metadata 16.8

TextBox 98

### Alt/Text Metadata 16.9

TextBox 100

### Alt/Text Metadata 16.10

TextBox 101

### Shape 17 TextBox 102

A[16][16],                           B[16][16], C[16][16];

### Alt/Text Metadata 17

TextBox 102

### Shape 18 TextBox 2

float

### Alt/Text Metadata 18

TextBox 2

### Notes XML fallback texts

- 119

## Slide 29

### Alt/Text Metadata 1

图片 2

### Relationships 1

- rId2: image:../media/image9.emf

### Shape 2 Title 1

增加计算模块

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

29

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 28 | Straight Connector 12 | Straight Connector 14 | Straight Connector 20 | Straight Connector 30 | Straight Connector 32 | Straight Connector 33 | Straight Connector 35 | Straight Connector 38

### Alt/Text Metadata 4.1

Straight Connector 12

### Alt/Text Metadata 4.2

Straight Connector 14

### Alt/Text Metadata 4.3

Straight Connector 20

### Alt/Text Metadata 4.4

Straight Connector 30

### Alt/Text Metadata 4.5

Straight Connector 32

### Alt/Text Metadata 4.6

Straight Connector 33

### Alt/Text Metadata 4.7

Straight Connector 35

### Alt/Text Metadata 4.8

Straight Connector 38

### Shape 5 内容占位符 2

Cube模块(算力核心)
单指令处理小矩阵乘法
Vector模块(算力核心)
单指令处理向量操作，如activation

### Alt/Text Metadata 5

内容占位符 2

### Slide media/diagram relationships

- rId2: image:../media/image9.emf

## Slide 30

### Shape 1 Title 1

增加计算模块

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

30

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 13

### Relationships 3

- rId2: image:../media/image20.emf

### Slide media/diagram relationships

- rId2: image:../media/image20.emf

## Slide 31

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

31

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

## Slide 32

### Shape 1 Title 1

AI Chips

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

32

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 28

### Relationships 3

- rId2: image:../media/image21.tiff

### Shape 4 Title 1

TPU

### Shape 5 Title 1

Ascend

### Alt/Text Metadata 6

Picture 2

### Relationships 6

- rId3: image:../media/image22.png

### Alt/Text Metadata 7

Picture 3

### Relationships 7

- rId4: image:../media/image23.tiff

### Shape 8 Title 1

Cambricon

### Slide media/diagram relationships

- rId3: image:../media/image22.png
- rId2: image:../media/image21.tiff
- rId4: image:../media/image23.tiff

## Slide 33

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

33

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

## Slide 34

### Shape 1 Title 1

AI Chips

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

34

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 28

### Relationships 3

- rId2: image:../media/image21.tiff

### Shape 4 Title 1

TPU

### Shape 5 Title 1

Ascend

### Alt/Text Metadata 6

Picture 2

### Relationships 6

- rId3: image:../media/image22.png

### Alt/Text Metadata 7

Picture 3

### Relationships 7

- rId4: image:../media/image23.tiff

### Shape 8 Title 1

Cambricon

### Alt/Text Metadata 9

Rectangle 8

### Slide media/diagram relationships

- rId3: image:../media/image22.png
- rId2: image:../media/image21.tiff
- rId4: image:../media/image23.tiff

## Slide 35

### Shape 1 Title 1

晟腾310/910 芯片结构示意图

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

35

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 11

### Relationships 3

- rId2: image:../media/image24.emf

### Shape 4 TextBox 17

L2 Buffer vs. L2 Cache
同一个介质，两种使用模式
Buffer：程序员可见并可以直接读写（地址空间和DDR/HBM不重合）
Cache: 作为DDR/HBM高速缓存，程序员不可见
DDR/HBM
DDR:  普通内存，带宽低/价格低，在推理芯片310中
HBM： High Bandwidth Memory, 带宽高, 成本高，在训练芯片310中

### Alt/Text Metadata 4

TextBox 17

### Slide media/diagram relationships

- rId2: image:../media/image24.emf

## Slide 36

### Shape 1 Title 1

华为晟腾310推理芯片

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

36

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Group 4 | Picture 2 | Rectangle 3

### Relationships 3

- rId2: image:../media/image25.emf

### Alt/Text Metadata 3.1

Picture 2

### Relationships 3.1

- rId2: image:../media/image25.emf

### Alt/Text Metadata 3.2

Rectangle 3

### Slide media/diagram relationships

- rId2: image:../media/image25.emf

## Slide 37

### Shape 1 Title 1

华为晟腾910训练芯片

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

37

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 5

### Relationships 3

- rId2: image:../media/image26.emf

### Slide media/diagram relationships

- rId2: image:../media/image26.emf

## Slide 38

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 5

DaVinci AI core内部是怎么样的？

### Alt/Text Metadata 2

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 39

### Shape 1 Title 1

Huawei Ascend

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

39

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 19

### Relationships 3

- rId2: image:../media/image24.emf

### Alt/Text Metadata 4

Straight Connector 20

### Alt/Text Metadata 5

Straight Connector 21

### Alt/Text Metadata 6

Picture 24

### Relationships 6

- rId3: image:../media/image27.emf

### Slide media/diagram relationships

- rId3: image:../media/image27.emf
- rId2: image:../media/image24.emf

## Slide 40

### Shape 1 Title 1

Cube模块 （矩阵运算， 算力担当）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

40

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId3: image:../media/image27.emf

### Alt/Text Metadata 4

矩形 3

### Shape 5 TextBox 31

矩阵乘运算单元Cube : 一拍完成一个fp16的 2个16x16矩阵相乘； C = A * B; 如果是int8输入,则一拍完成 16*32 与 32*16 矩阵乘。
累加器Accumulator: 把当前矩阵乘的结果与前次计算的中间结果相加 （ C = A * B + C ）， 可以用于完成卷积中加bias操作。
L0A/L0B/L0C Buffer:  L0A 存储矩阵乘的左矩阵数据，L0B 存储矩阵乘的右矩阵数据， L0C 存储矩阵乘的结果和中间结果。
A/B DFF: 数据寄存器，缓存当前计算的16*16 左/右子矩阵。
Accum DFF : 数据寄存器，缓存当前计算的16*16结果矩阵。

### Alt/Text Metadata 5

TextBox 31

### Speaker notes

Cube : 矩阵乘运算单元，一拍完成一个fp16的 16x16与16x16矩阵乘； C = A * B; 如果是int8输入,则一拍完成 16*32 与 32*16 矩阵乘。

Accumulator: 累加器， 把当前矩阵乘的结果与前次计算的中间结果相加， 可以用于完成卷积中加bias操作。
 	C = A * B + C

L0A/L0B/L0C Buffer:  L0A 存储矩阵乘的左矩阵数据，L0B 存储矩阵乘的右矩阵数据， L0C 存储矩阵乘的结果和中间结果。

A/B DFF: 数据寄存器，缓存当前计算的16*16 左/右子矩阵。

Accum DFF : 数据寄存器，缓存当前计算的16*16结果矩阵。

### Slide media/diagram relationships

- rId3: image:../media/image27.emf

## Slide 41

### Shape 1 Title 1

Vector模块 （向量运算，多面手）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

41

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId3: image:../media/image27.emf

### Alt/Text Metadata 4

Group 28 | Straight Connector 15 | Straight Connector 16 | Straight Connector 17 | Straight Connector 18 | Straight Connector 19 | Straight Connector 20

### Alt/Text Metadata 4.1

Straight Connector 15

### Alt/Text Metadata 4.2

Straight Connector 16

### Alt/Text Metadata 4.3

Straight Connector 17

### Alt/Text Metadata 4.4

Straight Connector 18

### Alt/Text Metadata 4.5

Straight Connector 19

### Alt/Text Metadata 4.6

Straight Connector 20

### Shape 5 TextBox 11

向量运算单元Vector Unit： 覆盖各种基本的计算类型和许多定制的计算类型，主要包括FP16/FP32/int32/Int8等数据类型的计算，支持连续或者固定间隔寻址；或者VA寄存器寻址（不规则向量运算）
SIMD长度：一条Vector指令可以完成两个128长度fp16类型的向量相加/乘，或者64个fp32/int32类型的向量相加/乘
Unified Buffer(UB)： 保存Vector运算的源操作数和目的操作数； 一般要求32Byte对齐；
数据从L0C->UB：随数据搬运在Vector Unit完成一些RELU/数据格式转换等操作

### Alt/Text Metadata 5

TextBox 11

### Speaker notes

Vector Unit： 向量运算单元，覆盖各种基本的计算类型和许多定制的计算类型，主要包括FP16/FP32/int32/Int8等数据类型的计算，支持连续或者固定间隔寻址；或者VA寄存器寻址（不规则向量运算）

SIMD长度：一条Vector指令可以完成两个128长度fp16类型的向量相加/乘， 或者64个fp32/int32类型的向量相加/乘

Unified Buffer(UB)： 保存Vector运算的源操作数和目的操作数； 一般要求32Byte对齐；

数据从L0C->UB，需要以Vector Unit作为中转，并可以随数据搬运完成一些RELU/数据格式转换等操作

### Slide media/diagram relationships

- rId3: image:../media/image27.emf

## Slide 42

### Shape 1 Title 1

Scalar模块 （标量运算，司令部）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

42

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId2: image:../media/image27.emf

### Alt/Text Metadata 4

Group 28 | Straight Connector 17 | Straight Connector 18 | Straight Connector 19 | Straight Connector 20

### Alt/Text Metadata 4.1

Straight Connector 17

### Alt/Text Metadata 4.2

Straight Connector 18

### Alt/Text Metadata 4.3

Straight Connector 19

### Alt/Text Metadata 4.4

Straight Connector 20

### Shape 5 TextBox 14

Scalar Unit： 负责完成AICore中的标量运算，功能上可以看做一个小CPU；完成整个程序的循环控制、分支判断、CUBE/Vector等指令的地址和参数计算以及基本的算术运算等‘
Unified Buffer or  Scalar Buffer: 晟腾310/910 Scalar Unit不能直接访问外面的DDR/HBM, 需要预留UB的一部分(310)或者使用专门的Scalar Buffer(910)用作Scalar Unit的堆栈空间
GPR：通用寄存器，目前包含32个通用寄存器
SPR:  专用寄存器，为了支持指令集一些指令的特殊需要，Davinci设计了许多专用寄存器，比如CoreID, BLOCKID, VA,  STATUS, CTRL等寄存器

### Alt/Text Metadata 5

TextBox 14

### Slide media/diagram relationships

- rId2: image:../media/image27.emf

## Slide 43

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 5

DaVinci AI core内部的Buffer模块是怎么工作的？

### Alt/Text Metadata 2

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 44

### Shape 1 Title 1

MTE/BIU和片上高速存储(Buffer)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

44

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 10

### Relationships 3

- rId3: image:../media/image28.emf

### Alt/Text Metadata 4

Rectangle 11

### Alt/Text Metadata 5

Rectangle 13

### Alt/Text Metadata 6

Rectangle 15

### Alt/Text Metadata 7

Rectangle 16

### Alt/Text Metadata 8

Rectangle 21

### Shape 9 TextBox 9

BIU (Bus Interface Unit): AICore 的“大门”，与总线交互的接口。AICore从外部（L2/DDR/HBM）读取、写入数据的出入口。负责把AICore的读写请求转换为总线上的请求并完成协议交互等工作。
MTE (Memory Transfer Unit): 也被称作 LSU (Load Store Unit), 负责AICore内部数据在不同Buffer之间的读写管理，以及完成一些格式转换的操作，比如padding, 转置, Img2Col, 解压等
L1 Buffer: AICore内最大的一块数据中转区(1MB)，可以用来暂存AICore需要反复使用的一些数据从而减少从总线读写； Img2col操作等MTE的数据格式转换功能需源数据必须位于L1 Buffer
L0A/L0B/L0C/UB/Scalar Buffer: 前面已介绍

### Alt/Text Metadata 9

TextBox 9

### Speaker notes

Buffer Name
Size
最小访问粒度
L1 Buffer
1MB
32B
L0A/B Buffer
64KB
512B/128B
L0C Buffer
256KB
512B/1024B
Unified Buffer(UB)
256KB
32B/2B
Scalar Buffer(SB)
16KB
2B

### Slide media/diagram relationships

- rId3: image:../media/image28.emf

## Slide 45

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 5

DaVinci AI core内部的控制模块是怎么样的？

### Alt/Text Metadata 2

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 46

### Shape 1 Title 1

指令和控制系统

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

46

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 17

### Relationships 3

- rId3: image:../media/image28.emf

### Alt/Text Metadata 4

Rectangle 18

### Alt/Text Metadata 5

Picture 19

### Relationships 5

- rId4: image:../media/image29.png

### Alt/Text Metadata 6

Freeform 20

### Alt/Text Metadata 7

Picture 23

### Relationships 7

- rId5: image:../media/image30.emf

### Alt/Text Metadata 8

Picture 24

### Relationships 8

- rId6: image:../media/image31.emf

### Alt/Text Metadata 9

Picture 25

### Relationships 9

- rId6: image:../media/image31.emf

### Alt/Text Metadata 10

Freeform 26

### Alt/Text Metadata 11

Picture 27

### Relationships 11

- rId7: image:../media/image32.emf

### Alt/Text Metadata 12

Picture 28

### Relationships 12

- rId8: image:../media/image33.emf

### Alt/Text Metadata 13

Picture 29

### Relationships 13

- rId9: image:../media/image34.emf

### Alt/Text Metadata 14

Freeform 30

### Alt/Text Metadata 15

Freeform 31

### Alt/Text Metadata 16

Freeform 32

### Alt/Text Metadata 17

Freeform 33

### Alt/Text Metadata 18

Freeform 34

### Alt/Text Metadata 19

Freeform 35

### Speaker notes

I Cache:  AICore内部的指令Cache, 具有指令预取功能

Scalar PSQ: Scalar 指令处理队列

Instr Dispatch: 指令分发模, CUBE/Vector/MTE 指令经过Scalar PSQ处理之后，地址、参数等要素都已经配置好，之后Instr Dispatch单元根据指令的类型，将CUBE/Vector/MTE指令分别分发到对应的指令队列等待相应的执行单元调度执行

Cube/Vector/MTE1/MTE2/MTE3 Queue:  Cube/Vector/MTE1/MTE2/MTE3指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行

### Slide media/diagram relationships

- rId8: image:../media/image33.emf
- rId3: image:../media/image28.emf
- rId7: image:../media/image32.emf
- rId6: image:../media/image31.emf
- rId5: image:../media/image30.emf
- rId4: image:../media/image29.png
- rId9: image:../media/image34.emf

## Slide 47

### Shape 1 Title 1

指令和控制系统

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

47

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 38

### Relationships 3

- rId3: image:../media/image35.png

### Alt/Text Metadata 4

Picture 39

### Relationships 4

- rId4: image:../media/image28.emf

### Alt/Text Metadata 5

Rectangle 40

### Shape 6 TextBox 36

Event Sync: 用于控制不同队列指令(也叫做不同指令流水)之间的依赖和同步的模块
 barrier()
 set_flag.PIPE_dst.PIPE_src wait_flag.PIPE_dst.PIPE_src

### Alt/Text Metadata 6

TextBox 36

### Speaker notes

System Control: 系统控制单元，外部的Task Scheduler 控制和初始化AICore的配置接口， 配置比如PC, Para_base,  BlockID等信息:
Block执行控制
Block执行完之后中断和状态申报
执行错误状态申报等

### Slide media/diagram relationships

- rId3: image:../media/image35.png
- rId4: image:../media/image28.emf

## Slide 48

### Shape 1 Title 1

Ascend: Pros and Cons

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

48

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 3

Davinci架构的优势：
 CUBE极致算力高 —— 同等功耗和面积下，Davinci Core比Nvidia V100/TPU 极致算力都高；功耗面积相似的情况下，晟腾910算力是Nvidia V100 2.1倍
 Buffer访问、管理效率高：单DavinciCore内 CUBE/VECTOR/MTE 有效并行+丰富的片上Buffer和带宽， 让Davinci 能够高效的发挥极致算力，且有效控制功耗
 硬核随路计算指令：提供了硬件支持的Img2Col/格式转换等随路计算指令，方便了程序设计

### Alt/Text Metadata 3

Rectangle 3

### Shape 4 Rectangle 3

Davinci架构的不足：
难编程：对编程人员要求比较高 (事件同步、Buffer使用), 编程易用性有待提升
生态不完善：软件生态才开始， 相关配套工具、包括Debug手段、PMU等都还不够丰富

### Speaker notes

I Cache:  AICore内部的指令Cache, 具有指令预取功能

Scalar PSQ: Scalar 指令处理队列

Instr Dispatch: 指令分发模, CUBE/Vector/MTE 指令经过Scalar PSQ处理之后，地址、参数等要素都已经配置好，之后Instr Dispatch单元根据指令的类型，将CUBE/Vector/MTE指令分别分发到对应的指令队列等待相应的执行单元调度执行

Cube/Vector/MTE1/MTE2/MTE3 Queue:  Cube/Vector/MTE1/MTE2/MTE3指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行

## Slide 49

### Shape 1 Title 1

Contents

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

49

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Rectangle 4

深度学习加速器设计目标
减少内存访问
减少Global Buffer访问
增加计算
常见AI加速器分析比较
华为Ascend
Google TPU
寒武纪Cambridge

### Alt/Text Metadata 3

Rectangle 4

## Slide 50

### Shape 1 Title 1

Google TPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

50

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

TPU v1
Inference only
TPU v2
Support Training
TPU v3
Support Training
More Computing Power
TPU v4
TPU4: for Training
TPU4i: for Inference

### Alt/Text Metadata 3

内容占位符 2

## Slide 51

### Shape 1 Title 1

TPU v1

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

51

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image36.emf

### Shape 4 内容占位符 2

Matrix Multiply Unit
256x256 MACs
Systolic Array
 24% area
Unified Buffer
24 MB
29% area

### Alt/Text Metadata 4

内容占位符 2

### Shape 5 Rectangle 2

[Google, In-Datacenter Performance Analysis of a Tensor Processing Unit, ISCA, 2017]

### Alt/Text Metadata 5

Rectangle 2

### Shape 6 内容占位符 2

TPU v1
For inference, model is pre-stored in DDR3, and data is from the host via PCIe

### Slide media/diagram relationships

- rId2: image:../media/image36.emf

## Slide 52

### Shape 1 Title 1

Systolic Arrays: Motivation

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Goal: design an accelerator that has
Simple, regular design (keep # unique parts small and regular)
High concurrency  high performance
Balanced computation and I/O (memory) bandwidth
Idea: Replace a single processing element (PE) with a regular array of PEs and carefully orchestrate flow of data between the PEs
such that they collectively transform a piece of input data before outputting it to memory
Benefit: Maximizes computation done on a single piece of data element brought from memory

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

52

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 53

### Shape 1 Title 1

Systolic Arrays: Intuition

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

H. T. Kung, “Why Systolic Architectures?,” IEEE Computer 1982.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

53

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 矩形 1

Normal CPU:

### Alt/Text Metadata 4

矩形 1

### Shape 5 矩形 15

Systolic Array:

### Alt/Text Metadata 5

矩形 15

### Shape 6 矩形: 圆角 4

Memory

### Alt/Text Metadata 6

矩形: 圆角 4

### Shape 7 Rectangle 9

PE

### Alt/Text Metadata 7

Rectangle 9

### Alt/Text Metadata 8

连接符: 肘形 6

### Alt/Text Metadata 9

连接符: 肘形 69

### Alt/Text Metadata 10

矩形: 圆角 73

### Shape 11 Rectangle 9

PE3

### Alt/Text Metadata 12

连接符: 肘形 75

### Alt/Text Metadata 13

连接符: 肘形 76

### Shape 14 Rectangle 9

PE2

### Shape 15 Rectangle 9

PE1

### Shape 16 Content Placeholder 2

Analogy: blood flow (heart  many cells  heart)
Memory: heart, Data: blood, PE: cell
Memory pulses data through PEs: Heart pulses the blood to different cells for “concurrent processing”.

## Slide 54

### Shape 1 Title 1

Systolic Arrays: Benefit （Intuition）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

54

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 矩形 1

Normal CPU:

### Alt/Text Metadata 3

矩形 1

### Shape 4 矩形 15

Systolic Array:

### Alt/Text Metadata 4

矩形 15

### Alt/Text Metadata 5

Group 3 | Rectangle 2 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11

### Shape 5.1 Rectangle 2

IF

### Alt/Text Metadata 5.1

Rectangle 2

### Shape 5.2 Rectangle 8

ID

### Alt/Text Metadata 5.2

Rectangle 8

### Shape 5.3 Rectangle 9

SUB

### Alt/Text Metadata 5.3

Rectangle 9

### Shape 5.4 Rectangle 10

MEM

### Alt/Text Metadata 5.4

Rectangle 10

### Shape 5.5 Rectangle 11

WB

### Alt/Text Metadata 5.5

Rectangle 11

### Shape 6.3 Rectangle 9

MUL

### Shape 7.3 Rectangle 9

ADD

### Alt/Text Metadata 10

组合 2 | Rectangle 2 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11

### Alt/Text Metadata 11

组合 3 | Rectangle 2 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11

### Shape 12 矩形: 圆角 4

Memory

### Alt/Text Metadata 12

矩形: 圆角 4

### Shape 13 Rectangle 9

PE

### Alt/Text Metadata 14

连接符: 肘形 6

### Alt/Text Metadata 15

连接符: 肘形 69

### Alt/Text Metadata 16

矩形: 圆角 73

### Shape 17 Rectangle 9

PE3

### Alt/Text Metadata 18

连接符: 肘形 75

### Alt/Text Metadata 19

连接符: 肘形 76

### Shape 20 Rectangle 9

PE2

### Shape 21 Rectangle 9

PE1

### Shape 22 矩形 107528

For Loop:
    ADD
    SUB
    MUL

### Alt/Text Metadata 22

矩形 107528

### Alt/Text Metadata 23

组合 107531 | Group 3 | Rectangle 2 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11 | 矩形 107529

### Shape 23.2 矩形 107529

T1:

### Alt/Text Metadata 23.2

矩形 107529

### Shape 24 矩形 107530

T2:

### Alt/Text Metadata 24

矩形 107530

### Shape 25 矩形 89

T3:

### Alt/Text Metadata 25

矩形 89

### Shape 26 矩形 90

T4:

### Alt/Text Metadata 26

矩形 90

### Shape 27 矩形 91

T5:

### Alt/Text Metadata 27

矩形 91

### Shape 28 矩形 92

T6:

### Alt/Text Metadata 28

矩形 92

### Alt/Text Metadata 29

Rectangle

### Alt/Text Metadata 30

直接连接符 107533

### Shape 31 文本框 107534

…

### Alt/Text Metadata 31

文本框 107534

### Alt/Text Metadata 32

文本框 99

## Slide 55

### Shape 1 Title 1

Systolic Arrays in AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

55

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

Systolic array can be multi-dimensional
The most popular one used by AI ａｃｃｅｌｅｒａｔｏｒ is two-dimensional．

### Alt/Text Metadata 3

Content Placeholder 2

### Alt/Text Metadata 4

组合 5 | 矩形 17 | 矩形 18 | 矩形 19 | 矩形 20 | 矩形 21 | 矩形 22 | 矩形 23 | 矩形 24 | 矩形 25 | 直接箭头连接符 26 | 直接箭头连接符 27 | 直接箭头连接符 28 | 直接箭头连接符 29 | 直接箭头连接符 30 | 直接箭头连接符 31 | 直接箭头连接符 32 | 直接箭头连接符 33 | 直接箭头连接符 34 | 直接箭头连接符 35 | 直接箭头连接符 36 | 直接箭头连接符 37 | 直接箭头连接符 38 | 直接箭头连接符 39 | 直接箭头连接符 40 | 直接箭头连接符 41 | 直接箭头连接符 42 | 直接箭头连接符 43

### Alt/Text Metadata 4.1

矩形 17

### Alt/Text Metadata 4.2

矩形 18

### Alt/Text Metadata 4.3

矩形 19

### Alt/Text Metadata 4.4

矩形 20

### Alt/Text Metadata 4.5

矩形 21

### Alt/Text Metadata 4.6

矩形 22

### Alt/Text Metadata 4.7

矩形 23

### Alt/Text Metadata 4.8

矩形 24

### Alt/Text Metadata 4.9

矩形 25

### Alt/Text Metadata 4.10

直接箭头连接符 26

### Alt/Text Metadata 4.11

直接箭头连接符 27

### Alt/Text Metadata 4.12

直接箭头连接符 28

### Alt/Text Metadata 4.13

直接箭头连接符 29

### Alt/Text Metadata 4.14

直接箭头连接符 30

### Alt/Text Metadata 4.15

直接箭头连接符 31

### Alt/Text Metadata 4.16

直接箭头连接符 32

### Alt/Text Metadata 4.17

直接箭头连接符 33

### Alt/Text Metadata 4.18

直接箭头连接符 34

### Alt/Text Metadata 4.19

直接箭头连接符 35

### Alt/Text Metadata 4.20

直接箭头连接符 36

### Alt/Text Metadata 4.21

直接箭头连接符 37

### Alt/Text Metadata 4.22

直接箭头连接符 38

### Alt/Text Metadata 4.23

直接箭头连接符 39

### Alt/Text Metadata 4.24

直接箭头连接符 40

### Alt/Text Metadata 4.25

直接箭头连接符 41

### Alt/Text Metadata 4.26

直接箭头连接符 42

### Alt/Text Metadata 4.27

直接箭头连接符 43

### Shape 5 矩形 57

PE

### Alt/Text Metadata 5

矩形 57

### Alt/Text Metadata 6

矩形 58

### Alt/Text Metadata 7

矩形 59

### Alt/Text Metadata 8

矩形 60

### Alt/Text Metadata 9

矩形 61

### Alt/Text Metadata 10

矩形 62

### Alt/Text Metadata 11

矩形 63

### Alt/Text Metadata 12

矩形 64

### Alt/Text Metadata 13

矩形 65

### Alt/Text Metadata 14

组合 8 | 矩形 48 | 直接箭头连接符 49 | 直接箭头连接符 50 | 直接箭头连接符 51 | 直接箭头连接符 52 | 矩形 7 | 矩形 54 | 矩形 55 | 矩形 56 | 矩形 67

### Shape 14.1 矩形 48

Cell

### Alt/Text Metadata 14.1

矩形 48

### Alt/Text Metadata 14.2

直接箭头连接符 49

### Alt/Text Metadata 14.3

直接箭头连接符 50

### Alt/Text Metadata 14.4

直接箭头连接符 51

### Alt/Text Metadata 14.5

直接箭头连接符 52

### Shape 14.6 矩形 7

Left

### Alt/Text Metadata 14.6

矩形 7

### Shape 14.7 矩形 54

Right

### Alt/Text Metadata 14.7

矩形 54

### Shape 14.8 矩形 55

Upper

### Alt/Text Metadata 14.8

矩形 55

### Shape 14.9 矩形 56

Down

### Alt/Text Metadata 14.9

矩形 56

### Shape 14.10 矩形 67

Processing engine (PE):

### Alt/Text Metadata 14.10

矩形 67

### Shape 15 矩形 68

How a PE updates:

### Alt/Text Metadata 15

矩形 68

### Shape 16 矩形 70

Right  = Left

### Alt/Text Metadata 16

矩形 70

### Shape 17 矩形 71

Down  = Upper

### Alt/Text Metadata 17

矩形 71

### Shape 18 矩形 9

Cell = Cell + Upper * Left

### Alt/Text Metadata 18

矩形 9

## Slide 56

### Alt/Text Metadata 1

Picture 6

### Relationships 1

- rId2: image:../media/image37.png

### Shape 2 Title 1

Example 2D Systolic Array Computation

### Alt/Text Metadata 2

Title 1

### Shape 3 Content Placeholder 2

Multiply two 3x3 matrices A and B
Keep the final result in PE accumulators

### Alt/Text Metadata 3

Content Placeholder 2

### Shape 4 Slide Number Placeholder 3

56

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Shape 5 文本框 8

=

### Alt/Text Metadata 5

文本框 8

### Shape 6 文本框 15

×

### Alt/Text Metadata 6

文本框 15

### Slide media/diagram relationships

- rId3: image:../media/image3.png
- rId2: image:../media/image37.png
- rId5: image:../media/image5.png
- rId4: image:../media/image4.png

## Slide 57

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 0

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

57

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 3

### Alt/Text Metadata 5

矩形 17

### Alt/Text Metadata 6

矩形 18

### Alt/Text Metadata 7

矩形 19

### Alt/Text Metadata 8

矩形 20

### Alt/Text Metadata 9

矩形 21

### Alt/Text Metadata 10

矩形 22

### Alt/Text Metadata 11

矩形 23

### Alt/Text Metadata 12

矩形 24

### Alt/Text Metadata 13

直接箭头连接符 6

### Alt/Text Metadata 14

直接箭头连接符 36

### Alt/Text Metadata 15

直接箭头连接符 37

### Alt/Text Metadata 16

直接箭头连接符 38

### Alt/Text Metadata 17

直接箭头连接符 40

### Alt/Text Metadata 18

直接箭头连接符 41

### Alt/Text Metadata 19

直接箭头连接符 52

### Alt/Text Metadata 20

直接箭头连接符 57

### Alt/Text Metadata 21

直接箭头连接符 60

### Alt/Text Metadata 22

直接箭头连接符 63

### Alt/Text Metadata 23

直接箭头连接符 68

### Alt/Text Metadata 24

直接箭头连接符 71

### Alt/Text Metadata 25

直接箭头连接符 74

### Alt/Text Metadata 26

直接箭头连接符 77

### Alt/Text Metadata 27

直接箭头连接符 80

### Alt/Text Metadata 28

直接箭头连接符 83

### Alt/Text Metadata 29

直接箭头连接符 84

### Alt/Text Metadata 30

直接箭头连接符 85

### Alt/Text Metadata 31

直接箭头连接符 86

### Alt/Text Metadata 32

直接箭头连接符 89

### Alt/Text Metadata 33

直接箭头连接符 92

### Alt/Text Metadata 34

直接箭头连接符 93

### Alt/Text Metadata 35

直接箭头连接符 94

### Alt/Text Metadata 36

直接箭头连接符 95

### Alt/Text Metadata 37

直接箭头连接符 96

### Alt/Text Metadata 38

直接箭头连接符 106

### Alt/Text Metadata 39

直接箭头连接符 110

### Alt/Text Metadata 40

直接箭头连接符 111

### Alt/Text Metadata 41

直接箭头连接符 112

### Alt/Text Metadata 42

直接箭头连接符 116

### Alt/Text Metadata 43

直接箭头连接符 120

### Alt/Text Metadata 44

直接箭头连接符 122

### Alt/Text Metadata 45

直接箭头连接符 123

### Alt/Text Metadata 46

直接箭头连接符 124

### Slide media/diagram relationships

- rId8: image:../media/image810.png
- rId13: image:../media/image13.png
- rId18: image:../media/image180.png
- rId3: image:../media/image310.png
- rId21: image:../media/image211.png
- rId7: image:../media/image7.png
- rId12: image:../media/image12.png
- rId17: image:../media/image173.png
- rId2: image:../media/image210.png
- rId16: image:../media/image168.png
- rId20: image:../media/image200.png
- rId6: image:../media/image6.png
- rId11: image:../media/image11.png
- rId5: image:../media/image510.png
- rId15: image:../media/image15.png
- rId23: image:../media/image381.png
- rId10: image:../media/image10.png
- rId19: image:../media/image190.png
- rId4: image:../media/image410.png
- rId9: image:../media/image9.png
- rId14: image:../media/image14.png
- rId22: image:../media/image371.png

## Slide 58

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

58

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

矩形 18

### Alt/Text Metadata 6

矩形 19

### Alt/Text Metadata 7

矩形 20

### Alt/Text Metadata 8

矩形 21

### Alt/Text Metadata 9

矩形 22

### Alt/Text Metadata 10

矩形 23

### Alt/Text Metadata 11

矩形 24

### Alt/Text Metadata 12

直接箭头连接符 6

### Alt/Text Metadata 13

直接箭头连接符 36

### Alt/Text Metadata 14

直接箭头连接符 37

### Alt/Text Metadata 15

直接箭头连接符 38

### Alt/Text Metadata 16

直接箭头连接符 40

### Alt/Text Metadata 17

直接箭头连接符 41

### Alt/Text Metadata 18

直接箭头连接符 52

### Alt/Text Metadata 19

直接箭头连接符 57

### Alt/Text Metadata 20

直接箭头连接符 60

### Alt/Text Metadata 21

直接箭头连接符 63

### Alt/Text Metadata 22

直接箭头连接符 68

### Alt/Text Metadata 23

直接箭头连接符 71

### Alt/Text Metadata 24

直接箭头连接符 74

### Alt/Text Metadata 25

直接箭头连接符 77

### Alt/Text Metadata 26

直接箭头连接符 80

### Alt/Text Metadata 27

直接箭头连接符 83

### Alt/Text Metadata 28

直接箭头连接符 84

### Alt/Text Metadata 29

直接箭头连接符 85

### Alt/Text Metadata 30

直接箭头连接符 86

### Alt/Text Metadata 31

直接箭头连接符 89

### Alt/Text Metadata 32

直接箭头连接符 92

### Alt/Text Metadata 33

直接箭头连接符 93

### Alt/Text Metadata 34

直接箭头连接符 94

### Alt/Text Metadata 35

直接箭头连接符 95

### Alt/Text Metadata 36

直接箭头连接符 96

### Alt/Text Metadata 37

直接箭头连接符 106

### Alt/Text Metadata 38

直接箭头连接符 110

### Alt/Text Metadata 39

直接箭头连接符 111

### Alt/Text Metadata 40

直接箭头连接符 112

### Alt/Text Metadata 41

直接箭头连接符 116

### Alt/Text Metadata 42

直接箭头连接符 120

### Alt/Text Metadata 43

直接箭头连接符 122

### Alt/Text Metadata 44

直接箭头连接符 123

### Alt/Text Metadata 45

直接箭头连接符 124

### XML fallback texts

- *

### Slide media/diagram relationships

- rId8: image:../media/image280.png
- rId13: image:../media/image33.png
- rId18: image:../media/image380.png
- rId3: image:../media/image230.png
- rId21: image:../media/image39.png
- rId7: image:../media/image27.png
- rId12: image:../media/image32.png
- rId17: image:../media/image370.png
- rId2: image:../media/image220.png
- rId16: image:../media/image360.png
- rId20: image:../media/image211.png
- rId6: image:../media/image26.png
- rId11: image:../media/image31.png
- rId5: image:../media/image25.png
- rId15: image:../media/image350.png
- rId23: image:../media/image381.png
- rId10: image:../media/image300.png
- rId19: image:../media/image200.png
- rId4: image:../media/image24.png
- rId9: image:../media/image290.png
- rId14: image:../media/image340.png
- rId22: image:../media/image40.png

## Slide 59

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 2

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

59

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

矩形 18

### Alt/Text Metadata 6

矩形 20

### Alt/Text Metadata 7

矩形 21

### Alt/Text Metadata 8

矩形 22

### Alt/Text Metadata 9

矩形 23

### Alt/Text Metadata 10

矩形 24

### Alt/Text Metadata 11

直接箭头连接符 6

### Alt/Text Metadata 12

直接箭头连接符 36

### Alt/Text Metadata 13

直接箭头连接符 37

### Alt/Text Metadata 14

直接箭头连接符 38

### Alt/Text Metadata 15

直接箭头连接符 40

### Alt/Text Metadata 16

直接箭头连接符 41

### Alt/Text Metadata 17

直接箭头连接符 52

### Alt/Text Metadata 18

直接箭头连接符 57

### Alt/Text Metadata 19

直接箭头连接符 60

### Alt/Text Metadata 20

直接箭头连接符 63

### Alt/Text Metadata 21

直接箭头连接符 68

### Alt/Text Metadata 22

直接箭头连接符 71

### Alt/Text Metadata 23

直接箭头连接符 74

### Alt/Text Metadata 24

直接箭头连接符 77

### Alt/Text Metadata 25

直接箭头连接符 80

### Alt/Text Metadata 26

直接箭头连接符 83

### Alt/Text Metadata 27

直接箭头连接符 84

### Alt/Text Metadata 28

直接箭头连接符 85

### Alt/Text Metadata 29

直接箭头连接符 86

### Alt/Text Metadata 30

直接箭头连接符 92

### Alt/Text Metadata 31

直接箭头连接符 93

### Alt/Text Metadata 32

直接箭头连接符 94

### Alt/Text Metadata 33

直接箭头连接符 95

### Alt/Text Metadata 34

直接箭头连接符 96

### Alt/Text Metadata 35

直接箭头连接符 110

### Alt/Text Metadata 36

直接箭头连接符 111

### Alt/Text Metadata 37

直接箭头连接符 112

### Alt/Text Metadata 38

直接箭头连接符 116

### Alt/Text Metadata 39

直接箭头连接符 120

### Alt/Text Metadata 40

直接箭头连接符 122

### Alt/Text Metadata 41

直接箭头连接符 123

### Alt/Text Metadata 42

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image47.png
- rId13: image:../media/image52.png
- rId18: image:../media/image57.png
- rId26: image:../media/image381.png
- rId3: image:../media/image42.png
- rId21: image:../media/image211.png
- rId7: image:../media/image46.png
- rId12: image:../media/image51.png
- rId17: image:../media/image56.png
- rId25: image:../media/image371.png
- rId2: image:../media/image41.png
- rId16: image:../media/image55.png
- rId20: image:../media/image200.png
- rId6: image:../media/image45.png
- rId11: image:../media/image50.png
- rId24: image:../media/image61.png
- rId5: image:../media/image44.png
- rId15: image:../media/image54.png
- rId23: image:../media/image60.png
- rId10: image:../media/image49.png
- rId19: image:../media/image58.png
- rId4: image:../media/image43.png
- rId9: image:../media/image48.png
- rId14: image:../media/image53.png
- rId22: image:../media/image59.png

## Slide 60

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 3

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

60

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

矩形 21

### Alt/Text Metadata 6

矩形 23

### Alt/Text Metadata 7

矩形 24

### Alt/Text Metadata 8

直接箭头连接符 6

### Alt/Text Metadata 9

直接箭头连接符 36

### Alt/Text Metadata 10

直接箭头连接符 37

### Alt/Text Metadata 11

直接箭头连接符 38

### Alt/Text Metadata 12

直接箭头连接符 40

### Alt/Text Metadata 13

直接箭头连接符 41

### Alt/Text Metadata 14

直接箭头连接符 52

### Alt/Text Metadata 15

直接箭头连接符 57

### Alt/Text Metadata 16

直接箭头连接符 60

### Alt/Text Metadata 17

直接箭头连接符 63

### Alt/Text Metadata 18

直接箭头连接符 68

### Alt/Text Metadata 19

直接箭头连接符 71

### Alt/Text Metadata 20

直接箭头连接符 74

### Alt/Text Metadata 21

直接箭头连接符 77

### Alt/Text Metadata 22

直接箭头连接符 80

### Alt/Text Metadata 23

直接箭头连接符 83

### Alt/Text Metadata 24

直接箭头连接符 84

### Alt/Text Metadata 25

直接箭头连接符 85

### Alt/Text Metadata 26

直接箭头连接符 86

### Alt/Text Metadata 27

直接箭头连接符 94

### Alt/Text Metadata 28

直接箭头连接符 95

### Alt/Text Metadata 29

直接箭头连接符 96

### Alt/Text Metadata 30

直接箭头连接符 111

### Alt/Text Metadata 31

直接箭头连接符 116

### Alt/Text Metadata 32

直接箭头连接符 120

### Alt/Text Metadata 33

直接箭头连接符 122

### Alt/Text Metadata 34

直接箭头连接符 123

### Alt/Text Metadata 35

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image68.png
- rId13: image:../media/image73.png
- rId18: image:../media/image78.png
- rId26: image:../media/image84.png
- rId3: image:../media/image63.png
- rId21: image:../media/image81.png
- rId7: image:../media/image67.png
- rId12: image:../media/image72.png
- rId17: image:../media/image77.png
- rId25: image:../media/image83.png
- rId2: image:../media/image62.png
- rId16: image:../media/image76.png
- rId20: image:../media/image80.png
- rId29: image:../media/image381.png
- rId6: image:../media/image66.png
- rId11: image:../media/image71.png
- rId24: image:../media/image211.png
- rId5: image:../media/image65.png
- rId15: image:../media/image75.png
- rId23: image:../media/image200.png
- rId28: image:../media/image371.png
- rId10: image:../media/image70.png
- rId19: image:../media/image79.png
- rId4: image:../media/image64.png
- rId9: image:../media/image69.png
- rId14: image:../media/image74.png
- rId22: image:../media/image82.png
- rId27: image:../media/image85.png

## Slide 61

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 4

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

61

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

矩形 24

### Alt/Text Metadata 6

直接箭头连接符 6

### Alt/Text Metadata 7

直接箭头连接符 36

### Alt/Text Metadata 8

直接箭头连接符 37

### Alt/Text Metadata 9

直接箭头连接符 38

### Alt/Text Metadata 10

直接箭头连接符 40

### Alt/Text Metadata 11

直接箭头连接符 41

### Alt/Text Metadata 12

直接箭头连接符 52

### Alt/Text Metadata 13

直接箭头连接符 57

### Alt/Text Metadata 14

直接箭头连接符 60

### Alt/Text Metadata 15

直接箭头连接符 63

### Alt/Text Metadata 16

直接箭头连接符 68

### Alt/Text Metadata 17

直接箭头连接符 71

### Alt/Text Metadata 18

直接箭头连接符 74

### Alt/Text Metadata 19

直接箭头连接符 77

### Alt/Text Metadata 20

直接箭头连接符 80

### Alt/Text Metadata 21

直接箭头连接符 83

### Alt/Text Metadata 22

直接箭头连接符 84

### Alt/Text Metadata 23

直接箭头连接符 85

### Alt/Text Metadata 24

直接箭头连接符 86

### Alt/Text Metadata 25

直接箭头连接符 94

### Alt/Text Metadata 26

直接箭头连接符 95

### Alt/Text Metadata 27

直接箭头连接符 96

### Alt/Text Metadata 28

直接箭头连接符 111

### Alt/Text Metadata 29

直接箭头连接符 116

### Alt/Text Metadata 30

直接箭头连接符 120

### Alt/Text Metadata 31

直接箭头连接符 122

### Alt/Text Metadata 32

直接箭头连接符 123

### Alt/Text Metadata 33

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image91.png
- rId13: image:../media/image96.png
- rId18: image:../media/image101.png
- rId26: image:../media/image107.png
- rId3: image:../media/image86.png
- rId21: image:../media/image104.png
- rId7: image:../media/image90.png
- rId12: image:../media/image95.png
- rId17: image:../media/image100.png
- rId25: image:../media/image106.png
- rId2: image:../media/image62.png
- rId16: image:../media/image99.png
- rId20: image:../media/image103.png
- rId29: image:../media/image381.png
- rId6: image:../media/image89.png
- rId11: image:../media/image94.png
- rId24: image:../media/image211.png
- rId5: image:../media/image88.png
- rId15: image:../media/image98.png
- rId23: image:../media/image200.png
- rId28: image:../media/image371.png
- rId10: image:../media/image93.png
- rId19: image:../media/image102.png
- rId4: image:../media/image87.png
- rId9: image:../media/image92.png
- rId14: image:../media/image97.png
- rId22: image:../media/image105.png
- rId27: image:../media/image108.png

## Slide 62

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 5

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

62

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

直接箭头连接符 6

### Alt/Text Metadata 6

直接箭头连接符 36

### Alt/Text Metadata 7

直接箭头连接符 37

### Alt/Text Metadata 8

直接箭头连接符 38

### Alt/Text Metadata 9

直接箭头连接符 40

### Alt/Text Metadata 10

直接箭头连接符 41

### Alt/Text Metadata 11

直接箭头连接符 52

### Alt/Text Metadata 12

直接箭头连接符 57

### Alt/Text Metadata 13

直接箭头连接符 60

### Alt/Text Metadata 14

直接箭头连接符 63

### Alt/Text Metadata 15

直接箭头连接符 68

### Alt/Text Metadata 16

直接箭头连接符 71

### Alt/Text Metadata 17

直接箭头连接符 74

### Alt/Text Metadata 18

直接箭头连接符 77

### Alt/Text Metadata 19

直接箭头连接符 80

### Alt/Text Metadata 20

直接箭头连接符 83

### Alt/Text Metadata 21

直接箭头连接符 84

### Alt/Text Metadata 22

直接箭头连接符 85

### Alt/Text Metadata 23

直接箭头连接符 86

### Alt/Text Metadata 24

直接箭头连接符 95

### Alt/Text Metadata 25

直接箭头连接符 96

### Alt/Text Metadata 26

直接箭头连接符 116

### Alt/Text Metadata 27

直接箭头连接符 120

### Alt/Text Metadata 28

直接箭头连接符 122

### Alt/Text Metadata 29

直接箭头连接符 123

### Alt/Text Metadata 30

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image113.png
- rId13: image:../media/image118.png
- rId18: image:../media/image200.png
- rId26: image:../media/image381.png
- rId3: image:../media/image109.png
- rId21: image:../media/image124.png
- rId7: image:../media/image112.png
- rId12: image:../media/image117.png
- rId17: image:../media/image122.png
- rId25: image:../media/image371.png
- rId2: image:../media/image62.png
- rId16: image:../media/image121.png
- rId20: image:../media/image123.png
- rId6: image:../media/image111.png
- rId11: image:../media/image116.png
- rId24: image:../media/image126.png
- rId5: image:../media/image110.png
- rId15: image:../media/image120.png
- rId23: image:../media/image125.png
- rId10: image:../media/image115.png
- rId19: image:../media/image211.png
- rId4: image:../media/image87.png
- rId9: image:../media/image114.png
- rId14: image:../media/image119.png
- rId22: image:../media/image108.png

## Slide 63

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 6

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

63

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

直接箭头连接符 6

### Alt/Text Metadata 6

直接箭头连接符 36

### Alt/Text Metadata 7

直接箭头连接符 37

### Alt/Text Metadata 8

直接箭头连接符 38

### Alt/Text Metadata 9

直接箭头连接符 40

### Alt/Text Metadata 10

直接箭头连接符 41

### Alt/Text Metadata 11

直接箭头连接符 52

### Alt/Text Metadata 12

直接箭头连接符 57

### Alt/Text Metadata 13

直接箭头连接符 60

### Alt/Text Metadata 14

直接箭头连接符 63

### Alt/Text Metadata 15

直接箭头连接符 68

### Alt/Text Metadata 16

直接箭头连接符 71

### Alt/Text Metadata 17

直接箭头连接符 74

### Alt/Text Metadata 18

直接箭头连接符 77

### Alt/Text Metadata 19

直接箭头连接符 80

### Alt/Text Metadata 20

直接箭头连接符 83

### Alt/Text Metadata 21

直接箭头连接符 84

### Alt/Text Metadata 22

直接箭头连接符 85

### Alt/Text Metadata 23

直接箭头连接符 86

### Alt/Text Metadata 24

直接箭头连接符 95

### Alt/Text Metadata 25

直接箭头连接符 96

### Alt/Text Metadata 26

直接箭头连接符 116

### Alt/Text Metadata 27

直接箭头连接符 120

### Alt/Text Metadata 28

直接箭头连接符 122

### Alt/Text Metadata 29

直接箭头连接符 123

### Alt/Text Metadata 30

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image128.png
- rId13: image:../media/image133.png
- rId18: image:../media/image135.png
- rId3: image:../media/image109.png
- rId7: image:../media/image112.png
- rId12: image:../media/image132.png
- rId17: image:../media/image134.png
- rId2: image:../media/image62.png
- rId16: image:../media/image108.png
- rId20: image:../media/image381.png
- rId6: image:../media/image127.png
- rId11: image:../media/image131.png
- rId5: image:../media/image110.png
- rId15: image:../media/image211.png
- rId10: image:../media/image130.png
- rId19: image:../media/image371.png
- rId4: image:../media/image87.png
- rId9: image:../media/image129.png
- rId14: image:../media/image200.png

## Slide 64

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

T = 7

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

64

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 17

### Alt/Text Metadata 5

直接箭头连接符 6

### Alt/Text Metadata 6

直接箭头连接符 36

### Alt/Text Metadata 7

直接箭头连接符 37

### Alt/Text Metadata 8

直接箭头连接符 38

### Alt/Text Metadata 9

直接箭头连接符 40

### Alt/Text Metadata 10

直接箭头连接符 41

### Alt/Text Metadata 11

直接箭头连接符 52

### Alt/Text Metadata 12

直接箭头连接符 57

### Alt/Text Metadata 13

直接箭头连接符 60

### Alt/Text Metadata 14

直接箭头连接符 63

### Alt/Text Metadata 15

直接箭头连接符 68

### Alt/Text Metadata 16

直接箭头连接符 71

### Alt/Text Metadata 17

直接箭头连接符 74

### Alt/Text Metadata 18

直接箭头连接符 77

### Alt/Text Metadata 19

直接箭头连接符 80

### Alt/Text Metadata 20

直接箭头连接符 83

### Alt/Text Metadata 21

直接箭头连接符 84

### Alt/Text Metadata 22

直接箭头连接符 85

### Alt/Text Metadata 23

直接箭头连接符 86

### Alt/Text Metadata 24

直接箭头连接符 95

### Alt/Text Metadata 25

直接箭头连接符 96

### Alt/Text Metadata 26

直接箭头连接符 116

### Alt/Text Metadata 27

直接箭头连接符 120

### Alt/Text Metadata 28

直接箭头连接符 122

### Alt/Text Metadata 29

直接箭头连接符 123

### Alt/Text Metadata 30

直接箭头连接符 124

### XML fallback texts

- *
- +

### Slide media/diagram relationships

- rId8: image:../media/image128.png
- rId13: image:../media/image137.png
- rId3: image:../media/image109.png
- rId7: image:../media/image112.png
- rId12: image:../media/image108.png
- rId2: image:../media/image62.png
- rId16: image:../media/image381.png
- rId6: image:../media/image127.png
- rId11: image:../media/image211.png
- rId5: image:../media/image110.png
- rId15: image:../media/image371.png
- rId10: image:../media/image200.png
- rId4: image:../media/image87.png
- rId9: image:../media/image136.png
- rId14: image:../media/image138.png

## Slide 65

### Shape 1 Title 1

TPU v1 TPU v2

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

65

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image38.emf

### Shape 4 Rectangle 2

[Google, Google’s Training Chips Revealed: TPUv2 and TPUv3, Hot Chips, 2020]

### Alt/Text Metadata 4

Rectangle 2

### Slide media/diagram relationships

- rId2: image:../media/image38.emf

## Slide 66

### Shape 1 Title 1

TPU v1 TPU v2 (Vector Memory)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

66

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image39.emf

### Alt/Text Metadata 4

Picture 5

### Relationships 4

- rId3: image:../media/image40.emf

### Shape 5 内容占位符 2

TPU1:Buffers between fixed function units

### Alt/Text Metadata 5

内容占位符 2

### Shape 6 内容占位符 2

  TPU2: Single vector memory

### Slide media/diagram relationships

- rId3: image:../media/image40.emf
- rId2: image:../media/image39.emf

## Slide 67

### Shape 1 Title 1

TPU v1 TPU v2 (Vector Unit)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

67

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId3: image:../media/image41.emf

### Alt/Text Metadata 4

Picture 6

### Relationships 4

- rId4: image:../media/image42.emf

### Shape 5 内容占位符 2

TPU1: A fixed function    activation pipeline

### Alt/Text Metadata 5

内容占位符 2

### Shape 6 内容占位符 2

  TPU2: General purpose vector unit

### Speaker notes

128 x 128

### Slide media/diagram relationships

- rId3: image:../media/image41.emf
- rId4: image:../media/image42.emf

## Slide 68

### Shape 1 Title 1

TPU v1 TPU v2 (Vector Unit)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

68

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

TPU1: MMU connected to vector memory

### Alt/Text Metadata 3

内容占位符 2

### Shape 4 内容占位符 2

  TPU2: MMU connected to vector unit

### Alt/Text Metadata 5

Picture 3

### Relationships 5

- rId2: image:../media/image43.emf

### Alt/Text Metadata 6

Picture 4

### Relationships 6

- rId3: image:../media/image44.emf

### Slide media/diagram relationships

- rId3: image:../media/image44.emf
- rId2: image:../media/image43.emf

## Slide 69

### Shape 1 Title 1

TPU v1 TPU v2 (Memory)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

69

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

TPU1: DDR3 connected to MMU

### Alt/Text Metadata 3

内容占位符 2

### Shape 4 内容占位符 2

  TPU2: HBM connected to Vector Memory

### Alt/Text Metadata 5

Picture 3

### Relationships 5

- rId2: image:../media/image45.emf

### Alt/Text Metadata 6

Picture 4

### Relationships 6

- rId3: image:../media/image46.emf

### Slide media/diagram relationships

- rId3: image:../media/image46.emf
- rId2: image:../media/image45.emf

## Slide 70

### Shape 1 Title 1

TPU v2 (Interconnect)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

70

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image47.emf

### Shape 4 内容占位符 2

500Gbps per link

### Alt/Text Metadata 4

内容占位符 2

### Shape 5 内容占位符 2

2Tbps

### Slide media/diagram relationships

- rId2: image:../media/image47.emf

## Slide 71

### Shape 1 Title 1

Google TPU v2

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

71

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image48.emf

### Slide media/diagram relationships

- rId2: image:../media/image48.emf

## Slide 72

### Shape 1 Title 1

Google TPU v3

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

72

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image49.emf

### Slide media/diagram relationships

- rId2: image:../media/image49.emf

## Slide 73

### Shape 1 Title 1

TPU v2 vs. TPU v3

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

73

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image50.tiff

### Shape 4 矩形 1

TPU v2

### Alt/Text Metadata 4

矩形 1

### Shape 5 矩形 5

TPU v3

### Alt/Text Metadata 5

矩形 5

### Slide media/diagram relationships

- rId2: image:../media/image50.tiff

## Slide 74

### Shape 1 Title 1

TPU v4

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

74

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2 | TPU v4 | Google Cloud

### Relationships 3

- rId3: image:../media/image139.png

### Speaker notes

4个MMU

### Slide media/diagram relationships

- rId3: image:../media/image139.png

## Slide 75

### Shape 1 Title 1

TPU v5/v6

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

75

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2 | v6e 主机示意图

### Relationships 3

- rId3: image:../media/image140.png

### Speaker notes

4个MMU

### Slide media/diagram relationships

- rId3: image:../media/image140.png

## Slide 76

### Shape 1 Title 1

GB200 NVL72 GPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

76

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2 | https://i0.wp.com/semianalysis.com/wp-content/uploads/2024/11/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fab46e1af-916d-4fa1-874a-e31095be4bf8_810x780.png?ssl=1

### Relationships 3

- rId3: image:../media/image141.png

### Shape 4 Content Placeholder 2

GB200 NVL72 GPU
18 1U Compute Tray
1 Compute Tray has 2 Bianca board
A board has 1 Grace CPU + 2 Blackwell GPUs
9 1U NVSwitch5 Tray
With two 28.8Tb/s NVSwitch5 ASIC chips
14.4Tb/s: backward toward the backplane
14.4Tb/s: toward the front plate
900GB/s between any two of 72 GPUs
4 1U Power Shelf 33KW

### Alt/Text Metadata 4

Content Placeholder 2

### Speaker notes

4个MMU

### Slide media/diagram relationships

- rId3: image:../media/image141.png

## Slide 77

### Alt/Text Metadata 1

Picture 2 | https://i0.wp.com/semianalysis.com/wp-content/uploads/2024/11/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2F7c2a43a7-20ec-4f25-a0dc-de125b9cb28b_1114x835.png?ssl=1

### Relationships 1

- rId3: image:../media/image142.png

### Shape 2 Title 1

GB200 NVL72 GPU: Bianca Board

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

77

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

矩形 1

### Speaker notes

4个MMU

### Slide media/diagram relationships

- rId3: image:../media/image142.png

## Slide 78

### Shape 1 Title 1

Huawei AI CloudMatrix 384

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

78

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

矩形 1

### Shape 4 Content Placeholder 2

CloudMatrix 384: 384 Ascend 910C NPUs
Advantages:
300 PFLOPs of dense BF16 compute (2x GB200 NVL72)
3.6x aggregate memory capacity
2.1x more memory bandwidth
Disadvantages:
4.1x the power of a GB200 NVL72,
2.5x worse power per FLOPs,
1.9x worse power per TB/s memory bandwidth,
1.2x worse power per TB HBM memory capacity

### Alt/Text Metadata 4

Content Placeholder 2

### Speaker notes

Huawei follows NV…

## Slide 79

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 4

AI模型训练中，内存带宽往往是整体性能的瓶颈，而AI加速器并不能很明显地提高内存带宽的利用效率。

### Alt/Text Metadata 2

TextBox 4

### Shape 3 TextBox 3

为啥AI加速器只要集中在推理(Inference)而不是训练(Training)?

### Alt/Text Metadata 3

TextBox 3

### Shape 4 TextBox 5

AI推理加速器才可以提高10倍以上的能耗比。

### Alt/Text Metadata 4

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 80

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 5

AI推理加速器提高10倍以上的能耗比，因为推理加速器能把模型存到AI芯片上.
而AI训练加速器不能太显著地提高能耗比，而训练加速器不能把模型和中间结果都存到AI芯片上。

### Alt/Text Metadata 2

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 81

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 5

END!!!

### Alt/Text Metadata 2

TextBox 5

### Speaker notes

现在的计算世界往三个方向发展

## Slide 82

### Shape 1 Title 1

Systolic Array in TPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Systolic Array in TPU
One 256 x 256 matrix multiply unit in TPU1.
Two 128x128 matrix multiply units in TPU2/TPU3.
What is the tradeoff?

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

82

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 5

Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

### Alt/Text Metadata 4

TextBox 5

### Alt/Text Metadata 5

图片 2

### Relationships 5

- rId2: image:../media/image143.emf

### Slide media/diagram relationships

- rId2: image:../media/image143.emf

## Slide 83

### Shape 1 Title 1

An Example Modern Systolic Array: TPU (I)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Tensor Processing Unit (ＴＰＵ)
First AI accelerator adopts systolic array to accelerate matrix multiplication.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

83

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image144.png

### Shape 5 TextBox 5

Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

### Alt/Text Metadata 5

TextBox 5

### Alt/Text Metadata 6

图片 1

### Relationships 6

- rId3: image:../media/image145.emf

### Slide media/diagram relationships

- rId3: image:../media/image145.emf
- rId2: image:../media/image144.png

## Slide 84

### Shape 1 Title 1

Systolic Computation Example

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Convolution
Used in filtering, pattern matching, correlation, polynomial evaluation, etc …
Many image processing tasks
Machine learning: up to hundreds of convolutional layers in Convolutional Neural Networks (CNN)

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

84

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image146.png

### Slide media/diagram relationships

- rId2: image:../media/image146.png

## Slide 85

### Shape 1 Title 1

Systolic Array: Advantages & Disadvantages

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Advantages:
Makes multiple uses of each data item  reduced need for fetching/refetching  better use of memory bandwidth
High concurrency
Regular design (both data and control flow)
Disadvantages:
Not good at exploiting irregular parallelism
Relatively special purpose  need software, programmer support to be a general purpose model

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

85

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 86

### Shape 1 Title 1

LeNet-5, a Convolutional Neural Network for Hand-Written Digit Recognition

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

86

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Shape 461

### Relationships 3

- rId2: image:../media/image147.png

### Shape 4 Shape 462

This is a 1024*8 bit input, which will have a truth table of 2 8196 entries

### Alt/Text Metadata 4

Shape 462

### Shape 5 TextBox 2

Slide credit: Hwu & Kirk

### Alt/Text Metadata 5

TextBox 2

### Slide media/diagram relationships

- rId2: image:../media/image147.png

## Slide 87

### Shape 1 Title 1

An Example of 2D Convolution

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 4

### Relationships 2

- rId3: image:../media/image148.gif

### Shape 3 TextBox 5

Structure information
Input: 5*5 (blue)
Kernel (filter): 3*3 (grey)
Output: 5*5 (green)
Computation information
Stride: 1
Padding: 1 (white)
Output Dim = (Input + 2*Padding - Kernel) / Stride + 1

### Alt/Text Metadata 3

TextBox 5

### Shape 4 TextBox 6

Input feature map

### Alt/Text Metadata 4

TextBox 6

### Shape 5 TextBox 7

Output feature map

### Alt/Text Metadata 5

TextBox 7

### Speaker notes

In a 2D convolution, the kernel is used to extract the two-dimensional information.
We usually use 3D convolution in image processing because we also need to extract the depth information.

Stride is the number of input values the kernel will jump when sliding on the input feature map. When stride = 1, the kernel moves to the adjacent input values without jumping.

Padding is the number of zeros added outside the input feature map. Padding = 1 means adding a circle of zeros outside the input feature map.

The size of output can be calculated: Output = (Input + 2*Padding – Kernel) / Stride + 1
In this example:  (5 + 2*1 – 3) / 1 + 1 = 5

### Slide media/diagram relationships

- rId3: image:../media/image148.gif

## Slide 88

### Shape 1 Title 1

An Example of 2D Convolution

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 4

88

### Alt/Text Metadata 2

Slide Number Placeholder 4

### Alt/Text Metadata 3

Picture 10 | Playing Super Mario Bros with Proximal Policy Optimization - Brandon Da  Silva

### Relationships 3

- rId3: image:../media/image149.gif

### Shape 4 TextBox 2

Input Layer

### Alt/Text Metadata 4

TextBox 2

### Shape 5 TextBox 6

CNN kernel

### Alt/Text Metadata 5

TextBox 6

### Shape 6 TextBox 7

Output Layer

### Alt/Text Metadata 6

TextBox 7

### Speaker notes

Mark which layer is which -> first layer as input, second as kernel and last as output

### Slide media/diagram relationships

- rId3: image:../media/image149.gif

## Slide 89

### Shape 1 Title 1

Convolutional Neural Networks: Demo

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

89

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

http://yann.lecun.com/exdb/lenet/index.html

### Alt/Text Metadata 3

TextBox 2

### Alt/Text Metadata 4

Picture 3

### Relationships 4

- rId2: image:../media/image150.png

### Alt/Text Metadata 5

Picture 5

### Relationships 5

- rId3: image:../media/image151.gif

### Alt/Text Metadata 6

Rounded Rectangle 44

### Slide media/diagram relationships

- rId3: image:../media/image151.gif
- rId2: image:../media/image150.png

## Slide 90

### Shape 1 Title 1

Implementing a Convolutional Layer with Matrix Multiplication

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

90

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image152.emf

### Shape 4 TextBox 2

Slide credit: Reproduced from Hwu & Kirk

### Alt/Text Metadata 4

TextBox 2

### Slide media/diagram relationships

- rId2: image:../media/image152.emf

## Slide 91

### Shape 1 Shape 328

Power of Convolutions and Applied Courses

### Alt/Text Metadata 1

Shape 328

### Shape 2 Shape 329

In 2010, Prof. Andreas Moshovos adopted Professor Hwu’s ECE498AL Programming Massively Parallel Processors Class
Several of Prof. Geoffrey Hinton’s graduate students took the course
These students developed the GPU implementation of the Deep CNN that was trained with 1.2M images to win the ImageNet competition

### Alt/Text Metadata 2

Shape 329

### Shape 3 Shape 462

Slide credit: Hwu & Kirk

### Alt/Text Metadata 3

Shape 462

### Shape 4 Marcador de número de diapositiva 3

91

### Alt/Text Metadata 4

Marcador de número de diapositiva 3

## Slide 92

### Shape 1 Title 1

Example: AlexNet (2012)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

92

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Shape 329

AlexNet wins the ImageNet classification competition with ~10% points higher accuracy than state-of-the-art
Krizhevsky et al., “ImageNet Classification with Deep Convolutional Neural Networks”, NIPS 2012.

### Alt/Text Metadata 3

Shape 329

### Alt/Text Metadata 4

Picture 1

### Relationships 4

- rId2: image:../media/image153.png

### Slide media/diagram relationships

- rId2: image:../media/image153.png

## Slide 93

### Shape 1 Shape 329

Google improves accuracy by adding more network layers
From 8 in AlexNet to 22 in GoogLeNet
Szegedy et al., “Going Deeper with Convolutions”, CVPR 2015.

### Alt/Text Metadata 1

Shape 329

### Shape 2 Title 1

Example: GoogLeNet (2014)

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

93

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 3

### Relationships 4

- rId2: image:../media/image154.png

### Slide media/diagram relationships

- rId2: image:../media/image154.png

## Slide 94

### Shape 1 Shape 329

He et al., “Deep Residual Learning for Image Recognition”, CVPR 2016.

### Alt/Text Metadata 1

Shape 329

### Alt/Text Metadata 2

Picture 1

### Relationships 2

- rId2: image:../media/image155.png

### Shape 3 Title 1

Example: ResNet (2015)

### Alt/Text Metadata 3

Title 1

### Shape 4 Slide Number Placeholder 3

94

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 4

### Relationships 5

- rId3: image:../media/image156.png

### Alt/Text Metadata 6

Straight Arrow Connector 6

### Shape 7 TextBox 8

Human: 5.1%

### Alt/Text Metadata 7

TextBox 8

### Alt/Text Metadata 8

Straight Arrow Connector 11

### Shape 9 TextBox 14

First CNN

### Alt/Text Metadata 9

TextBox 14

### Slide media/diagram relationships

- rId3: image:../media/image156.png
- rId2: image:../media/image155.png

## Slide 95

### Shape 1 Title 1

Neural Network Layer Examples

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

95

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 2

### Relationships 4

- rId2: image:../media/image157.png

### Shape 5 TextBox 4

By Cmglee - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=104937230

### Alt/Text Metadata 5

TextBox 4

### Slide media/diagram relationships

- rId2: image:../media/image157.png

## Slide 96

### Shape 1 Content Placeholder 2

Convolution
Used in filtering, pattern matching, correlation, polynomial evaluation, etc …
Many image processing tasks
Machine learning: up to hundreds of convolutional layers in Convolutional Neural Networks (CNN)

### Alt/Text Metadata 1

Content Placeholder 2

### Shape 2 Slide Number Placeholder 3

96

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image146.png

### Shape 4 Title 1

Systolic Computation Example: Convolution (I)

### Alt/Text Metadata 4

Title 1

### Slide media/diagram relationships

- rId2: image:../media/image146.png

## Slide 97

### Shape 1 Title 1

Systolic Computation Example: Convolution (II)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

y1 = w1x1 + w2x2 + w3x3
y2 = w1x2 + w2x3 + w3x4
y3 = w1x3 + w2x4 + w3x5

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

97

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image158.png

### Slide media/diagram relationships

- rId2: image:../media/image158.png

## Slide 98

### Shape 1 Title 1

Systolic Computation Example: Convolution (III)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Worthwhile to implement adder and multiplier separately  to allow overlapping of add/mul executions

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

98

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image159.png

### Slide media/diagram relationships

- rId2: image:../media/image159.png

## Slide 99

### Shape 1 Title 1

Systolic Computation Example: Convolution (IV)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

One needs to carefully orchestrate when data elements are input to the array
And when output is buffered
This gets more involved when
Array dimensionality increases
PEs are less predictable in terms of latency

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

99

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 100

### Alt/Text Metadata 1

Picture 6

### Relationships 1

- rId2: image:../media/image37.png

### Shape 2 Title 1

Example 2D Systolic Array Computation

### Alt/Text Metadata 2

Title 1

### Shape 3 Content Placeholder 2

Multiply two 3x3 matrices (inputs)
Keep the final result in PE accumulators

### Alt/Text Metadata 3

Content Placeholder 2

### Shape 4 Slide Number Placeholder 3

100

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 4

### Relationships 5

- rId3: image:../media/image160.png

### Alt/Text Metadata 6

Picture 7

### Relationships 6

- rId4: image:../media/image161.png

### Shape 7 TextBox 10

P = M

### Alt/Text Metadata 7

TextBox 10

### Shape 8 TextBox 11

Q = N

### Alt/Text Metadata 8

TextBox 11

### Shape 9 TextBox 12

R = R + M*N

### Alt/Text Metadata 9

TextBox 12

### Slide media/diagram relationships

- rId3: image:../media/image160.png
- rId2: image:../media/image37.png
- rId4: image:../media/image161.png

## Slide 101

### Shape 1 Title 1

Two-Dimensional Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

101

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image162.png

### Alt/Text Metadata 5

Picture 5

### Relationships 5

- rId3: image:../media/image163.png

### Slide media/diagram relationships

- rId3: image:../media/image163.png
- rId2: image:../media/image162.png

## Slide 102

### Shape 1 Title 1

Combinations

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

102

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image164.png

### Shape 4 Content Placeholder 2

Systolic arrays can be chained together to form powerful systems
This systolic array is capable of producing on-the-fly least-squares fit to all the data that has arrived up to any given moment

### Alt/Text Metadata 4

Content Placeholder 2

### Slide media/diagram relationships

- rId2: image:../media/image164.png

## Slide 103

### Shape 1 Title 1

Systolic Arrays: Pros and Cons

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Advantages:
Principled: Efficiently makes use of limited memory bandwidth, balances computation to I/O bandwidth availability
Specialized (computation needs to fit PE organization/functions)
	 improved efficiency, simple design, high concurrency/	performance
	 good to do more with less memory bandwidth requirement
Downside:
Specialized
	 not generally applicable because computation needs to fit 	the PE functions/organization

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

103

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 104

### Shape 1 Content Placeholder 2

Each PE in a systolic array
Can store multiple “weights”
Weights can be selected on the fly
Eases implementation of, e.g., adaptive filtering
Taken further
Each PE can have its own data and instruction memory
Data memory  to store partial/temporary results, constants
Leads to stream processing, pipeline parallelism
More generally, staged execution

### Alt/Text Metadata 1

Content Placeholder 2

### Shape 2 Slide Number Placeholder 3

104

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Title 1

More Programmability in Systolic Arrays

### Alt/Text Metadata 3

Title 1

## Slide 105

### Shape 1 Title 1

Pipeline-Parallel (Pipelined) Programs

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

105

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image165.png

### Shape 5 TextBox 1

Suleman+, “Data Marshaling for Multi-core Architectures,” ISCA 2010.

### Alt/Text Metadata 5

TextBox 1

### Slide media/diagram relationships

- rId2: image:../media/image165.png

## Slide 106

### Shape 1 Title 1

Stages of Pipelined Programs

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Loop iterations are divided into code segments called stages
Threads execute stages on different cores

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

106

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 5

loop {
   Compute1
   Compute2
   Compute3
}

### Alt/Text Metadata 4

TextBox 5

### Alt/Text Metadata 5

Rectangle 6

### Shape 6 TextBox 7

A

### Alt/Text Metadata 6

TextBox 7

### Alt/Text Metadata 7

Rectangle 8

### Shape 8 TextBox 9

B

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

Rectangle 10

### Shape 10 TextBox 11

C

### Alt/Text Metadata 10

TextBox 11

### Alt/Text Metadata 11

Picture 12 | pipeline.png

### Relationships 11

- rId3: image:../media/image166.png

### Alt/Text Metadata 12

Oval 14

### Alt/Text Metadata 13

Oval 15

### Alt/Text Metadata 14

TextBox 16

### Alt/Text Metadata 15

TextBox 17

### Alt/Text Metadata 16

TextBox 18

### Alt/Text Metadata 17

Oval 19

### Alt/Text Metadata 18

Oval 32

### Alt/Text Metadata 19

Oval 24

### Alt/Text Metadata 20

Oval 25

### Slide media/diagram relationships

- rId3: image:../media/image166.png

## Slide 107

### Shape 1 Title 1

Pipelined File Compression Example

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

107

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image167.png

### Alt/Text Metadata 5

Rounded Rectangle 1

### Slide media/diagram relationships

- rId2: image:../media/image167.png

## Slide 108

### Shape 1 Title 1

Example Systolic Array: The WARP Computer

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

HT Kung, CMU, 1984-1988
Linear array of 10 cells, each cell a 10 Mflop programmable processor
Attached to a general purpose host machine
HLL and optimizing compiler to program the systolic array
Used extensively to accelerate vision and robotics tasks
Annaratone et al., “Warp Architecture and Implementation,” ISCA 1986.
Annaratone et al., “The Warp Computer: Architecture, Implementation, and Performance,” IEEE TC 1987.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

108

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 109

### Shape 1 Title 1

The WARP Computer

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

109

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image169.png

### Slide media/diagram relationships

- rId2: image:../media/image169.png

## Slide 110

### Shape 1 Title 1

The WARP Cell

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

110

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image170.png

### Slide media/diagram relationships

- rId2: image:../media/image170.png

## Slide 111

### Shape 1 Title 1

An Example Modern Systolic Array: TPU (I)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

111

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image144.png

### Shape 5 TextBox 5

Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

### Alt/Text Metadata 5

TextBox 5

### Slide media/diagram relationships

- rId2: image:../media/image144.png

## Slide 112

### Shape 1 Title 1

An Example Modern Systolic Array: TPU (II)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

112

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image171.png

### Shape 4 TextBox 5

Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

### Alt/Text Metadata 4

TextBox 5

### Alt/Text Metadata 5

Picture 7

### Relationships 5

- rId3: image:../media/image172.png

### Slide media/diagram relationships

- rId3: image:../media/image172.png
- rId2: image:../media/image171.png

## Slide 113

### Alt/Text Metadata 1

Picture 6

### Relationships 1

- rId2: image:../media/image37.png

### Shape 2 Title 1

Recall: Example 2D Systolic Array Computation

### Alt/Text Metadata 2

Title 1

### Shape 3 Content Placeholder 2

Multiply two 3x3 matrices (inputs)
Keep the final result in PE accumulators

### Alt/Text Metadata 3

Content Placeholder 2

### Shape 4 Slide Number Placeholder 3

113

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 4

### Relationships 5

- rId3: image:../media/image160.png

### Alt/Text Metadata 6

Picture 7

### Relationships 6

- rId4: image:../media/image161.png

### Shape 7 TextBox 10

P = M

### Alt/Text Metadata 7

TextBox 10

### Shape 8 TextBox 11

Q = N

### Alt/Text Metadata 8

TextBox 11

### Shape 9 TextBox 12

R = R + M*N

### Alt/Text Metadata 9

TextBox 12

### Slide media/diagram relationships

- rId3: image:../media/image160.png
- rId2: image:../media/image37.png
- rId4: image:../media/image161.png

## Slide 114

### Shape 1 Title 1

An Example Modern Systolic Array: TPU (III)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

114

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 4

### Relationships 3

- rId2: image:../media/image174.png

### Slide media/diagram relationships

- rId2: image:../media/image174.png

## Slide 115

### Shape 1 Title 1

An Example Modern Systolic Array: TPU2

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

115

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 1

### Relationships 3

- rId2: image:../media/image175.tiff

### Shape 4 TextBox 2

https://www.nextplatform.com/2017/05/17/first-depth-look-googles-new-second-generation-tpu/

### Alt/Text Metadata 4

TextBox 2

### Shape 5 TextBox 3

4 TPU chips
vs 1 chip in TPU1

### Alt/Text Metadata 5

TextBox 3

### Shape 6 TextBox 7

High Bandwidth Memory
vs DDR3

### Alt/Text Metadata 6

TextBox 7

### Shape 7 TextBox 8

Floating point operations
vs FP16

### Alt/Text Metadata 7

TextBox 8

### Shape 8 TextBox 9

45 TFLOPS per chip
vs 23 TOPS

### Alt/Text Metadata 8

TextBox 9

### Shape 9 TextBox 10

Designed for training
and inference
vs only inference

### Alt/Text Metadata 9

TextBox 10

### Slide media/diagram relationships

- rId2: image:../media/image175.tiff

## Slide 116

### Shape 1 Title 1

An Example Modern Systolic Array: TPU3

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

116

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

https://cloud.google.com/tpu/docs/system-architecture

### Alt/Text Metadata 3

TextBox 2

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image176.png

### Shape 5 TextBox 9

32GB HBM per chip
vs 16GB HBM in TPU2

### Alt/Text Metadata 5

TextBox 9

### Shape 6 TextBox 10

4 Matrix Units per chip
vs 2 Matrix Units in TPU2

### Alt/Text Metadata 6

TextBox 10

### Shape 7 TextBox 11

90 TFLOPS per chip
vs 45 TFLOPS in TPU2

### Alt/Text Metadata 7

TextBox 11

### Slide media/diagram relationships

- rId2: image:../media/image176.png

## Slide 117

### Shape 1 Title 1

Cerebras’s Wafer Scale Engine (2019)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

117

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 6

### Relationships 4

- rId3: image:../media/image177.png

### Alt/Text Metadata 5

Picture 7

### Relationships 5

- rId3: image:../media/image177.png

### Shape 6 TextBox 8

Cerebras WSE
1.2 Trillion transistors
46,225 mm2

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

Largest GPU
21.1 Billion transistors
815 mm2

### Alt/Text Metadata 7

TextBox 9

### Shape 8 Rectangle 11

The largest ML
    accelerator chip
400,000 cores

### Alt/Text Metadata 8

Rectangle 11

### Shape 9 Rectangle 12

NVIDIA TITAN V

### Alt/Text Metadata 9

Rectangle 12

### Shape 10 TextBox 4

https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning

### Alt/Text Metadata 10

TextBox 4

### Shape 11 Rectangle 13

https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/

### Alt/Text Metadata 11

Rectangle 13

### Speaker notes

The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.

### Slide media/diagram relationships

- rId3: image:../media/image177.png

## Slide 118

### Shape 1 Title 1

Cerebras’s Wafer Scale Engine-2 (2021)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

118

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 7

### Relationships 4

- rId3: image:../media/image177.png

### Shape 5 TextBox 8

Cerebras WSE-2
2.6 Trillion transistors
46,225 mm2

### Alt/Text Metadata 5

TextBox 8

### Shape 6 TextBox 9

Largest GPU
54.2 Billion transistors
826 mm2

### Alt/Text Metadata 6

TextBox 9

### Shape 7 Rectangle 11

The largest ML
    accelerator chip
850,000 cores

### Alt/Text Metadata 7

Rectangle 11

### Shape 8 Rectangle 12

NVIDIA Ampere GA100

### Alt/Text Metadata 8

Rectangle 12

### Alt/Text Metadata 9

Picture 2 | https://cerebras.net/wp-content/uploads/2021/03/img-chip-section-1.png

### Relationships 9

- rId4: image:../media/image178.png

### Shape 10 TextBox 14

https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning

### Alt/Text Metadata 10

TextBox 14

### Shape 11 Rectangle 15

https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/

### Alt/Text Metadata 11

Rectangle 15

### Speaker notes

The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.

### Slide media/diagram relationships

- rId3: image:../media/image177.png
- rId4: image:../media/image178.png

## Slide 119

### Shape 1 Rectangle 4

Digital Design & Computer Arch.Lecture 19b: Systolic Arrays

### Alt/Text Metadata 1

Rectangle 4

### Shape 2 Rectangle 5

Prof. Onur Mutlu
ETH Zürich
Spring 2021
7 May 2021

### Alt/Text Metadata 2

Rectangle 5

## Slide 120

### Shape 1 Title 1

Approaches to (Instruction-Level) Concurrency

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Pipelining
Fine-Grained Multithreading
Out-of-order Execution
Dataflow (at the ISA level)
Superscalar Execution
VLIW
Systolic Arrays
Decoupled Access Execute
SIMD Processing (Vector and array processors, GPUs)

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

120

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 121

### Shape 1 Title 1

Systolic Arrays

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

H. T. Kung, “Why Systolic Architectures?,” IEEE Computer 1982.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

121

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image179.png

### Shape 5 TextBox 5

Analogy:
  Memory: heart
   Data:      blood
   PEs:        cells
Memory pulses
data through
PEs

### Alt/Text Metadata 5

TextBox 5

### Slide media/diagram relationships

- rId2: image:../media/image179.png

## Slide 122

### Shape 1 Title 1

Systolic Architectures

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Basic principle: Replace a single PE with a regular array of PEs and carefully orchestrate flow of data between the PEs
Balance computation and memory bandwidth
Differences from pipelining:
These are individual PEs
Array structure can be non-linear and multi-dimensional
PE connections can be multidirectional (and different speed)
PEs can have local memory and execute kernels (rather than a piece of the instruction)

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

122

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image179.png

### Slide media/diagram relationships

- rId2: image:../media/image179.png
