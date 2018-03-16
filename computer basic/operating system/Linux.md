## Linux的文件权限与目录配置

### 1. 用户与用户组

- 文件所有者
- 用户组
- 其他人

### 2. 文件权限

- #### **Linux文件属性**

  - **查看** `ls -al` `-rw-r--rr 1 root root 42304 Sep 4 18:26 install.log`

    - 第一个字符代表这个文件是“目录、文件或链接文件”
      - [d] 目录
      - [-] 文件
      - [l] 连接文件
      - [b] 接口设备
      - [c] 串行端口设备
    - 接下来三组三个字符
      - 第一组 “文件所有者的权限”
      - 第二组 “同用户组的权限”
      - 第三组 “其他非本用户组的权限”
    - 第二列表示文件的连接数
    - 第三列 这个文件的“所有者账号”
    - 第四列 这个文件的所属用户组
    - 第五列 文件的容量大小
    - 第六列 创建日期或修改日期
    - 第七列 文件名

  - **修改权限**

    - `chgrp` 改变文件所属用户组
    - `chown` 改变文件所有者
    - `chmod` 改变文件的权限

  - **目录与文件的权限意义**

    - |      |       文件        |                    目录                    |
      | :--: | :-------------: | :--------------------------------------: |
      |  r   |      读取此文件      |              具有读取目录结构列表的权限               |
      |  w   |     修改文件内容      | 具有更改该目录结构列表的权限:<br />新建新的文件与目录；<br />删除已经存在的文件与目录；<br />将已存在的文件或目录进行重命名;<br />转移该目录的文件、目录位置 |
      |  x   | 该文件具有可以被系统执行的权限 |             用户能否进行该目录称为工作目录              |

  - **Linux文件种类与扩展名**

    - |         |                                          |
      | :-----: | :--------------------------------------: |
      |  普通文件   |            纯文本文件；二进制文件；数据格式文件            |
      |   目录    |                   [d]                    |
      |  连接文件   |                   [l]                    |
      | 设备与设备文件 | 在/dev目录下：**块设备文件/dev/sda；字符设备文件[c] 串行端口** |
      |   套接字   |          网络上的数据连接 [s] /var/run           |
      |   管道    |          解决多个程序同时访问一个文件所造成的错误问题          |

  - **目录树**

    - |                              |                            |
      | :--------------------------: | :------------------------: |
      |              /               |           开机系统有关           |
      | /usr(Unix software resourse) |         软件安装、执行有关          |
      |        /var（variable）        |         与系统运作过程有关          |
      |             /bin             |     单用户维护模式下还能够被操作的命令      |
      |            /boot             |         开机会使用到的文件          |
      |             /dev             |            设备文件            |
      |             /etc             |          系统的配置文件           |
      |            /home             |           用户主文件夹           |
      |             /lib             |         开机时用到的函数库          |
      |            /media            |           可删除的设备           |
      |             /mnt             |          暂时挂载的设备           |
      |             /opt             |         第三方软件放置的目录         |
      |            /root             |         系统管理员的主文件夹         |
      |            /sbin             | 开机过程中所有的，开机、修复、还原系统所需要的命令  |
      |             /srv             |  网络服务启动之后，这些服务所需要去用的数据目录   |
      |             /tmp             |            临时目录            |
      |         /lost+found          | 当文件系统发生错误，将一些丢失的片段放置在这个目录下 |
      |            /proc             |           虚拟文件系统           |
      |             /sys             |     虚拟文件系统，记录与内核相关的信息      |

      ​

  ## Linux文件与目录管理

  ### 目录的相关操作

  - `cd` 切换目录
  - `.` 代表此层目录
  - `..` 代表上一层目录
  - `-` 代表前一个工作目录
  - `~` 代表家目录
  - `pwd` 显示当前目录
  - `mkdir` 新建一个新的目录
  - `rmdir` 删除一个空的目录

  ### 执行文件路径的变量 $PATH

  - 不同身份用户默认的PATH不同，默认能够随意执行的命令也不同
  - PATH是可以修改的，所以一般用户还是可以通过修改PATH来执行某些位于`/sbin`或 `/usr/sbin`下的命令来查询

  ### 文件和目录管理

  - `ls` 查看文件与目录
  - `cp` `rm` `mv`
  - `basename` 取得文件名
  - `dirname` 取得目录名

  ### 文件内容查阅

  - `cat` 从第一行开始显示文件内容
  - `tac` 从最后一行开始显示
  - `nl` 显示的时候，顺便输出行号
  - `more` 一页一页的显示文件内容
  - `less` 与more类似，但是比more更好的是，它可以往前翻页
  - `head` 只看头几行
  - `tail` 只看结尾几行
  - `od` 以二进制的方式读取文件内容

  ### 修改文件时间或创建新文件 touch

  - mtime ： 当该文件的“内容数据”更改时，就会更新这个时间。内容数据指的是文件的内容，而不是文件的属性或权限。
  - status time : 当该文件的状态改变时，就会更新这个时间，举例来说，像是权限与属性被更改了，就都会更新这个时间。
  - access time : 当“该文件的内容被取用”时，就会更新这个读取时间。

  **默认情况下，ls显示出来的是该文件的mtime，也就是这个文件的内容上次被更改的时间。**

  ### 文件默认权限 ： umask

  默认权限为 777，umask显示的分数为“**该默认值需要减掉的权限”**

  ### 查看文件类型

  - file

  ### 命令与文件的查询

  - `which` 寻找执行文件
  - `whereis` `locate` `find`寻找特定文件 

  ### 权限和命令间的关系

  - 让用户能进入目录成为“可工作目录”的基本权限是什么？
    - 可使用的命令：例如`cd`等切换工作目录的命令。
    - 目录所需权限：用户对这个至少需要具有`x`的权限。
    - 额外需求：如果用户想要在这个目录内利用`ls`查阅文件名，则用户对此目录还需要`r`的权限。

## Linux磁盘与文件系统管理

### 文件系统特性

文件系统通常会文件数据和文件属性这两部分的数据分别存放在不同的块，权限与属性放置到`inode`中，至于实际数据则放置到`data block`块中。另外还有一个`超级块`会记录整个文件系统的整体信息，包括`inode`与`block`的总量、使用量、剩余量。

![](data:image/png;base64,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)

- **Superblock** : 记录此文件系统的整体信息，包括inode/block的总量，使用量，剩余量，以及文件系统的格式与相关信息等；
  - block与inode的总量；
  - 未使用和已使用的inode/block的总量；
  - block与inode的大小；
  - 文件系统的挂载时间、最近一次写入数据的时间、最近一次检验磁盘的时间等；
- **文件系统描述说明：**这个区段可以描述每个block group的开始于结束的block号码，以及说明每个区段分别介于哪一个block号码之间。
- **block bitmap:**
  - 从block bitmap中可以知道哪些block是空的。
- **inode bitmap:**
  - 记录未使用的inode号码。
- **inode** : 记录文件的属性，一个文件占用一个inode，同时记录此文件的数据所在的block号码；
  - 该文件的访问模式；
  - 该文件的所有者与组；
  - 该文件的大小；
  - 该文件创建或状态改变的时间；
  - 最近一次的读取时间；
  - 最近修改的时间；
  - 定义文件特性的标志，如SetUID；
  - 该文件真正内容的指向；
  - 每个inode大小均固定为**128bytes**；
  - 文件系统能够创建的文件数量与inode的数量有关；
  - 系统读取文件时需要先找到inode，并分析inode所记录的权限与用户是否符合，若符合才能够开始实际读取block的内容；


- **block**：实际记录文件的内容，若文件太大时，会占用多个block。

属于索引式文件结构，先找到`inode`，然后从`inode`中找到对应的`block`。

- **Inodetable**

![](https://tech.meituan.com/img/about-desk-io/inode%E7%BB%93%E6%9E%84%E7%A4%BA%E6%84%8F%E5%9B%BE.png)