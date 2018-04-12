# ThreadLocal

- 可以理解为用HashMap存储数据，Key是Thread，Value是数据。
- 通过重写`initialValue`方法来定义初始值。
- 可以用于线程上下文带来的参数传递。

