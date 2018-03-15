# CAS(Compare-and-swap)

In [computer science](https://www.wikiwand.com/en/Computer_science), **compare-and-swap** (**CAS**) is an [atomic](https://www.wikiwand.com/en/Atomic_(computer_science)) [instruction](https://www.wikiwand.com/en/Instruction_(computer_science)) used in [multithreading](https://www.wikiwand.com/en/Thread_(computer_science)#Multithreading) to achieve [synchronization](https://www.wikiwand.com/en/Synchronization_(computer_science)). It compares the contents of a memory location with a given value and, only if they are the same, modifies the contents of that memory location to a new given value.

```c
int compare_and_swap(int* reg, int oldval, int newval)
{
  ATOMIC();
  int old_reg_val = *reg;
  if (old_reg_val == oldval)
     *reg = newval;
  END_ATOMIC();
  return old_reg_val;
}
```

### CAS的问题：

Some CAS-based algorithms are affected by and must handle the problem of a [false positive](https://www.wikiwand.com/en/Type_I_error#False_negative_vs._false_positive) match, or the [ABA problem](https://www.wikiwand.com/en/ABA_problem). It is possible that between the time the old value is read and the time CAS is attempted, some other processors or threads change the memory location two or more times such that it acquires a bit pattern which matches the old value. 

解决的方式一般都是多设置一个计数器或者说设置一个版本号。