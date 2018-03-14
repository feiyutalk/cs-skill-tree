# 支持向量机实战

基于`scikit-learn`的实现。

### 优点：

- 在高维度空间中仍然效率很高。
- 即便是样本维度大于样本数量，算法仍然有效。
- 空间复杂度低，只需要存储支持向量即可。
- 不同的核函数可用于不同的决策函数，还可以定义自己的核函数。

### 缺点：

- 如果样本特征维度过高，容易发生过拟合。
- 不能直接计算概率值。

### 输入:

- X : `[n_samples, n_features]`
- Y : `[n_samples]`

### 获取支持向量信息:

```python
>>> # get support vectors
>>> clf.support_vectors_
array([[ 0.,  0.],
       [ 1.,  1.]])
>>> # get indices of support vectors
>>> clf.support_ 
array([0, 1]...)
>>> # get number of support vectors for each class
>>> clf.n_support_ 
array([1, 1]...)
```

