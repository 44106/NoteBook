# 11_mass_storage.pdf 与 12_io.pdf 零基础完整讲解

这份笔记按两节课的原始结构整理：第 11 讲是大容量存储结构，第 12 讲是 I/O 系统。你可以把它们合起来理解成一句话：用户程序想读写数据时，先通过操作系统的 I/O 接口进入内核，再经过驱动、控制器、总线，最后落到磁盘、SSD、RAID、网络存储等硬件上。

## 总览：这两讲在计算机系统中的位置

CPU 负责执行指令，Memory 负责临时保存正在运行的数据，I/O System 负责和外部世界交换数据。磁盘、SSD、键盘、网卡、显示器、打印机、计时器都属于 I/O 设备或 I/O 子系统的一部分。

这两讲的关系是：

```text
应用程序 read/write/ioctl
        |
        v
操作系统 I/O 子系统
        |
        v
设备驱动 device driver
        |
        v
设备控制器 controller / DMA / interrupt
        |
        v
具体设备：HDD、SSD、RAID、NAS、SAN、键盘、网卡、tty...
```

第 11 讲重点问：数据真正放在哪里？磁盘和 SSD 怎么组织？怎样调度磁盘请求？RAID 为什么能提高可靠性或性能？

第 12 讲重点问：程序怎样和设备交互？CPU 怎样控制 I/O 设备？轮询、中断、DMA 各解决什么问题？内核 I/O 子系统做哪些事情？

---

# 第 11 讲：Mass-Storage Structure

## 1. 本讲目录

PPT 的内容包括：

- Overview of Mass Storage Structure：大容量存储概述
- Disk Structure：磁盘结构
- Disk Scheduling：磁盘调度
- Disk Management：磁盘管理
- Swap-Space Management：交换空间管理
- RAID Structure：RAID 结构

这里的 mass storage 指容量大、断电后数据仍然保留的存储设备，典型是硬盘、SSD、磁带、RAID 阵列、网络存储。

## 2. 大容量存储概述

磁盘长期以来是计算机系统二级存储的主体。所谓二级存储，就是和主存 DRAM 相对的持久存储：主存快但断电丢失，磁盘慢但容量大、断电不丢。

磁盘通过 I/O 总线连接到计算机。PPT 举的接口包括 USB、SCSI、EIDE、SATA。这里的关键不是记名字，而是理解：磁盘不是 CPU 直接控制的裸设备，中间通常隔着总线、控制器和驱动。

磁盘会旋转，转速大约每秒 60 到 250 圈。7200 RPM 的含义是每分钟 7200 转，换成每秒就是：

```text
7200 revolutions / minute / 60 = 120 revolutions / second
```

磁盘盘片 platter 的尺寸历史上从 0.85 英寸到 14 英寸都有；现在常见的是 3.5 英寸、2.5 英寸、1.8 英寸。单盘容量 PPT 中写的是 30GB 到 3TB，甚至更大。

PPT 还展示了第一台商业磁盘驱动器：1956 年 IBM RAMDAC computer 使用 IBM Model 350 disk storage system。它有 5M 个 7-bit 字符，50 个 24 英寸盘片，访问时间小于 1 秒。这个历史例子要说明：早期磁盘巨大、容量小、访问很慢；现代磁盘容量和速度已经大幅提高，但“机械移动导致延迟”这个本质仍然存在。

## 3. 磁盘结构：从盘片到 LBA

机械磁盘的基本结构包括：

- platter：盘片，真正保存磁性数据的圆盘。
- spindle：主轴，带动盘片旋转。
- track：磁道，盘片上一圈一圈的同心圆。
- sector：扇区，磁道被切成的小块，是物理读写单位。
- cylinder：柱面，多个盘片上半径相同的一组磁道。
- read-write head：读写磁头，靠近盘片表面读取或写入数据。
- arm / arm assembly：磁臂和磁臂组件，移动磁头到目标柱面。

PPT 中强调：磁盘驱动器对外通常被看作一维的 logical block array，也就是 LBA。LBA 的全称是 Logical Block Addressing。操作系统通常不想直接关心“第几个盘片、第几个柱面、第几个磁道、第几个扇区”，而是把磁盘看成：

```text
block 0, block 1, block 2, block 3, ...
```

logical block 是最小传输单位。逻辑块会顺序映射到磁盘扇区：

1. sector 0 是最外层柱面上第一条磁道的第一个扇区。
2. 先沿着这条磁道顺序编号。
3. 再编号同一柱面上的其他磁道。
4. 再从最外层柱面逐步走到最内层柱面。

这个映射本来应该很简单，但坏扇区会打破简单映射。磁盘遇到坏扇区时，控制器或文件系统可能会把坏扇区重映射到备用扇区。

## 4. 磁盘访问时间：为什么机械磁盘慢

磁盘慢的核心原因是机械运动。PPT 把定位时间 positioning time 拆成两部分：

```text
positioning time = seek time + rotational latency
```

seek time 是寻道时间：磁臂移动到目标柱面需要的时间。你可以把它想成唱片机唱针移动到某一圈。

rotational latency 是旋转延迟：磁头已经到目标磁道了，但目标扇区还没有转到磁头下面，需要等盘片继续转。

positioning time 又称 random-access time，因为随机访问某个位置时，不知道磁头当前在哪里，也不知道目标扇区当前转到哪里，所以需要等待。

PPT 给出的典型性能指标：

- transfer rate：磁盘和计算机之间的数据传输率。PPT 写理论约 6 Gb/s，有效约 1 Gb/s。
- seek time：3ms 到 12ms，桌面磁盘常见约 9ms。
- latency based on spindle speed：一次完整旋转时间是 `60 / RPM` 秒。
- average latency：平均旋转延迟是一圈时间的一半。

以 7200 RPM 为例：

```text
7200 RPM = 120 转/秒
一圈时间 = 1 / 120 秒 = 8.33ms
平均旋转延迟 = 8.33ms / 2 = 4.17ms
```

PPT 给出平均访问时间：

```text
average access time = average seek time + average latency
```

快速磁盘例子：

```text
3ms + 2ms = 5ms
```

慢速磁盘例子：

```text
9ms + 5.56ms = 14.56ms
```

平均 I/O 时间进一步加上传输时间和控制器开销：

```text
average I/O time
= average access time
  + data to transfer / transfer rate
  + controller overhead
```

PPT 例子：在 7200 RPM 磁盘上传输 4KB block，平均寻道 5ms，传输率 1Gb/s，控制器开销 0.1ms：

```text
5ms + 4.17ms + 4KB / 1Gb/s + 0.1ms
```

这个式子的重点是：对小块随机 I/O 来说，seek time 和 rotational latency 往往比真正传输 4KB 数据的时间大得多。所以机械硬盘最怕大量随机小 I/O。

## 5. 磁盘调度：为什么请求顺序会影响性能

操作系统要高效使用硬件。对磁盘来说，它希望：

- access time 小：寻道时间和旋转延迟小。
- disk bandwidth 大：单位时间传输的数据多。

disk bandwidth 的定义是：

```text
disk bandwidth = transferred bytes / total time
```

这里的 total time 是从第一个请求开始到最后一个请求完成的时间。

磁盘调度 disk scheduling 的任务是：当磁盘请求队列里有多个 pending requests 时，决定下一个服务哪一个。

多个来源都可能产生磁盘 I/O 请求：

- 操作系统自身。
- 系统进程。
- 用户进程。

如果磁盘空闲，请求可以立即执行。如果磁盘忙，操作系统就把请求放进队列。一个请求通常包含：

- I/O mode：读还是写。
- disk address：磁盘地址。
- memory address：内存地址，数据从哪里来或到哪里去。
- number of sectors：读写多少个扇区。

PPT 提醒：优化算法只有在队列存在时才有意义。如果每次只有一个请求，根本没有“调度谁先做”的问题。

过去操作系统负责队列管理和磁头调度。现在很多排序逻辑已经内置在存储设备、控制器和固件中。系统通常只提供 LBA，设备自己处理请求排序。

本节用同一个例子比较算法：

```text
request queue = 98, 183, 37, 122, 14, 124, 65, 67
cylinder range = [0, 199]
initial head position = 53
```

### 5.1 FCFS

FCFS 是 First-Come First-Served，先来先服务。请求按到达顺序执行：

```text
53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67
```

总磁头移动距离：

```text
|98-53| + |183-98| + |37-183| + |122-37|
+ |14-122| + |124-14| + |65-124| + |67-65|
= 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2
= 640 cylinders
```

优点：

- 公平，每个请求都有机会。
- 不会 indefinite postponement，也就是不会无限期推迟某个老请求。

缺点：

- 完全不优化 seek time。
- 服务质量可能很差，磁头可能来回大幅跳动。

### 5.2 SSTF

SSTF 是 Shortest Seek Time First，最短寻道时间优先。每一步都从当前磁头位置选择最近的请求。

例子中的顺序是：

```text
53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183
```

总磁头移动距离：

```text
12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 cylinders
```

SSTF 类似 CPU 调度里的 SJF，都是“短任务优先”的思想。但 PPT 强调两个点：

- SSTF may cause starvation：远处请求可能一直等不到，因为近处不断有新请求到来。
- Unlike SJF, SSTF may not be optimal：每一步选当前最近，不代表全局总移动距离最小。

优点：

- Average response time decreases：平均响应时间下降。
- Throughput increases：吞吐量上升。

缺点：

- 需要提前计算 seek time，有额外开销。
- 远距离请求可能饥饿。
- response time variance 高，因为 SSTF 偏向某些位置附近的请求。

### 5.3 SCAN

SCAN 又叫 elevator algorithm，电梯算法。磁头像电梯一样朝一个方向走，沿途服务请求；到达磁盘一端后反向，再沿途服务请求。

它不像 FCFS 那样乱跳，也不像 SSTF 那样只顾附近请求。

优点：

- High throughput：吞吐量高。
- Low variance of response time：响应时间方差较低。
- Average response time 较稳定。

缺点：

- 磁臂刚经过的位置如果马上来了新请求，需要等磁臂走到端点再回来，所以等待时间可能很长。

注意：SCAN 的总移动距离取决于初始方向，以及是否真的走到 0 或 199 端点。PPT 的重点是算法行为，不是固定某一个唯一数值。

### 5.4 C-SCAN

C-SCAN 是 Circular SCAN，循环扫描。它为了提供更 uniform wait time：

1. 磁头只在一个方向上服务请求。
2. 到达磁盘一端后，立即返回另一端。
3. 返回途中不服务任何请求。
4. 把柱面看成一个 circular list。

直观理解：普通 SCAN 像电梯上下都载客；C-SCAN 像只从低楼层往高楼层载客，到顶楼后空车回到底楼。

优点：

- 相比 SCAN，等待时间更均匀。

### 5.5 LOOK 和 C-LOOK

SCAN 和 C-SCAN 在概念上会走到磁盘端点，即使端点附近没有请求。这可能浪费时间。

LOOK 的思想是：磁头“看一眼”当前方向上最远的请求在哪里，只走到最后一个请求，不必继续走到磁盘物理端点。

C-LOOK 是 C-SCAN 的 LOOK 版本，也只走到当前方向最后一个请求，然后跳到另一端的第一个请求。

优点：

- 避免不必要地走到磁盘端点造成额外延迟。

### 5.6 如何选择调度算法

PPT 给出的选择原则：

- 性能取决于请求数量和请求类型。
- 磁盘调度应该写成独立、可替换模块。
- SSTF 常见，可以作为默认算法。
- LOOK 和 C-LOOK 在 heavy I/O load 系统中表现更好。
- 文件分配和元数据布局也会影响磁盘性能。
- 文件系统会努力提高 spatial locality，也就是让相关数据在磁盘上尽量靠近，减少寻道。

## 6. 非易失性内存设备：SSD 与 NAND Flash

如果非易失性设备表现得像磁盘驱动器，就叫 SSD。其他形式包括 USB drives、thumb drive、flash drive、DRAM disk replacements、主板上的表面贴装存储等。

SSD 和 HDD 的关键差异：

- SSD 没有机械运动。
- 没有 seek time。
- 没有 rotational latency。
- 速度通常更快。
- 可靠性可能更高。
- 每 MB 成本更贵。
- 容量可能比 HDD 小。
- 寿命可能更短，需要小心管理。
- 总线可能成为瓶颈，所以高性能 SSD 常直接连 PCIe。

因为 SSD 没有寻道和旋转延迟，FCFS 对 SSD 往往已经不错；机械磁盘那些“减少磁头移动”的算法对 SSD 没有同样意义。

NAND Flash 有几个重要特性：

- 以 page 为单位读写，可以类比磁盘 sector。
- 不能原地覆盖 overwrite in place。
- 写入前必须 erase。
- erase 的单位比 page 大，叫 block。
- PPT 假设 block size 是 64KB，page size 是 4KB，因此一个 block 有 16 pages。
- 每个单元擦写次数有限，PPT 给出约 100,000 次。
- 寿命可用 DWPD 衡量。

DWPD 是 Drive Writes Per Day。例子：

```text
1TB NAND drive, rating = 5 DWPD
```

表示保修期内预计每天写入 5TB 数据仍不失败。

### 6.1 FTL、垃圾回收、预留空间、磨损均衡

因为 flash 不能原地覆盖，所以旧 page 可能变成 invalid，新数据写到别的 page。结果是一个 block 里混有 valid data 和 invalid data。

控制器维护 FTL，Flash Translation Layer。它记录：

```text
逻辑块地址 -> 真实 flash 物理位置
```

当 invalid page 越来越多时，控制器需要 garbage collection：

1. 找到混有有效页和无效页的 block。
2. 把有效数据复制到 over-provisioning area。
3. erase 原 block。
4. 原 block 变成可再次写入的空 block。

over-provisioning 是 SSD 额外预留但不暴露给用户的空间，用来给 GC、坏块替换、磨损均衡提供工作区。

wear leveling 是磨损均衡。因为每个 cell 擦写次数有限，控制器要尽量让所有 cell 被均匀写入，避免少数位置过早坏掉。

## 7. 磁带

磁带 tape 是早期二级存储，现在主要用于备份。

特点：

- 容量大，PPT 写 200GB 到 1.5TB。
- 随机访问很慢。
- seek time 比磁盘高得多。
- 一旦数据到磁头下方，传输率可接近磁盘，PPT 写 140MB/s。
- 随机访问需要 wind/rewind。
- 数据相对永久，适合归档和备份。

磁带的本质是顺序访问强、随机访问弱。

## 8. 磁盘管理

### 8.1 物理格式化

Physical formatting 是把磁盘划分成 controller 可读写的 sector。

每个 sector 可以包含：

- header information。
- data。
- ECC，Error Correction Code。

PPT 写 sector 通常有 512 bytes 数据，但有些磁盘可选择其他大小。

### 8.2 操作系统的数据结构

OS 会在磁盘上记录自己的数据结构：

1. Partition disk：把磁盘分成若干柱面组，每个分区可看作 logical disk。
2. Logical formatting：在分区上创建文件系统。
3. Some FS reserve spare sectors：一些文件系统保留备用扇区处理坏块。
4. FS may group blocks into clusters：文件系统可能把多个 block 组成 cluster，提高性能。

PPT 特别区分：

```text
Disk I/O done in blocks
File I/O done in clusters
```

也就是说硬盘底层按块读写，文件系统可能以 cluster 作为更高层的分配单位。

如果分区包含 OS image，还要初始化 boot sector。

### 8.3 Linux 设备命名

PPT 讲的是传统命名约定：

IDE drives：

- `/dev/hda` 到 `/dev/hdd`
- `/dev/hda` 是第一块硬盘。
- `/dev/hdc` 是第三块硬盘。

SCSI drives：

- 使用 `sd` 而不是 `hd`。
- 例如 `/dev/sda` 表示第一块 SCSI disk。
- 分区从 1 开始，例如 `/dev/sda1` 或 `/dev/hda1`。
- 第二块 SCSI disk 的第一个分区是 `/dev/sdb1`。

注意：现代 Linux 上 SATA、USB、NVMe 等命名会更多样，例如 `/dev/nvme0n1p1`。但 PPT 这里讲的是经典块设备命名规则。

### 8.4 分区：主分区与逻辑分区

PPT 说一个磁盘最多有 4 个 primary partitions。这是传统 MBR 分区表的限制。

如果需要超过 4 个分区，就使用 logical partition。逻辑分区编号从 5 开始。

例子：

```text
/dev/hda1, /dev/hda2, /dev/hda3, /dev/hda4  -> primary 或 swap 等
/dev/hda5, /dev/hda6, ...                   -> logical partitions
```

### 8.5 mount、boot block、raw disk、bad blocks

Root partition 包含 OS。其他分区可以保存其他 OS、其他文件系统，或者作为 raw 分区。

根分区在 boot time 挂载。其他分区可以自动或手动挂载。

mount 时会检查文件系统一致性：

- metadata 是否正确？
- 如果不正确，尝试修复，再重新挂载。
- 如果正确，加入 mount table，允许访问。

boot block 可以指向：

- boot volume。
- boot loader blocks，其中有足够代码知道如何从文件系统加载 kernel。
- boot management program，用于多系统启动。

Raw disk access 是让应用自己管理块，尽量绕开 OS 的文件系统管理。数据库系统常见这种需求，因为它们自己有复杂的页缓存、日志、事务管理。

Boot block initializes system：

- bootstrap 存在 ROM 或 firmware 中。
- bootstrap loader program 存在 boot partition 的 boot blocks 中。

坏块处理方法包括 sector sparing：用备用扇区替代坏扇区。

## 9. Swap Space Management

当 DRAM 不够容纳所有进程或页面时，操作系统会把数据移到二级存储。

PPT 区分：

- swapping：移动整个 process。
- paging：移动 pages。

swap space management 由操作系统提供。因为二级存储比 DRAM 慢很多，所以性能优化很重要。

优化建议：

- 可以有多个 swap spaces，减少单个设备 I/O 压力。
- 最好使用 dedicated devices。
- swap 可以是独立分区，也可以是文件系统中的一个文件。文件方式更方便添加。

Linux swap 的数据结构示例：

- `0` 表示 not used。
- `3` 表示 mapped to 3 proc。

更准确地说，这类 swap map 数字可以理解为引用/占用计数：一个 swap slot 是否空闲，或者被多少个映射引用。

## 10. Disk Attachment：磁盘如何连接到系统

PPT 分三类：

- host-attached storage。
- network-attached storage。
- storage area network。

### 10.1 Host-Attached Storage

host-attached storage 是通过本机 I/O bus 直接连接。

例子包括 hard disk、RAID arrays、CD、DVD、tape。

SCSI 是一种 bus architecture，一根 cable 上最多 16 个 devices。SCSI 中：

- initiator 发起操作请求。
- target 执行任务，例如 disk。
- 每个 target 最多可有 8 个 logical units。
- Linux 使用 `/dev/sda` 表示 SCSI disk drive，`sd` stands for SCSI disk。

IDE 是 Integrated Drive Electronics。Linux 使用 `/dev/hda` 表示 IDE disk drive。

Fiber Channel 是高速串行总线：

- 可以是 switched fabric。
- 有 24-bit address space。
- 是常见 SAN interconnection。

PPT 的 PC bus structure 图包括：

- processor 连接 bridge/memory controller。
- cache 和 memory 接在处理器/内存控制器附近。
- graphics controller 连接 monitor。
- PCIe bus 连接高速外设。
- SAS controller 连接多个 disk。
- expansion bus interface 连接 expansion bus。
- USB port、keyboard 等低速外设挂在扩展总线上。

这个图要表达：外设不是直接插到 CPU 内部，而是经由不同层级的 bus 和 controller 连接。

### 10.2 Network-Attached Storage

NAS 是通过网络提供的存储，不是通过本地总线。

特点：

- client 可以远程 attach server 上的 file systems。
- 常见协议有 NFS、CIFS、iSCSI。
- 通常用 RPC 实现。
- 通常跑在 TCP 或 UDP over IP network 上。
- iSCSI 是用 IP network carrying SCSI protocol。

NAS 的抽象更像“远程文件系统”。

### 10.3 Storage Area Network

SAN 是连接服务器和存储单元的 private network。

为什么需要 SAN？

- 存储访问会消耗大量 data network 带宽，需要和普通业务网络分离。
- TCP/IP stack 对存储访问不一定足够高效。
- SAN 使用高速互连和高效协议。
- PPT 写 FC 和 infiniband 是常见 SAN interconnection。

SAN 支持：

- 多个 hosts 和 storage arrays 接入同一个 SAN。
- 一组服务器 cluster 共享同一份存储。
- 存储可以动态分配给主机。

## 11. RAID

PPT 对 RAID 的动机很直接：

```text
Disks are unreliable, slow, but cheap.
Simple idea: use redundancy.
```

RAID 全称是 Redundant Array of Independent Disks。

RAID 通过多块磁盘组合来：

- 提高可靠性：一块坏了还有冗余数据。
- 提高速度：数据拆到多个磁盘并行读写，aggregate disk bandwidth。

RAID 可以由不同层实现：

- OS 用多个 bus-attached disks 实现。
- 硬件 RAID controller 实现。
- 独立 RAID array 盒子实现。

### 11.1 RAID 的三种基本技术

Data Mirroring：

- 同一份数据保存在多个磁盘。
- 每次写入都写到每个 mirror。
- 写入更慢，空间成本更高，但可靠性好。

Data Striping：

- 把数据拆到多个磁盘。
- 支持并行读取。
- 例如一个 byte 的 bits 分散到 8 个 disks。

Error Correcting Code / Parity Bits：

- 保存额外信息。
- 当某块盘失败时，可用这些信息重建丢失的数据。

RAID levels 本质上是这些技术的组合。PPT 说 levels 有点像 marketing tool，但常见级别还是要知道：0、1、1+0、5、5+0、6、6+0。RAID 2 书上讲，但现实中不用。

### 11.2 RAID 0

RAID 0：

- 把数据均匀 split 到两块或更多 disks。
- 没有 parity bits。
- No redundancy。
- 使用固定 strip size。

RAID 0 的效果：

- 看起来像一个更大的磁盘。
- 顺序读写大文件时带宽高。
- 访问单个 strip 不一定更快。
- 性能提高，但可靠性降低。

为什么可靠性降低？因为任意一块盘坏掉，分散在上面的条带就丢了，整个阵列中的许多文件都可能损坏。

PPT 的 RAID 0 图用 5 个不同大小文件、4 块磁盘展示：不同颜色的数据条带分布在四块盘上，这体现的是 striping。

### 11.3 RAID 1

RAID 1 是 mirror：

- 两块盘保存完全相同的数据。
- Mirroring 也叫 shadowing。
- 每个 written byte 都写到 2 disks。
- 使用的磁盘数量是 RAID 0 的两倍。

可靠性：

- 只要不是镜像两块盘同时失败，数据仍在。
- 同时失败概率很低，但不是不可能。

性能：

- 写入要写两份，可能更慢。
- 读取可以选择 seek time 最快的那块盘，也就是磁臂离目标柱面更近的盘。

PPT 的 RAID 1 图展示 5 个不同大小文件放在 4 块盘上，颜色成对出现，表示镜像副本。

### 11.4 RAID 2

RAID 2：

- bit-level striping。
- 使用 Hamming code 做 error correction。
- PPT 写 hamming code 的例子：4 bit data + 3 bit parity，可以使用 7 disks。
- not used。

RAID 2 不常用的原因是现代磁盘本身已有错误校验，位级条带化和专门的 Hamming 冗余复杂且不划算。

### 11.5 RAID 3

RAID 3 是 bit-interleaved parity：

- 数据按 bit 分散到多个数据盘。
- 有一个 dedicated parity disk。
- 每次写入涉及所有磁盘，每块盘存一个 bit。
- parity bit 用 XOR 计算。

PPT 例子：

```text
data bits = 0 1 1 0
parity = 0 xor 1 xor 1 xor 0 = 0
```

如果丢失一个 bit：

```text
0 ? 1 0, parity = 0
missing = 0 xor 0 xor 1 xor 0 = 1
```

如果丢失另一个 bit：

```text
0 1 1 ?, parity = 0
missing = 0 xor 1 xor 1 xor 0 = 0
```

XOR 能恢复单块丢失信息的原因是：XOR 中同一个值出现两次会抵消。

RAID 3：

- bit-level striping 提高性能。
- 每次写都要 XOR，有开销，但可用硬件完成。
- 恢复时间长，因为要大量 XOR。

### 11.6 RAID 4、5、6

RAID 4：

- 类似 RAID 3，但用 strips/blocks 做 interleaving。
- 小读只涉及一块 disk。
- 有专用 parity disk。
- 问题是 parity disk 容易成为写瓶颈。

RAID 5：

- 类似 RAID 4。
- 但 parity 分布在所有 disks 上，而不是只放在一个 parity disk。
- 这能减少单个 parity disk 的瓶颈。

RAID 6：

- 在 RAID 5 基础上增加额外 parity block。
- block-level striping with 2 parity blocks。
- 图中用 P 和 Q 两类冗余块表示。
- 能容忍更多故障，通常可容忍两块盘失败。

PPT 图中还列出：

- RAID 0：non-redundant striping。
- RAID 1：mirrored disks。
- RAID 4：block-interleaved parity。
- RAID 5：block-interleaved distributed parity。
- RAID 6：P + Q redundancy。
- Multidimensional RAID 6。

### 11.7 RAID 与文件系统

PPT 特别强调：RAID 只能 detect/recover from disk failures。

RAID 不解决：

- 数据被静默篡改。
- 文件系统元数据损坏。
- 软件 bug 写错数据。
- 内存或控制器导致的 corruption。

所以文件系统仍需要更强的数据完整性机制。PPT 举 Solaris ZFS：

- ZFS 给所有 FS data 和 metadata 添加 checksums。
- checksum 和指向 data/metadata 的 pointer 放在一起。
- 可以 detect and correct data and metadata corruption。
- ZFS 用 storage pools，而不是传统 volumes 或 partitions。
- 一个 pool 中多个文件系统共享空间，从 pool 中 allocate/free。

ZFS checksums 图的意思是：

```text
metadata block 1 指向 metadata block 2，并保存 checksum MB2
metadata block 2 指向 data 1/data 2，并保存 checksum D1/D2
```

读数据时，不只读数据，还用上层 metadata 中保存的 checksum 验证它是否正确。

Traditional and Pooled Storage 图的对比：

传统方式：

```text
FS -> volume -> disks
FS -> volume -> disks
FS -> volume -> disks
```

ZFS pooled storage：

```text
多个 ZFS 文件系统 -> 一个 storage pool -> 多块 disks
```

池化存储让空间管理更灵活，文件系统之间可以共享池中的容量。

## 12. 第 11 讲 Takeaway

你需要掌握：

- 磁盘由 platter、track、sector、cylinder、head、arm 组成。
- 磁盘对操作系统通常抽象成 LBA。
- 机械磁盘随机访问时间主要来自 seek time 和 rotational latency。
- 磁盘调度包括 FCFS、SSTF、SCAN、C-SCAN、LOOK、C-LOOK。
- SSD 没有机械延迟，但有 page/block、erase-before-write、FTL、GC、wear leveling 等问题。
- 磁盘管理包括物理格式化、分区、逻辑格式化、mount、boot block、bad block。
- swap 是 DRAM 不够时把进程或页移到二级存储。
- 存储连接方式包括 host-attached、NAS、SAN。
- RAID 用 striping、mirroring、parity 组合提升性能和可靠性。
- RAID 不能替代文件系统级 checksum，ZFS 是更完整的数据完整性方案。

---

# 第 12 讲：I/O Systems

## 1. 本讲开头复习

PPT 先复习第 11 讲：

- Disk：platter、cylinder、sector、track。
- Time：positioning time = seek time + rotational latency。
- Disk structure。
- Disk attachment：host-attached、network-attached、storage area network。
- Disk scheduling：FCFS、SSTF、SCAN、C-SCAN、LOOK、C-LOOK。
- Disk management：physical formatting、partition disk、logical formatting。
- RAID：Redundant Array of Inexpensive/Independent Disks。
- RAID 0 split，RAID 1 mirror，RAID 4/5/6 block with parity。

## 2. 本讲目录

PPT 的 outline：

- Overview。
- I/O Hardware。
- Application I/O Interface。
- Kernel I/O Subsystem。
- Transforming I/O Requests to Hardware Operations。
- Performance。
- Example: Linux tty device。

这节课不是只讲磁盘，而是讲所有 I/O 设备的统一管理框架。

## 3. I/O 管理为什么是操作系统核心

I/O management 是 OS design and operation 的主要组成部分。

原因：

- I/O device 是计算机和用户、其他系统交互的方式。
- I/O devices 差异极大。
- 控制不同设备的方法不同。
- 性能差异巨大。
- 设备驱动封装设备细节，对上提供统一接口。
- 新设备类型频繁出现。

如果没有操作系统和驱动提供抽象，应用程序就必须知道每个设备的寄存器、协议、时序和错误处理，这是不可接受的。

## 4. I/O Hardware：硬件层的基本概念

I/O 设备种类非常多：

- Storage：磁盘、SSD、磁带。
- Communication：网卡、串口。
- Human-interface：键盘、鼠标、显示器。

尽管种类多，PPT 提取了几个共同概念：

### 4.1 Bus

Bus 是 components 之间的 interconnection，包括 CPU 和外设之间的连接。

PC bus structure 图中：

- processor 通过 bridge/memory controller 连接 memory。
- cache 在处理器附近。
- PCIe bus 连接 graphics controller、SAS controller、expansion bus interface。
- SAS controller 下挂多个 disks。
- expansion bus 下挂 USB ports 和 keyboard。

### 4.2 Port

Port 是设备的连接点。可以理解为 CPU 或总线访问某个设备的入口。

### 4.3 Controller

Controller 是控制设备的组件。它可以集成在设备内部，也可以是单独电路板。

controller 通常包含：

- processor。
- microcode。
- private memory。
- bus controller。

设备控制器负责把高层命令变成具体设备动作。

### 4.4 Polling 与 Interrupt

I/O access 可以用：

- polling：CPU 主动反复检查设备状态。
- interrupt：设备完成后主动通知 CPU。

这两种方法后面详细讲。

## 5. I/O 指令、寄存器、端口与内存映射 I/O

有些 CPU architecture 有专门 I/O 指令。x86 的例子：

- `in`
- `out`
- `ins`
- `outs`

设备通常提供 registers 来控制 I/O：

- data-in register。
- data-out register。
- status register。
- control register 或 command register。

device driver 会把 command 和 data，或者指向 command/data 的 pointer，写入这些寄存器。

寄存器通常很小，1 到 4 bytes，或者是 FIFO buffer。

设备会被分配地址：

### 5.1 Direct I/O instructions

直接用 I/O 指令访问设备寄存器。多用于访问小寄存器。

### 5.2 Memory-mapped I/O

把设备的数据和命令寄存器映射到内存地址空间。CPU 像访问内存一样访问设备。

适合访问较大的 on-device memory，例如 graphics 显存。

### 5.3 PC I/O ports 表

PPT 给出部分 PC I/O 端口地址：

| I/O address range | device |
|---|---|
| 000-00F | DMA controller |
| 020-021 | interrupt controller |
| 040-043 | timer |
| 200-20F | game controller |
| 2F8-2FF | serial port, secondary |
| 320-32F | hard-disk controller |
| 378-37F | parallel port |
| 3D0-3DF | graphics controller |
| 3F0-3F7 | diskette-drive controller |
| 3F8-3FF | serial port, primary |

这张表说明：设备在机器里有可寻址的控制入口。

## 6. Polling：轮询

每个 I/O operation 的轮询流程：

1. 如果设备 busy，就 busy-wait status register。
2. 设备空闲后，把 command 发给 device controller 的 command register。
3. 不断读取 status register，直到它显示命令已经执行。
4. 读取 execution status，必要时 reset device status。

Polling 的优点：

- 简单。
- 如果设备非常快，轮询可能合理。

缺点：

- busy wait 浪费 CPU。
- 如果设备慢，CPU 会一直空转等待。

## 7. Interrupts：中断

中断的目的是避免 busy-wait。

流程：

1. device driver 把命令发送给 controller。
2. driver 返回。
3. OS 可以调度其他活动。
4. 设备完成命令后 interrupt processor。
5. OS 处理中断并取回结果。

中断的成本：

- I/O 开始和结束时需要 context switch 或状态切换。
- 如果 interrupt frequency 极高，频繁切换会浪费 CPU。
- 解决方法可能是改用 polling。
- PPT 举例：Linux 的 NAPI 在高网络负载下启用 polling。

### 7.1 Interrupt-Driven I/O Cycle

PPT 图中的 7 步：

1. CPU 侧 device driver initiates I/O。
2. I/O controller initiates I/O。
3. 当 input ready、output complete 或 error 时，controller 生成 interrupt signal。
4. CPU 接收 interrupt，把控制转给 interrupt handler。
5. interrupt handler 处理数据，然后 return from interrupt。
6. CPU resumes processing of interrupted task。
7. CPU 继续执行，并在指令之间检查中断。

这体现一个重要思想：中断让 CPU 不必一直等设备，但完成时 CPU 仍要暂停当前任务来处理事件。

### 7.2 Interrupt vector table

PPT 展示 Intel Pentium interrupt vector table：

- 0：divide error。
- 1：debug exception。
- 2：null interrupt。
- 3：breakpoint。
- 4：INTO-detected overflow。
- 5：bound range exception。
- 6：invalid opcode。
- 7：device not available。
- 8：double fault。
- 9：coprocessor segment overrun，reserved。
- 10：invalid task state segment。
- 11：segment not present。
- 12：stack fault。
- 13：general protection。
- 14：page fault。
- 15：Intel reserved。
- 16：floating-point error。
- 17：alignment check。
- 18：machine check。
- 19-31：Intel reserved。
- 32-255：maskable interrupts。

中断向量表本质是：

```text
中断/异常编号 -> 对应处理函数入口
```

### 7.3 ARM64 与 RISC-V64 的向量表

ARM64：

- Define vector table。
- Set the value to VBAR。
- VBAR 是 Vector Base Address Register。

RISC-V64：

- Define vector table。
- Set handle_exception to stvec。
- stvec 是 Supervisor Trap Vector Base Address Register。
- handle_exception jumps to entries of exception table。

这说明不同架构寄存器名字不同，但思想相同：发生 trap/interrupt/exception 时，CPU 要知道跳到哪里执行处理代码。

### 7.4 Interrupt 也用于 exceptions

PPT 强调 interrupt 也用于异常：

- protection error for access violation。
- page fault for memory access error。
- software interrupt for system calls。

也就是说，硬件设备通知 CPU 是 interrupt；程序出错、缺页、系统调用进入内核，也都可以走类似 trap/exception 机制。

### 7.5 多 CPU 与 IRQ affinity

Multi-CPU systems 可以并发处理中断。

有时某个 CPU 可以 dedicated to handle interrupts。中断也可以有 CPU affinity。

SMP IRQ affinity 从 Linux 2.4 kernel 开始支持：可以把某些 IRQ 分配给特定 processor 或 processor group。

作用：

- 控制系统如何响应硬件事件。
- 限制或重新分配服务器工作负载。
- 多网卡多处理器机器中，可以把不同 NIC 绑定到不同 CPU，提高网络吞吐。
- 数据库服务器或大量磁盘服务器，同时网络负载重时，可以一个 CPU 处理 disk controller，另一个 CPU 处理 NIC，提高响应。

## 8. DMA：Direct Memory Access

DMA 让数据直接在 I/O device 和 memory 之间传输。

没有 DMA 时，CPU 可能要用 programmed I/O 一字节一字节搬数据。这样 CPU 被大量数据搬运占用。

DMA 的特点：

- OS 只需发命令。
- 数据传输 bypass CPU。
- 数据以 large blocks 传输。
- 需要 DMA controller，可能在设备里，也可能在系统中。

OS 给 DMA controller 的 command 包含：

- operation。
- memory address for data。
- count of bytes。

通常是 command 的 pointer 被写到 command register。

完成后，设备用 interrupt 通知 CPU。

### 8.1 DMA transfer 五步

PPT 图中例子：从 drive 2 传输数据到内存地址 `x` 的 buffer。

1. device driver 被告知：把 drive2 data transfer 到 address `x` 的 buffer。
2. device driver 告诉 drive controller：把 `c` bytes 传到 address `x`。
3. drive controller initiates DMA transfer。
4. DMA controller 把 bytes 传到 buffer `x`，每传一段就增加 memory address，减少 `c`，直到 `c = 0`。
5. 当 `c = 0` 时，DMA interrupt CPU，表示 transfer completion。

核心理解：CPU 不搬每个字节，只负责设置任务和处理完成通知。

## 9. Application I/O Interface

操作系统的 I/O system calls 把不同设备封装成 generic classes。

Linux 中，设备可以像文件一样访问。低层特殊控制可以用 `ioctl`。

device-driver layer 隐藏不同 I/O controllers 的差异，对 kernel 提供统一接口。

每个 OS 有自己的 I/O subsystem 和 device driver framework。新设备如果使用已有协议，往往不需要额外工作。

PPT 的 `/dev` 截图展示 Linux 设备文件，例如：

- `autofs`
- `block`
- `bsg`
- `btrfs-control`
- `bus`
- `cdrom -> sr0`
- `char`
- `console`
- `core -> /proc/kcore`
- `cpu_dma_latency`
- `cuse`
- `disk`
- `dma_heap`
- `dri`
- `ecryptfs`

重点是：Linux 把很多设备暴露在 `/dev` 下，应用可以通过类似文件的接口操作设备。

## 10. I/O Structure：软件与硬件分层

PPT 图从上到下：

```text
software:
  kernel
  kernel I/O subsystem
  device drivers: SCSI, keyboard, mouse, PCI bus, floppy, ATAPI...

hardware:
  device controllers: SCSI controller, keyboard controller, mouse controller...
  devices: SCSI devices, keyboard, mouse, PCI bus, floppy-disk drives, ATAPI devices...
```

这张图最重要：应用和内核不直接操纵裸设备，而是通过分层：

```text
kernel I/O subsystem -> device driver -> controller -> device
```

## 11. I/O 设备特征分类

PPT 列出 I/O devices 变化的维度：

- character-stream or block。
- sequential or random-access。
- synchronous or asynchronous。
- sharable or dedicated。
- speed of operation。
- read-write, read only, or write only。

设备特征表：

| aspect | variation | example |
|---|---|---|
| data-transfer mode | character, block | terminal, disk |
| access method | sequential, random | modem, CD-ROM |
| transfer schedule | synchronous, asynchronous | tape, keyboard |
| sharing | dedicated, sharable | tape, keyboard |
| device speed | latency, seek time, transfer rate, delay between operations | varies |
| I/O direction | read only, write only, read-write | CD-ROM, graphics controller, disk |

操作系统通常把设备大致分成：

- block I/O：read、write、seek。
- character I/O：stream。
- memory-mapped file access。
- network sockets。

OS 通常还有 escape/back door，把任意 I/O commands 从 app 传给 device，例如 Linux 的 `ioctl`。

### 11.1 Block devices

Block devices 按块访问数据，例如 disk drives。

命令包括：

- read。
- write。
- seek。

访问方式可以是：

- raw I/O。
- direct I/O。
- file-system access。
- memory-mapped file access。
- DMA。

### 11.2 Character devices

Character devices 包括：

- keyboards。
- mice。
- serial ports。

它们类型非常多样，通常按字符流或事件流处理。

### 11.3 Network devices

Network devices 与 block/character 都很不同，因此有自己的接口。

常用 network access interface 是 socket interface。

socket interface：

- 把 network protocol 和具体 network operation 分离。
- 一些非网络操作也实现为 sockets，例如 Unix socket。

### 11.4 Clocks and Timers

Clocks and timers 可以看成 character devices。

它们非常重要，因为提供：

- current time。
- elapsed time。
- timer。

普通 resolution 约 1/60 second，有些 OS 提供 higher-resolution timers。

## 12. Synchronous / Asynchronous I/O

PPT 把 synchronous I/O 分成 blocking 和 non-blocking。

### 12.1 Blocking I/O

blocking I/O：

- 进程 suspended until I/O completed。
- 易用、易理解。
- 可能效率低。
- 对某些需求不够。

例子：程序调用 `read()`，如果数据没来，进程睡眠，直到数据准备好。

### 12.2 Non-blocking I/O

non-blocking I/O：

- I/O call 立即返回尽可能多的可用数据。
- 进程不阻塞。
- 如果暂时没有数据，就返回“现在没有”。
- 可以用 `select` 判断数据是否 ready，再用 `read` 或 `write` 传输。

### 12.3 Asynchronous I/O

asynchronous I/O：

- 进程在 I/O 执行期间继续运行。
- I/O subsystem 完成后通过 signal 或 callback 通知进程。
- 使用困难，但很高效。

Two I/O Methods 图中，左边像 blocking：requesting process 进入等待，内核驱动和硬件完成后再返回。右边像 asynchronous：请求进程提交后继续运行，硬件完成时再通过中断处理和通知返回结果。

## 13. Kernel I/O Subsystem

内核 I/O 子系统提供多种服务。

### 13.1 I/O scheduling

I/O scheduling：

- 通过 per-device queue 排队 I/O requests。
- 调度 I/O，保证 fairness 和 quality of service。

磁盘调度就是 I/O scheduling 的具体例子。

### 13.2 Buffering

Buffering 是在设备之间传输数据时先把数据存在内存里。

用途：

1. 处理 device speed mismatch。
   - 例如从 network 接收数据再写到 SSD。
   - 可以用 double buffering。
2. 处理 transfer size mismatch。
   - 例如 network buffer reassembly of message。
3. 保持 copy semantics。
   - 例如 `write()` 返回后，用户缓冲区即使被修改，内核也应保证之前写入的数据语义正确。

### 13.3 Caching

Caching 是保存数据副本以便快速访问。

PPT 强调：

- caching 是性能关键。
- 有时和 buffering 结合。
- 文件操作中的内存 buffer 也可以作为 cache。

buffering 和 caching 的区别：

- buffering 主要为了解决传输过程中的速度、粒度、语义问题。
- caching 主要为了避免重复访问慢设备。

### 13.4 Spooling

Spool 是一个 buffer，用来保存设备输入。如果设备一次只能服务一个请求，就先把输出排队。

典型例子是 printing。多个程序都要打印，打印机一次只能打印一个任务，因此先放进 spool。

### 13.5 Device reservation

Device reservation 提供 exclusive access。

操作系统提供分配和释放设备的 system calls。

风险：deadlock。比如进程 A 占用设备 1 等设备 2，进程 B 占用设备 2 等设备 1，就可能死锁。

## 14. Error Handling

一些 OS 会尝试从错误中恢复：

- device unavailable。
- transient write failures。
- retry read or write。
- 更高级系统会 track error frequencies。
- 对错误频率过高的设备，停止使用。

另一些 OS 在 I/O request 失败时只返回 error number 或 error code。

system error logs 保存问题报告。

## 15. I/O Protection

OS 需要保护 I/O devices。

例子：如果 keyboard 不受保护，恶意程序可以偷 keystrokes，形成 keylogger。

安全假设：

```text
always assume user may attempt to obtain illegal I/O access
```

保护方式：

- 所有 I/O instructions 定义为 privileged。
- I/O 必须通过 system calls 完成。
- memory-mapped I/O 和 I/O ports 也必须被保护。

Use System Call to Perform I/O 图中流程：

1. 用户程序 trap to kernel。
2. 内核进行 system call dispatch，执行 `read` 等 I/O。
3. 完成后 return to calling thread。

核心：用户态不能随便直接控制硬件，必须让内核代为操作。

## 16. Kernel Data Structures

内核保存 I/O 组件状态信息：

- open file tables。
- network connections。
- character device state。
- buffers。
- memory allocation。
- dirty blocks。

这些数据结构可能非常复杂。

PPT 提到 Windows 某些 I/O 通过 message passing 实现：

- 含 I/O 信息的 message 从 user mode 传入 kernel。
- message 在 device driver 和 process 之间流动时被修改。

### 16.1 UNIX I/O Kernel Structure

PPT 图展示 UNIX 的 I/O 内核结构：

```text
user-process memory
  file descriptor
        |
        v
  per-process open-file table
        |
        v
kernel memory
  system-wide open-file table
        |
        +-> file-system record -> active-inode table
        |
        +-> networking socket record -> network-information table
```

file-system record 里有：

- inode pointer。
- pointer to read and write functions。
- pointer to select function。
- pointer to ioctl function。
- pointer to close function。

networking socket record 里有：

- pointer to network info。
- pointer to read and write functions。
- pointer to select function。
- pointer to ioctl function。
- pointer to close function。

这解释了为什么 Linux/UNIX 可以“一切皆文件”：不同对象背后挂着不同函数指针，表面上都可以通过 fd 操作。

## 17. I/O Requests to Hardware

系统资源访问必须映射到硬件。

以进程读文件为例：

1. determine device holding file：确定文件在哪个设备上。
2. translate name to device representation：把名字翻译成设备表示。
   - FAT、UNIX 中涉及 major/minor。
3. physically read data from disk into buffer。
4. make data available to requesting process。
5. return control to process。

major/minor 的思想：

- major number 表示哪类设备驱动。
- minor number 表示该驱动管理的哪个具体设备。

## 18. Life Cycle of An I/O Request

PPT 的 I/O request 生命周期图非常重要。按层次展开：

1. user land 发起 request I/O。
2. 进入 system call。
3. kernel I/O subsystem 判断：can already satisfy I/O request？
   - 如果 yes，把数据放入 return values 或 process space，然后 return from system call。
   - 如果 no，继续往下。
4. send request to device driver，必要时 block process。
5. device driver process request，向 controller 发命令，配置 controller，等待 interrupt。
6. device controller execute command，monitor device。
7. I/O complete 后 controller generate interrupt。
8. interrupt handler receive interrupt。
9. 如果是 input，把数据存在 device-driver buffer。
10. interrupt handler signal to unblock device driver。
11. device driver determine which I/O completed，并把状态变化通知 I/O subsystem。
12. kernel I/O subsystem 把数据放入 return values 或 process space。
13. return from system call。
14. 用户程序看到 I/O complete，input data available 或 output completed。

这张图把第 12 讲所有概念串起来了：system call、kernel I/O subsystem、device driver、interrupt handler、device controller、buffer、process blocking。

## 19. Performance

I/O 是系统性能的重要因素。

PPT 列出开销来源：

- CPU 执行 device driver。
- CPU 执行 kernel I/O code。
- interrupts 导致 context switches。
- data buffering and copying。
- network traffic especially stressful。

### 19.1 网络通信的高上下文切换

PPT 例子：remote login from one machine to another。

本地机器每输入一个字符，都要传输到远程机器。

发送系统大致过程：

- keyboard character typed。
- interrupt generated。
- state save。
- interrupt received。
- interrupt handler。
- device driver。
- context switch。
- user process 处理字符。
- send character system call。
- network adapter 发 packet。

接收系统：

- network adapter 收 packet。
- interrupt generated。
- state save。
- interrupt received。
- interrupt handler。
- device driver。
- context switch。
- network daemon 或 user process 收到 packet。

这个例子说明：小粒度 I/O，尤其网络和交互式输入，会产生大量中断、状态保存、内核路径和上下文切换。

### 19.2 Improve Performance

PPT 给出的优化方法：

- Reduce number of context switches。
- Reduce data copying。
- Reduce interrupts by using large transfers, smart controllers, polling。
- Use DMA。
- Use smarter hardware devices。
- Balance CPU, memory, bus, and I/O performance for highest throughput。
- Move user-mode processes / daemons to kernel threads。

这里的核心思想：I/O 性能不只由设备速度决定，还由 CPU、内存、总线、拷贝次数、中断频率、调度开销共同决定。

## 20. Linux I/O 示例：tty device

PPT 以 Linux tty 为例说明设备初始化、write、ioctl 路径。

### 20.1 Device initialization

`/dev/tty`：

- `tty_init`
- 源码链接指向 Linux `drivers/tty/tty_io.c`
- 创建 `/dev/tty` 文件。

也就是说，设备文件不是凭空存在的，内核初始化时会注册设备并创建相应接口。

### 20.2 Device write

PPT 说：

```text
Write (echo) to the file reaches vfs_write, which eventually calls tty_write
```

路径可以理解为：

```text
用户程序 write(fd, ...)
        |
        v
系统调用进入内核
        |
        v
VFS: vfs_write
        |
        v
具体文件/设备的 write 函数
        |
        v
tty_write
```

VFS 是 Virtual File System，用来把统一文件接口分发到具体文件系统或设备实现。

### 20.3 ioctl system call

PPT 说 ioctl syscall implementation：

```text
ioctl syscall -> vfs_ioctl -> indirect call -> tty_ioctl
```

并指出：

```text
Leads to many security problems
```

为什么 ioctl 容易有安全问题？因为 ioctl 是一个非常通用的“后门式”接口，能传递很多设备特定命令。如果权限检查、参数校验、指针处理不严格，就可能产生漏洞。

## 21. 第 12 讲 Takeaway

你需要掌握：

- I/O hardware 包括 bus、port、controller、device registers。
- I/O access 有 polling 和 interrupt。
- Polling 简单但可能 busy-wait 浪费 CPU。
- Interrupt 避免忙等，但频繁中断会造成上下文切换开销。
- DMA 让设备和内存直接传输，CPU 只设置命令和处理完成中断。
- I/O devices 可按 block/character、sequential/random、sync/async、sharable/dedicated 等分类。
- Linux 把设备暴露为 `/dev` 下的设备文件，特殊控制用 ioctl。
- Kernel I/O subsystem 负责 scheduling、buffering、caching、spooling、reservation、error handling、protection。
- I/O 请求从 user system call 进入内核，经 I/O subsystem、driver、controller、interrupt handler，最后返回用户程序。
- I/O 性能受 context switch、data copying、interrupt、DMA、bus、CPU、memory 共同影响。

---

# 两讲合起来的完整路径：一次磁盘 read 到底发生了什么

假设用户程序执行：

```c
read(fd, buf, 4096);
```

完整过程可以这样串：

1. 用户程序在 user land 调用 `read`。
2. CPU 通过 trap/software interrupt 进入 kernel。
3. system call dispatch 找到 read 的内核实现。
4. VFS 根据 fd 找到 per-process open-file table。
5. 再找到 system-wide open-file table。
6. 如果是普通文件，找到 inode 和文件系统记录。
7. kernel I/O subsystem 判断 page cache 是否已有数据。
8. 如果 cache 命中，直接复制/映射数据给用户，返回。
9. 如果 cache miss，确定文件数据在哪个块设备上。
10. 文件系统把文件偏移转换成逻辑块地址 LBA。
11. block I/O 层生成磁盘 I/O 请求。
12. I/O scheduler 排队并选择调度顺序。
13. device driver 接收请求，向磁盘 controller 发命令。
14. 对机械磁盘，磁头 seek 到目标 cylinder，等待 rotational latency，读 sector。
15. 对 SSD，控制器通过 FTL 找到真实 flash page，可能涉及 GC 或 wear leveling。
16. 如果使用 DMA，controller 直接把数据搬到内存 buffer。
17. 完成后设备发 interrupt。
18. interrupt handler 运行，确认 I/O 完成。
19. driver 通知 kernel I/O subsystem。
20. 内核把数据放入 page cache，并把用户请求的数据返回到 `buf`。
21. system call 返回，用户程序继续执行。

这就是第 11 和第 12 讲合起来要你掌握的主线。

---

# 初学者最容易混淆的点

## 1. sector、block、page、cluster 不是同一个层次

- sector：磁盘物理扇区。
- logical block：设备对上暴露的逻辑传输单位。
- flash page：SSD/NAND 的读写单位。
- flash block：SSD/NAND 的擦除单位。
- file-system block/cluster：文件系统管理空间的单位。
- virtual memory page：内存管理单位。

它们都叫“块状单位”，但属于不同层次。

## 2. seek time 和 rotational latency 只对机械磁盘关键

SSD 没有磁头和旋转盘片，所以没有机械 seek 和 rotational latency。SSD 的性能瓶颈更多来自控制器、flash page/block 特性、GC、写放大、总线。

## 3. RAID 不是备份

RAID 可以提高可用性，但不是备份。RAID 不能防止：

- 用户误删。
- 软件 bug 写坏数据。
- 病毒加密。
- 文件系统 corruption。
- 整机损坏。

RAID 只处理某类磁盘故障。

## 4. interrupt 不是没有成本

中断避免 CPU 忙等，但会带来：

- 保存上下文。
- 切到内核。
- 运行 handler。
- 可能唤醒进程。
- 调度开销。

所以高频小包网络中，Linux NAPI 会在高负载时转向 polling。

## 5. DMA 不是不需要 CPU

DMA 不需要 CPU 搬每个字节，但 CPU 仍要：

- 配置 DMA。
- 管理 buffer。
- 处理完成中断。
- 维护缓存一致性和权限。

## 6. Linux “设备是文件”不是说设备真的等于磁盘文件

意思是：应用可以用类似 open/read/write/ioctl 的接口操作设备。内核背后通过函数指针把这些操作分发给具体设备驱动。

---

# 自测题

1. 为什么机械硬盘随机小读写比顺序读写慢很多？

答案：随机小读写每次都可能需要新的 seek time 和 rotational latency，而真正传输几 KB 数据的时间很短。顺序读写可以减少磁头移动并连续传输。

2. FCFS 为什么公平但性能可能差？

答案：它按请求到达顺序执行，不会饿死请求；但不考虑磁头当前位置，可能让磁头在远距离柱面间来回跳。

3. SSTF 为什么可能 starvation？

答案：如果远处请求一直在队列里，而当前磁头附近不断有新请求到来，SSTF 会一直选择近请求，远请求长期得不到服务。

4. SSD 为什么不能简单原地覆盖？

答案：NAND flash 写入前必须 erase，而 erase 单位是比 page 更大的 block。更新数据通常写到新 page，旧 page 标记 invalid。

5. RAID 5 比 RAID 4 改进在哪里？

答案：RAID 4 用专用 parity disk，写入时 parity disk 容易成为瓶颈；RAID 5 把 parity 分散到所有磁盘，降低单点写瓶颈。

6. Polling 和 interrupt 的核心区别是什么？

答案：Polling 是 CPU 主动反复检查设备；interrupt 是设备完成后主动通知 CPU。

7. DMA 解决了什么问题？

答案：避免 CPU 逐字节搬运数据，让设备和内存直接大块传输，CPU 只负责设置命令和处理完成通知。

8. 为什么 I/O 指令需要 privileged？

答案：如果用户程序能直接访问设备，就可能偷键盘输入、破坏磁盘、绕过权限。必须通过系统调用让内核检查权限并执行 I/O。

9. `ioctl` 为什么容易引发安全问题？

答案：它是设备特定命令通道，参数和语义复杂。如果驱动没有严格校验命令、权限和用户指针，就容易出现漏洞。

10. 一次 `read()` 可能为什么不真的访问磁盘？

答案：如果数据已经在 page cache 中，内核可以直接从缓存满足请求，不需要下发硬件 I/O。
