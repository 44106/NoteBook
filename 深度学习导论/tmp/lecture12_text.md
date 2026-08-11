# ???? ???? - PPT????
??: C:\Users\njb18\Downloads\深度学习导论\第十二课 检索增强.pptx
????: 114
??: 217 ?; ??: {'.svg': 10, '.png': 181, '.jpeg': 22, '.gif': 3, '.bin': 1}

## Slide 1
### Shapes/Text
- [3.1] 标题 1: 第十二章：检索增强生成
- [5] 文本框 10: 主讲教师：毛玉仁
- [6] 文本框 3: 课程名称：深度学习导论
### Images
- ppt/media/image1.png

## Slide 2
### Shapes/Text
- [3] object 5: 幻觉现象
- [4] 矩形 2: 大语言模型（LLMs）生成的内容可能存在“幻觉”现象：生成内容看似合理但实际上逻辑混乱或与事实相悖。
### Tables
- [16] 表格 6
  -  | GPT-4o | Claude 3.5 | Gemini | 通义千问 | 文心一言 | 豆包 | Kimi
  - 9.11和9.9哪个大？ |  |  |  |  |  |  | 
### Images
- ppt/media/image2.png
- ppt/media/image3.png
- ppt/media/image4.png
- ppt/media/image5.png
- ppt/media/image6.png
- ppt/media/image7.png
- ppt/media/image8.svg
- ppt/media/image9.svg

## Slide 3
### Shapes/Text
- [3] object 5: 幻觉现象
- [4] 矩形 2: “幻觉”现象可能直接来源于训练数据中的知识错误，也可能源于训练出的模型本身对知识的掌握不足。
- [6] 矩形 27: 训练数据
- [8] 矩形 30: 模型本身
- [9] 矩形 31: 知识过时 / 知识边界 / 知识偏差 / 对齐不当 / 
- [10] 矩形 33: 知识长尾 / 曝光偏差 / 解码偏差
### Images
- ppt/media/image10.png
- ppt/media/image11.jpeg

## Slide 4
### Shapes/Text
- [3] object 5: 幻觉现象-训练数据
- [4] 矩形 2: 知识过时：由于训练数据中的时间滞后，其中的知识可能在模型训练后又发生了更新，导致模型内部知识过时。
- [5] 矩形 30: 正确答案：西班牙队。
- [6] 文本框 11: 注：例子中的大语言模型采用 DeepSeek-V2.5.
- [10] 圆角矩形标注 33: Once we were the champions !
- [11] 圆角矩形标注 36: NOW IT IS US !!!
### Images
- ppt/media/image12.png
- ppt/media/image13.png
- ppt/media/image14.jpeg
- ppt/media/image9.svg
- ppt/media/image8.svg

## Slide 5
### Shapes/Text
- [3] 矩形 2: 知识边界：由于训练数据的有限性，无法覆盖所有范围，且知识在训练数据采集完成后仍会不断新增。
- [4] 文本框 4: 注：例子中的大语言模型采用 GPT-3.5.
- [6] 矩形 14: 正确答案：考拉的基因组包含了大约26,000个基因。
- [8] object 5: 幻觉现象-训练数据
### Images
- ppt/media/image15.png
- ppt/media/image16.jpeg

## Slide 6
### Shapes/Text
- [3] 矩形 2: 知识偏差：训练数据中可能包含不实与偏见信息。
- [4] 文本框 4: 注：例子中的大语言模型采用 GPT-4o.
- [5] object 5: 幻觉现象-训练数据
- [7] 圆角矩形标注 17:    默认描述男性，忽略了    /    女性身份的成功企业家。
- [11] 圆角矩形标注 22: 不应有性别偏见
### Images
- ppt/media/image9.svg
- ppt/media/image17.png
- ppt/media/image18.jpeg
- ppt/media/image8.svg

## Slide 7
### Shapes/Text
- [5] 矩形 1: 对齐不当：在模型与人类偏好对齐阶段中，偏好数据标注不当可能引入了不良偏好。
- [6] object 5: 幻觉现象-训练数据
- [8] 矩形 10: 人类标注
- [11] 矩形 36: 人类标注
- [13] 矩形 38: 大模型 / 候选答案
- [14] 矩形 40: 用户问题
- [16] 矩形 48: 偏好数据标注过程引入偏差
- [17] 矩形 49: 模型推理过程出现不良偏好
### Notes
- 不用画框，改一下图标
### Images
- ppt/media/image19.png
- ppt/media/image20.png
- ppt/media/image21.png
- ppt/media/image22.png
- ppt/media/image23.png
- ppt/media/image24.png

## Slide 8
### Shapes/Text
- [3] 矩形 16: 正确答案：美国心理学家G.W.奥尔波特。
- [7] 矩形 33: 知识长尾：训练数据中部分信息的出现频率较低，导致模型对这些知识的学习程度较低。
- [8] object 5: 幻觉现象-模型本身
- [9] 矩形 12: 卡尔·罗杰斯
- [10] 矩形 13: G.W.奥尔波特
- [11] 文本框 14: 注：例子中的大语言模型采用 GPT-3.5.
- [13] 圆角矩形标注 18:     Haha, that's not me.
- [14] 圆角矩形标注 19: IT’S ME !
### Images
- ppt/media/image25.png
- ppt/media/image26.jpeg
- ppt/media/image27.png
- ppt/media/image9.svg
- ppt/media/image8.svg

## Slide 9
### Shapes/Text
- [4] 矩形 1: 曝光偏差：由于模型训练与推理任务存在差异，导致模型在实际推理时存在偏差。
- [5] 矩形 64: 模型训练过程采用Teacher Forcing
- [9] 文本框 67: Ground Truth
- [10] 矩形 68: 模型推理过程会出现错误累积
- [11] object 5: 幻觉现象-模型本身
### Images
- ppt/media/image28.png
- ppt/media/image29.png

## Slide 10
### Shapes/Text
- [3] 矩形 1: 解码偏差：模型解码策略中的随机因素可能影响输出的准确性。
- [4] object 5: 幻觉现象-模型本身
- [12] 矩形 18: 解码过程中存在的随机性导致模型可能输出不符合常理的内容。
- [14] 圆角矩形标注 16:    符合常理
- [15] 圆角矩形标注 17:  不符合常理
### Images
- ppt/media/image30.png
- ppt/media/image31.jpeg
- ppt/media/image32.png
- ppt/media/image33.svg
- ppt/media/image34.png
- ppt/media/image9.svg
- ppt/media/image8.svg

## Slide 11
### Shapes/Text
- [4] 矩形 1: 如何缓解幻觉问题呢？类别人类的解决方式，当我们遇到无法回答的问题时，通常会借助搜索引擎或查阅书籍资料来寻找相关信息。
- [5] object 5: RAG止“幻”
- [6] 文本框 7: 2023年的考拉数量大约有多少？
- [14] 文本框 25: 2023年，调整后的考拉种群估计数（考虑到数据很少或没有数据的地区）得出的考拉种群估计数在86,000至176,000之间。
- [21] 文本框 38: 2023年的考拉数量在86.000至176.000之间。
### Images
- ppt/media/image35.jpeg
- ppt/media/image36.png
- ppt/media/image37.png
- ppt/media/image38.png
- ppt/media/image39.png
- ppt/media/image40.png

## Slide 12
### Shapes/Text
- [5] object 5: RAG止“幻”
- [6] 矩形 12: 因此，对于大语言模型，同样可以通过检索与问题相关的信息进行辅助，从而有效缓解“幻觉”现象，大幅提升模型的生成质量。这便是检索增强生成（RAG）的核心思想。
- [8] 文本框 60: 2023年的考拉数量大约有多少？
- [16] 文本框 68: 2023年，调整后的考拉种群估计数（考虑到数据很少或没有数据的地区）得出的考拉种群估计数在86,000至176,000之间。
- [19] 文本框 75: 2023年的考拉数量在86.000至176.000之间。
- [23] 文本框 110: 大模型
- [25] 文本框 4: 大模型
### Images
- ppt/media/image35.jpeg
- ppt/media/image36.png
- ppt/media/image37.png
- ppt/media/image38.png
- ppt/media/image41.png
- ppt/media/image42.png
- ppt/media/image43.png
- ppt/media/image44.png
- ppt/media/image40.png
- ppt/media/image39.png

## Slide 13
### Shapes/Text
- [8] 文本框 60: 2023年的考拉数量大约有多少？
- [16] 文本框 68: 2023年，调整后的考拉种群估计数（考虑到数据很少或没有数据的地区）得出的考拉种群估计数在86,000至176,000之间。
- [19] 文本框 75: 2023年的考拉数量在86.000至176.000之间。
- [21] 圆角矩形 108: 知识检索
- [22] 圆角矩形 109: 生成增强
- [27] object 5: RAG概念与组成
- [28] 矩形 82: RAG（Retrieval-Augmented Generation），即检索增强生成，是一种从外部数据库中检索相关信息来辅助改善大语言模型生成质量的系统。一个基本的RAG框架主要包含知识检索和生成增强两大模块。
- [31] 文本框 5: 大模型
- [32] 文本框 6: 大模型
### Images
- ppt/media/image35.jpeg
- ppt/media/image36.png
- ppt/media/image37.png
- ppt/media/image38.png
- ppt/media/image41.png
- ppt/media/image42.png
- ppt/media/image43.png
- ppt/media/image44.png
- ppt/media/image40.png
- ppt/media/image39.png

## Slide 14
### Shapes/Text
- [3] object 5: RAG概念与组成
- [4] 矩形 3: RAG（Retrieval-Augmented Generation），即检索增强生成，是一种从外部数据库中检索相关信息来辅助改善大语言模型生成质量的系统。一个基本的RAG框架主要包含知识检索和生成增强两大模块。
- [12] 文本框 55: 2023年的考拉数量大约有多少？
- [20] 文本框 63: 2023年，调整后的考拉种群估计数（考虑到数据很少或没有数据的地区）得出的考拉种群估计数在86,000至176,000之间。
- [23] 文本框 66: 2023年的考拉数量在86.000至176.000之间。
- [29] 圆角矩形 82: 知识检索
- [30] 文本框 86: 对输入问题进行编码，从大规模的知识库（如维基百科）中高效检索出与问题相关的文档。常用的检索算法包括基于关键词匹配的稀疏检索算法与基于神经网络的稠密检索算法；
- [33] 圆角矩形 83: 生成增强
- [34] 文本框 87: 利用检索文档和输入问题，生成最终的输出序列，一般采用预训练语言模型如Llama等。生成器利用外部知识的最常见的方式便是通过Prompt的形式。
### Images
- ppt/media/image35.jpeg
- ppt/media/image36.png
- ppt/media/image37.png
- ppt/media/image38.png
- ppt/media/image41.png
- ppt/media/image42.png
- ppt/media/image43.png
- ppt/media/image44.png

## Slide 15
### Shapes/Text
- [3] object 5: RAG概念与组成
- [5] 矩形 9: RAG（Retrieval-Augmented Generation），即检索增强生成，是一种从外部数据库中检索相关信息来辅助改善大语言模型生成质量的系统。
### Notes
- 换一个原来ppt的图
### Images
- ppt/media/image45.png

## Slide 16
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 16
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png

## Slide 17
### Shapes/Text
- [3] object 5: RAG架构分类
- [4] 矩形 3: 在RAG中，大语言模型根据参数进行感知和调节可分为“黑盒”模型与“白盒”模型。其中，闭源模型视为“黑盒”模型，而开源模型根据是否对参数微调既可视作“白盒”模型也可视作“黑盒”模型。
- [5] 文本框 21: 常见闭源模型
- [16] 圆角矩形标注 19:  “黑盒”模型
- [17] 文本框 21: 常见开源模型
- [18] 圆角矩形标注 27:  视为“黑盒”
- [19] 圆角矩形标注 28:  “白盒”模型
### Images
- ppt/media/image46.png
- ppt/media/image47.png
- ppt/media/image48.png
- ppt/media/image49.jpeg
- ppt/media/image50.jpeg
- ppt/media/image41.png
- ppt/media/image42.png
- ppt/media/image43.png
- ppt/media/image44.png
- ppt/media/image51.svg

## Slide 18
### Shapes/Text
- [3] object 5: RAG架构分类
- [4] 矩形 1: 从是否对大语言模型进行的参数进行更新的角度出发，RAG架构可分为两大类： / 黑盒增强架构和白盒增强架构。 
- [8] 矩形 5: 黑盒增强架构
- [10] 矩形 7: 白盒增强架构
### Images
- ppt/media/image52.png
- ppt/media/image53.png
- ppt/media/image54.gif

## Slide 19
### Shapes/Text
- [3] object 5: 黑盒增强架构
- [4] 矩形 3: 黑盒增强架构可根据是否对检索器进行微调分为两类：无微调和检索器微调
- [5] 文本框 5: 语言模型参数不变，检索器根据语言模型的输出反馈进行参数的针对性调整。
- [9] 矩形 2: 无微调架构
- [11] 矩形 6: 检索器微调架构
- [12] 文本框 10: 检索器和大语言模型均不进行任何微调，仅依靠它们在预训练阶段掌握的能力完成相应的检索和生成任务。
### Images
- ppt/media/image55.png
- ppt/media/image56.png
- ppt/media/image54.gif

## Slide 20
### Shapes/Text
- [3] object 5: 白盒增强架构
- [4] 文本框 2:  / 检索器和大语言模型迭代交互、一起协同微调。
- [5] 矩形 3: 白盒增强架构也可根据是否对检索器进行微调分为两类：仅微调大语言模型和检索器与大语言模型协同微调（简称协同微调）。
- [7] 矩形 5: 仅微调大语言模型
- [9] 矩形 8: 协同微调
- [12] 文本框 13: 仅微调大语言模型：检索器其参数保持不变，语言模型根据检索器提供的信息进行参数调整。
### Images
- ppt/media/image57.png
- ppt/media/image58.png
- ppt/media/image54.gif

## Slide 21
### Shapes/Text
- [3] object 5: 黑盒增强架构——无微调
- [4] 矩形 1: 检索器和大语言模型在RAG过程中参数不更新，二者直接组合使用来完成生成任务。代表性方法是In-Context RALM。其直接将检索器检索到的文档前置到输入问题前作为上下文。
- [6] 文本框 9: Ori Ram, Yoav Levine, Itay Dalmedigos et al. 2023. In-context retrieval-augmented language models. In TACL. 
### Images
- ppt/media/image59.png

## Slide 22
### Shapes/Text
- [3] object 5: 黑盒增强架构——无微调
- [4] 矩形 1: 检索器和大语言模型在RAG过程中参数不更新，二者直接组合使用来完成生成任务。代表性方法是In-Context RALM。
- [5] 文本框 2: In-Context RALM方法与大模型解耦，易于实现，计算成本最低，相比于无检索能提升性能； /  / 该方法大模型与检索器缺乏交互，完全依赖大模型的指令跟随能力，RAG整体效果难保证。
- [8] 文本框 4: 困惑度 / 越低越好
- [9] 文本框 6: 相较于不检索，该方法 / 能显著提升回答性能
### Images
- ppt/media/image60.png
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 23
### Shapes/Text
- [4] 矩形 1: 大语言模型参数固定，检索器参数根据大语言模型的输出进行更新，使检索器能更好地适应大语言模型的需求。代表性方法为REPLUG。其使用语言模型的困惑度作为监督信号来训练检索器，以检索出能够显著降低语言模型困惑度的文档。
- [5] object 5: 黑盒增强架构——检索器微调
- [6] 文本框 9: Weijia Shi, Sewon Min et al. 2023. Replug: Retrieval-augmented black-box language models. arXiv preprint arXiv:2301.12652 (2023).
### Images
- ppt/media/image63.png

## Slide 24
### Shapes/Text
- [3] 矩形 1: 大语言模型参数固定，检索器参数根据大语言模型的输出进行更新，使检索器能更好地适应大语言模型的需求。代表性方法为REPLUG。
- [4] 文本框 3: REPLUG 更新检索器以迎合LLM的需求，无需更新LLM，成本低，效果良好 /  / LLM 参数固定，可能无法与检索器良好适配。 / 
- [7] 文本框 9: 微调检索器效果良好
- [8] object 5: 黑盒增强架构——检索器微调
- [11] 文本框 6: 指标为BPB，越低越好
### Images
- ppt/media/image64.png
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 25
### Shapes/Text
- [3] 矩形 1: 检索器作为一个预先训练好的组件其参数保持不变，大语言模型根据检索器输出对自身参数进行更新。代表性方法为RETRO。其通过交叉编码，将检索信息动态地融合到大语言模型的隐藏状态中。
- [5] object 5: 白盒增强架构——仅微调语言模型
- [6] 文本框 9: Sebastian Borgeaud et al. 2022. Improving language models by retrieving from trillions of tokens. In ICML.
### Images
- ppt/media/image65.png

## Slide 26
### Shapes/Text
- [3] 文本框 3: 该方法能优化语言模型生成能力，使其能够更好地利用检索到的外部信息； /  / 微调资源需求高；微调效果依赖原生的检索器的性能。 / 
- [5] 矩形 12: 检索器作为一个预先训练好的组件其参数保持不变，大语言模型根据检索器输出对自身参数进行更新。代表性方法为RETRO。
- [6] object 5: 白盒增强架构——仅微调语言模型
- [8] 文本框 16: 相较于其他方法， / RETRO能显著降低困惑度
### Images
- ppt/media/image66.png
- ppt/media/image67.png
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 27
### Shapes/Text
- [4] 矩形 1: 在检索器和语言模型协同微调的架构中，检索器和语言模型的参数更新同步进行。代表性方法为ATLAS。其使用 KL 散度损失函数来联合训练检索器和语言模型，以确保检索器输出的文档相关性分布与文档对语言模型的贡献分布相一致。
- [5] object 5: 白盒增强架构——协同微调
- [6] 文本框 9: Gautier Izacard, Patrick Lewis et al. 2023. ATLAS: Few-shot learning with retrieval augmented language models. In JMLR.
### Images
- ppt/media/image68.png

## Slide 28
### Shapes/Text
- [3] 文本框 3: 检索器和语言模型能够在训练过程中深度交互，不断优化RAG性能。 /  / 资源需求高；实现与训练过程复杂。
- [5] 矩形 8: 在检索器和语言模型协同微调的架构中，检索器和语言模型的参数更新同步进行。代表性方法为ATLAS。
- [8] object 5: 白盒增强架构——协同微调
- [11] 文本框 4: 指标为EM，越高越好
### Images
- ppt/media/image69.png
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 29
### Shapes/Text
- [3] object 5: 对比与分析
- [5] 文本框 6: 与LLM解耦，且易于实现，计算成本最低
- [6] 文本框 7: 计算成本高；实现与训练过程复杂
- [7] 文本框 8: 检索器和LLM在训练中深度交互，不断优化RAG性能
- [8] 文本框 9: 更新检索器迎合LLM需求，成本低，效果良好
- [9] 文本框 10: LLM与检索器缺乏交互，RAG效果难保证
- [10] 文本框 11: LLM参数固定，可能无法与检索器良好适配。 / 
- [11] 文本框 12: 计算成本高；微调效果依赖原生的检索器的性能
- [14] 文本框 15: 优化语言模型生成能力，更好地利用检索到的外部信息
### Tables
- [4] 表格 4
  - 架构分类 |  | 优点 | 缺点
  - 黑盒增强 | 无微调(e.g. In-context ralm) |  | 
  -  | 检索器微调(e.g. Replug, AAR) |  | 
  - 白盒增强 | 仅微调语言模型(e.g. realm, Self-rag) |  | 
  -  | 协同微调(e.g. Atlas) |  | 
### Images
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 30
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 30
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png

## Slide 31
### Shapes/Text
- [3] object 5: 知识检索
- [5] 矩形 9: 如何检索出相关信息来辅助改善大语言模型生成质量的系统。
### Notes
- 换一个原来ppt的图
### Images
- ppt/media/image45.png
- ppt/media/image54.gif

## Slide 32
### Shapes/Text
- [1] 矩形 2: 知识检索通常包括知识库构建、查询构建、文本检索和检索结果重排四部分。
- [5] object 5: 知识检索
### Notes
- 合并32、33
### Images
- ppt/media/image70.png

## Slide 33
### Shapes/Text
- [3] object 5: 知识库构建
- [4] 文本框 14: 从不同渠道整合、转换多元数据资源，将其转换为统一的文档对象。例如维基百科语料库，采集内容不仅包括正文，还包括一系列元信息，如标题、目录、分类等。 
- [5] 矩形 20: 数据采集与预处理：数据采集与预处理为构建知识库提供“原材料”
- [22] 矩形 23: 数据采集
- [24] 矩形 30: 存储库
- [25] 矩形 31: 采集数据
### Images
- ppt/media/image35.jpeg
- ppt/media/image71.jpeg
- ppt/media/image72.jpeg
- ppt/media/image73.jpeg
- ppt/media/image74.png
- ppt/media/image75.png
- ppt/media/image76.png
- ppt/media/image77.png
- ppt/media/image78.png
- ppt/media/image79.png
- ppt/media/image80.png
- ppt/media/image81.png
- ppt/media/image82.png

## Slide 34
### Shapes/Text
- [3] object 5: 知识库构建
- [4] 文本框 30: 数据清洗：清除文本中的干扰元素，如特殊字符等； / 文本分块：将大块本切割成较小单元，例如把一篇长文章分为多个短段落。
- [8] 矩形 26: 文本分块
- [10] 矩形 14: 数据清洗
- [12] 矩形 13: 数据采集与预处理：数据采集与预处理为构建知识库提供“原材料”。
- [14] 矩形 16: 数据预处理
### Images
- ppt/media/image83.png
- ppt/media/image84.png

## Slide 35
### Shapes/Text
- [4] object 5: 知识库构建
- [5] 矩形 13: 文本分块后得到的文本片段更精细，能更准确地匹配用户的查询意图，提升检索结果的相关性。文本分块方法包括固定大小分块、和基于内容的分块两种方法。
- [6] 文本框 12: 句分割/递归分割 /     （1）用句号和换行分割句子； /     （2）借助强大的 NLP 库来进行句分割，例如NLTK，spaCy 等； /         …… / 用LLM进行分割 /      利用LLM按照语义进行分块。
- [8] 矩形 22: 固定大小分块
- [9] 文本框 24: 简单直观，按照预先设定的固定长度，将文本划分为若干块。
- [11] 矩形 28: 基于内容的分块
- [12] 文本框 31: 根据待分块的内容，对文本进行更贴合内容逻辑的分块。
### Images
- ppt/media/image85.bin

## Slide 36
### Shapes/Text
- [3] object 5: 知识库构建
- [4] 文本框 14: 利用大语言模型生成与知识库中的文档内容紧密相关的伪查询，可以作为相关文档的“键”，供检索时与用户查询进行匹配。
- [5] 矩形 20: 知识库增强：知识库增强是通过改进和丰富知识库的内容和结构，为查询提供“抓手”，包括查询生成与标题生成两种方法。
- [6] 文本框 30: 利用大语言模型为没有标题的文档生成合适的标题，可以帮助快速理解文档内容，并在检索时更准确地定位到与用户提问相关的信息。
- [10] 矩形 15: 伪查询生成
- [12] 矩形 17: 标题生成
### Images
- ppt/media/image86.png
- ppt/media/image87.png

## Slide 37
### Shapes/Text
- [3] object 5: 查询构建
- [4] 矩形 15: 查询构建: 旨在通过查询增强的方式，扩展和丰富用户查询的语义和内容，提高检索结果的准确性和全面性，“钩”出相应内容。增强方式可分为语义增强与内容增强。
- [6] 矩形 9: 语义增强
- [7] 文本框 11: 查询的语义增强旨在通过同义改写和多视角分解等方法来扩展、丰富用户查询的语义，以提高检索的准确性和全面性。
- [9] 矩形 13: 内容增强
- [10] 文本框 17: 查询的内容增强旨在通过背景文档生成等方法挖掘出与查询主题相关的内容，提供更全面的知识支撑，丰富查询的广度与深度。

## Slide 38
### Shapes/Text
- [4] 矩形 8: 同义改写：通过将原始查询改写成相同语义下不同的表达方式，来解决用户查询单一的表达形式可能无法全面覆盖到知识库中多样化表达的知识的问题。
- [5] object 5: 查询语义增强
- [7] 矩形 11: 同义改写
### Images
- ppt/media/image88.png

## Slide 39
### Shapes/Text
- [4] 矩形 7: 多视角分解：采用分而治之的方法来处理复杂查询，将复杂查询分解为不同视角的子查询，以检索到查询相关的不同角度的信息，从而生成更为全面的答案。 
- [5] object 5: 查询语义增强
- [7] 矩形 8: 多视角分解
### Images
- ppt/media/image89.png

## Slide 40
### Shapes/Text
- [4] 文本框 9: 注：图中的大模型采用的型号为 GPT-4o。
- [5] 矩形 10: 背景文档生成：旨在利用大语言模型在原始查询的基础上，生成与查询内容相关的背景文档，从而丰富查询的广度与深度。
- [6] object 5: 查询内容增强
- [8] 矩形 12: 背景文档生成
### Images
- ppt/media/image90.png

## Slide 41
### Shapes/Text
- [3] object 5: 文本检索
- [4] 矩形 4: 给定知识库和用户查询，文本检索旨在找到知识库中与用户查询相关的知识文本；检索效率增强旨在解决检索时的性能瓶颈问题。
- [6] 文本框 3: 知识库
- [9] 文本框 14: 与用户查询 / 相关的知识文本
- [10] 文本框 16: 用户查询
- [13] 文本框 22: …
- [17] 文本框 12: 检索器
### Notes
- 颜色，排版
### Images
- ppt/media/image91.png
- ppt/media/image92.png
- ppt/media/image93.png
- ppt/media/image10.png
- ppt/media/image94.png
- ppt/media/image95.png
- ppt/media/image96.png

## Slide 42
### Shapes/Text
- [1] 矩形 2: 优化检索过程，提升检索的质量和效率，对改善 RAG 的性能具有重要意义。
- [5] 文本框 16: 检索的质量（召回率、精度、多样性等）会直接影响大语言模型的生成质量。
- [6] 矩形 13: 检索质量
- [12] 矩形 24: 袋熊
- [13] 矩形 25: 树袋熊
- [14] object 5: 文本检索
### Images
- ppt/media/image97.png
- ppt/media/image16.jpeg
- ppt/media/image98.png

## Slide 43
### Shapes/Text
- [1] 矩形 2: 优化检索过程，提升检索的质量和效率，对改善 RAG 的性能具有重要意义。
- [5] 文本框 16: 检索的效率也是评估整个RAG系统性能的关键部分，将极大影响用户的使用体验。
- [6] 矩形 13: 检索效率
- [8] 矩形 27: 等不了了！
- [12] 矩形 30: 啊啊啊啊啊！
- [14] 文本框 22: 不同检索索引的查询时间 / 向量数
- [15] 文本框 23: 图源：https://www.pinecone.io/learn/series/faiss/faiss-tutorial/
- [16] object 5: 文本检索
### Images
- ppt/media/image99.png
- ppt/media/image100.jpeg
- ppt/media/image101.png
- ppt/media/image102.png

## Slide 44
### Shapes/Text
- [3] object 5: 文本检索
- [4] 矩形 4: 常见的文本检索器可以分为三类：判别式检索器、生成式检索器和图检索器。 
- [5] 矩形: 圆角 2: 判别式检索器
- [6] 矩形: 圆角 8: 生成式编码器
- [8] 矩形: 圆角 11: 图检索器
### Notes
- 改成之前的四种架构
### Images
- ppt/media/image103.png
- ppt/media/image104.png
- ppt/media/image105.png

## Slide 45
### Shapes/Text
- [3] object 5: 判别式检索器
- [4] 矩形 4: 判别式检索器对问题和文档进行特征向量提取，以得到问题和文档的相关性分数。判别式检索器包括稀疏编码器，交叉编码器和双编码器三类。 
- [6] 矩形: 圆角 2: 稀疏编码器
- [7] 矩形: 圆角 8: 交叉编码器
- [9] 矩形: 圆角 11: 双编码器
### Notes
- 改成之前的四种架构
### Images
- ppt/media/image106.png

## Slide 46
### Shapes/Text
- [4] 矩形 4: 一类经典的判别式检索器是稀疏检索器，其使用稀疏表示方法来匹配文本。其中TF-IDF是一种典型的稀疏检索方法。
- [5] 文本框 16: TF-IDF 基于词频（TF）和逆文档频率（IDF）来衡量词语在语料库中的重要性，然后用此重要性对文本进行编码。
- [7] object 5: 判别式检索器
- [9] 矩形 10: TF-IDF
### Notes
- 先给出IT-IDF
### Images
- ppt/media/image107.png
- ppt/media/image108.png

## Slide 47
### Shapes/Text
- [5] 文本框 15: 其中，IDF 衡量词语的普遍性，TF 表示词语在文档中的出现频率：
- [6] 文本框 19: # 总文档数
- [7] 文本框 22: # 包含 i 的文档数
- [8] 文本框 30: 句子中词语的 TF-IDF 值的计算方式：
- [13] 文本框 1: # i在文档j中出现次数
- [14] 文本框 2: #文档 j中的总词数
- [16] 矩形 20: 一类经典的判别式检索器是稀疏检索器，其使用稀疏表示方法来匹配文本。其中TF-IDF是一种典型的稀疏检索方法。
- [17] object 5: 判别式检索器
- [19] 矩形 25: TF-IDF
### Notes
- 先给出IT-IDF
### Images
- ppt/media/image109.png
- ppt/media/image110.png
- ppt/media/image111.png
- ppt/media/image112.png
- ppt/media/image113.png

## Slide 48
### Shapes/Text
- [3] 文本框 3: 1. 词频 TF 计算表：
- [7] 文本框 14: 2. 逆文档频率 IDF 计算
- [8] 文本框 17: 3. TF-IDF 计算
- [10] 文本框 24: 句 1:  [“家人” “们”]句 2:  [“集美” “们”]句 3:  [“家人” “集美” “们”]
- [13] 文本框 27: 有相似性！
- [14] 文本框 28: 有相似性！
- [15] 矩形 1:  计算句子间相似性
- [17] 文本框 6: 句子的 / TF-IDF向量
- [18] 矩形 20: 一类经典的判别式检索器是稀疏检索器，其使用稀疏表示方法来匹配文本。其中TF-IDF是一种典型的稀疏检索方法。
- [19] object 5: 判别式检索器
### Tables
- [4] 表格 8
  -  | 句1 | 句2 | 句3
  - 家人 | 1/2 | 0 | 1/3
  - 集美 | 0 | 1/2 | 1/3
  - 们 | 1/2 | 1/2 | 1/3
- [5] 表格 10
  -  | IDF
  - 家人 | log(3/2)
  - 集美 | log(3/2)
  - 们 | log(3/3) = 0
- [6] 表格 11
  -  | 家人 | 集美 | 们
  - 句 1 | 1/2 × log(3/2) | 0 | 0
  - 句 2 | 0 | 1/2 × log(3/2) | 0
  - 句 3 | 1/3 × log(3/2) | 1/3 × log(3/2) | 0
### Images
- ppt/media/image114.png

## Slide 49
### Shapes/Text
- [4] 矩形 4: 双编码类检索器首先将查询和文档首先各自通过独立的编码器生成各自的向量表示，再对这两个向量之间的相似度进行计算，以评估它们的相关性。
- [6] 文本框 1: 双编码类检索器架构
- [9] 文本框 21: # u=Encoder(query) 
- [10] 文本框 22: # v=Encoder(doc) 
- [12] 文本框 24: # 例如使用Bert作为编码器
- [14] 文本框 31: 提取特征向量时缺乏交互
- [16] 文本框 8: 允许预先离线计算并存储所有文档的向量表示，匹配效率高
- [17] object 5: 判别式检索器
### Notes
- 后面再加一些cross=encoder
### Images
- ppt/media/image115.png
- ppt/media/image62.png

## Slide 50
### Shapes/Text
- [4] 矩形 4: 为了双编码器类检索器查询与文档在提取特征向量时缺乏交互问题， ColBERT以查询和文档间的Token级的相似度为度量，通过对比学习对双编码器进行微调。
- [8] 文本框 7: Query中qi 的embedding
- [9] 文本框 8: Doc 中dj  的embedding
- [10] 文本框 10: 对于集合 Eq​ 中的每一个嵌入 Eqi​，都会与文档嵌入集合 Ed​ 中的所有嵌入 Edj​  计算最大余弦相似度。
- [12] 文本框 9: Khattab and Omar. 2020. Colbert: Efficient and effective passage search via contextualized late interaction over bert. In SIGIR. 
- [13] object 5: 判别式检索器
### Notes
- 一句话总结里面体现出方法词级别的
### Images
- ppt/media/image116.png
- ppt/media/image117.png
- ppt/media/image113.png

## Slide 51
### Shapes/Text
- [5] 矩形 4: 交叉编码类检索器“端到端”的给出查询与文档的相似度。该类检索器将查询和文档结合后直接输入到模型中，最终模型输出一个介于0到1之间的数值，用以表示查询与文档之间的相似性。
- [6] 文本框 1: 交叉编码类检索器架构
- [9] 文本框 8: # 使用预训练模型生成向量表示
- [11] 文本框 15: 模型结构简单，能够实现查询和文档之间的深度交互；
- [12] 文本框 33: 计算量大，不适合在大规模的检索阶段使用，更适用于小规模的重排阶段。
- [13] object 5: 判别式检索器
### Notes
- 后面再加一些cross=encoder
### Images
- ppt/media/image118.png
- ppt/media/image62.png

## Slide 52
### Shapes/Text
- [3] object 5: 判别式检索效率增强
- [4] 矩形 4: 知识库海量文本的向量编码储存在向量数据库中，对其中编码进行逐一检索缓慢而低效，高效的向量索引方法可以来提高检索效率。
- [5] 文本框 3: 向量数据库通过优化相似度索引算法来提高检索效率，现有的向量索引方法可以分为：
- [6] 文本框 15: 基于量化的向量索引方法 / 基于哈希的向量索引方法 / 基于树的向量索引方法 / 基于图的向量索引方法
- [8] 矩形 2: 索引算法
- [10] 矩形 6: 向量数据库
### Tables
- [11] 表格 7
  - 向量数据库 | Langchain集成 | 语言
  - milvus | √ | Go/Python/C++
  - typesense | √ | C++
  - qdrant | √ | Rust
  - chroma | √ | python
  - weaviate | √ | Go
  - pinecone | √ | -
### Notes
- 改善索引，介绍索引，索引重要性

## Slide 53
### Shapes/Text
- [3] object 5: 生成式检索器
- [4] 矩形 4: 生成式检索器直接将知识库中的文档信息记忆在模型参数中。然后，在接收到查询请求时，能够直接生成相关文档的标识符（即 Doc ID），以完成检索。 
- [10] 文本框 18: 判别式检索器
- [11] 文本框 19: 生成式检索器
### Images
- ppt/media/image103.png

## Slide 54
### Shapes/Text
- [3] 矩形 4: 生成式检索器直接将知识库中的文档信息记忆在模型参数中。然后，在接收到查询请求时，能够直接生成相关文档的标识符（即 Doc ID），以完成检索。 
- [5] 文本框 6: 训练方式：训练包括索引任务与检索任务，两个任务以多任务的形式端到端直接优化。 /  /  / 索引任务：模型学习文档的内容与其对应的文档ID之间的映射关系； /  / 检索任务：模型学习为输入查询返回一个潜在相关的候选文档的排名列表。
- [6] 文本框 12: 生成式检索器
- [7] object 5: 生成式检索器
### Images
- ppt/media/image106.png

## Slide 55
### Shapes/Text
- [3] 矩形 4: 生成式检索器直接将知识库中的文档信息记忆在模型参数中。然后，在接收到查询请求时，能够直接生成相关文档的标识符（即 Doc ID），以完成检索。 
- [4] 文本框 16: 内存效率高：仅存储文档标识符和模型参数；
- [7] 文本框 1: 注: 稠密检索器为GTR-Base，生成式检索器为LTGR[1]，TopK=100，数据源自[1]。
- [8] 文本框 3: 生成速度快：仅需生成轻量的文档标识符。
- [10] 文本框 9: [1] Sun, Weiwei, et al. 2024. Learning to tokenize for generative retrieval. In NeurIPS.
- [11] object 5: 生成式检索器
### Images
- ppt/media/image62.png
- ppt/media/image119.png

## Slide 56
### Shapes/Text
- [3] object 5: 生成式检索效率增强
- [4] 矩形 4: 生成式检索效率的增强可从多个关键方面入手，包括提升文档标识符的构建效率、加速增量更新过程以及优化推理环节等。
- [6] 矩形 2: 提升Docid构建效率
- [7] 文本框 12: 根据任务特点选择合适采样方式，如约束波束搜索和约束贪婪搜索等，提高推理效率。
- [8] 文本框 22: 平衡docid的精度和效率，适当接受一定程度的近似解（如伪随机数或简化语义）。
- [9] 文本框 26: 采用分层的标识符生成策略，简单文档用基础规则，复杂文档用语义增强策略。
- [11] 矩形 28: 增量更新加速
- [13] 矩形 32: 推理优化
- [14] 文本框 43: 构建动态记忆模块，通过记忆与新文档相似的旧文档，优化新旧文档的关联学习，减少全局重新训练的需求。 
- [15] 文本框 48: 结合量化策略，减少计算开销，确保在性能和资源间的平衡。
### Notes
- 改善索引，介绍索引，索引重要性
### Images
- ppt/media/image120.png
- ppt/media/image121.png
- ppt/media/image122.png

## Slide 57
### Shapes/Text
- [3] 矩形 4: 在以下场景中，当传统的检索器性能不佳时，可以考虑使用图检索器。
- [4] 文本框 9: 需捕捉结构化关系
- [5] 文本框 11: 需解决信息冗余问题
- [6] 文本框 14: 需全面获取全局信息
- [7] 文本框 16: ……
- [8] object 5: 图检索器
- [9] 文本框 3: 图检索器能有效识别内容之间的显著结构化关系，而传统方法仅基于语义相似性，无法体现这些关键关系。
- [10] 文本框 6: 图检索器能保持信息的精简和关键性，避免因拼接文本片段导致的“lost in the middle”现象。
- [11] 文本框 8: 图检索器在全局层面理解文档，而非仅依赖部分文档内容，确保任务结果的完整性与准确性。
### Images
- ppt/media/image123.png
- ppt/media/image124.png
- ppt/media/image125.png

## Slide 58
### Shapes/Text
- [4] 矩形 4: 图检索器的知识库为图数据库，包括开放知识图谱和自建图两种，它们一般由<主体、谓词和客体>三元组构成。这样做不仅可以捕捉概念间的语义关系，还允许人类和机器可以共同对知识进行理解与推理。
- [5] object 5: 图检索器
- [7] 文本框 8: 向量数据库里的苹果
- [8] 文本框 9: 图数据库里的苹果
- [11] 文本框 25: 属性值
- [13] 文本框 31: 属性
- [14] 文本框 43: 实体
- [17] 文本框 6: 实体
- [19] 文本框 12: 关系
- [20] 文本框 13: 实体
### Images
- ppt/media/image126.png
- ppt/media/image127.png
- ppt/media/image128.png

## Slide 59
### Shapes/Text
- [4] 矩形 4: 基于图数据库的检索增强生成方法，能改善在推理复杂信息时的问答性能。其核心链路可以分成图索引构建、图检索和生成三阶段。
- [5] 文本框 13: # 2. 检索（子图召回）
- [6] 文本框 25: # 1. 图索引构建
- [7] object 5: 图检索器
- [10] 文本框 16: # 3. 生成
### Images
- ppt/media/image129.png

## Slide 60
### Shapes/Text
- [3] 矩形 4: 图检索效率增强可以从多个方面入手，包括索引构建优化，检索优化等。
- [4] object 5: 图检索效率增强
- [6] 矩形 8: 索引构建优化
- [8] 矩形 10: 检索优化
- [9] 文本框 22: 检索缓存优化
- [10] 文本框 26: 使用缓存技术将查询结果缓存起来，减少对数据库的访问次数。
- [11] 文本框 28: 检索算法优化
- [12] 文本框 30: 采用多阶段检索策略，如先利用大模型规划路径对大图进行剪枝，再从子图中提取满足条件的路径；
- [13] 文本框 33: ……
- [14] 文本框 37: 索引方法选择
- [15] 文本框 39: 使用混合检索，结合图索引和向量索引的优势，同时保留结构信息并实现快速向量搜索。
- [16] 文本框 42: ……
- [17] 文本框 1: 索引数据优化
- [18] 文本框 3: 层次化数据组织，为图数据库建立多级索引，根据任务需求选择粒度更细或更广的子图进行检索。

## Slide 61
### Shapes/Text
- [3] 矩形 4: 检索阶段为了保证检索速度通常会损失一定的性能，可能检索到质量较低的文档。重排的目的是对检索到的段落进行进一步的排序精选。重排可以分为基于交叉编码的方法和基于上下文学习的方法。
- [7] object 5: 检索结果重排
### Notes
- 标一下，不明显
### Images
- ppt/media/image130.png
- ppt/media/image9.svg

## Slide 62
### Shapes/Text
- [3] 矩形 4: 基于交叉编码的重排方法利用交叉编码器来评估文档与查询之间的语义相关性。
- [5] 文本框 5: 交叉编码类重排器架构
- [6] 文本框 33: cross-encoder/ms-marco-mini lm / cross-encoder/ms-marco-TinyBERT-L / cross-encoder/stsb-roberta-large
- [7] 文本框 2: 双编码器架构在提取查询和文档特征向量时为浅交互，而交叉编码类模型能实现查询和文档的深度交互，所以常用于重排阶段。
- [8] 文本框 7: 常见的交叉编码器
- [9] 文本框 13: Sentence-Transformer 系列
- [10] 文本框 18: BGE 系列
- [11] 文本框 20: BAAI/bge-reranker-large
- [12] 文本框 21: ……
- [15] object 5: 检索结果重排
### Images
- ppt/media/image118.png
- ppt/media/image131.png
- ppt/media/image132.png

## Slide 63
### Shapes/Text
- [3] 矩形 4: 基于上下文学习的方法是指通过设计精巧的 Prompt，使用大模型来执行重排任务。
- [4] 文本框 3: RankGPT 是基于上下文学习的重排方法中的代表性方法。其使用的 Prompt 如下。
- [6] 文本框 9: Sun W, et al. Is ChatGPT good at search? investigating large language models as re-ranking agents. arXiv preprint arXiv:2304.09542, 2023.
- [7] object 5: 检索结果重排
### Images
- ppt/media/image133.png

## Slide 64
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 64
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png

## Slide 65
### Shapes/Text
- [3] object 5: 生成增强
- [5] 矩形 9: 检索器得到相关信息后，需要将其传递给大语言模型以期增强模型的生成能力。如何优化生成增强过程，以得到更好的RAG性能？
### Notes
- 换一个原来ppt的图
### Images
- ppt/media/image45.png
- ppt/media/image54.gif

## Slide 66
### Shapes/Text
- [3] object 5: 生成增强
- [4] 矩形 1: 利用检索到的信息进行生成增强是一个复杂的过程，不同的方式会显著影响 RAG 的性能。可以从三个角度进行分析：何时增强、何处增强、多次增强。
- [5] 文本框 9: 观测长度有限
- [6] 矩形: 圆角 2: 何时增强
- [7] 文本框 5: 确定何时需要检索增强，以确保非必要不增强。
- [9] 文本框 68: 观测长度有限
- [10] 矩形: 圆角 2: 何处增强
- [12] 文本框 71: 确定在模型中的何处融入检索到的知识以最大化效用。
- [13] 文本框 73: 观测长度有限
- [14] 矩形: 圆角 2: 多次增强
- [16] 文本框 76: 确定是否需要多次检索，以解决复杂问题。
### Images
- ppt/media/image134.png
- ppt/media/image135.png
- ppt/media/image136.png

## Slide 67
### Shapes/Text
- [3] object 5: 何时增强
- [4] 矩形 1:  确定何时需要检索增强，以确保非必要不增强。
- [5] 文本框 9: 观测长度有限
- [7] 文本框 7: 非必要增强时进行增强， / 类似于画蛇添足
- [8] 文本框 10: 判断是否需要增强的核心在于判断大语言模型是否具有内部知识。 /  /  / 对于内部知识可以解决的问题，我们可以不对该问题进行增强。
### Images
- ppt/media/image137.jpeg

## Slide 68
### Shapes/Text
- [3] object 5: 何时增强
- [4] 文本框 9: 观测长度有限
- [5] 文本框 6: 不侵入模型内部参数。通过对大模型的训练数据和输出进行观测来判断大模型是否具备相应知识。类似于面试考察应聘者的知识。
- [6] 矩形: 圆角 4: 外部观测法
- [7] 文本框 12: 在模型参数可访问的情况下，观测模型内部的隐藏状态来更精确地评估其知识掌握情况。类似于对人体内部进行脑电波诊断。
- [8] 矩形: 圆角 6: 内部观测法
- [13] 矩形 17: 可以通过判断大语言模型是否具有相关内部知识来判断其是否需要增强。
### Images
- ppt/media/image138.png
- ppt/media/image139.png
- ppt/media/image140.png

## Slide 69
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 通过Prompt直接询问对是否具备内部知识进行预测。
- [6] 矩形 5: Prompt直接询问
- [7] 文本框 2: 设计Prompt直接询问，根据模型的回答情况进行判断； /  /    局限性：模型过度自信。 /  /  /  /  / 
### Notes
- 过度自信，问啥啥会，换成表情包或例子
### Images
- ppt/media/image141.png
- ppt/media/image142.png

## Slide 70
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 训练数据是大模型的知识来源，可以通过观察训练数据预测模型的内部知识水平。
- [6] 矩形 5: 观察训练数据
- [7] 文本框 2: 知识在训练数据中的出现频率与模型对该知识的记忆程度是正相关的。 /  / 根据知识在训练数据中的出现频率估计模型的学习情况； /  / 局限性：部分模型无法获取训练数据。
- [9] 文本框 10: 类似于面试官通过履历来判断 / 面试者的知识水平
### Images
- ppt/media/image143.png

## Slide 71
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 无法观察训练数据时，可以通过构造伪训练数据来拟合训练数据的相关情况。
- [6] 矩形 5: 构造伪训练数据
- [13] 文本框 14: 出现在训练数据中的频率未知
- [14] 文本框 15:      ？                   ？                  ？
- [15] 文本框 16:      ？                  ？                  ？
- [17] 文本框 10: 由食物的网络流行度生成的词云
### Images
- ppt/media/image144.png
- ppt/media/image145.png
- ppt/media/image146.png
- ppt/media/image147.png
- ppt/media/image148.png
- ppt/media/image149.png
- ppt/media/image150.png

## Slide 72
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 通过构造伪训练数据统计量对是否具备内部知识进行预测。
- [6] 矩形 5: 构造伪训练数据统计量
- [7] 文本框 2: 流行度：流行度是指实体或知识在特定环境中被广泛关注或使用的频率。 /  / 由于模型对低频的知识掌握不足，而对更“流行”（高频）的知识掌握更好，因此流行度可以作为伪训练数据统计量。
- [9] 文本框 10: 由食物的流行度生成的词云
### Images
- ppt/media/image150.png

## Slide 73
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 通过构造伪训练数据统计量对是否具备内部知识进行预测。
- [6] 文本框 2: 通过设定流行度阈值来判别模型是否具备相应的内部知识； /  / 流行度阈值可以设定为维基百科/谷歌搜索的某个访问量值或热度值。 / 
- [7] 文本框 8: 通过流行度阈值来判断该模型是否具备相应的内部知识
- [9] 矩形 3: 构造伪训练数据统计量
### Images
- ppt/media/image151.svg

## Slide 74
### Shapes/Text
- [3] object 5: 外部观测法
- [4] 矩形 1: 通过设定流行度阈值来判别模型是否具备相应的内部知识。
- [6] 矩形 5: 构造伪训练数据统计量示例
- [7] 文本框 3: “大熊猫”在维基百科上的热度（流行知识）
- [8] 文本框 6: “叶口蝠”在维基百科上的热度（非流行知识）
- [9] 文本框 10: 可以设定在维基百科中，过去30天页面访问量超过100的知识为流行知识
### Images
- ppt/media/image152.png
- ppt/media/image153.png

## Slide 75
### Shapes/Text
- [3] object 5: 内部观测法
- [4] 矩形 1: 通过分析大模型在生成文本时的内部状态变化，来评估其内部知识水平。
- [6] 矩形 5: 如何观测
- [7] 文本框 3: 在处理包含或不包含内部知识的不同问题时，模型的中间层（注意力层、MLP层等）会展现出不同的动态变化。 /  / 基于这一特性，我们可以训练分类器进行判别，这种方法被称为探针。
- [9] 文本框 6: 类似于通过心率、血压、呼吸频率进行测谎的过程
### Images
- ppt/media/image154.png

## Slide 76
### Shapes/Text
- [3] object 5: 内部观测法
- [4] 矩形 1: 对于输入问题，利用训练好的探针，即线性分类器，根据问题所对应的内部表示预测该问题是属于模型已知还是未知。
- [6] 矩形 5: 如何观测
- [8] 文本框 9: Yuxin Liang et al. 2024. Learning to trust your feelings: Leveraging self-awareness in llms for hallucination mitigation. In: arXiv preprint arXiv:2401.15449.
### Images
- ppt/media/image155.png

## Slide 77
### Shapes/Text
- [3] object 5: 何处增强
- [4] 矩形 1: 确定在模型中的何处融入检索到的知识以最大化效用。
- [5] 文本框 9: 观测长度有限
- [7] 文本框 2: 泛化性
- [8] 文本框 3:  / 在确定大语言模型需要外部知识后，我们需要考虑在何处利用检索到的外部知识，即何处增强的问题。 /  / 得益于大语言模型的上下文学习能力、注意力机制的可扩展性以及自回归生成能力，其输入端、中间层和输出端都可以进行知识融合操作。 / 
- [9] 文本框 15: 类似于一个汉堡，选择在哪一层加入沙拉酱
### Images
- ppt/media/image156.png

## Slide 78
### Shapes/Text
- [3] object 5: 何处增强
- [4] 文本框 9: 观测长度有限
- [5] 矩形 3: 输入端：将问题和检索到的外部知识拼接在Prompt中，然后输入给大模型； / 中间层：采用交叉注意力将外部知识直接编码到模型的隐藏状态中； / 输出端：利用外部知识对生成的文本进行后矫正。
### Notes
- 加两个图片
### Images
- ppt/media/image157.png

## Slide 79
### Shapes/Text
- [3] object 5: 在输入端增强
- [4] 矩形 3: 在输入端增强的方法直接将检索到的外部知识文本与用户查询拼接到 Prompt / 中，然后输入给大语言模型，是当前主流的增强方法。
### Notes
- 没有外部知识也画一张图片
### Images
- ppt/media/image158.png
- ppt/media/image159.png
- ppt/media/image160.png
- ppt/media/image161.png

## Slide 80
### Shapes/Text
- [3] object 5: 在中间层增强
- [4] 矩形 3: 在中间层增强的方法先将检索到的外部知识转换为向量表示，然后将这些向量插入通过交叉注意力融合到模型的隐藏状态中。
- [5] 文本框 10: 在中间层增强的代表性方法为RETRO，其在语言模型的中间层通过交叉编码将检索信息动态融合到模型的隐层状态中，从而增强模型的语义理解与生成能力。
- [7] 文本框 9: Sebastian Borgeaud et al. 2022. Improving language models by retrieving from trillions of tokens. In ICML.
### Images
- ppt/media/image65.png

## Slide 81
### Shapes/Text
- [3] object 5: 在输出端增强
- [4] 矩形 3: 在输出端增强的方法利用检索到的外部知识对大语言模型生成的文本进行校准，是一种后处理的方法。
- [5] 文本框 15: 在输出端增强的代表性方法为RETRO框架，其在输出端通过比对生成内容与检索信息的一致性，动态调整生成结果并矫正潜在错误，从而提高生成文本的准确性和可靠性。
- [6] 文本框 9: Sebastian Borgeaud et al. 2022. Improving language models by retrieving from trillions of tokens. In ICML.
### Images
- ppt/media/image162.png

## Slide 82
### Shapes/Text
- [3] 文本框 9: 观测长度有限
- [4] object 5: 优点和缺点
- [8] 文本框 6: 直观且易于实现。模型可以直接从输入的上下文中提取到所需信息，无需复杂的处理或转换。
- [9] 文本框 1: 更深入地影响模型的内部表示，减少对模型输入长度的依赖。
- [10] 文本框 2: 可以确保生成的文本与外部知识保持一致，提高答案的准确性和可靠性。
- [11] 文本框 5: 当检索到的文本过长时，会增加模型推理计算成本、增加其计算负担。 / 
- [12] 文本框 7: 需要对模型的结构进行复杂的设计和调整，无法应用于黑盒模型。 / 
- [13] 文本框 8: 效果在很大程度上依赖于检索到的外部知识的质量和相关性。校准结果容易受到较大影响。 / 
### Tables
- [5] 表格 4
  - 架构分类 | 优点 | 缺点
  - 在输入端增强 |  | 
  - 在中间层增强 |  | 
  - 在输出端增强 |  | 
### Notes
- 统一下样式
### Images
- ppt/media/image61.png
- ppt/media/image62.png

## Slide 83
### Shapes/Text
- [3] object 5: 多次增强
- [4] 矩形 1:  对复杂查询与模糊查询进行多次迭代增强，以提升RAG在困难问题上的效果。
- [5] 文本框 9: 观测长度有限
- [7] 文本框 2: 泛化性
- [8] 文本框 6:     没有什么是一次增强解决不了的， / 如果一次不行，那就两次 / 如果两次不行，那就三次 / ……
- [10] 文本框 14: 图源：哔哩哔哩UP主@朝阳冬泳怪鸽
- [11] 文本框 3: 复杂问题往往涉及多个知识点，需要多跳（multi-hop）的理解；而模糊问题往往指代范围不明，难以一次就理解问题的含义。 /  / 对于复杂问题和模糊问题，我们难以通过一次检索增强就确保生成正确，多次迭代检索增强在所难免。
### Images
- ppt/media/image163.png

## Slide 84
### Shapes/Text
- [3] 文本框 9: 观测长度有限
- [5] 矩形 1: 对于复杂问题和模糊问题，我们难以通过一次检索增强就确保生成正确，多次迭代检索增强在所难免。
- [6] object 5: 多次增强
### Notes
- 结论放到上面
### Images
- ppt/media/image164.svg

## Slide 85
### Shapes/Text
- [3] object 5: 分解式增强
- [4] 文本框 1: 世界上睡眠时间最长 / 的动物爱吃什么？
- [12] 文本框 13: 世界上睡眠时间最长 / 的动物是什么？
- [15] 文本框 17: 考拉
- [19] 文本框 22: 考拉爱吃什么？
- [20] 文本框 24: 桉树叶
- [21] 矩形 26: 在复杂问题的检索增强中，通常无法仅通过一次检索增强就得到满意的答案。可以采用分解式增强，将复杂问题化为多个子问题，在子问题间进行迭代检索增强。
### Notes
- 加两个图片
### Images
- ppt/media/image165.png
- ppt/media/image166.png
- ppt/media/image167.png
- ppt/media/image168.png
- ppt/media/image169.png

## Slide 86
### Shapes/Text
- [3] object 5: 细化式增强
- [4] 矩形 3: 在模糊问题中，问题主体通常指代不明，容易引发歧义。可以通过细化式检索来引导大语言模型探索模糊问题的多种细化路径。
- [6] 文本框 10: 国宝动物爱吃什么？
- [8] 文本框 13: 中国的国宝动物
- [9] 文本框 14: 澳大利亚的国宝动物
- [23] 文本框 9: Omar Khattab et al. 2022. Demonstrate-search-predict: Composing retrieval and language models for knowledge-intensive nlp. In: arXiv preprint arXiv:  / 2212.14024.
- [24] 文本框 25: 竹子
- [25] 文本框 30: 桉树叶
- [26] 文本框 31: 灌木
### Notes
- 加两个图片
### Images
- ppt/media/image170.png
- ppt/media/image166.png
- ppt/media/image171.jpeg
- ppt/media/image172.png
- ppt/media/image167.png
- ppt/media/image173.png
- ppt/media/image168.png
- ppt/media/image174.png

## Slide 87
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 87
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png

## Slide 88
### Shapes/Text
- [3] object 5: 降本增效
- [5] 矩形 9: 检索的外部知识通常包含大量文本，如何降本增效，以提升处理文本效率？
### Notes
- 换一个原来ppt的图
### Images
- ppt/media/image45.png
- ppt/media/image54.gif

## Slide 89
### Shapes/Text
- [3] 文本框 9: 观测长度有限
- [4] object 5: 降本增效
- [6] 矩形 4: 检索出的外部知识通常包含大量原始文本。如果不加处理，会增加大语言模型的推理计算成本。可从去除冗余文本与复用计算结果两个角度进行解决。
### Notes
- 加两个图片
### Images
- ppt/media/image175.svg

## Slide 90
### Shapes/Text
- [3] 文本框 9: 观测长度有限
- [4] object 5: 去除冗余文本
- [7] 矩形 5: 去除冗余文本的方法通过对检索出的原始文本的词句进行过滤，从中选择出部分有益于增强生成的部分。
### Notes
- 加两个图片
### Images
- ppt/media/image176.GIF
- ppt/media/image177.GIF
- ppt/media/image178.png

## Slide 91
### Shapes/Text
- [3] object 5: 去除冗余文本
- [4] 矩形 5: 去除冗余文本的方法主要分为三类：Token 级别的方法，全文本级别的方法以及子文本级别的方法。
- [6] 矩形 12: Token级别的方法
- [7] 文本框 15: 其中，“您”、“需要”、“上”、“的”、“然后”、“会”等 Token困惑度较低，可以去除。
- [9] 文本框 9: Huiqiang Jiang et al. 2023. Longllmlingua: Accelerating and enhancing llms in long context scenarios via prompt compression. In: arXiv preprint arXiv: 2310.06839.
### Notes
- 加两个图片
### Images
- ppt/media/image179.svg

## Slide 92
### Shapes/Text
- [3] object 5: 去除冗余文本
- [5] 矩形 12: 全文本级别的方法
- [7] 矩形 15: 全文本级别的方法直接从整个文档中抽取出重要信息，以去除掉冗余信息。
- [8] 文本框 9: Haoyan Yang et al. 2023. Prca: Fitting black-box large language models for retrieval question answering via pluggable reward-driven contextual adapter. In EMNLP.
### Notes
- 加两个图片
### Images
- ppt/media/image180.svg

## Slide 93
### Shapes/Text
- [3] object 5: 去除冗余文本
- [4] 矩形 11: Yuren Mao et al. “FIT-RAG: Black-Box RAG with Factual Information and Token / Reduction”. In: ACM Transactions on Information Systems (2024).
- [5] 矩形 12: 子文本级别的方法
- [7] 矩形 14: 子文本级别的方法通过对文档分割后的子文本打分，删除不必要的子文本。
### Notes
- 加两个图片
### Images
- ppt/media/image181.svg

## Slide 94
### Shapes/Text
- [3] object 5: 去除冗余文本
- [4] 矩形 11: Yuren Mao et al. “FIT-RAG: Black-Box RAG with Factual Information and Token / Reduction”. In: ACM Transactions on Information Systems (2024).
- [5] 矩形 14: 子文本级别的代表性方法有FIT-RAG。它是一款高效低资源的通用检索增强生成框架，集检索文档打分精排，内部知识检测，检索文档压缩和输入提升设计于一体。
- [7] 矩形 3: 结构框图
- [8] 文本框 9: Yuren Mao et al. 2024. FIT-RAG: Black-Box RAG with Factual Information and Token Reduction. In: ACM Transactions on Information Systems.
### Notes
- 加两个图片
### Images
- ppt/media/image182.png

## Slide 95
### Shapes/Text
- [3] object 5: 去除冗余文本
- [4] 矩形 11: Yuren Mao et al. “FIT-RAG: Black-Box RAG with Factual Information and Token / Reduction”. In: ACM Transactions on Information Systems (2024).
- [5] 文本框 9: Yuren Mao et al. 2024. FIT-RAG: Black-Box RAG with Factual Information and Token Reduction. In: ACM Transactions on Information Systems.
- [6] 矩形 1: 子文本级别压缩
- [7] 矩形 9: FIT-RAG的子文档压缩方法通过将文档划分为子文档，并利用预先构建的打分器对子文本进行打分，筛选出既包含事实信息又符合大模型偏好的少量子文本组合。
### Notes
- 加两个图片
### Images
- ppt/media/image183.png

## Slide 96
### Shapes/Text
- [3] object 5: 去除冗余文本
- [5] 文本框 4: 准确率均优于所有对比方法，并有效减少了Token数量。
- [8] 矩形 2: 实验结果
- [9] 矩形 10: FIT-RAG 有效地筛选出符合大模型偏好的高质量文档，极大提升了大语言模型的回答准确率，同时能够平均压缩约50%的输入 Token，极大提升了输入有效性，并节约了计算资源。
### Notes
- 加两个图片
### Images
- ppt/media/image184.png

## Slide 97
### Shapes/Text
- [4] 文本框 9: 观测长度有限
- [5] object 5: 复用计算结果
- [6] 矩形 5: 除了对冗余信息进行筛除，还可以对计算必需的中间结果进行复用，以优化 RAG 效率。
- [8] 对话气泡: 矩形 2: 我想吃土豆炖牛肉。
- [13] 对话气泡: 矩形 2: 我想吃番茄炖牛肉。
- [14] 文本框 23: 中间结果 / （炖好的牛肉）
- [15] 文本框 24: 最终结果 / （土豆炖牛肉）
- [23] 文本框 38: 最终结果 / （番茄炖牛肉）
- [24] 文本框 39: 复用中间结果
### Notes
- 改成两个人，将检索到的知识算成中间结果
### Images
- ppt/media/image166.png
- ppt/media/image185.png
- ppt/media/image186.png
- ppt/media/image187.png
- ppt/media/image188.png
- ppt/media/image189.png

## Slide 98
### Shapes/Text
- [3] object 5: 复用计算结果
- [4] 矩形 5: 为避免每次生成新Token时重复计算之前的Key和Value，可以将它们缓存起来（即KV-cache），在需要时直接调用缓存结果，从而减少计算。
### Notes
- 改成考拉，存的是文本token（向量）
### Images
- ppt/media/image190.png

## Slide 99
### Shapes/Text
- [3] object 5: 复用计算结果
- [4] 矩形 5: RAGCache是一种经典方法，它设计了一种 RAG系统专用的多级动态缓存机制，由三个核心部分组成：KV 张量缓存库、缓存检索器与 RAG 控制器。
- [6] 文本框 9: Chao Jin et al. 2024. RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation. In: arXiv preprint arXiv:2404.12457
### Notes
- 加两个图片
### Images
- ppt/media/image191.png

## Slide 100
### Shapes/Text
- [3] 文本框 9: 观测长度有限
- [4] object 5: 降本增效
- [7] 文本框 8: 可以结合上述去除冗余文本（ Prompt 压缩）与复用计算结果（ KV-cache 机制），这样RAG 框架在保持高性能的同时，还可以显著提升效率！
### Notes
- 加两个图片
### Images
- ppt/media/image192.png

## Slide 101
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 101
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png

## Slide 102
### Shapes/Text
- [3] object 5: RAG应用之多模态
- [4] 矩形 7: 在诸多垂直领域中，除文本数据之外，对多模态数据的处理需求也日益凸显。
- [6] 文本框 10: 多模态通过结合多种感知通道，可同时理解和处理不同形态的信息，例如文本、图像，从而提供更完整的信息输入和更丰富的交互体验。 / 为了适配广泛的应用场景，RAG 系统需要具备融合与处理不同模态数据的能力。
- [8] 文本框 28: 图源： https://jina.ai/news/paradigm-shift-towards-multimodal-ai/; https://medium.com/@baicenxiao/introduction-to-the-large-multi-modal-models-llms-part-1-07de7e9caf40
### Images
- ppt/media/image193.jpeg
- ppt/media/image194.png

## Slide 103
### Shapes/Text
- [3] object 5: RAG应用之多模态
- [4] 矩形 7: 在诸多垂直领域中，除文本数据之外，对多模态数据的处理需求也日益凸显。
- [5] 文本框 10: 例如，在医疗领域中，多模态数据十分普遍，包括 X 光片、MRI、CT 扫描等影像资料，病历、生理监测数据等文本资料。这些数据不仅来源广泛，而且彼此之间存在着复杂的相互联系。
### Images
- ppt/media/image195.png
- ppt/media/image196.jpeg
- ppt/media/image197.png
- ppt/media/image198.png
- ppt/media/image199.png

## Slide 104
### Shapes/Text
- [3] object 5: RAG应用之多模态
- [5] 矩形 8: 在医疗领域多模态数据十分普遍，RAG可以帮助融合不同模态的数据。
- [6] 文本框 9: Stanislav Morozov, et al. 2018. Non-metric similarity graphs for maximum inner product search. In NeurIPS.
### Images
- ppt/media/image200.png

## Slide 105
### Shapes/Text
- [3] object 5: RAG应用之Agent
- [4] 矩形 7: 在 Agent 系统运行过程中，需要检索并整合多样化的信息资源，以更精确地满足用户的需求， RAG 技术在其中扮演着重要角色。 
- [5] 文本框 12: Agent 组成： /  / 配置模块：设定 Agent 基本信息以定义角色。 / 记忆模块：存储知识与历史信息，支持多种记忆操作。RAG 辅助记忆检索与更新。 / 计划模块：进行任务分解与规划，并依反馈调整。RAG 利用信息辅助规划任务。 / 行动模块：转化 Agent 计划为行动，如工具调用等。RAG 检索信息辅助决策与行动执行。
- [7] 文本框 25: 图源： https://otter.ai/blog/what-are-ai-agents-a-guide-to-types-benefits-and-examples
### Images
- ppt/media/image201.jpeg

## Slide 106
### Shapes/Text
- [3] object 5: RAG应用之Agent
- [5] 文本框 18: 当面对用户关于想去抱考拉的询问时，Agent 经过一系列的规划与行动，给出了合适的出行建议。
- [7] 文本框 10: 图源： http://www.1989c.com/youxigonglue/107165.html
- [8] 矩形 11: 在 Agent 系统运行过程中，需要检索并整合多样化的信息资源，以更精确地满足用户的需求， RAG 技术在其中扮演着重要角色。 
### Images
- ppt/media/image202.png
- ppt/media/image203.jpeg

## Slide 107
### Shapes/Text
- [3] object 5: RAG企业落地
- [4] 矩形 7: 在企业落地中，RAG 技术对下一代AI产品开发至关重要。
- [6] 文本框 12: 阿里云推出企业级大模型RAG解决方案
- [8] 文本框 16: 百度智能云：千帆大模型平台升级十大能力，企业级RAG全面升级
- [10] 文本框 19: 95% 向量资源节省，火山引擎云搜索RAG 技术体系演进
- [12] 文本框 22: 腾讯云发布RAG解决方案，支持企业多种方式落地
- [13] 文本框 24: 华为云发布KooSearch的RAG解决方案
- [16] 文本框 28: 谷歌推出 DataGemma，结合检索增强生成和检索交错生成技术
### Images
- ppt/media/image204.png
- ppt/media/image205.png
- ppt/media/image206.png
- ppt/media/image207.png
- ppt/media/image208.png
- ppt/media/image209.jpeg

## Slide 108
### Shapes/Text
- [3] object 5: RAG企业落地
- [4] 矩形 7: 在企业落地中，企业 AI 产品开发中存在多个痛点。
- [5] 文本框 9: 图源：https://retool.com/reports/state-of-ai-2023
- [6] 文本框 10: 根据受访者关于开发 AI 产品痛点的统计结果，准确性、数据安全性以及幻觉是目前最大的三个痛点问题。而针对这些问题，RAG 是一种可行的解决技术手段。
- [8] 文本框 14: 2023 年 Retool 一项研究调查了各行各业的 1,500 多名技术人员，包括软件工程师、工程师和商业领袖、高管、产品人员、设计师等，以了解在企业实际中是如何使用 AI 和构建 AI 的。
- [9] 文本框 11: 关于开发 AI 产品痛点的统计
### Images
- ppt/media/image210.png

## Slide 109
### Shapes/Text
- [4] object 5: RAG企业落地
- [5] 矩形 7: RAG 可协助开发人员攻克构建 AI 应用时常面临的多项痛点问题与挑战
- [6] 文本框 10: 信息变化迅速，系统响应过时问题 / RAG解决方案：将语言模型和知识库分开，知识库可以实时更新，并始终从最新信息中提取。
- [7] 文本框 11: 保护隐私和数据问题 / RAG解决方案：可以创建仅访问批准的数据集并将敏感信息检索限制在特定本地设备的检索系统。
- [8] 文本框 12: 数据类型多样问题 / RAG解决方案：RAG 可扩展到传统文本之外，检索多种类型数据，例如图像、音频等。
- [9] 文本框 14: 知识集成困难问题 / RAG解决方案：RAG 模块化与微服务架构配合良好，可设单独信息检索微服务。
- [10] 文本框 15: 处理大量数据问题 / RAG解决方案：高级索引技术和向量数据库优化大型数据集搜索，促进快速准确的信息检索。
- [11] 文本框 16: 扩展时保持个性化问题 / RAG解决方案：开发人员可以创建针对用户偏好、历史和上下文量身定制的检索系统，并生成量身定制的响应。
### Images
- ppt/media/image211.png

## Slide 110
### Shapes/Text
- [3] object 5: RAG企业落地
- [4] 矩形 7: 在企业对内的AI应用场景中，以RAG技术为核心的应用场景占据大比例。
- [5] 文本框 9: 图源：https://retool.com/reports/state-of-ai-2023
- [9] 文本框 16: 36.2%
- [10] 文本框 17: 28.9%
- [11] 文本框 18: 从企业对内场景而言，知识管理以知识库问答（36.2%）和支持聊天机器人（28.9%）的形式在企业应用中极为普遍，而这些应用均以 RAG 技术为核心。
- [13] 文本框 21: 高效工作中
- [14] 文本框 14: 关于企业内部 AI 的使用场景统计
### Images
- ppt/media/image212.png
- ppt/media/image213.jpeg

## Slide 111
### Shapes/Text
- [4] object 5: RAG企业落地
- [5] 矩形 7: 在企业面向客户的AI应用场景中，以RAG技术为核心的应用场景同样占比很大。
- [6] 文本框 9: 图源：https://retool.com/reports/state-of-ai-2023
- [7] 文本框 10: 从企业面向客户的场景来看，其结果与企业内部场景类似，以 RAG 技术为核心的场景，即客户支持聊天机器人（占比 26.5%）和知识库问答（占比 26%）场景，二者共计占据了半数份额。
- [10] 文本框 16: 26.5%
- [11] 文本框 17: 26.0%
- [13] 文本框 13: 关于企业内部 AI 的使用场景统计
### Images
- ppt/media/image214.png
- ppt/media/image215.png

## Slide 112
### Shapes/Text
- [3] 矩形 7: 在AI应用的未来发展中，RAG仍将作为核心技术引领AI产品的进步。
- [4] 文本框 9: 图源：https://blog.stackademic.com/building-a-robust-rag-application-on-the-ai-stack-of-the-future-3bc42f84bbe8
- [5] object 5: RAG企业落地
- [7] 文本框 10: RAG 技术在未来的 AI 产品中必不可少，它在AI 技术栈的各个层次均具有重要意义，有助于提升知识获取效率、增强智能交互体验、推动多领域应用拓展等。
### Images
- ppt/media/image216.jpeg

## Slide 113
### Shapes/Text
- [3] 矩形 7: 在AI应用的未来发展中，RAG仍将作为核心技术引领AI产品的进步。
- [4] 文本框 9: 图源：https://retool.com/reports/state-of-ai-2023
- [6] 文本框 19: Let’s Embrace the Future with RAG !
- [7] object 5: RAG企业落地
### Notes
- 无论是看涨、看跌还是随波逐流，各行各业和角色的技术人员都在认真思考 AI 技术的可能性和影响，以及它们将如何塑造未来的许多方面。在这一进程中，RAG 有望成为未来人工智能领域的核心技术之一，发挥至关重要的作用。
### Images
- ppt/media/image217.png

## Slide 114
### Shapes/Text
- [1] TextBox 83: 01 RAG架构
- [3] 灯片编号占位符 1: 114
- [5] TextBox 83: 02 知识检索
- [6] TextBox 81: 03 生成增强
- [7] TextBox 81: 04 降本增效
- [8] TextBox 81: 05 应用落地 
### Images
- ppt/media/image1.png
