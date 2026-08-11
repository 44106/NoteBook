# ???-????.pptx ??????

Slides: 73

## Slide 1
### Text 1
课程名称：深度学习导论

### Text 2
第八章：表征学习

### Text 3
主讲教师：王文冠


## Slide 2
### Text 1
一、图像的表征学习


## Slide 3
### Text 1
什么是表征？

### Text 2
表征是对数据含义的编码，是对原始数据的映射

### Text 3
表征提取

### Text 4
表征向量空间

### Text 5
好的表征使得“语义相似”=“几何接近”


## Slide 4
### Text 1
传统表征提取模式：特征工程

### Text 2
Scale-Invariant Feature Transform (SIFT)

### Text 3
Histogram of Oriented Gradients (HOG)


## Slide 5
### Text 1
传统表征提取模式：特征工程

### Text 2
特征工程的缺陷：
需要人工设计特征模式，需要领域经验，设计成本高
只能表达局部语义，难以捕捉复杂语义，难以建模非线性结构
泛化能力弱，需要对任务针对性的设计特征


## Slide 6
### Text 1
现代范式：表征学习

### Text 2
数据驱动代替人工设计，用模型来学习表征

### Text 3
表征 z=f(x)

### Text 4
原始数据 x

### Text 5
Encoder f

### Text 6
常见范式：监督学习（依赖下游任务标注）、自监督学习（依赖数据自身特性）


## Slide 7
### Text 1
为什么需要表征学习？

### Text 2
② 捕获数据语义

### Text 3
① 降低数据维度

### Text 4
③ 提升泛化能力

### Text 5
人工设计表征

### Text 6
下游任务1

### Text 7
表征
学习

### Text 8
下游任务2

### Text 9
下游任务3


## Slide 8
### Text 1
如何评估表征的好坏？

### Text 2
① Linear Probing：
在下游任务上，用学好的表征和标签来训练一个线性分类器，用分类效果来评判表征的语义表达能力

### Text 3
② 可视化观察聚类效果：
可以对高维表征进行降维可视化，观察是否形成自然的聚类，类间是否分离，类内是否紧凑（PCA、T-SNE算法）

### Text 4
y

### Text 5
Linear Classifier

### Text 6
Encoder

### Text 7
x


## Slide 9
### Text 1
有监督表征学习 vs 无监督/自监督学习

### Text 2
有监督表征学习

### Text 3
Encoder f

### Text 4
Classifier g

### Text 5
Dog

### Text 6
表征 z=f(x)

### Text 7
标签 y

### Text 8
原始数据 x

### Text 9
Encoder f

### Text 10
Classifier g

### Text 11
无监督表征学习

### Text 12
0°
90°
180°
270°

### Text 13
…

### Text 14
表征 z=f(x)

### Text 15
原始数据 x

### Text 16
自监督标签


## Slide 10
### Text 1
有监督表征学习 vs 无监督/自监督学习

### Text 2
本节主要专注于无监督/自监督表征学习


## Slide 11
### Text 1
什么是 Pretext 任务？

### Text 2
核心思想：摒弃人工标注，以数据自身属性为“伪标签”，通过解决人为设计的代理任务，间接习得数据的语义特征。

### Text 3
原始图像

### Text 4
自动变换

### Text 5
伪标签

### Text 6
预训练模型

### Text 7
下游任务

### Text 8
未标注数据

### Text 9
旋转 / 打乱 / 灰度化 / 取 patch

### Text 10
角度 / 排列 / 相对位置 / 颜色

### Text 11
学习视觉表示

### Text 12
分类 / 检测


## Slide 12
### Text 1
Pretext 任务---旋转预测（Rotation Prediction）

### Text 2
训练方式：把一张自然图像随机旋转为 0°、90°、180°、270°，再让模型预测旋转角度（4分类问题）
模型通常需要识别主体轮廓、部件朝向与场景重力方向，才能判断角度


## Slide 13
### Text 1
Pretext 任务---旋转预测（Rotation Prediction）

### Text 2
训练
使用构造的标签训练

### Text 3
训练
使用下游任务标签训练

### Text 4
迁移

### Text 5
模型层
常规Backbone（如RestNet）

### Text 6
模型层
微调已经训练的Backbone

### Text 7
数据层
构造pretext数据集

### Text 8
数据层
下游任务数据


## Slide 14
### Text 1
Pretext 任务---相对位置预测（Context Prediction）

### Text 2
从同一张图像中采样两个 patch，让模型预测第二个 patch 相对第一个 patch 位于哪个方向（8分类）

### Text 3
如果认识这个物体，那判断相对位置应该很简单


## Slide 15
### Text 1
Pretext 任务---拼图游戏（Jigsaw Puzzle）

### Text 2
对图片进行分块并打乱，训练模型进行permutation的分类（排列空间从9!=362,880，选择100种）
帮助模型学习局部之间的空间关系，以及从局部推断全局物体结构的能力


## Slide 16
### Text 1
Pretext 任务---着色（Colorization）

### Text 2
把彩色图变成灰度图，再让模型恢复颜色
颜色往往依赖语义：天空通常偏蓝，植被偏绿，皮肤、道路、海面也各有统计规律；着色任务使模型关注纹理与材质、区域类别与场景上下文、同一物体内部的颜色连续性


## Slide 17
### Text 1
不同 Pretext 任务的效果比较

### Text 2
不同的无监督方法在ImageNet-1000分类任务上的效果（冻结表征+MLP）


## Slide 18
### Text 1
Pretext 任务的局限性

### Text 2
局限性：
泛化性有限：模型可能学会“如何解这道题”，却不一定得到对下游任务最有用的通用表示
可能出现学习捷径：例如通过边缘连续性、颜色分布或相机伪影取巧，而不是理解高层语义
自监督学习的发展：

### Text 3
2016

### Text 4
2018

### Text 5
2020

### Text 6
2021

### Text 7
2022

### Text 8
Jigsaw

### Text 9
Colorization

### Text 10
SimCLR / BYOL

### Text 11
DINO

### Text 12
MAE

### Text 13
RotNet

### Text 14
教师-学生

### Text 15
掩码重建

### Text 16
角度标签

### Text 17
视角一致性

### Text 18
空间关系

### Text 19
语义颜色


## Slide 19
### Text 1
二、对比学习：从依赖标签到实例判别


## Slide 20
### Text 1
对比学习

### Text 2
Pretext 任务教会了模型“如何玩游戏”，但我们真正需要的是模型能“区分谁是谁”
-> 对比学习：在特征空间中，拉近同类事物，推远不同事物，让模型学会区分万物。

### Text 3
拉近本源
推开异源
直击语义

### Text 4
回归本质

### Notes
前面我们介绍了很多 pretext 任务，比如预测相对位置、做拼图、颜色恢复等等。这些任务的共同特点是：我们先人为设计一个“游戏规则”，再让模型去完成这个游戏。这样做当然有用，因为模型在玩这些游戏的过程中，确实能学到一些纹理、边缘、局部结构，甚至物体部件之间的关系。但是问题也很明显：模型学会的，很多时候只是“怎么把这个游戏玩好”，却不一定真正学会“怎么把世界区分清楚”。

于是大家就开始想：我们真正需要的表征，到底应该具备什么性质？答案其实很自然，就是在特征空间里，相似的东西应该靠近，不相似的东西应该远离。 这就是对比学习的核心思想。
大家看右边这张图。中间这个圆可以理解成特征空间，周围每个点是图像经过神经网络编码之后得到的 embedding，也就是特征向量。对于同一个对象的不同视图，比如同一只小狗经过裁剪、旋转、颜色扰动之后得到的几张图片，我们希望它们在特征空间里彼此靠近，因为它们本质上还是同一个语义对象，这叫正样本，也就是 positives。而对于其他对象，比如猫，或者另一类狗，甚至背景差异很大的图像，我们希望它们离当前样本更远，这就是负样本，也就是 negatives。


## Slide 21
### Text 1
对比学习

### Text 2
监督对比学习：需要人工标注哪些属于同类事物，哪些属于不同类事物 -> 成本太高
自监督对比学习：通过数据变换自动构建正负样本对用于模型训练 -> free lunch!


## Slide 22
### Text 1
SimCLR

### Text 2
SimCLR 框架: 对每张图施加两种不同的数据增强，形成一对互为“正样本”的分身。模型的目标就是识别出这些分身属于同一母体，并同时排斥 batch 内的所有其他图片。

### Text 3
展示出自监督特征仅用 1% 标签微调就能超越 AlexNet 的惊人潜力！

### Text 4
A Simple Framework for Contrastive Learning of Visual Representations. ICML2020.


## Slide 23
### Text 1
SimCLR

### Text 2
数据增强（Data augmentation）: 在保留数据原本含义的前提下，通过旋转、翻转等方式对现有数据进行变换，从而创造出更多新样本。

### Text 3
关键发现：
- 数据增强组合对自监督学习质量起决定性作用
- 单纯的随机裁剪往往效果不佳（模型作弊），必须与 “颜色抖动” 结合使用


## Slide 24
### Text 1
SimCLR

### Text 2
基础编码器（Base Encoder）: 通常采用经典的卷积神经网络（如 ResNet），作为模型的“主干”负责将原始图像转化为高维特征向量，旨在捕捉图像中核心的语义内容。


## Slide 25
### Text 1
SimCLR

### Text 2
投影头（Projector）: 专门负责吸收和过滤掉那些对对比任务有用、但对通用识别没用的冗余信息（颜色、位置），保护前面的编码器能学到更纯净、更本质的语义特征。


## Slide 26
### Text 1
SimCLR

### Text 2
对比损失（NT-Xent 损失）: 最大化同一图像不同增强视图（正样本对）之间的相似度，同时最小化不同图像（负样本对）之间的相似度。


## Slide 27
### Text 1
SimCLR

### Text 2
下游任务应用: 经过 SimCLR 训练之后的模型可以用于迁移学习。为此，使用来自基础编码器的表示，这些表示可以很好地应用于像 ImageNet 分类这样的下游任务。


## Slide 28
### Text 1
MoCo——动量更新Encoder

### Text 2
需要更多负样本的另一种解决方案:引入样本队列记住负样本的特征；使用非对称更新的方式，让其中一个Encoder以动量的形式进行更新
注：SimCLR发表更晚消融更全面，发现算力充足不如直接开大Batch

### Text 3
1. 引入一个队列记住mini-batch的负样本

### Text 4
2. 让右侧的Encoder以Exponential Moving Average的方式逐步更新：

### Text 5
3. 把当前的key feature压入队列中


## Slide 29
### Text 1
对比学习家族


## Slide 30
### Text 1
三、单词的表征学习


## Slide 31
### Text 1
One-hot向量

### Text 2
在传统NLP中，每个单词可以被看作离散的符号，这些符号可以被表示为One-hot向量形式：
该向量的维度=词表Vocabulary中词汇的数量（如，500000个）

### Text 3
火车 = [0, 0, 0, 0, 0, 1, 0, 0]
高铁 = [0, 0, 0, 1, 0, 0, 0, 0]


## Slide 32
### Text 1
从One-hot到Embedding

### Text 2
当我们想要搜索“去杭州的火车”时，也隐含了我们想搜索“去杭州的高铁”，但是在One-hot表征下“火车”和“高铁”是正交的——One-hot向量无法体现语义相似度

### Text 3
火车 = [0, 0, 0, 0, 0, 1, 0, 0]
高铁 = [0, 0, 0, 1, 0, 0, 0, 0]

### Text 4
解决方案：通过表征学习得到能够包含词汇语义的表征


## Slide 33
### Text 1
通过上下文表示单词

### Text 2
一个词的含义是由经常出现在它附近的词语决定的


## Slide 34
### Text 1
Word2vec算法

### Text 2
Word2vec (Mikolov et al. 2013, ICLR Workshop)


## Slide 35
### Text 1
Word2vec算法的思想

### Text 2
统计语言模型——最大化文本语料的概率

### Text 3
词表为N次共有N^T的可能性！！


## Slide 36
### Text 1
Word2vec算法的思想

### Text 2
前提：有一个大的语料库
词表Vocabulary中每个单词由一个向量表示
对于文本中的每个位置t，有一个中心词c和上下文o
可以通过c和o的向量相似度，来计算当中心词是c时上下文是o的概率（或当上下文是o时中心词是c的概率）
通过调整单词的向量，使得语料库中上述概率最大化


## Slide 37
### Text 1
Word2vec算法的思想

### Text 2
两种变体：Skip-gram（中心词预测上下文）；CBOW（上下文预测中心词）

### Text 3
下面以Skip-gram为例介绍
（避免高频词淹没）


## Slide 38
### Text 1
Word2vec算法的思想


## Slide 39
### Text 1
Word2vec算法的思想


## Slide 40
### Text 1
Word2vec算法的目标函数

### Text 2
t：单词在文本中的位置
m：上下文窗口的大小，如5

### Text 3
求log平均，得到损失函数


## Slide 41
### Text 1
Word2vec算法的目标函数

### Text 2
中心词向量和上下文向量分开更加灵活，有利于模型优化

### Text 3
V表示词表Vocabulary中的所有单词


## Slide 42
### Text 1
Word2vec算法的优化——Negative Sampling

### Text 2
问题：
对于每一个上下文o，需要计算其与词表V中所有单词的相似度，复杂度极高
如何解决？
无需计算词表中所有单词，采样负样本
多分类 → 多个二分类

### Text 3
鼓励真实的上下文其向量相似度与中心词高，其他的负样本向量相似度与中心词低


## Slide 43
### Text 1
Word2vec算法的优化——层次Softmax

### Text 2
另一个解决方案：
多分类 → 多个二分类
构建二叉树，每个叶子节点对应词表中的一个单词，非叶子节点为二分类器
将Softmax转化为中心词向量从根节点一直到叶子节点二分类概率的连乘
优化：使用基于词频的Huffman树，高词频对应更短的路径，加快速度


## Slide 44
### Text 1
从局部上下文预测到全局统计

### Text 2
语义关系是否可以直接从“全局统计结构”中恢复？——GloVe

### Text 3
GloVe (Pennington et al. 2014, EMNLP)


## Slide 45
### Text 1
从局部上下文预测到全局统计

### Text 2
现象：单词共现矩阵（co-occurrence matrix）蕴含了相似度语义


## Slide 46
### Text 1
GloVe算法的思想与目标函数

### Text 2
核心思想：学习表征向量使单词之间的向量相似度拟合共现次数
目标函数：最小化
X：共现矩阵
i：中心词
j：上下文词
v：可学习的单词向量
对词频进行log缩小频率差距；b：偏置项，提高拟合的灵活性
f是权重参数，平衡高频词和低频词的训练比重


## Slide 47
### Text 1
表征的线性结构

### Text 2
woman – man + king = queen


## Slide 48
### Text 1
四、文本数据的自监督学习


## Slide 49 (hidden)
### Text 1
RNN和LSTM基本概念

### Text 2
② LSTM (Long Short-Term Memory)
针对长序列数据，普通RNN梯度会指数级衰减或膨胀，导致遗忘久远历史信息
LSTM引入遗忘门、输入门和输出门改进了RNN的隐藏状态传递方式。进而可以有选择地保留关键信息，丢弃无关内容

### Text 3
① RNN (Recurrent Neural Networks)：
需要针对序列数据的上下文连续建模能力
当前时刻的输出同时取决于当前输入和前一时刻的隐藏状态，递归传递历史信息

### Text 4
注：本节课我们不关注具体架构细节


## Slide 50
### Text 1
Transformer——可扩展序列建模基座

### Text 2
RNN/CNN序列建模并行性、长程依赖差
Self-Attention+并行训练 → “规模化预训练”
突破并行瓶颈：允许序列中所有位置同时计算。
解决长程依赖：任意两个词的距离都被视为 1.
开启Scaling Law：使得利用海量数据训练超大参数模型成为可能。
Attention Is All You Need
核心思想：不再需要复杂的循环神经网络或卷积神经网络来提取表征。

### Text 3
注：本节课我们不关注具体架构细节


## Slide 51 (hidden)
### Text 1
ELMo

### Text 2
Word2Vec为每个词赋予唯一向量，无法解决一词多义，下游依赖大量人工标注。

### Text 3
ELMo (Embeddings from Language Models)
训练两个独立方向LSTM（左→右和右→左），将同一词在两组LSTM顶层产生的隐藏状态与原始词向量拼接，形成随上下文动态变化的深层语境化表征

### Text 4
局限：由于两个LSTM独立训练、参数不共享，上下文信息仅在最后阶段进行浅层拼接，无法实现词语间的深层双向交互与融合。


## Slide 52
### Text 1
BERT动机

### Text 2
BERT (Bidirectional Encoder Representations from Transformers) 旨在通过自注意力使每一层都同时编码两侧上下文，实现更深层的双向理解

### Text 3
早期LSTM-序列预测

### Text 4
Transformer-双向全连接
（更兼容预训练）


## Slide 53
### Text 1
BERT核心机制

### Text 2
去噪自编码：随机15%掩码，利用上下文重建（完形填空！）

### Text 3
随机选择输入序列中15%的token进行遮挡处理，迫使模型利用被遮挡位置左右的所有可见上下文来预测原始词汇

### Text 4
通过去噪自编码机制，强制模型深度整合上下文进行语义推理，而非依赖单侧序列


## Slide 54
### Text 1
BERT核心机制

### Text 2
双向掩码预测：每个被遮挡位置基于双向上下文输出词表概率分布

### Text 3
在Transformer Encoder输出层，被遮挡位置对应的隐藏向量经简单分类头映射到词表空间，通过softmax分布预测原始token

### Text 4
M 是被遮挡位置的索引集合，x\M 为其余可见token

### Text 5
单向生成 → 双向去噪，为深度语义理解表征奠定基础


## Slide 55
### Text 1
BERT优势与应用

### Text 2
优势：BERT通过双向去噪自编码预训练，在多项语言理解基准上显著超越此前的静态词向量与单向模型

### Text 3
通过为不同理解任务设计简单的输出层（如分类头或起止位置预测），BERT表征可直接支持情感分析、语义推理、问答抽取与实体识别等任务


## Slide 56
### Text 1
BERT局限

### Text 2
训练规模保守，模型潜力尚未激发——Scaling Law
引入的句级NSP (Next Sentence Prediction)辅助任务以及输入格式可能分散核心掩码——消融实验探究


## Slide 57
### Text 1
RoBERTa——Scaling Law

### Text 2
RoBERTa (Robustly optimized BERT approach) 在保持BERT架构完全不变的前提下，改变了训练规模：
训练数据：16GB → 160GB
步数：100K → 500K

### Text 3
Scaling Law：架构不变的情况下，仅通过扩大数据规模、增加训练步数，可收获明显性能提升。说明训练充分性比架构创新更能决定预训练模型上限。


## Slide 58
### Text 1
RoBERTa——消融探究

### Text 2
RoBERTa 移除NSP辅助任务，改变输入格式，进行了消融实验探究

### Text 3
聚焦学习目标：预训练任务的设计应聚焦于核心表征学习目标，冗余的辅助任务不仅非必需，还可能干扰模型对深层语义结构的捕捉


## Slide 59
### Text 1
NTP回归——从理解到生成

### Text 2
BERT双向去噪——理解路线
NTP (Next Token Prediction)单向预测下一个token——生成路线

### Text 3
NTP将序列建模为条件概率的连乘积，模型只能依赖左侧已生成内容来推断后续token，这种单向约束使其在生成流畅文本上具有先天优势

### Text 4
NTP确立了自回归生成的训练范式，为GPT系列将技术路线从理解转变为生成奠定了目标函数基础


## Slide 60
### Text 1
GPT系列

### Text 2
NTP的规模化与能力涌现：GPT (Generative Pre-trained Transformer)系列

### Text 3
从GPT-1到GPT-3，OpenAI坚持decoder-only自回归架构，通过参数与数据规模的指数级扩展，证明规模化本身足以驱动性能从“需要微调”提升至“上下文即学习”

### Text 4
GPT系列将NTP从学术验证推向工程化规模化，以175B参数宣告大模型时代来临，并催生了以提示驱动模型的新交互范式


## Slide 61
### Text 1
ChatGPT

### Text 2
在GPT-3.5基础上引入RLHF (Reinforcement Learning from Human Feedback)，将模型输出与人类偏好对齐

### Text 3
ChatGPT证明，在规模化预训练之后，对齐技术是激发生成模型实用价值的一个里程碑，为后续大模型产品化确立了预训练+对齐的标准路径


## Slide 62
### Text 1
Chinchilla动机

### Text 2
基于Scaling Law，GPT-3后大模型普遍进行盲目扩参。性能提升唯一解法？

### Text 3
Chinchilla以与Gopher相同的计算预算、仅1/4的参数和4.7倍的数据，在广泛下游任务上全面超越Gopher、GPT-3、Jurassic-1及MT-NLG 530B

### Text 4
结论：在相同计算预算下，主流大模型严重训练不足。缩小模型规模并等比例增加数据量，可获得更优的下游性能


## Slide 63
### Text 1
Chinchilla最优配比

### Text 2
Chinchilla通过对400余个模型（70M~16B参数）的训练曲线进行三种独立拟合，发现计算最优条件下模型规模与训练token数应近似等比例增长。推翻了此前结论“扩参远快于扩数据”

### Text 3
模型规模与数据规模应随计算预算近似等比例扩展，约20:1的token-参数比成为计算最优训练的核心约束


## Slide 64
### Text 1
Chinchilla启示

### Text 2
Chinchilla表明，在固定计算预算下追求更大模型导致严重欠训练
预训练的竞争指标应该从参数量转变为单位计算量的性能效率

### Text 3
图中标注了Chinchilla(70B)、Gopher(280B)、GPT-3(175B)及MT-NLG(530B)的位置
显示当前主流大模型均显著偏离最优前沿


## Slide 65
### Text 1
Chinchilla工程优势与伦理挑战

### Text 2
Chinchilla不仅以更小模型获得更强性能，还显著降低了推理与微调的计算开销

### Text 3
工程优势
更优的模型并不一定需要更大的部署开销
伦理挑战
更大规模的数据将不可避免地包含有毒信息、社会偏见与私人信息。随着训练数据量级不断提高，数据集的质量控制、训练-测试重叠检测以及伦理审查变得至关重要


## Slide 66
### Text 1
图像与文本自监督学习的区别

### Text 2
语言 NLP：离散符号与天然序列文本由离散 Token 组成，天然具备顺序、句法和上下文依赖，模型可直接通过掩码预测学习深层语义。

### Text 3
图像 CV：连续信号与语义鸿沟图像是连续像素信号，局部像素相似性并不代表语义理解，所以我们考虑了构造代理任务来帮助表征学习。

### Text 4
但是……图像能不能也像文本那样学习呢？


## Slide 67
### Text 1
图像掩码重建（Masked Image Modeling）

### Text 2
核心思想：基于掩码的重建与理解 -> “通过残缺理解整体”
通过遮挡图像75%的区域，迫使模型利用仅存的可见部分去重建全局内容，从而跳出局部纹理的局限，真正习得物体结构与语义关联。

### Text 3
BERT：mask 15% token → 预测缺失词
MIM：mask 75% patches → 重建缺失图像块


## Slide 68
### Text 1
MAE

### Text 2
计算聚焦策略：利用 75% 的高比例遮挡，让 Encoder 仅处理 25% 的可见图块，将计算资源集中在对核心语义的理解上，避免算力浪费

### Text 3
非对称高效架构：重型 Encoder 学习强表征，轻型 Decoder 仅负责像素重建，解耦了学习与重建，将训练速度提升了 3-5 倍。

### Text 4
说明了：高比例 Mask 不仅能够学习到更强的表征，还能提高效率！


## Slide 69
### Text 1
图像序列预测（Image Sequence Prediction）

### Text 2
iGPT：将图像展平为像素序列，类比文本生成逻辑，采用 Transformer Decoder 架构，通过自回归方式依据前序像素预测下一像素，实现图像序列的生成式建模。

### Text 3
问题：计算量极大（序列太长），且像素级的自回归预测在视觉上不如掩码重建有效！


## Slide 70
### Text 1
SimMIM

### Text 2
直接对图像块进行随机掩码并通过轻量预测头回归原始像素值。这种无需离散化或复杂结构的方案，不仅大幅降低了计算成本，还能适配 ViT、Swin 等多种骨干网络。


## Slide 71
### Text 1
自监督表征学习总结


## Slide 72
### Text 1
广泛应用

### Text 2
自监督学习的核心就在于表征学习，即不依赖人工标注，而是通过从数据内部挖掘结构来自动生成监督信号，从而训练模型提取出能抓住数据本质的通用特征表示。

### Text 3
视觉领域的爆发

### Text 4
大模型的核心引擎


## Slide 73
### Text 1
发展历程

### Text 2
早期 (2015-2018)
核心：设计各种手工 Pretext 任务帮助模型理解
代表方法：Rotation, Jigsaw

### Text 3
融合期 (2021-2022)
核心：遮蔽图像建模（MIM），视觉与 NLP 架构大统一
代表方法：MAE, BEiT

### Text 4
爆发期 (2019-2020)
核心：对比学习，实例判别，从本质上学习核心特征
代表方法：SimCLR,  MoCo

### Text 5
现代 (2023-Present)
核心：多模态表征，通向通用人工智能（AGI）
代表方法：LLM, VLM
