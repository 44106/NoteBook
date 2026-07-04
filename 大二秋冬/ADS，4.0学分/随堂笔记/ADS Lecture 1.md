# ADS Lecture 1

## AVL tree 平衡树（Adelson-Velsky and Landis Tree）

是一种**自平衡的二叉搜索树（Self-Balancing Binary Search Tree）**

**height balanced**： | h~L~ - h~R~  | <= 1 . an empty tree is defined -1.

The balanced factor BF(node)= h~L~ - h~R~ .(每个节点) BF of AVL tree only have -1,0,1.

### Tree rotation 树的旋转

​	在 **AVL 树**中，当插入或删除节点导致某个节点“失衡”（即平衡因子 = ±2）时，需要通过 **旋转操作** 来恢复平衡。四种旋转类型：**LL、RR、LR、RL** —— 它们的名字来源于“失衡路径”的形状。

LL 左子树的左子树

LR

RL解决方法也是先右旋（右子树）再左旋根节点

RR

出问题的根节点到插入节点的路径是左/右+左/右

### 完整插入后调整示例（伪代码）

```python
def right_rotate(A):
    B = A.left
    D = B.right

    # 旋转
    B.right = A
    A.left = D

    # 更新高度（后续会讲）
    update_height(A)
    update_height(B)

    return B  # 新的子树根

def left_rotate(A):
    C = A.right
    B = C.left

    # 旋转
    C.left = A
    A.right = B

    update_height(A)
    update_height(C)

    return C  # 新的子树根

def insert(root, key):
    # 1. 执行标准 BST 插入
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # 2. 更新当前节点高度
    update_height(root)

    # 3. 获取平衡因子
    balance = get_balance(root)

    # 4. 如果失衡，分四种情况处理

    # Left Left
    if balance < -1 and key < root.left.key:
        return right_rotate(root)

    # Right Right
    if balance > 1 and key > root.right.key:
        return left_rotate(root)

    # Left Right
    if balance < -1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left
    if balance > 1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    # 5. 无旋转，返回原根
    return root
```

n~h~ = F~h+3~ - 1 for h>=1

F~i~ 约等于 1/根号5 （(1+sqrt(5))/2）^i^

所以insert的时间复杂度是O(logN)

## Splay tree**（伸展树）**

**target : Any M consecutive tree operations starting from an empty tree take at most O(MlogN)time.**只保证总时间

for any nonroot X ,denote its parent by P and grandparent by G:

case 1:P is the root -> Rotate X and P

Case 2: P Is not the root.

Zig-zag Double rotation（先旋父子，再旋爷孙）方向交叉

Zig-zig single rotation(先旋转P-G，再旋转X-P)方向一致

#### 将X伸展到根

```python
function splay(root, x):
    # 从 x 开始，不断旋转，直到 x 成为根
    while x.parent is not None:
        p = x.parent
        g = p.parent

        if g is None:
            # Zig: x 的父节点就是根
            if x == p.left:
                right_rotate(p)   # Zig (右旋)
            else:
                left_rotate(p)    # Zig (左旋)
        else:
            # Zig-Zig 或 Zig-Zag
            if x == p.left and p == g.left:
                # Zig-Zig Left-Left
                right_rotate(g)   # 先转祖父
                right_rotate(p)   # 再转父
            elif x == p.right and p == g.right:
                # Zig-Zig Right-Right
                left_rotate(g)
                left_rotate(p)
            elif x == p.left and p == g.right:
                # Zig-Zag Right-Left
                right_rotate(p)   # 先转父
                left_rotate(g)    # 再转祖父
            elif x == p.right and p == g.left:
                # Zig-Zag Left-Right
                left_rotate(p)
                right_rotate(g)

    # x 现在是根节点
    return x
```

#### 右旋

```python
function right_rotate(x):
    # x 必须有左孩子
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x

    y.parent = x.parent
    if x.parent is None:
        root = y          # y 成为新根（需在调用处更新）
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.right = x
    x.parent = y

    # 如果需要，更新高度/大小等（Splay Tree 通常不需要）
    return y   # 新的子树根
```

#### 左旋

```python
function left_rotate(x):
    # x 必须有右孩子
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x

    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    return y
```

#### **Splay Tree 的 `find`（查找）操作**

```python
function splay_find(root, key):
    if root is None:
        return None

    # Step 1: BST 查找，同时记录路径（或直接在查找中 Splay）
    # 我们采用“边查找边准备 Splay”的方式，最后调用 splay(node)

    current = root
    while current is not None:
        if key == current.key:
            # 找到！跳出循环，准备 Splay 此节点
            break
        elif key < current.key:
            if current.left is None:
                break  # 未找到，停在 current
            current = current.left
        else: # key > current.key
            if current.right is None:
                break  # 未找到，停在 current
            current = current.right

    # Step 2: 将 current 伸展到根
    root = splay(root, current)   # splay 操作会返回新的根

    # Step 3: 返回新根（调用者需比较 root.key == key 判断是否找到）
    return root
```



### Deletions

Find X(X will be at the root)

Remove X

findMax(T~L~);

Make T~R~ the right child of the root of T~L~ ;

## Amortized Analysis 均摊分析

target ： Any M consecutive operations take at most O(MlogN)time. ——Amortized time bound

worst-case bound >= amortized bound >= average-case bound

### Aggregate ananlysis**聚合分析**

计算执行 **n 次操作的总代价 T(n)**，然后将总代价平均分摊到每次操作上，得到 **每次操作的均摊代价 = T(n) / n**

### Accounting method 会计方法

When an operation's amortized cost c^ ~i~ exceeds its actual cost c~i~ ,we assign the difference to specific objects in the data structure as credit.

为每个操作分配一个“摊还代价”，并保证在任何操作序列中，预先收取的“信用”始终足以支付后续的实际开销。

- **核心思想**：

  - 对每个操作分配一个**摊还代价** `ĉ_i`，它可能高于或低于其**实际代价** `c_i`。

  - 如果 `ĉ_i > c_i`，差额作为**信用（credit）** 存储起来，为以后代价高的操作做准备。

  - 如果 `ĉ_i < c_i`，则使用之前存储的信用来支付差额。

  - **关键 invariant（不变式）**：**在任何操作序列的每一步，累计的总信用必须始终非负**。即，我们不能“透支”。

    ### 势能方法（Potential Method）

potential function势能函数

- 定义一个**势函数（Potential Function）** `Φ(D_i)`，它将数据结构 `D_i` 的状态映射到一个实数，表示其当前存储的“势能”或“信用”。
- 第 i 次操作的**摊还代价** `ĉ_i` 定义为：
  **`ĉ_i = c_i + Φ(D_i) - Φ(D_{i-1})`**
  - `c_i`: 实际代价
  - `Φ(D_i) - Φ(D_{i-1})`: 本次操作引起的**势能变化**（ΔΦ）
- **总摊还代价**：整个序列的总摊还代价为：
  **`Σĉ_i = Σc_i + Φ(D_n) - Φ(D_0)`**
- 要证明摊还代价有上界，我们通常需要保证 `Φ(D_n) ≥ Φ(D_0)`，这样总摊代价就是总实际代价的一个上界。

if a+b <= c, then log a +lag b<=2log c - 2

for slay tree

c~i~ = 1(for zig ) or 2(for zig-zag or zig-zig)

zig : c~i~^ = 1 + R~2~(X) -R~1~(X) + R~2~(P) -R~1~(P) <=1+R~2~(X)-R~1~(X)

zig-zag : c~i~^ = 2 +R~2~(X) -R~1~(X) + R~2~(P) -R~1~(P) +R~2~(G) - R~1~(G) <= 2(R~2~(X)-R~1~(X))

zig-zig : c~i~^ = 2 +R~2~(X) -R~1~(X) + R~2~(P) -R~1~(P) +R~2~(G) - R~1~(G) <=3(R~2~(X)-R~1~(X))

c~i~ <= 1+3(R~2~(X)-R~1~(X))
