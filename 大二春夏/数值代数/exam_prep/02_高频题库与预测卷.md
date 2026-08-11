# 数值代数高频题库与预测卷

## 一、高频题库

### 1. 范数证明

**题型**：证明 `||A||_F` 是矩阵范数，或证明 `||A||_X=||X^{-1}AX||_2` 是矩阵范数。  
**证据**：历年卷 2022-2025；Homework4；总复习。

**答题骨架**：

1. 先证非负、齐次；
2. 再证次乘性；
3. `||A||_F` 用 `tr(A^TA)` 和 `U^TU=I`；
4. `||A||_X` 直接套 2-范数的性质。

---

### 2. LU / PLU / 全主元

**题型**：给 3 阶矩阵，求 `LU`、`PLU`，并解 `Ax=b`。  
**证据**：历年卷 2021、2025；Homework2。

**标准例题**：

\[
A=\begin{pmatrix}1&4&7\\2&5&8\\3&6&10\end{pmatrix},\quad b=(1,1,1)^T.
\]

**答案**：

\[
L=\begin{pmatrix}1&0&0\\2&1&0\\3&2&1\end{pmatrix},\quad
U=\begin{pmatrix}1&4&7\\0&-3&-6\\0&0&1\end{pmatrix},\quad
x=(-1/3,1/3,0)^T.
\]

一种列主元分解：

\[
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\ 
L=\begin{pmatrix}1&0&0\\1/3&1&0\\2/3&1/2&1\end{pmatrix},\ 
U=\begin{pmatrix}3&6&10\\0&2&11/3\\0&0&-1/2\end{pmatrix}.
\]

**要点**：

- 普通 LU 可能失败；
- 选主元是为了控制增长因子和舍入误差；
- `PAQ=LU` 只在全主元题里出现。

---

### 3. 正定性与平方根法

**题型**：证明 SPD，再做 Cholesky / `LDL^T`。  
**证据**：历年卷 2020、2022、2025；Homework3。

**标准例题**：

\[
A=\begin{pmatrix}
4&-2&4&2\\
-2&10&-2&-7\\
4&-2&8&4\\
2&-7&4&7
\end{pmatrix},\quad
b=(8,2,16,6)^T.
\]

**答案**：

\[
L=\begin{pmatrix}
2&0&0&0\\
-1&3&0&0\\
2&0&2&0\\
1&-2&1&1
\end{pmatrix},
\quad
LL^T=A,
\quad
x=(1,2,1,2)^T.
\]

**常考问法**：

- 说明为什么 `A` 正定；
- 写出 Cholesky 递推；
- 说明 `LDL^T` 为什么比平方根法更稳妥。

---

### 4. 最小二乘与正则方程

**题型**：写正则方程并用平方根法解。  
**证据**：历年卷 2022、2025；Homework7。

**标准例题**：

\[
A=\begin{pmatrix}0&-1\\3&2\\0&-2\end{pmatrix},\quad
b=\begin{pmatrix}-1/3\\5/3\\-2/3\end{pmatrix}.
\]

**答案**：

\[
A^TA=\begin{pmatrix}9&6\\6&9\end{pmatrix},\quad
A^Tb=\begin{pmatrix}5\\5\end{pmatrix},\quad
x=(1/3,1/3)^T.
\]

**证明套路**：

\[
A^T(Ax-b)=0 \iff A^TAx=A^Tb.
\]

---

### 5. Householder 与 Givens

**题型**：构造 Householder，或求 Givens 的 `c,s,beta`。  
**证据**：历年卷 2020、2024、2025；Homework8。

**标准例题 1**：

\[
x=(3,1,6,4,2,2)^T.
\]

把尾部子向量 `(1,2,2)^T` 变成 `(3,0,0)^T`，一组可用的 3 维 Householder 为

\[
H=\begin{pmatrix}
1/3&2/3&2/3\\
2/3&1/3&-2/3\\
2/3&-2/3&1/3
\end{pmatrix}.
\]

**标准例题 2**：

\[
\begin{pmatrix}c&s\\-s&c\end{pmatrix}
\begin{pmatrix}7\\-1\end{pmatrix}
=\begin{pmatrix}\beta\\\beta\end{pmatrix}.
\]

可取

\[
c=3/5,\quad s=-4/5,\quad \beta=5
\]

或等价符号解。

**要点**：

- Householder 是“一次消掉一串”；
- Givens 是“一次消掉一个”；
- `H` 正交对称，`G` 正交。

---

### 6. Jacobi / Gauss-Seidel / SOR

**题型**：写迭代矩阵，判收敛，求最优松弛因子。  
**证据**：历年卷 2020、2022、2024、2025；Homework10。

**标准模板**：

\[
A=D-L-U.
\]

Jacobi：

\[
B_J=D^{-1}(L+U).
\]

G-S：

\[
B_{GS}=(D-L)^{-1}U.
\]

SOR：

\[
B_\omega=(D-\omega L)^{-1}[(1-\omega)D+\omega U].
\]

**参数矩阵**：

\[
A=\begin{pmatrix}1&0&a\\0&1&0\\a&0&1\end{pmatrix}
\]

答案：

- 正定当且仅当 `|a|<1`
- Jacobi 收敛当且仅当 `|a|<1`
- G-S 收敛当且仅当 `|a|<1`

**两个 3 阶高频矩阵**：

\[
A_1=\begin{pmatrix}2&1&1\\1&-1&-1\\1&1&-2\end{pmatrix},\quad
A_2=\begin{pmatrix}1&2&-2\\1&1&-1\\2&-2&1\end{pmatrix}
\]

对应 Jacobi 谱半径：

\[
\rho(B_1)=\sqrt5/2>1,\quad \rho(B_2)=0.
\]

所以 `A1` 不收敛，`A2` 收敛。

---

### 7. 共轭梯度法

**题型**：证明共轭向量线性无关、写 `A^{-1}` 展开式、手算 CG。  
**证据**：历年卷 2020；Homework11；总复习。

**必须会写**：

\[
\alpha_k=\frac{r_k^Tr_k}{p_k^TAp_k},\quad
\beta_k=\frac{r_{k+1}^Tr_{k+1}}{r_k^Tr_k},\quad
p_{k+1}=r_{k+1}+\beta_k p_k.
\]

**证明关键词**：

- `A` 对称正定；
- `p_i^T A p_j = 0`；
- 左乘 `p_j^T A` 直接锁死系数；
- `x_k` 在 Krylov 子空间里。

---

### 8. Hessenberg / QR / Schur / SVD

**题型**：Householder 化上 Hessenberg，证明 QR 迭代保结构，写 Schur 分解，或考 SVD/广义逆。  
**证据**：历年卷 2023；Homework13；参考书 197-199。

**答题骨架**：

- 上 Hessenberg：只对第 `k` 列下面部分做 Householder；
- QR 迭代：`A_{k+1}=Q_k^T A_k Q_k`；
- Schur：实数域用实 Schur，复数域用上三角 Schur；
- SVD：$A=U\Sigma V^T$，$A^+=V\Sigma^+U^T$；
- `AA^+` 是到列空间的正交投影。

---

## 二、今年最可能的预测卷

### 题 1

证明 `||A||_X=||X^{-1}AX||_2` 是矩阵范数。  
**考点**：范数定义、相似变换、次乘性。  
**关键结论**：直接借 `2`-范数的四条性质。

### 题 2

\[
A=\begin{pmatrix}1&4&7\\2&5&8\\3&6&10\end{pmatrix},\quad
b=(1,1,1)^T.
\]

求 `LU`、`PLU`，并解 `Ax=b`。  
**关键结论**：`x=(-1/3,1/3,0)^T`。

### 题 3

\[
A=\begin{pmatrix}0&-1\\3&2\\0&-2\end{pmatrix},\quad
b=\begin{pmatrix}-1/3\\5/3\\-2/3\end{pmatrix}.
\]

1. 写出正则方程；  
2. 用平方根法解。  
**关键结论**：`A^TA=[[9,6],[6,9]]`，`x=(1/3,1/3)^T`。

### 题 4

\[
x=(3,1,6,4,2,2)^T,\qquad
\begin{pmatrix}c&s\\-s&c\end{pmatrix}\begin{pmatrix}7\\-1\end{pmatrix}
=\begin{pmatrix}\beta\\\beta\end{pmatrix}.
\]

分别求 Householder 和 Givens。  
**关键结论**：Householder 子块可取使 `(1,2,2)^T \mapsto (3,0,0)^T`；Givens 可取 `c=3/5, s=-4/5, beta=5`。

### 题 5

\[
A=\begin{pmatrix}1&0&a\\0&1&0\\a&0&1\end{pmatrix}.
\]

1. 何时正定？  
2. 何时 Jacobi 收敛？  
3. 何时 G-S 收敛？  
**关键结论**：三问都等价于 `|a|<1`。

### 题 6

给出两个 3 阶矩阵，分别写 Jacobi 迭代矩阵并判断收敛性。  
**关键结论**：

\[
\rho(B_1)=\sqrt5/2>1,\quad \rho(B_2)=0.
\]

### 题 7

证明 `p_1,...,p_n` 是 A-共轭向量系，则线性无关，并推出

\[
A^{-1}=\sum_{k=1}^n\frac{p_kp_k^T}{p_k^TAp_k}.
\]

### 题 8

证明 Householder 变换可将一般矩阵化为上 Hessenberg 矩阵，并说明 QR 迭代为何保持 Hessenberg 结构。  
**关键结论**：每步只作用在活动子块上，结构不被破坏。

### 题 9

写出 Schur 分解定理，并说明其与 QR 迭代的关系。  
**关键结论**：复 Schur 是 `A=QTQ^*`，实 Schur 是 `A=QTQ^T`。

### 题 10

写出 SVD 及 Moore-Penrose 广义逆的基本性质，并证明 `AA^+` 是正交投影。  
**关键结论**：`P=AA^+` 对称幂等，故是投影。

---

## 三、书后习题加练（谨慎参考）

这些题只在和讲义/历年卷同向时提高权重，不单独当作“必考原题”。

### 1. 第 74-75 页

重点是舍入误差、增长因子、后向误差界、Cholesky/列主元 Gauss 的误差分析。

### 2. 第 136 页

重点是：

- Jacobi / G-S / SOR 的收敛条件；
- `rho(B)` 与最优 `omega`；
- 松弛迭代和 G-S 的关系。

### 3. 第 158-159 页

重点是：

- 最速下降法误差估计；
- 共轭梯度法中的正交/共轭关系；
- `A^{-1}` 的共轭向量展开；
- 用 CG 解正定方程组。

### 4. 第 197-199 页

重点是：

- 幂法；
- 逆迭代；
- 位移 QR；
- Hessenberg 结构；
- Schur/QL/QR 类算法。

---

## 四、最短背诵版

1. `LU/PLU` 会算，会写 `P,L,U`，会解释选主元。  
2. `||.||_F`、`||.||_2`、`||.||_X` 会证明。  
3. `Householder/Givens` 会构造，会说正交。  
4. `Jacobi/G-S/SOR` 会写迭代矩阵，会用 `rho(B)<1`。  
5. `Cholesky/LDL^T` 会做，会判正定。  
6. 最小二乘会写正则方程、会写 QR 解法。  
7. CG 会写三条递推，会证共轭向量展开。  
8. `Hessenberg/QR/Schur/SVD` 至少会讲清核心定理和为什么这么用。
