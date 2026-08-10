# Raw extraction: 14-parallel-training.pptx

Slide count: 86
Slide size EMU: 9144000 x 6858000


---

## Slide 1
**Title:** Computer Arch. & AI System

Lecture 14:
Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Rectangle 4; pos_in=[-0.25, 0.418, 10.75, 1.882]]
  - Computer Arch. & AI System
  - 
  - Lecture 14:
  - Parallel Training
- Shape 2 [PLACEHOLDER (14); name=Rectangle 5; pos_in=[0.75, 3.917, 8.583, 3.172]]
  - Prof. Zeke Wang
  - 
  - Zhejiang University
  - June 8 2026

---

## Slide 2
**Title:** Recall: Overall Architecture of DLP-S

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Recall: Overall Architecture of DLP-S
- Shape 3 [PLACEHOLDER (14); name=内容占位符 2; pos_in=[0.25, 1.139, 9.417, 5.68]]
  - Control Module
  - IFU (Instruction Fetch Unit)
  - IDU (Instruction Decode Unit)
  - 
  - Compute Unit
  - VFU (Vector Function Unit)
  - MFU (Matrix Function Unit)
  - 
  - SRAM Unit
  - WRAM (Weight RAM)
  - NRAM (Neuron RAM)
  - DMA (Direct Memory Access)
- Shape 4 [PICTURE (13); name=图片 4; pos_in=[5.159, 1.68, 4.799, 5.049]] PICTURE
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 2

---

## Slide 3
**Title:** Recall: Cambricon DLP ISA

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Recall: Cambricon DLP ISA
- Shape 3 [PICTURE (13); name=图片 4; pos_in=[0.54, 2.0, 8.919, 3.883]] PICTURE
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 3

---

## Slide 4
**Title:** Recall: DLP-M Architecture

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Recall: DLP-M Architecture
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[6.576, 1.005, 1.061, 0.438]]
  - DLP-C
- Shape 5 [AUTO_SHAPE (1); name=矩形 1; pos_in=[2.333, 1.041, 1.091, 0.438]]
  - DLP-M
- Shape 3 [PICTURE (13); name=图片 4; pos_in=[0.75, 1.361, 8.67, 4.098]] PICTURE
- Shape 4 [TEXT_BOX (17); name=内容占位符 2; pos_in=[0.443, 5.243, 9.45, 1.34]]
  - 多核处理器分层结构设计
  - 一个DLP-M由多个DLP-C构成
  - 一个DLP-C由多个DLP-S构成
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 4

---

## Slide 5
**Title:** Recall: AI Architecture

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.809]]
  - Recall: AI Architecture
- Shape 20 [PICTURE (13); name=image12.png; pos_in=[1.044, 1.183, 2.11, 1.192]] PICTURE
- Shape 17 [PICTURE (13); name=图片 21; pos_in=[14.805, 1.658, 4.78, 3.977]] PICTURE
- Shape 42 [AUTO_SHAPE (1); name=圆角矩形 181; pos_in=[3.285, 1.667, 4.381, 0.336]]
  - Hybrid parallel
- Shape 9 [TEXT_BOX (17); name=框架; pos_in=[0.402, 1.716, 0.926, 0.471]]
  - Parallel
  - Training
- Shape 28 [AUTO_SHAPE (1); name=圆角矩形 181; pos_in=[2.5, 2.083, 1.715, 0.336]]
  - Data parallel
- Shape 41 [AUTO_SHAPE (1); name=圆角矩形 181; pos_in=[6.534, 2.086, 1.966, 0.336]]
  - Pipeline parallel
- Shape 40 [AUTO_SHAPE (1); name=圆角矩形 181; pos_in=[4.522, 2.088, 1.811, 0.336]]
  - Model parallel
- Shape 33 [PICTURE (13); name=Picture 121; pos_in=[5.792, 2.261, 1.026, 0.931]] PICTURE
- Shape 32 [PICTURE (13); name=图片 42; pos_in=[6.736, 2.352, 0.746, 0.717]] PICTURE
- Shape 31 [PICTURE (13); name=image12.png; pos_in=[6.857, 2.505, 0.574, 0.414]] PICTURE
- Shape 12 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[4.417, 2.671, 2.333, 0.291]]
  - 模型训练和推理框架
- Shape 8 [TEXT_BOX (17); name=框架; pos_in=[0.026, 3.058, 1.52, 0.269]]
  - AI Framework
- Shape 23 [AUTO_SHAPE (1); name=圆角矩形 190; pos_in=[1.89, 3.144, 1.389, 0.351]]
  - MindSpore
- Shape 24 [AUTO_SHAPE (1); name=圆角矩形 191; pos_in=[3.347, 3.144, 0.924, 0.351]]
  - TensorFlow
- Shape 25 [AUTO_SHAPE (1); name=圆角矩形 192; pos_in=[4.357, 3.144, 0.79, 0.351]]
  - PyTorch
- Shape 26 [AUTO_SHAPE (1); name=圆角矩形 192; pos_in=[5.232, 3.144, 1.005, 0.351]]
  - PaddlePaddle
- Shape 27 [AUTO_SHAPE (1); name=圆角矩形 192; pos_in=[6.322, 3.144, 0.59, 0.351]]
  - …
- Shape 22 [AUTO_SHAPE (1); name=矩形 112; pos_in=[2.919, 3.73, 5.835, 0.37]]
  - 计算加速库、芯片算子库和高度自动化的算子开发工具
- Shape 7 [TEXT_BOX (17); name=芯片使能; pos_in=[0.249, 4.018, 1.641, 0.269]]
  - AI Runtime
- Shape 10 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[2.027, 4.157, 0.874, 0.381]]
  - CANN*
- Shape 35 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[6.096, 4.193, 0.874, 0.381]]
  - CUDA*
- Shape 13 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[2.901, 4.268, 4.038, 0.333]]
  - Compute Architecture for Neural Network
- Shape 36 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[6.948, 4.304, 2.635, 0.333]]
  - Compute Unified Device Architecture
- Shape 15 [AUTO_SHAPE (1); name=矩形 73; pos_in=[5.175, 4.8, 1.375, 0.37]]
  - AI IP和芯片
- Shape 39 [PICTURE (13); name=Picture 2; pos_in=[5.527, 5.21, 1.519, 1.289]] PICTURE
- Shape 37 [PICTURE (13); name=Picture 28; pos_in=[7.588, 5.239, 1.519, 1.163]] PICTURE
- Shape 38 [PICTURE (13); name=Picture 3; pos_in=[3.86, 5.384, 1.02, 1.038]] PICTURE
- Shape 11 [TEXT_BOX (17); name=芯片使能; pos_in=[0.392, 5.425, 1.35, 0.269]]
  - AI Chip
- Shape 21 [TEXT_BOX (17); name=Ascend-Nano; pos_in=[3.159, 6.151, 0.626, 0.242]]
  - Ascend
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[8.069, 6.917, 2.333, 0.5]]
  - 5

**Notes:**
- 全流程服务，分层API和预集成方案
- 降低核心代码量20%,效率提升50%以上
- 应对算子多样性，开发效率提升3倍

---

## Slide 6
**Title:** Recall: MindSpore

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Recall: MindSpore
- Shape 5 [AUTO_SHAPE (1); name=矩形 7; pos_in=[0.083, 1.162, 2.961, 0.9]]
  - Model Zoo
- Shape 3 [AUTO_SHAPE (1); name=矩形 5; pos_in=[3.157, 1.162, 6.054, 0.9]]
  - MindSpore Extend
  - GNN/深度概率编程/强化学习/微分方程
- Shape 37 [TEXT_BOX (17); name=文本框 39; pos_in=[6.936, 1.748, 3.019, 4.651]]
  - 自动并行：整图切分，感知集群拓扑，实现通信开销最小，融合数据并行与模型并行；
  - 二阶优化：利用二阶计算修正梯度更新方向，找到训练梯度最优下降路径，从而加速训练收敛过程；
  - 动静态图结合：统一自动微分引擎支持动静态图，一行代码完成模式切换，兼顾模型开发和执行效率；
  - AI+科学计算，场景应用创新，拓展MindSpore的边界
- Shape 27 [AUTO_SHAPE (1); name=矩形 29; pos_in=[8.056, 2.169, 1.156, 3.749]]
  - Mind
  - Insight
- Shape 4 [AUTO_SHAPE (1); name=矩形 6; pos_in=[0.083, 2.175, 1.239, 3.742]]
  - Mind
  - Armour
- Shape 6 [AUTO_SHAPE (1); name=矩形 8; pos_in=[1.417, 2.176, 2.076, 0.919]]
  - MindData
- Shape 14 [AUTO_SHAPE (1); name=矩形 16; pos_in=[7.112, 2.176, 0.775, 0.9]]
  - 仓颉
  - 前端
- Shape 22 [AUTO_SHAPE (1); name=矩形 24; pos_in=[3.631, 2.177, 3.348, 0.898]]
  - MindExpression
- Shape 28 [AUTO_SHAPE (1); name=圆角矩形 82; pos_in=[8.154, 2.768, 0.955, 0.3]]
  - 网络调试
- Shape 24 [AUTO_SHAPE (1); name=圆角矩形 78; pos_in=[0.221, 2.784, 0.907, 0.3]]
  - 密态AI
- Shape 10 [AUTO_SHAPE (1); name=矩形 12; pos_in=[1.424, 3.19, 6.488, 1.856]]
  - MindCompiler
- Shape 25 [AUTO_SHAPE (1); name=圆角矩形 79; pos_in=[0.228, 3.253, 0.907, 0.3]]
  - 可信AI
- Shape 29 [AUTO_SHAPE (1); name=圆角矩形 83; pos_in=[8.154, 3.338, 0.955, 0.3]]
  - 精度调优
- Shape 21 [AUTO_SHAPE (1); name=圆角矩形 75; pos_in=[4.959, 3.55, 1.09, 0.3]]
  - 二阶优化
- Shape 12 [AUTO_SHAPE (1); name=圆角矩形 66; pos_in=[6.13, 3.55, 1.563, 0.693]]
  - 量化/剪枝/….
- Shape 19 [AUTO_SHAPE (1); name=圆角矩形 73; pos_in=[1.633, 3.561, 1.051, 0.3]]
  - 类型推导
- Shape 18 [AUTO_SHAPE (1); name=圆角矩形 72; pos_in=[2.729, 3.561, 1.088, 0.3]]
  - 自动微分
- Shape 20 [AUTO_SHAPE (1); name=圆角矩形 74; pos_in=[3.862, 3.561, 1.066, 0.3]]
  - 自动并行
- Shape 30 [AUTO_SHAPE (1); name=圆角矩形 84; pos_in=[8.154, 3.879, 0.955, 0.3]]
  - 性能调优
- Shape 16 [AUTO_SHAPE (1); name=圆角矩形 70; pos_in=[1.628, 3.927, 1.432, 0.3]]
  - 内存优化
- Shape 17 [AUTO_SHAPE (1); name=圆角矩形 71; pos_in=[4.636, 3.938, 1.432, 0.3]]
  - 流水线执行
- Shape 15 [AUTO_SHAPE (1); name=圆角矩形 69; pos_in=[3.132, 3.941, 1.432, 0.3]]
  - 图算融合
- Shape 11 [AUTO_SHAPE (1); name=圆角矩形 65; pos_in=[1.602, 4.298, 6.09, 0.3]]
  - MindIR
- Shape 13 [AUTO_SHAPE (1); name=圆角矩形 67; pos_in=[4.81, 4.663, 2.883, 0.3]]
  - MindAKG(算子自动生成)
- Shape 23 [AUTO_SHAPE (1); name=圆角矩形 77; pos_in=[1.635, 4.665, 3.029, 0.3]]
  - 硬件相关优化
- Shape 7 [AUTO_SHAPE (1); name=矩形 9; pos_in=[1.406, 5.178, 6.512, 0.762]]
  - MindRT
- Shape 8 [AUTO_SHAPE (1); name=圆角矩形 62; pos_in=[1.626, 5.516, 3.624, 0.3]]
  - MindRT(分布式DAG并行执行)
- Shape 9 [AUTO_SHAPE (1); name=圆角矩形 63; pos_in=[5.377, 5.516, 2.315, 0.3]]
  - MindRT Lite/Micro
- Shape 36 [AUTO_SHAPE (1); name=圆角矩形 90; pos_in=[7.07, 6.168, 1.478, 0.372]]
  - iOS
- Shape 35 [AUTO_SHAPE (1); name=圆角矩形 89; pos_in=[5.462, 6.169, 1.478, 0.372]]
  - Android
- Shape 33 [AUTO_SHAPE (1); name=圆角矩形 87; pos_in=[2.268, 6.171, 1.478, 0.372]]
  - CUDA
- Shape 34 [AUTO_SHAPE (1); name=圆角矩形 88; pos_in=[3.821, 6.171, 1.478, 0.372]]
  - Eigen
- Shape 32 [AUTO_SHAPE (1); name=圆角矩形 86; pos_in=[0.602, 6.173, 1.611, 0.372]]
  - CANN昇腾
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 6

---

## Slide 7
**Title:** Recall: 关键技术4：AI+科学计算

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Recall: 关键技术4：AI+科学计算
- Shape 3 [AUTO_SHAPE (1); name=矩形 26; pos_in=[0.333, 1.006, 2.036, 0.543]]
  - 科学计算近况：
- Shape 4 [TEXT_BOX (17); name=文本框 27; pos_in=[0.5, 1.453, 7.854, 0.953]]
  - 科学计算核心问题是微分方程求解，算力消耗巨大，大规模求解器垄断历年戈登贝尔奖，近年来结合AI方法成为趋势。
- Shape 11 [AUTO_SHAPE (1); name=圆角矩形 20; pos_in=[3.521, 2.5, 3.177, 0.265]]
  - 传统数值方法
- Shape 10 [AUTO_SHAPE (1); name=矩形 37; pos_in=[3.497, 2.765, 3.36, 0.697]]
  - 高维微分方程求解，计算量大
  - 边界条件复杂，求解不稳定
- Shape 9 [AUTO_SHAPE (1); name=圆角矩形 32; pos_in=[3.525, 4.042, 3.177, 0.267]]
  - AI方法求解
- Shape 8 [AUTO_SHAPE (1); name=矩形 34; pos_in=[3.497, 4.282, 3.52, 0.697]]
  - 非线性拟合，无需解高维方程
  - 神经网络模拟，不需要处理边界条件
- Shape 5 [TEXT_BOX (17); name=文本框 28; pos_in=[0.16, 5.006, 9.667, 2.119]]
  - 业界AI+科学计算现状：
  - TF：众筹方式构建AI求解模型，典型应用领域取得突破；面向DNN设计的自动微分，计算高阶微分时效率低下；
  - Nvidia：支持高精度计算；构筑cuBLAS、cuFFT等基础数学库；上层框架依赖TensorFlow，继承TF缺点
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 7

---

## Slide 8
**Title:** Where Are We?

- Shape 1 [TEXT_BOX (17); name=文本框 1; pos_in=[0.25, 0.25, 2.969, 0.572]]
  - Where Are We?
- Shape 2 [PICTURE (13); name=Picture 2; pos_in=[-0.083, 1.25, 10.0, 5.728]] PICTURE

---

## Slide 9
**Title:** AI System: Four Components

- Shape 6 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AI System: Four Components
- Shape 3 [TEXT_BOX (17); name=TextBox 9; pos_in=[4.001, 2.255, 2.11, 0.505]]
  - Computing
- Shape 4 [AUTO_SHAPE (1); name=菱形 1; pos_in=[3.567, 2.866, 2.167, 1.917]]
  - Model
  - Training
- Shape 2 [TEXT_BOX (17); name=TextBox 4; pos_in=[2.333, 3.527, 1.697, 0.505]]
  - Storage
- Shape 1 [TEXT_BOX (17); name=TextBox 2; pos_in=[5.917, 3.527, 2.11, 0.505]]
  - Networking
- Shape 5 [TEXT_BOX (17); name=TextBox 9; pos_in=[3.992, 4.878, 1.741, 0.505]]
  - Compiling

---

## Slide 10
**Title:** Neural Network Training:  An Example

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Neural Network Training:  An Example
- Shape 23 [TEXT_BOX (17); name=object 30; pos_in=[2.734, 1.337, 0.559, 0.278]]
  - Input
- Shape 7 [TEXT_BOX (17); name=object 8; pos_in=[3.655, 1.979, 0.421, 0.184]]
  - Linear
- Shape 10 [TEXT_BOX (17); name=object 12; pos_in=[5.14, 2.001, 0.421, 0.184]]
  - Linear
- Shape 13 [TEXT_BOX (17); name=object 16; pos_in=[6.621, 2.016, 0.42, 0.184]]
  - Linear
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.543, 2.795, 8.914, 3.884]]
  - 1, Start with randomly initialized weights
  - 2, Iterate through your data a mini-batch of training data samples at a time:
  - Forward pass
  - Backward pass
  - Weight update
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 10
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 11
**Title:** An example: Network of 3 Linear Layers

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - An example: Network of 3 Linear Layers
- Shape 21 [TEXT_BOX (17); name=object 30; pos_in=[1.295, 1.727, 0.559, 0.278]]
  - Input
- Shape 5 [TEXT_BOX (17); name=object 8; pos_in=[2.216, 2.37, 0.421, 0.184]]
  - Linear
- Shape 8 [TEXT_BOX (17); name=object 12; pos_in=[3.7, 2.391, 0.421, 0.184]]
  - Linear
- Shape 11 [TEXT_BOX (17); name=object 16; pos_in=[5.182, 2.406, 0.42, 0.184]]
  - Linear
- Shape 23 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.336, 2.977, 8.914, 3.884]]
  - Each layer:
  - Input: vector
  - Output: vector
  - Learned parameters (weights):  projection matrix
  - Operations:
  - 1, Multiply the input vector with the matrix
  - 2, Apply a point-wise nonlinearity, say, ReLU
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 11
- Shape 22 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 12
**Title:** Network of 3 Linear Layers: Forward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Network of 3 Linear Layers: Forward Pass
- Shape 7 [TEXT_BOX (17); name=object 8; pos_in=[2.216, 2.37, 0.421, 0.184]]
  - Linear
- Shape 10 [TEXT_BOX (17); name=object 12; pos_in=[3.7, 2.391, 0.421, 0.184]]
  - Linear
- Shape 13 [TEXT_BOX (17); name=object 16; pos_in=[5.182, 2.406, 0.42, 0.184]]
  - Linear
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.336, 2.977, 8.914, 3.884]]
  - Each layer:
  - Input: vector
  - Output: vector
  - Learned parameters (weights): projection matrix
  - Operations:
  - 1, Multiply the input vector with the matrix
  - 2, Apply a point-wise nonlinearity, say, ReLU
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 12
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 13
**Title:** Network of 3 Linear Layers: Forward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Network of 3 Linear Layers: Forward Pass
- Shape 7 [TEXT_BOX (17); name=object 8; pos_in=[2.216, 2.37, 0.421, 0.184]]
  - Linear
- Shape 10 [TEXT_BOX (17); name=object 12; pos_in=[3.7, 2.391, 0.421, 0.184]]
  - Linear
- Shape 13 [TEXT_BOX (17); name=object 16; pos_in=[5.182, 2.406, 0.42, 0.184]]
  - Linear
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.336, 2.977, 8.914, 3.884]]
  - Each layer:
  - Input: vector
  - Output: vector
  - Learned parameters (weights): projection matrix
  - Operations:
  - 1, Multiply the input vector with the matrix
  - 2, Apply a point-wise nonlinearity, say, ReLU
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 13
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 14
**Title:** Network of 3 Linear Layers: Forward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Network of 3 Linear Layers: Forward Pass
- Shape 25 [TEXT_BOX (17); name=object 33; pos_in=[5.894, 1.874, 0.738, 0.278]]
  - Output
- Shape 7 [TEXT_BOX (17); name=object 8; pos_in=[2.216, 2.37, 0.421, 0.184]]
  - Linear
- Shape 10 [TEXT_BOX (17); name=object 12; pos_in=[3.7, 2.391, 0.421, 0.184]]
  - Linear
- Shape 13 [TEXT_BOX (17); name=object 16; pos_in=[5.182, 2.406, 0.42, 0.184]]
  - Linear
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.336, 2.977, 8.914, 3.884]]
  - Each layer:
  - Input: vector
  - Output: vector
  - Learned parameters (weights): projection matrix
  - Operations:
  - 1, Multiply the input vector with the matrix
  - 2, Apply a point-wise nonlinearity, say, ReLU
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 14
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 15
**Title:** Forward Pass: A Minibatch of 2 Samples

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Forward Pass: A Minibatch of 2 Samples
- Shape 92 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[5.537, 1.058, 4.949, 4.526]]
  - Matrix-vector multiplies
  - 
  -   Matrix-matrix multiplies
- Shape 93 [AUTO_SHAPE (1); name=矩形 1; pos_in=[1.317, 1.533, 3.037, 0.404]]
  - A minibatch of 1 sample
- Shape 90 [TEXT_BOX (17); name=object 98; pos_in=[0.512, 3.716, 0.559, 0.278]]
  - Input
- Shape 91 [TEXT_BOX (17); name=object 99; pos_in=[5.11, 3.862, 0.738, 0.278]]
  - Output
- Shape 6 [TEXT_BOX (17); name=object 7; pos_in=[1.438, 4.358, 0.421, 0.184]]
  - Linear
- Shape 9 [TEXT_BOX (17); name=object 11; pos_in=[2.922, 4.38, 0.421, 0.184]]
  - Linear
- Shape 12 [TEXT_BOX (17); name=object 15; pos_in=[4.403, 4.395, 0.42, 0.184]]
  - Linear
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 15
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 16
**Title:** Forward Pass: A Minibatch of 2 Samples

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Forward Pass: A Minibatch of 2 Samples
- Shape 5 [TEXT_BOX (17); name=object 3; pos_in=[1.295, 1.727, 0.559, 0.278]]
  - Input
- Shape 4 [TEXT_BOX (17); name=object 2; pos_in=[5.894, 1.874, 0.738, 0.278]]
  - Output
- Shape 8 [TEXT_BOX (17); name=object 9; pos_in=[2.221, 2.37, 0.421, 0.184]]
  - Linear
- Shape 11 [TEXT_BOX (17); name=object 13; pos_in=[3.705, 2.391, 0.421, 0.184]]
  - Linear
- Shape 14 [TEXT_BOX (17); name=object 17; pos_in=[5.186, 2.406, 0.42, 0.184]]
  - Linear
- Shape 197 [TEXT_BOX (17); name=object 206; pos_in=[4.832, 4.608, 0.176, 0.277]]
  - Y
- Shape 195 [TEXT_BOX (17); name=object 204; pos_in=[3.17, 4.61, 0.236, 0.277]]
  - W
- Shape 196 [TEXT_BOX (17); name=object 205; pos_in=[4.135, 4.61, 0.176, 0.277]]
  - X
- Shape 199 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[6.094, 4.667, 4.949, 3.109]]
  - Matrix-matrix multiplies
- Shape 191 [TEXT_BOX (17); name=object 200; pos_in=[3.78, 5.015, 0.887, 0.39]]
  - ×	=
- Shape 194 [TEXT_BOX (17); name=object 203; pos_in=[4.481, 5.467, 0.927, 0.464]]
  - Output  Activations
- Shape 192 [TEXT_BOX (17); name=object 201; pos_in=[2.853, 5.505, 0.703, 0.24]]
  - Weights
- Shape 193 [TEXT_BOX (17); name=object 202; pos_in=[3.756, 5.946, 0.927, 0.464]]
  - Input  Activations
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 16
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 17
**Title:** Forward Pass: Compute Loss

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Forward Pass: Compute Loss
- Shape 5 [TEXT_BOX (17); name=object 4; pos_in=[1.31, 1.792, 4.28, 0.781]]
  - Input
  - 
  - Linear	Linear	Linear
- Shape 55 [TEXT_BOX (17); name=object 60; pos_in=[5.894, 1.874, 0.738, 0.278]]
  - Output
- Shape 53 [TEXT_BOX (17); name=object 58; pos_in=[5.61, 2.286, 3.59, 1.264]]
  - Loss Value
  - Loss
  - Function
  - 
  - Ground Truth
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.327, 3.519, 9.583, 3.96]]
  - Loss function:
  - Produces a loss value that indicates how “wrong” the network was
  - Compares the output to the ground truth for each sample
  - Exact function math varies by task
  - Goal of training: minimize the loss value
  - Update network weights so the predicted output closely matches ground truth
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 17
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 18
**Title:** Backward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Backward Pass
- Shape 80 [TEXT_BOX (17); name=object 89; pos_in=[7.76, 1.848, 1.171, 0.278]]
  - Loss Value
- Shape 7 [TEXT_BOX (17); name=object 7; pos_in=[1.953, 1.931, 0.421, 0.184]]
  - Linear
- Shape 10 [TEXT_BOX (17); name=object 11; pos_in=[3.437, 1.953, 0.421, 0.184]]
  - Linear
- Shape 13 [TEXT_BOX (17); name=object 15; pos_in=[4.918, 1.968, 0.42, 0.184]]
  - Linear
- Shape 76 [TEXT_BOX (17); name=object 84; pos_in=[6.718, 2.048, 0.743, 0.464]]
  - Loss  Function
- Shape 4 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.128, 3.387, 9.661, 3.96]]
  - Goal: compute the gradients to the layer weights
  - Implementation: “back propagating” the loss through layers
  - Each layer computes weight gradient, used to update the weights
  - Each layer computes activation gradient, to be backpropagated to preceding layer
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 18
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 19
**Title:** Backward Pass: Compute dW

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Backward Pass: Compute dW
- Shape 318 [AUTO_SHAPE (1); name=Rectangle 326; pos_in=[2.922, 1.443, 0.342, 0.404]]
  - X
- Shape 317 [AUTO_SHAPE (1); name=Rectangle 325; pos_in=[3.738, 1.443, 0.418, 0.404]]
  - W
- Shape 319 [AUTO_SHAPE (1); name=Rectangle 327; pos_in=[4.412, 1.443, 0.346, 0.404]]
  - Y
- Shape 177 [TEXT_BOX (17); name=object 184; pos_in=[8.029, 2.286, 1.171, 0.278]]
  - Loss Value
- Shape 8 [TEXT_BOX (17); name=object 9; pos_in=[2.221, 2.37, 0.421, 0.184]]
  - Linear
- Shape 11 [TEXT_BOX (17); name=object 13; pos_in=[3.705, 2.391, 0.421, 0.184]]
  - Linear
- Shape 14 [TEXT_BOX (17); name=object 17; pos_in=[5.186, 2.406, 0.42, 0.184]]
  - Linear
- Shape 173 [TEXT_BOX (17); name=object 179; pos_in=[6.986, 2.486, 0.743, 0.464]]
  - Loss  Function
- Shape 320 [TEXT_BOX (17); name=object 8; pos_in=[5.056, 3.476, 4.69, 2.961]]
  - Compute the weight gradient dw
  - dW: weight gradient (to update weights)
  - dY:	incoming activation gradient
  - X:	input activations (from fwd pass)
  - 
  - Compute the activation gradient dx
  - dX: output activation gradient
  - to backpropagate to the preceding layer
- Shape 314 [TEXT_BOX (17); name=object 322; pos_in=[3.753, 3.938, 0.361, 0.277]]
  - X T
- Shape 312 [TEXT_BOX (17); name=object 320; pos_in=[5.061, 3.999, 0.356, 0.277]]
  - dW
- Shape 313 [TEXT_BOX (17); name=object 321; pos_in=[2.835, 4.002, 0.296, 0.277]]
  - dY
- Shape 310 [TEXT_BOX (17); name=object 318; pos_in=[3.184, 4.235, 0.212, 0.39]]
  - ×
- Shape 311 [TEXT_BOX (17); name=object 319; pos_in=[4.472, 4.241, 0.212, 0.39]]
  - =
- Shape 309 [TEXT_BOX (17); name=object 317; pos_in=[3.359, 5.227, 0.42, 0.278]]
  - W T
- Shape 307 [TEXT_BOX (17); name=object 315; pos_in=[4.844, 5.256, 0.296, 0.277]]
  - dX
- Shape 308 [TEXT_BOX (17); name=object 316; pos_in=[4.131, 5.264, 0.296, 0.278]]
  - dY
- Shape 178 [TEXT_BOX (17); name=object 185; pos_in=[3.829, 5.63, 0.9, 0.39]]
  - ×	=
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 19
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 20
**Title:** Weight Update

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Weight Update
- Shape 204 [AUTO_SHAPE (1); name=矩形 2; pos_in=[0.177, 0.984, 9.758, 2.516]]
  - Weight update (SGD)
  - Input: Weight W, gradient dW
  - Output: updated weight
  - Operation:
  - Increment each weight with the corresponding gradient value
- Shape 203 [TEXT_BOX (17); name=object 207; pos_in=[7.509, 1.756, 0.451, 0.262]]
  - SGD
- Shape 70 [TEXT_BOX (17); name=object 74; pos_in=[6.347, 2.134, 0.212, 0.262]]
  - W
- Shape 200 [TEXT_BOX (17); name=object 204; pos_in=[7.94, 2.141, 0.32, 0.262]]
  - dW
- Shape 135 [TEXT_BOX (17); name=object 139; pos_in=[9.151, 2.141, 0.212, 0.262]]
  - W
- Shape 69 [TEXT_BOX (17); name=object 73; pos_in=[8.647, 2.491, 0.191, 0.362]]
  - =
- Shape 201 [TEXT_BOX (17); name=object 205; pos_in=[7.0, 2.494, 0.121, 0.362]]
  - -
- Shape 202 [TEXT_BOX (17); name=object 206; pos_in=[7.229, 2.521, 0.376, 0.283]]
  - lr×
- Shape 205 [AUTO_SHAPE (1); name=矩形 691; pos_in=[0.204, 3.0, 5.459, 2.886]]
  - Weight update (Momentum)
  - Input: Weight W, gradient dW
  - States: 1 momenta (～model)
  - Output: updated weight
  - Operation:
  - Update internal state with weight gradient, then update weights using internal state
- Shape 603 [TEXT_BOX (17); name=object 606; pos_in=[8.784, 3.781, 1.993, 0.262]]
  - SGD with momentum
- Shape 273 [TEXT_BOX (17); name=object 276; pos_in=[8.095, 4.129, 0.126, 0.262]]
  - v
- Shape 403 [TEXT_BOX (17); name=object 406; pos_in=[9.67, 4.152, 0.32, 0.262]]
  - dW
- Shape 338 [TEXT_BOX (17); name=object 341; pos_in=[10.923, 4.152, 0.126, 0.262]]
  - v
- Shape 272 [TEXT_BOX (17); name=object 275; pos_in=[10.376, 4.453, 0.191, 0.362]]
  - =
- Shape 405 [TEXT_BOX (17); name=object 408; pos_in=[8.972, 4.487, 0.405, 0.283]]
  - lr×
- Shape 604 [TEXT_BOX (17); name=object 608; pos_in=[7.291, 4.504, 0.399, 0.283]]
  - µ×
- Shape 404 [TEXT_BOX (17); name=object 407; pos_in=[8.74, 4.512, 0.102, 0.294]]
  - -
- Shape 471 [TEXT_BOX (17); name=object 474; pos_in=[8.07, 4.977, 0.212, 0.262]]
  - W
- Shape 601 [TEXT_BOX (17); name=object 604; pos_in=[9.725, 4.978, 0.126, 0.262]]
  - v
- Shape 536 [TEXT_BOX (17); name=object 539; pos_in=[10.874, 4.984, 0.212, 0.262]]
  - W
- Shape 470 [TEXT_BOX (17); name=object 473; pos_in=[10.376, 5.276, 0.191, 0.362]]
  - =
- Shape 602 [TEXT_BOX (17); name=object 605; pos_in=[8.913, 5.278, 0.191, 0.362]]
  - +
- Shape 206 [AUTO_SHAPE (1); name=矩形 692; pos_in=[0.25, 5.917, 9.685, 1.223]]
  - Weight update (Adam)
  - States: 1 momenta, 1 variance
  - (reading and updating momenta/variance/parameters)
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 20
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Usually fp32 in reduced precision (FP16/BF16) training
- 
- Optimizer may need 2-6x more memory than just the model

---

## Slide 21
**Title:** One Iteration for a Layer

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - One Iteration for a Layer
- Shape 542 [TEXT_BOX (17); name=TextBox 559; pos_in=[0.089, 1.136, 2.481, 0.505]]
  - One iteration:
- Shape 543 [TEXT_BOX (17); name=object 3; pos_in=[5.672, 1.238, 4.255, 2.975]]
  - Backward pass:
  - Its compute is ~2x of forward
  - requires activations computed during the fwd pass
- Shape 105 [TEXT_BOX (17); name=object 108; pos_in=[5.48, 1.745, 0.176, 0.278]]
  - Y
- Shape 103 [TEXT_BOX (17); name=object 106; pos_in=[3.819, 1.748, 0.236, 0.278]]
  - W
- Shape 104 [TEXT_BOX (17); name=object 107; pos_in=[4.783, 1.748, 0.176, 0.278]]
  - X
- Shape 106 [TEXT_BOX (17); name=object 109; pos_in=[0.592, 2.095, 1.794, 0.286]]
  - 1, Forward Pass:
- Shape 101 [TEXT_BOX (17); name=object 104; pos_in=[4.428, 2.147, 0.212, 0.39]]
  - ×
- Shape 102 [TEXT_BOX (17); name=object 105; pos_in=[5.103, 2.152, 0.212, 0.39]]
  - =
- Shape 223 [TEXT_BOX (17); name=object 229; pos_in=[4.129, 3.23, 0.361, 0.278]]
  - X T
- Shape 221 [TEXT_BOX (17); name=object 227; pos_in=[5.436, 3.292, 0.356, 0.278]]
  - dW
- Shape 222 [TEXT_BOX (17); name=object 228; pos_in=[3.21, 3.295, 0.296, 0.278]]
  - dY
- Shape 224 [TEXT_BOX (17); name=object 230; pos_in=[0.576, 3.353, 2.037, 0.555]]
  - 2, Backward Pass:
  - weight gradients
- Shape 187 [TEXT_BOX (17); name=object 192; pos_in=[3.56, 3.527, 0.212, 0.39]]
  - ×
- Shape 188 [TEXT_BOX (17); name=object 193; pos_in=[4.848, 3.534, 0.212, 0.39]]
  - =
- Shape 544 [AUTO_SHAPE (1); name=Data Ar; pos_in=[6.449, 4.284, 3.265, 1.178]]
  - Read After Write (RAW) Dependency Regarding the Model w
- Shape 340 [TEXT_BOX (17); name=object 349; pos_in=[3.688, 4.415, 0.42, 0.277]]
  - W T
- Shape 338 [TEXT_BOX (17); name=object 347; pos_in=[5.173, 4.443, 0.296, 0.277]]
  - dX
- Shape 339 [TEXT_BOX (17); name=object 348; pos_in=[4.46, 4.452, 0.296, 0.277]]
  - dY
- Shape 341 [TEXT_BOX (17); name=object 350; pos_in=[0.576, 4.8, 2.14, 0.554]]
  - 2, Backward Pass:
  - activation gradients
- Shape 225 [TEXT_BOX (17); name=object 231; pos_in=[4.158, 4.817, 0.9, 0.39]]
  - ×	=
- Shape 408 [TEXT_BOX (17); name=object 423; pos_in=[2.962, 6.083, 0.236, 0.277]]
  - W
- Shape 473 [TEXT_BOX (17); name=object 489; pos_in=[6.06, 6.092, 0.236, 0.277]]
  - W
- Shape 538 [TEXT_BOX (17); name=object 555; pos_in=[4.112, 6.099, 0.356, 0.277]]
  - dW
- Shape 342 [TEXT_BOX (17); name=object 356; pos_in=[0.59, 6.43, 1.931, 0.285]]
  - 3, Weight update:
- Shape 539 [TEXT_BOX (17); name=object 556; pos_in=[3.516, 6.482, 0.212, 0.39]]
  - +
- Shape 407 [TEXT_BOX (17); name=object 422; pos_in=[4.806, 6.489, 0.86, 0.39]]
  - + … =
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 21
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 22
**Title:** Outline

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Outline
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 4; pos_in=[0.57, 1.542, 8.5, 5.119]]
  - Why Distributed Training？
  - Data Parallelism
  - Model Parallelism
  - Pipeline
  - Intra-layer
  - Communication Pattern Review
  - Summary
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 22

---

## Slide 23
**Title:** Why Distributed Training?

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Why Distributed Training?
- Shape 3 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.5, 1.083, 9.333, 5.75]]
  - Challenge from Model Side: Larger models
  - Language models (GPT-3): 175B parameters
  - Recommender models: largest ones are reaching O(1B) parameters
  - Vision models: deeper and wider Resnets and ResNeXTs
  - 
  - Challenge from Dataset Side: Larger datasets
  - Recommender data (user behavior): terabytes to petabytes
  - Image data: 1B Instagram dataset, JFT (300M images)
  - 
  - Challenge from System Side:
  - The memory size of a single accelerator, e.g., GPU, is 80GB.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 23

---

## Slide 24
**Title:** Why GPU memory size is 80GB?

- Shape 2 [TEXT_BOX (17); name=TextBox 5; pos_in=[1.944, 3.275, 6.113, 0.555]]
  - Why GPU memory size is 80GB?

**Notes:**
- 内存的速度跟容量只能要一个。。。

---

## Slide 25
**Title:** NVIDIA A100 Block Diagram

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - NVIDIA A100 Block Diagram
- Shape 5 [PICTURE (13); name=Picture 4; pos_in=[0.0, 1.12, 10.0, 5.008]] PICTURE
- Shape 3 [TEXT_BOX (17); name=TextBox 2; pos_in=[6.321, 6.098, 3.701, 0.236]]
  - https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
- Shape 2 [PLACEHOLDER (14); name=Content Placeholder 2; pos_in=[0.278, 6.333, 9.453, 0.583]]
  - 108 cores on the A100
  - (Up to 128 cores in the full-blown chip)
  - 40MB L2 cache
- Shape 4 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 25

**Notes:**
- The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2 cache.The L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

---

## Slide 26
**Title:** Why Distributed Training?

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Why Distributed Training?
- Shape 3 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.5, 1.083, 9.333, 5.75]]
  - Challenge from Model Side: Larger models
  - Language models: in the past 2 years grew from 340M (BERT-large) to 175B (GPT-3) parameters
  - Recommender models: largest ones are reaching O(1B) parameters
  - Vision models: deeper and wider Resnets and ResNeXTs
  - 
  - Challenge from Dataset Side: Larger datasets
  - Recommender data (user behavior): terabytes to petabytes
  - Image data: 1B Instagram dataset, JFT (300M images)
  - 
  - Challenge from System Side:
  - The memory size of a single accelerator, e.g., GPU, is 40GB.
- Shape 4 [AUTO_SHAPE (1); name=矩形 2; pos_in=[1.333, 6.333, 7.333, 0.64]]
  - Solution: scale out computing
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 26

---

## Slide 27
**Title:** Outline

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Outline
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 4; pos_in=[0.57, 1.542, 8.5, 5.119]]
  - Why Distributed Training？
  - Data Parallelism
  - Model Parallelism
  - Pipeline Parallelism
  - Tensor Parallelism
  - Communication Pattern Review
  - Summary
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 27

---

## Slide 28
**Title:** Parallelism Taxonomy

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Parallelism Taxonomy
- Shape 5 [TEXT_BOX (17); name=object 4; pos_in=[3.065, 1.992, 1.592, 0.278]]
  - Parallel Training
- Shape 9 [TEXT_BOX (17); name=object 8; pos_in=[6.356, 2.988, 1.4, 0.278]]
  - Model Parallel
- Shape 7 [TEXT_BOX (17); name=object 6; pos_in=[0.791, 3.107, 1.269, 0.278]]
  - Data Parallel
- Shape 11 [TEXT_BOX (17); name=object 10; pos_in=[4.083, 4.104, 1.417, 0.553]]
  - Intra Layer/
  - Tensor
- Shape 13 [TEXT_BOX (17); name=object 12; pos_in=[8.075, 4.216, 1.679, 0.553]]
  - Inter Layer/
  - Pipeline
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 28
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 29
**Title:** Data Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Data Parallel Training
- Shape 3 [TEXT_BOX (17); name=Content Placeholder 2; pos_in=[0.5, 1.083, 9.008, 1.917]]
  - Each worker:
  - Model: has a copy of the entire neural network model
  - Dataset: responsible for compute of a portion of data (training minibatch)
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 29
- Shape 4 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 30
**Title:** Data Parallel: Forward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Data Parallel: Forward Pass
- Shape 481 [TEXT_BOX (17); name=文本框 1; pos_in=[1.451, 1.23, 1.412, 0.404]]
  - Whole Model
- Shape 482 [TEXT_BOX (17); name=文本框 496; pos_in=[2.865, 1.251, 1.529, 0.404]]
  - Partial dataset
- Shape 6 [TEXT_BOX (17); name=object 6; pos_in=[4.696, 1.813, 0.176, 0.278]]
  - Y
- Shape 4 [TEXT_BOX (17); name=object 4; pos_in=[2.253, 1.821, 0.236, 0.278]]
  - W
- Shape 5 [TEXT_BOX (17); name=object 5; pos_in=[3.218, 1.821, 0.176, 0.278]]
  - X
- Shape 187 [TEXT_BOX (17); name=object 191; pos_in=[2.862, 2.221, 0.212, 0.39]]
  - ×
- Shape 188 [TEXT_BOX (17); name=object 192; pos_in=[4.319, 2.221, 0.212, 0.39]]
  - =
- Shape 475 [TEXT_BOX (17); name=object 487; pos_in=[0.356, 2.227, 1.028, 0.278]]
  - Worker 0:
- Shape 479 [AUTO_SHAPE (1); name=Rectangle 490; pos_in=[5.432, 2.85, 4.455, 1.582]]
  - Forward pass:
  - Computes output activations for its portion of minibatch
  - No communication is needed
- Shape 337 [TEXT_BOX (17); name=object 345; pos_in=[2.862, 3.48, 0.212, 0.39]]
  - ×
- Shape 338 [TEXT_BOX (17); name=object 346; pos_in=[4.319, 3.48, 0.212, 0.39]]
  - =
- Shape 476 [TEXT_BOX (17); name=object 488; pos_in=[0.356, 3.511, 1.027, 0.278]]
  - Worker 1:
- Shape 455 [TEXT_BOX (17); name=object 466; pos_in=[2.862, 4.74, 0.212, 0.39]]
  - ×
- Shape 456 [TEXT_BOX (17); name=object 467; pos_in=[4.319, 4.74, 0.212, 0.39]]
  - =
- Shape 477 [TEXT_BOX (17); name=object 489; pos_in=[0.386, 4.747, 1.027, 0.277]]
  - Worker 2:
- Shape 480 [AUTO_SHAPE (1); name=Rectangle 491; pos_in=[6.266, 5.792, 3.794, 1.15]]
  - X : input activations
  - W : model
  - Y : output activations
- Shape 104 [TEXT_BOX (17); name=object 106; pos_in=[2.862, 5.999, 0.212, 0.39]]
  - ×
- Shape 105 [TEXT_BOX (17); name=object 107; pos_in=[4.319, 5.999, 0.212, 0.39]]
  - =
- Shape 478 [TEXT_BOX (17); name=object 490; pos_in=[0.364, 6.006, 1.027, 0.277]]
  - Worker 3:
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 30
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 31
**Title:** Data Parallel: Backward Pass

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Data Parallel: Backward Pass
- Shape 6 [TEXT_BOX (17); name=object 5; pos_in=[3.275, 1.685, 0.361, 0.278]]
  - X T
- Shape 7 [TEXT_BOX (17); name=object 6; pos_in=[1.953, 1.743, 0.296, 0.278]]
  - dY
- Shape 5 [TEXT_BOX (17); name=object 4; pos_in=[4.76, 1.758, 0.665, 0.278]]
  - dW1
- Shape 478 [AUTO_SHAPE (1); name=Rectangle 488; pos_in=[5.357, 2.063, 4.731, 2.811]]
  - Backward pass:
  - Computes activation gradients for its portion of minibatch
  - Computes contribution to the weight gradient based on its portion of minibatch
  - All workers’ contributions must be summed before weight update
- Shape 72 [TEXT_BOX (17); name=object 72; pos_in=[2.673, 2.157, 0.212, 0.39]]
  - ×
- Shape 73 [TEXT_BOX (17); name=object 73; pos_in=[4.129, 2.157, 0.212, 0.39]]
  - =
- Shape 124 [TEXT_BOX (17); name=object 126; pos_in=[0.167, 2.163, 1.028, 0.278]]
  - Worker 0:
- Shape 479 [TEXT_BOX (17); name=object 4; pos_in=[4.684, 3.068, 0.665, 0.278]]
  - dW2
- Shape 125 [TEXT_BOX (17); name=object 127; pos_in=[0.167, 3.448, 1.027, 0.278]]
  - Worker 1:
- Shape 192 [TEXT_BOX (17); name=object 195; pos_in=[2.673, 3.452, 0.212, 0.39]]
  - ×
- Shape 193 [TEXT_BOX (17); name=object 196; pos_in=[4.129, 3.452, 0.212, 0.39]]
  - =
- Shape 480 [TEXT_BOX (17); name=object 4; pos_in=[4.667, 4.307, 0.665, 0.278]]
  - dW3
- Shape 126 [TEXT_BOX (17); name=object 128; pos_in=[0.197, 4.683, 1.027, 0.277]]
  - Worker 2:
- Shape 308 [TEXT_BOX (17); name=object 314; pos_in=[2.666, 4.695, 0.212, 0.39]]
  - ×
- Shape 309 [TEXT_BOX (17); name=object 315; pos_in=[4.123, 4.695, 0.212, 0.39]]
  - =
- Shape 481 [TEXT_BOX (17); name=object 4; pos_in=[4.623, 5.597, 0.665, 0.278]]
  - dW4
- Shape 4 [AUTO_SHAPE (1); name=Rectangle 491; pos_in=[6.266, 5.792, 3.794, 1.15]]
  - X : input activations
  - W : model
  - Y : output activations
- Shape 426 [TEXT_BOX (17); name=object 435; pos_in=[2.687, 5.938, 0.212, 0.39]]
  - ×
- Shape 427 [TEXT_BOX (17); name=object 436; pos_in=[4.144, 5.938, 0.212, 0.39]]
  - =
- Shape 127 [TEXT_BOX (17); name=object 129; pos_in=[0.174, 5.942, 1.027, 0.277]]
  - Worker 3:
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 31
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 32
**Title:** Data Parallel Training: Weight Update

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Data Parallel Training: Weight Update
- Shape 4 [AUTO_SHAPE (1); name=Rectangle 3; pos_in=[0.083, 1.52, 6.58, 0.572]]
  - Weight update:
- Shape 5 [AUTO_SHAPE (1); name=Rectangle 22; pos_in=[0.397, 2.256, 7.524, 1.29]]
  - 1, Each of N workers accumulates gradients:
  - Summing 1/N gradients collected from (N – 1) peers
- Shape 12 [TEXT_BOX (17); name=TextBox 9; pos_in=[6.663, 3.644, 1.282, 0.37]]
  - Worker a
- Shape 13 [TEXT_BOX (17); name=TextBox 10; pos_in=[8.743, 3.644, 1.282, 0.37]]
  - Worker b
- Shape 6 [AUTO_SHAPE (1); name=Rectangle 22; pos_in=[0.477, 3.7, 6.444, 1.234]]
  - 2, Each worker updates its model:
  - Each worker updates its copy of the model with combined gradients from all 4 workers
- Shape 8 [PICTURE (13); name=Icons8-Ios7-Industry-Memory-Module.ico; pos_in=[9.082, 3.927, 0.601, 0.601]] PICTURE
- Shape 9 [PICTURE (13); name=Icons8-Ios7-Industry-Memory-Module.ico; pos_in=[7.011, 3.929, 0.601, 0.601]] PICTURE
- Shape 16 [TEXT_BOX (17); name=TextBox 13; pos_in=[7.461, 5.108, 1.86, 0.404]]
  - (a+b+c+d)/4
- Shape 10 [PICTURE (13); name=Icons8-Ios7-Industry-Memory-Module.ico; pos_in=[7.011, 6.106, 0.601, 0.601]] PICTURE
- Shape 11 [PICTURE (13); name=Icons8-Ios7-Industry-Memory-Module.ico; pos_in=[9.082, 6.106, 0.601, 0.601]] PICTURE
- Shape 15 [TEXT_BOX (17); name=TextBox 12; pos_in=[6.659, 6.684, 1.282, 0.37]]
  - Worker d
- Shape 14 [TEXT_BOX (17); name=TextBox 11; pos_in=[8.783, 6.684, 1.282, 0.37]]
  - Worker c
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 32
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 33
**Title:** AI System: Four Components

- Shape 6 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AI System: Four Components
- Shape 3 [TEXT_BOX (17); name=TextBox 9; pos_in=[4.001, 2.255, 1.529, 0.505]]
  - Computing
- Shape 4 [AUTO_SHAPE (1); name=菱形 1; pos_in=[3.567, 2.866, 2.167, 1.917]]
  - Model
  - Training
- Shape 2 [TEXT_BOX (17); name=TextBox 4; pos_in=[2.333, 3.527, 1.697, 0.505]]
  - Storage
- Shape 1 [TEXT_BOX (17); name=TextBox 2; pos_in=[5.917, 3.527, 2.11, 0.505]]
  - Networking
- Shape 5 [TEXT_BOX (17); name=TextBox 9; pos_in=[3.992, 4.878, 1.529, 0.505]]
  - Compiling

---

## Slide 34
**Title:** AI System: Network

- Shape 53 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AI System: Network
- Shape 18 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[4.931, 0.494, 1.079, 0.288]]
  - NCCL
- Shape 11 [TEXT_BOX (17); name=文本框 13; pos_in=[8.578, 0.629, 1.54, 0.707]]
  - Scale Up
  - Network
- Shape 21 [TEXT_BOX (17); name=Text Box 7; pos_in=[6.459, 0.672, 1.772, 0.412]]
  - In-network computing
- Shape 19 [AUTO_SHAPE (1); name=双括号 21; pos_in=[4.733, 0.807, 1.481, 0.288]]
  - Collective     primitive
- Shape 10 [TEXT_BOX (17); name=文本框 12; pos_in=[1.827, 0.867, 1.54, 0.707]]
  - Scale Out
  - Network
- Shape 44 [TEXT_BOX (17); name=文本框 46; pos_in=[-0.115, 0.953, 1.29, 0.64]]
  - Application Layer
- Shape 48 [PICTURE (13); name=图片 50; pos_in=[2.505, 1.947, 2.212, 1.254]] PICTURE
- Shape 49 [AUTO_SHAPE (1); name=矩形: 圆角 51; pos_in=[4.893, 2.206, 1.153, 0.52]]
  - Offloaded
  - NCCL
- Shape 25 [TEXT_BOX (17); name=文本框 27; pos_in=[6.988, 2.298, 1.153, 0.572]]
  - 1us
  - 900GBps
- Shape 47 [TEXT_BOX (17); name=文本框 49; pos_in=[0.957, 2.585, 1.29, 0.404]]
  - Process on NIC
- Shape 24 [AUTO_SHAPE (1); name=矩形: 圆角 26; pos_in=[6.185, 2.591, 1.687, 0.641]]
  - NVLink
- Shape 31 [AUTO_SHAPE (1); name=双括号 33; pos_in=[7.872, 2.681, 1.663, 0.445]]
  - Differential Signaling
  - Serialization/Deserialization
- Shape 16 [TEXT_BOX (17); name=文本框 18; pos_in=[4.776, 3.331, 1.153, 0.572]]
  - 3us
  - 400Gbps
- Shape 34 [AUTO_SHAPE (1); name=双括号 36; pos_in=[7.018, 3.335, 1.46, 0.767]]
  - CXL based on PCIe, can direct LD/ST remote device memory, even can cross Node by CXL Switch
- Shape 6 [AUTO_SHAPE (1); name=矩形: 圆角 8; pos_in=[1.244, 3.338, 1.687, 0.641]]
  - On-NIC Stack
  - RDMA
- Shape 9 [AUTO_SHAPE (1); name=双括号 11; pos_in=[2.929, 3.377, 2.012, 0.557]]
  - RDMA engine or TCP offload engine, usually programmed by IB Verbs
- Shape 32 [AUTO_SHAPE (1); name=矩形: 圆角 34; pos_in=[8.607, 3.506, 1.291, 0.496]]
  - CXL
- Shape 38 [TEXT_BOX (17); name=文本框 40; pos_in=[-0.168, 3.948, 1.29, 0.64]]
  - Transaction Layer
- Shape 22 [AUTO_SHAPE (1); name=矩形: 圆角 24; pos_in=[6.174, 4.055, 1.687, 0.641]]
  - PCIe
- Shape 35 [AUTO_SHAPE (1); name=双括号 37; pos_in=[7.872, 4.281, 1.899, 0.547]]
  - Serial Bus, endpoint to endpoint transfer, provide up to 32Gbit/s serial data rate per lane
- Shape 5 [AUTO_SHAPE (1); name=矩形: 圆角 7; pos_in=[1.235, 4.37, 1.687, 0.641]]
  - Userspace
  - TCP/UDP
- Shape 17 [TEXT_BOX (17); name=文本框 19; pos_in=[4.684, 4.371, 1.153, 0.572]]
  - 10us
  - 100Gbps
- Shape 23 [TEXT_BOX (17); name=文本框 25; pos_in=[6.951, 4.408, 1.153, 0.572]]
  - 1us
  - 512Gbps
- Shape 8 [AUTO_SHAPE (1); name=双括号 10; pos_in=[2.921, 4.457, 2.012, 0.474]]
  - Programmed by DPDK, running network stack in userspace program
- Shape 46 [TEXT_BOX (17); name=文本框 48; pos_in=[4.192, 5.089, 1.29, 0.404]]
  - Process on CPU
- Shape 20 [AUTO_SHAPE (1); name=矩形: 圆角 22; pos_in=[2.916, 5.308, 0.816, 0.358]]
  - eBPF
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 6; pos_in=[1.235, 5.558, 1.687, 0.641]]
  - Kernel Stack
  - TCP/UDP
- Shape 15 [TEXT_BOX (17); name=文本框 17; pos_in=[4.681, 5.571, 1.153, 0.572]]
  - 100us
  - 10Gbps
- Shape 26 [AUTO_SHAPE (1); name=矩形: 圆角 28; pos_in=[6.174, 5.599, 1.687, 0.641]]
  - PCI
- Shape 45 [AUTO_SHAPE (1); name=双括号 47; pos_in=[7.862, 5.599, 1.899, 0.641]]
  - Parallels Bus, transfer 64 bit data in a clock cycle, bandwidth limited by frequent (33MHZ)
- Shape 7 [AUTO_SHAPE (1); name=双括号 9; pos_in=[2.919, 5.71, 1.976, 0.362]]
  - Programmed by Unix Socket
- Shape 27 [TEXT_BOX (17); name=文本框 29; pos_in=[7.09, 5.941, 1.153, 0.572]]
  - 2us
  - 4Gbps
- Shape 39 [TEXT_BOX (17); name=文本框 41; pos_in=[-0.063, 6.313, 1.29, 0.64]]
  - Network
  - Layer
- Shape 40 [AUTO_SHAPE (1); name=矩形: 圆角 42; pos_in=[1.235, 6.474, 1.687, 0.393]]
  - IP/ARP/ICMP
- Shape 43 [TEXT_BOX (17); name=文本框 45; pos_in=[-0.093, 6.914, 1.29, 0.64]]
  - Data Link Layer
- Shape 42 [AUTO_SHAPE (1); name=矩形: 圆角 44; pos_in=[1.225, 7.072, 1.687, 0.393]]
  - MAC/CSMA

---

## Slide 35
**Title:** AllReduce Implementation Choices

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AllReduce Implementation Choices
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.333, 1.191, 8.96, 2.389]]
  - “Ring” AllReduce (Baidu)
  - For any topology that contains a 1D torus (ring)
  - Each worker communicates with 2 neighbors
  - 2(N – 1) steps, worker sends/receives 1/N of all bytes
  - Each step requires a synchronization -> 2(N – 1) syncs total
  - Each worker needs CPU and GPU cycles to do ring AllReduce
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 35
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 36
**Title:** “Ring” AllReduce: Initial States

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.833]]
  - “Ring” AllReduce: Initial States
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c1
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d1
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d2
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 36
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 37
**Title:** “Ring” AllReduce: Results

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.833]]
  - “Ring” AllReduce: Results
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 37
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 38
**Title:** “Ring” AllReduce

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.833]]
  - “Ring” AllReduce
- Shape 6 [AUTO_SHAPE (1); name=矩形: 圆角 8; pos_in=[3.917, 1.213, 1.5, 0.667]]
  - GPU0
- Shape 7 [AUTO_SHAPE (1); name=矩形: 圆角 9; pos_in=[1.93, 2.667, 1.5, 0.667]]
  - GPU3
- Shape 8 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[5.899, 2.667, 1.5, 0.667]]
  - GPU1
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 11; pos_in=[3.917, 3.953, 1.5, 0.667]]
  - GPU2
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.333, 4.833, 9.333, 1.25]]
  - “Ring” AllReduce (Baidu) has two stages:
  - 1, Reduce_scatter: N-1 rounds, M/N data per round
  - 2, Allgather: N-1 rounds, M/N data per round
- Shape 5 [AUTO_SHAPE (1); name=矩形 1; pos_in=[2.68, 6.607, 4.727, 0.438]]
  - N: number of GPUs (4), M: data size
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 38
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 39
**Title:** “Ring” AllReduce: Initial States

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.833]]
  - “Ring” AllReduce: Initial States
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c1
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d1
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d2
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 24 [AUTO_SHAPE (1); name=矩形 3; pos_in=[2.433, 6.347, 5.9, 0.404]]
  - Partitioning of an array into N=4 chunks
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 39
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 40
**Title:** “Ring” AllReduce: Reduce_scatter iter. 0

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Reduce_scatter iter. 0
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c1
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d1
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d2
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 40
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 41
**Title:** “Ring” AllReduce: Reduce_scatter iter. 1

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Reduce_scatter iter. 1
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c1
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d1
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b1+b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d2
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 41
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 42
**Title:** “Ring” AllReduce: Reduce_scatter iter. 2

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Reduce_scatter iter. 2
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c1
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b1+b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d2
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 42
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 43
**Title:** “Ring” AllReduce: Reduce_scatter iter. 3

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Reduce_scatter iter. 3
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b1+b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 43
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 44
**Title:** “Ring” AllReduce: Allgather iter. 0

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Allgather iter. 0
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b1
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b1+b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c2
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 44
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 45
**Title:** “Ring” AllReduce: Allgather iter. 1

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Allgather iter. 1
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b1+b2
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 45
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 46
**Title:** “Ring” AllReduce: Allgather iter. 2

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Allgather iter. 2
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 46
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 47
**Title:** “Ring” AllReduce: Allgather iter. 3

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.667, 0.833]]
  - “Ring” AllReduce: Allgather iter. 3
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 47
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 48
**Title:** “Ring” AllReduce: Results

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 0.833]]
  - “Ring” AllReduce: Results
- Shape 4 [AUTO_SHAPE (1); name=矩形: 圆角 1; pos_in=[0.667, 1.766, 1.5, 0.667]]
  - GPU0
- Shape 5 [AUTO_SHAPE (1); name=矩形 2; pos_in=[2.333, 1.891, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 6 [AUTO_SHAPE (1); name=矩形 7; pos_in=[4.0, 1.891, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 7 [AUTO_SHAPE (1); name=矩形 8; pos_in=[5.667, 1.891, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 8 [AUTO_SHAPE (1); name=矩形 9; pos_in=[7.333, 1.891, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 9 [AUTO_SHAPE (1); name=矩形: 圆角 10; pos_in=[0.667, 2.846, 1.5, 0.667]]
  - GPU1
- Shape 10 [AUTO_SHAPE (1); name=矩形 11; pos_in=[2.333, 2.971, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 11 [AUTO_SHAPE (1); name=矩形 12; pos_in=[4.0, 2.971, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 12 [AUTO_SHAPE (1); name=矩形 13; pos_in=[5.667, 2.971, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 13 [AUTO_SHAPE (1); name=矩形 14; pos_in=[7.333, 2.971, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 14 [AUTO_SHAPE (1); name=矩形: 圆角 15; pos_in=[0.667, 3.926, 1.5, 0.667]]
  - GPU2
- Shape 15 [AUTO_SHAPE (1); name=矩形 16; pos_in=[2.333, 4.051, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 16 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.0, 4.051, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 17 [AUTO_SHAPE (1); name=矩形 18; pos_in=[5.667, 4.051, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 18 [AUTO_SHAPE (1); name=矩形 19; pos_in=[7.333, 4.051, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 19 [AUTO_SHAPE (1); name=矩形: 圆角 20; pos_in=[0.667, 5.012, 1.5, 0.667]]
  - GPU3
- Shape 20 [AUTO_SHAPE (1); name=矩形 21; pos_in=[2.333, 5.137, 1.667, 0.417]]
  - a0+a1+a2+a3
- Shape 21 [AUTO_SHAPE (1); name=矩形 22; pos_in=[4.0, 5.137, 1.667, 0.417]]
  - b0+b1+b2+b3
- Shape 22 [AUTO_SHAPE (1); name=矩形 23; pos_in=[5.667, 5.137, 1.667, 0.417]]
  - c0+c1+c2+c3
- Shape 23 [AUTO_SHAPE (1); name=矩形 24; pos_in=[7.333, 5.137, 1.667, 0.417]]
  - d0+d1+d2+d3
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 48
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[2.433, 7.111, 5.743, 0.37]]
  - [https://zhuanlan.zhihu.com/p/69797852, 2020]

---

## Slide 49
**Title:** AllReduce Implementation Choices

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AllReduce Implementation Choices
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.333, 1.191, 8.96, 2.016]]
  - “Ring” AllReduce (Baidu)
  - For any topology that contains a 1D torus (ring)
  - Each worker communicates with 2 neighbors
  - 2(N – 1) steps, worker sends/receives 1/N of all bytes
  - Each step requires a synchronization -> 2(N – 1) syncs total
- Shape 5 [TEXT_BOX (17); name=object 3; pos_in=[0.333, 4.0, 8.96, 1.623]]
  - “In-switch” AllReduce
  - Each worker communicates with the switch
  - Only one step, a worker sends/receives N of all bytes
  - All workers work in a lock step.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 49
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 50
**Title:** Data Parallel: Challenges

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Data Parallel: Challenges
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.146, 1.354, 9.771, 4.067]]
  - Strong scaling (increase the number of workers, keep minibatch size constant)
  - Certain layers require minimum minibatch sizes to properly operate
  - Example: batch normalization (BN) generally requires 16+ samples
  - Maybe lower GPU utilization
  - 
  - Weak scaling (increase the number of workers, increase minibatch size)
  - Training networks with large minibatches requires hyper-parameter adjustment
  - Learning rate schedule, BN decay, …
  - Example: R50 (SGD up to bs=16K, LARS above 16K, …)
  - Often increase the amount of work required to reach the same model accuracy
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 50
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 51
**Title:** Workload Increasing with Batch Size

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Workload Increasing with Batch Size
- Shape 6 [TEXT_BOX (17); name=object 4; pos_in=[0.167, 5.072, 9.5, 1.224]]
  - Epochs to reach the same model accuracy (from various submissions to MLPerf v0.7)
  - Epoch = 1 processing pass through entire dataset
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 51
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 52
**Title:** Workload Increasing with Batch Size

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Workload Increasing with Batch Size
- Shape 6 [TEXT_BOX (17); name=object 4; pos_in=[0.167, 5.072, 9.5, 1.224]]
  - Epochs to reach the same model accuracy (from various submissions to MLPerf v0.7)
  - Epoch = 1 processing pass through entire dataset
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 52
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 53
**Title:** Outline

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Outline
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 4; pos_in=[0.57, 1.542, 8.5, 5.119]]
  - Why Distributed Training？
  - Data Parallelism
  - Model Parallelism
  - Pipeline
  - Intra-layer
  - Communication Pattern Review
  - Summary
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 53

---

## Slide 54
**Title:** Parallelism Taxonomy

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Parallelism Taxonomy
- Shape 5 [TEXT_BOX (17); name=object 4; pos_in=[3.065, 1.992, 1.592, 0.278]]
  - Parallel Training
- Shape 9 [TEXT_BOX (17); name=object 8; pos_in=[6.356, 2.988, 1.4, 0.278]]
  - Model Parallel
- Shape 7 [TEXT_BOX (17); name=object 6; pos_in=[0.791, 3.107, 1.269, 0.278]]
  - Data Parallel
- Shape 13 [TEXT_BOX (17); name=object 12; pos_in=[8.075, 4.216, 1.679, 0.553]]
  - Inter Layer/
  - Pipeline
- Shape 11 [TEXT_BOX (17); name=object 10; pos_in=[4.091, 4.227, 1.06, 0.277]]
  - Intra Layer
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 54
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 55
**Title:** Model Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Model Parallel Training
- Shape 61 [TEXT_BOX (17); name=object 74; pos_in=[4.705, 1.708, 1.015, 0.278]]
  - Worker 0
- Shape 62 [TEXT_BOX (17); name=object 75; pos_in=[6.565, 1.708, 1.015, 0.278]]
  - Worker 1
- Shape 63 [TEXT_BOX (17); name=object 76; pos_in=[8.568, 1.71, 1.015, 0.278]]
  - Worker 2
- Shape 64 [TEXT_BOX (17); name=object 3; pos_in=[0.131, 2.13, 3.022, 1.524]]
  - Inter-layer Parallel (aka Pipeline Parallel):
  - A worker is responsible for its portion of the layers
- Shape 36 [TEXT_BOX (17); name=object 42; pos_in=[4.412, 2.98, 0.396, 0.352]]
  - Layer  1
- Shape 41 [TEXT_BOX (17); name=object 48; pos_in=[5.455, 2.98, 0.396, 0.352]]
  - Layer  2
- Shape 47 [TEXT_BOX (17); name=object 56; pos_in=[6.524, 2.98, 0.396, 0.352]]
  - Layer  3
- Shape 52 [TEXT_BOX (17); name=object 62; pos_in=[7.568, 2.98, 0.396, 0.352]]
  - Layer  4
- Shape 58 [TEXT_BOX (17); name=object 70; pos_in=[8.678, 2.98, 0.396, 0.352]]
  - Layer  5
- Shape 33 [AUTO_SHAPE (1); name=Rectangle 77; pos_in=[5.529, 4.849, 1.621, 0.37]]
  - Worker 0
- Shape 32 [TEXT_BOX (17); name=object 38; pos_in=[2.92, 5.035, 3.153, 1.664]]
  - Intra-layer Parallel
  - (aka Tensor Parallel):
  - A worker is responsible for its portion of each layer
- Shape 6 [TEXT_BOX (17); name=object 7; pos_in=[7.64, 5.491, 0.396, 0.352]]
  - Layer  1
- Shape 11 [TEXT_BOX (17); name=object 13; pos_in=[8.683, 5.491, 0.396, 0.352]]
  - Layer  2
- Shape 16 [TEXT_BOX (17); name=object 19; pos_in=[9.752, 5.491, 0.396, 0.352]]
  - Layer  3
- Shape 21 [TEXT_BOX (17); name=object 25; pos_in=[10.796, 5.491, 0.396, 0.352]]
  - Layer  4
- Shape 26 [TEXT_BOX (17); name=object 31; pos_in=[11.906, 5.491, 0.396, 0.352]]
  - Layer  5
- Shape 30 [TEXT_BOX (17); name=object 36; pos_in=[6.074, 5.558, 1.015, 0.277]]
  - Worker 1
- Shape 31 [TEXT_BOX (17); name=object 37; pos_in=[6.074, 6.113, 1.015, 0.277]]
  - Worker 2
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 55
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 56
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 22 [TABLE (19); name=object 23; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 25 [TEXT_BOX (17); name=object 26; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 56
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 57
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 22 [TABLE (19); name=object 23; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 25 [TEXT_BOX (17); name=object 26; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 57
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 58
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 26 [TEXT_BOX (17); name=object 26; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 19 [TABLE (19); name=object 19; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 24 [TEXT_BOX (17); name=object 24; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 22 [TEXT_BOX (17); name=object 22; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 23 [TEXT_BOX (17); name=object 23; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 58
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 59
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 22 [TABLE (19); name=object 23; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 25 [TEXT_BOX (17); name=object 26; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 59
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 60
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 22 [TABLE (19); name=object 23; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 25 [TEXT_BOX (17); name=object 26; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 60
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 61
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 22 [TABLE (19); name=object 23; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 25 [TEXT_BOX (17); name=object 26; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 61
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 62
**Title:** Pipeline Parallel Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training
- Shape 50 [TEXT_BOX (17); name=object 57; pos_in=[5.249, 1.609, 0.511, 0.278]]
  - Time
- Shape 43 [TABLE (19); name=object 50; pos_in=[0.283, 2.229, 7.977, 2.098]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  | 
- Shape 48 [TEXT_BOX (17); name=object 55; pos_in=[5.11, 4.927, 0.489, 0.277]]
  - Loss
- Shape 46 [TEXT_BOX (17); name=object 53; pos_in=[3.51, 4.943, 0.822, 0.277]]
  - Forward
- Shape 47 [TEXT_BOX (17); name=object 54; pos_in=[6.293, 4.943, 0.981, 0.277]]
  - Backward
- Shape 51 [TEXT_BOX (17); name=object 3; pos_in=[0.554, 5.127, 3.153, 1.748]]
  - Idle bubbles:
  - 67%: 12/18 step-slots
  - For N workers:
  - (N – 1)/N idle slots
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 62
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- N: number of workers, devices.

---

## Slide 63
**Title:** Pipeline Parallel Training: GPipe

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training: GPipe
- Shape 56 [AUTO_SHAPE (1); name=Rectangle 70; pos_in=[2.819, 1.081, 4.892, 0.505]]
  - Key Idea: 	Subminibatches
- Shape 54 [TABLE (19); name=object 66; pos_in=[0.394, 1.894, 9.442, 2.104]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  | 
- Shape 34 [TEXT_BOX (17); name=object 40; pos_in=[7.575, 4.522, 0.981, 0.277]]
  - Backward
- Shape 33 [TEXT_BOX (17); name=object 39; pos_in=[4.06, 4.547, 0.822, 0.277]]
  - Forward
- Shape 35 [TEXT_BOX (17); name=object 41; pos_in=[5.998, 4.547, 0.489, 0.277]]
  - Loss
- Shape 55 [TEXT_BOX (17); name=object 67; pos_in=[0.999, 5.339, 4.275, 1.294]]
  - 2 subminibatches
  - 2x more steps
  - Each step is ½  compute
- Shape 57 [AUTO_SHAPE (1); name=矩形 1; pos_in=[5.417, 5.43, 3.666, 0.849]]
  - Idle bubbles: 50%
  - 12/24 steps-slots
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 63
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 64
**Title:** Pipeline Parallel Training: GPipe

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel Training: GPipe
- Shape 56 [TABLE (19); name=object 68; pos_in=[0.394, 1.894, 9.442, 2.104]] TABLE
  - TABLE_ROW: Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  | 
  - TABLE_ROW: Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  | 
- Shape 36 [TEXT_BOX (17); name=object 42; pos_in=[7.575, 4.522, 0.981, 0.277]]
  - Backward
- Shape 35 [TEXT_BOX (17); name=object 41; pos_in=[4.06, 4.547, 0.822, 0.277]]
  - Forward
- Shape 37 [TEXT_BOX (17); name=object 43; pos_in=[5.998, 4.547, 0.489, 0.277]]
  - Loss
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.372, 4.973, 4.265, 0.352]]
  - N workers, K subminibatches:
- Shape 57 [TEXT_BOX (17); name=object 69; pos_in=[6.189, 5.029, 2.298, 0.352]]
  - As N  grows:
- Shape 5 [TEXT_BOX (17); name=object 4; pos_in=[0.789, 5.306, 4.804, 1.659]]
  - 2(N + K – 1) steps for fwd/bwd
  - Total step-slots: 2N(N + K – 1)
  - Idle step-slots: 2N(N – 1)
  - Fraction of idle slots: (N – 1)/(N + K – 1)
- Shape 58 [TEXT_BOX (17); name=object 70; pos_in=[6.795, 5.367, 2.938, 0.836]]
  - K = N →  50% idle slots
  - K = 4N →  20% idle slots
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 64
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 65
**Title:** Pipeline Parallel: Communication

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel: Communication
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.609, 1.616, 9.136, 4.268]]
  - A worker communicates with its 2 neighbors
  - 1D mesh topology
  - 1D torus when interleaving layers
  - 
  - Communication in each step of the fwd and bwd pass
  - Activations in fwd, activation gradients in bwd
  - 
  - Overlap communication with computation
  - Very hard
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 65
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 66
**Title:** Pipeline Parallel: Challenges

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Pipeline Parallel: Challenges
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.333, 1.167, 9.411, 4.571]]
  - Load balancing workload across workers is difficult
  - Different layers of a network can take different amounts of time
  - Leads to even busy slots for other workers idling for portions of time
  - 
  - Lots of computation to hide communication
  - 
  - Idle slots reduce scaling efficiency
  - Many subminibatches help with this, but run into the same problems as strong-scaling of data-parallel.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 66
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 67
**Title:** Outline

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Outline
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 4; pos_in=[0.57, 1.542, 8.5, 5.119]]
  - Why Distributed Training？
  - Data Parallelism
  - Model Parallelism
  - Pipeline
  - Tensor Parallelism
  - Communication Pattern Review
  - Summary
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 67

---

## Slide 68
**Title:** Tensor Parallel

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Tensor Parallel
- Shape 31 [TEXT_BOX (17); name=object 37; pos_in=[1.351, 1.416, 1.015, 0.278]]
  - Worker 0
- Shape 7 [TEXT_BOX (17); name=object 8; pos_in=[2.916, 1.982, 0.396, 0.352]]
  - Layer  1
- Shape 12 [TEXT_BOX (17); name=object 14; pos_in=[3.96, 1.982, 0.396, 0.352]]
  - Layer  2
- Shape 17 [TEXT_BOX (17); name=object 20; pos_in=[5.029, 1.982, 0.396, 0.352]]
  - Layer  3
- Shape 22 [TEXT_BOX (17); name=object 26; pos_in=[6.073, 1.982, 0.396, 0.352]]
  - Layer  4
- Shape 27 [TEXT_BOX (17); name=object 32; pos_in=[7.182, 1.982, 0.396, 0.352]]
  - Layer  5
- Shape 32 [TEXT_BOX (17); name=object 38; pos_in=[1.351, 2.01, 1.015, 0.278]]
  - Worker 1
- Shape 33 [TEXT_BOX (17); name=object 39; pos_in=[1.351, 2.604, 1.015, 0.278]]
  - Worker 2
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.417, 3.153, 8.649, 1.94]]
  - Partition a given layer’s weights among the workers
  - Addresses some of the Pipeline Parallel challenges
  - Idle slots, load imbalance
- Shape 358 [AUTO_SHAPE (1); name=Rectangle 370; pos_in=[3.78, 5.093, 3.026, 0.404]]
  - Row-wise partitioning:
- Shape 359 [AUTO_SHAPE (1); name=Rectangle 371; pos_in=[6.73, 5.097, 3.294, 0.404]]
  - Column-wise partitioning:
- Shape 360 [TEXT_BOX (17); name=object 4; pos_in=[-0.392, 5.111, 4.686, 1.441]]
  - Two variants:
  - Row-wise partitioning
  - Column-wise partitioning
- Shape 130 [TEXT_BOX (17); name=object 138; pos_in=[5.474, 5.626, 0.212, 0.39]]
  - ×
- Shape 357 [TEXT_BOX (17); name=object 368; pos_in=[8.566, 5.784, 0.212, 0.39]]
  - ×
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 68
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 69
**Title:** Row-wise Partitioning: Allgather between Layers

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.089, 0.189, 9.995, 1.167]]
  - Row-wise Partitioning: Allgather between Layers
- Shape 56 [AUTO_SHAPE (1); name=Rectangle 59; pos_in=[2.623, 0.915, 0.434, 0.404]]
  - W
- Shape 55 [AUTO_SHAPE (1); name=Rectangle 58; pos_in=[3.463, 0.927, 0.444, 0.404]]
  - X
- Shape 57 [AUTO_SHAPE (1); name=Rectangle 60; pos_in=[4.069, 0.934, 0.443, 0.404]]
  - Y
- Shape 15 [TABLE (19); name=object 15; pos_in=[2.441, 1.379, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 16 [TABLE (19); name=object 16; pos_in=[3.554, 1.379, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 17 [TABLE (19); name=object 17; pos_in=[4.162, 1.379, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 39 [TABLE (19); name=object 39; pos_in=[5.597, 1.379, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 28 [TABLE (19); name=object 28; pos_in=[6.375, 1.416, 0.795, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 27 [TABLE (19); name=object 27; pos_in=[7.488, 1.416, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 29 [TABLE (19); name=object 29; pos_in=[8.095, 1.416, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 18 [TEXT_BOX (17); name=object 18; pos_in=[3.299, 1.527, 0.759, 0.39]]
  - ×	=
- Shape 52 [TEXT_BOX (17); name=object 53; pos_in=[1.163, 1.543, 1.015, 0.278]]
  - Worker 0
- Shape 30 [TEXT_BOX (17); name=object 30; pos_in=[7.232, 1.563, 0.759, 0.39]]
  - ×	=
- Shape 20 [TABLE (19); name=object 20; pos_in=[2.441, 2.56, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 19 [TABLE (19); name=object 19; pos_in=[3.554, 2.56, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 21 [TABLE (19); name=object 21; pos_in=[4.162, 2.56, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 40 [TABLE (19); name=object 40; pos_in=[5.597, 2.56, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 32 [TABLE (19); name=object 32; pos_in=[6.375, 2.596, 0.795, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 31 [TABLE (19); name=object 31; pos_in=[7.488, 2.596, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 33 [TABLE (19); name=object 33; pos_in=[8.095, 2.596, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 22 [TEXT_BOX (17); name=object 22; pos_in=[3.314, 2.708, 0.744, 0.39]]
  - ×	=
- Shape 34 [TEXT_BOX (17); name=object 34; pos_in=[7.247, 2.743, 0.744, 0.39]]
  - ×	=
- Shape 53 [TEXT_BOX (17); name=object 54; pos_in=[1.168, 2.749, 1.015, 0.277]]
  - Worker 1
- Shape 23 [TABLE (19); name=object 23; pos_in=[2.441, 3.722, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 24 [TABLE (19); name=object 24; pos_in=[3.554, 3.722, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 25 [TABLE (19); name=object 25; pos_in=[4.162, 3.722, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 41 [TABLE (19); name=object 41; pos_in=[5.597, 3.722, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 35 [TABLE (19); name=object 35; pos_in=[6.375, 3.757, 0.795, 0.715]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 36 [TABLE (19); name=object 36; pos_in=[7.488, 3.757, 0.204, 0.715]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 37 [TABLE (19); name=object 37; pos_in=[8.095, 3.757, 0.204, 0.715]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 54 [TEXT_BOX (17); name=object 55; pos_in=[1.168, 3.869, 1.015, 0.277]]
  - Worker 2
- Shape 26 [TEXT_BOX (17); name=object 26; pos_in=[3.299, 3.869, 0.759, 0.39]]
  - ×	=
- Shape 38 [TEXT_BOX (17); name=object 38; pos_in=[7.232, 3.906, 0.759, 0.39]]
  - ×	=
- Shape 47 [TEXT_BOX (17); name=object 48; pos_in=[4.178, 5.035, 2.103, 0.539]]
  - Fwd communication:  Allgather
- Shape 49 [TEXT_BOX (17); name=object 50; pos_in=[2.819, 5.042, 1.168, 0.277]]
  - Layer K fwd
- Shape 51 [TEXT_BOX (17); name=object 52; pos_in=[6.472, 5.078, 1.675, 0.277]]
  - Layer (K + 1) fwd
- Shape 13 [TEXT_BOX (17); name=object 12; pos_in=[0.077, 5.447, 2.103, 0.352]]
  - Each worker:
- Shape 14 [TEXT_BOX (17); name=object 13; pos_in=[0.263, 5.744, 5.378, 1.248]]
  - W: Has a portion of weight rows
  - X: All of input activations X
  - Y: Computes a portion of output activations
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 69
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 70
**Title:** Column-wise Partitioning: ReduceScatter between Layers

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.0, 0.278, 10.072, 0.722]]
  - Column-wise Partitioning: ReduceScatter between Layers
- Shape 95 [AUTO_SHAPE (1); name=Rectangle 106; pos_in=[2.964, 1.03, 0.424, 0.404]]
  - W
- Shape 94 [AUTO_SHAPE (1); name=Rectangle 105; pos_in=[3.806, 1.03, 0.428, 0.404]]
  - X
- Shape 96 [AUTO_SHAPE (1); name=Rectangle 107; pos_in=[4.415, 1.03, 0.425, 0.404]]
  - Y
- Shape 74 [TABLE (19); name=object 81; pos_in=[2.839, 1.446, 0.716, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 76 [TABLE (19); name=object 83; pos_in=[6.689, 1.462, 0.712, 0.794]] TABLE
  - TABLE_ROW:  |  | 
- Shape 86 [TEXT_BOX (17); name=object 94; pos_in=[5.593, 1.477, 0.14, 0.24]]
  - +
- Shape 71 [TABLE (19); name=object 78; pos_in=[5.953, 1.486, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 23 [TEXT_BOX (17); name=object 23; pos_in=[3.655, 1.634, 0.759, 0.39]]
  - ×	=
- Shape 83 [TEXT_BOX (17); name=object 91; pos_in=[1.519, 1.65, 1.015, 0.278]]
  - Worker 0
- Shape 58 [TEXT_BOX (17); name=object 62; pos_in=[7.505, 1.65, 0.759, 0.39]]
  - ×	=
- Shape 75 [TABLE (19); name=object 82; pos_in=[2.839, 2.627, 0.716, 0.794]] TABLE
  - TABLE_ROW:  |  | 
- Shape 77 [TABLE (19); name=object 84; pos_in=[6.689, 2.642, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 72 [TABLE (19); name=object 79; pos_in=[5.953, 2.668, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 62 [TABLE (19); name=object 67; pos_in=[8.368, 2.684, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 49 [TEXT_BOX (17); name=object 51; pos_in=[3.671, 2.816, 0.744, 0.39]]
  - ×	=
- Shape 63 [TEXT_BOX (17); name=object 68; pos_in=[7.5, 2.832, 0.744, 0.39]]
  - ×	=
- Shape 84 [TEXT_BOX (17); name=object 92; pos_in=[1.524, 2.856, 1.015, 0.277]]
  - Worker 1
- Shape 89 [TEXT_BOX (17); name=object 98; pos_in=[5.611, 2.899, 0.124, 0.24]]
  - +
- Shape 50 [TABLE (19); name=object 52; pos_in=[2.839, 3.788, 0.716, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 64 [TABLE (19); name=object 69; pos_in=[6.689, 3.803, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 73 [TABLE (19); name=object 80; pos_in=[5.953, 3.829, 0.205, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 69 [TABLE (19); name=object 76; pos_in=[8.368, 3.846, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 85 [TEXT_BOX (17); name=object 93; pos_in=[1.525, 3.977, 1.015, 0.277]]
  - Worker 2
- Shape 54 [TEXT_BOX (17); name=object 57; pos_in=[3.655, 3.977, 0.759, 0.39]]
  - ×	=
- Shape 70 [TEXT_BOX (17); name=object 77; pos_in=[7.454, 4.012, 0.759, 0.39]]
  - ×	=
- Shape 92 [TEXT_BOX (17); name=object 102; pos_in=[5.635, 4.296, 0.14, 0.24]]
  - +
- Shape 9 [TEXT_BOX (17); name=object 48; pos_in=[4.609, 5.086, 2.103, 0.539]]
  - Fwd communication:  ReduceScatter
- Shape 80 [TEXT_BOX (17); name=object 88; pos_in=[3.176, 5.149, 1.168, 0.277]]
  - Layer K fwd
- Shape 82 [TEXT_BOX (17); name=object 90; pos_in=[6.745, 5.165, 1.676, 0.277]]
  - Layer (K + 1) fwd
- Shape 7 [TEXT_BOX (17); name=object 12; pos_in=[0.117, 5.413, 2.103, 0.352]]
  - Each worker:
- Shape 8 [TEXT_BOX (17); name=object 13; pos_in=[0.393, 5.74, 5.378, 1.248]]
  - W: Has a portion of weight rows
  - X: All of input activations X
  - Y: Computes a portion of output activations
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 70
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Fwd communication:
- Reduce_scatter: each worker needs partial activations at next layer

---

## Slide 71
**Title:** Reducing Synchronization By Alternating Partitioning

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.0, 0.278, 10.072, 0.722]]
  - Reducing Synchronization By Alternating Partitioning
- Shape 64 [TEXT_BOX (17); name=object 67; pos_in=[2.237, 1.17, 6.593, 0.319]]
  - Row-wise partitioning    Column-wise partitioning
- Shape 54 [TABLE (19); name=object 57; pos_in=[5.353, 1.578, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 63 [TABLE (19); name=object 7; pos_in=[6.418, 1.604, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 6 [TABLE (19); name=object 5; pos_in=[2.529, 1.619, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 7 [TABLE (19); name=object 6; pos_in=[3.642, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 8 [TABLE (19); name=object 7; pos_in=[4.249, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 30 [TABLE (19); name=object 31; pos_in=[6.436, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 9 [TEXT_BOX (17); name=object 8; pos_in=[3.402, 1.767, 0.744, 0.39]]
  - ×	=
- Shape 36 [TEXT_BOX (17); name=object 38; pos_in=[6.184, 1.767, 0.744, 0.39]]
  - ×	=
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[1.25, 1.783, 1.015, 0.278]]
  - Worker 0
- Shape 55 [TABLE (19); name=object 58; pos_in=[5.353, 2.76, 0.712, 0.794]] TABLE
  - TABLE_ROW:  |  | 
- Shape 11 [TABLE (19); name=object 10; pos_in=[2.529, 2.8, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 10 [TABLE (19); name=object 9; pos_in=[3.642, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 12 [TABLE (19); name=object 11; pos_in=[4.249, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 37 [TABLE (19); name=object 39; pos_in=[6.423, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 13 [TEXT_BOX (17); name=object 12; pos_in=[3.402, 2.948, 0.744, 0.39]]
  - ×	=
- Shape 51 [TEXT_BOX (17); name=object 54; pos_in=[6.184, 2.948, 0.744, 0.39]]
  - ×	=
- Shape 28 [TEXT_BOX (17); name=object 29; pos_in=[1.255, 2.989, 1.015, 0.277]]
  - Worker 1
- Shape 52 [TABLE (19); name=object 55; pos_in=[5.353, 3.921, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 14 [TABLE (19); name=object 13; pos_in=[2.529, 3.961, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[1.256, 4.109, 1.015, 0.277]]
  - Worker 2
- Shape 24 [TEXT_BOX (17); name=object 25; pos_in=[3.402, 4.109, 0.744, 0.39]]
  - ×	=
- Shape 53 [TEXT_BOX (17); name=object 56; pos_in=[6.184, 4.109, 0.744, 0.39]]
  - ×	=
- Shape 66 [AUTO_SHAPE (1); name=Rectangle 59; pos_in=[2.71, 4.697, 0.434, 0.404]]
  - W
- Shape 67 [AUTO_SHAPE (1); name=Rectangle 59; pos_in=[5.485, 4.71, 0.434, 0.404]]
  - W
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[2.907, 5.282, 1.168, 0.277]]
  - Layer K fwd
- Shape 62 [TEXT_BOX (17); name=object 66; pos_in=[5.389, 5.282, 1.676, 0.277]]
  - Layer (K + 1) fwd
- Shape 65 [TEXT_BOX (17); name=object 4; pos_in=[0.568, 5.745, 8.94, 0.893]]
  - Note: no communication is needed for two matrices
  - Worker i produces output, which is its input for the next layer
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 71
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Fwd communication:
- Reduce_scatter: each worker needs partial activations at next layer

---

## Slide 72
**Title:** Reducing Synchronization By Alternating Partitioning

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.0, 0.278, 10.072, 0.722]]
  - Reducing Synchronization By Alternating Partitioning
- Shape 64 [TEXT_BOX (17); name=object 67; pos_in=[2.237, 1.17, 6.593, 0.319]]
  - Row-wise partitioning    Column-wise partitioning
- Shape 54 [TABLE (19); name=object 57; pos_in=[5.353, 1.578, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 63 [TABLE (19); name=object 7; pos_in=[6.418, 1.604, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 6 [TABLE (19); name=object 5; pos_in=[2.529, 1.619, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 7 [TABLE (19); name=object 6; pos_in=[3.642, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 8 [TABLE (19); name=object 7; pos_in=[4.249, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 30 [TABLE (19); name=object 31; pos_in=[6.436, 1.619, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 9 [TEXT_BOX (17); name=object 8; pos_in=[3.402, 1.767, 0.744, 0.39]]
  - ×	=
- Shape 36 [TEXT_BOX (17); name=object 38; pos_in=[6.184, 1.767, 0.744, 0.39]]
  - ×	=
- Shape 27 [TEXT_BOX (17); name=object 28; pos_in=[1.25, 1.783, 1.015, 0.278]]
  - Worker 0
- Shape 55 [TABLE (19); name=object 58; pos_in=[5.353, 2.76, 0.712, 0.794]] TABLE
  - TABLE_ROW:  |  | 
- Shape 11 [TABLE (19); name=object 10; pos_in=[2.529, 2.8, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 10 [TABLE (19); name=object 9; pos_in=[3.642, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 12 [TABLE (19); name=object 11; pos_in=[4.249, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 37 [TABLE (19); name=object 39; pos_in=[6.423, 2.8, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 13 [TEXT_BOX (17); name=object 12; pos_in=[3.402, 2.948, 0.744, 0.39]]
  - ×	=
- Shape 51 [TEXT_BOX (17); name=object 54; pos_in=[6.184, 2.948, 0.744, 0.39]]
  - ×	=
- Shape 28 [TEXT_BOX (17); name=object 29; pos_in=[1.255, 2.989, 1.015, 0.277]]
  - Worker 1
- Shape 68 [TEXT_BOX (17); name=文本框 1; pos_in=[7.542, 3.001, 1.596, 0.505]]
  - +Next two?
- Shape 52 [TABLE (19); name=object 55; pos_in=[5.353, 3.921, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 14 [TABLE (19); name=object 13; pos_in=[2.529, 3.961, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 29 [TEXT_BOX (17); name=object 30; pos_in=[1.256, 4.109, 1.015, 0.277]]
  - Worker 2
- Shape 24 [TEXT_BOX (17); name=object 25; pos_in=[3.402, 4.109, 0.744, 0.39]]
  - ×	=
- Shape 53 [TEXT_BOX (17); name=object 56; pos_in=[6.184, 4.109, 0.744, 0.39]]
  - ×	=
- Shape 66 [AUTO_SHAPE (1); name=Rectangle 59; pos_in=[2.71, 4.697, 0.434, 0.404]]
  - W
- Shape 67 [AUTO_SHAPE (1); name=Rectangle 59; pos_in=[5.485, 4.71, 0.434, 0.404]]
  - W
- Shape 26 [TEXT_BOX (17); name=object 27; pos_in=[2.907, 5.282, 1.168, 0.277]]
  - Layer K fwd
- Shape 62 [TEXT_BOX (17); name=object 66; pos_in=[5.389, 5.282, 1.676, 0.277]]
  - Layer (K + 1) fwd
- Shape 65 [TEXT_BOX (17); name=object 4; pos_in=[0.568, 5.745, 8.94, 0.893]]
  - Note: no communication is needed for two matrices
  - Worker i produces output, which is its input for the next layer
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 72
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Fwd communication:
- Reduce_scatter: each worker needs partial activations at next layer

---

## Slide 73
**Title:** Reducing Synchronization By Alternating Partitioning

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.0, 0.278, 10.072, 0.722]]
  - Reducing Synchronization By Alternating Partitioning
- Shape 117 [TEXT_BOX (17); name=object 129; pos_in=[1.085, 1.322, 8.882, 0.278]]
  - Row-wise partitioning      Column-wise partitioning                       Row-wise partitioning
- Shape 66 [TABLE (19); name=object 71; pos_in=[4.117, 2.345, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 78 [TEXT_BOX (17); name=object 84; pos_in=[6.583, 2.381, 0.14, 0.24]]
  - +
- Shape 5 [TABLE (19); name=object 4; pos_in=[1.293, 2.386, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 6 [TABLE (19); name=object 5; pos_in=[2.406, 2.386, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 7 [TABLE (19); name=object 6; pos_in=[3.013, 2.386, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 36 [TABLE (19); name=object 38; pos_in=[5.187, 2.386, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 118 [TABLE (19); name=object 31; pos_in=[5.2, 2.386, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 63 [TABLE (19); name=object 68; pos_in=[7.232, 2.386, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 88 [TABLE (19); name=object 97; pos_in=[7.833, 2.393, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 87 [TABLE (19); name=object 96; pos_in=[8.946, 2.393, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 89 [TABLE (19); name=object 98; pos_in=[9.554, 2.393, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 8 [TEXT_BOX (17); name=object 7; pos_in=[2.15, 2.534, 0.759, 0.39]]
  - ×	=
- Shape 43 [TEXT_BOX (17); name=object 46; pos_in=[4.932, 2.534, 0.759, 0.39]]
  - ×	=
- Shape 90 [TEXT_BOX (17); name=object 99; pos_in=[8.691, 2.541, 0.759, 0.39]]
  - ×	=
- Shape 33 [TEXT_BOX (17); name=object 35; pos_in=[0.014, 2.549, 1.015, 0.278]]
  - Worker 0
- Shape 67 [TABLE (19); name=object 72; pos_in=[4.117, 3.526, 0.712, 0.794]] TABLE
  - TABLE_ROW:  |  | 
- Shape 16 [TABLE (19); name=object 16; pos_in=[1.293, 3.567, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 64 [TABLE (19); name=object 69; pos_in=[7.239, 3.567, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 98 [TABLE (19); name=object 108; pos_in=[7.833, 3.575, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 17 [TEXT_BOX (17); name=object 17; pos_in=[2.15, 3.715, 0.759, 0.39]]
  - ×	=
- Shape 51 [TEXT_BOX (17); name=object 55; pos_in=[4.932, 3.715, 0.759, 0.39]]
  - ×	=
- Shape 99 [TEXT_BOX (17); name=object 109; pos_in=[8.691, 3.722, 0.759, 0.39]]
  - ×	=
- Shape 34 [TEXT_BOX (17); name=object 36; pos_in=[0.019, 3.756, 1.015, 0.277]]
  - Worker 1
- Shape 81 [TEXT_BOX (17); name=object 88; pos_in=[6.586, 3.804, 0.14, 0.24]]
  - +
- Shape 52 [TABLE (19); name=object 56; pos_in=[4.117, 4.687, 0.712, 0.796]] TABLE
  - TABLE_ROW:  |  | 
- Shape 18 [TABLE (19); name=object 18; pos_in=[1.293, 4.728, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 65 [TABLE (19); name=object 70; pos_in=[7.232, 4.728, 0.204, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 100 [TABLE (19); name=object 110; pos_in=[7.833, 4.736, 0.796, 0.713]] TABLE
  - TABLE_ROW: 
  - TABLE_ROW: 
  - TABLE_ROW: 
- Shape 35 [TEXT_BOX (17); name=object 37; pos_in=[0.02, 4.876, 1.015, 0.277]]
  - Worker 2
- Shape 28 [TEXT_BOX (17); name=object 29; pos_in=[2.15, 4.876, 0.759, 0.39]]
  - ×	=
- Shape 62 [TEXT_BOX (17); name=object 67; pos_in=[4.932, 4.876, 0.759, 0.39]]
  - ×	=
- Shape 110 [TEXT_BOX (17); name=object 121; pos_in=[8.691, 4.883, 0.759, 0.39]]
  - ×	=
- Shape 84 [TEXT_BOX (17); name=object 92; pos_in=[6.625, 5.2, 0.14, 0.24]]
  - +
- Shape 74 [TEXT_BOX (17); name=object 80; pos_in=[6.185, 6.048, 1.593, 0.539]]
  - Communication:  Allreduce
- Shape 32 [TEXT_BOX (17); name=object 34; pos_in=[1.67, 6.049, 1.168, 0.277]]
  - Layer K fwd
- Shape 76 [TEXT_BOX (17); name=object 82; pos_in=[4.153, 6.049, 1.676, 0.277]]
  - Layer (K + 1) fwd
- Shape 116 [TEXT_BOX (17); name=object 128; pos_in=[7.986, 6.056, 1.676, 0.277]]
  - Layer (K + 2) fwd
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 73
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Fwd communication:
- Reduce_scatter: each worker needs partial activations at next layer

---

## Slide 74
**Title:** Intra-Layer Parallel: Communication

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.083, 0.253, 9.661, 0.722]]
  - Intra-Layer Parallel: Communication
- Shape 4 [TEXT_BOX (17); name=object 3; pos_in=[0.25, 1.269, 10.522, 5.256]]
  - Row-wise in forward becomes Col-wise in backward
  - Col-wise in forward becomes Row-wise in backward
  - Row-wise:
  - Fwd: allgather
  - Bwd: reduce_scatter
  - Col-wise:
  - Fwd: reduce_scatter
  - Bwd: allgather
  - When row- and col- are alternated:
  - Allreduce every two layers, in fwd and bwd
  - Halves the synchronizations compared to not alternating
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 74
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

**Notes:**
- Fwd communication:
- Reduce_scatter: each worker needs partial activations at next layer

---

## Slide 75
**Title:** Tensor Parallelism for Transformer Block

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Tensor Parallelism for Transformer Block
- Shape 7 [AUTO_SHAPE (1); name=矩形 10; pos_in=[5.813, 1.085, 1.632, 0.404]]
  - Column-wise
- Shape 9 [AUTO_SHAPE (1); name=矩形 4; pos_in=[7.833, 1.085, 1.247, 0.404]]
  - Row-wise
- Shape 6 [AUTO_SHAPE (1); name=矩形 2; pos_in=[0.5, 1.116, 1.632, 0.404]]
  - Column-wise
- Shape 8 [AUTO_SHAPE (1); name=矩形 3; pos_in=[3.369, 1.126, 1.247, 0.404]]
  - Row-wise
- Shape 5 [PICTURE (13); name=图片 1; pos_in=[-0.007, 1.509, 10.0, 1.648]] PICTURE
- Shape 4 [TEXT_BOX (17); name=object 4; pos_in=[0.341, 3.639, 9.167, 1.247]]
  - Tensor Parallelism:
  - Attention: column-wise + row-wise.
  - MLP: column-wise + row-wise.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 75
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 30; pos_in=[1.858, 7.096, 7.649, 0.37]]
  - [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

---

## Slide 76
**Title:** Outline

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Outline
- Shape 3 [AUTO_SHAPE (1); name=Rectangle 4; pos_in=[0.57, 1.542, 8.5, 5.119]]
  - Why Distributed Training？
  - Data Parallelism
  - Model Parallelism
  - Pipeline
  - Intra-layer
  - Communication Pattern Review
  - Summary
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 76

---

## Slide 77
**Title:** Communication Pattern Summary

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Communication Pattern Summary
- Shape 3 [TEXT_BOX (17); name=object 3; pos_in=[0.25, 1.25, 9.583, 5.297]]
  - Data Parallel:
  - Allreduce of weights
  - Can be overlapped with computation
  - 
  - Pipeline Parallel:
  - Point-wise communication of activations and activation gradients
  - Hard to overlap with computation
  - Hard to load-balance
  - 
  - Tensor Parallel:
  - Allgather, Reduce_scatter of activations and activation gradients
  - Allreduce if row-wise and col-wise partitioning is alternated
  - Hard to overlap with computation
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 77

---

## Slide 78
**Title:** Memory Size for a Huge Model

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Memory Size for a Huge Model
- Shape 3 [TEXT_BOX (17); name=object 3; pos_in=[0.25, 1.25, 9.583, 3.131]]
  - Memory Size Needed when Training GPT3-175B
  - Optimizer: 3259 GB
  - Parameters
  - Gradients
  - Optimizer states
  - Activation (without checkpoint): 360 GB （seq=1024，bsz=8）
  - Activation (with checkpoint): 3.75 GB （seq=1024，bsz=8， each block ）
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 78

---

## Slide 79
**Title:** 基于transformer的模型的显存占用

- Shape 1 [PLACEHOLDER (14); name=标题 1; pos_in=[0.083, 0.25, 5.659, 0.755]]
  - 基于transformer的模型的显存占用
- Shape 2 [PICTURE (13); name=图片 4; pos_in=[0.0, 1.083, 10.0, 1.799]] PICTURE
- Shape 3 [TEXT_BOX (17); name=文本框 5; pos_in=[0.0, 3.065, 10.0, 3.4]]
  - Transformer layer
  - 	param : 		12 * hid * hid
  - 	activation : 	20 * bsz * seq * hid + n_h * bsz * seq * seq （QK乘积）
  - 
  - Embedding
  - 	param : 		voc * hid
  - 	activation : 	bsz * seq * hid
  - 
  - 混合精度训练：		FP32的参数，梯度和优化器参数（动量，方差）	4 * 4(byte)
  - 			FP16的参数和梯度				2 * 2(byte)
  - 			activation都是FP16的

---

## Slide 80
**Title:** AI System: Four Components

- Shape 6 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AI System: Four Components
- Shape 3 [TEXT_BOX (17); name=TextBox 9; pos_in=[4.001, 2.255, 1.733, 0.505]]
  - Computing
- Shape 4 [AUTO_SHAPE (1); name=菱形 1; pos_in=[3.567, 2.866, 2.167, 1.917]]
  - Model
  - Training
- Shape 2 [TEXT_BOX (17); name=TextBox 4; pos_in=[2.333, 3.527, 1.697, 0.505]]
  - Storage
- Shape 1 [TEXT_BOX (17); name=TextBox 2; pos_in=[5.917, 3.527, 2.11, 0.505]]
  - Networking
- Shape 5 [TEXT_BOX (17); name=TextBox 9; pos_in=[3.992, 4.878, 1.741, 0.505]]
  - Compiling

---

## Slide 81
**Title:** AI System: Storage

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - AI System: Storage
- Shape 2 [PICTURE (13); name=图片 2; pos_in=[0.0, 1.333, 10.0, 5.533]] PICTURE

---

## Slide 82
**Title:** ZeRO: Zero Redundancy Optimizer

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - ZeRO: Zero Redundancy Optimizer
- Shape 4 [PICTURE (13); name=图片 2; pos_in=[1.71, 1.083, 6.79, 3.521]] PICTURE
- Shape 3 [TEXT_BOX (17); name=object 3; pos_in=[0.23, 5.25, 9.75, 1.384]]
  - Key Idea:
  - Each GPU stores a subset of optimizer states, rather than the whole states like data parallel.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 82

---

## Slide 83
**Title:** ZeRO: Zero Redundancy Optimizer

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - ZeRO: Zero Redundancy Optimizer
- Shape 3 [PICTURE (13); name=图片 1; pos_in=[0.267, 0.984, 8.901, 4.583]] PICTURE
- Shape 4 [AUTO_SHAPE (1); name=矩形 3; pos_in=[0.25, 5.567, 8.25, 0.993]]
  - Benefit:
  - Training a larger model.
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 83

---

## Slide 84
**Title:** Overhead of ZeRO: More Communication

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.5, 1.167]]
  - Overhead of ZeRO: More Communication
- Shape 3 [PICTURE (13); name=图片 2; pos_in=[0.475, 1.045, 4.236, 5.793]] PICTURE
- Shape 6 [AUTO_SHAPE (1); name=矩形 5; pos_in=[4.653, 1.321, 1.757, 0.64]]
  - Typical PyTorch step:
- Shape 13 [AUTO_SHAPE (1); name=Data Ar; pos_in=[6.0, 2.707, 3.801, 0.639]]
  - Overhead: more collectives
- Shape 9 [AUTO_SHAPE (1); name=矩形 14; pos_in=[4.653, 3.943, 1.757, 0.37]]
  - Forward:
- Shape 11 [AUTO_SHAPE (1); name=矩形 17; pos_in=[4.647, 5.477, 1.757, 0.37]]
  - Backward:
- Shape 12 [AUTO_SHAPE (1); name=矩形 18; pos_in=[4.661, 6.468, 1.757, 0.37]]
  - Optimizer:
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 84

---

## Slide 85
**Title:** Summary

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Summary
- Shape 3 [TEXT_BOX (17); name=object 3; pos_in=[0.083, 0.963, 9.75, 6.2]]
  - Networks and dataset are getting larger to set new state of art results
  - Scale-out enables these neural networks to be trained
  - Success requires many optimized components:
  - Hardware:
  - Fast accelerators for DL
  - High-bandwidth, low-latency interconnects
  - Topologies matter (must match communication patterns)
  - Network switches with math capabilities free up DL accelerators to do compute
  - SmartNIC for offloaded compression/decompression
  - Software:
  - Math libraries (CUDNN, CUBLAS, MKL, CANN …)
  - Collective communication libraries (NCCL, Horovod,  …)
  - Training frameworks (MindSpore, PyTorch, TensoFlow, HugeCTR, …)
  - Proper choice of parallelism (manual, MeshTensorFlow, Gshard, ZeRO)
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 85

---

## Slide 86
**Title:** Batch Size Limitation of LLM Training

- Shape 1 [PLACEHOLDER (14); name=Title 1; pos_in=[0.25, 0.167, 9.417, 1.167]]
  - Batch Size Limitation of LLM Training
- Shape 3 [TEXT_BOX (17); name=object 4; pos_in=[0.245, 1.492, 9.5, 1.71]]
  - Batch Size Limitation of LLM Training
  - Llama: 4M token,
  - Seq length: 4K,
  - Batch size: 1K
- Shape 4 [TEXT_BOX (17); name=object 4; pos_in=[0.25, 4.235, 6.917, 1.43]]
  - How to choose the parallel training strategy?
  - When you have 1K NPU/GPU?
  - When you have 10K NPU/GPU?
- Shape 2 [PLACEHOLDER (14); name=Slide Number Placeholder 3; pos_in=[7.411, 6.91, 2.333, 0.5]]
  - 86