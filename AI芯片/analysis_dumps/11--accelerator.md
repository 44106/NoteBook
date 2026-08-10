# 11--accelerator_motivation.pptx selected slides

## Slide 13: 为啥需要AI加速器?
- 为啥需要AI加速器?
- ?
Notes:
- 现在大家都在讨论
- Ai
- for
- 任意应用，如金融，医疗，数据库等等
- 那我们能不能反过来想想这个事，别的技术也用于
- AI
- 呢？事实上这个也很有必要，
- 13

## Slide 14: 为什么需要深度学习处理器?
- 为什么需要深度学习处理器?
- 深度学习应用广泛(市场大)
- AI for X: 图像识别、语音处理、自然语言处理
- 平台：已渗透到云服务器和智能手机
- 通用CPU/GPU处理人工神经网络效率低下(费电)
- 谷歌大脑：1.6万个CPU核跑数天完成猫脸识别训练
- AlphaGo：和李世石下棋用了1202个CPU和176个GPU
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 14

## Slide 15: 处理器&性能指标
- 处理器&性能指标
- CPU: Central Processing Unit (一个大学生)
- GPU: Graphics Processing Unit (100个小学生)
- DL Accelerator: Deep Learning Accelerator (一个偏科生)
- 延时: AI模型做出决定的时间。
- 通用性: 适合运行的应用程序范围。
- 能效: 单位能量所支持的计算量。
- 可迭代性: AI模型变化时的硬件适应能力。
Notes:
- 15

## Slide 16: 不同计算平台：能效 vs. 通用性
- 不同计算平台：能效 vs. 通用性
- ASICs
- 通用性
- 能效
- CPU
- 深度学习处理器
- GPU
- FPGA
- 好
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 16

## Slide 17: 不同计算平台：延时 vs. 可迭代性
- 不同计算平台：延时 vs. 可迭代性
- ASICs
- 可迭代性
- 延时
- CPU
- 深度学习处理器
- GPU
- FPGA
- 好
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 17

## Slide 18: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- Conv
- Activation
- Pooling
- Fully Connection
- Attention
- 深度学习加速器设计思路
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 18

## Slide 19: 在分析深度学习算法的时候，我们关心啥？
- 在分析深度学习算法的时候，我们关心啥？
- 在设计深度学习加速器的时候，
- 咋们先得搞清楚目标应用：深度学习算法。
- 两大特性！
Notes:
- 现在的计算世界往三个方向发展
- 19

## Slide 20: 深度学习算法分析
- 深度学习算法分析
- 计算特性
- 是否存在固定的、重复的计算模式？
- 访存特性
- 数据访问的局部性
- 数据访问和后续计算的关系（对于带宽的实际需求）
- 分析深度学习算法的两大特性:
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 20

## Slide 21: 典型卷积神经网络：VGG19
- 典型卷积神经网络：VGG19
- Conv: 卷积层
- Maxpool: 最大池化层
- FC: 全链接层
Notes:
- 21

## Slide 22: 典型卷积神经网络：VGG19
- 典型卷积神经网络：VGG19
- TABLE:
  | VGG19 |  |
  | 参数 | 1.14 （亿） |
  | 层类型 | 卷积，池化，全连接 |
  | 计算过程 | 简洁 |
  |  |  |
  | 层数 | 25（16+5+3+1) |
  | 卷积层 | 16（3x3卷积核，图大小不变） |
  | 池化层 | 5（Max Pooling） |
  | 全连接层 | 3 |
  | SoftMax | 1 |
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 22

## Slide 23: 目录
- 目录
- 为什么需要深度学习处理器
- 通用处理器CPU的工作原理与特性
- 深度学习算子分析
- Conv
- Activation
- Pooling
- Fully Connection
- 深度学习加速器设计思路
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 23

## Slide 24: 卷积层
- 卷积层
- 3
- 32
- 32
- 28
- 28
- 1
- 32x32x3图像
- 5x5x3 Filter
- 3
- 5
- 5
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 24

## Slide 25: 卷积层
- 卷积层
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- X
- +1
- -1
- -1
- +1
- Image
- +
- +
- -
- -
- 4
- (1, -1, -1, 1)
- 1
- -1
- -1
- 1
- =
- 4
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 25

## Slide 26: 卷积层
- 卷积层
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- X
- +1
- -1
- -1
- +1
- Image
- +
- +
- -
- -
- 4
- (-1, 1, 1 , -1)
- 1
- -1
- -1
- 1
- =
- -4
- -4
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 26

## Slide 27: 卷积层
- 卷积层
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- X
- +1
- -1
- -1
- +1
- Image
- +
- +
- -
- -
- 4
- (-1, 1, 1 , -1)
- 1
- -1
- -1
- 1
- =
- -4
- -4
- -4
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 27

## Slide 28: 卷积层
- 卷积层
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- -1
- 1
- X
- +1
- -1
- -1
- +1
- Image
- +
- +
- -
- -
- 4
- (1, -1, -1 , 1)
- 1
- -1
- -1
- 1
- =
- 4
- -4
- -4
- 4
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 28

## Slide 29: 卷积层
- 卷积层
- 3 channels下的卷积计算:
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 29

## Slide 30: 卷积层计算和访存特性
- 卷积层计算和访存特性
- 处理后的数据
- 1, -1, -1 , 1
- 1
- -1
- -1
- 1
- =
- -1, 1, 1 , -1
- -1, 1, 1 , -1
- 1, -1, -1 , 1
- 4
- -4
- -4
- 4
- 1 Filter
- 计算特性: 矩阵乘向量
- 处理后的数据
- 1, -1, -1 , 1
- 1
- -1
- -1
- 1
- =
- -1, 1, 1 , -1
- -1, 1, 1 , -1
- 1, -1, -1 , 1
- 4,
- -4,
- -4,
- 4,
- 2 Filters
- 1
- -1
- -1
- 1
- -4
- 4
- 4
- -4
- 计算特性: 矩阵乘矩阵
- 访存特性: Burst+Stride
- Burst: 突发传输访问， Stride: 跳着访问
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 30

## Slide 31: 激活函数的计算和访存特性
- 激活函数的计算和访存特性
- 计算特性: 向量运算
- 访存特性: Burst
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 31

## Slide 32: 池化层
- 池化层
- 3
- 5
- 2
- 6
- 2
- 5
- 5
- 7
- 6
- 4
- 8
- 4
- 1
- 9
- 5
- 8
- 2x2 Pooling
- stride=2
- Max Pooling
- Average Pooling
- 6
- 4
- Max Pooling = Max (3, 5, 6, 2) = 6
- Average Pooling = AVG (3, 5, 6, 2) = 4
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 32

## Slide 33: 池化层
- 池化层
- 3
- 5
- 2
- 6
- 2
- 5
- 5
- 7
- 6
- 4
- 8
- 4
- 1
- 9
- 5
- 8
- 2x2 Pooling
- stride=2
- Max Pooling
- Average Pooling
- 6
- 4
- 5
- 3
- Max Pooling = Max (2, 4, 5, 1) = 5
- Average Pooling = AVG (2, 4, 5, 1) = 3
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 33

## Slide 34: 池化层
- 池化层
- 3
- 5
- 2
- 6
- 2
- 5
- 5
- 7
- 6
- 4
- 8
- 4
- 1
- 9
- 5
- 8
- 2x2 Pooling
- stride=2
- Max Pooling
- Average Pooling
- 6
- 4
- 5
- 3
- 8
- 6
- Max Pooling = Max (5, 7, 8, 4) = 8
- Average Pooling = AVG (5, 7, 8, 4) = 6
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 34

## Slide 35: 池化层
- 池化层
- 3
- 5
- 2
- 6
- 2
- 5
- 5
- 7
- 6
- 4
- 8
- 4
- 1
- 9
- 5
- 8
- 2x2 Pooling
- stride=2
- Max Pooling
- Average Pooling
- 6
- 4
- 5
- 3
- 8
- 6
- 9
- 7
- Max Pooling = Max (6, 8, 9, 5) = 9
- Average Pooling = AVG (6, 8, 9, 5) = 7
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 35

## Slide 36: 池化层计算和访存特性
- 池化层计算和访存特性
- 处理后的数据
- 3, 5, 6, 2
- 6
- 5
- 8
- 9
- Max
- 计算特性: 二维空间上reduce
- 2, 4, 5, 1
- 5, 7, 8, 4
- 6, 8, 9, 5
- =
- 4
- 3
- 6
- 7
- Avg
- 访存特性: Burst+Stride
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 36

## Slide 37: 全连接层
- 全连接层
- Flatten
- Fully Connected
- Flatten: 把output map摊平，用于输入全连接层。
- Fully Connection: 把output map摊平，用于输入全连接层。
- Input
- Output
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 37

## Slide 38: 全连接层的计算和访存特性
- 全连接层的计算和访存特性
- *Source from Feifei Li CS231N (http://cs231n.stanford.edu/slides/2018/cs231n_2018_lecture05.pdf)
- 输入：x
- 输出：y
- 计算特性: 矩阵乘向量
- 访存特性: Burst+Stride
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 38

## Slide 39: Introduction to Transformer
- Introduction to Transformer
- *Source from Feifei Li CS231N (http://cs231n.stanford.edu/slides/2018/cs231n_2018_lecture05.pdf)
- 1.
- Tokenization
- 2. Input
- Layer
- 3.
- Attention
- 4. Feed
- Forward
- 5. Output
- Layer
- Transformer Block
- X N
- Token
- Output
- Text2Token
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 39

## Slide 40: Attention
- Attention
- Q
- (HxH)
- K
- (HxH)
- V
- (HxH)
- a
- (SxH)
- Qa
- (SxH)
- Ka
- (SxH)
- Va
- (SxH)
- A
- (SxS)
- dot
- L1
- (HxH)
- dot
- Atten
- (SxH)
- Ao
- (SxH)
- 计算特性: 矩阵乘矩阵
- 访存特性: Burst+Stride
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 40

## Slide 41: Feed Forward
- Feed Forward
- L2
- (Hx4H)
- L3
- (Hx4H)
- Ao
- (SxH)
- F1
- (Sx4H)
- Fo
- (SxH)
- 计算特性: 矩阵乘矩阵
- 访存特性: Burst+Stride
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 41

## Slide 42: 目录
- 目录
- 为什么需要深度学习处理器
- 通用处理器CPU的工作原理与特性
- 深度学习算子分析
- 深度学习加速器设计思路
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 42

## Slide 43: 深度学习算法计算和访存特性分析
- 深度学习算法计算和访存特性分析
- MAC (Multiply–Accumulate)
- TABLE:
  | Operator | 计算特性 | 访存特性 |
  | Conv | 矩阵相乘 | Burst+stride |
  | Activation | 单向量操作 | Burst |
  | Pooling | 单矩阵Reduce操作 | Burst+stride |
  | FC | 矩阵相乘 | Burst |
- Fixed Memory Access Pattern
- 计算特性：矩阵乘法计算量的占比高于90%。
- TABLE:
  | Attention | 矩阵相乘 | Burst+stride |
- 访存特性：Burst + Stride
Notes:
- 43

## Slide 44: 1，矩阵、向量乘法
- 1，矩阵、向量乘法
- 2，固定的内存访问方式
- 那怎么设计深度学习加速器呢？
- 类似考前划重点！
Notes:
- 现在的计算世界往三个方向发展
- 44

## Slide 45: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 45

## Slide 46: 深度学习加速器: DSA (Domain Specific Architecture)
- 深度学习加速器: DSA (Domain Specific Architecture)
- 5个DSA设计思想:
- Global Buffer: 使用专有的存储器来减少数据搬运的距离与开销，比如将复杂的cache设计替换成scratchpad memory (global buffer)。
- 简化控制模块: 将缩减的高级微架构特性而节省出的面积，用于增加更多的运算单元或者片上存储。
- 并行计算模块: 使用能够符合特定领域加速需求最简单的并行形式，例如，对于矩阵运算的加速，单条指令直接支持小矩阵运算。
- 量化: 减少计算数据尺寸与类型来符合特定领域性能要求，例如，深度学习中，推理可以采用int8量化方式进行。
- 专用编程语言: 使用DSA专用语言进行编程。
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 46

## Slide 47: 如何理解DSA 设计思想
- 如何理解DSA 设计思想
- 利用CPU上的对应设计，来说明基于DSA设计的AI处理器的特殊之处
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 47

## Slide 48: Example AI Processor: 华为DaVinci AI Core
- Example AI Processor: 华为DaVinci AI Core
- 我们用DaVinci Core来说明AI Core的特性。
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 48

## Slide 49: CPU 冯.诺依曼架构简介
- CPU 冯.诺依曼架构简介
- 冯.诺依曼结构的五大基本组件：
- 输入设备: 输入数据和程序
- 存储器: 记忆程序和数据
- 运算器: 完成数据加工处理
- 控制器: 控制程序执行
- 输出设备: 输出处理结果
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 49

## Slide 50: CPU支持的功能
- CPU支持的功能
- CPU很多资源用在辅助功能: Cache、分支预测、预取、中断、权限等。
- 数据读存
- Load
- 将数据从内存加载到寄存器
- Store
- 将寄存器中的数据存到内存
- 算术与逻辑运算
- Integer（整数运算）
- 如ADD/SUB/MUL/etc…
- Float（浮点运算）
- 如fADD/fSUB/fMUL/etc…
- Logical（二进制逻辑运算）
- 如AND/OR/NOT/etc…
- 分支跳转
- Conditional Jump
- 有条件跳转
- Unconditional Jump
- 无条件跳转
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 50

## Slide 51: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 51

## Slide 52: 目标：并行计算模块
- 目标：并行计算模块
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 52

## Slide 53: CPU?
- CPU?
Notes:
- 现在的计算世界往三个方向发展
- 53

## Slide 54: CPU经典5级流水线
- CPU经典5级流水线
- IF: 取指令 (Instruction Fetch )
- ID: 指令解码 (Instruction Decode)
- EXE: 执行 (Execute)
- MEM: 取内存操作数(Memory Operand Fetch)
- WB: 写回 (Writeback)
- IF
- ID
- EXE
- MEM
- WB
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 54

## Slide 55: 流水线类比
- 流水线类比
- 洗衣房洗衣服类比:
- 洗衣机洗涤，
- 干衣机烘干，
- 折叠烘干的衣服，
- 放进柜子。
- 非流水线
- 流水线
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 55

## Slide 56: CPU经典5级流水线
- CPU经典5级流水线
- IF: 取指令 (Instruction Fetch )
- ID: 指令解码 (Instruction Decode)
- EXE: 执行 (Execute)
- MEM: 取内存操作数(Memory Operand Fetch)
- WB: 写回 (Writeback)
- t0
- t1
- t2
- t3
- t4
- t5
- t6
- t7
- IF
- ID
- EXE
- MEM
- WB
- 1, ADD
- IF
- ID
- EXE
- MEM
- WB
- 2, MUL
- IF
- ID
- EXE
- MEM
- WB
- 3, SUB
- IF
- ID
- EXE
- MEM
- WB
- 1, ADD
- 2, MUL
- 3, SUB
- 程序：
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 56

## Slide 57: CPU经典5级流水线
- CPU经典5级流水线
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- t0
- t1
- t2
- t3
- t4
- t5
- t6
- t7
- 1, ADD
- 2, MUL
- 3, SUB
- 1, ADD
- 2, MUL
- 3, SUB
- 程序：
- 优势：一条指令操作一个数，灵活，可实现任意功能函数。
- 劣势：效率很低，五个流水线模块只要EXE模块是真正计算的。
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 57

## Slide 58: CPU 并行方式SIMD (Single Instruction Multiple Data)
- CPU 并行方式SIMD (Single Instruction Multiple Data)
- 计算任务 (A[6:0] + B[6:0])
- Scalar: 一个周期完成一个加法
- SIMD : 一个周期完成多个加法
- +
- t0
- A[0]
- B[0]
- t1
- A[1]
- B[1]
- t2
- A[2]
- B[2]
- t3
- A[3]
- B[3]
- t4
- A[4]
- B[4]
- t5
- A[5]
- B[5]
- t6
- A[6]
- B[6]
- t1
- A[4]
- B[4]
- A[5]
- B[5]
- A[6]
- B[6]
- +
- +
- +
- +
- t0
- A[0]
- B[0]
- A[1]
- B[1]
- A[2]
- B[2]
- A[3]
- B[3]
- Scalar
- SIMD
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 58

## Slide 59: 1, 256-bit AVX2 (8个32-bit float)
- 1, 256-bit AVX2 (8个32-bit float)
- 2, 512-bit AVX512 (16个32-bit float)
- Intel CPU上的SIMD：
- Not aggressive enough!
- Linus Torvalds: “I hope AVX512 dies a painful death, and that Intel starts fixing real problems instead of trying to create magic instructions to then create benchmarks that they can look good on…”
Notes:
- 现在的计算世界往三个方向发展
- 59

## Slide 60: CPU：样样行，样样不精
- CPU：样样行，样样不精
Notes:
- 现在的计算世界往三个方向发展
- 60

## Slide 61: AI Processor上的并行计算模块?
- AI Processor上的并行计算模块?
- Aggressive enough!
Notes:
- 现在的计算世界往三个方向发展
- 61

## Slide 62: 经典5级流水线是否适合深度学习计算？
- 经典5级流水线是否适合深度学习计算？
- t0
- t1
- t2
- t3
- t4
- t5
- t6
- t7
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- 灵活性 (优点)
- 一个指令可以操作一个数据，可以实现任意功能。
- 性能差(缺点)
- 一个数的操作都需要5级流水线，只有1级流水线是真正在计算的。
- 类比: 考前老师划重点了，你非得全课程地毯式复习！
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 62

## Slide 63: 深度学习加速器处理矩阵乘法
- 深度学习加速器处理矩阵乘法
- FC和Conv相关计算占据了99%的计算!
- Conv层数多
- FC的参数多
- 专门支持矩阵计算的电路会很大程度地提高整体性能!
- 专门支持向量计算的电路会很大程度地提高整体性能!
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 63

## Slide 64: 经典5级流水线是否适合深度学习？
- 经典5级流水线是否适合深度学习？
- t0
- t1
- t2
- t3
- t4
- t5
- t6
- t7
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- IF
- ID
- EXE
- MEM
- WB
- 灵活性 (优点)
- 一个指令可以操作一个数据，可以实现任意功能。
- 性能差(缺点)
- 一个数的操作都需要5级流水线，只有1级流水线是真正在计算的。
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 64

## Slide 65: 目标：并行计算模块
- 目标：并行计算模块
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 65

## Slide 66: AI Processor:
- AI Processor:
- Aggressive Custom Computing Unit
Notes:
- 现在的计算世界往三个方向发展
- 66

## Slide 67: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 67

## Slide 68: 目标：控制模块
- 目标：控制模块
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 68

## Slide 69: Control Logic on the CPU?
- Control Logic on the CPU?
Notes:
- 现在的计算世界往三个方向发展
- 69

## Slide 70: CPU: 超标量Superscalar
- CPU: 超标量Superscalar
- CISC指令内部RISC化
- 读入CISC指令
- 转换成RISC指令后执行
- 指令多并发
- 4条uop并发
- 6 条CISC指令一起解析
- 指令之间的并行执行
- 96条uop间找并行
Notes:
- Intel core 2:
- 蛮久之前之前的设计了
- 。。。
- 70

## Slide 71: AI Processor?
- AI Processor?
Notes:
- 现在的计算世界往三个方向发展
- 71

## Slide 72: AI Processor: 超标量Superscalar
- AI Processor: 超标量Superscalar
- 多instruction queue管理指令
- Scalar/Vector/Cube/MTE有单独的instruction queue
- 每个instruction queue顺序issue
- 没有特别优化instruction之间的并行
- AI Processor : 优化重点不在提升指令间并行，即不在控制模块。
Notes:
- 72

## Slide 73: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 73

## Slide 74: 目标：Global Buffer模块
- 目标：Global Buffer模块
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 74

## Slide 75: Why Cache on the CPU?
- Why Cache on the CPU?
Notes:
- 现在的计算世界往三个方向发展
- 75

## Slide 76: Recall: Data Movement vs. Computation
- Recall: Data Movement vs. Computation
- TABLE:
  | 32-bit Operation | Energy (pJ) | ADD (int) Relative Cost |
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
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 76

## Slide 77: Recall: DRAM Capacity, Bandwidth & Latency
- Recall: DRAM Capacity, Bandwidth & Latency
- 128x
- 20x
- 1.3x
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 77

## Slide 78: Recall: FF vs. SRAM vs. DRAM vs. Flash
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
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 78

## Slide 79: Motivation: CPU超长的内存访问时间
- Motivation: CPU超长的内存访问时间
- Main memory (DRAM)
- CPU
- ALU
- ~100ns
- ~0.4ns
- Memory access latency is two orders of magnitude longer than register access.
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 79

## Slide 80: Cache的位置和作用
- Cache的位置和作用
- Main memory (DRAM)
- CPU
- ALU
- ~100ns
- ~0.4ns
- Main memory (DRAM)
- CPU
- ALU
- Cache
- ~100ns
- ~2-12 ns
- ~0.4ns
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 80

## Slide 81: Cache的类比
- Cache的类比
Notes:
- 现在的计算世界往三个方向发展
- 81

## Slide 82: Analogy of Cache
- Analogy of Cache
- Main memory (DRAM)
- CPU
- ALU
- Cache
- 大臣
- 皇宫
- 皇帝
- 太监
Notes:
- 82

## Slide 83: Cache vs. 太监
- Cache vs. 太监
- Cache
- “ALU” talks to cache for its
- main memory access.
- 太监
- “皇帝” 通过 太监 去传唤大臣。
- Cache does not have address.
- 太监 没有编制。
- Cache is extremely important to performance.
- 太监 的地位很高（明朝）。
Notes:
- 讲完了背景，我现在想讲讲我的贡献
- mlweaving
- 。这个
- 包括两个部分，新的数据存储结构和新的定制硬件设计。首先我讲讲这个新的数据存储结构，这个用于任意精度的读取数据。
- 83

## Slide 84: Cache基本原理
- Cache基本原理
- Cache(高速缓存):
- 在处理器与DRAM之间的存储器, 主要使用SRAM技术。
- Cache的设计思想：
- 让硬件结构对程序员透明(硬件抽象)
- 给程序员一个拥有“快且大”存储空间的“幻觉”
- Cache基本工作原理（图书馆类比）：
- 一个学生坐在图书馆中的桌前写论文，桌上放着10本参考书。
- 大多数情况下，这10本参考书足够他参考。
- 当这个学生写到一个主题时，发现桌上10本参考书都找不到参考材料，所以他需要再去书架上找书。
- 由于桌子容量有限，最多只能放10本书，因此他将使用最少的那本书放回书架，并取回新书。
- 由于书架距离桌子较远，找书换书的过程中花费了他10分钟。
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 84

## Slide 85: Cache基本原理（Cont.）
- Cache基本原理（Cont.）
- Cache Hit(缓存中找到想要的数据)
- 桌子上找到想要的书
- Cache Miss(缓存中无想要的数据)
- 桌子上不到想要的书
- 内存
- 去书架找书
- 性能开销
- (访问内存的latency)
- 替换策略（Random/FIFO/LRU/…）：Cache满时，将已有数据替换出去
- 将使用最少的书放回书架并拿取新书
- 高速缓存（Cache）
- 桌子
- Cache容量
- 桌子最多放10本书
Notes:
- 举个例子，假如现在
- CS
- 有
- 100
- 门课，每门课有
- 10
- 本教材，例如我们今天讲人工智能芯片，都在
- 本里，这样一整天都只要读桌子上的书就行，不需要去书架上找书了。
- 85

## Slide 86: What is Cache?
- What is Cache?
- Generically, any structure that “memorizes” frequently used results to avoid repeating the long-latency operations required to reproduce the results from scratch, e.g., a web cache.
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 86

## Slide 87: Cache的运行机理？
- Cache的运行机理？
- Locality!
Notes:
- 现在的计算世界往三个方向发展
- 87

## Slide 88: Cache运行机制的依据：局部性Locality
- Cache运行机制的依据：局部性Locality
- 时间局部性 (Temporal Locality)
- 程序在运行时，最近刚刚被引用过的一个内存位置容易再次被引用。比如在调取一个函数的时候，前不久才调取过的本地参数容易再度被调取使用。
- 空间局部性 (Spatial Locality)
- 最近引用过的内存位置以及其周边的内存位置容易再次被使用。空间局部性比较常见于循环中，比如在一个数列中，如果上一个循环中使用第3个元素，那么本次循环中极有可能会使用第4个元素。
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 88

## Slide 89: Tag
- Tag
- 16B Cache Line
- Set 0
- Set 1
- Set 2
- Set 3
- Line 0
- Line 1
- Line 2
- Line 3
- Line 4
- Line 5
- Line 6
- Line 7
- Line 8
- Line 9
- Line 10
- Line 11
- Memory Op
- Memory
- Cache (2-way, 4-set)
- Tag
- Set
- Offset
- Equal?
- 10
- 2
- 4
- Memory Address (16bits)
Notes:
- 我们将
- ddr
- 以
- cache
- size
- 进行分割，这里
- memory
- 的地址为
- 5bit
- ，我们通过合理的地址划分，建立
- 与
- 的映射关系。
- tag
- 用来指定数据来源于
- 中的哪一块，
- set
- 用来指定数据放在
- 中的哪个位置。当
- 地址高位与对应
- 中的
- 可以匹配上时，我们就认为是
- Cache hit
- ，否则认为是
- cache miss
- 。
- direct mapped cache
- 使用高
- 2-bit
- 为
- ，低
- 3bit
- set selection
- 2-way set associative cache
- 3-bit
- 2bit
- 4-way set associative cache
- 4-bit
- 1bit
- 8-way set associative cache
- ，在上图中也就是
- fully associative cache
- ，使用全部
- 5-bit
- 地址作为
- ，没有
- set selection bit
- 课程名称

## Slide 90: Intel 4核CPU中的cache面积
- Intel 4核CPU中的cache面积
- Intel CPU内近一半芯片空间都花在L3 cache上，L1、L2呢？
- L3 cache大小： 2.5MB/core
- Cache的芯片面积利用率太低!
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 90

## Slide 91: Benefit of Cache
- Benefit of Cache
- Automatic: Hardware manages data movement across levels, transparently to the programmer.
- The programmer’s life is easier.
- A simple heuristic: keep most recently used items in cache.
- The average programmer doesn’t need to know about cache, but can still get benefit from it.
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 91

## Slide 92: Global Buffer on AI Processor?
- Global Buffer on AI Processor?
- Manual Control & High Performance!
Notes:
- 现在的计算世界往三个方向发展
- 92

## Slide 93: 目标应用: 深度学习算子访存特性分析
- 目标应用: 深度学习算子访存特性分析
- TABLE:
  | Operator | 计算特性 | 访存特性 |
  | Conv | 矩阵相乘 | Burst+stride |
  | Activation | 单向量操作 | Sequential |
  | Pooling | 单矩阵Reduce操作 | Burst+stride |
  | FC | 矩阵相乘 | Sequential |
Notes:
- 那我们的
- mlweaving
- 是怎么存储的呢，还是以行为单位，先把第一行的每个
- feature
- 的第一位存到一起，接着存每个
- 第二位，第三位，第四位。
- 93

## Slide 94: 复杂的cache设计是否适合深度学习？
- 复杂的cache设计是否适合深度学习？
- Tag
- 16B Cache Line
- Set 0
- Set 1
- Set 2
- Set 3
- Tag
- Set
- Offset
- Equal?
- 10
- 2
- 4
- Memory Address (16bits)
- Strided内存访问容易竞争同一个cache set。
- Strided内存访问的pattern比较固定，无需cache这么精致的结构，人工控制即可。
Notes:
- 举个
- 例子，当
- stride=2^6,7,8,…
- 时，会访问同一个
- set
- ，引起
- cache
- eviction
- 94

## Slide 95: AI Accelerator: Global Buffer
- AI Accelerator: Global Buffer
- 分块使用、降低单位内存访问的功耗!
- 编程真的会比较难，因为要考虑Buffer位置!
Notes:
- 分
- 块使用
- 95

## Slide 96: Cache or Buffer
- Cache or Buffer
- Main memory (DRAM)
- Mat
- Cache or Buffer
- Vec
- Scalar
- AI加速器
- TABLE:
  |  | Cache | Buffer |
  | 能耗 | 高 | 低 |
  | 芯片面积 | 大 | 小 |
  | 管理方式 | 自动 | 手动 |
Notes:
- Tensor computing
-  buffer….
- 96

## Slide 97: Main memory (DRAM)
- Main memory (DRAM)
- Mat
- Cache or Buffer
- Vec
- Scalar
- AI加速器
- TABLE:
  |  | Cache | Buffer |
  | 能耗 | 高 | 低 |
  | 芯片面积 | 大 | 小 |
  | 管理方式 | 自动 | 手动 |
- AI加速器的主要目标: 提高算力、降低功耗!
- 隐含的意思:可以牺牲可编程性!
- Cache or Buffer
Notes:
- 为什么要这个新的数据存储结构呢，这个是基于三个发现。第一个发现是现在的数据处理平台经常内存带宽是瓶颈。第二，低精度通常也可以提供一个合理的训练质量，一般情况下，
- 8
- 位就完全足够了。第三，即使是同一个数据集，不同的训练任务可能需要不同的精度。而且事先可能不知道是多少精度，这个就可能把数据集存不同的精度，这样会大大加大存储的需求量。那问题来了，我们能不能只存一份数据，然后可以非常高效的取出任意精度的数据。答案就是我所要讲的
- mlweaving
- 。接着我来讲讲
- 是怎么工作的？我们先来看看现在的机器学习系统是怎么存数据的，其实是按行来存储的，先存第一个
- feature
- 的第一位，然后第二位，第三位，第四位，然后是第二个
- 的第一位，第二位，第三位，第四位。然后是第二行。这里我们假设每行有两个
- ，每个
- 有四位。
- 97

## Slide 98: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 98

## Slide 99: Intuition: Why Low Precision Works for ML
- Intuition: Why Low Precision Works for ML
- ML
- 0
- 0.5
- 1
- “cat”
- “Not cat”
Notes:
- Suppose the output of machine learning model ranges from 0 to 1. If the prediction result is from 0.5 to 1, we can say that the machine learning model predict that the figure contains a cat.
- 99

## Slide 100: Intuition: Why Low Precision Works for ML
- Intuition: Why Low Precision Works for ML
- “It is a cat” (>0.5)
- 1.310245
- X 0.602069
- 0.788857897
- about 1.3
- X about 0.6
- about 0.78
- Full precision
- Low precision
- Relax, It is only Machine Learning.
Notes:
- Suppose the machine learning model contains a simple multiplication. The multiplication can be done in full precision, like the left side. It is larger than 0.5, it means the figure is a cat. Actually, we can also use low precision, the result is 0.78, which is also larger than 0.5. The low precision computation is able to show that the figure contains a cat.
- 100

## Slide 101: Different Precision Levels are Required
- Different Precision Levels are Required
- “It is a cat”
- “It is a cat”
- 3-bit
- 9-bit
Notes:
- Now we know why low precision works. We may need different precision levels for different input images. For this figure, we may need 3-bit. For the other figure, it may need 9 bits.
- 101

## Slide 102: Current Hardware Supports Limited Precision Levels
- Current Hardware Supports Limited Precision Levels
- Char (8-bit),
- Short (16-bit)
- FP8 (8-bit),
- FP16 (16-bit)
- CPU
- GPU
- 对低精度支持得不是很好
- 容易缺对应指令支持
- 没有资源倾斜
- 主要优化浮点操作、32位定点操作
Notes:
- We know that machine learning training can benefit from low precision, but the current commercial hardware only support limited precision levels. CPU can only support 8-bit and 16-bit. GPU can only support FP8 and FP16. TPU can only support 8-bit. The problem of limited precision levels is that we cannot fully take advantage of low precision. For instance, if your machine learning training needs only 4-bit precision, you have to pad it to 8-bit to compute in the modern hardware.
- 102

## Slide 103: AI Processor?
- AI Processor?
Notes:
- 现在的计算世界往三个方向发展
- 103

## Slide 104: Current Hardware Supports Limited Precision Levels
- Current Hardware Supports Limited Precision Levels
- INT8 (8-bit)
- TPU
- 对低精度支持得很好
- 有完备的指令支持
- 有资源倾斜
- 主要优化低精度指令操作
- Ascend
- INT8 (8-bit)
- INT8 (16-bit)
Notes:
- We know that machine learning training can benefit from low precision, but the current commercial hardware only support limited precision levels. CPU can only support 8-bit and 16-bit. GPU can only support FP8 and FP16. TPU can only support 8-bit. The problem of limited precision levels is that we cannot fully take advantage of low precision. For instance, if your machine learning training needs only 4-bit precision, you have to pad it to 8-bit to compute in the modern hardware.
- 104

## Slide 105: 用第一性原理重新考虑低精度:
- 用第一性原理重新考虑低精度:
- 支持任意精度
Notes:
- 所以
- AI
- 计算系统得是异构
- +
- 分布式。
- 105

## Slide 106: Stochastic Gradient Descent (SGD)
- Stochastic Gradient Descent (SGD)
- Linear Regression
- Training Data:
- Database,
- Sensor
- Computing Device:
- FPGA, GPU,
- CPU
- Model:
- DRAM,
- Cache
- Data Ar
- Model x
- Gradient: dot(Ar, x)Ar
- Ar = get_data()
- 1
- 2
- 3
- One Interesting Property:
- g = comp_grad(x,Ar)
- x = x – g
- Can be done in low precision
- (not 32-bit floating point)
- x = get_model()
- 4
- set_model(x)
Notes:
- Typically, SGD has three components: training data, computing device and model. OK. how
- sgd
- works? First, SGD read one row Ar. Second, SGD read the model x. Third, compute the gradient. Fourth, accumulate gradient to the model x. Then, SGD repeats such a process until it converges. SGD has two interesting properties. First, the model x can be staled, especially when running on multiple cores. Second, the dataset and gradient can be low precision, not always full precision.
- 106

## Slide 107: 我们的低精度方案
- 我们的低精度方案
- Arbitrary-precision NN Accelerator [1, 2]
- New Memory Layout (Software)
- New Hardware Design (Hardware)
- [1] Zeke Wang, et.al. Accelerating generalized linear models with MLWeaving: a one-size-fits-all system for any-precision learning. VLDB. 2019.
- [2] Zhenhao He, Zeke Wang, and Gustavo Alonso. BiS-KM: Enabling Any-Precision K-Means on FPGAs. FPGA. 2020.
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 107

## Slide 108: Data
- Data
- Compute
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that efficiently supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- MLWeaving:
- 1st row A
- New Memory Layout
- Observation 1:
- Often memory bandwidth bound
Notes:
- Why we need MLWeaving memory layout? Because we have three observations. First, memory bandwidth is always the bottleneck. Second, low precision dataset always provides reasonable training quality, for example, 8-bit is typically enough. The third observation is that even on the same dataset, different training task might need different precision level, then we have to store the same dataset in several precisions. It increases the storage requirement. Here is the question: can we store the data in a new memory layout that supports arbitrary precision data movement? Our answer is yes. It is MLWeaving. Before talking about MLWeaving, we first talk about how the most systems store ML data today. It is stored row-wise. We first store the first row, first bit of the first feature, the second bit of the first feature, the third bit and the fourth bit. Then the first bit of the second feature, the second bit of the second feature, the third bit and the fourth bit. Now comes to the second row, first feature, followed by the second feature. Then, How MLWeaving store the data? It is also row-wise. We first store the first row.
- 108

## Slide 109: New Memory Layout
- New Memory Layout
- Data
- Compute
- Observation 1:
- Often memory bandwidth bound
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that efficiently supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- 1st row A
- MLWeaving:
Notes:
- 109

## Slide 110: Data
- Data
- Compute
- Observation 1:
- Often memory bandwidth bound
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- 1st row A
- New Memory Layout
- MLWeaving:
Notes:
- Here
- is the difference. We store the first bits of all the features of the first row together, just the blue bits. Next store the second bits of the first row, yellow bits followed by the third and fourth bits. When the first row is done, we begin to deal with the second row.
- 110

## Slide 111: Data
- Data
- Compute
- Observation 1:
- Often memory bandwidth bound
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- 1st row A
- New Memory Layout
- MLWeaving:
Notes:
- 111

## Slide 112: Data
- Data
- Compute
- Observation 1:
- Often memory bandwidth bound
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- 1st row A
- New Memory Layout
- 2nd row B
- MLWeaving:
Notes:
- 112

## Slide 113: Data
- Data
- Compute
- Observation 1:
- Often memory bandwidth bound
- Observation 2: Low precision (e.g., 8 bit fixed point) often provides reasonable quality
- Observation 3: Different inference task might need different precision level even on the same dataset
- Can we store the data in a new data structure that supports arbitrary precision data movement?
- How most systems store ML data today:
- 1
- 1
- 1
- 1
- 1
- 1
- 2
- 2
- 2
- 2
- 2
- 2
- 2
- 1st row A
- 2nd row B
- 1st feature
- 2nd feature
- 1st row A
- New Memory Layout
- 2nd row B
- More complicated when a row has thousands of features, but you get the idea.
- If we need 1-bit?
- If we need 3-bits?
- Does not work out on CPUs. CPU does not have custom instruction for new memory layout and then we have to group bits from different memory locations before the further computing.
- MLWeaving:
Notes:
- It will be more complicated when we have thousands of feature, but I am sure you get the basic idea now. What is the benefit of such a data structure? Let me give you one concreate example. If FPGA needs 1-bit precision, actually, we only need to read the bits in blue. If we need 3-bit precision, we only fetch the necessary bits, without wasting any memory bandwidth. So far so good?
- Everything looks perfect right now?
- MLWeaving does not work out on CPUs
- . CPU does not have custom instruction for MLWeaving and then we have to
- group bits from different memory locations
- before the further computing.
- 113

## Slide 114: 我们的方案
- 我们的方案
- Arbitrary-precision NN Accelerator [1, 2]
- New Memory Layout (Software)
- New Hardware Design (Hardware)
- [1] Zeke Wang, et.al. Accelerating generalized linear models with MLWeaving: a one-size-fits-all system for any-precision learning. VLDB. 2019.
- [2] Zhenhao He, Zeke Wang, and Gustavo Alonso. BiS-KM: Enabling Any-Precision K-Means on FPGAs. FPGA. 2020.
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 114

## Slide 115: New memory layout:
- New memory layout:
- Key idea of hardware design:
- Key Idea of Hardware Design
- To use bit-serial multiplier to enable efficient data processing from the new memory layout.
- How bit-serial multiplier works?
- 1st row A
- 2nd row B
Notes:
- According to the properties of MLWeaving memory layout, the key idea of MLWeaving hardware design is to use FPGA to efficiently process data in the MLWeaving memory layout using bit-serial multiplier. Let me briefly talk about how bit-serial multiplier works.
- 115

## Slide 116: 4 3 2 1
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- How Bit-serial Multiplier Deals with Low Precision?
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Each bit should be binary, but we use decimal for ease of understanding.
Notes:
- I will use one concrete example to illustrate how bit-serial multiplier works, say 4-bit times 4-bit multiplication.
- In this example, we use decimal number for ease of understanding, it should be binary. The full precision is 4 bits 43
- handred
- 21 times 20. When the precision becomes 3-bit, we mean 4321 becomes 4320, 2-bit means 4300, and 1-bit means 4000
- 116

## Slide 117: 4 3 2 1
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- How Bit-serial Multiplier Deals with Low Precision?
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- 1
- 2
- 3
- 4
- BSM
- X 0020
- Initialization:
- 0
- 0
- 0
- 0
- 0
- Sum =
Notes:
- . Now we can see how bit-serial multiplier works. Bit serial multiplier has two parts.
- 117

## Slide 118: 4 3 2 1
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- How Bit-serial Multiplier Deals with Low Precision?
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- BSM
- X 0020
- Initialization:
- Bit-Serial (S)
- Bit-Parallel (P)
- 1
- 2
- 3
- 4
- 0
- 0
- 0
- 0
- 0
- Sum =
- Sum += P *
- [i]
- S
Notes:
- The first part is bit-serial part, which is shown in color. The second part is the bit-parallel part which is in black. The bit-serial multiplier does not do a multiplication as a whole, but accumulates bit by bit and stores the accumulation result in the variable sum.
- 118

## Slide 119: 4 3 2 1
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 1-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- BSM
- X 0020
- Memory
- Hardware
- 1
- 2
- 3
- 4
- 1st Cycle:
- 0
- 0
- 0
- 0
- 0
- 1
- 2
- 3
- 4
- Sum =
Notes:
- 119

## Slide 120: 4
- 4
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 1-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- BSM
- X 0020
- 1
- 2
- 3
- 4
- 1st Cycle:
- 0
- 0
- 0
- 0
- 0
- 1
- 2
- 3
- 4 means 4000.
- Sum += 20 * 4000
- Sum =
- Hardware
- Memory
Notes:
- What if we we want 1-bit precision? At the first cycle, we fetch the most significant bit 4 out of memory and feed it into the bit-serial multiplier in the FPGA.
- 120

## Slide 121: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 1-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 1st Cycle:
- 0
- 0
- 0
- 8
- 0
- 1
- 2
- 3
- Done with 1-bit precision, or proceed to the next bit.
- Sum =
- Hardware
- Memory
Notes:
- Then the result becomes 80000. It is done with 1-bit precision. If we want higher precision, we try to read the second bit.
- 121

## Slide 122: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 2-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 2nd Cycle:
- 0
- 0
- 0
- 8
- 0
- 1
- 2
- 3
- Sum =
- Hardware
- Memory
Notes:
- In the second cycle, we fetch the second bit 3 from memory and feed it into the bit-serial multiplier.
- 122

## Slide 123: 3
- 3
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 2-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 2nd Cycle:
- 0
- 0
- 0
- 8
- 0
- 1
- 2
- 3 means 300.
- Sum += 20 * 300
- Sum =
- Hardware
- Memory
Notes:
- 3 here means 300.
- 123

## Slide 124: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 2-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 2nd Cycle:
- 0
- 0
- 6
- 8
- 0
- 1
- 2
- Done with 2-bit precision, or proceed to the next bit.
- Sum =
- Hardware
- Memory
Notes:
- Then the accumulation result becomes 86000. It is done with 2-bit precision. If we want higher precision, we try to read the third bit.
- 124

## Slide 125: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 3-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 3th Cycle:
- 0
- 0
- 6
- 8
- 0
- 1
- 2
- Sum =
- Hardware
- Memory
Notes:
- In the third cycle, we fetch the third bit 2 from memory and feed it into the bit-serial multiplier.
- 125

## Slide 126: 2
- 2
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 3-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 3th Cycle:
- 0
- 0
- 6
- 8
- 0
- 1
- 2 means 20.
- Sum += 20 * 20
- Sum =
- Hardware
- Memory
Notes:
- Here 2 means 20.
- 126

## Slide 127: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 3-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 3th Cycle:
- 0
- 4
- 6
- 8
- 0
- 1
- Done with 3-bit precision, or proceed to the next bit.
- Sum =
- Hardware
- Memory
Notes:
- Then the accumulation result becomes 86400. It is done with 3-bit precision. If we want full-precision, we have to proceed to the next bit.
- 127

## Slide 128: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 4-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 4th Cycle:
- 0
- 4
- 6
- 8
- 0
- 1
- Sum =
- Hardware
- Memory
Notes:
- I will use one concrete example to illustrate how bit-serial multiplier works, say 4-bit times 4-bit multiplication.
- 128

## Slide 129: 1
- 1
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 4-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 4th Cycle:
- 0
- 4
- 6
- 8
- 0
- 1 means 1.
- Sum += 20 * 1
- Sum =
- Hardware
- Memory
Notes:
- 1 means 1.
- 129

## Slide 130: BSM
- BSM
- 4 3 2 1
- 4 3 2 0
- 4 0 0 0
- 4 3 0 0
- Bit-serial Multiplier: 4-Bit Precision
- Normal Multiplier
- X 0 0 2 0
- 8 6 4 2 0
- X 0 0 2 0
- 8 6 4 0 0
- 4-bit:
- 3-bit:
- X 0 0 2 0
- 8 6 0 0 0
- 2-bit:
- X 0 0 2 0
- 8 0 0 0 0
- 1-bit:
- Bit-serial Multiplier (BSM)
- X 0020
- 1
- 2
- 3
- 4
- 4th Cycle:
- 2
- 4
- 6
- 8
- 0
- Done with 4-bit precision
- Sum =
- Hardware
- Memory
Notes:
- Then the accumulation result becomes 86420. It is done, and we can proceed to the multiplication.
- 130

## Slide 131: MLWeaving’s Performance: Almost Linear Speedup with Lower Precision
- MLWeaving’s Performance: Almost Linear Speedup with Lower Precision
- Computing time vs. Precision
- Memory traffic vs. Precision
Notes:
- What is the real performance characteristics of MLWeaving? It can achieve almost linear speedup with lower precision, illustrated in black. Except when the precision is 1 bit. The underlying reason why 1-bit cannot achieve linear speedup is due to the long pipeline latency, which cannot be amortized. However, people rarely use 1-bit precision to train because the dataset will loses too much useful information.
- 131

## Slide 132: 目录
- 目录
- 为什么需要深度学习处理器
- 深度学习算子分析
- 深度学习加速器设计思路
- 并行计算模块
- 简化控制模块
- Global Buffer
- 量化
- 专用编程语言
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 132

## Slide 133: CPU编程 vs. AI Accelerator编程
- CPU编程 vs. AI Accelerator编程
- CPU编程 : 程序员不需要显式管理数据转移
- AI Accelerator编程: 程序员需要显式管理数据转移
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
- 显式buffer管理
- CPU编程
- AI Accelerator编程
Notes:
- To fully take advantage of MLWeaving memory layout, we have to rely on the custom computation, in our case, it is FPGA.
- 133

## Slide 134: 那AI加速器的编程模式怎么样？
- 那AI加速器的编程模式怎么样？
- 高性能
- 难编程
- 怎么处理编程难这个问题？
- 厂商提供算子库，用户直接调用库
Notes:
- 现在的计算世界往三个方向发展
- 134

## Slide 135: 整体比较: AI Accelerator vs. CPU
- 整体比较: AI Accelerator vs. CPU
- TABLE:
  |  | CPU | DSA |
  | On-chip Memory | Cache | Global Buffer |
  | Instruction Issue | Superscalar | In-order/simple |
  | Parallelism | Inter-instruction | Intra-instruction |
  | Fuctionality | Full | Partial |
  | Optimization Purpose | Low Latency | High Throughput |
  | Programming Language | General | Domain-specific |
Notes:
- 为啥需要深度学习处理器呢？
- 深度学习应用到很多应用，图像识别，语音处理，自然语言处理、博弈游戏等领域，
- AI for X
- 。
- 深度学习已在云服务器和智能手机上广泛应用。解读一下，本质上，人是懒惰，深度学习一定程度上能帮我们做一些事情，允许咋们懒惰。
- 通用
- CPU/GPU
- 处理人工神经网络效率非常低下，例如 谷歌大脑需要
- 1.6
- 万个
- CPU
- 核跑数天完成猫脸识别训练，
- 135