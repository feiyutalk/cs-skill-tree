# 线性表的定义和基本操作

![](http://www.it5art.com/wp-content/uploads/2017/08/%E7%BA%BF%E6%80%A7%E8%A1%A8-1.png)

## 定义

> 线性表是具有相同数据类型的n(n>=0)个数据元素的有限序列。其中n为表长，当n=0时，该线性表是一个空表。若用L命名线性表，则其一般表示如下:
>
> ​		$L = (a_1, a_2, …, a_i, a_{i+1}, …, a_n)$
>
> 其中，$a_1$是唯一的“第一个”数据元素，又称为表头元素；$a_n$是唯一的“最后一个”数据元素，又称为表尾元素。除第一个元素外，每个元素**有且仅有**一个直接前驱。除最后一个元素外，每个元素**有且仅有**一个直接后继。

以上是线性表的逻辑特性，特点如下:

- 表中元素的个数有限；
- 表中元素具有逻辑上的顺序性，在序列中各元素排序有先后次序；
- 表中元素都是数据元素，每个表元素都是单个元素；
- 表中元素的数据类型相同。这意味着每一个表元素占有相同数量的存储空间。
- 表中元素具有抽象性，就是说，仅讨论元素之间的逻辑关系，不考虑元素究竟表示什么内容。

## 基本操作

一个数据结构的基本操作是指其最核心、最基本的操作。其他较复杂的操作可以通过调用其基本操作来实现。

```c
InitList(&L)	初始化表
Length(L)		求表长度
LocateElem(L, e)	按值查找
GetElem(L, i)	按位查找
ListInsert(&L, i, e) 插入操作
ListDelete(&L, i, &e) 删除操作
PrintList(L)	输出操作
Empty(L)	判空操作
DestroyList(&L)		销毁操作
```

# 线性表的顺序表示

## 顺序表的定义

> 线性表的顺序存储又称为**顺序表**。它是用一组地址连续的存储单元，依次存储线性表中的数据元素，从而使得逻辑上相邻的两个元素在物理位置上也相邻。

因此，顺序表的特点是表中元素的逻辑顺序与其物理顺序相同。

![](http://upload-images.jianshu.io/upload_images/2918620-8ebdaf65c4d32f0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/400)

## 顺序表上基本操作的实现

仅仅列出插入操作、删除操作和按值查找，其他的自行思考。

### 插入操作

```c
bool ListInsert(SqList &L, int i, ElemType e){
  if(i < 1 || i>L.length + 1)
    return false;
  if(L.length >= MaxSize)
    return false;
  for(int j=L.length; j>=i; j--)
    L.data[j] = L.data[j-1];
  L.data[i-1] = e;
  L.length++;
  return true;
}
```

- 最好情况：在表尾插入(即i=n+1)，元素后移语句将不执行，时间复杂度为$O(1)$。
- 最坏情况: 在表头插入(即 i = 1)， 元素后移语句将执行n次，时间复杂度为$O(n)$。
- 假设$p_i(p_i = 1/(n+1))$是在第i个位置上插入一个节点的概率，则在长度为n的线性表中插入一个节点时所需移动节点的平均次数为:

$\sum_{i=1}^{n}p_i(n-i+1) = \sum_{i=1}^{n+1} \frac{1}{n+1}(n-i+1) = \frac{1}{n+1} \sum_{i=1}^{n+1}(n-i+1) = \frac{1}{n+1} = \frac{n}{2}$

因此，线性表插入算法的平均时间复杂度为$O(n)$。

### 删除操作

```c
bool ListDelete(SqList &L, int i, int &e){
  if(i<1 || i>L.length)
    return false;
  e = L.data[i-1];
  for(int j=i; j<L.length; j++)
    L.data[j-1] = L.data[j];
  L.length--;
  return true;
}
```

- 最好情况 $O(1)$
- 最坏情况 $O(n)$
- 平均时间复杂度 $O(n)$

### 按值查找

```c
int LocateElem(SqList L, ElemType e){
  int i;
  for(i = 0; i<L.length; i++){
    if(L.data[i] == e)
      return i+1;
  }
  return 0;
}
```

- 最好情况 $O(1)$
- 最坏情况 $O(n)$
- 平均时间复杂度 $O(n)$


# 线性表的链式表示

由于顺序表的插入、删除操作需要移动大量的元素，影响了运行效率，由此引入了线性表的链式存储。链式存储线性表时，不需要使用地址连续的存储单元，即它不要求逻辑上相邻的两个元素在物理位置上也相邻，它是通过“链”建立起数据元素之间的逻辑关系，因此，对线性表的插入、删除不需要移动元素，而只需要修改指针。

## 单链表的定义

> 线性表的链式存储又称为单链表，它是指通过一组任意的存储单元来存储线性表中的数据元素。为了建立数据元素之间的线性关系，对每个链表节点，除了存放元素自身的信息之外，还需要存放一个指向其后继的指针。

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrIIW02g2SLTlERSmIlPD8cuqgCLz7BGEyBcgw8p9_JbZpWuCCfg)

- 优点 : 解决顺序表需要大量的连续存储空间的缺点。
- 缺点 : 单链表附加指针域，浪费存储空间。

## 单链表上基本操作的实现

### 利用头插法建立单链表

![](http://c.biancheng.net/cpp/uploads/allimg/140709/1-140F9152T3201.jpg)

采用头插法建立单链表，读入数据的顺序与生产的链表中元素的顺序是相反的。

```c
LinkList CreateList1(LinkList &L){
  LNode *s;
  int x;
  L = (LinkList)malloc(sizeof(LNode));
  L->next = NULL;
  scanf("%d", &x);
  while(x!=9999){
    s = (LNode*)malloc(sizeof(LNode));
    s->data = x;
    s->next = L->next;
    L->next = s;
    scanf("%d", &x);
  }
  return L;
}
```



### 采用尾插法建立单链表

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgL3jyomv56gpsIsgeP0AfTM3H9Ek5aVdqNTv6IFPw5ff61fURlw)

```c
LinkList CreateList2(LinkList &L){
	int x;
  	L = (LinkList)malloc(sizeof(LNode));
  	LNode *s, *r = L;
    scanf("%d", &x);
    while(x!=9999){
		s = (LNode *)malloc(sizeof(LNode));
      	s->data = x;
      	r->next = s;
      	r = s;
      	scanf("%d", &x);
    }
  	r->next = NULL;
  	return L;
}
```

### 按序号查找节点值

```c
LNode *GetElem(LinkList L, int i){
  int j = 1;
  LNode *p = L->next;
  if(i == 0) return L;
  while(p && j<i){
    p = p -> next;
    j++;
  }
  return p;
}
```

### 按值查找表节点

```c
LNode *LocateElem(LinkList L, ElemType e){
  LNode *p = L->next;
  while(p!=NULL && p->data != e){
    p=p->next;
  }
  return p;
}
```

### 删除结点操作

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNziP1lYFUlYiMn7thy7i6EMNRqXTx9KSQeIHWKMBV2PbS_Iu0GQ)

## 双链表

单链表节点中只有一个指向其后继的指针，这使得单链表只能从头节点依次顺序地向后遍历。若要访问某个节点的前驱节点(插入、删除操作时)，只能从头开始遍历，访问后继节点的时间复杂度为$O(1)$，访问前驱节点的时间复杂度为$O(n)$。

![](http://oc703ax52.bkt.clouddn.com/list06.jpg)

## 循环单链表

循环单链表和单链表的区别在于，表中最后一个节点的指针不是NULL，而改为指向头节点，从而整个链表形成一个环。

![](http://images0.cnblogs.com/blog/641601/201508/291005416094507.png)

因为循环单链表是一个“环”，因此，在任何一个位置上的插入和删除操作都是等价的，无须判断是否是表尾。

## 循环双链表

![](http://img.blog.csdn.net/20160110144043307)

## 静态链表

静态链表是借助数组来描述线性表的链式存储结构，结点也有数据域data和指针域next，与前面所讲的链表中的指针不同的是，这里的指针是结点的相对地址（数组下标），又称为游标。和顺序表一样，静态链表也要预先分配一块连续的内存空间。

![](http://c.biancheng.net/cpp/uploads/allimg/140709/1-140F91J525408.jpg)

# 顺序表和链表的比较

- **存取方式**

顺序表可以顺序存取，也可以随机存取，链表只能从表头顺序存取元素。

- **逻辑结构与物理结构**

采用顺序存储时，逻辑上相邻的元素，其对应的物理存储位置也相邻。而采用链式存储时，逻辑上相邻的元素，其物理存储位置则不一定相邻，其对应的逻辑关系是通过指针来链接的。

- **查找，插入和删除操作**

对于按值查找，当顺序表在无序的情况下，两者的时间复杂度为O(n)，而当顺序表有序时，可采用折半查找，此时时间复杂度为$O(log_2n)$。

- **空间分配**

顺序存储在静态存储分配情形下，一旦存储空间装满空间就不能扩充，如果再加入新元素将出现内存溢出，需要预先分配足够大的存储空间。预先分配过大，可能会导致顺序表后补大量闲置；预先分配过小，又会造成溢出。动态存储分配虽然存储空间可以扩充，但需要移动大量元素，导致操作效率降低，而且弱内存中没有更大块的连续存储空间将导致分配失败。链式存储的节点空间只在需要的时候申请分配，只要内存有空间就可以分配，操作灵活、高效。



