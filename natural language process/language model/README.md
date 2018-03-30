# 语言模型

语言模型本质上就是对语言的评分：$Score(语言)$

话题模型：$Score(话题|语言)$

## 概率语言模型

概率语言模型需要满足两个条件：

- $P(sentence) = P(w_1,w_2,…,w_n)$
- $\sum_{sentence \in L}P(sentence)=1$

核心就是通过分数来告诉机器怎么说人话。

### N-gram LM

**一个法则**

$P(w_1,w_2,…,w_n) = P(w_1)P(w_2|w_1)…P(w_n|w_1,…,w_{n-1})$

**一个假设**

马尔科夫假设：未来的事件，只取决于有限的历史

**多种情形**

$P(w_5|w_4,w_3,w_2,w_1)$

- unigram $P(w_5)$
- bigram $P(w_5|w_4)$
- trigram $P(w_5|w_4,w_3)$

### RNN LM

不用马尔科夫假设

## 评价指标

$Perplexity(W_{test})=2^{-\frac{1}{N}\sum_{i=1}^Nq(w_i)}=2^{-\sum_{i=1}^{|V|}\frac{count(V_i)}{N}q(v_i)}=2^{-\sum_{i=1}^{|V|}p(v_i)q(v_i)}$

## Out of Vocabulary

可能出现0的问题。



