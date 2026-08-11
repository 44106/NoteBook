# ???-??????.pptx ??????

## Slide 1: 第五章：神经网络基础（二）
- screenshot: tmp/ch5_slides_png/???1.PNG
- pictures: 1

### Shape 2/0 TEXT_BOX (17)
- 第五章：神经网络基础（二）

### Shape 4 TEXT_BOX (17)
- 主讲教师：王文冠

### Shape 5 TEXT_BOX (17)
- 课程名称：深度学习导论

## Slide 2: 基本流程
- screenshot: tmp/ch5_slides_png/???2.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 2

### Shape 2 TEXT_BOX (17)
- 基本流程

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型训练的基本流程通常包括数据准备、模型构建、训练与优化、模型评估（与超参数优化）。

### Shape 4 TEXT_BOX (17)
- 数据准备
-   归一化（Normalization）
-   数据增强（Augmentation）
-   类型转换
-   …

### Shape 6 TEXT_BOX (17)
- https://keras.io/examples/vision/mnist_convnet/

## Slide 3: 基本流程
- screenshot: tmp/ch5_slides_png/???3.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 3

### Shape 2 TEXT_BOX (17)
- 基本流程

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型训练的基本流程通常包括数据准备、模型构建、训练与优化、模型评估（与超参数优化） 。

### Shape 4 TEXT_BOX (17)
- 模型构建
-   输入层
-   隐藏层
-     丢弃层（Dropout Layer）
-     批归一化（Batch Normalization）
-     层归一化（Layer Normalization）
-   输出层
-   初始化

### Shape 5 TEXT_BOX (17)
- https://keras.io/examples/vision/mnist_convnet/

## Slide 4: 基本流程
- screenshot: tmp/ch5_slides_png/???4.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 4

### Shape 2 TEXT_BOX (17)
- 基本流程

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型训练的基本流程通常包括数据准备、模型构建、训练与优化、模型评估（与超参数优化） 。

### Shape 4 TEXT_BOX (17)
- 训练与优化
-   损失函数
-     正则化项（与传统机器学习类似）
-   优化器：SGD（随机梯度下降）、Momentum、AdaGrad、RMSProp、Adam

### Shape 5 TEXT_BOX (17)
- https://keras.io/examples/vision/mnist_convnet/

## Slide 5: 基本流程
- screenshot: tmp/ch5_slides_png/???5.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 5

### Shape 2 TEXT_BOX (17)
- 基本流程

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型训练的基本流程通常包括数据准备、模型构建、训练与优化、模型评估（与超参数优化） 。

### Shape 4 TEXT_BOX (17)
- 训练与优化
- 模型评估

### Shape 5 TEXT_BOX (17)
- https://keras.io/examples/vision/mnist_convnet/

## Slide 6: 课程思路
- screenshot: tmp/ch5_slides_png/???6.PNG

### Shape 1 PLACEHOLDER (14)
- 6

### Shape 2 TEXT_BOX (17)
- 课程思路

### Shape 3 TEXT_BOX (17)
- 深度神经网络训练的基本流程：
- 数据准备
- 模型架构
- 训练方法

## Slide 7: 课程思路
- screenshot: tmp/ch5_slides_png/???7.PNG

### Shape 1 PLACEHOLDER (14)
- 7

### Shape 2 TEXT_BOX (17)
- 课程思路

### Shape 3 TEXT_BOX (17)
- 深度神经网络训练的基本流程：
- 数据准备
- 模型架构
- 训练方法

## Slide 8: 数据准备：归一化（normalization）
- screenshot: tmp/ch5_slides_png/???8.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 8

### Shape 2 TEXT_BOX (17)
- 数据准备：归一化（normalization）

### Shape 3 AUTO_SHAPE (1)
- 数据归一化是指将不同量纲或不同取值范围的特征变换到可比较的尺度上，从而避免大数值特征在模型训练中占主导，提高训练稳定性和特征利用的公平性。

### Shape 4 TEXT_BOX (17)
- 实例：是否捐款预测

### Shape 8 TEXT_BOX (17)
- Zigzag

### XML text fragments not otherwise grouped
- 逻辑回归
- 关于单个数据
- 的梯度

## Slide 9: 数据归一化是指将不同量纲或不同取值范围的特征变换到可比较的尺度上，从而避免大数值特征在模型训练中占主导，提高训练稳定性和特征利用的公平性。
- screenshot: tmp/ch5_slides_png/???9.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 9

### Shape 2 AUTO_SHAPE (1)
- 数据归一化是指将不同量纲或不同取值范围的特征变换到可比较的尺度上，从而避免大数值特征在模型训练中占主导，提高训练稳定性和特征利用的公平性。

### Shape 3 TEXT_BOX (17)
- 实例：是否捐款预测

### Shape 6 TEXT_BOX (17)
- 数据准备：归一化（normalization）

### XML text fragments not otherwise grouped
- 常用归一化方法
- 标准化（
- Standardization
- ）：假设第
- 个特征的均值和方差分别为
- Min-Max
- 归一化（对异常值较为敏感）：
- 将特征映射到

## Slide 10: 数据准备：归一化
- screenshot: tmp/ch5_slides_png/???10.PNG
- pictures: 3

### Shape 1 PLACEHOLDER (14)
- 10

### Shape 2 TEXT_BOX (17)
- 数据准备：归一化

### Shape 3 AUTO_SHAPE (1)
- 数据归一化是指将不同量纲或不同取值范围的特征变换到可比较的尺度上，从而避免大数值特征在模型训练中占主导，提高训练稳定性和特征利用的公平性。

### Shape 4 TEXT_BOX (17)
- 实例：是否捐款预测

### Shape 7 TEXT_BOX (17)
- 逻辑回归
-   归一化前
-   归一化后

## Slide 11: 数据准备：数据增强
- screenshot: tmp/ch5_slides_png/???11.PNG
- pictures: 1
- tables: 1

### Shape 1 PLACEHOLDER (14)
- 11

### Shape 2 TEXT_BOX (17)
- 数据准备：数据增强

### Shape 3 AUTO_SHAPE (1)
- 数据增强是通过对原始样本进行旋转、翻转、裁剪、加噪声等变换，构造更多训练样本的方法，旨在扩大数据分布、提升模型泛化能力。

### Shape 4 TEXT_BOX (17)
- 图像变换

### Shape 7 TEXT_BOX (17)
- 增强训练数据的多样性

### Table 1 5
| 方法 | 描述 |
| 翻转 | 将图像水平翻转、垂直翻转或同时翻转 |
| 旋转 | 以某一个角度旋转图像 |
| 缩放 | 增大或减小图像尺寸 |
| 噪声注入 | 在图像中加入噪声 |
| 颜色空间 | 改变图像颜色通道 |
| 对比度 | 改变图像对比度 |
| 锐化 | 修改图像清晰度 |
| 平移 | 将图像水平移动、垂直移动或同时移动 |
| 裁剪 | 裁剪图像的一个子区域 |

### XML text fragments not otherwise grouped
- 描述
- 将图像水平翻转、垂直翻转或同时翻转
- 以某一个角度旋转图像
- 缩放
- 增大或减小图像尺寸
- 噪声注入
- 在图像中加入噪声
- 颜色空间
- 改变图像颜色通道
- 对比度
- 改变图像对比度
- 锐化
- 修改图像清晰度
- 平移
- 将图像水平移动、垂直移动或同时移动
- 裁剪图像的一个子区域

## Slide 12: 数据准备：数据增强
- screenshot: tmp/ch5_slides_png/???12.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 12

### Shape 2 TEXT_BOX (17)
- 数据准备：数据增强

### Shape 3 AUTO_SHAPE (1)
- 数据增强是通过对原始样本进行旋转、翻转、裁剪、加噪声等变换，构造更多训练样本的方法，旨在扩大数据分布、提升模型泛化能力。

### Shape 4 TEXT_BOX (17)
- 图像擦除：从训练图像中抹去一部分信息，迫使模型关注其它相关部分，而不仅仅是最具判别力的部分

## Slide 13: 数据准备：数据增强
- screenshot: tmp/ch5_slides_png/???13.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 13

### Shape 2 TEXT_BOX (17)
- 数据准备：数据增强

### Shape 3 AUTO_SHAPE (1)
- 数据增强是通过对原始样本进行旋转、翻转、裁剪、加噪声等变换，构造更多训练样本的方法，旨在扩大数据分布、提升模型泛化能力。

### Shape 4 TEXT_BOX (17)
- 图像混合：混合多个图像样本，模拟多目标或多标签场景

### Shape 6 TEXT_BOX (17)
- 将一张图的一部分贴到另一张图上

### Shape 7 TEXT_BOX (17)
- 按比例像素融合

### Shape 8 TEXT_BOX (17)
- 多种增强操作的加权组合

### Shape 9 TEXT_BOX (17)
- 通过频率空间操作，生成
- 形状光滑自然的掩码

## Slide 14: 数据准备：数据增强
- screenshot: tmp/ch5_slides_png/???14.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 14

### Shape 2 TEXT_BOX (17)
- 数据准备：数据增强

### Shape 3 AUTO_SHAPE (1)
- 数据增强是通过对原始样本进行旋转、翻转、裁剪、加噪声等变换，构造更多训练样本的方法，旨在扩大数据分布、提升模型泛化能力。

### Shape 4 TEXT_BOX (17)
- 文本数据：回译法

## Slide 15: 数据准备：数据增强
- screenshot: tmp/ch5_slides_png/???15.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 15

### Shape 2 TEXT_BOX (17)
- 数据准备：数据增强

### Shape 3 AUTO_SHAPE (1)
- 数据增强是通过对原始样本进行旋转、翻转、裁剪、加噪声等变换，构造更多训练样本的方法，旨在扩大数据分布、提升模型泛化能力。

### Shape 4 TEXT_BOX (17)
- 文本数据：回译法
- 文本数据：随机词替换

### Shape 6 TEXT_BOX (17)
- 原始文本：
- 今天天气很好。

### Shape 7 TEXT_BOX (17)
- 同意词替换：
- 今天天气不错。

### Shape 8 TEXT_BOX (17)
- 随机插入：
- 今天不错天气很好。

### Shape 9 TEXT_BOX (17)
- 随机交换：
- 今天很好天气。

### Shape 10 TEXT_BOX (17)
- 随机删除：
- 今天天气好。

## Slide 16: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???16.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 16

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 数值型数据（Numerical Data）：连续有序
-   图像数据的像素值
- 类别型数据（Categorical Data）：离散无序

## Slide 17: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???17.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 17

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 5 AUTO_SHAPE (1)
- 二值化！

### Shape 7 TEXT_BOX (17)
- 1st  Category

### Shape 9 TEXT_BOX (17)
- 2nd Category

### Shape 11 TEXT_BOX (17)
- 3rd  Category

### XML text fragments not otherwise grouped
- 类别型数据（
- Categorical Data
- ）：离散无序
- 二类：
- 或
- 类：独热（
- One-Hot
- ）编码
- 维指示向量
- 其中取值为
- 的位置表示具体类

## Slide 18: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???18.PNG

### Shape 1 PLACEHOLDER (14)
- 18

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）：
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     分词（Tokenization）：将一段连续的文本（字符串）切分成更小的语义单位，确定了模型处理的最小信息单位

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

### Shape 6 TEXT_BOX (17)
- "John likes to watch movies."   →
- ["John", "likes", "to", "watch", "movies", "."]

## Slide 19: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???19.PNG

### Shape 1 PLACEHOLDER (14)
- 19

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）：
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     分词（Tokenization）
-     移除停止词：删除文本中频率极高但携带语义信息极少的词，如英文中的 "the", "a", "is", "at", "to"；中文中的“的”、“了”、“在”。

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

## Slide 20: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???20.PNG

### Shape 1 PLACEHOLDER (14)
- 20

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）：
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     分词（Tokenization）
-     移除停止词
-     提取词干："running", "runs", "ran" → "run"

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

## Slide 21: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???21.PNG

### Shape 1 PLACEHOLDER (14)
- 21

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）：
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     分词（Tokenization）、移除停止词、提取词干
-     词典：{John, likes, to, watch, movies, Mary, too}
-     词袋模型（Bag-of-Words）：记录该文本中出现的单词（加权）频率

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

## Slide 22: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???22.PNG

### Shape 1 PLACEHOLDER (14)
- 22

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）：
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     词袋模型（Bag-of-Words）：记录该文本中出现的单词（加权）频率

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

### Shape 6 TEXT_BOX (17)
- 丢失语序："I love you" 和 "You love me" 的 BoW 向量是一模一样的

## Slide 23: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???23.PNG

### Shape 1 PLACEHOLDER (14)
- 23

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     词典：{John, likes, to, watch, movies, Mary, too}
-     嵌入（Embedding）：将文本中每个词映射为向量，再整合成矩阵

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

### Shape 6 TEXT_BOX (17)
- 以独热编码为例

### Shape 7 AUTO_SHAPE (1)
- 如何处理长短不一的文本？

## Slide 24: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???24.PNG

### Shape 1 PLACEHOLDER (14)
- 24

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）
-   原始数据：字符串
-   自然语言处理（Natural Language Processing）
-     词典：{John, likes, to, watch, movies, Mary, too}
-     嵌入（Embedding）：将文本中每个词映射为向量，再整合成矩阵

### Shape 5 TEXT_BOX (17)
-   “John likes to watch movies.”、“Mary likes movies too.”

### Shape 6 TEXT_BOX (17)
- 填充（Padding）：设定一个最大长度（Max_Len），短句子后面补 0（或特定的 [PAD] 标识）。
- 截断（Truncation）：过长的句子直接砍掉尾部。
- 池化（Pooling）：对 Embedding 矩阵进行平均或取最大值，将其压缩为固定长度的向量。
- 循环神经网络 (RNN) / Transformer：这些架构原生支持处理变长序列（通过 Masking 技术忽略填充位）。

## Slide 25: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???25.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 25

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）
-   BPE（Byte Pair Encoding，字节对编码）：目前最主流
-   子词（Subword）分词法：介于“按单词分”和“按字母分”之间，取两者长处

### Shape 6 TEXT_BOX (17)
- BPE 核心逻辑：不断合并出现频率最高的相邻字符对

## Slide 26: 数据准备：类型转换
- screenshot: tmp/ch5_slides_png/???26.PNG

### Shape 1 PLACEHOLDER (14)
- 26

### Shape 2 TEXT_BOX (17)
- 数据准备：类型转换

### Shape 3 AUTO_SHAPE (1)
- 神经网络模型通常要求输入数据的特征为连续数值型，因此对于其它类型的数据需要执行类型转换。

### Shape 4 TEXT_BOX (17)
- 文本数据（Text Data）
-   BPE 核心逻辑：不断合并出现频率最高的相邻字符对
- 语料库：“hug”: 10次、“pug”: 5次、“pun”: 12次、"bun": 4次
- 1.拆分成基础字符：词表目前是：h, u, g, p, n, b
- 2.统计相邻字符对的频率：u和n经常连在一起；u, n 出现了 12 + 4 = 16 次。
- 3.合并频率最高的字符对：把u和n合并成新Token：un。词表变成：h, u, g, p, n, b, un
- 4.重复上述过程：u和g经常在一起，出现10+5=15次。词表变成：h, u, g, p, n, b, un, ug
- 5.直到达到预设的词表大小

### Shape 5 TEXT_BOX (17)
- 解决“未知词”（OOV）问题、词表大小可控、高效的语义压缩

### Shape 6 TEXT_BOX (17)
- 其他还有： WordPiece、 SentencePiece

## Slide 27: 课程思路
- screenshot: tmp/ch5_slides_png/???27.PNG

### Shape 1 PLACEHOLDER (14)
- 27

### Shape 2 TEXT_BOX (17)
- 课程思路

### Shape 3 TEXT_BOX (17)
- 深度神经网络训练的基本流程：
- 数据准备
- 模型架构
- 训练方法

## Slide 28: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???28.PNG

### Shape 1 PLACEHOLDER (14)
- 28

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 4 TEXT_BOX (17)
- “共适应” (Co-adaptation)
- 在深度神经网络中，如果某些神经元总是协同工作，它们可能会产生一种依赖性，即一个神经元的权重是为了弥补另一个神经元的错误而存在的。这种现象称为“共适应”，会导致模型过于依赖训练数据的特定组合，产生严重的过拟合

## Slide 29: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???29.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 29

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 4 TEXT_BOX (17)
- 示意图

### Shape 6 TEXT_BOX (17)
- Srivastava et al. Dropout: A Simple Way to Prevent Neural Networks from Overfitting. In JMLR, 2014.

### XML text fragments not otherwise grouped
- 常规隐藏层（第
- 层）
- 和
- 表示参数
- 假设第
- 层使用
- ，则

## Slide 30: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???30.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 30

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 4 TEXT_BOX (17)
- 示意图

### Shape 6 TEXT_BOX (17)
- Srivastava et al. Dropout: A Simple Way to Prevent Neural Networks from Overfitting. In JMLR, 2014.

### XML text fragments not otherwise grouped
- 训练：假设第
- 层使用
- ，则
- 作用：
- 降低拟合训练集的模型容量
- 破坏神经元间的关联性
- 近似于训练大量不同的“子网络”

## Slide 31: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???31.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 31

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 4 TEXT_BOX (17)
- 示意图

### Shape 6 TEXT_BOX (17)
- Srivastava et al. Dropout: A Simple Way to Prevent Neural Networks from Overfitting. In JMLR, 2014.

### Shape 7 AUTO_SHAPE (1)
- 为何缩放？

### XML text fragments not otherwise grouped
- 训练：假设第
- 层使用
- ，则
- 测试：对
- 层输出进行缩放

## Slide 32: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???32.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 32

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 5 TEXT_BOX (17)
- Dropout层

### Shape 6 TEXT_BOX (17)
- Dropout层

### Shape 7 TEXT_BOX (17)
- 测试时缩放会使输出范围与训练时对齐！

### XML text fragments not otherwise grouped
- 算例：假设
- ，对于仅有一个隐藏层的神经网络，在其隐藏层后接
- 层，训练和测试时的神经元计算分别如左右图所示

## Slide 33: 模型构建：丢弃层
- screenshot: tmp/ch5_slides_png/???33.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 33

### Shape 2 TEXT_BOX (17)
- 模型构建：丢弃层

### Shape 3 AUTO_SHAPE (1)
- Dropout是一种缓解神经网络模型过拟合的关键技术，其核心思想是在训练过程中，随机丢弃神经网络中的一些神经元及其连接，防止神经元之间产生过强的共适应。

### Shape 5 TEXT_BOX (17)
- Srivastava et al. Dropout: A Simple Way to Prevent Neural Networks from Overfitting. In JMLR, 2014.

## Slide 34: 模型构建：批归一化（batch normalization）
- screenshot: tmp/ch5_slides_png/???34.PNG

### Shape 1 PLACEHOLDER (14)
- 34

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化（batch normalization）

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 内部协变量偏移（
- Internal
- Covariate
- Shift
- 多层感知机第
- 层梯度
- 训练过程中，前层参数改变导致后层神经元输入分布发生变化
- 网络层数的增加会加剧这种影响
- 仅考虑关于
- 的部分

## Slide 35: 模型构建：批归一化（batch normalization）
- screenshot: tmp/ch5_slides_png/???35.PNG

### Shape 1 PLACEHOLDER (14)
- 35

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化（batch normalization）

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 内部协变量偏移（
- Internal
- Covariate
- Shift
- 多层感知机第
- 层梯度
- 训练过程中，前层参数改变导致后层神经元输入分布发生变化
- 需不断适应新的输入分布、速度变慢；出现梯度爆炸
- /
- 消失、不稳定
- 仅考虑关于
- 的部分

## Slide 36: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???36.PNG

### Shape 1 PLACEHOLDER (14)
- 36

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 5 AUTO_SHAPE (1)
- 如何推广到层输出？

### XML text fragments not otherwise grouped
- 内部协变量偏移（
- Internal
- Covariate
- Shift
- ）
- 多层感知机第
- 层梯度
- 回顾数据的标准化方法：
- 假设第
- 个特征的均值和方差分别为
- 和
- ，计算
- 仅考虑关于
- 的部分

## Slide 37: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???37.PNG

### Shape 1 PLACEHOLDER (14)
- 37

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 5 TEXT_BOX (17)
- 削弱了非线性激活函数带来的表达能力

### XML text fragments not otherwise grouped
- 考虑基于小批量（
- Mini-batch
- ）数据进行参数随机优化，假设批大小为
- 令
- 表示神经网络某层原本的加权求和输入，例如
- 首先计算小批量均值和方差
- 一种朴素的标准化方案：令

## Slide 38: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???38.PNG

### Shape 1 PLACEHOLDER (14)
- 38

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 考虑基于小批量（
- Mini-batch
- ）数据进行参数随机优化，假设批大小为
- 令
- 表示神经网络某层原本的加权求和输入，例如
- 首先计算小批量均值和方差
- 可学习的标准化方案：令
- ，并引入缩放参数
- 、偏移参数

## Slide 39: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???39.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 39

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 4 TEXT_BOX (17)
- 内部协变量偏移（Internal Covariate Shift）？？？

### Shape 6 TEXT_BOX (17)
- ICS和网络性能的关系并不大：向使用了BN的网络加入随机噪声，目的是使这个网络的ICS更加严重。实验结果表明虽然加入了随机噪声的BN的ICS问题更加严重，但它的性能要优于没有使用BN的普通网络

### Shape 7 TEXT_BOX (17)
- How Does Batch Normalization Help Optimization?(No, It Is Not About Internal Covariate Shift)

## Slide 40: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???40.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 40

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 4 TEXT_BOX (17)
- 内部协变量偏移（Internal Covariate Shift）？？？

### Shape 5 TEXT_BOX (17)
- BN和ICS的关系并不是很大

### Shape 6 TEXT_BOX (17)
- How Does Batch Normalization Help Optimization?(No, It Is Not About Internal Covariate Shift)

## Slide 41: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???41.PNG
- pictures: 3

### Shape 1 PLACEHOLDER (14)
- 41

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 4 TEXT_BOX (17)
- 内部协变量偏移（Internal Covariate Shift）？？？

### Shape 5 TEXT_BOX (17)
- BN处理之后的损失函数满足Lipschitz连续，即损失函数的梯度小于一个常量：

### Shape 6 TEXT_BOX (17)
- How Does Batch Normalization Help Optimization?(No, It Is Not About Internal Covariate Shift)

### Shape 8 TEXT_BOX (17)
- 而且损失函数的梯度也满足Lipschitz连续，即斜率的斜率也不会超过一个常量：

## Slide 42: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???42.PNG

### Shape 1 PLACEHOLDER (14)
- 42

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 链式法则：
- 中同样包含

## Slide 43: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???43.PNG

### Shape 1 PLACEHOLDER (14)
- 43

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 4 TEXT_BOX (17)
- 分路径求导，最后求和

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 多元函数链式法则：若
- ，且
- ，则

## Slide 44: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???44.PNG

### Shape 1 PLACEHOLDER (14)
- 44

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 关于
- 有
- 1
- ）
- ；
- 2
- ）
- ；
- 3
- ）

## Slide 45: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???45.PNG

### Shape 1 PLACEHOLDER (14)
- 45

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 关于
- 有
- 1
- ）
- ；
- 2
- ）
- ；
- 3
- ）

## Slide 46: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???46.PNG

### Shape 1 PLACEHOLDER (14)
- 46

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 关于
- 有
- 1
- ）
- ；
- 2
- ）
- ；
- 3
- ）

## Slide 47: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???47.PNG

### Shape 1 PLACEHOLDER (14)
- 47

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 反向传播：令
- 表示单个数据上的损失函数，需计算
- 等
- 关于
- 和
- 有

## Slide 48: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???48.PNG

### Shape 1 PLACEHOLDER (14)
- 48

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 测试阶段：利用训练阶段获取的均值与方差信息
- 均值：
- ，其中
- 表示训练阶段某批次的均值，
- 表示对训练阶段所有批次求（滑动）平均
- 方差：
- ，其中
- 表示训练阶段某批次的方差

## Slide 49: 模型构建：批归一化
- screenshot: tmp/ch5_slides_png/???49.PNG

### Shape 1 PLACEHOLDER (14)
- 49

### Shape 2 TEXT_BOX (17)
- 模型构建：批归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 测试阶段：利用训练阶段获取的均值与方差信息
- 均值和方差：
- 批归一化层输出
- 如果
- 太小会如何？

## Slide 50: 模型构建：层归一化
- screenshot: tmp/ch5_slides_png/???50.PNG

### Shape 1 PLACEHOLDER (14)
- 50

### Shape 2 TEXT_BOX (17)
- 模型构建：层归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 5 AUTO_SHAPE (1)
- 适用于任意批大小！

### XML text fragments not otherwise grouped
- 层归一化：对某层不同神经元的输入进行归一化
- 令
- 表示某层原本的加权求和输入，例如
- 计算该层神经元输入的均值和方差
- 可学习的标准化方案：

## Slide 51: 模型构建：实例归一化
- screenshot: tmp/ch5_slides_png/???51.PNG

### Shape 1 PLACEHOLDER (14)
- 51

### Shape 2 TEXT_BOX (17)
- 模型构建：实例归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### XML text fragments not otherwise grouped
- 为便于讨论，假设考虑输入为
- 个图片，其中每个图片大小为
- 表示通道数，例如彩色图片的
- R
- 、
- G
- 、
- B
- 通道；
- 和
- 表示图片高度和宽度
- 所有输入可以表示为
- 实例归一化（
- Instance
- Normalization
- ）：对每个样本及通道的
- 个取值进行归一化
- 可以是任意特征图！

## Slide 52: 模型构建：实例归一化
- screenshot: tmp/ch5_slides_png/???52.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 52

### Shape 2 TEXT_BOX (17)
- 模型构建：实例归一化

### Shape 3 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 4 TEXT_BOX (17)
- 多用于图像风格迁移：IN有助于消除内容图原风格
-   BN进一步混淆不同数据
-   LN进一步混淆不同通道

### Shape 5 TEXT_BOX (17)
- Ulyanov et al. Improved Texture Networks: Maximizing Quality and Diversity in Feed-forward Stylization and Texture Synthesis. In CVPR, 2017.

## Slide 53: 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。
- screenshot: tmp/ch5_slides_png/???53.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 53

### Shape 2 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 3 TEXT_BOX (17)
- 模型构建：组归一化

### Shape 5 TEXT_BOX (17)
- Wu and He. Group Normalization. In ECCV, 2018.

### XML text fragments not otherwise grouped
- 为便于讨论，假设考虑输入为
- 个图片，其中每个图片大小为
- 表示通道数，例如彩色图片的
- R
- 、
- 、
- B
- 通道；
- 和
- 表示图片高度和宽度
- 所有输入可以表示为
- 组归一化（
- ）：将特征通道等分为
- 组，对每个样本在组内进行归一化

## Slide 54: 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。
- screenshot: tmp/ch5_slides_png/???54.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 54

### Shape 2 AUTO_SHAPE (1)
- 由于层状结构，除数据归一化外，神经网络模型还可以对每一层输出的激活值进行归一化，减小不同维度或不同样本之间的分布差异，从而稳定训练并加快收敛。

### Shape 3 TEXT_BOX (17)
- ImageNet数据集

### Shape 4 TEXT_BOX (17)
- 模型构建：归一化方法对比

### Shape 5 TEXT_BOX (17)
- Wu and He. Group Normalization. In ECCV, 2018.

### Shape 8 TEXT_BOX (17)
- 不同批大小

### XML text fragments not otherwise grouped
- 固定批大小为

## Slide 55: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???55.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 55

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- 不同初始化参数可能导致不同的局部最优解

## Slide 56: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???56.PNG
- pictures: 3

### Shape 1 PLACEHOLDER (14)
- 56

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- 不同初始化参数可能导致不同的局部最优解

### Shape 8 TEXT_BOX (17)
- https://www.deeplearning.ai/ai-notes/initialization/index.html

### Shape 9 TEXT_BOX (17)
- 全0初始化

### Shape 10 TEXT_BOX (17)
- 合适的初始化

### Shape 11 TEXT_BOX (17)
- 网络结构

## Slide 57: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???57.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 57

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- 为什么不能使用全0初始化？

### Shape 6 TEXT_BOX (17)
- “对称权重”：同一层神经元参数初始化相同，则前向传播与反向梯度都相同，等价于该层只有一个神经元。

## Slide 58: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???58.PNG

### Shape 1 PLACEHOLDER (14)
- 58

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- 梯度爆炸

### Shape 5 TEXT_BOX (17)
- 梯度消失

### XML text fragments not otherwise grouped
- 回顾多层感知机的
- 第
- 层梯度：
- 过大的初始化容易导致梯度爆炸
- 过小的初始化容易导致梯度消失

## Slide 59: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???59.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 59

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 6 TEXT_BOX (17)
- 随着层数增加，激活值逐渐趋向于0

### XML text fragments not otherwise grouped
- 小随机数初始化
- 方法
- 1
- ：对于任意参数
- ，从区间
- 中均匀采样选取初始值
- 方法
- 2
- ：对于任意参数
- ，从均值为
- 、方差为
- 的高斯分布中采样初始值
- 50
- 层、每层
- 256
- 神经元、
- 的高斯分布

## Slide 60: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???60.PNG

### Shape 1 PLACEHOLDER (14)
- 60

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### XML text fragments not otherwise grouped
- 小随机数初始化的方差传播
- 首先考虑无偏置项的线性层，假设其输入为
- ，则输出为
- 假设输入的每个维度
- 独立同分布，且均值为
- 、方差为
- 假设每个权重参数
- 独立同分布，且均值为
- 、方差为
- 容易验证：
- ，以及

## Slide 61: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???61.PNG

### Shape 1 PLACEHOLDER (14)
- 61

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### XML text fragments not otherwise grouped
- 小随机数初始化的方差传播
- 首先考虑无偏置项的线性层，假设其输入为
- ，则输出为
- 假设输入的每个维度
- 独立同分布，且均值为
- 、方差为
- 假设每个权重参数
- 独立同分布，且均值为
- 0
- 、方差为
- 容易验证：
- ，以及
- 按比例衰减

## Slide 62: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???62.PNG

### Shape 1 PLACEHOLDER (14)
- 62

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### XML text fragments not otherwise grouped
- 小随机数初始化的方差传播
- 首先考虑无偏置项的线性层，假设其输入为
- ，则输出为
- 基于独立同分布假设：
- ，以及
- tanh
- 激活函数：其在
- 0
- 附近的取值满足
- 基于独立同分布假设：
- ，以及

## Slide 63: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???63.PNG

### Shape 1 PLACEHOLDER (14)
- 63

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 AUTO_SHAPE (1)
- 能否改进？

### XML text fragments not otherwise grouped
- 小随机数初始化的方差传播
- 首先考虑无偏置项的线性层，假设其输入为
- ，则输出为
- 基于独立同分布假设：
- ，以及
- ReLU
- 激活函数：
- 基于独立同分布假设：

## Slide 64: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???64.PNG

### Shape 1 PLACEHOLDER (14)
- 64

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- Xavier初始化
-   首先对于tanh等对称或近线性激活函数，控制前向传播方差衰减
-   同理，考虑反向传播过程等方差控制
-   两者结合得到Xavier初始化

### XML text fragments not otherwise grouped
- 均匀分布
- 或高斯分布

## Slide 65: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???65.PNG

### Shape 1 PLACEHOLDER (14)
- 65

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- He初始化
-   对于ReLU这种非对称激活函数，控制前向传播方差衰减
-   同样可以考虑反向传播影响，但实践中上述改变已足够有效

### XML text fragments not otherwise grouped
- 均匀分布
- 或高斯分布

## Slide 66: 模型构建：初始化
- screenshot: tmp/ch5_slides_png/???66.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 66

### Shape 2 TEXT_BOX (17)
- 模型构建：初始化

### Shape 3 AUTO_SHAPE (1)
- 一个好的模型参数初始化对于大多数优化算法的收敛都起到关键作用，尤其是神经网络模型所面临的非凸目标函数。

### Shape 4 TEXT_BOX (17)
- 基于方差控制的初始化方法对比

### Shape 7 TEXT_BOX (17)
- 合理控制方差后，即使层数增加，激活值仍远大于0

### XML text fragments not otherwise grouped
- 50
- 层、每层
- 256
- 神经元、
- 的高斯分布

## Slide 67: 课程思路
- screenshot: tmp/ch5_slides_png/???67.PNG

### Shape 1 PLACEHOLDER (14)
- 67

### Shape 2 TEXT_BOX (17)
- 课程思路

### Shape 3 TEXT_BOX (17)
- 深度神经网络训练的基本流程：
- 数据准备
- 模型架构
- 训练方法

## Slide 68: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???68.PNG

### Shape 1 PLACEHOLDER (14)
- 68

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 批量梯度，而非全量梯度
- 提高计算效率，引入随机性

### Shape 7 TEXT_BOX (17)
- 沿负梯度方向更新参数

### Shape 8 TEXT_BOX (17)
- 如何选择学习率？

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- ）
- 计算随机梯度：
- 表示批大小
- 进行参数更新

## Slide 69: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???69.PNG

### Shape 1 PLACEHOLDER (14)
- 69

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 批量梯度，而非全量梯度
- 提高计算效率，引入随机性

### Shape 7 TEXT_BOX (17)
- 沿负梯度方向更新参数

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- ）
- 计算随机梯度：
- 表示批大小
- 进行参数更新
- 虽然深度学习的目标函数是
- 高度非凸
- 的，但
- SGD
- 及其变体的收敛性理论最早是在凸优化中建立起来的
- 在凸优化中，可以严格证明
- SGD
- 能够收敛到全局最优解，并给出
- （
- 如
- ）
- 利用凸优化理论可以为
- SGD
- 学习率选择提供数学依据和解释

## Slide 70: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???70.PNG

### Shape 1 PLACEHOLDER (14)
- 70

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- ）
- 计算随机梯度：
- 表示批大小
- 进行参数更新
- 学习率的选择
- 取决于目标函数的性质
- （在线或随机凸优化理论）
- 非平滑函数：
- 或
- ，其中
- 为总迭代次数
- 平滑函数：
- ，其中
- 为某些常数

## Slide 71: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???71.PNG

### Shape 1 PLACEHOLDER (14)
- 71

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- ）
- 计算随机梯度：
- 表示批大小
- 进行参数更新
- 学习率的选择
- 取决于目标函数的性质
- （在线或随机凸优化理论）
- 非平滑函数：梯度可能剧烈变化，如果学习率不衰减，容易在最优解附
- 近震荡，无法收敛
- 平滑函数：
- 梯度变化有界，固定学习率可以在保证收敛的同时，实现更
- 快的迭代速度

## Slide 72: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???72.PNG

### Shape 1 PLACEHOLDER (14)
- 72

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 参数无区分：
- 对所有参数使用同一个全局学习率，不会根据参数的重要性、更新频率或梯度大小来区别对待
- 如果模型参数在尺度上差异很大（比如某些层参数范围很大，某些层很小），全局学习率很难同时适配所有参数
- 对于出现频率较低的特征（如稀疏数据中的罕见词），其参数更新次数少，若学习率太小则更新缓慢；若学习率太大则容易过调
- 深层网络中，不同层的梯度大小可能相差几个数量级，统一学习率会导致某些层更新过快或过慢

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- 计算随机梯度：
- 表示批大小
- 进行参数更新
- 学习率的选择
- 取决于目标函数的性质
- （在线或随机凸优化理论）
- 非平滑函数：梯度可能剧烈变化，如果学习率不衰减，容易在最优解附
- 近震荡，无法收敛
- 平滑函数：
- 梯度变化有界，固定学习率可以在保证收敛的同时，实现更
- 快的迭代速度

## Slide 73: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???73.PNG

### Shape 1 PLACEHOLDER (14)
- 73

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 随机梯度方差较大：
- 每次只基于一个 mini-batch 计算梯度，而非全量数据 → 得到的梯度是真实梯度的有噪声估计，这个噪声的方差随批量大小变化
- 方差大会导致更新方向不稳定，损失曲线震荡严重
- 为了稳定收敛，往往需要较小的学习率，但又会减慢收敛速度
- 即使理论上最终能收敛，在非平滑区域（如尖锐极小值附近），梯度噪声可能使参数无法稳定落点

### XML text fragments not otherwise grouped
- 随机梯度下降（
- Stochastic Gradient Descent
- SGD
- 计算随机梯度：
- 表示批大小
- 进行参数更新
- 学习率的选择
- 取决于目标函数的性质
- （在线或随机凸优化理论）
- 非平滑函数：梯度可能剧烈变化，如果学习率不衰减，容易在最优解附
- 近震荡，无法收敛
- 平滑函数：
- 梯度变化有界，固定学习率可以在保证收敛的同时，实现更
- 快的迭代速度

## Slide 74: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???74.PNG

### Shape 1 PLACEHOLDER (14)
- 74

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 根据每个参数的历史梯度大小，动态调整其学习率

### XML text fragments not otherwise grouped
- 针对
- “
- 所有参数共享同一学习率”问题的早期重要改进：
- 自适应梯度（
- Adaptive Gradient
- AdaGrad
- ）：给不同参数分配自适应的学习率
- 计算随机梯度：
- 表示批大小
- 进行参数更新：

## Slide 75: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???75.PNG

### Shape 1 PLACEHOLDER (14)
- 75

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 频繁更新的参数会获得较小的学习率，而稀疏更新的参数则能获得较大的学习率，从而更好地处理稀疏特征或不同尺度的问题

### XML text fragments not otherwise grouped
- 针对
- “
- 所有参数共享同一学习率”问题的早期重要改进：
- 自适应梯度（
- Adaptive Gradient
- AdaGrad
- ）：给不同参数分配自适应的学习率
- 计算随机梯度：
- 表示批大小
- 进行参数更新：

## Slide 76: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???76.PNG

### Shape 1 PLACEHOLDER (14)
- 76

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 AUTO_SHAPE (1)
- 学习率逐渐收敛至0！

### XML text fragments not otherwise grouped
- 自适应梯度（
- Adaptive Gradient
- AdaGrad
- ）：给不同参数分配自适应的学习率
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 每个参数的学习率由其累计梯度大小自适应调节
- →
- 全局学习率
- 可以设为
- 常数，真正的参数级学习率由
- 自动决定
- （累计梯度平方）

## Slide 77: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???77.PNG

### Shape 1 PLACEHOLDER (14)
- 77

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 AUTO_SHAPE (1)
- 仍面临SGD的学习率问题！

### XML text fragments not otherwise grouped
- 基于动量法（
- Momentum
- ）的
- ：保留一部分之前的更新方向
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 相对更稳定

## Slide 78: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???78.PNG

### Shape 1 PLACEHOLDER (14)
- 78

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 频繁更新的参数会获得较小的学习率，而稀疏更新的参数则能获得较大的学习率，从而更好地处理稀疏特征或不同尺度的问题

### XML text fragments not otherwise grouped
- 针对
- “
- 所有参数共享同一学习率”问题的早期重要改进：
- 自适应梯度（
- Adaptive Gradient
- AdaGrad
- ）：给不同参数分配自适应的学习率
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 自适应机制：
- 对于经常被更新的参数，其累积的
- 较大，因此
- 较小，学习率自动降低
- 对于很少被更新的参数，
- 较小，学习率相对较大，从而在出现梯度时能更快调整
- 这种机制使得
- AdaGrad
- 在稀疏数据（如自然语言处理、推荐系统）中表现优异

## Slide 79: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???79.PNG

### Shape 1 PLACEHOLDER (14)
- 79

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 频繁更新的参数会获得较小的学习率，而稀疏更新的参数则能获得较大的学习率，从而更好地处理稀疏特征或不同尺度的问题

### XML text fragments not otherwise grouped
- 针对
- “
- 所有参数共享同一学习率”问题的早期重要改进：
- 自适应梯度（
- Adaptive Gradient
- AdaGrad
- ）：给不同参数分配自适应的学习率
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 优点：
- 无需手动调整每个参数的学习率
- ，自动适应参数频率
- 对稀疏数据友好，能有效处理不同特征出现频率差异大的情况
- 局限性：
- 单调递增（始终累加正数），因此学习率会
- 持续单调下降
- ，甚至趋向于零
- 在深度学习中，如果训练过程很长，学习率可能过早变得过小，导致模型无法继续学习
- 后续的优化器（如
- RMSprop
- 、
- Adam
- ）
- 通过引入
- 指数衰减
- 来缓解这一问题

## Slide 80: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???80.PNG

### Shape 1 PLACEHOLDER (14)
- 80

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 AUTO_SHAPE (1)
- 学习率不再单调递减！

### XML text fragments not otherwise grouped
- 均方根传递（
- Root Mean Square Prop
- RMSProp
- ）
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 可被视为带有（近似）二阶动量的
- AdaGrad

## Slide 81: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???81.PNG

### Shape 1 PLACEHOLDER (14)
- 81

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- RMSPro
- p
- +
- 一阶动量
- 计算随机梯度：
- 表示批大小
- 进行参数更新：
- 偏向于
- 0

## Slide 82: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???82.PNG

### Shape 1 PLACEHOLDER (14)
- 82

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 TEXT_BOX (17)
- 去偏

### Shape 7 AUTO_SHAPE (1)
- 最为广泛使用的优化器！

### XML text fragments not otherwise grouped
- Adam
- ：一阶矩动量
- +
- 二阶矩自适应
- +
- 计算随机梯度：
- 表示批大小
- 进行参数更新：

## Slide 83: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???83.PNG

### Shape 1 PLACEHOLDER (14)
- 83

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- Adam
- 实践技巧：
- 简单设置
- 和
- 即可，且原文推荐使用
- 理论分析：
- 需要设置
- 及
- （学习率及一阶动量系数随时间衰减；但工程实践中很少使用）

## Slide 84: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???84.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 84

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- Adam
- 令
- 及
- ，原文给出了在线凸优化设定下的遗憾界
- 直觉上，
- 和
- 等数据相关项表明
- Adam
- 能够利用数据结构特性

## Slide 85: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???85.PNG
- pictures: 2

### Shape 1 PLACEHOLDER (14)
- 85

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 TEXT_BOX (17)
- Adam原文的理论分析存在错误

### Shape 10 TEXT_BOX (17)
-     Kingma, and Ba. Adam: A Method for Stochastic Optimization. In ICLR, 2015.

### XML text fragments not otherwise grouped
- 并不一定单调递增

## Slide 86: 训练与优化：优化器
- screenshot: tmp/ch5_slides_png/???86.PNG

### Shape 1 PLACEHOLDER (14)
- 86

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 TEXT_BOX (17)
-     S. J. Reddi, S. Kale, and S. Kumar. On the Convergence of Adam and Beyond. In ICLR, 2018. (Best Paper, 1/3)

### Shape 5 TEXT_BOX (17)
- 有效学习率单调递减

### XML text fragments not otherwise grouped
- AMSGrad
- 令
- ，下式成立
- （历史最大二阶矩）

## Slide 87: 训练与优化：优化器 + 权重衰减
- screenshot: tmp/ch5_slides_png/???87.PNG

### Shape 1 PLACEHOLDER (14)
- 87

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 权重衰减

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 TEXT_BOX (17)
- 标准SGD

### XML text fragments not otherwise grouped
- 权重衰减（
- Weight
- Decay
- ）：除执行更新
- 之外，以
- 的比例调低权重
- 结合
- ，即
- 当
- 为常数
- 时等价于对损失函数做二范数正则

## Slide 88: 训练与优化：优化器 + 权重衰减
- screenshot: tmp/ch5_slides_png/???88.PNG

### Shape 1 PLACEHOLDER (14)
- 88

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 权重衰减

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- AdamW
- Adam +
- 即使
- 不再等价于对损失函数做二范数正则
- 实践中优于标准
- Adam +

## Slide 89: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???89.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 89

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 TEXT_BOX (17)
- 学习率技巧：固定衰减
-   优化早期使用较大的学习率以确保收敛速度，随后逐渐调低学习率

### XML text fragments not otherwise grouped
- 分段衰减：每经过一定迭代次数，调低学习率
- 逆时衰减：
- 指数衰减：
- 自然指数衰减：
- 余弦衰减（当前大模型训练主流）：

## Slide 90: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???90.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 90

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 5 AUTO_SHAPE (1)
- 降低前期随机性影响！

### XML text fragments not otherwise grouped
- 学习率技巧：预热（
- Warmup
- ）
- 设定预热步数
- ，对于前
- 步，设定学习率
- 预热阶段结束后，再执行学习率衰减方法

## Slide 91: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???91.PNG

### Shape 1 PLACEHOLDER (14)
- 91

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- 学习率技巧：周期性学习率（
- Cyclical Learning Rate, CLR
- ）
- 动机：神经网络训练可能陷入局部最优或鞍点区域，周期性地增大学习率有助于跳出这些区域
- 令
- 分别表示学习率上下界，在
- 之间周期性变化

## Slide 92: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???92.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 92

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- 学习率技巧：周期性学习率（
- Cyclical Learning Rate, CLR
- ）
- 动机：神经网络训练可能陷入局部最优或鞍点区域，周期性地增大学习率有助于跳出这些区域
- 令
- 分别表示学习率上下界，在
- 之间周期性变化

## Slide 93: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???93.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 93

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### XML text fragments not otherwise grouped
- 学习率技巧：周期性学习率（
- Cyclical Learning Rate, CLR
- ）
- 动机：神经网络训练可能陷入局部最优或鞍点区域，周期性地增大学习率有助于跳出这些区域
- 令
- 分别表示学习率上下界，在
- 之间周期性变化

## Slide 94: 训练与优化：优化器 + 学习率技巧
- screenshot: tmp/ch5_slides_png/???94.PNG
- pictures: 1

### Shape 1 PLACEHOLDER (14)
- 94

### Shape 2 TEXT_BOX (17)
- 训练与优化：优化器 + 学习率技巧

### Shape 3 AUTO_SHAPE (1)
- 尽管随机梯度下降能够用于深度神经网络模型的高效更新，但是其实践中的收敛速度仍存在一些问题。

### Shape 4 TEXT_BOX (17)
- 学习率技巧：周期性学习率（Cyclical Learning Rate, CLR）

### Shape 7 TEXT_BOX (17)
- Huang et al. Snapshot Ensembles: Train 1, get M for free. In ICLR, 2017.

### Shape 8 TEXT_BOX (17)
- 普通学习率调整，容易陷入局部极值

### Shape 9 TEXT_BOX (17)
- CLR有助于逃离局部极值

## Slide 95: 总结
- screenshot: tmp/ch5_slides_png/???95.PNG

### Shape 1 PLACEHOLDER (14)
- 95

### Shape 2 TEXT_BOX (17)
- 总结

### Shape 3 TEXT_BOX (17)
- 数据准备
-   归一化
-   数据增强
-   类型转换

### Shape 4 TEXT_BOX (17)
- 模型构建
-   丢弃层
-   批归一化、层归一化、…
-   初始化

### Shape 5 TEXT_BOX (17)
- 训练与优化
-   优化器
-   权重衰减
-   学习率技巧

### Shape 6 AUTO_SHAPE (1)
- Q&A？
