# 4-superscalar-cores-SIMD.pptx

- Slides: 98

## Slide 1: Computer Arch. & AI ChipLecture 4: Superscalar + SIMD + Multi-core

### Extracted Shape Text
- Computer Arch. & AI ChipLecture 4: Superscalar + SIMD + Multi-core
- Prof. Zeke Wang
- Zhejiang University
- 26 March 2026

### Notes
- 1

## Slide 2: Recall: Reorder Buffer (ROB)

### Extracted Shape Text
- Recall: Reorder Buffer (ROB)
- Key Idea: Complete instructions out-of-order, but reorder them before writing results to architectural state (Commit).
- 1, When instruction is decoded in order, it reserves the next-sequential entry in the ROB, rename the destination register.
- 2, When instruction completes out-of-order, it writes result into ROB entry.
- 3, When instruction oldest in ROB and it has completed without exceptions, its result writes to reg. file or memory (In order commitment)
- Register
- File
- Func Unit
- Func Unit
- Func Unit
- Reorder
- Buffer
- Instruction
- Cache
- Complete out-of-order
- Commit
- in order
- Decoded
- in order

### Notes
- Need the animation here…
- R
- ob index, write, read…
- 2

## Slide 3: In order dispatch + precise exceptions:

### Extracted Shape Text
- In order dispatch + precise exceptions:
- Out-of-order dispatch + precise exceptions:
- IO: 16 vs. OoO:12 cycles
- Recall: Effect of Out-of-order Dispatch
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
- STALL
- F
- D
- E
- R
- W
- STALL
- F
- D
- E
- R
- W
- E
- E
- E
- E
- F
- D
- E
- R
- W
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
- F
- D
- E
- R
- W
- WAIT
- F
- D
- E
- R
- W
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R1  R6, R7
- IMUL R5  R6, R8
- ADD R7  R3, R5
- IMUL: 4 cycles, ADD： 1 cycle

### Notes
- 假设有forward
- ，
- IMUL 4 cycles, ADD 1 cycle.
- 3

## Slide 4: Recall: Two Humps in a Modern Pipeline

### Extracted Shape Text
- Recall: Two Humps in a Modern Pipeline
- Hump 1: Reservation stations (enabling in-order issue and out-of-order dispatch/execution)
- Hump 2: Reorder buffer (enabling OoO completion, in-order commitment)
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
- Reservation Station
- TAG and VALUE Broadcast Bus
- In order issue
- OoO dispatch
- In order commitment
- OoO execution

## Slide 5: Register rename table (register alias table)

- Images: 0; Tables: 1

### Extracted Shape Text
- Register rename table (register alias table)
- Recall: Tomasulo’s Algorithm: Components
- R0
- R1
- R2
- R3
- tag
- value
- valid?
- R4
- R5
- R6
- R7
- R8
- R9
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1

|  | Source 1 |  |  | Source 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | V | Tag | Value | V | Tag | Value |
| a |  |  |  |  |  |  |
| b |  |  |  |  |  |  |
| c |  |  |  |  |  |  |
| d |  |  |  |  |  |  |

- Reservation station
- rs.tag
- IF
- ID
- E
- W
- RS
- Common Data Bus:
- Broadcasts the tag and result to all RSs
- Updates the RF using the tag and result

### Notes
- T
- ag: reservation station entry ID
- Valid: 1 means the register is readable, 0 means the new value exists in a reservation station entry.
- 5

## Slide 6: Recall: Tomasulo’s Algorithm

### Extracted Shape Text
- Recall: Tomasulo’s Algorithm
- ID: If reservation station entry available before renaming dest. register
- Occupy a RS entry for the instruction
- For each source register in the RS entry: if the valid bit of source register in RF is 1, RS.source.v = 1 and RS.source.value=source register; else RS.source.v = 0 and RS.source.tag = source register.tag.
- For dest. register in RF: Rename to the tag of the corresponding RS entry, set the valid bit to 0.
- Else stall
- RS: While in reservation station, each instruction:
- Update: Watches common data bus (CDB) for tag of its sources. When tag seen, grab value for the source and keep it in the reservation station.
- Issue: When both operands available, instruction ready to be dispatched to FU
- EXE: Execute the instruction in FU, produce its broadcast tag and value
- WB: After instruction finishes in the Functional Unit
- a, Arbitrate for CDB
- b, Put broadcast tag and its broadcast value onto CDB (tag broadcast)
- c, Update register file connected to the CDB
- If the tag in the register file matches the broadcast tag, write broadcast value into register (and set valid bit)
- d, Update reservation station connected to the CDB
- If the broadcast tag matches the tag of any source in a RS entry, write the broadcast value to the source and set the valid bit of the source.

### Notes
- d, Reclaim rename tag
- no valid copy of tag in system!
- 6

## Slide 7: Outline

### Extracted Shape Text
- Outline
- Superscalar
- Vector Insn
- Multithreading
- Multi-core

## Slide 8: Superscalar Execution

### Extracted Shape Text
- Superscalar Execution

### Notes
- 8

## Slide 9: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 10: Superscalar Execution

### Extracted Shape Text
- Superscalar Execution
- Idea: Fetch, decode, execute, retire multiple instructions per cycle
- N-wide superscalar  N instructions per cycle
- Issues:
- Need to add the hardware resources for doing so
- Hardware performs the dependence checking between concurrently-fetched instructions
- Superscalar execution and out-of-order execution are orthogonal concepts
- Can have all four combinations of processors:
- [in-order, out-of-order] x [scalar, superscalar]

## Slide 11: In-Order Superscalar Processor Example

### Extracted Shape Text
- In-Order Superscalar Processor Example
- Idea: Multiple copies of data-path: Can fetch/decode/execute multiple instructions per cycle.
- Issue: Dependences make it tricky to dispatch multiple instructions in the same cycle.
- Need dependence detection between concurrently-fetched instructions.
- Here: Ideal IPC = 2

### Notes
- 11

## Slide 12: In-Order Superscalar: Ideal

### Extracted Shape Text
- In-Order Superscalar: Ideal
- lw $t0, 40($s0)
- add $t1, $s1, $s2
- sub $t2, $s1, $s3 and $t3, $s3, $s4 or $t4, $s1, $s5
- sw $s5, 80($s0)
- Ideal IPC = 2
- Actual IPC = 2 (6 instructions issued in 3 cycles)

## Slide 13: In-Order Superscalar: Dependences

### Extracted Shape Text
- In-Order Superscalar: Dependences
- lw $t0, 40($s0)
- add $t1, $t0, $s1
- sub $t0, $s2, $s3 and $t2, $s4, $t0 or $t3, $s5, $s6
- sw $s7, 80($t3)
- Ideal IPC = 2
- Actual IPC = 1.2
- (6 instructions issued in 5 cycles)

### Notes
- Pointer chasing
- 13

## Slide 14: Superscalar Execution Tradeoffs

### Extracted Shape Text
- Superscalar Execution Tradeoffs
- Advantages
- Higher instruction throughput
- Higher IPC: instructions per cycle (i.e., lower CPI)
- Disadvantages
- Higher complexity for dependence checking
- Require checking within a pipeline stage
- Register renaming becomes more complex in an OoO processor
- Potentially lengthens critical path delay  clock cycle time
- More hardware resources needed

## Slide 15: Can superscalar tech affect the result in Roofline model?

### Extracted Shape Text
- Can superscalar tech affect the result in Roofline model?

### Notes
- 不太行
- 15

## Slide 16: Outline

### Extracted Shape Text
- Outline
- Superscalar
- Vector Insn
- Multithreading
- Multi-core

## Slide 17: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 18: Flynn’s Taxonomy of Computers

### Extracted Shape Text
- Flynn’s Taxonomy of Computers
- SISD: Single instruction operates on single data element
- SIMD: Single instruction operates on multiple data elements
- Array processor
- Vector processor
- MISD: Multiple instructions operate on single data element
- Closest form: systolic array processor, streaming processor
- MIMD: Multiple instructions operate on multiple data elements (multiple instruction streams)
- Multiprocessor
- Multithreaded processor
- Mike Flynn, “Very High-Speed Computing Systems,” Proc. of IEEE, 1966

### Notes
- Flynn:
- 弗林
- 18

## Slide 19: Single-Instruction/Single-Data Stream (SISD)

### Extracted Shape Text
- Single-Instruction/Single-Data Stream (SISD)
- SISD computer that exploits no parallelism in either the instruction or data streams.
- Examples of SISD：
- traditional uniprocessor machines, e.g. our trusted RISC-V pipeline
- Instruction Pool
- PU
- Data Pool

## Slide 20: Single-Instruction/Multiple-Data (SIMD or “sim-dee”)

### Extracted Shape Text
- Single-Instruction/Multiple-Data (SIMD or “sim-dee”)
- SIMD computer exploits multiple data streams against a single instruction stream to operations that are naturally parallelized.
- Examples of SIMD:
- Intel SIMD instruction extensions
- AMD, PowerPC
- Instruction Pool
- PU
- PU
- PU
- PU
- Data Pool

## Slide 21: Multi-Instruction/Multiple-Data (MIMD or “mim-dee”)

### Extracted Shape Text
- Multi-Instruction/Multiple-Data (MIMD or “mim-dee”)
- MIMD computer exploits a number of processors that function asynchronously and independently for parallelism. At any time, different processors may be executing different instructions on different pieces of data.
- Example of MIMD:
- Intel Xeon Phi
- Instruction Pool
- PU
- PU
- PU
- PU
- Data Pool

## Slide 22: Multiple-Instruction/Single-Data Stream (MISD)

### Extracted Shape Text
- Multiple-Instruction/Single-Data Stream (MISD)
- MISD computer exploits multiple instruction streams against a single data stream.
- Example of MISD:
- Historical significance,
- Systolic array processor,
- Streaming processor
- Instruction Pool
- PU
- PU
- Data Pool

## Slide 23: SIMD Applications & Implementations

### Extracted Shape Text
- SIMD Applications & Implementations
- Applications:
- Scientific computing
- Matlab, NumPy
- Graphics and video processing
- Photoshop, …
- Big Data
- Deep learning
- Gaming
- …
- Implementations:
- x86
- ARM
- RISC-V vector extensions

## Slide 24: Intuition of SIMD Capability

### Extracted Shape Text
- Intuition of SIMD Capability
- Computing task (A[6:0] + B[6:0])
- Scalar: one addition per cycle
- SIMD : Multiple additions per cycle
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

## Slide 25: 1, 256-bit AVX2 (8个32-bit float)

### Extracted Shape Text
- 1, 256-bit AVX2 (8个32-bit float)
- 2, 512-bit AVX512 (16个32-bit float)
- SIMD in Intel CPU：
- Linus Torvalds: “I hope AVX512 dies a painful death, and that Intel starts fixing real problems instead of trying to create magic instructions to then create benchmarks that they can look good on…”

### Notes
- 现在的计算世界往三个方向发展
- 25

## Slide 26: Recall: Amdahl’s Law

### Extracted Shape Text
- Recall: Amdahl’s Law
- Amdahl’s Law
- f: Parallelizable fraction of a program
- N: Number of processors
- Maximum speedup limited by serial portion: Serial bottleneck
- All parallel machines “suffer from” the serial bottleneck
- Speedup =
- 1
- +
- 1 - f
- f
- N
- Amdahl, “Validity of the single processor approach to achieving large scale computing capabilities,” AFIPS 1967.

## Slide 27: Vector Processor Limitations

### Extracted Shape Text
- Vector Processor Limitations
- -- Memory (bandwidth) can easily become a bottleneck, especially if
- 1. compute/memory operation balance is not maintained
- 2. data is not mapped appropriately to memory banks

## Slide 28: What needs us to do to support SIMD instructions?

### Extracted Shape Text
- What needs us to do to support SIMD instructions?

### Notes
- 现在的计算世界往三个方向发展
- 28

## Slide 29: Recall: MIPS State Elements

### Extracted Shape Text
- Recall: MIPS State Elements
- Program counter:
- 32-bit register
- Instruction memory:
- Takes input 32-bit address A and reads the 32-bit data (i.e., instruction) from that address to the read data output RD.
- Register file:
- The 32-element, 32-bit register file has 2 read ports and 1 write port
- Data memory:
- If the write enable, WE, is 1, it writes 32-bit data WD into memory location at 32-bit address A on the rising edge of the clock.
- If the write enable is 0, it reads 32-bit data from address A onto RD.
- This notation is used in H&H single-cycle MIPS implementation (H&H Chapter 7.3)

### Notes
- 29

## Slide 30: Recall: The Full MIPS Datapath

### Extracted Shape Text
- Recall: The Full MIPS Datapath
- **Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]
- JAL, JR, JALR omitted

## Slide 31: MIPS State Elements When Enabling SIMD

### Extracted Shape Text
- MIPS State Elements When Enabling SIMD
- Program counter:
- 32-bit register
- Instruction memory:
- Takes input 32-bit address A and reads the 32-bit data (i.e., instruction) from that address to the read data output RD.
- Register file (s):
- The 32-element, 32-bit register file has 2 read ports and 1 write port
- The 32-element, 128-bit register file has 2 read ports and 1 write port
- Data memory:
- If WE is 1, it writes 32-bit data WD into memory location at 32-bit address A. If WE1 = 1, writes 128-bit data WD1 to A1 address.
- This notation is used in H&H single-cycle MIPS implementation (H&H Chapter 7.3)
- What else parts needs to add?

### Notes
- 31
- EXE

## Slide 32: What will This Graph Be to Support Vector Insns?

### Extracted Shape Text
- What will This Graph Be to Support Vector Insns?
- VRF VALU VMemory

## Slide 33: Programmer Visible (Architectural) States

### Extracted Shape Text
- Programmer Visible (Architectural) States
- M[0]
- M[1]
- M[2]
- M[3]
- M[4]
- M[N-1]
- Memory:
- 1, array of storage locations
- indexed by an address;
- 2, Multiple bank design.
- Program Counter
- Registers:
- General purpose register file
- Vector register file
- Program Counter:
- memory address
- of the current (or next) instruction

## Slide 34: Roofline Model for SIMD CPU

### Extracted Shape Text
- Roofline Model for SIMD CPU

### Notes
- 34
- KB MB GB TB
- K M B T
- 1B=10
- 亿

## Slide 35: Outline

### Extracted Shape Text
- Outline
- Superscalar
- Vector Insn
- Multithreading
- Multi-core

## Slide 36: Fine-Grained Multithreading

### Extracted Shape Text
- Fine-Grained Multithreading

## Slide 37: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 38: Fine-Grained Multithreading

- Images: 1; Tables: 0

### Extracted Shape Text
- Fine-Grained Multithreading
- Idea: Hardware has multiple thread contexts (PC+registers). Each cycle, fetch engine fetches from a different thread.
- By the time the fetched branch/instruction resolves, no instruction is fetched from the same thread
- Branch/instruction resolution latency overlapped with execution of other threads’ instructions
- + No logic needed for handling control and
- data dependences within a thread
- -- Single thread performance suffers
- -- Extra logic for keeping thread contexts
- -- Does not overlap latency if not enough
- threads to cover the whole pipeline

### Notes
- Latency overlap/hiding
- 38

## Slide 39: Fine-Grained Multithreading (II)

### Extracted Shape Text
- Fine-Grained Multithreading (II)
- Idea: Switch to another thread every cycle such that no two instructions from a thread are in the pipeline concurrently
- Advantages：
- Tolerates the control and data dependency latencies by overlapping the latency with useful work from other threads
- Improves pipeline utilization by taking advantage of multiple threads
- Thornton, “Parallel Operation in the Control Data 6600,” AFIPS 1964.
- Smith, “A pipelined, shared resource MIMD computer,” ICPP 1978.

## Slide 40: Fine-Grained Multithreading: History

### Extracted Shape Text
- Fine-Grained Multithreading: History
- CDC 6600’s peripheral processing unit is fine-grained multithreaded
- Thornton, “Parallel Operation in the Control Data 6600,” AFIPS 1964.
- Processor executes a different I/O thread every cycle
- An operation from the same thread is executed every 10 cycles
- Denelcor HEP (Heterogeneous Element Processor)
- Smith, “A pipelined, shared resource MIMD computer,” ICPP 1978.
- 120 threads/processor
- Available queue vs. unavailable (waiting) queue for threads
- Each thread can have only 1 instruction in the processor pipeline; each thread independent
- For each thread, processor looks like a non-pipelined machine
- System throughput vs. single thread performance tradeoff

## Slide 41: Fine-Grained Multithreading in HEP

- Images: 2; Tables: 0

### Extracted Shape Text
- Fine-Grained Multithreading in HEP
- Cycle time: 100ns
- 8 stages  800 ns to complete an instruction
- assuming no memory access
- No control and data dependency checking
- Burton Smith
- (1941-2018)

## Slide 42: Multithreaded Pipeline Example

- Images: 1; Tables: 0

### Extracted Shape Text
- Multithreaded Pipeline Example
- Slide credit: Joel Emer

## Slide 43: Sun Niagara Multithreaded Pipeline

- Images: 1; Tables: 0

### Extracted Shape Text
- Sun Niagara Multithreaded Pipeline
- Kongetira et al., “Niagara: A 32-Way Multithreaded Sparc Processor,” IEEE Micro 2005.

## Slide 44: Fine-grained Multithreading

### Extracted Shape Text
- Fine-grained Multithreading
- Advantages
- + No need for dependency checking between instructions
- (only one instruction in pipeline from a single thread)
- + No need for branch prediction logic
- + Otherwise-bubble cycles used for executing useful instructions from different threads
- + Improved system throughput, latency tolerance, utilization
- Disadvantages
- - Extra hardware complexity: multiple hardware contexts (PCs, register files, …), thread selection logic
- - Reduced single thread performance (one instruction fetched every N cycles from the same thread)
- - Resource contention between threads in caches and memory
- - Some dependency checking logic between threads remains (load/store)

## Slide 45: Can multithreading tech affect the result in Roofline model?

### Extracted Shape Text
- Can multithreading tech affect the result in Roofline model?

### Notes
- 现在的计算世界往三个方向发展
- 45

## Slide 46: Outline

### Extracted Shape Text
- Outline
- Superscalar
- Vector Insn
- Multithreading
- Multi-core

## Slide 47: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 48: Multi-Core Processors

### Extracted Shape Text
- Multi-Core Processors

## Slide 49: Moore’s Law

- Images: 1; Tables: 0

### Extracted Shape Text
- Moore’s Law

### Notes
- 晶体管数量两年翻倍
- 49

## Slide 50: 50

- Images: 1; Tables: 0

### XML Text
- 50

## Slide 51: Gordon E. Moore Dies at 94

- Images: 1; Tables: 0

### Extracted Shape Text
- Gordon E. Moore Dies at 94
- Intel and the Gordon and Betty Moore Foundation announce that company co-founder Gordon Moore died on March 24, 2023, at the age of 94.

## Slide 52: Multi-Core

### Extracted Shape Text
- Multi-Core
- Idea: Put multiple cores on the same die.
- Technology scaling (Moore’s Law) enables more transistors to be placed on the same die area
- What else could you do with the die area you dedicate to multiple processors?
- Have a bigger, more powerful core
- Have larger caches in the memory hierarchy
- Simultaneous multithreading
- Integrate platform components on chip (e.g., network interface, memory controllers)

## Slide 53: Why Multi-Core?

### Extracted Shape Text
- Why Multi-Core?
- Alternative: Bigger, more powerful single core
- Larger superscalar issue width, larger instruction window, more execution units, large trace caches, large branch predictors, etc
- + Improves single-thread performance transparently to programmer, compiler;
- - Very difficult to design (Scalable algorithms for improving single-thread performance elusive);
- - Power hungry – many out-of-order execution structures consume significant power/area when scaled. Why?
- - Diminishing returns on performance;
- - Does not significantly help memory-bound application performance (Scalable algorithms for this elusive).

## Slide 54: Large Superscalar vs. Multi-Core

- Images: 1; Tables: 0

### Extracted Shape Text
- Large Superscalar vs. Multi-Core
- Olukotun et al., “The Case for a Single-Chip Multiprocessor,” ASPLOS 1996.
- Vs.
- Large Superscalar
- Multi-Core

## Slide 55: Multi-Core vs. Large Superscalar

### Extracted Shape Text
- Multi-Core vs. Large Superscalar
- Multi-core advantages
- + Simpler cores  more power efficient, lower complexity, easier to design and replicate, higher frequency (shorter wires, smaller structures)
- + Higher system throughput on multiprogrammed workloads  reduced context switches
- + Higher system throughput in parallel applications
- Multi-core disadvantages
- - Requires parallel tasks/threads to improve performance (parallel programming)
- - Resource sharing can reduce single-thread performance
- - Shared hardware resources need to be managed
- - Number of pins limits data supply for increased demand

## Slide 56: Why Multi-Core over Large Superscalar

### Extracted Shape Text
- Why Multi-Core over Large Superscalar
- Technology push
- Instruction issue queue size limits the cycle time of the superscalar, OoO processor  diminishing performance
- Quadratic increase in complexity with issue width
- Large, multi-ported register files to support large instruction windows and issue widths  more resources, reduced frequency or longer RF access, diminishing performance
- Application pull
- Multiple applications run on your CPU
- Olukotun et al., “The Case for a Single-Chip Multiprocessor,” ASPLOS 1996.

### Notes
- What does application pull mean?
- Cell phone use multiple cores…
- 56

## Slide 57: Comparison Points…

### Extracted Shape Text
- Comparison Points…

## Slide 58: Can multi-core tech affect the result in Roofline model?

### Extracted Shape Text
- Can multi-core tech affect the result in Roofline model?

### Notes
- 现在的计算世界往三个方向发展
- 58

## Slide 59: Can Multi-core CPU Increase Throughput?

### Extracted Shape Text
- Can Multi-core CPU Increase Throughput?

### Notes
- 59
- KB MB GB TB
- K M B T
- 1B=10
- 亿

## Slide 60: Multi-Core Evolution (An Early History)

### Extracted Shape Text
- Multi-Core Evolution (An Early History)

## Slide 61: Piranha Chip Multiprocessor

### Extracted Shape Text
- Piranha Chip Multiprocessor
- Barroso et al., “Piranha: A Scalable Architecture Based on Single-Chip Multiprocessing,” ISCA 2000.
- An early example of a symmetric multi-core processor
- Large-scale server based on CMP nodes
- Designed for commercial workloads
- Read:
- Barroso et al., “Memory System Characterization of Commercial Workloads,” ISCA 1998.
- Ranganathan et al., “Performance of Database Workloads on Shared-Memory Systems with Out-of-Order Processors,” ASPLOS 1998.

### Notes
- 61

## Slide 62: Commercial Workload Characteristics

### Extracted Shape Text
- Commercial Workload Characteristics
- Memory system is the main bottleneck
- Very high CPI
- Execution time dominated by memory stall times
- Instruction stalls as important as data stalls
- Fast/large L2 caches are critical
- Very poor Instruction Level Parallelism (ILP) with existing techniques
- Frequent hard-to-predict branches
- Large L1 miss ratios
- Small gains from wide-issue out-of-order techniques
- No need for floating point and multimedia units

## Slide 63: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- Alpha core:
- 1-issue, in-order,
- 500MHz
- CPU
- Next few slides from
- Luiz Barroso’s ISCA 2000 presentation of
- Piranha: A Scalable ArchitectureBased on Single-Chip Multiprocessing

### Notes
- 63

## Slide 64: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- D$
- I$

### Notes
- 64

## Slide 65: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- D$
- I$
- ICS
- CPU
- D$
- I$
- CPU
- D$
- I$
- CPU
- D$
- I$
- CPU
- D$
- I$
- CPU
- D$
- I$
- CPU
- D$
- I$
- CPU
- D$
- I$

### Notes
- 65

## Slide 66: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- L2 cache:
- shared, 1MB, 8-way
- D$
- I$
- L2$
- ICS
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$

### Notes
- 66

## Slide 67: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- L2 cache:
- shared, 1MB, 8-way
- Memory Controller (MC)
- RDRAM, 12.8GB/sec
- D$
- I$
- L2$
- ICS
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- 8 banks
- @1.6GB/sec

### Notes
- 67

## Slide 68: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- L2 cache:
- shared, 1MB, 8-way
- Memory Controller (MC)
- RDRAM, 12.8GB/sec
- Protocol Engines (HE & RE)
- prog., 1K instr.,
- even/odd interleaving
- D$
- I$
- L2$
- ICS
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- RE
- HE

### Notes
- 68

## Slide 69: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- L2 cache:
- shared, 1MB, 8-way
- Memory Controller (MC)
- RDRAM, 12.8GB/sec
- Protocol Engines (HE & RE):
- prog., 1K instr.,
- even/odd interleaving
- System Interconnect:
- 4-port Xbar router
- topology independent
- 32GB/sec total bandwidth
- D$
- I$
- L2$
- ICS
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- RE
- HE
- Router
- 4 Links
- @ 8GB/s

### Notes
- 69

## Slide 70: Piranha Processing Node

- Images: 15; Tables: 0

### Extracted Shape Text
- Piranha Processing Node
- CPU
- Alpha core:
- 1-issue, in-order,
- 500MHz
- L1 caches:
- I&D, 64KB, 2-way
- Intra-chip switch (ICS)
- 32GB/sec, 1-cycle delay
- L2 cache:
- shared, 1MB, 8-way
- Memory Controller (MC)
- RDRAM, 12.8GB/sec
- Protocol Engines (HE & RE):
- prog., 1K instr.,
- even/odd interleaving
- System Interconnect:
- 4-port Xbar router
- topology independent
- 32GB/sec total bandwidth
- D$
- I$
- L2$
- ICS
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- L2$
- L2$
- CPU
- D$
- I$
- L2$
- CPU
- D$
- I$
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- MEM-CTL
- RE
- HE
- Router
- Single Chip

### Notes
- 70

## Slide 71: Piranha Processing Node

- Images: 1; Tables: 0

### Extracted Shape Text
- Piranha Processing Node

## Slide 72: Inter-Node Coherence Protocol Engine

### Extracted Shape Text
- Inter-Node Coherence Protocol Engine

## Slide 73: Piranha System

### Extracted Shape Text
- Piranha System

## Slide 74: Piranha I/O Node

### Extracted Shape Text
- Piranha I/O Node

## Slide 75: Sun Niagara (UltraSPARC T1)

- Images: 1; Tables: 0

### Extracted Shape Text
- Sun Niagara (UltraSPARC T1)
- Kongetira et al., “Niagara: A 32-Way Multithreaded SPARC Processor,” IEEE Micro 2005.

## Slide 76: Niagara Core

- Images: 1; Tables: 0

### Extracted Shape Text
- Niagara Core
- 4-way fine-grain multithreaded, 6-stage, dual-issue in-order
- Round robin thread selection (unless cache miss)
- Shared FP unit among cores

## Slide 77: Niagara Design Point

- Images: 2; Tables: 0

### Extracted Shape Text
- Niagara Design Point
- Also designed for commercial applications

## Slide 78: Sun Niagara II (UltraSPARC T2)

### Extracted Shape Text
- Sun Niagara II (UltraSPARC T2)
- 8 SPARC cores, 8 threads/core. 8 stages. 16 KB I$ per Core. 8 KB D$ per Core. FP, Graphics, Crypto, units per Core.
- 4 MB Shared L2, 8 banks, 16-way set associative.
- 4 dual-channel FBDIMM memory controllers.
- X8 PCI-Express @ 2.5 Gb/s.
- Two 10G Ethernet ports @ 3.125 Gb/s.

## Slide 79: Chip Multithreading (CMT)

### Extracted Shape Text
- Chip Multithreading (CMT)
- Spracklen and Abraham, “Chip Multithreading: Opportunities and Challenges,” HPCA Industrial Session, 2005.
- Idea: Chip multiprocessor where each core is multithreaded
- Niagara 1/2: fine grained multithreading
- IBM POWER5: simultaneous multithreading
- Motivation: Tolerate memory latency better
- A simple core stays idle on a cache miss
- Multithreading enables tolerating cache miss latency when there is TLP

## Slide 80: CMT (CMP + MT) vs. CMP

### Extracted Shape Text
- CMT (CMP + MT) vs. CMP
- Advantages of adding multithreading to each core
- + Better memory latency tolerance when there are enough threads
- + Fine grained multithreading can simplify core design (no need for branch prediction, dependency checking)
- + Potentially better utilization of core, cache, memory resources
- + Shared instructions and data among threads not replicated
- + When one thread is not using a resource, another can
- Disadvantages
- - Reduced single-thread performance (a thread does not have the core and L1 caches to itself)
- - More pressure on the shared resources (cache, off-chip bandwidth)  more resource contention
- - Applications with limited TLP do not benefit

## Slide 81: Sun ROCK

### Extracted Shape Text
- Sun ROCK
- Chaudhry et al., “Rock: A High-Performance Sparc CMT Processor,” IEEE Micro, 2009.
- Chaudhry et al., “Simultaneous Speculative Threading: A Novel Pipeline Architecture Implemented in Sun's ROCK Processor,” ISCA 2009
- Goals:
- Maximize throughput when threads are available
- Boost single-thread performance when threads are not available and on cache misses
- Ideas:
- Runahead on a cache miss  ahead thread executes miss-independent instructions, behind thread executes dependent instructions
- Branch prediction (gshare)

## Slide 82: Sun ROCK

- Images: 1; Tables: 0

### Extracted Shape Text
- Sun ROCK
- 16 cores, 2 threads per core (fewer threads than Niagara 2)
- 4 cores share a 32KB instruction cache
- 2 cores share a 32KB data cache
- 2MB L2 cache (smaller than Niagara 2)

## Slide 83: Sun ROCK Cores

### Extracted Shape Text
- Sun ROCK Cores
- Load miss in L1 cache starts parallelization using 2 HW threads
- Ahead thread
- Checkpoints state and executes speculatively
- Instructions independent of load miss are speculatively executed
- Load miss(es) and dependent instructions are deferred to behind thread
- Behind thread
- Executes deferred instructions and re-defers them if necessary
- Memory-Level Parallelism (MLP)
- Run ahead on load miss and generate additional load misses
- Instruction-Level Parallelism (ILP)
- Ahead and behind threads execute independent instructions from different points in program in parallel

## Slide 84: ROCK Pipeline

- Images: 1; Tables: 0

### Extracted Shape Text
- ROCK Pipeline

## Slide 85: More Powerful Cores in Sun ROCK

### Extracted Shape Text
- More Powerful Cores in Sun ROCK
- Advantages
- + Higher single-thread performance (MLP + ILP)
- + Better cache miss tolerance  Can reduce on-chip cache sizes
- Disadvantages
- - Bigger cores  Fewer cores  Lower parallel throughput (in terms of threads).
- How about each thread’s response time?
- - More complex than Niagara cores (but simpler than conventional out-of-order execution)  Longer design time?

## Slide 86: More Powerful Cores in Sun ROCK

- Images: 1; Tables: 0

### Extracted Shape Text
- More Powerful Cores in Sun ROCK
- Chaudhry talk, Aug 2008.

## Slide 87: More Powerful Cores in Sun ROCK

- Images: 1; Tables: 0

### Extracted Shape Text
- More Powerful Cores in Sun ROCK
- Chaudhry et al., “Simultaneous Speculative Threading: A Novel Pipeline Architecture Implemented in Sun's ROCK Processor,” ISCA 2009

## Slide 88: IBM POWER4

- Images: 2; Tables: 0

### Extracted Shape Text
- IBM POWER4
- Tendler et al., “POWER4 system microarchitecture,” IBM J R&D, 2002.
- Another symmetric multi-core chip…
- But, fewer and more powerful cores

## Slide 89: IBM POWER4

### Extracted Shape Text
- IBM POWER4
- 2 cores, out-of-order execution
- 100-entry instruction window in each core
- 8-wide instruction fetch, issue, execute
- Large, local+global hybrid branch predictor
- 1.5MB, 8-way L2 cache
- Aggressive stream based prefetching

## Slide 90: IBM POWER5

- Images: 1; Tables: 0

### Extracted Shape Text
- IBM POWER5
- Kalla et al., “IBM Power5 Chip: A Dual-Core Multithreaded Processor,” IEEE Micro 2004.

## Slide 91: IBM POWER6

- Images: 1; Tables: 0

### Extracted Shape Text
- IBM POWER6
- Le et al., “IBM POWER6 microarchitecture,” IBM J R&D, 2007.
- 2 cores, in order, high frequency (4.7 GHz)
- 8 wide fetch
- Simultaneous multithreading in each core
- Runahead execution in each core
- Similar to Sun ROCK

## Slide 92: IBM POWER7

### Extracted Shape Text
- IBM POWER7
- Kalla et al., “Power7: IBM’s Next-Generation Server Processor,” IEEE Micro 2010.
- 8 out-of-order cores, 4-way SMT in each core
- TurboCore mode
- Can turn off cores so that other cores can be run at higher frequency

## Slide 93: Large vs. Small Cores

### Extracted Shape Text
- Large vs. Small Cores
- Out-of-order
- Wide fetch e.g. 4-wide
- Deeper pipeline
- Aggressive branch predictor (e.g. hybrid)
- Multiple functional units
- Trace cache
- Memory dependence speculation
- In-order
- Narrow Fetch e.g. 2-wide
- Shallow pipeline
- Simple branch predictor (e.g. Gshare)
- Few functional units
- LargeCore
- SmallCore
- Large Cores are power inefficient:e.g., 2x performance for 4x area (power)

## Slide 94: Large vs. Small Cores

- Images: 1; Tables: 0

### Extracted Shape Text
- Large vs. Small Cores
- Grochowski et al., “Best of both Latency and Throughput,” ICCD 2004.

## Slide 95: Tile-Large Approach

### Extracted Shape Text
- Tile-Large Approach
- Tile a few large cores
- IBM Power 5, AMD Barcelona, Intel Core2Quad, Intel Nehalem
- + High performance on single thread, serial code sections (2 units)
- - Low throughput on parallel program portions (8 units)
- Largecore
- Largecore
- Large
- core
- Largecore
- “Tile-Large”

## Slide 96: Tile-Small Approach

### Extracted Shape Text
- Tile-Small Approach
- Tile many small cores
- Sun Niagara, Intel Larrabee, Tilera TILE (tile ultra-small)
- + High throughput on the parallel part (16 units)
- - Low performance on the serial part, single thread (1 unit)
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- “Tile-Small”

## Slide 97: Can We Get the Best of Both worlds?

### Extracted Shape Text
- Can We Get the Best of Both worlds?
- Tile Large
- + High performance on single thread, serial code sections (2 units)
- - Low throughput on parallel program portions (8 units)
- Tile Small
- + High throughput on the parallel part (16 units)
- - Low performance on the serial part, single thread (1 unit), reduced single-thread performance compared to existing single thread processors
- Idea: Have both large and small on the same chip  Performance asymmetry

## Slide 98: Asymmetric Chip Multiprocessor (ACMP)

### Extracted Shape Text
- Asymmetric Chip Multiprocessor (ACMP)
- Provide one large core and many small cores
- + Accelerate serial part using the large core (2 units)
- + Execute parallel part on all cores for high throughput (14 units)
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Large
- core
- ACMP
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- Smallcore
- “Tile-Small”
- Largecore
- Largecore
- Large
- core
- Largecore
- “Tile-Large”
