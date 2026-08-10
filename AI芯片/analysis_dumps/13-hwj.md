# 13-hwj-cann-mindspore.pptx selected slides

## Slide 13: AI Chips
- AI Chips
- TPU
- Ascend
- Cambricon

## Slide 14: Cambricon
- Cambricon
- Cambricon tries to solve two main problems:
- How to increase performance/power ratio?
- How to increase programmability?
- Goal of Cambricon:
- Design high performance/power ratio, high programmability deep learning accelerator.

## Slide 15: Cambricon AI Accelerator
- Cambricon AI Accelerator
- 单核深度学习处理器
- 多核深度学习处理器
- 整体架构
- 数据流
- 指令集
- 整体架构
- Cluster架构
Notes:
- 跟别的
- AI
- 加速器比较类似，没本质区别
- 15

## Slide 16: Cambricon AI Accelerator DLP-S
- Cambricon AI Accelerator DLP-S
- 控制模块
- 指令的语义粒度（提供专用指令，操作粒度为tensor）
- 领域专用指令 vs. RISC vs. CISC
- 运算模块
- 基于tensor语义设计运算模块
- 存储模块
- 基于tensor语义设计存储模块

## Slide 17: Overall Architecture of DLP-S
- Overall Architecture of DLP-S
- Control Module
- IFU (Instruction Fetch Unit)
- IDU (Instruction Decode Unit)
- Compute Unit
- VFU (Vector Function Unit)
- MFU (Matrix Function Unit)
- SRAM Unit
- WRAM (Weight RAM)
- NRAM (Neuron RAM)
- DMA (Direct Memory Access)

## Slide 18: Cambricon AI Accelerator DLP-S
- Cambricon AI Accelerator DLP-S
- DLP-S
- Control Module
- Compute Unit
- SRAM Unit

## Slide 19: Control Module of DLP-S
- Control Module of DLP-S
- Control Module
- Simple control
- Register Renaming

## Slide 20: Instruction Fetch Unit
- Instruction Fetch Unit
- IFU
- Address Generator Unit
- Instruction Cache
- Refill Buffer
- Instruction Queue
- Refill Buffer

## Slide 21: Instruction Decode Unit
- Instruction Decode Unit
- IDU (Instruction Decode Unit)
- Decoder
- ALU
- Issue Queue
- Control IQ, Compute IQ, Memory IQ

## Slide 22: Instruction Issue Queue
- Instruction Issue Queue
- Instruction Issue Queue
- Between queue: Out of order, inserting SYNC instructions between instruction queues
- In queue: in order

## Slide 23: Compute Module of DLP-S
- Compute Module of DLP-S
- Compute Module
- Matrix instruction
- Vector instruction
- Quantization

## Slide 24: SRAM Module of DLP-S
- SRAM Module of DLP-S
- SRAM Module
- Separate management for performance and efficiency
- Access via DMA

## Slide 25: Cambricon AI Accelerator
- Cambricon AI Accelerator
- 单核深度学习处理器
- 多核深度学习处理器
- 整体架构
- 数据流
- 指令集
- 整体架构
- Cluster架构

## Slide 26: Overall Execution Flow
- Overall Execution Flow
- 控制
- 神经元
- 权重
- 神经元tensor数据流
- DRAM->NRAM->VFU->（MFU->VFU->）NRAM->DRAM
- 权值tensor数据流
- DRAM->WRAM->MFU

## Slide 27: Execution Flow: Step 1
- Execution Flow: Step 1
- Step #1：IFU 通过 DMA 从 DRAM 中读取程序指令，然后经过 IDU 进行译码后分发给DMA、VFU 和 MFU
- 控制

## Slide 28: Execution Flow: Step 2
- Execution Flow: Step 2
- Step #2： DMA 接收到访存指令（读tensor指令，包括地址，数据量等信息），从 DRAM 读取神经元tensor至 NRAM，读取权值tensor至 WRAM。
- 控制
- 神经元
- 权重

## Slide 29: Execution Flow: Step 3
- Execution Flow: Step 3
- Step #3：VFU 接收到指令后从 NRAM 中读取神经元tensor，并对神经元tensor进行预处理（如边界扩充等），然后发送给 MFU。
- 控制
- 神经元
- 权重

## Slide 30: Execution Flow: Step 4
- Execution Flow: Step 4
- Step #4： MFU 接收到指令后从 VFU 接收经过预处理的神经元tensor，并从 WRAM 中读取权重tensor，完成矩阵运算后将结果发送给 VFU。
- 控制
- 神经元
- 权重

## Slide 31: Execution Flow: Step 5
- Execution Flow: Step 5
- Step #5： VFU 对输出神经元tensor进行后处理（如激活、池化等） 。
- 控制
- 神经元
- 权重

## Slide 32: Execution Flow: Step 6
- Execution Flow: Step 6
- Step #6： VFU 将运算结果tensor写回NRAM。
- 控制
- 神经元
- 权重

## Slide 33: Execution Flow: Step 7
- Execution Flow: Step 7
- Step #7： DMA 将输出神经元tensor从 NRAM 写回到 DRAM。
- 控制
- 神经元
- 权重

## Slide 34: Cambricon AI Accelerator
- Cambricon AI Accelerator
- 单核深度学习处理器
- 多核深度学习处理器
- 整体架构
- 数据流
- 指令集
- 整体架构
- Cluster架构
Notes:
- Risc
- 核可以考虑实现
- scalar+vector+matrix
- 。。。
- 34

## Slide 35: DLP ISA
- DLP ISA

## Slide 36: Control ISA
- Control ISA
- Control instruction
- JUMP：立即跳转指令
- CB：条件分支指令

## Slide 37: Data Movement ISA
- Data Movement ISA
- Data Movement instruction
- Load/Store指令：主存和片上存储交互
- MLOAD/MSTORE：矩阵数据（变长）
- VLOAD/VSTORE：向量数据（变长）
- SLOAD/SSTORE：标量数据
- MOVE指令：片上数据传输
- MMOVE，VMOVE，SMOVE

## Slide 38: Compute ISA
- Compute ISA
- 计算指令
- 矩阵运算：
- MMV，VMM，MMS，OP（外积），MAM，MSM
- 向量运算：
- VAV，VSV，VMV，VDV，VEXP（向量指数），VLOG（向量对数），IP（内积），RV（随机向量生成），VMAX/VMIN（向量最值）
- 标量运算：
- 加减乘除基本运算，标量超越函数
- MMV (Matrix-Multiply-Vector):

## Slide 39: Logic ISA
- Logic ISA
- Logic ISA
- 向量逻辑：
- 比较（VGT，VE）
- 逻辑（VAND，VOR，VNOT）
- 最值归约VGTM
- 标量逻辑：
- 标量比较，标量逻辑运算
- 最值归约：Vout[i] = (Vin0[i] > Vin1[i])?Vin0[i] : Vin1[i]

## Slide 40: Cambricon AI Accelerator
- Cambricon AI Accelerator
- 单核深度学习处理器
- 多核深度学习处理器
- 整体架构
- 数据流
- 指令集
- 整体架构
- Cluster架构

## Slide 41: DLP-M总体架构
- DLP-M总体架构
- 多核处理器分层结构设计
- 一个DLP-M由多个DLP-C构成
- 一个DLP-C由多个DLP-S构成
- DLP-M
- DLP-C
- 为什么需要进行分层结构设计?
- 减少NoC的负载核开销

## Slide 42: Cambricon AI Accelerator
- Cambricon AI Accelerator
- 单核深度学习处理器
- 多核深度学习处理器
- 整体架构
- 数据流
- 指令集
- 整体架构
- Cluster架构
Notes:
- DLP-M: deep learning processor-multi-core
- DLP-S: deep learning processor-single-core
- DLP-C: deep learning processor-cluster
- 42

## Slide 43: DLP-C总体架构
- DLP-C总体架构
- DLP-C整体架构：
- 四个DLP-S
- 存储核MEMCORE（Memory Core）
- 存储SMEM：DLP-S共享数据
- 通信：
- GDMA: DLP-C与片外DRAM
- CDMA: DLP-C之间，多个DLP-S之间

## Slide 44: Homogeneous Architecture
- Homogeneous Architecture
- (Huawei and Nvidia)
- vs.
- Heterogeneous architecture (Cambricon)?
Notes:
- 个人看好同构架构，好编程。。很重要。。。
- 44

## Slide 45: Recall: Huawei Acend 910
- Recall: Huawei Acend 910

## Slide 46: Recall: NVIDIA A100 (Homogeneous)
- Recall: NVIDIA A100 (Homogeneous)
- 108 cores on the A100
- (Up to 128 cores in the full-blown chip)
- 40MB L2 cache
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
Notes:
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

## Slide 47: Homogeneous Architecture
- Homogeneous Architecture
- (Huawei and Nvidia)
- vs.
- Heterogeneous architecture (Cambricon)?
Notes:
- 个人看好同构架构，好编程。。很重要。。。
- 47

## Slide 48: Where Are We?
- Where Are We?

## Slide 49: AI Architecture
- AI Architecture
- AscendXX…
- ？
- GPU

## Slide 50: AI Architecture
- AI Architecture
- AI Runtime
- AI Framework
- Parallel
- Training
- CANN*
- AI Chip
- 模型训练和推理框架
- Compute Architecture for Neural Network
- AI IP和芯片
- Ascend
- 计算加速库、芯片算子库和高度自动化的算子开发工具
- MindSpore
- TensorFlow
- PyTorch
- PaddlePaddle
- …
- Data parallel
- CUDA*
- Compute Unified Device Architecture
- Model parallel
- Pipeline parallel
- Hybrid parallel
Notes:
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

## Slide 51: Compute Architecture for Neural Network (CANN)
- Compute Architecture for Neural Network (CANN)
Notes:
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

## Slide 52: Compute Architecture for Neural Network (CANN)
- Compute Architecture for Neural Network (CANN)
Notes:
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

## Slide 53: Why NN Operator Library?
- Why NN Operator Library?
- Each layer in Caffe is an operator
- Each node in TensorFlow is an operator

## Slide 54: Difficulties of Developing NN Operator Library
- Difficulties of Developing NN Operator Library
- 功能逻辑
- 如何实现
- 如何适配
- 对应硬件
- 如何处理不同
- 类型的输入
- 如何处理不同
- 大小的输入
- 如何保证算子
- 运行的性能
- 不同AI芯片

## Slide 55: Why NN Operator Library?
- Why NN Operator Library?
- The motivation of NN operator library:
- 1, NN tasks are composed of NN operators
- 2, AI chips are difficult to program, we cannot let AI programmer directly program AI chips
- The goal of NN operator library:
- Performance + Usability: provide high-performance, well-documented NN library for the upper AI framework such as MindSpore.

## Slide 56: Ascend NN Operator Library
- Ascend NN Operator Library
- 昇腾算子库包含了丰富的高性能算子：
- NN（Neural Network）算子库：覆盖了包括TensorFlow、Pytorch、MindSpore、ONNX等框架的常用深度学习算法的计算类型，在算子库中占有最大比重。
- BLAS（Basic Linear Algebra Subprograms）算子库：基础线性代数程序集，是进行向量和矩阵等基本线性代数操作的数值库。
- DVPP（Digital Video Pre-Processor）算子库：提供高性能的视频编解码、图片编解码、图像裁剪缩放等预处理能力。
- AIPP（AI Pre-Processing）算子库：主要实现改变图像尺寸、色域转换（转换图像格式）、减均值/乘系数（图像归一化），并与模型推理过程融合，以满足推理输入要求。
- HCCL（Huawei Collective Communication Library）算子库：提供单机多卡以及多机多卡间的Broadcast，allreduce，reducescatter，allgather等集合通信功能，在分布式训练中提供高效的数据传输能力。

## Slide 57: 算子基本概念-总揽
- 算子基本概念-总揽
- 算子名称（Name）
- 算子的名称，用于标志网络中的某个算子，同一网络中算子的名称需要保持唯一。如右图所示Conv1，Pool1，Conv2都是此网络中的算子名称，其中Conv1与Conv2算子的类型为Convolution，表示分别做一次卷积运算。
- 算子类型（Type）
- 网络中每一个算子根据算子类型进行算子实现的匹配，相同类型的算子的实现逻辑相同。在一个网络中同一类型的算子可能存在多个，例如右图中名称为Conv1的算子与Conv2算子的类型都为Convolution。
- Conv1
- 输入数据
- 输出数据
- 数据容器（Tensor）
- 张量（Tensor）是承载算子数据的容器。如右图所示，算子在网络中执行时，输入数据是一个tensor，算子执行完后，输出数据也是一个tensor。

## Slide 58: 算子基本概念-Tensor
- 算子基本概念-Tensor
- TABLE:
  | 属性 | 定义 |
  | 名称（name） | 用于对Tensor进行索引，不同Tensor的name需保持唯一。 |
  | 形状（shape） | Tensor的形状，比如（10,）或者（1024, 1024）或者（2, 3, 4）等。
形式：(i1, i2,…in)，其中i1到in均为正整数 |
  | 数据类型（dtype） | 指定Tensor对象的数据类型。
例如：float16, float32, int8, int16, int32, uint8, uint16, bool等。
不同计算操作支持的数据类型不同。 |
  | 数据排布格式（format） | 数据的物理排布格式，定义了解读数据的维度。 |
- 张量（Tensor）是存储算子输入数据与输出数据的容器，
- 而张量描述符（TensorDesc）是对输入数据与输出数据的描述，
- 张量描述符的数据结构包含如下属性：

## Slide 59: 算子基本概念-Tensor
- 算子基本概念-Tensor
- TABLE:
  | 张量 | 形状 |
  | 1 | (0,) |
  | [1,2,3] | (3,) |
  | [[1,2],[3,4]] | (2,2) |
  | [[[1,2],[3,4]], [[5,6],[7,8]]] | (2,2,2) |
- 形状（shape）
- 下面分别介绍张量描述符中的形状和数据排布格式。
- 1，张量的形状，以(D0, D1, … ,Dn-1)的形式表示，D0到Dn是任意的正整数。
- 如形状(3,4)表示第一维有3个元素，第二维有4个元素，是一个3行4列的矩阵数组。
- 2，在形状的小括号中有多少个数字，就代表这个张量是多少维的张量。
- 形状的第一个元素要看张量最外层的中括号中有几个元素，形状的第二个元素要看张量中从左边开始数第二个中括号中有几个元素，依此类推。

## Slide 60: 算子基本概念-Tensor
- 算子基本概念-Tensor
- produce A {
- for (i, 0, 4) {
- for (j, 0, 20) {
- for (p, 0, 20) {
- for (q, 0, 3) {
- A[((((((i*20) + j)*20) + p)*3) + q)] = a_tensor[((((((i*20) + j)*20) + p)*3) + q)]
- }
- }
- }
- }
- }
- shape=(4, 20, 20, 3)的物理含义:
- shape里4的含义：假设有4张照片
- shape里20,20的含义：每张照片的宽和高都是20，也就是20*20=400个像素,
- shape里面3的含义：每个像素点都由红/绿/蓝3色组成
- shape=(4, 20, 20, 3)的运算操作:
- 在编程上，可以把shape理解为操作Tensor的各层循环

## Slide 61: 算子基本概念-Tensor
- 算子基本概念-Tensor
- 数据排布格式（format）:
- 在深度学习领域，多维数据通过多维数组存储，比如卷积神经网络的特征图（Feature Map）通常用四维数组保存，即4D格式：
- N：Batch数量，例如图像的数目。
- H：Height，特征图高度，即垂直高度方向的像素个数。
- W：Width，特征图宽度，即水平宽度方向的像素个数。
- C：Channels，特征图通道，例如彩色RGB图像的Channels为3。
- 不同深度学习框架会按照不同的顺序存储特征图数据:
- Caffe的排列顺序为[Batch, Channels, Height, Width]即NCHW
- TensorFlow的排列顺序为[Batch, Height, Width, Channels] 即NHWC

## Slide 62: 算子基本概念-属性
- 算子基本概念-属性
- 权重（Weight）:
- 当输入数据进入计算单元时，会乘以一个权重。例如，如果一个算子有两个输入，则每个输入会分配一个关联权重，一般将认为较重要数据赋予较高的权重，不重要的数据赋予较小的权重，为零的权重则表示特定的特征是无需关注的。
- 如下图所示，假设输入数据为X1，与其相关联的权重为W1，那么在通过计算单元后，数据变为了X1*W1。

## Slide 63: 算子基本概念-属性
- 算子基本概念-属性
- 偏差（Bias）:
- 偏差是除了权重之外，另一个被应用于输入数据的线性分量。它被加到权重与输入数据相乘的结果中，用于改变权重与输入相乘所得结果的范围。
- 如下图所示，假设输入数据为X1，与其相关联的权重为W1，偏差为B1，那么在通过计算单元后，数据变为了X1*W1+B1

## Slide 64: CANN算子开发方式
- CANN算子开发方式
- TBE （Tensor Boost Engine）算子
- 运行在昇腾AI处理器的AI Core上，鉴于AI Core的强大算力，主要负责执行矩阵、向量、标量的计算密集型算子。
- TBE提供了基于张量虚拟机（Tensor Virtual Machine，TVM）框架的自定义算子开发能力，提供了用户开发自定义算子所需工具。
- AI CPU算子
- 运行在昇腾AI处理器的AI CPU上，主要负责执行不适合跑在AI Core上的算子，例如非矩阵类的复杂计算，逻辑比较复杂的分支密集型算子，或者算子需要某些数据类型，但AI Core不支持，此时可通过开发AI CPU算子实现昇腾AI处理器对此算子的支持。

## Slide 65: CANN算子开发方式-TBE
- CANN算子开发方式-TBE
- DSL（ Domain-Specific Language，基于特性域语言）
- DSL接口已高度封装，用户仅需要使用DSL接口完成计算过程的表达，后续的算子调度、算子优化及编译都可通过已有的接口一键式完成，适合初级开发用户。
- TIK（ Tensor Iterator Kernel， 张量嵌套内核）
- 开发者可以通过调用TIK提供的API基于Python语言编写自定义算子，然后TIK编译器会将其编译为适配昇腾AI处理器SoC应用程序的二进制文件。但TIK需要用户手工控制数据搬运和计算流程，入门较高，但开发方式比较灵活，在性能上有一定的优势。

## Slide 66: CANN算子开发方式比较
- CANN算子开发方式比较
- TABLE:
  | 参数 | TBE DSL方式 | TIK方式 | AI CPU方式 |
  | 语言 | Python | Python | C++ |
  | 计算单元 | AI Core | AI Core | AI CPU |
  | 运用场景 | 常用于各种算术逻辑简单向量运算，或内置支持的矩阵运算及池化运算 | 适用各类算子的开发，对于无法通过lambda表达描述的复杂计算场景也有很好的支持，例如排序类操作 | 某些场景下，无法通过AI Core实现的自定义算子，或者需要临时快速打通网络的场景下使用 |
  | 入门难度 | 较低 | 较高 | 中等 |
  | 适用人群 | 入门用户，需要了解NN、TBE DSL相关知识 | 高级用户，需要了解NN，深入理解昇腾AI处理器架构、指令集、数据搬运等相关知识 | 具备C++程序开发能力，对机器学习、深度学习、AI CPU开发流程有一定的了解 |
  | 特点 | TBE DSL接口已高度封装，用户仅需要使用DSL接口完成计算过程的表达，后续的Schedule创建、优化及编译都可通过已有接口一键式完成 | 入门难度高，程序员直接使用TIK提供的API完成计算过程的描述及Schedule过程，需要手工控制数据搬运的参数和Schedule。用户无须关注Buffer地址的分配及数据同步处理，由TIK工具进行管理 | 开发的流程和DSL都是类似的， 不需要了解AI Core的内部架构设计，入门较快 |
  | 不足 | 某些场景下性能可能较低，复杂算子逻辑无法支持表达 | 需要开发者手工控制数据搬运的参数和Schedule过程。 | 无封装的计算接口，计算过程相对繁琐，另外AI CPU性能较低。 |

## Slide 67: 昇腾CANN：向下使能处理器并行加速，向上使能高效开发
- 昇腾CANN：向下使能处理器并行加速，向上使能高效开发
- 全面支持业界AI框架，同步PyTorch社区版本发布
- AI框架
- 昇腾芯片
- 昇腾系列处理器 ......
- ......
- Ascend C 支持算子极简开发
- 支持GPU生态向NPU高效迁移
- CANN
- 图编译加速技术使能处理器并行加速
- 自动流水
- 算子深度融合
- 整图下沉
- 自适应梯度切分
- … …
- 周级迁移
- 保持AI框架不变，模型快速由GPU迁移至NPU运行
- 全流程工具链
- 适配扫描、精度调试、性能调优
- 支持Transformer架构融合算子高效开发
- GPU
- NPU
- 融合算子库
- FlashAttention等Transformer网络加速算子，多模型/多尺寸/多shape全面支持，精度、性能持平业界
- 符合开发者编程习惯
- 遵循C/C++标准规范
- 简化算子编程逻辑
- 结构化核函数编程
- 自动获取最优调度
- 自动化流水并行调度
- 使能大模型并行计算加速
- 发挥数学力量优化算子及算法，释放澎湃算力
- 1
- 全面开放，生态兼容
- 兼容业界主流框架
- 3
- 高效原生开发与生态迁移
- 典型场景算子开发周期 <2人周
- 2

## Slide 68: 编程范式—— SPMD模型（类CUDA）
- 编程范式—— SPMD模型（类CUDA）
- Ascend C算子编程是SPMD的编程，将需要处理的数据拆分并分布在多个计算核心上运行
- 多个AI Core共享相同的指令代码，每个核上的运行实例唯一的区别是block_idx不同
- block的类似于进程，block_idx就是标识进程唯一性的进程ID，编程中使用函数GetBlockIdx()获取ID
- 昇腾AI处理器SPMD并行计算示意图
- SPMD数据并行示意图

## Slide 69: Motivation of In-network Computing
- Motivation of In-network Computing
- 算子的输入输出都是tensor，tensor在哪里？
- Device memory

## Slide 70: Compute Architecture for Neural Network (CANN)
- Compute Architecture for Neural Network (CANN)
Notes:
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

## Slide 71: CANN平台 —— 计算图引擎GE
- CANN平台 —— 计算图引擎GE
- GE的核心功能组件：
- 图准备：全局优化，完成shape推导，维测类算子并行拆分
- 图拆分：引擎子图切分&边界连接
- 图优化：引擎/部件级优化，权值格式转换，图聚合（allreduce）
- 图编译：资源分配和Task生成
- 图加载：将Task加载到Runtime上
- 图执行：在Runtime上运行Task
- MindSpore
Notes:
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
- 71

## Slide 72: 计算图引擎GE—例子
- 计算图引擎GE—例子
- 下边我们将以右侧的MindSpore编写的构建Lenet5的简单代码为入口（见左图），探究异构计算架构对计算图都做了哪些动作。
- Lenet5
Notes:
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

## Slide 73: 图准备阶段——计算图的构建
- 图准备阶段——计算图的构建
- Lenet5
- x
- conv1
- relu
- max_pool2d
- conv2
- relu
- max_pool2d
- flatten
- fc1
- relu
- fc2
- relu
- fc3
- output
Notes:
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

## Slide 74: 初阶图优化-CSE
- 初阶图优化-CSE
- +
- *
- *
- +
- B
- C
- D
- B
- C
- E
- +
- +
- *
- *
- +
- B
- C
- D
- E
- w
- w
Notes:
- CSE
- （
- Common-Subexpression Elimination
- ），公共子表达式消除。
- 简单而言就是将相同输入的表达式进行消除，复用计算结果。
- 74

## Slide 75: 图优化-算子融合（Intuition）
- 图优化-算子融合（Intuition）
- Data
- Conv2D
- BatchNorm
- Relu
- Data
- Conv2D_BatchNorm_Relu
- 算子执行的访存特性：
- ConvD：顺序写
- BatchNorm：顺序读写
- ReLU：顺序读写
- 算子特性：
- 每个算子都从内存读数
- 计算完成放回内存
Notes:
- Reducing high-cost operations: global memory access
- 75

## Slide 76: Recall: Comparison of Memories
- Recall: Comparison of Memories
- SRAM
- HBM
- DRAM
- SSD
- DISK
- Capacity
- SRAM
- HBM
- DRAM
- SSD
- DISK
- Latency
- Bandwidth
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DRAM
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 77: 图优化-算子融合（UB融合）
- 图优化-算子融合（UB融合）
- NPU
- Vector
- Unified Buffer
- Main Memory
- 以一个简单的Vector算子计算为例，其计算过程通常包含以下几个步骤：
- 计算任务和数据在片上的上下文切换
- 新的算子所需数据从主存搬运到Unified Buffer（以下简称UB）
- Vector读取UB中的数据进行计算，并将结果存回UB
- 计算结果从UB搬出到主存
Notes:
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 77

## Slide 78: 图优化-算子融合（UB融合）
- 图优化-算子融合（UB融合）
- Key Idea of UB融合：泛指片上缓存级别的融合，即数据搬进芯片后，下发的算子计算任务是由多个小算子融合而成的大算子。
- UB融合具体计算步骤：
- 计算任务和数据在片上的上下文切换
- 新的算子所需数据从主存搬运到Unified Buffer（以下简称UB）
- Vector读取UB中的数据进行算子1计算，并将结果存回UB
- Vector读取UB中的数据进行算子2计算，并将结果存回UB
- Vector读取UB中的数据进行算子3计算，并将结果存回UB
- 计算结果从UB搬出到主存
Notes:
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 78

## Slide 79: 算子融合-PyTorch版Attention
- 算子融合-PyTorch版Attention
Notes:
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 79

## Slide 80: 算子融合-计算复杂度 vs 内存复杂度
- 算子融合-计算复杂度 vs 内存复杂度
- 计算复杂度 (O(S²D))
- 标准 Attention 的理论计算量（主要是矩阵乘法）与序列长度平方 (S²)和隐藏维度 (D)成正比。FlashAttention 并未改变这一理论复杂度，依然需要计算所有 Q-K 对的相似度。
- 内存复杂度 (O(S²))
- 直接实现时，存储 Score 和 Probability 中间矩阵所需显存与序列长度平方 (S²)成正比。随着序列变长，巨大的矩阵读写会迅速耗尽显存带宽，导致性能瓶颈。
- FlashAttention 的策略
- 通过分块 (Tiling)和重新组织计算流程，避免将完整 S×S 矩阵写入高带宽内存(HBM)。用少量额外的计算量换取大量的内存读写优化，实现显著加速。
- 💡 核心区别与洞察
- 计算复杂度关注“运算次数”，而内存复杂度关注“数据搬运的量”。在现代 GPU 架构下，内存带宽（数据搬运）往往比算力更早成为瓶颈。FlashAttention 正是抓住了这一点，通过“以计算换内存”的思路，解决了长序列 Attention 的落地难题。
Notes:
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 80

## Slide 81: Where Are We?
- Where Are We?

## Slide 82: AI Architecture
- AI Architecture
- AI Runtime
- AI Framework
- Parallel
- Training
- CANN*
- AI Chip
- 模型训练和推理框架
- Compute Architecture for Neural Network
- AI IP和芯片
- Ascend
- 计算加速库、芯片算子库和高度自动化的算子开发工具
- MindSpore
- TensorFlow
- PyTorch
- PaddlePaddle
- …
- Data parallel
- CUDA*
- Compute Unified Device Architecture
- Model parallel
- Pipeline parallel
- Hybrid parallel
Notes:
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

## Slide 83: Why AI Framework?
- Why AI Framework?
- Reasons:
- AI algorithms are gaining great attention.
- More and more companies and programmers are using them.

## Slide 84: Why AI Framework?
- Why AI Framework?
- Two Properties of AI tasks:
- AI tasks are varying, but built on common operators.
- Implementation complexity is high
- 有必要将算法中的常用操作封装成组件提供给程序员，以提高深度学习算法开发效率和性能。

## Slide 85: MindSpore逻辑架构
- MindSpore逻辑架构
- MindSpore Extend
- GNN/深度概率编程/强化学习/微分方程
- Mind
- Armour
- Model Zoo
- MindData
- MindRT
- MindRT(分布式DAG并行执行)
- MindRT Lite/Micro
- MindCompiler
- MindIR
- 量化/剪枝/….
- MindAKG(算子自动生成)
- 仓颉
- 前端
- 图算融合
- 内存优化
- 流水线执行
- 自动微分
- 类型推导
- 自动并行
- 二阶优化
- MindExpression
- 硬件相关优化
- 密态AI
- 可信AI
- Mind
- Insight
- 网络调试
- 精度调优
- 性能调优
- CANN昇腾
- CUDA
- Eigen
- Android
- iOS
- 自动并行：整图切分，感知集群拓扑，实现通信开销最小，融合数据并行与模型并行；
- 二阶优化：利用二阶计算修正梯度更新方向，找到训练梯度最优下降路径，从而加速训练收敛过程；
- 动静态图结合：统一自动微分引擎支持动静态图，一行代码完成模式切换，兼顾模型开发和执行效率；
- AI+科学计算，场景应用创新，拓展MindSpore的边界

## Slide 86: 关键技术：自动并行
- 关键技术：自动并行
- 算法科学家需要训练大模型：
- 需求：超大模型与超大数据集的分布式训练，需通过数据并行+模型并行的混合并行方式，才能高效训练网络。
- 挑战：
- 传统graph-level模型切分，计算资源利用率不高，需通过operator-level模型切分提高并行加速比；选择一种高效的模型切分方式需要专家经验；
- 混合并行复杂度高，传统API难以编写混合并行代码，算法与并行逻辑耦合，修改并行策略，就要重新修改编码；
- 算法科学家需要关注系统（集群拓扑、网络带宽等）和并行的实现细节，才能写出高性能算法。

## Slide 87: 关键技术2：二阶优化
- 关键技术2：二阶优化
- 学习率
- 二阶信息矩阵
- 一阶梯度
- 参数
- 二阶矩阵近似表达
- 二阶矩阵降频
- 二阶矩阵降维
- 软硬协同
- 高性能算子加速
- 方案
- 二阶矩阵近似表达
- 二阶矩阵降频
- 二阶矩阵降维

## Slide 88: 关键技术3：动静态图结合
- 关键技术3：动静态图结合
- 统一的自动微分引擎
- 动态图
- 调试+调优
- 静态图
- 执行+部署
- set_context
- 统一的自动微分引擎，保证动态图和静态图语法一致
- TABLE:
  | @ms_function
 def sub_net(self, x):
 x = self.conv(x)
 return x

 def construct(self, x):
 x = self.sub_net(x)
 x = self.relu(x)
 return x |
- 灵活切换：一行代码完成动静态图模式切换
- TABLE:
  | #切换为动态图模式
context.set_context(mode=contex.PYNATIVE_MODE)
#切换为静态图模式
context.set_context(mode=contex.GRAPH_MODE) |
- 调试通过的代码
- 静态图模式执行
- 待调试的代码
- 动态图模式执行

## Slide 89: 关键技术4：AI+科学计算
- 关键技术4：AI+科学计算
- 科学计算近况：
- 科学计算核心问题是微分方程求解，算力消耗巨大，大规模求解器垄断历年戈登贝尔奖，近年来结合AI方法成为趋势。
- 业界AI+科学计算现状：
- TF：众筹方式构建AI求解模型，典型应用领域取得突破；面向DNN设计的自动微分，计算高阶微分时效率低下；
- Nvidia：支持高精度计算；构筑cuBLAS、cuFFT等基础数学库；上层框架依赖TensorFlow，继承TF缺点
- 非线性拟合，无需解高维方程
- 神经网络模拟，不需要处理边界条件
- AI方法求解
- 高维微分方程求解，计算量大
- 边界条件复杂，求解不稳定
- 传统数值方法
Notes:
- 科学计算才是
- AI
- 应用的蓝海。。。
- 89

## Slide 90: 关键技术4：AI+科学计算
- 关键技术4：AI+科学计算
- 异构硬件
- 通用（稀疏）张量代数计算加速
- 电磁仿真
- 气象
- 分子动力学
- …
- 大规模高维微分方程AI求解器
- 应用场景
- AI建模
- AI求解
- 框架加速
- MindCompiler
- 自动微分
- 1
- 2
- 3
- MindSpore
- 台风灾害预警
- 40小时
- 分钟级
- 台风公里级风速预报
- 手机电磁场模拟
- 10小时
- 1小时
Notes:
- 大规模高维微分方程
- AI
- 求解器
- ：
- 建模加速材料、气象等领域；
- 求解加速麦克斯韦电磁方程、
- Burgers
- 等，性能提升
- 10
- 倍
- ；
- 框架加速支持海洋
- GOMO
- 模型，性能提升
- 1.5
- 。
- 自动微分
- ：前向自动微分、混合自动微分、向量化自动微等，性能提升
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
- 90

## Slide 91: Cerebras’s Wafer Scale Engine (2019)
- Cerebras’s Wafer Scale Engine (2019)
- Cerebras WSE
- 1.2 Trillion transistors
- 46,225 mm2
- Largest GPU
- 21.1 Billion transistors
- 815 mm2
- The largest ML accelerator chip
- 400,000 cores
- 18 GB of on-chip memory
- 9 PB/s memory bandwidth
- NVIDIA TITAN V
- https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning
- https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/
Notes:
- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 91

## Slide 92: Scratchpad Memory in Cerebras WSE
- Scratchpad Memory in Cerebras WSE
- Scratchpad Memory
- Highly parallel and distributed scratchpad SRAM memory with 2D mesh interconnection fabric across tiles
- 16-byte read and 8-byte write single-cycle latency
- 48 KB scratchpad in each tile, totaling 18 GB on the full chip
- No shared memory
- Rocki et al., “Fast stencil-code computation on a wafer-scale processor.” SC 2020.
- 84 dies
- 4539 tiles
Notes:
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

## Slide 93: Cerebras’s Wafer Scale Engine-2 (2021)
- Cerebras’s Wafer Scale Engine-2 (2021)
- Cerebras WSE-2
- 2.6 Trillion transistors
- 46,225 mm2
- Largest GPU
- 54.2 Billion transistors
- 826 mm2
- NVIDIA Ampere GA100
- https://cerebras.net/product/#overview
- The largest ML accelerator chip
- 850,000 cores
- 40 GB of on-chip memory
- 20 PB/s memory bandwidth
Notes:
- 93