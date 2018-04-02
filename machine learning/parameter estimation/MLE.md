# 最大似然估计MLE

$L(\theta|X)=p(X|\theta)=\prod_{x\in X}p(X=x|\theta)$

由于有连乘运算，通过对似然函数取对数计算，即对数似然函数：

$\hat{\theta}_{ML}=argmax_{\theta}L(\theta|X)=argmax_{\theta}\sum_{x\in X}logp(x|\theta)$

这是一个关于$\theta$的函数，求解这个优化问题通常对$\theta$求导，得到导数为0的极值点，该函数取得最大值是对应的$\theta$的取值就是我们估计的模型参数。