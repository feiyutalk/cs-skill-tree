# 线索二叉树

> 遍历二叉树就是以一定的规则将二叉树中的结点排列成一个线性序列，从而得到二叉树结点的各种遍历序列。其实质就是对一个非线性结构进行线性化操作，使在这个访问序列中每一个结点都有一个直接前驱和直接后继。

传统的链式存储仅能体现一种父子关系，不能直接得到结点在遍历中的前驱或后继。通过观察，我们发现在二叉链表表示的二叉树中存在大量的空指针，若利用这些空链域存放指向其直接前驱或后继的指针，则可以更方便的运用某些二叉树算法。

![](http://img.blog.csdn.net/20170220142145477?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXE3ODQ0Mjc2MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

线索二叉树的存储结构:

```c
typedef struct ThreadNode{
  ElemType data;
  struct ThreadNode *lchild, *rchild;
  int ltag, rtag;
}ThreadNode, *ThreadNode;
```

## 构造

### 前序遍历构造:

```c
void PreThread(ThreadTree &p, ThreadTree & pre){
	if(p == NULL)
      return;
    if(p->lchild == NULL){
      p->ltag = 1;
      p->lchild = pre;
    }
    if(pre != NULL && pre->rchild == NULL){
        pre->rtag = 1;
        pre->rchild = p;
    }
    pre = p;
    if(p->ltag == 0)
      PreThread(p->lchild);
    if(p->rtag == 0)
      PreThread(p->rchild);
}
```

### 中序遍历构造:

```c
void InThread(ThreadTree &p, ThreadTree &pre){
    if(p == NULL)
      return ;
  
    InThread(p->lchild, pre); //递归，线索化左子树
  
    if(p->lchild == NULL){
      p->lchild = pre;
      p->ltag = 1;
    }
    if(pre != NULL && pre->rchild == NULL){
      pre->rchild = p;
      pre->rtag = 1;
    }
    pre = p;
  
    InThread(p->rchild, pre);
}

void CreateInThread(ThreadTree T){
  ThreadTree pre = NULL;
  if(T != NULL){
    InThread(T, pre);
    pre->rchild = NULL;
    pre->rtag = 1;
  }
}
```

### 后序遍历构造:

```c
void PostThread(ThreadTree &p, ThreadTree &pre){
  if(p){
    PostThread(p->left, pre);
    PostThread(p->right, pre);
    if(p->left == NULL){
      p->left = pre;
      p->ltag = 1;
    }
    if(pre != NULL && pre->rchild ==NULL){
		pre->rchild = p;
      pre->rtag = 1;
    }
    pre = p;
  }
}
```

## 遍历

![](http://www.imlifengfeng.com/blog/wp-content/uploads/2016/12/Snip20161212_58.jpg)

如何才能求解线索二叉树的题目呢？

- 画出示意图，请区分是先序、中序还是后序线索二叉树。

- 正规遍历，即先序线索二叉树进行先序遍历、中序线索二叉树进行中序遍历和后序线索二叉树进行后序遍历。求先序为例子

  - 左孩子为空:

     ```c
    return t.left;
     ```

  - 左孩子不为空:

    左子树进行中序遍历的最后一个节点 左 中 右 最右边的那个节点就是最后一个节点

    ```c
    return findRight(t.left);

    void findRight(BiTree t){
      if(t.right == null)
        return t;
      return findRight(t.right);
    }
    ```

- 非正规遍历，求前驱或后继。分四种情况讨论:

  - 左右子树都有

  ```c
  if(p.left && p.right)
    return p.right;
  ```

  - 只有左子树

  ```c
  if(p.rtag == 1){
    return p.left;
  }
  ```

  - 只有右子树

  ```c
  if(p.ltag == 1)
    return p.right;
  ```

  - 左右子树都无

  ```c
  p = p.left;
  while(p != NULL && p.ltag == 1)
    p = p.left;
  if(p == NULL)
    return NULL;
  else
    return p.left;
  ```

### 中序线索二叉树

- 中序遍历

```c
void Inorder(ThreadNode *T){
  for(ThreadNode *p=Firstnode(T); p!=NULL; p=Nextnode(p)){
    visit(p);
  }
}

ThreadNode *Firstnode(ThreadNode *p){
  while(p->ltag == 0)
    p=p->lchild;
  return p;
}

ThreadNode *Nextnode(ThreadNode *p){
  if(p->rtag == 0)
    return Firstnode(p->rchild);
  else
    return p->rchild;
}
```

- 后序前驱


- 后续后继


- 先序前驱
- 先序后继

