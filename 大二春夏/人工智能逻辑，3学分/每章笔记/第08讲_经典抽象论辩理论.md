# 第8讲 经典抽象论辩理论

---

## 概述

在人工智能和认知科学中，**论辩 (Argumentation)** 是一种重要的推理模式。与经典逻辑基于演绎证明的推理方式不同，论辩推理模拟了人类在日常生活中进行辩论、说服和决策的认知过程：不同的论证 (Arguments) ==相互支持或攻击，最终通过评估各个论证的可接受性==来得出结论。

本章介绍**经典抽象论辩理论 (Classical Abstract Argumentation Theory)**，该理论由 **Phan Minh Dung** 于1995年在其奠基性论文《On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games》中系统建立。Dung 的抽象论辩框架已经成为人工智能中论辩推理的标准形式体系。

**核心思想**：抽象论辩理论采用一种**两级方法 (Two-level Approach)** 来处理论辩推理：

1. **具体层 (Concrete Level / Structured Argumentation)**：关注如何从知识库中构造论证，包括论证的内部结构（前提、推理规则、结论）以及论证之间的各种关系（攻击、支持等）。
2. **抽象层 (Abstract Level / Abstract Argumentation)**：忽略论证的内部结构，将论证视为原子实体，只关注论证之间的攻击关系。通过定义各种**论辩语义 (Argumentation Semantics)** 来评估哪些论证是可以接受的。

举例来说，两位学生就人性本质展开辩论：一方主张"性善论"（人之初，性本善），另一方主张"性恶论"（人之初，性本恶）。双方各自提出论证并互相攻击。在抽象层，我们只需要知道存在一组论证和它们之间的攻击关系，而不关心每个论证具体使用了什么前提和推理规则。论辩语义的任务是：给定这样一组论证及其攻击关系，判定哪些论证是可以接受的（被辩护的）、哪些应当被拒绝、哪些处于未决状态。

**抽象论辩理论的应用**：该理论在法律推理、医疗决策、多主体系统、非单调推理、逻辑程序设计、自然语言处理（如虚假信息检测、事实核查）等领域有广泛应用。

---

## 8.1 抽象论辩框架

### 8.1.1 基本定义

抽象论辩框架是整个理论的基石。它以一种极其简洁的方式刻画了论证之间的冲突关系。

**定义8.1**（抽象论辩框架，Abstract Argumentation Framework）：
一个**抽象论辩框架 (AF)** 是一个二元组 $\text{AF} = \langle AR, \text{attacks} \rangle$，其中：

- $AR$ 是一个有限集合，其元素称为**论证 (Arguments)**；
- $\text{attacks} \subseteq AR \times AR$ 是一个二元关系，称为**攻击关系 (Attack Relation)**。

**记号说明**：

- 若 $(\alpha, \beta) \in \text{attacks}$，记作 $\alpha \to \beta$，读作"论证 $\alpha$ 攻击论证 $\beta$"。
- 对于一个论证集合 $S \subseteq AR$ 和一个论证 $\beta$，记 $S \to \beta$ 当且仅当 $\exists \alpha \in S$ 使得 $\alpha \to \beta$，表示"集合 $S$ 中的某个论证攻击 $\beta$"。
- 类似地，记 $\alpha \to S$ 当且仅当 $\exists \beta \in S$ 使得 $\alpha \to \beta$。
- ==对于一个论证集合 $S$，记 $S^+ = \{\beta \in AR \mid S \to \beta\}$，即被 $S$ 攻击的所有论证的集合。==

**图论视角**：一个抽象论辩框架可以被视为一个**有向图 (Directed Graph)**，称为**论辩图 (Argumentation Graph)**。其中节点表示论证，有向边表示攻击关系。这一图论视角为理解论辩框架的结构性质（如环、强连通分量等）提供了直观的工具。

### 8.1.2 实例分析

**例8.1**（国家发展道路的论辩）：
考虑关于国家发展道路选择的论辩，涉及以下三个论证：

- $\alpha$："坚持和平发展之路，通过互利共赢实现国家繁荣"
- $\beta$："推行单边主义，以自身利益优先为原则处理国际关系"
- $\gamma$："构建人类命运共同体，推动全球治理体系变革"

论证之间的攻击关系为：$\alpha \to \beta$（和平发展反对单边主义），$\gamma \to \beta$（人类命运共同体理念反对单边主义），$\beta \to \alpha$（单边主义否定和平发展的可行性），$\beta \to \gamma$（单边主义否定全球合作的必要性）。

由此构成的论辩框架 $\text{AF}_1 = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\gamma, \beta), (\beta, \alpha), (\beta, \gamma)\} \rangle$。

在 $\text{AF}_1$ 中，$\alpha$ 和 $\gamma$ 共同攻击 $\beta$，同时又各自受到 $\beta$ 的攻击。直观上，由于 $\beta$ 受到 $\alpha$ 和 $\gamma$ 的联合攻击而缺乏辩护，而 $\alpha$ 和 $\gamma$ 虽然受到 $\beta$ 的攻击，但 $\beta$ 本身不被接受，因此 $\alpha$ 和 $\gamma$ 应该被接受。

**例8.2**（先秦诸子思想的论辩）：
考虑儒、墨、道、法四家思想的论辩，涉及四个论证：

- $\alpha$："儒家主张以仁义礼智信治国"（儒家）
- $\beta$："墨家主张兼爱非攻，反对儒家的等级礼制"（墨家）
- $\gamma$："道家主张无为而治，认为儒墨之争无意义"（道家）
- $\delta$："法家主张以法治国，反对儒家的德治和墨家的兼爱"（法家）

攻击关系为：$\beta \to \alpha$（墨家批判儒家），$\gamma \to \alpha$ 且 $\gamma \to \beta$（道家超越儒墨之争），$\delta \to \alpha$、$\delta \to \beta$、$\delta \to \gamma$（法家以实效性否定三家），同时 $\alpha \to \beta$（儒家也批判墨家）。

由此构成的论辩框架 $\text{AF}_2 = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\beta, \alpha), (\gamma, \alpha), (\gamma, \beta), (\delta, \alpha), (\delta, \beta), (\delta, \gamma), (\alpha, \beta)\} \rangle$。

**例8.3**（法律推理案例）：
在一起刑事案件的法庭辩论中，控辩双方提出以下论证：

- $\alpha$："被告在犯罪现场被目击"（控方论证）
- $\beta$："被告有不在场证明，案发时在另一城市开会"（辩方论证）

攻击关系为 $\beta \to \alpha$（不在场证明攻击"在犯罪现场"的论证）。

构成的论辩框架 $\text{AF}_3 = \langle \{\alpha, \beta\}, \{(\beta, \alpha)\} \rangle$。==直观上，由于 $\beta$ 攻击 $\alpha$ 且 $\beta$ 自身没有受到任何攻击，因此 $\beta$ 应被接受而 $\alpha$ 应被拒绝。==

---

## 8.2 论证的可接受性

### 8.2.1 直观概念

在给定一个抽象论辩框架后，核心问题是：**哪些论证是可以接受的？哪些应该被拒绝？** 抽象论辩理论通过==定义各种**论辩语义 (Argumentation Semantics)**== 来回答这一问题。

**论证可接受性的三条基本原则**：

1. **无攻击者原则**：如果一个论证==没有受到任何攻击==（也不自攻击），那么它应该是可接受的。
2. **攻击传递原则**：如果一个已被接受的论证攻击另一个论证，那么==被攻击的论证应当被拒绝==。
3. **复原原则 (Reinstatement)**：如果一个论证的==所有攻击者都已被拒绝==，那么该论证应当被重新接受（即被"复原"）。

**例8.4**（可接受论证）：
在论辩框架 $\text{AF}_4$ 中，只有一个论证 $\alpha$，无攻击关系。根据原则1，$\alpha$ 是可接受的。

**例8.5**（被拒绝论证和复原）：
在论辩框架 $\text{AF}_5 = \langle \{\alpha, \beta, \gamma\}, \{(\beta, \alpha), (\gamma, \beta)\} \rangle$ 中：

- $\gamma$ 没有受到攻击，根据原则1，$\gamma$ 可接受；
- $\gamma$ 攻击 $\beta$，根据原则2，$\beta$ 被拒绝；
- $\beta$ 攻击 $\alpha$，但 $\beta$ 已被拒绝，根据原则3，$\alpha$ 被复原从而可接受。

因此，可接受的论证为 $\{\gamma, \alpha\}$。

**例8.6**（相互攻击的情况）：
在论辩框架 $\text{AF}_6 = \langle \{\alpha, \beta\}, \{(\alpha, \beta), (\beta, \alpha)\} \rangle$ 中，$\alpha$ 和 $\beta$ 互相攻击，形成一个长为2的环。这种情况下，可以在两者之间选择其一（但不能同时接受两者，因为它们互相攻击），或者都不接受。不同的论辩语义会对这种情况给出不同的处理方式。

### 8.2.2 两种语义描述方式

抽象论辩理论提供两种等价的方式来描述论辩语义：

1. **基于外延的方法 (Extension-based Approach)**：将论辩语义定义为从==论辩框架到一组"外延 (Extensions)"的映射==，每个外延是满足特定条件的一个论证集合。
2. **基于标记的方法 (Labelling-based Approach)**：为每个论证分配一个标记：==$\text{IN}$（接受）、$\text{OUT}$（拒绝）或 $\text{UNDEC}$（未决）==，通过标记函数来刻画论证的可接受状态。

这两种方法被证明是等价的：在合理的条件下，外延中的论证恰好对应被标记为 $\text{IN}$ 的论证。

---

## 8.3 基于外延的语义

### 8.3.1 语义函数的基本定义

**定义8.2**（论辩语义，Argumentation Semantics）：
一个**论辩语义 $\sigma$** 是一个函数，它将每个抽象论辩框架 $\text{AF}$ 映射到一个外延集合 $\mathcal{E}_\sigma(\text{AF})$，其中每个 $E \in \mathcal{E}_\sigma(\text{AF})$ 是 $AR$ 的一个子集，称为 $\sigma$ 语义下的一个**外延 (Extension)**。

不同的==论辩语义（可相容、完全、基、优先、稳定、半稳定）对"什么是合理的论证集合"有不同的判断标准==。这些语义形成了一个层次体系，从最宽松到最严格。

### 8.3.2 可相容外延

可相容外延 (Admissible Extension) 是最基本的语义概念。它要求一个论证集合==既内部无冲突，又能自我辩护==。

**定义8.3**（无冲突性，Conflict-free）：
设 $\text{AF} = \langle AR, \text{attacks} \rangle$，$E \subseteq AR$。称 $E$ 是**无冲突的 (Conflict-free)**，当且仅当不存在 $\alpha, \beta \in E$ 使得 $\alpha \to \beta$。

换言之，在一个无冲突的集合中，任何两个论证之间都不存在攻击关系。

**定义8.4**（可防御性，Defense）：
设 $E \subseteq AR$，$\alpha \in AR$。称 $E$ **防御 (Defend)** $\alpha$，当且仅当对于任意 $\beta \in AR$，若 $\beta \to \alpha$，则 $E \to \beta$（即 $E$ 中的某个论证攻击 $\beta$）。

换言之，==$E$ 防御 $\alpha$ 意味着 $E$ 能够"反击"$\alpha$ 的每一个攻击者。==

**定义8.5**（可相容外延，Admissible Extension）：
$E \subseteq AR$ 是一个**可相容外延 (Admissible Extension)**，当且仅当：

1. $==E$ 是无冲突的（Conflict-free）；==
2. ==$E$ 防御 $E$ 中的每一个论证（即 $\forall \alpha \in E$，$E$ 防御 $\alpha$）。==

**单调性性质**：可相容外延的一个重要性质是单调性：如果 $E$ 是可相容的，并且 $E$ 防御某个论证 $\alpha$，那么 $E \cup \{\alpha\}$ 也是可相容的。

**例8.7**（可相容外延示例）：
在 $\text{AF}_3 = \langle \{\alpha, \beta\}, \{(\beta, \alpha)\} \rangle$ 中：
- $\emptyset$ 是可相容的（空集显然无冲突，且不需要防御任何论证）；
- $\{\beta\}$ 是可相容的（无冲突，且 $\beta$ 不需要防御任何攻击者，因为无人攻击 $\beta$）；
- $\{\alpha\}$ 不是可相容的（因为 $\beta \to \alpha$ 但 $\alpha$ 不能防御 $\beta$ 的攻击）；
- $\{\alpha, \beta\}$ 不是可相容的（因为 $\beta \to \alpha$，不无冲突）。

**例8.8**：
在 $\text{AF}_5 = \langle \{\alpha, \beta, \gamma\}, \{(\beta, \alpha), (\gamma, \beta)\} \rangle$ 中：
- $\{\gamma\}$ 是可相容的；
- $\{\gamma, \alpha\}$ 是可相容的：$\gamma$ 防御 $\alpha$（因为 $\gamma \to \beta$ 且 $\beta \to \alpha$），且内部无冲突。

**例8.9**（互相攻击的情况）：
在 $\text{AF}_6 = \langle \{\alpha, \beta\}, \{(\alpha, \beta), (\beta, \alpha)\} \rangle$ 中：
- $\emptyset$ 是可相容的；
- $\{\alpha\}$ 是可相容的（$\alpha$ 攻击 $\beta$，防御了自己免受 $\beta$ 的攻击，且内部无冲突）；
- $\{\beta\}$ 是可相容的（同理）；
- $\{\alpha, \beta\}$ 不是可相容的（不无冲突）。

### 8.3.3 完全外延

完全外延 (Complete Extension) 在可相容的基础上增加了"完备性"要求：外延必须恰好包含它所防御的所有论证。

**定义8.6**（特征函数，Characteristic Function）：
对于论辩框架 $\text{AF} = \langle AR, \text{attacks} \rangle$，定义其**特征函数** $F_{\text{AF}}: 2^{AR} \to 2^{AR}$ 如下：

$$F_{\text{AF}}(S) = \{\alpha \in AR \mid S \text{ 防御 } \alpha\}$$

即 $F_{\text{AF}}(S)$ 返回所有被 $S$ 防御的论证的集合。

**核心概念理解：特征函数**

特征函数 $F_{\text{AF}}$ 可以理解为"一步推理"操作：给定当前接受的论证集合 $S$，$F_{\text{AF}}(S)$ 给出所有被 $S$ 保护的论证。如果一个论证的所有攻击者都被 $S$ 中的论证攻击（从而被击败），则该论证被 $S$ 防御，因而属于 $F_{\text{AF}}(S)$。

**定义8.7**（完全外延，Complete Extension）：
==$E \subseteq AR$ 是一个**完全外延 (Complete Extension)**，当且仅当：==

1. ==$E$ 是可相容的；==
2. ==$F_{\text{AF}}(E) = E$（即 $E$ 是特征函数的一个不动点）。==

换言之，完全外延不仅防御自身中的所有论证，还必须恰好包含所有它能防御的论证——不多不少。

**例8.10**（特征函数的计算）：
在 $\text{AF}_3 = \langle \{\alpha, \beta\}, \{(\beta, \alpha)\} \rangle$ 中：
- $F_{\text{AF}}(\emptyset) = \{\beta\}$（空集防御 $\beta$，因为 $\beta$ 没有攻击者）；
- $F_{\text{AF}}(\{\beta\}) = \{\beta\}$（$\{\beta\}$ 防御 $\beta$，也防御 $\alpha$？不，$\beta \to \alpha$ 但 $\{\beta\}$ 防御 $\alpha$ 吗？$\alpha$ 的唯一攻击者是 $\beta$，而 $\{\beta\} \to \beta$？不对——$\beta$ 攻击 $\alpha$，但为了防御 $\alpha$，需要攻击 $\alpha$ 的攻击者即 $\beta$。而 $\beta \in \{\beta\}$ 不攻击自身。所以 $\{\beta\}$ 不防御 $\alpha$。因此 $F_{\text{AF}}(\{\beta\}) = \{\beta\}$）。

由于 $\{\beta\}$ 是可相容的且 $F_{\text{AF}}(\{\beta\}) = \{\beta\}$，因此 $\{\beta\}$ 是完全外延。

**例8.11**：
在 $\text{AF}_5 = \langle \{\alpha, \beta, \gamma\}, \{(\beta, \alpha), (\gamma, \beta)\} \rangle$ 中：

- 空集 $\emptyset$：$F_{\text{AF}}(\emptyset) = \{\gamma\}$，因为 $\gamma$ 没有攻击者，被空集防御。而 $\emptyset \neq F_{\text{AF}}(\emptyset)$，所以 $\emptyset$ 不是完全外延。
- $\{\gamma\}$：$F_{\text{AF}}(\{\gamma\}) = \{\gamma, \alpha\}$，因为 $\{\gamma\}$ 防御 $\gamma$（无攻击者），也防御 $\alpha$（$\alpha$ 的唯一攻击者是 $\beta$，而 $\gamma \to \beta$）。因为 $F_{\text{AF}}(\{\gamma\}) \neq \{\gamma\}$，所以不是完全外延。
- $\{\gamma, \alpha\}$：$F_{\text{AF}}(\{\gamma, \alpha\}) = \{\gamma, \alpha\}$，因为 $\{\gamma, \alpha\}$ 防御自身。因此 $\{\gamma, \alpha\}$ 是完全外延。

**例8.12**（多个完全外延）：
考虑论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \alpha), (\alpha, \gamma), (\beta, \gamma)\} \rangle$。
完全外延有：$\emptyset$，$\{\alpha\}$，$\{\beta\}$。

**例8.13**（复杂框架中的完全外延）：
考虑论辩框架 $\text{AF}_4 = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \alpha), (\alpha, \gamma), (\beta, \gamma), (\gamma, \delta)\} \rangle$。
完全外延有：$\emptyset$，$\{\alpha, \delta\}$，$\{\beta, \delta\}$。

### 8.3.4 基外延和优先外延

不同的完全外延代表了不同的"合理观点"。在某些论辩框架中，可能存在多个完全外延。**基外延 (Grounded Extension)** 和**优先外延 (Preferred Extension)** 分别从极小和极大的角度来挑选最合理的完全外延。

**定义8.8**（基外延和优先外延）：
设 $\text{AF} = \langle AR, \text{attacks} \rangle$，$\sigma$ 为完全语义。
- $E$ 是 $\text{AF}$ 的一个**基外延 (Grounded Extension)**，当且仅当 $E$ 是 $\text{AF}$ 的所有完全外延中关于集合包含关系 $\subseteq$ 的**极小元**。
- $E$ 是 $\text{AF}$ 的一个**优先外延 (Preferred Extension)**，当且仅当 $E$ 是 $\text{AF}$ 的所有完全外延中关于集合包含关系 $\subseteq$ 的**极大元**。

**核心概念理解：基外延和优先外延**

- **基外延**：采用最"谨慎"的立场，只接受那些在所有可能的合理观点中都无可争议的论证。它对应于特征函数 $F_{\text{AF}}$ 的**最小不动点 (Least Fixed Point)**。
- **优先外延**：采用最"大胆"的立场，尽可能多地接受论证，只要它们能构成一个一致的、自辩护的集合。一个论辩框架可以有多个优先外延，代表不同的合理但互不相容的立场。

基外延是唯一的（任何论辩框架恰好有一个基外延），而优先外延可以有多个。基外延一定是某个优先外延的子集。

**计算基外延**：基外延可以通过迭代计算特征函数来得到。定义：

$$F_{\text{AF}}^0 = \emptyset, \quad F_{\text{AF}}^{i+1} = F_{\text{AF}}(F_{\text{AF}}^i)$$

由于 $AR$ 是有限的，存在 $k$ 使得 $F_{\text{AF}}^{k} = F_{\text{AF}}^{k+1}$，此时基外延即为 $F_{\text{AF}}^k$。

**例8.14**（基外延和优先外延示例）：
考虑论辩框架 $\text{AF}_5 = \langle \{\alpha, \beta, \gamma, \eta\}, \{(\beta, \alpha), (\gamma, \beta), (\eta, \beta), (\gamma, \eta), (\eta, \gamma)\} \rangle$。

完全外延为：$\{\alpha\}$，$\{\alpha, \gamma\}$，$\{\alpha, \eta\}$。

- **基外延**：$\{\alpha\}$（最小的完全外延，也是特征函数的最小不动点）。
- **优先外延**：$\{\alpha, \gamma\}$ 和 $\{\alpha, \eta\}$（两个极大的完全外延，互不相容，因为 $\gamma$ 和 $\eta$ 互相攻击，不能同时接受）。

直观解释：$\alpha$ 是唯一在所有合理观点中都接受的论证（因为它的攻击者 $\beta$ 总是被击败）。而 $\gamma$ 和 $\eta$ 的相互冲突导致存在两种对立的合理观点。

**例8.14续**（基外延的计算过程）：
- $F_{\text{AF}}^0 = \emptyset$
- $F_{\text{AF}}^1 = F_{\text{AF}}(\emptyset) = \{\alpha\}$（$\alpha$ 没有受到任何不被空集反击的攻击）
- 实际上 $\beta \to \alpha$，但 $\beta$ 受到 $\gamma$ 和 $\eta$ 的攻击。空集不能反击 $\beta$，所以需要检查。$\alpha$ 是否被空集防御？不，因为 $\beta \to \alpha$ 而空集不攻击 $\beta$。但 $\gamma$ 被空集防御吗？$\gamma$ 的攻击者是 $\eta$，而空集不攻击 $\eta$。所以 $F_{\text{AF}}(\emptyset) = \emptyset$。
- 重新考虑：如果 $\gamma, \eta$ 互相攻击，空集不能防御任何一方。但 $\alpha$ 的唯一攻击者是 $\beta$，而 $\beta$ 有攻击者 $\gamma$ 和 $\eta$。空集不能攻击 $\beta$。所以 $F_{\text{AF}}(\emptyset) = \emptyset$。
- 因此基外延为 $\emptyset$。

（注：此例的具体细节依赖于实际的攻击关系图，具体框架详见教材。）

### 8.3.5 稳定外延与半稳定外延

稳定外延 (Stable Extension) 是最严格、最直观的语义之一：它要求外延恰好"击败"所有不属于它的论证。

**定义8.9**（稳定外延，Stable Extension）：
$E \subseteq AR$ 是一个**稳定外延 (Stable Extension)**，当且仅当：
1. $E$ 是无冲突的；
2. 对于所有 $\alpha \in AR \setminus E$，$E \to \alpha$（即 $E$ 攻击每一个不在其中的论证）。

换言之，一个稳定外延将论证集合严格划分为"胜利者"（属于 $E$）和"失败者"（不属于 $E$），且每一个失败者都被至少一个胜利者直接攻击。

**性质**：
- 每一个稳定外延都是优先外延，但反过来不一定成立。
- 不是每一个论辩框架都有稳定外延。存在稳定外延的框架称为**稳定的 (Stable)**。

**例8.15**（稳定外延示例）：
在 $\text{AF}_3 = \langle \{\alpha, \beta\}, \{(\beta, \alpha)\} \rangle$ 中：
- $\{\beta\}$ 是稳定外延：无冲突，且 $\beta \to \alpha$（攻击了唯一不在 $E$ 中的 $\alpha$）。

**例8.16**（无稳定外延的框架——奇数环）：
考虑论辩框架 $\text{AF}_7 = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \alpha)\} \rangle$（一个长为3的有向环）。

检查可能的候选：
- $\emptyset$：需要攻击 $\alpha, \beta, \gamma$，但空集不能攻击任何论证。不是稳定外延。
- $\{\alpha\}$：需要攻击 $\beta$ 和 $\gamma$。$\alpha \to \beta$，但 $\alpha \not\to \gamma$（$\alpha$ 不攻击 $\gamma$）。不是稳定外延。
- $\{\beta\}$：需要攻击 $\alpha$ 和 $\gamma$。$\beta \to \gamma$，但 $\beta \not\to \alpha$。不是稳定外延。
- $\{\gamma\}$：需要攻击 $\alpha$ 和 $\beta$。$\gamma \to \alpha$，但 $\gamma \not\to \beta$。不是稳定外延。
- $\{\alpha, \beta\}$：不无冲突（$\alpha \to \beta$）。
- $\{\alpha, \beta, \gamma\}$：不无冲突（存在攻击环）。

因此 $\text{AF}_7$ 没有稳定外延。这种现象是由奇数长度的有向攻击环导致的。

**定义8.10**（半稳定外延，Semi-stable Extension）：
$E \subseteq AR$ 是一个**半稳定外延 (Semi-stable Extension)**，当且仅当：
1. $E$ 是完全外延；
2. $E \cup E^+$ 在所有完全外延中关于 $\subseteq$ 是极大的，其中 $E^+ = \{\alpha \in AR \mid E \to \alpha\}$。

半稳定外延可以视为稳定外延的推广：在稳定外延中，$E \cup E^+ = AR$（覆盖全部论证）；在半稳定外延中，$E \cup E^+$ 尽可能大，但不一定覆盖全部论证。

**性质**：
- 每一个稳定外延都是半稳定外延。
- 每一个半稳定外延都是优先外延。
- 每一个论辩框架至少有一个半稳定外延（存在性保证）。

**例8.17**（半稳定外延示例）：
在 $\text{AF}_7$（三元环）中，虽然不存在稳定外延，但存在半稳定外延。完全外延有：$\emptyset$。$E \cup E^+ = \emptyset$，且 $\emptyset$ 是唯一的完全外延，因此它也是半稳定外延。

**例8.18**（法律推理中的稳定外延应用）：
考虑涉及四个论证的合同法案例：
- $\alpha$："合同因欺诈而无效"
- $\beta$："合同经双方自愿签署，合法有效"
- $\gamma$："签名经鉴定为伪造"
- $\delta$："被告声称未签署过该合同"

攻击关系：$\gamma \to \beta$（伪造签名否定合同有效性），$\beta \to \alpha$（合同有效否定无效主张），$\alpha \to \beta$（无效主张否定合同有效），$\gamma \to \delta$（签名为伪造不影响"未签署"的主张？实际上 $\gamma$ 支持了"伪造"但不等同于 $\delta$）。

在该框架中，稳定外延可能是 $\{\alpha, \gamma\}$ 或 $\{\beta\}$，取决于具体的攻击关系配置，反映出法律推理中存在多种合理判决的可能性。

### 8.3.6 各外延语义之间的关系总结

各外延语义之间的包含关系如下（箭头表示"是...的子集"或"蕴含"关系）：

- 稳定外延 $\subseteq$ 半稳定外延 $\subseteq$ 优先外延 $\subseteq$ 完全外延 $\subseteq$ 可相容外延
- 基外延 $\subseteq$ 完全外延
- 基外延 $\subseteq$ 每一个优先外延

可以用下表总结每种外延的定义条件：

| 外延类型 | 无冲突 | 自防御 | 完备性 | 额外条件 |
|---------|--------|--------|--------|---------|
| 可相容 | 是 | 是 | 否 | — |
| 完全 | 是 | 是 | 是（不动点） | — |
| 基 | 是 | 是 | 是 | 极小完全外延 |
| 优先 | 是 | 是 | 是 | 极大完全外延 |
| 稳定 | 是 | 是（导出） | 是（导出） | 攻击所有不在外延中的论证 |
| 半稳定 | 是 | 是（导出） | 是 | $E \cup E^+$ 极大 |

---

## 8.4 基于标记的语义

基于标记的语义 (Labelling-based Semantics) 提供了另一种理解论辩语义的视角：为每个论证分配一个标记，而不是构造论证的集合。

### 8.4.1 基本定义

**定义8.11**（标记，Labelling）：
对于论辩框架 $\text{AF} = \langle AR, \text{attacks} \rangle$，一个**标记 (Labelling)** 是一个全函数 $L: AR \to \{\text{IN}, \text{OUT}, \text{UNDEC}\}$，将每个论证映射到三个可能状态之一：

- $\text{IN}$：论证被接受；
- $\text{OUT}$：论证被拒绝；
- $\text{UNDEC}$：论证处于未决状态（既不接受也不拒绝）。

记 $\text{in}(L) = \{\alpha \in AR \mid L(\alpha) = \text{IN}\}$，类似地定义 $\text{out}(L)$ 和 $\text{undec}(L)$。

### 8.4.2 合法标记

合法标记 (Legal Labelling) 刻画了单个论证的标记是否与其攻击者的标记一致。

**定义8.12**（合法标记，Legal Labelling）：
对于论证 $\alpha$ 和标记 $L$：
- $L(\alpha) = \text{IN}$ 是**合法的**，当且仅当对于所有攻击 $\alpha$ 的论证 $\beta$，$L(\beta) = \text{OUT}$。
- $L(\alpha) = \text{OUT}$ 是**合法的**，当且仅当存在某个攻击 $\alpha$ 的论证 $\beta$，使得 $L(\beta) = \text{IN}$。
- $L(\alpha) = \text{UNDEC}$ 是**合法的**，当且仅当：(1) 不存在攻击 $\alpha$ 的论证 $\beta$ 使得 $L(\beta) = \text{IN}$，且 (2) 存在攻击 $\alpha$ 的论证 $\beta$ 使得 $L(\beta) \neq \text{OUT}$（即至少有一个攻击者不是 $\text{OUT}$——通常是 $\text{UNDEC}$）。

**直观理解**：
- 一个论证可以被标记为 $\text{IN}$，意味着它战胜了所有攻击者（所有攻击者都是 $\text{OUT}$）。
- 一个论证被标记为 $\text{OUT}$，意味着它被某个被接受的论证（$\text{IN}$）击败。
- 一个论证被标记为 $\text{UNDEC}$，意味着它在冲突中处于"僵局"状态——没有 $\text{IN}$ 的攻击者击败它，但也不是所有攻击者都被击败。

### 8.4.3 可相容标记和完全标记

**定义8.13**（可相容标记，Admissible Labelling）：
标记 $L$ 是**可相容的 (Admissible)**，当且仅当对于所有论证 $\alpha \in AR$：
- 若 $L(\alpha) = \text{IN}$，则 $\alpha$ 的 $\text{IN}$ 标记是合法的；
- 若 $L(\alpha) = \text{OUT}$，则 $\alpha$ 的 $\text{OUT}$ 标记是合法的。

注意：在可相容标记中，$\text{UNDEC}$ 标记不需要是合法的——它们可以是"不确定"的任意状态。

**定义8.14**（完全标记，Complete Labelling）：
标记 $L$ 是**完全的 (Complete)**，当且仅当：
1. $L$ 是可相容的；
2. 对于所有 $\alpha \in AR$，若 $L(\alpha) = \text{UNDEC}$，则 $\alpha$ 的 $\text{UNDEC}$ 标记也是合法的。

换言之，完全标记要求所有论证的标记（包括 $\text{UNDEC}$）都是合法的。

### 8.4.4 各类标记的层次

与基于外延的语义类似，基于标记的语义也形成一个层次体系：

**定义8.15**（各类标记的定义）：
- **优先标记 (Preferred Labelling)**：极大化 $\text{in}(L)$（即 $\text{in}(L)$ 在完全标记中关于 $\subseteq$ 极大）。
- **基标记 (Grounded Labelling)**：极小化 $\text{in}(L)$（即 $\text{in}(L)$ 在完全标记中关于 $\subseteq$ 极小）。
- **稳定标记 (Stable Labelling)**：$\text{undec}(L) = \emptyset$（即完全标记中没有任何 $\text{UNDEC}$ 论证）。
- **半稳定标记 (Semi-stable Labelling)**：在完全标记中，极小化 $\text{undec}(L)$（即最大化确定的论证数量）。

### 8.4.5 与外延语义的对应关系

基于外延的语义和基于标记的语义之间存在自然的对应关系：

- 若 $L$ 是一个完全标记，则 $\text{in}(L)$ 是一个完全外延。
- 若 $E$ 是一个完全外延，则定义 $L$ 使得 $L(\alpha) = \text{IN}$（若 $\alpha \in E$），$L(\alpha) = \text{OUT}$（若 $E \to \alpha$），$L(\alpha) = \text{UNDEC}$（其他情况），那么 $L$ 是一个完全标记。

这一对应关系同样适用于优先/基/稳定/半稳定标记与外延之间。

### 8.4.6 标记方法的实例

**例8.19**（简单标记示例）：
在 $\text{AF}_3 = \langle \{\alpha, \beta\}, \{(\beta, \alpha)\} \rangle$ 中：
- 完全标记：$L_1 = \{\beta: \text{IN}, \alpha: \text{OUT}\}$（也是稳定标记和优先标记）；
- 基标记：同 $L_1$（$\text{in}(L_1) = \{\beta\}$ 是最小的完全标记的 $\text{IN}$ 集）。

**例8.20**（互相攻击的标记）：
在 $\text{AF}_6 = \langle \{\alpha, \beta\}, \{(\alpha, \beta), (\beta, \alpha)\} \rangle$ 中：
- 完全标记有三个：
  - $L_1 = \{\alpha: \text{IN}, \beta: \text{OUT}\}$（优先标记）
  - $L_2 = \{\alpha: \text{OUT}, \beta: \text{IN}\}$（优先标记）
  - $L_3 = \{\alpha: \text{UNDEC}, \beta: \text{UNDEC}\}$（基标记）
- 不存在稳定标记（因为无法使 $\text{undec} = \emptyset$）。

**例8.21**（三元环的标记）：
在 $\text{AF}_7 = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \alpha)\} \rangle$ 中：
- 唯一的完全标记是 $L = \{\alpha: \text{UNDEC}, \beta: \text{UNDEC}, \gamma: \text{UNDEC}\}$，也是基标记和唯一的优先标记。
- 不存在稳定标记。

**例8.22**（对话系统中的标记应用）：
考虑一个论证对话系统，两个智能体进行辩论。Agent A 提出论证 $\alpha$；Agent B 以 $\beta$ 反驳；Agent A 再以 $\gamma$ 反驳 $\beta$。论辩框架：

$$\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\beta, \alpha), (\gamma, \beta)\} \rangle$$

唯一完全标记为 $L = \{\alpha: \text{IN}, \beta: \text{OUT}, \gamma: \text{IN}\}$，这也是基标记、优先标记和稳定标记。这表明 Agent A 的立场（$\alpha$ 和 $\gamma$）是胜利的。

---

## 8.5 论证的状态

### 8.5.1 基于外延的论证状态

**定义8.16**（论证的接受状态）：
给定一个外延 $E$，论证 $\alpha$ 的状态可以是：
- ==**被接受 (Accepted)**：$\alpha \in E$==
- ==**被拒绝 (Rejected)**：$E \to \alpha$（即 $E$ 攻击 $\alpha$）==
- ==**未决 (Undecided)**：$\alpha \notin E$ 且 $E \not\to \alpha$==

基于标记的对应定义：
- $L(\alpha) = \text{IN}$：被接受
- $L(\alpha) = \text{OUT}$：被拒绝
- $L(\alpha) = \text{UNDEC}$：未决

### 8.5.2 辩护状态

当论辩语义产生多个外延时（如优先语义允许多个外延），同一个论证在不同外延中可能有不同的状态。**辩护状态 (Justification Status)** 刻画了论证在所有可能外延中的整体接受情况。

**定义8.17**（辩护状态，Justification Status）：
给定论辩语义 $\sigma$ 和论辩框架 $\text{AF}$：
- $\alpha$ 是**怀疑性被辩护的 (Skeptically Justified)**（或在 $\sigma$ 语义下被接受），当且仅当对于所有 $E \in \mathcal{E}_\sigma(\text{AF})$，$\alpha \in E$。即 $\alpha$ 在每一个 $\sigma$ 外延中都被接受。
- $\alpha$ 是**轻信性被辩护的 (Credulously Justified)**，当且仅当存在 $E_1, E_2 \in \mathcal{E}_\sigma(\text{AF})$，使得 $\alpha \in E_1$ 但 $\alpha \notin E_2$。即 $\alpha$ 在至少一个外延中被接受，但不是全部。
- $\alpha$ 是**不被辩护的 (Not Justified)**，当且仅当不存在 $E \in \mathcal{E}_\sigma(\text{AF})$ 使得 $\alpha \in E$。即 $\alpha$ 在所有外延中都不被接受。

**核心概念理解：三种辩护状态**

- **怀疑性辩护**：最严格的接受标准，要求论证在每一种合理的立场中都被接受。相当于"无可争议地为真"。
- **轻信性辩护**：较宽松的标准，论证在至少一种合理立场中被接受，但存在其他合理立场不接受它。相当于"可以合理地被相信"。
- **不被辩护**：论证在任何合理立场中都不被接受。

### 8.5.3 应用实例

**例8.23**（法律推理中的辩护状态）：
在涉及四个论证的法律案例论辩框架中，假设优先语义有两个外延：
- $E_1 = \{\alpha, \gamma\}$（原告胜诉）
- $E_2 = \{\beta, \delta\}$（被告胜诉）

则：
- $\alpha$ 是轻信性被辩护的（仅在 $E_1$ 中被接受）
- $\beta$ 是轻信性被辩护的（仅在 $E_2$ 中被接受）
- 没有任何论证是怀疑性被辩护的

这反映出法律推理中合理分歧的存在——两种对立的判决在不同视角下都可以是合理的。

**例8.24**（AIGC事实核查应用——珠穆朗玛峰高度验证）：
在人工智能生成内容 (AIGC) 的事实核查中，可以使用论辩理论整合来自多个信息源的论证。考虑关于珠穆朗玛峰高度的验证问题，有五个信息源提供了论证：

- $\alpha_1$："珠峰高度为8848.86米——中国-尼泊尔联合测量（2020年）"
- $\alpha_2$："珠峰高度为8848米——尼泊尔官方数据（旧）"
- $\alpha_3$："珠峰高度为8844.43米——中国测绘局数据（2005年岩面高度）"
- $\alpha_4$："珠峰高度为8850米——美国国家地理学会估计"
- $\alpha_5$："珠峰高度持续变化，无法确定——基于地质板块运动理论"

论辩框架中的攻击关系：
- $\alpha_1 \to \alpha_2$（最新权威数据否定旧数据）
- $\alpha_1 \to \alpha_3$（2020年测量更新2005年结果）
- $\alpha_1 \to \alpha_4$（国际联合测量比单方估计更可信）
- $\alpha_5 \to \alpha_1, \alpha_2, \alpha_3, \alpha_4$（地质变化论否定所有固定数值）
- $\alpha_1 \to \alpha_5$（精确测量可以确定当前高度）

在优先语义下，假设存在外延 $E_1 = \{\alpha_1\}$ 和 $E_2 = \{\alpha_5\}$。则：
- $\alpha_1$ 是轻信性被辩护的（最精确的测量数据）
- $\alpha_5$ 是轻信性被辩护的（地质理论的挑战）
- $\alpha_2, \alpha_3, \alpha_4$ 是不被辩护的（过时或较不可靠的数据）

这一分析表明，虽然8848.86米是当前最权威的数据，但"高度可能持续变化"的观点也有其合理性。

**例8.25**（基语义下的唯一结论）：
在上述高度验证案例的**基语义**下，由于不同外延之间不一致（$\alpha_1$ 和 $\alpha_5$ 互相攻击），基外延可能仅包含那些在所有外延中都一致的论证。具体的基外延取决于框架的完整定义。

---

## 8.6 论辩语义的局部性和可组合性

### 8.6.1 基本概念

在大规模论辩系统中，逐一评估所有论证的语义代价高昂。==**局部性 (Locality)** 和**可组合性 (Composability)** 研究如何将大框架分解为子框架，分别评估后再合成全局结果。==

**四种局部查询类型**：
1. 给定论证 $\alpha$，判断其辩护状态；
2. 给定论证集合 $S$，找出相关的论证子集；
3. 分析论证的拓扑位置（如在哪个 SCC 中）；
4. 动态论辩：新增或删除论证/攻击关系后，更新已有的语义计算结果。

### 8.6.2 子框架的定义

**外部父节点 (External Parents)**：
对于 $B \subseteq AR$（$B$ 是框架的子集），定义 $B$ 的外部父节点集合：

$$B^- = \{\alpha \in AR \setminus B \mid \exists \beta \in B: (\alpha, \beta) \in \text{attacks}\}$$

即 $B^-$ 包含了所有不在 $B$ 中但攻击 $B$ 中某个论证的论证。

**定义8.18**（子框架，Sub-framework）：
- **无约束子框架 (Unconstrained Sub-framework)**：当 $B^- = \emptyset$（即 $B$ 不受外部论证的攻击）时，子框架为 $(B, R_B)$，其中 $R_B = \text{attacks} \cap (B \times B)$。此时 $B$ 在语义上是独立的。
- **有约束子框架 (Constrained Sub-framework)**：当 $B^- \neq \emptyset$ 时，子框架为 $((B, R_B), (B^-, I_B))$，其中 $I_B = \text{attacks} \cap (B^- \times B)$。此时 $B$ 的语义依赖外部论证 $B^-$ 的标记状态。

**例8.26**（子框架示例）：
考虑论辩框架 $\text{AF}_{11} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \gamma), (\delta, \gamma)\} \rangle$：
- 取 $B = \{\alpha, \beta\}$，则 $B^- = \emptyset$（没有外部论证攻击 $B$ 中的论证）。$(B, R_B) = (\{\alpha, \beta\}, \{(\alpha, \beta)\})$ 是一个无约束子框架。
- 取 $C = \{\gamma\}$，则 $C^- = \{\beta, \delta\}$。$(C, R_C) = (\{\gamma\}, \emptyset)$，且 $I_C = \{(\beta, \gamma), (\delta, \gamma)\}$。这是一个有约束子框架，其语义依赖于 $\beta$ 和 $\delta$ 的标记。

### 8.6.3 子框架的语义

在**方向性语义 (Directional Semantics)**（完全、优先、基语义）下，无约束子框架中的论证状态可以独立评估，不受框架其余部分的影响。这一性质使得"分而治之"的评估策略成为可能。

**定义8.19-8.22**（局部标记子框架的定义）：
对于各类语义，可以定义"局部合法标记"的概念，使得子框架的标记与其父节点的状态一致。

- **局部可相容标记**：子框架中的论证标记在给定外部论证标记的条件下，满足可相容标记的合法性条件。
- **局部完全标记**：类似地扩展到完全标记。
- **局部优先标记**：在给定外部标记条件下，最大化子框架中的 $\text{IN}$ 论证。
- **局部基/稳定标记**：对应地进行极小化或消除 $\text{UNDEC}$。

### 8.6.4 框架分解与合并

**基于 SCC 的分解**：

论辩框架 $\text{AF}$ 可以基于其有向图结构的**强连通分量 (Strongly Connected Components, SCCs)** 进行分解：

1. 将 $\text{AF}$ 的论证集合划分为 SCCs；
2. 在 SCC 之间定义偏序关系：$S_1 \preceq S_2$ 当且仅当存在从 $S_1$ 到 $S_2$ 的路径；
3. 由此得到的**浓缩图 (Condensed Graph)** 是一个有向无环图 (DAG)。

每个 SCC 被视为一个子框架，按照 DAG 的拓扑序从"源"到"汇"依次评估。

### 8.6.5 子框架的语义合成

**组合标记运算**：

给定两个相邻的 SCC $B$ 和 $C$（其中 $B^- \subseteq C$，即 $C$ 是 $B$ 的"父"SCC），语义合成规则为：

$$\text{CombLab}_\sigma((B \cup C, R_{B \cup C})) = \{L_1 \cup L_2 \mid L_1 \in \mathcal{L}_\sigma((C, R_C)) \land L_2 \in \mathcal{L}_\sigma(((B, R_B), (B^-, I_B)^{L_1}))\}$$

其中 $(B^-, I_B)^{L_1}$ 表示在给定 $L_1$ 对 $B^- \subseteq C$ 中论证的标记下，$B$ 的约束条件。

**例8.27**（语义合成示例）：
考虑论辩框架：
$$\text{AF} = \langle \{a, b, c, d\}, \{(a, b), (b, a), (b, c), (c, d)\} \rangle$$

SCC 分解：
- $S_1 = \{a, b\}$（$\{a, b\}$ 构成一个 SCC，因为 $a \to b$ 和 $b \to a$ 形成双向可达）
- $S_2 = \{c\}$（单个论证的 SCC）
- $S_3 = \{d\}$

按照拓扑序（$S_1 \to S_2 \to S_3$），先评估 $S_1$ 的语义，然后将其结果作为 $S_2$ 的外部条件，依此类推，最终合成全局语义结果。

---

## 8.7 小结

本章系统介绍了经典抽象论辩理论的核心内容：

1. **抽象论辩框架 (AF)**：将论证视为原子实体，只关注论证之间的攻击关系，形成一个有向图结构。这一抽象层次允许我们以统一的方式处理各种论辩推理场景。

2. **论辩语义的两种表示方法**：
   - **基于外延的方法**：通过定义论证集合（外延）必须满足的条件来刻画"合理的论证集合"。包括：可相容外延（无冲突且自防御）、完全外延（可相容且满足不动点条件）、基外延（最小的完全外延，最谨慎）、优先外延（最大的完全外延，最大胆）、稳定外延（击败所有不在外延中的论证）、半稳定外延（稳定外延在无解时的推广）。
   - **基于标记的方法**：为每个论证分配 $\text{IN}$/$\text{OUT}$/$\text{UNDEC}$ 三种状态中的一个。标记方法与外延方法等价。

3. **论证的辩护状态**：在产生多个外延的语义下，论证可以是怀疑性被辩护的（在所有外延中都被接受）、轻信性被辩护的（仅在部分外延中被接受）或不被辩护的。

4. **论辩语义的局部性和可组合性**：利用 SCC 分解和方向性语义性质，可以将大框架分解为子框架分别评估后合成结果。

抽象论辩理论为人工智能中的非单调推理、不一致处理、多主体对话和决策提供了坚实的数学基础。它不仅是理论研究的重要工具，也在法律推理、医疗决策、事实核查、AIGC 内容评估等实际应用中展现出强大的适用性。

---

## 学习要点与AI关联

### 学习要点

1. 理解抽象论辩框架的形式定义（论证集合 + 攻击关系），并能够将实际问题建模为抽象论辩框架。
2. 掌握论证可接受性的三条基本原则：无攻击者原则、攻击传递原则、复原原则。
3. 熟练掌握六种基于外延的论辩语义（可相容、完全、基、优先、稳定、半稳定）的定义和相互关系。
4. 理解基于标记的论辩语义及其与外延语义的等价性。
5. 能够计算给定论辩框架在各语义下的外延，并判断论证的辩护状态（怀疑性/轻信性/不被辩护）。
6. 理解论辩语义的局部性、SCC 分解和语义合成的基本思想。

### 与AI的关联

- **非单调推理**：抽象论辩理论为非单调推理提供了统一的形式框架，与缺省逻辑、逻辑程序设计（回答集编程）有深刻联系。
- **可解释AI**：论辩框架提供了一种自然地解释AI推理过程的方式——通过展示论证之间的攻击与支持关系。
- **多智能体系统**：在多智能体对话和协商中，论辩框架可以形式化不同智能体的立场和交互。
- **AIGC事实核查与虚假信息检测**：利用论辩框架整合来自多个信息源的论证，检测矛盾和不一致，评估信息的可信度。
- **法律AI**：法律推理天然具有论辩特征（控辩双方各自提出论证），抽象论辩理论是法律AI的核心工具。
- **推荐系统与决策支持**：通过对支持和反对某一选项的论证进行结构化评估，论辩框架可以支持更透明的决策。

---

## 扩展阅读

1. Dung, P. M. (1995). On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games. *Artificial Intelligence*, 77(2), 321-357.（抽象论辩理论的奠基性论文）

2. Baroni, P., Caminada, M., & Giacomin, M. (2011). An Introduction to Argumentation Semantics. *The Knowledge Engineering Review*, 26(4), 365-410.（论辩语义的全面综述）

3. Rahwan, I., & Simari, G. R. (Eds.). (2009). *Argumentation in Artificial Intelligence*. Springer.（AI中论辩理论的综合性著作）

4. Caminada, M., & Gabbay, D. (2009). A Logical Account of Formal Argumentation. *Studia Logica*, 93(2-3), 109-145.（论辩标记语义的逻辑基础）

5. Modgil, S., & Prakken, H. (2014). The ASPIC+ Framework for Structured Argumentation: A Tutorial. *Argument & Computation*, 5(1), 31-62.（结构化论辩框架 ASPIC+ 教程）

6. Atkinson, K., & Bench-Capon, T. (2021). Argumentation Schemes in AI and Law. *Argument & Computation*, 12(3), 417-434.（法律AI中的论辩模式）

---

## 第8讲练习

### 练习 8-1

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta\}, \{(\alpha, \beta), (\beta, \alpha)\} \rangle$（$\alpha$ 和 $\beta$ 互相攻击）。请找出：
1. 所有可相容外延
2. 所有完全外延
3. 基外延
4. 所有优先外延
5. 是否存在稳定外延？为什么？

### 练习 8-2

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \gamma)\} \rangle$（三个论证形成长度为2的链式攻击）。请找出所有完全外延，并指出基外延和优先外延。

### 练习 8-3

证明：每一个稳定外延都是优先外延，但反过来不一定成立。请举例说明一个存在优先外延但不存在稳定外延的论辩框架。

### 练习 8-4

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \alpha), (\beta, \gamma), (\gamma, \delta), (\delta, \gamma)\} \rangle$，请：
1. 画出论辩图；
2. 找出该框架的 SCC 分解；
3. 计算基外延和所有优先外延。

### 练习 8-5

对于 $\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \alpha)\} \rangle$（三元攻击环），使用标记方法给出所有完全标记和优先标记。是否存在稳定标记？

### 练习 8-6

证明：在任何论辩框架中，基外延是唯一的。

### 练习 8-7

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\gamma, \beta), (\beta, \delta)\} \rangle$：
1. 计算特征函数 $F_{\text{AF}}$ 从空集开始迭代的各步结果。
2. 求出基外延。
3. 求所有优先外延和稳定外延。

### 练习 8-8

解释为什么在论辩框架中，可相容外延具有单调性，而优先外延一般不具有单调性。

### 练习 8-9

考虑以下场景：三位评审专家对一篇论文提出评审意见：
- $\alpha$："论文方法创新，建议接受"
- $\beta$："论文实验不充分，建议拒稿"
- $\gamma$："论文理论贡献突出，实验可以在修改阶段补充，建议接受"
- $\delta$："实验结果显示该方法不如基线方法"

攻击关系：$\alpha \to \beta$（创新性否定拒稿意见），$\beta \to \alpha$（实验不足否定接受意见），$\gamma \to \beta$（理论贡献弥补实验不足），$\beta \to \gamma$（实验不足削弱理论贡献），$\delta \to \alpha$（实验不如基线），$\delta \to \gamma$（实验不如基线削弱修改价值）。

1. 给出论辩框架的形式定义；
2. 找出所有优先外延；
3. 判断每个论证在优先语义下的辩护状态（怀疑性/轻信性/不被辩护）。

### 练习 8-10

证明：在论辩框架中，如果外延 $E$ 是稳定的，则 $E$ 也是完全外延。

### 练习 8-11

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta, \varepsilon\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \delta), (\delta, \varepsilon), (\varepsilon, \alpha)\} \rangle$（五元攻击环）：
1. 求所有完全外延；
2. 求基外延和优先外延；
3. 是否存在稳定外延？

### 练习 8-12

对于论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \alpha), (\beta, \gamma)\} \rangle$，使用基于标记的方法：
1. 给出所有可相容标记；
2. 给出所有完全标记；
3. 给出基标记和优先标记。

### 练习 8-13

证明：在标记方法中，若 $L$ 是稳定标记，则 $L$ 也是优先标记。

### 练习 8-14

在论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \alpha), (\alpha, \delta)\} \rangle$ 中：
1. 进行 SCC 分解；
2. 按拓扑序依次计算各 SCC 的完全标记；
3. 合成得到全局完全标记。

### 练习 8-15

讨论：为什么在抽象论辩理论中要忽略论证的内部结构？这种抽象化的优势和局限分别是什么？

### 练习 8-16

在法律推理中，考虑以下关于合同纠纷的论证：
- $\alpha$："合同条款已明确约定交付日期，被告应承担违约责任"
- $\beta$："交货延迟是由于不可抗力（自然灾害）导致的，合同中有不可抗力条款"
- $\gamma$："天气预报显示灾害发生前已有预警，被告未尽到合理注意义务"
- $\delta$："合同中关于不可抗力的定义排除了可预见的自然灾害"

攻击关系：$\beta \to \alpha$，$\gamma \to \beta$，$\delta \to \beta$。

1. 建模为论辩框架；
2. 找出所有完全外延和优先外延；
3. 在优先语义下，判断论证 $\alpha$（原告主张违约责任）的辩护状态。

### 练习 8-17

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta\}, \{(\alpha, \beta)\} \rangle$（$\alpha$ 单方面攻击 $\beta$）：
1. 求所有可相容外延；
2. 求完全外延、基外延、优先外延、稳定外延、半稳定外延；
3. 说明在这种情况下，所有主要语义是否一致。

### 练习 8-18

考虑论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta, \varepsilon\}, \{(\alpha, \beta), (\alpha, \gamma), (\beta, \delta), (\gamma, \delta), (\delta, \varepsilon)\} \rangle$：
1. 画出论辩图；
2. 进行 SCC 分解并画出浓缩 DAG；
3. 按照自底向上的顺序计算基外延。

### 练习 8-19

证明或反驳：如果论辩框架中不存在任何有向环，则任何完全外延都是稳定外延。

### 练习 8-20

在论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \delta), (\delta, \beta)\} \rangle$ 中：
1. 求所有完全外延；
2. 说明基外延与优先外延的关系；
3. 将结果用标记方法重新表述。

### 练习 8-21

考虑论辩框架 $\text{AF}$ 中有 $n$ 个论证 $\alpha_1, \alpha_2, \dots, \alpha_n$，且 $\alpha_i \to \alpha_{i+1}$（对 $i = 1, 2, \dots, n-1$），没有其他攻击关系。请描述当 $n$ 为偶数和奇数时，分别有多少个完全外延，以及基外延和优先外延各是什么。

### 练习 8-22

给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma\}, \{(\alpha, \beta), (\beta, \gamma), (\gamma, \beta)\} \rangle$：
1. 使用标记方法找出所有完全标记；
2. 解释为什么存在不同于基标记的完全标记；
3. 判断稳定标记是否存在。

### 练习 8-23

在论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta\}, \{(\alpha, \beta), (\beta, \alpha), (\alpha, \gamma), (\beta, \gamma), (\gamma, \delta)\} \rangle$ 中：
1. 找出无约束子框架和有约束子框架；
2. 使用语义合成方法计算完全外延；
3. 验证结果是否与直接计算全局完全外延一致。

### 练习 8-24

阅读理解：Dung 的抽象论辩框架如何统一了非单调推理、逻辑程序设计和博弈论？尝试用自己的语言总结这种统一的本质。

### 练习 8-25

实际建模练习：选择以下一个场景（或自选场景），建模为抽象论辩框架，并分析各论证的辩护状态：
- 自动驾驶汽车面对"电车难题"时的伦理决策
- 疫苗安全性的公共卫生辩论
- 人工智能是否会导致大规模失业的经济辩论

要求：(1) 明确列出论证和攻击关系；(2) 画出论辩图；(3) 计算至少两种语义下的外延；(4) 分析论证的辩护状态。

### 练习 8-26

综合性练习：给定论辩框架 $\text{AF} = \langle \{\alpha, \beta, \gamma, \delta, \varepsilon, \zeta\}, \{(\alpha, \beta), (\beta, \alpha), (\alpha, \gamma), (\beta, \gamma), (\gamma, \delta), (\gamma, \varepsilon), (\delta, \zeta), (\varepsilon, \zeta), (\zeta, \gamma)\} \rangle$：
1. 画出论辩图；
2. 进行 SCC 分解并画出浓缩 DAG；
3. 按拓扑序计算各 SCC 的完全外延；
4. 使用语义合成获得全局的基外延和所有优先外延；
5. 判断是否存在稳定外延；
6. 对每个论证，给出其在优先语义下的辩护状态。

---

*本章内容基于 Phan Minh Dung (1995) 的抽象论辩框架理论，结合法律推理、AIGC事实核查等AI应用场景进行阐述。*
