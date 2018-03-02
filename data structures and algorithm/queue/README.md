# 队列

## 定义

> 队列: 也是一种操作受限的线性表，只允许在表的一端进行插入，而在表的另一端进行删除。向队列中插入元素称为入队或进队；删除元素称为出队或离队。其操作的特性是先进先出，故又称为先进先出的线性表。

![](http://www.cppblog.com/images/cppblog_com/cxiaojia/queue1.png)

## 基本操作

```c
InitQueue(&Q)	初始化队列，构造一个空队列Q。
QueueEmpty(Q)	判队列空
EnQueue(&Q, x)	入队
DeQueue(&Q, &x)	出队
GetHead(Q, &x)	读队头元素，若队列Q非空，则将对头元素赋值给x
```

# 队列的顺序存储

![](http://img.my.csdn.net/uploads/201303/12/1363062817_8752.jpg)

队列的顺序实现是指分配一块连续的存储单元存放队列中的元素，并附设两个指针front和rear分别指示队头元素和队尾元素。

一般实现，都会采用循环队列的实现方式，把存储队列元素的表从逻辑上看成是一个环，称为循环队列。

![](http://7xnwyt.com1.z0.glb.clouddn.com/Algorithm1-140G32234251B.jpg)

这里需要注意，循环队列队空和队满的判断条件是什么呢？显然，队空的条件是 `Q.front == Q.rear`。但是，队满的判断条件也是`Q.front == Q.rear`，我们需要一种策略来区分队空还是队满，一般有三种解决策略:

- 队满条件为 `(Q.rear+1)%MaxSize == Q.front`， 即牺牲一个单元来区分队空和队满。队空的条件为`Q.front == Q.rear`
- 类型中增设表示元素个数的数据成员，这样，队空的条件为`Q.size == 0` ，队满的条件为`Q.size == MaxSize`。 这两种情况都有`Q.front == Q.rear`
- 类型中增设tag数据成员，以区分是队满还是队空。tag等于0的情况下，若因删除导致`Q.front == Q.rear`则为队空；tag等于1的情况下，若因插入导致`Q.front == Q.rear`则为队满。

## 操作

### 初始化

```c
void InitQeueu(&Q){
  Q.rear = Q.front = 0;
}
```

### 判队空

```c
bool isEmpty(Q){
  if(Q.rear == Q.front) return true;
  else return false;
}
```

### 入队

```c
bool EnQueue(SqQueue &Q, ElemType x){
	if((Q.rear +1)%MaxSize == Q.front) return false;
  	Q.data[Q.rear] = x;
  	Q.rear = (Q.rear + 1)%MaxSize;
  	return true;
}
```

### 出队

```c
bool DeQueue(SqQueue &Q, ElemType &x){
  if(Q.rear == Q.front) return false;
  x = Q.data[Q.front];
  Q.front = (Q.front + 1)%MaxSize;
  return true;
}
```

# 队列的链式存储

队列的链式表示称为链队列，它实际上是一个同事带有队头指针和队尾指针的单链表。头指针指向队头结点，尾指针指向队尾结点，即单链表的最后一个节点。

![](http://static.oschina.net/uploads/space/2014/0917/135018_e6eq_1469576.png)

## 双端队列

![](http://interactivepython.org/courselib/static/pythonds/_images/basicdeque.png)

