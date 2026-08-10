# 2-pipelining-reorder-buffer.pptx

- Slides: 82

## Slide 1: Computer Arch. & AI ChipLecture 2: Pipeline Hazard +Reorder Buffer

### Extracted Shape Text
- Computer Arch. & AI ChipLecture 2: Pipeline Hazard +Reorder Buffer
- Prof. Zeke Wang
- Zhejiang University
- 09 March 2026

### Notes
- 1

## Slide 2: Recall: Axiom

### Extracted Shape Text
- Recall: Axiom
- To achieve the highest energy efficiency and performance:
- we must take the expanded view
- of LLM system
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

## Slide 3: Recall: Amdahl’s Law

### Extracted Shape Text
- Recall: Amdahl’s Law
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

## Slide 4: Recall: Key Term in Roofline Model

### Extracted Shape Text
- Recall: Key Term in Roofline Model
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
- 4

## Slide 5: Recall: Roofline Model’s 3 Steps

### Extracted Shape Text
- Recall: Roofline Model’s 3 Steps
- Roofline model’s 3 Steps:
- 1, Machine characterization:
- Memory bandwidth,
- Peak compute;
- 2, Application Characterization:
- Arithmetic intensity;
- 3, Application execution monitoring:
- Real Throughput
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009

### Notes
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 5

## Slide 6: Recall: Little’s Law：Intuition

- Images: 1; Tables: 0

### Extracted Shape Text
- Recall: Little’s Law：Intuition
- Image the services provided by counters in the bank.
- Arrival rate: one customer/min;
- Counter’s average serve time: 6 mins;
- Question: how many counters are needed for people who need the service? (Cond: The customer will leave if no counter is available. )
- Answer: 6 counters (one slot for one person, then no customer will leave).
- How many Counters?
- Arrival rate: one person/min
- Average service time: 6 mins

### Notes
- 这里server不太合理
- 6

## Slide 7: Recall: Little’s Law Used in Memory Subsystem

### Extracted Shape Text
- Recall: Little’s Law Used in Memory Subsystem
- Little’s law is widely used in hardware design whose latency is larger than one cycle, e.g., memory subsystem:
- Throughput: 12GB/s;
- Latency: 100ns;
- Buffer Size (concurrency):
- 100ns * 12GB/s = 1200B
- Memory
- Throughput: 12GB/s
- Latency: ~100ns
- Buffer
- Concurrency = Latency * Throughput

## Slide 8: Recall von Neumann Model: Key Properties

### Extracted Shape Text
- Recall von Neumann Model: Key Properties
- Von Neumann model is also called stored program computer (instructions in memory).
- von Neumann Model has two key properties:
- 1，Stored program
- Instructions stored in a linear memory array
- Memory is unified between instructions and data
- The interpretation of a stored value depends on the control signals
- 2，Sequential instruction processing
- One instruction processed (fetched, executed, completed) at a time
- Program counter (instruction pointer) identifies the current instruction
- Program counter is advanced sequentially except for control transfer instructions

### Notes
- Every application can be descripted by this complete design von Neumann
- 8

## Slide 9: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 10: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 11: Pipeline hazards

### Extracted Shape Text
- Pipeline hazards
- A hazard is a condition that prevents an instruction in the pipeline from executing its next scheduled pipeline stage.
- Taxonomy of hazard:
- Structural hazards
- Conflict due to limited hardware resources
- Data hazards
- Instruction depends on result of a prior instruction which is not ready (computed or stored) yet
- Control hazards
- Not able to fetch the next instruction for the next clock due to unsolved branch condition or unavailable branch.

## Slide 12: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 13: Structural hazard

### Extracted Shape Text
- Structural hazard
- Structural hazard
- Reason: Occurs when two or more instructions try to use the same hardware resource in the same cycle.
- Outcome: Causes bubble (stall) in a pipelined CPU.
- Solution: Can be overcome by replicating hardware resources
- Multiple accesses to the register file
- Multiple accesses to memory
- Fully pipeline the functional unit

## Slide 14: Structural Hazard: Multi Ports of Register File

### Extracted Shape Text
- Structural Hazard: Multi Ports of Register File
- Condition of Register file to avoid structural hazard?
- Allows concurrently two reads and one write to avoid structural hazard regarding register file.

### Notes
- 下面，从寄存器文件来说结构冲突：多少个读口，多少个写口才能解决冲突？
- 答案：两个读口 一个写口
- Generalization
- ：硬件设计需要满足最坏
- 的情况
- 14

## Slide 15: Instruction and Data Memory Ports Split

### Extracted Shape Text
- Instruction and Data Memory Ports Split
- Structural hazard regarding memory?
- Solution: Split instruction and data memory
- Fetch the instruction and data using different memory ports, rather than contenting for the same port.
- IM
- I
- n
- s
- t
- r.
- O
- r
- d
- e
- r
- Time (clock cycles)
- Ld/St
- Instr 1
- Instr 2
- Instr 3
- ALU
- IM
- Reg
- DM
- Reg
- ALU
- IM
- Reg
- DM
- Reg
- ALU
- IM
- Reg
- DM
- Reg
- ALU
- Reg
- DM
- Reg

### Notes
- 15

## Slide 16: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 17: Data Dependences

### Extracted Shape Text
- Data Dependences
- Three Types of data dependences
- Flow dependence (read after write – true data dependence)
- Output dependence (write after write)
- Anti dependence (write after read)
- Which ones cause stalls in a pipelined machine?
- Assumption: we need to ensure semantics of the program is correct.
- Flow dependences always need to be obeyed because they constitute true dependence on a register
- Anti and output dependences exist due to limited number of architectural registers.
- Essentially, insns are dependent on a name, not a value.

## Slide 18: Data Dependence Types

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

## Slide 19: How to Handle Data Dependences

### Extracted Shape Text
- How to Handle Data Dependences
- Anti and output dependences
- They are easier to handle.
- Write to the destination only in last stage and in program order
- Handling flow dependences:
- Hardware Pipeline Stall:
- Detect and wait until value is available in register file
- Software Pipeline Stall:
- Detect and eliminate the dependence at the software level
- No need for the hardware to detect dependence
- Data Forward/Bypass:
- Detect and forward/bypass data to dependent instruction

## Slide 20: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 21: Remember: Data Dependence Types

### Extracted Shape Text
- Remember: Data Dependence Types
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

## Slide 22: RAW Data Dependence: Example

### Extracted Shape Text
- RAW Data Dependence: Example
- One instruction writes a register ($s0) and next instructions read this register => read after write (RAW) dependence.
- add writes into $s0 in the first half of cycle 5
- and reads $s0 on cycle 3, obtaining the wrong value
- or reads $s0 on cycle 4, again obtaining the wrong value
- sub reads $s0 in 2nd half of cycle 5, getting the correct value
- subsequent instructions read the correct value of $s0
- Only if the pipeline handles
- data dependences incorrectly!

### Notes
- 22

## Slide 23: How to Handle Data Dependences

### Extracted Shape Text
- How to Handle Data Dependences
- Anti and output dependences
- They are easier to handle.
- Write to the destination only in last stage and in program order
- Handling flow dependences:
- Hardware Pipeline Stall:
- Detect and wait until value is available in register file
- Software Pipeline Stall:
- Detect and eliminate the dependence at the software level
- No need for the hardware to detect dependence
- Data Forward/Bypass:
- Detect and forward/bypass data to dependent instruction

## Slide 24: Hardware Pipeline Stall for Flow Dependency

### Extracted Shape Text
- Hardware Pipeline Stall for Flow Dependency
- The simplest way to "fix" flow dependency is to stall the pipeline.
- A pipeline stall, called a pipeline bubble or simply bubble.
- What does a pipeline stall do to:
- Previous instructions: go on proceeding in the pipeline.
- Following instructions: stalled in the pipeline by one or more clock cycles until the waiting register is ready.
- New instructions: Not fetched during a pipeline stall.

## Slide 25: Hardware Pipeline Stall: An Example

### Extracted Shape Text
- Hardware Pipeline Stall: An Example
- Issue: dependency regarding register ra
- Solution: hardware pipeline stalls the second insn until the first insn. writes the latest value of ra back.
- MEM
- WB
- IF
- ID
- IF
- EX
- ID
- MEM
- EX
- WB
- addi ra r- -
- subi r- ra -
- MEM
- IF
- ID
- EX
- IF
- ID
- EX
- IF
- ID
- IF
- subi r- ra -
- subi r- ra -
- subi r- ra -
- subi r- ra -
- ?

### Notes
- 25

## Slide 26: Pipeline Stall: Resolving Data Dependence

### Extracted Shape Text
- Pipeline Stall: Resolving Data Dependence
- IF
- WB
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- t0
- t1
- t2
- t3
- t4
- t5
- IF
- ID
- MEM
- IF
- ID
- ALU
- IF
- ID
- Insti
- Instj
- Instk
- Instl
- WB
- WB
- i: rx  _
- j: _  rx dist(i,j)=1
- i
- j
- Insth
- WB
- MEM
- ALU
- i: rx  _
- bubble
- j: _  rx dist(i,j)=2
- WB
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- t0
- t1
- t2
- t3
- t4
- t5
- MEM
- Insti
- Instj
- Instk
- Instl
- WB
- WB
- i
- j
- Insth
- ID
- IF
- IF
- IF
- ID
- ALU
- IF
- ID
- i: rx  _
- bubble
- bubble
- j: _  rx dist(i,j)=3
- IF
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- IF
- ID
- t0
- t1
- t2
- t3
- t4
- t5
- IF
- MEM
- ALU
- ID
- Insti
- Instj
- Instk
- Instl
- WB
- WB
- i
- j
- Insth
- ID
- IF
- ID
- IF
- i: rx  _
- bubble
- bubble
- bubble
- j: _  rx dist(i,j)=4
- IF
- IF
- ID
- ALU
- MEM
- IF
- ID
- ALU
- MEM
- IF
- ID
- IF
- t0
- t1
- t2
- t3
- t4
- t5
- ALU
- ID
- Insti
- Instj
- Instk
- Instl
- WB
- WB
- i
- j
- Insth
- ID
- IF
- ID
- IF
- ID
- IF
- Pipeline stall = make the dependent instruction
- wait until its source data value is available.
- 1. stop all up-stream stages,
- 2. drain all down-stream stages.

## Slide 27: How to Implement Stalling in Pipeline?

- Images: 1; Tables: 0

### Extracted Shape Text
- How to Implement Stalling in Pipeline?
- Pipeline stalling:
- Disables PC and IF/ID latching; ensure stalled instruction stays in its stage
- Pushs a bubble into next stage: Bubble = 1 and disables control signal Wreg and Wmem; Puch a nop forward into ID/EX.
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 28: Hardware Needed for Stalling

### Extracted Shape Text
- Hardware Needed for Stalling
- Stalls are supported by the following hardware:
- adding enable inputs (EN) to the Fetch and Decode pipeline registers
- and a synchronous reset/clear (CLR) input to the Execute pipeline register
- or an INV bit associated with each pipeline register, indicating that contents are INValid
- When a lw stall occurs
- StallD and StallF are asserted to force the Decode and Fetch stage pipeline registers to hold their old values.
- FlushE is also asserted to clear the contents of the Execute stage pipeline register, introducing a bubble

### Notes
- 28

## Slide 29: Stalling and Dependence Detection Hardware

### Extracted Shape Text
- Stalling and Dependence Detection Hardware

### Notes
- 29

## Slide 30: How to Handle Data Dependences

### Extracted Shape Text
- How to Handle Data Dependences
- Anti and output dependences
- They are easier to handle.
- Write to the destination only in last stage and in program order
- Handling flow dependences:
- Hardware Pipeline Stall:
- Detect and wait until value is available in register file
- Software Pipeline Stall:
- Detect and eliminate the dependence at the software level
- No need for the hardware to detect dependence
- Data Forward/Bypass:
- Detect and forward/bypass data to dependent instruction

## Slide 31: Compile-Time Detection and Elimination

### Extracted Shape Text
- Compile-Time Detection and Elimination
- Insert enough NOPs for the required result to be ready
- Or (if you can) move independent useful instructions up
- Reorder/reschedule instructions at the compiler level

## Slide 32: What is the issue of issuing NOPs from the compiler?

### Extracted Shape Text
- What is the issue of issuing NOPs from the compiler?
- Insn’s latency varies, based on the context.

### Notes
- The majority of you will not work on Systems.
- But you should know the key principles that help you understand the system on which your AI task runs.
- Our course has to include both computer architecture and AI chip courses.
- 32

## Slide 33: More on Software vs. Hardware

### Extracted Shape Text
- More on Software vs. Hardware
- Software based scheduling of instructions  static scheduling
- Compiler orders the instructions, hardware executes them in that order
- Contrast this with dynamic scheduling (in which hardware can execute instructions out of the compiler-specified order)
- How does the compiler know the latency of each instruction?
- What information does the compiler not know that makes static scheduling difficult?
- Answer: Anything that is determined at run time
- Variable-length operation latency, memory addr, branch direction
- How can the compiler alleviate this (i.e., estimate the unknown)?
- Answer: Profiling

## Slide 34: How to Handle Data Dependences

### Extracted Shape Text
- How to Handle Data Dependences
- Anti and output dependences
- They are easier to handle.
- Write to the destination only in last stage and in program order
- Handling flow dependences:
- Hardware Pipeline Stall:
- Detect and wait until value is available in register file
- Software Pipeline Stall:
- Detect and eliminate the dependence at the software level
- No need for the hardware to detect dependence
- Data Forward/Bypass:
- Detect and forward/bypass data to dependent instruction

## Slide 35: Data Forwarding

### Extracted Shape Text
- Data Forwarding
- Data Forwarding (called Data Bypassing)
- Forwards the result value to the dependent instruction as soon as the value is available.
- Act like Dataflow?
- Data value supplied to dependent instruction as soon as it is available.
- Instruction executes when all its operands are available.
- Data forwarding brings a pipeline closer to dataflow execution principles.

## Slide 36: Data Forwarding

### Extracted Shape Text
- Data Forwarding

### Notes
- 36
- 关于
- s0
- 有依赖。。。第一条写，后面读。。。

## Slide 37: Data Forwarding

### Extracted Shape Text
- Data Forwarding

### Notes
- 37
- Rse
- rte
- 是对应的读寄存器，
- regwriteM
- memory stage
- regwriteW
- write back stage

## Slide 38: Data Forwarding

### Extracted Shape Text
- Data Forwarding
- Forward to Execute stage from either:
- Memory stage or
- Writeback stage
- When should we forward from either Memory or Writeback stage?
- Answer：If that stage will write to a destination register and the destination register matches the source register.
- If both the Memory and Writeback stages contain matching destination registers?
- Answer： The Memory stage should have priority, because it contains the more recently executed instruction.

### Notes
- 38

## Slide 39: Data Forwarding (in Pseudocode)

### Extracted Shape Text
- Data Forwarding (in Pseudocode)
- Forward to Execute stage from either:
- Memory stage or
- Writeback stage
- Forwarding logic for ForwardAE (pseudo code):
- if ((rsE != 0) AND (rsE == WriteRegM) AND RegWriteM) then ForwardAE = 10 # forward from Memory stageelse if ((rsE != 0) AND (rsE == WriteRegW) AND RegWriteW) then ForwardAE = 01 # forward from Writeback stageelse ForwardAE = 00 # no forwarding
- Forwarding logic for ForwardBE same, but replace rsE with rtE

### Notes
- 39
- A B
- 是两个不同操作数

## Slide 40: Forwarding Is Not Always Possible

### Extracted Shape Text
- Forwarding Is Not Always Possible
- Forwarding is sufficient to resolve RAW data dependences
- Unfortunately, there are cases when forwarding is not possible
- Due to pipeline design and instruction latencies
- The lw instruction does not finish reading data until the end of the Memory stage
-  its result cannot be forwarded to the Execute stage of the next instruction

### Notes
- 40
- 本质上：把一个周期变成两个部分，第一部分结束
- --》
- 第二部分开始。

## Slide 41: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 42: Control Dependence

### Extracted Shape Text
- Control Dependence
- Control dependence
- Data dependence on the Instruction Pointer / Program Counter

## Slide 43: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 44: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 45: Review: Single-Cycle MIPS FSM

### Extracted Shape Text
- Review: Single-Cycle MIPS FSM
- Single-cycle machine
- AS
- Sequential
- Logic
- (State)
- Combinational
- Logic
- AS’
- AS: Architectural State

## Slide 46: Review: Multi-Cycle MIPS FSM

### Extracted Shape Text
- Review: Multi-Cycle MIPS FSM
- What is the shortcoming of
- this design?
- What does
- this design
- assume
- about memory?

## Slide 47: Recall: Illustrating Pipeline Operation

- Images: 0; Tables: 1

### Extracted Shape Text
- Recall: Illustrating Pipeline Operation
- I0
- I0
- I1
- I0
- I1
- I2
- I0
- I1
- I2
- I3
- I0
- I1
- I2
- I3
- I4
- I1
- I2
- I3
- I4
- I5
- I2
- I3
- I4
- I5
- I6
- I3
- I4
- I5
- I6
- I7
- I4
- I5
- I6
- I7
- I8
- I5
- I6
- I7
- I8
- I9
- I6
- I7
- I8
- I9
- I10

|  | t0 | t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 | t9 | t10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IF |  |  |  |  |  |  |  |  |  |  |  |
| ID |  |  |  |  |  |  |  |  |  |  |  |
| EX |  |  |  |  |  |  |  |  |  |  |  |
| MEM |  |  |  |  |  |  |  |  |  |  |  |
| WB |  |  |  |  |  |  |  |  |  |  |  |


## Slide 48: Recall: Pipelined Control

### Extracted Shape Text
- Recall: Pipelined Control
- Same control unit as single-cycle processorControl delayed to proper pipeline stage

## Slide 49: Recall: Data Dependence Types

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

## Slide 50: Recall: How to Handle Data Dependences

### Extracted Shape Text
- Recall: How to Handle Data Dependences
- Anti and output dependences
- They are easier to handle.
- Write to the destination only in last stage and in program order
- Handling flow dependences:
- Hardware Pipeline Stall:
- Detect and wait until value is available in register file
- Software Pipeline Stall:
- Detect and eliminate the dependence at the software level
- No need for the hardware to detect dependence
- Data Forward/Bypass:
- Detect and forward/bypass data to dependent instruction

## Slide 51: Pipelined CPU: Ideal vs. Realistic

### Extracted Shape Text
- Pipelined CPU: Ideal vs. Realistic
- Ideal pipelined CPU has：
- One pipeline
- Fixed latency
- Dependency is known at compiler time
- no support for exception/interrupt
- Realistic Pipelined CPU has:
- Multiple pipelines with different latencies
- Unpredictable latency
- Unknown dependency at compiler time
- Support for exception/interrupt

## Slide 52: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 53: Multi-Cycle Execution

### Extracted Shape Text
- Multi-Cycle Execution
- Multi-Cycle Execution： Not all instructions take the same amount of time for “execution”.
- Question: How to address multi-cycle execution issue?
- Answer: Have multiple different functional units that take different number of cycles
- Can let independent instructions start execution on a different functional unit before a previous long-latency instruction finishes execution
- F
- D
- E
- ?
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

## Slide 54: Example of Multi-Cycle Execution

### Extracted Shape Text
- Example of Multi-Cycle Execution
- Instructions take different number of cycles in EXECUTE stage
- Integer ADD (1 cycle) versus Integer DIVide (8 cycles)
- What is wrong with this picture in a Von Neumann architecture?
- Sequential semantics of the ISA NOT preserved!
- F
- D
- E
- W
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
- DIV R4  R1, R2
- ADD R3  R1, R2
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
- DIV R2  R5, R6
- ADD R7  R5, R6
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
- ……

## Slide 55: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 56: Exceptions and Interrupts

### Extracted Shape Text
- Exceptions and Interrupts
- “Unplanned” changes or interruptions in program execution
- Exceptions: Due to internal problems in execution of the program
- Interrupts: Due to external events that need to be handled by the processor
- Both exceptions and interrupts require
- 1, stopping of the current program
- 2, saving the architectural state
- 3, handling the exception/interrupt  switch to handler
- 4, return back to program execution (if possible and makes sense)

## Slide 57: Exceptions vs. Interrupts

### Extracted Shape Text
- Exceptions vs. Interrupts
- Cause
- Exceptions: internal to the running thread
- Interrupts: external to the running thread
- When to Handle
- Exceptions: when detected (and known to be non-speculative)
- Interrupts: when convenient
- Except for very high priority ones
- Power failure
- Machine check (error)

### Notes
- I
- nterrupt: machine check
- 57

## Slide 58: Precise Exceptions/Interrupts

### Extracted Shape Text
- Precise Exceptions/Interrupts
- The architectural state should be consistent (precise) when the exception/interrupt is ready to be handled
- 1. All previous instructions should be completely retired.
- 2. No later instruction should be retired.
- Retire = commit = finish execution and update arch. state

### Notes
- 意外、中断处理：之前的指令完成，后面的指令还未更新到寄存器等系统状态内。
- 58

## Slide 59: Checking for and Handling Exceptions in Pipelining

### Extracted Shape Text
- Checking for and Handling Exceptions in Pipelining
- When the oldest instruction ready-to-be-retired is detected to have caused an exception, the control logic
- 1，Ensures architectural state is precise (register file, PC, memory)
- 2，Flushes all younger instructions in the pipeline
- 3，Saves PC and registers (as specified by the ISA)
- 4，Redirects the fetch engine to the appropriate exception handling routine

## Slide 60: Why Do We Want Precise Exceptions?

### Extracted Shape Text
- Why Do We Want Precise Exceptions?
- Four Goals of Precise Exception:
- 1. Keeps the semantics of the von Neumann model
- 2. Aids software debugging
- 3. Enables (easy) recovery from exceptions
- 4. Enables traps into software (e.g., software implemented opcodes)

### Notes
- T
- rap: opcode not software emulate the opcode…
- 60

## Slide 61: Ensuring Precise Exceptions

### Extracted Shape Text
- Ensuring Precise Exceptions
- Easy to do in single-cycle and multi-cycle machines
- Single-cycle
- Instruction boundaries == Cycle boundaries
- Multi-cycle
- Add special states in the control FSM that lead to the exception or interrupt handlers
- Switch to the handler only at a precise state  before fetching the next instruction
- See H&H Section 7.7 for a treatment of exceptions in multi-cycle uarch

## Slide 62: Precise Exceptions in Multi-Cycle FSM

- Images: 1; Tables: 0

### Extracted Shape Text
- Precise Exceptions in Multi-Cycle FSM

### Notes
- S1
- 62

## Slide 63: Precise Exceptions in Multi-Cycle Datapath

- Images: 1; Tables: 0

### Extracted Shape Text
- Precise Exceptions in Multi-Cycle Datapath
- See H&H Section 7.7 for a treatment of exceptions in multi-cycle uarch

## Slide 64: Ensuring Precise Exceptions in Pipelining

### Extracted Shape Text
- Ensuring Precise Exceptions in Pipelining
- Idea: Make each operation take the same amount of time
- Downside:
- Worst-case instruction latency determines all instructions’ latency
- What about memory operations?
- Each functional unit takes worst-case number of cycles?
- F
- D
- E
- W
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
- E
- E
- DIV R3  R1, R2
- ADD R4  R1, R2

### Notes
- 第一种：摆烂
- 64

## Slide 65: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 66: False Dependencies: Lack of registers

### Extracted Shape Text
- False Dependencies: Lack of registers
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

## Slide 67: Pipelining and Precise Exceptions: Preserving Sequential Semantics

### Extracted Shape Text
- Pipelining and Precise Exceptions: Preserving Sequential Semantics

### Notes
- 67

## Slide 68: Outline

### Extracted Shape Text
- Outline
- Pipeline Hazard
- Structural Hazard
- Data Hazard (Dependencies)
- RAW
- WAW
- WAR
- Control Hazard
- Reorder Buffer
- For Multi-cycle Execution
- For Exception and Interrupt
- For False Dependencies (WAW & WAR)
- Definition of Reorder Buffer

## Slide 69: Reorder Buffer

### Extracted Shape Text
- Reorder Buffer
- Reorder buffer
- For false dependencies
- For exception and interrupt
- For multi-cycle execute
- Suggested reading
- Smith and Plezskun, “Implementing Precise Interrupts in Pipelined Processors,” IEEE Trans on Computers 1988 and ISCA 1985.

## Slide 70: Reorder Buffer (ROB)

### Extracted Shape Text
- Reorder Buffer (ROB)
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
- 70

## Slide 71: Reorder buffer类似临时工，没编制。

### Extracted Shape Text
- Reorder buffer类似临时工，没编制。
- 出问题就怪临时工。

### Notes
- The majority of you will not work on Systems.
- But you should know the key principles that help you understand the system on which your AI task runs.
- Our course has to include both computer architecture and AI chip courses.
- 71

## Slide 72: What’s in a ROB Entry?

### Extracted Shape Text
- What’s in a ROB Entry?
- ROBs need to:
- 1, correctly reorder instructions back into the program order
- 2, update the architectural state with the instruction’s result(s), if instruction can retire without any issues
- 3, handle an exception/interrupt precisely, if an exception/interrupt needs to be handled before retiring the instruction
- 4, use valid bits to keep track of readiness of the result(s) and find out if the instruction has completed execution
- V
- DestRegID
- DestRegVal
- StoreAddr
- StoreData
- PC
- Valid bits for reg/data + control bits
- Exception?

## Slide 73: Reorder Buffer: Independent Operations

### Extracted Shape Text
- Reorder Buffer: Independent Operations
- Indirection:
- 1, Result first written to ROB on instruction completion
- 2, Result written to register file at commit time
- What if a later instruction needs a value in the reorder buffer?
- One option: stall the operation  stall the pipeline
- Better: Read the value from the reorder buffer. How?
- F
- D
- E
- W
- F
- D
- E
- R
- E
- E
- E
- E
- E
- E
- E
- F
- D
- E
- W
- F
- D
- E
- R
- F
- D
- E
- R
- F
- D
- E
- R
- F
- D
- E
- R
- E
- E
- E
- E
- E
- E
- E
- W
- R
- R
- W
- W
- W
- W

### Notes
- Use
- bypass
- 73

## Slide 74: Reorder Buffer: Where to put?

### Extracted Shape Text
- Reorder Buffer: Where to put?
- A register value can be in the register file, reorder buffer.
- Register
- File
- Func Unit
- Func Unit
- Func Unit
- Reorder
- Buffer
- Instruction
- Cache

## Slide 75: Simplifying Reorder Buffer Access

### Extracted Shape Text
- Simplifying Reorder Buffer Access
- Idea: Use indirection
- 1, Access register file first (check if the register is valid)
- If register not valid, register file stores the ID of the reorder buffer entry that contains (or will contain) the value of the register
- Mapping of the register to a ROB entry: Register file maps the register to a reorder buffer entry if there is an in-flight instruction writing to the register
- 2, Access reorder buffer next

### Notes
- Access ROB first
- 75

## Slide 76: Reorder Buffer in Intel Pentium III

- Images: 1; Tables: 0

### Extracted Shape Text
- Reorder Buffer in Intel Pentium III
- Boggs et al., “The Microarchitecture of the Pentium 4 Processor,” Intel Technology Journal, 2001.

## Slide 77: Reorder Buffer: For False Dependencies

### Extracted Shape Text
- Reorder Buffer: For False Dependencies
- Output and anti dependences are not true dependences
- WHY? The same register refers to values that have nothing to do with each other
- They exist due to lack of register ID’s (i.e. names) in the ISA
- RB eliminates anti and output dependences
- Gives the illusion that there are a large number of registers
- HOW: The register ID is renamed to the reorder buffer entry that will hold the register’s value
- Register ID  ROB entry ID
- Architectural register ID  Physical register ID
- After renaming, ROB entry ID used to refer to the register

### Notes
- ROB
- 临时工，临时工多，有编制的少
- 77

## Slide 78: Reorder Buffer: For False Dependencies

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

## Slide 79: To address false dependency,

### Extracted Shape Text
- To address false dependency,
- number of registers > number of ROB entries?
- NO.

### Notes
- The majority of you will not work on Systems.
- But you should know the key principles that help you understand the system on which your AI task runs.
- Our course has to include both computer architecture and AI chip courses.
- 79

## Slide 80: In-Order Pipeline with Reorder Buffer

### Extracted Shape Text
- In-Order Pipeline with Reorder Buffer
- In-order dispatch/execution, out-of-order completion, in-order retirement
- Decode (D): Access regfile/ROB, allocate entry in ROB, check if instruction can execute, if so dispatch instruction
- Execute (E): Instructions can complete out-of-order
- Completion (R): Write result to reorder buffer
- Retirement/Commit (W): Check for exceptions; if none, write result to architectural register file or memory; else, flush pipeline and start from exception handler
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
- Out of Order
- In order

## Slide 81: Reorder Buffer Tradeoffs

### Extracted Shape Text
- Reorder Buffer Tradeoffs
- Advantages
- Conceptually simple for supporting precise exceptions
- Can eliminate false dependences
- Disadvantages
- Reorder buffer needs to be accessed to get the results that are yet to be written to the register file
- Indirection  increased latency and complexity

## Slide 82: Can Reorder Buffer Change This Map?

### Extracted Shape Text
- Can Reorder Buffer Change This Map?

### Notes
- 82
- NO
