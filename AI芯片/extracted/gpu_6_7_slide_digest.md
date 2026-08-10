# Digest: 6-gpus-architecture.pptx

- Slides: 91

## 6-gpus-architecture.pptx Slide 1: AI Chip & Systems.Lecture 6: Graphics Processing Units

AI Chip & Systems.Lecture 6: Graphics Processing Units

Prof. Zeke Wang
Zhejiang University
April 9 2026

---

## 6-gpus-architecture.pptx Slide 2: Recall: Comparison of Memories

Recall: Comparison of Memories

2

SRAM

HBM

DDR

SSD

DISK

Capacity

Latency

Bandwidth

~10MB

~10GB

~100GB

~1TB

~10TB

~1ns

~100ns

~1us

~1ms

~100GB/s

~10MB/s

~1GB/s

~10GB/s

~1TB/s

---

## 6-gpus-architecture.pptx Slide 3: Recall: FF vs. SRAM vs. DRAM vs. SSD

Recall: FF vs. SRAM vs. DRAM vs. SSD

Flip-Flops (~K)
Very fast, parallel access
Very expensive (one bit costs tens of transistors)
Static RAM (~M)
Relatively fast, only one data word at a time
Expensive (one bit costs 6+ transistors)
Dynamic RAM (~G)
Slower, one data word at a time, reading destroys content (refresh), needs special process for manufacturing
Cheap (one bit costs only one transistor plus one capacitor)
Flash Memory (~T)
Much slower, access takes a long time, non-volatile
Very cheap (one transistor stores 16 bits or no transistors involved)

3

---

## 6-gpus-architecture.pptx Slide 4: SRAM

SRAM
Goal: buffering data on chip to reduce external memory traffic
Advantage: random access still keeps high performance
Disadvantage: low capacity (multiple MBs)
Where to Use SRAM?
Cache in CPU
Shared memory in GPU
On-chip buffer in AI accelerator
How to Use SRAM?
Multiple small separate SRAMs: low latency and high throughput
Banked design: wide access ports

Recall: SRAM Summary

4

---

## 6-gpus-architecture.pptx Slide 5: Recall: A Large Fraction of CPU is SRAM

Recall: A Large Fraction of CPU is SRAM

5

SRAM (Cache) in a CPU
Half chip area is occupied by cache
10MB (2.5MB/core * 4 cores)

Media/diagram refs: rId2:image:../media/image2.tiff

---

## 6-gpus-architecture.pptx Slide 6: CHART: {"chart_type": "LINE_MARKERS (65)", "has_title": false, "title": null, "series": [{"name": "Capacity", "values": 

CHART: {"chart_type": "LINE_MARKERS (65)", "has_title": false, "title": null, "series": [{"name": "Capacity", "values": [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 64.0, 128.0, 128.0]}, {"name": "Bandwidth", "values": [1.0, 3.007518796992481, 6.015037593984962, 8.01503759398496, 10.02255639097744, 12.03007518796992, 14.03007518796992, 16.03759398496241, 18.04511278195488, 19.54887218045113]}, {"name": "Latency", "values": [1.0, 1.0, 1.043478260869565, 1.142857142857143, 1.212121212121212, 1.263157894736842, 1.252086811352254, 1.274968125796855, 1.299826689774697, 1.31868131868132]}]}

Recall: DRAM Capacity, Bandwidth & Latency

128x

20x

1.3x

Media/diagram refs: rId3:chart:../charts/chart1.xml

---

## 6-gpus-architecture.pptx Slide 7: Recall: Key Messages behind Memory

Recall: Key Messages behind Memory

Memory Optimizations aim at size, bandwidth, not latency.
A memory read/write may need a few DDR operations, e.g., ACTIVATE, Column, Prechange, within a memory chip…
Different access sequence leads to different throughput, sequential (mainly row buffer hit) > random (mainly row buffer miss).
Random access is slow due to low row buffer miss rate.

7

---

## 6-gpus-architecture.pptx Slide 8: Recall: DRAM vs. SRAM

Recall: DRAM vs. SRAM

DRAM
Slower access (capacitor)
Higher density (1T 1C cell)
Lower cost
Requires refresh (power, performance, circuitry)
Manufacturing requires putting capacitor and logic together
SRAM
Faster access (no capacitor)
Lower density (6T cell)
Higher cost
No need for refresh
Manufacturing compatible with logic process (no capacitor)

8

---

## 6-gpus-architecture.pptx Slide 9: Recall: HBM

Recall: HBM

HBM stack:
It is used in conjunction with high-end GPUs, AI ASICs and FPGAs.
Each stack has 4/8 DRAM dies and a logic die.

9

Speaker notes: Substrate: 底座
Interposer: 插入式选样

Media/diagram refs: rId3:image:../media/image3.jpeg

---

## 6-gpus-architecture.pptx Slide 10: Recall: HBM in Nvidia A100

Recall: HBM in Nvidia A100

10

A100 GPU: 6 HBM2 stacks at the left/right side.

Media/diagram refs: rId2:image:../media/image4.jpeg

---

## 6-gpus-architecture.pptx Slide 11: Recall: Advantage and Disadvantage of HBM

Recall: Advantage and Disadvantage of HBM

11

Advantage of HBM:
High bandwidth: ~500GB/s per stack.
Low power consumption: due to running without termination.

Disadvantage of HBM:
Less flexibility: fixed, in the same package with compute chip.
Low capacity: really close to compute chip.
High cost: strict condition.

Speaker notes: Termination is needed when CPU is long away from memory. However, HBM is close to accelerator, so termination is not needed.

---

## 6-gpus-architecture.pptx Slide 12: Recall: NVME SSD

Recall: NVME SSD

12

Advantage: Large memory size, e.g., 16TB per SSD
Disadvantage: Low throughput, high latency, hard to use

Samsung PM853T 960GB Enterprise SSD (from https://www.tweaktown.com/reviews/6695/samsung-pm853t-960gb-enterprise-ssd-review/index.html)

Core

HW
Flash Ctrl.

Request Handler

ECC/Randomizer

Encryption Engine

SSD Controller

NAND Packages

8×128 GB = 1 TB

LPDDR DRAM

0.001×1,024 = 1 GB

Media/diagram refs: rId2:image:../media/image5.tiff

---

## 6-gpus-architecture.pptx Slide 13: Recall: Comparison of Memories

Recall: Comparison of Memories

13

SRAM

HBM

DDR

SSD

DISK

Capacity

Latency

Bandwidth

~10MB

~10GB

~100GB

~1TB

~10TB

~1ns

~100ns

~1us

~1ms

~100GB/s

~10MB/s

~1GB/s

~10GB/s

~1TB/s

---

## 6-gpus-architecture.pptx Slide 14: 14

14

Where Are We?

Media/diagram refs: rId2:image:../media/image6.png

---

## 6-gpus-architecture.pptx Slide 15: Agenda for Today

Agenda for Today

Why GPU?
Hardware Execution Model
Programming Model
SISD vs. SIMD vs. SPMD
GPU Programming Example
Advance
SIMT (Hardware) & Warp (Software)

15

---

## 6-gpus-architecture.pptx Slide 16: Motivation of In-network Computing

Motivation of In-network Computing

Why GPU?

Need More Computing Power.

---

## 6-gpus-architecture.pptx Slide 17: OpenAI: Compute Power Needed by NN Model

OpenAI: Compute Power Needed by NN Model

TABLE:
Model | Model Size | Compute/iteration / (OPs)
VGG 19 | 114M | ~19.6 B
“GPT-3” | 175B | ~250 T

One Forward Pass of Model:

CHART: {"chart_type": "LINE (4)", "has_title": false, "title": null, "series": [{"name": "One-cycle CPU", "values": [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]}, {"name": "Pipeline CPU", "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, {"name": "SIMD CPU", "values": [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]}, {"name": "GPU", "values": [20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0]}, {"name": "VGG19", "values": [19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6]}, {"name": "GPT-3", "values": [250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0, 250000.0]}]}

Speaker notes: KB MB GB TB
K M B T
1B=10亿

Media/diagram refs: rId3:chart:../charts/chart2.xml

---

## 6-gpus-architecture.pptx Slide 18: CPU:

CPU:
Few complex cores
Larger cache for low memory latency
Large and slow memory

CPU vs GPU： Compute Perspective

18

GPU:
Lots of simple cores
Small cache for low memory latency
Small and fast memory

Media/diagram refs: rId3:image:../media/image8.png; rId2:image:../media/image7.png

---

## 6-gpus-architecture.pptx Slide 19: State-of-the-art CPU GPU and FPGA

State-of-the-art CPU GPU and FPGA

TABLE:
 | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network
CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), / 1.4 (FP64) | 512GB / (80GB/s) | 32.0GB/s / (PCIe 4.0 X16) | No
GPU (Nvidia H100) | 18432 (128K) | 67 (FP32), / 34 (FP64), / 989 (FP32, Tensor), / 1979 (FP16, Tensor) | 80GB / (3350GB/s) | 64.0GB/s / (PCIe 5.0 X16) | No
FPGA (U280) | 9,024 / (25x18 MULs) | 1.8 (FP32) | 40GB / (460GB/s) | 16.0GB/s / (PCIe 4.0 X8) | Yes

Speaker notes: KB MB GB TB
K M B T E P
1B=10亿

---

## 6-gpus-architecture.pptx Slide 20: Relationship between CPU and GPU

Relationship between CPU and GPU

20

PCI Bus

CPU

GPU

Media/diagram refs: rId3:image:../media/image10.emf; rId2:image:../media/image9.png; rId4:image:../media/image11.jpg

---

## 6-gpus-architecture.pptx Slide 21: Motivation of In-network Computing

Motivation of In-network Computing

More cores  More trouble

Challenge: How to manipulate them?

Speaker notes: 之前千核项目  很多，只活了英伟达。

---

## 6-gpus-architecture.pptx Slide 22: GPU Computing

GPU Computing

Key Idea:
Computation is offloaded to the GPU
Three steps:
CPU-GPU data transfer (1)
GPU kernel execution (2)
GPU-CPU data transfer (3)

22

Media/diagram refs: rId3:image:../media/image12.emf

---

## 6-gpus-architecture.pptx Slide 23: CPU-GPU Co-processing:

CPU-GPU Co-processing:
CPU: Sequential or modestly parallel sections
GPU: Massively parallel sections

Serial Code (CPU):

. . .

Parallel Kernel (GPU):
KernelA<<<nBlk, nThr>>>(args);

Parallel Kernel (GPU):
KernelB<<<nBlk, nThr>>>(args);

Programming Model: CPU and GPU

23

---

## 6-gpus-architecture.pptx Slide 24: Recall: Amdahl’s Law

Recall: Amdahl’s Law

Amdahl’s Law
f: Parallelizable fraction of a program
N: Number of processors
Serial bottleneck of Amdahl’s Law:
Maximum speedup (1/(1-f)) limited by serial portion (1 - f)
Parallel portion (f) is usually not perfectly parallel
Synchronization overhead (e.g., updates to shared data)
Load imbalance overhead (imperfect parallelization)
Resource sharing overhead (contention among N processors)

24

Speedup =

1

+

1 - f

f

N

Amdahl, “Validity of the single processor approach to achieving large scale computing capabilities,” 1967.

---

## 6-gpus-architecture.pptx Slide 25: GPUs are SIMD Engines Underneath

GPUs are SIMD Engines Underneath

The instruction pipeline operates like a SIMD pipeline (e.g., an array processor)
However, the programming is done using threads, NOT SIMD instructions
To understand this, let’s go back to our parallelizable code example
But, before that, let’s distinguish between
Programming Model (Software)
	      vs.
Execution Model (Hardware)

25

---

## 6-gpus-architecture.pptx Slide 26: Programming Model vs. Hardware Execution Model

Programming Model vs. Hardware Execution Model

Programming Model： how the programmer expresses the code
E.g., Sequential (von Neumann), Data Parallel (SIMD), Dataflow, Multi-threaded (MIMD, SPMD), …
Hardware Execution Model： how the hardware executes the code underneath
E.g., Out-of-order execution, Vector processor, Array processor, Dataflow processor, Multiprocessor, Multithreaded processor, …
Discussion: Execution Model can be very different from Programming Model
E.g., von Neumann model implemented by an OoO processor
E.g., SPMD model implemented by a SIMD processor (a GPU)

26

---

## 6-gpus-architecture.pptx Slide 27: GPU: Programming Model vs. Hardware Execution Model

GPU: Programming Model vs. Hardware Execution Model

27

Hardware Execution Model

CUDA Programming Model

Streaming
 Multi-processor

GPU

CUDA core

Thread

Thread block

Grid

...

Media/diagram refs: rId8:image:../media/image18.png; rId3:image:../media/image13.png; rId7:image:../media/image17.png; rId6:image:../media/image16.png; rId5:image:../media/image15.png; rId4:image:../media/image14.png

---

## 6-gpus-architecture.pptx Slide 28: Agenda for Today

Agenda for Today

Where is GPU? & Key Message
Hardware Execution Model
Programming Model
SISD vs. SIMD vs. SPMD
GPU Programming Example
Advance
SIMT (Hardware) & Warp (Software)

28

---

## 6-gpus-architecture.pptx Slide 29: A Many-core GPU (Hardware Execution Model)

A Many-core GPU (Hardware Execution Model)

---

## 6-gpus-architecture.pptx Slide 30: NVIDIA GeForce GTX 285

NVIDIA GeForce GTX 285

NVIDIA-speak:
240 stream processors (CUDA cores)
“SIMT execution”
Generic speak:
30 cores
8 SIMD functional units per core
NVIDIA, “NVIDIA GeForce GTX 200 GPU. Architectural Overview. White Paper,” 2008.

Slide credit: Kayvon Fatahalian

30

Speaker notes: Link to the GTX 200 series white paper:
https://www.nvidia.com/docs/IO/55506/GeForce_GTX_200_GPU_Technical_Brief.pdf
The NVIDIA GeForce GTX 285 was launched on January 2009.

Media/diagram refs: rId3:image:../media/image19.png

---

## 6-gpus-architecture.pptx Slide 31: NVIDIA GeForce GTX 285 “core”(SM)

NVIDIA GeForce GTX 285 “core”(SM)

…

= instruction stream decode

= SIMD functional unit, control
   shared across 8 units

= execution context storage

= multiply-add

= multiply

64 KB of storage
for thread contexts (registers)

Slide credit: Kayvon Fatahalian

31

Speaker notes: 30 * 32 * 32 = 30 * 1024 = 30K fragments
64KB register file = 16 32-bit registers per thread = 64B (1/32 that of LRB)
16KB of shared scratch

80KB / core available to software

---

## 6-gpus-architecture.pptx Slide 32: NVIDIA GeForce GTX 285

NVIDIA GeForce GTX 285

Tex

…

30 cores on the GTX 285: 30K threads

Slide credit: Kayvon Fatahalian

32

Speaker notes: If you’re running a CUDA program, and your not launching 30K threads, you are certainly not getting full latency hiding, and you might not be using the GPU well

---

## 6-gpus-architecture.pptx Slide 33: Evolution of NVIDIA GPUs: Compute

Evolution of NVIDIA GPUs: Compute

33

Media/diagram refs: rId8:image:../media/image24.tiff; rId3:image:../media/image20.emf; rId7:image:../media/image23.tiff; rId6:image:../media/image22.tiff; rId5:image:../media/image21.tiff; rId10:image:../media/image26.tiff; rId4:image:../media/image19.png; rId9:image:../media/image25.tiff

---

## 6-gpus-architecture.pptx Slide 34: NVIDIA V100

NVIDIA V100

NVIDIA-speak:
5120 stream processors (CUDA cores)
“SIMT execution”
Generic speak:
80 cores
64 SIMD functional units per core
Tensor cores for Machine Learning
NVIDIA, “NVIDIA Tesla V100 GPU Architecture. White Paper,” 2017.

34

Speaker notes: CUDA core： stream processor

Media/diagram refs: rId3:image:../media/image23.tiff

---

## 6-gpus-architecture.pptx Slide 35: NVIDIA V100 Block Diagram

NVIDIA V100 Block Diagram

80 cores on the V100

https://devblogs.nvidia.com/inside-volta/

35

Media/diagram refs: rId3:image:../media/image11.jpg

---

## 6-gpus-architecture.pptx Slide 36: NVIDIA A100

NVIDIA A100

NVIDIA-speak:
6912 stream processors (CUDA cores)
“SIMT execution”
Generic speak:
108 cores
64 SIMD functional units per core
Tensor cores for Machine Learning
Support for sparsity
New floating point data type (TF32)
https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

36

Speaker notes: 5 HBM2 stacks, 10 512-bit memory controllers

Sparsity is possible in deep learning because the importance of individual weights evolves during the learning process, and by the end of network training, only a subset of weights have acquired a meaningful purpose in determining the learned output. The remaining weights are no longer needed (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

TensorFloat-32 (TF32) uses 8 bit for exponent and 10 bits for mantissa. This way, TF32 provides the range of FP32 with the precision of FP16 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

Media/diagram refs: rId4:image:../media/image26.tiff

---

## 6-gpus-architecture.pptx Slide 37: NVIDIA A100 Block Diagram

NVIDIA A100 Block Diagram

108 cores on the A100
(Up to 128 cores in the full-blown chip)
40MB L2 cache

https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

37

Speaker notes: The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2 cache.The L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

Media/diagram refs: rId3:image:../media/image27.png

---

## 6-gpus-architecture.pptx Slide 38: NVIDIA H100

NVIDIA H100

NVIDIA-speak:
8448 stream processors (CUDA cores)
“SIMT execution”
Generic speak:
132 cores
64 SIMD functional units per core
Tensor cores for Machine Learning
Support for sparsity
Support for transformer
https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

38

Speaker notes: 5 HBM2 stacks, 10 512-bit memory controllers

Sparsity is possible in deep learning because the importance of individual weights evolves during the learning process, and by the end of network training, only a subset of weights have acquired a meaningful purpose in determining the learned output. The remaining weights are no longer needed (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

TensorFloat-32 (TF32) uses 8 bit for exponent and 10 bits for mantissa. This way, TF32 provides the range of FP32 with the precision of FP16 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

Media/diagram refs: rId3:image:../media/image28.jpeg

---

## 6-gpus-architecture.pptx Slide 39: NVIDIA H100 Block Diagram

NVIDIA H100 Block Diagram

https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

39

Speaker notes: The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2 cache.The L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/).

Media/diagram refs: rId3:image:../media/image29.jpeg

---

## 6-gpus-architecture.pptx Slide 40: GPU Trend: H100 vs. A100

GPU Trend: H100 vs. A100

40

TABLE:
 | FP8 | FP16 | FP32 | FP64 | Memory bandwidth | Memory capacity
H100 | 4000T | 2000T | 1000T | 60T | 3TB/s | 80GB
A100 | 666T | 666T | 333T | 20T | 2TB/s | 80GB

Compute power scales well.

GPU memory capacity does not scale well.

Speaker notes: 军迷：
算力：武器 坦克等
内存：后勤

---

## 6-gpus-architecture.pptx Slide 41: Agenda for Today

Agenda for Today

Where is GPU? & Key Message
Hardware Execution Model
Programming Model
SISD vs. SIMD vs. SPMD
GPU Programming Example
Advance
SIMT (Hardware) & Warp (Software)

41

---

## 6-gpus-architecture.pptx Slide 42: How Can You Exploit Parallelism Here?

How Can You Exploit Parallelism Here?

42

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Scalar Sequential Code

Let’s examine three programming options to exploit instruction-level parallelism present in this sequential code:
1. Sequential (SISD)
2. Data-Parallel (SIMD)
3. Multithreaded (SPMD)

---

## 6-gpus-architecture.pptx Slide 43: Prog. Model 1: Sequential (SISD)

Prog. Model 1: Sequential (SISD)

43

load

add

store

Iter. 1

Iter. 2

Scalar Sequential Code

Can be executed on thee processors:
1, Pipelined processor
2, Out-of-order execution processor
Independent instructions executed when ready
Different iterations are present in the instruction window and can execute in parallel in multiple functional units
3, Superscalar or VLIW processor
Can fetch and execute multiple instructions per cycle

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

---

## 6-gpus-architecture.pptx Slide 44: load

load

add

store

Iter. 1

Iter. 2

Scalar Sequential Code

Prog. Model 2: Data Parallel (SIMD)

44

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

Vector Instruction

Vectorized Code

Motivation: Each iteration is independent
Idea: Programmer or compiler generates a SIMD instruction to execute the same instruction from all iterations across different data

VLD     A  V1

VLD     B  V2

VADD     V1 + V2  V3

VST     V3  C

---

## 6-gpus-architecture.pptx Slide 45: load

load

add

store

Iter. 1

Iter. 2

Scalar Sequential Code

Prog. Model 3: Multithreaded

45

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

Motivation: Each iteration is independent
Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)

---

## 6-gpus-architecture.pptx Slide 46: Prog. Model 3: Multithreaded

Prog. Model 3: Multithreaded

46

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Realization: Each iteration is independent
Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)

This programming model (software) is called:
SPMD: Single Program Multiple Data

---

## 6-gpus-architecture.pptx Slide 47: SPMD

SPMD

SPMD: Single procedure/program, multiple data
This is a programming model rather than computer organization
Each processing element executes the same procedure, except on different data elements
Procedures can synchronize at certain points in program, e.g. barriers
Key Idea of SPMD: multiple instruction streams execute the same program
Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
Modern GPUs programmed in a similar way on a SIMD hardware

47

---

## 6-gpus-architecture.pptx Slide 48: Agenda for Today

Agenda for Today

Where is GPU? & Key Message
Hardware Execution Model
Programming Model
SISD vs. SIMD vs. SPMD
GPU Programming Example
Advance
SIMT (Hardware) & Warp (Software)

48

---

## 6-gpus-architecture.pptx Slide 49: CUDA/OpenCL Programming Model

CUDA/OpenCL Programming Model

Single Program Multiple Data (SPMD), e.g., CUDA
Bulk synchronous programming: Global (coarse-grain) synchronization between kernels
The device (typically GPU) executes CUDA kernels
Grid
Thread Block
CUDA runtime schedules at granularity of thread block.
A thread block is a programming abstraction that represents a group of threads that can be executed in parallel.
Within a block, shared memory, and synchronization.
Thread
A thread corresponds to an iteration.

49

---

## 6-gpus-architecture.pptx Slide 50: GPU: Programming Model vs. Hardware Execution Model

GPU: Programming Model vs. Hardware Execution Model

50

Hardware Execution Model

CUDA Programming Model

Streaming
 Multi-processor

GPU

CUDA core

Thread

Thread block

Grid

...

Speaker notes: Wrap

Media/diagram refs: rId8:image:../media/image18.png; rId3:image:../media/image13.png; rId7:image:../media/image17.png; rId6:image:../media/image16.png; rId5:image:../media/image15.png; rId4:image:../media/image14.png

---

## 6-gpus-architecture.pptx Slide 51: CUDA: Memory Hierarchy

CUDA: Memory Hierarchy

51

Media/diagram refs: rId2:image:../media/image30.emf

---

## 6-gpus-architecture.pptx Slide 52: Function prototypes

Function prototypes
   float serialFunction(…);
   __global__ void kernel(…);
main()
1) Allocate memory space on the device – cudaMalloc(&d_in, bytes);
2) Transfer data from host to device – cudaMemCpy(d_in, h_in, …);
3) Execution configuration setup: #blocks and #threads
4) Kernel call – kernel<<<execution configuration>>>(args…);
5) Transfer results from device to host – cudaMemCpy(h_out, d_out, …);
Kernel – __global__ void kernel(type args,…)
Automatic variables transparently assigned to registers
Shared memory:  __shared__
Intra-block synchronization: __syncthreads();

Repeat as needed

Traditional Program Structure in CUDA

52

Slide credit: Hwu & Kirk

---

## 6-gpus-architecture.pptx Slide 53: CUDA Programming Language

CUDA Programming Language

Memory allocation
cudaMalloc((void**)&d_in, #bytes);
Memory copy
cudaMemcpy(d_in, h_in, #bytes, cudaMemcpyHostToDevice);
Kernel launch
kernel<<< #blocks, #threads >>>(args);
Memory deallocation
cudaFree(d_in);
Explicit synchronization
cudaDeviceSynchronize();

53

---

## 6-gpus-architecture.pptx Slide 54: First GPU Example: Vector Addition (I)

First GPU Example: Vector Addition (I)

Key Idea: one GPU thread to each element-wise addition

54

Media/diagram refs: rId3:image:../media/image32.emf; rId2:image:../media/image31.emf

---

## 6-gpus-architecture.pptx Slide 55: First GPU Example: Vector Addition (II)

First GPU Example: Vector Addition (II)

A grid: the whole set of threads
We need a way to assign threads to GPU cores

55

Media/diagram refs: rId3:image:../media/image32.emf; rId2:image:../media/image31.emf

---

## 6-gpus-architecture.pptx Slide 56: First GPU Example: Vector Addition (III)

First GPU Example: Vector Addition (III)

We group threads into blocks

Block 0

Block 1

Block 2

Block 3

56

blockIdx = 0

blockIdx = 1

blockIdx = 2

blockIdx = 3

threadIdx = 0

threadIdx = 1

threadIdx = 2

blockDim = 4

Speaker notes: 每个block有四个threads。
blockIdx = 0

Media/diagram refs: rId3:image:../media/image31.emf; rId4:image:../media/image32.emf

---

## 6-gpus-architecture.pptx Slide 57: GPU: Programming Model vs. Hardware Execution Model

GPU: Programming Model vs. Hardware Execution Model

57

Hardware Execution Model

CUDA Programming Model

Streaming
 Multi-processor

GPU

CUDA core

Thread

Thread block

Grid

...

Speaker notes: Wrap

Media/diagram refs: rId8:image:../media/image18.png; rId3:image:../media/image13.png; rId7:image:../media/image17.png; rId6:image:../media/image16.png; rId5:image:../media/image15.png; rId4:image:../media/image14.png

---

## 6-gpus-architecture.pptx Slide 58: Host Code Example: Vector Addition

Host Code Example: Vector Addition

void vecadd(float* A, float* B, float* C, int N) {
    //1, Allocate GPU memory
    float *A_d, *B_d, *C_d;
    cudaMalloc((void**) &A_d, N*sizeof(float));
    cudaMalloc((void**) &B_d, N*sizeof(float));
    cudaMalloc((void**) &C_d, N*sizeof(float));
    //2, Copy data to GPU memory
    cudaMemcpy(A_d, A, N*sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(B_d, B, N*sizeof(float), cudaMemcpyHostToDevice);
    //3, Perform computation on GPU
    ...
    //4, Copy data from GPU memory
    cudaMemcpy(C, C_d, N*sizeof(float), cudaMemcpyDeviceToHost);
    //5, Deallocate GPU memory
    cudaFree(A_d);
    cudaFree(B_d);
    cudaFree(C_d);
}

58

Slide credit: Izzat El Hajj

const unsigned int numThreadsPerBlock = 512;
const unsigned int numBlocks = N/numThreadsPerBlock;
vecadd_kernel<<<numBlocks, numThreadsPerBlock>>>(A_d, B_d, C_d, N);

---

## 6-gpus-architecture.pptx Slide 59: Kernel Code Example: Vector Addition

Kernel Code Example: Vector Addition

59

Slide credit: Izzat El Hajj

__global__ void vecadd_kernel(float* A, float* B, float* C, int N) {
    int i = blockDim.x*blockIdx.x + threadIdx.x;
    C[i] = A[i] + B[i];
}

blockDim: block dimension

blockIdx: block index within a grid

threadIdx: thread index within a block

---

## 6-gpus-architecture.pptx Slide 60: Boundary Conditions

Boundary Conditions

Question: What if the size of the input is not a multiple of the number of threads per block?
Solution: use the ceiling to launch extra threads then omit the threads after the boundary
Host code:
Kernel code:

const unsigned int numBlocks = (N +numThreadsPerBlock – 1)/numThreadsPerBlock;

__global__ void vecadd_kernel(float* A, float* B, float* C, int N) {
    int i = blockDim.x*blockIdx.x + threadIdx.x;
    if(i < N) {
        C[i] = A[i] + B[i]; }
}

60

vecadd_kernel<<<numBlocks, numThreadsPerBlock>>>(A_d, B_d, C_d, N);

---

## 6-gpus-architecture.pptx Slide 61: Sample GPU Program: Matrix Multiplication

Sample GPU Program: Matrix Multiplication

61

Slide credit: Hyesoon Kim

Media/diagram refs: rId2:image:../media/image33.png

---

## 6-gpus-architecture.pptx Slide 62: Indexing and Memory Access

Indexing and Memory Access

Images are 2D data structures
height x width
Image[j][i], where 0 ≤ j < height, and 0 ≤ i < width

Image[0][1]

Image[1][2]

62

0

1

2

3

4

5

6

7

Media/diagram refs: rId3:image:../media/image34.emf

---

## 6-gpus-architecture.pptx Slide 63: Image Layout in Memory

Image Layout in Memory

Row-major layout
Image[j][i] = Image[j x width + i]

Image[0][1] = Image[0 x 8 + 1]

Image[1][2] = Image[1 x 8 + 2]

63

Stride = width

Media/diagram refs: rId3:image:../media/image35.emf

---

## 6-gpus-architecture.pptx Slide 64: Indexing and Memory Access: 1D Grid

Indexing and Memory Access: 1D Grid

One GPU thread per pixel
Grid of Blocks of Threads
gridDim.x, blockDim.x
blockIdx.x, threadIdx.x

Block 0

Thread 0

Thread 1

Thread 2

Thread 3

blockIdx.x

threadIdx.x

blockIdx.x * blockDim.x + threadIdx.x

6 * 4 + 1 = 25

64

Media/diagram refs: rId3:image:../media/image36.emf; rId6:image:../media/image39.emf; rId5:image:../media/image38.emf; rId4:image:../media/image37.emf

---

## 6-gpus-architecture.pptx Slide 65: Agenda for Today

Agenda for Today

Where is GPU? & Key Message
Hardware Execution Model
Programming Model
SISD vs. SIMD vs. SPMD
GPU Programming Example
Advance
SIMT (Hardware) & Warp (Software)

65

---

## 6-gpus-architecture.pptx Slide 66: GPU: Programming Model vs. Hardware Execution Model

GPU: Programming Model vs. Hardware Execution Model

66

Hardware Execution Model

CUDA Programming Model

Streaming
 Multi-processor

GPU

CUDA core

Thread

Thread block

Grid

...

Wrap

SIMT

Speaker notes: SIMD Wrap

Media/diagram refs: rId8:image:../media/image18.png; rId3:image:../media/image13.png; rId7:image:../media/image17.png; rId6:image:../media/image16.png; rId5:image:../media/image15.png; rId4:image:../media/image14.png

---

## 6-gpus-architecture.pptx Slide 67: SIMT (Hardware) & Warp (Software)

SIMT (Hardware) & Warp (Software)

SIMT: Single Instruction Multiple Thread
Key Feature: 16 CUDA cores in a SM are executed in a lock step.

67

Warp:
A warp, a basic execution unit, consists of 32 consecutive threads
A thread block is divided into warps for SIMT execution.

…

t0 t1 t2 … t31

Block 0’s warps

Block 1’s warps

Block 2’s warps

---

## 6-gpus-architecture.pptx Slide 68: Motivation of In-network Computing

Motivation of In-network Computing

Why SIMT and Warp?

Reduce GPU scheduling overhead

---

## 6-gpus-architecture.pptx Slide 69: Warp 0 at PC X+3

Warp 0 at PC X+3

Warp 0 at PC X+2

Warp 0 at PC X+1

How to Form Warps?

69

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Warp 0 at PC X

Warp: A set of threads that execute
the same instruction (i.e., at the same PC)

Iter. 32

---

## 6-gpus-architecture.pptx Slide 70: Mapping Warps on a SIMT Hardware

Mapping Warps on a SIMT Hardware

Warp:
A thread block is divided into warps.
A warp executes the same instruction on different data elements
SIMT Pipeline:
16 CUDA cores are executed in a lock step to serve each warp.

70

Thread Warp 0

Thread Warp 8

Thread Warp 7

Thread Warp

Scalar

Thread

0

1

2

31

Common PC

SIMT Pipeline

Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

Speaker notes: In SIMD, you need to specify the data array + an instruction (on which to operate the data on) + THE INSTRUCTION WIDTH.Eg: You might want to add 2 integer arrays of length 16, then a SIMD instruction would look like (the instruction has been cooked-up by me for demo)add.16 arr1 arr2However, SIMT doesn't bother about the instruction width. So, essentially, you could write the above example as:arr1[i] + arr2[i]and then launch as many threads as the length of the array, as you want.Note that, if the array size was, let us say, 32, then SIMD EXPECTS you to explicitly call two such 'add.16' instructions!Whereas, this is not the case with SIMT.

---

## 6-gpus-architecture.pptx Slide 71: GPU Execution with Warps

GPU Execution with Warps

71

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Warp 0 at PC X

Assume: a warp consists of 32 threads
If you have 32K iterations, and 1 iteration/thread  1K warps
Warps can be interleaved on the same pipeline  Fine grained multithreading of warps.

Warp 1 at PC X

Iter. 33

Iter. 34

Warp 20 at PC X+2

Iter.
20*32 + 1

Iter.
20*32 + 2

---

## 6-gpus-architecture.pptx Slide 72: Warp Instruction Level Parallelism

Warp Instruction Level Parallelism

Can overlap execution of multiple instructions
Example machine has 32 threads per warp and 8 lanes
Completes 24 operations/cycle while issuing 1 warp/cycle

72

W3

W0

W1

W4

W2

W5

Load Unit

Multiply Unit

Add Unit

time

Warp issue

Slide credit: Krste Asanovic

---

## 6-gpus-architecture.pptx Slide 73: Motivation of In-network Computing

Motivation of In-network Computing

SIMT is not SIMD!

---

## 6-gpus-architecture.pptx Slide 74: SIMD vs. SIMT Execution Model

SIMD vs. SIMT Execution Model

SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
[VLD, VLD, VADD, VST], VLEN
SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
[LD, LD, ADD, ST], NumThreads
Two Major SIMT Advantages:
Can treat each thread separately  i.e., can execute each thread independently on any type of scalar pipeline  MIMD processing
Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

74

---

## 6-gpus-architecture.pptx Slide 75: Slide credit: Hyesoon Kim

Slide credit: Hyesoon Kim

75

GPUs were invented and gpus are a kind vector computer which is really wild because while gpus have big vectors they essentially run scalar programs on each element and you can think of them as running a vector of scalar programs which by the way was a genius abstraction because everybody can write a scalar program almost nobody can write a vector program but suddenly we had all kinds of people doing vector programs on GPUs”
                                                               --- Jim Keller @DAC’24

SPMD: Genius Abstraction

---

## 6-gpus-architecture.pptx Slide 76: SIMT Code vs. SIMD Code

SIMT Code vs. SIMD Code

for (ii = 0; ii < 100000; ++ii) {
C[ii] = A[ii] + B[ii];
}

// there are 100000 threads
__global__ void KernelFunction(…) {
  int tid = blockDim.x * blockIdx.x + threadIdx.x;
  int varA = aa[tid];
  int varB = bb[tid];
  C[tid] = varA + varB;
}

CPU scalar code

CUDA code

Slide credit: Hyesoon Kim

76

// there are 25000 loops with SIMD=4
…
v_A = vec_load (A);
v_B = vec_load (B);
 v_C = vec_add(v_A, v_B);
Vec_store(v_C, C)
…
}

CPU vector code

---

## 6-gpus-architecture.pptx Slide 77: Warp-based SIMD vs. Traditional SIMD

Warp-based SIMD vs. Traditional SIMD

Traditional SIMD contains a single thread
Sequential instruction execution; lock-step operations in a SIMD instruction
Programming model is SIMD (no extra threads)  SW needs to know vector length
ISA contains vector/SIMD instructions
Warp-based SIMD consists of multiple scalar threads executing in a SIMD manner (i.e., same instruction executed by all threads)
Does not have to be lock step
Each thread can be treated individually (i.e., placed in a different warp)  programming model not SIMD
SW does not need to know vector length
Enables multithreading and flexible dynamic grouping of threads
ISA is scalar  SIMD operations can be formed dynamically
Essentially, it is SPMD programming model implemented on SIMD hardware

77

---

## 6-gpus-architecture.pptx Slide 78: Threads Can Take Different Paths in Warp-based SIMD

Threads Can Take Different Paths in Warp-based SIMD

Each thread can have conditional control flow instructions
Threads can execute different control flow paths

78

Thread Warp

Common PC

Thread
2

Thread
3

Thread
4

Thread
1

B

C

D

E

F

A

G

Slide credit: Tor Aamodt

---

## 6-gpus-architecture.pptx Slide 79: Control Flow Problem in GPUs/SIMT

Control Flow Problem in GPUs/SIMT

A GPU uses a SIMD pipeline to save area on control logic
Groups scalar threads into warps
Branch divergence occurs when threads inside warps branch to different execution paths

79

Branch

Path A

Path B

Slide credit: Tor Aamodt

---

## 6-gpus-architecture.pptx Slide 80: SIMD Utilization

SIMD Utilization

Intra-warp divergence

Compute(threadIdx.x);
if (threadIdx.x % 2 == 0){
  Do_this(threadIdx.x);
}
else{
  Do_that(threadIdx.x);
}

80

Media/diagram refs: rId2:image:../media/image40.emf

---

## 6-gpus-architecture.pptx Slide 81: Increasing SIMD Utilization

Increasing SIMD Utilization

Divergence-free execution

Compute(threadIdx.x);
if (threadIdx.x < 32){
  Do_this(threadIdx.x * 2);
}
else{
  Do_that((threadIdx.x%32)*2+1);
}

81

Media/diagram refs: rId2:image:../media/image41.emf

---

## 6-gpus-architecture.pptx Slide 82: Vector Reduction: Naïve Mapping (I)

Vector Reduction: Naïve Mapping (I)

0

1

2

3

4

5

7

6

10

9

8

11

0+1

2+3

4+5

6+7

10+11

8+9

0...3

4..7

8..11

0..7

8..15

iterations

Thread 0

Thread 8

Thread 2

Thread 4

Thread 6

Thread 10

82

Slide credit: Hwu & Kirk

…

---

## 6-gpus-architecture.pptx Slide 83: Vector Reduction: Naïve Mapping (II)

Vector Reduction: Naïve Mapping (II)

Program with low SIMD utilization

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = 1; stride < blockDim.x; stride *= 2) {
  __syncthreads();
  if (t % (2*stride) == 0)
    partialSum[t] += partialSum[t + stride];
}

83

---

## 6-gpus-architecture.pptx Slide 84: Divergence-Free Mapping (I)

Divergence-Free Mapping (I)

All active threads belong to the same warp

Thread 0

0

1

2

3

…

13

15

14

18

17

16

19

0+16

15+31

Thread 1

Thread 2

Thread 14

Thread 15

iterations

84

Slide credit: Hwu & Kirk

---

## 6-gpus-architecture.pptx Slide 85: Divergence-Free Mapping (II)

Divergence-Free Mapping (II)

Program with high SIMD utilization

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = blockDim.x; stride > 0;  stride >> 1){
  __syncthreads();
  if (t < stride)
    partialSum[t] += partialSum[t + stride];
}

85

---

## 6-gpus-architecture.pptx Slide 86: Programming Model vs. Hardware Execution Model

Programming Model vs. Hardware Execution Model

86

Hardware Programming Model

Programming Model

Core

Streaming
 Multi-processor

GPU

CUDA core:

Thread

Thread block (s)

Wrap

Thread blocks

---

## 6-gpus-architecture.pptx Slide 87: NVIDIA H100 Block Diagram

NVIDIA H100 Block Diagram

144 cores on the full GH100
60MB L2 cache

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

87

Media/diagram refs: rId4:image:../media/image42.png

---

## 6-gpus-architecture.pptx Slide 88: NVIDIA H100 Core

NVIDIA H100 Core

48 TFLOPS Single Precision*
24 TFLOPS Double Precision*
800 TFLOPS (FP16, Tensor Cores)*

88

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
* Preliminary performance estimates

Media/diagram refs: rId5:image:../media/image44.jpg; rId4:image:../media/image43.png

---

## 6-gpus-architecture.pptx Slide 89: Asynchronous memory copy with LDGSTS instruction vs. TMA

Asynchronous memory copy with LDGSTS instruction vs. TMA

NVIDIA H100 Tensor Memory Accelerator

89

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

TMA unit reduces addressing overhead
A single thread per warp issues the TMA operation
Support for different tensor layouts (1D-5D)

Speaker notes: New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can transfer large blocks of data efficiently between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.
New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can efficiently transfer large blocks of data between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.

Media/diagram refs: rId5:image:../media/image46.jpg; rId4:image:../media/image45.jpg

---

## 6-gpus-architecture.pptx Slide 90: Shared memory virtual address space distributed across the blocks of a cluster

Shared memory virtual address space distributed across the blocks of a cluster
Load, store, and atomic operations to other SM’s shared memory

NVIDIA H100 Distributed Shared Memory

90

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

Thread block clusters and distributed shared memory (DSMEM) are leveraged via cooperative_groups API
TMA unit supports copies across thread blocks in a cluster
Asynchronous transaction barriers

Speaker notes: Distributed shared memory allows direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks.
Distributed shared memory enables direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks

Media/diagram refs: rId4:image:../media/image47.jpg

---

## 6-gpus-architecture.pptx Slide 91: NVIDIA GeForce GTX 285 “core”

NVIDIA GeForce GTX 285 “core”

…

64 KB of storage
for thread contexts (registers)

Groups of 32 threads share instruction stream (each group is a Warp)
Up to 32 warps are simultaneously interleaved
Up to 1024 thread contexts can be stored

Slide credit: Kayvon Fatahalian

91

Speaker notes: To get maximal latency hiding:
Run 1/32 of the time
16 words per thread = 64B

---

# Digest: 7-gpus-optimization.pptx

- Slides: 120

## 7-gpus-optimization.pptx Slide 1: AI Chip & Systems.Lecture 7: GPU Optimization

AI Chip & Systems.Lecture 7: GPU Optimization

Prof. Zeke Wang
Zhejiang University
April 20 2026

---

## 7-gpus-optimization.pptx Slide 2: CPU:

CPU:
Few complex cores
Larger cache for low memory latency
Large and slow memory

Recall: CPU vs GPU： Compute Perspective

2

GPU:
Lots of simple cores
Small cache for low memory latency
Small and fast memory

Media/diagram refs: rId3:image:../media/image3.png; rId2:image:../media/image2.png

---

## 7-gpus-optimization.pptx Slide 3: Recall: Relationship between CPU and GPU

Recall: Relationship between CPU and GPU

3

PCI Bus

CPU

GPU

Media/diagram refs: rId3:image:../media/image5.emf; rId2:image:../media/image4.png; rId4:image:../media/image6.jpg

---

## 7-gpus-optimization.pptx Slide 4: Recall: SPMD

Recall: SPMD

SPMD: Single procedure/program, multiple data
This is a programming model rather than computer organization
Each processing element executes the same procedure, except on different data elements
Procedures can synchronize at certain points in program, e.g. barriers
Key Idea of SPMD: multiple instruction streams execute the same program
Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
Modern GPUs programmed in a similar way on a SIMD hardware

4

---

## 7-gpus-optimization.pptx Slide 5: Recall Programming Model vs. Hardware Execution Model

Recall Programming Model vs. Hardware Execution Model

5

Hardware Execution Model

CUDA Programming Model

Streaming
 Multi-processor

GPU

CUDA core

Thread

Thread block

Grid

...

Warp

SIMT

Speaker notes: SIMD Wrap

Media/diagram refs: rId8:image:../media/image12.png; rId3:image:../media/image7.png; rId7:image:../media/image11.png; rId6:image:../media/image10.png; rId5:image:../media/image9.png; rId4:image:../media/image8.png

---

## 7-gpus-optimization.pptx Slide 6: Recall: SIMT (Hardware) & Warp (Software)

Recall: SIMT (Hardware) & Warp (Software)

SIMT: Single Instruction Multiple Thread
More precisely, SIMD (Single Instruction Multiple Data)
Key Feature: 16 CUDA cores in a SM are executed in a lock step.

6

Warp:
A warp, a basic execution unit, consists of 32 consecutive threads
A thread block is divided into warps for SIMT execution.

…

t0 t1 t2 … t31

Block 0’s warps

Block 1’s warps

Block 2’s warps

---

## 7-gpus-optimization.pptx Slide 7: Motivation of In-network Computing

Motivation of In-network Computing

Why SIMT and Warp?

Reduce GPU scheduling overhead

---

## 7-gpus-optimization.pptx Slide 8: Recall: Mapping Warps on a SIMT Hardware

Recall: Mapping Warps on a SIMT Hardware

Warp:
A thread block is divided into warps.
A warp executes the same instruction on different data elements
SIMT Pipeline:
16 CUDA cores are executed in a lock step to serve each warp.

8

Thread Warp 0

Thread Warp 8

Thread Warp 7

Thread Warp

Scalar

Thread

0

1

2

31

Common PC

SIMT Pipeline

Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

Speaker notes: In SIMD, you need to specify the data array + an instruction (on which to operate the data on) + THE INSTRUCTION WIDTH.Eg: You might want to add 2 integer arrays of length 16, then a SIMD instruction would look like (the instruction has been cooked-up by me for demo)add.16 arr1 arr2However, SIMT doesn't bother about the instruction width. So, essentially, you could write the above example as:arr1[i] + arr2[i]and then launch as many threads as the length of the array, as you want.Note that, if the array size was, let us say, 32, then SIMD EXPECTS you to explicitly call two such 'add.16' instructions!Whereas, this is not the case with SIMT.

---

## 7-gpus-optimization.pptx Slide 9: Recall: GPU Execution with Warps

Recall: GPU Execution with Warps

9

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Warp 0 at PC X

Assume: a warp consists of 32 threads
If you have 32K iterations, and 1 iteration/thread  1K warps
Warps can be interleaved on the same pipeline  Fine grained multithreading of warps.

Warp 1 at PC X

Iter. 33

Iter. 34

Warp 20 at PC X+2

Iter.
20*32 + 1

Iter.
20*32 + 2

---

## 7-gpus-optimization.pptx Slide 10: Recall: Warp Instruction Level Parallelism

Recall: Warp Instruction Level Parallelism

Can overlap execution of multiple instructions
Example machine has 32 threads per warp and 8 lanes
Completes 24 operations/cycle while issuing 1 warp/cycle

10

W3

W0

W1

W4

W2

W5

Load Unit

Multiply Unit

Add Unit

time

Warp issue

Slide credit: Krste Asanovic

---

## 7-gpus-optimization.pptx Slide 11: Motivation of In-network Computing

Motivation of In-network Computing

SIMT is not SIMD!

---

## 7-gpus-optimization.pptx Slide 12: Recall: SIMT Code vs. SIMD Code

Recall: SIMT Code vs. SIMD Code

for (ii = 0; ii < 100000; ++ii) {
C[ii] = A[ii] + B[ii];
}

// there are 100000 threads
__global__ void KernelFunction(…) {
  int tid = blockDim.x * blockIdx.x + threadIdx.x;
  int varA = aa[tid];
  int varB = bb[tid];
  C[tid] = varA + varB;
}

CPU scalar code

CUDA code

Slide credit: Hyesoon Kim

12

// there are 25000 loops with SIMD=4
…
v_A = vec_load (A);
v_B = vec_load (B);
 v_C = vec_add(v_A, v_B);
Vec_store(v_C, C)
…
}

CPU vector code

---

## 7-gpus-optimization.pptx Slide 13: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

13

---

## 7-gpus-optimization.pptx Slide 14: GPU Memories

GPU Memories

---

## 7-gpus-optimization.pptx Slide 15: Memory in the GPU Architecture

Memory in the GPU Architecture

15

…

SM

Core

Control

L2 Cache

Global Memory

Registers

Shared Memory

L1 Cache

Constant Cache

≈1 cycle

≈5 cycles

≈500 cycles

Slide credit: Izzat El Hajj

---

## 7-gpus-optimization.pptx Slide 16: Memory in the GPU Architecture

Memory in the GPU Architecture

16

…

SM

Core

Control

L2 Cache

Global Memory

Registers

Shared Memory

L1 Cache

Constant Cache

≈1 cycle

≈5 cycles

≈500 cycles

Slide credit: Izzat El Hajj

50 MB

80 GB

Direct copy

3 TB/s

Speaker notes: HBM3 memory subsystem provides nearly a 2x bandwidth increase over the previous generation. The H100 SXM5 GPU is the world’s first GPU with HBM3 memory delivering a class-leading 3 TB/sec of memory bandwidth.
50 MB L2 cache architecture caches large portions of models and datasets for repeated access, reducing trips to HBM3.
SM： streaming multiprocessor

---

## 7-gpus-optimization.pptx Slide 17: Example of data movement between GPU global memory (DRAM) and GPU cores.

Example of data movement between GPU global memory (DRAM) and GPU cores.

NVIDIA V100 & A100 Memory Hierarchy

A100 feature:
Direct copy from L2 to scratchpad, bypassing L1 and register file.

17

https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf

Speaker notes: A100: New load instruction that copies from global memory (DRAM) to shared memory (scratchpad) directly, without having to use registers (i.e., no need to copy from global memory to register and then from register to shared memory).

Media/diagram refs: rId3:image:../media/image13.emf

---

## 7-gpus-optimization.pptx Slide 18: CUDA Variable Type Qualifiers

CUDA Variable Type Qualifiers

__device__ is optional when used with __shared__, or  __constant__
Recall cudaMalloc(…) allocates memory from the host
Constant memory can also be allocated and initialized from the host
Automatic variables without any qualifier reside in a register
Except arrays that reside in global memory

TABLE:
Variable declaration | Memory | Scope | Lifetime
int LocalVar; | register | thread | thread
int localArr[N]; | global | thread | thread
__device__ __shared__   int SharedVar; | shared | block | block
__device__              int GlobalVar; | global | grid | application
__device__ __constant__ int ConstantVar; | constant | grid | application

18

---

## 7-gpus-optimization.pptx Slide 19: Memory Hierarchy in CUDA Programs

Memory Hierarchy in CUDA Programs

19

Media/diagram refs: rId2:image:../media/image14.emf

---

## 7-gpus-optimization.pptx Slide 20: Recall: Comparison of Memories

Recall: Comparison of Memories

20

SRAM

HBM

DDR

SSD

DISK

Capacity

Latency

Bandwidth

~10MB

~10GB

~100GB

~1TB

~10TB

~1ns

~100ns

~1us

~1ms

~100GB/s

~10MB/s

~1GB/s

~10GB/s

~1TB/s

---

## 7-gpus-optimization.pptx Slide 21: The DRAM SubsystemThe Top-Down View

The DRAM SubsystemThe Top-Down View

---

## 7-gpus-optimization.pptx Slide 22: DRAM Subsystem Organization

DRAM Subsystem Organization

Channel
DIMM
Rank
Chip
Bank
Row/Column

22

---

## 7-gpus-optimization.pptx Slide 23: The DRAM Subsystem

The DRAM Subsystem

Memory channel

DIMM (Dual in-line memory module)

Processor

“Channel”

23

Media/diagram refs: rId3:image:../media/image16.jpeg; rId2:image:../media/image15.jpeg

---

## 7-gpus-optimization.pptx Slide 24: Breaking down a DIMM (module)

Breaking down a DIMM (module)

DIMM (Dual in-line memory module)

Side view

Front of DIMM

Back of DIMM

Rank 0: collection of 8 chips

Rank 1

24

Media/diagram refs: rId3:image:../media/image17.png; rId2:image:../media/image15.jpeg; rId5:image:../media/image19.png; rId4:image:../media/image18.png

---

## 7-gpus-optimization.pptx Slide 25: Breaking down a Rank

Breaking down a Rank

Rank 0

<0:63>

Chip 0

Chip 1

Chip 7

. . .

<0:7>

<8:15>

<56:63>

Data <0:63>

25

---

## 7-gpus-optimization.pptx Slide 26: Breaking down a Chip

Breaking down a Chip

Chip 0

<0:7>

TABLE:
 |  |  |  |  | 
 |  |  |  |  | 
 |  |  |  |  | 
 |  |  |  |  | 
 |  |  |  |  | 
 |  |  |  |  | 

8 banks

Bank 0

...

26

---

## 7-gpus-optimization.pptx Slide 27: Inside a DRAM Chip

Inside a DRAM Chip

Access
Transistor

Storage
Capacitor

Bitline

Wordline

Subarray
(2D Array of DRAM Cells)

Sense Amplifiers

DRAM Module

DRAM Chips

DRAM Bank

DRAM Cells

8

Row Buffer

Media/diagram refs: rId3:image:../media/image20.png

---

## 7-gpus-optimization.pptx Slide 28: DRAM Bank Operation

DRAM Bank Operation

28

Row Buffer

(Row 0, Column 0)

Row decoder

Column mux

Row address 0

Column address 0

Data

Row 0

Empty

(Row 0, Column 1)

Column address 1

(Row 0, Column 85)

Column address 85

(Row 1, Column 0)

HIT

Row address 1

Row 1

CONFLICT !

Columns

Rows

Access Address:

---

## 7-gpus-optimization.pptx Slide 29: Long Global Memory Access Latency

Long Global Memory Access Latency

---

## 7-gpus-optimization.pptx Slide 30: Motivation of In-network Computing

Motivation of In-network Computing

How to optimize global memory access?

Multithreading

Shared Memory

Memory Coalescing

---

## 7-gpus-optimization.pptx Slide 31: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

31

---

## 7-gpus-optimization.pptx Slide 32: Latency Hiding via Warp-Level FGMT

Latency Hiding via Warp-Level FGMT

Warp: A set of threads that execute the same instruction (on different data elements)
Fine-grained multithreading
One instruction per thread in pipeline at a time (No interlocking)
Interleaving warp execution to hide latencies
Register values of all threads stay in register file
FGMT enables long latency tolerance
Millions of pixels

32

Decode

R

F

A

L

U

D-Cache

Thread Warp 6

Thread Warp 1

Thread Warp 2

Data

All Hit?

Miss?

Warps accessing

memory hierarchy

Thread Warp 3

Thread Warp 8

Writeback

Warps available

for scheduling

Thread Warp 7

I-Fetch

SIMD Pipeline

Slide credit: Tor Aamodt

Speaker notes: With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread’s warp from the pool of “ready” warps and thereby allows other threads to proceed while the memory system processes its request.
 With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.

---

## 7-gpus-optimization.pptx Slide 33: Latency Hiding and Occupancy

Latency Hiding and Occupancy

FGMT can hide long latency operations (e.g., memory accesses)
Occupancy: ratio of active warps to the maximum number of warps per GPU core

4 active warps

2 active warps

33

Media/diagram refs: rId8:image:../media/image27.emf; rId3:image:../media/image22.emf; rId7:image:../media/image26.emf; rId2:image:../media/image21.emf; rId6:image:../media/image25.emf; rId5:image:../media/image24.emf; rId4:image:../media/image23.emf

---

## 7-gpus-optimization.pptx Slide 34: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

34

---

## 7-gpus-optimization.pptx Slide 35: Memory Coalescing (I)

Memory Coalescing (I)

Memory Coalescing：
When threads in the same warp access consecutive memory locations in the same burst, the accesses can be combined and served by one burst
 Only one DRAM transaction is needed.
Memory Divergence：
If threads in the same warp access locations not in the same burst, accesses cannot be combined
Multiple memory transactions are needed
Takes longer to service data to the warp

Slide credit: Izzat El Hajj

35

---

## 7-gpus-optimization.pptx Slide 36: Memory Coalescing:

Memory Coalescing:
When accessing global memory, memory coalescing makes sure that concurrent threads access nearby memory locations
Peak bandwidth utilization occurs when all threads in a warp access one cache line (or several consecutive cache lines)

Md

Nd

W

I

D

T

H

WIDTH

Thread 1

Thread 2

Not coalesced

Coalesced

Memory Coalescing (II)

36

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 37: Uncoalesced Memory Accesses

Uncoalesced Memory Accesses

M2,0

M1,1

M1,0

M0,0

M0,1

M3,0

M2,1

M3,1

M1,2

M0,2

M2,2

M3,2

M1,3

M0,3

M2,3

M3,3

M

T1

T2

T3

T4

Warp 1

Warp 2

Access direction of each thread

…

37

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 38: Coalesced Memory Accesses

Coalesced Memory Accesses

M2,0

M1,1

M1,0

M0,0

M0,1

M3,0

M2,1

M3,1

M1,2

M0,2

M2,2

M3,2

M1,3

M0,3

M2,3

M3,3

M

T1

T2

T3

T4

Warp 1

Warp 2

…

38

Slide credit: Hwu & Kirk

Access direction of each thread

---

## 7-gpus-optimization.pptx Slide 39: Same instruction in different threads uses thread id to index and access different data elements

Same instruction in different threads uses thread id to index and access different data elements

SIMT Memory Access

Let’s assume N=16, 4 threads per warp  4 warps

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

+

Slide credit: Hyesoon Kim

Threads

Data elements

Warp 0

Warp 1

Warp 2

Warp 3

39

---

## 7-gpus-optimization.pptx Slide 40: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

40

---

## 7-gpus-optimization.pptx Slide 41: Shared Memory

Shared Memory

Shared memory is an interleaved (banked) memory
Each bank can service one address per cycle
Typically, 32 banks in NVIDIA GPUs
Successive 32-bit words are assigned to successive banks
Bank = Address % 32
Bank conflicts are only possible within a warp
No bank conflicts between different warps

41

---

## 7-gpus-optimization.pptx Slide 42: Shared Memory Bank Conflicts (I)

Shared Memory Bank Conflicts (I)

Bank conflict free

Bank 15

Bank 7

Bank 6

Bank 5

Bank 4

Bank 3

Bank 2

Bank 1

Bank 0

Thread 15

Thread 7

Thread 6

Thread 5

Thread 4

Thread 3

Thread 2

Thread 1

Thread 0

Linear addressing: stride = 1

Random addressing 1:1

42

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 43: Shared Memory Bank Conflicts (II)

Shared Memory Bank Conflicts (II)

N-way bank conflicts

2-way bank conflict: stride = 2

8-way bank conflict: stride = 8

Thread 11

Thread 10

Thread 9

Thread 8

Thread 4

Thread 3

Thread 2

Thread 1

Thread 0

Bank 15

Bank 7

Bank 6

Bank 5

Bank 4

Bank 3

Bank 2

Bank 1

Bank 0

Thread 15

Thread 7

Thread 6

Thread 5

Bank 9

Bank 8

x8

43

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 44: Use Shared Memory to Improve Coalescing

Use Shared Memory to Improve Coalescing

Md

Nd

W

I

D

T

H

WIDTH

Original

Access

Pattern

Tiled

Copy into

scratchpad

memory

Perform

multiplication

with scratchpad

values

Slide credit: Hwu & Kirk

44

---

## 7-gpus-optimization.pptx Slide 45: Reducing Shared Memory Bank Conflicts

Reducing Shared Memory Bank Conflicts

Bank conflicts are only possible within a warp
No bank conflicts between different warps
If strided accesses are needed, some optimization techniques can help
Padding
Randomized mapping
Rau, “Pseudo-randomly interleaved memory,” ISCA 1991
Hash functions
V.d.Braak+, “Configurable XOR Hash Functions for Banked Scratchpad Memories in GPUs,” IEEE TC, 2016

45

---

## 7-gpus-optimization.pptx Slide 46: No Data Reuse

No Data Reuse

No Data reuse:
Each thread reads its only elements.

for (int i = 0; i < 3; i++){
    for (int j = 0; j < 3; j++){
        sum += gauss[i][j] * Image[(i+row-1)*width + (j+col-1)];
    }
}

46

Loading Amount:
9 elements per thread

Speaker notes: 对每一个row，col,计算一个sum。

Media/diagram refs: rId3:image:../media/image28.emf

---

## 7-gpus-optimization.pptx Slide 47: Data Reuse: Tiling

Data Reuse: Tiling

For data reuse, we divide the input into tiles, each of which loads L_SIZE chunks together into shared memory, then compute together

__shared__ int l_data[(L_SIZE+2)*(L_SIZE+2)];
…
Load tile into shared memory l_data
__syncthreads();
for (int i = 0; i < 3; i++){
  for (int j = 0; j < 3; j++){
    sum += gauss[i][j] * l_data[(i+l_row-1)*(L_SIZE+2)+j+l_col-1];
  }
}

47

Loading Amount:
(L_SIZE+2)2/L_SIZE2
elements per thread

Compute Amount:
The same

Speaker notes: L_SIZE: number of points together…

Media/diagram refs: rId3:image:../media/image29.emf

---

## 7-gpus-optimization.pptx Slide 48: void __syncthreads();

void __syncthreads();
Synchronizes all threads in a block
Once all threads in a block have reached this point, execution resumes normally
Used to avoid RAW / WAR / WAW hazards when accessing shared or global memory

48

Synchronization Function

---

## 7-gpus-optimization.pptx Slide 49: Tiling/Blocking in On-chip Memories

Tiling/Blocking in On-chip Memories

Tiling or Blocking
Divide loops operating on arrays into computation chunks so that each chunk can hold its data in the on-chip RAM (or other on-chip memory, e.g., scratchpad)
Avoids on-chip RAM conflicts between different chunks of computation
Essentially: Divide the working set so that each piece fits in the on-chip RAMs

49

---

## 7-gpus-optimization.pptx Slide 50: CPU: Naïve Matrix Multiplication (I)

CPU: Naïve Matrix Multiplication (I)

Matrix multiplication: C = A x B
Consider two input matrices A and B in row-major layout
A size is M x P
B size is P x N
C size is M x N

50

A

B

C

P

M

N

i

j

k

---

## 7-gpus-optimization.pptx Slide 51: CPU: Naïve Matrix Multiplication (II)

CPU: Naïve Matrix Multiplication (II)

Naïve implementation of matrix multiplication
Poor access locality

51

#define A(i,j) matrix_A[i * P + j]
#define B(i,j) matrix_B[i * N + j]
#define C(i,j) matrix_C[i * N + j]
for (i = 0; i < M; i++){ // i = row index
    for (j = 0; j < N; j++){ // j = column index
        C(i, j) = 0; // Set to zero
        for (k = 0; k < P; k++) // Row x Col
            C(i, j) += A(i, k) * B(k, j);
    }
}

A

B

C

P

M

N

i

j

k

Consecutive accesses to B are far from each other, in different memory lines.
Every access to B is likely to cause a row buffer miss

---

## 7-gpus-optimization.pptx Slide 52: CPU: Tiled Matrix Multiplication (I)

CPU: Tiled Matrix Multiplication (I)

Tiled Matrix Multiplication:
Achieve better on-chip RAM locality by computing on smaller tiles or blocks that fit in the RAMs

52

A

B

C

P

M

N

k

tile_dim

i

j

Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4

---

## 7-gpus-optimization.pptx Slide 53: CPU: Tiled Matrix Multiplication (II)

CPU: Tiled Matrix Multiplication (II)

Tiled implementation operates on submatrices (tiles or blocks) that fit fast RAMs (cache, scratchpad, RF)

53

#define A(i,j) matrix_A[i * P + j]
#define B(i,j) matrix_B[i * N + j]
#define C(i,j) matrix_C[i * N + j]
for (I = 0; I < M; I += tile_dim){
    for (J = 0; J < N; J += tile_dim){
        Set_to_zero(&C(I, J)); // Set to zero
        for (K = 0; K < P; K += tile_dim)
            Multiply_tiles(&C(I, J), &A(I, K), &B(K, J));
    }
}

Multiply small submatrices (tiles or blocks) of size tile_dim x tile_dim

A

B

C

P

M

N

k

tile_dim

i

j

Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4

---

## 7-gpus-optimization.pptx Slide 54: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Matrix-Matrix Multiplication (I)

C = A x B

A

B

C

Slide credit: Izzat El Hajj

54

---

## 7-gpus-optimization.pptx Slide 55: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Matrix-Matrix Multiplication (II)

A

B

C

Parallelization approach: assign one thread to each element in the output matrix (C)

Slide credit: Izzat El Hajj

C = A x B

55

---

## 7-gpus-optimization.pptx Slide 56: GPU: Matrix-Matrix Multiplication (III)

GPU: Matrix-Matrix Multiplication (III)

__global__ void mm_kernel(float* A, float* B, float* C, unsigned int N) {
    unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
    unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
    float sum = 0.0f;
    for(unsigned int i = 0; i < N; ++i) {
        sum += A[row*N + i]*B[i*N + col];
    }
    C[row*N + col] = sum;
}

Slide credit: Izzat El Hajj

56

Media/diagram refs: rId2:image:../media/image30.emf

---

## 7-gpus-optimization.pptx Slide 57: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Reuse in Matrix-Matrix Multiplication (I)

A

B

C

Some of the threads in the same thread block use the same input data

Slide credit: Izzat El Hajj

C = A x B

57

---

## 7-gpus-optimization.pptx Slide 58: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Reuse in Matrix-Matrix Multiplication (II)

A

B

C

Some of the threads in the same thread block use the same input data

Slide credit: Izzat El Hajj

C = A x B

58

---

## 7-gpus-optimization.pptx Slide 59: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Tiled Matrix-Matrix Multiplication (I)

A

B

C

Step 1: Load the first tile of each input matrix to shared memory (each thread loads one element)

Slide credit: Izzat El Hajj

Ctile = Atile1 x Btile1

59

---

## 7-gpus-optimization.pptx Slide 60: TABLE:

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Tiled Matrix-Matrix Multiplication (II)

Ctile += Atile2 x Btile2

Atile2

Btile2

Ctile

Step 2: Each thread computes its partial sum from the tiles in shared memory (threads wait for each other to finish)

Slide credit: Izzat El Hajj

60

---

## 7-gpus-optimization.pptx Slide 61: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Tiled Matrix-Matrix Multiplication (III)

A

B

C

…accumulate the second tile

Slide credit: Izzat El Hajj

Ctile += Atile2 x Btile2

61

---

## 7-gpus-optimization.pptx Slide 62: N

N

TABLE:
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | 

GPU: Tiled Matrix-Matrix Multiplication (IV)

A

B

C

…and accumulate the third tile

Slide credit: Izzat El Hajj

Ctile += Atile3 x Btile3

62

---

## 7-gpus-optimization.pptx Slide 63: GPU: Tiled Matrix-Matrix Multiplication (V)

GPU: Tiled Matrix-Matrix Multiplication (V)

__shared__ float A_s[TILE_DIM][TILE_DIM];
__shared__ float B_s[TILE_DIM][TILE_DIM];
unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
float sum = 0.0f;
for(unsigned int tile = 0; tile < N/TILE_DIM; ++tile) {
    // Load tile to shared memory
    A_s[threadIdx.y][threadIdx.x] = A[row*N + tile*TILE_DIM + threadIdx.x];
    B_s[threadIdx.y][threadIdx.x] = B[(tile*TILE_DIM + threadIdx.y)*N + col];
    __syncthreads();
    // Compute with tile
    for(unsigned int i = 0; i < TILE_DIM; ++i) {
        sum += A_s[threadIdx.y][i]*B_s[i][threadIdx.x];
    }
    __syncthreads();
}
C[row*N + col] = sum;

Declare arrays in shared memory

Threads wait for each other to finish loading before computing

Threads wait for each other to finish computing before loading

Slide credit: Izzat El Hajj

63

---

## 7-gpus-optimization.pptx Slide 64: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

64

---

## 7-gpus-optimization.pptx Slide 65: Threads Can Take Different Paths in Warp-based SIMT

Threads Can Take Different Paths in Warp-based SIMT

Each thread can have conditional control flow instructions
Threads can execute different control flow paths

65

Thread Warp

Common PC

Thread
2

Thread
3

Thread
4

Thread
1

B

C

D

E

F

A

G

Slide credit: Tor Aamodt

---

## 7-gpus-optimization.pptx Slide 66: Control Flow Problem in GPUs/SIMT

Control Flow Problem in GPUs/SIMT

A GPU uses a SIMT pipeline to save area on control logic
Groups scalar threads into warps
Branch divergence occurs when threads inside warps branch to different execution paths

66

Branch

Path A

Path B

Slide credit: Tor Aamodt

---

## 7-gpus-optimization.pptx Slide 67: SIMT Utilization

SIMT Utilization

Intra-warp divergence

Compute(threadIdx.x);
if (threadIdx.x % 2 == 0){
  Do_this(threadIdx.x);
}
else{
  Do_that(threadIdx.x);
}

67

Media/diagram refs: rId2:image:../media/image31.emf

---

## 7-gpus-optimization.pptx Slide 68: Increasing SIMT Utilization

Increasing SIMT Utilization

Divergence-free execution

Compute(threadIdx.x);
if (threadIdx.x < 32){
  Do_this(threadIdx.x * 2);
}
else{
  Do_that((threadIdx.x%32)*2+1);
}

68

Media/diagram refs: rId2:image:../media/image32.emf

---

## 7-gpus-optimization.pptx Slide 69: Vector Reduction: Naïve Mapping (I)

Vector Reduction: Naïve Mapping (I)

0

1

2

3

4

5

7

6

10

9

8

11

0+1

2+3

4+5

6+7

10+11

8+9

0...3

4..7

8..11

0..7

8..15

iterations

Thread 0

Thread 8

Thread 2

Thread 4

Thread 6

Thread 10

69

Slide credit: Hwu & Kirk

…

---

## 7-gpus-optimization.pptx Slide 70: Vector Reduction: Naïve Mapping (II)

Vector Reduction: Naïve Mapping (II)

Program with low SIMD utilization

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = 1; stride < blockDim.x; stride *= 2) {
  __syncthreads();
  if (t % (2*stride) == 0)
    partialSum[t] += partialSum[t + stride];
}

70

---

## 7-gpus-optimization.pptx Slide 71: Divergence-Free Mapping (I)

Divergence-Free Mapping (I)

All active threads belong to the same warp

Thread 0

0

1

2

3

…

13

15

14

18

17

16

19

0+16

15+31

Thread 1

Thread 2

Thread 14

Thread 15

iterations

71

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 72: Divergence-Free Mapping (II)

Divergence-Free Mapping (II)

Program with high SIMD utilization

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = blockDim.x; stride > 0;  stride >> 1){
  __syncthreads();
  if (t < stride)
    partialSum[t] += partialSum[t + stride];
}

72

---

## 7-gpus-optimization.pptx Slide 73: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

73

---

## 7-gpus-optimization.pptx Slide 74: Atomic Operations

Atomic Operations

---

## 7-gpus-optimization.pptx Slide 75: Atomic Operations (I)

Atomic Operations (I)

CUDA provides atomic instructions on shared memory and global memory
They perform read-modify-write operations atomically
Arithmetic functions
Add, sub, max, min, exch, inc, dec, CAS
int atomicAdd(int*, int);
Bitwise functions
And, or, xor
Datatypes: int, uint, ull, float (half, single, double)*

75

Pointer to shared memory or global memory

Value to add

Return value (old value)

* Datatypes for different atomic operations in https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#atomic-functions

---

## 7-gpus-optimization.pptx Slide 76: Atomic operations serialize the execution if there are atomic conflicts

Atomic operations serialize the execution if there are atomic conflicts

Atomic Operations (II)

tbase

tconflict

Shared memory

No atomic conflict = concurrent updates

Atomic conflict = serialized updates

76

Media/diagram refs: rId3:image:../media/image34.emf; rId7:image:../media/image38.emf; rId2:image:../media/image33.emf; rId6:image:../media/image37.emf; rId5:image:../media/image36.emf; rId4:image:../media/image35.emf

---

## 7-gpus-optimization.pptx Slide 77: Uses of Atomic Operations

Uses of Atomic Operations

Use atomic operations to prevent data races when more than one thread need to update the same memory location
Computation
Atomics on an array that will be the output of the kernel
Example
Histogram, reduction
Synchronization
Atomics on memory locations that are used for synchronization or coordination
Example
Counters, locks, flags…

77

---

## 7-gpus-optimization.pptx Slide 78: Histograms are widely used in image processing

Histograms are widely used in image processing
Some computation before voting in the histogram may be needed
Parallel threads frequently incur atomic conflicts in image histogram computation

For (each pixel i in image I){
Pixel = I[i]			// Read pixel
Pixel’ = Computation(Pixel)	// Optional computation
Histogram[Pixel’]++		// Vote in histogram bin
}

Image Histogram

78

Media/diagram refs: rId2:image:../media/image39.emf

---

## 7-gpus-optimization.pptx Slide 79: Agenda for Today

Agenda for Today

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

79

---

## 7-gpus-optimization.pptx Slide 80: Asynchronous Data Transfers between CPU and GPU

Asynchronous Data Transfers between CPU and GPU

---

## 7-gpus-optimization.pptx Slide 81: CUDA Streams

CUDA Streams

CUDA streams (command queues in OpenCL)
Sequence of operations that are performed in order
1. Data transfer CPU-GPU
2. Kernel execution
D input data instances, B blocks
#Streams: (D / #Streams) data instances, (B / #Streams) blocks
3. Data transfer GPU-CPU

81

Speaker notes: Computation is divided such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.

Media/diagram refs: rId3:image:../media/image40.emf

---

## 7-gpus-optimization.pptx Slide 82: Asynchronous Transfers between CPU & GPU

Asynchronous Transfers between CPU & GPU

Computation divided into #Streams
D input data instances, B blocks
#Streams
D/#Streams data instances
B/#Streams blocks
Estimates

tE >= tT (dominant kernel)

tT > tE (dominant transfers)

82

Default stream

Several streams

Speaker notes: Computation is divided such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.

Media/diagram refs: rId3:image:../media/image40.emf; rId5:image:../media/image93.png; rId4:image:../media/image80.png

---

## 7-gpus-optimization.pptx Slide 83: 83

83

Overlap of Data Transfers and Kernel Execution

// Create streams
int number_of_streams = 32;
cudaStream_t stream[number_of_streams]; // Stream declaration
for(int i = 0; i < number_of_streams; ++i)
    cudaStreamCreate(&stream[i]); // Stream creation
// CPU-GPU data transfers
for (int i = 0; i < number_of_streams; ++i)
    cudaMemcpyAsync(inputDevPtr + i * size, hostPtr + i * size, size,
                    cudaMemcpyHostToDevice, stream[i]);
// Kernel launches
for (int i = 0; i < number_of_streams; ++i)
    MyKernel<<<num_blocks / number_of_streams, num_threads, 0, stream[i]>>>
                              (outputDevPtr + i * size, inputDevPtr + i * size, size);
// GPU-CPU data transfers
for (int i = 0; i < number_of_streams; ++i)
    cudaMemcpyAsync(hostPtr + i * size, outputDevPtr + i * size, size,
                    cudaMemcpyDeviceToHost, stream[i]);
cudaDeviceSynchronize(); // Explicit synchronization
// Destroy streams
for (int i = 0; i < number_of_streams; ++i)
    cudaStreamDestroy(stream[i]); // Stream destruction

Code for devices that do not support concurrent data transfers

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

Check CUDA programming guide
https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#streams

---

## 7-gpus-optimization.pptx Slide 84: Applications with independent computation on different data instances can benefit from asynchronous transfers

Applications with independent computation on different data instances can benefit from asynchronous transfers
For instance, video processing

Use Case: Video Processing

84

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

Speaker notes: A number b of blocks per frame executes.
Data transfers are overlapped with computation. Thus, some time can be saved.

Media/diagram refs: rId3:image:../media/image41.emf

---

## 7-gpus-optimization.pptx Slide 85: Asynchronous memory copy with LDGSTS instruction vs. TMA

Asynchronous memory copy with LDGSTS instruction vs. TMA

NVIDIA H100 Tensor Memory Accelerator

85

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

TMA unit reduces addressing overhead
A single thread per warp issues the TMA operation
Support for different tensor layouts (1D-5D)

Speaker notes: New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can transfer large blocks of data efficiently between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.
New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can efficiently transfer large blocks of data between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.

Media/diagram refs: rId5:image:../media/image43.jpg; rId4:image:../media/image42.jpg

---

## 7-gpus-optimization.pptx Slide 86: State-of-the-art CPU GPU and FPGA

State-of-the-art CPU GPU and FPGA

TABLE:
 | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network
CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), / 1.4 (FP64) | 512GB / (80GB/s) | 32.0GB/s / (PCIe 4.0 X16) | No
GPU (Nvidia A100) | 8192 (128K) | 19.5 (FP32), / 9.7 (FP64), / 156 (FP32, Tensor), / 312 (FP16, Tensor) | 40/80GB / (1935GB/s) | 32.0GB/s / (PCIe 4.0 X16) | No
FPGA (U280) | 9,024 / (25x18 MULs) | 1.8 (FP32) | 40GB / (460GB/s) | 16.0GB/s / (PCIe 4.0 X8) | Yes

Speaker notes: KB MB GB TB
K M B T E P
1B=10亿

---

## 7-gpus-optimization.pptx Slide 87: Limitation of GPU

Limitation of GPU

87

CPU

GPU

PCIe

32.0GB/s

1935GB/s

Media/diagram refs: rId3:image:../media/image4.png; rId2:image:../media/image44.png

---

## 7-gpus-optimization.pptx Slide 88: 88

88

Serial Code of Prefix sum:

GPU Code of Prefix sum:
    Multi-pass (ISSUE)

Limitation of GPU

// Fills prefix sum array
void fillPrefixSum(int arr[], int n, int prefixSum[])
{ prefixSum[0] = arr[0];
  // Adding present element
  for (int i = 1; i < n; i++)
   prefixSum[i] = prefixSum[i-1] + arr[i]; }

Media/diagram refs: rId3:image:../media/image45.jpeg

---

## 7-gpus-optimization.pptx Slide 89: Nvidia’s Success: Transparent Scalability

Nvidia’s Success: Transparent Scalability

Hardware is free to schedule thread blocks

Device

Block 0

Block 1

Block 2

Block 3

Block 4

Block 5

Block 6

Block 7

Kernel grid

Each block can execute in any order relative to other blocks.

time

89

Slide credit: Hwu & Kirk

Gen 1

Gen 2

The CUDA code stays the same and enjoys performance improvement while GPU hardware evolves.

Speaker notes: Thread block is the key innovation to scale-up GPU architecture. The software code stays the same and enjoys performance speedup while GPU hardware evolves.

---

## 7-gpus-optimization.pptx Slide 90: Key Messages:

Key Messages:

Programming model is the key success of Nvidia, rather than the GPU itself.
GPU has an order of magnitude higher memory bandwidth and compute power than CPU.
Offloading a task to GPU pays off only when the task has enough compute intensity.
AI task needs compute-intensive accelerators, e.g., GPU and AI processor.

90

---

## 7-gpus-optimization.pptx Slide 91: Prog. Model 3: Multithreaded

Prog. Model 3: Multithreaded

91

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

load

add

store

Iter. 1

Iter. 2

Realization: Each iteration is independent
Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)

This programming model (software) is called:
SPMD: Single Program Multiple Data

Executed on a SIMT machine (hardware)
Single Instruction Multiple Thread

---

## 7-gpus-optimization.pptx Slide 92: A GPU is a SIMD (SIMT) Machine

A GPU is a SIMD (SIMT) Machine

Except it is not programmed using SIMD instructions
It is programmed using threads (SPMD programming model)
Each thread executes the same code but operates a different piece of data
Each thread has its own context (i.e., can be treated/restarted/executed independently)
A set of threads executing the same instruction are dynamically grouped into a warp (wavefront) by the hardware
A warp is essentially a SIMD operation formed by hardware!

92

---

## 7-gpus-optimization.pptx Slide 93: SIMD vs. SIMT Execution Model

SIMD vs. SIMT Execution Model

SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
[VLD, VLD, VADD, VST], VLEN
SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
[LD, LD, ADD, ST], NumThreads
Two Major SIMT Advantages:
Can treat each thread separately  i.e., can execute each thread independently on any type of scalar pipeline
Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

93

---

## 7-gpus-optimization.pptx Slide 94: Brief Review of GPU Architecture (I)

Brief Review of GPU Architecture (I)

Streaming Processor Array
Tesla architecture (G80/GT200)

94

Media/diagram refs: rId2:image:../media/image46.emf

---

## 7-gpus-optimization.pptx Slide 95: Brief Review of GPU Architecture (II)

Brief Review of GPU Architecture (II)

Streaming Multiprocessors (SM)
Streaming Processors (SP)
Blocks are divided into warps
SIMD unit (32 threads)

…

t0 t1 t2 … t31

Block 0’s warps

Block 1’s warps

Block 2’s warps

95

NVIDIA Fermi architecture

Media/diagram refs: rId2:image:../media/image47.emf

---

## 7-gpus-optimization.pptx Slide 96: Brief Review of GPU Architecture (III)

Brief Review of GPU Architecture (III)

Streaming Multiprocessors (SM) or Compute Units (CU)
SIMD pipelines
Streaming Processors (SP) or CUDA ”cores”
Vector lanes
Number of SMs x SPs across generations
Tesla (2007): 30 x 8
Fermi (2010): 16 x 32
Kepler (2012): 15 x 192
Maxwell (2014): 24 x 128
Pascal (2016): 56 x 64
Volta (2017): 80 x 64

96

---

## 7-gpus-optimization.pptx Slide 97: Graphics Processing UnitsSIMD not Exposed to Programmer (SIMT)

Graphics Processing UnitsSIMD not Exposed to Programmer (SIMT)

---

## 7-gpus-optimization.pptx Slide 98: SIMD vs. SIMT Execution Model

SIMD vs. SIMT Execution Model

SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
[VLD, VLD, VADD, VST], VLEN
SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
[LD, LD, ADD, ST], NumThreads
Two Major SIMT Advantages:
Can treat each thread separately  i.e., can execute each thread independently (on any type of scalar pipeline)  MIMD processing
Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

98

---

## 7-gpus-optimization.pptx Slide 99: High-Level View of a GPU

High-Level View of a GPU

99

Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

Media/diagram refs: rId2:image:../media/image48.png

---

## 7-gpus-optimization.pptx Slide 100: Latency Hiding via Warp-Level FGMT

Latency Hiding via Warp-Level FGMT

Warp: A set of threads that execute the same instruction (on different data elements)
Fine-grained multithreading
No interlocking: One instruction per thread in pipeline at a time.
Interleave warp execution to hide latencies
Register values of all threads stay in register file
FGMT enables long latency tolerance
Millions of pixels

100

Decode

R

F

A

L

U

D-Cache

Thread Warp 6

Thread Warp 1

Thread Warp 2

Data

All Hit?

Miss?

Warps accessing

memory hierarchy

Thread Warp 3

Thread Warp 8

Writeback

Warps available

for scheduling

Thread Warp 7

I-Fetch

SIMD Pipeline

Slide credit: Tor Aamodt

Speaker notes: With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread’s warp from the pool of “ready” warps and thereby allows other threads to proceed while the memory system processes its request.
 With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.

---

## 7-gpus-optimization.pptx Slide 101: Warp Execution (Recall the Slide)

Warp Execution (Recall the Slide)

101

32-thread warp executing ADD A[tid],B[tid]  C[tid]

C[1]

C[2]

C[0]

A[3]

B[3]

A[4]

B[4]

A[5]

B[5]

A[6]

B[6]

Execution using one pipelined functional unit

C[4]

C[8]

A[12]

B[12]

A[16]

B[16]

A[20]

B[20]

A[24]

B[24]

C[5]

C[9]

A[13]

B[13]

A[17]

B[17]

A[21]

B[21]

A[25]

B[25]

C[6]

C[10]

A[14]

B[14]

A[18]

B[18]

A[22]

B[22]

A[26]

B[26]

C[7]

C[11]

C[3]

A[15]

B[15]

A[19]

B[19]

A[23]

B[23]

A[27]

B[27]

Execution using four pipelined functional units

Slide credit: Krste Asanovic

Time

Space

---

## 7-gpus-optimization.pptx Slide 102: 102

102

Lane

Functional Unit

Registers
for each
Thread

Memory Subsystem

Registers for thread IDs
0, 4, 8, …

Registers for thread IDs
1, 5, 9, …

Registers for thread IDs
2, 6, 10, …

Registers for thread IDs
3, 7, 11, …

Slide credit: Krste Asanovic

SIMD Execution Unit Structure

---

## 7-gpus-optimization.pptx Slide 103: CPU threads and GPU kernels

CPU threads and GPU kernels
Sequential or modestly parallel sections on CPU
Massively parallel sections on GPU: Blocks of threads

Serial Code (host)

. . .

Parallel Kernel (device)
KernelA<<<nBlk, nThr>>>(args);

Parallel Kernel (device)
KernelB<<<nBlk, nThr>>>(args);

Warps not Exposed to GPU Programmers

103

Slide credit: Hwu & Kirk

---

## 7-gpus-optimization.pptx Slide 104: From Blocks to Warps

From Blocks to Warps

GPU cores: SIMD pipelines
Streaming Multiprocessors (SM)
Streaming Processors (SP)
Blocks are divided into warps
SIMD unit (32 threads)

…

t0 t1 t2 … t31

Block 0’s warps

Block 1’s warps

Block 2’s warps

104

NVIDIA Fermi architecture

Media/diagram refs: rId2:image:../media/image47.emf

---

## 7-gpus-optimization.pptx Slide 105: SPMD

SPMD

Single procedure/program, multiple data
This is a programming model rather than computer organization
Each processing element executes the same procedure, except on different data elements
Procedures can synchronize at certain points in program, e.g. barriers
Essentially, multiple instruction streams execute the same program
Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
Modern GPUs programmed in a similar way on a SIMD hardware

105

---

## 7-gpus-optimization.pptx Slide 106: Dynamic Warp Formation/Merging

Dynamic Warp Formation/Merging

Idea: Dynamically merge threads executing the same instruction (after branch divergence)
Form new warps from warps that are waiting
Enough threads branching to each path enables the creation of full new warps

106

Warp X

Warp Y

Warp Z

---

## 7-gpus-optimization.pptx Slide 107: Dynamic Warp Formation/Merging

Dynamic Warp Formation/Merging

Idea: Dynamically merge threads executing the same instruction (after branch divergence)
Fung et al., “Dynamic Warp Formation and Scheduling for Efficient GPU Control Flow,” MICRO 2007.

107

Branch

Path A

Path B

---

## 7-gpus-optimization.pptx Slide 108: Dynamic Warp Formation Example

Dynamic Warp Formation Example

108

A

B

G

C

D

E

F

Time

x/1111

y/1111

x/1110

y/0011

x/1000

y/0010

x/0110

y/0001

x/0001

y/1100

A new warp created from scalar threads of both Warp x and y executing at Basic Block D

Execution of Warp x

at Basic Block A

Execution of Warp y

Legend

Baseline

Dynamic
Warp
Formation

Slide credit: Tor Aamodt

---

## 7-gpus-optimization.pptx Slide 109: Hardware Constraints Limit Flexibility of Warp Grouping

Hardware Constraints Limit Flexibility of Warp Grouping

109

Lane

Functional Unit

Registers
for each
Thread

Memory Subsystem

Registers for thread IDs
0, 4, 8, …

Registers for thread IDs
1, 5, 9, …

Registers for thread IDs
2, 6, 10, …

Registers for thread IDs
3, 7, 11, …

Slide credit: Krste Asanovic

---

## 7-gpus-optimization.pptx Slide 110: Clarification of Some GPU Terms

Clarification of Some GPU Terms

110

TABLE:
Generic Term | NVIDIA Term | AMD Term | Comments
Vector length | Warp size | Wavefront size | Number of threads that run in parallel (lock-step) on a SIMD functional unit
Pipelined functional unit / / Scalar pipeline | Streaming processor / / CUDA core | - | Functional unit that executes instructions for one GPU thread
SIMD functional unit / / SIMD pipeline | Group of N streaming processors (e.g., N=8 in GTX 285, N=16 in Fermi) | Vector ALU | SIMD functional unit that executes instructions for an entire warp
GPU core | Streaming multiprocessor | Compute unit | It contains one or more warp schedulers and one or several SIMD pipelines

---

## 7-gpus-optimization.pptx Slide 111: Programming Model vs. Hardware Execution Model

Programming Model vs. Hardware Execution Model

111

Hardware Programming Model

Programming Model

Core

Streaming
 Multi-processor

GPU

CUDA core:

Thread

Thread block (s)

Wrap

Thread blocks

---

## 7-gpus-optimization.pptx Slide 112: NVIDIA H100 Block Diagram

NVIDIA H100 Block Diagram

144 cores on the full GH100
60MB L2 cache

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

112

Media/diagram refs: rId4:image:../media/image49.png

---

## 7-gpus-optimization.pptx Slide 113: NVIDIA H100 Core

NVIDIA H100 Core

48 TFLOPS Single Precision*
24 TFLOPS Double Precision*
800 TFLOPS (FP16, Tensor Cores)*

113

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
* Preliminary performance estimates

Media/diagram refs: rId5:image:../media/image51.jpg; rId4:image:../media/image50.png

---

## 7-gpus-optimization.pptx Slide 114: Shared memory virtual address space distributed across the blocks of a cluster

Shared memory virtual address space distributed across the blocks of a cluster
Load, store, and atomic operations to other SM’s shared memory

NVIDIA H100 Distributed Shared Memory

114

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

Thread block clusters and distributed shared memory (DSMEM) are leveraged via cooperative_groups API
TMA unit supports copies across thread blocks in a cluster
Asynchronous transaction barriers

Speaker notes: Distributed shared memory allows direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks.
Distributed shared memory enables direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks

Media/diagram refs: rId4:image:../media/image52.jpg

---

## 7-gpus-optimization.pptx Slide 115: 7 versions in CUDA samples: Tree-based reduction in shared memory

7 versions in CUDA samples: Tree-based reduction in shared memory
Version 0: No whole warps active
Version 1: Contiguous threads, but many bank conflicts
Version 2: No bank conflicts
Version 3: First level of reduction when reading from global memory
Version 4: Warp shuffle or unrolling of final warp
Version 5: Warp shuffle or complete unrolling
Version 6: Multiple elements per thread sequentially

Optimized Parallel Reduction

https://docs.nvidia.com/cuda/cuda-samples/index.html#cuda-parallel-reduction
Harris, “Optimizing Parallel Reduction in CUDA,” https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf

115

---

## 7-gpus-optimization.pptx Slide 116: 3 new versions of reduction based on 3 previous versions

3 new versions of reduction based on 3 previous versions
Version 0: No whole warps active
Version 3: First level of reduction when reading from global memory
Version 6: Multiple elements per thread sequentially
New versions 7, 8, and 9
Replace the for loop (tree-based reduction) with one shared memory atomic operation per thread

Reduction with Atomic Operations

116

---

## 7-gpus-optimization.pptx Slide 117: 256-bin histogram calculation

256-bin histogram calculation

Video Processing: Performance Results (I)

117

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

44%

21%

Media/diagram refs: rId3:image:../media/image53.emf

---

## 7-gpus-optimization.pptx Slide 118: RGB-to-grayscale conversion

RGB-to-grayscale conversion

Video Processing: Performance Results (II)

118

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

63%

18%

Media/diagram refs: rId3:image:../media/image54.emf

---

## 7-gpus-optimization.pptx Slide 119: Performance Considerations

Performance Considerations

Main bottlenecks
CPU-GPU data transfers
Global memory access
Memory access
Latency hiding
Occupancy
Memory coalescing
Data reuse
Shared memory usage
SIMD (Warp) Utilization: Divergence
Other considerations
Atomic operations: Serialization
Data transfers between CPU and GPU
Overlap of communication and computation

119

---

## 7-gpus-optimization.pptx Slide 120: Recommended Readings

Recommended Readings

Hwu and Kirk, “Programming Massively Parallel Processors,” Third Edition, 2017
Chapter 5: Performance considerations
Chapter 18 - Programming
a heterogeneous computing cluster,
Section 18.5

120

Media/diagram refs: rId3:image:../media/image55.tiff

---
