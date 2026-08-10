from __future__ import annotations

import json
from pathlib import Path


SOURCE_JSON = Path("extracted/11--accelerator_motivation.json")
OUTPUT = Path("期末复习资料/11-accelerator_motivation-完整讲义.md")


MANUAL = r"""# Lecture 11: Accelerator Motivation 完整零基础讲义

来源课件：`11--accelerator_motivation.pptx`
课件页数：136 页
主题：为什么深度学习需要专用加速器，以及 AI 加速器为什么通常采用 DSA、并行计算模块、简化控制、Global Buffer、低精度/量化和专用编程模式。

说明：我按 PPT 的可见内容、表格、备注和渲染图进行了整理。PPT 后半部分有不少 speaker notes 是从 MLWeaving 相关页复制到其他页的重复备注，和当前页可见内容不完全对应；本讲义把这些备注完整放在附录中，但正文讲解以可见课件内容为主。

---

## 0. 先建立整节课的主线

这节课不是单纯讲“AI 芯片很快”，而是在建立一个体系结构判断：

深度学习计算有很强的规律性。大量算子最终都可以归结为矩阵乘法、矩阵向量乘法、向量运算、二维 reduce，以及固定的 Burst/Stride 访存模式。既然任务规律很强，就没有必要让硬件像 CPU 那样为所有可能的程序付出巨大通用性成本。我们可以把硬件设计成“偏科但极强”的 DSA，也就是 Domain Specific Architecture，面向特定领域优化。

整节课可以串成下面这条链：

```mermaid
flowchart TB
    A[深度学习应用广泛] --> B[模型计算量和能耗很大]
    B --> C[通用 CPU/GPU 效率不够理想]
    C --> D[先分析深度学习算子]
    D --> E[计算特性: MAC/矩阵乘为主]
    D --> F[访存特性: Burst + Stride/局部规律明显]
    E --> G[DSA: 深度学习加速器]
    F --> G
    G --> H[并行计算模块]
    G --> I[简化控制模块]
    G --> J[Global Buffer]
    G --> K[量化/低精度]
    G --> L[专用编程语言和算子库]
```

你可以把这节课理解为一个硬件设计问题：如果我们知道考试范围只考矩阵乘、卷积、池化、Attention，那还要不要像复习全课程一样准备所有知识点？CPU 就像“全课程地毯式复习”的通才；AI 加速器就像“按老师划重点准备”的偏科高手。

---

## 1. Slides 1-10：先复习 cache coherence 和 memory consistency

PPT 前 10 页不是新主题，而是在衔接前面课程：CPU 和多核系统为了通用性、正确性、透明性，需要付出很多硬件复杂度。理解这些复杂度，才能理解为什么 AI 加速器愿意放弃一部分通用性。

### 1.1 Coherence 和 Consistency 的区别

课件给出两句话：

- Cache coherence 关注不同处理器对同一个内存位置的操作顺序。
- Memory consistency 关注不同处理器对所有内存位置的内存操作顺序。

初学者最容易混淆这两个词。可以这样分：

Coherence 是“同一份数据的多个副本要一致”。例如两个 CPU core 都缓存了地址 `x`，一个 core 写了 `x=1`，另一个 core 以后读 `x`，就不能一直读旧值。这是针对同一个 cache block 的局部顺序。

Consistency 是“程序看到的所有内存操作顺序是什么”。例如线程 1 写 `x` 再写 `y`，线程 2 先读 `y` 再读 `x`，硬件是否允许线程 2 看见 `y` 已更新但 `x` 没更新？这涉及跨地址的全局顺序。

一句话记忆：

| 概念 | 关注对象 | 关键词 | 程序员关心的问题 |
|---|---|---|---|
| Coherence | 同一 cache block/同一地址 | 副本一致 | 我读到的是不是这个地址的最新合理值 |
| Consistency | 所有内存操作/多个地址 | 全局顺序 | 多线程程序中操作顺序是否符合约定 |

### 1.2 Cache coherence 的硬件组成

PPT 说 cache coherence 依赖 cores、caches、interconnect、memory 共同工作。关键组件包括：

- Interconnect：可以是 snoop/bus，也可以是 directory/switch。
- Cache updating：可以 invalidate，也可以 update。
- Cache tags：用 MESI 等状态记录每个 cache line 的状态。

核心理解：coherence 不是“某一个缓存自己决定”的事情。一个 core 的读写会影响其他 core 的 cache line 状态，所以 cache、互连网络和内存控制都必须配合。

### 1.3 MESI 协议

MESI 是四个 cache line 状态：

| 状态 | 英文 | 含义 | 本地 core 是否可直接读/写 |
|---|---|---|---|
| I | Invalid | 该 cache 中没有有效副本，需要从内存或其他 cache 获取 | 不能直接读写 |
| S | Shared | 多个 cache 可能有该 block，内容干净 | 可以直接读，写前要通知/失效别人 |
| E | Exclusive | 只有本 cache 有该 block，内容干净 | 可直接读；写时无需 bus action，转 M |
| M | Modified | 只有本 cache 有该 block，且内容已被修改 | 可直接读写，必要时写回或响应别人 |

MESI 比 MSI 多了 E 状态。E 状态的价值是：如果一个 block 只有我有，而且还没改，那么我写它时不需要发 invalidate，因为没有别人要失效。PPT 的表格说明 MSI 中某些写操作需要 bus action，而 MESI 可以省掉。

要点：

- Local core writes block in E：转为 M，不需要 bus action。
- Remote core reads block in E：E 转 S，因为别人也开始共享。
- Remote core writes block in E：E 转 I，因为别人要独占修改。

### 1.4 Bus-based protocol 和 Directory

Bus-based protocol 的流程：

1. cache 仲裁总线访问权。
2. cache 获得 bus access。
3. cache 把命令放到总线上。
4. 其他 cache 在总线上响应。

总线的特点是简单，但一次只能有一个 transaction，扩展性差。core 数变多时，所有人抢一条路，容易拥塞。

Directory 的思想是：每个 cache block 有一个 home node 维护目录，记录谁有副本、谁是 owner。PPT 中每个 cache line 的 directory 需要：

- 2-bit cache states。
- N-bit sharer list：每个 cache 一个 bit，记录是否共享。
- `log2N` owner bits：记录唯一 owner 是谁。

目录协议比总线更适合多核扩展，因为不需要每次广播给所有节点，但需要额外目录存储和协议复杂度。

### 1.5 Memory consistency 与四类 barrier

PPT 复习四类内存操作顺序：

- Load-Load：读后读顺序。
- Load-Store：读后写顺序。
- Store-Store：写后写顺序。
- Store-Load：写后读顺序。

内存模型越强，程序员越容易理解，但硬件性能开销越高。课件表格：

| 内存模型 | 保留顺序 | 例子 |
|---|---|---|
| Sequential Consistency | LL、LS、SS、SL 都保留 | Dual 386 |
| Total Store Order | LL、LS、SS 保留，SL 放松 | x86/64 |
| Partial Store Order | LL、LS 保留，SS、SL 放松 | Arm |
| Really weak memory model | 更弱 | DEC Alpha |

这一段和 AI 加速器的关系：CPU 为了通用程序正确性，需要支持复杂一致性、cache、乱序执行、load-store queue 等机制。AI 加速器面对的算子更固定，可以把这些复杂资源减少，把面积和功耗转给矩阵计算和片上 buffer。

---

## 2. Slides 11-17：为什么需要深度学习处理器

### 2.1 深度学习应用广泛，所以市场和需求足够大

PPT 用 “AI for X” 表达深度学习已进入大量应用：

- 图像识别。
- 语音处理。
- 自然语言处理。
- 云服务器。
- 智能手机。

如果一种计算只用于很小众场景，专门做硬件可能不划算。但深度学习已经广泛渗透，足以支撑专用硬件生态。

### 2.2 通用 CPU/GPU 处理神经网络效率低

课件列出两个例子：

- Google Brain 用 1.6 万个 CPU 核跑数天完成猫脸识别训练。
- AlphaGo 与李世石下棋用了 1202 个 CPU 和 176 个 GPU。

这些数字不只是“看起来很大”，它们说明神经网络计算如果只靠通用处理器，会消耗巨大算力和电力。深度学习的瓶颈不是“能不能算”，而是“能不能以可接受成本算”。

### 2.3 CPU、GPU、DL Accelerator 的直观类比

PPT 给出三个类比：

- CPU：Central Processing Unit，一个大学生。
- GPU：Graphics Processing Unit，100 个小学生。
- DL Accelerator：Deep Learning Accelerator，一个偏科生。

这个类比很重要：

- CPU 像大学生：理解力强，能处理各种复杂任务，但做大量重复简单计算时成本高。
- GPU 像很多小学生：每个人能力简单，但人数多，适合大量相似任务。
- DL Accelerator 像偏科生：只擅长某些题型，但在这些题型上极强。

### 2.4 四个性能指标

| 指标 | PPT 定义 | 初学者解释 |
|---|---|---|
| 延时 latency | AI 模型做出决定的时间 | 单次请求从输入到输出要多久 |
| 通用性 generality | 适合运行的应用程序范围 | 能不能跑各种程序 |
| 能效 energy efficiency | 单位能量支持的计算量 | 同样电量能做多少计算 |
| 可迭代性 iterability | AI 模型变化时硬件适应能力 | 算法变了硬件是否还能跟上 |

### 2.5 不同计算平台的取舍

能效 vs 通用性图：

- CPU 通用性最好，但能效较低。
- GPU 通用性低于 CPU，能效更高。
- FPGA 可重构，通用性/能效在中间。
- ASIC 能效很高，但通用性低。
- 深度学习处理器位于 CPU/GPU 与 ASIC 之间，专门针对深度学习提升能效，同时保留一定可编程性。

延时 vs 可迭代性图：

- CPU/GPU 可迭代性好，因为软件改一改就能跑新模型，但延时可能更高。
- ASIC 延时低，但如果算法变了，硬件难改。
- FPGA 可迭代性比 ASIC 好，但通常不如 ASIC 极致。
- 深度学习处理器追求低延时和一定可迭代性的平衡。

核心结论：AI 加速器不是单方面“比 CPU/GPU 好”，而是在通用性、能效、延时、可迭代性之间选择更适合深度学习的点。

---

## 3. Slides 18-44：深度学习算子分析

设计加速器前，必须先知道目标应用是什么。PPT 说分析深度学习算法时关心两大特性：

1. 计算特性：是否存在固定、重复的计算模式。
2. 访存特性：数据访问是否有局部性，数据访问和后续计算之间有什么关系，对带宽有什么真实需求。

### 3.1 VGG19 作为典型 CNN

PPT 用 VGG19 作为例子：

- 参数：1.14 亿。
- 层类型：卷积、池化、全连接。
- 计算过程：简洁。
- 层数：25 = 16 + 5 + 3 + 1。
- 卷积层：16 个，3x3 卷积核，图大小不变。
- 池化层：5 个，Max Pooling。
- 全连接层：3 个。
- SoftMax：1 个。

为什么用 VGG19？因为它结构清楚，能代表 CNN 中常见的 Conv、Activation、Pooling、FC 等算子。讲清这些算子，就能看出 AI 加速器应该优化什么。

### 3.2 卷积层 Conv

PPT 从一个 `32x32x3` 图像和 `5x5x3` filter 开始。`3` 表示 RGB 三个通道。卷积的基本动作是：filter 在输入图像上滑动，每次拿出一个局部窗口，与 filter 对应位置相乘并求和，得到输出 feature map 的一个点。

课件用 `1` 和 `-1` 的小例子演示卷积：

- 输入局部窗口可以看成一个向量，例如 `(1, -1, -1, 1)`。
- filter 也可以看成一个向量，例如 `(1, -1, -1, 1)`。
- 对应相乘再求和：`1*1 + (-1)*(-1) + (-1)*(-1) + 1*1 = 4`。
- 如果输入变成 `(-1, 1, 1, -1)`，同一个 filter 得到 `-4`。

这说明卷积本质上可以展开成矩阵乘向量或矩阵乘矩阵：

- 1 个 filter：处理后的数据矩阵 × filter 向量 = 输出向量。
- 多个 filters：处理后的数据矩阵 × filters 矩阵 = 输出矩阵。

卷积层的结论：

- 计算特性：矩阵乘向量或矩阵乘矩阵。
- 访存特性：Burst + Stride。

Burst 是连续突发访问，例如一次读一段连续内存。Stride 是跳着访问，例如每隔固定距离取一个元素。卷积滑窗会导致既有连续访问，也有固定步长访问。

### 3.3 Activation 激活函数

课件总结：

- 计算特性：向量运算。
- 访存特性：Burst。

激活函数例如 ReLU、sigmoid、tanh，通常对每个元素独立操作。比如 ReLU 是 `max(0, x)`。它不需要复杂矩阵乘，只要把一串数据读出来逐个处理，所以是向量运算，访存多为连续 Burst。

### 3.4 Pooling 池化层

PPT 用 `2x2 pooling, stride=2` 演示：

输入局部块 `(3, 5, 6, 2)`：

- Max Pooling = `max(3, 5, 6, 2) = 6`。
- Average Pooling = `avg(3, 5, 6, 2) = 4`。

后续窗口：

- `(2, 4, 5, 1)` 得到 max=5, avg=3。
- `(5, 7, 8, 4)` 得到 max=8, avg=6。
- `(6, 8, 9, 5)` 得到 max=9, avg=7。

池化层的结论：

- 计算特性：二维空间上的 reduce 操作。
- 访存特性：Burst + Stride。

Reduce 指“把多个值合成一个值”，例如 max、sum、average。池化不像卷积那样做大量乘法，但它仍然有固定窗口和步长。

### 3.5 Fully Connected 全连接层

PPT 说：

- Flatten：把 output map 摊平，用于输入全连接层。
- Fully Connected：输入向量中的每个元素都和输出层神经元相连。
- 计算特性：矩阵乘向量。
- 访存特性：Burst + Stride。

从数学上看，全连接层就是：

```text
y = W x + b
```

其中 `x` 是输入向量，`W` 是权重矩阵，`b` 是偏置，`y` 是输出向量。每个输出元素都是一行权重和输入向量的点积。

### 3.6 Transformer、Attention、Feed Forward

课件也把 Transformer 纳入分析。

Transformer Block 的流程：

1. Tokenization：文本转 token。
2. Input Layer：输入嵌入。
3. Attention。
4. Feed Forward。
5. Output Layer。

Attention 页给出张量维度：

- `Q (H x H)`、`K (H x H)`、`V (H x H)`：投影矩阵。
- `a (S x H)`：输入序列表示，S 是序列长度，H 是隐藏维度。
- `Qa, Ka, Va (S x H)`：输入乘 Q/K/V 后的结果。
- `A (S x S)`：attention score 矩阵。
- `Atten (S x H)`、`Ao (S x H)`：注意力输出。

Attention 的结论：

- 计算特性：矩阵乘矩阵。
- 访存特性：Burst + Stride。

Feed Forward 页给出：

- `Ao (S x H)` 输入。
- `L2 (H x 4H)`、`L3 (H x 4H)` 相关矩阵。
- `F1 (S x 4H)` 中间结果。
- `Fo (S x H)` 输出。

Feed Forward 的结论：

- 计算特性：矩阵乘矩阵。
- 访存特性：Burst + Stride。

### 3.7 算子总结表

PPT 的总结非常关键：

| Operator | 计算特性 | 访存特性 |
|---|---|---|
| Conv | 矩阵相乘 | Burst + stride |
| Activation | 单向量操作 | Burst |
| Pooling | 单矩阵 Reduce 操作 | Burst + stride |
| FC | 矩阵相乘 | Burst |
| Attention | 矩阵相乘 | Burst + stride |

另外两个结论：

- MAC（Multiply-Accumulate，乘加）是核心操作。
- 矩阵乘法计算量占比高于 90%。
- 深度学习有 Fixed Memory Access Pattern，固定内存访问模式。

所以 DSA 的设计重点就很自然：

1. 强化矩阵/向量乘法。
2. 针对固定访存模式优化数据搬运。

---

## 4. Slides 45-50：DSA 设计思想

DSA 是 Domain Specific Architecture，领域专用体系结构。PPT 给出五个设计思想。

### 4.1 Global Buffer

使用专有存储器减少数据搬运距离与开销，例如用 scratchpad memory/global buffer 替换复杂 cache。

初学者理解：CPU cache 是硬件自动猜“你等下可能用什么”；Global Buffer 是程序/编译器明确安排“这块数据放这里，等下计算单元直接用”。前者省程序员，后者省硬件和能耗。

### 4.2 简化控制模块

减少高级微架构特性，把节省出来的面积用于更多运算单元或片上存储。

CPU 需要分支预测、乱序执行、复杂调度，因为它不知道程序会怎么跑。AI 加速器面对大量规则矩阵计算，控制逻辑可以简单很多。

### 4.3 并行计算模块

使用符合特定领域加速需求的最简单并行形式。例如对于矩阵运算，单条指令直接支持小矩阵运算。

CPU 的 SIMD 是“一个指令处理多个数据”；AI 加速器更进一步，可以把矩阵乘做成硬件核心能力。

### 4.4 量化

减少计算数据尺寸与类型，以符合性能要求。深度学习推理可采用 int8 量化。

数值位宽越低：

- 每个数占用存储更少。
- 内存带宽压力更小。
- 乘法器面积和功耗更低。
- 并行度更高。

### 4.5 专用编程语言

使用 DSA 专用语言进行编程。因为 DSA 的存储和计算方式不同于 CPU，普通 C/C++ 的抽象不一定能表达高性能数据搬运。

---

## 5. Slides 49-66：并行计算模块，为什么 CPU 流水线不够适合深度学习

### 5.1 CPU 的冯诺依曼结构

PPT 回顾五大基本组件：

- 输入设备：输入数据和程序。
- 存储器：记忆程序和数据。
- 运算器：完成数据加工处理。
- 控制器：控制程序执行。
- 输出设备：输出处理结果。

CPU 支持的功能非常多：

- Load：内存加载到寄存器。
- Store：寄存器存回内存。
- Integer 运算：ADD/SUB/MUL 等。
- Float 运算：fADD/fSUB/fMUL 等。
- Logical 运算：AND/OR/NOT 等。
- Conditional Jump：有条件跳转。
- Unconditional Jump：无条件跳转。
- 辅助功能：Cache、分支预测、预取、中断、权限等。

CPU 的问题不是功能少，而是功能太全。为通用性付出的面积、功耗和控制复杂度，在深度学习这种规则计算里未必划算。

### 5.2 CPU 经典 5 级流水线

五级流水线：

| 阶段 | 全称 | 含义 |
|---|---|---|
| IF | Instruction Fetch | 取指令 |
| ID | Instruction Decode | 指令解码 |
| EXE | Execute | 执行 |
| MEM | Memory Operand Fetch | 取内存操作数 |
| WB | Writeback | 写回 |

PPT 用洗衣房类比：

- 洗衣机洗涤。
- 干衣机烘干。
- 折叠衣服。
- 放进柜子。

非流水线是洗完一件完整流程再处理下一件；流水线是不同衣服处在不同阶段，总吞吐更高。

但对深度学习来说，问题在于：一条 CPU 指令通常只操作一个数或有限几个数，五级流水线中真正做计算的是 EXE，其余阶段服务于指令管理和数据搬运。对于海量矩阵乘，这些指令级开销太大。

PPT 总结：

- 优势：一条指令操作一个数，灵活，可实现任意功能函数。
- 劣势：效率低，五个流水线模块只有 EXE 真正在计算。

### 5.3 SIMD 是 CPU 的并行方式，但还不够激进

SIMD = Single Instruction Multiple Data，单指令多数据。

PPT 示例：

- Scalar：一个周期完成一个加法。
- SIMD：一个周期完成多个加法。

Intel CPU 上：

- 256-bit AVX2：可容纳 8 个 32-bit float。
- 512-bit AVX512：可容纳 16 个 32-bit float。

但 PPT 说 “Not aggressive enough”。原因是深度学习需要的不是 8 个或 16 个 float 的小并行，而是大规模矩阵乘的持续高吞吐。AI Processor 应该有更 aggressive 的 custom computing unit。

### 5.4 深度学习加速器处理矩阵乘法

PPT 说：

- FC 和 Conv 相关计算占据 99% 的计算。
- Conv 层数多。
- FC 参数多。
- 专门支持矩阵计算的电路会大幅提高整体性能。
- 专门支持向量计算的电路也会提高整体性能。

这就是 AI 加速器中 Cube/Tensor Core/MAC array 的动机：既然大部分时间都在矩阵乘，就把矩阵乘做成硬件主角。

---

## 6. Slides 67-72：简化控制模块

### 6.1 CPU 的超标量 Superscalar

CPU 为了提升单线程性能，会用复杂控制逻辑挖掘指令级并行。PPT 以 Intel Core 2 为例：

- CISC 指令内部 RISC 化。
- 读入 CISC 指令。
- 转换成 RISC 指令后执行。
- 6 条 CISC 指令一起解析。
- 4 条 uop 并发。
- 在 96 条 uop 间寻找并行。

这非常强大，但也非常复杂。CPU 不知道程序里哪些指令能并行，所以硬件要动态分析依赖、乱序调度、预测分支。

### 6.2 AI Processor 的控制逻辑

PPT 说 AI Processor：

- 多 instruction queue 管理指令。
- Scalar/Vector/Cube/MTE 有单独 instruction queue。
- 每个 instruction queue 顺序 issue。
- 没有特别优化 instruction 之间的并行。
- 优化重点不在提升指令间并行，即不在控制模块。

这句话很关键。AI 加速器不是完全没有控制，而是控制模块不做 CPU 那种极复杂的动态调度。它把重点放在：

- 指令内部并行，例如一条 Cube 指令完成大量矩阵乘。
- 数据搬运和计算流水。
- 编译器/程序员提前安排好执行顺序。

换句话说，CPU 靠硬件“临场发挥”；AI 加速器靠编译器和算子库“提前排练”。

---

## 7. Slides 73-97：Global Buffer，为什么 AI 加速器不用复杂 cache 作为核心

### 7.1 数据搬运比计算更耗能

PPT 引用 EIE/ISCA 2016 的能耗表：

| 32-bit Operation | Energy (pJ) | 相对 int ADD 成本 |
|---|---:|---:|
| ADD int | 0.1 | 1 |
| ADD float | 0.9 | 9 |
| Register File | 1 | 10 |
| MULT int | 3.1 | 31 |
| MULT float | 3.7 | 37 |
| SRAM Cache | 5 | 50 |
| DRAM | 640 | 6400 |

重点：一次 DRAM 访问约等于一次整数加法能耗的 6400 倍。很多初学者以为“计算最贵”，但在现代体系结构里，数据搬运常常更贵。AI 加速器必须减少数据从远处搬来搬去。

### 7.2 DRAM、SRAM、FF、Flash 的特点

PPT 复习不同存储：

- Flip-Flops：非常快、可并行访问，但非常贵，一个 bit 需要几十个晶体管。
- SRAM：较快，一次一个 data word，贵，一个 bit 需要 6+ 个晶体管。
- DRAM：较慢，一次一个 data word，读取会破坏内容，需要 refresh，制造需要特殊工艺，但便宜，一个 bit 只需一个晶体管加一个电容。
- Flash：更慢，非易失，非常便宜。

结论：越快越贵，越便宜越慢。AI 加速器要在芯片上放足够的 SRAM/global buffer，让高频访问尽量不去 DRAM。

### 7.3 CPU 为什么需要 cache

PPT 给出 CPU 访问时间：

- Main memory/DRAM：约 100 ns。
- ALU/register 附近：约 0.4 ns。
- Cache：约 2-12 ns。

内存访问延时比寄存器访问长两个数量级。Cache 放在 CPU 和 DRAM 中间，用 SRAM 缓存最近/常用数据，给程序员“又大又快”的存储幻觉。

### 7.4 Cache 的图书馆类比

PPT 类比：

- 学生坐在图书馆桌前写论文。
- 桌上最多放 10 本参考书。
- 大多数情况下桌上的书够用。
- 找不到材料时去远处书架找书。
- 桌子满了就把最少用的书放回书架，换新书。
- 找书换书花 10 分钟。

对应关系：

| Cache 概念 | 图书馆类比 |
|---|---|
| Cache hit | 桌上找到想要的书 |
| Cache miss | 桌上没有，需要去书架 |
| 内存访问 latency | 去书架找书的时间 |
| 替换策略 Random/FIFO/LRU | 决定哪本书放回书架 |
| Cache 容量 | 桌子能放几本书 |

### 7.5 Cache 的本质与局部性

PPT 定义：

Cache 是任何“记住 frequently used results，从而避免重复长延时操作”的结构。

Cache 能工作的依据是 locality：

- 时间局部性 Temporal Locality：最近访问过的位置容易再次访问。例如函数本地参数可能反复使用。
- 空间局部性 Spatial Locality：最近访问位置附近的位置容易被访问。例如数组循环中访问第 3 个元素后，可能访问第 4 个。

### 7.6 Tag、Set、Offset

PPT 图中 16-bit memory address 被拆成：

- Tag：10 bit。
- Set：2 bit。
- Offset：4 bit。

Cache 是 2-way、4-set，每条 cache line 为 16B。

理解方式：

- Offset：在一个 cache line 内取哪个字节/位置。
- Set：这个地址应该映射到 cache 的哪个 set。
- Tag：进入 set 后，用 tag 判断这个 line 是否真的是目标内存块。

访问流程：

1. 用 set 位找到对应 set。
2. 比较 set 内各 way 的 tag。
3. tag 相等则 cache hit。
4. tag 不相等则 cache miss，需要从内存取对应 line。

PPT 备注还提到 associativity：

- Direct mapped cache：更多地址位用于 set selection。
- 2-way set associative：tag 和 set 分配如图。
- Fully associative：没有 set selection bit，任何 line 可放任何位置，但比较更贵。

### 7.7 CPU cache 面积问题

PPT 指出 Intel 4 核 CPU 中，近一半芯片空间花在 L3 cache 上，L3 大小约 2.5MB/core。问题是：cache 对通用程序很有用，但芯片面积利用率对深度学习不一定最优。

CPU cache 的好处：

- Automatic：硬件自动管理层级间数据搬运。
- 对程序员透明。
- 平均程序员不懂 cache 也能受益。
- 简单启发式：保留最近使用的数据。

但 AI 加速器的目标不同：提高算力、降低功耗，可以牺牲一部分可编程性。

### 7.8 为什么 Global Buffer 更适合 AI 加速器

PPT 问：“复杂 cache 设计是否适合深度学习？”

结论：

- Strided 内存访问容易竞争同一个 cache set，引起 eviction。
- Strided 访问 pattern 比较固定，无需 cache 这么精致的结构，人工控制即可。
- 举例：当 stride = 2^6、2^7、2^8 等时，可能反复访问同一个 set，导致冲突。

AI Accelerator 的 Global Buffer：

- 分块使用。
- 降低单位内存访问功耗。
- 编程更难，因为要考虑 buffer 位置。

PPT 对比 Cache 和 Buffer：

| 项目 | Cache | Buffer |
|---|---|---|
| 能耗 | 高 | 低 |
| 芯片面积 | 大 | 小 |
| 管理方式 | 自动 | 手动 |

一句话：cache 让程序员舒服，global buffer 让硬件高效。AI 加速器选择高性能和低功耗，所以接受更难的编程/编译。

---

## 8. Slides 98-131：低精度、任意精度和 MLWeaving

### 8.1 为什么低精度对机器学习可行

PPT 的直觉例子：

- 模型输出在 0 到 1。
- 大于 0.5 就判断为 cat。
- 全精度计算：`1.310245 * 0.602069 = 0.788857897`，大于 0.5。
- 低精度近似：`about 1.3 * about 0.6 = about 0.78`，仍然大于 0.5。

所以如果最终决策边界没有改变，低精度误差可以接受。PPT 用一句话总结：“Relax, It is only Machine Learning.” 意思不是机器学习随便算，而是很多 ML 任务对小数值误差有容忍度。

### 8.2 不同任务需要不同精度

PPT 说不同输入可能需要不同 bit：

- 某些图像 3-bit 就够。
- 另一些图像可能需要 9-bit。

这说明固定只支持 int8/fp16 不是最理想。若任务只需 4-bit，而硬件只能 8-bit，就浪费带宽和计算资源。

### 8.3 当前硬件的低精度支持

PPT 分两类：

CPU/GPU：

- CPU：Char 8-bit、Short 16-bit。
- GPU：FP8、FP16。
- 对低精度支持不是很好。
- 容易缺对应指令支持。
- 没有资源倾斜。
- 主要优化浮点操作、32 位定点操作。

AI Processor/TPU/Ascend：

- TPU：INT8。
- Ascend：INT8 等。
- 对低精度支持更好。
- 有完备指令支持。
- 有资源倾斜。
- 主要优化低精度指令操作。

PPT 进一步提出：用第一性原理重新考虑低精度，应支持任意精度。

### 8.4 SGD 中低精度的机会

PPT 用线性回归和 SGD 说明：

SGD 有三部分：

- Training Data：Database/Sensor。
- Computing Device：FPGA/GPU/CPU。
- Model：DRAM/Cache。

流程：

1. `Ar = get_data()`：取一行数据。
2. `x = get_model()`：取模型。
3. `g = comp_grad(x, Ar)`：计算梯度，例如 `dot(Ar, x)Ar`。
4. `x = x - g`，再 `set_model(x)`：更新模型。

PPT 备注指出两个性质：

- 多核运行时 model `x` 可能 stale。
- dataset 和 gradient 可以低精度，不一定总是 32-bit float。

本节重点是第二点：数据和梯度可低精度，为任意精度加速提供空间。

### 8.5 MLWeaving 的三个观察

PPT 提出任意精度 NN Accelerator：

- New Memory Layout (Software)。
- New Hardware Design (Hardware)。

引用：

- Zeke Wang 等，MLWeaving，VLDB 2019。
- Zhenhao He、Zeke Wang、Gustavo Alonso，BiS-KM，FPGA 2020。

三个观察：

1. 经常 memory bandwidth bound，内存带宽是瓶颈。
2. 低精度如 8-bit fixed point 通常能提供合理质量。
3. 同一数据集上的不同 inference/training task 可能需要不同精度。

问题：能不能只存一份数据，但高效支持任意精度的数据搬运？

### 8.6 传统数据布局 vs MLWeaving 新布局

传统系统存 ML 数据：

- 按 row 存。
- 对第 1 行 A，先存第 1 个 feature 的 bit1、bit2、bit3、bit4。
- 再存第 2 个 feature 的 bit1、bit2、bit3、bit4。
- 再存第 2 行 B。

MLWeaving：

- 仍按 row，但在 row 内按 bit-plane 组织。
- 先把第 1 行所有 feature 的第 1 位存一起。
- 再把所有 feature 的第 2 位存一起。
- 再存第 3 位、第 4 位。
- 然后处理第 2 行。

好处：

- 如果只需要 1-bit，只读第一组 bit。
- 如果需要 3-bit，只读前三组 bit。
- 不浪费内存带宽读取不需要的低位。

局限：

- 在 CPU 上不好用。
- CPU 没有针对新 memory layout 的 custom instruction。
- CPU 需要从不同内存位置 group bits，再进入后续计算，开销很大。

所以 MLWeaving 必须结合新硬件设计，例如 FPGA 上的 bit-serial multiplier。

### 8.7 Bit-Serial Multiplier (BSM)

PPT 用十进制数字帮助理解，但说明真实每一位应该是 binary。

例子：`4321 x 0020`。

不同精度含义：

- 4-bit：`4321`。
- 3-bit：`4320`。
- 2-bit：`4300`。
- 1-bit：`4000`。

普通乘法会一次处理完整数。Bit-serial multiplier 的思想是逐位累加：

```text
Sum += P * S[i]
```

其中：

- S 是 bit-serial part，彩色部分，一次读一位/一组 bit-plane。
- P 是 bit-parallel part，黑色部分，例如 `0020`。
- Sum 保存累加结果。

PPT 展示四个周期：

1-bit precision：

- 第 1 cycle 取最高位 `4`。
- `4` 表示 `4000`。
- `Sum += 20 * 4000`。
- 得到 `80000`，完成 1-bit precision。

2-bit precision：

- 第 2 cycle 取第二位 `3`。
- `3` 表示 `300`。
- `Sum += 20 * 300`。
- 累加得到 `86000`，完成 2-bit precision。

3-bit precision：

- 第 3 cycle 取第三位 `2`。
- `2` 表示 `20`。
- `Sum += 20 * 20`。
- 累加得到 `86400`，完成 3-bit precision。

4-bit precision：

- 第 4 cycle 取第四位 `1`。
- `1` 表示 `1`。
- `Sum += 20 * 1`。
- 累加得到 `86420`，完成 4-bit precision。

这个例子要学到的不是十进制乘法，而是思想：精度越低，需要处理的 bit-plane 越少；硬件能在任意精度处停下。

### 8.8 MLWeaving 性能

PPT 的图显示：

- Computing time vs Precision：精度越低，计算时间近似线性降低。
- Memory traffic vs Precision：精度越低，内存流量近似线性降低。

备注指出：

- MLWeaving 可实现几乎线性的低精度加速。
- 1-bit 情况没有达到理想线性加速，原因是 pipeline latency 太长，无法被摊销。
- 实际训练中很少用 1-bit，因为数据会丢失太多有用信息。

---

## 9. Slides 132-135：AI 加速器编程模式

### 9.1 CPU 编程 vs AI Accelerator 编程

CPU 代码：

```c
uint32_t a[32] = {0, 1, 2, ..., 31};
uint32_t b[32] = {0, 1, 2, ..., 31};
uint32_t c[32];
for (uint i = 0; i < 32; i++) {
    c[i] = a[i] + b[i];
}
```

程序员只写数组和循环，不需要显式管理数据从 DDR 到片上 buffer 的搬运。cache 和内存层级由硬件透明处理。

AI Accelerator 代码思想：

```c
DDR uint32_t a[32] = {0, 1, 2, ..., 31};
DDR uint32_t b[32] = {0, 1, 2, ..., 31};
DDR uint32_t c[32];

Unified_Buffer uint32_t a_ub[32];
Unified_Buffer uint32_t b_ub[32];
Unified_Buffer uint32_t c_ub[32];

Dma_Mov(a_ub, a);
Dma_Mov(b_ub, b);
Vector_add(c_ub, a_ub, b_ub);
Dma_Mov(c, c_ub);
```

这里程序员/编译器必须显式：

- 在 DDR 和 Unified Buffer 之间搬数据。
- 调用向量计算单元。
- 再把结果搬回 DDR。

这就是显式 buffer 管理。

### 9.2 高性能但难编程

PPT 问：“那 AI 加速器的编程模式怎么样？”

答案：

- 高性能。
- 难编程。

解决方式：

- 厂商提供算子库。
- 用户直接调用库。

所以多数用户不会手写最底层 DMA 和 vector/cube 指令，而是通过 CANN、CUDA、cuDNN、算子库、深度学习框架间接使用。

### 9.3 整体比较：AI Accelerator vs CPU

PPT 最后一张总结表：

| 维度 | CPU | DSA/AI Accelerator |
|---|---|---|
| On-chip Memory | Cache | Global Buffer |
| Instruction Issue | Superscalar | In-order/simple |
| Parallelism | Inter-instruction | Intra-instruction |
| Functionality | Full | Partial |
| Optimization Purpose | Low Latency | High Throughput |
| Programming Language | General | Domain-specific |

逐项解释：

- On-chip Memory：CPU 用 cache 自动管理；AI 加速器用 global buffer 手动/编译器管理。
- Instruction Issue：CPU 复杂超标量乱序/并发发射；AI 加速器更简单、有序。
- Parallelism：CPU 挖掘指令之间的并行；AI 加速器让一条指令内部做大量并行。
- Functionality：CPU 功能完整；DSA 功能不完整但针对领域强。
- Optimization Purpose：CPU 常优化单任务低延时；AI 加速器常优化大批量高吞吐。
- Programming Language：CPU 用通用语言；DSA 需要领域专用语言、DSL 或算子库。

---

## 10. 本节课最重要的知识点压缩

如果你只背结论，至少要会下面这些：

1. 深度学习加速器的动机：深度学习应用广泛，计算量巨大，通用 CPU/GPU 能效不够，专用处理器能在能效、延时、吞吐上更好。
2. CPU/GPU/加速器类比：CPU 是通才，GPU 是大量简单并行，加速器是偏科高手。
3. 深度学习算子分析看两点：计算特性和访存特性。
4. Conv/FC/Attention 主要是矩阵乘；Activation 是向量运算；Pooling 是 reduce。
5. MAC 和矩阵乘占比极高，这是并行计算模块的依据。
6. DSA 五个思想：Global Buffer、简化控制、并行计算模块、量化、专用编程语言。
7. CPU 五级流水线灵活但深度学习效率低，因为大量阶段不是实际计算。
8. SIMD 是 CPU 并行方式，但对 AI 大规模矩阵乘还不够激进。
9. CPU 超标量用复杂控制挖指令间并行；AI 加速器把重点放在指令内大并行。
10. 数据搬运比计算耗能得多，DRAM 访问约为 int add 的 6400 倍。
11. Cache 自动、易用、面积/能耗较大；Global Buffer 手动、难编程、低能耗。
12. Stride 访存可能导致 cache set 冲突；深度学习访存 pattern 固定，适合人工/编译器控制。
13. 低精度可行，因为 ML 对小误差有一定容忍度。
14. 任意精度的意义：不同任务需要不同 bit，固定 int8/fp16 可能浪费。
15. MLWeaving 通过 bit-plane 式 memory layout 支持按需读取精度。
16. Bit-serial multiplier 可以逐位累加，精度越低处理周期越少。
17. AI 加速器编程需要显式管理数据搬运，因此通常依赖厂商算子库和框架。

---

## 11. 初学者概念依赖图

```mermaid
flowchart TB
    A[内存层级和 cache] --> B[数据搬运能耗]
    A --> C[局部性/Tag Set Offset]
    B --> D[Global Buffer]
    C --> D
    E[神经网络算子] --> F[Conv/FC/Attention 矩阵乘]
    E --> G[Activation 向量运算]
    E --> H[Pooling Reduce]
    F --> I[并行计算模块/MAC Array]
    G --> I
    H --> I
    J[CPU 流水线/SIMD/超标量] --> K[CPU 通用性成本]
    K --> L[简化控制模块]
    I --> M[DSA]
    D --> M
    L --> M
    N[低精度/量化] --> M
    O[专用编程/算子库] --> M
```

学习顺序建议：

1. 先懂 cache 为什么存在：DRAM 慢，cache 用局部性隐藏延迟。
2. 再懂深度学习算子为什么规则：矩阵乘、向量操作、reduce、固定访存。
3. 再懂 DSA 为什么要牺牲通用性：把通用控制/cache 的成本换成 MAC 和 buffer。
4. 最后懂低精度和编程模型：数值位宽、数据布局、DMA、算子库。

---

## 12. 易错点

### 易错 1：把 GPU 和 AI 加速器混为一谈

GPU 也能跑深度学习，但它仍比专用 AI processor 更通用。AI processor 更偏向矩阵/张量计算、片上 buffer、低精度和专用指令。

### 易错 2：以为 cache 一定比 buffer 高级

cache 对程序员友好，但不是所有场景都最高效。深度学习访存 pattern 固定，global buffer 手动控制反而能减少面积和能耗。

### 易错 3：以为低精度一定降低正确率

低精度可能降低精度，但机器学习有误差容忍。关键是任务需要多少 bit，而不是永远越高越好。

### 易错 4：以为 CPU 慢是因为没有并行

CPU 有流水线、SIMD、超标量、乱序执行。问题是它的并行形式和控制开销不是为大规模矩阵乘专门设计的。

### 易错 5：只背 DSA 五点，不会解释为什么

每一点都来自前面的算子和硬件分析：

- 矩阵乘多，所以要并行计算模块。
- 控制规律，所以可简化控制。
- 数据搬运贵，所以要 global buffer。
- ML 容忍误差，所以要量化。
- 硬件特殊，所以需要专用语言/库。

---

## 13. 自测题

### 题 1

问：Cache coherence 和 memory consistency 的区别是什么？

答：coherence 关注不同处理器对同一内存位置/cache block 的操作顺序和副本一致性；consistency 关注不同处理器对所有内存位置的操作顺序，是程序员与微架构之间关于内存可见顺序的约定。

### 题 2

问：为什么 MESI 比 MSI 多一个 E 状态可以减少 bus action？

答：E 表示该 cache 独占且干净。如果本地 core 写 E 状态 block，不需要通知别人，因为没有其他 cache 共享该 block，只需本地转为 M。

### 题 3

问：深度学习算子分析主要看哪两类特性？

答：计算特性和访存特性。计算特性看是否有固定重复计算模式，如矩阵乘；访存特性看数据访问局部性、Burst/Stride 模式以及带宽需求。

### 题 4

问：卷积为什么能看成矩阵乘？

答：把每个滑动窗口展开为一行，把 filter 展开为向量，所有窗口组成矩阵。一个 filter 时是矩阵乘向量；多个 filters 时是矩阵乘矩阵。

### 题 5

问：为什么 AI 加速器更偏向 Global Buffer 而不是复杂 Cache？

答：深度学习访存模式相对固定，可由程序/编译器提前安排；cache 自动但面积和能耗较高，stride 访问还可能造成 set 冲突。Global Buffer 手动管理更难编程，但能降低数据搬运功耗和芯片面积。

### 题 6

问：CPU 超标量和 AI Processor 简化控制的区别是什么？

答：CPU 用复杂硬件在很多 uop 中动态寻找指令间并行；AI Processor 通常用多个 instruction queue 顺序 issue，把重点放在 scalar/vector/cube/MTE 等指令内部的大并行，而不是复杂控制逻辑。

### 题 7

问：为什么低精度能用于机器学习？

答：很多 ML 任务只需保持最终分类/回归结果足够正确，对小数值误差有容忍度。若全精度和低精度结果都位于同一决策边界侧，低精度计算就可能足够。

### 题 8

问：MLWeaving 的 memory layout 解决什么问题？

答：解决同一份数据需要支持不同精度读取的问题。它按 bit-plane 组织数据，需要 1-bit 就读第一组 bit，需要 3-bit 就读前三组 bit，从而减少不必要内存流量。

### 题 9

问：Bit-serial multiplier 的核心思想是什么？

答：不一次处理完整数，而是按位读取 bit-serial 部分并与 bit-parallel 部分相乘累加。精度越低，读取和累加的位数越少，因此可节省计算和内存流量。

### 题 10

问：CPU 编程和 AI Accelerator 编程的主要差异是什么？

答：CPU 编程通常不显式管理数据在内存层级中的转移，cache 自动处理；AI Accelerator 编程常需要显式把数据从 DDR 搬到 Unified Buffer，计算后再搬回，性能高但编程难，因此依赖算子库。

---

## 14. 逐页学习索引

下面是按 slide 范围整理的学习索引。完整逐页抽取文本在后面的“逐页原文附录”中。

| 页码 | 内容 | 学习重点 |
|---|---|---|
| 1 | 深度学习加速器介绍 | 本讲主题 |
| 2-10 | cache coherence、MESI、directory、memory consistency | CPU 通用正确性机制很复杂 |
| 11-17 | 为什么需要深度学习处理器 | 应用广、能耗高、平台取舍 |
| 18-23 | 深度学习算子分析入口，VGG19 | 先分析目标应用再设计硬件 |
| 24-30 | 卷积层 | 卷积转矩阵乘，Burst+Stride |
| 31 | 激活函数 | 向量运算，Burst |
| 32-36 | 池化层 | 二维 reduce，Burst+Stride |
| 37-38 | 全连接层 | 矩阵乘向量 |
| 39-41 | Transformer Attention/FFN | 矩阵乘矩阵，Burst+Stride |
| 42-44 | 算子总结 | MAC、矩阵乘、固定访存模式 |
| 45-50 | DSA 和 CPU 功能 | 五个 DSA 思想 |
| 51-66 | 并行计算模块 | CPU 流水线/SIMD vs aggressive custom unit |
| 67-72 | 控制模块 | CPU 超标量 vs AI 加速器简单 issue |
| 73-97 | Global Buffer | 数据搬运能耗、cache 原理、buffer 取舍 |
| 98-131 | 低精度与 MLWeaving | 任意精度、bit-plane layout、BSM |
| 132-135 | 编程模式和总比较 | 显式 buffer 管理、专用语言 |
| 136 | 结束 | 复习总结 |

---

## 15. 关键词表

| 词 | 中文解释 | 本节课中的作用 |
|---|---|---|
| DSA | 领域专用体系结构 | AI 加速器总体设计范式 |
| MAC | Multiply-Accumulate，乘加 | 深度学习核心计算 |
| Burst | 连续突发访问 | 常见高效访存模式 |
| Stride | 固定步长跳跃访问 | 卷积/池化/Attention 中常见 |
| SIMD | 单指令多数据 | CPU 的向量并行方式 |
| Superscalar | 超标量 | CPU 挖掘指令间并行 |
| Global Buffer | 全局/统一片上缓冲 | AI 加速器替代复杂 cache 的关键 |
| Scratchpad Memory | 显式管理片上存储 | Global Buffer 的典型形式 |
| Quantization | 量化 | 用更低位宽表示数据和计算 |
| INT8/FP16/FP8 | 低精度数值格式 | 提高吞吐和能效 |
| MLWeaving | 任意精度数据布局方案 | 按 bit-plane 支持不同精度读取 |
| BSM | Bit-Serial Multiplier | 支持逐位任意精度计算 |
| DMA | Direct Memory Access | AI 编程中显式数据搬运 |
| Unified Buffer | 统一片上 buffer | DaVinci/AI Core 中放临时数据 |
| Cube Unit | 矩阵/张量计算单元 | 负责高吞吐矩阵计算 |
| MTE | Memory Transfer Engine | 数据搬运模块 |

---

## 16. 一句话总复习

深度学习加速器的本质，是利用深度学习算子“计算模式固定、矩阵乘占比高、访存规律明显、低精度可接受”的特点，牺牲 CPU 式通用性和透明编程，换取更多矩阵计算单元、更简单控制、更高效片上 buffer、更低精度计算和更高吞吐/能效。

---

## 17. 逐页原文附录

这一部分从 `extracted/11--accelerator_motivation.json` 自动生成，用于逐页核对 PPT 中的文字、表格和备注。正文讲解已按逻辑重组；如果你要检查某一页是否遗漏，优先看这里。
"""


def table_to_markdown(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    lines = []
    header = [cell.replace("\n", "<br>") for cell in padded[0]]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * width) + " |")
    for row in padded[1:]:
        cells = [cell.replace("\n", "<br>") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def slide_body(slide: dict) -> str:
    lines: list[str] = []
    lines.append(f"### Slide {slide['number']}: {slide['title']}")
    lines.append("")
    lines.append(f"- 图片数量：{slide['image_count']}")
    lines.append(f"- 表格数量：{slide['table_count']}")
    lines.append("")

    if slide.get("shape_items"):
        lines.append("**页面文字/表格：**")
        lines.append("")
        for item in slide["shape_items"]:
            if isinstance(item, str):
                for para in item.splitlines():
                    para = para.strip()
                    if para:
                        lines.append(f"- {para}")
            elif isinstance(item, dict) and "table" in item:
                lines.append("")
                lines.append(table_to_markdown(item["table"]))
                lines.append("")
        lines.append("")

    if slide.get("notes_text"):
        lines.append("**Speaker notes：**")
        lines.append("")
        for note in slide["notes_text"]:
            for para in str(note).splitlines():
                para = para.strip()
                if para:
                    lines.append(f"- {para}")
        lines.append("")
    return "\n".join(lines)


def build() -> None:
    data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    parts = [MANUAL.rstrip(), ""]
    for slide in data["slides"]:
        parts.append(slide_body(slide))
    OUTPUT.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
    print(OUTPUT)
