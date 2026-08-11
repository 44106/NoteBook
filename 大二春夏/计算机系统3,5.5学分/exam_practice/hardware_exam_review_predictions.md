# Sys3 硬件期末复习: 历年卷筛选、趋势与预测题

本材料只按你本学期实际覆盖的三份硬件复习提纲和对应 PPT 来筛题：

- `notes/sys3_ch1_ch2_ilp_zero_base.md`: 性能分析、流水线、分支预测、Scoreboard、Tomasulo、ROB、推测、多发射、VLIW、超流水。
- `chapter3_memory_hierarchy_zero_base_notes.md`: 存储层次、Cache 四问、地址划分、写策略、AMAT/CPI、Cache 优化、安全侧信道。
- `chapter5_DLP_TLP_零基础完整讲解.md`: DLP/SIMD/向量、GPU、循环级并行、TLP/MIMD、UMA/NUMA、Cache coherence、memory consistency、DSA/TPU。

23-24 的 `docx` 主体文字层有不可恢复乱码，但图片可读；因此 23-24 只作为题型证据，不按完整原卷处理。22-23 是完整题卷，24-25 是最新回忆，二者权重更高。

## 1. 历年卷中真正可用的题

### 22-23 硬件卷

高价值选择题，建议直接做：

| 题号 | 保留程度 | 考点 | 备注 |
|---:|---|---|---|
| 1 | 高 | pipeline hazards | “exception hazard”不是典型流水线引入的三大 hazard |
| 3 | 高 | loop unrolling / LLP | 独立数组加法最适合展开 |
| 4 | 高 | 乱序执行的合法顺序 | 不能违反 RAW 真实依赖 |
| 5 | 高 | dynamic scheduling | Scoreboard/Tomasulo/ROB 概念辨析 |
| 6-8 | 高 | 3C miss、miss penalty、Cache optimization | 选择题很可能复用 |
| 9 | 高 | UMA/NUMA/coherence/consistency | 注意 coherence 和 consistency 的定义常被反着出 |
| 10, 15 | 高 | forwarding / load-use | 细节选择题高概率 |
| 11, 16, 17 | 高 | precise exception、renaming、multiple issue | 概念题高概率 |
| 18 | 中高 | memory consistency | 本学期 Chapter 5 覆盖，选择题可能考 |
| 19-23 | 高 | Cache 优化、blocking、CPI、vector、write policy | 都在本学期范围内 |
| 24 | 高 | branch prediction penalty | 预测 taken/not taken 的 penalty |
| 25 | 高 | MESI 状态 | 送分题但易漏 E/M 含义 |
| 26 | 中 | 五级流水 ID/EX 操作 | 偏基础，仍可考 |
| 27-33 | 高 | direct mapped、block size、TLB、PA/VIPT tag、superscalar/VLIW | 今年选择题非常适合考这些细节 |
| 34 | 低 | spin lock LL/SC | 不在三份硬件提纲主线，除非老师从 TLP 同步扩展 |
| 35 | 高 | write invalidate vs write update | 容易出反向说法 |

大题可用性：

- 大题二 Cache miss 分析: 可练，但今年只有一道大题且已说明考乱序，所以降为选择题/小计算准备。
- 大题三 Scoreboard 与 hardware speculation timeline: 今年最高价值。应作为乱序大题模板反复做。
- 大题四 Directory protocol: 概念和状态可用于选择题；不再优先按大题准备。

### 23-24 硬件卷

可见题型主要来自截图和残留文字：

- ISA 类型: stack / accumulator / register-memory / load-store，特别是 `C = A + B` 在 load-store ISA 下必须 `Load R1,A; Load R2,B; Add R3,R1,R2; Store C,R3`。
- Cache 优化四类: reduce miss penalty、reduce miss rate、reduce hit time、via parallelism。
- Vector/SIMD: 512-bit vector add、loop unrolling、GPU SIMD throughput。
- Cache blocking: blocked vs unblocked transpose miss ratio。
- Memory consistency: SC/TSO/PSO/weak/release 的 ordering 约束。
- U-shaped block-size performance curve: 小块 miss rate 高，大块 miss penalty/冲突/容量压力高。
- MSI/MESI coherence 状态图和状态更新。

### 24-25 硬件卷

这是最新回忆，趋势权重最高：

- 性能平均数: normalized geometric mean。
- Tomasulo + speculation: issue 需要 ROB 和 RS 都有空；operand 可来自寄存器或 ROB；值进入 reservation station。
- Correlating branch predictor: `(2,2)` 且 4K 项时约 `2^2 * 2 * 4K = 32K bits`，另有全局历史 2 bit 可忽略或单列。
- 2-bit predictor 对 `T,T,N` 重复模式的长期 miss rate: `1/3`。
- 时钟频率与 CPI 同时变化: `Performance = clock rate / CPI`。
- Vector chaining/convoy 小计算。
- Cache line size、locality、AMAT 中 5.4/6.6 类题。
- Loop-carried dependence、RAW/WAR/WAW、寄存器重命名、可向量化改写。
- MESI 状态全称与状态序列。
- Scoreboard 表格。

## 2. 今年题型趋势判断

1. 选择题覆盖会很宽，而且会考“细节定义”。
   旧卷大题里的 Cache、MESI、Directory、vector、AMAT，很可能被压缩成选择题。

2. 近两年题目明显喜欢 PPT 原话或 PPT 例题变体。
   比如 22-23 的 vector add 524、23-24 的 Cache 优化分类、24-25 的 Tomasulo issue 条件，都是课件原型。

3. 乱序执行是唯一大题的最高概率范围。
   准备重点不是背一个答案，而是会区分 `issue / read operands / execute / write result / commit`，以及 Scoreboard、Tomasulo、ROB 的约束差异。

4. Cache 仍然是选择题大户。
   高概率包括 3C miss、AMAT、write policy、tag/index/offset、TLB/VIPT、blocking、block size U-curve、优化分类。

5. DLP/TLP 不会只考大概念。
   可能会问 vector chaining 公式、SIMD vs MIMD、TLP 多 PC、UMA/NUMA、Snoopy/Directory、MESI/MOESI、memory consistency、DSA/TPU。

## 3. 最高概率预测清单

优先级 A:

- `CPU Time = IC * CPI / ClockRate` 与性能提升百分比。
- Amdahl's Law。
- normalized geometric mean。
- RAW/WAR/WAW、loop-carried dependence、register renaming。
- forwarding 和 load-use stall。
- 1-bit/2-bit predictor、BHT、BTB、correlating predictor bit 数。
- Scoreboard、Tomasulo、ROB、hardware speculation 的阶段与表格。
- Superscalar vs VLIW，为什么 multiple issue 才能 CPI < 1。
- AMAT、多级 Cache stall cycles、3C miss。
- Cache tag/index/offset、TLB、VIPT。
- write-through/write-back、write allocate/no-write allocate、dirty bit。
- vector length / vector instruction cycles / chaining / convoy。
- MESI 状态序列、coherence vs consistency。

优先级 B:

- Cache security: Meltdown/Spectre 基本机制。
- FIFO/LRU/OPT、Belady anomaly。
- GPU grid/block/thread、host/device、GPU memory hierarchy。
- UMA/NUMA/COMA、MPP/COW。
- DSA/TPU 的设计原则。
- Dynamic interconnection network、Omega、hypercube 等网络细节。

低优先级或可剔除:

- 操作系统旧卷中的 Linux 命令、文件系统、进程同步、磁盘调度等，属于软件部分，不纳入硬件准备。
- 22-23 的 LL/SC spin lock 题，如果没有老师强调同步原语，可降权。
- Directory protocol 画消息流程今年不适合作为大题准备，但状态含义仍要会选。

## 4. 乱序执行大题模板

### 模板一: Scoreboard vs Hardware-Based Speculation timeline

题型特征：

- 给一串指令。
- 给 FU latency。
- 问 Scoreboard 的 issue/read/execute/write。
- 问带 ROB 的 speculation 的 issue/execute/write/commit。

关键规则：

- Scoreboard:
  - Issue 通常按序。
  - Issue 阶段要检查结构冲突和 WAW。
  - Read operands 等 RAW 解除。
  - Write result 可能被 WAR 阻塞。
  - 不能靠重命名消除 WAR/WAW。

- Tomasulo:
  - Issue 需要对应 reservation station/load buffer 有空。
  - `Vj/Vk` 存已就绪操作数值，`Qj/Qk` 存等待哪个 RS/ROB 产生值。
  - CDB 广播结果给寄存器和所有等待的 RS。
  - 通过硬件重命名消除 WAR/WAW，但不能消除 RAW。

- Tomasulo + ROB / hardware speculation:
  - Issue 需要 RS 和 ROB 都有空。
  - operand 来源可以是 register，也可以是 ROB。
  - execute/write result 可以乱序。
  - commit 必须按程序顺序。
  - ROB 支持 precise exception 和错误推测恢复。

### 模板二: 22-23 原型表

按旧卷简化规则：单发射，RS 在 result broadcast 后释放；add/sub 1 cycle，mul 10 cycles，div 40 cycles。

```text
I1: div x2, x3, x4
I2: mul x1, x5, x6
I3: add x3, x7, x8
I4: mul x1, x1, x3
I5: sub x4, x1, x5
I6: sub x1, x4, x2
```

Scoreboard 参考表：

| instruction | issue | read operand | execution | write result | 关键限制 |
|---|---:|---:|---|---:|---|
| div x2,x3,x4 | 1 | 2 | 3-42 | 43 | 第一条 |
| mul x1,x5,x6 | 2 | 3 | 4-13 | 14 | 独立 |
| add x3,x7,x8 | 3 | 4 | 5 | 6 | 独立 |
| mul x1,x1,x3 | 14 | 15 | 16-25 | 26 | 等前面对 x1 的 WAW 清掉 |
| sub x4,x1,x5 | 15 | 27 | 28 | 29 | 等 I4 产生 x1 |
| sub x1,x4,x2 | 30 | 31 | 32 | 33 | 等 x4，且避免名字冲突 |

Hardware speculation 参考表：

| instruction | issue | execution start | write result | commit | 关键限制 |
|---|---:|---:|---:|---:|---|
| div x2,x3,x4 | 1 | 2 | 42 | 43 | 老长延迟指令 |
| mul x1,x5,x6 | 2 | 3 | 13 | 44 | 早完成但等 I1 commit |
| add x3,x7,x8 | 3 | 4 | 5 | 45 | 写回早，提交晚 |
| mul x1,x1,x3 | 14 | 15 | 25 | 46 | 等乘法 RS 释放 |
| sub x4,x1,x5 | 15 | 26 | 27 | 47 | 等 I4 的 x1 |
| sub x1,x4,x2 | 28 | 43 | 44 | 48 | 等 I1 的 x2 和 I5 的 x4 |

阅卷点：

- 只要 commit 列乱序，基本就是大错。
- 如果把 WAR/WAW 当成 RAW，说“重命名可以解决 RAW”，也是大错。
- 如果忘记 ROB 会阻塞年轻指令提交，容易把 I2/I3 的 commit 写得太早。

### 模板三: ROB 状态题

典型指令：

```asm
FLD    F6,  34(R2)
FLD    F2,  45(R3)
FMUL.D F0,  F2, F4
FSUB.D F8,  F6, F2
FDIV.D F10, F0, F6
FADD.D F6,  F8, F2
```

当 `FMUL.D` ready to commit 时，要能解释：

- ROB 保存 instruction type、destination、value。
- Register status 记录寄存器当前由哪个 ROB entry 产生。
- `F6` 可能已有旧值 commit，同时又有年轻的 `FADD.D F6` 在 ROB 中等待。
- ROB 允许多个未来版本共存，但最终按序 commit。

## 5. 高覆盖选择题预测

### A. 性能、ISA 与基础概念

1. 同一个 RISC-V 程序能在单周期 CPU、流水线 CPU、乱序 CPU 上运行，根本原因是它们有相同的什么？

A. microarchitecture  
B. ISA  
C. clock rate  
D. cache hierarchy

2. 若 X is n times faster than Y，则 n 等于：

A. `ExecutionTime_X / ExecutionTime_Y`  
B. `ClockRate_X / ClockRate_Y`  
C. `ExecutionTime_Y / ExecutionTime_X`  
D. `CPI_Y / CPI_X`

3. 在 IC 不变时，CPU 性能正比于：

A. `ClockRate / CPI`  
B. `CPI / ClockRate`  
C. `ClockRate * CPI`  
D. `IC * CPI`

4. 某处理器 clock rate 从 1.8GHz 变为 2.2GHz，CPI 从 1.2 变为 1.5，IC 不变。性能变化约为：

A. 提升 22.2%  
B. 提升 1.8%  
C. 不变  
D. 下降 2.2%

5. 比较多个机器和多个 benchmark 时，哪种平均数对 reference machine 的选择不敏感？

A. arithmetic mean  
B. weighted arithmetic mean  
C. normalized geometric mean  
D. harmonic mean

6. 某优化使原执行时间 30% 的部分加速 10 倍，整体加速比约为：

A. 3.33  
B. 1.37  
C. 10  
D. 1.03

7. 想用 100 个处理器达到 80 倍加速，原程序串行部分最多约为：

A. 0.25%  
B. 1.25%  
C. 20%  
D. 80%

8. Load-store ISA 计算 `C = A + B` 的正确序列是：

A. `Push A; Push B; Add; Pop C`  
B. `Load A; Add B; Store C`  
C. `Load R1,A; Add R1,B; Store C,R1`  
D. `Load R1,A; Load R2,B; Add R3,R1,R2; Store C,R3`

### B. 流水线、分支预测与乱序执行

9. 下列哪一种不是流水线技术典型引入的 hazard？

A. structural hazard  
B. exception hazard  
C. data hazard  
D. control hazard

10. 在经典五级流水线中，紧邻的 `ld x1,0(x2); and x6,x1,x7` 即使有 forwarding 通常仍需要 stall，原因是：

A. load 数据到 MEM 末才可用  
B. ALU 不能 forwarding  
C. store buffer 满  
D. branch target 未知

11. `RAW/WAR/WAW` 中，真正数据依赖是：

A. RAW  
B. WAR  
C. WAW  
D. RAR

12. 寄存器重命名主要消除：

A. RAW  
B. WAR 和 WAW  
C. structural hazard  
D. compulsory miss

13. 1-bit predictor 预测内层循环时，典型问题是：

A. 每次循环都错  
B. 入口和退出附近可能错两次  
C. 只能预测 indirect jump  
D. 必须配合 ROB

14. 2-bit predictor 对长期重复模式 `T,T,N` 的稳定 miss rate 约为：

A. 0  
B. 1/3  
C. 1/2  
D. 2/3

15. `(2,2)` correlating predictor，若每个 predictor buffer 有 4K 项，则预测表位数约为：

A. 8K bits  
B. 16K bits  
C. 32K bits  
D. 64K bits

16. BHT 和 BTB 的核心区别是：

A. BHT 存目标地址，BTB 存 taken/not taken  
B. BHT 存历史方向，BTB 存分支目标地址  
C. 二者都只存指令数据  
D. 二者都只用于 Cache replacement

17. 分支条件和目标到 EX 末才确定时，predict taken 且实际 taken 的 penalty，以及 predict not taken 且实际 not taken 的 penalty 通常为：

A. 2, 0  
B. 2, 2  
C. 3, 0  
D. 3, 3

18. Scoreboard 的正确说法是：

A. 通过 ROB 保证按序提交  
B. 通过硬件重命名消除 WAR/WAW  
C. 能检测 RAW/WAR/WAW，但不能像 Tomasulo 那样用重命名消除名字相关  
D. 所有指令都乱序 issue

19. Tomasulo 中 `Qj/Qk` 表示：

A. 已经就绪的操作数值  
B. 等待哪个 RS/ROB 产生操作数  
C. 功能部件 latency  
D. cache tag

20. 带 ROB 的硬件推测中，issue 一条普通运算指令通常要求：

A. 只有 ROB 有空  
B. 只有 reservation station 有空  
C. ROB 和 reservation station 都有空  
D. ROB 或 reservation station 任一有空

21. 带 ROB 的 Tomasulo 中，issue 后源操作数可以来自：

A. 只能来自寄存器  
B. 只能来自 ROB  
C. 寄存器或 ROB  
D. 只能来自 FU

22. ROB 最重要的正确性作用是：

A. 让所有指令按序 execute  
B. 支持乱序执行但按序 commit，从而支持 precise exception  
C. 消除 Cache miss  
D. 替代所有 reservation station

23. 下列哪种技术最直接可能让 CPI < 1？

A. Scoreboard  
B. Tomasulo  
C. Multiple issue  
D. Loop unrolling

24. Superscalar 与 VLIW 的主要区别是：

A. Superscalar 主要靠硬件发现并行，VLIW 主要靠编译器静态打包  
B. Superscalar 不能乱序，VLIW 必须乱序  
C. VLIW 只用于 Cache  
D. 二者完全相同

25. 硬件推测中，年轻指令早早 write result 但迟迟不能 commit，最常见原因是：

A. CDB 不存在  
B. 前面更老的长延迟指令还没 commit  
C. 没有 BHT  
D. Cache line 太大

### C. Cache 与 Memory Hierarchy

26. 单核 CPU Cache 的 3C miss 不包括：

A. compulsory miss  
B. conflict miss  
C. coherency miss  
D. capacity miss

27. 增大 block size 主要利用：

A. temporal locality，减少 capacity miss  
B. spatial locality，减少 compulsory miss  
C. coherence，减少 dirty bit  
D. TLB，减少 branch penalty

28. 较大 block size 可能导致性能曲线呈 U 型，原因是：

A. 小块 miss rate 高，大块 miss penalty 和冲突/容量压力高  
B. 小块 miss penalty 高，大块 hit time 一定为 0  
C. block size 与性能无关  
D. 大块总是更快

29. `AMAT` 的基本公式是：

A. `Hit Time + Miss Rate * Miss Penalty`  
B. `Miss Rate + Hit Rate`  
C. `ClockRate / CPI`  
D. `IC * CPI`

30. 1000 次 memory references 中 L1 misses 40 次、L2 misses 20 次，L2 hit time 10 cycles，L2 到内存 miss penalty 200 cycles，1.5 memory references/instruction。平均 memory stall cycles/instruction 为：

A. 6.6  
B. 5.4  
C. 11  
D. 15

31. 下列哪项不能降低 miss rate？

A. pipelined cache access  
B. larger block size  
C. larger cache size  
D. higher associativity

32. 下列哪项主要降低 miss penalty？

A. multilevel caches  
B. increasing associativity  
C. loop interchange  
D. larger cache size

33. write-back cache 中 dirty bit 的作用是：

A. 表示该行是否有效  
B. 表示该行是否被修改且尚未写回内存  
C. 表示该行是否是指令  
D. 表示该行是否在 TLB 中

34. 常见组合中，write-back 通常搭配：

A. write allocate  
B. no-write allocate  
C. no valid bit  
D. no dirty bit

35. TLB 是页表的 Cache。全相联 TLB 中 tag 和 data line 通常对应：

A. tag=VPN，data=page offset  
B. tag=VPN，data=PPN  
C. tag=PPN，data=VPN  
D. tag=PPN，data=page offset

36. 物理地址 36 bits、Cache capacity 16KB，直接映射且物理寻址时，tag 位数为：

A. 20  
B. 21  
C. 23  
D. 22

37. 同样物理地址 36 bits、Cache 16KB、8-way physically addressed cache，tag 位数为：

A. 25  
B. 26  
C. 27  
D. 28

38. 物理地址 36 bits、page size 8KB、Cache 16KB、2-way VIPT cache，tag 位数为：

A. 26  
B. 25  
C. 24  
D. 23

39. direct mapped cache 相比 fully associative cache 的主要优势是：

A. miss rate 一定更低  
B. hit time 小、硬件简单  
C. 不需要 tag  
D. 不会 conflict

40. LRU 不会出现 Belady anomaly 的核心原因是它满足：

A. stack property  
B. write-through property  
C. branch folding  
D. CDB property

41. `for row; for col; use(x[row][col])` 在 C 行主序数组上通常比按列访问更好，原因是：

A. 空间局部性更好  
B. 消除了 RAW  
C. 自动产生 ROB  
D. 不需要 Cache

42. Blocking/tiling 对矩阵程序的主要作用是：

A. 改变算法复杂度为 O(N)  
B. 提高局部性，减少 Cache miss  
C. 消除所有分支  
D. 替代 TLB

43. Meltdown/Spectre 类漏洞共同利用的关键微结构痕迹是：

A. Cache 时延差异  
B. 磁盘分区名  
C. 文件系统 inode  
D. 进程 PID

### D. DLP、TLP、Coherence 与 Consistency

44. Flynn 分类中，SIMD 表示：

A. Single Instruction Multiple Data  
B. Single Instruction Single Data  
C. Multiple Instruction Single Data  
D. Multiple Instruction Multiple Data

45. TLP 通常意味着多个 program counters，因此主要通过哪类架构利用？

A. SIMD  
B. MIMD  
C. MISD  
D. SISD

46. 512-bit vector add 处理 64-bit 元素，每条 vector add 4 cycles。计算 524 个元素需要多少 add cycles？

A. 264  
B. 268  
C. 524  
D. 48

47. 向量链接 vector chaining 的核心好处是：

A. 必须等整个源向量全部写回后再开始下一条  
B. 前一条产生第一个元素后，后一条可接着消费，形成流水  
C. 消除所有 loop-carried dependence  
D. 只用于标量 ALU

48. `A[i+1] = A[i] + C[i]` 的循环主要问题是：

A. loop-carried dependence  
B. no-write allocate  
C. branch target buffer  
D. MOESI owned state

49. `for i: C[i]=A[i]+B[i]` 最适合：

A. DLP/vectorization  
B. write invalidate  
C. sequential consistency only  
D. directory writeback only

50. GPU 编程模型中，CPU 通常是：

A. host  
B. device  
C. cache line  
D. ROB

51. UMA/SMP 的特征是：

A. 所有处理器访问共享内存的延迟统一  
B. 每个处理器只能访问本地内存  
C. 没有共享地址空间  
D. 只能消息传递

52. NUMA 的正确说法是：

A. 没有共享地址空间  
B. 有共享地址空间，但本地/远程访问延迟不同  
C. 只能是单核  
D. 不需要 coherence

53. UMA 常用的 Cache coherence 协议类型是：

A. snoopy protocol  
B. directory protocol only  
C. no coherence  
D. branch predictor

54. NUMA/大规模分布式共享内存更常用 directory protocol，原因是：

A. 避免向所有处理器广播，目录只联系相关 sharers/owner  
B. Directory 用来预测分支  
C. Directory 只存 page offset  
D. Directory 不能处理 dirty block

55. Cache coherence 主要规定：

A. 同一地址的多个缓存副本如何保持一致  
B. 不同地址读写在全局上必须如何排序  
C. 页表如何分级  
D. BTB 如何索引

56. Memory consistency 主要规定：

A. 同一 cache line 的 tag 位数  
B. 多地址读写顺序对程序员呈现什么语义  
C. CDB 的广播位宽  
D. vector lane 数量

57. MESI 四个状态不包括：

A. Invalid  
B. Exclusive  
C. Outdated  
D. Modified

58. MESI 中 E 状态的含义是：

A. 本 Cache 独有且 clean，内存最新  
B. 多 Cache 共享且 dirty  
C. 本 Cache 无效  
D. 内存过期且多个 Cache 都可写

59. MESI 初始四个处理器均为 I，执行 `P0 read a; P1 read a; P2 read a; P3 write a; P0 read a` 后，最后状态为：

A. P0=S, P1=I, P2=I, P3=S  
B. P0=E, P1=S, P2=S, P3=M  
C. P0=M, P1=I, P2=I, P3=I  
D. P0=I, P1=I, P2=I, P3=M

60. MOESI 中 O/Owned 状态表示：

A. cache block 被该 Cache 拥有，内存可能过期，它负责提供最新数据  
B. cache block 无效  
C. cache block 只能在内存中  
D. branch 预测 taken

61. Write invalidate 相比 write update/broadcast 的常见优势是：

A. 连续写同一块时，总线流量更少  
B. 每次写必须广播新数据给所有副本  
C. 不能用于 write-back  
D. 不需要独占权

62. Sequential consistency 要求普通内存操作中保持：

A. 只保持 W->W  
B. 只保持 W->R  
C. R->R、R->W、W->R、W->W  
D. 不保持任何顺序

63. Total Store Order 相对 SC 通常放松的是：

A. W->R  
B. R->R  
C. R->W  
D. 所有同步顺序

64. Domain-Specific Architecture 的典型设计原则不包括：

A. 使用专用存储减少数据移动  
B. 使用适合领域的并行形式  
C. 尽量使用领域需要的简单数据类型  
D. 用最复杂的通用乱序机制解决所有问题

65. TPU 的典型特征是：

A. 256 x 256 8-bit matrix multiply unit 和软件管理 scratchpad  
B. 只支持 branch prediction  
C. 没有专用存储  
D. 专门用于磁盘调度

## 6. 选择题答案与速解

| 题号 | 答案 | 速解 |
|---:|---|---|
| 1 | B | ISA 是软件可见接口，微结构可以不同。 |
| 2 | C | 性能是执行时间倒数。 |
| 3 | A | `Perf ∝ ClockRate / CPI`。 |
| 4 | D | 新旧比 `(2.2/1.5)/(1.8/1.2)=0.9778`。 |
| 5 | C | normalized geometric mean 与 reference choice 无关。 |
| 6 | B | `1/(0.7+0.3/10)=1.37`。 |
| 7 | A | `1/(F+(1-F)/100)=80`，`F≈0.25%`。 |
| 8 | D | load-store ISA 的 ALU 操作数来自寄存器。 |
| 9 | B | 三大典型 hazard 是 structural/data/control。 |
| 10 | A | load-use 数据到得太晚。 |
| 11 | A | RAW 是真依赖。 |
| 12 | B | WAR/WAW 是名字相关。 |
| 13 | B | 1-bit 在循环边界易错两次。 |
| 14 | B | 长期稳定每 3 次错 1 次。 |
| 15 | C | `2^2 * 2 * 4096 = 32768 bits`。 |
| 16 | B | BHT 方向，BTB 目标。 |
| 17 | A | 旧卷答案为 2,0。 |
| 18 | C | Scoreboard 检测但不重命名消除名字相关。 |
| 19 | B | Q 表示等待谁产生值。 |
| 20 | C | speculation issue 要 ROB+RS 都可用。 |
| 21 | C | 值可能来自 register 或 ROB。 |
| 22 | B | 乱序执行，按序提交。 |
| 23 | C | 每周期多发射才可能 CPI<1。 |
| 24 | A | Superscalar 硬件为主，VLIW 编译器为主。 |
| 25 | B | ROB 按序 commit。 |
| 26 | C | coherency miss 是多核共享相关。 |
| 27 | B | 大块利用空间局部性，减少冷启动 miss。 |
| 28 | A | 小块和大块各有代价。 |
| 29 | A | AMAT 基本公式。 |
| 30 | A | `(40*10+20*200)/1000*1.5=6.6`。 |
| 31 | A | pipelining cache 主要影响 hit time/throughput。 |
| 32 | A | L1 miss 后先去 L2/L3。 |
| 33 | B | dirty 表示改过但未写回。 |
| 34 | A | write-back 常搭配 write allocate。 |
| 35 | B | TLB 映射 VPN 到 PPN。 |
| 36 | D | `36-log2(16KB)=36-14=22`。 |
| 37 | A | `36-log2(16KB/8)=36-11=25`。 |
| 38 | D | 2-way 时 index+offset=`log2(8KB)=13`，tag=`36-13=23`。 |
| 39 | B | direct mapped 硬件简单、hit time 小。 |
| 40 | A | LRU 有 stack property。 |
| 41 | A | 行主序按行连续。 |
| 42 | B | tiling 提高局部性。 |
| 43 | A | 微结构状态通过 timing 泄露。 |
| 44 | A | Flynn 分类。 |
| 45 | B | TLP 对应多 PC，主要是 MIMD。 |
| 46 | A | `ceil(524/8)*4=66*4=264`。 |
| 47 | B | chaining 是元素级流水。 |
| 48 | A | 下一迭代依赖上一迭代。 |
| 49 | A | 各迭代独立，适合 DLP。 |
| 50 | A | CPU host，GPU device。 |
| 51 | A | UMA 统一访问延迟。 |
| 52 | B | NUMA 地址统一但延迟非统一。 |
| 53 | A | UMA 总线系统常 snoopy。 |
| 54 | A | Directory 降低广播规模。 |
| 55 | A | coherence 管同一地址。 |
| 56 | B | consistency 管多地址顺序。 |
| 57 | C | MESI 没有 Outdated。 |
| 58 | A | E 是 clean exclusive。 |
| 59 | A | P3 M 被 P0 read 后 P0/P3 为 S。 |
| 60 | A | O 表示 owner 提供最新数据，内存可旧。 |
| 61 | A | invalidate 对连续写更省流量。 |
| 62 | C | SC 保持四类普通顺序。 |
| 63 | A | TSO 典型放松 W->R。 |
| 64 | D | DSA 追求领域简化和专用化。 |
| 65 | A | TPU 是 DNN ASIC，有矩阵单元和 scratchpad。 |

## 7. 最后冲刺建议

1. 先把第 6 节 65 道选择题做两遍，错题回到三份 notes 对应小节。
2. 乱序大题每天手写一遍模板一和模板二，重点检查 commit 是否按序。
3. Cache 地址题只用一个模板：`offset = log2(block size)`，`index = log2(sets)`，`tag = address bits - index - offset`。VIPT 题注意 tag 用物理地址，index 受 page offset 约束。
4. DLP/TLP 复习不要只背名词，要能用一句话区分：SIMD/DLP 同一指令多数据，MIMD/TLP 多指令流多 PC，coherence 管同一地址，consistency 管多地址顺序。
5. 如果考试真的“选择题很多”，不要在网络拓扑、GPU throughput 这种低频难题上投入过多时间；先把 PPT 原题型的 Cache、branch、ROB、vector、MESI 拿稳。
