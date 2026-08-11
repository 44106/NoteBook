# 第七章-视觉模型2.pptx ???????

Slides: 91


## Slide 1: 第七章：深度视觉模型（二）


### Text 1
第七章：深度视觉模型（二）


### Text 2
主讲教师：王文冠


### Text 3
课程名称：深度学习导论


### Notes
1


## Slide 2: 目标检测（Object Detection）


### Text 1
目标检测（Object Detection）


### Text 2
相比于只能判断整张图像类别的分类任务，目标检测则更进一步，它不仅能识别图像中存在哪些对象，还能用边界框精确定位每个对象的位置，实现分类与定位的结合，广泛应用于自动驾驶、异常行为检测、医疗影像分析等领域。


### Text 3
识别行人、车辆等不同对象


### Text 4
分类


### Text 5
分类 + 定位


### Notes
3


## Slide 3: 单目标检测


### Text 1
单目标检测


### Text 2
单目标检测是指图像中只存在或只需检测一个目标对象的情况，任务相对简单。


### Text 3
网络结构与损失函数


### Text 4
共享的卷积特征提取器 + 两个并行的全连接头。
分类头：输出类别得分（Class Scores），使用 Softmax Loss 作为分类损失。
回归头：输出边界框坐标 (x, y, w, h)，使用 L2 Loss 作为定位损失。
总损失 = 分类损失 + λ * 定位损失（多任务损失）


### Text 5
(x, y)


### Text 6
h


### Text 7
w


### Text 8
卷积特征提取器 (AlexNet)


### Text 9
特征向量


### Text 10
4096


### Text 11
分类头:
4096 -> 1000


### Text 12
回归头:
4096 -> 4


### Text 13
类别分数：
Cat: 0.9
Dog: 0.05
......


### Text 14
边界框坐标：
(x, y, w, h)


### Text 15
正确类别：Cat


### Text 16
分类损失：Softmax Loss


### Text 17
定位损失：L2 Loss


### Text 18
正确坐标：(x’, y’, w’, h’)


### Text 19
总损失


### Notes
4


## Slide 4: 多目标检测


### Text 1
多目标检测


### Text 2
多目标检测需要在同一图像中同时识别和定位多个目标，这些目标可能属于相同或不同类别，且常伴随目标重叠、尺度变化等复杂场景，技术难度显著增加。


### Text 3
核心挑战


### Text 4
每张图片需要不同数量的输出，而深度学习模型通常期望输入和输出具有固定的维度。


### Text 5
4 个输出


### Text 6
16 个输出


### Text 7
很多个输出！


### Text 8
如何将单目标检测的方法扩展到多目标检测上呢？


### Notes
5


## Slide 5: 多目标检测


### Text 1
多目标检测


### Text 2
朴素思路：在图像上滑动不同尺寸和长宽比的窗口，对每个窗口应用一个 CNN 分类器，判断其是否包含物体及物体类别。


### Text 3
问题：需要将 CNN 应用于海量位置、尺度和宽高比，计算成本非常高！


### Text 4
Dog? NO
Cat? NO
Background? YES


### Text 5
Dog? YES
Cat? NO
Background? NO


### Text 6
Dog? NO
Cat? YES
Background? NO


### Notes
6


## Slide 6: 多目标检测


### Text 1
多目标检测


### Text 2
区域提议 (Region Proposals)：先快速找出图像中“可能包含物体”的候选区域。只需对这几百到几千个候选区域进行精细分类和定位，大幅减少计算量。


### Text 3
解决方案


### Text 4
经典方法 Selective Search: 基于颜色、纹理、大小、形状等相似性，自底向上合并超像素，生成约2000个“blobby”区域。


### Notes
7


## Slide 7: R-CNN


### Text 1
R-CNN


### Text 2
R-CNN（Region-based CNN）：利用 Selective Search 生成候选区域，经 CNN 提取特征后分类并回归边界框，首次实现了高精度的多目标检测。


### Text 3
特征提取


### Text 4
1. 使用 Selective Search 生成大约 2000 个感兴趣区域（RoI）


### Text 5
2. 将每个 RoI 独立地缩放到固定尺寸（如 224x224）


### Text 6
3. 将每个缩放后的 RoI 独立地通过一个预训练的 CNN 提取特征


### Notes
8


## Slide 8: R-CNN


### Text 1
R-CNN


### Text 2
分类与精调


### Text 3
1. 使用 Selective Search 生成大约 2000 个感兴趣区域（RoI）


### Text 4
2. 将每个 RoI 独立地缩放到固定尺寸（如 224x224）


### Text 5
3. 将每个缩放后的 RoI 独立地通过一个预训练的 CNN 提取特征


### Text 6
4. 为每个 RoI 的特征向量训练一个线性 SVM 分类器


### Text 7
5. 为每个 RoI 的特征向量训练一个线性回归器，预测从当前 RoI 到真实边界框的微小修正量（dx, dy, dw, dh）。


### Notes
9


## Slide 9: R-CNN


### Text 1
R-CNN


### Text 2
效率瓶颈


### Text 3
1. 使用 Selective Search 生成大约 2000 个感兴趣区域（RoI）


### Text 4
2. 将每个 RoI 独立地缩放到固定尺寸（如 224x224）


### Text 5
3. 将每个缩放后的 RoI 独立地通过一个预训练的 CNN 提取特征


### Text 6
4. 为每个 RoI 的特征向量训练一个线性 SVM 分类器


### Text 7
5. 为每个 RoI 的特征向量训练一个线性回归器，预测从当前 RoI 到真实边界框的微小修正量（dx, dy, dw, dh）。


### Text 8
问题：速度极慢! 每个图像需要执行大约 2000 次独立的 CNN 前向传播。计算高度冗余，因为大部分 RoI 在空间上是重叠的。


### Notes
10


## Slide 10: Fast R-CNN


### Text 1
Fast R-CNN


### Text 2
Fast R-CNN：先将整张图像通过 ConvNet 提取一个共享的稠密特征图，再将候选区域映射到该特征图上提取固定长度特征，显著提升了训练效率与推理速度。


### Text 3
特征提取


### Text 4
整图输入 ConvNet，得到特征图 (如 conv5)
将 Selective Search 生成的 RoI 映射到特征图上
从特征图上裁剪 (Crop)出对应的 RoI 特征块


### Text 5
Fast R-CNN


### Text 6
"Slow" R-CNN


### Notes
11


## Slide 11: Fast R-CNN


### Text 1
Fast R-CNN


### Text 2
RoI 池化


### Text 3
裁剪出的 RoI 特征块尺寸不一，无法直接送入全连接层。
RoI Pooling 层：将任意尺寸的 RoI 特征块池化成固定尺寸的特征图
实现了端到端的训练


### Text 4
Fast R-CNN


### Text 5
"Slow" R-CNN


### Notes
12


## Slide 12: Fast R-CNN


### Text 1
Fast R-CNN


### Text 2
分类与精调


### Text 3
将 RoI Pooling 后的固定尺寸特征送入全连接层
两个并行输出头：Softmax 分类器 & 边界框回归器
损失函数同样是分类损失与定位损失的加权和。


### Text 4
Fast R-CNN


### Text 5
"Slow" R-CNN


### Notes
13


## Slide 13: Fast R-CNN


### Text 1
Fast R-CNN


### Text 2
优势与遗留问题


### Text 3
优势：速度大幅提升（共享卷积计算），端到端训练，精度高
遗留问题：区域提议方法（Selective Search）仍然是一个外部、独立、耗时的步骤，且是在 CPU 上运行，成为整个系统的瓶颈。


### Text 4
效率瓶颈！


### Notes
14


## Slide 14: Faster R-CNN


### Text 1
Faster R-CNN


### Text 2
Faster R-CNN：引入区域提议网络（Region Proposal Network, RPN），与检测网络共享底层卷积特征。RPN 取代了 Selective Search，实现完全在 GPU 上的端到端训练和推理。


### Notes
15


## Slide 15: Faster R-CNN


### Text 1
Faster R-CNN


### Text 2
RPN 锚点机制：在卷积特征图的每个空间位置上，预设 K 个不同尺度和长宽比的锚点框（Anchor Boxes）。锚点框覆盖了图像中可能出现的物体的各种形态。


### Text 3
锚点框


### Notes
16


## Slide 16: Faster R-CNN


### Text 1
Faster R-CNN


### Text 2
RPN 二分类任务：对于每个锚点框，RPN 预测一个“物体性”（Objectness）得分。这是一个二分类问题，即该锚点框是“前景”（包含物体）还是“背景”，输出一个 K x H x W 的概率图。


### Notes
17


## Slide 17: Faster R-CNN


### Text 1
Faster R-CNN


### Text 2
RPN 边界框回归：对于被预测为“前景”的锚点框，RPN 同时预测一个 4 维的修正向量 (dx, dy, dw, dh)，这个向量用于将原始的锚点框精调到更接近真实物体的位置和尺寸，最终输出一个 4K x H x W 的概率图。


### Notes
18


## Slide 18: 训练与推理


### Text 1
训练与推理


### Text 2
训练：将与真实框 IoU 较高的锚点视为正样本，较低的视为负样本。
推理：对所有 K x H x W 个锚点框，根据其“物体性”得分排序，选取得分最高的大约 300 个作为最终的区域提议（Proposals）。


### Text 3
Faster R-CNN


### Notes
19


## Slide 19: 两阶段 vs. 单阶段


### Text 1
两阶段 vs. 单阶段


### Text 2
两阶段 -> 单阶段：
能否摒弃区域提议阶段，直接从图像特征中预测物体类别和位置？


### Notes
20


## Slide 20: 单阶段目标检测器


### Text 1
单阶段目标检测器


### Text 2
单阶段目标检测器：将检测问题转化为一个密集预测问题；在特征图的每个位置上，直接预测多个边界框及其类别。代表工作包括 YOLO / SSD / RetinaNet ......


### Text 3
在每个网格单元内：
对每个 base boxes 回归出最终边界框的 5 个参数：(dx, dy, dh, dw, confidence)
预测 C 个类别（含背景类）的得分
看起来很像 RPN，但是是针对特定类别的！


### Notes
21


## Slide 21: YOLO


### Text 1
YOLO


### Text 2
YOLO (You Only Look Once)：将输入图像划分为 𝑆×𝑆 的网格，每个网格直接预测边界框坐标、置信度及类别概率，仅需一次前向传播即可完成全图检测，真正实现了端到端的实时目标检测。


### Notes
22


## Slide 22: YOLO


### Text 1
YOLO


### Text 2
YOLO后处理：先经置信度筛选剔除低分框，再通过非极大值抑制（NMS）去除重复检测，保留最优结果。


### Text 3
许多具有不同对象概率的边界框


### Text 4
S x S 网格


### Text 5
置信度筛选 +
非极大值抑制


### Notes
23


## Slide 23: SSD: 多尺度特征融合


### Text 1
SSD: 多尺度特征融合


### Text 2
核心思想： 利用 CNN 不同层级的特征图来检测不同尺度的物体。
浅层特征图（高分辨率）用于检测小物体。
深层特征图（低分辨率）用于检测大物体。


### Notes
24


## Slide 24: SSD vs. YOLO


### Text 1
SSD vs. YOLO


### Text 2
YOLO 主要依赖最后的特征图，对小物体和密集物体检测效果不佳。
SSD 通过多尺度特征融合，显著提升了对小物体的检测能力。


### Notes
25


## Slide 25: 单阶段检测器的挑战


### Text 1
单阶段检测器的挑战


### Text 2
在密集预测中，绝大多数锚点/位置都是背景（负样本）。
这种极端的不平衡（长尾）会导致模型训练困难，梯度被大量简单的负样本主导，是阻碍单阶段检测器实现最先进精度的主要障碍。


### Text 3
正负样本不平衡


### Notes
26


## Slide 26: 单阶段检测器的挑战


### Text 1
单阶段检测器的挑战


### Text 2
标准交叉熵损失的问题：对所有样本一视同仁。
Focal Loss 的改进：
引入调制因子 ，降低易分样本（高 ）的权重。
使模型在训练过程中更加关注难分样本（低  ）。
有效解决了正负样本不平衡问题，使单阶段检测器的精度能够媲美甚至超越两阶段检测器。


### Text 3
正负样本不平衡


### Notes
27


## Slide 27: DETR


### Text 1
DETR


### Text 2
核心架构：CNN 主干 + Transformer 编码器-解码器。
简单的目标检测流程：直接从 Transformer 输出一组边界框，无需锚点框和回归边界框变换。
使用二分匹配（匈牙利算法）将预测边界框与 GT 边界框进行匹配；训练以回归边界框坐标。


### Notes
28


## Slide 28: 密集预测


### Text 1
密集预测


### Text 2
目前我们讨论了图像分类与目标检测，这两者主要关注图像整体或特定区域的稀疏预测（Sparse Prediction），输出的是类别标签或边界框。
不同于这两者仅在图像级或对象级给出离散结果，密集预测（Dense Prediction Tasks）则更有挑战性，它要求模型对每一个像素都做出预测。我们将重点讨论：
语义分割（Semantic Segmentation）
实例分割（Instance Segmentation）


### Text 3
图像分类


### Text 4
目标检测


### Text 5
语义分割


### Text 6
实例分割


### Text 7
稀疏预测 -> 密集预测


### Notes
https://link.springer.com/article/10.1007/s13735-017-0141-z
29


## Slide 29: 语义分割（Semantic Segmentation）


### Text 1
语义分割（Semantic Segmentation）


### Text 2
与图像分类任务只能判断整张图像的类别不同，语义分割能够为图像中的每一个像素点分配一个语义类别标签，从而实现对图像的精细化理解，被广泛应用于自动驾驶、医学影像分析、遥感图像分析等领域。


### Text 3
分割图


### Text 4
原图


### Notes
30


## Slide 30: 语义分割的应用


### Text 1
语义分割的应用


### Text 2
应用场景1：自动驾驶


### Text 3
语义分割在自动驾驶中的作用


### Text 4
示例：Cityscapes 数据集


### Text 5
语义分割技术为自动驾驶车辆提供像素级的环境感知能力，能够精确识别可行驶区域、检测车辆与行人等动态障碍物、理解车道线与交通标志等道路要素，将摄像头采集的原始图像转化为结构化的场景理解，为后续的路径规划、避障决策和安全控制提供关键的环境信息支撑。


### Text 6
城市街景语义分割标准数据集（19类像素级标注）


### Notes
31


## Slide 31: 语义分割的应用


### Text 1
语义分割的应用


### Text 2
应用场景2：医学影像


### Text 3
语义分割在医学影像中的作用


### Text 4
示例：BRATS 数据集


### Text 5
语义分割技术在医学影像分析中发挥着关键作用，它能够对 CT、MRI 等医学扫描图像进行像素级的精细标注，自动分割出心脏、肝脏、肿瘤等特定器官或病灶区域，不仅辅助医生进行快速准确的诊断与量化分析，还为手术路径规划、治疗效果监测等提供了重要的客观依据。


### Text 6
模态：多模态脑部MRI图像
内容：健康组织、水肿区、坏死区等多区域标注
临床意义：辅助医生快速定位肿瘤区域、量化肿瘤体积和生长速度、…


### Notes
32


## Slide 32: 语义分割的应用


### Text 1
语义分割的应用


### Text 2
应用场景3：遥感图像


### Text 3
语义分割在遥感图像中的作用


### Text 4
示例：FoVx4 数据集


### Text 5
语义分割技术能够对卫星遥感影像和航空摄影进行像素级的地物分类，自动识别并提取建筑物、道路、水体、植被、农田等地理要素，实现大范围的土地覆盖分类与变化检测。


### Notes
33


## Slide 33: 语义分割的引入


### Text 1
语义分割的引入


### Text 2
如前所述，我们可以将语义分割理解为像素级的分类任务
然而，单个像素缺乏上下文，无法独立判断类别


### Notes
34


## Slide 34: 语义分割的网络架构思考


### Text 1
语义分割的网络架构思考


### Text 2
像素级的分类也是分类任务，
因此借鉴图像分类方法——
先对图片下采样，然后做像素级预测？


### Notes
35


## Slide 35: 语义分割的网络架构思考


### Text 1
语义分割的网络架构思考


### Text 2
朴素思路：对图片下采样，然后做像素级预测


### Text 3
问题：图像分类的下采样是为了增大感受野，理解高层语义信息即可。
而我们是像素级的预测！


### Notes
36


## Slide 36: 语义分割的网络架构思考


### Text 1
语义分割的网络架构思考


### Text 2
可否不进行下采样，
直接保持原分辨率做预测？


### Notes
37


## Slide 37: 语义分割的网络架构思考


### Text 1
语义分割的网络架构思考


### Text 2
朴素思路：直接保持原分辨率做预测


### Text 3
问题：每张图的分辨率通常较大(512x512, 1024x1024, …)，这会导致计算量爆炸！
不下采样也会影响上下文的理解


### Notes
38


## Slide 38: 语义分割的网络架构思考


### Text 1
语义分割的网络架构思考


### Text 2
采用下采样-上采样的结构
层次化特征提取：捕获多尺度上下文和语义信息
计算高效：瓶颈层压缩特征维度，降低后续解码开销
空间恢复可控：解码器上采样，兼顾定位精度与语义一致性
…


### Text 3
解决方案


### Notes
39


## Slide 39: 上采样


### Text 1
上采样


### Text 2
上采样：重建像素级预测图，将低分辨率特征图恢复至原始空间尺寸


### Text 3
反池化方法


### Text 4
最近邻插值
0-填充
…


### Notes
40


## Slide 40: 上采样


### Text 1
上采样


### Text 2
上采样：重建像素级预测图，将低分辨率特征图恢复至原始空间尺寸


### Text 3
单线性插值


### Text 4
利用邻近已知点的加权平均估计未知点值


### Text 5
公式推导


### Text 6
几何意义


### Notes
41


## Slide 41: 上采样


### Text 1
上采样


### Text 2
上采样：重建像素级预测图，将低分辨率特征图恢复至原始空间尺寸


### Text 3
双线性插值


### Text 4
公式推导


### Text 5
几何意义


### Text 6
两次线性插值，利用目标点周围4个相邻像素的加权平均值来计算新像素位置的值


### Notes
42


## Slide 42: 上采样


### Text 1
上采样


### Text 2
上采样：重建像素级预测图，将低分辨率特征图恢复至原始空间尺寸


### Text 3
Max Unpooling


### Text 4
Max Pooling：
不仅要输出最大值，还要记住每个最大值的位置


### Text 5
Max Unpooling：
利用池化时记录的位置信息，把值放回原来的位置


### Notes
43


## Slide 43: 上采样


### Text 1
上采样


### Text 2
上采样：重建像素级预测图，将低分辨率特征图恢复至原始空间尺寸


### Text 3
转置卷积


### Text 4
参数（示例）：3×3卷积核，stride=2，pad=1
机制：每个输入像素通过卷积核"扩散"到输出的3×3区域


### Text 5
重叠求和：多个输入的影响区域重叠时，对应位置求和
可学习：卷积核权重通过训练学习，实现自适应上采样


### Notes
44


## Slide 44: FCN: 从图像分类到图像分割


### Text 1
FCN: 从图像分类到图像分割


### Text 2
FCN vs 图像分类


### Text 3
核心思想： 全连接层 -> 卷积层
全连接层：整图分类
卷积层：像素级预测
支持任意尺寸输入，端到端训练


### Text 4
因此输出热力图(heatmap)，
而不是单一类别


### Notes
45


## Slide 45: FCN: 从图像分类到图像分割


### Text 1
FCN: 从图像分类到图像分割


### Text 2
架构图


### Text 3
流程：
特征提取
全卷积化
分类层
上采样
像素级分割图


### Text 4
多尺度特征融合


### Text 5
深层特征：语义强，但位置模糊
浅层特征：位置准，但语义弱
因此，融合不同层的特征，
兼顾语义和定位


### Notes
46


## Slide 46: U-Net


### Text 1
U-Net


### Text 2
U-Net通过完全对称的编码器-解码器结构和密集的跳跃连接，在恢复分辨率的同时精确保留空间细节，成为小数据医学图像分割的标杆方法。


### Text 3
架构图


### Notes
47


## Slide 47: U-Net


### Text 1
U-Net


### Text 2
U-Net通过完全对称的编码器-解码器结构和密集的跳跃连接，在恢复分辨率的同时精确保留空间细节，成为小数据医学图像分割的标杆方法。


### Text 3
下采样 & 上采样


### Notes
48


## Slide 48: U-Net


### Text 1
U-Net


### Text 2
U-Net通过完全对称的编码器-解码器结构和密集的跳跃连接，在恢复分辨率的同时精确保留空间细节，成为小数据医学图像分割的标杆方法。


### Text 3
跳跃连接


### Text 4
将编码器对应阶段的特征图与解码器上采样后的特征图按通道拼接
保留空间细节：浅层的边缘、纹理信息直接传递到解码端，避免上采样丢失
精确定位：解码时能准确知道位置，提升分割边界精度
多尺度融合：深层语义 + 浅层细节，让网络自己学习如何组合


### Notes
49


## Slide 49: DeepLab系列


### Text 1
DeepLab系列


### Text 2
DeepLab是语义分割领域的经典系列工作，通过空洞卷积扩大感受野、ASPP模块建模多尺度上下文等设计，系统性解决了"多尺度目标"和"边界模糊"两大核心挑战。


### Text 3
DeepLab v1/v2


### Text 4
针对语义分割出现的两个挑战：
多尺度目标：同一类别物体大小差异大
边界模糊：深层特征及上采样带来的边界处挑战
DeepLab v1/v2 引入空洞卷积，扩大感受野，捕获更多上下文。


### Notes
50


## Slide 50: DeepLab系列


### Text 1
DeepLab系列


### Text 2
DeepLab是语义分割领域的经典系列工作，通过空洞卷积扩大感受野、ASPP模块建模多尺度上下文等设计，系统性解决了"多尺度目标"和"边界模糊"两大核心挑战。


### Text 3
DeepLab v3


### Text 4
然而，单一眼洞率无法适应所有尺度目标
因此，DeepLab v3 提出 ASPP（Atrous Spatial Pyramid Pooling），并行多个不同空洞率的卷积 + 全局池化
从而同时捕获局部细节与全局上下文，适应不同大小目标，提升鲁棒性。


### Notes
51


## Slide 51: DeepLab系列


### Text 1
DeepLab系列


### Text 2
DeepLab是语义分割领域的经典系列工作，通过空洞卷积扩大感受野、ASPP模块建模多尺度上下文等设计，系统性解决了"多尺度目标"和"边界模糊"两大核心挑战。


### Text 3
DeepLab v3+


### Text 4
最终形态：DeepLab v3+ 架构图
改进ASPP，加入Batch Normalization层
实现Feature Map的跨Block融合


### Notes
https://arxiv.org/pdf/2105.15203
52


## Slide 52: SegFormer


### Text 1
SegFormer


### Text 2
SegFormer：基于Transformer骨干网络的语义分割领域的代表性工作。通过引入层次化Mix Transformer Backbone和轻量级MLP Decoder，开创了高效灵活的新范式。


### Text 3
性能与效率


### Text 4
作为Transformer-based语义分割的代表作，SegFormer展现了纯Transformer架构的全面优势：
vs CNN方法
vs 其他Transformer方法
SegFormer在参数效率和推理速度上实现数量级提升，成为语义分割从CNN向Transformer范式转变的关键里程碑。


### Notes
53


## Slide 53: SegFormer


### Text 1
SegFormer


### Text 2
SegFormer：基于Transformer骨干网络的语义分割领域的代表性工作。通过引入层次化Mix Transformer Backbone和轻量级MLP Decoder，开创了高效灵活的新范式。


### Text 3
架构图


### Text 4
SegFormer由两部分组成：
层次化Transformer-based Encoder
仅由几个FC构成的Decoder


### Notes
54


## Slide 54: SegFormer


### Text 1
SegFormer


### Text 2
MiT-Bx Backbone


### Text 3
层次化特征提取
重叠 Patch Embedding
混合前馈网络 Mix-FFN
相比传统baseline，具备更大感受野


### Text 4
All-MLP Decoder


### Text 5
由于MiT Backbone具备更大感受野，解码器无需复杂结构


### Notes
55


## Slide 55: MaskFormer


### Text 1
MaskFormer


### Text 2
MaskFormer提出掩码分类新范式，将问题转化为"预测一组{掩码, 类别}对"的集合预测问题，通过Query机制与匈牙利匹配实现端到端训练，无需复杂后处理。


### Text 3
范式更改


### Text 4
分类范式的更改：不再是逐像素分类，而是Mask Classification


### Notes
56


## Slide 56: MaskFormer


### Text 1
MaskFormer


### Text 2
MaskFormer提出掩码分类新范式，将问题转化为"预测一组{掩码, 类别}对"的集合预测问题，通过Query机制与匈牙利匹配实现端到端训练，无需复杂后处理。


### Text 3
架构图


### Text 4
Backbone+Pixel Decoder 生成像素级嵌入，Transformer Decoder 处理 N 个 Query 生成对象级嵌入
通过计算 Query 嵌入与像素嵌入的相似度，直接生成 N 个候选掩码
并行输出类别预测和掩码预测，语义分割推理时聚合同类掩码生成最终分割图


### Notes
57


## Slide 57: MaskFormer


### Text 1
MaskFormer


### Text 2
MaskFormer提出掩码分类新范式，将问题转化为"预测一组{掩码, 类别}对"的集合预测问题，通过Query机制与匈牙利匹配实现端到端训练，无需复杂后处理。


### Text 3
架构图


### Text 4
Object Queries: 使用 N 个可学习的 query 向量
每个 query 独立预测一个语义 mask 和一个全局类别标签
通过 Transformer 解码器并行生成所有 mask
无需预定义类别数量，自然适应不同场景


### Notes
58


## Slide 58: 大模型时代: SAM


### Text 1
大模型时代: SAM


### Text 2
SAM (Segment Anything Model) 是 Meta 发布的分割基础模型，通过提示式交互（点/框/文本）实现 zero-shot 通用分割，开创了"一个模型分割万物"的新范式。


### Text 3
架构图


### Text 4
v1


### Text 5
v2


### Notes
59


## Slide 59: 大模型时代: SAM


### Text 1
大模型时代: SAM


### Text 2
可提示分割


### Text 3
点 Prompt
框 Prompt
文本 Prompt


### Text 4
SA-1B 数据集


### Text 5
模型+人工 构建数据集
包含11亿+掩码，1100万+图片
为编码器提供海量数据支持


### Notes
60


## Slide 60: 大模型时代: SAM


### Text 1
大模型时代: SAM


### Text 2
实验结果


### Text 3
突破闭集限制：SAM未在某些多样化数据上训练，却能有效分割训练集中未充分出现的物体类别


### Text 4
突破单一任务限制：
分割相关任务很多，如交互式分割、边缘检测、前景分割、语义分割、实例分割、全景分割…
SAM 可在推理时充当更大系统中的组件


### Notes
61


## Slide 61: 常见框架


### Text 1
常见框架


### Text 2
MMEngine


### Text 3
Detectron 2


### Notes
62


## Slide 62: 常见工具


### Text 1
常见工具


### Text 2
WandB


### Text 3
结果曲线、Loss曲线等监控


### Text 4
结果可视化对比


### Notes
63


## Slide 63: 实例分割


### Text 1
实例分割


### Text 2
为图像中的每一个物体实例生成一个二值掩码（Binary Mask），精确到像素级别。
需要同时解决检测（定位和分类）和分割（像素级描绘）两个子任务，对空间对齐精度要求极高。


### Text 3
图像分类


### Text 4
目标检测


### Text 5
语义分割


### Text 6
实例分割


### Text 7
只知道图片里面有什么物体


### Text 8
不知道每个物体的精确轮廓


### Text 9
不区分同一类别的个体


### Text 10
区分同一类别的不同个体


### Notes
64


## Slide 64: Mask R-CNN


### Text 1
Mask R-CNN


### Text 2
RoI Align


### Text 3
核心思想：在 Faster R-CNN 的基础上，增加一个预测掩码的分支。
架构详解：
共享主干和 RPN：与 Faster R-CNN 相同。
三个并行输出头：分类头、边界框回归头、掩码头。
RoI Align：替换 RoI Pooling，以保证掩码预测的像素级对齐精度。


### Notes
65


## Slide 65: Mask R-CNN


### Text 1
Mask R-CNN


### Text 2
问题：RoI Pooling 在映射和池化过程中存在两次量化（取整）操作，导致特征与原始 RoI 位置不对齐，对像素级任务（如实例分割）影响显著。


### Text 3
举例：图中 4×5 的 RoI（蓝色框）要池化为 2 x 2 的输出，理想情况下每个 bin 应当为 2 x 2.5，但是 RoI Pooling 会将高度取整为 2 或 3，导致实际池化区域偏离等分位置，最终使实例分割的 mask 边界错位。


### Notes
66


## Slide 66: Mask R-CNN


### Text 1
Mask R-CNN


### Text 2
解决方案 (RoI Align)：移除量化操作，使用双线性插值来精确地从特征图上采样 RoI 所需的值。


### Text 3
举例：RoI Align 保留浮点坐标，如第一个 bin 左上角在 (0, 0)，右下角在 (2, 2.5)。对于 bin 内的特征值，通过双线性插值从四个最近邻像素，如 (0, 0), (0, 1), (1, 0), (1, 1) 计算得到，确保每个特征值准确反映其实际覆盖区域。


### Notes
67


## Slide 67: Mask R-CNN


### Text 1
Mask R-CNN


### Text 2
掩码预测策略


### Text 3
逐类掩码：掩码头为每个类别都输出一个二值掩码。
掩码选择：根据分类头的预测结果，只选择对应类别的掩码通道作为最终输出。


### Text 4
训练目标


### Text 5
分类和边界框损失：与 Faster R-CNN 相同。
掩码损失：对 RoI 内的真实掩码进行下采样，与网络预测的 28x28 掩码计算逐像素的 sigmoid 交叉熵损失。


### Notes
68


## Slide 68: Mask R-CNN


### Text 1
Mask R-CNN


### Text 2
多功能性


### Text 3
除了实例分割，Mask R-CNN 稍作修改即可用于 人体姿态估计（Human Pose Estimation）
将关键点（如关节）视为一种特殊的“实例”，用类似掩码的方式预测。


### Text 4
Note


### Text 5
Mask R-CNN 是两阶段实例分割的典范，精度高。
也存在单阶段的实例分割方法（如 YOLACT, SOLO），追求速度。


### Notes
69


## Slide 69: 视频理解


### Text 1
视频理解


### Text 2
回顾：目前我们已经学习了四大关于 2D 图像的基础性任务。
现在，我们进一步从静态图像识别迈向动态视频理解。
视频理解在现实世界中的应用场景：监控、人机交互、内容审核等。


### Text 3
图像分类


### Text 4
目标检测


### Text 5
语义分割


### Text 6
实例分割


### Text 7
静态图像 -> 动态视频


### Notes
70


## Slide 70: 视频理解


### Text 1
视频理解


### Text 2
视频的本质：一连串按时间顺序排列的图像帧（视频 = 2D + 时间）。
数据表示：一个 4D 张量，通常为 T x 3 x H x W 或 3 x T x H x W，其中 T 是帧数。
核心挑战：如何有效建模和利用时间维度上的信息。


### Notes
71


## Slide 71: 视频理解


### Text 1
视频理解


### Text 2
任务定义：给定一个视频片段，预测其所属的动作类别。
关键区别：图像识别“物体”，视频识别“动作”或“事件”。
输入：视频片段 (T x 3 x H x W)；输出：一个动作类别。


### Notes
72


## Slide 72: 视频理解


### Text 1
视频理解


### Text 2
核心挑战：视频数据量巨大。未压缩的视频标清约 1.5 GB/分钟，高清约 10 GB/分钟。
解决方案：基于短片段训练
实践策略：不在完整长视频上训练，而是采样短片段（clips）。
训练阶段： 模型学习对这些短片段进行分类。
测试阶段： 对多个片段进行推理，取平均预测结果作为最终视频级预测。


### Notes
73


## Slide 73: 单帧 CNN


### Text 1
单帧 CNN


### Text 2
基线方法：单帧 CNN
核心思想：将视频分类问题简化为对每一帧独立进行图像分类。
流程：使用一个标准的 2D CNN 分别处理视频中的每一帧，得到每帧的类别概率，最后在时间维度上取平均。
优点：实现简单，常作为强有力的基线。


### Notes
74


## Slide 74: 早期融合


### Text 1
早期融合


### Text 2
早期融合：在输入层融合时间信息
核心思想：在模型的第一层就将时间信息融合进来。
实现方式：将 T 帧的 RGB 通道堆叠，形成一个 (3T) x H x W 的“超图像”，然后送入标准的 2D CNN。
直觉：让第一个卷积层直接比较不同帧之间的像素差异。


### Notes
75


## Slide 75: 早期融合


### Text 1
早期融合


### Text 2
早期融合的局限性
关键问题：第一个2D卷积层会将所有时间信息压缩掉（输出为 D x H x W），后续网络无法再访问原始的时间结构。
后果：仅有一层进行时间处理，对于复杂的、长时序的动作可能不足以捕获足够的动态信息。


### Notes
76


## Slide 76: 晚期融合


### Text 1
晚期融合


### Text 2
晚期融合：在高层特征融合时间信息
核心思想：先独立提取每帧的高层特征，再在特征层面进行时间融合。
实现方式A（MLP）：对每帧用 2D CNN 提取特征，将所有帧的特征向量拼接成一个长向量，送入全连接层（MLP）进行分类。


### Notes
77


## Slide 77: 晚期融合


### Text 1
晚期融合


### Text 2
晚期融合：在高层特征融合时间信息
实现方式B（Pooling）：对每帧用 2D CNN 提取特征后，在时间和空间维度上进行全局平均池化，得到一个紧凑的视频级特征向量，再送入线性分类器。


### Notes
78


## Slide 78: 晚期融合


### Text 1
晚期融合


### Text 2
晚期融合的局限性
关键问题：由于每帧是独立处理的，模型难以直接比较帧与帧之间的底层运动信息（如像素位移）。
后果：虽然能捕捉到每帧的变化，但对精细、局部的运动模式建模能力弱。


### Notes
79


## Slide 79: 3D CNN


### Text 1
3D CNN


### Text 2
3D CNN：时空慢速融合
核心思想：使用 3D 卷积核在整个网络中逐步、同步地融合空间和时间信息。
实现方式：将 2D CNN 中的卷积和池化操作全部替换为 3D 版本。
直觉：每一层的特征图都是一个 4D 张量，保留了完整的时空结构。


### Notes
80


## Slide 80: 早期融合 vs. 晚期融合 vs. 3D CNN


### Text 1
早期融合 vs. 晚期融合 vs. 3D CNN


### Text 2
3D卷积精度更高，但是计算开销也极其高昂！


### Notes
81


## Slide 81: 运动识别


### Text 1
运动识别


### Text 2
从运动识别人类行为
运动信息是视频理解中至关重要的线索，有时甚至比外观信息更重要。


### Text 3
度量运动：光流
光流是一个二维向量场，描述从帧  到帧  每个像素点的位移 (dx, dy)。
水平分量 (dx) 和垂直分量 (dy) 可以用灰度图表示，共同构成运动模式。


### Notes
82


## Slide 82: 运动识别


### Text 1
运动识别


### Text 2
融合策略：在预测阶段，将两个流的 softmax 分数进行平均，或使用 SVM 等方法进行融合。
性能优势：在双流网络显著超越了仅使用空间信息或早期/晚期融合的方法，证明了显式建模运动的有效性。


### Notes
83


## Slide 83: 长期时序建模


### Text 1
长期时序建模


### Text 2
局限性：前述方法（3D CNN, 双流网络）主要处理短片段（~2-5秒），只能捕获局部的时序动态。
现实需求：许多复杂活动（如“做早餐”、“打篮球比赛”）包含跨越数十秒甚至数分钟的长期依赖和事件顺序。
问题：如何建模这种长距离的时序结构？


### Notes
84


## Slide 84: RNN/LSTM -> 序列建模的经典工具：


### Text 1
RNN/LSTM -> 序列建模的经典工具：
核心思想：使用循环神经网络来处理由 CNN 提取的逐帧特征序列。
流程：(1) 使用 CNN 从视频中提取局部特征向量；(2) 将这些特征向量按时间顺序送入 RNN；(3) RNN 的最终状态或所有状态用于最终预测。
优势：理论上可以捕获任意长度的时序依赖。


### Text 2
我们是否可以把 RNN 和 CNN 结合起来呢？


### Text 3
长期时序建模


### Notes
85


## Slide 85: 循环卷积网络 (Recurrent Convolutional Networks)：


### Text 1
循环卷积网络 (Recurrent Convolutional Networks)：
核心思想：将 RNN 的递归思想与 CNN 的权重共享思想结合。
架构特点：网络由多层组成，每一层在时间步 t 的输出，不仅取决于当前时间步上一层的输出，还取决于同一层在上一时间步 t-1 的输出。


### Text 2
优势：相比标准RNN，参数更少，且保留了空间局部性。
问题：RNN的计算是顺序依赖的，难以并行！


### Text 3
长期时序建模


### Notes
86


## Slide 86: 时空自注意力：并行化序列建模


### Text 1
时空自注意力：并行化序列建模
核心思想：将自注意力机制应用于 3D CNN 的特征图上，以捕获长距离的时空依赖。


### Text 2
长期时序建模


### Notes
87


## Slide 87: 长期时序建模


### Text 1
长期时序建模


### Text 2
I3D：膨胀2D网络至3D
核心思想：复用在图像上取得成功的 2D CNN 架构来构建 3D 视频模型。
实现：将 2D 卷积核 ( x ) 和 2D 池化核膨胀为 3D 核 (x x )


### Notes
88


## Slide 88: 从 CNN 到 Transformer


### Text 1
从 CNN 到 Transformer
趋势：Vision Transformer 及其变体（如 MViT, VideoMAE）已成为当前视频理解的主流和 SOTA 架构。


### Text 2
长期时序建模


### Notes
89


## Slide 89: 超越分类：时序动作定位 / 检测


### Text 1
超越分类：时序动作定位 / 检测


### Text 2
时序动作定位：
给定一个未修剪的长视频，不仅要识别出其中发生的动作类别，还要精确定位每个动作发生的起止时间（帧）。
这是视频领域的“目标检测”任务，只不过是在一维时间轴上进行。


### Notes
90


## Slide 90: 超越分类：时序动作定位 / 检测


### Text 1
超越分类：时序动作定位 / 检测


### Text 2
时空动作检测：
在未修剪的长视频中，同时在空间（定位人物边界框）和时间（定位动作起止）上检测并识别人物执行的原子动作。
挑战：需要同时处理复杂的外观、姿态、运动以及精确的时空定位。


### Notes
91


## Slide 91: 前沿方向：视频大语言模型


### Text 1
前沿方向：视频大语言模型


### Text 2
趋势：将强大的视频编码器（如ViViT, VideoMAE）与大语言模型（LLM）相结合。
能力：实现开放词汇的视频问答、视频描述生成、基于指令的视频内容理解等。


### Text 3
通向通用人工智能（AGI）的重要一步！
