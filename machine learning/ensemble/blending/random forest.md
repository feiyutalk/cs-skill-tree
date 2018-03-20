## Random Forest

在模型融合里，blending方式通过组合不同模型投票的结果，来使得融合后的模型variance变小。而决策树，通过variance比较大，我们是否能够结合这两种思路呢？答案是可以，这就是随机森林。

Random Forest(RF) = bagging + fully-grown C&RT decision tree.

基本做法：

1. 通过Bootstrap的方式取得不同数据和特征，输入到决策树中训练得到不同的决策树。
2. 组合不同的决策树，构成最终的分类器。

随机性的体现：

1. Bootstrap采用
2. 特征投影
   1. 选择不同的特征
   2. 随机的方向

### 特征选择

假设我们资料里面特征具有依赖性，比如生日和年龄（用生日可以推出年龄），或者说有一些特征对于最后的分类结果没有什么作用。

如果模型是线性的，那么我们通过w分量大小就可以判断出哪个模型比较重要，因为$score = wx​$，但是如果是非线性的模型，那么这个问题就比较复杂，但是Random Forest由于其模型的特性，也可以用来做特征选择。

##### permutation test进行特征重要性衡量:

- 对于第i个特征的所有样本，我们进行重排列（即甲的身高值给乙的身高值，乙的身高值给甲的身高值）。

- 计算重排序后的**performance**：

  - $importance(i) = performance(D) - performance(D^p)$ with $D^p$ is D with $\{x_n, i\}$ replaced by permuted $\{x_n, i\}_{n=1}^N$
  - 正常来说，performance应该怎么得到呢？我们应该对资料为D的模型进行训练，然后获得交叉验证的结果，作为performance(D)。并且对资料为$D^p$的模型进行训练，然后获得交叉验证的结果，作为performance($D^p$)。**注意**，由于训练样本的获取是采样bootstrap，所以可以利用out-of-bag样本做验证集。即，上面的式子就变成了 importance(i) = $E_{oob}(G) - E_{oob}(G^p)$
  - 但是，原始的随机森林的作者， 提出了在验证的过程中做permutation而不是训练的过程中，这样的话，我们只需要做一次训练，两次验证即可。这样的话，结果就变成了importance(i) = $E_{oob}(G) - E_{oob}^p(G)$

  ​