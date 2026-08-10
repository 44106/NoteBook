# 自测题与闪卡

建议闭卷做。每题先自己写答案，再展开讲义核对。

## A. 概念自测

1. 体系结构 ISA 和微结构 microarchitecture 的区别是什么？
2. 为什么单周期 CPU 的 CPI 是 1，但不一定性能最好？
3. 多周期 CPU 相比单周期 CPU 的优势是什么？
4. 流水线提高的是单条指令延迟还是吞吐？为什么？
5. Structural hazard、data hazard、control hazard 各举一例。
6. RAW、WAR、WAW 分别是什么意思？哪个是真依赖？
7. Forwarding 为什么不能解决所有 RAW？
8. Precise exception 的定义是什么？
9. ROB 如何保证 precise exception？
10. Reservation station 为什么能让独立指令越过依赖指令？
11. RAT 中 valid/tag/value 的含义是什么？
12. RS 中 V/tag/value 的含义是什么？
13. Tomasula 中 CDB 广播时会更新哪些结构？
14. Superscalar 为什么会提高 peak compute，但不一定提高 memory-bound 程序性能？
15. SIMD 和 SIMT 的区别是什么？
16. GPU 为什么用大量 warp 隐藏延迟？
17. Branch divergence 为什么降低 SIMT 利用率？
18. Memory coalescing 是什么？
19. Shared memory bank conflict 是什么？
20. Tiling 为什么提高矩阵乘性能？
21. Cache 为什么有效？
22. Direct-mapped、set-associative、fully associative 区别是什么？
23. Compulsory、capacity、conflict miss 如何区分？
24. Write-back 和 write-through 的区别是什么？
25. Write-allocate 和 write-no-allocate 的区别是什么？
26. Coherence 和 consistency 的区别是什么？
27. MSI 三个状态分别是什么？
28. MESI 比 MSI 多的 E 状态解决什么问题？
29. Snoop 协议为什么扩展性差？
30. Directory 协议记录什么？
31. AI 加速器为什么喜欢 buffer/scratchpad 而不是复杂 cache？
32. Weight stationary、output stationary、input stationary 分别想固定什么？
33. Systolic array 的核心思想是什么？
34. Ascend 中 Cube、Vector、Scalar、MTE 大致分别负责什么？
35. 算子融合为什么能提升性能？
36. Data parallel 的通信是什么？
37. Pipeline parallel 的通信是什么？
38. Tensor parallel 的 row-wise 通信是什么？
39. Tensor parallel 的 column-wise 通信是什么？
40. Ring AllReduce 的轮数和每 worker 通信量是多少？

## B. 计算自测

### B1. Amdahl

一个程序 75% 可并行，加速 8 倍，其余不变。总加速比是多少？

答案：

```text
1 / (0.25 + 0.75/8) = 1 / 0.34375 = 2.91
```

### B2. Roofline

某 kernel 每次迭代读 2 个 float、写 1 个 float，做 4 FLOPs。机器 peak = 20 TFLOP/s，bandwidth = 1 TB/s。判断瓶颈和性能上限。

答案：

```text
Bytes = 3 * 4 = 12 B
AI = 4/12 = 0.333 FLOPs/B
AI * BW = 0.333 * 1 TB/s = 0.333 TFLOP/s
min(20, 0.333) = 0.333 TFLOP/s
Memory-bound
```

### B3. CPI

某程序 30% load CPI=5，20% store CPI=4，40% ALU CPI=2，10% branch CPI=3。平均 CPI？

答案：

```text
0.3*5 + 0.2*4 + 0.4*2 + 0.1*3
= 1.5 + 0.8 + 0.8 + 0.3
= 3.4
```

### B4. Cache index

Cache 64B，block 8B，2-way。地址 0x38 属于哪个 block 和 set？

答案：

```text
block = 0x38 / 8 = 56/8 = 7
B = 64/8 = 8 blocks
sets = 8/2 = 4
set = block mod 4 = 7 mod 4 = 3
offset bits = log2(8)=3
index bits = log2(4)=2
```

### B5. Ring AllReduce

8 个 GPU，梯度大小 M=800 MB。Ring AllReduce 总轮数？每个 GPU 总发送多少？

答案：

```text
Rounds = 2(N-1)=14
Each round = M/N = 100 MB
Per GPU send = 14 * 100 MB = 1400 MB
```

## C. Anki 风格闪卡

```text
Front	Back	Tags
Roofline 的核心公式是什么？	Attainable FLOP/s = min(Peak FLOP/s, AI * Bandwidth)。	roofline
Arithmetic intensity 如何定义？	AI = Total FLOPs / Total Memory Bytes。	roofline
AI 小通常意味着什么？	Memory-bound，优先优化访存和数据复用。	roofline
Little's Law 是什么？	L = λW，即系统中平均请求数 = 吞吐率 * 延迟。	performance
CPU time 公式是什么？	CPU time = Instruction Count * Average CPI * Clock Cycle Time。	performance
RAW 是什么？	Read After Write，真数据依赖，后指令读前指令写的值。	cpu
WAR 是什么？	Write After Read，反依赖，通常是寄存器名字造成的 false dependence。	cpu
WAW 是什么？	Write After Write，输出依赖，通常可由 register renaming 消除。	cpu
ROB 的核心作用是什么？	保存乱序完成结果，并按程序顺序 commit，保证 precise exception。	cpu
Reservation station 的核心作用是什么？	缓存等待操作数的指令，让 ready 的独立指令可乱序执行。	cpu
RAT 中 valid=0 表示什么？	寄存器最新值尚未在寄存器文件中，而会由 tag 指向的 producer 产生。	tomasula
RS 中 source.V=0 表示什么？	该源操作数还没 ready，需要等待 source.tag 对应的广播。	tomasula
CDB 广播会更新什么？	匹配 tag 的 RAT/RF 项和所有 RS source 项。	tomasula
SIMT 是什么？	Single Instruction Multiple Thread，多个线程以 warp 形式 lock-step 执行。	gpu
Warp 通常是多少线程？	NVIDIA 常见为 32 个线程。	gpu
Branch divergence 为什么慢？	同一 warp 线程走不同分支，硬件需串行执行不同路径并 mask 不活跃线程。	gpu
Memory coalescing 是什么？	warp 中连续线程访问连续地址，合并成少数内存事务。	gpu
Shared memory bank conflict 是什么？	同一 warp 多线程访问同一 bank 的不同地址，访问被串行化。	gpu
Cache block 是什么？	Cache 管理和搬运的基本单位，也叫 cache line。	cache
Direct-mapped cache 的特点？	每个 memory block 只能放一个 cache line，简单快但冲突多。	cache
Fully associative cache 的特点？	每个 block 可放任意位置，冲突少但硬件复杂。	cache
Set-associative cache 的特点？	block 映射到一个 set，可放该 set 的 N 个 way。	cache
Compulsory miss 是什么？	第一次访问某个 block 导致的 miss。	cache
Conflict miss 是什么？	总容量够，但映射冲突导致的 miss。	cache
Capacity miss 是什么？	工作集超过 cache 总容量，即使全相联也会 miss。	cache
Write-back 的特点？	先写 cache，evict 时写回 memory，需要 dirty bit，节省带宽。	cache
Write-through 的特点？	写 cache 同时写 memory，简单但带宽压力大。	cache
Coherence 关注什么？	不同 core 对同一 memory location 的操作顺序。	coherence
Consistency 关注什么？	不同 core 对所有 memory locations 的全局可见顺序。	consistency
MSI 的 M 是什么？	Modified，唯一脏副本，本地可读写。	coherence
MESI 的 E 是什么？	Exclusive，唯一干净副本，本地写可无 bus action 地变 M。	coherence
Directory 协议为什么更可扩展？	不需要全局广播，每个 block 由 directory 跟踪 sharers/owner。	coherence
AI 加速器为什么用 scratchpad？	规则张量计算可显式管理数据，减少 tag/replacement/coherence 开销，提高数据复用。	accelerator
Cube 模块负责什么？	矩阵乘等高吞吐张量计算。	ascend
Vector 模块负责什么？	逐元素、激活、格式转换等向量计算。	ascend
Scalar 模块负责什么？	控制、分支、循环、地址和参数计算。	ascend
MTE 负责什么？	片上/片外数据搬运。	ascend
Systolic array 的优势？	规则 PE 阵列、局部通信、高数据复用，适合矩阵乘。	tpu
Data parallel 的主要通信？	梯度/权重 AllReduce。	parallel
Pipeline parallel 的主要通信？	相邻 stage 传 activations 和 activation gradients。	parallel
Row-wise tensor parallel forward 常需什么通信？	AllGather output activations。	parallel
Column-wise tensor parallel forward 常需什么通信？	ReduceScatter partial outputs；若每卡要完整输出则 AllReduce。	parallel
Ring AllReduce 几个阶段？	ReduceScatter 和 AllGather。	parallel
Ring AllReduce 总轮数？	2(N-1)。	parallel
Ring AllReduce 每 worker 发送量？	2M(N-1)/N。	parallel
ZeRO 的核心思想？	把 optimizer states/gradients/parameters 等冗余状态切分存储，减少每卡显存。	parallel
算子融合为什么有效？	减少中间结果写回/读回 HBM，提高片上复用。	runtime
```
