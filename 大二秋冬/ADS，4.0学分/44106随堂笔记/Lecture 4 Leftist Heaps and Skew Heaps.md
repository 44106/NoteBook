# Lecture 4 Leftist Heaps and Skew Heaps

Leftist Heaps: speed up merging in O(N).

Leftist Heaps: Order Property ——the same

Structrue Property ——binary tree but unbalanced

两个儿子的节点成为内部节点，否则为根节点。

外节点的NPL为1，空节点视为-1

Npl(X) = min{NPL(C)+1 for all C as children of X}

左偏树 NPL(leftchild) >=NPL(rightchild)

A leftist tree with r nodes on the right path must have at least 2^r^-1nodes

```c++
struct TreeNode{
	ElementType Element;
	PriorityQueue Left;
	PriorityQueue Right;
	int NPL;
};
```

Merge(recursive version):

H1->root< H2-->root

Step1:merge(H1->Right,H2)

Step2:Attach(H2,H1->Right)

Swap(H1->right,H1->Left)if necessary

```c++
if H2 is NULL ,return H1;
if H1 is NULL,return H2;
if H1->root->Element < H2->root->Element return Merge1(H1,H2);
else return Merge1(H2,H1);

Merge1(H1,H2){
    if(H1->left == NULL)
        H1->left =H2;
    else{
        H1 ->Right = Merge(H1->right,H2);
        if(H1->left->NPL < H1->right->NPL)Swap(H1);
        H1->NPL = H1->right->NPL+1;
    }
    return H1;
}
```

Merge (iterative version)

Step1: Sort the right paths without changing their left children(合并两个有序数列)

Step2 :Swap children if necessary（从叶子开始）

DeleteMin

Step1:Delect the root

Step2:Merge the two subtrees

## Skew Heaps

Any M consecutive operations take at most O(MlogN) time.

Always swap the left and right children except that the largest of all the nodes on the right paths does not have its childeren swapped. No NPL.



即相必左偏树，merge时无论如何都交换，除非最后一次。