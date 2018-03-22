# RNN

![](http://www.wildml.com/wp-content/uploads/2015/09/rnn.jpg)

### 计算步骤

- $x_t$是时间$t$的输入。
- $s_t$是隐层在时间t的状态值。该值也称为“**记忆**”，它的值取决于$s_{t-1}$和$x_t$，即$s_t=f(Ux_t+W_{s_{t-1}})$，这个激活函数通常选择tanh和ReLU。$s_{-1}$通常初始化为0。
- $o_t$是我们在时间t的输出，它通常是在词汇表上的softmax：$o_t = softmax(V_{s_t})$。

### 特性

- 网络结构有$U,V,W$三个参数，这三个参数在每个时刻共享。

### 类型

- Elman Network 上一个时间点的隐层输出到下一个时间点
- Jordan Network 上一个时间点的输出层接到下一个时间点

### 应用

- **语言建模和文本生成**
  - 给定一个文本，我们想根据之前的一些单词预测后面出现的单词。语言模型可以给出该句子的概率。
- **机器翻译**
  - ![](http://www.wildml.com/wp-content/uploads/2015/09/Screen-Shot-2015-09-17-at-10.39.06-AM-1024x557.png)
- **语音识别**
- **生成图片描述**

### 训练

RNN的训练方式也是通过反向传播，但是和传统神经网络训练过程不同的是，我们在计算当前时刻的梯度的时候，需要考虑之前时刻的值。例如，t=4，我们需要反向传播3步，然后把所有的gradient加起来。这种方式成为**Backpropagation Through Time(BPTT)。**但是，在RNN训练的过程中，会出现梯度消失和梯度爆炸的问题。

## Bidirectional RNNs

## Deep(Bidirectional) RNNs

