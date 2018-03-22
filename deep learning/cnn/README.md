# CNN

### 卷积层

- feature map大小的计算公式
  - 图片长度为 $n_{in}$
  - filter长度为 $n_{filter}$
  - 步长为 $p$
  - padding为 $n_{padding}$
  - 输出 : **$n_{out} = (n_{in} + 2*n_{padding} -n_{filter}) + 1$**
- 宽卷积和窄卷积：宽卷积就是有填充的；窄卷积没有填充。

#### 通道

通道代表着你观测数据的不同维度，在图像中，你可能有RGB(red, green, blue)三个通道。同样的，在自然语言处理中，我们也可以对同一个句子使用不同的通道。

### 池化层

![](http://www.wildml.com/wp-content/uploads/2015/11/Screen-Shot-2015-11-05-at-2.18.38-PM.png)

- 池化层可以输出固定大小的矩阵；比如说你要偶1000个filter，然后你对每个filter后的结果进行max池化操作，那么你就可以得到1000维度的向量，不管每个filter的大小为多少。**这意味着，通过池化操作，你可以使用不同的sentence，不同的filter，最后得到相同维度的输出。**
- ​