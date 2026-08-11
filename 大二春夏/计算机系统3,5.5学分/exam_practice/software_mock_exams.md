# 计算机系统软件部分期末模拟卷包

> 范围严格限定为本学期软件部分：内存管理与虚拟内存、Mass Storage 与 I/O、文件系统，以及少量 Lab3 RV64/Sv39 虚拟内存实验相关内容。
>
> 已排除历年操作系统卷中本学期未覆盖的软件部分旧考点；本卷只保留当前复习提纲与 Lab3 相关内容。

## 0. 命题依据与趋势判断

### 0.1 历年卷中真正可参考的题型

1. 选择题风格偏“概念细节 + 小计算 + 易错判断”：
   - `ln -s`、软链接目标删除后的行为。
   - 分区、挂载、swap-space 形式。
   - 磁盘调度，例如 SSTF。
   - 页替换，例如 LRU/FIFO。
   - 地址绑定、分段、分页、页表访问次数。
   - `open()`、路径名、文件分配、inode 最大文件大小。

2. 大题风格偏“步骤型计算”：
   - 二级页表：页号、页内偏移、页目录号、页表号、页表占用空间。
   - 文件分配：连续分配、索引分配、Unix mixed inode 的最大文件大小与访问 I/O 次数。

3. 23-24 卷面虽然不完整，但可确认的高价值考点包括：
   - thrashing、working set、page fault order。
   - Belady anomaly、FIFO/LRU/OPT。
   - page-table access count。
   - segmentation address translation。
   - absolute path、linked allocation、open、buffering。
   - SSTF、PTE 字段、two-level page table、inode max file size。

### 0.2 今年更可能出现的结构

1. 选择题：覆盖所有软件知识点，题量大，细节多。
2. 唯一大题：明确是 paging 相关，最可能落在以下三类之一：
   - 传统二级页表计算：地址拆分、页表大小、TLB/EAT、缺页。
   - Lab3/Sv39：VPN[2:0]、PTE 位、`satp`、`sfence.vma`、权限映射。
   - 虚拟内存综合：page fault、replacement、working set、thrashing。

### 0.3 Lab3 需要掌握到什么程度

重点不是背代码，而是能解释代码为什么这样写：

1. Sv39 地址结构：`VPN[2] | VPN[1] | VPN[0] | offset = 9 + 9 + 9 + 12`。
2. 4 KiB 页表页、8B PTE，所以每级页表 512 项。
3. `satp`：MODE=8 表示 Sv39，ASID 本实验置 0，PPN 是根页表物理页号。
4. PTE：`V/R/W/X/U/G/A/D`；非叶子 PTE 是 `V=1` 且 `R/W/X=0`。
5. 叶子权限：
   - `.text`: R/X。
   - `.rodata`: R。
   - `.data/.bss/剩余内存`: R/W。
6. 页表项中写的是物理页号，所以分配出的页表页地址要 `VA2PA(page)` 后再写入 PTE。
7. `sfence.vma`：切换或修改页表后保证旧翻译失效；不能只依赖 QEMU 写 `satp` 自动刷新。
8. 链接脚本使用高地址 VMA、物理 LMA；符号地址是虚拟地址，镜像加载地址仍是物理地址。
9. OpenSBI 在 M-mode 使用物理地址；S-mode 高地址指针传给 SBI 时要注意转换。
10. 你提供的实现中，`setup_vm()` 只填了高地址 gigapage 映射，`relocate` 会调整 `ra/sp/stvec` 并写 `satp`；若题干按实验文档说“临时页表包含等值映射和高地址映射”，按题干答。

---

# 模拟卷 A

## A 卷选择题

每题只有一个最佳答案。

1. 下列哪种地址绑定方式最需要硬件 MMU 在程序运行时参与地址转换？
   A. compile-time binding
   B. load-time binding
   C. execution-time binding
   D. 静态链接

2. 关于分段机制，下列说法正确的是：
   A. 段内偏移超过 limit 时仍可通过分页修正
   B. 段表项通常包含 base、limit 和保护信息
   C. 分段完全消除了外部碎片
   D. 分段地址只包含页号和页内偏移

3. 32 位虚拟地址、4 KiB 页、每个 PTE 4B，单级页表完整覆盖地址空间时页表大小为：
   A. 1 MiB
   B. 2 MiB
   C. 4 MiB
   D. 8 MiB

4. TLB 查找 10 ns，内存访问 100 ns，TLB 命中率 90%。命中时先查 TLB 再访存，未命中时先查 TLB、再访问页表、再访问数据。EAT 为：
   A. 110 ns
   B. 120 ns
   C. 200 ns
   D. 210 ns

5. 在其他条件不变时，增大页大小通常会：
   A. 减小内部碎片，增大页表
   B. 增大内部碎片，减少页表项数量
   C. 同时减少内部碎片和 TLB reach
   D. 使 TLB 完全不再需要

6. 关于 TLB miss 与 page fault，下列说法正确的是：
   A. TLB miss 一定导致 page fault
   B. page fault 一定说明磁盘坏了
   C. TLB miss 只是地址翻译缓存未命中，页可能仍在内存
   D. page fault 只能由用户程序显式触发

7. major page fault 与 minor page fault 的主要区别是：
   A. major fault 必然是权限错误
   B. major fault 通常需要磁盘 I/O
   C. minor fault 不能由 COW 引起
   D. minor fault 不会更新页表

8. 下列页面置换算法中，可能出现 Belady anomaly 的是：
   A. OPT
   B. LRU
   C. FIFO
   D. stack algorithm

9. working-set 模型中，若所有进程工作集总需求 `D` 大于可用物理 frame 数 `m`，最可能出现：
   A. cache hit 率必然为 100%
   B. thrashing 风险升高
   C. 页表自动缩小
   D. 文件系统无法挂载

10. dirty bit 在页面置换中的作用主要是：
   A. 判断页是否被写过，决定换出时是否需要写回
   B. 判断页是否存在于 TLB
   C. 表示页表项是否是非叶子 PTE
   D. 表示页大小是否为 4 KiB

11. 关于 copy-on-write，下列说法正确的是：
   A. fork 后立即复制父进程全部物理页
   B. 父子进程先共享只读映射，写入时触发缺页并复制
   C. COW 只能用于文件系统，不能用于虚拟内存
   D. COW 不需要页表权限位参与

12. buddy system 的典型特点是：
   A. 每次只能分配 1 字节
   B. 按 2 的幂大小分裂与合并空闲块
   C. 专门缓存 inode 对象
   D. 不可能产生任何碎片

13. slab allocator 更适合：
   A. 为固定大小的内核对象提供缓存
   B. 为用户文件内容建立目录项
   C. 替代所有磁盘调度算法
   D. 直接管理硬盘扇区

14. Linux 中描述进程虚拟地址空间映射的核心结构是：
   A. `inode`
   B. `mm_struct`
   C. `dentry`
   D. `superblock`

15. RISC-V Sv39 虚拟地址的低 39 位划分为：
   A. 10 + 10 + 12
   B. 9 + 9 + 9 + 12
   C. 16 + 16 + 7
   D. 8 + 8 + 8 + 15

16. RV64 中 `satp.MODE=8` 表示：
   A. Bare
   B. Sv32
   C. Sv39
   D. Sv48

17. Sv39 中，一个有效的非叶子页表项通常应满足：
   A. `V=0`
   B. `V=1` 且 `R/W/X=0`
   C. `V=1` 且 `W=1,R=0`
   D. `X=1` 且没有 PPN

18. Lab3 中最终页表对内核段权限设置，正确的是：
   A. `.text` R/W/X，`.rodata` W，`.data` X
   B. `.text` R/X，`.rodata` R，其他数据区域 R/W
   C. 所有段统一 R/W/X
   D. 所有段都不可读，只可执行

19. 机械磁盘一次访问的主要时间组成通常包括：
   A. 寻道时间、旋转延迟、传输时间
   B. 编译时间、链接时间、执行时间
   C. 页表时间、TLB 时间、缺页时间
   D. inode 时间、dentry 时间、VFS 时间

20. SSTF 磁盘调度算法的主要缺点是：
   A. 总是比所有算法移动距离更大
   B. 可能使远处请求饥饿
   C. 必须走到磁盘两端
   D. 只能用于 SSD

21. 与 SCAN 相比，C-SCAN 的主要目标是：
   A. 减少所有请求到 0
   B. 提供更均匀的等待时间
   C. 禁用磁头移动
   D. 替代 DMA

22. 关于 SSD/NAND Flash，下列说法正确的是：
   A. 可以像 DRAM 一样任意原地覆盖
   B. 完全没有写放大和磨损问题
   C. 通常需要 FTL、垃圾回收和磨损均衡
   D. 寻道时间是其主要瓶颈

23. RAID 0 的特点是：
   A. 镜像，容量减半，可靠性提高
   B. 条带化，无冗余，性能可能提高但可靠性下降
   C. 分布式奇偶校验，可容忍两盘故障
   D. 只用于磁带

24. RAID 5 的核心特征是：
   A. 只有镜像，没有校验
   B. block-interleaved distributed parity
   C. 不允许条带化
   D. 不能恢复任何磁盘故障

25. DMA 的主要意义是：
   A. 让 CPU 一字节一字节搬运所有数据
   B. 让设备和内存之间可直接传输数据，完成后中断 CPU
   C. 删除中断机制
   D. 把文件名翻译成 inode

26. polling 的典型问题是：
   A. 需要 busy-wait，可能浪费 CPU
   B. 不能读取设备状态
   C. 一定比中断更低效
   D. 只能用于文件系统

27. buffering 与 caching 的区别，较准确的是：
   A. buffering 主要协调速度/粒度差异，caching 主要利用重复访问
   B. 二者完全等价
   C. caching 只能用于打印机
   D. buffering 一定要求断电持久化

28. `ioctl` 常被看作 I/O 接口中的 escape/back door，是因为它：
   A. 只用于普通文件顺序读写
   B. 允许应用向设备传递低层、设备相关控制命令
   C. 只能创建硬链接
   D. 只负责页替换

29. Unix/Linux 中，`open()` 成功返回的 fd 通常是：
   A. 当前进程未使用的最小非负整数
   B. inode number
   C. 磁盘物理块号
   D. VFS superblock 地址

30. 正确的文件访问链路是：
   A. fd -> file object -> inode
   B. inode -> fd -> dentry -> CPU
   C. fd -> superblock -> TLB
   D. file name -> frame table -> RAID

31. 同一进程对同一路径调用两次 `open()`，通常会：
   A. 得到同一个 fd，且共享 offset
   B. 得到两个 file object，offset 通常相互独立
   C. 自动创建两个 inode
   D. 必然复制文件内容

32. `write()` 返回成功通常表示：
   A. 数据一定已经写入磁盘介质
   B. 内核已接受写入请求，数据可能仍在缓存中
   C. 文件名已从目录中删除
   D. fd 一定被关闭

33. 一个进程打开文件后，另一个进程 `rm` 该文件。已打开进程通常仍能继续读，是因为：
   A. `rm` 不会调用 unlink
   B. fd/file object 仍引用 inode，释放要等链接数和打开引用都为 0
   C. inode 中保存了多个文件名
   D. 软链接会自动修复

34. 关于硬链接和软链接，下列说法正确的是：
   A. 硬链接创建新的 inode
   B. 软链接一定增加目标 inode 的 hard link count
   C. 硬链接是另一个目录项指向同一 inode
   D. 软链接删除目标后仍一定可正常访问

35. Unix/Linux 中，文件名通常保存在：
   A. inode 中
   B. 页表项中
   C. 目录项中
   D. TLB 中

36. VFS 的四类核心对象包括：
   A. page、frame、TLB、PTE
   B. superblock、inode、dentry、file
   C. page、frame、TLB、cache line
   D. disk、track、sector、cylinder

37. 连续分配文件块的主要优点是：
   A. 顺序和随机访问都简单快速
   B. 文件增长永远不需要搬迁
   C. 完全没有外部碎片
   D. 不需要记录文件起始位置

38. linked allocation 的主要缺点是：
   A. 不能顺序访问
   B. 随机访问性能差，链指针损坏影响后续块
   C. 必须预先知道文件最终大小
   D. 一定产生外部碎片

39. indexed allocation 的特点是：
   A. 用索引块记录数据块地址，随机访问较好
   B. 每个数据块都必须物理连续
   C. 不需要任何元数据
   D. 只能存放空文件

40. 1 TiB 磁盘、4 KiB 块，使用 bitmap 管理空闲块，需要 bitmap 大小约为：
   A. 4 MiB
   B. 16 MiB
   C. 32 MiB
   D. 256 MiB

## A 卷大题：二级页表与 TLB

某 32 位系统使用 4 KiB 页、二级页表。虚拟地址格式为：

```text
31          22 21          12 11          0
| page directory | page table | page offset |
```

每个页表项 4B，每个页表页大小 4 KiB。某进程只使用以下虚拟地址范围：

```text
[0x00000000, 0x00003fff]
[0x00400000, 0x00402fff]
[0xbffff000, 0xbfffffff]
```

1. 单级页表完整覆盖 32 位地址空间需要多大？
2. 二级页表中，需要分配几个二级页表页？包括页目录本身共占多少内存？
3. 对虚拟地址 `0x00402abc` 写出 page directory index、page table index、offset，并判断是否在已映射范围内。
4. 若无 TLB，一次普通数据访问最多需要几次内存访问？若 TLB 命中，需要几次内存访问？
5. TLB lookup 10 ns，内存访问 100 ns，TLB 命中率 98%，未命中时不发生缺页。求 EAT。
6. 页引用串为 `1 2 3 4 1 2 5 1 2 3 4 5`，物理内存 3 个 frame，分别计算 FIFO、LRU、OPT 的缺页次数。

## A 卷答案与简析

### 选择题答案

| 题号 | 答案 | 简析 |
|---:|:---:|---|
| 1 | C | 运行时绑定依赖 MMU 动态翻译。 |
| 2 | B | 分段表项核心是 base、limit、保护位。 |
| 3 | C | 2^32 / 2^12 = 2^20 项，每项 4B，共 4 MiB。 |
| 4 | B | 0.9*(10+100)+0.1*(10+100+100)=120 ns。 |
| 5 | B | 页更大：页表更小、TLB reach 更大，但内部碎片更大。 |
| 6 | C | TLB miss 与 page fault 是不同层次事件。 |
| 7 | B | major fault 通常要从磁盘读页。 |
| 8 | C | FIFO 可能 Belady anomaly。 |
| 9 | B | D > m 表示物理内存无法容纳工作集。 |
| 10 | A | 干净页可直接丢弃，脏页要写回。 |
| 11 | B | COW 通过只读共享页和写保护缺页延迟复制。 |
| 12 | B | buddy 按 2 的幂分裂/合并。 |
| 13 | A | slab 是对象缓存。 |
| 14 | B | `mm_struct` 描述进程虚拟地址空间。 |
| 15 | B | Sv39 是三级 9 位 VPN 加 12 位 offset。 |
| 16 | C | RV64 `satp.MODE=8` 为 Sv39。 |
| 17 | B | `R/W/X` 全 0 表示指向下一级页表。 |
| 18 | B | 这是 Lab3 要求的细粒度权限。 |
| 19 | A | 机械磁盘访问三大组成。 |
| 20 | B | SSTF 偏向近处请求。 |
| 21 | B | C-SCAN 改善等待时间均匀性。 |
| 22 | C | SSD 需要 FTL/GC/wear leveling。 |
| 23 | B | RAID 0 无冗余。 |
| 24 | B | RAID 5 是分布式奇偶校验。 |
| 25 | B | DMA 减少 CPU 搬运数据。 |
| 26 | A | 轮询的核心成本是 busy-wait。 |
| 27 | A | buffer 为协调，cache 为复用。 |
| 28 | B | `ioctl` 传设备相关控制命令。 |
| 29 | A | fd 是进程 fd 表最小空位。 |
| 30 | A | fd 指向打开文件对象，再到 inode。 |
| 31 | B | 两次 open 通常得到独立 file object。 |
| 32 | B | `write` 成功不等于落盘。 |
| 33 | B | unlink 删除名字，不立即释放打开文件。 |
| 34 | C | 硬链接是同 inode 的另一个名字。 |
| 35 | C | 文件名在目录项中。 |
| 36 | B | VFS 四对象必须熟记。 |
| 37 | A | 连续分配定位简单。 |
| 38 | B | 链式分配随机访问差。 |
| 39 | A | 索引块换取随机访问能力。 |
| 40 | C | 1 TiB / 4 KiB = 2^28 块，bitmap 为 2^28 bit = 32 MiB。 |

### 大题答案

1. 单级页表：`2^32 / 2^12 = 2^20` 项，每项 4B，所以 `2^22 B = 4 MiB`。
2. 三段地址分别落在 page directory index `0`、`1`、`767`，所以需要 3 个二级页表页。加 1 个页目录页，共 4 页，即 `16 KiB`。
3. `0x00402abc`：
   - page directory index = `1`
   - page table index = `2`
   - offset = `0xabc`
   - 它位于 `[0x00400000, 0x00402fff]`，已映射。
4. 无 TLB：页目录、二级页表、数据，共 3 次内存访问。TLB 命中：直接访问数据，共 1 次内存访问。
5. 命中时间 `10 + 100 = 110 ns`；未命中时间 `10 + 100 + 100 + 100 = 310 ns`。EAT = `0.98*110 + 0.02*310 = 114 ns`。
6. 3 个 frame：
   - FIFO：9 次。
   - LRU：10 次。
   - OPT：7 次。

---

# 模拟卷 B

## B 卷选择题

每题只有一个最佳答案。

1. fixed partition 的典型碎片问题是：
   A. 外部碎片
   B. 内部碎片
   C. inode 碎片
   D. RAID parity 碎片

2. variable partition 中，空洞大小依次为 `100, 500, 200, 300, 600`，申请 212。first-fit、best-fit、worst-fit 分别选择：
   A. 500、300、600
   B. 300、300、600
   C. 500、500、500
   D. 600、300、100

3. 某段表中 segment 2 的 base=1000、limit=400。逻辑地址 `<2,420>` 会：
   A. 转换为物理地址 1420
   B. 转换为物理地址 420
   C. 触发越界异常
   D. 自动转入 segment 3

4. 三级页表、无 TLB、无缺页时，一次数据访问最多需要几次内存访问？
   A. 1
   B. 2
   C. 3
   D. 4

5. inverted page table 的大小主要取决于：
   A. 虚拟页数量
   B. 物理 frame 数量
   C. 目录项数量
   D. 文件名长度

6. hashed page table 常用于：
   A. 大而稀疏的虚拟地址空间
   B. 只含一个页的系统
   C. 磁盘坏块替换
   D. 打印机 spooling

7. 某地址属于合法 VMA，但页表项 present/valid 表示不在内存，访问该地址会：
   A. 直接访问磁盘块，不经内核
   B. 触发 page fault，由内核补页
   C. 必然说明程序非法
   D. 立即修改文件名

8. page-fault frequency 太高时，操作系统较合理的动作是：
   A. 给进程增加 frame 或减少多道程度
   B. 收回该进程所有 frame
   C. 禁用所有页表
   D. 删除文件系统

9. global replacement 与 local replacement 的区别是：
   A. 前者可从所有进程 frame 中选牺牲页，后者限制在本进程
   B. 前者只用于文件系统，后者只用于磁盘
   C. 前者没有 page fault，后者必然 thrashing
   D. 二者完全相同

10. 下列哪种情况最可能是 minor fault？
    A. 页在磁盘 swap 中，需要读盘
    B. COW 写保护页触发，物理页已在内存中
    C. 磁盘控制器损坏
    D. 访问不存在的 VMA

11. 对按行存储的二维数组，按列遍历可能导致更多缺页，主要原因是：
    A. 破坏空间局部性
    B. 增加 inode 数量
    C. 改变 RAID 级别
    D. 关闭了 MMU

12. TLB 有 128 项，页大小 4 KiB，则 TLB reach 为：
    A. 128 KiB
    B. 256 KiB
    C. 512 KiB
    D. 1 MiB

13. swap space 常见形式包括：
    A. swap partition 或 swap file
    B. inode 或 dentry
    C. TLB 或 cache line
    D. RAID0 或 RAID5

14. Linux 中 `vmalloc` 获得的内存通常：
    A. 虚拟地址连续，物理地址不一定连续
    B. 物理地址必然连续，虚拟地址必然不连续
    C. 只能用于磁盘块
    D. 不经过页表

15. Lab3 的内核虚拟地址空间起点是：
    A. `0x0`
    B. `0x4000000000`
    C. `0xffffffe000000000`
    D. `0xffffffff00000000`

16. Sv39 中，虚拟地址的 63 到 39 位必须：
    A. 全为 0
    B. 全为 1
    C. 与第 38 位一致
    D. 与 offset 一致

17. Lab3 `create_mapping()` 中，分配新的页表页后写入上级 PTE 时要使用物理地址，是因为：
    A. PTE 的 PPN 字段表示物理页号
    B. C 语言不能处理虚拟地址
    C. 页表不能放在内存中
    D. `memset` 只能清零物理地址

18. 若 RISC-V 实现不自动设置 A/D 位，而叶子 PTE 中 A/D 为 0，可能发生：
    A. 访问或写入时触发异常
    B. 文件名丢失
    C. RAID 自动重建
    D. TLB 永不 miss

19. 磁头当前在 53，请求队列为 `98,183,37,122,14,124,65,67`。SSTF 的服务顺序和总移动距离是：
    A. `65,67,37,14,98,122,124,183`，236
    B. `98,183,37,122,14,124,65,67`，640
    C. `14,37,65,67,98,122,124,183`，183
    D. `183,124,122,98,67,65,37,14`，299

20. LOOK 与 SCAN 的关键差别是：
    A. LOOK 不再必然走到磁盘端点，只走到该方向最后一个请求
    B. LOOK 只能向一个方向移动
    C. SCAN 不服务沿途请求
    D. LOOK 只能用于 SSD

21. C-SCAN 相比 SCAN 通常更强调：
    A. 坏块恢复
    B. 等待时间均匀
    C. 文件名解析
    D. 页表压缩

22. SSD wear leveling 的目的主要是：
    A. 让擦写次数在物理块之间更均匀
    B. 增加寻道时间
    C. 禁止垃圾回收
    D. 替换 VFS

23. bad block management 的目标是：
    A. 让坏块继续承载关键数据
    B. 识别并避免使用不可可靠读写的块
    C. 删除所有 inode
    D. 关闭 DMA

24. raw disk access 常见于数据库系统，主要因为：
    A. 数据库可能希望绕过文件系统，自行管理缓存和布局
    B. raw disk 只能存放软链接
    C. raw disk 会自动提供 VFS 对象
    D. raw disk 不需要任何 I/O

25. NAS 与 SAN 的常见区别是：
    A. NAS 通常提供文件级服务，SAN 通常提供块级存储
    B. NAS 是页表，SAN 是 TLB
    C. NAS 只能用于 CPU cache
    D. SAN 只能用于软链接

26. RAID 1 的特点是：
    A. striping without redundancy
    B. mirroring
    C. distributed parity
    D. no duplicated data

27. DMA 传输完成后，通常通过什么通知 CPU？
    A. 中断
    B. 创建硬链接
    C. 改写 inode number
    D. 改变页大小

28. memory-mapped I/O 的基本思想是：
    A. 将设备寄存器映射到内存地址空间，通过 load/store 访问
    B. 将所有文件变成目录
    C. 将 TLB 写入磁盘
    D. 将 RAID parity 映射为 inode

29. blocking I/O 的典型语义是：
    A. 请求发出后进程等待直到操作完成或出错
    B. 请求发出后必然立即返回且完成
    C. 请求发出后文件被 unlink
    D. 请求发出后页表被删除

30. kernel I/O subsystem 不包括下列哪项职责？
    A. I/O scheduling
    B. buffering/caching
    C. device driver interface
    D. page directory index 的二进制编码规则

31. 路径 `/usr/bin/ls` 是：
    A. 相对路径
    B. 绝对路径
    C. inode number
    D. 页内偏移

32. 将一个文件系统挂载到 `/mnt` 后，原 `/mnt` 目录下的旧内容通常：
    A. 永久删除
    B. 在挂载期间被覆盖隐藏，卸载后可重新看到
    C. 自动变成软链接
    D. 被写入 TLB

33. `ln a b` 成功后，`a` 与 `b` 通常：
    A. 是两个目录项，指向同一个 inode
    B. 一定跨文件系统
    C. 一定是两个 inode
    D. `b` 保存的是字符串路径

34. `ln -s a b` 创建的 `b` 通常：
    A. 是硬链接
    B. 有自己的 inode，内容是目标路径
    C. 增加 `a` 的 hard link count
    D. 删除 `a` 后一定仍能正常打开 `b`

35. 块大小 1 KiB，指针 4B，inode 有 10 个 direct、1 个 single indirect、1 个 double indirect 指针，则最大文件数据块数为：
    A. `10 + 256 + 256^2`
    B. `10 + 1024 + 1024^2`
    C. `256^3`
    D. `10 * 256`

36. dentry cache 主要缓存：
    A. 文件名路径解析结果
    B. 磁盘旋转速度
    C. TLB entry
    D. DMA byte count

37. 系统级 open-file table 中的 file object 通常保存：
    A. 当前 offset、打开模式、引用计数、指向 inode 的指针
    B. 所有虚拟页号
    C. RAID parity 公式
    D. 段表 limit

38. `fsync(fd)` 的主要作用是：
    A. 尽量强制该文件相关脏数据落盘
    B. 创建软链接
    C. 修改 TLB hit ratio
    D. 扩大页大小

39. counting free-space management 记录的是：
    A. 起始空闲块和连续空闲块数量
    B. 每个 inode 的文件名
    C. 每个 TLB 项的 ASID
    D. 每个磁道的温度

40. journaling/logging 文件系统主要改善：
    A. 崩溃后一致性恢复
    B. TLB lookup 速度
    C. CPU 指令译码
    D. Sv39 VPN 位宽

## B 卷大题：Lab3/Sv39 页表与权限

已知 Lab3 中：

```c
#define PGSIZE 0x1000
#define PHY_START 0x80000000
#define VM_START  0xffffffe000000000
#define PA2VA_OFFSET (VM_START - PHY_START)
#define SATP_SV39 (8UL << 60)
#define PTE_V (1UL << 0)
#define PTE_R (1UL << 1)
#define PTE_W (1UL << 2)
#define PTE_X (1UL << 3)
#define PTE_A (1UL << 6)
#define PTE_D (1UL << 7)
#define PA2PTE(pa) ((((uint64_t)(pa)) >> 12) << 10)
```

假设虚拟地址 `VA = 0xffffffe000203abc` 位于 `.text` 段，映射到物理地址 `PA = 0x80203abc`，根页表物理地址为 `0x80207000`。

1. 写出该 VA 的 `VPN[2]`、`VPN[1]`、`VPN[0]`、offset。
2. `.text` 段叶子 PTE 应包含哪些权限位？
3. 该页的物理页基址是 `0x80203000`。写出叶子 PTE 的值。
4. 写出写入 `satp` 的值。
5. 为什么上级非叶子 PTE 不能设置 `R/W/X`？
6. 为什么 `setup_vm_final()` 写 `satp` 后还要执行 `sfence.vma`？
7. 为什么最终页表通常不需要映射 OpenSBI 所在物理区域？
8. 若尝试向 `.rodata` 页写入，应发生什么？

## B 卷答案与简析

### 选择题答案

| 题号 | 答案 | 简析 |
|---:|:---:|---|
| 1 | B | 固定分区容易有内部碎片。 |
| 2 | A | first-fit 找 500，best-fit 找 300，worst-fit 找 600。 |
| 3 | C | offset 420 超过 limit 400。 |
| 4 | D | 三级页表 3 次查表 + 1 次数据访问。 |
| 5 | B | 反向页表按物理 frame 建表。 |
| 6 | A | 哈希页表适合大地址空间。 |
| 7 | B | 合法但不在内存是典型 demand paging。 |
| 8 | A | PFF 高说明 frame 不足或多道程度过高。 |
| 9 | A | global/local 的牺牲页候选集合不同。 |
| 10 | B | COW 页在内存中，通常是 minor fault。 |
| 11 | A | 按列访问破坏连续布局局部性。 |
| 12 | C | 128 * 4 KiB = 512 KiB。 |
| 13 | A | swap 可用分区或文件。 |
| 14 | A | `vmalloc` 虚拟连续、物理不一定连续。 |
| 15 | C | Lab3 `VM_START` 为 `0xffffffe000000000`。 |
| 16 | C | Sv39 要求 canonical address。 |
| 17 | A | PTE 存物理页号。 |
| 18 | A | 无硬件自动 A/D 时可触发异常。 |
| 19 | A | 逐步选最近，总移动 236。 |
| 20 | A | LOOK 不空走到端点。 |
| 21 | B | C-SCAN 让等待更均匀。 |
| 22 | A | wear leveling 均衡擦写。 |
| 23 | B | 坏块管理避免使用坏块。 |
| 24 | A | 数据库常自管缓存、日志和布局。 |
| 25 | A | NAS 文件级，SAN 块级。 |
| 26 | B | RAID 1 是镜像。 |
| 27 | A | DMA 完成后中断通知。 |
| 28 | A | MMIO 用地址访问设备寄存器。 |
| 29 | A | blocking I/O 会等待。 |
| 30 | D | 地址位划分属于内存管理硬件，不是 I/O 子系统职责。 |
| 31 | B | 以 `/` 开头是绝对路径。 |
| 32 | B | mount 会暂时遮住原目录内容。 |
| 33 | A | hard link 是同 inode 多目录项。 |
| 34 | B | symlink 是独立文件，保存目标路径。 |
| 35 | A | 1 KiB / 4B = 256 个指针。 |
| 36 | A | dentry cache 加速名字解析。 |
| 37 | A | file object 存打开状态。 |
| 38 | A | `fsync` 用于持久化。 |
| 39 | A | counting 利用连续空闲区。 |
| 40 | A | 日志提升崩溃一致性。 |

### 大题答案

1. `VA = 0xffffffe000203abc`：
   - `VPN[2] = 384`
   - `VPN[1] = 1`
   - `VPN[0] = 3`
   - `offset = 0xabc`
2. `.text` 是可读、可执行，不可写；叶子 PTE 需要 `V | R | X | A | D`。
3. `PA2PTE(0x80203000) = ((0x80203000 >> 12) << 10) = 0x20080c00`。权限位 `V|R|X|A|D = 0xcb`，所以 PTE = `0x20080ccb`。
4. `satp = (8UL << 60) | (0x80207000 >> 12) = 0x8000000000080207`。
5. Sv39 中 `R/W/X` 全 0 表示非叶子 PTE；若设置权限位，硬件会把它当作叶子映射。
6. 写入最终页表后，旧 TLB 项可能仍缓存临时映射；`sfence.vma` 保证后续地址翻译使用新页表。
7. OpenSBI 运行在 M-mode，使用物理地址；S-mode 内核最终页表不必把 OpenSBI 映射进高地址。
8. `.rodata` 只有读权限，写入应触发 page fault/访问权限异常。

---

# 模拟卷 C

## C 卷选择题

每题只有一个最佳答案。

1. 文件扩展名与 magic number 的区别，较准确的是：
   A. 扩展名通常只是用户约定，magic number 是文件内容中的识别信息
   B. magic number 只能用于目录
   C. 扩展名一定由 OS 强制解释
   D. 二者都存放在 TLB 中

2. 顺序访问与直接访问的主要区别是：
   A. 是否只能按当前位置附近顺序读写
   B. 是否使用 inode
   C. 是否允许目录存在
   D. 是否需要磁盘供电

3. 目录本质上可理解为：
   A. 名字到 inode/FCB 的映射
   B. 页号到 frame 号的映射
   C. 物理块到磁道号的映射
   D. TLB 到 cache line 的映射

4. tree-structured directory 的主要优点是：
   A. 支持层次化命名，避免单级目录命名冲突
   B. 每个文件必须只有一个名字
   C. 不能使用绝对路径
   D. 不需要路径解析

5. general graph directory 相比 acyclic graph directory 更危险，主要因为：
   A. 可能出现环，导致遍历和回收复杂
   B. 不能共享文件
   C. 不能创建目录
   D. 必然损坏磁盘

6. 关于硬链接跨文件系统问题，下列说法正确的是：
   A. 硬链接通常不能跨文件系统，因为 inode number 只在文件系统内有意义
   B. 软链接也绝不能跨文件系统
   C. 硬链接本质是复制数据块
   D. 硬链接一定指向目录

7. Unix/Linux 中删除文件更准确地说是：
   A. unlink 一个目录项与 inode 的关联
   B. 清空 TLB
   C. 删除所有硬链接
   D. 清除整个文件系统

8. `open("x", O_WRONLY | O_TRUNC)` 成功后，通常会：
   A. 把文件长度截断为 0
   B. 创建软链接
   C. 只读打开文件
   D. 改变页大小

9. `read(fd, buf, n)` 成功读到若干字节后，通常会：
   A. 更新该 file object 的当前 offset
   B. 改变 inode number
   C. 删除 fd
   D. 修改磁盘调度算法

10. `dup(fd)` 得到的新 fd 通常：
    A. 指向同一个 file object，共享 offset
    B. 创建新 inode
    C. 一定复制文件内容
    D. 关闭原 fd

11. 软链接与目标文件的关系是：
    A. 软链接有自己的 inode，内容通常是目标路径
    B. 软链接和目标必须同 inode
    C. 软链接一定不能悬空
    D. 软链接一定增加目标硬链接计数

12. `read()` 返回 0 通常表示：
    A. EOF
    B. 文件一定损坏
    C. fd 一定是目录
    D. TLB miss

13. per-process fd table 中保存的是：
    A. fd 到 file object 的引用
    B. 所有 inode 内容
    C. 物理页号
    D. RAID 校验块

14. file object 与 inode 的区别是：
    A. file object 表示一次打开状态，inode 表示文件对象元数据
    B. inode 保存当前 offset，file object 保存文件名
    C. 二者完全相同
    D. 二者都只存在磁盘上

15. VFS 中 `file->f_op` 的意义是：
    A. 指向具体文件系统/文件类型的操作函数表
    B. 保存页表根地址
    C. 保存磁盘转速
    D. 表示 TLB associativity

16. 下列属于 on-disk file-system structure 的是：
    A. superblock、inode table、bitmap、directory data
    B. TLB、register file、pipeline
    C. CPU cache、branch predictor
    D. process ready queue

17. 创建一个普通新文件，通常不需要立即分配的是：
    A. inode
    B. 目录项
    C. 文件数据块
    D. inode bitmap 更新

18. 删除一个已打开文件时，真正释放 inode 和数据块的条件通常是：
    A. link count 为 0 且没有打开引用
    B. 任意一个进程调用 read
    C. fd 数字大于 2
    D. 文件名长度超过 255

19. contiguous allocation 的主要问题是：
    A. 外部碎片和文件增长困难
    B. 无法顺序访问
    C. 不支持随机访问
    D. 每个块都必须保存 next 指针

20. FAT 相比普通 linked allocation 的改进是：
    A. 把链指针集中在表中，缓存 FAT 后随机访问更方便
    B. 删除所有元数据
    C. 强制文件连续
    D. 不再需要空闲空间管理

21. indexed allocation 的一个空间代价是：
    A. 小文件也可能需要索引块，产生额外开销
    B. 必须复制所有数据块
    C. 必须禁用目录
    D. 必须使用 RAID 6

22. Unix inode 使用 direct、single indirect、double indirect、triple indirect 的原因是：
    A. 兼顾小文件低开销和大文件可扩展
    B. 只为支持软链接
    C. 为了让所有文件物理连续
    D. 为了替代页表

23. bitmap 管理空闲空间的优点是：
    A. 容易寻找连续空闲块
    B. 不需要额外空间
    C. 不能表示已用块
    D. 只适合一个块的磁盘

24. grouping free-space management 的思想是：
    A. 在空闲块中批量保存其他空闲块地址
    B. 每个文件复制两份
    C. 每个目录保存页表项
    D. 把所有 inode 放入 TLB

25. read-ahead 更适合：
    A. 顺序读
    B. 完全随机读
    C. 删除文件名
    D. 修改 PTE 权限

26. asynchronous writes 看起来可能比读快，是因为：
    A. write 可先写入缓存后返回，稍后落盘
    B. write 不需要文件系统
    C. write 不需要 fd
    D. write 会跳过内核

27. unified buffer cache 的主要思想是：
    A. 用统一 page cache 缓存文件 I/O 和 mmap 页面，减少双重缓存
    B. 把所有磁盘变成 RAID 0
    C. 禁用页表
    D. 只缓存目录名，不缓存数据

28. journaling 文件系统通常先写日志，是为了：
    A. 崩溃后能根据日志恢复到一致状态
    B. 提高 TLB reach
    C. 改变页面大小
    D. 替代所有备份

29. `fsck` 的典型检查对象包括：
    A. 目录项与 inode、bitmap 与块指针、link count
    B. CPU 频率
    C. `satp.MODE`
    D. 磁头当前位置

30. block device 通常支持：
    A. read、write、seek
    B. 只支持字符流输入
    C. 只能发出中断，不能保存数据
    D. 只用于软链接

31. interrupt vector table 的作用是：
    A. 将中断/异常编号映射到处理入口
    B. 将文件名映射到 inode
    C. 将 VPN 映射到 PPN
    D. 将 RAID 块映射到 parity

32. spooling 最典型的例子是：
    A. 打印任务排队
    B. 页表查找
    C. 段表越界
    D. COW 复制

33. device reservation 主要用于：
    A. 独占使用某些设备，避免并发冲突
    B. 创建硬链接
    C. 计算 offset
    D. 替换 buddy system

34. 对非常快且频繁就绪的设备，polling 有时可以接受，是因为：
    A. 忙等时间短，避免中断开销可能划算
    B. polling 永远优于中断
    C. polling 不需要读设备状态
    D. polling 会自动写回脏页

35. 关于 interrupt-driven I/O，下列说法正确的是：
    A. CPU 发出请求后可继续执行，设备完成后中断通知
    B. CPU 必须一直 busy-wait
    C. 不需要设备控制器
    D. 不能与 DMA 配合

36. 你给出的 Lab3 `head.S` 启动顺序中，较关键的一段是：
    A. `setup_vm -> relocate -> mm_init -> setup_vm_final`
    B. `fsync -> unlink -> mount -> open`
    C. `RAID0 -> RAID1 -> RAID5 -> RAID6`
    D. `inode -> dentry -> superblock -> fd`

37. Lab3 中 `PA2VA_OFFSET` 的含义是：
    A. 物理地址到高位 direct mapping 虚拟地址的固定差值
    B. 页内偏移位数
    C. inode table 起始块号
    D. RAID parity 大小

38. Lab3 中 `pgtbl[VPN2(now_va)] = PA2PTE(VA2PA(page)) | PTE_V` 的原因是：
    A. 新分配的页表页在内核用 VA 访问，但 PTE 中必须存 PA
    B. PTE 中必须存文件名
    C. VPN2 必须等于 offset
    D. `PTE_V` 表示 writable

39. `PA2PTE(pa)` 使用 `((pa >> 12) << 10)`，是因为：
    A. 物理页号从 bit 12 开始，而 PTE 的 PPN 字段从 bit 10 开始
    B. offset 从 bit 10 开始
    C. `satp` 只能存虚拟地址
    D. inode number 必须左移 10 位

40. Lab3 链接脚本中 `>ramv AT>ram` 表示：
    A. VMA 使用高虚拟地址，LMA 仍是物理加载地址
    B. 文件系统挂载到 RAM
    C. RAID parity 写到内存
    D. 所有地址都关闭 MMU

## C 卷大题：Demand Paging、替换与 Thrashing

某系统采用 demand paging。物理内存给某进程分配 3 个 frame，使用 LRU 替换。引用序列如下，`R` 表示读，`W` 表示写：

```text
R1, W2, R3, W2, R4, R1, W3, R2, R5, R1
```

初始内存为空；写访问会将页置 dirty；换出 dirty 页需要写回。

1. 计算缺页次数。
2. 计算 dirty page write-back 次数。
3. 写出 page fault 的一般处理步骤。
4. 若内存访问时间 100 ns，page fault service time 8 ms，要求 EAT < 200 ns，page fault rate 必须小于多少？
5. 三个进程 working set size 分别为 5、4、8，系统可用 frame 为 14。是否有 thrashing 风险？如何处理？

## C 卷答案与简析

### 选择题答案

| 题号 | 答案 | 简析 |
|---:|:---:|---|
| 1 | A | 扩展名是命名约定，magic number 在内容中。 |
| 2 | A | 顺序访问依赖当前位置。 |
| 3 | A | 目录就是名字解析结构。 |
| 4 | A | 树形目录支持层次命名。 |
| 5 | A | 一般图可能有环。 |
| 6 | A | inode number 只在文件系统内唯一。 |
| 7 | A | 删除文件名本质是 unlink。 |
| 8 | A | `O_TRUNC` 截断文件。 |
| 9 | A | read/write 会推进 file object offset。 |
| 10 | A | `dup` 共享 file object 和 offset。 |
| 11 | A | symlink 是独立文件。 |
| 12 | A | read 返回 0 表示 EOF。 |
| 13 | A | fd 表指向 file object。 |
| 14 | A | file object 是打开状态，inode 是对象元数据。 |
| 15 | A | `f_op` 实现 VFS 多态分派。 |
| 16 | A | 这些是磁盘上持久结构。 |
| 17 | C | 空文件创建不一定马上分配数据块。 |
| 18 | A | unlink 后还要等打开引用释放。 |
| 19 | A | 连续分配的经典问题。 |
| 20 | A | FAT 把链集中到表。 |
| 21 | A | 索引块有空间开销。 |
| 22 | A | mixed inode 同时优化小文件和大文件。 |
| 23 | A | bitmap 容易找连续 0/1 串。 |
| 24 | A | grouping 批量记录空闲块地址。 |
| 25 | A | read-ahead 利用顺序局部性。 |
| 26 | A | buffered write 可先返回。 |
| 27 | A | unified cache 减少重复缓存。 |
| 28 | A | journaling 为崩溃恢复。 |
| 29 | A | fsck 检查元数据一致性。 |
| 30 | A | block device 支持块级随机访问。 |
| 31 | A | vector table 是编号到入口。 |
| 32 | A | 打印队列是典型 spooling。 |
| 33 | A | reservation 控制独占设备。 |
| 34 | A | 设备很快时轮询可能比中断开销小。 |
| 35 | A | 中断驱动 I/O 避免长期 busy-wait。 |
| 36 | A | 这是该实现中的虚存开启顺序。 |
| 37 | A | 高地址 direct mapping 差值。 |
| 38 | A | C 代码拿 VA，硬件页表要 PA。 |
| 39 | A | PTE PPN 字段从 bit 10 开始。 |
| 40 | A | 链接 VMA 与加载 LMA 分离。 |

### 大题答案

1. LRU 缺页次数为 9 次。
2. dirty page write-back 次数为 2 次。被换出的 dirty 页是页 2 和页 3。
3. 一般 page fault 处理步骤：
   1. CPU 触发 page fault trap，进入内核。
   2. 内核检查 fault address 是否属于合法 VMA，以及访问权限是否匹配。
   3. 若非法，向进程发送异常/终止；若合法，继续处理。
   4. 找空闲 frame；若没有，按替换算法选择牺牲页。
   5. 若牺牲页 dirty，写回磁盘。
   6. 从文件或 swap 读入目标页，或分配 zero page/COW page。
   7. 更新页表项、权限位、present/valid bit。
   8. 必要时刷新 TLB。
   9. restart faulting instruction。
4. EAT = `(1-p)*100 + p*8,000,000 < 200`，所以 `p < 100 / 7,999,900 ≈ 1.25e-5`。
5. `D = 5 + 4 + 8 = 17 > 14`，有 thrashing 风险。处理方式包括减少多道程度、挂起/换出部分进程、给高 PFF 进程增加 frame、使用 working-set/PFF 控制。

---

# 模拟卷 D

## D 卷选择题

每题只有一个最佳答案。

1. 多级页表相对单级页表节省内存的前提是：
   A. 虚拟地址空间稀疏，只为实际使用区域分配下级页表
   B. 每个进程必须用满全部虚拟空间
   C. 页大小必须为 1 字节
   D. TLB 必须禁用

2. PTBR 的作用是：
   A. 指向当前进程页表基址
   B. 保存文件名
   C. 保存磁盘坏块表
   D. 指向 RAID parity

3. TLB 本质上缓存的是：
   A. 虚拟页到物理 frame 的地址翻译
   B. 文件名到 inode 的映射
   C. 磁盘请求队列
   D. dirty inode 列表

4. 页表保护位不能实现的是：
   A. 禁止写只读页
   B. 禁止执行不可执行页
   C. 区分用户页和内核页
   D. 自动修复所有程序 bug

5. 共享代码页通常要求代码：
   A. 只读、可重入
   B. 每次执行都自修改
   C. 必须 writable
   D. 必须与数据段共用同一页

6. I/O interlock 的目的之一是：
   A. 防止正在进行 I/O 的页面被错误换出或复用
   B. 加快文件名比较
   C. 删除 TLB
   D. 合并硬链接

7. enhanced second-chance algorithm 中，一般最优先换出的是：
   A. `(reference=0, modify=0)`
   B. `(reference=0, modify=1)`
   C. `(reference=1, modify=0)`
   D. `(reference=1, modify=1)`

8. LFU 页面置换主要依据：
   A. 页面被访问次数
   B. 页面未来最晚使用时间
   C. 页面进入内存时间
   D. 文件名长度

9. page buffering 的思想包括：
   A. 保持一定空闲 frame 池，降低缺页服务延迟
   B. 把所有文件改成软链接
   C. 禁用 dirty bit
   D. 删除 page cache

10. pre-paging 的风险是：
    A. 预取了不会用的页，增加无效 I/O
    B. 必然降低所有 page fault
    C. 不能和虚拟内存共存
    D. 只能用于 inode

11. `mmap()` 的含义更接近：
    A. 把文件或对象映射进进程虚拟地址空间
    B. 把磁盘格式化
    C. 创建硬链接
    D. 设置 RAID 级别

12. Linux page fault 处理中，若地址不属于任何合法 VMA，通常会：
    A. 对用户进程产生错误处理，如发送信号
    B. 自动创建任意新 VMA
    C. 静默忽略
    D. 修改文件扩展名

13. Lab3 中 `PHY_SIZE=0x8000000`，页大小 4 KiB，物理页数量为：
    A. 8192
    B. 16384
    C. 32768
    D. 65536

14. slab 中常见的 slab 状态包括：
    A. full、partial、empty
    B. clean、dirty、invalid
    C. root、middle、leaf
    D. seek、rotate、transfer

15. Lab3 中一个 Sv39 页表页有多少项？
    A. 256
    B. 512
    C. 1024
    D. 4096

16. Sv39 只使用根页表的 gigapage 映射时，一个根 PTE 覆盖：
    A. 4 KiB
    B. 2 MiB
    C. 1 GiB
    D. 512 GiB

17. 你给出的 `setup_vm()` 实现只写入 `early_pgtbl[VPN2(VM_START)]`。对此最准确的理解是：
    A. 该代码只建立高地址 gigapage 映射，随后 `relocate` 调整返回地址/栈等以转入高地址执行
    B. 该代码建立了完整三级页表
    C. 该代码建立了所有用户进程页表
    D. 该代码与分页无关

18. `sfence.vma` 的正确理解是：
    A. 与地址翻译一致性有关，常用于页表修改或切换后
    B. 用于创建文件
    C. 用于磁盘寻道
    D. 用于计算 inode 最大大小

19. Lab3 中 `clock_set_next_event()` 改为读取 `rdtime` 后设置下一次时钟，核心原因是：
    A. SBI set timer 需要传入下一次触发的绝对时间
    B. `rdtime` 返回 inode number
    C. 这样可以关闭 MMU
    D. 这样可以创建软链接

20. RISC-V PTE 中 `W=1, R=0` 的组合通常：
    A. 是保留/非法组合，writable page 必须 readable
    B. 表示普通可写页
    C. 表示非叶子 PTE
    D. 表示 `satp.MODE=8`

21. 磁盘调度算法对 SSD 的意义通常弱于 HDD，是因为 SSD：
    A. 没有机械寻道和旋转延迟
    B. 没有任何延迟
    C. 不能随机访问
    D. 必须使用 SCAN

22. 平均旋转延迟通常近似为：
    A. 转一整圈时间
    B. 半圈时间
    C. 寻道时间两倍
    D. 传输时间平方

23. 磁盘传输时间主要取决于：
    A. 数据量和传输带宽
    B. inode link count
    C. TLB associativity
    D. `satp.PPN`

24. swap partition 相比普通 swap file 的一个潜在优势是：
    A. 可绕过文件系统布局开销，管理更直接
    B. 一定比内存更快
    C. 不需要磁盘
    D. 只能用于软链接

25. RAID 不能替代备份的原因是：
    A. RAID 主要应对磁盘故障，不防误删、软件 bug、静默数据损坏等所有问题
    B. RAID 不能读写数据
    C. RAID 只存在于 TLB
    D. RAID 会删除 inode

26. non-blocking I/O 的典型语义是：
    A. 若数据未就绪，可立即返回而不是睡眠等待
    B. 调用后一定等待完成
    C. 调用后一定同步落盘
    D. 调用后一定 unlink 文件

27. asynchronous I/O 的典型特点是：
    A. 提交请求后进程继续运行，完成后再通知
    B. 必须 busy-wait
    C. 不需要设备驱动
    D. 不允许 DMA

28. character device 更接近：
    A. 字节流接口
    B. 随机块数组
    C. 页表
    D. inode bitmap

29. device driver 的作用是：
    A. 隐藏具体控制器差异，向内核上层提供统一操作
    B. 替代所有文件系统
    C. 只负责路径解析
    D. 只负责页面置换

30. 相对路径解析依赖：
    A. 当前工作目录
    B. `satp.MODE`
    C. RAID 条带大小
    D. TLB entry 数量

31. mount table 的作用之一是：
    A. 记录挂载点与对应文件系统
    B. 记录 TLB miss 次数
    C. 记录 page offset
    D. 记录磁盘转速

32. dentry 与 inode 的关系，正确的是：
    A. dentry 负责名字到 inode 的关联，inode 保存文件对象元数据
    B. inode 保存文件名字符串，dentry 保存数据块
    C. 二者完全等价
    D. 二者都只在 CPU 寄存器中

33. `fsync(fd)` 之后再断电，相比只 `write()` 后断电：
    A. 数据持久化概率和语义保证更强
    B. inode number 必然改变
    C. 文件一定被 unlink
    D. 页大小变为 8 KiB

34. 创建软链接通常：
    A. 不增加目标文件 hard link count
    B. 必然复制目标文件数据
    C. 必须与目标同 inode
    D. 只能指向普通文件，不能指向目录路径

35. inode number 的唯一性范围通常是：
    A. 同一文件系统内部
    B. 整个互联网
    C. 所有已启动进程
    D. 所有 TLB 项

36. inode table 从块 10 开始，inode 大小 256B，块大小 4 KiB。按 0 起始编号，inode 32 位于：
    A. 块 10，偏移 0
    B. 块 11，偏移 0
    C. 块 12，偏移 0
    D. 块 12，偏移 256

37. 一个 64 块的小文件系统，使用 1 bit 表示一个块是否空闲，block bitmap 至少需要：
    A. 8 B
    B. 64 B
    C. 512 B
    D. 4 KiB

38. VFS 使同一个 `write(fd,...)` 能写 ext4、NFS、procfs 等不同对象，主要依赖：
    A. 统一对象模型和函数表分派
    B. 所有文件系统必须有完全相同磁盘布局
    C. 禁用缓存
    D. 禁用 inode

39. 对文件偏移 24 MiB + 9 KiB 处的数据进行访问，文件系统最关心的是：
    A. 该文件逻辑块号如何映射到物理块
    B. 当前进程的 CPU 时间片
    C. `satp.MODE`
    D. TLB 中断向量

40. 若题目给出“只有一道大题考 paging”，最应优先熟练的是：
    A. 地址拆分、页表层级、PTE 位、TLB/EAT、page fault/replacement
    B. 文件系统 inode 最大文件大小计算
    C. RAID 容错能力辨析
    D. 磁盘 SSTF 调度

## D 卷大题：预测型 Paging 综合题

某 RV64 内核采用 Sv39，页大小 4 KiB，PTE 8B。内核 final page table 需要把区间：

```text
VA: [VM_START + 0x200000, VM_START + 0x8000000)
PA: [0x80200000, 0x88000000)
VM_START = 0xffffffe000000000
```

按 4 KiB 页建立三级页表映射，不映射 OpenSBI 的前 2 MiB。假设所有地址范围按 2 MiB 边界对齐。

1. 需要映射多少个 4 KiB 数据页？
2. 这些映射需要多少个最低级页表页？若根页表已静态存在，还需要通过 `alloc_page()` 分配多少个页表页？
3. 对 VA `VM_START + 0x204abc`，写出 `VPN[2]`、`VPN[1]`、`VPN[0]`、offset 和物理地址。
4. 若该 VA 位于 `.data` 段，叶子 PTE 应包含哪些权限位？
5. 若 TLB 命中，一次 load 需要几次内存访问？若 TLB 未命中且页表三级都要走、无缺页，需要几次内存访问？
6. 若删除 final page table 中低地址 identity mapping，访问 `0x80204abc` 会怎样？为什么？
7. 简述 `create_mapping()` 为什么按需分配下级页表页，而不是一次性为全部虚拟地址空间分配页表。

## D 卷答案与简析

### 选择题答案

| 题号 | 答案 | 简析 |
|---:|:---:|---|
| 1 | A | 多级页表按需分配下级表才省空间。 |
| 2 | A | PTBR 指向页表基址。 |
| 3 | A | TLB 缓存地址翻译。 |
| 4 | D | 保护位不能修复逻辑 bug。 |
| 5 | A | 共享代码通常只读可重入。 |
| 6 | A | I/O 中页面不能随意换出。 |
| 7 | A | 未引用且干净页最适合换出。 |
| 8 | A | LFU 按访问次数。 |
| 9 | A | page buffering 维护空闲 frame 池。 |
| 10 | A | 预调页可能浪费 I/O。 |
| 11 | A | `mmap` 建立文件到地址空间映射。 |
| 12 | A | 非法地址通常给用户进程异常。 |
| 13 | C | 128 MiB / 4 KiB = 32768 页。 |
| 14 | A | slab 常见 full/partial/empty。 |
| 15 | B | 4 KiB / 8B = 512 项。 |
| 16 | C | Sv39 根级叶子 PTE 覆盖 1 GiB。 |
| 17 | A | 这是你这份实现与实验文档模板的关键差异。 |
| 18 | A | `sfence.vma` 维护地址翻译一致性。 |
| 19 | A | timer 传下一次触发时间。 |
| 20 | A | RISC-V writable page 必须 readable。 |
| 21 | A | SSD 无机械寻道/旋转。 |
| 22 | B | 平均等半圈。 |
| 23 | A | transfer time 与数据量/带宽相关。 |
| 24 | A | swap partition 管理更直接。 |
| 25 | A | RAID 不是备份。 |
| 26 | A | non-blocking 未就绪可返回。 |
| 27 | A | async I/O 完成后通知。 |
| 28 | A | 字符设备是流式接口。 |
| 29 | A | driver 屏蔽设备细节。 |
| 30 | A | 相对路径从 cwd 开始。 |
| 31 | A | mount table 记录挂载关系。 |
| 32 | A | dentry 是名字关联，inode 是元数据。 |
| 33 | A | `fsync` 强化持久化保证。 |
| 34 | A | symlink 不增加目标 hard link count。 |
| 35 | A | inode number 通常文件系统内唯一。 |
| 36 | C | 32*256=8192B=2 块，块 10+2=12，偏移 0。 |
| 37 | A | 64 bit = 8 B。 |
| 38 | A | VFS 通过统一对象和函数表分派。 |
| 39 | A | 文件偏移要转逻辑块再转物理块。 |
| 40 | A | 这是今年大题最核心能力。 |

### 大题答案

1. 映射大小为 `0x8000000 - 0x200000 = 0x7e00000 = 126 MiB`。数据页数为 `126 MiB / 4 KiB = 32256`。
2. 一个最低级页表页有 512 项，映射 `512 * 4 KiB = 2 MiB`。`126 MiB / 2 MiB = 63` 个最低级页表页。整个区间位于同一个 `VPN[2]` 下，因此还需要 1 个中间级页表页。根页表已静态存在，所以 `alloc_page()` 需要分配 `63 + 1 = 64` 个页表页。
3. `VA = VM_START + 0x204abc = 0xffffffe000204abc`：
   - `VPN[2] = 384`
   - `VPN[1] = 1`
   - `VPN[0] = 4`
   - `offset = 0xabc`
   - `PA = 0x80204abc`
4. `.data` 段需要 `V | R | W | A | D`，不可执行。
5. TLB 命中：1 次数据内存访问。TLB 未命中且三级页表 walk：3 次页表访问 + 1 次数据访问，共 4 次内存访问。
6. 访问低地址 `0x80204abc` 会 page fault，因为 final page table 只保留高地址 direct mapping，不再保留低地址 identity mapping。
7. Sv39 虚拟地址空间很大，但内核实际只用其中一部分。按需分配下级页表页可以只为实际映射区域付出页表内存，避免为整个虚拟空间建立庞大空页表。

---

# 5. 高频陷阱表

| 陷阱 | 正确理解 |
|---|---|
| TLB miss = page fault | 错。TLB miss 只是翻译缓存未命中；page fault 是页表权限/存在性问题。 |
| `write()` 成功 = 数据落盘 | 错。可能还在 page cache/buffer 中；持久化看 `fsync()` 等。 |
| 文件名保存在 inode 中 | 错。文件名在目录项中，inode 保存元数据和块指针。 |
| `rm` 立即释放文件数据 | 错。unlink 后还要等 link count 和 open reference 都为 0。 |
| 软链接等同硬链接 | 错。软链接有自己的 inode，通常保存目标路径；硬链接是同 inode 的另一个目录项。 |
| 多级页表一定更快 | 错。主要省空间；没有 TLB 时访问次数更多。 |
| RAID 可以替代备份 | 错。RAID 主要处理磁盘故障，不处理误删、软件 bug、静默损坏等所有问题。 |
| SSD 不需要任何管理 | 错。SSD 仍有 FTL、GC、wear leveling、写放大等问题。 |
| Sv39 PTE 里可以写虚拟地址 | 错。PTE 的 PPN 是物理页号。 |
| final page table 还必须保留 identity mapping | 一般不需要；Lab3 final mapping 主要保留高地址 direct mapping。 |
| `.rodata` 可写也没关系 | 错。权限题会考：text R/X，rodata R，data/bss R/W。 |
| `sfence.vma` 可永远省略 | 错。QEMU 行为不能代替规范要求。 |

## 6. 最后预测：优先级排序

1. 最高优先级：
   - 二级页表地址拆分、页表大小、内存访问次数。
   - Sv39 `VPN[2:0]`、PTE 位、`satp`、`sfence.vma`。
   - page fault、replacement、working set、thrashing。

2. 高优先级：
   - TLB/EAT、TLB reach、major/minor fault、COW。
   - inode、fd、file object、dentry、VFS。
   - `write()`/`fsync()`、`unlink()`、硬链接/软链接。
   - inode mixed index 最大文件大小。

3. 中高优先级：
   - SSTF/SCAN/C-SCAN/LOOK。
   - RAID 0/1/5/6。
   - DMA、interrupt、polling、buffering、caching、spooling、ioctl。
   - bitmap/grouping/counting free-space management。

4. 只作辨析，不建议投入大题时间：
   - 过细的 Linux 发行版命令路径。
   - 旧卷中超出当前三份复习提纲与 Lab3 的题。

