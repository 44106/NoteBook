# 第八讲 正交化方法：逐行讲解

> 公式说明：这个版本把行内公式写成 `\( ... \)`，整行公式写成 `\[ ... \]`。请用支持 MathJax/KaTeX 的 Markdown 预览查看；如果只看源码，看到反斜杠是正常的。

本文按讲义 8 页的顺序解释。讲义是手写图片版，下面的“行”按页面中的内容块和公式顺序编号，不是 PDF 内部文字行号。

## 0. 先把这讲放进整门课的位置

这讲属于“第三章 最小二乘问题”。

最小二乘问题的标准形式是：

\[
\min_{x\in\mathbb{R}^n}\|b-Ax\|_2,
\]

其中：

- \(A\in\mathbb{R}^{m\times n}\) 通常是一个高矩阵，也就是 \(m\ge n\)；
- \(b\in\mathbb{R}^m\) 是观测数据；
- \(x\in\mathbb{R}^n\) 是要求的未知量；
- \(b-Ax\) 是残差；
- 目标是让残差的 2-范数尽可能小。

前面通常有两种思路：

- 正规方程：\(A^T A x=A^T b\)。它推导简单，但数值稳定性较差，因为条件数会被平方。
- 正交化方法：先把 \(A\) 做 QR 分解，再解上三角方程。它更稳定，是这讲重点。

---

## 1. 第 1 页：为什么正交变换适合最小二乘

### 1.1 讲义开头的目录

讲义写：

\[
\S 3.1 \quad \text{最小二乘问题定义、存在唯一性}
\]

意思是先说明最小二乘问题是什么，什么时候有解，什么时候唯一。

接着写：

\[
\S 3.2 \quad \text{正规化方法}
\]

这里的“正规化方法”指正规方程法，也就是从

\[
\min_x \|b-Ax\|_2
\]

推出

\[
A^T A x=A^T b.
\]

讲义旁边红字写“最古老”，意思是这种方法历史早、形式简单，但现在数值计算中不是首选。

再接着写：

\[
\S 3.3 \quad \text{正交化方法}
\]

旁边红字写“更实用”。原因是正交变换不会放大向量长度，也就不容易放大舍入误差。

### 1.2 正交矩阵的定义

讲义写：

\[
Q\in\mathbb{R}^{m\times m},\qquad Q^TQ=QQ^T=I.
\]

这叫正交矩阵。初学时可以把它理解为“保持长度和角度的矩阵”。

因为 \(Q^TQ=I\)，所以对于任意向量 \(y\)：

\[
\|Qy\|_2^2=(Qy)^T(Qy)=y^TQ^TQy=y^Ty=\|y\|_2^2.
\]

也就是说，乘以正交矩阵不会改变 2-范数。

### 1.3 正交变换保持最小二乘目标

讲义写：

\[
\|b-Ax\|_2^2
=(b-Ax)^T(b-Ax).
\]

这是 2-范数平方的定义：

\[
\|r\|_2^2=r^Tr.
\]

令 \(r=b-Ax\)，就是上式。

讲义接着在中间插入 \(Q^TQ=I\)：

\[
(b-Ax)^T(b-Ax)
=(b-Ax)^TQ^TQ(b-Ax).
\]

因为 \(Q^TQ=I\)，插入它不会改变值。

然后得到：

\[
\|b-Ax\|_2^2=\|Q(b-Ax)\|_2^2.
\]

展开括号：

\[
Q(b-Ax)=Qb-QAx.
\]

所以：

\[
\|b-Ax\|_2^2=\|Qb-QAx\|_2^2.
\]

核心含义：如果我们同时对 \(A\) 和 \(b\) 左乘同一个正交矩阵 \(Q\)，最小二乘问题的残差长度不变。因此我们可以选择一个好用的 \(Q\)，把 \(A\) 变成容易求解的形状。

### 1.4 为什么不直接用 Gauss 消元

讲义画了 Gauss 变换：

\[
A\longrightarrow
\begin{pmatrix}
a_{11}&a_{12}&\cdots\\
0&*&\cdots\\
\vdots&\vdots&\\
0&*&\cdots
\end{pmatrix}.
\]

普通 Gauss 消元可以把第一列下面的元素消成 0。

但是普通 Gauss 变换一般不是正交变换。也就是说，它不保证

\[
\|b-Ax\|_2
\]

保持不变。

讲义红字写：

“Motivation: 找到一个具有消元性质且正交矩阵。”

意思是：我们希望像 Gauss 消元一样把矩阵变成上三角，但又要每一步都是正交变换，这样最小二乘目标不被破坏。

这就引出两个基本工具：

- Householder 变换：一次可以消掉一整列下面的多个元素；
- Givens 变换：一次主要消掉一个指定元素。

---

## 2. 第 1-3 页：Householder 变换

## 2.1 Householder 变换的定义

讲义写：

设 \(w\in\mathbb{R}^n\) 且

\[
\|w\|_2=1.
\]

定义

\[
H=I-2ww^T.
\]

则 \(H\in\mathbb{R}^{n\times n}\)，称为 Householder 变换，也叫 Householder 矩阵。

这里：

- \(w\) 是列向量，大小 \(n\times 1\)；
- \(w^T\) 是行向量，大小 \(1\times n\)；
- \(ww^T\) 是 \(n\times n\) 矩阵；
- \(I-2ww^T\) 也是 \(n\times n\) 矩阵。

直觉上，\(H\) 是一个“镜面反射矩阵”。

## 2.2 性质 1：对称性

讲义写：

\[
H=H^T.
\]

证明：

\[
H^T=(I-2ww^T)^T=I^T-2(ww^T)^T=I-2ww^T=H.
\]

因为 \((ww^T)^T=ww^T\)。

所以 Householder 矩阵是对称矩阵。

## 2.3 性质 2：正交性

讲义写：

\[
H^TH=I.
\]

因为刚才已经知道 \(H^T=H\)，所以只要证明 \(H^2=I\)。

讲义上的计算是：

\[
H^TH
=(I-2ww^T)(I-2ww^T).
\]

展开：

\[
=I-2ww^T-2ww^T+4w(w^Tw)w^T.
\]

因为

\[
w^Tw=\|w\|_2^2=1,
\]

所以：

\[
4w(w^Tw)w^T=4ww^T.
\]

于是：

\[
I-4ww^T+4ww^T=I.
\]

这说明 Householder 矩阵是正交矩阵。

## 2.4 性质 3：对合性

讲义写：

\[
H^2=I.
\]

对合性的意思是：做两次同样的 Householder 反射，就回到原处。

这和几何中的镜面反射完全一致。一个点关于同一平面反射两次，回到原来的位置。

## 2.5 性质 4：反射性

讲义写：

对任意 \(x\in\mathbb{R}^n\)，\(Hx\) 是 \(x\) 关于与 \(w\) 垂直的超平面 \(\operatorname{span}\{w\}^{\perp}\) 的镜像反射。

这里有几个概念：

- \(\operatorname{span}\{w\}\) 是 \(w\) 张成的一维直线；
- \(\operatorname{span}\{w\}^{\perp}\) 是所有与 \(w\) 垂直的向量组成的超平面；
- “超平面”在二维里是直线，在三维里是平面，在 \(n\) 维里是 \(n-1\) 维平面。

讲义证明：

\[
\mathbb{R}^n=\operatorname{span}\{w\}\oplus \operatorname{span}\{w\}^{\perp}.
\]

意思是任意向量 \(x\) 都可以唯一分解成两部分：

\[
x=\alpha w+y,
\]

其中：

\[
y^Tw=0.
\]

这里 \(\alpha w\) 是沿 \(w\) 方向的部分，\(y\) 是垂直于 \(w\) 的部分。

接着计算：

\[
Hx=(I-2ww^T)(\alpha w+y).
\]

展开：

\[
Hx=\alpha w+y-2w(w^T(\alpha w+y)).
\]

因为

\[
w^Tw=1,\qquad w^Ty=0,
\]

所以：

\[
w^T(\alpha w+y)=\alpha.
\]

于是：

\[
Hx=\alpha w+y-2\alpha w=y-\alpha w.
\]

也就是说，垂直于 \(w\) 的部分 \(y\) 不变，沿 \(w\) 的部分 \(\alpha w\) 变成 \(-\alpha w\)。这正是关于超平面的反射。

因此 Householder 变换也叫初等反射变换或镜像变换。

---

## 3. 第 2-3 页：如何构造 Householder，把向量变成 \(\alpha e_1\)

## 3.1 定理

讲义写：

设 \(x\in\mathbb{R}^n\)，\(x\ne0\)。则存在 \(w\in\mathbb{R}^n\)，\(\|w\|_2=1\)，使得

\[
H=I-2ww^T
\]

满足

\[
Hx=\alpha e_1,
\]

其中

\[
\alpha=\pm \|x\|_2.
\]

这里 \(e_1\) 是第一个标准单位向量：

\[
e_1=(1,0,\ldots,0)^T.
\]

这条定理的意思非常重要：任意非零向量 \(x\)，都可以通过一个 Householder 反射，变成只有第一个分量非零的向量。

例如：

\[
x=
\begin{pmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{pmatrix}
\quad\longrightarrow\quad
Hx=
\begin{pmatrix}
\alpha\\
0\\
\vdots\\
0
\end{pmatrix}.
\]

这就是“消元”的核心。

## 3.2 为什么 \(\alpha=\pm\|x\|_2\)

因为 \(H\) 是正交矩阵，所以保持 2-范数：

\[
\|Hx\|_2=\|x\|_2.
\]

如果 \(Hx=\alpha e_1\)，那么

\[
\|Hx\|_2=\|\alpha e_1\|_2=|\alpha|.
\]

所以：

\[
|\alpha|=\|x\|_2.
\]

因此：

\[
\alpha=\pm\|x\|_2.
\]

讲义中用代数方式展开，结论一样。

## 3.3 构造 \(w\) 的基本想法

如果希望

\[
Hx=\alpha e_1,
\]

则 \(x\) 和 \(\alpha e_1\) 应该是关于某个超平面的镜像。镜面法向量就是 \(w\)。

反射中，被反射点和反射后点的连线方向垂直于镜面，所以 \(w\) 应该和

\[
x-\alpha e_1
\]

同方向。

因此可取：

\[
w=\frac{x-\alpha e_1}{\|x-\alpha e_1\|_2}.
\]

这是讲义第 2 页底部写的公式。

## 3.4 讲义中的代数推导

讲义写：

\[
Hx=(I-2ww^T)x=x-2w(w^Tx)=\alpha e_1.
\]

移项得到：

\[
x-\alpha e_1=2(w^Tx)w.
\]

这说明 \(x-\alpha e_1\) 确实平行于 \(w\)。

再结合

\[
x-\alpha e_1=\|x-\alpha e_1\|_2 w,
\]

可以推出讲义中的关系。

把 \(w\) 的表达式代入，可以推出：

\[
\|x-\alpha e_1\|_2^2=2(x-\alpha e_1)^Tx.
\]

设

\[
x=(x_1,x_2,\ldots,x_n)^T.
\]

左边：

\[
\|x-\alpha e_1\|_2^2
=(x_1-\alpha)^2+x_2^2+\cdots+x_n^2.
\]

右边：

\[
2(x-\alpha e_1)^Tx
=2\left((x_1-\alpha)x_1+x_2^2+\cdots+x_n^2\right).
\]

整理后得到：

\[
\|x\|_2^2-2\alpha x_1+\alpha^2
=2\|x\|_2^2-2\alpha x_1.
\]

两边消去 \(-2\alpha x_1\)：

\[
\alpha^2=\|x\|_2^2.
\]

所以：

\[
\alpha=\pm\|x\|_2.
\]

讲义红字提醒：通常取

\[
\alpha=\|x\|_2.
\]

---

## 4. 第 3 页：Householder 的实际构造步骤与数值稳定性

## 4.1 构造步骤 1：先取 \(v=x-\alpha e_1\)

讲义写：

\[
v=x-\alpha e_1,\qquad \alpha=\|x\|_2.
\]

设

\[
v=(v_1,v_2,\ldots,v_n)^T.
\]

那么：

\[
v_1=x_1-\alpha=x_1-\|x\|_2.
\]

其余分量不变：

\[
v_i=x_i,\qquad i=2,\ldots,n.
\]

## 4.2 为什么直接算 \(v_1=x_1-\|x\|_2\) 可能不稳定

如果 \(x_1>0\)，并且 \(x_2,\ldots,x_n\) 很小，那么

\[
x_1\approx \|x\|_2.
\]

于是

\[
x_1-\|x\|_2
\]

是在两个非常接近的数之间做减法，会造成有效数字大量丢失。这叫相消误差。

讲义用恒等变形：

\[
v_1=x_1-\|x\|_2
=\frac{x_1^2-\|x\|_2^2}{x_1+\|x\|_2}.
\]

而

\[
\|x\|_2^2=x_1^2+x_2^2+\cdots+x_n^2.
\]

所以：

\[
x_1^2-\|x\|_2^2
=-(x_2^2+\cdots+x_n^2).
\]

因此：

\[
v_1=-\frac{x_2^2+\cdots+x_n^2}{x_1+\|x\|_2}.
\]

这就是讲义标记的第二种公式。

## 4.3 何时用哪个公式

讲义写：

- 若 \(x_1>0\)，用变形后的公式；
- 若 \(x_1\le0\)，用直接公式。

原因：

- \(x_1>0\) 时，\(x_1\) 和 \(\|x\|_2\) 可能接近，直接减法容易相消；
- \(x_1\le0\) 时，\(x_1-\|x\|_2\) 是两个同号方向的量相加，不容易相消。

## 4.4 构造步骤 2：归一化

讲义写：

\[
w=\frac{v}{\|v\|_2}.
\]

这一步是为了让

\[
\|w\|_2=1.
\]

因为 Householder 定义要求 \(w\) 是单位向量。

## 4.5 构造步骤 3：写出 \(H\)

讲义写：

\[
H=I-2ww^T
=I-2\frac{vv^T}{\|v\|_2^2}.
\]

因为

\[
w=\frac{v}{\|v\|_2},
\]

所以：

\[
ww^T=\frac{vv^T}{v^Tv}.
\]

讲义又写：

\[
H=I-\beta vv^T,\qquad \beta=\frac{2}{v^Tv}.
\]

这在程序实现中非常重要：不一定要显式算 \(w\)，只保存 \(v\) 和 \(\beta\)，需要乘 \(H\) 时用

\[
Hy=y-\beta v(v^Ty).
\]

## 4.6 讲义红字备注

讲义红字写了三点。

第一点：不用求 \(w\)，只需求 \(v\) 和 \(\beta\)。

这是因为实际计算 \(Hy\) 时：

\[
Hy=(I-\beta vv^T)y=y-\beta v(v^Ty).
\]

这个公式只需要 \(v\) 和 \(\beta\)。

第二点：当 \(x\) 分量很大时，计算中可能溢出。

例如计算 \(\|x\|_2\) 或 \(v^Tv\) 时，需要平方。如果某些分量特别大，平方可能超过浮点数表示范围。讲义建议用

\[
\frac{x}{\|x\|_\infty}
\]

代替 \(x\) 做缩放，避免溢出。

第三点：如果 \(v^Tv\) 变成 0，要特殊处理。

因为

\[
\beta=\frac{2}{v^Tv},
\]

如果 \(v=0\)，分母就是 0。通常这表示向量已经是目标形式，不需要做反射。

---

## 5. 第 4 页：Givens 变换

## 5.1 引入 Givens 的原因

讲义先写 Householder 的备注：

- 可以把一个向量中若干元素消成 0；
- 实际计算中不需要形成完整的 \(H\)；
- 数值性态良好，舍入误差是 \(O(u)\) 级别。

然后进入 Givens 变换。

讲义红字写：

“思想：选择性地化一些元素为 0。”

Householder 是“一次消一串”，Givens 是“一次消一个指定元素”。如果矩阵很稀疏，Givens 常常更方便，因为它只影响两行或两列。

## 5.2 Givens 矩阵的定义

讲义画了一个单位矩阵，只在第 \(i\) 行、第 \(k\) 行以及第 \(i\) 列、第 \(k\) 列交叉的位置改成：

\[
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}.
\]

其中：

\[
c=\cos\theta,\qquad s=\sin\theta.
\]

这就是 Givens 旋转矩阵，记作：

\[
G(i,k,\theta).
\]

讲义右侧写了紧凑表达式：

\[
G(i,k,\theta)
=I+s(e_ie_k^T-e_ke_i^T)
+(c-1)(e_ie_i^T+e_ke_k^T).
\]

这个公式的作用是精准描述：除了 \(i,k\) 两个坐标外，其他坐标都不动。

## 5.3 为什么 Givens 是正交矩阵

二维旋转矩阵

\[
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}
\]

满足：

\[
c^2+s^2=1.
\]

所以它是正交矩阵。

Givens 矩阵只是在 \((i,k)\) 平面上做这个二维旋转，其余方向保持不变，因此整体也是正交矩阵。

## 5.4 Givens 对向量的作用

讲义写：

对任意 \(x\in\mathbb{R}^n\)，令

\[
y=G(i,k,\theta)x.
\]

则：

\[
y_i=cx_i+sx_k,
\]

\[
y_k=-sx_i+cx_k,
\]

\[
y_j=x_j,\qquad j\ne i,k.
\]

也就是说，只有第 \(i\) 和第 \(k\) 个分量发生变化，其他分量都不变。

## 5.5 如何选择 \(c,s\) 把 \(x_k\) 消成 0

讲义写：

若取

\[
c=\frac{x_i}{\sqrt{x_i^2+x_k^2}},
\qquad
s=\frac{x_k}{\sqrt{x_i^2+x_k^2}},
\]

则：

\[
y_i=\sqrt{x_i^2+x_k^2},\qquad y_k=0.
\]

验证：

\[
y_k=-sx_i+cx_k
=-\frac{x_k}{r}x_i+\frac{x_i}{r}x_k=0,
\]

其中

\[
r=\sqrt{x_i^2+x_k^2}.
\]

这就是 Givens 消元。

## 5.6 几何意义

讲义写：

\(G(i,k,\theta)\) 是在 \((i,k)\) 平面内将 \(x\) 按顺时针方向旋转 \(\theta\) 度。

所以 Givens 变换又称为平面旋转变换。

---

## 6. 第 4-5 页：Givens 的稳定计算公式

## 6.1 基本问题

讲义写：

\[
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}
\begin{pmatrix}
a\\
b
\end{pmatrix}
=
\begin{pmatrix}
r\\
0
\end{pmatrix}.
\]

展开：

\[
ca+sb=r,
\]

\[
-sa+cb=0.
\]

理想上可以取：

\[
c=\frac{a}{\sqrt{a^2+b^2}},
\qquad
s=\frac{b}{\sqrt{a^2+b^2}}.
\]

但如果 \(a,b\) 很大，直接算 \(a^2+b^2\) 可能溢出。

## 6.2 稳定算法

讲义给了两种情况。

第一种：

\[
|b|>|a|.
\]

令

\[
\tau=\frac{a}{b}.
\]

此时 \(|\tau|<1\)，不会太大。

然后：

\[
s=\frac{1}{\sqrt{1+\tau^2}},
\qquad
c=s\tau.
\]

第二种：

\[
|a|\ge |b|.
\]

令

\[
\tau=\frac{b}{a}.
\]

此时 \(|\tau|\le1\)。

然后：

\[
c=\frac{1}{\sqrt{1+\tau^2}},
\qquad
s=c\tau.
\]

这种写法避免了直接计算 \(a^2+b^2\)，所以更稳定。

## 6.3 两个备注

讲义红字写：

第一，\(r\) 不一定为正。

因为这里的 \(c,s\) 取法主要是为了稳定和消元，不强制 \(r=\sqrt{a^2+b^2}\)。实际得到的 \(r\) 可能带有 \(a\) 或 \(b\) 的符号。

第二，数值性态良好，是 \(O(u)\) 级别。

这里 \(u\) 是机器精度。意思是 Givens 旋转的舍入误差可以控制在很小的数量级。

---

## 7. 第 5 页：正交化方法的总思想

## 7.1 从原问题变成正交变换后的问题

讲义写：

\[
\min_{x\in\mathbb{R}^n}\|b-Ax\|_2
=
\min_{x\in\mathbb{R}^n}\|Q^Tb-Q^TAx\|_2.
\]

这里用的是正交矩阵保持 2-范数。

为什么写 \(Q^T\) 而不是 \(Q\)？因为如果 \(Q\) 正交，\(Q^T\) 也正交。并且 QR 分解通常写成：

\[
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

于是左乘 \(Q^T\) 就得到：

\[
Q^TA=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

## 7.2 正交化方法的目标

讲义红字写：

选择适当的 \(m\) 阶正交阵 \(Q\)，使得原来的最小二乘问题变成容易求解的最小二乘问题。

也就是希望把 \(A\) 变成：

\[
\begin{pmatrix}
R\\
0
\end{pmatrix},
\]

其中 \(R\) 是上三角矩阵。

如果成功，问题就从“最小二乘”变成“解上三角线性方程”。

---

## 8. 第 5-6 页：QR 分解定理

## 8.1 定理陈述

讲义写：

设

\[
A\in\mathbb{R}^{m\times n}.
\]

则 \(A\) 有 QR 分解：

\[
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

其中：

- \(Q\in\mathbb{R}^{m\times m}\) 是正交矩阵；
- \(R\in\mathbb{R}^{n\times n}\) 是具有非负对角元的上三角矩阵；
- \(0\) 是 \((m-n)\times n\) 的零矩阵。

讲义还写：

当 \(m=n\) 且 \(A\) 非奇异时，上述分解唯一。

非奇异表示 \(A\) 可逆。

## 8.2 为什么 \(Q\) 是 \(m\times m\)

因为这里使用的是完全 QR 分解。

如果 \(A\) 是 \(m\times n\)，\(m\ge n\)，则：

\[
Q\in\mathbb{R}^{m\times m},
\qquad
\begin{pmatrix}
R\\
0
\end{pmatrix}\in\mathbb{R}^{m\times n}.
\]

二者相乘后仍然是 \(m\times n\)。

## 8.3 存在性证明：归纳法

讲义写：

“证明：对 \(n\) 用数学归纳法。”

这里 \(n\) 是列数。证明思路是：先证明一列矩阵可以分解，再假设 \(n-1\) 列可以分解，推出 \(n\) 列也可以分解。

### 8.3.1 当 \(n=1\)

此时 \(A\) 只有一列，可以看成一个向量。

根据 Householder 定理，存在 Householder 变换 \(H\)，使得：

\[
HA=\alpha e_1.
\]

也就是：

\[
HA=
\begin{pmatrix}
\alpha\\
0\\
\vdots\\
0
\end{pmatrix},
\qquad
\alpha=\|A\|_2.
\]

因为 Householder 矩阵满足 \(H^T=H\) 且 \(H^{-1}=H\)，所以：

\[
A=H
\begin{pmatrix}
\alpha\\
0\\
\vdots\\
0
\end{pmatrix}.
\]

这就是 \(n=1\) 的 QR 分解。

### 8.3.2 归纳假设

讲义写：

假设对 \(n-1\) 都成立。

把 \(A\) 分块：

\[
A=(A_1,v),
\]

其中：

\[
A_1\in\mathbb{R}^{m\times(n-1)},
\qquad
v\in\mathbb{R}^m.
\]

根据归纳假设，\(A_1\) 有 QR 分解：

\[
A_1=Q_1
\begin{pmatrix}
R_1\\
0
\end{pmatrix}.
\]

其中 \(Q_1\) 正交，\(R_1\) 是 \((n-1)\times(n-1)\) 上三角矩阵。

### 8.3.3 对整个 \(A\) 左乘 \(Q_1^T\)

讲义写：

\[
Q_1^TA
=
\left[
Q_1^TA_1,\ Q_1^Tv
\right]
=
\left[
\begin{pmatrix}
R_1\\
0
\end{pmatrix},
y
\right].
\]

设：

\[
y=Q_1^Tv
=
(y_1,y_2,\ldots,y_{n-1},\hat y_n,\ldots,\hat y_m)^T.
\]

前 \(n-1\) 个分量放在已有的上三角结构旁边，不需要动。后面的尾部

\[
(\hat y_n,\ldots,\hat y_m)^T
\]

需要被消成只有第一个分量非零。

### 8.3.4 对尾部再做一次 Householder

构造

\[
\widetilde H_1\in
\mathbb{R}^{(m-n+1)\times(m-n+1)}
\]

使得：

\[
\widetilde H_1
\begin{pmatrix}
\hat y_n\\
\vdots\\
\hat y_m
\end{pmatrix}
=
\begin{pmatrix}
\alpha_1\\
0\\
\vdots\\
0
\end{pmatrix},
\qquad
\alpha_1>0.
\]

然后把它嵌入到 \(m\times m\) 矩阵：

\[
H_1=
\begin{pmatrix}
I_{n-1}&0\\
0&\widetilde H_1
\end{pmatrix}.
\]

这样 \(H_1\) 只作用在后面的尾部，不破坏前面已经形成的上三角结构。

于是：

\[
H_1Q_1^TA
=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

因为 \(H_1\) 和 \(Q_1\) 都正交，所以它们的乘积也是正交。

最终得到：

\[
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

这证明了 QR 分解存在。

## 8.4 唯一性证明

讲义写：

当 \(m=n\) 且 \(A\) 非奇异时，若 QR 分解不唯一，则：

\[
A=QR=\widetilde Q\widetilde R.
\]

其中：

- \(Q,\widetilde Q\) 都是正交矩阵；
- \(R,\widetilde R\) 都是对角元为正的上三角矩阵。

由

\[
QR=\widetilde Q\widetilde R
\]

推出：

\[
\widetilde Q^TQ=\widetilde R R^{-1}.
\]

设：

\[
B=\widetilde Q^TQ=\widetilde R R^{-1}.
\]

左边说明 \(B\) 是正交矩阵，因为正交矩阵乘正交矩阵仍正交。

右边说明 \(B\) 是上三角矩阵，因为上三角矩阵的逆仍是上三角，上三角乘上三角仍是上三角。

所以 \(B\) 同时是正交矩阵和上三角矩阵。

一个上三角正交矩阵只能是对角矩阵，且对角元素只能是 \(\pm1\)。又因为 \(R,\widetilde R\) 的对角元都取正，所以 \(B\) 的对角元为正，只能全是 \(1\)。

因此：

\[
B=I.
\]

于是：

\[
\widetilde Q^TQ=I,
\]

所以：

\[
Q=\widetilde Q.
\]

再代回：

\[
QR=\widetilde Q\widetilde R
\]

得到：

\[
R=\widetilde R.
\]

唯一性得证。

---

## 9. 第 6-7 页：用 QR 分解求解最小二乘

## 9.1 问题条件

讲义写：

\[
A\in\mathbb{R}^{m\times n},
\qquad
\operatorname{rank}(A)=n,
\qquad
b\in\mathbb{R}^m.
\]

要求：

\[
\min_{x\in\mathbb{R}^n}\|b-Ax\|_2.
\]

\(\operatorname{rank}(A)=n\) 表示 \(A\) 满列秩。也就是 \(A\) 的 \(n\) 列线性无关。

这保证 QR 分解里的 \(R\) 是非奇异上三角矩阵，因此 \(Rx=C_1\) 有唯一解。

## 9.2 利用 QR 分解

根据 QR 分解，存在正交矩阵 \(Q\)，使得：

\[
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

其中 \(R\in\mathbb{R}^{n\times n}\) 是上三角矩阵。

对残差做正交变换：

\[
\|Ax-b\|_2^2
=
\|Q^TAx-Q^Tb\|_2^2.
\]

因为 \(Q^TQ=I\)：

\[
Q^TA=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

所以：

\[
\|Ax-b\|_2^2
=
\left\|
\begin{pmatrix}
R\\
0
\end{pmatrix}x
-Q^Tb
\right\|_2^2.
\]

## 9.3 把 \(Q\) 分块

讲义写：

\[
Q=[Q_1,Q_2],
\]

其中：

\[
Q_1\in\mathbb{R}^{m\times n},
\qquad
Q_2\in\mathbb{R}^{m\times(m-n)}.
\]

也就是 \(Q_1\) 是 \(Q\) 的前 \(n\) 列，\(Q_2\) 是剩余列。

然后：

\[
Q^Tb=
\begin{pmatrix}
Q_1^T\\
Q_2^T
\end{pmatrix}b
=
\begin{pmatrix}
C_1\\
C_2
\end{pmatrix},
\]

其中：

\[
C_1\in\mathbb{R}^n,\qquad C_2\in\mathbb{R}^{m-n}.
\]

## 9.4 残差分解

代入后：

\[
\left\|
\begin{pmatrix}
R\\
0
\end{pmatrix}x
-
\begin{pmatrix}
C_1\\
C_2
\end{pmatrix}
\right\|_2^2
=
\left\|
\begin{pmatrix}
Rx-C_1\\
-C_2
\end{pmatrix}
\right\|_2^2.
\]

由于向量上下两部分的平方和相加：

\[
=\|Rx-C_1\|_2^2+\|C_2\|_2^2.
\]

第二项 \(\|C_2\|_2^2\) 与 \(x\) 无关。

因此要最小化整个式子，只需要让第一项最小：

\[
\|Rx-C_1\|_2^2.
\]

因为 \(R\) 非奇异，所以可以直接令：

\[
Rx=C_1.
\]

此时第一项为 0，达到最小。

## 9.5 基本步骤

讲义列出三个步骤：

1. 计算 \(A\) 的 QR 分解，这是关键步骤。
2. 计算 \(C_1=Q_1^Tb\)。
3. 解上三角方程组

\[
Rx=C_1
\]

得到最小二乘解 \(x\)。

这就是正交化方法求最小二乘的完整框架。

---

## 10. 第 7-8 页：用 Householder 实现 QR 分解

## 10.1 第一步：消第一列

讲义画：

\[
A=
\begin{pmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{pmatrix}.
\]

用 Householder 矩阵 \(H_1\) 作用在 \(A\) 左边：

\[
H_1A.
\]

选择 \(H_1\)，让第一列变成：

\[
\begin{pmatrix}
\alpha_1\\
0\\
\vdots\\
0
\end{pmatrix}.
\]

矩阵形状变成：

\[
\begin{pmatrix}
\alpha_1&*&\cdots&*\\
0&*&\cdots&*\\
\vdots&\vdots&&\vdots\\
0&*&\cdots&*
\end{pmatrix}.
\]

这一步类似消元，但它是正交变换。

## 10.2 第二步：消第二列的下方元素

第一列已经完成，不能破坏它。

所以第二步只对右下角子矩阵做 Householder。

讲义写：

\[
H_2=
\begin{pmatrix}
1&0\\
0&\widetilde H_2
\end{pmatrix}.
\]

这里 \(\widetilde H_2\) 作用在从第 2 行到第 \(m\) 行的部分。

左乘 \(H_2\) 后，第二列第 3 行到第 \(m\) 行被消成 0，同时第一列不变。

## 10.3 重复下去

继续第 3 步、第 4 步，直到第 \(n\) 列。

讲义写：

对 \(A\) 依次进行 \(n\) 次 Householder 变换：

\[
A\longrightarrow
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

并且 \(H_1,H_2,\ldots,H_n\) 都是正交矩阵。

因为 Householder 矩阵对称：

\[
H_i^T=H_i.
\]

所以：

\[
H_nH_{n-1}\cdots H_2H_1A
=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

两边左乘逆矩阵。由于 \(H_i^{-1}=H_i\)，得到：

\[
A=H_1H_2\cdots H_n
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

因此：

\[
Q=H_1H_2\cdots H_n.
\]

这就是用 Householder 做 QR 分解。

---

## 11. 第 8 页：QR 分解中的存储问题

## 11.1 为什么不显式存 \(Q\)

讲义写：

\(A\) 分解完成后本来应存 \(Q,R\)，但并不将 \(Q\) 算出，而是存这些 Householder 变换。

原因是：

- \(Q\) 是 \(m\times m\)，可能很大；
- 构造完整 \(Q\) 需要额外计算；
- 解最小二乘时通常只需要计算 \(Q^Tb\)，可以用 Householder 向量逐步作用在 \(b\) 上，而不用形成 \(Q\)。

## 11.2 每个 Householder 只需存一个向量

每个 Householder 变换形如：

\[
H_k=I-\beta_k v_kv_k^T.
\]

所以只要存 \(v_k\) 和 \(\beta_k\)，就能恢复它对任意向量的作用：

\[
H_ky=y-\beta_kv_k(v_k^Ty).
\]

讲义写：

“对每个 \(H_k\)，只需存 \(v\)。”

严格实现时通常还要存 \(\beta_k\)，或者用某种规范化让 \(\beta_k\) 可以由 \(v_k\) 恢复。

## 11.3 \(m=4,n=3\) 的存储例子

讲义以 \(m=4,n=3\) 为例。

分解后，\(A\) 的存储区域可以被复用。

原来 \(A\) 有 4 行 3 列。QR 后：

- 上三角部分存 \(R\)；
- 下三角部分存 Householder 向量的后续分量。

讲义画出的结构可以理解为：

\[
\begin{pmatrix}
r_{11}&r_{12}&r_{13}\\
v_2^{(1)}&r_{22}&r_{23}\\
v_3^{(1)}&v_3^{(2)}&r_{33}\\
v_4^{(1)}&v_4^{(2)}&v_4^{(3)}
\end{pmatrix}.
\]

其中：

- 第一列对角线以上和对角线位置的 \(r_{11}\) 是 \(R\) 的内容；
- 第一列对角线以下的 \(v_2^{(1)},v_3^{(1)},v_4^{(1)}\) 存第一个 Householder 向量的信息；
- 第二列对角线以下的 \(v_3^{(2)},v_4^{(2)}\) 存第二个 Householder 向量的信息；
- 第三列对角线以下的 \(v_4^{(3)}\) 存第三个 Householder 向量的信息。

通常为了节省空间，可以把每个 Householder 向量的首分量规范化为 1，不再显式存它。

## 11.4 三个 Householder 的形式

讲义写：

第一步，对第 1 列：

\[
v^{(1)}=
\begin{pmatrix}
1\\
v_2^{(1)}\\
v_3^{(1)}\\
v_4^{(1)}
\end{pmatrix},
\qquad
H_1=I-2\frac{v^{(1)}(v^{(1)})^T}{(v^{(1)})^Tv^{(1)}}.
\]

第二步，对第 2 列的尾部：

\[
v^{(2)}=
\begin{pmatrix}
1\\
v_3^{(2)}\\
v_4^{(2)}
\end{pmatrix}.
\]

它生成小的 \(\widetilde H_2\)，再嵌入：

\[
H_2=
\begin{pmatrix}
1&0\\
0&\widetilde H_2
\end{pmatrix}.
\]

第三步，对第 3 列的尾部：

\[
v^{(3)}=
\begin{pmatrix}
1\\
v_4^{(3)}
\end{pmatrix}.
\]

它生成 \(\widetilde H_3\)，再嵌入：

\[
H_3=
\begin{pmatrix}
I_2&0\\
0&\widetilde H_3
\end{pmatrix}.
\]

最后：

\[
Q=H_1H_2H_3.
\]

这就是讲义最后一页的存储思想。

---

## 12. 初学者最容易混淆的点

## 12.1 \(Q\) 和 \(Q^T\) 到底谁乘在左边

QR 分解写成：

\[
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

因此：

\[
Q^TA=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

在算法里，我们常常通过一系列 Householder 左乘把 \(A\) 变成 \([R;0]\)：

\[
H_n\cdots H_1A=
\begin{pmatrix}
R\\
0
\end{pmatrix}.
\]

所以：

\[
Q^T=H_n\cdots H_1,
\qquad
Q=H_1\cdots H_n.
\]

注意顺序会反过来。

## 12.2 Householder 和 Givens 的区别

Householder：

- 一次消掉一个向量尾部的多个分量；
- 适合稠密矩阵；
- QR 分解常用它。

Givens：

- 一次消掉一个指定分量；
- 只影响两个坐标；
- 适合稀疏矩阵或需要局部更新的场景。

## 12.3 为什么 QR 比正规方程稳定

正规方程要解：

\[
A^TAx=A^Tb.
\]

而条件数满足：

\[
\kappa(A^TA)=\kappa(A)^2.
\]

也就是说，病态程度被平方放大。

QR 方法只使用正交变换。正交变换保持长度，不放大 2-范数误差，所以数值稳定性更好。

## 12.4 最小二乘解为什么只需要解 \(Rx=C_1\)

因为 QR 后：

\[
\|Ax-b\|_2^2
=
\|Rx-C_1\|_2^2+\|C_2\|_2^2.
\]

第二项与 \(x\) 无关，不能通过选择 \(x\) 改变。

因此只要让第一项最小。若 \(A\) 满列秩，则 \(R\) 可逆，可以令：

\[
Rx=C_1.
\]

这就是最小二乘解。

---

## 13. 一句话总结整讲

这讲的核心是：

用正交矩阵保持残差范数不变，再通过 Householder 或 Givens 把 \(A\) 变成上三角形式；于是最小二乘问题从

\[
\min_x\|b-Ax\|_2
\]

变成解一个稳定的上三角方程

\[
Rx=Q_1^Tb.
\]

如果你只记一个算法流程，就是：

1. 用 Householder 或 Givens 求 \(A=Q[R;0]\)；
2. 算 \(C_1=Q_1^Tb\)；
3. 解 \(Rx=C_1\)；
4. 得到最小二乘解。
