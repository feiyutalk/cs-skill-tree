# Resilient Distributed Dataset

- 弹性分布式数据集是可以被划分到集群中各个节点上并行工作的数据集。
- 共享变量是需要在不同子问题中共享的变量。
  - **广播变量**：该变量值被缓存到所有节点的内存中。
  - **accumulators**：该变量只是用来添加。

## 操作

### 转化 transformation

