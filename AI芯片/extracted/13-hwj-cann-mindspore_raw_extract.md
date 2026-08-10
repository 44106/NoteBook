# Raw Extract: 13-hwj-cann-mindspore.pptx

- Slides: 93

## Slide 1

### Shape 1 Rectangle 4

Computer Arch. & AI ChipLecture 13: AI Chip+Runtime+Framework

### Alt/Text Metadata 1

Rectangle 4

### Shape 2 Rectangle 5

Prof. Zeke Wang
Zhejiang University
June 1 2026

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- 1

## Slide 2

### Shape 1 Title 1

Recall: Ascend Cube模块 （算力担当）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

2

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId3: image:../media/image2.emf

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

- rId3: image:../media/image2.emf

## Slide 3

### Shape 1 Title 1

Recall: Vector模块 （多面手）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

3

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId3: image:../media/image2.emf

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

- rId3: image:../media/image2.emf

## Slide 4

### Shape 1 Title 1

Recall: Scalar模块 （司令部）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

4

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 12

### Relationships 3

- rId2: image:../media/image2.emf

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
- 5

### Slide media/diagram relationships

- rId2: image:../media/image2.emf

## Slide 5

### Shape 1 Title 1

Recall: Ascend: Pros and Cons

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

5

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

## Slide 6

### Shape 1 Title 1

Recall: Google TPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

6

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

### Notes XML fallback texts

- Risc
- 核可以考虑实现
- scalar+vector+matrix
- 。。。
- 34

## Slide 7

### Shape 1 Title 1

Recall: TPU v1

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

7

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 3

### Relationships 3

- rId2: image:../media/image3.emf

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

### Notes XML fallback texts

- DLP-M: deep learning processor-multi-core
- DLP-S: deep learning processor-single-core
- DLP-C: deep learning processor-cluster
- 42

### Slide media/diagram relationships

- rId2: image:../media/image3.emf

## Slide 8

### Shape 1 Title 1

Recall: Systolic Arrays: Intuition

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

H. T. Kung, “Why Systolic Architectures?,” IEEE Computer 1982.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

8

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

### Notes XML fallback texts

- 个人看好同构架构，好编程。。很重要。。。
- 44

## Slide 9

### Shape 1 Title 1

Recall: Systolic Arrays in AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

9

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

### Notes XML fallback texts

- The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2
- cache.The
- L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see
- https://
- developer.nvidia.com
- /blog/
- nvidia
- -ampere-architecture-in-depth/
- ).
- 46

## Slide 10

### Shape 1 Title 1

Recall: TPU v1 TPU v2

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

10

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

TPU1: for inference

### Alt/Text Metadata 3

内容占位符 2

### Shape 4 内容占位符 2

  TPU2: for training

### Alt/Text Metadata 5

Picture 4

### Relationships 5

- rId2: image:../media/image4.emf

### Relationships 6

- rId3: image:../media/image5.emf

### Notes XML fallback texts

- 个人看好同构架构，好编程。。很重要。。。
- 47

### Slide media/diagram relationships

- rId3: image:../media/image5.emf
- rId2: image:../media/image4.emf

## Slide 11

### Shape 1 Title 1

Recall: TPU v2 vs. TPU v3

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

11

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 2

### Relationships 3

- rId2: image:../media/image6.tiff

### Shape 4 矩形 1

TPU v2

### Alt/Text Metadata 4

矩形 1

### Shape 5 矩形 5

TPU v3

### Alt/Text Metadata 5

矩形 5

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 50

### Slide media/diagram relationships

- rId2: image:../media/image6.tiff

## Slide 12

### Shape 1 文本框 1

Where Are We?

### Alt/Text Metadata 1

文本框 1

### Alt/Text Metadata 2

Picture 2

### Relationships 2

- rId2: image:../media/image7.emf

### Alt/Text Metadata 3

Rectangle 36

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 51

### Slide media/diagram relationships

- rId2: image:../media/image7.emf

## Slide 13

### Shape 1 Title 1

AI Chips

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

13

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 28

### Relationships 3

- rId2: image:../media/image8.tiff

### Shape 4 Title 1

TPU

### Shape 5 Title 1

Ascend

### Alt/Text Metadata 6

Picture 2

### Relationships 6

- rId3: image:../media/image9.png

### Alt/Text Metadata 7

Picture 3

### Relationships 7

- rId4: image:../media/image10.tiff

### Shape 8 Title 1

Cambricon

### Alt/Text Metadata 9

Rectangle 8

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 52

### Slide media/diagram relationships

- rId3: image:../media/image9.png
- rId2: image:../media/image8.tiff
- rId4: image:../media/image10.tiff

## Slide 14

### Shape 1 Title 1

Cambricon

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

14

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

Cambricon tries to solve two main problems:
How to increase performance/power ratio?
How to increase programmability?

### Alt/Text Metadata 3

Content Placeholder 2

### Shape 4 Content Placeholder 2

Goal of Cambricon:
Design high performance/power ratio, high programmability deep learning accelerator.

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 70

## Slide 15

### Shape 1 Title 1

Cambricon AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

15

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

单核深度学习处理器

### Alt/Text Metadata 3

TextBox 2

### Shape 4 TextBox 3

多核深度学习处理器

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 4

整体架构

### Alt/Text Metadata 5

TextBox 4

### Shape 6 TextBox 5

数据流

### Alt/Text Metadata 6

TextBox 5

### Alt/Text Metadata 7

Rectangle 10

### Shape 8 TextBox 9

指令集

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

TextBox 11

### Shape 10 TextBox 12

Cluster架构

### Alt/Text Metadata 10

TextBox 12

### Speaker notes

跟别的AI加速器比较类似，没本质区别

## Slide 16

### Shape 1 Title 1

Cambricon AI Accelerator DLP-S

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

16

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

控制模块
指令的语义粒度（提供专用指令，操作粒度为tensor）
领域专用指令 vs. RISC vs. CISC
运算模块
基于tensor语义设计运算模块
存储模块
基于tensor语义设计存储模块

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 72

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 17

### Shape 1 Title 1

Overall Architecture of DLP-S

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

17

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Control Module
IFU (Instruction Fetch Unit)
IDU (Instruction Decode Unit)
Compute Unit
VFU (Vector Function Unit)
MFU (Matrix Function Unit)
SRAM Unit
WRAM (Weight RAM)
NRAM (Neuron RAM)
DMA (Direct Memory Access)

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 73

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 18

### Shape 1 Title 1

Cambricon AI Accelerator DLP-S

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

图片 4

### Relationships 2

- rId2: image:../media/image11.png

### Shape 3 内容占位符 2

DLP-S
Control Module
Compute Unit
SRAM Unit

### Alt/Text Metadata 3

内容占位符 2

### Shape 4 Slide Number Placeholder 3

18

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

内容占位符 4

### Relationships 5

- rId3: image:../media/image12.png

### Notes XML fallback texts

- CSE
- （
- Common-Subexpression Elimination
- ），公共子表达式消除。
- 简单而言就是将相同输入的表达式进行消除，复用计算结果。
- 74

### Slide media/diagram relationships

- rId3: image:../media/image12.png
- rId2: image:../media/image11.png

## Slide 19

### Shape 1 Title 1

Control Module of DLP-S

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

19

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image11.png

### Alt/Text Metadata 4

内容占位符 4

### Relationships 4

- rId3: image:../media/image12.png

### Shape 5 内容占位符 2

Control Module
Simple control
Register Renaming

### Alt/Text Metadata 5

内容占位符 2

### Alt/Text Metadata 6

矩形 9

### Alt/Text Metadata 7

矩形 10

### Notes XML fallback texts

- Reducing high-cost operations: global memory access
- 75

### Slide media/diagram relationships

- rId3: image:../media/image12.png
- rId2: image:../media/image11.png

## Slide 20

### Shape 1 Title 1

Instruction Fetch Unit

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

20

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

IFU
Address Generator Unit
Instruction Cache
Refill Buffer
Instruction Queue

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

组合 6 | 图片 4 | 矩形 5

### Relationships 4

- rId2: image:../media/image13.png

### Alt/Text Metadata 4.1

图片 4

### Relationships 4.1

- rId2: image:../media/image13.png

### Shape 4.2 矩形 5

Refill Buffer

### Alt/Text Metadata 4.2

矩形 5

### Notes XML fallback texts

- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 77

### Slide media/diagram relationships

- rId2: image:../media/image13.png

## Slide 21

### Shape 1 Title 1

Instruction Decode Unit

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

21

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

IDU (Instruction Decode Unit)
Decoder
ALU
Issue Queue
Control IQ, Compute IQ, Memory IQ

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image14.png

### Notes XML fallback texts

- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 78

### Slide media/diagram relationships

- rId2: image:../media/image14.png

## Slide 22

### Shape 1 Title 1

Instruction Issue Queue

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

22

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Instruction Issue Queue
Between queue: Out of order, inserting SYNC instructions between instruction queues
In queue: in order

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 5

### Relationships 4

- rId2: image:../media/image15.png

### Notes XML fallback texts

- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 79

### Slide media/diagram relationships

- rId2: image:../media/image15.png

## Slide 23

### Shape 1 Title 1

Compute Module of DLP-S

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

23

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image11.png

### Alt/Text Metadata 4

内容占位符 4

### Relationships 4

- rId3: image:../media/image12.png

### Shape 5 内容占位符 2

Compute Module
Matrix instruction
Vector instruction
Quantization

### Alt/Text Metadata 5

内容占位符 2

### Alt/Text Metadata 6

矩形 9

### Alt/Text Metadata 7

矩形 10

### Notes XML fallback texts

- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 80

### Slide media/diagram relationships

- rId3: image:../media/image12.png
- rId2: image:../media/image11.png

## Slide 24

### Shape 1 Title 1

SRAM Module of DLP-S

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

24

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image11.png

### Alt/Text Metadata 4

内容占位符 4

### Relationships 4

- rId3: image:../media/image12.png

### Shape 5 内容占位符 2

SRAM Module
Separate management for performance and efficiency
Access via DMA

### Alt/Text Metadata 5

内容占位符 2

### Alt/Text Metadata 6

矩形 9

### Alt/Text Metadata 7

矩形 10

### Notes XML fallback texts

- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 82

### Slide media/diagram relationships

- rId3: image:../media/image12.png
- rId2: image:../media/image11.png

## Slide 25

### Shape 1 Title 1

Cambricon AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

25

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

单核深度学习处理器

### Alt/Text Metadata 3

TextBox 2

### Shape 4 TextBox 3

多核深度学习处理器

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 4

整体架构

### Alt/Text Metadata 5

TextBox 4

### Shape 6 TextBox 5

数据流

### Alt/Text Metadata 6

TextBox 5

### Alt/Text Metadata 7

Rectangle 10

### Shape 8 TextBox 9

指令集

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

TextBox 11

### Shape 10 TextBox 12

Cluster架构

### Alt/Text Metadata 10

TextBox 12

### Alt/Text Metadata 11

内容占位符 2

### Notes XML fallback texts

- 科学计算才是
- AI
- 应用的蓝海。。。
- 89

## Slide 26

### Shape 1 Title 1

Overall Execution Flow

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

26

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image11.png

### Alt/Text Metadata 4

箭头: 下 9

### Alt/Text Metadata 5

箭头: 下 10

### Alt/Text Metadata 6

箭头: 下 12

### Shape 7 文本框 13

控制

### Alt/Text Metadata 7

文本框 13

### Shape 8 文本框 14

神经元

### Alt/Text Metadata 8

文本框 14

### Shape 9 文本框 15

权重

### Alt/Text Metadata 9

文本框 15

### Alt/Text Metadata 10

箭头: 上下 8

### Alt/Text Metadata 11

箭头: 上下 9

### Alt/Text Metadata 12

箭头: 上下 10

### Alt/Text Metadata 13

箭头: 下 11

### Shape 15 内容占位符 2

神经元tensor数据流
DRAM->NRAM->VFU->（MFU->VFU->）NRAM->DRAM
权值tensor数据流
DRAM->WRAM->MFU

### Alt/Text Metadata 15

内容占位符 2

### Notes XML fallback texts

- 大规模高维微分方程
- AI
- 求解器
- ：
- AI
- 建模加速材料、气象等领域；
- AI
- 求解加速麦克斯韦电磁方程、
- Burgers
- 等，性能提升
- 10
- 倍
- ；
- AI
- 框架加速支持海洋
- GOMO
- 模型，性能提升
- 1.5
- 倍
- 。
- 自动微分
- ：前向自动微分、混合自动微分、向量化自动微等，性能提升
- 10
- 倍
- 。
- 通用（稀疏）张量代数计算加速
- ：支持基础
- BLAS
- 运算
- (
- 矩阵求逆等
- )
- 、
- FFT
- 运算、稀疏矩阵运算等，性能提升
- 2-3
- 倍
- 。
- 90

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 27

### Shape 1 Title 1

Execution Flow: Step 1

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

27

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #1：IFU 通过 DMA 从 DRAM 中读取程序指令，然后经过 IDU 进行译码后分发给DMA、VFU 和 MFU

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

Group 2 | 箭头: 下 9 | 文本框 10 | 箭头: 下 6 | 箭头: 下 8

### Alt/Text Metadata 5.1

箭头: 下 9

### Shape 5.2 文本框 10

控制

### Alt/Text Metadata 5.2

文本框 10

### Alt/Text Metadata 5.3

箭头: 下 6

### Alt/Text Metadata 5.4

箭头: 下 8

### Notes XML fallback texts

- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 91

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 28

### Shape 1 Title 1

Execution Flow: Step 2

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

28

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #2： DMA 接收到访存指令（读tensor指令，包括地址，数据量等信息），从 DRAM 读取神经元tensor至 NRAM，读取权值tensor至 WRAM。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

矩形 5

### Alt/Text Metadata 6

箭头: 下 6

### Alt/Text Metadata 7

箭头: 下 7

### Alt/Text Metadata 8

箭头: 下 8

### Alt/Text Metadata 9

箭头: 下 9

### Alt/Text Metadata 10

箭头: 下 10

### Alt/Text Metadata 11

箭头: 下 12

### Shape 12 文本框 13

控制

### Alt/Text Metadata 12

文本框 13

### Shape 13 文本框 14

神经元

### Alt/Text Metadata 13

文本框 14

### Shape 14 文本框 15

权重

### Alt/Text Metadata 14

文本框 15

### Notes XML fallback texts

- Kamil
- Rocki
- , Dirk Van
- Essendelft
- , Ilya
- Sharapov
- , Robert Schreiber, Michael Morrison, Vladimir
- Kibardin
- , Andrey Portnoy, Jean Francois
- Dietiker
- , Madhava
- Syamlal
- , and Michael James. 2020. Fast stencil-code computation on a wafer-scale processor. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis(SC '20). IEEE Press, Article 58, 1–14.
- 92

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 29

### Shape 1 Title 1

Execution Flow: Step 3

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

29

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #3：VFU 接收到指令后从 NRAM 中读取神经元tensor，并对神经元tensor进行预处理（如边界扩充等），然后发送给 MFU。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

箭头: 下 9

### Alt/Text Metadata 6

箭头: 下 10

### Alt/Text Metadata 7

箭头: 下 12

### Shape 8 文本框 13

控制

### Alt/Text Metadata 8

文本框 13

### Shape 9 文本框 14

神经元

### Alt/Text Metadata 9

文本框 14

### Shape 10 文本框 15

权重

### Alt/Text Metadata 10

文本框 15

### Alt/Text Metadata 11

矩形 5

### Alt/Text Metadata 12

箭头: 下 6

### Alt/Text Metadata 13

箭头: 下 7

### Notes XML fallback texts

- 93

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 30

### Shape 1 Title 1

Execution Flow: Step 4

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

30

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #4： MFU 接收到指令后从 VFU 接收经过预处理的神经元tensor，并从 WRAM 中读取权重tensor，完成矩阵运算后将结果发送给 VFU。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

箭头: 下 9

### Alt/Text Metadata 6

箭头: 下 10

### Alt/Text Metadata 7

箭头: 下 12

### Shape 8 文本框 13

控制

### Alt/Text Metadata 8

文本框 13

### Shape 9 文本框 14

神经元

### Alt/Text Metadata 9

文本框 14

### Shape 10 文本框 15

权重

### Alt/Text Metadata 10

文本框 15

### Alt/Text Metadata 11

矩形 5

### Alt/Text Metadata 12

箭头: 下 6

### Alt/Text Metadata 13

箭头: 下 7

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 31

### Shape 1 Title 1

Execution Flow: Step 5

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

31

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #5： VFU 对输出神经元tensor进行后处理（如激活、池化等） 。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

箭头: 下 9

### Alt/Text Metadata 6

箭头: 下 10

### Alt/Text Metadata 7

箭头: 下 12

### Shape 8 文本框 13

控制

### Alt/Text Metadata 8

文本框 13

### Shape 9 文本框 14

神经元

### Alt/Text Metadata 9

文本框 14

### Shape 10 文本框 15

权重

### Alt/Text Metadata 10

文本框 15

### Alt/Text Metadata 11

矩形 5

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 32

### Shape 1 Title 1

Execution Flow: Step 6

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

32

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #6： VFU 将运算结果tensor写回NRAM。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

箭头: 下 9

### Alt/Text Metadata 6

箭头: 下 10

### Alt/Text Metadata 7

箭头: 下 12

### Shape 8 文本框 13

控制

### Alt/Text Metadata 8

文本框 13

### Shape 9 文本框 14

神经元

### Alt/Text Metadata 9

文本框 14

### Shape 10 文本框 15

权重

### Alt/Text Metadata 10

文本框 15

### Alt/Text Metadata 11

箭头: 下 5

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 33

### Shape 1 Title 1

Execution Flow: Step 7

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

33

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Step #7： DMA 将输出神经元tensor从 NRAM 写回到 DRAM。

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image11.png

### Alt/Text Metadata 5

箭头: 下 9

### Alt/Text Metadata 6

箭头: 下 10

### Alt/Text Metadata 7

箭头: 下 12

### Shape 8 文本框 13

控制

### Alt/Text Metadata 8

文本框 13

### Shape 9 文本框 14

神经元

### Alt/Text Metadata 9

文本框 14

### Shape 10 文本框 15

权重

### Alt/Text Metadata 10

文本框 15

### Alt/Text Metadata 11

箭头: 下 5

### Slide media/diagram relationships

- rId2: image:../media/image11.png

## Slide 34

### Shape 1 Title 1

Cambricon AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

34

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

单核深度学习处理器

### Alt/Text Metadata 3

TextBox 2

### Shape 4 TextBox 3

多核深度学习处理器

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 4

整体架构

### Alt/Text Metadata 5

TextBox 4

### Shape 6 TextBox 5

数据流

### Alt/Text Metadata 6

TextBox 5

### Alt/Text Metadata 7

Rectangle 10

### Shape 8 TextBox 9

指令集

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

TextBox 11

### Shape 10 TextBox 12

Cluster架构

### Alt/Text Metadata 10

TextBox 12

### Alt/Text Metadata 11

内容占位符 2

### Speaker notes

Risc核可以考虑实现scalar+vector+matrix。。。

## Slide 35

### Shape 1 Title 1

DLP ISA

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

35

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image16.png

### Slide media/diagram relationships

- rId2: image:../media/image16.png

## Slide 36

### Shape 1 Title 1

Control ISA

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

36

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Control instruction
JUMP：立即跳转指令
CB：条件分支指令

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image17.png

### Slide media/diagram relationships

- rId2: image:../media/image17.png

## Slide 37

### Shape 1 Title 1

Data Movement ISA

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

37

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Data Movement instruction
Load/Store指令：主存和片上存储交互
MLOAD/MSTORE：矩阵数据（变长）
VLOAD/VSTORE：向量数据（变长）
SLOAD/SSTORE：标量数据
MOVE指令：片上数据传输
MMOVE，VMOVE，SMOVE

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image18.png

### Slide media/diagram relationships

- rId2: image:../media/image18.png

## Slide 38

### Shape 1 Title 1

Compute ISA

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

38

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image19.png

### Shape 4 内容占位符 2

计算指令
矩阵运算：
MMV，VMM，MMS，OP（外积），MAM，MSM
向量运算：
VAV，VSV，VMV，VDV，VEXP（向量指数），VLOG（向量对数），IP（内积），RV（随机向量生成），VMAX/VMIN（向量最值）
标量运算：
加减乘除基本运算，标量超越函数

### Alt/Text Metadata 4

内容占位符 2

### Shape 5 矩形 5

MMV (Matrix-Multiply-Vector):

### Alt/Text Metadata 5

矩形 5

### Slide media/diagram relationships

- rId2: image:../media/image19.png

## Slide 39

### Shape 1 Title 1

Logic ISA

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

39

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

Logic ISA
向量逻辑：
比较（VGT，VE）
逻辑（VAND，VOR，VNOT）
最值归约VGTM
标量逻辑：
标量比较，标量逻辑运算

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image20.png

### Shape 5 文本框 5

最值归约：Vout[i] = (Vin0[i] > Vin1[i])?Vin0[i] : Vin1[i]

### Alt/Text Metadata 5

文本框 5

### Slide media/diagram relationships

- rId2: image:../media/image20.png

## Slide 40

### Shape 1 Title 1

Cambricon AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

40

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

单核深度学习处理器

### Alt/Text Metadata 3

TextBox 2

### Shape 4 TextBox 3

多核深度学习处理器

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 4

整体架构

### Alt/Text Metadata 5

TextBox 4

### Shape 6 TextBox 5

数据流

### Alt/Text Metadata 6

TextBox 5

### Alt/Text Metadata 7

Rectangle 10

### Shape 8 TextBox 9

指令集

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

TextBox 11

### Shape 10 TextBox 12

Cluster架构

### Alt/Text Metadata 10

TextBox 12

### Alt/Text Metadata 11

内容占位符 2

## Slide 41

### Shape 1 Title 1

DLP-M总体架构

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

41

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image21.png

### Shape 4 内容占位符 2

多核处理器分层结构设计
一个DLP-M由多个DLP-C构成
一个DLP-C由多个DLP-S构成

### Alt/Text Metadata 4

内容占位符 2

### Shape 5 矩形 1

DLP-M

### Alt/Text Metadata 5

矩形 1

### Shape 6 矩形 7

DLP-C

### Alt/Text Metadata 6

矩形 7

### Shape 7 矩形 2

为什么需要进行分层结构设计?

### Alt/Text Metadata 7

矩形 2

### Shape 8 矩形 3

减少NoC的负载核开销

### Alt/Text Metadata 8

矩形 3

### Slide media/diagram relationships

- rId2: image:../media/image21.png

## Slide 42

### Shape 1 Title 1

Cambricon AI Accelerator

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

42

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 TextBox 2

单核深度学习处理器

### Alt/Text Metadata 3

TextBox 2

### Shape 4 TextBox 3

多核深度学习处理器

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 4

整体架构

### Alt/Text Metadata 5

TextBox 4

### Shape 6 TextBox 5

数据流

### Alt/Text Metadata 6

TextBox 5

### Alt/Text Metadata 7

Rectangle 10

### Shape 8 TextBox 9

指令集

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

TextBox 11

### Shape 10 TextBox 12

Cluster架构

### Alt/Text Metadata 10

TextBox 12

### Speaker notes

DLP-M: deep learning processor-multi-core
DLP-S: deep learning processor-single-core
DLP-C: deep learning processor-cluster

## Slide 43

### Shape 1 Title 1

DLP-C总体架构

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

43

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 内容占位符 2

DLP-C整体架构：
四个DLP-S
存储核MEMCORE（Memory Core）
存储SMEM：DLP-S共享数据
通信：
GDMA: DLP-C与片外DRAM
CDMA: DLP-C之间，多个DLP-S之间

### Alt/Text Metadata 3

内容占位符 2

### Alt/Text Metadata 4

图片 4

### Relationships 4

- rId2: image:../media/image22.png

### Slide media/diagram relationships

- rId2: image:../media/image22.png

## Slide 44

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 3

Homogeneous Architecture
(Huawei and Nvidia)
vs.
Heterogeneous architecture (Cambricon)?

### Alt/Text Metadata 2

TextBox 3

### Speaker notes

个人看好同构架构，好编程。。很重要。。。

## Slide 45

### Shape 1 Title 1

Recall: Huawei Acend 910

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

45

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Picture 5

### Relationships 3

- rId2: image:../media/image23.emf

### Slide media/diagram relationships

- rId2: image:../media/image23.emf

## Slide 46

### Shape 1 Title 1

Recall: NVIDIA A100 (Homogeneous)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

108 cores on the A100
(Up to 128 cores in the full-blown chip)
40MB L2 cache

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 TextBox 2

https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

### Alt/Text Metadata 3

TextBox 2

### Shape 4 Slide Number Placeholder 3

46

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 4

### Relationships 5

- rId3: image:../media/image24.png

### Speaker notes

The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2 cache.The L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

### Slide media/diagram relationships

- rId3: image:../media/image24.png

## Slide 47

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 TextBox 3

Homogeneous Architecture
(Huawei and Nvidia)
vs.
Heterogeneous architecture (Cambricon)?

### Alt/Text Metadata 2

TextBox 3

### Speaker notes

个人看好同构架构，好编程。。很重要。。。

## Slide 48

### Shape 1 文本框 1

Where Are We?

### Alt/Text Metadata 1

文本框 1

### Alt/Text Metadata 2

Picture 2

### Relationships 2

- rId2: image:../media/image7.emf

### Alt/Text Metadata 3

Rectangle 36

### Slide media/diagram relationships

- rId2: image:../media/image7.emf

## Slide 49

### Shape 1 Title 1

AI Architecture

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

49

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 60

### Relationships 3

- rId2: image:../media/image25.png

### Alt/Text Metadata 4

图片 61

### Relationships 4

- rId3: image:../media/image26.png

### Alt/Text Metadata 5

图片 62

### Relationships 5

- rId4: image:../media/image27.png

### Alt/Text Metadata 6

图片 63

### Relationships 6

- rId5: image:../media/image28.png

### Alt/Text Metadata 7

图片 64

### Relationships 7

- rId6: image:../media/image29.png

### Alt/Text Metadata 8

组合 68 | 图片 69 | 图片 70

### Relationships 8

- rId7: image:../media/image30.png
- rId8: image:../media/image31.png

### Alt/Text Metadata 8.1

图片 69

### Relationships 8.1

- rId7: image:../media/image30.png

### Alt/Text Metadata 8.2

图片 70

### Relationships 8.2

- rId8: image:../media/image31.png

### Shape 9 文本框 71

AscendXX…

### Alt/Text Metadata 9

文本框 71

### Shape 10 矩形 72

？

### Alt/Text Metadata 10

矩形 72

### Alt/Text Metadata 11

直接箭头连接符 73

### Alt/Text Metadata 12

直接箭头连接符 74

### Alt/Text Metadata 13

直接箭头连接符 75

### Alt/Text Metadata 14

直接箭头连接符 76

### Alt/Text Metadata 15

直接箭头连接符 77

### Alt/Text Metadata 16

直接箭头连接符 78

### Alt/Text Metadata 17

直接箭头连接符 79

### Alt/Text Metadata 18

直接箭头连接符 80

### Alt/Text Metadata 19

Picture 2 | Ampere架構NVIDIA A100 GPU正式亮相，確認發行GeForce產品線| 4Gamers

### Relationships 19

- rId9: image:../media/image32.jpeg

### Shape 20 TextBox 4

GPU

### Alt/Text Metadata 20

TextBox 4

### Slide media/diagram relationships

- rId8: image:../media/image31.png
- rId3: image:../media/image26.png
- rId7: image:../media/image30.png
- rId2: image:../media/image25.png
- rId6: image:../media/image29.png
- rId5: image:../media/image28.png
- rId4: image:../media/image27.png
- rId9: image:../media/image32.jpeg

## Slide 50

### Shape 1 Title 1

AI Architecture

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

50

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

矩形 59

### Alt/Text Metadata 4

矩形 60

### Alt/Text Metadata 5

矩形 61

### Alt/Text Metadata 6

矩形 62

### Shape 7 芯片使能

AI Runtime

### Alt/Text Metadata 7

芯片使能

### Shape 8 框架

AI Framework

### Alt/Text Metadata 8

框架

### Shape 9 框架

Parallel
Training

### Shape 10 Ascend-Nano

CANN*

### Alt/Text Metadata 10

Ascend-Nano

### Shape 11 芯片使能

AI Chip

### Shape 12 Ascend-Nano

模型训练和推理框架

### Shape 13 Ascend-Nano

Compute Architecture for Neural Network

### Shape 15 矩形 73

AI IP和芯片

### Alt/Text Metadata 15

矩形 73

### Alt/Text Metadata 16

直接连接符 83

### Alt/Text Metadata 17

组合 86 | 组合 87 | 图片 21 | 成组 | 矩形 | image12.png | Ascend-Nano

### Relationships 17

- rId3: image:../media/image33.png
- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1

组合 87 | 图片 21 | 成组 | 矩形 | image12.png

### Relationships 17.1

- rId3: image:../media/image33.png
- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1.1

图片 21

### Relationships 17.1.1

- rId3: image:../media/image33.png

### Alt/Text Metadata 17.1.2

成组 | 矩形 | image12.png

### Relationships 17.1.2

- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1.2.1

矩形

### Alt/Text Metadata 17.1.2.3

image12.png

### Relationships 17.1.2.3

- rId4: image:../media/image34.png

### Shape 17.2 Ascend-Nano

Ascend

### Shape 18 矩形 112

计算加速库、芯片算子库和高度自动化的算子开发工具

### Alt/Text Metadata 18

矩形 112

### Shape 19 圆角矩形 190

MindSpore

### Alt/Text Metadata 19

圆角矩形 190

### Shape 20 圆角矩形 191

TensorFlow

### Alt/Text Metadata 20

圆角矩形 191

### Shape 21 圆角矩形 192

PyTorch

### Alt/Text Metadata 21

圆角矩形 192

### Shape 22 圆角矩形 192

PaddlePaddle

### Shape 23 圆角矩形 192

…

### Shape 24 圆角矩形 181

Data parallel

### Alt/Text Metadata 24

圆角矩形 181

### Alt/Text Metadata 25

Group 119 | Group 120 | 矩形 | image12.png | 图片 42 | Picture 121

### Relationships 25

- rId5: image:../media/image35.png
- rId6: image:../media/image36.png
- rId7: image:../media/image37.png

### Alt/Text Metadata 25.1

Group 120 | 矩形 | image12.png | 图片 42

### Relationships 25.1

- rId5: image:../media/image35.png
- rId6: image:../media/image36.png

### Relationships 25.1.3

- rId5: image:../media/image35.png

### Alt/Text Metadata 25.1.4

图片 42

### Relationships 25.1.4

- rId6: image:../media/image36.png

### Alt/Text Metadata 25.2

Picture 121

### Relationships 25.2

- rId7: image:../media/image37.png

### Alt/Text Metadata 26

矩形 145

### Shape 27 Ascend-Nano

CUDA*

### Shape 28 Ascend-Nano

Compute Unified Device Architecture

### Alt/Text Metadata 29

Picture 28

### Relationships 29

- rId8: image:../media/image8.tiff

### Alt/Text Metadata 30

Picture 3

### Relationships 30

- rId9: image:../media/image10.tiff

### Alt/Text Metadata 31

Picture 2 | Ampere架構NVIDIA A100 GPU正式亮相，確認發行GeForce產品線| 4Gamers

### Relationships 31

- rId10: image:../media/image32.jpeg

### Shape 32 圆角矩形 181

Model parallel

### Shape 33 圆角矩形 181

Pipeline parallel

### Shape 34 圆角矩形 181

Hybrid parallel

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId8: image:../media/image8.tiff
- rId3: image:../media/image33.png
- rId7: image:../media/image37.png
- rId6: image:../media/image36.png
- rId5: image:../media/image35.png
- rId10: image:../media/image32.jpeg
- rId4: image:../media/image34.png
- rId9: image:../media/image10.tiff

## Slide 51

### Shape 1 Title 1

Compute Architecture for Neural Network (CANN)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

51

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 49

### Relationships 3

- rId4: image:../media/image38.png

### Alt/Text Metadata 4

矩形 50

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId4: image:../media/image38.png

## Slide 52

### Shape 1 Title 1

Compute Architecture for Neural Network (CANN)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

52

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 49

### Relationships 3

- rId4: image:../media/image38.png

### Alt/Text Metadata 4

矩形 50

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId4: image:../media/image38.png

## Slide 53

### Shape 1 Title 1

Why NN Operator Library?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

53

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId2: image:../media/image39.png

### Shape 4 文本框 5

Each layer in Caffe is an operator

### Alt/Text Metadata 4

文本框 5

### Alt/Text Metadata 5

图片 6

### Relationships 5

- rId3: image:../media/image40.png

### Shape 6 矩形 7

Each node in TensorFlow is an operator

### Alt/Text Metadata 6

矩形 7

### Slide media/diagram relationships

- rId3: image:../media/image40.png
- rId2: image:../media/image39.png

## Slide 54

### Shape 1 Title 1

Difficulties of Developing NN Operator Library

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

54

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

组合 9 | Group 19 | Oval 20 | Picture 21 | guang8 | Text Box 33

### Relationships 3

- rId2: image:../media/image41.png

### Alt/Text Metadata 3.1

Group 19 | Oval 20 | Picture 21 | guang8

### Relationships 3.1

- rId2: image:../media/image41.png

### Alt/Text Metadata 3.1.1

Oval 20

### Alt/Text Metadata 3.1.2

Picture 21 | guang8

### Relationships 3.1.2

- rId2: image:../media/image41.png

### Shape 3.2 Text Box 33

功能逻辑
如何实现

### Alt/Text Metadata 3.2

Text Box 33

### Alt/Text Metadata 4

组合 14 | Group 26 | Oval 27 | Picture 28 | guang8 | Text Box 33

### Relationships 4

- rId2: image:../media/image41.png

### Alt/Text Metadata 4.1

Group 26 | Oval 27 | Picture 28 | guang8

### Relationships 4.1

- rId2: image:../media/image41.png

### Alt/Text Metadata 4.1.1

Oval 27

### Alt/Text Metadata 4.1.2

Picture 28 | guang8

### Relationships 4.1.2

- rId2: image:../media/image41.png

### Shape 4.2 Text Box 33

如何适配
对应硬件

### Alt/Text Metadata 5

组合 20 | Group 16 | Oval 17 | Picture 18 | guang8 | Text Box 33

### Relationships 5

- rId2: image:../media/image41.png

### Alt/Text Metadata 5.1

Group 16 | Oval 17 | Picture 18 | guang8

### Relationships 5.1

- rId2: image:../media/image41.png

### Alt/Text Metadata 5.1.1

Oval 17

### Alt/Text Metadata 5.1.2

Picture 18 | guang8

### Relationships 5.1.2

- rId2: image:../media/image41.png

### Shape 5.2 Text Box 33

如何处理不同
类型的输入

### Alt/Text Metadata 6

组合 25 | Group 29 | Oval 30 | Picture 31 | guang8 | Text Box 33

### Relationships 6

- rId2: image:../media/image41.png

### Alt/Text Metadata 6.1

Group 29 | Oval 30 | Picture 31 | guang8

### Relationships 6.1

- rId2: image:../media/image41.png

### Alt/Text Metadata 6.1.1

Oval 30

### Alt/Text Metadata 6.1.2

Picture 31 | guang8

### Relationships 6.1.2

- rId2: image:../media/image41.png

### Shape 6.2 Text Box 33

如何处理不同
大小的输入

### Alt/Text Metadata 7

组合 30 | Group 13 | Oval 14 | Picture 15 | guang8 | Text Box 33

### Relationships 7

- rId2: image:../media/image41.png

### Alt/Text Metadata 7.1

Group 13 | Oval 14 | Picture 15 | guang8

### Relationships 7.1

- rId2: image:../media/image41.png

### Alt/Text Metadata 7.1.1

Oval 14

### Alt/Text Metadata 7.1.2

Picture 15 | guang8

### Relationships 7.1.2

- rId2: image:../media/image41.png

### Shape 7.2 Text Box 33

如何保证算子
运行的性能

### Alt/Text Metadata 8

组合 35 | Group 13 | Oval 14 | Picture 15 | guang8 | Text Box 33

### Relationships 8

- rId2: image:../media/image41.png

### Relationships 8.1

- rId2: image:../media/image41.png

### Relationships 8.1.2

- rId2: image:../media/image41.png

### Shape 8.2 Text Box 33

不同AI芯片

### Slide media/diagram relationships

- rId2: image:../media/image41.png

## Slide 55

### Shape 1 Title 1

Why NN Operator Library?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

55

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

The motivation of NN operator library:
1, NN tasks are composed of NN operators
2, AI chips are difficult to program, we cannot let AI programmer directly program AI chips
The goal of NN operator library:
Performance + Usability: provide high-performance, well-documented NN library for the upper AI framework such as MindSpore.

### Alt/Text Metadata 3

Content Placeholder 2

## Slide 56

### Shape 1 Title 1

Ascend NN Operator Library

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

56

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 矩形 4

昇腾算子库包含了丰富的高性能算子：
NN（Neural Network）算子库：覆盖了包括TensorFlow、Pytorch、MindSpore、ONNX等框架的常用深度学习算法的计算类型，在算子库中占有最大比重。
BLAS（Basic Linear Algebra Subprograms）算子库：基础线性代数程序集，是进行向量和矩阵等基本线性代数操作的数值库。
DVPP（Digital Video Pre-Processor）算子库：提供高性能的视频编解码、图片编解码、图像裁剪缩放等预处理能力。
AIPP（AI Pre-Processing）算子库：主要实现改变图像尺寸、色域转换（转换图像格式）、减均值/乘系数（图像归一化），并与模型推理过程融合，以满足推理输入要求。
HCCL（Huawei Collective Communication Library）算子库：提供单机多卡以及多机多卡间的Broadcast，allreduce，reducescatter，allgather等集合通信功能，在分布式训练中提供高效的数据传输能力。

### Alt/Text Metadata 3

矩形 4

## Slide 57

### Shape 1 Title 1

算子基本概念-总揽

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

57

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 矩形 5

算子名称（Name）

### Alt/Text Metadata 3

矩形 5

### Shape 4 矩形 6

算子的名称，用于标志网络中的某个算子，同一网络中算子的名称需要保持唯一。如右图所示Conv1，Pool1，Conv2都是此网络中的算子名称，其中Conv1与Conv2算子的类型为Convolution，表示分别做一次卷积运算。

### Alt/Text Metadata 4

矩形 6

### Shape 5 矩形 7

算子类型（Type）

### Alt/Text Metadata 5

矩形 7

### Shape 6 矩形 8

网络中每一个算子根据算子类型进行算子实现的匹配，相同类型的算子的实现逻辑相同。在一个网络中同一类型的算子可能存在多个，例如右图中名称为Conv1的算子与Conv2算子的类型都为Convolution。

### Alt/Text Metadata 6

矩形 8

### Alt/Text Metadata 7

图片 9

### Relationships 7

- rId2: image:../media/image42.png

### Alt/Text Metadata 8

组合 10 | 圆角矩形 13 | 直接箭头连接符 12 | 直接箭头连接符 13 | 文本框 14 | 文本框 15

### Shape 8.1 圆角矩形 13

Conv1

### Alt/Text Metadata 8.1

圆角矩形 13

### Alt/Text Metadata 8.2

直接箭头连接符 12

### Alt/Text Metadata 8.3

直接箭头连接符 13

### Shape 8.4 文本框 14

输入数据

### Alt/Text Metadata 8.4

文本框 14

### Shape 8.5 文本框 15

输出数据

### Alt/Text Metadata 8.5

文本框 15

### Shape 9 矩形 16

数据容器（Tensor）
张量（Tensor）是承载算子数据的容器。如右图所示，算子在网络中执行时，输入数据是一个tensor，算子执行完后，输出数据也是一个tensor。

### Alt/Text Metadata 9

矩形 16

### Slide media/diagram relationships

- rId2: image:../media/image42.png

## Slide 58

### Shape 1 Title 1

算子基本概念-Tensor

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

58

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 表格 17

- 属性 | 定义
- 名称（name） | 用于对Tensor进行索引，不同Tensor的name需保持唯一。
- 形状（shape） | Tensor的形状，比如（10,）或者（1024, 1024）或者（2, 3, 4）等。 / 形式：(i1, i2,…in)，其中i1到in均为正整数
- 数据类型（dtype） | 指定Tensor对象的数据类型。 / 例如：float16, float32, int8, int16, int32, uint8, uint16, bool等。 / 不同计算操作支持的数据类型不同。
- 数据排布格式（format） | 数据的物理排布格式，定义了解读数据的维度。

### Alt/Text Metadata 3

表格 17

### Shape 4 矩形 18

张量（Tensor）是存储算子输入数据与输出数据的容器，
而张量描述符（TensorDesc）是对输入数据与输出数据的描述，
张量描述符的数据结构包含如下属性：

### Alt/Text Metadata 4

矩形 18

### XML fallback texts

- 定义
- 名称（
- name）
- 用于对
- 进行索引，不同
- name
- 需保持唯一。
- 形状（
- shape）
- 的形状，比如（
- 10,
- ）或者（
- 1024, 1024
- 2, 3, 4
- ）等。
- 形式：
- (i1, i2,…in)
- ，其中
- i1
- 到
- in
- 均为正整数
- 数据类型（
- dtype
- 指定
- 对象的数据类型。
- 例如：
- float16, float32, int8, int16, int32, uint8, uint16,
- bo
- 等
- 。
- 不同计算操作支持的数据类型不同。
- 数据排布格式（
- format）
- 数据的物理排布格式，定义了解读数据的维度。

## Slide 59

### Shape 1 Title 1

算子基本概念-Tensor

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

59

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 表格 5

- 张量 | 形状
- 1 | (0,)
- [1,2,3] | (3,)
- [[1,2],[3,4]] | (2,2)
- [[[1,2],[3,4]], [[5,6],[7,8]]] | (2,2,2)

### Alt/Text Metadata 3

表格 5

### Shape 4 矩形 6

形状（shape）

### Alt/Text Metadata 4

矩形 6

### Shape 5 矩形 7

下面分别介绍张量描述符中的形状和数据排布格式。

### Alt/Text Metadata 5

矩形 7

### Shape 6 矩形 8

1，张量的形状，以(D0, D1, … ,Dn-1)的形式表示，D0到Dn是任意的正整数。
如形状(3,4)表示第一维有3个元素，第二维有4个元素，是一个3行4列的矩阵数组。
2，在形状的小括号中有多少个数字，就代表这个张量是多少维的张量。
形状的第一个元素要看张量最外层的中括号中有几个元素，形状的第二个元素要看张量中从左边开始数第二个中括号中有几个元素，依此类推。

### Alt/Text Metadata 6

矩形 8

### XML fallback texts

- (0,)
- [1,2,3]
- (3,)
- [[1,2],[3,4]]
- (2,2)
- [[[1,2],[3,4]], [[5,6],[7,8]]]
- (2,2,2)

## Slide 60

### Shape 1 Title 1

算子基本概念-Tensor

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

60

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 10

### Relationships 3

- rId2: image:../media/image43.png

### Shape 4 文本框 12

produce A {
  for (i, 0, 4) {
    for (j, 0, 20) {
      for (p, 0, 20) {
        for (q, 0, 3) {
          A[((((((i*20) + j)*20) + p)*3) + q)] = a_tensor[((((((i*20) + j)*20) + p)*3) + q)]
        }
      }
    }
  }
}

### Alt/Text Metadata 4

文本框 12

### Shape 5 Content Placeholder 2

shape=(4, 20, 20, 3)的物理含义:
shape里4的含义：假设有4张照片
shape里20,20的含义：每张照片的宽和高都是20，也就是20*20=400个像素,
shape里面3的含义：每个像素点都由红/绿/蓝3色组成
shape=(4, 20, 20, 3)的运算操作:
在编程上，可以把shape理解为操作Tensor的各层循环

### Alt/Text Metadata 5

Content Placeholder 2

### Slide media/diagram relationships

- rId2: image:../media/image43.png

## Slide 61

### Shape 1 Title 1

算子基本概念-Tensor

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

61

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 10

### Relationships 3

- rId2: image:../media/image43.png

### Shape 4 Content Placeholder 2

数据排布格式（format）:
在深度学习领域，多维数据通过多维数组存储，比如卷积神经网络的特征图（Feature Map）通常用四维数组保存，即4D格式：
N：Batch数量，例如图像的数目。
H：Height，特征图高度，即垂直高度方向的像素个数。
W：Width，特征图宽度，即水平宽度方向的像素个数。
C：Channels，特征图通道，例如彩色RGB图像的Channels为3。

### Alt/Text Metadata 4

Content Placeholder 2

### Shape 5 Content Placeholder 2

不同深度学习框架会按照不同的顺序存储特征图数据:
Caffe的排列顺序为[Batch, Channels, Height, Width]即NCHW
TensorFlow的排列顺序为[Batch, Height, Width, Channels] 即NHWC

### Alt/Text Metadata 6

图片 9

### Relationships 6

- rId3: image:../media/image44.png

### Slide media/diagram relationships

- rId3: image:../media/image44.png
- rId2: image:../media/image43.png

## Slide 62

### Shape 1 Title 1

算子基本概念-属性

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

62

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

权重（Weight）:
当输入数据进入计算单元时，会乘以一个权重。例如，如果一个算子有两个输入，则每个输入会分配一个关联权重，一般将认为较重要数据赋予较高的权重，不重要的数据赋予较小的权重，为零的权重则表示特定的特征是无需关注的。
如下图所示，假设输入数据为X1，与其相关联的权重为W1，那么在通过计算单元后，数据变为了X1*W1。

### Alt/Text Metadata 3

Content Placeholder 2

### Alt/Text Metadata 4

图片 7

### Relationships 4

- rId2: image:../media/image45.png

### Slide media/diagram relationships

- rId2: image:../media/image45.png

## Slide 63

### Shape 1 Title 1

算子基本概念-属性

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

63

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

偏差（Bias）:
偏差是除了权重之外，另一个被应用于输入数据的线性分量。它被加到权重与输入数据相乘的结果中，用于改变权重与输入相乘所得结果的范围。
如下图所示，假设输入数据为X1，与其相关联的权重为W1，偏差为B1，那么在通过计算单元后，数据变为了X1*W1+B1

### Alt/Text Metadata 3

Content Placeholder 2

### Alt/Text Metadata 4

图片 5

### Relationships 4

- rId2: image:../media/image46.png

### Slide media/diagram relationships

- rId2: image:../media/image46.png

## Slide 64

### Shape 1 Title 1

CANN算子开发方式

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

64

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

TBE （Tensor Boost Engine）算子
运行在昇腾AI处理器的AI Core上，鉴于AI Core的强大算力，主要负责执行矩阵、向量、标量的计算密集型算子。
TBE提供了基于张量虚拟机（Tensor Virtual Machine，TVM）框架的自定义算子开发能力，提供了用户开发自定义算子所需工具。
AI CPU算子
运行在昇腾AI处理器的AI CPU上，主要负责执行不适合跑在AI Core上的算子，例如非矩阵类的复杂计算，逻辑比较复杂的分支密集型算子，或者算子需要某些数据类型，但AI Core不支持，此时可通过开发AI CPU算子实现昇腾AI处理器对此算子的支持。

### Alt/Text Metadata 3

Content Placeholder 2

## Slide 65

### Shape 1 Title 1

CANN算子开发方式-TBE

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

65

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

DSL（ Domain-Specific Language，基于特性域语言）
DSL接口已高度封装，用户仅需要使用DSL接口完成计算过程的表达，后续的算子调度、算子优化及编译都可通过已有的接口一键式完成，适合初级开发用户。
TIK（ Tensor Iterator Kernel， 张量嵌套内核）
开发者可以通过调用TIK提供的API基于Python语言编写自定义算子，然后TIK编译器会将其编译为适配昇腾AI处理器SoC应用程序的二进制文件。但TIK需要用户手工控制数据搬运和计算流程，入门较高，但开发方式比较灵活，在性能上有一定的优势。

### Alt/Text Metadata 3

Content Placeholder 2

## Slide 66

### Shape 1 Title 1

CANN算子开发方式比较

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

66

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 表格 4

- 参数 | TBE DSL方式 | TIK方式 | AI CPU方式
- 语言 | Python | Python | C++
- 计算单元 | AI Core | AI Core | AI CPU
- 运用场景 | 常用于各种算术逻辑简单向量运算，或内置支持的矩阵运算及池化运算 | 适用各类算子的开发，对于无法通过lambda表达描述的复杂计算场景也有很好的支持，例如排序类操作 | 某些场景下，无法通过AI Core实现的自定义算子，或者需要临时快速打通网络的场景下使用
- 入门难度 | 较低 | 较高 | 中等
- 适用人群 | 入门用户，需要了解NN、TBE DSL相关知识 | 高级用户，需要了解NN，深入理解昇腾AI处理器架构、指令集、数据搬运等相关知识 | 具备C++程序开发能力，对机器学习、深度学习、AI CPU开发流程有一定的了解
- 特点 | TBE DSL接口已高度封装，用户仅需要使用DSL接口完成计算过程的表达，后续的Schedule创建、优化及编译都可通过已有接口一键式完成 | 入门难度高，程序员直接使用TIK提供的API完成计算过程的描述及Schedule过程，需要手工控制数据搬运的参数和Schedule。用户无须关注Buffer地址的分配及数据同步处理，由TIK工具进行管理 | 开发的流程和DSL都是类似的， 不需要了解AI Core的内部架构设计，入门较快
- 不足 | 某些场景下性能可能较低，复杂算子逻辑无法支持表达 | 需要开发者手工控制数据搬运的参数和Schedule过程。 | 无封装的计算接口，计算过程相对繁琐，另外AI CPU性能较低。

### Alt/Text Metadata 3

表格 4

### XML fallback texts

- 参数
- TBE DSL
- TIK
- AI CPU
- 语言
- Python
- C++
- 计算单元
- AI Core
- 运用场景
- 常用于各种算术逻辑简单向量运算，或内置支持的矩阵运算及池化运算
- 适用各类算子的开发，对于无法通过
- lambda
- 表达描述的复杂计算场景也有很好的支持，例如排序类操作
- 某些场景下，无法通过
- 实现的自定义算子
- ，或者需要临时快速打通网络的场景下使用
- 入门难度
- 较低
- 较高
- 中等
- 适用人群
- 入门用户，需要了解
- 、
- 相关知识
- 高级用户，需要了解
- ，深入理解昇腾
- AI
- 处理器架构、指令集、数据搬运等相关知识
- 具备
- 程序开发能力，对机器学习、深度学习、
- 开发流程有一定的了解
- 特点
- 接口已高度封装，用户仅需要使用
- DSL
- 接口完成计算过程的表达，后续的
- Schedule
- 创建、优化及编译都可通过已有接口一键式完成
- 入门难度高，程序员直接使用
- 提供的
- API
- 完成计算过程的描述及
- 过程，需要手工控制数据搬运的参数和
- 。用户无须关注
- Buffer
- 地址的分配及数据同步处理，由
- 工具进行管理
- 开发的流程和
- 都是类似的， 不需要了解
- 的内部架构设计，入门较快
- 不足
- 某些场景下性能可能较低，复杂算子逻辑无法支持表达
- 需要
- 开发者
- 手工控制数据搬运的参数和
- chedule
- 过程。
- 无
- 封装
- 的计算
- 接口，计算过程
- 相对繁琐，另外
- 性能较低
- 。

## Slide 67

### Shape 1 用算力跨越空间

昇腾CANN：向下使能处理器并行加速，向上使能高效开发

### Alt/Text Metadata 1

用算力跨越空间

### Alt/Text Metadata 2

矩形 4

### Alt/Text Metadata 3

矩形 5

### Alt/Text Metadata 4

矩形 6

### Shape 5 文本框 7

全面支持业界AI框架，同步PyTorch社区版本发布

### Alt/Text Metadata 5

文本框 7

### Shape 6 文本框 8

AI框架

### Alt/Text Metadata 6

文本框 8

### Shape 7 文本框 9

昇腾芯片

### Alt/Text Metadata 7

文本框 9

### Alt/Text Metadata 8

矩形 10

### Shape 9 文本框 11

昇腾系列处理器  ......

### Alt/Text Metadata 9

文本框 11

### Alt/Text Metadata 10

图片 4 | 资源 25-8.png

### Relationships 10

- rId2: image:../media/image47.png

### Alt/Text Metadata 11

图片 13

### Relationships 11

- rId3: image:../media/image48.png

### Alt/Text Metadata 12

Group 9 | 图片 15 | 图片 16 | 图片 17 | 图片 18 | 图片 19 | 图片 20 | 文本框 21

### Relationships 12

- rId4: image:../media/image49.png
- rId5: image:../media/image50.png
- rId6: image:../media/image51.png
- rId7: image:../media/image52.png
- rId8: image:../media/image53.png
- rId9: image:../media/image54.png

### Alt/Text Metadata 12.1

图片 15

### Relationships 12.1

- rId4: image:../media/image49.png

### Alt/Text Metadata 12.2

图片 16

### Relationships 12.2

- rId5: image:../media/image50.png

### Alt/Text Metadata 12.3

图片 17

### Relationships 12.3

- rId6: image:../media/image51.png

### Alt/Text Metadata 12.4

图片 18

### Relationships 12.4

- rId7: image:../media/image52.png

### Alt/Text Metadata 12.5

图片 19

### Relationships 12.5

- rId8: image:../media/image53.png

### Alt/Text Metadata 12.6

图片 20

### Relationships 12.6

- rId9: image:../media/image54.png

### Shape 12.7 文本框 21

......

### Alt/Text Metadata 12.7

文本框 21

### Alt/Text Metadata 13

矩形 22

### Alt/Text Metadata 14

直接连接符 23

### Shape 15 文本框 24

Ascend C 支持算子极简开发

### Alt/Text Metadata 15

文本框 24

### Shape 16 文本框 25

支持GPU生态向NPU高效迁移

### Alt/Text Metadata 16

文本框 25

### Shape 17 TextBox 2

CANN

### Alt/Text Metadata 17

TextBox 2

### Alt/Text Metadata 18

直接连接符 93

### Shape 19 矩形 28

图编译加速技术使能处理器并行加速

### Alt/Text Metadata 19

矩形 28

### Shape 20 文本框 29

自动流水

### Alt/Text Metadata 20

文本框 29

### Shape 21 文本框 30

算子深度融合

### Alt/Text Metadata 21

文本框 30

### Shape 22 文本框 31

整图下沉

### Alt/Text Metadata 22

文本框 31

### Shape 23 文本框 32

自适应梯度切分

### Alt/Text Metadata 23

文本框 32

### Shape 24 文本框 33

… …

### Alt/Text Metadata 24

文本框 33

### Alt/Text Metadata 25

矩形: 圆角 26

### Alt/Text Metadata 26

箭头: 下 122

### Alt/Text Metadata 28

图片 37

### Relationships 28

- rId10: image:../media/image55.png

### Alt/Text Metadata 29

组合 38 | 矩形: 圆角 26 | 矩形

### Alt/Text Metadata 29.2

矩形

### Shape 30 文本框 41

周级迁移

### Alt/Text Metadata 30

文本框 41

### Shape 31 文本框 42

保持AI框架不变，模型快速由GPU迁移至NPU运行

### Alt/Text Metadata 31

文本框 42

### Shape 32 文本框 43

全流程工具链
适配扫描、精度调试、性能调优

### Alt/Text Metadata 32

文本框 43

### Shape 33 文本框 44

支持Transformer架构融合算子高效开发

### Alt/Text Metadata 33

文本框 44

### Shape 34 文本框 45

GPU

### Alt/Text Metadata 34

文本框 45

### Shape 35 文本框 46

NPU

### Alt/Text Metadata 35

文本框 46

### Alt/Text Metadata 36

矩形 47

### Shape 37 文本框 48

融合算子库

### Alt/Text Metadata 37

文本框 48

### Shape 38 文本框 49

FlashAttention等Transformer网络加速算子，多模型/多尺寸/多shape全面支持，精度、性能持平业界

### Alt/Text Metadata 38

文本框 49

### Shape 42 文本框 53

符合开发者编程习惯
遵循C/C++标准规范

### Alt/Text Metadata 42

文本框 53

### Shape 43 文本框 54

简化算子编程逻辑
结构化核函数编程

### Alt/Text Metadata 43

文本框 54

### Shape 44 文本框 55

自动获取最优调度
自动化流水并行调度

### Alt/Text Metadata 44

文本框 55

### Alt/Text Metadata 46

组合 57 | 矩形 10 | 直接连接符 14 | Rectangle 121 | 椭圆 18

### Shape 46.1 矩形 10

使能大模型并行计算加速

### Alt/Text Metadata 46.2

直接连接符 14

### Shape 46.3 Rectangle 121

发挥数学力量优化算子及算法，释放澎湃算力

### Alt/Text Metadata 46.3

Rectangle 121

### Shape 46.4 椭圆 18

1

### Alt/Text Metadata 46.4

椭圆 18

### Alt/Text Metadata 47

组合 62 | 矩形 65 | 直接连接符 66 | Rectangle 7 | 椭圆 18

### Shape 47.1 矩形 65

全面开放，生态兼容

### Alt/Text Metadata 47.1

矩形 65

### Alt/Text Metadata 47.2

直接连接符 66

### Shape 47.3 Rectangle 7

兼容业界主流框架

### Alt/Text Metadata 47.3

Rectangle 7

### Shape 47.4 椭圆 18

3

### Alt/Text Metadata 48

组合 67 | 矩形 16 | 直接连接符 17 | Rectangle 120 | 椭圆 18

### Shape 48.1 矩形 16

高效原生开发与生态迁移

### Alt/Text Metadata 48.1

矩形 16

### Alt/Text Metadata 48.2

直接连接符 17

### Shape 48.3 Rectangle 120

典型场景算子开发周期 <2人周

### Alt/Text Metadata 48.3

Rectangle 120

### Shape 48.4 椭圆 18

2

### Slide media/diagram relationships

- rId8: image:../media/image53.png
- rId3: image:../media/image48.png
- rId7: image:../media/image52.png
- rId2: image:../media/image47.png
- rId6: image:../media/image51.png
- rId5: image:../media/image50.png
- rId10: image:../media/image55.png
- rId4: image:../media/image49.png
- rId9: image:../media/image54.png

## Slide 68

### Shape 1 用算力跨越空间

编程范式—— SPMD模型（类CUDA）

### Alt/Text Metadata 1

用算力跨越空间

### Alt/Text Metadata 2

副标题 1

### Shape 3 矩形 73

Ascend C算子编程是SPMD的编程，将需要处理的数据拆分并分布在多个计算核心上运行
多个AI Core共享相同的指令代码，每个核上的运行实例唯一的区别是block_idx不同
block的类似于进程，block_idx就是标识进程唯一性的进程ID，编程中使用函数GetBlockIdx()获取ID

### Alt/Text Metadata 3

矩形 73

### Alt/Text Metadata 4

Picture 2 | https://resource.idp.huawei.com/idpresource/nasshare/editor/image/34040284354/1_zh-cn_image_0000001618836657.png#https://resource.idp.huawei.com/idpresource/nasshare/editor/image/34040284354/1_zh-cn_image_0000001568756418.eddx

### Relationships 4

- rId2: image:../media/image56.png

### Shape 5 矩形 75

昇腾AI处理器SPMD并行计算示意图

### Alt/Text Metadata 5

矩形 75

### Shape 6 矩形 76

SPMD数据并行示意图

### Alt/Text Metadata 6

矩形 76

### Alt/Text Metadata 7

Picture 2 | https://resource.idp.huawei.com/idpresource/nasshare/editor/image/34040284354/1_zh-cn_image_0000001568596262.png#https://resource.idp.huawei.com/idpresource/nasshare/editor/image/34040284354/1_zh-cn_image_0000001568756194.eddx

### Relationships 7

- rId3: image:../media/image57.png

### Slide media/diagram relationships

- rId3: image:../media/image57.png
- rId2: image:../media/image56.png

## Slide 69

### Shape 1 矩形 25

Motivation of In-network Computing

### Alt/Text Metadata 1

矩形 25

### Alt/Text Metadata 2

Rectangle 2

### Shape 3 TextBox 3

算子的输入输出都是tensor，tensor在哪里？

### Alt/Text Metadata 3

TextBox 3

### Shape 4 TextBox 3

Device memory

## Slide 70

### Shape 1 Title 1

Compute Architecture for Neural Network (CANN)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

70

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 49

### Relationships 3

- rId4: image:../media/image38.png

### Alt/Text Metadata 4

矩形 50

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId4: image:../media/image38.png

## Slide 71

### Shape 1 Title 1

CANN平台 —— 计算图引擎GE

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

71

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Ascend-Nano

### Shape 4 矩形 49

GE的核心功能组件：
图准备：全局优化，完成shape推导，维测类算子并行拆分
图拆分：引擎子图切分&边界连接
图优化：引擎/部件级优化，权值格式转换，图聚合（allreduce）
图编译：资源分配和Task生成
图加载：将Task加载到Runtime上
图执行：在Runtime上运行Task

### Alt/Text Metadata 4

矩形 49

### Alt/Text Metadata 5

组合 50 | 图片 51 | 文本框 52

### Relationships 5

- rId3: image:../media/image58.png

### Alt/Text Metadata 5.1

图片 51

### Relationships 5.1

- rId3: image:../media/image58.png

### Shape 5.2 文本框 52

MindSpore

### Alt/Text Metadata 5.2

文本框 52

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId3: image:../media/image58.png

## Slide 72

### Shape 1 Title 1

计算图引擎GE—例子

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

72

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Ascend-Nano

### Alt/Text Metadata 4

图片 9

### Relationships 4

- rId3: image:../media/image59.png

### Shape 5 文本框 21

下边我们将以右侧的MindSpore编写的构建Lenet5的简单代码为入口（见左图），探究异构计算架构对计算图都做了哪些动作。

### Alt/Text Metadata 5

文本框 21

### Shape 6 矩形 1

Lenet5

### Alt/Text Metadata 6

矩形 1

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId3: image:../media/image59.png

## Slide 73

### Shape 1 Title 1

图准备阶段——计算图的构建

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

73

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 9

### Relationships 3

- rId3: image:../media/image59.png

### Shape 4 矩形 1

Lenet5

### Alt/Text Metadata 4

矩形 1

### Shape 5 椭圆 7

x

### Alt/Text Metadata 5

椭圆 7

### Shape 6 椭圆 8

conv1

### Alt/Text Metadata 6

椭圆 8

### Shape 7 椭圆 10

relu

### Alt/Text Metadata 7

椭圆 10

### Shape 8 椭圆 11

max_pool2d

### Alt/Text Metadata 8

椭圆 11

### Shape 9 椭圆 12

conv2

### Alt/Text Metadata 9

椭圆 12

### Alt/Text Metadata 10

椭圆 13

### Alt/Text Metadata 11

椭圆 14

### Shape 12 椭圆 15

flatten

### Alt/Text Metadata 12

椭圆 15

### Shape 13 椭圆 16

fc1

### Alt/Text Metadata 13

椭圆 16

### Alt/Text Metadata 14

椭圆 17

### Shape 15 椭圆 18

fc2

### Alt/Text Metadata 15

椭圆 18

### Alt/Text Metadata 16

椭圆 19

### Shape 17 椭圆 20

fc3

### Alt/Text Metadata 17

椭圆 20

### Shape 18 椭圆 22

output

### Alt/Text Metadata 18

椭圆 22

### Alt/Text Metadata 19

直接箭头连接符 23

### Alt/Text Metadata 20

直接箭头连接符 24

### Alt/Text Metadata 21

直接箭头连接符 25

### Alt/Text Metadata 22

直接箭头连接符 26

### Alt/Text Metadata 23

直接箭头连接符 27

### Alt/Text Metadata 24

直接箭头连接符 28

### Alt/Text Metadata 25

直接箭头连接符 29

### Alt/Text Metadata 26

直接箭头连接符 30

### Alt/Text Metadata 27

直接箭头连接符 31

### Alt/Text Metadata 28

直接箭头连接符 32

### Alt/Text Metadata 29

直接箭头连接符 33

### Alt/Text Metadata 30

直接箭头连接符 34

### Alt/Text Metadata 31

直接箭头连接符 35

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId3: image:../media/image59.png

## Slide 74

### Shape 1 Title 1

初阶图优化-CSE

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

74

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 椭圆 36

+

### Alt/Text Metadata 3

椭圆 36

### Shape 4 椭圆 37

*

### Alt/Text Metadata 4

椭圆 37

### Alt/Text Metadata 5

椭圆 38

### Alt/Text Metadata 6

椭圆 39

### Shape 7 椭圆 40

B

### Alt/Text Metadata 7

椭圆 40

### Shape 8 椭圆 41

C

### Alt/Text Metadata 8

椭圆 41

### Shape 9 椭圆 42

D

### Alt/Text Metadata 9

椭圆 42

### Alt/Text Metadata 10

椭圆 43

### Alt/Text Metadata 11

椭圆 44

### Shape 12 椭圆 45

E

### Alt/Text Metadata 12

椭圆 45

### Alt/Text Metadata 13

椭圆 46

### Alt/Text Metadata 14

直接箭头连接符 47

### Alt/Text Metadata 15

直接箭头连接符 48

### Alt/Text Metadata 16

直接箭头连接符 49

### Alt/Text Metadata 17

直接箭头连接符 50

### Alt/Text Metadata 18

直接箭头连接符 51

### Alt/Text Metadata 19

直接箭头连接符 52

### Alt/Text Metadata 20

直接箭头连接符 53

### Alt/Text Metadata 21

直接箭头连接符 54

### Alt/Text Metadata 22

直接箭头连接符 55

### Alt/Text Metadata 23

直接箭头连接符 56

### Alt/Text Metadata 24

椭圆 57

### Alt/Text Metadata 25

椭圆 58

### Alt/Text Metadata 26

椭圆 59

### Alt/Text Metadata 27

椭圆 60

### Alt/Text Metadata 28

椭圆 61

### Alt/Text Metadata 29

椭圆 62

### Alt/Text Metadata 30

椭圆 63

### Alt/Text Metadata 31

椭圆 64

### Shape 32 椭圆 65

w

### Alt/Text Metadata 32

椭圆 65

### Alt/Text Metadata 33

直接箭头连接符 66

### Alt/Text Metadata 34

直接箭头连接符 67

### Alt/Text Metadata 35

直接箭头连接符 68

### Alt/Text Metadata 36

直接箭头连接符 69

### Alt/Text Metadata 37

直接箭头连接符 70

### Alt/Text Metadata 38

直接箭头连接符 71

### Alt/Text Metadata 39

直接箭头连接符 72

### Alt/Text Metadata 40

直接箭头连接符 73

### Alt/Text Metadata 41

椭圆 74

### Alt/Text Metadata 42

直接箭头连接符 75

### Alt/Text Metadata 43

箭头: 左弧形 76

### Alt/Text Metadata 44

矩形 77

### Alt/Text Metadata 45

矩形 78

### Alt/Text Metadata 46

矩形 79

### Alt/Text Metadata 47

矩形 80

### Speaker notes

CSE（Common-Subexpression Elimination），公共子表达式消除。
简单而言就是将相同输入的表达式进行消除，复用计算结果。

## Slide 75

### Shape 1 Title 1

图优化-算子融合（Intuition）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

75

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

箭头: 右 88

### Alt/Text Metadata 4

组合 3 | 椭圆 81 | 椭圆 82 | 椭圆 83 | 椭圆 84 | 直接箭头连接符 85 | 直接箭头连接符 86 | 直接箭头连接符 87 | 矩形 89

### Shape 4.1 椭圆 81

Data

### Alt/Text Metadata 4.1

椭圆 81

### Shape 4.2 椭圆 82

Conv2D

### Alt/Text Metadata 4.2

椭圆 82

### Shape 4.3 椭圆 83

BatchNorm

### Alt/Text Metadata 4.3

椭圆 83

### Shape 4.4 椭圆 84

Relu

### Alt/Text Metadata 4.4

椭圆 84

### Alt/Text Metadata 4.5

直接箭头连接符 85

### Alt/Text Metadata 4.6

直接箭头连接符 86

### Alt/Text Metadata 4.7

直接箭头连接符 87

### Alt/Text Metadata 4.8

矩形 89

### Alt/Text Metadata 5

组合 2 | 椭圆 90 | 椭圆 91 | 直接箭头连接符 92

### Alt/Text Metadata 5.1

椭圆 90

### Shape 5.2 椭圆 91

Conv2D_BatchNorm_Relu

### Alt/Text Metadata 5.2

椭圆 91

### Alt/Text Metadata 5.3

直接箭头连接符 92

### Shape 6 矩形 93

算子执行的访存特性：
ConvD：顺序写
BatchNorm：顺序读写
ReLU：顺序读写

### Alt/Text Metadata 6

矩形 93

### Alt/Text Metadata 7

组合 6 | 矩形 4 | 矩形 5

### Shape 7.1 矩形 4

算子特性：
  每个算子都从内存读数

### Alt/Text Metadata 7.1

矩形 4

### Shape 7.2 矩形 5

计算完成放回内存

### Alt/Text Metadata 7.2

矩形 5

### Speaker notes

Reducing high-cost operations: global memory access

## Slide 76

### Shape 1 Title 1

Recall: Comparison of Memories

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

76

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

等腰三角形 9

### Alt/Text Metadata 4

直接连接符 13

### Alt/Text Metadata 5

直接连接符 14

### Alt/Text Metadata 6

直接连接符 17

### Alt/Text Metadata 7

直接连接符 19

### Shape 8 文本框 28

SRAM

### Alt/Text Metadata 8

文本框 28

### Shape 9 文本框 29

HBM

### Alt/Text Metadata 9

文本框 29

### Shape 10 文本框 30

DRAM

### Alt/Text Metadata 10

文本框 30

### Shape 11 文本框 31

SSD

### Alt/Text Metadata 11

文本框 31

### Shape 12 文本框 32

DISK

### Alt/Text Metadata 12

文本框 32

### Shape 13 文本框 33

Capacity

### Alt/Text Metadata 13

文本框 33

### Alt/Text Metadata 14

组合 45 | 等腰三角形 34 | 直接连接符 35 | 直接连接符 36 | 直接连接符 37 | 直接连接符 38 | 文本框 39 | 文本框 40 | 文本框 41 | 文本框 42 | 文本框 43 | 文本框 44

### Alt/Text Metadata 14.1

等腰三角形 34

### Alt/Text Metadata 14.2

直接连接符 35

### Alt/Text Metadata 14.3

直接连接符 36

### Alt/Text Metadata 14.4

直接连接符 37

### Alt/Text Metadata 14.5

直接连接符 38

### Alt/Text Metadata 14.6

文本框 39

### Alt/Text Metadata 14.7

文本框 40

### Alt/Text Metadata 14.8

文本框 41

### Alt/Text Metadata 14.9

文本框 42

### Alt/Text Metadata 14.10

文本框 43

### Shape 14.11 文本框 44

Latency

### Alt/Text Metadata 14.11

文本框 44

### Shape 15 文本框 57

Bandwidth

### Alt/Text Metadata 15

文本框 57

### Shape 16 文本框 58

~10MB

### Alt/Text Metadata 16

文本框 58

### Shape 17 文本框 59

~10GB

### Alt/Text Metadata 17

文本框 59

### Shape 18 文本框 60

~100GB

### Alt/Text Metadata 18

文本框 60

### Shape 19 文本框 61

~1TB

### Alt/Text Metadata 19

文本框 61

### Shape 20 文本框 62

~10TB

### Alt/Text Metadata 20

文本框 62

### Shape 21 文本框 63

~1ns

### Alt/Text Metadata 21

文本框 63

### Shape 22 文本框 64

~100ns

### Alt/Text Metadata 22

文本框 64

### Alt/Text Metadata 23

文本框 65

### Shape 24 文本框 66

~1us

### Alt/Text Metadata 24

文本框 66

### Shape 25 文本框 67

~1ms

### Alt/Text Metadata 25

文本框 67

### Alt/Text Metadata 26

组合 8 | 文本框 71 | 组合 7 | 组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51 | 文本框 52 | 文本框 53 | 文本框 54 | 文本框 55 | 文本框 56 | 文本框 68 | 文本框 69 | 文本框 70 | 文本框 72

### Shape 26.1 文本框 71

~100GB/s

### Alt/Text Metadata 26.1

文本框 71

### Alt/Text Metadata 26.2

组合 7 | 组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51 | 文本框 52 | 文本框 53 | 文本框 54 | 文本框 55 | 文本框 56 | 文本框 68 | 文本框 69 | 文本框 70 | 文本框 72

### Alt/Text Metadata 26.2.1

组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51

### Alt/Text Metadata 26.2.1.1

等腰三角形 47

### Alt/Text Metadata 26.2.1.2

直接连接符 48

### Alt/Text Metadata 26.2.1.3

直接连接符 49

### Alt/Text Metadata 26.2.1.4

直接连接符 50

### Alt/Text Metadata 26.2.1.5

直接连接符 51

### Alt/Text Metadata 26.2.2

文本框 52

### Alt/Text Metadata 26.2.3

文本框 53

### Alt/Text Metadata 26.2.4

文本框 54

### Alt/Text Metadata 26.2.5

文本框 55

### Alt/Text Metadata 26.2.6

文本框 56

### Shape 26.2.7 文本框 68

~10MB/s

### Alt/Text Metadata 26.2.7

文本框 68

### Shape 26.2.8 文本框 69

~1GB/s

### Alt/Text Metadata 26.2.8

文本框 69

### Shape 26.2.9 文本框 70

~10GB/s

### Alt/Text Metadata 26.2.9

文本框 70

### Shape 26.2.10 文本框 72

~1TB/s

### Alt/Text Metadata 26.2.10

文本框 72

## Slide 77

### Shape 1 Title 1

图优化-算子融合（UB融合）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

77

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

椭圆 18

### Shape 4 文本框 19

NPU

### Alt/Text Metadata 4

文本框 19

### Shape 5 矩形: 圆角 20

Vector

### Alt/Text Metadata 5

矩形: 圆角 20

### Shape 6 矩形 21

Unified Buffer

### Alt/Text Metadata 6

矩形 21

### Shape 7 矩形: 圆角 22

Main Memory

### Alt/Text Metadata 7

矩形: 圆角 22

### Alt/Text Metadata 8

直接箭头连接符 23

### Alt/Text Metadata 9

直接箭头连接符 24

### Shape 10 文本框 31

以一个简单的Vector算子计算为例，其计算过程通常包含以下几个步骤：
计算任务和数据在片上的上下文切换
新的算子所需数据从主存搬运到Unified Buffer（以下简称UB）
Vector读取UB中的数据进行计算，并将结果存回UB
计算结果从UB搬出到主存

### Alt/Text Metadata 10

文本框 31

### Speaker notes

这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。

## Slide 78

### Shape 1 Title 1

图优化-算子融合（UB融合）

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

78

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 文本框 11

Key Idea of UB融合：泛指片上缓存级别的融合，即数据搬进芯片后，下发的算子计算任务是由多个小算子融合而成的大算子。
UB融合具体计算步骤：
计算任务和数据在片上的上下文切换
新的算子所需数据从主存搬运到Unified Buffer（以下简称UB）
Vector读取UB中的数据进行算子1计算，并将结果存回UB
Vector读取UB中的数据进行算子2计算，并将结果存回UB
Vector读取UB中的数据进行算子3计算，并将结果存回UB
计算结果从UB搬出到主存

### Alt/Text Metadata 3

文本框 11

### Speaker notes

这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。

## Slide 79

### Shape 1 Title 1

算子融合-PyTorch版Attention

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

79

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

图片 4

### Relationships 3

- rId3: image:../media/image60.png

### Speaker notes

这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。

### Slide media/diagram relationships

- rId3: image:../media/image60.png

## Slide 80

### Shape 1 Title 1

算子融合-计算复杂度 vs 内存复杂度

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

80

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

AutoShape 2

### Alt/Text Metadata 4

AutoShape 5

### Alt/Text Metadata 5

Picture 6

### Relationships 5

- rId3: image:../media/image61.png
- rId4: image:../media/image62.svg

### Shape 6 AutoShape 7

计算复杂度 (O(S²D))

### Alt/Text Metadata 6

AutoShape 7

### Shape 7 AutoShape 8

标准 Attention 的理论计算量（主要是矩阵乘法）与序列长度平方 (S²)和隐藏维度 (D)成正比。FlashAttention 并未改变这一理论复杂度，依然需要计算所有 Q-K 对的相似度。

### Alt/Text Metadata 7

AutoShape 8

### Alt/Text Metadata 8

AutoShape 9

### Alt/Text Metadata 9

Picture 10

### Relationships 9

- rId5: image:../media/image63.png
- rId6: image:../media/image64.svg

### Shape 10 AutoShape 11

内存复杂度 (O(S²))

### Alt/Text Metadata 10

AutoShape 11

### Shape 11 AutoShape 12

直接实现时，存储 Score 和 Probability 中间矩阵所需显存与序列长度平方 (S²)成正比。随着序列变长，巨大的矩阵读写会迅速耗尽显存带宽，导致性能瓶颈。

### Alt/Text Metadata 11

AutoShape 12

### Alt/Text Metadata 12

AutoShape 13

### Alt/Text Metadata 13

Picture 14

### Relationships 13

- rId7: image:../media/image65.png
- rId8: image:../media/image66.svg

### Shape 14 AutoShape 15

FlashAttention 的策略

### Alt/Text Metadata 14

AutoShape 15

### Shape 15 AutoShape 16

通过分块 (Tiling)和重新组织计算流程，避免将完整 S×S 矩阵写入高带宽内存(HBM)。用少量额外的计算量换取大量的内存读写优化，实现显著加速。

### Alt/Text Metadata 15

AutoShape 16

### Alt/Text Metadata 16

AutoShape 17

### Alt/Text Metadata 17

Picture 18

### Relationships 17

- rId9: image:../media/image67.png
- rId10: image:../media/image68.svg

### Shape 18 AutoShape 19

💡 核心区别与洞察

### Alt/Text Metadata 18

AutoShape 19

### Shape 19 AutoShape 20

计算复杂度关注“运算次数”，而内存复杂度关注“数据搬运的量”。在现代 GPU 架构下，内存带宽（数据搬运）往往比算力更早成为瓶颈。FlashAttention 正是抓住了这一点，通过“以计算换内存”的思路，解决了长序列 Attention 的落地难题。

### Alt/Text Metadata 19

AutoShape 20

### Speaker notes

这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。

### Slide media/diagram relationships

- rId8: image:../media/image66.svg
- rId3: image:../media/image61.png
- rId7: image:../media/image65.png
- rId6: image:../media/image64.svg
- rId5: image:../media/image63.png
- rId10: image:../media/image68.svg
- rId4: image:../media/image62.svg
- rId9: image:../media/image67.png

## Slide 81

### Shape 1 文本框 1

Where Are We?

### Alt/Text Metadata 1

文本框 1

### Alt/Text Metadata 2

Picture 2

### Relationships 2

- rId2: image:../media/image7.emf

### Alt/Text Metadata 3

Rectangle 36

### Slide media/diagram relationships

- rId2: image:../media/image7.emf

## Slide 82

### Shape 1 Title 1

AI Architecture

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

82

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

矩形 59

### Alt/Text Metadata 4

矩形 60

### Alt/Text Metadata 5

矩形 61

### Alt/Text Metadata 6

矩形 62

### Shape 7 芯片使能

AI Runtime

### Alt/Text Metadata 7

芯片使能

### Shape 8 框架

AI Framework

### Alt/Text Metadata 8

框架

### Shape 9 框架

Parallel
Training

### Shape 10 Ascend-Nano

CANN*

### Alt/Text Metadata 10

Ascend-Nano

### Shape 11 芯片使能

AI Chip

### Shape 12 Ascend-Nano

模型训练和推理框架

### Shape 13 Ascend-Nano

Compute Architecture for Neural Network

### Shape 15 矩形 73

AI IP和芯片

### Alt/Text Metadata 15

矩形 73

### Alt/Text Metadata 16

直接连接符 83

### Alt/Text Metadata 17

组合 86 | 组合 87 | 图片 21 | 成组 | 矩形 | image12.png | Ascend-Nano

### Relationships 17

- rId3: image:../media/image33.png
- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1

组合 87 | 图片 21 | 成组 | 矩形 | image12.png

### Relationships 17.1

- rId3: image:../media/image33.png
- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1.1

图片 21

### Relationships 17.1.1

- rId3: image:../media/image33.png

### Alt/Text Metadata 17.1.2

成组 | 矩形 | image12.png

### Relationships 17.1.2

- rId4: image:../media/image34.png

### Alt/Text Metadata 17.1.2.1

矩形

### Alt/Text Metadata 17.1.2.3

image12.png

### Relationships 17.1.2.3

- rId4: image:../media/image34.png

### Shape 17.2 Ascend-Nano

Ascend

### Shape 18 矩形 112

计算加速库、芯片算子库和高度自动化的算子开发工具

### Alt/Text Metadata 18

矩形 112

### Shape 19 圆角矩形 190

MindSpore

### Alt/Text Metadata 19

圆角矩形 190

### Shape 20 圆角矩形 191

TensorFlow

### Alt/Text Metadata 20

圆角矩形 191

### Shape 21 圆角矩形 192

PyTorch

### Alt/Text Metadata 21

圆角矩形 192

### Shape 22 圆角矩形 192

PaddlePaddle

### Shape 23 圆角矩形 192

…

### Shape 24 圆角矩形 181

Data parallel

### Alt/Text Metadata 24

圆角矩形 181

### Alt/Text Metadata 25

Group 119 | Group 120 | 矩形 | image12.png | 图片 42 | Picture 121

### Relationships 25

- rId5: image:../media/image35.png
- rId6: image:../media/image36.png
- rId7: image:../media/image37.png

### Alt/Text Metadata 25.1

Group 120 | 矩形 | image12.png | 图片 42

### Relationships 25.1

- rId5: image:../media/image35.png
- rId6: image:../media/image36.png

### Relationships 25.1.3

- rId5: image:../media/image35.png

### Alt/Text Metadata 25.1.4

图片 42

### Relationships 25.1.4

- rId6: image:../media/image36.png

### Alt/Text Metadata 25.2

Picture 121

### Relationships 25.2

- rId7: image:../media/image37.png

### Alt/Text Metadata 26

矩形 145

### Shape 27 Ascend-Nano

CUDA*

### Shape 28 Ascend-Nano

Compute Unified Device Architecture

### Alt/Text Metadata 29

Picture 28

### Relationships 29

- rId8: image:../media/image8.tiff

### Alt/Text Metadata 30

Picture 3

### Relationships 30

- rId9: image:../media/image10.tiff

### Alt/Text Metadata 31

Picture 2 | Ampere架構NVIDIA A100 GPU正式亮相，確認發行GeForce產品線| 4Gamers

### Relationships 31

- rId10: image:../media/image32.jpeg

### Shape 32 圆角矩形 181

Model parallel

### Shape 33 圆角矩形 181

Pipeline parallel

### Shape 34 圆角矩形 181

Hybrid parallel

### Speaker notes

全流程服务，分层API和预集成方案
降低核心代码量20%,效率提升50%以上
应对算子多样性，开发效率提升3倍

### Slide media/diagram relationships

- rId8: image:../media/image8.tiff
- rId3: image:../media/image33.png
- rId7: image:../media/image37.png
- rId6: image:../media/image36.png
- rId5: image:../media/image35.png
- rId10: image:../media/image32.jpeg
- rId4: image:../media/image34.png
- rId9: image:../media/image10.tiff

## Slide 83

### Shape 1 Title 1

Why AI Framework?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

83

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

Reasons:
AI algorithms are gaining great attention.
More and more companies and programmers are using them.

### Alt/Text Metadata 3

Content Placeholder 2

### Alt/Text Metadata 4

内容占位符 6

### Relationships 4

- rId2: image:../media/image69.jpeg

### Alt/Text Metadata 5

图片 5

### Relationships 5

- rId3: image:../media/image70.png

### Slide media/diagram relationships

- rId3: image:../media/image70.png
- rId2: image:../media/image69.jpeg

## Slide 84

### Shape 1 Title 1

Why AI Framework?

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

84

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Content Placeholder 2

Two Properties of AI tasks:
AI tasks are varying, but built on common operators.
Implementation complexity is high

### Alt/Text Metadata 3

Content Placeholder 2

### Alt/Text Metadata 4

组合 4 | 矩形 5 | 矩形 6

### Alt/Text Metadata 4.1

矩形 5

### Shape 4.2 矩形 6

有必要将算法中的常用操作封装成组件提供给程序员，以提高深度学习算法开发效率和性能。

### Alt/Text Metadata 4.2

矩形 6

## Slide 85

### Shape 1 Title 1

MindSpore逻辑架构

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

85

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

组合 4 | 矩形 5 | 矩形 6 | 矩形 7 | 矩形 8 | 矩形 9 | 圆角矩形 62 | 圆角矩形 63 | 矩形 12 | 圆角矩形 65 | 圆角矩形 66 | 圆角矩形 67 | 矩形 16 | 圆角矩形 69 | 圆角矩形 70 | 圆角矩形 71 | 圆角矩形 72 | 圆角矩形 73 | 圆角矩形 74 | 圆角矩形 75 | 矩形 24 | 圆角矩形 77 | 圆角矩形 78 | 圆角矩形 79 | 矩形 28 | 矩形 29 | 圆角矩形 82 | 圆角矩形 83 | 圆角矩形 84 | 矩形 33 | 圆角矩形 86 | 圆角矩形 87 | 圆角矩形 88 | 圆角矩形 89 | 圆角矩形 90

### Shape 3.1 矩形 5

MindSpore Extend
GNN/深度概率编程/强化学习/微分方程

### Alt/Text Metadata 3.1

矩形 5

### Shape 3.2 矩形 6

Mind
Armour

### Alt/Text Metadata 3.2

矩形 6

### Shape 3.3 矩形 7

Model Zoo

### Alt/Text Metadata 3.3

矩形 7

### Shape 3.4 矩形 8

MindData

### Alt/Text Metadata 3.4

矩形 8

### Shape 3.5 矩形 9

MindRT

### Alt/Text Metadata 3.5

矩形 9

### Shape 3.6 圆角矩形 62

MindRT(分布式DAG并行执行)

### Alt/Text Metadata 3.6

圆角矩形 62

### Shape 3.7 圆角矩形 63

MindRT Lite/Micro

### Alt/Text Metadata 3.7

圆角矩形 63

### Shape 3.8 矩形 12

MindCompiler

### Alt/Text Metadata 3.8

矩形 12

### Shape 3.9 圆角矩形 65

MindIR

### Alt/Text Metadata 3.9

圆角矩形 65

### Shape 3.10 圆角矩形 66

量化/剪枝/….

### Alt/Text Metadata 3.10

圆角矩形 66

### Shape 3.11 圆角矩形 67

MindAKG(算子自动生成)

### Alt/Text Metadata 3.11

圆角矩形 67

### Shape 3.12 矩形 16

仓颉
前端

### Alt/Text Metadata 3.12

矩形 16

### Shape 3.13 圆角矩形 69

图算融合

### Alt/Text Metadata 3.13

圆角矩形 69

### Shape 3.14 圆角矩形 70

内存优化

### Alt/Text Metadata 3.14

圆角矩形 70

### Shape 3.15 圆角矩形 71

流水线执行

### Alt/Text Metadata 3.15

圆角矩形 71

### Shape 3.16 圆角矩形 72

自动微分

### Alt/Text Metadata 3.16

圆角矩形 72

### Shape 3.17 圆角矩形 73

类型推导

### Alt/Text Metadata 3.17

圆角矩形 73

### Shape 3.18 圆角矩形 74

自动并行

### Alt/Text Metadata 3.18

圆角矩形 74

### Shape 3.19 圆角矩形 75

二阶优化

### Alt/Text Metadata 3.19

圆角矩形 75

### Shape 3.20 矩形 24

MindExpression

### Alt/Text Metadata 3.20

矩形 24

### Shape 3.21 圆角矩形 77

硬件相关优化

### Alt/Text Metadata 3.21

圆角矩形 77

### Shape 3.22 圆角矩形 78

密态AI

### Alt/Text Metadata 3.22

圆角矩形 78

### Shape 3.23 圆角矩形 79

可信AI

### Alt/Text Metadata 3.23

圆角矩形 79

### Alt/Text Metadata 3.24

矩形 28

### Shape 3.25 矩形 29

Mind
Insight

### Alt/Text Metadata 3.25

矩形 29

### Shape 3.26 圆角矩形 82

网络调试

### Alt/Text Metadata 3.26

圆角矩形 82

### Shape 3.27 圆角矩形 83

精度调优

### Alt/Text Metadata 3.27

圆角矩形 83

### Shape 3.28 圆角矩形 84

性能调优

### Alt/Text Metadata 3.28

圆角矩形 84

### Alt/Text Metadata 3.29

矩形 33

### Shape 3.30 圆角矩形 86

CANN昇腾

### Alt/Text Metadata 3.30

圆角矩形 86

### Shape 3.31 圆角矩形 87

CUDA

### Alt/Text Metadata 3.31

圆角矩形 87

### Shape 3.32 圆角矩形 88

Eigen

### Alt/Text Metadata 3.32

圆角矩形 88

### Shape 3.33 圆角矩形 89

Android

### Alt/Text Metadata 3.33

圆角矩形 89

### Shape 3.34 圆角矩形 90

iOS

### Alt/Text Metadata 3.34

圆角矩形 90

### Shape 4 文本框 39

自动并行：整图切分，感知集群拓扑，实现通信开销最小，融合数据并行与模型并行；
二阶优化：利用二阶计算修正梯度更新方向，找到训练梯度最优下降路径，从而加速训练收敛过程；
动静态图结合：统一自动微分引擎支持动静态图，一行代码完成模式切换，兼顾模型开发和执行效率；
AI+科学计算，场景应用创新，拓展MindSpore的边界

### Alt/Text Metadata 4

文本框 39

## Slide 86

### Shape 1 Title 1

关键技术：自动并行

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

86

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 文本框 7

算法科学家需要训练大模型：
需求：超大模型与超大数据集的分布式训练，需通过数据并行+模型并行的混合并行方式，才能高效训练网络。
挑战：
传统graph-level模型切分，计算资源利用率不高，需通过operator-level模型切分提高并行加速比；选择一种高效的模型切分方式需要专家经验；
混合并行复杂度高，传统API难以编写混合并行代码，算法与并行逻辑耦合，修改并行策略，就要重新修改编码；
算法科学家需要关注系统（集群拓扑、网络带宽等）和并行的实现细节，才能写出高性能算法。

### Alt/Text Metadata 3

文本框 7

## Slide 87

### Shape 1 Title 1

关键技术2：二阶优化

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

87

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

组合 5 | 文本框 6 | 文本框 8 | 文本框 9 | 直接箭头连接符 10 | 直接箭头连接符 11 | 直接箭头连接符 12 | 直接箭头连接符 13 | 文本框 14

### Shape 3.1 文本框 6

学习率

### Alt/Text Metadata 3.1

文本框 6

### Shape 3.2 文本框 8

二阶信息矩阵

### Alt/Text Metadata 3.2

文本框 8

### Shape 3.3 文本框 9

一阶梯度

### Alt/Text Metadata 3.3

文本框 9

### Alt/Text Metadata 3.4

直接箭头连接符 10

### Alt/Text Metadata 3.5

直接箭头连接符 11

### Alt/Text Metadata 3.6

直接箭头连接符 12

### Alt/Text Metadata 3.7

直接箭头连接符 13

### Shape 3.8 文本框 14

参数

### Alt/Text Metadata 3.8

文本框 14

### Shape 4 矩形 15

二阶矩阵近似表达

### Alt/Text Metadata 4

矩形 15

### Shape 5 矩形 16

二阶矩阵降频

### Alt/Text Metadata 5

矩形 16

### Shape 6 矩形 17

二阶矩阵降维

### Alt/Text Metadata 6

矩形 17

### Shape 7 矩形 18

软硬协同
高性能算子加速

### Alt/Text Metadata 7

矩形 18

### Shape 8 文本框 19

方案

### Alt/Text Metadata 8

文本框 19

### Alt/Text Metadata 9

上箭头 40

### Alt/Text Metadata 10

上箭头 46

### Alt/Text Metadata 11

上箭头 47

### Alt/Text Metadata 12

矩形 23

### Alt/Text Metadata 13

矩形 24

### Alt/Text Metadata 14

矩形 25

### XML fallback texts

- 挑战
- 训练深度学习模型需要进行大量的计算，训练收敛时间长；
- 二阶优化方法可以有效加速模型收敛，减少迭代次数，同时会引入大量复杂计算，限制其在深度模型训练中广泛应用；
- 二阶优化器参数更新：
- 核心问题
- ：二阶优化器需要额外计算二阶信息矩阵的逆矩阵，计算量大，直接求解时间可达小时级
- ，
- 如何
- 高效求解
- 二阶矩阵是技术难点。

### Slide media/diagram relationships

- rId2: image:../media/image560.png

## Slide 88

### Shape 1 Title 1

关键技术3：动静态图结合

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

88

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

组合 4 | 矩形 5 | 矩形 6 | 矩形 8 | 曲线连接符 53 | 肘形连接符 54 | 肘形连接符 55 | 文本框 12

### Shape 3.1 矩形 5

统一的自动微分引擎

### Alt/Text Metadata 3.1

矩形 5

### Shape 3.2 矩形 6

动态图
调试+调优

### Alt/Text Metadata 3.2

矩形 6

### Shape 3.3 矩形 8

静态图
执行+部署

### Alt/Text Metadata 3.3

矩形 8

### Alt/Text Metadata 3.4

曲线连接符 53

### Alt/Text Metadata 3.5

肘形连接符 54

### Alt/Text Metadata 3.6

肘形连接符 55

### Shape 3.7 文本框 12

set_context

### Alt/Text Metadata 3.7

文本框 12

### Shape 4 矩形 13

统一的自动微分引擎，保证动态图和静态图语法一致

### Alt/Text Metadata 4

矩形 13

### Alt/Text Metadata 5

矩形 14

### Table 6 表格 15

- @ms_function /     def sub_net(self, x): /         x = self.conv(x) /         return x /  /     def construct(self, x): /         x = self.sub_net(x) /         x = self.relu(x) /         return x

### Alt/Text Metadata 6

表格 15

### Alt/Text Metadata 7

矩形 16

### Shape 8 文本框 17

灵活切换：一行代码完成动静态图模式切换

### Alt/Text Metadata 8

文本框 17

### Table 9 表格 18

- #切换为动态图模式 / context.set_context(mode=contex.PYNATIVE_MODE) / #切换为静态图模式 / context.set_context(mode=contex.GRAPH_MODE)

### Alt/Text Metadata 9

表格 18

### Shape 10 文本框 19

调试通过的代码
静态图模式执行

### Alt/Text Metadata 10

文本框 19

### Shape 11 文本框 20

待调试的代码
动态图模式执行

### Alt/Text Metadata 11

文本框 20

### Alt/Text Metadata 12

右大括号 21

### Alt/Text Metadata 13

右大括号 22

### XML fallback texts

- @
- ms_function
- def
- sub_net
- (self, x):
- x =
- self.conv
- (x)
- return x
- construct(self, x):
- self.sub_net
- self.relu
- #
- 切换为动态图模式
- context.set_context
- (mode=
- contex.PYNATIVE_MODE
- )
- 切换为静态图模式
- context.set_context(mode=
- contex.GRAPH_MODE

## Slide 89

### Shape 1 Title 1

关键技术4：AI+科学计算

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

89

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 矩形 26

科学计算近况：

### Alt/Text Metadata 3

矩形 26

### Shape 4 文本框 27

科学计算核心问题是微分方程求解，算力消耗巨大，大规模求解器垄断历年戈登贝尔奖，近年来结合AI方法成为趋势。

### Alt/Text Metadata 4

文本框 27

### Shape 5 文本框 28

业界AI+科学计算现状：
TF：众筹方式构建AI求解模型，典型应用领域取得突破；面向DNN设计的自动微分，计算高阶微分时效率低下；
Nvidia：支持高精度计算；构筑cuBLAS、cuFFT等基础数学库；上层框架依赖TensorFlow，继承TF缺点

### Alt/Text Metadata 5

文本框 28

### Alt/Text Metadata 6

圆角矩形 54

### Alt/Text Metadata 7

直接箭头连接符 33

### Shape 8 矩形 34

非线性拟合，无需解高维方程
神经网络模拟，不需要处理边界条件

### Alt/Text Metadata 8

矩形 34

### Shape 9 圆角矩形 32

AI方法求解

### Alt/Text Metadata 9

圆角矩形 32

### Shape 10 矩形 37

高维微分方程求解，计算量大
边界条件复杂，求解不稳定

### Alt/Text Metadata 10

矩形 37

### Shape 11 圆角矩形 20

传统数值方法

### Alt/Text Metadata 11

圆角矩形 20

### Speaker notes

科学计算才是AI应用的蓝海。。。

## Slide 90

### Shape 1 Title 1

关键技术4：AI+科学计算

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

90

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

组合 12 | 矩形 13 | 组合 14 | 矩形 31 | 矩形 36 | 圆角矩形 81 | 矩形 40 | 矩形 41 | 矩形 42 | 矩形 43 | 矩形 44 | 矩形 45 | 矩形 46 | 矩形 47 | 矩形 48 | 矩形 49 | 圆角矩形 92 | 矩形 51 | 椭圆 52 | 椭圆 53 | 椭圆 54 | 矩形 55 | 组合 15 | 组合 21 | 矩形 29 | 图片 30 | 文本框 22 | 文本框 23 | 矩形 24 | 上箭头 22 | 矩形 16 | Hx | 文本框 18 | 文本框 19

### Relationships 3

- rId5: image:../media/image71.png
- rId2: video:../media/media1.avi
- rId1: media:../media/media1.avi
- rId6: image:../media/image72.png

### Alt/Text Metadata 3.1

矩形 13

### Alt/Text Metadata 3.2

组合 14 | 矩形 31 | 矩形 36 | 圆角矩形 81 | 矩形 40 | 矩形 41 | 矩形 42 | 矩形 43 | 矩形 44 | 矩形 45 | 矩形 46 | 矩形 47 | 矩形 48 | 矩形 49 | 圆角矩形 92 | 矩形 51 | 椭圆 52 | 椭圆 53 | 椭圆 54 | 矩形 55

### Alt/Text Metadata 3.2.1

矩形 31

### Shape 3.2.2 矩形 36

异构硬件

### Alt/Text Metadata 3.2.2

矩形 36

### Shape 3.2.3 圆角矩形 81

通用（稀疏）张量代数计算加速

### Alt/Text Metadata 3.2.3

圆角矩形 81

### Shape 3.2.4 矩形 40

电磁仿真

### Alt/Text Metadata 3.2.4

矩形 40

### Shape 3.2.5 矩形 41

气象

### Alt/Text Metadata 3.2.5

矩形 41

### Shape 3.2.6 矩形 42

分子动力学

### Alt/Text Metadata 3.2.6

矩形 42

### Shape 3.2.7 矩形 43

…

### Alt/Text Metadata 3.2.7

矩形 43

### Shape 3.2.8 矩形 44

大规模高维微分方程AI求解器

### Alt/Text Metadata 3.2.8

矩形 44

### Shape 3.2.9 矩形 45

应用场景

### Alt/Text Metadata 3.2.9

矩形 45

### Shape 3.2.10 矩形 46

AI建模

### Alt/Text Metadata 3.2.10

矩形 46

### Shape 3.2.11 矩形 47

AI求解

### Alt/Text Metadata 3.2.11

矩形 47

### Shape 3.2.12 矩形 48

框架加速

### Alt/Text Metadata 3.2.12

矩形 48

### Alt/Text Metadata 3.2.13

矩形 49

### Shape 3.2.14 圆角矩形 92

MindCompiler

### Alt/Text Metadata 3.2.14

圆角矩形 92

### Shape 3.2.15 矩形 51

自动微分

### Alt/Text Metadata 3.2.15

矩形 51

### Shape 3.2.16 椭圆 52

1

### Alt/Text Metadata 3.2.16

椭圆 52

### Shape 3.2.17 椭圆 53

2

### Alt/Text Metadata 3.2.17

椭圆 53

### Shape 3.2.18 椭圆 54

3

### Alt/Text Metadata 3.2.18

椭圆 54

### Shape 3.2.19 矩形 55

MindSpore

### Alt/Text Metadata 3.2.19

矩形 55

### Alt/Text Metadata 3.3

组合 15 | 组合 21 | 矩形 29 | 图片 30 | 文本框 22 | 文本框 23 | 矩形 24 | 上箭头 22

### Relationships 3.3

- rId5: image:../media/image71.png

### Alt/Text Metadata 3.3.1

组合 21 | 矩形 29 | 图片 30

### Relationships 3.3.1

- rId5: image:../media/image71.png

### Shape 3.3.1.1 矩形 29

台风灾害预警

### Alt/Text Metadata 3.3.1.1

矩形 29

### Alt/Text Metadata 3.3.1.2

图片 30

### Relationships 3.3.1.2

- rId5: image:../media/image71.png

### Shape 3.3.2 文本框 22

40小时

### Alt/Text Metadata 3.3.2

文本框 22

### Shape 3.3.3 文本框 23

分钟级

### Alt/Text Metadata 3.3.3

文本框 23

### Shape 3.3.4 矩形 24

台风公里级风速预报

### Alt/Text Metadata 3.3.4

矩形 24

### Alt/Text Metadata 3.3.5

上箭头 22

### Shape 3.4 矩形 16

手机电磁场模拟

### Alt/Text Metadata 3.4

矩形 16

### Alt/Text Metadata 3.5

Hx

### Relationships 3.5

- rId2: video:../media/media1.avi
- rId1: media:../media/media1.avi
- rId6: image:../media/image72.png

### Shape 3.6 文本框 18

10小时

### Alt/Text Metadata 3.6

文本框 18

### Shape 3.7 文本框 19

1小时

### Alt/Text Metadata 3.7

文本框 19

### Speaker notes

大规模高维微分方程AI求解器： AI建模加速材料、气象等领域；AI求解加速麦克斯韦电磁方程、Burgers等，性能提升10倍；AI框架加速支持海洋GOMO模型，性能提升1.5倍。
自动微分：前向自动微分、混合自动微分、向量化自动微等，性能提升10倍。
通用（稀疏）张量代数计算加速：支持基础BLAS运算(矩阵求逆等)、FFT运算、稀疏矩阵运算等，性能提升2-3倍。

### Slide media/diagram relationships

- rId1: media:../media/media1.avi
- rId6: image:../media/image72.png
- rId5: image:../media/image71.png

## Slide 91

### Shape 1 Title 1

Cerebras’s Wafer Scale Engine (2019)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

91

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 6

### Relationships 4

- rId3: image:../media/image73.png

### Alt/Text Metadata 5

Picture 7

### Relationships 5

- rId3: image:../media/image73.png

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

The largest ML accelerator chip
400,000 cores
18 GB of on-chip memory
9 PB/s memory bandwidth

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

- rId3: image:../media/image73.png

## Slide 92

### Shape 1 Title 1

Scratchpad Memory in Cerebras WSE

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Scratchpad Memory
Highly parallel and distributed scratchpad SRAM memory with 2D mesh interconnection fabric across tiles
16-byte read and 8-byte write single-cycle latency
48 KB scratchpad in each tile, totaling 18 GB on the full chip
No shared memory

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

92

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId3: image:../media/image74.emf

### Shape 5 TextBox 5

Rocki et al., “Fast stencil-code computation on a wafer-scale processor.” SC 2020.

### Alt/Text Metadata 5

TextBox 5

### Shape 6 TextBox 6

84 dies

### Alt/Text Metadata 6

TextBox 6

### Shape 7 TextBox 7

4539 tiles

### Alt/Text Metadata 7

TextBox 7

### Alt/Text Metadata 8

Rectangle 8

### Alt/Text Metadata 9

Straight Arrow Connector 10

### Speaker notes

Kamil Rocki, Dirk Van Essendelft, Ilya Sharapov, Robert Schreiber, Michael Morrison, Vladimir Kibardin, Andrey Portnoy, Jean Francois Dietiker, Madhava Syamlal, and Michael James. 2020. Fast stencil-code computation on a wafer-scale processor. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis(SC '20). IEEE Press, Article 58, 1–14.

### Slide media/diagram relationships

- rId3: image:../media/image74.emf

## Slide 93

### Shape 1 Title 1

Cerebras’s Wafer Scale Engine-2 (2021)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

93

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 7

### Relationships 4

- rId3: image:../media/image73.png

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

### Shape 7 Rectangle 12

NVIDIA Ampere GA100

### Alt/Text Metadata 7

Rectangle 12

### Alt/Text Metadata 8

Picture 2 | https://cerebras.net/wp-content/uploads/2021/03/img-chip-section-1.png

### Relationships 8

- rId4: image:../media/image75.png

### Shape 9 Rectangle 15

https://cerebras.net/product/#overview

### Alt/Text Metadata 9

Rectangle 15

### Shape 10 Rectangle 13

The largest ML accelerator chip
850,000 cores
40 GB of on-chip memory
20 PB/s memory bandwidth

### Alt/Text Metadata 10

Rectangle 13

### Slide media/diagram relationships

- rId3: image:../media/image73.png
- rId4: image:../media/image75.png
