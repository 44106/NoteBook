# Computer System III: Chapter 1 and Chapter 2 ILP Zero-Base Notes

来源文件：

- `chapter 1(13).pdf`: Chapter 1, 86 pages
- `chapter 2-1(12).pdf`: Chapter 2-1, 92 pages
- `chapter 2-2(13).pdf`: Chapter 2-2, 77 pages

这份讲义按零基础学习顺序组织。页码范围写在小节标题里，方便和 PPT 对照。这里不是只记结论，而是把“为什么要这样设计”“公式为什么成立”“例题每一步在算什么”串起来。

## 0. 先建立全局地图

这三份 PPT 的主线其实是一句话：

> 从一个问题 `problem` 到真实电子 `electrons`，中间隔着算法、程序、运行时系统、ISA、微结构、逻辑、电路；计算机系统课程就是要教你看懂这些层次如何连接，并用定量方法判断设计是否真的更快。

第 1 章先回答：计算机系统是什么？性能怎么定义？为什么架构设计必须定量分析？

第 2 章回答：当 CPU 已经能一条条执行指令后，怎样让多条指令重叠执行？流水线会遇到什么冲突？硬件如何用动态调度、Tomasulo、ROB、推测、多发射、VLIW、超流水进一步挖掘指令级并行性？

核心层级如下：

```text
problem
  -> algorithm
  -> program
  -> runtime system (VM, OS, MM)
  -> ISA / architecture
  -> microarchitecture
  -> logic
  -> circuits
  -> electrons
```

你可以把它理解成“用户想解决的问题”一步步变成“芯片里电信号变化”的翻译链。

## 1. Chapter 1: Fundamentals of Computer System

### 1.1 课程目标：拿走自己的系统，而不只是背概念（p1-p19）

PPT 开头反复问：

- What are you take away from computer system III?
- In the age of AI, is a deep understanding of the computer system still important?
- Seriously, you take away your own system.

老师想强调：这门课不是只学名词，而是要把软件、操作系统、ISA、CPU、内存、I/O、硬件电路贯通起来，最后理解乃至搭建一个能运行程序的系统。

#### 系统 1、系统 2、系统 3 的递进

PPT 用三张“大结构图”展示课程实验的逐级扩展：

1. 系统 1：从门级电路到单周期 CPU
   - 组合逻辑电路
   - 时序逻辑电路
   - 数值表示与门电路
   - 基本运算电路
   - Verilog
   - 多路选择器、七段数码管、加法器、有限状态机、乘法器、计数器
   - 单周期 CPU
   - SCPU 数据通路
   - SCPU 控制单元
   - RISC-V 指令集与汇编
   - Spike、QEMU、Vivado、Verilator、FPGA 等工具链

2. 系统 2：加入流水线、异常中断和操作系统启动
   - 流水线 CPU
   - Pipeline 基础、阶段寄存器
   - 冒险处理 forwarding 技术
   - 流水线实现与性能分析
   - 流水线冲突与处理
   - AXI4-Lite 总线模型与使用
   - CSR 寄存器、中断与异常处理
   - RISC-V 时钟中断处理
   - 内核启动逻辑与运行
   - 内核线程管理与调度
   - 进程管理、进程调度、CPU 调度、进程通信、同步、互斥、死锁
   - 软硬件协同，例如 OS 加载

3. 系统 3：加入虚拟内存、Cache、动态预测和用户态
   - 定量分析方法
   - ILP、DLP、TLP
   - Cache 设计与性能分析
   - 内存 Cache 设计
   - 内存管理单元 MMU
   - 虚拟地址转换
   - SV39 分页/虚拟内存管理
   - 用户态进程实现与用户态切换
   - 缺页异常处理与 fork 机制
   - 基于 BHT/BTB 的动态分支预测
   - RAT、RS、ROB 等乱序执行相关结构

这些词先不用全懂。现在只要建立感觉：越往后，CPU 不再只是“算术器+寄存器”，而是要和操作系统、内存层次、异常、中断、预测、乱序执行一起协同。

#### ZJV：自己的 CPU 和系统

PPT 展示了 ZJV 1.0、ZJV 2.0、ZJV plus、MMM、求是 I 号等成果。里面提到：

- 自主搭建差分测试框架 `dtqemu`
- 模拟 RAM 和串口等外设
- 同步中断
- 比对 QEMU 和 AMipsel 的寄存器
- 支持 pmon 全部指令运行
- 支持 ucore 运行
- 完成 Linux 启动流程到用户态
- 便捷 Linux 调试
- 逐梦杯总决赛中自主设计优化，获得 1789 性能分
- 面向通用系统，启动 Linux 发行版
- 着眼安全特性，保护数据完整性和机密性

这说明课程背后的目标不是“纸面 CPU”，而是能跑系统软件的 CPU + system。

### 1.2 从问题到电子：系统抽象层次（p20-p31）

PPT 从 `problem` 一层层加：

```text
problem
algorithm
program
runtime system (VM, OS, MM)
ISA (architecture)
microarchitecture
logic
circuits
electrons
```

每一层的含义：

- problem：用户真正想解决的问题，比如排序、训练模型、播放视频、存储文件。
- algorithm：解决问题的方法，比如快速排序、矩阵乘法算法、图搜索算法。
- program：把算法写成 C/C++/Java/Python/Rust 等程序。
- runtime system：程序运行时依赖的环境，包括虚拟机 VM、操作系统 OS、内存管理 MM。
- ISA / architecture：指令集架构。软件能看到的硬件接口，例如 RISC-V 有哪些指令、寄存器、异常规则。
- microarchitecture：微结构。某个 CPU 具体怎样实现 ISA，例如单周期、流水线、乱序、多发射。
- logic：逻辑设计，如与门、或门、加法器、控制逻辑。
- circuits：电路层，晶体管、电压、电容、时序。
- electrons：最底层的物理电子运动。

关键区别：

- ISA 是“承诺给软件的接口”。
- 微结构是“硬件内部如何兑现这个承诺”。

同一个 RISC-V 程序可以在简单单周期 CPU 上跑，也可以在高性能乱序 CPU 上跑。软件看到的 ISA 一样，但内部微结构完全不同。

PPT 还给了能力要求：系统能力在计算机科学与技术培养中占很大比例，其中包括系统开发能力、系统设计能力、系统应用能力、系统认知能力等。意思是系统不是边缘知识，而是计算机专业核心能力。

PPT 接着用 Cyber Security / Information Security 的 CSEC 2017 和 Cyber2yr 2020 说明：系统能力对网络安全/信息安全方向同样重要。安全不是只会写策略或使用工具；很多安全问题直接发生在 ISA、操作系统、内存层次、Cache、异常、中断、侧信道和硬件执行机制里。比如后面第 1 章提到的 side-channel attacks、第 2 章的分支预测和推测执行，都可能成为安全分析对象。

### 1.3 冯诺依曼结构 Von Neumann Structure（p34-p35）

PPT 定义：

- 数据和程序都在内存中。
- CPU 从内存取指令和数据进行运算，并把结果放回内存。

基本结构：

```text
Input -> Memory <-> CPU -> Output
          ^
          |
       Storage
```

CPU 内部有：

- Controller / 控制器：决定下一步执行什么，控制数据流向。
- Computer / 运算器：真正做加减乘除、逻辑运算等。

图中还区分：

- Data path / 数据通路：数据实际流动的路线。
- Control path / 控制通路：控制信号流动的路线。

零基础理解：

把 CPU 想成厨房：

- 内存是冰箱和货架，放食材和菜谱。
- 指令是菜谱步骤。
- 数据是食材。
- 控制器像厨师长，决定下一步做哪一步。
- 运算器像刀、锅、炉子，负责真正加工。
- 输入设备提供原料或命令，输出设备展示结果。
- 外存储器像仓库，容量大但取用慢。

### 1.4 计算机革命与学习方法（p36-p37）

PPT 说计算机技术进步：

- 由 Moore's Law 支撑。
- 使许多新应用成为可能：
  - 汽车中的计算机
  - 手机
  - 人类基因组计划
  - World Wide Web
  - 搜索引擎
  - 大语言模型
- 计算机无处不在。

学习方法：

- standing on the shoulder of giants
- Concepts, Ideas and Principles
- Quantitative approaches
- Hit the problem and right way to solve problem
- As a man sows, so he shall reap.

这里最重要的是“定量方法”。系统课不是只问“这个设计看起来是不是高级”，而是问：

- 快多少？
- 成本多大？
- 功耗多大？
- 面积多大？
- 复杂度多大？
- 哪部分成为瓶颈？

### 1.5 计算机体系结构重要人物（p38-p47）

PPT 列了许多人物，不要求你背传记，但要知道他们对应的知识点。

| 人物 | PPT 中强调的贡献 | 和本课关系 |
|---|---|---|
| John L. Hennessy | MIPS 创始人之一，Stanford 前校长，被称为 Silicon Valley godfather | 和 Patterson 一起推动 RISC 和定量体系结构设计 |
| David A. Patterson | UC Berkeley 教授，RISC-V Foundation 董事会相关职位 | RISC、定量设计、计算机体系结构教材核心人物 |
| Hennessy & Patterson | 图灵奖：系统化、定量化设计与评价计算机体系结构 | 第 1 章的定量方法、第 2 章 ILP 都沿用他们的体系 |
| Frederick P. Brooks | 计算机体系结构、操作系统、软件工程贡献，IBM 360 ISA | ISA、计算机家族、指令系统设计 |
| Robert Tomasulo | Tomasulo 算法发明者 | 第 2 章动态调度、乱序执行核心 |
| Seymour Cray | 超级计算机设计 | 高性能计算、并行设计 |
| Gene Amdahl | 流水线、指令前看、Cache 等创新；Amdahl's Law | 第 1 章 Amdahl 定律、第 2 章流水线 |
| Mateo Valero | 指令级并行和超标量处理器 | 第 2 章 ILP、Superscalar |
| Yale Patt | 指令级并行和超标量处理器 | 第 2 章 ILP |
| Michael J. Flynn | 处理器组织和分类、计算机算术、性能评价 | Flynn 分类 SISD/SIMD/MISD/MIMD |

### 1.6 Flynn 分类与计算机类别（p48-p50）

Flynn 分类按指令流和数据流分类：

- IS: Instruction stream，指令流
- DS: Data stream，数据流
- CS: Control stream，控制流
- CU: Control unit，控制单元
- PU: Process unit，处理单元
- MM / SM: Memory，存储器

四类：

1. SISD: Single Instruction Single Data
   - 单指令流、单数据流
   - 传统单处理器顺序机可以这么理解。

2. SIMD: Single Instruction Multiple Data
   - 单指令流、多数据流
   - 同一条指令同时作用于多份数据。
   - 典型例子：向量处理、GPU 中大量相同操作。
   - 比如对数组每个元素都加 1。

3. MISD: Multiple Instruction Single Data
   - 多指令流、单数据流
   - 实际通用系统中较少见，多用于特定容错或流水式处理概念。

4. MIMD: Multiple Instruction Multiple Data
   - 多指令流、多数据流
   - 多核、多处理器、集群常见。

PPT 还按用途分类：

- Desktop / Personal Computers
  - 通用用途
  - 软件种类多
  - 低成本下强调单用户性能
  - 多运行第三方软件

- Server computers
  - 强调少数复杂应用的高性能
  - 或许多用户同时使用时的可靠性能
  - 比 PC 有更强计算、存储、网络能力

- Embedded computers
  - 数量最大、种类最多
  - 隐藏在系统组件中
  - 对功耗、性能、成本约束严格

- Personal Mobile Devices
  - 智能手机、平板、iPad
  - 设计要求和 PC 类似，但更重视能耗、体积、交互

- Supercomputer
  - 计算机集群
  - 高容量、高性能、高可靠性
  - 规模可到建筑级

### 1.7 本课程会学什么（p51）

PPT 列出：

- 程序如何翻译成机器语言。
- 硬件如何执行机器语言。
- 硬件/软件接口。
- 什么决定程序性能。
- 性能如何改进。
- 硬件设计者如何提升性能。
- 什么是并行处理。

这恰好对应后续：

- 编译器/汇编/ISA
- 数据通路/控制器/流水线
- Cache/内存/虚拟内存
- ILP/DLP/TLP
- 分支预测、乱序执行、多发射

### 1.8 性能 performance：先问“哪种性能”（p52-p56）

PPT 用飞机举例：哪架飞机性能最好？

可能指标包括：

- Passenger Capacity：载客量
- Cruising Range：航程
- Cruising Speed：巡航速度
- Passengers x mph：吞吐式指标，载客量乘速度

同样，计算机性能也不能只说“好”或“快”，必须说明指标。

#### 影响性能的因素

PPT 列出：

- Algorithm：决定执行多少操作。
- Programming language, compiler, architecture：决定每个操作需要多少机器指令。
- Processor and memory system：决定指令执行多快。
- I/O system including OS：决定 I/O 操作多快。

也就是说，程序慢可能有很多原因：

- 算法太差，操作数量太多。
- 编译器生成的指令多。
- ISA 表达能力或指令编码影响指令数量。
- CPU 执行慢。
- Cache miss 太多。
- 磁盘、网络、系统调用慢。

#### Response time 和 Throughput

单用户 PC 常关注：

- Response time / Latency / Elapsed time
  - 从事件开始到完成的时间。
  - 做完一个任务要多久。
  - 越小越好。

大数据、服务器常关注：

- Throughput
  - 单位时间完成的总工作量。
  - 例如每小时任务数、每秒事务数。
  - 越大越好。

区别例子：

- 你打开一个网页，关心响应时间：多久显示出来？
- 搜索引擎后台每秒处理多少查询，关心吞吐量。

#### Response time / Elapsed time 和 CPU time

PPT 区分：

- Response time / Elapsed time
  - 总响应时间。
  - 包括处理、I/O、OS 开销、等待、空闲等。
  - 决定用户感受到的系统性能。

- Execution time / CPU time
  - CPU 真正在处理某个任务上花的时间。
  - 不包括 I/O 时间，不包括其他作业抢占走的时间。
  - 包括：
    - User CPU time：程序自身代码消耗的 CPU 时间。
    - System CPU time：OS 代表程序执行任务消耗的 CPU 时间。

不同程序对 CPU 和系统性能的敏感程度不同。比如：

- 纯计算程序主要看 CPU time。
- 下载文件可能大量时间在网络 I/O。
- 数据库可能受 CPU、内存、磁盘、锁竞争共同影响。

#### 性能定义

PPT 定义：

```text
Performance = 1 / Execution Time
```

如果说 “X is n times faster than Y”，则：

```text
Performance_X / Performance_Y
= ExecutionTime_Y / ExecutionTime_X
= n
```

例子：

- 程序在 A 上运行 10s。
- 在 B 上运行 15s。
- ExecutionTime_B / ExecutionTime_A = 15 / 10 = 1.5。
- 所以 A 比 B 快 1.5 倍。

注意：不是快 5 秒就叫快 1.5 倍。倍数一定是比值。

### 1.9 数据大小单位（p59）

PPT 的数据单位：

- bit：binary digit，二进制位。
- nibble：4 bits。
- byte：8 bits。
- word：4 bytes，即 32 bits，在许多嵌入式/移动处理器中常见；有些服务器是 8 bytes，即 64 bits。
- KiB / kibibyte = 2^10 = 1,024 bytes。
- MiB / mebibyte = 2^20 = 1,048,576 bytes。
- GiB / gibibyte = 2^30 = 1,073,741,824 bytes。
- TiB / tebibyte = 2^40 = 1,099,511,627,776 bytes。
- PiB / pebibyte = 2^50 = 1,125,899,906,842,624 bytes。

要注意 KB 和 KiB 的区别：

- KB 在很多商业场景可能按 1000。
- KiB 明确按 1024。

系统课里常用 2 的幂，因为地址、Cache、页大小都天然和二进制相关。

### 1.10 CPU 时钟与 CPU 时间公式（p60-p63）

数字硬件由固定速率时钟控制。

两个概念：

- Clock period / clock cycle time：一个时钟周期多长。
  - 例如 250ps = 0.25ns = 250 x 10^-12 s。
- Clock frequency / clock rate：每秒多少个周期。
  - 例如 4.0GHz = 4000MHz = 4.0 x 10^9 Hz。

二者互为倒数：

```text
Clock Rate = 1 / Clock Cycle Time
Clock Cycle Time = 1 / Clock Rate
```

CPU 时间公式：

```text
CPU Time = CPU Clock Cycles x Clock Cycle Time
         = CPU Clock Cycles / Clock Rate
```

提升性能有两条路：

- 减少 clock cycles。
- 提高 clock rate。

但硬件设计者经常需要权衡：提高频率可能使每条指令需要更多周期，或者流水线更复杂、功耗更高。

#### 例题：Computer B 需要多高频率？

条件：

- Computer A: 2GHz clock, 10s CPU time。
- 设计 Computer B，目标 CPU time = 6s。
- 更快时钟会导致 clock cycles 变为 A 的 1.2 倍。

计算：

```text
ClockCycles_A = CPUTime_A x ClockRate_A
              = 10s x 2GHz
              = 20 x 10^9 cycles

ClockCycles_B = 1.2 x ClockCycles_A
              = 24 x 10^9 cycles

ClockRate_B = ClockCycles_B / CPUTime_B
            = 24 x 10^9 / 6s
            = 4GHz
```

所以 B 必须达到 4GHz。

零基础理解：B 每秒要跑更多周期，因为它总周期数还增加了。如果只把频率从 2GHz 提到 3GHz，不够。

### 1.11 Instruction Count、CPI 与完整 CPU 性能公式（p64-p69）

PPT 定义：

- Instruction Count / IC：一个程序执行的机器指令数量。
  - 由程序、ISA、编译器共同决定。
- CPI: Cycles Per Instruction，平均每条指令需要多少周期。
  - 由 CPU 硬件决定。
  - 如果不同指令 CPI 不同，平均 CPI 受 instruction mix 影响。

完整公式：

```text
CPU Time = Instruction Count x CPI x Clock Cycle Time
         = Instruction Count x CPI / Clock Rate
```

PPT 的 big picture：

```text
CPU Time = Instructions / Program
         x Clock cycles / Instruction
         x Seconds / Clock cycle
```

每个因素由谁影响：

- Algorithm：影响 IC，可能影响 CPI。
- Programming language：影响 IC、CPI。
- Compiler：影响 IC、CPI。
- ISA：影响 IC、CPI、clock cycle time。

#### 例题：CPI 和 cycle time 的权衡

条件：

- Computer A: Cycle Time = 250ps, CPI = 2.0。
- Computer B: Cycle Time = 500ps, CPI = 1.2。
- Same ISA，所以假设 Instruction Count 相同，记为 I。

计算：

```text
CPUTime_A = I x 2.0 x 250ps = I x 500ps
CPUTime_B = I x 1.2 x 500ps = I x 600ps

CPUTime_B / CPUTime_A = 600 / 500 = 1.2
```

B 时间更长，所以 A 更快。A 比 B 快 1.2 倍。

关键理解：CPI 小不一定更快，周期时间也重要。B 每条指令周期数少，但每个周期太长。

#### 加权平均 CPI

如果有 n 类指令：

```text
Clock Cycles = sum(CPI_i x InstructionCount_i)

CPI = ClockCycles / InstructionCount
    = sum(CPI_i x InstructionCount_i / InstructionCount)
```

也就是按每类指令出现比例加权平均。

#### 例题：两段编译代码哪个更好？

指令类别：

| Class | A | B | C |
|---|---:|---:|---:|
| CPI for class | 1 | 2 | 3 |
| IC in sequence 1 | 2 | 1 | 2 |
| IC in sequence 2 | 4 | 1 | 1 |

Sequence 1：

```text
IC = 2 + 1 + 2 = 5
ClockCycles = 2x1 + 1x2 + 2x3 = 10
Avg CPI = 10 / 5 = 2.0
```

Sequence 2：

```text
IC = 4 + 1 + 1 = 6
ClockCycles = 4x1 + 1x2 + 1x3 = 9
Avg CPI = 9 / 6 = 1.5
```

Sequence 2 指令数更多，但总周期更少，所以更快。

易错点：不能只看 instruction count。也不能只看 CPI。要看 `IC x CPI x clock cycle time`。

### 1.12 多处理器与并行编程（p70）

PPT 提到 multicore microprocessors：

- 一个芯片上有多个 processor / core。
- 需要显式并行编程。

和 ILP 对比：

- Instruction-level parallelism：硬件同时执行多条指令，通常对程序员隐藏。
- 多核并行：程序员或运行时需要把任务分给多个核心。

困难：

- Programming for performance：写出真正快的并行程序。
- Load balancing：负载均衡，不能一个核心很忙其他核心闲着。
- Optimizing communication and synchronization：通信和同步成本不能太高。

### 1.13 Amdahl's Law（p71-p80）

Amdahl 定律回答：只优化一部分系统，整体最多能快多少？

PPT 公式：

```text
ImprovedTime = AffectedTime / ImprovementFactor + UnaffectedTime
```

整体加速比：

```text
Speedup = Performance_with_enhancement / Performance_without_enhancement
        = TotalExecutionTime_without / TotalExecutionTime_with
```

定义：

- Fraction_enhanced：可被增强部分占原总执行时间的比例，<= 1。
- Speedup_enhanced：增强部分自身的加速比，> 1。

常用形式：

```text
Speedup_overall =
1 / ((1 - Fraction_enhanced) + Fraction_enhanced / Speedup_enhanced)
```

最重要的直觉：

> 系统整体加速受“未优化部分”限制。你把一部分做得无限快，整体也不可能超过 `1 / (1 - Fraction_enhanced)`。

PPT 的例子：multiply 占 80s/100s，想整体 5x。

整体原时间 100s，5x 后目标时间 20s。未受影响部分已经 20s：

```text
20 = 80 / n + 20
```

这要求 `80/n = 0`，也就是 n 无限大才行，现实中做不到。结论：Can’t be done。

#### 例题 1.1

题目：

- 某功能加速到原来的 20 倍。
- 该功能原来占总运行时间 40%。
- 整体性能提升多少？

计算：

```text
Fraction = 0.4
Speedup_enhanced = 20

Speedup_overall =
1 / ((1 - 0.4) + 0.4 / 20)
= 1 / (0.6 + 0.02)
= 1 / 0.62
= 1.6129
```

整体约快 1.61 倍。

注意：局部快 20 倍，整体只快 1.61 倍，因为 60% 完全没变。

#### 例题 1.2

题目：

- 浮点部件使浮点运算速度提高 20 倍。
- 某程序整体性能提高 5 倍。
- 求浮点操作在原程序中占比。

设比例为 F：

```text
5 = 1 / ((1 - F) + F / 20)

(1 - F) + F/20 = 1/5 = 0.2

1 - 0.95F = 0.2
0.95F = 0.8
F = 0.8 / 0.95 = 0.8421
```

所以 Fraction = 84.2%。

### 1.14 八个伟大架构思想（p81-p84）

PPT 说，过去半个多世纪，计算机设计中反复使用 8 个 great architectural ideas。后续每学一个技术，都要问它用了哪些思想。

1. Design for Moore's Law
   - 芯片上晶体管数量大约每 18-24 个月翻倍。
   - 架构师设计系统时必须预判系统完成时的技术水平。

2. Use abstraction to simplify design
   - 用不同层次的表示来描述设计。
   - 低层细节可以隐藏起来，高层得到更简单的模型。
   - 例如程序员看到文件，不必每次都考虑磁盘扇区和电信号。

3. Make the common case fast
   - 找出最常见情况并优先优化。
   - 这是性价比最高的改进方法。
   - 例如 Cache 优化常见内存访问，而不是让所有访问都一样慢。

4. Improve performance via parallelism
   - 通过并行执行操作提高性能。
   - 并行有很多层次：指令级、进程级等。

5. Improve performance via pipelining
   - 把任务拆成阶段，让多个任务同时处在不同阶段。
   - 常用于提高指令吞吐率。
   - 第 2 章大量内容都围绕流水线。

6. Improve performance via prediction
   - 有时先猜一个结果比等待结果出来更快。
   - 也叫 speculation。
   - 常用于猜分支结果。

7. Use a hierarchy of memories
   - 第一层使用最快、最小、每 bit 最贵的存储。
   - 最后一层使用最慢、最大、每 bit 最便宜的存储。
   - 目标是多数访问命中前几层，同时最后一层能保留大部分信息。

8. Improve dependability via redundancy
   - 加入冗余组件以检测甚至纠正错误。
   - 可用于许多层次。

### 1.15 为什么学体系结构（p85-p86）

PPT 强调：提升程序性能不只是减少内存占用。现代程序员需要理解程序下面发生的事：

- 处理器的并行本质
  - 怎样通过线程或多进程引入并行？
  - 编译器怎样翻译和重排你的指令级代码，使指令并行执行？

- 内存的层次本质
  - 怎样重排内存访问模式以更高效读取数据？
  - page/cache coloring、false sharing、side-channel attacks 都和内存层次相关。

- 高级语言到硬件指令的翻译
  - 编译器生成指令级语句时做了哪些决定？

结论：

- 成本/性能持续改善，来自底层技术发展。
- 硬件和软件都有层次化抽象。
- ISA 是硬件/软件接口。
- Execution time 是最好的性能度量。
- 8 个架构思想贯穿后续课程。

## 2. Chapter 2-1: Instruction-Level Parallelism and Dynamic Scheduling

### 2.1 ILP 是什么（p1-p2）

ILP = Instruction-Level Parallelism，指令级并行。

直观含义：

> 程序看起来是一条条指令，但 CPU 尝试在不改变程序语义的前提下，让多条指令重叠执行，甚至乱序执行。

最简单的 ILP 是流水线：一条指令在 EX 阶段时，下一条可以在 ID，再下一条可以在 IF。

更高级的 ILP 是：

- forwarding
- branch prediction
- dynamic scheduling
- scoreboard
- Tomasulo
- register renaming
- out-of-order execution
- multiple issue
- speculation

### 2.2 依赖 dependences 和冒险 hazards 的区别（p3-p7, p50）

这是初学者最容易混的地方。

PPT 明确说：

- Dependences are a property of programs.
- Hazards are properties of the pipeline organization.

也就是说：

- 依赖是程序语义本身存在的关系。
- 冒险是某个硬件流水线在执行这些依赖时遇到的问题。

#### Data dependence

例子：

```asm
FLD     F0, 0(R1)
FADD.D  F4, F0, F2
```

第二条要用第一条产生的 `F0`，这是真数据依赖。

对应 hazard：RAW, Read After Write。

```text
先写，后读。
后面的指令必须读到前面写出的新值。
```

#### Name dependence

名字相关不是数据真的流动，而是寄存器名字复用导致的限制。

PPT 给了两类：

1. Anti-dependence / WAR

```asm
FDIV.D F2, F6, F4
FADD.D F6, F0, F12
FSUB.D F8, F6, F14
```

`FDIV.D` 读 `F6`，后面的 `FADD.D` 写 `F6`。如果 FADD 太早写，就会覆盖 FDIV 本来要读的旧值。这叫 WAR：Write After Read。

可通过改名解决：

```asm
FDIV.D F2, F6, F4
FADD.D S,  F0, F12
FSUB.D F8, S,  F14
```

把后面写的 `F6` 改成临时寄存器 `S`，就没有名字冲突。

2. Output-dependence / WAW

```asm
FDIV.D F2, F6, F4
FADD.D F6, F0, F12
FSUB.D F2, F6, F14
```

`FDIV.D` 和 `FSUB.D` 都写 `F2`。如果乱序执行，后写的可能先写回，造成最终结果错误。这叫 WAW：Write After Write。

可通过改名解决：

```asm
FDIV.D F2, F0, F4
FADD.D F6, F0, F12
FSUB.D S,  F6, F14
```

#### Control dependence

例子：

```c
if p1 {
    Statement 1
}
Statement
if p2 {
    Statement 2
}
```

分支决定哪些语句会执行。流水线提前取指时，不知道分支结果，就可能取错路径。

#### 三类 hazards

PPT 定义：

- Structure hazard：资源冲突。需要的硬件资源正忙。
- Data hazard：要等待前面指令完成读/写数据。
- Control hazard：下一步控制流取决于前面分支/跳转结果。

数据 hazard 又分：

- RAW: Read after write
- WAR: Write after read
- WAW: Write after write

在经典五级顺序流水线中，主要关心 RAW；但乱序执行会引入 WAR 和 WAW 的可能。

### 2.3 五级流水线复习：IF ID EX MEM WB（p8-p15, p49）

经典 RISC 五级流水线：

```text
IF  -> Instruction Fetch，取指
ID  -> Instruction Decode / Register Read，译码/读寄存器
EX  -> Execute / ALU，执行/地址计算
MEM -> Data Memory，访存
WB  -> Write Back，写回寄存器
```

#### Forwarding / Bypassing

问题：后面的指令需要前面指令的结果，但前面还没 WB。

解决：不用等写回寄存器，而是从流水线中间直接把结果转发给后续指令。

PPT 例子：

```asm
DADD R1, R2, R3
DSUB R4, R1, R5
XOR  R6, R1, R7
AND  R8, R1, R9
OR   R10, R1, R11
```

`DADD` 产生 `R1`，后面多条指令用 `R1`。Forwarding 允许后面指令从 ALU 结果路径直接拿到值。

#### Load-use hazard 和 bubble

Load 指令的数据到 MEM 阶段末尾才可用，紧跟的使用者在 EX 阶段就需要这个值，即使用 forwarding 也可能来不及。

例子：

```asm
LD   R1, 0(R2)
DADD R4, R1, R5
AND  R6, R1, R7
XOR  R8, R1, R9
```

`DADD` 紧跟在 `LD` 后使用 `R1`，需要插入 bubble / stall。

Bubble 就像流水线里塞一个空操作，让后面的指令等一拍。

#### Code scheduling 避免 stall

PPT 例子：

原顺序：

```asm
LD   Rb, B
LD   Rc, C
DADD Ra, Rb, Rc
SD   Ra, A
LD   Re, E
LD   Rf, F
DSUB Rd, Re, Rf
SD   Rd, D
```

调度后：

```asm
LD   Rb, B
LD   Rc, C
LD   Re, E
DADD Ra, Rb, Rc
LD   Rf, F
SD   Ra, A
DSUB Rd, Re, Rf
SD   Rd, D
```

核心思想：在 load 和使用 load 结果之间插入无关指令，填掉等待时间。

另一个 PPT 例子：

未调度 13 cycles：

```asm
lw   $t1, 0($t0)
lw   $t2, 4($t0)
stall
add  $t3, $t1, $t2
sw   $t3, 12($t0)
lw   $t4, 8($t0)
stall
add  $t5, $t1, $t4
sw   $t5, 16($t0)
```

调度后 11 cycles：

```asm
lw   $t1, 0($t0)
lw   $t2, 4($t0)
lw   $t4, 8($t0)
add  $t3, $t1, $t2
sw   $t3, 12($t0)
add  $t5, $t1, $t4
sw   $t5, 16($t0)
```

### 2.4 控制冒险与分支预测（p16-p24）

分支改变控制流：

- 下一条应该取顺序地址？
- 还是跳到目标地址？

流水线不能总等分支完全确定，因为长流水线中等待代价很大。

RISC-V 流水线中，PPT 说需要尽早比较寄存器并计算目标地址，添加硬件让它在 ID 阶段完成。

相关指令：

- Unconditional Jump
- Conditional Branch
- `Jal`: Jump and Link
- `Jalr`: Jump and Link-Register

#### Stall on branch

如果等待分支结果再取下一条，会插入 stall。分支 taken 和 not taken 都可能让流水线浪费周期。

#### Predict not taken

策略：先假设分支不跳，继续取下一条顺序指令。

如果预测正确：

- 不需要额外延迟。

如果预测错误：

- 已取的错误路径指令要 flush。
- 重新从 branch target 取指。

PPT 的 RISC-V 示例：

```asm
add x4, x5, x6
beq x1, x2, 40
lw  x3, 300(x0)
...
or  x7, x8, x9
```

如果 `beq` 不跳，预测 not taken 正确，继续执行 `lw`。

如果 `beq` 实际跳转，`lw` 等顺序路径指令是错的，要清掉。

### 2.5 减少分支延迟：taken/not taken/delay slot（p22-p32）

PPT 列了三种：

- Predict branch taken
- Predict branch not taken
- Delayed Branch

#### PC-relative branch 例子

```asm
36: sub x10, x4, x8
40: beq x1, x3, 16    // PC-relative branch
                      // to 40 + 16*2 = 72
44: and x12, x2, x5
48: or  x13, x2, x6
52: add x14, x4, x2
56: sub x15, x6, x7
...
72: ld  x4, 50(x7)
```

RISC-V 条件分支立即数按 2 字节对齐编码，因此这里目标地址是 `40 + 16*2 = 72`。

#### Branch 数据 hazard

如果分支比较寄存器依赖前面指令：

- 比较寄存器是前面第 2 或第 3 条 ALU 指令的目的寄存器：可 forwarding。
- 比较寄存器是前 1 条 ALU 指令目的寄存器，或前第 2 条 load 指令目的寄存器：需要 1 个 stall cycle。
- 比较寄存器是紧前一条 load 指令目的寄存器：需要 2 个 stall cycles。

#### Delay slot

Delay slot 是分支后一条指令无论分支是否跳转都会执行的位置。

思想：既然分支结果还没出来，就让编译器把一条“总能安全执行”的指令放在分支后，填掉延迟。

PPT 问：Is delay slot a really good design?

RISC-V 手册说：

- RISC-V base integer ISA 类似早期 RISC，但没有 branch delay slots。
- 支持 optional variable-length instruction encodings。

为什么现代 ISA 不喜欢 delay slot？

- 它把微结构细节暴露给 ISA。
- 以后流水线变深、变乱序后，一个固定 delay slot 不再合适。
- 编译器更难保证总能找到安全指令。

### 2.6 动态分支预测、BHT、2-bit predictor、BTB（p33-p47）

深流水和超标量中，分支代价更大，因此使用动态预测。

#### BHT / Branch History Table

也叫 branch prediction buffer。

- 用近期分支指令地址索引。
- 存 taken / not taken 历史。
- 执行分支时：
  - 查表。
  - 假设未来行为和过去一致。
  - 从 fall-through 或 target 开始取指。
  - 若错误，flush pipeline，并更新历史。

#### 1-bit predictor 缺点

1-bit 只记录上次 taken/not taken。

内层循环会误判两次：

```asm
outer:
    ...
inner:
    ...
    beq ..., ..., inner
    ...
    beq ..., ..., outer
```

内层循环最后一次退出时：

- 前面多次都是 taken。
- 最后一次 not taken，会误判为 taken。

下次进入内层循环第一次：

- 上次记录变成 not taken。
- 但这次通常 taken，又误判。

所以两次。

#### 2-bit predictor

2-bit predictor 用四个状态：

- Strongly taken
- Weakly taken
- Weakly not taken
- Strongly not taken

只有连续两次反方向结果，才改变强预测方向。

好处：内层循环通常只在最后退出时误判一次，下次进入仍保持 taken 倾向。

#### Buffer 在体系结构中很重要

PPT 强调：Buffer plays an important role in Computer Architecture.

例子：

- instruction buffer
- branch history table
- branch target buffer
- load/store buffer
- reorder buffer

Buffer 的共同点：

- FIFO 或类似队列。
- 由多个快速访问存储单元和控制逻辑组成。
- 用于解耦生产者和消费者，减少等待。

#### 指令获取的高级技术

PPT 列出：

- Increasing Instruction Fetch Bandwidth
- Branch-Target Buffers
- Specialized Branch Predictors
  - procedure returns
  - indirect jumps
  - loop branches
- Integrated Instruction Fetch Units

Integrated instruction fetch unit 集成：

- branch prediction
- instruction prefetch
- instruction memory access and buffering

在多发射复杂流水线中，不能再把取指简单看成一个 pipe stage。

#### BTB / Branch Target Buffer

即使预测了 taken，也还要计算目标地址。没有目标地址就不能马上取目标指令。

BTB 是 target address 的 cache：

- 按 PC 索引。
- 如果命中且预测 taken，可立即从目标地址取指。

PPT 表格：

| BTB 中有该指令？ | Predict | Reality | Delay cycle |
|---|---|---|---:|
| Yes | Taken | Taken | 0 |
| Yes | Taken | Not taken | 2 |
| No | Not taken | Taken | 2 |
| No | Not taken | Not taken | 0 |

BTB 好处：

- 更快获得分支目标指令。
- 可一次提供目标处多条指令，对多发射处理器必要。
- branch folding：无条件分支可无延迟，有时条件分支也可无延迟。

### 2.7 动态调度的动机（p52-p56）

简单流水线的重大限制：

- in-order instruction issue
- in-order execution

PPT 例子：

```asm
FDIV.D F4,  F0, F2
FSUB.D F10, F4, F6
FADD.D F12, F6, F14
```

`FSUB.D` 依赖 `FDIV.D` 的结果 `F4`，所以要等。

但 `FADD.D` 不依赖前面任何正在等待的结果，理论上可以先执行。顺序流水线不允许它越过被卡住的 `FSUB.D`，所以浪费。

动态调度思想：

- 让硬件在运行时判断哪些指令准备好了。
- 准备好的先执行，即 out-of-order execution。

PPT 也提醒：乱序执行会引入顺序五级整数流水线中不存在的 WAR 和 WAW 可能。

例子：

```asm
FDIV.D F10, F0, F2
FSUB.D F10, F4, F6   # WAW: 都写 F10
FADD.D F6,  F8, F14  # WAR: 可能和前面对 F6 的读写相关
```

两条路线：

- Scoreboard algorithm：通过记分牌调度指令。
- Tomasulo's Approach：硬件寄存器重命名，减少 WAW/WAR。

### 2.8 Scoreboard 记分牌算法（p55-p68）

为了允许乱序执行，PPT 把 ID 阶段拆成两段：

- Issue (IS)
  - Decode instructions。
  - Check structural hazards。
  - in-order issue。

- Read Operands (RO)
  - 等到没有 data hazards。
  - 读操作数。
  - out-of-order execution 从这里开始体现。

流水线变成：

```text
IS -> RO -> EX -> WB
```

#### 记分牌表格

记分牌记录三类信息：

1. Instruction Status
   - 每条指令处于 IS / RO / EX / WB 哪些阶段。

2. Function Component Status
   - 每个功能部件是否 Busy。
   - Op：操作类型。
   - Fi：目的寄存器。
   - Fj、Fk：源寄存器。
   - Qj、Qk：哪个功能部件将产生源操作数。
   - Rj、Rk：源操作数状态。

3. Register Status
   - Qi：哪个功能部件将写某个寄存器。

PPT 对 Rj/Rk 的解释：

- `yes`：operand is ready but not read，操作数已经准备好但尚未读。
- `no` 且 `Qj = null`：operand is read，已经读走。
- `no` 且 `Qj != null`：operand is not ready，操作数还没准备好，等待 Qj 指定的部件。

#### 记分牌例题指令序列

```asm
FLD    F6,  34(R2)
FLD    F2,  45(R3)
FMUL.D F0,  F2, F4
FSUB.D F8,  F6, F2
FDIV.D F10, F0, F6
FADD.D F6,  F8, F2
```

阶段耗时：

- Add instruction: 2 cycles
- Multiply instruction: 10 cycles
- Division instruction: 40 cycles
- LD instruction: 1 cycle

PPT 给出的 Scoreboard 时间表：

| inst | Fi | Fj | Fk | IS | RO | EX | WB |
|---|---|---|---|---:|---:|---|---:|
| L.D | F6 | 34+R2 | | 1 | 2 | 3 | 4 |
| L.D | F2 | 45+R3 | | 5 | 6 | 7 | 8 |
| MUL.D | F0 | F2 | F4 | 6 | 9 | 10-19 | 20 |
| SUB.D | F8 | F2 | F6 | 7 | 9 | 10-11 | 12 |
| DIV.D | F10 | F0 | F6 | 8 | 21 | 22-61 | 62 |
| ADD.D | F6 | F8 | F2 | 13 | 14 | 15-16 | 22 |

为什么有些看起来奇怪？

- 第二个 load 到 IS=5，是因为记分牌对结构资源和写寄存器冲突很保守。
- `MUL.D` 要等 `F2` 的 load 在 cycle 8 写回后，cycle 9 才能 RO。
- `DIV.D` 依赖 `F0`，必须等 `MUL.D` 写回 cycle 20 后，cycle 21 才能 RO。
- `ADD.D` 虽然 EX 在 15-16 完成，但 WB 到 22，说明它受写回冲突/WAW/WAR 约束影响，不能随便早写 `F6`。

记分牌的特点：

- 能乱序执行。
- 但没有真正消除名字相关。
- 因此 WAR/WAW 仍会限制写回。

### 2.9 Tomasulo 算法的动机：寄存器重命名（p69-p72）

PPT 例子：

```asm
FDIV.D F0, F2,  F4
FADD.D F6, F0,  F8
FSD    F6, 0(R1)
FSUB.D F8, F10, F14
FMUL.D F6, F10, F8
```

存在：

- WAR anti-dependence，例如 `F8`。
- WAW output-dependence，例如 `F6`。

PPT 说：这些 name dependences 都可通过 register renaming 消除。

假设有临时寄存器 S 和 T，可改写为：

```asm
FDIV.D F0, F2,  F4
FADD.D S,  F0,  F8
FSD    S,  0(R1)    # F6 改名为 S
FSUB.D T,  F10, F14 # F8 改名为 T
FMUL.D F6, F10, T
```

问题是：谁完成改名？怎样完成？

Tomasulo 的答案：硬件用 reservation station 和 register status 来完成动态寄存器重命名。

### 2.10 Tomasulo 结构（p71-p81）

PPT 的浮点 Tomasulo 结构包括：

- Instruction queue
- FP registers
- Register status Qi
- Load buffers
- Store buffers
- Address unit
- FP adder
- FP multiplier
- Reservation stations
- Operand buses
- Operation bus
- Common Data Bus (CDB)
- Memory unit

主思想：

1. 跟踪每条指令的操作数何时可用，以减少 RAW hazard。
2. 在硬件中引入寄存器重命名，以减少 WAW 和 WAR hazard。

#### 三个步骤

1. Issue
   - 从 instruction queue 头部取下一条指令，FIFO。
   - 如果有匹配的空 reservation station，就 issue。
   - 如果源操作数现在在寄存器中，就把值带入 station。
   - 如果没有空 station/buffer，则结构冒险，stall。
   - 如果操作数不在寄存器中，就记录将产生该操作数的功能部件。
   - 这一步完成寄存器重命名，消除寄存器层面的 WAR/WAW。

2. Execute
   - 当所有操作数可用，在对应功能单元执行。
   - Load/store 两步：
     - base register 可用后计算 effective address。
     - 把 effective address 放入 load/store buffer。

3. Write results
   - 结果可用后写到 CDB。
   - CDB 广播到寄存器和所有等待的 reservation stations，包括 store buffers。
   - Store 在 store buffer 中等待，直到存储值和地址都可用，且 memory unit 空闲，再写内存。

#### 三张表

1. Instruction status table
   - 只帮助理解算法，不一定是真实硬件的一部分。
   - 记录 Issue / Execute / Write Result。

2. Reservation stations table
   - 记录已经 issue 的每个操作的状态。

3. Register status table
   - 字段 Qi。
   - 记录哪个 reservation station 的结果应该写入某个寄存器。

Reservation station 字段：

- Op：要对源操作数执行的操作。
- Qj, Qk：将产生对应源操作数的 reservation station。
- Vj, Vk：源操作数的值。
- Busy：station 和配套功能单元是否被占用。
- A：用于 load/store 的地址计算信息。

理解 V 和 Q：

- 有 V，说明值已经到了。
- 有 Q，说明值还没到，但知道该等谁。

### 2.11 Tomasulo 例题（p82-p91）

同样的指令序列：

```asm
FLD    F6,  34(R2)
FLD    F2,  45(R3)
FMUL.D F0,  F2, F4
FSUB.D F8,  F6, F2
FDIV.D F10, F0, F6
FADD.D F6,  F8, F2
```

Tomasulo 时间表：

| inst | Fi | Fj | Fk | IS | EX | WB |
|---|---|---|---|---:|---|---:|
| L.D | F6 | 34+R2 | | 1 | 3 | 4 |
| L.D | F2 | 45+R3 | | 2 | 4 | 5 |
| MUL.D | F0 | F2 | F4 | 3 | 6-15 | 16 |
| SUB.D | F8 | F2 | F6 | 4 | 6-7 | 8 |
| DIV.D | F10 | F0 | F6 | 5 | 17-56 | 57 |
| ADD.D | F6 | F8 | F2 | 6 | 9-10 | 11 |

和 Scoreboard 对比：

| 指令 | Scoreboard WB | Tomasulo WB | 为什么 Tomasulo 更早 |
|---|---:|---:|---|
| L.D F6 | 4 | 4 | 类似 |
| L.D F2 | 8 | 5 | Tomasulo load buffer/renaming 更灵活 |
| MUL.D F0 | 20 | 16 | 更早拿到 F2 并执行 |
| SUB.D F8 | 12 | 8 | 依赖值到达后即可执行并广播 |
| DIV.D F10 | 62 | 57 | 依赖 MUL，MUL 更早完成 |
| ADD.D F6 | 22 | 11 | 寄存器重命名消除 WAW/WAR 限制，不必等很晚写 F6 |

核心理解：

- Tomasulo 不是真的创造了不存在的数据并行。
- 它只是减少了不必要的等待，尤其是名字相关和集中控制造成的等待。

### 2.12 Tomasulo 总结与限制（p87-p89）

主要贡献：

- Dynamic scheduling
- Register renaming，消除 WAW 和 WAR hazards
- Load/store disambiguation
- Better than Scoreboard Algorithm

缺点：

- 结构复杂。
- 性能受 Common Data Bus 限制。
- load/store 乱序必须谨慎：
  - 如果 load 和 store 访问不同地址，可安全乱序。
  - 如果访问相同地址：
    - load 在 store 前，交换会产生 WAR。
    - store 在 load 前，交换会产生 RAW。
    - 两个 store 同地址交换会产生 WAW。

PPT 问：

> Does out-of-order execution mean out-of-order completion?

答案：不一定。

- Tomasulo 原始形式可能乱序写回。
- 加 ROB 后可以乱序执行/写回，但按序提交。
- “完成”这个词要看是 execute 完成、writeback 完成，还是 commit 完成。

## 3. Chapter 2-2: Hardware-Based Speculation, Multiple Issue, VLIW, Superpipeline

### 3.1 从 Tomasulo 到硬件推测（p1-p6）

Tomasulo 已经能动态调度和乱序执行，但还缺一个现代处理器特别重要的能力：

> 在分支结果还没确定之前，先按预测路径执行；如果错了，能撤销。

这叫 Hardware-Based Speculation。

PPT 给出的未提交结果缓存：

- 3 fields:
  - instruction type
  - destination address
  - value

这个结构就是 ROB / Reorder Buffer。

#### 为什么需要 ROB

如果一条预测路径上的指令直接改寄存器或内存，后来发现分支预测错了，状态就被污染了。

ROB 的做法：

- 指令执行完先把结果放 ROB。
- 先不真正更新体系结构寄存器/内存。
- 等确认这条指令可以提交，再 commit。
- 如果预测错或异常，丢弃 ROB 中错误路径结果，恢复状态。

PPT 中硬件推测四阶段：

1. Issue: 从 FP Op Queue 取指令。
2. Execution: 对操作数执行 EX。
3. Write result: 完成执行，WB。
4. Commit: 用 reorder result 更新寄存器。

硬件推测结合三件事：

- dynamic branch prediction：选择执行哪条路径。
- speculation：控制相关尚未解决时先执行，并能撤销错误推测。
- dynamic scheduling：调度来自不同 basic blocks 的指令组合。

#### ROB 的关键规则

PPT 强调：

- ROB 在指令执行完成和指令 commit 之间保存结果。
- ROB 像 reservation station 一样，也可作为操作数来源。
- 推测实现的关键：允许 out-of-order execute，但强制 in-order commit。
- 在 commit 前，禁止不可撤销动作，例如真正更新状态或处理异常。
- ROB 像 Tomasulo reservation stations 一样扩展了寄存器集合。

一句话：

> 乱序执行提高性能，按序提交保证精确状态。

### 3.2 ROB 表格例子：FMUL.D ready to commit（p7-p9）

指令序列：

```asm
FLD    F6,  34(R2)
FLD    F2,  45(R3)
FMUL.D F0,  F2, F4
FSUB.D F8,  F6, F2
FDIV.D F10, F0, F6
FADD.D F6,  F8, F2
```

当 `FMUL.D` ready to commit 时，ROB 状态大意：

| No. | Instruction | Status | Object | Value |
|---:|---|---|---|---|
| 1 | FLD F6, 34(R2) | Commit | F6 | Mem[34+Regs[R2]] |
| 2 | FLD F2, 45(R3) | Commit | F2 | Mem[45+Regs[R3]] |
| 3 | FMUL.D F0, F2, F4 | WB | F0 | #2 x Regs[F4] |
| 4 | FSUB.D F8, F6, F2 | WB | F8 | #1 - #2 |
| 5 | FDIV.D F10, F0, F6 | EX | F10 | |
| 6 | FADD.D F6, F8, F2 | WB | F6 | #4 + #2 |

Register Status：

- F0 -> ROB #3
- F6 -> ROB #6
- F8 -> ROB #4
- F10 -> ROB #5
- F2/F4 等已经不忙

理解：

- `FADD.D` 写 F6 的新结果在 ROB #6。
- 但早先 `FLD F6` 的结果已经 commit 到体系结构 F6。
- ROB 让多个“未来版本”的 F6 同时存在，直到按序提交。

### 3.3 Hardware-Based Speculation 完整时间线（p10-p35）

PPT 给出同类例题：

- Add: 2 cycles
- Multiply: 10 cycles
- Division: 40 cycles
- LD: 1 cycle

对照 PPT 时注意一个细节：p10、p11 的练习指令里 `FSUB.D` 的两个源寄存器出现了不一致写法，p35 的 summary 表使用的是 `FSUB.D F8, F6, F2`。下面的时间线按 p35 summary 表讲解，因为它是本组逐周期推演的收束页。

一组结果 summary：

| Instruction | Issue | Exec Comp / EX | Writeback | Commit |
|---|---:|---|---:|---:|
| FLD F6, 34(R2) | 1 | 3 | 4 | 5 |
| FLD F2, 45(R3) | 2 | 4 | 5 | 6 |
| FMUL.D F0, F2, F4 | 3 | 6-15 | 16 | 17 |
| FSUB.D F8, F6, F2 | 4 | 6-7 | 8 | 18 |
| FDIV.D F10, F0, F6 | 5 | 17-56 | 57 | 58 |
| FADD.D F6, F8, F2 | 6 | 9-10 | 11 | 59 |

这个表特别重要。

观察：

- `FSUB.D` 在 cycle 8 就 WB，但 commit 要等到 18。
- 为什么？因为它前面的 `FMUL.D` 到 17 才 commit，ROB 必须按程序顺序提交。

- `FADD.D` 在 cycle 11 就 WB，但 commit 要等到 59。
- 为什么？因为它前面有长延迟 `FDIV.D`，除法到 58 才 commit，`FADD.D` 只能下一周期 59 commit。

这说明：

- 乱序执行/写回可以很早得到结果。
- 按序提交保证精确异常和正确状态。
- 长延迟老指令会阻塞后面年轻指令 commit，即使年轻指令早完成。

### 3.4 Hardware speculation 总结（p36）

PPT 总结：

- Instructions are finished in order according to ROB。
- It can be precise exception。
- It is easily extended to integer register and integer function unit。
- But hardware is too complex。

精确异常 precise exception：

当异常发生时，机器状态看起来像：

- 异常之前的指令都已经完成。
- 异常之后的指令都没有改变体系结构状态。

ROB 正是通过按序提交实现这个性质。

### 3.5 多发射 Multiple Issue（p37-p43）

单发射处理器每周期最多 issue 一条指令。多发射处理器每周期可以 issue 多条。

PPT 比较：

- single-issue spatiotemporal diagram
- multiple-issue spatiotemporal diagram

目标：提高 instruction throughput。

两类多发射处理器：

#### Superscalar

PPT 定义：

- 每个周期 issue 的指令数不固定。
- 取决于代码具体情况。
- 通常 1-8 条，有上限。
- 如果上限是 n，叫 n-issue processor。
- 可由编译器静态调度，也可基于 Tomasulo 动态调度。
- 是目前通用计算最成功的方法。

特点：

- 对程序员透明。
- 处理器检测下一条指令能否流出，不要求程序员手动重排。
- 老编译器生成的代码也能跑，只是效果可能不好。
- 想要好效果，可用 dynamic superscalar scheduling。

#### VLIW

Very Long Instruction Word。

PPT 定义：

- 每周期 issue 的指令数固定，通常 4-16。
- 多条可并行指令组成一个 long instruction / instruction packet。
- 指令包中显式表达指令间并行性。
- 静态由编译器调度。
- 成功应用于数字信号处理和多媒体应用。

Superscalar 和 VLIW 的根本区别：

| 对比 | Superscalar | VLIW |
|---|---|---|
| 每周期发射数 | 不固定，有上限 | 固定 |
| 谁发现并行 | 硬件为主，也可编译器辅助 | 编译器为主 |
| 对程序员/旧代码 | 透明，兼容性好 | 更依赖编译器和机器结构 |
| 硬件复杂度 | 高 | 相对把复杂度转给编译器 |
| 典型场景 | 通用处理器 | DSP、多媒体、嵌入式 |

### 3.6 静态调度的多发射（p45-p49）

PPT 以典型 superscalar 为例：

- 每周期可 issue 1 到 8 条。
- 指令按顺序流出。
- 流出时做冲突检测。
- 当前指令序列中不能有 data conflict 或 structural conflict。

4-issue 静态调度 superscalar：

- IF 阶段从取指部件接收 1-4 条指令，称 issue packet。
- 一个周期中，这些指令可能全能 issue，也可能只有一部分。

冲突检测通常两阶段：

1. 检查 issue packet 内部冲突，初步选择可流出指令。
2. 检查所选指令是否和正在执行的指令冲突。

MIPS 示例假设：

- 每周期流出两条：
  - 1 条 integer instruction
  - 1 条 floating-point operation instruction
- load、store、branch 都归为 integer instructions。

要求：

- 同时取两条指令，即 64 bits。
- 同时 decode 两条指令。
- 从 Cache 取两条指令。
- 判断哪些能流出，范围 0-2 条。
- 发送到对应功能部件。

PPT 假设：

- 所有浮点指令都是加法。
- 浮点执行时间为 2 cycles。
- 简化起见，图中 integer instruction 总在 floating-point instruction 前。

硬件影响：

- “1 integer + 1 floating point” 增加硬件较少。
- FP load/store 会使用 integer 部件，增加访问 FP register 的冲突。
- 可增加 FP register 的读/写端口。
- 流水线中指令数量翻倍，forwarding path 也要增加。

### 3.7 动态调度的多发射（p50-p57）

扩展 Tomasulo 支持 two-way superscalar：

- 每周期 issue 两条：
  - 一条 integer
  - 一条 floating-point
- 简化方法：
  - 指令仍按顺序流向 RS，否则程序语义会破坏。
  - 整数表结构和浮点表结构分开处理。
  - 这样一条 FP 指令和一条 integer 指令可同时进入各自 RS。

#### 循环例子

程序：把向量每个元素加 1，然后存回。

```asm
Loop:
    LD   X2, 0(X1)      // X2 = array element
    ADDI X2, X2, 1      // increment X2
    SD   X2, 0(X1)      // store result
    ADDI X1, X1, 8      // pointer += 8，每个数据 8 bytes
    BNE  X2, X3, Loop   // if not last, branch
```

假设：

- 每周期可流出一条 integer 和一条 floating-point，即使相关。
- 有 integer 部件用于 integer ALU 和地址计算。
- 每类 FP 操作有独立流水化 FP 功能部件。
- 指令流出和写结果各占 1 cycle。
- 有动态分支预测部件和独立分支条件计算部件。
- branch 单独流出，无 delayed branch。
- branch prediction perfect。
- branch 完成前，后续指令只能 fetch/issue，不能 execute。

延迟：

- integer operation 产生结果延迟 1 cycle。
- load 延迟 2 cycles。
- FP add 延迟 3 cycles。

#### Without speculation

PPT 表格前三轮共 15 条指令，19 cycles：

| Iter | Instruction | IS | EX | MEM | Write CDB | Explanation |
|---:|---|---:|---:|---:|---:|---|
| 1 | LD X2, 0(X1) | 1 | 2 | 3 | 4 | first instruction |
| 1 | ADDI X2, X2, 1 | 1 | 5 | | 6 | wait for LD |
| 1 | SD X2, 0(X1) | 2 | 3 | 7 | | wait for ADDI |
| 1 | ADDI X1, X1, 8 | 2 | 3 | | 4 | execute directly |
| 1 | BNE X2, X3, Loop | 3 | 7 | | | wait for ADDI |
| 2 | LD X2, 0(X1) | 4 | 8 | 9 | 10 | wait for BNE |
| 2 | ADDI X2, X2, 1 | 4 | 11 | | 12 | wait for LD |
| 2 | SD X2, 0(X1) | 5 | 9 | 13 | | wait for ADDI |
| 2 | ADDI X1, X1, 8 | 5 | 8 | | 9 | wait for BNE |
| 2 | BNE X2, X3, Loop | 6 | 13 | | | wait for ADDI |
| 3 | LD X2, 0(X1) | 7 | 14 | 15 | 16 | wait for BNE |
| 3 | ADDI X2, X2, 1 | 7 | 17 | | 18 | wait for LD |
| 3 | SD X2, 0(X1) | 8 | 13 | 19 | | wait for ADDI |
| 3 | ADDI X1, X1, 8 | 8 | 14 | | 15 | wait for BNE |
| 3 | BNE X2, X3, Loop | 9 | 19 | | | wait for ADDI |

结论：

- 虽然 issue 率高，但效率不高。
- 15 条指令 / 19 cycles = 0.79 instruction per cycle。
- 原因：
  - data-dependent branches。
  - ALU components 成为瓶颈。
- 一个解决思路：增加一个 adder，把 ALU 功能和地址计算分开。

#### With hardware speculation

有硬件推测后：

| Iter | Instruction | IS | EX | MEM | Write CDB | Commit | Explanation |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | LD X2, 0(X1) | 1 | 2 | 3 | 4 | 5 | first instruction |
| 1 | ADDI X2, X2, 1 | 1 | 5 | | 6 | 7 | wait for LD |
| 1 | SD X2, 0(X1) | 2 | 3 | | | 7 | wait for ADDI |
| 1 | ADDI X1, X1, 8 | 2 | 3 | | 4 | 8 | commit in order |
| 1 | BNE X2, X3, Loop | 3 | 7 | | | 8 | wait for ADDI |
| 2 | LD X2, 0(X1) | 4 | 5 | 6 | 7 | 9 | no execute delay |
| 2 | ADDI X2, X2, 1 | 4 | 8 | | 9 | 10 | wait for LD |
| 2 | SD X2, 0(X1) | 5 | 6 | | | 10 | wait for ADDI |
| 2 | ADDI X1, X1, 8 | 5 | 6 | | 7 | 11 | commit in order |
| 2 | BNE X2, X3, Loop | 6 | 10 | | | 11 | wait for ADDI |
| 3 | LD X2, 0(X1) | 7 | 8 | 9 | 10 | 12 | earliest possible |
| 3 | ADDI X2, X2, 1 | 7 | 11 | | 12 | 13 | wait for LD |
| 3 | SD X2, 0(X1) | 8 | 9 | | | 13 | wait for ADDI |
| 3 | ADDI X1, X1, 8 | 8 | 9 | | 10 | 14 | executes earlier |
| 3 | BNE X2, X3, Loop | 9 | 13 | | | 14 | wait for ADDI |

结论：

- 分支是关键性能限制时，speculation 帮助明显。
- 非推测流水线 completion rate 很快落后于 issue rate，发射更多迭代后会 stall。
- 数据相关分支会限制性能，推测可以缓解。
- 优势依赖准确分支预测。
- 错误推测不仅不提升性能，还会损害性能并显著降低能效。

### 3.8 VLIW 详细问题（p60-p64）

VLIW 做法：

- 把多条可并行执行的指令组合成一个很长指令。
- 长度可超过 100 bits 到数百 bits。
- 指令字分成多个字段，每个字段叫 operation slot。
- 每个 operation slot 直接独立控制一个功能单元。
- 所有处理和指令安排由编译器完成。
- 编译时把多个无关或可并行操作组合成 VLIW。

PPT 要求展示 loop `X[i] = x[i] + s` 的 unrolled version。虽然这页只给题意，核心思想是：

- 展开循环产生更多独立操作。
- 编译器把不同迭代的 load/add/store 填到不同 operation slots。
- 减少空槽，提高并行度。

VLIW 问题：

1. Program code length increased
   - 需要大量 loop unrolling 提高并行性。
   - operation slot 不一定总能填满。
   - 解决：命令共享立即数字段、命令压缩存储、传到 Cache 或 decode 时扩展。

2. Lockstep mechanism
   - 任一操作部件暂停，整个处理器必须暂停。

3. Machine code incompatibility
   - 不同机器功能单元数量、延迟、slot 格式不同，二进制兼容差。

多流出处理器限制：

- 程序固有的 instruction-level parallelism。
- 硬件实现困难。
- superscalar 和 VLIW 自身技术限制。

### 3.9 Superpipelining 超流水（p66-p77）

Super pipelined：

- 把每个流水阶段进一步细分。
- 使多个指令能在一个 clock cycle 中分时进入。
- 如果每 clock cycle 能流出 n 条，它们不是同时流出，而是每 `1/n` 个 clock cycle 流出一条。
- 实际上，超流水的流水线周期是 `1/n` 个 clock cycle。

PPT 给出 two-issue time-sharing 图：同一主时钟周期内分成更小时间片，I1、I2、I3... 更密集进入 IF/ID/EX/MEM/WB。

定义：

- 8 个或更多 instruction pipeline stages 的流水线处理器叫 superpipelining processor。

典型例子：SGI MIPS R4000。

R4000 特征：

- 芯片上有两个 Cache：
  - Instruction Cache
  - Data Cache
- 每个 Cache 容量 8KB。
- 每个 Cache 数据宽度 64b。
- 核心 integer components：
  - 32 x 32 bit general register bank
  - ALU
  - 专用 multiplication/division unit

#### R4000 八级流水

阶段：

```text
IF -> IS -> RF -> EX -> DF -> DS -> TC -> WB
```

每阶段含义：

- IF: First half of instruction fetch
  - PC selection 在这里发生。
  - 同时开始 instruction cache access。

- IS: Second half of instruction fetch
  - 完成 instruction cache access。

- RF: Register Fetch
  - instruction decode
  - register fetch
  - hazard checking
  - instruction cache hit detection

- EX: Execution
  - effective address calculation
  - ALU operation
  - branch-target computation
  - condition evaluation

- DF: Data Fetch first half
  - data cache access 前半。

- DS: Data Fetch second half
  - 完成 data cache access。

- TC: Tag Check
  - 判断 data cache access 是否 hit。

- WB: Write Back
  - loads 和 register-register operations 写回。

PPT 最后展示：

- MIPS R4000 pipeline spatiotemporal diagram。
- Two clock cycles for load delay。

这意味着：流水线越深，load-use 和 branch penalty 往往更严重，所以更需要 forwarding、预测、动态调度等技术。

## 4. 三个核心对比表

### 4.1 依赖、冒险、解决方法

| 问题 | 本质 | 典型例子 | 解决方法 |
|---|---|---|---|
| RAW | 真数据依赖 | 后读前写结果 | stall, forwarding, dynamic scheduling |
| WAR | 名字相关/反相关 | 前读旧值，后写同名寄存器 | register renaming |
| WAW | 名字相关/输出相关 | 两条指令写同一寄存器 | register renaming, in-order commit |
| Structural hazard | 硬件资源不够 | 同时要访问同一端口 | 增加资源、调度、stall |
| Control hazard | 分支方向/目标未知 | branch/jump | branch prediction, BTB, speculation |

### 4.2 Scoreboard、Tomasulo、Tomasulo+ROB

| 机制 | 能乱序执行 | 消除 WAR/WAW | 是否按序提交 | 核心结构 | 主要问题 |
|---|---|---|---|---|---|
| Scoreboard | 可以 | 不彻底 | 不是核心目标 | 统一记分牌表 | WAR/WAW 仍限制写回 |
| Tomasulo | 可以 | 通过保留站/Qi 重命名 | 原始形式不一定 | Reservation stations, CDB | CDB 瓶颈、结构复杂 |
| Tomasulo + ROB | 可以 | 可以 | 是 | ROB + RS + CDB | 更复杂，但支持精确异常和推测恢复 |

### 4.3 同一组指令的时间对比

指令序列：

```asm
FLD    F6,  34(R2)
FLD    F2,  45(R3)
FMUL.D F0,  F2, F4
FSUB.D F8,  F6/F2, F2/F6
FDIV.D F10, F0, F6
FADD.D F6,  F8, F2
```

| 指令 | Scoreboard WB | Tomasulo WB | ROB Commit |
|---|---:|---:|---:|
| FLD F6 | 4 | 4 | 5 |
| FLD F2 | 8 | 5 | 6 |
| FMUL.D F0 | 20 | 16 | 17 |
| FSUB.D F8 | 12 | 8 | 18 |
| FDIV.D F10 | 62 | 57 | 58 |
| FADD.D F6 | 22 | 11 | 59 |

这个表的学习重点：

- Scoreboard 被名字相关和集中控制拖慢。
- Tomasulo 让很多结果更早写回。
- ROB 让完成早的年轻指令不能越过老指令提交，因此 `FADD.D` 虽然 cycle 11 WB，但 cycle 59 才 commit。

## 5. 初学者最容易错的地方

1. 把“依赖”和“冒险”混为一谈。
   - 依赖是程序属性。
   - 冒险是流水线实现遇到的问题。

2. 以为 forwarding 能解决所有 RAW。
   - load-use 紧邻使用时，数据到得太晚，仍需 bubble。

3. 以为 CPI 小就一定快。
   - 要看 `IC x CPI x CycleTime`。

4. 以为局部加速多少，整体就加速多少。
   - Amdahl 定律说明整体受未优化部分限制。

5. 以为乱序执行就一定乱序提交。
   - 现代处理器常乱序执行、乱序写回、按序提交。

6. 以为寄存器重命名能解决 RAW。
   - 不能。RAW 是真实数据流，必须等值产生。
   - 重命名主要解决 WAR/WAW 名字相关。

7. 以为分支预测错了只是浪费一点时间。
   - 深流水/多发射中，错误推测会浪费大量已取/已执行指令和能量。

8. 以为 VLIW 和 superscalar 都只是“每周期多条指令”，没有本质区别。
   - Superscalar 主要靠硬件动态判断。
   - VLIW 主要靠编译器静态打包。

## 6. 自测题

### 6.1 概念题

1. ISA 和 microarchitecture 有什么区别？为什么同一个 ISA 可以有不同 CPU 实现？
2. Response time 和 throughput 分别适合衡量什么场景？
3. `CPU Time = IC x CPI x CycleTime` 中，算法、编译器、ISA、硬件分别影响哪些项？
4. 为什么 Amdahl 定律说明“优化常见情况”很重要？
5. RAW、WAR、WAW 各是什么意思？哪些可通过寄存器重命名消除？
6. 为什么 load-use hazard 即使有 forwarding 也可能需要 stall？
7. 1-bit branch predictor 为什么在内层循环中会误判两次？
8. BTB 和 BHT 分别存什么？为什么二者都重要？
9. Tomasulo 中 `Vj/Vk` 和 `Qj/Qk` 的区别是什么？
10. ROB 为什么能支持 precise exception？

### 6.2 计算题

1. A 程序在机器 X 上 8s，在机器 Y 上 12s。X 比 Y 快多少倍？

2. 某程序执行 10^9 条指令，CPI=1.5，clock rate=3GHz。CPU time 是多少？

3. 某优化让占总时间 30% 的部分加速 10 倍。整体加速比是多少？

4. 某系统整体要提升 4 倍，某部件加速 20 倍。该部件原来至少要占总时间多少比例？

5. 指令类别 A/B/C 的 CPI 分别为 1/3/5，某程序执行数量分别为 100/40/10。平均 CPI 是多少？

### 6.3 简答题参考答案

1. X 比 Y 快 `12/8 = 1.5` 倍。

2. 

```text
CPU Time = IC x CPI / ClockRate
         = 10^9 x 1.5 / (3 x 10^9)
         = 0.5s
```

3.

```text
Speedup = 1 / (0.7 + 0.3/10)
        = 1 / 0.73
        = 1.37
```

4.

```text
4 = 1 / ((1-F) + F/20)
0.25 = 1 - F + F/20
0.25 = 1 - 0.95F
0.95F = 0.75
F = 0.7895
```

至少约 78.95%。

5.

```text
ClockCycles = 100x1 + 40x3 + 10x5 = 270
InstructionCount = 150
Avg CPI = 270 / 150 = 1.8
```

## 7. 建议学习顺序

1. 先背熟第 1 章三条公式：
   - `Performance = 1 / Execution Time`
   - `CPU Time = Clock Cycles x Cycle Time = Clock Cycles / Clock Rate`
   - `CPU Time = IC x CPI x Cycle Time`

2. 再理解 Amdahl：
   - 先画出“可优化部分”和“不可优化部分”。
   - 再套公式。

3. 学第 2 章时先画五级流水：
   - IF, ID, EX, MEM, WB。
   - 标出每条指令什么时候需要源操作数、什么时候产生结果。

4. 再分清三种数据 hazard：
   - RAW 真依赖，必须等数据。
   - WAR/WAW 名字问题，靠重命名解决。

5. 最后比较三个调度层次：
   - Scoreboard：能乱序，但名字相关限制仍多。
   - Tomasulo：保留站 + CDB + Qi，动态重命名。
   - ROB：加提交层，支持推测和精确异常。
