# 图

## 定义

> 图G由顶点集V和边集E组成，记为 G=(V,E)，其中V(G)表示图G中顶点的有限非空集；E(G)表示图G中顶点之间的关系(边)集合。若$V={v_1, v_2, …, v_n}$，用$|V|$表示图G中顶点的个数，也称为图G的阶，$E={(u, v)|u \in V, v \in V}$，用$|E|$表示图G中边的条数。

### 有向图

![](http://images2015.cnblogs.com/blog/816310/201705/816310-20170518185314041-751743590.jpg)

### 无向图

![](http://7xospc.com1.z0.glb.clouddn.com/7-2-2.jpg)

### 简单图

- 不存在重复边
- 不存在顶点到自身的边

### 多重图

- 图G中某两个节点之间的边数多于一条。

### 完全图

含有n个顶点$n(n-1)/2$条边。

### 子图

### 连通图

任意两个顶点都是连通（即任意两个顶点之间存在路径）

### 连通分量

是极大连通子图，要求连通，并且包含所有的边。

### 极小连通子图

保持图连通，又要使边数最少。

### 生成树、生成森林

包含图中全部顶点的一个极小连通子图。若图中顶点数为n，则它的生成树包含n-1条边。

### 网

边上带有权值的图称为带权图，也称作网。

### 路径、路径长度和回路

顶点序列。

### 距离

从顶点u出发到顶点v的最短路径若存在，则此路径的长度称作从u到v的距离。

## 存储结构

### 邻接矩阵

![](http://www.educity.cn/zk/sjjg/images/95.jpg)

### 邻接表

![](http://kjwy.5any.com/sjjg/content/sjjg07/image/image0203005.jpg)

### 十字链表

![](http://c.biancheng.net/cpp/uploads/allimg/120223/1-120223224210X3.jpg)

![](http://c.biancheng.net/cpp/uploads/allimg/120223/1-120223224315394.jpg)

### 邻接多重表

![](http://5b0988e595225.cdn.sohucs.com/images/20170913/cc2e09910c4e401a9d4d1d73fb08a1c2.jpeg)

## 遍历

- 有可能非连通
- 访问过的有可能还会被访问

### 广度优先搜索

```c
bool visited[MAX_VERTEX_NUM];
void BFSTraverse(Graph G){
  for(i =0; i<G; i++)
    visited[i] = FALSE;
  InitQueue(Q);
  for(i=0; i<G.vexnum; i++)
    if(!visited[i])
      BFS(G, i);
}

void BFS(Graph G, int v){
  visit(v);
  visited[v] = TRUE;
  Enqueue(Q, v);
  while(!isEmpty(Q)){
    for(w = FirstNeighbor(G, v); w>=0; w=NextNeighbor(G,v w)){
      if(!visited[w]){
        visit(w);
        visited[w]=TRUE;
        EnQueue(Q, w);
      }
    }
  }
}
```

### 深度优先遍历

#### 递归

```c
bool visited[MAX_VERTEX_NUM];
void DFSTraverse(Graph G){
  for(v=0;v<G.vexnum; v++){
    visited[v] = FALSE;
  }
  for(v=0;v<G.vexnum; v++){
    if(!visited[v])
      DFS(G, v);
  }
}
void DFS(Graph G, int v){
  visit(V);
  visited[v] = TRUE;
  for(w=FirstNeighbor(G,v);w>=0;w=NextNeighbor(G,v,w))
    if(!visited[w])
      DFS(G, w);
}
```

#### 非递归

```c
void DFS_Non_RC(Graph& G, int v){
  int w;
  InitStack(S);
  for(i=0; i<G.vexnum; i++)
    visited[i] = FALSE;
  Push(S, v);
  visited[v] = TRUE;
  while(!IsEmpty(S)){
    k = Pop(S);
    visit(k);
    for(w=FirstNeighbor(G, k); w>=0; w=NextNeighbor(G, k, w))
      if(!visited[w]){
        Push(S, w);
        visited[w] = true;
      }
  }
}
```

## 应用

### 最小生成树

#### Prim算法

![](http://images2015.cnblogs.com/blog/679880/201604/679880-20160420211808460-1390498636.png)

```c
void prim(Graph G, int start){
  int min,i,j,k,m,n,sum;
  int index = 0;
  char prims[MAX];
  int weights[MAX];
  
  prims[index++] = G.vexs[start];
  
  for(i=0; i<G.vexnum; i++){
    weights[i] = G.matrix[start][i];
  }
  weights[start] = 0;
  
  for(i=0; i<G.vexnum; i++){
    if(start == i)
      continue;
    j=0;
    k=0;
    min = INF;
    while(j < G.vexnum){
      if(weights[j] != 0 && weights[j] < min){
        min = weights[j];
        k = j;
      }
      j++;
    }
    prims[index++] = G.vexs[k];
    weights[k] = 0;
    for(j = 0; j<G.vexnum; j++){
      if(weights[j] != 0 && G.matrix[k][j] < weights[j])
        weights[j] = G.matrix[k][k];
    }
  }
}
```

### 克鲁斯卡尔算法

![](http://c.biancheng.net/cpp/uploads/allimg/120223/1-120223233052I4.jpg)

### 最短路径

![](http://upload-images.jianshu.io/upload_images/1388564-aa20d024f0faceae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Floyd算法

```c
        for(k=1;k<=n;k++)
            for(i=1;i<=n;i++)
                for(j=1;j<=n;j++)
                    if(e[i][j]>e[i][k]+e[k][j] )
                        e[i][j]=e[i][k]+e[k][j];
```



![](http://7xospc.com1.z0.glb.clouddn.com/7-7-15.jpg)

### 拓扑排序

### 关键路径



