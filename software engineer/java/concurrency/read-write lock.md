# 读写锁

读写分离，提高效率；

1. read read 并行化
2. read write 不允许
3. write write 不允许

|           | READ | WRITE |
| :-------: | :--: | :---: |
| **READ**  |  NO  |  YES  |
| **WRITE** | YES  |  YES  |

