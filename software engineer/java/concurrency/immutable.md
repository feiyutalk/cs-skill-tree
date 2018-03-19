# 不可变对象

不可变对象一定是线程安全的，可变对象不一定是不安全的。

- 属性定义为private final
- 不提供任何改变这个变量的方法
- 不让子类继承，即类定义为final

在JDK中有哪些是不可变的对象呢？

- String

谈到了String，我们来讲一讲String，StringBuffer和StringBuilder的区别：

1. 三者中，只有String是不可变的，StringBuffer和StringBuilder都是可变的。
2. 三者中，String和StringBuffer都是线程安全的，StringBuilder不是线程安全的。前两者保证线程安全的方式不一样，其中String是通过不可变对象来保证的，而StringBuffer是通过synchronized关键字进行加锁保证的，所以，StringBuffer效率比较低。