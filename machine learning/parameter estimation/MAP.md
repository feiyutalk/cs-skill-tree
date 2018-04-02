# 最大后验估计MAP

最大后验估计与最大似然估计相似，不同点在于估计$\theta$的函数中允许加入一个先验$p(\theta)$，也就是说此时不是要求似然函数最大，而是要求由贝叶斯公式计算出的整个后验概率最大，即：

$\hat{\theta}_{MAP}=argmax_{\theta}\frac{p(X|\theta)p(\theta)}{p(X)}=argmax_{\theta}p(X|\theta)p(\theta)=argmax_{\theta}{L(\theta|X)+logp(\theta)}$

$=argmax_{\theta}\{\sum_{x\in X}logp(x|\theta)+logp(\theta)\}$

这里$P(X)$与参数$\theta$无关，因此等价于要使分子最大，与最大似然估计相比，现在需要多加上一个先验分布概率的队伍。在实际应用中，这个先验可以用来描述人们已经知道或者接受的普遍规律。先验分布的参数我们称为超参数。



