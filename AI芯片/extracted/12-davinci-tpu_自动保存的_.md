# 12-davinci-tpu [自动保存的].pptx

- Slides: 122

## Slide 1: Computer Arch. & AI SystemsLecture 12: AI Processors

### Extracted Shape Text
- Computer Arch. & AI SystemsLecture 12: AI Processors
- Prof. Zeke Wang
- Zhejiang University
- May 21 2026

### Notes
- 1

## Slide 2: Recall:深度学习算法计算和访存特性分析

- Images: 0; Tables: 2

### Extracted Shape Text
- Recall:深度学习算法计算和访存特性分析
- MAC (Multiply–Accumulate)

| Operator | 计算特性 | 访存特性 |
| --- | --- | --- |
| Conv | 矩阵相乘 | Burst+stride |
| Activation | 单向量操作 | Sequential |
| Pooling | 单矩阵Reduce操作 | Burst+stride |
| FC | 矩阵相乘 | Sequential |

- Fixed Memory Access Pattern
- AI相关计算内，矩阵乘法计算量的占比高于90%。

| Attention | 矩阵相乘 | Burst+stride |
| --- | --- | --- |


## Slide 3: Recall: Five Design Principles of AI Accelerators

### Extracted Shape Text
- Recall: Five Design Principles of AI Accelerators
- Five Design Principles:
- Global Buffer: 使用专有的存储器来减少数据搬运的距离与开销，比如将复杂的cache设计替换成scratchpad memory (global buffer)。
- 简化控制模块: 将缩减的高级微架构特性而节省出的面积，用于增加更多的运算单元或者片上存储。
- 并行计算模块: 使用能够符合特定领域加速需求最简单的并行形式，例如，对于矩阵运算的加速，单条指令直接支持小矩阵运算。
- 量化: 减少计算数据尺寸与类型来符合特定领域性能要求，例如，深度学习中，推理可以采用int8量化方式进行。
- 专用编程语言: 使用DSA专用语言进行编程。

## Slide 4: Recall: AI Accelerator vs. CPU

- Images: 0; Tables: 1

### Extracted Shape Text
- Recall: AI Accelerator vs. CPU

|  | CPU | DSA |
| --- | --- | --- |
| On-chip Memory | Cache | Global Buffer |
| Instruction Issue | Superscalar | In-order/simple |
| Parallelism | Inter-instruction | Intra-instruction |
| Fuctionality | Full | Partial |
| Optimization Purpose | Low Latency | High Throughput |
| Programming Language | General | Domain-specific |


## Slide 5: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 6: Two Main Properties of AI Accelerators

- Images: 2; Tables: 0

### Extracted Shape Text
- Two Main Properties of AI Accelerators
- 访存
- 计算
- 很多矩阵、向量计算
- 当前的主要挑战: 不足的算力, 访存代价太大!
- [Sze, MIT, https://tinyurl.com/SzeMITDL2020]
- 很多外存访问

## Slide 7: Main Challenges of AI Accelerator

- Images: 1; Tables: 0

### Extracted Shape Text
- Main Challenges of AI Accelerator
- 能耗分析: 32bit的DRAM读比32bit的浮点乘法能耗高出2个数量级!
- Mission: 减少能耗高的操作, DRAM/SRAM Read、32b Multiply。

## Slide 8: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 9: Why On-chip Buffer?

### Extracted Shape Text
- Why On-chip Buffer?
- 最差情况：所有内存读写都是访问外部内存。
- AlexNet: 需要 724M MAC操作和2896M次外部内存访问
- [Sze, MIT, https://tinyurl.com/SzeMITDL2020]
- MAC
- ALU
- Filter weight
- Partial sum
- Feature map
- 1x
- DRAM
- Memory Read
- 200x
- DRAM
- Memory Write
- 200x
- Updated partial sum

## Slide 10: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 11: Cache or Buffer?

- Images: 6; Tables: 1

### Extracted Shape Text
- Cache or Buffer?

|  | Cache | Buffer |
| --- | --- | --- |
| 能耗 | 高 | 低 |
| 芯片面积 | 大 | 小 |
| 管理方式 | 自动 | 手动 |

- Main memory (DRAM)
- Mat
- Cache or Buffer
- Vec
- Scalar
- AI加速器
- AI加速器的主要目标: 提高算力、降低功耗!
- 隐含的意思: 可以牺牲可编程性!

## Slide 12: Programming Model: Cache vs. Buffer

### Extracted Shape Text
- Programming Model: Cache vs. Buffer
- DDR uint32_t a[32] = {0, 1, 2, …, 31};
- DDR uint32_t b[32] = {0, 1, 2, …, 31};
- DDR uint32_t c[32];
- Unified_Buffer uint32_t a_ub[32];
- Unified_Buffer uint32_t b_ub[32];
- Unified_Buffer uint32_t c_ub[32];
- Dma_Mov(a_ub, a);
- Dma_Mov(b_ub, b);
- Vector_add(c_ub, a_ub, b_ub);
- Dma_Mov(c, c_ub);
- uint32_t a[32] = {0, 1, 2, …, 31};
- uint32_t b[32] = {0, 1, 2, …, 31};
- uint32_t c[32];
- for(uint i = 0; i < 32; i++){
- c[i] = a[i] + b[i];
- }
- Manual
- Cache
- Buffer
- Cache-based Programming Model: Automatic
- Buffer-based Programming Model: manual manipulation

## Slide 13: How to Use Buffer?

- Images: 1; Tables: 0

### Extracted Shape Text
- How to Use Buffer?
- Global Buffer: Separate, low unit access cost!
- L1: for MTE module
- UB: for Vector module
- L0A/B/C: for Cube module
- Difficult to program due to awareness of buffer location!

## Slide 14: External Memory Access: Solved!

- Images: 1; Tables: 0

### Extracted Shape Text
- External Memory Access: Solved!
- [Sze, MIT, https://tinyurl.com/SzeMITDL2020]
- Global Buffer

## Slide 15: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 16: Recall: Data Movement Energy

- Images: 0; Tables: 1

### Extracted Shape Text
- Recall: Data Movement Energy

| 32-bit Operation | Energy (pJ) | ADD (int) Relative Cost |
| --- | --- | --- |
| ADD (int) | 0.1 | 1 |
| ADD (float) | 0.9 | 9 |
| Register File | 1 | 10 |
| MULT (int) | 3.1 | 31 |
| MULT (float) | 3.7 | 37 |
| SRAM Cache | 5 | 50 |
| DRAM | 640 | 6400 |

- Han+, “EIE: Efficient Inference Engine on Compressed Deep Neural Network,” ISCA 2016.
- A memory access consumes ~6400X
- the energy of an integer addition

## Slide 17: Recall: FF vs. SRAM vs. DRAM vs. Flash

### Extracted Shape Text
- Recall: FF vs. SRAM vs. DRAM vs. Flash
- Flip-Flops
- Very fast, parallel access
- Very expensive (one bit costs tens of transistors)
- Static RAM
- Relatively fast, only one data word at a time
- Expensive (one bit costs 6+ transistors)
- Dynamic RAM
- Slower, one data word at a time, reading destroys content (refresh), needs special process for manufacturing
- Cheap (one bit costs only one transistor plus one capacitor)
- Flash Memory
- Much slower, access takes a long time, non-volatile
- Very cheap (one transistor stores 16 bits or no transistors involved)

### Notes
- 17

## Slide 18: Reducing Global Buffer Accesses

- Images: 1; Tables: 0

### Extracted Shape Text
- Reducing Global Buffer Accesses
- AI Core
- DRAM
- Global
- Buffer
- PE
- PE
- PE
- PE
- Control
- Reg File
- Problem: Global Buffer access is expensive.
- Solution: Increasing Register File utilization.

## Slide 19: Weight Stationary (WS)

- Images: 1; Tables: 0

### Extracted Shape Text
- Weight Stationary (WS)
- [Sze, https://tinyurl.com/SzeMITDL2020]
- Key idea (Systolic array):
- 最大程度地减少从Global Buffer读取Weight (conv),
- 广播Activations和沿着PE水平方向上累加Psum.
- 例子: TPU [Jouppi, ISCA, 2017]

## Slide 20: Output Stationary (OS)

- Images: 1; Tables: 0

### Extracted Shape Text
- Output Stationary (OS)
- Key idea:
- 最大程度地减少从Global Buffer读取和存储Psum, 尽量把Psum留在PE内。
- 广播Weight和沿着PE水平方向上复用Activation。
- 例子: [Moons, VLSI, 2016]
- [Sze, https://tinyurl.com/SzeMITDL2020]

## Slide 21: Input Stationary (IS)

- Images: 1; Tables: 0

### Extracted Shape Text
- Input Stationary (IS)
- Key idea:
- 最大程度地减少从Global Buffer读取Activation, 尽量把Activation留在PE内。
- 并行读Weight, 沿着PE水平方向上累加Psum。
- 例子: [SCNN, ISCA, 2017]
- [Sze, https://tinyurl.com/SzeMITDL2020]

## Slide 22: Row Stationary (RS)

- Images: 1; Tables: 0

### Extracted Shape Text
- Row Stationary (RS)
- Key idea:
- 从Global Buffer读出Filter中的一行和Activation的一个滑窗, 留在PE内。
- 尽量减少从Global Buffer的整体读出量，而不只是一个维度的。
- 例子: [Chen, ISCA, 2016]
- [Sze, https://tinyurl.com/SzeMITDL2020]

## Slide 23: Goal of Reducing Global Buffer Accesses

- Images: 1; Tables: 0

### Extracted Shape Text
- Goal of Reducing Global Buffer Accesses
- Global Buffer
- Data Reuse
- [Sze, MIT, https://tinyurl.com/SzeMITDL2020]

## Slide 24: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 25: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 26: 深度学习：计算和访存特性

- Images: 0; Tables: 1

### Extracted Shape Text
- 深度学习：计算和访存特性
- MAC (Multiply–Accumulate)

| Operator | 计算特性 | 访存特性 |
| --- | --- | --- |
| Conv | 矩阵相乘 | Burst+stride |
| Activation | 单向量操作 | Sequential |
| Pooling | 单矩阵Reduce操作 | Burst+stride |
| FC | 矩阵相乘 | Sequential |
| … | … | … |

- Fixed Memory Access Pattern
- AI相关计算量里，矩阵乘法计算量的占比高于90%。

## Slide 27: 计算模块的设计原则

- Images: 3; Tables: 0

### Extracted Shape Text
- 计算模块的设计原则
- 尽量多定制计算单元，略不择手段！

## Slide 28: Matrix Multiplication Unit

### Extracted Shape Text
- Matrix Multiplication Unit
- Scalar:
- for (int i = 0; i < 16; i++)
- for (int j = 0; j < 16; j++)
- for (int k = 0; k < 16; k++)
- C[i][j] += A[i][k] * B[k][j]
- for (int i = 0; i < 16; i++)
- for (int j = 0; j < 16; j++)
- C[i][j] = A[i][:] * B[:][j]
- C[:][:] = A[:][:] * B[:][:]
- Vector:
- Matrix:
- 周期数：16*16*16 = 4096
- 每周期内存访问量: 2 (rd), 1/16 (wr)
- 周期数：16*16 = 256
- 每周期内存访问量: 2*16 (rd), 1 (wr)
- 周期数：1
- 每周期内存访问量: 2*16*16 (rd), 16*16 (wr)
- 算力密度高
- 灵活
- A
- 16
- 16
- B
- 16
- X
- C
- =
- 16
- 16
- A[16][16], B[16][16], C[16][16];
- float

## Slide 29: 增加计算模块

- Images: 1; Tables: 0

### Extracted Shape Text
- 增加计算模块
- Cube模块(算力核心)
- 单指令处理小矩阵乘法
- Vector模块(算力核心)
- 单指令处理向量操作，如activation

## Slide 30: 增加计算模块

- Images: 1; Tables: 0

### Extracted Shape Text
- 增加计算模块

## Slide 31: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 32: AI Chips

- Images: 3; Tables: 0

### Extracted Shape Text
- AI Chips
- TPU
- Ascend
- Cambricon

## Slide 33: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 34: AI Chips

- Images: 3; Tables: 0

### Extracted Shape Text
- AI Chips
- TPU
- Ascend
- Cambricon

## Slide 35: 晟腾310/910 芯片结构示意图

- Images: 1; Tables: 0

### Extracted Shape Text
- 晟腾310/910 芯片结构示意图
- L2 Buffer vs. L2 Cache
- 同一个介质，两种使用模式
- Buffer：程序员可见并可以直接读写（地址空间和DDR/HBM不重合）
- Cache: 作为DDR/HBM高速缓存，程序员不可见
- DDR/HBM
- DDR: 普通内存，带宽低/价格低，在推理芯片310中
- HBM： High Bandwidth Memory, 带宽高, 成本高，在训练芯片310中

## Slide 36: 华为晟腾310推理芯片

### Extracted Shape Text
- 华为晟腾310推理芯片

## Slide 37: 华为晟腾910训练芯片

- Images: 1; Tables: 0

### Extracted Shape Text
- 华为晟腾910训练芯片

## Slide 38: DaVinci AI core内部是怎么样的？

### Extracted Shape Text
- DaVinci AI core内部是怎么样的？

### Notes
- 现在的计算世界往三个方向发展
- 38

## Slide 39: Huawei Ascend

- Images: 2; Tables: 0

### Extracted Shape Text
- Huawei Ascend

## Slide 40: Cube模块 （矩阵运算， 算力担当）

- Images: 1; Tables: 0

### Extracted Shape Text
- Cube模块 （矩阵运算， 算力担当）
- 矩阵乘运算单元Cube : 一拍完成一个fp16的 2个16x16矩阵相乘； C = A * B; 如果是int8输入,则一拍完成 16*32 与 32*16 矩阵乘。
- 累加器Accumulator: 把当前矩阵乘的结果与前次计算的中间结果相加 （ C = A * B + C ）， 可以用于完成卷积中加bias操作。
- L0A/L0B/L0C Buffer: L0A 存储矩阵乘的左矩阵数据，L0B 存储矩阵乘的右矩阵数据， L0C 存储矩阵乘的结果和中间结果。
- A/B DFF: 数据寄存器，缓存当前计算的16*16 左/右子矩阵。
- Accum DFF : 数据寄存器，缓存当前计算的16*16结果矩阵。

### Notes
- Cube
- :
- 矩阵乘运算单元，一拍完成一个
- fp16
- 的
- 16x16
- 与
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
- 32*16
- 矩阵乘。
- Accumulator
- 累加器， 把当前矩阵乘的结果与前次计算的中间结果相加， 可以用于完成卷积中加
- bias
- 操作。
- B + C
- L0A/L0B/L0C Buffer
- : L0A
- 存储矩阵乘的左矩阵数据，
- L0B
- 存储矩阵乘的右矩阵数据，
- L0C
- 存储矩阵乘的结果和中间结果。
- A/B DFF
- 数据寄存器，缓存当前计算的
- 16
- 左
- /
- 右子矩阵。
- Accum
- DFF
- 16*16
- 结果矩阵。
- 40

## Slide 41: Vector模块 （向量运算，多面手）

- Images: 1; Tables: 0

### Extracted Shape Text
- Vector模块 （向量运算，多面手）
- 向量运算单元Vector Unit： 覆盖各种基本的计算类型和许多定制的计算类型，主要包括FP16/FP32/int32/Int8等数据类型的计算，支持连续或者固定间隔寻址；或者VA寄存器寻址（不规则向量运算）
- SIMD长度：一条Vector指令可以完成两个128长度fp16类型的向量相加/乘，或者64个fp32/int32类型的向量相加/乘
- Unified Buffer(UB)： 保存Vector运算的源操作数和目的操作数； 一般要求32Byte对齐；
- 数据从L0C->UB：随数据搬运在Vector Unit完成一些RELU/数据格式转换等操作

### Notes
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
- fp16
- 类型的向量相加
- /
- 乘， 或者
- 64
- 个
- fp32/int32
- 乘
- Unified Buffer(UB)
- ： 保存
- 运算的源操作数和目的操作数； 一般要求
- 32Byte
- 对齐；
- 数据从
- L0C->UB
- ，需要以
- 作为中转，并可以随数据搬运完成一些
- RELU/
- 数据格式转换等操作
- 41

## Slide 42: Scalar模块 （标量运算，司令部）

- Images: 1; Tables: 0

### Extracted Shape Text
- Scalar模块 （标量运算，司令部）
- Scalar Unit： 负责完成AICore中的标量运算，功能上可以看做一个小CPU；完成整个程序的循环控制、分支判断、CUBE/Vector等指令的地址和参数计算以及基本的算术运算等‘
- Unified Buffer or Scalar Buffer: 晟腾310/910 Scalar Unit不能直接访问外面的DDR/HBM, 需要预留UB的一部分(310)或者使用专门的Scalar Buffer(910)用作Scalar Unit的堆栈空间
- GPR：通用寄存器，目前包含32个通用寄存器
- SPR: 专用寄存器，为了支持指令集一些指令的特殊需要，Davinci设计了许多专用寄存器，比如CoreID, BLOCKID, VA, STATUS, CTRL等寄存器

## Slide 43: DaVinci AI core内部的Buffer模块是怎么工作的？

### Extracted Shape Text
- DaVinci AI core内部的Buffer模块是怎么工作的？

### Notes
- 现在的计算世界往三个方向发展
- 43

## Slide 44: MTE/BIU和片上高速存储(Buffer)

- Images: 1; Tables: 0

### Extracted Shape Text
- MTE/BIU和片上高速存储(Buffer)
- BIU (Bus Interface Unit): AICore 的“大门”，与总线交互的接口。AICore从外部（L2/DDR/HBM）读取、写入数据的出入口。负责把AICore的读写请求转换为总线上的请求并完成协议交互等工作。
- MTE (Memory Transfer Unit): 也被称作 LSU (Load Store Unit), 负责AICore内部数据在不同Buffer之间的读写管理，以及完成一些格式转换的操作，比如padding, 转置, Img2Col, 解压等
- L1 Buffer: AICore内最大的一块数据中转区(1MB)，可以用来暂存AICore需要反复使用的一些数据从而减少从总线读写； Img2col操作等MTE的数据格式转换功能需源数据必须位于L1 Buffer
- L0A/L0B/L0C/UB/Scalar Buffer: 前面已介绍

### Notes
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
- 32B/2B
- Scalar Buffer(SB)
- 16KB
- 2B
- 44

## Slide 45: DaVinci AI core内部的控制模块是怎么样的？

### Extracted Shape Text
- DaVinci AI core内部的控制模块是怎么样的？

### Notes
- 现在的计算世界往三个方向发展
- 45

## Slide 46: 指令和控制系统

- Images: 8; Tables: 0

### Extracted Shape Text
- 指令和控制系统

### Notes
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
- 指令分发模
- , CUBE/Vector/MTE
- 指令经过
- 处理之后，地址、参数等要素都已经配置好，之后
- 单元根据指令的类型，将
- CUBE/Vector/MTE
- 指令分别分发到对应的指令队列等待相应的执行单元调度执行
- Cube/Vector/MTE1/MTE2/MTE3 Queue:
- Cube/Vector/MTE1/MTE2/MTE3
- 指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行
- 46

## Slide 47: 指令和控制系统

- Images: 2; Tables: 0

### Extracted Shape Text
- 指令和控制系统
- Event Sync: 用于控制不同队列指令(也叫做不同指令流水)之间的依赖和同步的模块
- barrier()
- set_flag.PIPE_dst.PIPE_src wait_flag.PIPE_dst.PIPE_src

### Notes
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
- Block
- 执行控制
- 执行完之后中断和状态申报
- 执行错误状态申报等
- 47

## Slide 48: Ascend: Pros and Cons

### Extracted Shape Text
- Ascend: Pros and Cons
- Davinci架构的优势：
- CUBE极致算力高 —— 同等功耗和面积下，Davinci Core比Nvidia V100/TPU 极致算力都高；功耗面积相似的情况下，晟腾910算力是Nvidia V100 2.1倍
- Buffer访问、管理效率高：单DavinciCore内 CUBE/VECTOR/MTE 有效并行+丰富的片上Buffer和带宽， 让Davinci 能够高效的发挥极致算力，且有效控制功耗
- 硬核随路计算指令：提供了硬件支持的Img2Col/格式转换等随路计算指令，方便了程序设计
- Davinci架构的不足：
- 难编程：对编程人员要求比较高 (事件同步、Buffer使用), 编程易用性有待提升
- 生态不完善：软件生态才开始， 相关配套工具、包括Debug手段、PMU等都还不够丰富

### Notes
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
- 指令分发模
- , CUBE/Vector/MTE
- 指令经过
- 处理之后，地址、参数等要素都已经配置好，之后
- 单元根据指令的类型，将
- CUBE/Vector/MTE
- 指令分别分发到对应的指令队列等待相应的执行单元调度执行
- Cube/Vector/MTE1/MTE2/MTE3 Queue:
- Cube/Vector/MTE1/MTE2/MTE3
- 指令队列；同一个队列里的指令顺序执行；不同队列之间，可以并行执行
- 48

## Slide 49: Contents

### Extracted Shape Text
- Contents
- 深度学习加速器设计目标
- 减少内存访问
- 减少Global Buffer访问
- 增加计算
- 常见AI加速器分析比较
- 华为Ascend
- Google TPU
- 寒武纪Cambridge

## Slide 50: Google TPU

### Extracted Shape Text
- Google TPU
- TPU v1
- Inference only
- TPU v2
- Support Training
- TPU v3
- Support Training
- More Computing Power
- TPU v4
- TPU4: for Training
- TPU4i: for Inference

## Slide 51: TPU v1

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v1
- Matrix Multiply Unit
- 256x256 MACs
- Systolic Array
- 24% area
- Unified Buffer
- 24 MB
- 29% area
- [Google, In-Datacenter Performance Analysis of a Tensor Processing Unit, ISCA, 2017]
- TPU v1
- For inference, model is pre-stored in DDR3, and data is from the host via PCIe

## Slide 52: Systolic Arrays: Motivation

### Extracted Shape Text
- Systolic Arrays: Motivation
- Goal: design an accelerator that has
- Simple, regular design (keep # unique parts small and regular)
- High concurrency  high performance
- Balanced computation and I/O (memory) bandwidth
- Idea: Replace a single processing element (PE) with a regular array of PEs and carefully orchestrate flow of data between the PEs
- such that they collectively transform a piece of input data before outputting it to memory
- Benefit: Maximizes computation done on a single piece of data element brought from memory

## Slide 53: Systolic Arrays: Intuition

### Extracted Shape Text
- Systolic Arrays: Intuition
- H. T. Kung, “Why Systolic Architectures?,” IEEE Computer 1982.
- Normal CPU:
- Systolic Array:
- Memory
- PE
- Memory
- PE3
- PE2
- PE1
- Analogy: blood flow (heart  many cells  heart)
- Memory: heart, Data: blood, PE: cell
- Memory pulses data through PEs: Heart pulses the blood to different cells for “concurrent processing”.

## Slide 54: Systolic Arrays: Benefit （Intuition）

### Extracted Shape Text
- Systolic Arrays: Benefit （Intuition）
- Normal CPU:
- Systolic Array:
- IF
- ID
- SUB
- MEM
- WB
- IF
- ID
- MUL
- MEM
- WB
- IF
- ID
- ADD
- MEM
- WB
- IF
- ID
- SUB
- MEM
- WB
- IF
- ID
- MUL
- MEM
- WB
- IF
- ID
- ADD
- MEM
- WB
- SUB
- MUL
- IF
- ID
- ADD
- MEM
- WB
- SUB
- MUL
- Memory
- PE
- Memory
- PE3
- PE2
- PE1
- For Loop:
- ADD
- SUB
- MUL
- IF
- ID
- ADD
- MEM
- WB
- T1:
- T2:
- T3:
- T4:
- T5:
- T6:
- …
- …

### Notes
- 54

## Slide 55: Systolic Arrays in AI Accelerator

### Extracted Shape Text
- Systolic Arrays in AI Accelerator
- Systolic array can be multi-dimensional
- The most popular one used by AI ａｃｃｅｌｅｒａｔｏｒ is two-dimensional．
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- Cell
- Left
- Right
- Upper
- Down
- Processing engine (PE):
- How a PE updates:
- Right = Left
- Down = Upper
- Cell = Cell + Upper * Left

## Slide 56: Example 2D Systolic Array Computation

- Images: 1; Tables: 0

### Extracted Shape Text
- Example 2D Systolic Array Computation
- Multiply two 3x3 matrices A and B
- Keep the final result in PE accumulators
- =
- ×

## Slide 57: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 0

## Slide 58: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 1

## Slide 59: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 2

## Slide 60: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 3

## Slide 61: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 4

## Slide 62: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 5

## Slide 63: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 6

## Slide 64: Systolic Arrays

### Extracted Shape Text
- Systolic Arrays
- T = 7

## Slide 65: TPU v1 TPU v2

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v1 TPU v2
- [Google, Google’s Training Chips Revealed: TPUv2 and TPUv3, Hot Chips, 2020]

## Slide 66: TPU v1 TPU v2 (Vector Memory)

- Images: 2; Tables: 0

### Extracted Shape Text
- TPU v1 TPU v2 (Vector Memory)
- TPU1:Buffers between fixed function units
-  TPU2: Single vector memory

## Slide 67: TPU v1 TPU v2 (Vector Unit)

- Images: 2; Tables: 0

### Extracted Shape Text
- TPU v1 TPU v2 (Vector Unit)
- TPU1: A fixed function activation pipeline
-  TPU2: General purpose vector unit

### Notes
- 128 x 128
- 67

## Slide 68: TPU v1 TPU v2 (Vector Unit)

- Images: 2; Tables: 0

### Extracted Shape Text
- TPU v1 TPU v2 (Vector Unit)
- TPU1: MMU connected to vector memory
-  TPU2: MMU connected to vector unit

## Slide 69: TPU v1 TPU v2 (Memory)

- Images: 2; Tables: 0

### Extracted Shape Text
- TPU v1 TPU v2 (Memory)
- TPU1: DDR3 connected to MMU
-  TPU2: HBM connected to Vector Memory

## Slide 70: TPU v2 (Interconnect)

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v2 (Interconnect)
- 500Gbps per link
- 2Tbps
- 2Tbps
- 2Tbps
- 2Tbps

## Slide 71: Google TPU v2

- Images: 1; Tables: 0

### Extracted Shape Text
- Google TPU v2

## Slide 72: Google TPU v3

- Images: 1; Tables: 0

### Extracted Shape Text
- Google TPU v3

## Slide 73: TPU v2 vs. TPU v3

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v2 vs. TPU v3
- TPU v2
- TPU v3

## Slide 74: TPU v4

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v4

### Notes
- 4
- 个
- MMU
- 74

## Slide 75: TPU v5/v6

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v5/v6

### Notes
- 4
- 个
- MMU
- 75

## Slide 76: GB200 NVL72 GPU

- Images: 1; Tables: 0

### Extracted Shape Text
- GB200 NVL72 GPU
- GB200 NVL72 GPU
- 18 1U Compute Tray
- 1 Compute Tray has 2 Bianca board
- A board has 1 Grace CPU + 2 Blackwell GPUs
- 9 1U NVSwitch5 Tray
- With two 28.8Tb/s NVSwitch5 ASIC chips
- 14.4Tb/s: backward toward the backplane
- 14.4Tb/s: toward the front plate
- 900GB/s between any two of 72 GPUs
- 4 1U Power Shelf 33KW

### Notes
- 4
- 个
- MMU
- 76

## Slide 77: GB200 NVL72 GPU: Bianca Board

- Images: 1; Tables: 0

### Extracted Shape Text
- GB200 NVL72 GPU: Bianca Board

### Notes
- 4
- 个
- MMU
- 77

## Slide 78: Huawei AI CloudMatrix 384

### Extracted Shape Text
- Huawei AI CloudMatrix 384
- CloudMatrix 384: 384 Ascend 910C NPUs
- Advantages:
- 300 PFLOPs of dense BF16 compute (2x GB200 NVL72)
- 3.6x aggregate memory capacity
- 2.1x more memory bandwidth
- Disadvantages:
- 4.1x the power of a GB200 NVL72,
- 2.5x worse power per FLOPs,
- 1.9x worse power per TB/s memory bandwidth,
- 1.2x worse power per TB HBM memory capacity

### Notes
- Huawei
- follows NV…
- 78

## Slide 79: AI模型训练中，内存带宽往往是整体性能的瓶颈，而AI加速器并不能很明显地提高内存带宽的利用效率。

### Extracted Shape Text
- AI模型训练中，内存带宽往往是整体性能的瓶颈，而AI加速器并不能很明显地提高内存带宽的利用效率。
- 为啥AI加速器只要集中在推理(Inference)而不是训练(Training)?
- AI推理加速器才可以提高10倍以上的能耗比。

### Notes
- 现在的计算世界往三个方向发展
- 79

## Slide 80: AI推理加速器提高10倍以上的能耗比，因为推理加速器能把模型存到AI芯片上.

### Extracted Shape Text
- AI推理加速器提高10倍以上的能耗比，因为推理加速器能把模型存到AI芯片上.
- 而AI训练加速器不能太显著地提高能耗比，而训练加速器不能把模型和中间结果都存到AI芯片上。

### Notes
- 现在的计算世界往三个方向发展
- 80

## Slide 81: END!!!

### Extracted Shape Text
- END!!!

### Notes
- 现在的计算世界往三个方向发展
- 81

## Slide 82: Systolic Array in TPU

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Array in TPU
- Systolic Array in TPU
- One 256 x 256 matrix multiply unit in TPU1.
- Two 128x128 matrix multiply units in TPU2/TPU3.
- What is the tradeoff?
- Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

## Slide 83: An Example Modern Systolic Array: TPU (I)

- Images: 2; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU (I)
- Tensor Processing Unit (ＴＰＵ)
- First AI accelerator adopts systolic array to accelerate matrix multiplication.
- Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

## Slide 84: Systolic Computation Example

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Computation Example
- Convolution
- Used in filtering, pattern matching, correlation, polynomial evaluation, etc …
- Many image processing tasks
- Machine learning: up to hundreds of convolutional layers in Convolutional Neural Networks (CNN)

## Slide 85: Systolic Array: Advantages & Disadvantages

### Extracted Shape Text
- Systolic Array: Advantages & Disadvantages
- Advantages:
- Makes multiple uses of each data item  reduced need for fetching/refetching  better use of memory bandwidth
- High concurrency
- Regular design (both data and control flow)
- Disadvantages:
- Not good at exploiting irregular parallelism
- Relatively special purpose  need software, programmer support to be a general purpose model

## Slide 86: LeNet-5, a Convolutional Neural Network for Hand-Written Digit Recognition

- Images: 1; Tables: 0

### Extracted Shape Text
- LeNet-5, a Convolutional Neural Network for Hand-Written Digit Recognition
- This is a 1024*8 bit input, which will have a truth table of 2 8196 entries
- Slide credit: Hwu & Kirk

## Slide 87: An Example of 2D Convolution

### Extracted Shape Text
- An Example of 2D Convolution
- Structure information
- Input: 5*5 (blue)
- Kernel (filter): 3*3 (grey)
- Output: 5*5 (green)
- Computation information
- Stride: 1
- Padding: 1 (white)
- Output Dim = (Input + 2*Padding - Kernel) / Stride + 1
- Input feature map
- Output feature map

### Notes
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
- depth
- Stride
- number
- of
- input
- values
- will
- jump
- when
- sliding
- on
- feature
- map.
- When
- stride
- =
- 1,
- moves
- adjacent input
- without
- jumping.
- Padding
- zeros
- added
- outside
- 1
- means
- adding
- circle
- The
- size
- output
- can
- be
- calculated:
- Output
- (Input
- +
- 2
- *
- –
- Kernel)
- /
- this
- example
- :
- (5
- 3)
- 5
- 87

## Slide 88: An Example of 2D Convolution

### Extracted Shape Text
- An Example of 2D Convolution
- Input Layer
- CNN kernel
- Output Layer

### Notes
- Mark which layer is which -> first layer as input, second as kernel and last as output
- 88

## Slide 89: Convolutional Neural Networks: Demo

- Images: 2; Tables: 0

### Extracted Shape Text
- Convolutional Neural Networks: Demo
- http://yann.lecun.com/exdb/lenet/index.html

## Slide 90: Implementing a Convolutional Layer with Matrix Multiplication

- Images: 1; Tables: 0

### Extracted Shape Text
- Implementing a Convolutional Layer with Matrix Multiplication
- Slide credit: Reproduced from Hwu & Kirk

## Slide 91: Power of Convolutions and Applied Courses

### Extracted Shape Text
- Power of Convolutions and Applied Courses
- In 2010, Prof. Andreas Moshovos adopted Professor Hwu’s ECE498AL Programming Massively Parallel Processors Class
- Several of Prof. Geoffrey Hinton’s graduate students took the course
- These students developed the GPU implementation of the Deep CNN that was trained with 1.2M images to win the ImageNet competition
- Slide credit: Hwu & Kirk

## Slide 92: Example: AlexNet (2012)

- Images: 1; Tables: 0

### Extracted Shape Text
- Example: AlexNet (2012)
- AlexNet wins the ImageNet classification competition with ~10% points higher accuracy than state-of-the-art
- Krizhevsky et al., “ImageNet Classification with Deep Convolutional Neural Networks”, NIPS 2012.

## Slide 93: Google improves accuracy by adding more network layers

- Images: 1; Tables: 0

### Extracted Shape Text
- Google improves accuracy by adding more network layers
- From 8 in AlexNet to 22 in GoogLeNet
- Szegedy et al., “Going Deeper with Convolutions”, CVPR 2015.
- Example: GoogLeNet (2014)

## Slide 94: He et al., “Deep Residual Learning for Image Recognition”, CVPR 2016.

- Images: 2; Tables: 0

### Extracted Shape Text
- He et al., “Deep Residual Learning for Image Recognition”, CVPR 2016.
- Example: ResNet (2015)
- Human: 5.1%
- First CNN

## Slide 95: Neural Network Layer Examples

- Images: 1; Tables: 0

### Extracted Shape Text
- Neural Network Layer Examples
- By Cmglee - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=104937230

## Slide 96: Convolution

- Images: 1; Tables: 0

### Extracted Shape Text
- Convolution
- Used in filtering, pattern matching, correlation, polynomial evaluation, etc …
- Many image processing tasks
- Machine learning: up to hundreds of convolutional layers in Convolutional Neural Networks (CNN)
- Systolic Computation Example: Convolution (I)

## Slide 97: Systolic Computation Example: Convolution (II)

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Computation Example: Convolution (II)
- y1 = w1x1 + w2x2 + w3x3
- y2 = w1x2 + w2x3 + w3x4
- y3 = w1x3 + w2x4 + w3x5

## Slide 98: Systolic Computation Example: Convolution (III)

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Computation Example: Convolution (III)
- Worthwhile to implement adder and multiplier separately to allow overlapping of add/mul executions

## Slide 99: Systolic Computation Example: Convolution (IV)

### Extracted Shape Text
- Systolic Computation Example: Convolution (IV)
- One needs to carefully orchestrate when data elements are input to the array
- And when output is buffered
- This gets more involved when
- Array dimensionality increases
- PEs are less predictable in terms of latency

## Slide 100: Example 2D Systolic Array Computation

- Images: 3; Tables: 0

### Extracted Shape Text
- Example 2D Systolic Array Computation
- Multiply two 3x3 matrices (inputs)
- Keep the final result in PE accumulators
- P = M
- Q = N
- R = R + M*N

## Slide 101: Two-Dimensional Systolic Arrays

- Images: 2; Tables: 0

### Extracted Shape Text
- Two-Dimensional Systolic Arrays

## Slide 102: Combinations

- Images: 1; Tables: 0

### Extracted Shape Text
- Combinations
- Systolic arrays can be chained together to form powerful systems
- This systolic array is capable of producing on-the-fly least-squares fit to all the data that has arrived up to any given moment

## Slide 103: Systolic Arrays: Pros and Cons

### Extracted Shape Text
- Systolic Arrays: Pros and Cons
- Advantages:
- Principled: Efficiently makes use of limited memory bandwidth, balances computation to I/O bandwidth availability
- Specialized (computation needs to fit PE organization/functions)
-  improved efficiency, simple design, high concurrency/ performance
-  good to do more with less memory bandwidth requirement
- Downside:
- Specialized
-  not generally applicable because computation needs to fit the PE functions/organization

## Slide 104: Each PE in a systolic array

### Extracted Shape Text
- Each PE in a systolic array
- Can store multiple “weights”
- Weights can be selected on the fly
- Eases implementation of, e.g., adaptive filtering
- Taken further
- Each PE can have its own data and instruction memory
- Data memory  to store partial/temporary results, constants
- Leads to stream processing, pipeline parallelism
- More generally, staged execution
- More Programmability in Systolic Arrays

## Slide 105: Pipeline-Parallel (Pipelined) Programs

- Images: 1; Tables: 0

### Extracted Shape Text
- Pipeline-Parallel (Pipelined) Programs
- Suleman+, “Data Marshaling for Multi-core Architectures,” ISCA 2010.

## Slide 106: Stages of Pipelined Programs

- Images: 1; Tables: 0

### Extracted Shape Text
- Stages of Pipelined Programs
- Loop iterations are divided into code segments called stages
- Threads execute stages on different cores
- loop {
- Compute1
- Compute2
- Compute3
- }
- A
- B
- C
- A
- B
- C

### Notes
- 106

## Slide 107: Pipelined File Compression Example

- Images: 1; Tables: 0

### Extracted Shape Text
- Pipelined File Compression Example

## Slide 108: Example Systolic Array: The WARP Computer

### Extracted Shape Text
- Example Systolic Array: The WARP Computer
- HT Kung, CMU, 1984-1988
- Linear array of 10 cells, each cell a 10 Mflop programmable processor
- Attached to a general purpose host machine
- HLL and optimizing compiler to program the systolic array
- Used extensively to accelerate vision and robotics tasks
- Annaratone et al., “Warp Architecture and Implementation,” ISCA 1986.
- Annaratone et al., “The Warp Computer: Architecture, Implementation, and Performance,” IEEE TC 1987.

## Slide 109: The WARP Computer

- Images: 1; Tables: 0

### Extracted Shape Text
- The WARP Computer

## Slide 110: The WARP Cell

- Images: 1; Tables: 0

### Extracted Shape Text
- The WARP Cell

## Slide 111: An Example Modern Systolic Array: TPU (I)

- Images: 1; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU (I)
- Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

## Slide 112: An Example Modern Systolic Array: TPU (II)

- Images: 2; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU (II)
- Jouppi et al., “In-Datacenter Performance Analysis of a Tensor Processing Unit”, ISCA 2017.

## Slide 113: Recall: Example 2D Systolic Array Computation

- Images: 3; Tables: 0

### Extracted Shape Text
- Recall: Example 2D Systolic Array Computation
- Multiply two 3x3 matrices (inputs)
- Keep the final result in PE accumulators
- P = M
- Q = N
- R = R + M*N

## Slide 114: An Example Modern Systolic Array: TPU (III)

- Images: 1; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU (III)

## Slide 115: An Example Modern Systolic Array: TPU2

- Images: 1; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU2
- https://www.nextplatform.com/2017/05/17/first-depth-look-googles-new-second-generation-tpu/
- 4 TPU chips
- vs 1 chip in TPU1
- High Bandwidth Memory
- vs DDR3
- Floating point operations
- vs FP16
- 45 TFLOPS per chip
- vs 23 TOPS
- Designed for training
- and inference
- vs only inference

## Slide 116: An Example Modern Systolic Array: TPU3

- Images: 1; Tables: 0

### Extracted Shape Text
- An Example Modern Systolic Array: TPU3
- https://cloud.google.com/tpu/docs/system-architecture
- 32GB HBM per chip
- vs 16GB HBM in TPU2
- 4 Matrix Units per chip
- vs 2 Matrix Units in TPU2
- 90 TFLOPS per chip
- vs 45 TFLOPS in TPU2

## Slide 117: Cerebras’s Wafer Scale Engine (2019)

- Images: 2; Tables: 0

### Extracted Shape Text
- Cerebras’s Wafer Scale Engine (2019)
- Cerebras WSE
- 1.2 Trillion transistors
- 46,225 mm2
- Largest GPU
- 21.1 Billion transistors
- 815 mm2
- The largest ML
- accelerator chip
- 400,000 cores
- NVIDIA TITAN V
- https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning
- https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/

### Notes
- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 117

## Slide 118: Cerebras’s Wafer Scale Engine-2 (2021)

- Images: 2; Tables: 0

### Extracted Shape Text
- Cerebras’s Wafer Scale Engine-2 (2021)
- Cerebras WSE-2
- 2.6 Trillion transistors
- 46,225 mm2
- Largest GPU
- 54.2 Billion transistors
- 826 mm2
- The largest ML
- accelerator chip
- 850,000 cores
- NVIDIA Ampere GA100
- https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning
- https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/

### Notes
- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 118

## Slide 119: Digital Design & Computer Arch.Lecture 19b: Systolic Arrays

### Extracted Shape Text
- Digital Design & Computer Arch.Lecture 19b: Systolic Arrays
- Prof. Onur Mutlu
- ETH Zürich
- Spring 2021
- 7 May 2021

### Notes
- 119

## Slide 120: Approaches to (Instruction-Level) Concurrency

### Extracted Shape Text
- Approaches to (Instruction-Level) Concurrency
- Pipelining
- Fine-Grained Multithreading
- Out-of-order Execution
- Dataflow (at the ISA level)
- Superscalar Execution
- VLIW
- Systolic Arrays
- Decoupled Access Execute
- SIMD Processing (Vector and array processors, GPUs)

## Slide 121: Systolic Arrays

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Arrays
- H. T. Kung, “Why Systolic Architectures?,” IEEE Computer 1982.
- Analogy:
- Memory: heart
- Data: blood
- PEs: cells
- Memory pulses
- data through
- PEs

## Slide 122: Systolic Architectures

- Images: 1; Tables: 0

### Extracted Shape Text
- Systolic Architectures
- Basic principle: Replace a single PE with a regular array of PEs and carefully orchestrate flow of data between the PEs
- Balance computation and memory bandwidth
- Differences from pipelining:
- These are individual PEs
- Array structure can be non-linear and multi-dimensional
- PE connections can be multidirectional (and different speed)
- PEs can have local memory and execute kernels (rather than a piece of the instruction)
