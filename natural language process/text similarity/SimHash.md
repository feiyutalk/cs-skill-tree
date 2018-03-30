![](http://7viirv.com1.z0.glb.clouddn.com/simhash.jpg)

### 算法过程

1. 将Doc进行关键词抽取（其中包括分词和计算权重），抽取n个（关键词，权重）对，即图中的`(feature, weight)`，记为`feature_weight_pairs=[fw1, fw2,...,fwn]`，其中`fwn=(feature_n, weight_n)`。
2. `hash_weight_pairs=[hash(feature), weight] for feature, weight in feature_weight_pairs]`生成`(hash, weight)`。
3. 然后对 `hash_weight_pairs` 进行位的纵向累加，如果该位是1，则`+weight`,如果是0，则`-weight`，最后生成`bits_count`个数字，如图所示是`[13, 108, -22, -5, -32, 55]`, 这里产生的值和hash函数所用的算法相关。
4. `[13,108,-22,-5,-32,55] -> 110001`这个就很简单啦，正1负0。

### 海明距离计算

二进制串A和二进制串B的海明距离就是`A xor B`后二进制中1的个数。

```python
A = 100111;
B = 101010;
hamming_distance(A, B) = count_1(A xor B) = count_1(001101) = 3;
```

### 特点

- 需要一种应对于海量数据场景的去重方案，该算法能够把文档降维到hash数字，数字两两计算运算量要小很多。
- simhash的发明人Charikar的论文中并没有给出具体的simhash算法和证明，“量子图灵”得出的证明simhash是由随机超平面hash算法演变而来的。