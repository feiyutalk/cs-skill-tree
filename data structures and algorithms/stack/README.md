# 栈

## 定义

> 只允许在一端进行插入和删除操作的线性表。首先栈是一种线性表，但是限定这种线性表只能在某一端进行插入和删除操作。

![](http://img.blog.csdn.net/20150508103631436)

由此可见，栈的一个明显的操作特性可以概括为后进先出，故又称为后进先出的线性表。

## 基本操作

```c
InitStack(&S)	初始化一个空栈S
StackEmpty(S)	判断一个栈是否为空，若栈S为空则返回true，否则返回false
Push(&S, x)		进栈，若栈S未满，将x加入使之成为新栈顶
Pop(&S, &x)		出栈，若栈S非空，弹出栈顶元素，并用x返回
GetTop(S, &x)	读栈顶元素，若栈S非空，用x返回栈顶元素
```

# 栈的顺序存储结构

栈的顺序存储称为顺序栈，它是利用一组地址连续的存储单元存放自栈底到栈顶的数据元素，同时附设一个指针(top)指示当前栈顶的位置。

![](http://img.blog.csdn.net/20160421103403950)

## 顺序栈的实现

```c
#define MaxSize 50
typedef struct{
  Elemtype data[MaxSize];
  int top;
}SqStack;
```

### 初始化

```c
void InitStack(&S){
  s.top= -1;
}
```

### 判栈空

```c
bool StackEmpty(S){
  if(s.top == -1)
    return true;
  else
    return false;
}
```

### 进栈

```c
bool Push(SqStack &S, ElemType x){
  if(S.top == MaxSize - 1)
    return false;
  s.data[++S.top] = x;
  return true;
}
```

### 出栈

```c
bool Pop(SqStack &S, ElemType &x){
  if(S.top == -1)
    return false;
  x = S.data[S.top--];
  return true;
}
```

### 读栈顶元素

```c
bool GetTop(SqStack S, ElemType &x){
  if(S.top == -1)
    return false;
  x = S.data[S.top];
  return true;
}
```

## 共享栈

利用栈底位置相对不变的特性，可以让两个顺序栈共享一个一维数据空间，将两个栈的栈底分别设置在共享空间的两端，两个栈顶向共享空间的中间延伸。

![](http://img.blog.csdn.net/20150414175754134?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTGl1a3g5NDA4MTg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

# 栈的链式存储结构

采用链式存储的栈称为链栈，链栈的有点是便于多个栈共享存储空间和提高其效率，且不存在栈满上溢的情况。通过采用单链表实现，并规定所有操作都是在单链表的表头进行的。

![](http://img.blog.csdn.net/20160506172449046?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

