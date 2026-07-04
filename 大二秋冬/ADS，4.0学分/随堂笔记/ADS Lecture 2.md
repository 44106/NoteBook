# **ADS Lecture 2**

## Red-Black Trees

Target : **balanced binary search tree**

```c
Typedef struct Node{
    Node* parent;
    int color;
    int key;
    Node* left;
    Node* right;
}
```

**外部节点**:虚拟节点连接：虚拟叶子节点+根节点的父节点，从而避免空指针判断。

性质：

1. Every node is either black or red.非红即黑
2. The root is black
3. Every leaf (NIL）is black
4. if a node is **red** ，then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain **the same number of black node**s. 

**【definition】** the black-height of any node x ,denoted by bh(x), is the number of black nodes on any simple path from x(x is not includes)down to a leaf.bh(Tree) = bh(root)

**[lemma]** A red-tree with N internal nodes has height at most 2 ln(N+1)

Proof: 1>For any node x ,sizeof(x) >= 2^bh(x)^-1.Prove by induction.

x->NULL === h(x) = 0 ;then h(x)<=k

Suppose it is true for x with h(x)<k

for x with h(x) = k+1,bh(child) = bh(x) or bh(x)-1

Since  h(child)<=k,sizeof(child)>= 2^bh(child)^ -1 >= 2^bh(x)-1^-1

Hense sizeof(x) = 1+2sizeof(child)>=2^bh(x)^-1

2> bh(Tree) >= h(Tree) /2

### Insert

```
BST_insert();
case 1（需迭代）:
	 黑                   红
	/  \                 /  \
   红   红   ----->     黑   黑
  /                   /
 红                  红
 case 2（进入case3）:
 	 黑                   黑
	/  \    rotation     /  \
   红   黑   ----->     红   黑
    \                 /
     红              红
case 3:
	 黑                   红						黑
	/  \                 /  \   rotation		/   \
   红   黑   ----->     黑   黑  ------>        红	 红
  /                   /								  \
 红                  红								 黑
```

时间复杂度O(logN)

### Delete

``` 
删除操作最后一定归结为删除叶子
													
                                                    w(H)
case 1:     									   /
       H				 R      rotation		  R
     /   \    ------>  /   \    ----------->     /  \
   x(H) w(r)          x(H) w(H)					x    H(可能是NIL)
```

![红黑树_deletjpg](E:\大二上\ADS\随堂笔记\红黑树_deletjpg.jpg)

![](E:\大二上\ADS\随堂笔记\红黑树_delet2.jpg)

```cpp
#include <stdio.h>
#include <stdlib.h>

// 颜色枚举
typedef enum { RED, BLACK } Color;

// 红黑树节点结构
typedef struct RBNode {
    int key;
    Color color;
    struct RBNode *left;
    struct RBNode *right;
    struct RBNode *parent;
} RBNode;

// 红黑树结构
typedef struct {
    RBNode *root;
    RBNode *nil;  // 哨兵节点，代表NIL
} RBTree;

// 创建哨兵节点
RBNode* create_nil_node() {
    RBNode *node = (RBNode*)malloc(sizeof(RBNode));
    node->color = BLACK;
    node->left = node->right = node->parent = NULL;
    return node;
}

// 初始化红黑树
void init_rb_tree(RBTree *tree) {
    tree->nil = create_nil_node();
    tree->root = tree->nil;
}

// 创建新节点
RBNode* create_node(int key) {
    RBNode *node = (RBNode*)malloc(sizeof(RBNode));
    node->key = key;
    node->color = RED;  // 新节点默认为红色
    node->left = node->right = node->parent = NULL;
    return node;
}

// 左旋
void left_rotate(RBTree *tree, RBNode *x) {
    RBNode *y = x->right;
    x->right = y->left;
    
    if (y->left != tree->nil) {
        y->left->parent = x;
    }
    
    y->parent = x->parent;
    
    if (x->parent == tree->nil) {
        tree->root = y;
    } else if (x == x->parent->left) {
        x->parent->left = y;
    } else {
        x->parent->right = y;
    }
    
    y->left = x;
    x->parent = y;
}

// 右旋
void right_rotate(RBTree *tree, RBNode *y) {
    RBNode *x = y->left;
    y->left = x->right;
    
    if (x->right != tree->nil) {
        x->right->parent = y;
    }
    
    x->parent = y->parent;
    
    if (y->parent == tree->nil) {
        tree->root = x;
    } else if (y == y->parent->right) {
        y->parent->right = x;
    } else {
        y->parent->left = x;
    }
    
    x->right = y;
    y->parent = x;
}

// 插入修复
void insert_fixup(RBTree *tree, RBNode *z) {
    while (z->parent->color == RED) {
        if (z->parent == z->parent->parent->left) {
            RBNode *y = z->parent->parent->right;  // 叔节点
            
            // Case 1: 叔节点为红色
            if (y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            } else {
                // Case 2: z 是右孩子
                if (z == z->parent->right) {
                    z = z->parent;
                    left_rotate(tree, z);
                }
                
                // Case 3: z 是左孩子
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                right_rotate(tree, z->parent->parent);
            }
        } else {
            // 对称情况（z.parent 是右孩子）
            RBNode *y = z->parent->parent->left;  // 叔节点
            
            if (y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            } else {
                if (z == z->parent->left) {
                    z = z->parent;
                    right_rotate(tree, z);
                }
                
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                left_rotate(tree, z->parent->parent);
            }
        }
    }
    tree->root->color = BLACK;
}

// 插入节点
void rb_insert(RBTree *tree, int key) {
    RBNode *z = create_node(key);
    RBNode *y = tree->nil;
    RBNode *x = tree->root;
    
    // 找到插入位置
    while (x != tree->nil) {
        y = x;
        if (z->key < x->key) {
            x = x->left;
        } else {
            x = x->right;
        }
    }
    
    // 插入新节点
    z->parent = y;
    if (y == tree->nil) {
        tree->root = z;
    } else if (z->key < y->key) {
        y->left = z;
    } else {
        y->right = z;
    }
    
    z->left = tree->nil;
    z->right = tree->nil;
    z->color = RED;
    
    insert_fixup(tree, z);
}

// 节点替换
void rb_transplant(RBTree *tree, RBNode *u, RBNode *v) {
    if (u->parent == tree->nil) {
        tree->root = v;
    } else if (u == u->parent->left) {
        u->parent->left = v;
    } else {
        u->parent->right = v;
    }
    v->parent = u->parent;
}

// 查找最小值节点
RBNode* tree_minimum(RBTree *tree, RBNode *x) {
    while (x->left != tree->nil) {
        x = x->left;
    }
    return x;
}

// 删除修复
void delete_fixup(RBTree *tree, RBNode *x) {
    while (x != tree->root && x->color == BLACK) {
        if (x == x->parent->left) {
            RBNode *w = x->parent->right;  // 兄弟节点
            
            // Case 1: 兄弟节点为红色
            if (w->color == RED) {
                w->color = BLACK;
                x->parent->color = RED;
                left_rotate(tree, x->parent);
                w = x->parent->right;
            }
            
            // Case 2: 兄弟节点的两个子节点都是黑色
            if (w->left->color == BLACK && w->right->color == BLACK) {
                w->color = RED;
                x = x->parent;
            } else {
                // Case 3: 兄弟节点的右子节点为黑色
                if (w->right->color == BLACK) {
                    w->left->color = BLACK;
                    w->color = RED;
                    right_rotate(tree, w);
                    w = x->parent->right;
                }
                
                // Case 4
                w->color = x->parent->color;
                x->parent->color = BLACK;
                w->right->color = BLACK;
                left_rotate(tree, x->parent);
                x = tree->root;
            }
        } else {
            // 对称情况（x 是右孩子）
            RBNode *w = x->parent->left;
            
            if (w->color == RED) {
                w->color = BLACK;
                x->parent->color = RED;
                right_rotate(tree, x->parent);
                w = x->parent->left;
            }
            
            if (w->right->color == BLACK && w->left->color == BLACK) {
                w->color = RED;
                x = x->parent;
            } else {
                if (w->left->color == BLACK) {
                    w->right->color = BLACK;
                    w->color = RED;
                    left_rotate(tree, w);
                    w = x->parent->left;
                }
                
                w->color = x->parent->color;
                x->parent->color = BLACK;
                w->left->color = BLACK;
                right_rotate(tree, x->parent);
                x = tree->root;
            }
        }
    }
    x->color = BLACK;
}

// 删除节点
void rb_delete(RBTree *tree, int key) {
    RBNode *z = tree->root;
    
    // 查找要删除的节点
    while (z != tree->nil) {
        if (key == z->key) {
            break;
        } else if (key < z->key) {
            z = z->left;
        } else {
            z = z->right;
        }
    }
    
    if (z == tree->nil) {
        printf("Key %d not found in the tree.\n", key);
        return;
    }
    
    RBNode *y = z;
    RBNode *x;
    Color y_original_color = y->color;
    
    if (z->left == tree->nil) {
        x = z->right;
        rb_transplant(tree, z, z->right);
    } else if (z->right == tree->nil) {
        x = z->left;
        rb_transplant(tree, z, z->left);
    } else {
        y = tree_minimum(tree, z->right);
        y_original_color = y->color;
        x = y->right;
        
        if (y->parent == z) {
            x->parent = y;
        } else {
            rb_transplant(tree, y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        
        rb_transplant(tree, z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    
    if (y_original_color == BLACK) {
        delete_fixup(tree, x);
    }
    
    free(z);
}

// 中序遍历（用于测试）
void inorder_traversal(RBTree *tree, RBNode *node) {
    if (node != tree->nil) {
        inorder_traversal(tree, node->left);
        printf("%d(%s) ", node->key, node->color == RED ? "RED" : "BLACK");
        inorder_traversal(tree, node->right);
    }
}

// 查找节点（用于测试）
RBNode* rb_search(RBTree *tree, int key) {
    RBNode *current = tree->root;
    while (current != tree->nil) {
        if (key == current->key) {
            return current;
        } else if (key < current->key) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    return NULL;
}

// 释放树的内存
void free_tree(RBTree *tree, RBNode *node) {
    if (node != tree->nil) {
        free_tree(tree, node->left);
        free_tree(tree, node->right);
        free(node);
    }
}

// 主函数测试
int main() {
    RBTree tree;
    init_rb_tree(&tree);
    
    // 测试插入
    int keys[] = {7, 3, 18, 10, 22, 8, 11, 26};
    int n = sizeof(keys) / sizeof(keys[0]);
    
    printf("Inserting keys: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", keys[i]);
        rb_insert(&tree, keys[i]);
    }
    printf("\n");
    
    printf("Inorder traversal: ");
    inorder_traversal(&tree, tree.root);
    printf("\n");
    
    // 测试查找
    int search_key = 10;
    RBNode *found = rb_search(&tree, search_key);
    if (found) {
        printf("Key %d found: %d(%s)\n", search_key, found->key, 
               found->color == RED ? "RED" : "BLACK");
    } else {
        printf("Key %d not found\n", search_key);
    }
    
    // 测试删除
    int delete_key = 18;
    printf("Deleting key: %d\n", delete_key);
    rb_delete(&tree, delete_key);
    
    printf("Inorder traversal after deletion: ");
    inorder_traversal(&tree, tree.root);
    printf("\n");
    
    // 释放内存
    free_tree(&tree, tree.root);
    free(tree.nil);
    
    return 0;
}
```



