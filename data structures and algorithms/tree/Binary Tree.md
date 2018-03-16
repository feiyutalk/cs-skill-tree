# 树

## 定义

>树是 N（N>=0）个结点的有限集合，N=0时，称为空树，这是一种特殊情况。在任意一颗非空树中应满足:
>
>1) 有且仅有一个特定的称为根的结点。
>
>2) 当N>1时，其余结点可分为m（m>0）个互不相较的有限集合$T_1,T_2,…,T_m$，其中每一个集合本身又是一棵树，并且称为根节点的子树。

显然树的定义是递归的，是一种递归的数据结构。树作为一种逻辑结构，同时也是一种分层结构，具有以下两个特点:

1. 树的根结点没有前驱结点，除根节点之外的所有结点有且只有一个前驱结点。
2. 树种所有结点可以有零个或多个后继结点。

树适合于表示具有层次结构的数据。树种的某个结点（除根节点外）最多只和上一层的一个结点（即其父结点）有直接关系，根节点没有直接上层节点，因此在n个结点的树中有n-1条边。

![](http://upload-images.jianshu.io/upload_images/851071-93d8eb813cd9f384.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

树具有如下最基本的性质:

- 树中的结点数等于所有结点的度数加1；
- 度为m的树种第i层上至多有$m^{i-1}$个结点；
- 高度为h的m叉树至多有$\frac {m^h-1}{m-1}$个结点；
- 具有n个结点的m叉树的最小高度为$\left \lceil log_m(n(m-1)+1) \right \rceil$

## 二叉树的定义

二叉树是另一种树形结构，其特点是每个结点至多只有两颗子树，并且，二叉树的子树有左右之分，其次序不能任意颠倒。

![](http://img.blog.csdn.net/20141024171124828?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTFVPWElOSklF/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

## 几种特殊的二叉树

### 满二叉树

一颗高度为h，并且含有$2^h -1$个结点的二叉树称为满二叉树，即树中的每一层都含有最多的结点。

可以对满二叉树按层序编号:约定编号从根结点起，自上而下，自左而右。这样每个结点对应一个编号，对于编号为i的结点，如果有双亲，其双亲为$\left \lfloor i/2 \right \rfloor$，如果有左孩子，则左孩子为$2i$，如果有右孩子，则右孩子为$2i+1$。

![](http://images2015.cnblogs.com/blog/857250/201605/857250-20160509222723796-1163926866.png)

### 完全二叉树

设一个高度为h，有n个结点的二叉树，当且仅当其每一个结点都与高度为h的满二叉树中编号为$1~n$的结点一一对应时，称为完全二叉树。

![](http://obvjfxxhr.bkt.clouddn.com/bitree_man.PNG)

完全二叉树具有如下的性质:

1. 如果 $i \leq \left \lfloor n/2 \right \rfloor$，则结点i为分支结点，否则为叶子结点。
2. 叶子结点只可能在层次最大的两层上出现，对于最大层次中的叶子结点，都一次排列在该层最左边的位置上。
3. 如果有度为1的结点，只可能有一个，且该节点只有左孩子而无右孩子。
4. 按层次编号后，一旦出现某节点为叶子结点或只有左孩子，则编号大于i的结点均为叶子结点。

### 二叉排序树

一颗二叉树或者是空二叉树，或者是具有如下性质的二叉树；左子树上所有结点的关键字均小于结点的关键字；右子树上的所有结点的关键字均大于根结点的关键字。左子树和右子树又各是一颗二叉排序树。

### 平衡二叉树

树上任一结点的左子树和右子树的深度之差不超过1。

## 二叉树的顺序存储结构

二叉树的顺序存储结构就是用一组地址连续的存储单元依次自上而下、自左而右存储完全二叉树上的结点元素，即将完全二叉树上编号为i的结点元素存储在某个数组下标为i-1的分量中，然后通过一些方法确定节点在逻辑上的父子和兄弟关系。

![](http://om6h9y7ik.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20170405212047.png)

依据二叉树的性质，完全二叉树和满二叉树采用顺序存储比较合适，树中结点的序号可以唯一地反映出结点之间的逻辑关系。这样既能最大可能地节省存储空间，又可以利用数组元素的下标值确定结点在二叉树中的位置，以及结点之间的关系。

## 二叉树的链式存储结构

由于顺序存储对空间利用率较低，因此，一般二叉树都采用链式存储结构。链式结构是指用一个链表来存储一颗二叉树，二叉树中每一个结点用链表的一个链结点来存储。**二叉链表至少包含3个域: 数据域data、左指针域lchild和右指针域rchild。**

![](http://img.blog.csdn.net/20170522184451553?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZ2F2aW5fam9obg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 遍历

所谓二叉树的遍历，是指按某条搜索路径访问树中的每个结点，使得每个结点均被访问一次，而且进被访问一次。

常见的遍历次序有先序(NLR)、中序(LNR)和后序(LRN)。

遍历的实现上也分为两种：一、递归遍历；二、非递归遍历。

### 先序遍历

#### 递归

```c
void PreOrder(BiTree T){
  if(T != NULL){
    visit(T);
    PreOrder(T->child);
    PreOrder(T->rchild);
  }
}
```

#### 非递归

在所有非递归遍历方式里面，前序遍历的非递归遍历是最简单的，如果没有要求用哪一种遍历的非递归方式，首先考虑用前序遍历的非递归。

```C
void PreOrder(BiTree T){
  stack s;
  s.push(t)
  while(!s.empty()){
    r = s.top();
    s.pop();
    if(r != null){
      	visit(r);
        s.push(r.right);
        s.push(r.left);
    }
  }
}
```

### 中序遍历

#### 递归

```c
void InOrder(BiTree T){
  if(T != NULL){
    InOrder(T->lchild);
    visit(T);
    InOrder(T->rchild);
  }
}
```

#### 非递归

```c
void InOrder(BiTree T){
	stack s;
  while(!s.empty() || t != null){
    while(t != null){
      s.push(t);
      t = t.left;
    }
    if(!s.empty()){
      t = s.top();
      visit(t);
      s.pop();
      t = t.right;
    }
  }
}
```

### 后续遍历

#### 递归

```c
void PostOrder(BiTree T){
  if(T != NULL){
    PostOrder(T->lchild);
    PostOrder(T->rchild);
    visit(T);
  }
}
```

### 非递归遍历模板方法

其实二叉树的3种遍历策略，无非是处理节点的时机不同：前序遍历是在遇到节点时即处理，中序遍历是在处理完左节点后再处理，而后序是在处理完左右节点后再处理。

使用费递归方法实现时，除了记录当前的节点的访问栈，还需要记录当前节点的状态。对于每一个节点，我们定义如下状态：

- 0 表示 尚未处理左右子节点
- 1 表示 仅仅处理完毕左节点
- 2 表示 左右节点都处理完毕

那么，前序、中序、后序遍历的唯一不同，无非是将节点加入序列化结果集合的时机不同而已。

```java
class Node{
  int value;
  Node left;
  Node right;
}

public static final int STATE_NONE = 0;
public static final int STATE_LEFT_DONE = 1;
public static final int STATE_LEFT_RIGHT_DONE = 2;

public static List<Node> traverse(Node node, int when){
  List<Node> res = new ArrayList<>() // 序列化结果
  Stack<Node> stackNode = new Stack<>() // 保存节点的栈
  Stack<Integer> stackState = new Stack<>() // 保存节点状态的栈
  
  stackNode.push(node);
  stackState.push(STATE_NONE);
  /*算法说明：
      *    初始时放入根节点，将其标记为左右节点尚未处理的状态
      *    每个循环，从栈中取出一个节点和其状态，根据其当前状态转移到下一个状态（很显然，你可以从状态转换机的角度解读这个算法）。
      *    状态转换规则：  STATE_NONE-->STATE_LEFT_DONE-->STATE_LEFT_RIGTH_DONE-->弹出栈
      *    伴随状态的变化，还需要相应的操作，如将左右子节点放入栈中，或者将当
    		前节点弹出栈；最重要的一点是，当当前节点的状态符合处理状态的要求时，就会将节点加入序列化集合。
      */
  while(!stackNode.isEmpty())
    {
      Node n=stackNode.peek(); 
      Integer  state=stackState.peek();

     if(state==when)//当前状态可处理节点
          res.add(n);
      //3种状态之间的转换
     if(state==STATE_NONE)
     {
       stackState.set(stackState.size()-1,STATE_LEFT_DONE);
       if(n.left!=null)
       {
          stackNode.push(n.left);
          stackState.push(STATE_NONE);
       }
    }else if(state==STATE_LEFT_DONE){ 
       stackState.set(stackState.size()-1,STATE_LEFT_RIGHT_DONE);
       if(n.right!=null)
       {
          stackNode.push(n.right);
          stackState.push(STATE_NONE);
       }
     }else if(state==STATE_LEFT_RIGHT_DONE){
        stackNode.pop();
        stackState.pop();
     }
  }
  return  res;
}
```

### 层次遍历

要进行层次遍历需要借助一个队列，先将二叉树根结点入队，然后出队，访问该结点，如果它由左子树，则将左子树根节点入队；如果它有右子树，则将右子树根结点入队。然后出队，对出队结点访问，如此反复，直到队列为空。

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVnyJv7VoQ4R-dsF0yPiYOhI_1Rm4fcDZsylPPMI8sWkHCAYUVDg)

## 线索二叉树

遍历二叉树就是以一定的规则将二叉树中的结点排列成一个线性序列，从而得到二叉树结点的各种遍历序列。其实质就是对一个非线性结构进行线性化操作，使在这个访问序列中每一个结点都有一个直接前驱和直接后继。

![](http://img.blog.csdn.net/20160301102930682)

![](http://obvjfxxhr.bkt.clouddn.com/threadTree_threadT2.PNG)

