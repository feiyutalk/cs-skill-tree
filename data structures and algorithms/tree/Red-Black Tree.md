# Preface

在二分搜索树中，进行查找、前驱、后继、最小值、最大值、插入和删除等操作，算法的时间复杂度都是O(h)。因此，当树的高度比较矮的时候，时间复杂度比较小；当树的高度变得很高的时候，那么它的时间复杂度就和链表没什么区别了。因此，我们需要设计一种搜索树的机制来保证树的高度的平和，使得基本的动态操作的时间复杂度最坏为O(logn)。

红黑树的节点和普通的二分搜索树节点的区别仅仅是多了一个color属性，color既可以是红色也可以是黑色，红黑树通过限制从根节点到叶子节点路径上节点color，以保证树是平衡的。

# Red-Black Trees

## 属性

1. 每个节点颜色要么是红色，要么是黑色。
2. 根节点是黑色。
3. 每个叶子节点都是黑色。(注意，这里的叶子节点是实际上是空节点，其值为NIL)。
4. 如果当前节点是红色， 则其孩子都是黑色。
5. 对于任何节点，它到子孙叶子节点路径上包含有相同数目的黑色节点。

![](data:image/png;base64,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)

## 性质

1. **一个包含n个内部节点的红黑树高度至多为 $2lg(n+1)$.**

   这个性质保证了，我们对红黑树的搜索、求最小值、求最大值、求后继、求前驱操作都可以在O(lgn)时间复杂度里完成。但是，对于插入，删除操作，虽然他们也可以在O(lgn)时间复杂度里完成，但是他们对树进行的修改，我们需要保证修改后的树仍然树红黑树。

## 操作

### 1. 旋转

树的插入和删除操作，可能破坏红黑树的属性，使其不是红黑树，我们需要通过旋转将其调整为红黑树。

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIxgDeGNw3C_ZCVgrYn9bdvglA5XAiccUOIbAUwZCpBexESbhU)

```c
y = x.right
x.right = y.left
if y.left != T.nil
	y.left.p = x
y.p = x.p
if x.p == T.nil
	T.root = y
else if x == x.p.left
	x.p.left = y
else 
    x.p.right = y
y.left = x
x.p = y
```

### 2. 插入

假设要插入的节点为z，红黑树节点的插入与二分搜索树有的插入不同之处如下:

1. 二分搜索树种的NIL节点全部替换为T.nil
2. 我们将z的左孩子和右孩子设置为T.nil以保证正确的树结构
3. 将插入节点z，涂成红色
4. 由于插入操作可能破坏红黑树的性质，通过调用 RB-INSERT-FIXUP(T,z)函数，对其进行重新上色和旋转操作

```c
RB-INSERT(T, z)
y = T.nil
x = T.root
while x != Y.nil
	y = x
	if z.key < x.key
		x = x.left
    else
    	x = x.right
z.p = y
if y == T.nil
	T.root = z
else if z.key < y.key
	y.left = z
else
	y.right = z
z.left = T.nil
z.right = T.nil
z.color = RED
RB-INSERT-FIXUP(T,z)
```

在进行调整之前，我们先要弄明白新节点的插入操作将会导致哪些属性被违反？

1. 每个节点颜色要么是红色，要么是黑色。
2. 根节点是黑色。
3. 每个叶子节点都是黑色。(注意，这里的叶子节点是实际上是空节点，其值为NIL)。
4. 如果当前节点是红色， 则其孩子都是黑色。
5. 对于任何节点，它到子孙叶子节点路径上包含有相同数目的黑色节点。

对于属性1，属性3，属性5，插入新节点都不会违反这几个属性，而仅仅会违反属性2和属性4。由于初始化时z被涂成红色， 所以属性2，属性4都可能被破坏。

```c
RB-INSERT-FIXUP(T,z)

while z.p.color == RED
	if z.p == z.p.p.left
		y = z.p.p.right
		if y.color == RED
			z.p.color = BLACK
			y.color = BLACK
			z.p.p.color = RED
			z = z.p.p
		else 
		      if z == z.p.right
			  z = z.p
			  LEFT-ROTATE(T,z)
		      z.p.color = BLACK
		      z.p.p.color = RED
		      RIGHT-ROTATE(T, z.p.p)
      else
          same as then clause with right and left exchanged
T.root.color = BLACK
```

我们需要分6种情况来讨论，红黑树属性被破坏的情况，又因为左右是对称的，所以，实际上我们只要处理三种情况就可以了。而这三种情况是通过检查z's uncle，即 z's parent's sibling。如果 y = z's uncle 是红色，我们执行case1，否则我们执行case 2 和 case 3。

- **Case 1 : z's uncle y is red**

  ![](http://www.geeksforgeeks.org/wp-content/uploads/redBlackCase2.png)

- **Case 2: z's uncle y is black and z is a right child**

- **Case 3: z's uncle y is black and z is a left child**

  在这种情况下，z's uncle都是黑色，这时候我们通过 `z is a right or left child of z.p` 来区分这两种情况。如果z是右孩子，我们需要多执行一步LEFT-ROTATE(T, z.p.p)，然后再执行RIGHT-ROTATE(T, z.p.p)。

  ![](http://www.geeksforgeeks.org/wp-content/uploads/redBlackCase3b.png)

  ### 3. 删除

  ​
