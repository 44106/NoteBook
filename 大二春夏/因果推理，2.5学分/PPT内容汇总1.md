![image-20260421154356265](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421154356265.png)

人工智能学习特点
1模型存在不可解释，不可泛化等问题——关联并未反映客观自然科学规律
2深度学习等人工智能学习特点：数据驱动的关联学习

![image-20260421154527510](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421154527510.png)

![image-20260421154719444](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421154719444.png)

#### GPT 训练：

1.自监督 挖空练习

2.提示学习与指令微调 ：指令微调，是指在已经训练好的语言模型的基础上，通过使用有标注的特定任务数据进行进一步的微调，从而使得模型具备遵循指令的能力

3.人类反馈 强化学习

大模型的训练特点：数据驱动 关联学习

soro超级涌现力：最小单元进行关联组合

![image-20260421155745292](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421155745292.png)

#### 因果如何赋能大模型：

1.因果去除数据偏置

2.因果支撑决策

3.因果赋能transformer

#### AGI三个通用世界模型：

简单来说，目前的AI往往偏科（有的擅长聊天，有的擅长看图），而未来的AGI需要是一个全能选手。这张图把AGI的能力拆解为了三个空间维度的叠加。

以下是详细解读：

**1. 左边的模型：Large Language Model (LLM)**

- **对应维度：语义空间**
- **核心能力：** 处理语言、符号、逻辑和知识。
- **解读：** 这是目前最成熟的领域（比如ChatGPT）。它让AI拥有了“大脑”层面的语言能力，能够理解人类的指令、进行推理、生成文本。它构建了一个基于文字和概念的虚拟世界。
- **作用：** 负责AGI的**认知与沟通**。

**2. 中间的模型：Embodied AI (具身智能)**

- **对应维度：物理空间**
- **核心能力：** 感知、行动、与真实世界交互。
- **解读：** 图中展示了机器人（Robots）在真实世界（Real-World）和模拟环境（Simulation）中导航（Navigation）和互动（Interaction）。这部分强调AI不能只活在服务器里，必须要有“身体”，能够理解物理定律（重力、碰撞等），并能在三维空间中移动和操作物体。
- **作用：** 负责AGI的**行动与感知**（即像人一样在物理世界中生存）。

**3. 右边的模型：Large Data Model (LDM)**

- **对应维度：数据空间**
- **核心能力：** 处理复杂的结构化数据、预测趋势、优化决策。
- **解读：** 图中展示了一个问号“?”，这暗示了这是目前还在探索或定义的领域。它不仅仅是处理文本或图像，而是处理更抽象的“数字数据”。比如金融市场的波动、气象数据的变化、或者复杂的科学计算。
- **作用：** 负责AGI的**量化分析与宏观决策**（处理人类语言描述不了的复杂数据规律）。

**核心结论：什么是AGI？**

幻灯片底部的定义总结了一切：

> **AGI是一种能够在几乎所有认知任务上匹配或超越人类能力的人工智能。**

**总结这张图的意思：**
要实现真正的AGI，我们需要把这三个模型加起来：

- **LLM（语义）** 提供智慧的大脑；
- **Embodied AI（物理）** 提供行动的手脚和感官；
- **LDM（数据）** 提供处理复杂世界规律的能力。

只有这三者融合，AI才能既懂语言，又懂物理世界，还能处理复杂数据，从而真正像人类一样全面。

#### 任何能够满足大量分布变化的遗憾界限的智能体都必须学会近似的因果模型

![image-20260421160552457](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421160552457.png)

![image-20260421160609874](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421160609874.png)

![image-20260421163442077](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421163442077.png)

LLM学习海量数据

而LDM学习数据的因果关系

## 一、因果与关联

模型优化从性能第一到风险控制

### 为什么从关联到因果推理？

1.不可解释

![image-20260421164543233](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421164543233.png)

2.不可用于支撑决策

![image-20260421164554283](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421164554283.png)

3.不稳定，随着时间数据环境变化而变化。绝大多数机器学习方法需要独立同分布假设

![image-20260421164800048](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421164800048.png)

4.关联数据带来不公平性问题

![image-20260421164908323](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421164908323.png)

#### 关联学习导致人工智能的不能

![image-20260421164949425](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421164949425.png)

#### 因果关系的三个层级：

![image-20260421165147204](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421165147204.png)

关联-干预-反事实

#### 关联：

定义： 两个或多个变量之间存在的一种统计依赖关系，当其中==一个变量的取值发生变化时，另一个变量的取值也倾向于随之发生规律性变化==
两个关键条件： 描述了一种共变模式、==不蕴含方向性==
真实案例：
• 下课铃声响起时，学生们同时走出教室
• 下雨天中，行人撑起伞时，地面同时变湿

#### 因果：

引起和被引起的关系，原因和结果。

定义：在控制相关变量不变的前提下，当==一个变量（因）的取值发生变化时，另一个变量（果）的取值也会发生相应的改变==
两个关键条件：保持其他相关变量不变的条件下改变因变量，具有==方向性==
真实案例：
• 在控制其他因素不变的条件下，下课铃声响起后，学生们就会走出教室

#### 因果与关联区别

![image-20260421165932175](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421165932175.png)

#### 混淆偏差

由于共同的原因产生非因果关联。

![image-20260421170250558](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421170250558.png)

#### 选择偏差

![image-20260421170358563](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421170358563.png)

#### 随机对照实验

![image-20260421171122449](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421171122449.png)

非随机样本选择不等于选择偏差，必须非随机样本选择与关心的原因和结果变量有关才行

#### 小结1

人工智能学习特点：数据驱动 ==关联学习== 概率输出

### 1.2潜在结果框架

#### 因果效应估计

![image-20260421171404479](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421171404479.png)

#### 理想方案是存在平行世界

可控相关变量不变，改变原因变量，观察结果变量

#### 金标准：随机试验

#### 个体因果效应

![image-20260421171604192](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421171604192.png)

#### 平均因果效应

![image-20260421171631320](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421171631320.png)

如何计算：![image-20260421171726841](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421171726841.png)

ATE无法揭示个体层面的多样性与复杂性

#### 条件平均因果框架

给定一组协变量X=x的条件下，个体处理效应的期望值![image-20260421172400639](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421172400639.png)

#### 比较

![image-20260421172419757](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421172419757.png)

当条件集合（子群体划分粒度）趋于无穷大，且样本量充足时，条件平均因果效应无限逼近于个体因果效应

#### 潜在结果框架下的可识别假设

![image-20260421172629867](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421172629867.png)

#### 复杂环境下因果推理三大挑战

关键信息缺失、数据偏差多样、干预变量复杂

在现实复杂环境中做因果推断时，科学家必须解决的**三大核心挑战**，以及对应的**科学问题**和**研究成果**。

1. **挑战一：关键信息缺失**
   - **问题：** 数据里缺东西，或者有隐藏的变量（混杂因素）没被记录下来。
   - **解法（研究成果1）：** 利用**工具变量**。就像图中提到的“异质数据下隐组工具变量生成学习”，简单说就是通过一些技巧，在数据缺失的情况下“无中生有”或者“借力打力”来推断因果。
2. **挑战二：数据偏差多样**
   - **问题：** 数据来源不同，分布不一样（比如北京的数据和上海的数据分布不同），导致模型泛化能力差。
   - **解法（研究成果2）：** **变量选择与协同表征**。也就是在复杂的偏差中，找到那些真正稳定、通用的特征变量。
3. **挑战三：干预变量复杂**
   - **问题：** 对应上一页的内容，干预不是简单的0/1，而是复杂的网络或高维数据。
   - **解法（研究成果3）：** **平衡表征与异质对比学习**。通过机器学习的方法，把复杂的数据映射到一个空间里，让因果效应更容易被区分出来。

#### 论文成果

1.因果推断的研究正在从理想化的“二选一”实验，转向处理现实中复杂的、连续的、组合式的干预措施。

2.因果推断不能只看当下，必须把**时间滞后性**和**长期后果**纳入考量，否则会被短期假象迷惑。

3.**不要为了因果而因果，因果推断的终极目标是辅助决策。** 评估一个因果模型好坏的标准，不应仅仅是估计误差（PEHE/MSE），更应该是决策的准确率。

### 1.3结构因果模型

#### 如何表示因果关系

![image-20260421175315084](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421175315084.png)

### 因果图和结构方程

![image-20260421175451924](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421175451924.png)

#### 因果与关系

![image-20260421175644707](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421175644707.png)

#### 基本结构：

1.链结构

![image-20260421175936850](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421175936850.png)

2.分连结构

![image-20260421180020205](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421180020205.png)

3.汇连结构

![image-20260421205829086](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421205829086.png)

#### D-分离与条件独立性

![image-20260421210901442](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421210901442.png)

独立性例题：

![image-20260421211622277](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421211622277.png)

#### 重新解释结构因果模型下的偏差

![image-20260421211723448](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421211723448.png)

#### do-算子

![image-20260421212011025](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421212011025.png)

因此去除了混淆路径，没有偏差

#### e.g.

![image-20260421212227267](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421212227267.png)

![image-20260421212236659](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421212236659.png)

#### do-算子计算因果效应差

操纵概率计算恒等式：

![image-20260421212954602](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421212954602.png)

以及$X垂直于Z$ 因为d-分离，所以条件独立

最终推得调整公式

![image-20260421213316414](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421213316414.png)

![image-20260421213257371](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421213257371.png)

![image-20260421213401627](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421213401627.png)

![image-20260421213543433](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260421213543433.png)

## 二、因果推理

### 2.1因果发现

#### 因果推断&因果发现

前者已知因果图 估计因果效应有多大

后者去学习因果图

#### 因果发现三大方法

![image-20260423122721993](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423122721993.png)

#### 基于约束方法

建立在：因果结构和统计性质存在精确对应关系

![image-20260423112941503](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423112941503.png)

#### 条件独立性检验

![image-20260423113302031](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113302031.png)

#### ==PC算法==

核心策略非常直观：先从一个完全连接的图出发，通过不断"删边"得到
骨架，再通过分离集信息确定边的方向

![image-20260423113451260](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113451260.png)

![image-20260423113500623](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113500623.png)

![image-20260423113728274](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113728274.png)

![image-20260423113908514](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113908514.png)

![image-20260423113850039](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423113850039.png)

![image-20260423114056493](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423114056493.png)

#### PC 算法局限性

![image-20260423115523340](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423115523340.png)

#### PC改进

![image-20260423115642782](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423115642782.png)

#### 对撞结构和叉式结构

A->B<-C    控制B AC相关

A<-B->C    控制B AC独立

### 2.2因果推断

![image-20260423120510529](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423120510529.png)

#### 随机试验

![image-20260423121021632](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423121021632.png)

![image-20260423121053228](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423121053228.png)

随机实验通过==随机分配==平衡干扰因素，有效避免选择偏倚，是可靠评估干预措施因果效应、进行因果推断的核心科研方法。当对照组和实验组中人群特征相同时，通过设计随机实验可以得到==无偏的RCT数据==。利用RCT数据的无偏性，可以直接对组间==直接取平均计算ATE==。

#### 应用场景：

医药领域药物试验 互联网推荐算法比较测试

#### 局限性：

成本高 样本有限

伦理问题

耗时

#### 基于观测数据

![image-20260423122537802](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423122537802.png)

#### 如何平衡实验组和对照组的协变量

#### 经典因果推断方法

**1.匹配法**

![image-20260423122958781](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423122958781.png)

当混杂变量高维时，就无法找到完全一样的个体，失效

**2.基于倾向得分的方法**

- 倾向得分匹配法：**先利用机器学习模型算出每个人接受干预的概率（倾向得分），然后基于这个概率值，把“相似概率”的干预组和对照组样本配对，从而模拟出随机实验的效果，进而准确评估因果效应。**  
- 倾向得分逆加权法：![image-20260423124540727](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423124540727.png)

根据数量分布进行加权，保证变量分布一致（干预和不干预的数量相同）

- 双稳健算法：![image-20260423133758872](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423133758872.png)

**倾向得分模型** **和结果回归模型** 有一个正确就能准确预测

#### 复杂因果推理

- 复杂数据偏差：==工具变量的使用==

说白了就是引入一个有一定关系但很随机的变量 用这个随机性消除其他混杂变量

![image-20260423135555643](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423135555643.png)

![image-20260423150903564](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423150903564.png)

![image-20260423151028911](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423151028911.png)

如何解决

![image-20260423151426802](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423151426802.png)

#### 如何寻找工具变量？

![image-20260423151911340](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423151911340.png)

将X分解为Z和C两个变量 Z只和T有关 C还和Y有关 Z就是我们需要的工具变量 但是不能保证Z和Y完全解耦 

#### 复杂偏差下的因果推断

**选择偏差**：

![image-20260423152632239](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423152632239.png)

**碰撞偏差**：

![image-20260423152755979](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423152755979.png)

S是碰撞节点

==解决方法——影子变量==

![image-20260423154514422](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423154514422.png)

如何获得？不断从X中学习出一个影子变量，检验是否复合条件，（一个等式），满足就是我们需要的影子变量

#### 两种偏差同时出现？

![image-20260423201954179](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423201954179.png)

利用工具变量Z，解耦成残差R（混杂信息）和影子变量$\phi$,

#### 如何用历史数据作为工具变量

![image-20260423202722825](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423202722825.png)

**例子**

![image-20260423202752537](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423202752537.png)

#### 复杂干预变量

**干预组变为多种离散值或者为连续变量**

##### 倾向得分方法扩展

![image-20260423203109117](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423203109117.png)

##### 混杂变量平衡法

从之前的加权方法（由于干预空间过大，产生极端权重）转化为表征学习方法

![image-20260423203939050](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423203939050.png)

- 经典的二元干预架构CFRNet：用原始特征X提取全新的高维特征$\phi(X)$，然后学习出剥离干预影响的纯净特征，双预测头是防止一维干预变量被淹没，强行使其作用
- 多值干预：m个预测头，两两对齐
- 多维/连续：共享预测头，但是引入“互信息”，让提取的特征不能和T有任何关联，保持独立，因此被平衡。
- 连续干预另一解：先分类划分区间，再回归预测

#### 连续干预效应估计

目标是在连续干预变量下让干预变量和协变量独立

- 随机打乱干预变量，伪造一个没有混杂偏差的数据集
- 给真实的数据集赋予权重，使其逼近完美数据集

![image-20260423210037212](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423210037212.png)

- 其实是用生成对抗式网络来进行权重的不断学习，最终排除混杂干扰。也即GAD

![image-20260423210634390](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423210634390.png)

#### 高维混杂变量

![image-20260423211657717](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423211657717.png)

如何实现？

![image-20260423212140894](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423212140894.png)

之前的很多方法主要关注“干预前”的变量（比如用户的年龄、性别），但现实中还有很多“干预后”或“结果前”的变量（比如吃药后的身体反应）。
**核心问题**：对于这些复杂的变量，我们该如何处理？是全都要（Brute-force），还是有选择地要？

三种策略的对比（中间的三张图）

这部分通过因果图展示了三种处理变量的思路：

- **图(a) Brute-force（暴力法）**：

  - 这是最传统的做法。它假设所有的协变量 U*U* （包括 X*X* ）都是混杂因素。
  - **做法**：不管三七二十一，把所有观测到的变量 X*X* 都放进模型里去调整。
  - **缺点**：如果 X*X* 里包含了“工具变量”（只影响T不影响Y）或者“无关变量”，强行调整反而可能增加偏差或方差。

- **图(b) Separation（分离法）**：

  - 这是更精细的做法（也是上一张PPT讲的内容）。它试图把变量 

    U*U*

     拆分成三类：

    - I*I* （蓝色）：工具变量（只影响 T*T* ）。
    - X*X* （黄色）：混杂变量（影响 T*T* 和 Y*Y* ）。
    - Z*Z* （绿色）：调整变量（只影响 Y*Y* ）。

  - **做法**：只调整 X*X* 和 Z*Z* ，排除 I*I* 。

- **图(c) Ours（本文提出的方法）**：

  - 这是最复杂的情况，也是这篇论文（KDD 2023）的贡献。它认为变量之间可能有更复杂的关系，比如存在多层的工具变量（ I1,I2*I*1,*I*2 ）或多层的调整变量（ Z1,Z2*Z*1,*Z*2 ）。
  - **附加假设**：这里特别提到“不存在中介变量”（即 T*T* 到 Y*Y* 之间没有中间传导变量），这是为了简化问题。
  - **理论结论**：==最优的特征组合应该是**“混杂变量” + “与结果相关的协变量”**==。

  #### 高维因果推理

  ![image-20260423213417677](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423213417677.png)

![image-20260423213505251](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423213505251.png)

#### 高维处理方法![](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423215236931.png)

做减法时会遇到的问题：

![image-20260423215331511](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423215331511.png)

#### 复杂环境：

当研究对象超出独立个体、单次处理、单一人群的经典设定时，因果推断需要在效应定义、识别条件与估计方法上进行结构性扩展，典型包括：干扰或网络效应、纵向动态过程、连续时间事件过程、跨人群外推与可迁移性。

![image-20260423220528984](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423220528984.png)

![image-20260423220611633](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423220611633.png)

### 因果赋能机器学习：

![image-20260423221553064](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423221553064.png)

![image-20260423221711567](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260423221711567.png)

#### 因果约束项：

学习全局样本权重 使得变量集合X中任何两个变量都相互独立，能找到因果相关项，丢弃混淆项

#### 传统表征学习的局限性

![image-20260424154905208](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424154905208.png)

#### 因果表征学习

从观测变量->低维潜在变量

![image-20260424154944396](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424154944396.png)

#### 不同环境下的因果表征学习：

- IID条件下（独立同分布）
  - 线性高斯情形：计算协方差![image-20260424155245849](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424155245849.png)![image-20260424155323998](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424155323998.png)![image-20260424155345336](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424155345336.png)
  - 线性非高斯![image-20260424160758900](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424160758900.png)![image-20260424161028873](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424161028873.png)![image-20260424161116649](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424161116649.png)
  - 非线性模型 结构稀疏性![image-20260424161344321](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424161344321.png)

- 多分布环境下因果表征学习：![image-20260424161904880](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424161904880.png)

![image-20260424162039813](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424162039813.png)

![image-20260424162436309](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424162436309.png)

#### 时序数据下的因果表征学习：

![image-20260424162739381](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424162739381.png)

![image-20260424162905248](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424162905248.png)

![image-20260424163058100](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424163058100.png)

![image-20260424165736621](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424165736621.png)

#### 数据抽象

![image-20260424170659327](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424170659327.png)

![image-20260424170736226](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424170736226.png)

![image-20260424171329827](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424171329827.png)

#### 因果公平：

![image-20260424171626581](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424171626581.png)

![image-20260424171704591](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424171704591.png)

![image-20260424172353679](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424172353679.png)

长短期兴趣

因果因子不变形

![image-20260424173424330](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424173424330.png)

### 四、因果与大模型

#### 语言模型定义：![image-20260424202345013](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424202345013.png)



![image-20260424202419173](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424202419173.png)

"预测下一个词"这一简单目标，迫使模型学习语言的深层规律和世界知识，这正是大模型涌现智能的根本原因。

#### NLP难的原因：

歧义 高度上下文相关 离散符号系统词汇多

#### 发展进程：

符号主义：规则驱动 ==形式逻辑和显示定义==的规则捕捉？

里程碑：ELIZA SHRDLU 定义了语言的边界 在受限领域 暴露符合主义的局限：基于规则的系统无法应对语言的==模糊性、进化和数不胜数的特殊情况==，规则回指数级增长

数据驱动范式崛起：从大规模文本语料库中自动学习模式，而手写规则。这一范式的转变标志着NLP从"教机器语法"转向"让机器自己发现规律"。![image-20260424203759610](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424203759610.png)

瓶颈：![image-20260424203908370](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424203908370.png)

深度学习范式：高维连续向量代替离散统计技术 捕捉语义相似性![image-20260424204129010](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424204129010.png)

RNN：引入隐藏状态作为记忆机制 可以捕捉任意长上下文依赖![image-20260424204246743](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424204246743.png)

LSTM：门控机制 缓解梯度消失 

无法并行训练

transformer:单词和单词的关联关系![image-20260424212556743](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424212556743.png)

![image-20260424212653951](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424212653951.png)

#### 预训练和微调两范式

![image-20260424212801183](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424212801183.png)

![image-20260424213133532](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213133532.png)

![image-20260424213401993](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213401993.png)

![image-20260424213620913](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213620913.png)

![image-20260424213745560](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213745560.png)

![image-20260424213844560](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213844560.png)

![image-20260424213920310](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424213920310.png)

![image-20260424214044290](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424214044290.png)

![image-20260424214135111](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424214135111.png)

![image-20260424214209186](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424214209186.png)

![image-20260424214648512](C:\Users\SuianWu\AppData\Roaming\Typora\typora-user-images\image-20260424214648512.png)
