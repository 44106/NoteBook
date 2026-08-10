# 16_overview (DESKTOP-H8IOQ49's conflicted copy 2025-06-11).pptx

- Slides: 176

## Slide 1: Computer Arch. & AI Chip and SystemsLecture 16: Overview

### Extracted Shape Text
- Computer Arch. & AI Chip and SystemsLecture 16: Overview
- Prof. Zeke Wang
- Zhejiang University
- 9 June 2025

### Notes
- 1

## Slide 2: Position of Systems

- Images: 1; Tables: 0

### Extracted Shape Text
- Position of Systems
- Application
- System (TensorFlow) &
- Hardware (AI Chip)

### Notes
- 2
- One more tip: which company earn the most money from the AI surge? Nvidia.

## Slide 3: Directly Talk About AI Chip and System?

### Extracted Shape Text
- Directly Talk About AI Chip and System?
- No, most of you do not take computer architecture course!
- Our course also includes computer architecture!

### Notes
- The majority of you will not work on Systems.
- But you should know the key principles that help you understand the system on which your AI task runs.
- Our course has to include both computer architecture and AI chip courses.
- 3

## Slide 4: Why Do We Have Computers?

### Extracted Shape Text
- Why Do We Have Computers?

## Slide 5: Answer

### Extracted Shape Text
- Answer
- To Solve Problems

## Slide 6: How Does a Computer Solve Problems?

### Extracted Shape Text
- How Does a Computer Solve Problems?

## Slide 7: Answer

### Extracted Shape Text
- Answer
- Orchestrating Electrons
- In today’s dominant technologies

## Slide 8: How Do Problems Get Solved by Electrons?

### Extracted Shape Text
- How Do Problems Get Solved by Electrons?

## Slide 9: The Transformation Hierarchy

### Extracted Shape Text
- The Transformation Hierarchy
- Micro-architecture
- SW/HW Interface
- Program/Language
- Algorithm
- Problem
- Logic
- Devices
- System Software
- Electrons
- Computer Architecture (narrow view)
- Computer Architecture (expanded view)

## Slide 10: Axiom

### Extracted Shape Text
- Axiom
- To achieve the highest energy efficiency and performance:
- we must take the expanded view
- of computer architecture
- Micro-architecture
- SW/HW Interface
- Program/Language
- Algorithm
- Problem
- Logic
- Devices
- System Software
- Electrons
- Co-design across the hierarchy:
- Algorithms to devices
- Specialize as much as possible
- within the design goals

## Slide 11: Why AI Systems?

### Extracted Shape Text
- Why AI Systems?
- 1, 卡脖子问题
- 2, More Design Space Exploration: Algorithm & Systems.

### Notes
- 11

## Slide 12: Topics of Computer Arch. and AI Chip

- Images: 1; Tables: 0

### Extracted Shape Text
- Topics of Computer Arch. and AI Chip

## Slide 13: Things Every Programmer Should know

### Extracted Shape Text
- Things Every Programmer Should know
- Amdhal Law
- A formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.
- Roofline Model
- Theoretical performance bound of your application running on your machine.
- Little’s Law: L = λ *W  (buffer size = throughput * latency)
- A theorem by John Little which states that the long-term average number L of customers in a stationary system is equal to the long-term average effective arrival rate λ multiplied by the average time W that a customer spends in the system.

### Notes
- 13

## Slide 14: Amdahl’s Law

### Extracted Shape Text
- Amdahl’s Law
- Amdahl’s Law
- f: Parallelizable fraction of a program
- N: Number of processors
- Serial bottleneck of Amdahl’s Law:
- Maximum speedup (1/(1-f)) limited by serial portion (1 - f)
- Parallel portion (f) is usually not perfectly parallel
- Synchronization overhead (e.g., updates to shared data)
- Load imbalance overhead (imperfect parallelization)
- Resource sharing overhead (contention among N processors)
- Speedup =
- 1
- +
- 1 - f
- f
- N
- Amdahl, “Validity of the single processor approach to achieving large scale computing capabilities,” 1967.

## Slide 15: Things Every Programmer Should know

### Extracted Shape Text
- Things Every Programmer Should know
- Amdhal Law
- A formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.
- Roofline Model
- Theoretical performance bound of your application running on your machine.
- Little’s Law: L = λ *W  (buffer size = throughput * latency)
- A theorem by John Little which states that the long-term average number L of customers in a stationary system is equal to the long-term average effective arrival rate λ multiplied by the average time W that a customer spends in the system.

### Notes
- 15

## Slide 16: Why Roofline Model

### Extracted Shape Text
- Why Roofline Model
- Why Roofline Model?
- 1, computing regime: Latency-limited  throughput-limited
- Original latency-oriented performance model does not work
- 2, Target processor’s perspective
- Showing inherent hardware limitations (or bound), in term of compute and memory
- 3, Compute kernel’s perspective
- Showing the priority of optimizations for a given compute kernel running on a given processor
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 16

## Slide 17: Key Term in Roofline Model

### Extracted Shape Text
- Key Term in Roofline Model
- Arithmetic intensity (AI)
- Definition: AI = Total Flops / Total Memory Bytes
- Arithmetic intensity describes the characteristics of a compute kernel running on a given processor
- Large AI  Compute-bound
- Small AI  Memory-bound
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 17

## Slide 18: Roofline Model’s Roof

### Extracted Shape Text
- Roofline Model’s Roof
- Roofline model’s Roofline:
- Application execution monitoring: arithmetic intensity;
- Machine characterization: memory bandwidth, peak compute;
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 18

## Slide 19: How to Compute Roofline

### Extracted Shape Text
- How to Compute Roofline
- Roofline model indicates the performance of an application is bounded by compute or memory
- Attainable Flop/s = min( peak Flop/s, AI * peak GB/s )
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Memory-bound
- Compute-bound

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 19

## Slide 20: How to Compute Roofline

### Extracted Shape Text
- How to Compute Roofline
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Memory-bound
- Compute-bound

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 20

## Slide 21: Compute Roofline Model

### Extracted Shape Text
- Compute Roofline Model
- Compute roofline model:
- No vectorization: none
- Vec: vectorization code
- Peak Flop/s: fused multiply-add + vectorization code
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Vec
- No vectorization

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 21

## Slide 22: HBM GB/s

### Extracted Shape Text
- HBM GB/s
- Memory Roofline Model
- Memory Roofline Model:
- DRAM: limited memory bandwidth;
- HBM: medium memory bandwidth;
- Cache: large memory bandwidth
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
- Cache GB/s

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 22

## Slide 23: Roofline Model: Examples

### Extracted Shape Text
- Roofline Model: Examples
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
- 7-point constant coefficient stencil :
- Type: short
- Memory: 16 Bytes/iteration
- Compute: 7 flops/iteration
- Arithmetic Intensity: 0.4375 flops/byte
- #pragma omp parallel for
- for(i=0;i<N;i++){
- Z[i] = X[i] + alpha*Y[i];
- }
- #pragma omp parallel for
- for(k=1;k<dim+1;k++){
- for(j=1;j<dim+1;j++){
- for(i=1;i<dim+1;i++){
- int ijk = i + j*jStride + k*kStride;
- new[ijk] = -6.0*old[ijk ]
- + old[ijk-1 ]
- + old[ijk+1 ]
- + old[ijk-jStride]
- + old[ijk+jStride]
- + old[ijk-kStride]
- + old[ijk+kStride];
- }}}
- STREAM Triad:
- Type: double
- Memory: 24 Bytes/iteration
- Compute: 2 flops/iteration
- Arithmetic Intensity: 0.083 flops/byte

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 23

## Slide 24: Roofline Model: Examples

### Extracted Shape Text
- Roofline Model: Examples
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
- Peak Flop/s
- Attainable Flop/s
- DRAM GB/s
- 7-point
- Stencil
- Gflop/s ≤ AI * DRAM GB/s
- TRIAD
- Arithmetic Intensity (Flop:Byte)
- 0.083
- 0.44

### Notes
- 24

## Slide 25: 9

### Extracted Shape Text
- 9
- You’re required to evaluate the performance of three operators (Conv, FC and Attention) on an AI processor.
- The chip manufacturer provides an empty roofline chart as below:
- Performance benchmark results of the three operators are given as follow:
- The operator Conv has 10000 operations (OPs) per 1000-byte memory access and achieves 5.8 TOP/s on the AI processor.
- The operator FC has 30000 operations (OPs) per 1000-byte memory access and achieves 7.9 TOP/s on the AI processor.
- The operator Attention has 50000 operations (OPs) per 1000-byte memory access and achieves 6.1 TOP/s on the AI processor.
- (a) Please calculate theoretical computing throughput and memory bandwidth of the processor.
- (b) Please place each operator onto the roofline chart given above.
- (c) Among the three operators, which operators are almost fully optimized and which are not? Please give the reason.
- (d) Which operators are memory-bound and which are compute-bound? Please give the reason.
- (e) If there exists another implementation of the Conv operator where computing units finish convolution in fewer clock cycles, will its throughput become higher or not? Please give the reason.

### Notes
- 25

## Slide 26: OpenAI: Compute Power Needed by NN Model

- Images: 0; Tables: 1

### Extracted Shape Text
- OpenAI: Compute Power Needed by NN Model

| Model | Model Size | Compute/iteration
(OPs) |
| --- | --- | --- |
| VGG 19 | 114M | ~19.6 B |
| “GPT-3” | 175B | ~250 T |

- One Forward Pass of Model:

### Notes
- 26
- KB MB GB TB
- K M B T
- 1B=10
- 亿

## Slide 27: OpenAI: Compute Needed by Whole Pre-training Model

- Images: 1; Tables: 1

### Extracted Shape Text
- OpenAI: Compute Needed by Whole Pre-training Model

| Model | Model Size | Compute
(Petaflop/s-days) | Compute
(OPs) |
| --- | --- | --- | --- |
| GPT-3 Small | 125M | ~3 | ~3*10^20 |
| GPT-3 2.7B | 2.7B | ~80 | ~8*10^21 |
| “GPT-3” | 175B | ~3100 | ~3.1*10^23 |

- Brown, Language Models are Few-Shot Learners, 2020

### Notes
- 27
- KB MB GB TB
- K M B T E P
- 1B=10
- 亿

## Slide 28: State-of-the-art CPU GPU and FPGA

- Images: 0; Tables: 1

### Extracted Shape Text
- State-of-the-art CPU GPU and FPGA
- Brown, Language Models are Few-Shot Learners, 2020

|  | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network |
| --- | --- | --- | --- | --- | --- |
| CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), 
1.4 (FP64) | 512GB (80GB/s) | 32.0GB/s (PCIe 4.0 X16) | No |
| GPU (Nvidia A100) | 8192 (128K) | 19.5 (FP32),
9.7 (FP64),
156 (FP32, Tensor),
312 (FP16, Tensor) | 40/80GB (1935GB/s) | 32.0GB/s (PCIe 4.0 X16) | No |
| FPGA (U280) | 9,024 
(25x18 MULs) | 1.8 (FP32) | 40GB (460GB/s) | 16.0GB/s (PCIe 4.0 X8) | Yes |


### Notes
- 28
- KB MB GB TB
- K M B T E P
- 1B=10
- 亿

## Slide 29: Things Every Programmer Should know

### Extracted Shape Text
- Things Every Programmer Should know
- Amdhal Law
- A formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.
- Roofline Model
- Theoretical performance bound of your application running on your machine.
- Little’s Law: L = λ *W  (buffer size = throughput * latency)
- A theorem by John Little which states that the long-term average number L of customers in a stationary system is equal to the long-term average effective arrival rate λ multiplied by the average time W that a customer spends in the system.

### Notes
- 29

## Slide 30: Little’s Law：Intuition

- Images: 1; Tables: 0

### Extracted Shape Text
- Little’s Law：Intuition
- Image the services provided by counters in the bank.
- Arrival rate: one customer/min;
- Counter’s average serve time: 6 mins;
- Question: how many counters are needed for people who need the service? (Cond: The customer will leave if no counter is available. )
- Answer: 6 counters (one slot for one person, then no customer will leave).
- How many counters?
- Arrival rate: one person/min
- Average service time: 6 mins

### Notes
- 这里server不太合理
- 30

## Slide 31: Little’s Law Used in Memory Subsystem

### Extracted Shape Text
- Little’s Law Used in Memory Subsystem
- Little’s law is widely used in hardware design whose latency is larger than one cycle, e.g., memory subsystem:
- Throughput: 12GB/s;
- Latency: 100ns;
- Buffer Size (concurrency): 100ns * 12GB/s = 120B
- Memory
- Throughput: 12GB/s
- Latency: ~100ns
- Buffer
- Concurrency = Latency * Throughput

## Slide 32: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 33: The von Neumann Model

- Images: 1; Tables: 0

### Extracted Shape Text
- The von Neumann Model
- In order to build a computer, we need an execution model for processing computer programs
- John von Neumann proposed a fundamental model in 1946
- von Neumann Model consists of 5 components
- Memory (stores the program and data)
- Processing unit
- Input
- Output
- Control unit (controls the order in which instructions are carried out)
- Throughout this lecture, we will examine one example of the von Neumann model
- MIPS
- Burks, Goldstein, von Neumann,
- “Preliminary discussion of the logical design
- of an electronic computing instrument,” 1946.

## Slide 34: von Neumann Model: Two Key Properties

### Extracted Shape Text
- von Neumann Model: Two Key Properties
- Von Neumann model is also called stored program computer (instructions in memory). It has two key properties:
- Stored program
- Instructions stored in a linear memory array
- Memory is unified between instructions and data
- The interpretation of a stored value depends on the control signals
- Sequential instruction processing
- One instruction processed (fetched, executed, completed) at a time
- Program counter (instruction pointer) identifies the current instruction
- Program counter is advanced sequentially except for control transfer instructions

### Notes
- Every application can be descripted by this complete design von Neumann
- 34

## Slide 35: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 36: A Single-Cycle MicroarchitectureA Closer Look

### Extracted Shape Text
- A Single-Cycle MicroarchitectureA Closer Look

## Slide 37: Single-cycle Machine

### Extracted Shape Text
- Single-cycle Machine
- AS
- Sequential
- Logic
- (State)
- Combinational
- Logic
- AS’
- AS: Architectural State

## Slide 38: A Very Basic Instruction Processing Engine

### Extracted Shape Text
- A Very Basic Instruction Processing Engine
- Each instruction takes a single clock cycle to execute.
- Only combinational logic is used to implement instruction execution.
- No intermediate, programmer-invisible state updates
- AS = Architectural (programmer visible) state
- at the beginning of a clock cycle
- Process instruction in one clock cycle
- AS’ = Architectural (programmer visible) state
- at the end of a clock cycle

## Slide 39: Multi-Cycle Microarchitectures

### Extracted Shape Text
- Multi-Cycle Microarchitectures

## Slide 40: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 41: Multi-Cycle Microarchitectures

### Extracted Shape Text
- Multi-Cycle Microarchitectures
- Goal: Let each instruction take (close to) only as much time it really needs
- Idea of multi-cycle CPU:
- Decrease clock cycle time
- Each instruction takes as many clock cycles as it needs to take
- Multiple state transitions per instruction
- The states followed by each instruction is different

## Slide 42: The “Process Instruction” Step of Multi-Cycle CPU

### Extracted Shape Text
- The “Process Instruction” Step of Multi-Cycle CPU
- ISA specifies abstractly what AS’ should be, given an instruction and AS
- It defines an abstract finite state machine where
- State = programmer-visible state
- Next-state logic = instruction execution specification
- From ISA point of view, there are no “intermediate states” between AS and AS’ during instruction execution
- One state transition per instruction
- Microarchitecture implements how AS is transformed to AS’
- We can have programmer-invisible state to optimize the speed of instruction execution: multiple state transitions per instruction
- Single-cycle: AS  AS’ (transform AS to AS’ in a single clock cycle)
- Multi-cycle: AS  AS+MS1  AS+MS2  AS+MS3  AS’ (take multiple clock cycles to transform AS to AS’)

## Slide 43: Multi-Cycle Microarchitecture

### Extracted Shape Text
- Multi-Cycle Microarchitecture
- AS = Architectural (programmer visible) state
- at the beginning of an instruction
- Step 1: Process part of instruction in one clock cycle
- Step 2: Process part of instruction in the next clock cycle
- …
- AS’ = Architectural (programmer visible) state
- at the end of a clock cycle

## Slide 44: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 45: Can We Use the Idle Hardware to Improve Concurrency?

### Extracted Shape Text
- Can We Use the Idle Hardware to Improve Concurrency?
- Goal: More concurrency  Higher instruction throughput (i.e., more “work” completed in one cycle)
- Key Idea: When an instruction is using some resources in its processing phase, process other instructions on idle resources not needed by that instruction
- E.g., when an instruction is being decoded, fetch the next instruction
- E.g., when an instruction is being executed, decode another instruction
- E.g., when an instruction is accessing data memory (ld/st), execute the next instruction
- E.g., when an instruction is writing its result into the register file, access data memory for the next instruction

## Slide 46: Pipelining: Basic Idea

### Extracted Shape Text
- Pipelining: Basic Idea
- More systematically:
- Pipeline the execution of multiple instructions
- Analogy: “Assembly line processing” of instructions
- Idea of pipelining:
- Divide the instruction processing cycle into distinct “stages” of processing
- Ensure enough hardware resources to process one instruction in each stage
- Process a different instruction in each stage
- Instructions consecutive in program order are processed in consecutive stages
- Benefit: Increases instruction processing throughput (1/CPI)

## Slide 47: Example: Execution of Four Independent ADDs

### Extracted Shape Text
- Example: Execution of Four Independent ADDs
- Multi-cycle: 4 cycles per instruction
- Pipelined: 4 cycles per 4 instructions (steady state)
- Time
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- F
- D
- E
- W
- Time
- 1 instruction completed per cycle

### Notes
- No, multi-cycle execution, unpredictable memory access cycles
- 47

## Slide 48: Data Dependences

### Extracted Shape Text
- Data Dependences
- Types of data dependences
- Flow dependence (read after write – true data dependence)
- Output dependence (write after write)
- Anti dependence (write after read)
- Which ones cause stalls in a pipelined machine?
- Our goal: we need to ensure semantics of the program is correct.
- Flow dependences always need to be obeyed because they constitute true dependence on a register
- Anti and output dependences exist due to limited number of architectural registers.
- Essentially, insns are dependent on a name, not a value.

## Slide 49: Data Dependence Types

### Extracted Shape Text
- Data Dependence Types
- Flow dependence
- r3  r1 op r2 Read-after-Write
- r5  r3 op r4 (RAW)
- Anti dependence
- r3  r1 op r2 Write-after-Read
- r1  r4 op r5 (WAR)
- Output-dependence
- r3  r1 op r2 Write-after-Write
- r5  r3 op r4 (WAW)
- r3  r6 op r7

## Slide 50: Reorder Buffer: For False Dependencies

### Extracted Shape Text
- Reorder Buffer: For False Dependencies
- Output and anti dependences are not true dependences
- WHY? The same register refers to values that have nothing to do with each other
- They exist due to lack of register ID’s (i.e. names) in the ISA
- This eliminates anti and output dependences
- Gives the illusion that there are a large number of registers
- HOW: The register ID is renamed to the reorder buffer entry that will hold the register’s value
- Register ID  ROB entry ID
- Architectural register ID  Physical register ID
- After renaming, ROB entry ID used to refer to the register

## Slide 51: Reorder Buffer: For False Dependencies

### Extracted Shape Text
- Reorder Buffer: For False Dependencies
- Flow dependence
- r3  r1 op r2 Read-after-Write
- r5  r3 op r4 (RAW)
- Anti dependence
- r3  r1 op r2 Write-after-Read
- r1  r4 op r5 (WAR)
- Output-dependence
- r3  r1 op r2 Write-after-Write
- r5  r3 op r4 (WAW)
- r3  r6 op r7
- RB100
- RB100
- RB101
- RB102

## Slide 52: In-Order Pipeline with Reorder Buffer

### Extracted Shape Text
- In-Order Pipeline with Reorder Buffer
- Decode (D): Access regfile/ROB, allocate entry in ROB, check if instruction can execute, if so dispatch instruction
- Execute (E): Instructions can complete out-of-order
- Completion (R): Write result to reorder buffer
- Retirement/Commit (W): Check for exceptions; if none, write result to architectural register file or memory; else, flush pipeline and start from exception handler
- In-order dispatch/execution, out-of-order completion, in-order retirement
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- R

## Slide 53: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 54: Recall: Data Dependence Types

### Extracted Shape Text
- Recall: Data Dependence Types
- Flow dependence
- r3  r1 op r2 Read-after-Write
- r5  r3 op r4 (RAW)
- Anti dependence
- r3  r1 op r2 Write-after-Read
- r1  r4 op r5 (WAR)
- Output-dependence
- r3  r1 op r2 Write-after-Write
- r5  r3 op r4 (WAW)
- r3  r6 op r7

## Slide 55: How Can We Do Better?

### Extracted Shape Text
- How Can We Do Better?
- What do the following two pieces of code have in common (with respect to execution in the previous design)?
- Answer: First ADD stalls the whole pipeline!
- ADD cannot dispatch because its source registers unavailable
- Later independent instructions cannot get executed
- How are the above code portions different?
- Answer: Load latency is variable (unknown until runtime)
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9
- LD R3  R1 (0)
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9

## Slide 56: Preventing Dispatch Stalls

### Extracted Shape Text
- Preventing Dispatch Stalls
- Problem: in-order dispatch (scheduling, or execution)
- Solution: out-of-order dispatch (scheduling, or execution)
- Goal of out-of-order dispatch:
- Like Dataflow, “fire” an instruction only when its inputs are ready
- LD R3  R1 (0)
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9
- The insn “ADD R3…” will not impede insns “ADD R4…, IMUL R5…, ADD R7…”.

## Slide 57: Out-of-order Execution (Dynamic Scheduling)

### Extracted Shape Text
- Out-of-order Execution (Dynamic Scheduling)
- Idea: Move the dependent instructions out of the way of independent ones (s.t. independent ones can execute)
- Rest areas for dependent instructions: Reservation stations
- Monitor the source “values” of each instruction in the resting area
- When all source “values” of an instruction are available, “fire” (i.e. dispatch) the instruction
- Instructions dispatched in dataflow (not control-flow) order
- Benefit:
- Latency tolerance: Allows independent instructions to execute and complete in the presence of a long-latency operation

### Notes
- O
- ne road with multiple ways…
- 57

## Slide 58: Tomasulo’s Algorithm for OoO Execution

### Extracted Shape Text
- Tomasulo’s Algorithm for OoO Execution
- OoO with register renaming invented by Robert Tomasulo
- Used in IBM 360/91 Floating Point Units
- Read: Tomasulo, “An Efficient Algorithm for Exploiting Multiple Arithmetic Units,” IBM Journal of R&D, Jan. 1967.
- OoO variants are used in most high-performance processors
- Initially in Intel Pentium Pro, AMD K5
- Alpha 21264, MIPS R10000, IBM POWER5, IBM z196, Oracle UltraSPARC T4, ARM Cortex A15, Apple M1, …

### Notes
- 360 is not commercially suceesful, without precious exception
- 58

## Slide 59: Two Humps in a Modern Pipeline

### Extracted Shape Text
- Two Humps in a Modern Pipeline
- Hump 1: Reservation station (scheduling window)
- Hump 2: Reorder Buffer ( aka instruction window or active window)
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- E
- O
- R
- D
- E
- R
- S
- C
- H
- E
- D
- U
- L
- E
- TAG and VALUE Broadcast Bus
- in order
- out of order
- in order

## Slide 60: In-order vs. Out-of-order Dispatch

### Extracted Shape Text
- In-order vs. Out-of-order Dispatch
- In order dispatch + precise exceptions:
- Out-of-order dispatch + precise exceptions:
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R1  R6, R7
- IMUL R5  R6, R8
- ADD R7  R3, R5
- F
- D
- W
- E
- E
- E
- E
- R
- F
- D
- E
- R
- W
- F
- D
- E
- R
- W
- F
- D
- E
- R
- W
- F
- D
- E
- R
- W
- STALL
- STALL
- E
- E
- E
- E
- STALL
- F
- D
- W
- E
- E
- E
- E
- R
- F
- D
- E
- R
- W
- F
- D
- E
- R
- F
- D
- E
- E
- E
- E
- R
- W
- F
- D
- E
- R
- W
- WAIT
- WAIT
- W
- 16 cycles
- 12 cycles

## Slide 61: This problem deals with a processor with out-of-order dispatch and precise exception with 1 adder and 1 multiplier. The 

### Extracted Shape Text
- This problem deals with a processor with out-of-order dispatch and precise exception with 1 adder and 1 multiplier. The adder has a two-cycle latency and is fully pipelined, while the multiplier has a four-cycle latency and is fully pipelined. Consider the following instruction sequence:
- I1 ADD $s3, $s1, $s2
- I2 IMUL $s4, $s1, $s3
- I3 IMUL $s1, $s3, $s4
- I4 ADD $s4, $s5, $s3
- I5 IMUL $s6, $s4, $s5
- [2 points] Give an example of write-after-write (WAW) hazard from the instruction sequence. What’s the solution to this hazard?
- Draw a dataflow graph for the instruction sequence. An example is given as follows.
- MUL $s3, $s1, $s2
- ADD $s5, $s3, $s4
- ×
- $s1
- $s2
- +
- $s4
- $s3
- $s5

## Slide 62: Please draw your own graph below.

- Images: 0; Tables: 2

### Extracted Shape Text

| Cycle | 1 | 2 | 3 | 4 | 5 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | F | D | E | E | R | W |  |  |  |  |  |  |  |  |  |  |  |  |
| I2 |  | F | D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I3 |  |  | F | D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I4 |  |  |  | F | D |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I5 |  |  |  |  | F | D |  |  |  |  |  |  |  |  |  |  |  |  |


| Cycle | 1 | 2 | 3 | 4 | 5 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| I5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

- Please draw your own graph below.
- Simulate the instruction execution procedure. Complete the state of each instruction at each cycle in the following table. Use F, D, E, R and W to represent IF, ID, EXE, reorder buffer and WB stage. Use “－” to represent waiting state. You are not required to use all columns in the table.
- (d) Given a processor with in-order dispatch without reorder buffer, while instruction sequence and computing units keep the same, how many cycles does the in-order processor take to finish the procedure? Please give your analysis. Note that precise exception should still be guaranteed here.

## Slide 63: Performance Analysis

### Extracted Shape Text
- Performance Analysis
- Execution time of a single instruction
- {CPI} x {clock cycle time}
- Execution time of an entire program
- Sum over all instructions [{CPI} x {clock cycle time}]
- {# of instructions} x {Average CPI} x {clock cycle time}
- Single-cycle microarchitecture performance
- CPI = 1
- Clock cycle time = long
- Multi-cycle microarchitecture performance
- CPI = different for each instruction
- Average CPI  hopefully small
- Clock cycle time = short
- CPI: Cycles Per Instruction

## Slide 64: P is a multi-cycle processor with a clock cycle of 2ns. Under ideal conditions (with a hit rate of 100%), P executes a l

### Extracted Shape Text
- P is a multi-cycle processor with a clock cycle of 2ns. Under ideal conditions (with a hit rate of 100%), P executes a load instruction in 4 cycles, a store instruction in 6 cycles, an arithmetic instruction in 2 cycles, and a branch instruction in 3 cycles.
- Let's consider an application called A with 20% of the instructions being load instructions, 10% being store instructions, 50% being arithmetic instructions, and 20% being branch instructions.
- (a) What is the CPI when running application A on processor P under ideal conditions?
- (b) P’s memory access time for a miss is 100ns, while the hit time is 1 clock cycle. The cache is direct-mapped cache, it has a miss rate of 1.4%. What is the average memory access time of P?
- (c) each instruction of application A requires an average of 1.3 memory accesses, and A has 100 instructions. What is the CPU time of process P to run application A, taking into account cache misses?
- (d) Replace the cache of P1 with a 2-way set-associative cache. It has a miss rate of 1.0%. Due to the existence of multi-way selection, the CPU clock cycle increases to 1.05 times of the original. Which caching method has faster execution time for application A?

## Slide 65: Flynn’s Taxonomy of Computers

### Extracted Shape Text
- Flynn’s Taxonomy of Computers
- Mike Flynn, “Very High-Speed Computing Systems,” Proc. of IEEE, 1966
- SISD: Single instruction operates on single data element
- SIMD: Single instruction operates on multiple data elements
- Array processor
- Vector processor
- MISD: Multiple instructions operate on single data element
- Closest form: systolic array processor, streaming processor
- MIMD: Multiple instructions operate on multiple data elements (multiple instruction streams)
- Multiprocessor
- Multithreaded processor

### Notes
- Flynn:
- 弗林
- 65

## Slide 66: Intuition of SIMD Capability

### Extracted Shape Text
- Intuition of SIMD Capability
- 计算任务 (A[6:0] + B[6:0])
- Scalar: 一个周期完成一个加法
- SIMD : 一个周期完成多个加法
- +
- t0
- A[0]
- B[0]
- t1
- A[1]
- B[1]
- t2
- A[2]
- B[2]
- t3
- A[3]
- B[3]
- t4
- A[4]
- B[4]
- t5
- A[5]
- B[5]
- t6
- A[6]
- B[6]
- t1
- A[4]
- B[4]
- A[5]
- B[5]
- A[6]
- B[6]
- +
- +
- +
- +
- t0
- A[0]
- B[0]
- A[1]
- B[1]
- A[2]
- B[2]
- A[3]
- B[3]
- Scalar
- SIMD

## Slide 67: GPUs are SIMD Engines Underneath

### Extracted Shape Text
- GPUs are SIMD Engines Underneath
- The instruction pipeline operates like a SIMD pipeline (e.g., an array processor)
- However, the programming is done using threads, NOT SIMD instructions
- To understand this, let’s go back to our parallelizable code example
- But, before that, let’s distinguish between
- Programming Model (Software)
- vs.
- Execution Model (Hardware)

## Slide 68: Programming Model vs. Hardware Execution Model

### Extracted Shape Text
- Programming Model vs. Hardware Execution Model
- Programming Model： how the programmer expresses the code
- E.g., Sequential (von Neumann), Data Parallel (SIMD), Dataflow, Multi-threaded (MIMD, SPMD), …
- Hardware Execution Model： how the hardware executes the code underneath
- E.g., Out-of-order execution, Vector processor, Array processor, Dataflow processor, Multiprocessor, Multithreaded processor, …
- Execution Model can be very different from Programming Model
- E.g., von Neumann model implemented by an OoO processor
- E.g., SPMD model implemented by a SIMD processor (a GPU)

## Slide 69: NVIDIA A100

- Images: 1; Tables: 0

### Extracted Shape Text
- NVIDIA A100
- NVIDIA-speak:
- 6912 stream processors
- “SIMT execution”
- Generic speak:
- 108 cores
- 64 SIMD functional units per core
- Tensor cores for Machine Learning
- Support for sparsity
- New floating point data type (TF32)
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

### Notes
- 5 HBM2 stacks, 10 512-bit memory controllers
- Sparsity is possible in deep learning because the importance of individual weights evolves during the learning process, and by the end of network training, only a subset of weights have acquired a meaningful purpose in determining the learned output. The remaining weights are no longer needed (see
- https://
- developer.nvidia.com
- /blog/
- nvidia
- -ampere-architecture-in-depth/
- ).
- TensorFloat-32 (TF32) uses 8 bit for exponent and 10 bits for mantissa. This way, TF32 provides the range of FP32 with the precision of FP16
- (see
- 69

## Slide 70: NVIDIA A100 Block Diagram

- Images: 1; Tables: 0

### Extracted Shape Text
- NVIDIA A100 Block Diagram
- 108 cores on the A100
- (Up to 128 cores in the full-blown chip)
- 40MB L2 cache
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/

### Notes
- The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2
- cache.The
- L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see
- https://
- developer.nvidia.com
- /blog/
- nvidia
- -ampere-architecture-in-depth/
- ).
- 70

## Slide 71: A GPU is a SIMD (SIMT) Machine

### Extracted Shape Text
- A GPU is a SIMD (SIMT) Machine
- Except it is not programmed using SIMD instructions
- It is programmed using threads (SPMD programming model)
- Each thread executes the same code but operates a different piece of data
- Each thread has its own context (i.e., can be treated/restarted/executed independently)
- A set of threads executing the same instruction are dynamically grouped into a warp (wavefront) by the hardware
- A warp is essentially a SIMD operation formed by hardware!

## Slide 72: Warp-based SIMD vs. Traditional SIMD

### Extracted Shape Text
- Warp-based SIMD vs. Traditional SIMD
- Traditional SIMD contains a single thread
- Sequential instruction execution; lock-step operations in a SIMD instruction
- Programming model is SIMD (no extra threads)  SW needs to know vector length
- ISA contains vector/SIMD instructions
- Warp-based SIMD consists of multiple scalar threads executing in a SIMD manner (i.e., same instruction executed by all threads)
- Does not have to be lock step
- Each thread can be treated individually (i.e., placed in a different warp)  programming model not SIMD
- SW does not need to know vector length
- Enables multithreading and flexible dynamic grouping of threads
- ISA is scalar  SIMD operations can be formed dynamically
- Essentially, it is SPMD programming model implemented on SIMD hardware

## Slide 73: Control Flow Problem in GPUs/SIMT

### Extracted Shape Text
- Control Flow Problem in GPUs/SIMT
- A GPU uses a SIMD pipeline to save area on control logic
- Groups scalar threads into warps
- Branch divergence occurs when threads inside warps branch to different execution paths
- Branch
- Path A
- Path B
- Branch
- Path A
- Path B
- Slide credit: Tor Aamodt
- This is the same as conditional/predicated/masked execution.

### Notes
- 73

## Slide 74: Nvidia’s Success: Transparent Scalability

### Extracted Shape Text
- Nvidia’s Success: Transparent Scalability
- Hardware is free to schedule thread blocks
- Device
- Block 0
- Block 1
- Block 2
- Block 3
- Block 4
- Block 5
- Block 6
- Block 7
- Kernel grid
- Block 0
- Block 1
- Block 2
- Block 3
- Block 4
- Block 5
- Block 6
- Block 7
- Device
- Block 0
- Block 1
- Block 2
- Block 3
- Block 4
- Block 5
- Block 6
- Block 7
- Each block can execute in any order relative to other blocks.
- time
- Slide credit: Hwu & Kirk
- time
- Gen 1
- Gen 2
- The CUDA code stays the same and enjoys performance improvement while GPU hardware evolves.

### Notes
- Thread block is the key innovation to scale-up GPU architecture. T
- h
- e software code stays the same and enjoys performance speedup while GPU hardware evolves.
- 74

## Slide 75: Memory Is Very Important

### Extracted Shape Text
- Memory Is Very Important

### Notes
- 75

## Slide 76: Idealism

### Extracted Shape Text
- Idealism
- Instruction
- Supply
- Pipeline
- (Instruction
- execution)
- Data
- Supply
- - Zero latency access
- - Infinite capacity
- - Zero cost
- - Perfect control flow
- No pipeline stalls
- Perfect data flow
- (reg/memory dependencies)
- Zero-cycle interconnect
- (operand communication)
- Enough functional units
- Zero latency compute
- Zero latency access
- Infinite capacity
- - Infinite bandwidth
- Zero cost

## Slide 77: DRAM Capacity, Bandwidth & Latency

### Extracted Shape Text
- DRAM Capacity, Bandwidth & Latency
- 128x
- 20x
- 1.3x

### Notes
- 77

## Slide 78: FF vs. SRAM vs. DRAM vs. Others

### Extracted Shape Text
- FF vs. SRAM vs. DRAM vs. Others
- Flip-Flops
- Very fast, parallel access
- Very expensive (one bit costs tens of transistors)
- Static RAM
- Relatively fast, only one data word at a time
- Expensive (one bit costs 6+ transistors)
- Dynamic RAM
- Slower, one data word at a time, reading destroys content (refresh), needs special process for manufacturing
- Cheap (one bit costs only one transistor plus one capacitor)
- Other storage technology (flash memory, hard disk, tape)
- Much slower, access takes a long time, non-volatile
- Very cheap (one transistor stores 16 bits or no transistors involved)

### Notes
- 78

## Slide 79: The DRAM Subsystem

- Images: 5; Tables: 0

### Extracted Shape Text
- The DRAM Subsystem
- Memory channel
- Memory channel
- DIMM (Dual in-line memory module)
- Processor
- “Channel”

## Slide 80: Breaking down a DIMM (module)

- Images: 4; Tables: 0

### Extracted Shape Text
- Breaking down a DIMM (module)
- DIMM (Dual in-line memory module)
- Side view
- Front of DIMM
- Back of DIMM

## Slide 81: Breaking down a DIMM (module)

- Images: 4; Tables: 0

### Extracted Shape Text
- Breaking down a DIMM (module)
- DIMM (Dual in-line memory module)
- Side view
- Front of DIMM
- Back of DIMM
- Rank 0: collection of 8 chips
- Rank 1

## Slide 82: Rank

### Extracted Shape Text
- Rank
- Rank 0 (Front)
- Rank 1 (Back)
- Data <0:63>
- CS <0:1>
- Addr/Cmd
- <0:63>
- <0:63>
- Memory channel

## Slide 83: Breaking down a Rank

### Extracted Shape Text
- Breaking down a Rank
- Rank 0
- <0:63>
- Chip 0
- Chip 1
- Chip 7
- . . .
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>

## Slide 84: Breaking down a Chip

- Images: 0; Tables: 2

### Extracted Shape Text
- Breaking down a Chip
- Chip 0
- <0:7>

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

- 8 banks
- Bank 0
- <0:7>
- <0:7>
- <0:7>
- ...
- <0:7>

## Slide 85: Breaking down a Bank

- Images: 0; Tables: 1

### Extracted Shape Text
- Breaking down a Bank
- Bank 0
- <0:7>
- row 0
- row 32k-1
- ...
- 2kB
- 1B
- 1B (column)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

- 1B
- Row-buffer
- 1B
- ...
- <0:7>

## Slide 86: Three DRAM Access States

### Extracted Shape Text
- Three DRAM Access States
- Page Hit:
- Occurs when a memory transaction accesses a row that is open in its bank, so no Precharge and Activate commands are required before the column access, resulting in minimum latency.
- Page Closed:
- Occurs when a memory transaction accesses a row whose corresponding bank is closed, so the row Activate command is required before the column access.
- Page Miss:
- Occurs when a memory transaction accesses a row that does not match the active row in the bank, so one Precharge command and one Activate command are issued before the column access, resulting in maximum latency.

## Slide 87: DRAM Refresh

### Extracted Shape Text
- DRAM Refresh
- DRAM capacitor charge leaks over time
- The memory controller needs to refresh each row periodically to restore charge
- Activate each row every N ms
- Typical N = 64 ms
- Downsides of refresh:
- -- Energy consumption: Each refresh consumes energy
- -- Performance degradation: DRAM rank/bank unavailable while refreshed
- -- QoS/predictability impact: (Long) pause times during refresh
- -- Refresh rate limits DRAM capacity scaling

## Slide 88: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 89: The Problem of Ideal Memory

### Extracted Shape Text
- The Problem of Ideal Memory
- Bigger is slower
- SRAM, 512 Bytes, sub-nanosec
- SRAM, KByte~MByte, ~nanosec
- DRAM, Gigabyte, ~50 nanosec
- PCM-DIMM (Intel Optane DC DIMM), Gigabyte, ~200 nanosec
- PCM-SSD (Intel Optane SSD), Gigabyte, ~10 µs
- Flash memory, Gigabyte~Terabyte, ~100 µs
- Hard Disk, Terabyte, ~10 millisec
- Faster is more expensive (dollars and chip area)
- SRAM, < 0.3$ per Megabyte
- DRAM, < 0.03$ per Megabyte
- PCM-DIMM (Intel Optane DC DIMM), < 0.004$ per Megabyte
- PCM-SSD, < 0.001$ per Megabyte
- Flash memory, < 0.00008$ per Megabyte
- Hard Disk, < 0.00003$ per Megabyte

### Notes
- 89

## Slide 90: Memory Hierarchy

### Extracted Shape Text
- Memory Hierarchy
- Fundamental tradeoff
- Fast memory: small
- Large memory: slow
- Idea: Memory hierarchy.
- Latency, cost, size,
- bandwidth
- CPU
- Main
- Memory
- (DRAM)
- RF
- Cache
- Hard Disk

## Slide 91: The Memory Hierarchy

### Extracted Shape Text
- The Memory Hierarchy
- fast
- small
- large but slow
- move what you use here
- backup
- everything
- here
- With good locality of reference, memory appears as fast as
- and as large as
- faster per byte
- cheaper per byte

## Slide 92: Why Cache Works? Locality

### Extracted Shape Text
- Why Cache Works? Locality
- Locality: One’s recent past is a very good predictor of his/her near future.
- Temporal Locality: If you just did something, it is very likely that you will do the same thing again soon
- since you are here today, there is a good chance you will be here again and again regularly
- Spatial Locality: If you did something, it is very likely you will do something similar/related (in space)
- every time I find you in this room, you are probably sitting close to the same people

## Slide 93: Caching Basics: Exploit Temporal Locality

### Extracted Shape Text
- Caching Basics: Exploit Temporal Locality
- Idea: Store recently accessed data in automatically-managed fast memory (called cache)
- Anticipation: same mem. location will be accessed again soon
- Temporal locality principle
- Recently accessed data will be again accessed in the near future
- This is what Maurice Wilkes had in mind:
- “The use is discussed of a fast core memory of, say 32000 words as a slave to a slower core memory of, say, one million words in such a way that in practical cases the effective access time is nearer that of the fast memory than that of the slow memory.”
- Wilkes, “Slave Memories and Dynamic Storage Allocation,” IEEE Trans. On Electronic Computers, 1965.

## Slide 94: Caching Basics: Exploit Spatial Locality

### Extracted Shape Text
- Caching Basics: Exploit Spatial Locality
- Idea: Store data in addresses adjacent to the recently accessed one in automatically-managed fast memory
- Logically divide memory into equal-size blocks
- Fetch to cache the accessed block in its entirety
- Anticipation: nearby memory locations will be accessed soon
- Spatial locality principle
- Nearby data in memory will be accessed in the near future
- E.g., sequential instruction access, array traversal
- This is what IBM 360/85 implemented
- 16 Kbyte cache with 64 byte blocks
- Liptay, “Structural aspects of the System/360 Model 85 II: the cache,” IBM Systems Journal, 1968.

## Slide 95: Caching Basics

### Extracted Shape Text
- Caching Basics
- Cache Block (line): Unit of storage in the cache
- Memory is logically divided into blocks that map to potential locations in the cache.
- On a reference:
- HIT: If in cache, use cached data instead of accessing memory
- MISS: If not in cache, bring block into cache
- May have to evict some other block
- For high cache hit rate, important cache design decisions:
- Placement: where and how to place/find a block in cache?
- Replacement: what data to remove to make room in cache?
- Granularity of management: large or small blocks? Subblocks?
- Write policy: what do we do about writes?
- Instructions/data: do we treat them separately?

## Slide 96: Cache: Placement

- Images: 1; Tables: 0

### Extracted Shape Text
- Cache: Placement
- A key question: How to map chunks of the main memory address space to blocks in the cache?
- Which location in cache can a given “main memory chunk” be placed in?

## Slide 97: Three Cache Organization Methods

- Images: 1; Tables: 0

### Extracted Shape Text
- Three Cache Organization Methods
- Direct-mapped:
- A chunk can go to only one cache block in the cache. (Another extreme)
- Fully-associative:
- A chunk can go to any cache block in the cache. (One extreme)
- Set-associative:
- A chunk can go to N cache blocks in the N-way set-associative cache. (Best choice)
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014

## Slide 98: Set-Associative Cache

### Extracted Shape Text
- Set-Associative Cache
- A block can be placed in any of N blocks of N-way set-associative cache
- Example of 2-way cache:
- Instead of having one column of 8, have 2 columns of 4 blocks
- 2-way Set-Associative Cache: Structure
- Tag store
- Data store
- V
- tag
- =?
- V
- tag
- =?
- Address:
- tag
- index
- byte in block
- 3 bits
- 2 bits
- 3 bits
- Logic
- MUX
- MUX
- byte in block
- 2-way SET
- Hit?

## Slide 99: 4-way Set Associativity

### Extracted Shape Text
- 4-way Set Associativity
- 4-way
- + Likelihood of conflict misses even lower
- -- More tag comparators and wider data mux; larger tags
- Tag store
- Data store
- =?
- =?
- =?
- =?
- MUX
- MUX
- byte in block
- Logic
- Hit?
- Address
- tag
- index
- byte in block
- 3 bits
- 1 b
- 4 bits

## Slide 100: Set-Associative Cache

### Extracted Shape Text
- Set-Associative Cache
- Key Idea: Associative memory within the set
- Advantage of Set-Associative Cache
- Accommodates conflicts better (fewer conflict misses)
- Assume addresses A and B have the same index bits but different tag bits
- A, B, A, B, A, B, A, B, …  store in the cache set
- All accesses are cache hit
- Issue of Set-Associative Cache
- More complex, slower access, larger tag store
- Set-Associative Cache: Advantage and Issue

## Slide 101: Caching Basics

### Extracted Shape Text
- Caching Basics
- Cache Block (line): Unit of storage in the cache
- Memory is logically divided into blocks that map to potential locations in the cache.
- On a reference:
- HIT: If in cache, use cached data instead of accessing memory
- MISS: If not in cache, bring block into cache
- May have to evict some other block
- For high cache hit rate, important cache design decisions:
- Placement: where and how to place/find a block in cache?
- Replacement: what data to remove to make room in cache?
- Granularity of management: large or small blocks? Subblocks?
- Write policy: what do we do about writes?
- Instructions/data: do we treat them separately?

## Slide 102: Replacement in Set-Associative Caches

### Extracted Shape Text
- Replacement in Set-Associative Caches
- Key Challenge:
- Which cache block in a set be replaced once new block comes?

## Slide 103: Cache Block Replacement Policy

### Extracted Shape Text
- Cache Block Replacement Policy
- Which block in the set to replace on a cache miss?
- 1, Any invalid block first
- 2, If all are valid, consult the replacement policy:
- Random
- FIFO
- Least recently used (how to implement?)
- Hybrid replacement policies
- Optimal replacement policy?

## Slide 104: Caching Basics

### Extracted Shape Text
- Caching Basics
- Cache Block (line): Unit of storage in the cache
- Memory is logically divided into blocks that map to potential locations in the cache.
- On a reference:
- HIT: If in cache, use cached data instead of accessing memory
- MISS: If not in cache, bring block into cache
- May have to evict some other block
- For high cache hit rate, important cache design decisions:
- Placement: where and how to place/find a block in cache?
- Replacement: what data to remove to make room in cache?
- Granularity of management: large or small blocks? Subblocks?
- Write policy: write-allocate, write-back/write-through
- Instructions/data: do we treat them separately?

## Slide 105: Cache Policies: Handling Memory Write

### Extracted Shape Text
- Cache Policies: Handling Memory Write
- Where should you write the result of a store? One policy for each step.
- Step 1: if not in cache, either policy works:
- Write-allocate policy (default):
- Allocate the cache line (put it in the cache).
- Issue: Read an entire cache block from memory
- Write-no-allocate policy (PCIe/IO):
- Write it directly to memory without allocation in cache.
- Ignore cache.
- Step 2: if in the cache, either policy works:
- Write-back policy (default):
- writes it to the cache and wait until we kick the cache block out
- Write-through policy (streaming write instruction):
- Writes it to the cache and memory right away

### Notes
- 4 combinations…
- 105

## Slide 106: Cache: Write-back vs. Write-through

### Extracted Shape Text
- Cache: Write-back vs. Write-through
- Write-back:
- Write goes to cache; cache writes to main memory (evicted)
- + Can combine multiple writes to the same block before eviction
- Potentially saves bandwidth between cache levels + saves energy
- -- Need a bit in the tag store indicating the block is “dirty/modified”
- Write-through:
- Write goes to memory and cache
- + Simpler
- + Evictions do not need to write to memory
- + All levels are up to date
- Consistency: Simpler cache coherence because no need to check close-to-processor caches’ tag stores for presence
- -- More memory bandwidth intensive; no combining of writes

## Slide 107: Caching Basics

### Extracted Shape Text
- Caching Basics
- Cache Block (line): Unit of storage in the cache
- Memory is logically divided into blocks that map to potential locations in the cache.
- On a reference:
- HIT: If in cache, use cached data instead of accessing memory
- MISS: If not in cache, bring block into cache
- May have to evict some other block
- For high cache hit rate, important cache design decisions:
- Placement: where and how to place/find a block in cache?
- Replacement: what data to remove to make room in cache?
- Granularity of management: large or small blocks? Subblocks?
- Write policy: what do we do about writes?
- Instructions/data: do we treat them separately?

## Slide 108: Cache Terminology

### Extracted Shape Text
- Cache Terminology
- Capacity (C):
- the number of data bytes a cache stores
- Block size (b):
- bytes of data brought into cache at once
- Number of blocks (B = C/b):
- number of blocks in cache: B = C/b
- Degree of associativity (N):
- number of blocks in a set
- Number of sets (S = B/N):
- each memory address maps to exactly one cache set

### Notes
- 108

## Slide 109: Cache Organization Recap

- Images: 0; Tables: 1

### Extracted Shape Text
- Cache Organization Recap
- Main Parameters
- Capacity: C
- Block size: b
- Number of blocks in cache: B = C/b
- Number of blocks in a set: N
- Number of Sets: S = B/N

| Organization | Number of Ways (N) | Number of Sets (S = B/N) |
| --- | --- | --- |
| Direct Mapped | 1 | B |
| N-Way Set Associative | 1 < N < B | B / N |
| Fully Associative | B | 1 |


### Notes
- 109

## Slide 110: Memory Consistency vs. Cache Coherence

### Extracted Shape Text
- Memory Consistency vs. Cache Coherence
- Coherence is about ordering of operations from different processors to the same memory location
- Local ordering of accesses to each cache block
- Consistency is about ordering of all memory operations from different processors (i.e., to different memory locations)
- Global ordering of accesses to all memory locations

### Notes
- Coherence;
- 一致性
- Consistency:
- 连贯性
- 110

## Slide 111: A computer system has a 32-byte cache, the size of each block is 4 bytes. The smallest addressable unit is 1 byte. Given

### Extracted Shape Text
- A computer system has a 32-byte cache, the size of each block is 4 bytes. The smallest addressable unit is 1 byte. Given the following access sequence S1 and the cache is empty at the beginning.
- S1: 0x8, 0x28, 0x8, 0x88, 0x8, 0x28
- (a) If the cache is direct mapped. Analyze whether each memory access is hit, if an access causes a cache miss, what kind of miss it is, compulsory miss, capacity miss, or conflict miss? And explain why.
- (b) if the cache is 2-way set-associative (using LRU replacement strategy), analyze whether each memory access is hit, if an access causes a cache miss, what kind of miss it is, compulsory miss, capacity miss, or conflict miss? And explain why.
- (c) If the cache is fully associative (using LRU replacement strategy), analyze whether each memory access is hit, if an access causes a cache miss, what kind of miss it is, compulsory miss, capacity miss, or conflict miss? And explain why.
- (d) Comparing the hit rates of three caches under the given access sequence in the question, which cache mapping policy has the highest hit rate.

## Slide 112: Cache Coherence

### Extracted Shape Text
- Cache Coherence

## Slide 113: Hardware Architecture for Cache Coherence

### Extracted Shape Text
- Hardware Architecture for Cache Coherence
- Hardware architecture for Cache Coherence:
- Cores, caches, interconnect, memory work together to achieve cache coherence from core’s point of view.
- Interconnect: Snoop/Directory
- Cache Updating: invl./update
- Cache Tags: MESI
- Core
- Interconnection Network
- Main Memory
- Core
- Core
- Cache
- Interconnect
- Memory
- CPU action
- Bus action
- CPU action
- Bus action
- Cache blocks
- Tags
- Cache blocks
- Tags
- R: read
- W:write
- I: invalidate
- U: update

## Slide 114: Cache Coherence Protocols

### Extracted Shape Text
- Cache Coherence Protocols
- Cache Coherence
- Snoop: [Goodman ISCA 1983]
- Bus-based, each bus action broadcasts on the bus, one action at a time, each bus action broadcasts on the bus, one action at a time.
- Single point of serialization for all memory requests.
- Directory:[Censier, ToC 1978]
- Single point of serialization per block, distributed among nodes
- Cores make explicit requests for blocks
- Directory tracks which caches have each block
- Directory coordinates invalidation and updates
- Core
- Switch (peer to peer)
- Main Memory
- Core
- CPU action
- Bus action
- CPU action
- Bus action
- Cache blocks
- Tags
- Cache blocks
- Tags
- Dict.
- Dict.

## Slide 115: Cache Coherence: Updating Policy

### Extracted Shape Text
- Cache Coherence: Updating Policy
- Cache Updating Policy: safely update replicated data in other caches.
- Update Protocol:
- Push a update command (bus action) to all copies
- Invalidate Protocol:
- Ensure only one local copy by sending out an invalidation command (bus action), then update the local copy
- Core
- Interconnect network
- Main Memory
- Core
- CPU action
- Bus action
- CPU action
- Bus action
- Cache blocks
- Tags
- Cache blocks
- Tags
- Dict.
- Dict.

### Notes
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 115

## Slide 116: Cache Coherence: Cache Tags

### Extracted Shape Text
- Cache Coherence: Cache Tags
- MSI Protocol: safely update replicated data in caches (goal).
- I(nvalid): block is not in cache, need to fetch from memory or other cache
- S(hared): in >=1 caches, clean, local cores can read it w/o bus action
- M(odified): in 1 cache, core can read/write it w/o bus action
- Core
- Bus (one trans. A time)
- Main Memory
- Core
- CPU action
- Bus action
- CPU action
- Bus action
- Cache blocks
- Tags
- Cache blocks
- Tags

### Notes
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 116

## Slide 117: Cache Coherence: Cache Tags

### Extracted Shape Text
- Cache Coherence: Cache Tags
- MSI Protocol: safely update replicated data in caches (goal).
- I(nvalid): block is not in cache, need to fetch from memory or other cache
- S(hared): in >=1 caches, clean, local cores can read it w/o bus action
- M(odified): in 1 cache, core can read/write it w/o bus action
- Core
- Bus (one trans. A time)
- Main Memory
- Core
- CPU action
- Bus action
- CPU action
- Bus action
- Cache blocks
- Tags
- Cache blocks
- Tags

### Notes
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 117

## Slide 118: The Problem with MSI

- Images: 0; Tables: 1

### Extracted Shape Text
- The Problem with MSI
- A block is not in cache at the beginning. On a read, the block immediately goes to the “Shared” state.
- Problem: The core that writes the block will issue a bus action invalidate even when only one cache copy exists.

| Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
| --- | --- | --- | --- | --- | --- |
| t0 |  |  | I | I |  |
| t1 | Read A |  | S | I | Read miss A |
| t2 | Write A |  | M | I | Invalidate |
| t3 |  | Read B | M | S | Read miss B |
| t4 |  | Write B | M | M | Invalidate |


## Slide 119: MESI Protocol

### Extracted Shape Text
- MESI Protocol
- MSI Protocol: safely update replicated data in caches (goal).
- I(nvalid): block is not in cache, need to fetch from memory or other cache
- S(hared): in >=1 caches, clean, local cores can read it w/o bus action
- M(odified): in 1 cache, core can read/write it w/o bus action
- MESI Protocol: Illinois protocol (ISCA, 84)
- I(nvalid): block is not in cache, need to fetch from memory or other cache
- S(hared): in >1 caches, clean, local cores directly reads it w/o bus action
- M(odified): in 1 cache, local core can read/write it w/o bus action
- E(xclusive): in 1 cache, clean, local core reads/writes it w/o bus action
- Papamarcos, “A low-overhead coherence solution for multiprocessors with private cache memories,” ISCA 1984.

### Notes
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 119

## Slide 120: MESI over MSI

- Images: 0; Tables: 2

### Extracted Shape Text
- MESI over MSI

| Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
| --- | --- | --- | --- | --- | --- |
| t0 |  |  | I | I |  |
| t1 | Read A |  | S | I | Read miss A |
| t2 | Write A |  | M | I | Invalidate |
| t3 |  | Read B | M | S | Read miss B |
| t4 |  | Write B | M | M | Invalidate |

- MSI:

| Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
| --- | --- | --- | --- | --- | --- |
| t0 |  |  | I | I |  |
| t1 | Read A |  | E | I | Read miss A |
| t2 | Write A |  | M | I |  |
| t3 |  | Read B | M | E | Read miss B |
| t4 |  | Write B | M | M |  |

- MESI:

## Slide 121: Memory Consistency vs. Cache Coherence

### Extracted Shape Text
- Memory Consistency vs. Cache Coherence
- Coherence is about ordering of operations from different processors to the same memory location
- Local ordering of accesses to each cache block
- Write serialization: all cores see the same write ordering
- Consistency is about ordering of all memory operations from different processors (i.e., to different memory locations).
- Global ordering of accesses to all memory locations

### Notes
- Coherence;
- 一致性
- Consistency:
- 连贯性
- 121

## Slide 122: Ordering of Operations

### Extracted Shape Text
- Ordering of Operations
- Operations: A, B, C, D
- In what order should the hardware execute (and report the results of) these operations?
- Consistency： A contract between programmer and microarchitect
- Preserving an “expected” (more accurately, “agreed upon”) order simplifies programmer’s life
- Ease of debugging; ease of state recovery, exception handling
- Preserving an “expected” order usually makes the hardware designer’s life difficult
- Especially if the goal is to design a high performance processor: Recall load-store queues in out of order execution and their complexity

## Slide 123: Four Types of Memory Barrier

### Extracted Shape Text
- Four Types of Memory Barrier
- Load-Load:
- Effectively prevents ordering of loads performed before the barrier with loads performed after the barrier
- Load-Store:
- Effectively prevents ordering of loads performed before the barrier with writes performed after the barrier
- Store-Store:
- Effectively prevents ordering of stores performed before the barrier with stores performed after the barrier
- Store-Load:
- Effectively prevents ordering of stores performed before the barrier with loads performed after the barrier

## Slide 124: Four Memory Barriers vs. Consistence Model

- Images: 0; Tables: 1

### Extracted Shape Text
- Four Memory Barriers vs. Consistence Model
- Comparison of memory models:
- The stronger memory model leads to lower performance/higher overhead
- The stronger memory model makes programmers’ life easier

| Load-Load | Load-Store | Store-Store | Store-Load | Consistence Model | CPU |
| --- | --- | --- | --- | --- | --- |
| √ | √ | √ | √ | Sequential Consistency | Dual 386 |
| √ | √ | √ |  | Total Store Order | X86/64 |
| √ | √ |  |  | Partial Store Order | Arm |
|  |  |  |  | Really weak memory model | DEC Alpha |


## Slide 125: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 126: Recall: Five Design Principles of AI Accelerators

- Images: 0; Tables: 1

### Extracted Shape Text
- Recall: Five Design Principles of AI Accelerators

| Operator | 计算特性 | 访存特性 |
| --- | --- | --- |
| Conv | 矩阵相乘 | Burst+stride |
| Activation | 单向量操作 | Sequential |
| Pooling | 单矩阵Reduce操作 | Burst+stride |
| FC | 矩阵相乘 | Sequential |

- MAC (Multiply–Accumulate)
- Fixed Memory Access Pattern
- AI相关计算内，矩阵乘法计算量的占比高于90%。

## Slide 127: Recall: Five Design Principles of AI Accelerators

### Extracted Shape Text
- Recall: Five Design Principles of AI Accelerators
- Five Design Principles:
- Global Buffer: 使用专有的存储器来减少数据搬运的距离与开销，比如将复杂的cache设计替换成scratchpad memory (global buffer)。
- 简化控制模块: 将缩减的高级微架构特性而节省出的面积，用于增加更多的运算单元或者片上存储。
- 并行计算模块: 使用能够符合特定领域加速需求最简单的并行形式，例如，对于矩阵运算的加速，单条指令直接支持小矩阵运算。
- 量化: 减少计算数据尺寸与类型来符合特定领域性能要求，例如，深度学习中，推理可以采用int8量化方式进行。
- 专用编程语言: 使用DSA专用语言进行编程。

## Slide 128: Matrix Multiplication Unit

### Extracted Shape Text
- Matrix Multiplication Unit
- Scalar:
- for (int i = 0; i < 16; i++)
- for (int j = 0; j < 16; j++)
- for (int k = 0; k < 16; k++)
- C[i][j] += A[i][k] * B[k][j]
- for (int i = 0; i < 16; i++)
- for (int j = 0; j < 16; j++)
- C[i][j] = A[i][:] * B[:][j]
- C[:][:] = A[:][:] * B[:][:]
- Vector:
- Matrix:
- 周期数：16*16*16 = 4096
- 每周期内存访问量: 2 (rd), 1/16 (wr)
- 周期数：16*16 = 256
- 每周期内存访问量: 2*16 (rd), 1 (wr)
- 周期数：1
- 每周期内存访问量: 2*16*16 (rd), 16*16 (wr)
- 算力密度高
- 灵活
- A
- 16
- 16
- B
- 16
- X
- C
- =
- 16
- 16
- float A[16][16], B[16][16], C[16][16];

## Slide 129: AI Chips

- Images: 3; Tables: 0

### Extracted Shape Text
- AI Chips
- TPU
- Ascend
- Cambricon

## Slide 130: 晟腾310/910 芯片结构示意图

- Images: 1; Tables: 0

### Extracted Shape Text
- 晟腾310/910 芯片结构示意图
- L2 Buffer vs. L2 Cache
- 同一个介质，两种使用模式
- Buffer：程序员可见并可以直接读写（地址空间和DDR/HBM不重合）
- Cache: 作为DDR/HBM高速缓存，程序员不可见
- DDR/HBM
- DDR: 普通内存，带宽低/价格低，在推理芯片310中
- HBM： High Bandwidth Memory, 带宽高, 成本高，在训练芯片310中

## Slide 131: 华为晟腾310推理芯片

### Extracted Shape Text
- 华为晟腾310推理芯片

## Slide 132: 华为晟腾910训练芯片

- Images: 1; Tables: 0

### Extracted Shape Text
- 华为晟腾910训练芯片

## Slide 133: Recall: Ascend Cube模块 （算力担当）

- Images: 1; Tables: 0

### Extracted Shape Text
- Recall: Ascend Cube模块 （算力担当）
- 矩阵乘运算单元Cube : 一拍完成一个fp16的 2个16x16矩阵相乘； C = A * B; 如果是int8输入,则一拍完成 16*32 与 32*16 矩阵乘。
- 累加器Accumulator: 把当前矩阵乘的结果与前次计算的中间结果相加 （ C = A * B + C ）， 可以用于完成卷积中加bias操作。
- L0A/L0B/L0C Buffer: L0A 存储矩阵乘的左矩阵数据，L0B 存储矩阵乘的右矩阵数据， L0C 存储矩阵乘的结果和中间结果。
- A/B DFF: 数据寄存器，缓存当前计算的16*16 左/右子矩阵。
- Accum DFF : 数据寄存器，缓存当前计算的16*16结果矩阵。

### Notes
- Cube
- :
- 矩阵乘运算单元，一拍完成一个
- fp16
- 的
- 16x16
- 与
- 矩阵乘；
- C
- =
- A
- *
- B
- ;
- 如果是
- int8
- 输入
- ,
- 则一拍完成
- 16*32
- 32*16
- 矩阵乘。
- Accumulator
- 累加器， 把当前矩阵乘的结果与前次计算的中间结果相加， 可以用于完成卷积中加
- bias
- 操作。
- B + C
- L0A/L0B/L0C Buffer
- : L0A
- 存储矩阵乘的左矩阵数据，
- L0B
- 存储矩阵乘的右矩阵数据，
- L0C
- 存储矩阵乘的结果和中间结果。
- A/B DFF
- 数据寄存器，缓存当前计算的
- 16
- 左
- /
- 右子矩阵。
- Accum
- DFF
- 16*16
- 结果矩阵。
- 133

## Slide 134: Recall: Vector模块 （多面手）

- Images: 1; Tables: 0

### Extracted Shape Text
- Recall: Vector模块 （多面手）
- 向量运算单元Vector Unit： 覆盖各种基本的计算类型和许多定制的计算类型，主要包括FP16/FP32/int32/Int8等数据类型的计算，支持连续或者固定间隔寻址；或者VA寄存器寻址（不规则向量运算）
- SIMD长度：一条Vector指令可以完成两个128长度fp16类型的向量相加/乘，或者64个fp32/int32类型的向量相加/乘
- Unified Buffer(UB)： 保存Vector运算的源操作数和目的操作数； 一般要求32Byte对齐；
- 数据从L0C->UB：随数据搬运在Vector Unit完成一些RELU/数据格式转换等操作

### Notes
- Vector Unit
- ： 向量运算单元，覆盖各种基本的计算类型和许多定制的计算类型，主要包括
- FP16/FP32/int32/Int8
- 等数据类型的计算，支持连续或者固定间隔寻址；或者
- VA
- 寄存器寻址（不规则向量运算）
- SIMD
- 长度
- ：一条
- Vector
- 指令可以完成两个
- 128
- fp16
- 类型的向量相加
- /
- 乘， 或者
- 64
- 个
- fp32/int32
- 乘
- Unified Buffer(UB)
- ： 保存
- 运算的源操作数和目的操作数； 一般要求
- 32Byte
- 对齐；
- 数据从
- L0C->UB
- ，需要以
- 作为中转，并可以随数据搬运完成一些
- RELU/
- 数据格式转换等操作
- 134

## Slide 135: Recall: Scalar模块 （司令部）

- Images: 1; Tables: 0

### Extracted Shape Text
- Recall: Scalar模块 （司令部）
- Scalar Unit： 负责完成AICore中的标量运算，功能上可以看做一个小CPU；完成整个程序的循环控制、分支判断、CUBE/Vector等指令的地址和参数计算以及基本的算术运算等‘
- Unified Buffer or Scalar Buffer: 晟腾310/910 Scalar Unit不能直接访问外面的DDR/HBM, 需要预留UB的一部分(310)或者使用专门的Scalar Buffer(910)用作Scalar Unit的堆栈空间
- GPR：通用寄存器，目前包含32个通用寄存器
- SPR: 专用寄存器，为了支持指令集一些指令的特殊需要，Davinci设计了许多专用寄存器，比如CoreID, BLOCKID, VA, STATUS, CTRL等寄存器

## Slide 136: TPU v1

- Images: 1; Tables: 0

### Extracted Shape Text
- TPU v1
- Matrix Multiply Unit
- 256x256 MACs
- Systolic Array
- 24% area
- Unified Buffer
- 24 MB
- 29% area
- [Google, In-Datacenter Performance Analysis of a Tensor Processing Unit, ISCA, 2017]
- TPU v1
- For inference, model is pre-stored in DDR3, and data is from the host via PCIe

## Slide 137: Systolic Arrays in AI Accelerator

### Extracted Shape Text
- Systolic Arrays in AI Accelerator
- Systolic array can be multi-dimensional
- The most popular one used by AI ａｃｃｅｌｅｒａｔｏｒ is two-dimensional．
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- PE
- Cell
- Left
- Right
- Upper
- Down
- Processing engine (PE):
- How a PE updates:
- Right = Left
- Down = Upper
- Cell = Cell + Upper * Left

## Slide 138: Cambricon AI Accelerator DLP-S

- Images: 2; Tables: 0

### Extracted Shape Text
- Cambricon AI Accelerator DLP-S
- DLP-S
- Control Module
- Compute Unit
- SRAM Unit

## Slide 139: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 140: AI Architecture

- Images: 3; Tables: 0

### Extracted Shape Text
- AI Architecture
- AI Runtime
- AI Framework
- Parallel
- Training
- CANN*
- AI Chip
- 模型训练和推理框架
- Compute Architecture for Neural Network
- AI IP和芯片
- Ascend
- 计算加速库、芯片算子库和高度自动化的算子开发工具
- MindSpore
- TensorFlow
- PyTorch
- PaddlePaddle
- …
- Data parallel
- CUDA*
- Compute Unified Device Architecture
- Model parallel
- Pipeline parallel
- Hybrid parallel

### Notes
- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 140

## Slide 141: Compute Architecture for Neural Network (CANN)

- Images: 1; Tables: 0

### Extracted Shape Text
- Compute Architecture for Neural Network (CANN)

### Notes
- 全流程服务，分层
- API
- 和预集成方案
- 降低核心代码量
- 20%,
- 效率提升
- 50%
- 以上
- 应对算子多样性，开发效率提升
- 3
- 倍
- 141

## Slide 142: CANN算子开发方式比较

- Images: 0; Tables: 1

### Extracted Shape Text
- CANN算子开发方式比较

| 参数 | TBE DSL方式 | TIK方式 | AI CPU方式 |
| --- | --- | --- | --- |
| 语言 | Python | Python | C++ |
| 计算单元 | AI Core | AI Core | AI CPU |
| 运用场景 | 常用于各种算术逻辑简单向量运算，或内置支持的矩阵运算及池化运算 | 适用各类算子的开发，对于无法通过lambda表达描述的复杂计算场景也有很好的支持，例如排序类操作 | 某些场景下，无法通过AI Core实现的自定义算子，或者需要临时快速打通网络的场景下使用 |
| 入门难度 | 较低 | 较高 | 中等 |
| 适用人群 | 入门用户，需要了解NN、TBE DSL相关知识 | 高级用户，需要了解NN，深入理解昇腾AI处理器架构、指令集、数据搬运等相关知识 | 具备C++程序开发能力，对机器学习、深度学习、AI CPU开发流程有一定的了解 |
| 特点 | TBE DSL接口已高度封装，用户仅需要使用DSL接口完成计算过程的表达，后续的Schedule创建、优化及编译都可通过已有接口一键式完成 | 入门难度高，程序员直接使用TIK提供的API完成计算过程的描述及Schedule过程，需要手工控制数据搬运的参数和Schedule。用户无须关注Buffer地址的分配及数据同步处理，由TIK工具进行管理 | 开发的流程和DSL都是类似的， 不需要了解AI Core的内部架构设计，入门较快 |
| 不足 | 某些场景下性能可能较低，复杂算子逻辑无法支持表达 | 需要开发者手工控制数据搬运的参数和Schedule过程。 | 无封装的计算接口，计算过程相对繁琐，另外AI CPU性能较低。 |


## Slide 143: 初阶图优化-CSE

### Extracted Shape Text
- 初阶图优化-CSE
- +
- *
- *
- +
- B
- C
- D
- B
- C
- E
- +
- +
- *
- *
- +
- B
- C
- D
- E
- w
- w

### Notes
- CSE
- （
- Common-Subexpression Elimination
- ），公共子表达式消除。
- 简单而言就是将相同输入的表达式进行消除，复用计算结果。
- 143

## Slide 144: 图优化-算子融合（Intuition）

### Extracted Shape Text
- 图优化-算子融合（Intuition）
- Data
- Conv2D
- BatchNorm
- Relu
- Data
- Conv2D_BatchNorm_Relu
- 算子执行的访存特性：
- ConvD：顺序写
- BatchNorm：顺序读写
- ReLU：顺序读写
- 算子特性：
- 每个算子都从内存读数
- 计算完成放回内存

### Notes
- Reducing high-cost operations
- 144

## Slide 145: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 146: MindSpore逻辑架构

### Extracted Shape Text
- MindSpore逻辑架构
- MindSpore Extend
- GNN/深度概率编程/强化学习/微分方程
- Mind
- Armour
- Model Zoo
- MindData
- MindRT
- MindRT(分布式DAG并行执行)
- MindRT Lite/Micro
- MindCompiler
- MindIR
- 量化/剪枝/….
- MindAKG(算子自动生成)
- 仓颉
- 前端
- 图算融合
- 内存优化
- 流水线执行
- 自动微分
- 类型推导
- 自动并行
- 二阶优化
- MindExpression
- 硬件相关优化
- 密态AI
- 可信AI
- Mind
- Insight
- 网络调试
- 精度调优
- 性能调优
- CANN昇腾
- CUDA
- Eigen
- Android
- iOS
- 自动并行：整图切分，感知集群拓扑，实现通信开销最小，融合数据并行与模型并行；
- 二阶优化：利用二阶计算修正梯度更新方向，找到训练梯度最优下降路径，从而加速训练收敛过程；
- 动静态图结合：统一自动微分引擎支持动静态图，一行代码完成模式切换，兼顾模型开发和执行效率；
- AI+科学计算，场景应用创新，拓展MindSpore的边界

## Slide 147: 关键技术4：AI+科学计算

### Extracted Shape Text
- 关键技术4：AI+科学计算
- 科学计算近况：
- 科学计算核心问题是微分方程求解，算力消耗巨大，大规模求解器垄断历年戈登贝尔奖，近年来结合AI方法成为趋势。
- 业界AI+科学计算现状：
- TF：众筹方式构建AI求解模型，典型应用领域取得突破；面向DNN设计的自动微分，计算高阶微分时效率低下；
- Nvidia：支持高精度计算；构筑cuBLAS、cuFFT等基础数学库；上层框架依赖TensorFlow，继承TF缺点
- 非线性拟合，无需解高维方程
- 神经网络模拟，不需要处理边界条件
- AI方法求解
- 高维微分方程求解，计算量大
- 边界条件复杂，求解不稳定
- 传统数值方法

### Notes
- 科学计算才是
- AI
- 应用的蓝海。。。
- 147

## Slide 148: One Iteration for a Layer

### Extracted Shape Text
- One Iteration for a Layer
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- ×
- =
- W
- X
- Y
- 1, Forward Pass:
- ×
- =
- dW
- dY
- X T
- 2, Backward Pass:
- weight gradients
- × =
- dX
- dY
- W T
- 2, Backward Pass:
- activation gradients
- 3, Weight update:
- + … =
- W
- W
- dW
- +
- One iteration:
- Backward pass:
- Its compute is ~2x of forward
- requires activations computed during the fwd pass
- Read After Write (RAW) Dependency Regarding the Model x

## Slide 149: Why Distributed Training?

### Extracted Shape Text
- Why Distributed Training?
- Challenge from Model Side: Larger models
- Language models: in the past 2 years grew from 340M (BERT-large) to 175B (GPT-3) parameters
- Recommender models: largest ones are reaching O(1B) parameters
- Vision models: deeper and wider Resnets and ResNeXTs
- Challenge from Dataset Side: Larger datasets
- Recommender data (user behavior): terabytes to petabytes
- Image data: 1B Instagram dataset, JFT (300M images)
- Challenge from System Side:
- The memory size of a single accelerator, e.g., GPU, is 40GB.

## Slide 150: Parallelism Taxonomy

### Extracted Shape Text
- Parallelism Taxonomy
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Parallel Training
- Data Parallel
- Model Parallel
- Intra Layer
- Inter Layer/
- Pipeline

## Slide 151: Data Parallel: Forward Pass

### Extracted Shape Text
- Data Parallel: Forward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- W
- X
- Y
- ×
- =
- ×
- =
- ×
- =
- ×
- =
- Worker 0:
- Worker 1:
- Worker 2:
- Worker 3:
- Forward pass:
- Computes output activations for its portion of minibatch
- No communication is needed
- X : input activations
- W : model
- Y : output activations
- Whole Model
- Partial dataset

## Slide 152: Data Parallel Training: Weight Update

- Images: 4; Tables: 0

### Extracted Shape Text
- Data Parallel Training: Weight Update
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Weight update:
- 1, Each of N workers accumulates gradients:
- Summing 1/N gradients collected from (N – 1) peers
- 2, Each worker updates its model:
- Each worker updates its copy of the model with combined gradients from all 4 workers
- Worker a
- Worker b
- Worker c
- Worker d
- (a+b+c+d)/4

## Slide 153: Data Parallel: Challenges

### Extracted Shape Text
- Data Parallel: Challenges
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Strong scaling (increase the number of workers, keep minibatch size constant)
- Certain layers require minimum minibatch sizes to properly operate
- Example: batch normalization (BN) generally requires 16+ samples
- Maybe lower GPU utilization
- Weak scaling (increase the number of workers, increase minibatch size)
- Training networks with large minibatches requires hyper-parameter adjustment
- Learning rate schedule, BN decay, …
- Example: R50 (SGD up to bs=16K, LARS above 16K, …)
- Often increase the amount of work required to reach the same model accuracy

## Slide 154: Parallelism Taxonomy

### Extracted Shape Text
- Parallelism Taxonomy
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Parallel Training
- Data Parallel
- Model Parallel
- Intra Layer
- Inter Layer/
- Pipeline

## Slide 155: Model Parallel Training

### Extracted Shape Text
- Model Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 1
- Worker 2
- Intra-layer Parallel
- A worker is responsible for its portion of each layer
- Worker 0
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 0
- Worker 1
- Worker 2
- Inter-layer Parallel (aka Pipeline Parallel):
- A worker is responsible for its portion of the layers

## Slide 156: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 157: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 158: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 159: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 160: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 161: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time

## Slide 162: Pipeline Parallel Training

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |

- Forward
- Backward
- Loss
- Time
- Idle bubbles:
- 67%: 12/18 step-slots
- For N workers:
- (N – 1)/N idle slots

### Notes
- N: number of workers, devices.
- 162

## Slide 163: Pipeline Parallel Training: GPipe

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training: GPipe
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Forward
- Backward
- Loss

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  |  |

- 2 subminibatches
- 2x more steps
- Each step is ½ compute
- Key Idea: Subminibatches
- Idle bubbles: 50%
- 12/24 steps-slots

## Slide 164: Pipeline Parallel Training: GPipe

- Images: 0; Tables: 1

### Extracted Shape Text
- Pipeline Parallel Training: GPipe
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- N workers, K subminibatches:
- 2(N + K – 1) steps for fwd/bwd
- Total step-slots: 2N(N + K – 1)
- Idle step-slots: 2N(N – 1)
- Fraction of idle slots: (N – 1)/(N + K – 1)
- Forward
- Backward
- Loss

| Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  |  |
| Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  |  |

- As N grows:
- K = N → 50% idle slots
- K = 4N → 20% idle slots

### Notes
- 164

## Slide 165: Pipeline Parallel: Communication

### Extracted Shape Text
- Pipeline Parallel: Communication
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- A worker communicates with its 2 neighbors
- 1D mesh topology
- 1D torus when interleaving layers
- Communication in each step of the fwd and bwd pass
- Activations in fwd, activation gradients in bwd
- Overlap communication with computation
- Very hard

## Slide 166: Pipeline Parallel: Challenges

### Extracted Shape Text
- Pipeline Parallel: Challenges
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Load balancing workload across workers is difficult
- Different layers of a network can take different amounts of time
- Leads to even busy slots for other workers idling for portions of time
- Lots of computation to hide communication
- Idle slots reduce scaling efficiency
- Many subminibatches help with this, but run into the same problems as strong-scaling of data-parallel.

## Slide 167: Outline

### Extracted Shape Text
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline
- Intra-layer
- Communication Pattern Review
- Summary

## Slide 168: Intra-layer Parallel

### Extracted Shape Text
- Intra-layer Parallel
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Partition a given layer’s weights among the workers
- Addresses some of the Pipeline Parallel challenges
- Idle slots, load imbalance
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 0
- Worker 1
- Worker 2
- ×
- ×
- Row-wise partitioning:
- Column-wise partitioning:
- Two variants:
- Row-wise partitioning
- Column-wise partitioning

## Slide 169: Row-wise Partitioning: Allgather between Layers

- Images: 0; Tables: 21

### Extracted Shape Text
- Row-wise Partitioning: Allgather between Layers
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each worker:
- W: Has a portion of weight rows
- X: All of input activations X
- Y: Computes a portion of output activations

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- Fwd communication: Allgather
- Layer K fwd
- Layer (K + 1) fwd
- Worker 0
- Worker 1
- Worker 2
- X
- W
- Y

## Slide 170: Column-wise Partitioning: ReduceScatter between Layers

- Images: 0; Tables: 11

### Extracted Shape Text
- Column-wise Partitioning: ReduceScatter between Layers
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each worker:
- W: Has a portion of weight rows
- X: All of input activations X
- Y: Computes a portion of output activations
- Fwd communication: ReduceScatter
- × =
- × =

|  |  |  |
| --- | --- | --- |

- × =
- × =

|  |
| --- |
|  |
|  |

- × =

|  |  |  |
| --- | --- | --- |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |

- Layer K fwd
- Layer (K + 1) fwd
- Worker 0
- Worker 1
- Worker 2
- +
- +
- +
- X
- W
- Y

### Notes
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 170

## Slide 171: Reducing Synchronization By Alternating Partitioning

- Images: 0; Tables: 13

### Extracted Shape Text
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2

|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =

|  |  |  |
| --- | --- | --- |

- × =

|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |

- Layer (K + 1) fwd

|  |
| --- |
|  |
|  |

- Row-wise partitioning Column-wise partitioning
- Note: no communication is needed for two layers
- Worker i produces output, which is its input for the next layer
- W
- W

### Notes
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 171

## Slide 172: Reducing Synchronization By Alternating Partitioning

- Images: 0; Tables: 13

### Extracted Shape Text
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2

|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =

|  |  |  |
| --- | --- | --- |

- × =

|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |

- Layer (K + 1) fwd

|  |
| --- |
|  |
|  |

- Row-wise partitioning Column-wise partitioning
- Note: no communication is needed for two layers
- Worker i produces output, which is its input for the next layer
- W
- W
- +Next two layers?

### Notes
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 172

## Slide 173: Reducing Synchronization By Alternating Partitioning

- Images: 0; Tables: 18

### Extracted Shape Text
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2

|  |
| --- |
|  |
|  |

- × =
- × =

|  |  |  |
| --- | --- | --- |

- × =

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |  |  |
| --- | --- | --- |


|  |  |  |
| --- | --- | --- |

- Communication: Allreduce
- Layer (K + 1) fwd
- +
- +
- +

|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |


|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =

|  |
| --- |
|  |
|  |

- × =
- Layer (K + 2) fwd
- Row-wise partitioning Column-wise partitioning Row-wise partitioning

|  |
| --- |
|  |
|  |


### Notes
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 173

## Slide 174: Communication Pattern Summary

### Extracted Shape Text
- Communication Pattern Summary
- Data Parallel:
- Allreduce of weights
- Can be overlapped with computation
- Pipeline Parallel:
- Point-wise communication of activations and activation gradients
- Hard to overlap with computation
- Hard to load-balance
- Intra-layer Parallel:
- Allgather, Reduce_scatter of activations and activation gradients
- Allreduce if row-wise and col-wise partitioning is alternated
- Hard to overlap with computation

## Slide 175: 5%: pop quiz + checking

### Extracted Shape Text
- 5%: pop quiz + checking
- 35%: 4-5 Lab assignments
- lab grade = report (40%) + check(60%)
- 5-10%: Bonus
- 60%: Final exam
- (close-book test with one A4 memo)
- Understand the key idea of each component
- Final grade = Min(Final exam + pop quiz + Labs, 99)
- Grading Policy:
- 40%

## Slide 176: Lab assignments 35%

### Extracted Shape Text
- Lab assignments 35%
- Objectives
- Implement a pipelined CPU with at least RISCV instructions + SIMD instructions via Verilog in Vivado (15%)
- GPU Programming (10%)
- AI Chip Programming (10%)
- How
- Do the lab by yourself and submit lab report and code to website.
- Do 3 lab assignments gradually, examine results each time
- TAs will ask questions regarding your lab reports and your code.
- Grading
- Lab1-3: 15%, 10%, 10% + Bonus
