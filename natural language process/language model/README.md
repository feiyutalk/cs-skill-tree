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

可能出现0的问题。使用平滑解决这些操作。

## 平滑

无论有多少数据，平滑几乎总是可以以很小的代价来提高performance。

- **+1** 平滑：$P_{add}(w_i|w_{i-1},w_{i-2})=\frac{\delta+count(w_{i-2},w_{i-1},w_i)}{\delta|V|+\sum_{w_i}}count(w_{i-2},w_{i-1},w_i)$（**政法发钱**）
  - 在分类问题中可能有用，但是在语言模型中表现一般；
- **Back-off** 回退法：使用Trigram如果count(trigram)满足一定的条件；否则使用Bigram；否则使用Unigram；（**自己有钱自己出，自己没钱爸爸出，爸爸没钱爷爷出**）
- **Interpolate**插值法：将Trigram，Bigram，Unigram线性组合起来（**自己 爸爸 爷爷都出一点**）：
  - $P_{int}(w_i|w_{i-1},w_{i-2})=\lambda_3P_{ML}(w_i|w_{i-1},w_{i-2})+\lambda_2P_{ML}(w_i|w_{i-1})+\lambda_1P_{ML}(w_i),\lambda_3+\lambda_2+\lambda_1=1$
  - 需要验证集来求$\lambda_1,\lambda_2,\lambda_3$，使用极大似然估计法
- **Absolute Discounting**绝对折扣：
- **Kneser-Ney Smoothing**

|          模型          |       简单理解       |       只需要记住        |
| :------------------: | :--------------: | :----------------: |
|        +1 平滑         |       政府发钱       |         没用         |
|       Backoff        |      用爸爸的钱       |                    |
|     Interpolate      |     自己和爸爸都出点     | Development Set;EM |
| Absolute Discounting | 有钱人缴固定税，按爸爸的资产分配 |                    |
|      Kneser-Ney      | 有钱人缴固定税，按爸爸人脉分配  |       词的适配度        |
|     Modified KN      | 有钱人缴阶梯税，按爸爸人脉分配  |     阶梯税率，最好的方法     |

