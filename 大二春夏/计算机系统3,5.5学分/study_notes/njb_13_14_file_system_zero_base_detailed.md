# 13-14 文件系统接口、实现与实践：零基础完整讲解

这份笔记覆盖三份 PPT：

- `13_fs_interface.pdf`：文件系统接口，也就是用户和程序眼里的“文件、目录、权限、访问方式”。
- `14_fs_implementation.pdf`：文件系统实现，也就是操作系统内部如何把“文件名、inode、目录、磁盘块、缓存、VFS”组织起来。
- `14_fs_in_practice.pdf`：文件与目录实践，也就是 Linux 里 `open`、文件描述符、`stat`、`link`、`unlink`、`fsync`、硬链接和软链接真正长什么样。

这份优化版不是只把 PPT 内容翻译一遍，而是按期末考试真正会考的理解方式来组织：

- 先讲“这个概念解决什么问题”，避免只背名词。
- 再讲“操作系统为什么这样设计”，抓住设计权衡。
- 再讲“如果条件变化会发生什么”，训练推理题能力。
- 最后给出“考试答题抓手”，方便你在简答题、计算题、流程题里组织答案。

建议你学习时按三遍读：

1. 第一遍只看每节的定义和例子，先建立直觉。
2. 第二遍重点看“为什么”和“对比”，理解设计动机。
3. 第三遍做最后的期末拓展题和答题模板，把知识转化成考试表达。

一句话总览：

```text
用户程序看到：       文件名、路径、read/write/open/close、权限
文件系统负责：       把“名字”翻译成“inode”，把“文件偏移”翻译成“磁盘块”
底层硬件负责：       最终在磁盘、SSD、网络存储上读写 block
```

上一讲讲过大容量存储和 I/O：磁盘、SSD、磁盘调度、轮询、中断、DMA、内核 I/O 子系统。到这里，问题变成：既然我们已经有了存储硬件和 I/O 通道，用户到底应该怎样使用它？答案不是让用户直接操作磁道、扇区和块号，而是给用户一个更高层、更稳定、更安全的抽象：文件系统。

---

# 0. 先建立总图：为什么需要文件系统

如果站在 1950 年代计算机科学家的角度，手里有一块磁盘，你当然可以直接读写磁盘上的某个位置，例如“第几个盘面、第几个磁道、第几个扇区”。但这会非常痛苦：

1. 用户不想记物理位置，只想说“我要读 `main.c`”。
2. 文件可能变大、变小、删除、移动，物理位置会变化。
3. 多个用户、多进程同时使用磁盘，需要权限和隔离。
4. 程序需要一种统一接口，不希望 HDD、SSD、NFS、UFS、ext4 都用不同 API。
5. 发生断电或崩溃时，需要恢复一致性。

文件系统的作用就是在“原始磁盘块”和“用户可理解的文件/目录”之间建立抽象层：

```text
用户进程
  |
  | open("/home/alice/a.txt"), read(fd), write(fd), close(fd)
  v
文件系统接口
  |
  | 路径名 -> inode；文件偏移 -> 逻辑块；逻辑块 -> 物理块
  v
块 I/O 子系统 / 驱动 / 中断处理
  |
  v
磁盘、SSD、网络文件系统
```

PPT 第 13 讲有一个抽象问题：

```text
CPU is abstracted to ____.
Memory is abstracted to ____.
Storage is abstracted to ____.
```

可以这样理解：

- CPU 常被抽象成“进程/线程执行指令的环境”。
- 内存常被抽象成“地址空间”，尤其是虚拟地址空间。
- 存储常被抽象成“文件系统”，用户不直接操作物理扇区，而操作文件和目录。

---

# 1. 文件系统接口：用户看到的世界

## 1.1 文件是什么

PPT 定义：文件是一个用于存储信息的连续逻辑空间。

这里的“连续”不是说它在磁盘上物理连续，而是说对用户程序来说，文件像一条从 0 开始编号的字节序列：

```text
file byte offset:  0  1  2  3  4  5  6 ...
file content:      H  e  l  l  o \n ...
```

你写程序时可以从偏移 0 读取，也可以 `lseek` 到偏移 1000 再读。文件系统会隐藏“这些字节实际放在哪些磁盘块上”的细节。

文件可保存各种信息：

- 数据库文件。
- 音频。
- 视频。
- 网页。
- 程序代码。
- 可执行程序。
- 特殊文件，例如 Linux 的 `/proc` 文件系统。`/proc` 不一定真的把数据存到磁盘上，但它使用文件系统接口暴露系统信息。例如你可以读 `/proc/cpuinfo` 来获得 CPU 信息。

PPT 提到文件类型：

- data file：数据文件。
  - character：字符/文本类。
  - binary：二进制类。
  - application-specific：某个应用专用格式，例如 Word 文档、数据库文件。
- program：程序文件。
- special file：特殊文件，例如 proc file system。

初学者要记住：操作系统通常不关心一个普通文件内部到底是什么格式。Linux 更倾向于把文件看成字节流。至于这个字节流是 C 源码、ELF 可执行文件、PNG 图片，通常由用户程序或工具自己解释。

## 1.2 文件属性：metadata

文件不仅有内容，还有描述内容的数据，这些描述数据叫元数据 metadata。PPT 列出的文件属性包括：

| 属性 | 含义 |
|---|---|
| Name | 文件名。通常是唯一人类可读的信息。 |
| Identifier | 文件在文件系统内的唯一标识，通常是某种数字标签，例如 inode number。 |
| Type | 文件类型。某些系统会显式支持不同类型。 |
| Location | 文件在设备上的位置指针。 |
| Size | 当前文件大小。 |
| Protection | 谁能读、写、执行这个文件。 |
| Time/date/user identification | 时间、日期、用户身份，用于保护、安全和使用监控。 |
| Extended attributes | 扩展属性，例如 checksum、ACL 等。 |

这些信息保存在目录结构或文件控制块中，并且目录结构本身也保存在磁盘上。

Linux 示例里，`file` 命令可以判断文件类型：

```text
file main.c
main.c: C source, ASCII text

file a.out
a.out: ELF 64-bit LSB pie executable, x86-64, dynamically linked, ...
```

`stat a.out` 可以看到更多元数据：

```text
File: a.out
Size: 15960
Blocks: 32
IO Block: 4096
regular file
Device: ...
Inode: ...
Links: 1
Access: (0775/-rwxrwxr-x)
Uid: ...
Gid: ...
Access: ...
Modify: ...
Change: ...
Birth: ...
```

这些字段的含义：

- `Size`：文件逻辑大小，单位字节。
- `Blocks`：为它分配的磁盘块数量，通常不是简单等于 `Size / 4096`，因为存在块粒度、稀疏文件等问题。
- `IO Block`：推荐 I/O 块大小。
- `Inode`：文件的低层名字/内部编号。
- `Links`：硬链接计数。
- `Access`：权限位，例如 `0775` 和 `-rwxrwxr-x`。
- `Uid/Gid`：所有者用户和所属组。
- `Access time`：最后访问时间。
- `Modify time`：文件内容最后修改时间。
- `Change time`：文件状态最后改变时间，例如权限、所有者、链接计数变化。
- `Birth time`：创建时间，有些文件系统不支持，所以可能显示 `-`。

注意 `Modify` 和 `Change` 的区别：

- 修改文件内容：`mtime` 会变，`ctime` 也会变。
- 修改权限或链接数：`ctime` 会变，但 `mtime` 不一定变。

## 1.3 文件类型：扩展名和 magic number

PPT 给了两种识别文件类型的方法：

1. 通过文件名的一部分，也就是扩展名。
2. 通过文件内容开头的 magic number，例如 ELF 文件。

扩展名例子：

| file type | usual extension | function |
|---|---|---|
| executable | `.exe`, `.com`, `.bin` 或无扩展名 | 可直接运行的机器语言程序 |
| object | `.obj`, `.o` | 编译后但还未链接的机器代码 |
| source code | `.c`, `.cc`, `.java`, `.asm` | 源代码 |
| batch | `.bat`, `.sh` | 命令脚本 |
| text | `.txt`, `.doc` | 文本或文档 |
| word processor | `.wp`, `.tex`, `.rtf`, `.doc` | 字处理格式 |
| library | `.lib`, `.a`, `.so`, `.dll` | 程序库 |
| print/view | `.ps`, `.pdf`, `.jpg` | 可打印或查看的格式 |
| archive | `.arc`, `.zip`, `.tar` | 多文件打包，有时压缩 |
| multimedia | `.mpeg`, `.mov`, `.mp3`, `.avi` | 音视频内容 |

但是扩展名不是可靠事实。例如 Linux 下一个可执行文件可以叫 `program`，没有 `.exe`。真正判断 ELF 可执行文件时，系统会看文件开头的魔数，例如 ELF 文件以特定字节开头。

初学者可以这样理解：

```text
扩展名：给人和应用看的提示，可能骗人。
magic number：文件内容自带的身份证，通常更可信。
```

## 1.4 文件结构：OS 是否理解文件内部

PPT 列出文件可有不同结构：

1. No structure：无结构，只是一串 bytes 或 words。
   - Linux 通常采用这种思路。
   - 操作系统不关心里面是图片、文本还是数据库页。
2. Simple record structure：简单记录结构。
   - 一行一条记录。
   - 固定长度记录。
   - 可变长度记录。
   - 数据库常见。
3. Complex structures：复杂结构。
   - Word 文档。
   - relocatable program file，可重定位目标文件。

多数情况下，用户程序负责识别文件结构。操作系统只提供“读若干字节、写若干字节、移动文件偏移”的基本能力。

## 1.5 文件操作

操作系统提供的基本文件操作包括：

### create

创建文件需要两件事：

1. 在文件系统中找到可用空间。
2. 在目录中分配一个目录项，把文件名加入目录。

注意：创建文件不是只写内容。哪怕你创建一个空文件，文件系统也要创建元数据，例如 inode、目录项、时间戳、权限等。

### open

大多数文件操作要先 `open`。打开文件后，内核返回一个 handle。在 Unix/Linux 里，这个 handle 是 file descriptor，文件描述符，是一个小的非负整数。

```c
int fd = open("foo", O_CREAT | O_WRONLY | O_TRUNC);
```

含义：

- `O_CREAT`：如果文件不存在，就创建它。注意不是 `O_CREATE`。
- `O_WRONLY`：只写打开。
- `O_TRUNC`：如果文件已经存在，把它截断为 0 字节。

`open()` 成功返回的文件描述符，会是当前进程尚未使用的最小编号。

### read/write

`read` 和 `write` 需要维护当前文件位置，也就是 file pointer 或 current offset。

例如：

```text
文件内容: abcdef
当前 offset = 0
read 2 bytes -> 得到 "ab"，offset 变成 2
read 2 bytes -> 得到 "cd"，offset 变成 4
```

如果两个不同进程分别打开同一个文件，它们通常有各自的文件偏移；如果通过 `fork` 或 `dup` 共享同一个 open file description，则可能共享偏移。

### reposition within file - seek

`seek` 或 `lseek` 用于移动当前文件偏移。

例子：

```text
lseek(fd, 1000, SEEK_SET)
```

表示把当前读写位置设置到文件偏移 1000。

### close

关闭文件，释放当前进程的文件描述符表项。如果这是最后一个引用，内核还可能释放系统级打开文件表中的结构。

### delete

删除文件要释放文件空间。对硬链接要特别小心：如果一个文件有多个硬链接，删除其中一个名字时，不能立刻释放文件内容。只有最后一个链接也被删除，并且没有进程还打开它时，文件实体才会真正释放。

所以 Unix/Linux 的删除更准确叫 unlink：解除一个目录项和 inode 的链接。

### truncate

`truncate` 会清空文件内容，或者把文件调整到指定大小，但保留文件属性。例如保留文件名、权限、所有者等。

PPT 还强调：其他复杂操作可以用这些基本操作实现。例如复制文件本质上是：

```text
create new file
open old file
read old file
write new file
close both
```

## 1.6 打开的文件：open-file table

为了管理已经打开的文件，操作系统需要若干数据结构。PPT 列出：

- open-file table：打开文件表，追踪打开的文件。
- file pointer：当前读写位置。每个打开文件的进程需要维护。
- file-open count：文件被打开的次数，用于决定何时从打开文件表中移除。
- disk location of the file：缓存文件位置，避免每次读写都重新查目录和元数据。
- access rights：每个进程以什么模式打开文件，例如只读、只写、读写。

可以这样理解：

```text
进程的 fd 表
  fd 0 -> stdin 对应的打开文件对象
  fd 1 -> stdout 对应的打开文件对象
  fd 2 -> stderr 对应的打开文件对象
  fd 3 -> main.c 对应的打开文件对象

系统级打开文件表
  打开文件对象 -> 当前 offset、打开模式、引用计数、指向 inode

inode 表
  inode -> 文件元数据、数据块位置
```

实践 PPT 中的文件描述符图说明：

- file descriptor 是进程私有 fd table 的索引。
- fd table entry 指向 file object。
- file object 表示一次打开的文件，里面有当前读写 offset、非阻塞标志等非持久状态。
- file object 指向 inode。
- inode 表示文件系统对象，里面有元数据和数据块指针。
- 多次 `open()` 同一路径，通常产生不同 file object，但它们指向同一个 inode。
- `dup()` 或 `fork()` 产生的重复文件描述符可能指向同一个 file object。

这也是为什么“文件描述符”和“文件”不是同一个东西：

```text
文件名  -> inode
fd     -> file object -> inode
```

## 1.7 文件锁

某些文件系统提供 file lock 来协调多个进程访问同一个文件。

PPT 提到两类锁：

1. Shared lock：共享锁。
   - 多个进程可以同时持有。
   - 适合多个读者同时读。
2. Exclusive lock：独占锁。
   - 同一时刻只能一个进程持有。
   - 适合写操作。

还有两种锁机制：

1. Mandatory lock：强制锁。
   - 如果锁冲突，系统直接拒绝访问。
2. Advisory lock：建议锁。
   - 进程可以查询锁状态，然后自己决定怎么做。
   - 如果进程不遵守约定，系统不一定强制阻止。

初学者可以这样理解：

```text
mandatory lock 像门禁系统，没权限门打不开。
advisory lock 像会议室预约表，大家自觉遵守才有效。
```

---

# 2. 文件访问方式

PPT 第 13 讲介绍两种基本访问方式：顺序访问和直接访问。

## 2.1 Sequential access：顺序访问

顺序访问表示按预定顺序访问一组元素。

典型例子：

```text
read next
read next
read next
write next
```

磁带 tape 很适合顺序访问。磁带要访问后面的内容，通常必须先经过前面的内容。虽然理论上也可以模拟随机访问，但访问时间会随位置变化，很慢。

顺序访问的特点：

- 简单。
- 适合日志、流式处理、视频播放、顺序扫描文件。
- 对机械磁盘友好，因为磁头移动较少。

## 2.2 Direct access / Random access：直接访问/随机访问

直接访问表示可以在序列中访问任意位置，并且访问时间大致与序列大小无关。

例如磁盘块可以这样读：

```text
read block 100
read block 5
read block 1000000
```

直接访问又叫 random access。这里的 random 不是随机数的意思，而是“任意位置都能访问”。

顺序访问可以建立在直接访问之上。例如磁盘支持直接访问，但我们可以按 offset 从小到大顺序读文件。

## 2.3 索引访问

PPT 还提到其他访问方法：基于 direct-access method，加一个 index。

思路：

1. 文件有一个索引。
2. 索引指向具体数据块。
3. 要找某条记录，先查索引，再根据索引指针访问数据块。
4. 索引可以有多层。

数据库索引就是非常典型的例子。假设你要找学号为 12345 的学生记录：

```text
无索引：从头扫描所有记录
有索引：先在索引中找到 12345 对应的数据块位置，再直接读那个块
```

文件系统中的 inode 也可以理解为一种索引结构：它把“文件的第几个逻辑块”映射到“磁盘上的哪个物理块”。

---

# 3. 目录结构：文件名如何组织

## 3.1 磁盘、分区、卷、文件系统

PPT 说磁盘可以被划分成 partitions。partition 也叫 minidisk 或 slice。

关系如下：

```text
物理磁盘 disk
  -> partition 1
  -> partition 2
  -> partition 3
```

不同分区可以有不同文件系统。例如：

```text
partition 1: ext4
partition 2: FAT32
partition 3: swap
```

包含文件系统的分区称为 volume。每个 volume 会追踪自己的文件系统信息，例如总块数、空闲块、目录、inode 等。

磁盘或分区也可以 raw 使用，也就是不建立普通文件系统。数据库等应用有时偏好 raw disk 或 direct I/O，因为它们想自己管理布局和缓存。

## 3.2 目录是什么

PPT 定义：目录是一个节点集合，包含关于所有文件的信息。

从实践课看，目录本质上也可以是特殊文件。它的内容不是普通文本，而是一组映射：

```text
用户可读名字 -> 低层名字/inode number

"foo" -> inode 10
"bar" -> inode 23
"main.c" -> inode 1328649
```

所以目录最核心的作用是名字翻译：

```text
external name/pathname -> internal name/inode
```

文件和目录都驻留在磁盘上。目录结构也不是凭空存在于内存中，最终也要持久化。

## 3.3 目录操作

PPT 列出目录上常见操作：

- Create a file：创建新文件并加入目录。
- Delete a file：从目录移除文件名。
- List a directory：列出目录下所有文件。
- Search for a file：按名字或模式搜索文件。
- Traverse the file system：遍历目录中的每个目录和文件。
- 其他操作。

例如 `ls` 是 list directory，`find` 是 traverse + search。

## 3.4 目录组织目标

目录结构要实现几个目标：

1. Efficiency：快速定位文件。
2. Naming：方便用户命名和组织。
   - 两个用户可以为不同文件取同一个名字。
   - 同一个文件可以有多个不同名字。
3. Grouping：把相关文件分组。

下面是几种目录结构。

## 3.5 Single-level directory：单级目录

单级目录就是所有用户共用一个目录：

```text
/
  a.txt
  b.txt
  program
  report.doc
```

问题：

- 命名冲突严重。两个用户都想创建 `report.txt` 怎么办？
- 无法按用户或项目分组。
- 文件多了之后搜索麻烦。

单级目录适合非常简单的系统，不适合多用户和复杂项目。

## 3.6 Two-level directory：两级目录

两级目录为每个用户分配一个用户文件目录 UFD，所有 UFD 放在主文件目录 MFD 下：

```text
MFD
  alice/
    report.txt
  bob/
    report.txt
```

优点：

- 不同用户可以有同名文件。
- 搜索更高效，因为先定位用户，再在用户目录中查找。

问题：

- 不同用户之间如何共享文件？
- 需要路径概念。

## 3.7 Tree-structured directories：树形目录

现代文件系统通常使用树形目录：

```text
/
  home/
    alice/
      main.c
      docs/
    bob/
  bin/
  usr/
```

优点：

- 搜索效率较好。
- 可以分组。
- 命名方便。
- 支持绝对路径和相对路径。

绝对路径 absolute path：

```text
/home/alice/main.c
```

从根目录 `/` 开始。

相对路径 relative path：

```text
docs/report.txt
../bob/file.txt
```

相对于当前目录 `pwd`。

创建文件：

```text
touch <file-name>
```

创建子目录：

```text
mkdir count
```

如果当前目录是 `/mail`，执行 `mkdir count` 会创建：

```text
/mail/count
```

删除目录有两种策略：

1. 目录必须为空才能删除。
2. 递归删除目录中的所有文件、子目录和更深层内容。

PPT 举了危险命令：

```text
sudo rm -rf /
```

这是递归强制删除根目录，极其危险。学习时只要理解它说明“递归删除会沿着目录树一直删除下去”即可。

树形目录的问题：天然不允许共享同一个文件或目录。如果同一个文件要出现在两个地方，树结构会被破坏。

## 3.8 Acyclic-graph directories：无环图目录

无环图目录允许链接到已有文件或目录项，实现共享和别名 aliasing。这样目录结构不再是树，而是 DAG，directed acyclic graph，有向无环图。

例子：

```text
/dict/all
/dict/w/list  -> 指向同一个文件
/spell/words/list -> 也指向同一个文件
```

问题：dangling pointer，悬空指针。

如果真正文件 `/dict/all` 被删除，而 `/dict/w/list` 和 `/spell/words/list` 还指向它，那么这些链接就悬空了。

解决方案：

1. Back pointers：反向指针。
   - 被共享对象记录所有指向自己的位置。
   - 缺点是记录数量可变，管理复杂。
2. Reference counter：引用计数。
   - 记录有多少链接指向实体。
   - 只有计数变为 0 时才真正删除实体。

Linux 硬链接就使用类似引用计数的思想。

## 3.9 General graph directory：一般图目录

如果允许任意链接，目录结构可能产生环：

```text
A -> B -> C -> A
```

环会带来两个问题：

1. 遍历可能无限循环。
2. 删除和回收空间变复杂。

解决思路：

- 允许环，但使用 garbage collection 回收磁盘空间。
- 每次添加新链接时执行 cycle detection algorithm，检测是否形成环。

实际系统中通常会限制某些链接，尤其是限制普通用户对目录创建硬链接，避免目录环带来的复杂问题。

---

# 4. 文件系统挂载与共享

## 4.1 Mounting：挂载

PPT 定义：文件系统必须先 mounted，才能被访问。mounting 把一个文件系统链接到系统中，通常形成单一命名空间。

mount point 是挂载点，也就是被挂载文件系统接入的位置。

例如：

```text
已有目录树：
/
  users/
  bin/

另一个分区里有：
  alice/
  bob/

把分区挂载到 /users 后：
/
  users/
    alice/
    bob/
  bin/
```

关键细节：挂载后，挂载点原来的目录内容会被隐藏，而不是删除。

```text
mount /dev/sdb1 /users
```

此时访问 `/users` 看到的是新文件系统根目录下的内容。

## 4.2 文件共享

多用户系统希望共享文件，但必须配合保护机制。

PPT 提到：

- User ID：标识用户，使权限能按用户设置。
- Group ID：标识用户组，使一组用户共享访问权。
- 分布式系统中文件可通过网络共享。
- NFS 是常见分布式文件共享方法。

## 4.3 远程文件共享

使用网络允许系统之间访问文件。方式包括：

1. 手动方式：FTP 等程序。
2. 自动、透明方式：分布式文件系统。
3. 半自动方式：World Wide Web。

客户端-服务器模型：

- 一个 server 可以服务多个 client。
- client 可以把 server 上的远程文件系统 mount 到本地。
- client 和用户身份识别很复杂，因为 server 不能简单相信 client。
- 标准 OS 文件调用会被翻译成远程调用。
- Unix 常见标准协议是 NFS。
- Windows 常见标准协议是 CIFS。

---

# 5. 文件保护：权限和 ACL

## 5.1 保护的目标

PPT 说：文件 owner/creator 应该能控制：

- 可以做什么。
- 谁可以做。

访问类型包括：

- read：读。
- write：写。
- append：追加。
- execute：执行。
- delete：删除。
- list：列出目录内容。

## 5.2 ACL：Access Control List

ACL 是访问控制列表。每个文件或目录可以有一个 ACL，明确列出谁拥有什么权限。

优点：

- 细粒度控制。可以说用户 A 可读写，用户 B 只读，用户 C 无权限。

缺点：

- 列表如何构造？
- 列表如何存储在目录或元数据里？
- 如果用户很多，管理会复杂。

实践 PPT 的 ACL 示例：

```text
ls -l
-rw-rw-r-- 1 os os 0 Dec 18 23:21 testacl

getfacl testacl
user::rw-
group::rw-
other::r--

setfacl -m u:test:rw testacl

getfacl testacl
user::rw-
user:test:rw-
group::rw-
mask::rw-
other::r--
```

解释：

- 原始 Unix 权限只有 owner/group/other 三类。
- ACL 可以额外给名为 `test` 的用户加 `rw-` 权限。
- `mask` 限制某些 ACL 项的最大有效权限。

## 5.3 Unix 权限模型

Unix 基本权限是三种访问模式：

- read，记作 `r`。
- write，记作 `w`。
- execute，记作 `x`。

三类用户：

- owner：所有者。
- group：所属组。
- others：其他用户。

每类用 3 个 bit 表示 `rwx`。

PPT 示例：

```text
owner access: 7   111   rwx
group access: 6   110   rw-
others access: 1  001   --x
```

所以 `761` 表示：

```text
owner: rwx
group: rw-
others: --x
```

常见命令：

```text
chmod 761 file
chgrp group file
```

`ls -l` 的目录列表示例：

```text
-rw-rw-r--  1 pbg staff    31200 Sep 3 08:30 intro.ps
drwx------  5 pbg staff      512 Jul 8 09:33 private/
drwxrwxr-x  2 pbg staff      512 Jul 8 09:35 doc/
drwxrwx---  2 pbg student    512 Aug 3 14:13 student-proj/
-rw-r--r--  1 pbg staff     9423 Feb 24 2003 program.c
-rwxr-xr-x  1 pbg staff    20471 Feb 24 2003 program
```

第一列解释：

```text
-rw-rw-r--
| ||| ||| |||
| |   |   |
| |   |   others permissions
| |   group permissions
| owner permissions
file type: '-' 普通文件，'d' 目录
```

例如：

- `-rw-r--r--`：普通文件，owner 可读写，group 可读，others 可读。
- `-rwxr-xr-x`：普通文件，owner 可读写执行，group/others 可读执行。
- `drwx------`：目录，只有 owner 可进入、列出、修改。

目录上的 `x` 很重要：对目录来说，execute 表示能“进入/穿过”目录，而不是执行目录。

---

# 6. 文件系统实现：从接口到磁盘块

第 14 讲开始问：用户看到文件和目录，那么 OS 内部如何实现？

## 6.1 文件系统历史

PPT 按时间列出文件系统演化：

### 1950s-1970s：早期文件系统

- 计算机主要用于科学研究和大型商业。
- 文件系统很基础。
- 常为特定 OS 或特定机器定制。
- IBM 早期大型机有自己的文件系统。
- PPT 例子：IBM 350 disk storage unit。

### 1970s-1980s：层次化文件系统

- 允许把文件组织到目录中。
- 例子：
  - UNIX file system。
  - Microsoft FAT，File Allocation Table。

### 1980s-1990s：网络文件系统

- 支持通过网络访问文件。
- 例子：NFS，Network File System。

### 1990s-2000s：日志文件系统

- 例子：ext3、ext4、NTFS。
- 操作前先记录日志。
- 崩溃后可根据日志恢复。
- 提高性能和可靠性。

### 2000s-present：现代文件系统

- ZFS、Btrfs 等加入高级特性：
  - snapshots：快照。
  - dynamic volume management：动态卷管理。
  - data integrity checks：数据完整性检查。
- 分布式文件系统变得普遍：
  - Google GFS。
  - Amazon S3。
- 目标是大规模、高可靠存储。

## 6.2 文件系统结构

PPT 说：

- 文件是相关信息集合的逻辑存储单元。
- OS 可同时支持多个文件系统。
  - Linux：ext2/3/4、ReiserFS、Btrfs 等。
  - Windows：FAT、FAT32、NTFS。
  - 新系统：ZFS、GoogleFS、Oracle ASM、FUSE。
- 文件系统驻留在二级存储上，例如磁盘。
- 磁盘驱动提供读写磁盘块接口。
- 文件系统给用户/程序提供存储接口，并把逻辑映射到物理。
- File Control Block，FCB，是包含文件信息的存储结构。
- 文件系统通常分层实现。

## 6.3 分层文件系统

PPT 的层次可以理解为：

```text
Application programs
  |
Logical file system
  |
File-organization module
  |
Basic file system / block I/O subsystem
  |
I/O control
  |
Devices
```

### Logical file system：逻辑文件系统

负责维护文件系统所需的元数据，也就是除文件内容之外的东西。

它存储：

- 目录结构。
- FCB，即文件描述结构。
  - name。
  - ownership。
  - permissions。
  - reference count。
  - timestamps。
  - pointers to other FCBs。
  - pointers to data blocks on disk。

输入：

```text
Open/Read/Write filepath
```

输出：

```text
Read/Write logical blocks
```

也就是说，这一层更关心“路径、文件名、权限、inode/FCB”，不直接关心设备控制器。

### File-organization module：文件组织模块

负责逻辑文件块和物理文件块之间的翻译，也管理空闲空间。

输入：

```text
Read logical block 3
Write logical block 17
```

输出：

```text
Read physical block 43
Write physical block 421
```

例子：

```text
用户要读文件 offset 8192 的数据
文件系统算出：这是文件逻辑块 2
文件组织模块查 inode：逻辑块 2 对应磁盘物理块 43
```

### Basic file system：基本文件系统

Linux 中可以类比 block I/O subsystem。

它负责：

- 分配和维护各种 buffer。
- 这些 buffer 包含文件系统块、目录块、数据块。
- buffer/cache 用于提升性能。

输入：

```text
Read physical block #43
Write physical block #421
```

输出仍是：

```text
Read physical block #43
Write physical block #421
```

区别在于它可能命中缓存。如果数据已经在内存中，就不需要马上访问磁盘。

### I/O Control：I/O 控制

这一层包括：

- device drivers。
- interrupt handlers。

输入：

```text
Read physical block #43
Write physical block #124
```

输出：

- 写设备控制器的内存/寄存器，让磁盘执行读写。
- 响应相关中断。

这一层离硬件最近。

## 6.4 分层的优缺点

优点：

- 降低复杂度。
- 减少重复。
- 不同文件系统可以复用下层机制。
- OS 可以通过统一接口管理多个文件系统。

缺点：

- 增加开销。
- 可能降低性能。

PPT 强调：分层会把文件名翻译成 file number、file handle、location。这依赖维护 FCB，在 Unix 中就是 inode。

## 6.5 多种文件系统

PPT 举例：

- ISO 9660：CD-ROM 文件系统标准。
- UNIX：UFS，基于 Berkeley Fast FS。
- Windows：FAT、FAT32、NTFS。
- Linux 基本支持 40 多种文件系统。
  - 标准包括 ext2、ext3。
- 活跃研究方向：
  - Distributed File Systems。
  - High-Performance File Systems。
  - Google File System。

这一段的重点是：文件系统不是一个固定算法，而是一类系统。不同文件系统有不同磁盘布局、元数据、分配策略、恢复策略，但对上层尽量暴露相似接口。

---

# 7. 文件系统数据结构

第 14 讲区分 on-disk structures 和 in-memory structures。

## 7.1 On-disk structures：磁盘上结构

磁盘上的结构必须持久化，断电后仍能恢复。

### Boot control block

可选。

- 是一个 volume 的第一个块。
- 如果该 volume 存储 OS，就可能包含启动信息。
- UFS 中叫 boot block。
- NTFS 中叫 partition boot sector。

### Volume control block

描述整个卷的信息，包括：

- volume 中 block 数量。
- block size。
- free-block count。
- free-block pointers。
- free-FCB count。
- FCB pointers。

在 UFS 中类似 superblock。

在 NTFS 中类似 master file table。

### Directory

目录保存：

- 文件名。
- 对应 ID。
- FCB pointer。

最核心就是名字到 inode/FCB 的映射。

### Per-file File Control Block

每个文件有自己的 FCB。

PPT 说 NTFS 中 FCB 是 relational database 中的一行。意思是 NTFS 的元数据组织得更像表，每个文件是一条记录。

## 7.2 In-memory structures：内存中结构

内存中的结构用于加速和管理运行状态，断电后可丢失或可从磁盘重建。

包括：

- Mount table：每个挂载卷一项。
- Directory cache：目录缓存，加速路径翻译。
- Global open-file table：全局打开文件表。
- Per-process open-file table：每进程打开文件表。
- Buffers holding disk blocks in transit：保存正在传输或缓存的磁盘块。

目录缓存非常重要。没有缓存的话，打开 `/foo/bar/baz` 可能需要逐级读 inode 和目录数据块；有缓存后，常用路径可以快速解析。

## 7.3 File Control Block 和 inode

FCB 包含文件元数据和数据块指针。PPT 图里列出：

- file permissions。
- file dates：create、access、write。
- file owner、group、ACL。
- file size。
- file data blocks 或 pointers to file data blocks。

Unix/Linux 中常见 FCB 叫 inode，index node。

PPT 的 ext2 inode 图包括：

- mode：文件类型和权限。
- owners：所有者信息。
- timestamps：时间戳。
- size block count：文件大小和块数。
- direct blocks：直接块指针。
- single indirect：一级间接块指针。
- double indirect：二级间接块指针。
- triple indirect：三级间接块指针。

inode 不保存文件名。文件名保存在目录项里。

这是本讲最重要的概念之一：

```text
文件名不是文件本体。
目录项把文件名链接到 inode。
inode 保存文件元数据和数据块位置。
```

---

# 8. 文件创建与打开的内部过程

## 8.1 创建文件

PPT 中创建文件过程：

1. 应用进程请求创建新文件。
2. 逻辑文件系统分配新的 FCB，也就是 inode 结构。
3. 对应目录更新：加入新文件名和 FCB/inode 的关联。

用更细的步骤看：

```text
create("/home/alice/foo")
  1. 找到 /home/alice 对应的目录 inode
  2. 检查权限：当前用户是否能在该目录创建文件
  3. 从 inode bitmap 找空闲 inode
  4. 初始化 inode：类型、权限、owner、时间戳、大小 0
  5. 在目录数据块中添加目录项："foo" -> inode number
  6. 更新目录时间、链接计数等元数据
  7. 可能写日志或标记脏页，之后写回磁盘
```

## 8.2 open() 的内部过程

PPT 分两种情况。

### 情况一：文件已经在系统级打开文件表中

1. 搜索 system-wide open-file table。
2. 如果文件已在用：
   - 创建 per-process open-file table entry。
   - 该 entry 指向已有 system-wide open-file table entry。

### 情况二：文件尚未在系统级打开文件表中

1. 搜索目录结构，找到文件名。
2. 找到后，把 FCB 从磁盘加载到内存。
3. 放入 system-wide open-file table。
4. 创建 per-process open-file table entry。

随后：

- 每进程打开文件表项中包含：
  - 指向系统级打开文件表项的指针。
  - 当前文件位置 pointer/current offset。
  - 打开模式/access mode。
- 系统级打开文件表的 open count 增加。
- `open()` 返回指向 per-process open-file table entry 的“指针”。在 Unix 用户态表现为文件描述符整数。
- 后续操作都用这个返回值。

关闭时：

```text
process closes file
  -> 删除 per-process open-file table entry
  -> system-wide open count --

all processes close file
  -> 内存中的目录/元数据信息写回磁盘
  -> system-wide open-file table entry 从内存移除
```

PPT 说 UFS 的 system-wide open-file table 保存 inodes，用于文件、目录、设备和网络连接。inode number 只在某个文件系统内部唯一，不是全系统全局唯一。

---

# 9. VFS：虚拟文件系统

## 9.1 为什么需要 VFS

问题：OS 如何同时支持 ext4、FAT、NTFS、NFS、procfs、tmpfs？

如果每种文件系统都直接暴露自己的 API，应用程序会非常痛苦：

```text
read_ext4(...)
read_fat(...)
read_nfs(...)
read_procfs(...)
```

所以操作系统使用一层间接层：Virtual File System，VFS。

PPT 引用 David Wheeler：

```text
All problems in computer science can be solved by another level of indirection,
except for the problem of too many layers of indirection.
```

意思是：加一层间接层常能解决抽象和兼容问题，但层太多也会带来复杂度和开销。

## 9.2 VFS 的作用

VFS 提供一种面向对象风格的文件系统实现方法：

- OS 定义文件系统通用接口。
- 所有具体文件系统实现这些接口。
- 系统调用基于通用接口实现。
- 同一个 syscall API 可用于不同文件系统。

例如用户都调用：

```c
write(fd, buf, count);
```

如果 `fd` 对应 ext4 文件，最终调用 ext4 的写函数。

如果 `fd` 对应 NFS 文件，最终调用 NFS 的写函数。

应用程序不需要改。

## 9.3 VFS 的四类对象

PPT 说 Linux 定义四种 VFS object types：

### superblock

描述文件系统整体：

- 文件系统类型。
- 大小。
- 状态。
- 其他元数据。

### inode

描述一个文件系统对象：

- 文件位置。
- 访问模式。
- owner。
- permissions。
- 其他元数据。

对象可以是：

- 普通文件。
- 目录。
- socket。
- 设备文件。

### dentry

directory entry 的缓存对象，负责名字与 inode 的关联，以及目录布局。

可以理解为：

```text
"foo" -> inode
```

路径解析大量依赖 dentry cache。

### file

表示一次已经打开的文件。它不是磁盘上的文件本体，而是运行时对象。

它保存：

- 当前 offset。
- 打开模式。
- 指向 inode。
- 指向操作函数表 `f_op`。

## 9.4 VFS 如何实现：函数表

VFS 定义对象上必须实现的一组操作。这些操作保存在 function table 中。

PPT 截图中有 `struct file_operations`，包含类似：

```c
struct file_operations {
    loff_t (*llseek)(struct file *, loff_t, int);
    ssize_t (*read)(struct file *, char __user *, size_t, loff_t *);
    ssize_t (*write)(struct file *, const char __user *, size_t, loff_t *);
    ssize_t (*read_iter)(struct kiocb *, struct iov_iter *);
    ssize_t (*write_iter)(struct kiocb *, struct iov_iter *);
    int (*iterate)(struct file *, struct dir_context *);
    long (*unlocked_ioctl)(struct file *, unsigned int, unsigned long);
    int (*mmap)(struct file *, struct vm_area_struct *);
    int (*open)(struct inode *, struct file *);
    int (*flush)(struct file *, fl_owner_t id);
    int (*release)(struct inode *, struct file *);
};
```

重点不是背字段，而是理解函数表机制：

```text
file->f_op->write_iter(...)
```

这意味着“这个打开文件对象的写操作是什么”由 `file->f_op` 指向的函数表决定。

PPT 给出 ext4 例子：

```text
write syscall -> vfs_write -> indirect call -> ext4_file_write_iter
```

如果写的是 NFS 文件，调用路径类似：

```text
write syscall -> vfs_write -> indirect call -> nfs 对应的 write_iter
```

`file->f_op` 什么时候设置？通常在 `open` 文件时，根据 inode 所属文件系统和文件类型设置到具体文件系统的操作函数表。

---

# 10. 目录实现

## 10.1 目录是特殊文件

PPT 说目录是特殊文件，保存 file name 到 inode 的映射。

实践课图里目录项包含：

- inode number。
- rec_len：目录项长度，通常是 4 的倍数，用于复用 entry 空间。
- name_len：文件名长度。
- file name：文件名。

形式类似：

```text
目录数据块：
  [inode=10, rec_len=12, name_len=3, name="foo"]
  [inode=23, rec_len=12, name_len=3, name="bar"]
  [inode=45, rec_len=24, name_len=12, name="foobar_is..."]
```

为什么要有 `rec_len`？

因为文件删除后，目录中可能留下空洞。`rec_len` 可以让文件系统把多个目录项空间合并或复用，不必每次都整体移动目录内容。

## 10.2 目录组织方法

PPT 列出两种实现：

### Linear list

线性列表保存文件名和指向元数据的指针。

优点：

- 简单。

缺点：

- 搜索耗时，需要线性查找。

优化：

- 按字母顺序维护链表。
- 使用 B+ tree。

### Hash table

用哈希结构减少搜索时间。

问题：

- 可能发生 collision：两个或更多文件名 hash 到同一位置。

实际文件系统会综合考虑目录大小、更新成本、查询性能。

PPT 还说：

- Unix 把目录当作包含特殊数据的文件。
- Windows 将目录和文件区别对待，需要一组单独系统调用创建和操作目录。

## 10.3 回顾 open/read 中目录的作用

打开文件时：

```text
open("/foo/bar")
```

需要路径解析：

1. 从根目录 `/` 的 inode 开始。
2. 读取根目录数据，找到 `foo` 对应的 inode。
3. 确认 `foo` 是目录。
4. 读取 `foo` 目录数据，找到 `bar` 对应的 inode。
5. 根据 `bar` inode 打开文件。

如果没有缓存，每一级目录可能需要：

- 读目录 inode。
- 读目录数据块。

所以路径越深，I/O 越多。目录缓存和 inode 缓存可以大幅加速。

---

# 11. 磁盘块分配方法

文件内容最终要放入磁盘块。PPT 讨论三种方法：

- Contiguous allocation。
- Linked allocation。
- Indexed allocation。

不同策略有不同复杂度和性能。

## 11.1 Contiguous allocation：连续分配

每个文件占用一组连续磁盘块。

目录只需要记录：

```text
start block
length in blocks
```

例如：

```text
file A: start=100, length=5
=> block 100, 101, 102, 103, 104
```

优点：

- 顺序访问非常快。
- 磁头移动少，seek time 小。
- 随机访问也容易：第 i 块就是 `start + i`。

缺点：

### 难以找到足够大的空闲连续空间

可以用 Best Fit、First Fit 等分配策略，但会产生碎片问题。

### External fragmentation：外部碎片

磁盘中可能有很多小空洞，总空闲空间够，但没有一段连续大空间。

解决可用 compaction/defrag：

- 整理磁盘。
- 把文件移动到一起。
- 代价昂贵但可做。

### 文件增长困难

如果文件后面没有空闲块，文件变大怎么办？

方案：

1. 底层复制到更大的空洞。
   - 开销高。
2. 要求用户提前声明最大文件大小。
   - 不方便。
   - 可能产生内部碎片。
3. 用文件块链表扩展。
   - 这叫 extent。

Extent 是现代文件系统常见思想：一个文件由若干个连续块区间组成，而不是必须整个文件完全连续。

## 11.2 Linked allocation：链接分配

每个文件是磁盘块链表。每个块包含指向下一个块的指针，文件以 nil pointer 结束。

形式：

```text
file A:
block 9 -> block 16 -> block 1 -> block 10 -> nil
```

优点：

- 块可以散落在磁盘任意位置。
- 没有外部碎片。
- 不需要 compaction。
- 文件增长容易，加一个块到链表即可。

缺点：

### 随机访问差

要访问文件第 1000 个块，必须从第一个块沿指针走 1000 次，可能产生大量 I/O 和 seek。

### 指针浪费空间

PPT 示例：512 字节块中 4 字节用于指针。

浪费比例：

```text
4 / 512 = 0.0078125 = 0.78%
```

### 可靠性问题

如果某个块中的“下一个块指针”损坏，后续内容可能全部丢失。

改进：

- cluster blocks，例如 4 个块一组。
- 减少指针比例，提高吞吐。
- 缺点是可能产生 internal fragmentation，内部碎片。

## 11.3 FAT：File Allocation Table

PPT 说 MS-DOS 的 FAT 使用 linked allocation。

FAT 的思想是把链表指针集中放在一张表中，而不是放在每个数据块里。

例如：

```text
FAT[9] = 16
FAT[16] = 1
FAT[1] = 10
FAT[10] = EOF
```

优点：

- 数据块本身不需要存指针。
- FAT 表如果缓存到内存，链表遍历可更快。

缺点：

- FAT 表可能很大。
- 表损坏会影响大量文件。

## 11.4 Indexed allocation：索引分配

每个文件有自己的 index blocks，索引块中保存指向数据块的指针。

形式：

```text
inode/index block:
  logical block 0 -> physical block 100
  logical block 1 -> physical block 203
  logical block 2 -> physical block 88
```

优点：

- 支持随机访问。
- 没有外部碎片。
- 支持文件空洞 holes。

缺点：

- 索引块需要空间。
- 小文件也要索引，可能浪费。
- 单次访问可能先读索引块，再读数据块。

问题：索引块不能太大，也不能太小。

如果太小，大文件不够用。

如果太大，小文件浪费严重。

解决：

- Linked index blocks：索引块之间再链接，支持大文件。
- Multiple-level index blocks：多级索引，例如二级索引。
- Combined scheme：组合方案。

## 11.5 Unix inode 的组合索引

PPT 讲 Unix FCB，也就是 inode：

- inode 中前 15 个指针。
- 前 12 个是 direct block pointers。
- 后 3 个是 indirect block pointers。
  - single indirect。
  - double indirect。
  - triple indirect。

假设：

```text
Block size = 512 bytes
Pointer = 4 bytes
每个索引块能放 512 / 4 = 128 个指针
```

最大文件大小：

```text
direct:          12 * 512
single indirect: 128 * 512
double indirect: 128^2 * 512
triple indirect: 128^3 * 512
```

合计：

```text
12*512 + 128*512 + 128^2*512 + 128^3*512 bytes
```

如果 block size 是 4KB，pointer 仍是 4 bytes：

```text
每个索引块可放 4096 / 4 = 1024 个指针

最大文件大小约为：
12*4096
+ 1024*4096
+ 1024^2*4096
+ 1024^3*4096
```

三级间接能支持非常大的文件。

组合索引的直觉：

- 小文件直接用 direct blocks，访问快、开销小。
- 中等文件用 single indirect。
- 大文件用 double/triple indirect。

这是一种兼顾小文件效率和大文件容量的设计。

## 11.6 分配方法比较

PPT 总结：

- 最佳分配方法取决于文件访问类型。
- Contiguous 对顺序和随机访问都很好。
- Linked 对顺序访问可以，但随机访问不好。
- Indexed/combined 更复杂。
  - 单个块访问可能需要读 2 个索引块再读数据块。
  - clustering 可以提高吞吐、减少 CPU 开销。
  - cluster 是一组连续块。

PPT 强调磁盘 I/O 很慢，要尽量减少 I/O 次数。

例子：

```text
Intel Core i7 Extreme Edition 990x (2011) at 3.46GHz = 159,000 MIPS
Typical disk drive = 250 I/Os per second
159,000 MIPS / 250 = 630 million instructions during one disk I/O
```

意思是：一次机械磁盘 I/O 的时间里，CPU 可以执行大量指令。

SSD 例子：

```text
Fast SSD = 60,000 IOPS
159,000 MIPS / 60,000 = 2.65 million instructions during one disk I/O
```

SSD 快很多，但 I/O 仍比 CPU 慢得多。因此缓存、批量、顺序化、减少随机 I/O 都非常重要。

---

# 12. 空闲空间管理

文件删除后，空间要回收。文件系统必须维护 free-space list 来追踪可用 blocks/clusters。

PPT 列出方法：

- Bit vector / bitmap。
- Linked free space。
- Grouping。
- Counting。

## 12.1 Bitmap free-space management

bitmap 用一个 bit 表示一个块是否空闲。

例如：

```text
block:  0 1 2 3 4 5 6 7
bitmap: 1 1 0 1 0 0 1 1
```

可以约定：

- `1` 表示已分配。
- `0` 表示空闲。

优点：

- 容易找到连续空闲块。
- 数据结构简单。

缺点：

- bitmap 需要额外空间。

PPT 示例：

```text
block size = 4KB = 2^12 bytes
disk size = 2^40 bytes = 1 TB
块数 n = 2^40 / 2^12 = 2^28 blocks
bitmap 需要 2^28 bits = 256 Mbits = 32 MB
```

如果使用 4 blocks 为一个 cluster：

```text
cluster 数 = 2^28 / 4 = 2^26
bitmap = 64 Mbits = 8 MB
```

注意：PPT 写的是 64M bits of memory。换成字节是 8 MB。

## 12.2 Linked free space

把空闲块组织成链表：

```text
free block 5 -> free block 18 -> free block 9 -> ...
```

优点：

- 不浪费额外空间，可以直接在空闲块中存指针。
- 分配一个空闲块时返回链表头即可。

缺点：

- 不容易找到连续空间。
- 如果要分配多个连续块，可能需要遍历很多节点。

## 12.3 Grouping

简单 linked list 低效，因为：

- 分配一个 free block 可能需要额外磁盘 I/O。
- 分配多个 free blocks 需要遍历链表。
- 难以分配连续块。

Grouping 的思想：

- 在第一个空闲块中存 n-1 个空闲块地址。
- 再加一个指向下一个 index block 的指针。

这样一次读一个索引块就知道多个空闲块地址，分配多个块不必逐个遍历。

## 12.4 Counting

Counting 记录连续空闲块区间：

```text
(starting block, count)
```

例如：

```text
(100, 20) 表示 block 100 到 119 都空闲
```

适用原因：

- 空间经常连续使用和释放。
- 一个记录可以表示很多连续空闲块。

这和 extent 的思想类似：用“起点 + 长度”表达连续区域。

---

# 13. 文件系统性能

PPT 说文件系统效率和性能取决于：

- 磁盘分配算法。
- 目录算法。
- 文件目录项中保存哪些数据。
- metadata structures 是预分配还是按需分配。
- 数据结构是 fixed-size 还是 varying-size。

## 13.1 提升性能的方法

PPT 列出：

### 让数据和元数据靠近

如果 inode 和数据块离得很远，读文件可能需要大量 seek。把相关数据放近可以减少磁盘移动，提高局部性。

### 使用 cache

把常用块放在主存中。缓存可保存：

- 文件数据块。
- 目录块。
- inode。
- superblock。

### 异步写 asynchronous writes

为了性能，写操作可以先写入内存 buffer/cache，稍后再写到磁盘。

优点：

- `write()` 很快返回。
- 多次小写可以合并。
- 可以更好调度磁盘 I/O。

风险：

- 程序以为写了，但数据可能还没落盘。
- 崩溃时可能丢失最近写入。

### 同步写 synchronous writes

同步写必须在返回前写到磁盘。不能简单缓存后就返回。

某些应用或 OS 需要同步写，例如数据库事务、文件系统元数据更新。

### Free-behind 和 read-ahead

针对顺序访问优化：

- free-behind：顺序读过的前面页可以从 buffer 中释放。
- read-ahead：预测接下来会读后面的页，提前读多个页。

例子：播放视频时，系统可以提前读后续块。

### Reads frequently slower than write: really?

PPT 提问：读经常比写慢，真的吗？

直觉上读似乎应该快，但在有缓存和异步写时：

- 写可以先写内存就返回，看起来很快。
- 读如果缓存未命中，必须等磁盘读回来，可能慢。

所以从系统调用返回时间看，普通 buffered write 可能比 cold read 更快。但真正持久化到磁盘需要后续 I/O。

## 13.2 Page cache 与 buffer cache

PPT 说 OS 有不同层次 cache：

- page cache：缓存 memory-mapped I/O 的页，例如 mmap 文件。
- buffer/disk cache：文件系统用于磁盘 I/O 的缓存。

早期系统可能出现 double caching：

```text
mmap 文件 -> page cache
read/write 文件 -> buffer cache
```

同一份文件数据可能缓存两份，浪费内存且一致性复杂。

Unified buffer cache 用同一个 page cache 缓存 memory-mapped pages 和 disk I/O，避免双重缓存。

---

# 14. 恢复与日志文件系统

## 14.1 Consistency checking

文件系统需要一致性检查，确保目录和磁盘元数据一致。

例如可能检查：

- 目录中指向的 inode 是否存在。
- inode 的链接计数是否和目录项数量匹配。
- 空闲块 bitmap 是否和 inode 使用块冲突。
- 文件大小和块指针是否一致。

PPT 说 FS recovery 可能很慢，有时也会失败。

恢复方法包括：

- Backup。
- Log-structured file system。

## 14.2 Log Structured File Systems

PPT 讲 LSFS：

- 更新的 metadata 顺序写到 circular log。
- 一旦 change 写入 log，就算 committed，系统调用可以返回。
- log 可以位于其他磁盘/分区。
- 后台把 log entries replay 到真正文件系统结构中。
- transaction replay 后，从 log 中移除。
- log 是 circular，但未 replay 的 entries 不能被覆盖。
- garbage collection 可以回收或压缩 log entries。
- 系统崩溃后，只需要 replay log 中存在的 transactions。

直觉：

```text
直接修改文件系统：
  改目录、改 inode、改 bitmap、改数据块
  如果中间崩溃，状态可能半新半旧

日志方式：
  先把“我要做哪些修改”完整写入日志
  崩溃后根据日志重做或撤销
```

日志文件系统的目标是减少崩溃后全盘扫描，提高可靠性和恢复速度。

---

# 15. 实践：Linux 文件接口

## 15.1 两个关键抽象：File 和 Directory

实践 PPT 第 1 个核心点：

### File

- 是一个线性字节数组，每个字节可读写。
- 有低层名字 low-level name，用户通常不知道，也就是 inode number。
- OS 通常不知道文件确切类型。

### Directory

- 也有低层名字。
- 内容很特殊：包含一组“用户可读名字 -> 低层名字”的映射。
- 例子：`("foo", inode number 10)`。
- 每个 entry 指向文件或其他目录。

第 2 个核心点：

- 文件外部名字 external name 对用户可见，必须是 symbolic。
- 层次化文件系统中，唯一外部名字通常是 pathname，也就是从 root 到文件的路径。
- 内部名字 internal name 在 Unix 中是 inode。
- inode 存储文件系统对象信息：file、directory、socket 等。
- directory 做 external name 到 internal name 的翻译。

## 15.2 open 创建文件

实践 PPT 代码：

```c
int fd = open("foo", O_CREAT | O_WRONLY | O_TRUNC);
```

含义再复述：

- `O_CREAT`：不存在就创建。
- `O_WRONLY`：只写。
- `O_TRUNC`：存在就截断为 0 字节。

`open()` 返回 file descriptor：

- 小的非负整数。
- 后续 `read(2)`、`write(2)`、`lseek(2)`、`fcntl(2)` 等系统调用用它引用打开文件。
- 成功时返回当前进程未打开的最小 fd。

## 15.3 stdin/stdout/stderr

每个进程启动时通常已有三个标准文件描述符：

```text
fd 0: stdin  标准输入
fd 1: stdout 标准输出
fd 2: stderr 标准错误
```

实践 PPT 的 `strace ./a.static` 示例中有：

```text
fstat(1, {st_mode=S_IFCHR|0620, ...}) = 0
write(1, "hello world!\n", 13) = 13
```

解释：

- `write(1, ...)` 表示把内容写到 fd 1，也就是 stdout。
- `hello world!\n` 长度 13 字节，返回 13 表示成功写入 13 字节。
- stdout 在终端里通常是字符设备 `S_IFCHR`。

## 15.4 cat main.c 的 fd 是多少

实践 PPT 给出：

```text
openat(AT_FDCWD, "main.c", O_RDONLY) = 3
newfstatat(3, "", {...}, AT_EMPTY_PATH)
read(3, "#include <stdio.h>\n\nint main () "... , 131072) = 89
write(1, "#include <stdio.h>\n\nint main () "... , 89) = 89
read(3, "", 131072) = 0
close(3) = 0
close(1) = 0
close(2) = 0
```

问题：`main.c` 的 file descriptor 是多少？

答案：3。

原因：

- 0、1、2 已经被 stdin/stdout/stderr 占用。
- `openat(..., "main.c", O_RDONLY) = 3` 表示打开 `main.c` 返回 fd 3。
- 后续 `read(3, ...)` 从 fd 3 读。
- `write(1, ...)` 写到 stdout。
- `close(3)` 关闭 `main.c`。

`read(...)=0` 表示到达文件末尾 EOF。

## 15.5 write 与 fsync

PPT 强调：

`write()` 的含义不是“数据已经持久化到磁盘”。更准确是：

```text
把数据交给文件系统，未来某个时候写到持久存储。
```

文件系统为了性能会把写操作 buffer 在内存中一段时间，例如 5 秒或 30 秒，之后再真正发到存储设备。

`fsync()`：

```text
forces all dirty data to disk
```

也就是强制把脏数据写到磁盘。

PPT 代码：

```c
int fd = open("foo", O_CREAT | O_WRONLY | O_TRUNC);
assert(fd > -1);

int rc = write(fd, buffer, size);
assert(rc == size);

rc = fsync(fd);
assert(rc == 0);
```

解释：

- `write` 成功只说明内核接受了这些数据。
- `fsync` 成功才更接近说明该文件相关脏数据已经刷到持久存储。

为什么说“更接近”？因为还涉及磁盘控制器缓存、存储设备是否真正遵守 flush 等更底层问题。但课程阶段理解为 `fsync` 强制落盘即可。

## 15.6 struct stat

实践 PPT 的 `struct stat` 包含：

```c
struct stat {
    unsigned long st_dev;     /* Device. */
    unsigned long st_ino;     /* File serial number. */
    unsigned int  st_mode;    /* File mode. */
    unsigned int  st_nlink;   /* Link count. */
    unsigned int  st_uid;     /* User ID of the file's owner. */
    unsigned int  st_gid;     /* Group ID of the file's group. */
    unsigned long st_rdev;    /* Device number, if device. */
    long          st_size;    /* Size of file, in bytes. */
    int           st_blksize; /* Optimal block size for I/O. */
    long          st_blocks;  /* Number 512-byte blocks allocated. */
    long          st_atime;   /* Time of last access. */
    long          st_mtime;   /* Time of last modification. */
    long          st_ctime;   /* Time of last status change. */
};
```

实践中的 `stat foo`：

```text
File: 'foo'
Size: 6
Blocks: 8
IO Block: 4096
regular file
Device: ...
Inode: 1328649
Links: 1
Access: (0664/-rw-rw-r--)
Uid: (1000/os)
Gid: (1000/os)
Access: ...
Modify: ...
Change: ...
Birth: -
```

对应关系：

- `st_ino` -> `Inode`。
- `st_size` -> `Size`。
- `st_nlink` -> `Links`。
- `st_mode` -> 文件类型 + 权限。
- `st_uid/st_gid` -> owner/group。
- `st_blocks` -> 分配的 512-byte blocks 数。

## 15.7 为什么删除文件叫 unlink

实践 PPT 提问：

```text
Why we just “remove” or “delete” the file, but using “unlinkat”?
```

`strace rm tmp` 中关键行：

```text
unlinkat(AT_FDCWD, "tmp", 0) = 0
```

原因：

创建文件做了两件事：

1. 创建 inode，记录几乎所有文件相关信息。
2. 把人类可读名字链接到 inode，并把这个链接放进目录。

删除文件本质上是：

```text
从目录中解除这个名字到 inode 的链接
```

所以系统调用叫 `unlink` 或 `unlinkat`。

如果 inode 的链接计数降到 0，并且没有进程还打开它，文件系统才释放 inode 和数据块。

---

# 16. 硬链接和软链接

## 16.1 Link 的概念

PPT 定义：

一个文件可以在一个或多个目录中被多个名字引用。这些多个名字叫 links。

两种链接：

- hard link。
- soft link，也叫 symbolic link 或 symlink。

## 16.2 Hard link：硬链接

PPT 定义：

硬链接是一个 directory entry，它关联到一个文件。

换句话说，硬链接不是额外的特殊文件，而是“另一个目录项指向同一个 inode”。

例子：

```text
目录项 A: "hello" -> inode 100
目录项 B: "hi"    -> inode 100
```

`hello` 和 `hi` 是同一个文件的两个名字。

`link()` 系统调用：

```c
link(old_pathname, new_pathname)
```

它接受两个参数：

- old pathname。
- new pathname。

效果：

- 创建另一种引用同一文件的方式。
- old 和 new 具有相同 inode number。
- inode 的 hard link count 增加。

实践 PPT 强调：

- 即使空目录也有两个 entry。
- 这两个是 `.` 和 `..`。

含义：

- `.` 是指向目录自身的硬链接。
- `..` 是指向父目录的硬链接。

PPT 还说：

- `.` in a directory is a hard link to the directory itself。
- `..` is a hard link to the parent directory。

## 16.3 Reference count

`rm` 做的是 unlink，并检查 inode 的 reference count / link count。

规则：

```text
unlink 一个名字
  -> link count --
  -> 如果 link count > 0，文件内容还在
  -> 如果 link count == 0 且无打开引用，释放 inode 和数据块
```

这解释了为什么删除一个硬链接名字不一定删除文件实体。

## 16.4 Soft link：软链接/符号链接

PPT 定义：

软链接是一个文件，文件内容是另一个文件的路径名。

例如软链接 `shortcut` 的数据块内容可能是：

```text
../xxx/path_to_target_file
```

特点：

- 软链接有自己的 inode。
- 软链接文件内容保存目标路径。
- 不增加目标文件的 hard link number。
- 可以指向目录。
- 可以跨文件系统边界。
- 如果目标文件被删除，软链接会失效，成为 dangling symlink。

对比：

| 特性 | 硬链接 | 软链接 |
|---|---|---|
| 本质 | 目录项直接指向同一个 inode | 一个特殊文件，内容是目标路径 |
| inode | 与目标相同 inode | 有自己的 inode |
| link count | 增加目标 hard link count | 不增加目标 hard link count |
| 跨文件系统 | 通常不行 | 可以 |
| 指向目录 | 通常受限制 | 可以 |
| 目标删除后 | 只删一个名字，inode 可能仍在 | 软链接变成无效路径 |

---

# 17. 实践：文件系统磁盘布局示例

实践 PPT 用一个小文件系统说明布局。

假设：

- 一串 blocks。
- block size = 4KB。
- 共 64 blocks。

## 17.1 Data region

保留部分块作为数据区：

```text
56 of 64 blocks for data
```

数据区存普通文件内容和目录内容。

## 17.2 Inode table

保留 5 个 blocks 存 inode table。

假设：

```text
inode size = 256 bytes
block size = 4KB = 4096 bytes
1 block 可放 4096 / 256 = 16 inodes
5 blocks 可放 5 * 16 = 80 inodes
```

所以这个小文件系统最多支持约 80 个 inode，也就是 80 个文件系统对象，包括普通文件和目录。

注意：文件数量上限不只由数据区大小决定，也由 inode 数量决定。即使还有很多数据块，如果 inode 用完，也不能创建新文件。

## 17.3 Bitmap

使用 bitmap 管理空闲空间：

- 一个 inode bitmap：哪些 inode 空闲。
- 一个 data region bitmap：哪些数据块空闲。

创建文件时：

1. 在 inode bitmap 找空闲 inode。
2. 如果要写数据，在 data bitmap 找空闲数据块。

删除文件时：

1. 释放 inode，对应 inode bitmap 置为空闲。
2. 释放数据块，对应 data bitmap 置为空闲。

## 17.4 Superblock

Superblock 保存文件系统整体信息：

- 有多少 inodes。
- 有多少 data blocks。
- inode table 从哪里开始。
- data region 从哪里开始。
- magic number。

Magic number 用来识别文件系统类型或判断 superblock 是否有效。

## 17.5 inode 地址计算

PPT 示例：

```text
inode size = 256 bytes
block size = 4KB
1 block = 16 inodes
5 blocks = 80 inodes
```

每个 inode 用 inumber 标识。

读取 inode number 32：

```text
32 * sizeof(inode) = 32 * 256 = 8192 bytes = 8KB
```

假设布局：

```text
superblock: 4KB
bitmaps:    8KB
inode table starts after 12KB
```

那么 inode 32 的地址：

```text
4KB(superblock) + 8KB(bitmap) + 8KB(offset in inode table) = 20KB
```

这说明 inode number 可以通过固定公式定位到 inode table 中的具体位置。

---

# 18. 读写路径示例：/foo/bar

实践 PPT 给了 `/foo/bar` 读写过程。

## 18.1 Read /foo/bar

假设：

- `foo` 是目录。
- `bar` 是 `foo` 目录中的文件。

路径：

```text
/ + foo/ + bar
```

读取过程：

1. 从根目录 `/` 开始。
2. 读根目录 inode。
3. 读根目录数据块，查找目录项 `foo`。
4. 得到 `foo` 的 inode number。
5. 读 `foo` 的 inode。
6. 读 `foo` 的目录数据块，查找目录项 `bar`。
7. 得到 `bar` 的 inode number。
8. 读 `bar` 的 inode。
9. 根据 `bar` inode 中的数据块指针读文件内容。
10. 更新 access time。

没有缓存时，每一级目录可能都要多次 I/O。有缓存后，根目录、`foo` 目录、`bar` inode 可能已经在内存中。

## 18.2 Write to disk: /foo/bar

如果要写 `/foo/bar`，并且 `bar` 不存在：

1. 找到根目录。
2. 找到 `foo` 目录。
3. 在 `foo` 目录中搜索 `bar`，发现不存在。
4. 分配新的 inode 给 `bar`。
5. 在 `foo` 的目录数据块中写入目录项：

```text
"bar" -> new inode number
```

6. 分配数据块写入文件内容。
7. 更新元数据：
   - 目录修改时间。
   - inode link count。
   - 文件大小。
   - 访问/修改/状态改变时间。
   - bitmap。
8. 根据缓存策略，可能先留在内存中，稍后写回磁盘。

---

# 19. Caching and buffering：缓存与缓冲

实践 PPT 总结：

- 没有 caching 时，每次 file open 对目录每一级都需要两次读取：
  - 一次 inode。
  - 一次 data。
- 早期系统分配固定大小 cache 保存热门 blocks。
- 现代系统使用 unified page cache，同时缓存虚拟内存页和文件系统页。
- Write buffering 不立即写磁盘，而是在 5-30 秒后同步到磁盘。
- 数据库可能使用 direct I/O with raw data。

为什么数据库可能绕过普通文件系统缓存？

数据库自身有 buffer pool、日志、事务恢复机制。如果 OS 再缓存一份，可能重复缓存、难以控制写入顺序。所以数据库常用 direct I/O 或特殊配置，让自己管理缓存和持久化。

---

# 20. 三份 PPT 的整体知识链

现在把所有内容串起来。

## 20.1 用户视角

用户以为文件系统是：

```text
mkdir
cd
ls
open
read
write
close
rm
chmod
ln
```

用户看到的是：

- 文件名。
- 路径。
- 目录。
- 权限。
- 文件类型。
- 文件大小。

## 20.2 内核视角

内核看到的是：

```text
pathname -> dentry -> inode -> file object -> file_operations
```

以及：

```text
file logical block -> physical block -> block I/O -> device driver
```

## 20.3 磁盘视角

磁盘看到的是：

```text
block 0
block 1
block 2
...
```

其中一些块用于：

- boot block。
- superblock。
- inode bitmap。
- data bitmap。
- inode table。
- data region。
- directory data。
- file data。

## 20.4 一次 open/read/write 的完整路线

以：

```c
int fd = open("/foo/bar", O_RDONLY);
read(fd, buf, 100);
close(fd);
```

为例：

```text
open("/foo/bar")
  -> VFS 接收 syscall
  -> 解析路径 "/"
  -> 查找 "foo" 的 dentry/inode
  -> 查找 "bar" 的 dentry/inode
  -> 检查权限
  -> 创建 file object
  -> 设置 file->f_op
  -> 加入系统级打开文件表
  -> 加入进程 fd 表
  -> 返回最小可用 fd，例如 3

read(3, buf, 100)
  -> 从当前进程 fd 表找到 file object
  -> 通过 file object 找 inode 和 f_op
  -> VFS 调具体文件系统 read/read_iter
  -> 文件系统把 offset 映射为逻辑块
  -> inode 把逻辑块映射为物理块
  -> page cache 命中则直接返回
  -> 未命中则发起 block I/O
  -> 驱动读设备
  -> 数据进入内存
  -> 拷贝到用户 buf
  -> 更新 file offset

close(3)
  -> 删除进程 fd 表项
  -> 减少打开引用计数
  -> 必要时释放 file object
```

## 20.5 一次 rm 的完整路线

```text
rm tmp
  -> 用户命令 rm 调用 unlinkat(AT_FDCWD, "tmp", 0)
  -> VFS 找当前目录中的 "tmp"
  -> 找到对应 inode
  -> 从目录中删除这个目录项
  -> inode link count --
  -> 如果 link count == 0 且没有进程打开
       释放数据块
       释放 inode
       更新 bitmaps
  -> 否则文件实体暂时保留
```

所以“删除文件”在 Unix 里叫 unlink，不是因为术语奇怪，而是因为它真的在解除名字和 inode 的链接。

---

# 21. 初学者最容易混淆的点

## 21.1 文件名不是 inode

错误理解：

```text
文件名就是文件。
```

正确理解：

```text
文件名是目录项里的字符串。
目录项把字符串映射到 inode。
inode 才保存文件元数据和数据块指针。
```

硬链接能存在，就是因为多个文件名可以映射到同一个 inode。

## 21.2 fd 不是 inode

错误理解：

```text
fd 就是 inode number。
```

正确理解：

```text
fd 是当前进程 fd table 的索引。
fd -> file object -> inode
```

同一个 inode 可以被多个 fd 引用。

同一个路径多次 open 可能得到多个不同 file object。

## 21.3 write 返回不等于数据已经落盘

错误理解：

```text
write 成功，数据一定已经在磁盘上。
```

正确理解：

```text
write 成功，通常只是内核接受了数据。
fsync 成功，才强制脏数据写到磁盘。
```

这也是为什么数据库、编辑器、文件系统日志需要认真处理 `fsync`。

## 21.4 hard link 和 soft link 完全不同

硬链接：

```text
另一个名字 -> 同一个 inode
```

软链接：

```text
一个特殊文件，内容是目标路径
```

目标删除后：

- 硬链接仍可访问 inode。
- 软链接可能失效。

## 21.5 目录也是文件，但内容格式特殊

Unix 里目录可以理解为特殊文件，它的数据块保存目录项，而不是普通用户文本。

目录项核心：

```text
name -> inode number
```

---

# 22. 按 PPT 的 takeaway 汇总

## 22.1 `13_fs_interface.pdf`

你需要掌握：

- File system 是对 disk 的抽象。
- 对用户进程，文件系统提供一组文件的 coherent view。
- Unix 中文件常看作连续字节块。
- 文件系统提供 protection。
- 文件概念：
  - 文件是连续逻辑空间。
  - 可保存数据库、音频、视频、网页、程序等。
  - 有数据文件、程序文件、特殊文件。
- 文件属性：
  - name。
  - identifier。
  - type。
  - location。
  - size。
  - protection。
  - time/date/user id。
  - extended attributes。
- 文件操作：
  - create。
  - open。
  - read/write。
  - seek。
  - close。
  - delete/unlink。
  - truncate。
- 打开文件所需数据：
  - open-file table。
  - file pointer。
  - file-open count。
  - disk location cache。
  - access rights。
- 文件锁：
  - shared/exclusive。
  - mandatory/advisory。
- 文件类型：
  - extension。
  - magic number。
- 文件结构：
  - no structure。
  - simple record。
  - complex structures。
- 访问方法：
  - sequential access。
  - direct/random access。
  - indexed access。
- 目录结构：
  - single-level。
  - two-level。
  - tree。
  - acyclic graph。
  - general graph。
- mounting。
- file sharing。
- remote file sharing。
- protection。
- ACL。
- Unix owner/group/others + rwx。

## 22.2 `14_fs_implementation.pdf`

你需要掌握：

- 文件系统历史：
  - early FS。
  - hierarchical FS。
  - network FS。
  - journaling FS。
  - modern FS。
- 文件系统可分层：
  - logical file system。
  - file-organization module。
  - basic file system。
  - I/O control。
- FCB/inode 是文件元数据核心。
- on-disk structures：
  - boot control block。
  - volume control block/superblock。
  - directory。
  - per-file FCB。
- in-memory structures：
  - mount table。
  - directory cache。
  - global open-file table。
  - per-process open-file table。
  - buffers。
- file creation：
  - 分配 inode/FCB。
  - 更新目录。
- open：
  - 查系统级打开文件表。
  - 查目录。
  - 加载 FCB。
  - 创建进程级表项。
  - 维护 open count。
- UFS inode。
- mounting root and external FS。
- VFS：
  - common interface。
  - dispatch to FS implementation。
  - superblock/inode/dentry/file。
  - function table。
- directory implementation：
  - linear list。
  - hash table。
- allocation methods：
  - contiguous。
  - linked。
  - FAT。
  - indexed。
  - Unix direct/indirect combined scheme。
- free-space management：
  - bitmap。
  - linked free space。
  - grouping。
  - counting。
- performance：
  - allocation and directory algorithms。
  - cache。
  - async/sync writes。
  - read-ahead/free-behind。
  - unified buffer cache。
- recovery：
  - consistency checking。
  - backup。
  - log-structured FS。

## 22.3 `14_fs_in_practice.pdf`

你需要掌握：

- File 是线性字节数组，有低层 inode number。
- Directory 负责 name -> inode number。
- external name 是路径名，internal name 是 inode。
- `open("foo", O_CREAT | O_WRONLY | O_TRUNC)`。
- open 返回 file descriptor。
- fd 是 per-process file descriptor table 的索引。
- fd -> file object -> inode。
- stdin/stdout/stderr 分别是 0/1/2。
- `cat main.c` 中 `openat(...)=3` 表示 `main.c` fd 是 3。
- `write()` 只保证未来某时写入持久存储。
- `fsync()` 强制脏数据落盘。
- 文件信息在 `struct stat` 中。
- `rm` 实际调用 `unlinkat`。
- 创建文件 = 创建 inode + 把名字链接到 inode。
- 删除文件 = unlink 名字。
- hard link 是目录项，多个名字同一个 inode。
- `.` 是指向目录自身的硬链接。
- `..` 是指向父目录的硬链接。
- soft link 是包含目标路径名的文件。
- soft link 有不同 inode，不增加目标 hard link number。
- 目标删除后 soft link 失效。
- 文件系统可分为：
  - VFS data structure。
  - in-memory data structure。
  - on-disk data structure。
- 示例磁盘布局：
  - superblock。
  - inode bitmap。
  - data bitmap。
  - inode table。
  - data region。
- inode 地址可由 inumber 和 inode size 计算。
- 读 `/foo/bar` 要逐级解析目录。
- 创建/写 `/foo/bar` 要更新目录项和元数据。
- caching 可避免每级目录两次读。
- modern systems 使用 unified page cache。
- 数据库可能使用 direct I/O with raw data。

---

# 23. 一组自测题

## 23.1 概念题

1. 为什么文件系统不是让用户直接操作磁盘扇区？
2. 文件名、目录项、inode 三者分别是什么？
3. `open()` 返回的 fd 是什么？它和 inode number 一样吗？
4. 为什么 `rm` 底层调用 `unlinkat`？
5. 硬链接和软链接的根本区别是什么？
6. `write()` 成功后为什么还可能丢数据？
7. VFS 为什么能让同一个 `write()` 同时支持 ext4 和 NFS？
8. 目录为什么可以说是特殊文件？
9. bitmap 管理空闲块的优点和缺点是什么？
10. 日志文件系统为什么能加速崩溃恢复？

## 23.2 计算题

题 1：如果 block size = 4KB，inode size = 256B，一个 inode table block 能放多少 inode？

答案：

```text
4096 / 256 = 16
```

题 2：如果磁盘大小 1TB，block size 4KB，用 bitmap 表示每个块是否空闲，需要多少 bitmap 空间？

答案：

```text
1TB = 2^40 bytes
4KB = 2^12 bytes
blocks = 2^40 / 2^12 = 2^28
bitmap = 2^28 bits = 2^25 bytes = 32MB
```

题 3：如果 block size = 512B，pointer = 4B，一个 indirect block 能存多少指针？

答案：

```text
512 / 4 = 128
```

题 4：Unix inode 有 12 个 direct pointer，1 个 single indirect，1 个 double indirect，1 个 triple indirect。block size = 512B，pointer = 4B，最大文件大小公式是什么？

答案：

```text
12*512 + 128*512 + 128^2*512 + 128^3*512 bytes
```

## 23.3 路径解析题

给定：

```text
/foo/bar
```

其中 `foo` 是目录，`bar` 是文件。解释读取 `bar` 的步骤。

参考答案：

```text
1. 从 root inode 开始
2. 读 root directory data，找 foo
3. 得到 foo inode number
4. 读 foo inode，确认是目录
5. 读 foo directory data，找 bar
6. 得到 bar inode number
7. 读 bar inode
8. 根据 bar inode 的块指针读数据块
9. 更新访问时间或相关缓存状态
```

---

# 24. 最后一张总图

```text
                             用户视角
        ----------------------------------------------------
        path: /foo/bar
        operations: open/read/write/close/link/unlink/stat
        permissions: rwx, ACL

                             VFS 层
        ----------------------------------------------------
        dentry: name -> inode
        inode: metadata + block pointers
        file: opened-file state, offset, f_op
        superblock: mounted filesystem metadata

                             具体文件系统
        ----------------------------------------------------
        ext4 / FAT / NTFS / NFS / procfs / tmpfs ...
        directory implementation
        allocation methods
        free-space management
        journaling/recovery

                             块 I/O 与设备
        ----------------------------------------------------
        logical block -> physical block
        cache/buffer/page cache
        driver, interrupt, device controller
        disk / SSD / network storage
```

如果你只背一句话，请背这句：

```text
文件系统的核心工作，是把用户可理解的“名字和字节序列”，可靠、高效、安全地映射到底层设备上的“块”。
```

---

# 25. 期末理解拓展强化：从会背到会答题

这一节是对前面内容的“考试型深化”。它不只是补充更多名词，而是训练你在期末考试中最常见的能力：

- 看到一个系统调用，能说出内核里发生了什么。
- 看到两个概念，能比较它们的差异和适用场景。
- 看到一个设计，能解释它解决了什么问题、带来了什么代价。
- 看到一个文件系统故障或性能现象，能沿着路径、inode、缓存、磁盘块去推理。

---

## 25.1 文件系统这一章到底想考什么

文件系统章节表面上有很多名词：file、directory、inode、VFS、bitmap、FAT、ACL、hard link、soft link、page cache、fsync。真正的主线只有一条：

```text
用户想用名字访问数据
        |
        v
文件系统把名字翻译成 inode
        |
        v
inode 把文件偏移翻译成数据块
        |
        v
缓存和块 I/O 把数据块读写到设备
```

所以期末常考的不是“inode 是什么”这种孤立定义，而是：

1. 为什么文件名不直接等于文件？
2. 为什么需要目录？
3. 为什么需要 inode？
4. 为什么需要打开文件表？
5. 为什么 `write()` 返回后还需要 `fsync()`？
6. 为什么 VFS 可以支持多种文件系统？
7. 为什么不同块分配方法有不同性能？
8. 为什么文件系统崩溃后需要恢复机制？

你回答任何文件系统题，都可以先找它属于哪条链：

```text
命名链：路径名 -> 目录项 -> inode
打开链：fd -> file object -> inode
存储链：offset -> logical block -> physical block
权限链：uid/gid/mode/ACL -> allow/deny
一致性链：metadata update -> log/journal -> recovery
性能链：cache -> locality -> fewer I/Os
```

---

## 25.2 文件抽象：为什么 OS 把存储抽象成文件

PPT 说 storage is abstracted to file system。考试可能不会只问这句话，而会问：

```text
为什么操作系统要提供文件系统抽象，而不是让应用直接读写磁盘块？
```

标准答题思路：

1. 磁盘块地址对人不友好。
   - 用户想记 `report.txt`，不想记 block 183942。
2. 磁盘物理布局会变化。
   - 文件增长、删除、移动、坏块重映射都会改变物理位置。
3. 需要统一接口。
   - 程序不应关心数据在 HDD、SSD、NFS 还是 RAM disk。
4. 需要共享与保护。
   - 多用户、多进程环境下要控制谁能读写执行。
5. 需要可靠性。
   - 崩溃后要知道哪些数据和元数据是一致的。
6. 需要性能优化。
   - OS 可以统一做缓存、预读、写回、调度。

一句考试答案：

```text
文件系统把低层的物理块抽象成高层的命名字节流，使应用用统一接口访问持久数据，同时由操作系统负责命名、保护、共享、空间管理、缓存和恢复。
```

容易丢分点：

- 只说“方便用户”，不够。
- 必须提到至少几个系统层面的理由：保护、共享、空间管理、性能、可靠性。

---

## 25.3 文件名、目录项、inode：期末必考关系

这是整章最核心的理解点。

### 25.3.1 三者不是一回事

```text
文件名：人类可读字符串，例如 "main.c"
目录项：目录文件中的一条记录，例如 "main.c" -> inode 1328649
inode：文件系统对象的内部编号和元数据结构
```

换句话说：

```text
name is not file
directory maps name to inode
inode represents the file-system object
```

### 25.3.2 为什么 inode 不保存文件名

因为同一个 inode 可以有多个名字，也就是硬链接。

如果 inode 里只保存一个文件名，那么下面这种情况就无法自然表达：

```text
/home/a/report -> inode 100
/tmp/backup    -> inode 100
```

这两个路径是同一个文件的两个名字。文件名属于目录项，不属于 inode，这样多个目录项就能指向同一个 inode。

### 25.3.3 考试可能这样问

题目：

```text
为什么 Unix 删除文件的系统调用叫 unlink，而不是 delete？
```

高分答案：

```text
因为 Unix 文件名本质上是目录项中从名字到 inode 的链接。删除一个路径名只是从目录中移除该目录项，使 inode 的链接计数减一。只有当链接计数为 0 且没有进程仍打开该 inode 时，文件系统才真正释放 inode 和数据块。因此底层操作更准确地说是 unlink，而不是立即删除文件实体。
```

这道题必须答出三层：

1. 文件名是链接。
2. unlink 使 link count 减少。
3. link count 为 0 且无打开引用才释放实体。

---

## 25.4 fd、file object、inode：打开文件后的三层关系

很多初学者会把 fd、file、inode 混在一起。考试很喜欢考这个。

### 25.4.1 三层结构

```text
进程 fd table
  fd 3
   |
   v
系统打开文件对象 file object
  current offset
  open mode
  flags
  f_op
   |
   v
inode
  metadata
  data block pointers
```

fd 是进程私有的整数索引。file object 是内核中表示“一次打开”的对象。inode 是文件系统对象本身。

### 25.4.2 多次 open 同一个文件会怎样

代码：

```c
int fd1 = open("a.txt", O_RDONLY);
int fd2 = open("a.txt", O_RDONLY);
```

通常结果：

```text
fd1 -> file object 1 -> inode X
fd2 -> file object 2 -> inode X
```

两个 fd 指向不同 file object，所以各自有独立 offset，但最终指向同一个 inode。

### 25.4.3 dup 或 fork 会怎样

代码：

```c
int fd1 = open("a.txt", O_RDONLY);
int fd2 = dup(fd1);
```

通常结果：

```text
fd1 \
     -> same file object -> inode X
fd2 /
```

这意味着 fd1 和 fd2 共享同一个 current offset。

### 25.4.4 考试可能这样问

题目：

```text
两个进程同时打开同一个文件，它们是否共享文件偏移？为什么？
```

答题模板：

```text
如果是两个独立的 open，一般不共享文件偏移，因为每次 open 创建独立的 file object，每个 file object 有自己的 current offset，但它们可以指向同一个 inode。

如果是 fork 后继承的文件描述符，或者通过 dup 复制出来的文件描述符，则可能共享同一个 open file description，因此共享 current offset。
```

这类题关键是不要只答“共享”或“不共享”，要看 fd 是否指向同一个 file object。

---

## 25.5 `open()` 的理解：不是“打开文件”这么简单

`open()` 在用户看来是一行：

```c
int fd = open("/foo/bar", O_RDONLY);
```

但内核里至少做了这些事：

```text
1. 从当前进程或根目录开始解析路径
2. 查找目录项 foo
3. 读取或命中 foo 的 inode/dentry
4. 查找目录项 bar
5. 读取或命中 bar 的 inode/dentry
6. 检查权限
7. 创建 file object
8. 设置 file object 的 offset、mode、flags、f_op
9. 在进程 fd table 中找最小可用 fd
10. 让 fd 指向 file object
11. 返回 fd
```

### 25.5.1 `open()` 为什么返回最小可用 fd

这是 Unix 传统接口约定。进程开始时通常已有：

```text
0 stdin
1 stdout
2 stderr
```

所以第一次打开普通文件通常返回 3。

这也是 PPT 中 `strace cat main.c` 看到：

```text
openat(..., "main.c", O_RDONLY) = 3
read(3, ...)
write(1, ...)
```

`main.c` 的 fd 是 3，输出写到 fd 1。

### 25.5.2 `O_CREAT | O_WRONLY | O_TRUNC` 的组合含义

```c
open("foo", O_CREAT | O_WRONLY | O_TRUNC)
```

可以拆成三句话：

- `O_CREAT`：如果不存在，创建目录项和 inode。
- `O_WRONLY`：这个 file object 的访问模式是只写。
- `O_TRUNC`：如果已经存在，打开时把文件大小截断为 0。

考试容易问：

```text
如果文件原来存在且大小为 1MB，执行 O_TRUNC 后会发生什么？
```

答案：

```text
文件仍是同一个路径对应的文件对象，权限等元数据大多保留，但文件内容被截断，逻辑大小变为 0；原来占用的数据块会被释放或标记可回收，mtime/ctime 等元数据会更新。
```

---

## 25.6 `write()`、缓存、`fsync()`：可靠性题高频点

这是期末最容易考“理解”的地方。

### 25.6.1 `write()` 成功到底表示什么

`write(fd, buf, size)` 返回 `size`，通常只表示：

```text
内核已经接受了这批数据，并把它放入页缓存或缓冲区，未来会写回存储设备。
```

它不一定表示：

```text
数据已经到达磁盘盘片或 SSD 非易失介质。
```

原因是文件系统会为了性能做 write buffering：

- 多个小写合并为大写。
- 重新排序写入顺序。
- 延迟写，减少设备访问。
- 让应用尽快返回。

### 25.6.2 `fsync()` 解决什么问题

`fsync(fd)` 强制把该文件相关的 dirty data 和必要元数据刷到持久存储。

典型使用场景：

- 数据库提交事务。
- 编辑器保存重要文件。
- 文件系统元数据更新。
- 日志系统保证某条日志真正落盘。

### 25.6.3 考试可能这样问

题目：

```text
程序调用 write() 写入文件后立刻崩溃，重启后文件中一定有这次写入的数据吗？为什么？
```

高分答案：

```text
不一定。普通 write() 成功通常只说明数据已经被内核接收，可能仍在 page cache 或 buffer 中，尚未写到持久设备。若系统在脏数据写回前崩溃，这部分数据可能丢失。若程序需要持久化保证，应调用 fsync() 或使用同步写模式，使脏数据和必要元数据在返回前写到磁盘。
```

必须答出：

- write 和持久化不是一回事。
- dirty cache 可能丢。
- fsync 或 synchronous write 才提供更强保证。

### 25.6.4 进一步理解：数据和元数据都重要

假设你创建新文件：

```text
create "a.txt"
write content
fsync(fd)
```

你可能还需要确保目录项也持久化。严格系统编程中，创建新文件后还可能需要 fsync 所在目录。课程未必细考，但理解上要知道：

```text
文件内容是 data。
目录项、inode、bitmap 是 metadata。
崩溃一致性不仅要求数据写回，也要求元数据状态一致。
```

---

## 25.7 硬链接和软链接：考试对比题模板

这部分很适合出简答题或判断题。

### 25.7.1 本质区别

```text
硬链接：目录项直接指向同一个 inode。
软链接：一个独立文件，文件内容是目标路径名。
```

### 25.7.2 关键对比

| 问题 | 硬链接 | 软链接 |
|---|---|---|
| 是否有独立 inode | 没有新文件实体，目录项指向原 inode | 有自己的 inode |
| 是否增加目标 link count | 增加 | 不增加 |
| 目标删除后 | 只要还有硬链接，文件仍存在 | 软链接可能失效 |
| 是否能跨文件系统 | 通常不能 | 可以 |
| 是否能链接目录 | 通常限制普通用户 | 可以 |
| 访问时多一步路径解析 | 不需要 | 需要读取软链接内容再解析目标路径 |

### 25.7.3 为什么硬链接通常不能跨文件系统

因为 inode number 只在一个文件系统内部有意义。

硬链接目录项保存的是 inode number。如果跨到另一个文件系统，那个 inode number 不再唯一，也不属于当前文件系统的 inode table。

软链接保存的是路径字符串，所以可以跨文件系统。

### 25.7.4 为什么普通用户通常不能给目录创建硬链接

如果目录允许任意硬链接，容易制造目录环：

```text
A -> B -> C -> A
```

这样会破坏树形目录结构，使路径遍历、删除、引用计数回收变复杂，甚至导致无限递归。

### 25.7.5 判断题训练

判断：

```text
删除软链接会删除目标文件。
```

答案：错。删除软链接只删除这个独立的 symlink 文件，不影响目标。

判断：

```text
删除目标文件后，硬链接一定失效。
```

答案：错。如果所谓“目标文件”只是其中一个目录项，删除它只是 link count 减一，其他硬链接仍可访问同一 inode。

判断：

```text
软链接可以指向一个不存在的路径。
```

答案：对。软链接本质是保存路径字符串，它可以成为 dangling symlink。

---

## 25.8 权限和 ACL：不要只背 rwx

### 25.8.1 文件上的 rwx

普通文件：

- `r`：可读文件内容。
- `w`：可修改文件内容。
- `x`：可作为程序执行。

目录：

- `r`：可列出目录项名称。
- `w`：可在目录中创建、删除、重命名目录项，通常还需要 `x` 配合。
- `x`：可进入目录、穿过目录进行路径解析。

这是考试常考易错点：目录的 `x` 不是“执行目录”，而是“搜索/进入权限”。

### 25.8.2 删除文件需要看哪个权限

在 Unix 语义下，删除一个文件本质是从父目录中移除目录项。因此删除文件主要看父目录权限，而不是只看文件本身的写权限。

常见高分表达：

```text
删除文件是修改父目录的内容，即删除父目录中的 name -> inode 映射，所以需要对父目录有写和执行权限。文件自身的写权限控制修改文件内容，不直接等价于删除该目录项的权限。
```

课程可能不展开 sticky bit，但你至少要知道“删除是目录操作”。

### 25.8.3 ACL 的设计意义

传统 Unix 权限只有三类：

```text
owner / group / others
```

如果想表达：

```text
用户 alice 可读写
用户 bob 只读
用户 carol 无权限
组 students 可读
```

三类权限就不够细。ACL 解决细粒度授权问题。

代价：

- 元数据更复杂。
- 权限检查更复杂。
- ACL 存储需要额外空间。
- 用户多时管理复杂。

考试问优缺点时就按“细粒度 vs 复杂度”回答。

---

## 25.9 目录结构：为什么从单级走到树、图

PPT 列了 single-level、two-level、tree、acyclic graph、general graph。考试常问对比，不会只让你画图。

### 25.9.1 单级目录的问题

```text
所有用户所有文件都在一个目录
```

问题：

- 命名冲突。
- 不方便分组。
- 文件多时搜索慢。
- 不支持自然的项目/用户组织。

### 25.9.2 两级目录解决什么

```text
MFD -> 每个用户一个 UFD
```

解决：

- 不同用户可有同名文件。
- 搜索范围缩小。

仍然不够：

- 用户内部文件仍难分组。
- 跨用户共享不自然。

### 25.9.3 树形目录为什么成为主流

树形目录支持层次化组织：

```text
/home/alice/project/src/main.c
```

优点：

- 分组自然。
- 路径命名清晰。
- 搜索可逐层缩小。
- 适合大型系统。

缺点：

- 天然不支持同一文件在多个位置共享。

### 25.9.4 无环图目录引入链接

无环图允许共享：

```text
多个路径 -> 同一文件
```

但要处理：

- dangling pointer。
- reference count。
- 删除时何时释放实体。

### 25.9.5 一般图为什么危险

一般图允许环，会导致：

- 遍历可能无限循环。
- 回收空间需要垃圾回收或环检测。
- 删除目录语义复杂。

期末答题金句：

```text
目录结构越灵活，共享能力越强，但命名、遍历和回收的复杂度也越高。
```

---

## 25.10 VFS：为什么“一层间接”这么重要

### 25.10.1 VFS 解决的问题

没有 VFS 时，不同文件系统可能需要不同接口：

```text
ext4_read
fat_read
nfs_read
proc_read
```

应用程序会被具体文件系统绑死。

VFS 引入统一抽象：

```text
read(fd, buf, size)
  -> vfs_read
  -> file->f_op->read_iter
  -> ext4/nfs/procfs 的具体实现
```

### 25.10.2 VFS 的四对象要这样理解

| VFS 对象 | 初学者理解 | 典型作用 |
|---|---|---|
| superblock | 一个挂载文件系统的总说明书 | 文件系统类型、大小、状态 |
| inode | 一个文件系统对象的身份证和档案 | 权限、大小、块指针、owner |
| dentry | 名字解析缓存 | 把名字关联到 inode |
| file | 一次打开的运行时状态 | offset、flags、f_op |

最容易混的是 inode 和 file：

```text
inode 是“文件对象本身”的元数据。
file 是“某次打开”的运行时状态。
```

### 25.10.3 `file->f_op` 的考试解释

`f_op` 是函数表指针。它让同一个系统调用可以被分派到不同文件系统实现。

例如：

```text
write(fd)
  -> vfs_write
  -> file->f_op->write_iter(...)
```

如果 fd 是 ext4 文件：

```text
file->f_op = ext4_file_operations
```

如果 fd 是 NFS 文件：

```text
file->f_op = nfs_file_operations
```

答题抓手：

```text
VFS 定义统一接口，具体文件系统填充对应操作函数表。系统调用通过 VFS 对象中的函数指针进行间接调用，从而实现同一 API 对不同文件系统的多态分派。
```

---

## 25.11 on-disk 与 in-memory：考试常见分类题

### 25.11.1 on-disk structures

断电后必须还在，可用于恢复文件系统：

- boot control block。
- superblock / volume control block。
- inode table / FCB。
- directories。
- free-space bitmap。
- data blocks。

### 25.11.2 in-memory structures

运行时加速或管理状态，断电后可以重建：

- mount table。
- directory cache / dentry cache。
- inode cache。
- global open-file table。
- per-process open-file table。
- page cache / buffer cache。

### 25.11.3 常见题目

题目：

```text
为什么文件系统既需要磁盘上的数据结构，也需要内存中的数据结构？
```

高分答案：

```text
磁盘上的数据结构用于持久保存文件系统状态，例如 superblock、inode、目录和空闲空间信息，保证重启后仍能找到文件。内存中的数据结构用于运行时管理和性能优化，例如挂载表、打开文件表、目录缓存和页缓存，它们避免频繁访问磁盘，保存打开状态和当前偏移。两者分别服务于持久性和运行时效率。
```

---

## 25.12 块分配方法：考点不是背表，而是性能权衡

### 25.12.1 连续分配

```text
file = start block + length
```

优点：

- 顺序访问快。
- 随机访问简单。
- 元数据少。

缺点：

- 外部碎片。
- 文件增长困难。
- 需要预估大小或搬移文件。

适合：

- 大小预先知道、主要顺序访问、变化少的文件。

考试表达：

```text
连续分配用空间连续性换取访问性能，但牺牲动态增长灵活性。
```

### 25.12.2 链接分配

```text
block A -> block B -> block C
```

优点：

- 没有外部碎片。
- 文件增长容易。

缺点：

- 随机访问差。
- 指针占空间。
- 指针损坏影响可靠性。
- 块分散导致 seek 多。

适合：

- 顺序访问。

考试表达：

```text
链接分配用指针串联离散块，解决连续空间难找的问题，但随机访问必须沿链遍历，因此性能较差。
```

### 25.12.3 FAT

FAT 是链接分配的集中表版本：

```text
FAT[block] = next block
```

优点：

- 链指针集中管理。
- FAT 缓存在内存中时查找较快。

缺点：

- FAT 可能很大。
- FAT 损坏影响范围大。
- 对大磁盘、大文件扩展性不如现代索引/extent 设计。

### 25.12.4 索引分配

```text
index block: logical block -> physical block
```

优点：

- 支持随机访问。
- 无外部碎片。
- 支持文件空洞。

缺点：

- 小文件可能浪费索引块。
- 大文件需要多级索引。
- 访问数据可能要先读索引块。

考试表达：

```text
索引分配用额外索引结构换取随机访问能力，是空间开销和访问灵活性之间的折中。
```

### 25.12.5 Unix inode 的组合方案为什么好

直接块适合小文件：

```text
inode -> data block
```

间接块适合大文件：

```text
inode -> indirect block -> data blocks
```

组合方案的优点：

- 小文件不需要额外索引块，访问快。
- 大文件可以通过一级、二级、三级间接块扩展。
- 大多数系统中小文件数量很多，所以 direct pointers 很重要。

期末金句：

```text
Unix inode 的直接块和多级间接块组合，是为了同时优化小文件的低开销访问和大文件的可扩展性。
```

---

## 25.13 inode 最大文件大小计算：必须会

通用步骤：

1. 算每个索引块能放几个指针。
2. 算 direct 能覆盖多少数据。
3. 算 single indirect 能覆盖多少数据。
4. 算 double indirect 能覆盖多少数据。
5. 算 triple indirect 能覆盖多少数据。
6. 相加。

设：

```text
block size = B
pointer size = P
每个索引块指针数 N = B / P
direct pointer 数 = D
```

最大文件大小：

```text
D * B + N * B + N^2 * B + N^3 * B
```

如果题目只给 single/double，没有 triple，就只加到对应层级。

例题：

```text
block size = 4KB
pointer size = 4B
direct pointers = 12
single, double, triple each one
```

解：

```text
N = 4096 / 4 = 1024

direct = 12 * 4096
single = 1024 * 4096
double = 1024^2 * 4096
triple = 1024^3 * 4096
```

考试中可以不算最终巨大数字，公式正确通常就有大部分分。

易错点：

- 忘记 double indirect 是 `N^2`。
- 忘记 triple indirect 是 `N^3`。
- 把 pointer 数量和 byte 数量混淆。
- 把 inode 里的 indirect pointer 本身当数据块。

---

## 25.14 空闲空间管理：bitmap、linked、grouping、counting

### 25.14.1 bitmap 为什么容易找连续块

bitmap 中每个 bit 对应一个块。要找连续空闲块，就是找连续的 0 或 1，取决于系统约定。

例如：

```text
001111000010
```

连续的 `0000` 可能表示连续空闲区域。

优点：

- 结构紧凑。
- 容易扫描连续空闲块。
- 适合配合连续分配或 extent。

缺点：

- 大磁盘仍需要一定内存。
- 扫描 bitmap 也有成本。

### 25.14.2 linked free space 为什么不适合找连续块

空闲块链表只告诉你“下一个空闲块在哪里”，不直接告诉你这些块是否物理连续。

所以：

```text
free 5 -> free 100 -> free 7 -> free 300
```

你很难快速找到“从 100 到 120 全空闲”的区域。

### 25.14.3 grouping 和 counting 的设计思想

Grouping：

```text
一个空闲块中存多个空闲块地址
```

减少逐块遍历。

Counting：

```text
(start, count)
```

用一个记录表示连续空闲区域。

Counting 特别适合空间连续释放的情况。

考试答题抓手：

```text
bitmap 擅长判断和寻找连续空闲块；linked 方法空间开销低但不擅长连续分配；grouping 批量记录空闲块地址，减少遍历；counting 用起点和长度描述连续空闲区，利用空闲空间的连续性。
```

---

## 25.15 缓存：为什么文件系统性能题总绕不开 cache

### 25.15.1 没有缓存会怎样

打开 `/a/b/c/d.txt` 时，每一级目录都可能要：

```text
读 inode
读目录数据块
```

路径越深，I/O 越多。机械磁盘 I/O 非常慢，SSD 也远慢于 CPU。

### 25.15.2 缓存解决什么

常见缓存：

- dentry cache：缓存路径名解析结果。
- inode cache：缓存 inode。
- page cache：缓存文件数据页。
- buffer cache：传统上缓存磁盘块。

效果：

- 重复打开常用文件更快。
- 重复读取同一文件更快。
- 路径解析减少磁盘 I/O。
- 写入可合并和延迟。

### 25.15.3 read-ahead 和 free-behind

顺序访问时，文件系统可以预测未来：

```text
你读了 block 100, 101, 102
系统猜测你接下来会读 103, 104, 105
```

于是提前读，这叫 read-ahead。

读过且不再需要的旧页可以释放，这叫 free-behind。

### 25.15.4 为什么写可能看起来比读快

普通 buffered write 可以先写内存后返回。

读如果 cache miss，必须等设备把数据读上来。

所以从系统调用返回时间看：

```text
buffered write 可能很快
cold read 可能很慢
```

但这不表示写入设备本身更快，只是写被延迟了。

考试回答时要强调：

```text
这是由于缓存和异步写造成的表观差异，不是持久化写入一定比读取更快。
```

---

## 25.16 崩溃一致性：为什么日志文件系统重要

### 25.16.1 文件系统更新通常不是一步

创建文件可能要更新：

- inode bitmap。
- inode table。
- 父目录数据块。
- 父目录 inode 时间戳。
- data bitmap。
- data blocks。
- superblock 中的空闲计数。

如果更新到一半断电，就可能出现不一致：

```text
目录项指向一个未初始化 inode
inode 占用数据块，但 bitmap 认为该块空闲
bitmap 认为 inode 已用，但没有任何目录项指向它
link count 与实际目录项数不符
```

### 25.16.2 fsck 的思路

一致性检查会扫描磁盘结构，比较：

- 目录项和 inode 是否匹配。
- inode link count 是否正确。
- block bitmap 和 inode 指针是否冲突。
- free count 是否正确。

缺点：

- 大磁盘扫描慢。
- 复杂损坏可能无法完美恢复。

### 25.16.3 journaling/logging 的思路

先写日志：

```text
我要做这些元数据更新
```

日志安全写入后，再真正修改文件系统结构。

崩溃后：

```text
看日志中哪些 transaction 已提交但未应用
replay 它们
```

优点：

- 恢复快。
- 不必全盘扫描。
- 元数据一致性更好。

代价：

- 写日志有额外 I/O。
- 实现复杂。
- 如果记录数据日志，开销更大。

考试金句：

```text
日志文件系统用顺序写日志换取崩溃后的快速恢复和元数据一致性，本质是在性能开销与可靠性之间做折中。
```

---

## 25.17 典型综合题：从 `cat main.c` 推完整流程

题目：

```text
执行 cat main.c，strace 显示 openat(..., "main.c", O_RDONLY) = 3，
随后 read(3, ...)=89，write(1, ...)=89。解释发生了什么。
```

高分答案结构：

1. `openat` 打开当前目录下的 `main.c`。
2. 返回 3，因为 0、1、2 分别是 stdin、stdout、stderr，3 是最小可用 fd。
3. 内核通过目录项把 `main.c` 路径名解析到 inode。
4. 创建 file object，并让当前进程 fd table 的第 3 项指向它。
5. `read(3, ...)` 通过 fd 3 找到 file object，再找到 inode 和数据块，把文件内容读入缓冲区。
6. 返回 89，说明读到 89 字节。
7. `write(1, ...)` 把这 89 字节写到 stdout。
8. stdout 通常连接终端，所以用户看到文件内容。
9. 后续 `read(3, ...)=0` 表示 EOF。
10. `close(3)` 关闭文件描述符。

这个答案把接口、fd、inode、目录、read/write 全串起来，属于典型综合题。

---

## 25.18 典型综合题：创建新文件要更新哪些结构

题目：

```text
在目录 /foo 下创建文件 bar，并写入一些数据。文件系统可能需要更新哪些结构？
```

答题路线：

```text
路径解析
  -> 找到 /foo 目录 inode

创建文件元数据
  -> 分配空闲 inode
  -> 初始化 inode mode/owner/time/size/link count
  -> 更新 inode bitmap

创建名字映射
  -> 在 /foo 的目录数据块中添加 "bar" -> inode number
  -> 更新 /foo 目录 inode 的 mtime/ctime

写入数据
  -> 分配数据块
  -> 更新 data bitmap/free-space structure
  -> 写 data block
  -> 更新 bar inode 的 size、block pointers、mtime、ctime

性能与可靠性
  -> 这些更新可能先进入 page cache/buffer cache
  -> 若有 journaling，先写日志
  -> fsync 或后台 writeback 后落盘
```

高分点：

- 不能只说“写数据块”。
- 必须提到目录项、inode、bitmap/free space、时间戳、缓存/日志。

---

## 25.19 典型综合题：为什么删除打开中的文件后进程还能读

这是文件系统经典理解题。

场景：

```text
进程 A 打开 file.txt，得到 fd 3。
进程 B 执行 rm file.txt。
进程 A 继续 read(fd 3)。
```

问题：

```text
进程 A 还能读吗？为什么？
```

答案：

```text
通常仍然可以。rm 只是 unlink 目录项，使文件名到 inode 的链接计数减少。如果进程 A 已经打开该文件，它的 fd 仍指向 file object，file object 仍引用 inode。即使目录项被删除，只要 inode 仍被打开文件对象引用，内核不会立即释放文件数据。等 link count 为 0 且所有打开引用关闭后，inode 和数据块才会被释放。
```

这题必须同时提到：

- unlink 删除名字。
- fd/file object 仍引用 inode。
- 释放条件是 link count 和 open references 都没了。

---

## 25.20 典型综合题：VFS 写 ext4 和写 NFS 的区别

题目：

```text
同样调用 write(fd, buf, n)，如果 fd 指向 ext4 文件和 NFS 文件，内核路径有什么共同点和不同点？
```

答案：

共同点：

- 用户态都调用同一个 `write()` syscall。
- 都进入 VFS 通用层。
- 都通过 fd 找到 file object。
- 都通过 `file->f_op` 调用具体写操作。

不同点：

- ext4 的 `f_op` 指向 ext4 本地文件系统实现，最终读写本地块设备。
- NFS 的 `f_op` 指向 NFS 客户端实现，最终可能发起网络 RPC 到远程服务器。
- 缓存、一致性、错误模式不同；NFS 还涉及网络延迟、服务器状态、身份验证。

高分总结：

```text
VFS 统一了系统调用入口和对象模型，但具体语义和底层路径由 file object 中的操作函数表分派给相应文件系统实现。
```

---

## 25.21 高频易错判断题

1. `write()` 返回成功说明数据一定已经写入磁盘。
   - 错。可能还在缓存中。

2. inode number 在整个操作系统中全局唯一。
   - 错。通常只在同一个文件系统内唯一。

3. 文件名保存在 inode 中。
   - 错。文件名保存在目录项中。

4. 软链接和硬链接都会增加目标文件的 hard link count。
   - 错。只有硬链接增加。

5. 删除文件就是直接清空数据块。
   - 错。通常先 unlink 目录项，满足条件后才释放 inode 和数据块。

6. 目录只是一个普通文本文件。
   - 错。目录可理解为特殊文件，但内容格式由文件系统解释，不是普通文本。

7. VFS 的目的只是提高性能。
   - 错。主要是提供统一抽象和分派机制，性能不是唯一目的。

8. 连续分配随机访问性能一定差。
   - 错。连续分配随机访问很好，因为第 i 块可直接由 start+i 算出。

9. 链接分配没有外部碎片。
   - 对。因为任意空闲块都可加入链。

10. bitmap 不占空间。
   - 错。每个块至少需要一个 bit，只是相对紧凑。

11. `rm` 一个硬链接会让其他硬链接失效。
   - 错。其他目录项仍指向同一 inode。

12. `.` 和 `..` 与硬链接思想相关。
   - 对。`.` 指向目录自身，`..` 指向父目录。

13. page cache 只对读有用。
   - 错。写也可先进入 page cache，成为 dirty page，之后写回。

14. 日志文件系统完全不需要写真实文件系统结构。
   - 错。日志用于恢复，最终仍要把更新应用到真实结构。

15. ACL 比传统 Unix 权限更细粒度，但也更复杂。
   - 对。

---

## 25.22 简答题答题模板

### 模板 1：解释一个机制为什么存在

```text
这个机制要解决的问题是 ______。
如果没有它，会出现 ______。
它的基本做法是 ______。
它带来的好处是 ______。
代价或局限是 ______。
```

例：VFS

```text
VFS 要解决多种文件系统接口不统一的问题。如果没有 VFS，应用和内核上层逻辑会被具体文件系统绑定。VFS 定义统一对象和操作接口，由具体文件系统实现函数表。好处是同一 syscall 可操作 ext4、NFS、procfs 等不同文件系统。代价是多一层间接调用和抽象复杂度。
```

### 模板 2：比较两个概念

```text
A 的本质是 ______。
B 的本质是 ______。
共同点是 ______。
关键差异是 ______。
因此 A 适合 ______，B 适合 ______。
```

例：硬链接 vs 软链接

```text
硬链接本质是另一个目录项直接指向同一 inode；软链接本质是一个独立文件，其内容是目标路径。二者都能让用户通过另一个名字访问文件。关键差异是硬链接共享 inode 并增加 link count，而软链接有自己的 inode、不增加目标 link count。硬链接适合同一文件系统内的多名字共享，软链接适合跨文件系统或指向目录。
```

### 模板 3：描述系统调用流程

```text
用户调用 ______。
内核首先通过 ______ 找到 ______。
然后检查 ______。
接着更新或创建 ______。
如果涉及磁盘块，还要通过 ______ 映射到 ______。
为了性能，可能经过 ______。
为了可靠性，可能需要 ______。
```

例：`open("/foo/bar")`

```text
用户调用 open。内核通过路径解析从根目录找到 foo，再在 foo 目录中找到 bar 的目录项和 inode。然后检查权限，创建 file object，并在当前进程 fd table 中分配最小可用 fd。file object 指向 inode，并设置对应文件系统的 f_op。后续 read/write 通过 fd 找回 file object。
```

### 模板 4：解释性能权衡

```text
该设计提升了 ______，因为 ______。
但它牺牲了 ______，因为 ______。
所以它适合 ______，不适合 ______。
```

例：连续分配

```text
连续分配提升顺序和随机访问性能，因为文件块物理连续且可用 start+i 定位。但它牺牲文件动态增长和空间利用，因为会产生外部碎片且需要连续空闲区域。所以它适合大小稳定、顺序访问多的文件，不适合频繁增长的文件。
```

---

## 25.23 期末复习优先级

如果时间很少，按这个顺序复习：

1. 路径名、目录项、inode、硬链接、软链接。
2. fd、file object、open-file table、`open/read/write/close`。
3. `write`、page cache、dirty data、`fsync`。
4. VFS 四对象和 `file->f_op` 分派。
5. 连续、链接、索引分配的优缺点。
6. bitmap/free-space 管理和 inode 最大文件大小计算。
7. 权限、ACL、目录上的 `rwx`。
8. journaling/logging 和崩溃恢复。
9. mount、remote file sharing、NFS。
10. 文件系统历史和各种文件系统名称。

最可能出综合题的是 1-6，最可能出简答/判断的是 7-10。

---

## 25.24 最后压缩成一张考试脑图

```text
File System
|
+-- Interface
|   +-- file = byte array
|   +-- open/read/write/seek/close/unlink/truncate
|   +-- fd -> file object -> inode
|
+-- Naming
|   +-- path
|   +-- directory entry: name -> inode
|   +-- hard link: another name to same inode
|   +-- soft link: file containing target path
|
+-- Protection
|   +-- owner/group/others
|   +-- rwx
|   +-- ACL
|
+-- Implementation
|   +-- on-disk: superblock, inode table, bitmap, directories, data blocks
|   +-- in-memory: mount table, dentry cache, open-file tables, page cache
|   +-- VFS: superblock, inode, dentry, file
|
+-- Allocation
|   +-- contiguous: fast but fragmentation/growth problem
|   +-- linked/FAT: flexible but random access poor
|   +-- indexed/inode: random access and scalable, with index overhead
|
+-- Performance and Reliability
    +-- cache, read-ahead, write buffering
    +-- fsync for persistence
    +-- journaling/logging for recovery
```

真正掌握这章的标志是：你能从任意一个现象倒推到这张图中的位置。例如：

- `cat main.c` 看到 fd 3：这是 interface/open-file table。
- `rm` 后进程还能读：这是 unlink/link count/open reference。
- `write` 成功后断电丢数据：这是 cache/fsync/recovery。
- ext4 和 NFS 都能用 `write`：这是 VFS/f_op。
- 大文件最大大小计算：这是 inode indexed allocation。
- 删除文件要看父目录权限：这是 directory entry/protection。
