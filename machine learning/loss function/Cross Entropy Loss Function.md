## Cross-Entropy交叉熵

![cross_entropy](http://p6sh0jwf6.bkt.clouddn.com/2018-04-08-024353.jpg)

### 数学表达式

- **二分类：**$−(ylog(p)+(1−y)log(1−p))$
- **分多类：**$-\sum_{c=1}^My_{o,c}\log(p_{o,c})$
  - $M$——类别的数量；
  - $y$——指示变量（0或1）,如果该类别和是观测到的类别就是1，否则是0；
  - $p$——对于观测样本属于类别c的预测概率

### 求偏导

![cross entroy求偏导1](http://p6sh0jwf6.bkt.clouddn.com/2018-04-08-024227.jpg)

![cross entroy求偏导2](http://p6sh0jwf6.bkt.clouddn.com/2018-04-08-024224.jpg)

![cross entroy求偏导3](http://p6sh0jwf6.bkt.clouddn.com/2018-04-08-023911.jpg)

# 参考

[1]. [MLCheatsheet](http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html)

[2]. [softmax function](http://sefiks.com/2017/11/08/softmax-as-a-neural-networks-activation-function/)

[3]. [cross entropy loss function](https://sefiks.com/2017/12/17/a-gentle-introduction-to-cross-entropy-loss-function/)