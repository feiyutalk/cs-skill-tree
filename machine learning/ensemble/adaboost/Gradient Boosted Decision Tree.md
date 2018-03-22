# GBDT

基于Adaboost-DTree，我们先看一下AdaBoost-DTree的损失函数:

$min_{\eta} min_h \frac{1}{N}\sum_{n=1}^{N}exp(-y_n(\sum_{\tau=1}^{t-1}\alpha_\tau g_\tau (x_n) + \eta h(x_n)))$

然后，我们想， 我们可不可以修改损失函数，得到另外一个模型呢？答案是可以的，我们定义损失函数为：

$min_{\eta} min_h \frac{1}{N}\sum_{n=1}^{N}err(\sum_{\tau=1}^{t-1}\alpha_\tau g_\tau (x_n) + \eta h(x_n), y_n)$

对于不同的任务，我们可以设定不同的损失函数：

### 回归任务

![](./images/10.png)

回归任务中的损失函数可以是哪些呢？

- **Least squares**：$r_i = y_i - f(x_i, b) , S=\sum_{i=1}^n r_i^2$  
- **Least absolute deviation**：$S = \sum_{i=1}^n|y_i-f(x_i)|$
- **Huber**：
  - ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/21983befe82b2509d1bb8dfa1064a35b6031d508)
- **Quantile**

### 分类任务

作为分类任务中的损失函数是哪些呢？

- **Binomial deviance**：负的极大似然
- **Multinomial deviance**
- **Exponential loss** ：和AdaBoostClassifier类似

### 特点

- 优点
  - 可以处理混合特征类型
  - 强大的预测能力
  - 对异常点鲁棒性强
- 缺点
  - 可扩展性差，因为其训练的过程是串行化的，没有办法并行化