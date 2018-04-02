## probabilistic Latent Semantic Analysis

增加了主题模型，形成简单的贝叶斯网络。

### 模型

$P(d_i, w_j)=P(w_j|d_i)P(d_i)$，$P(w_j|d_i)=\sum_{k=1}^KP(w_j|z_k)P(z_k|d_i)$

其中，$P(z_k|d_i)$对应的是每个文档的主题分布，$P(w_j|z_k)$对应的是每个主题的词分布。

### 估计

记$w_j$在$d_i$中出现的次数为：$n(d_i,w_j)$

$L=\prod_{i=1}^N \prod_{j=1}^MP(d_i,w_j)=\prod_{i=1} \prod_{j=1}P(d_i,w_j)^{n(d_i,w_j)}$

$l=\sum_i\sum_jn(d_i,w_j)logP(d_i,w_j)$

$=\sum_i\sum_jn(d_i,w_j)log(P(w_j|d_i)P(d_i))$

$=\sum_i\sum_jn(d_i,w_j)logP(w_j|d_i)+\sum_i\sum_jn(d_i,w_j)logP(d_i)$

可以发现，$\sum_i\sum_jn(d_i,w_j)logP(d_i)$和参数没有关系，在优化的过程中不需要考虑这一项；

 $l_{new}=\sum_i\sum_jn(d_i,w_j)logP(w_j|d_i)$ $=\sum_i\sum_jn(d_i,w_j)log(\sum_{k=1}^KP(w_j|z_k)P(z_k|d_i))$

- 观测数据为$(d_i, w_j)​$对，主题$z_k​$是隐含变量。
- 使用逐次逼近的办法，即EM算法：
  - 求隐变量$z_k$的后验概率：$P(z_k|d_i,w_j)=\frac{P(w_j|z_k)P(z_k|d_i)}{\sum_{l=1}^KP(w_j|z_l)P(z_l|d_i)}$
  - 在$(d_i, w_j, z_k)$已知的前提下，求关于参数$P(z_k|d_i)、P(w_j|z_k)$的似然函数期望的极大值，得到最优解$P(z_k|d_i)、P(w_j|z_k)$，带入上一步，从而循环迭代。









