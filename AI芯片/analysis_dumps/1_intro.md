# 1_intro_course-neuman_isa-single-multi-cycle-pipeline.pptx selected slides

## Slide 43: Things Every Programmer Should know
- Things Every Programmer Should know
- Amdhal Law
- A formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.
- Roofline Model
- Theoretical performance bound of your application running on your machine.
- Little’s Law: L = λ *W  (buffer size = throughput * latency)
- A theorem by John Little which states that the long-term average number L of customers in a stationary system is equal to the long-term average effective arrival rate λ multiplied by the average time W that a customer spends in the system.
Notes:
- 43

## Slide 44: Amdahl’s Law
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

## Slide 45: Things Every Programmer Should know
- Things Every Programmer Should know
- Amdhal Law
- A formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.
- Roofline Model
- Theoretical performance bound of your application running on your machine.
- Little’s Law: L = λ *W  (buffer size = throughput * latency)
- A theorem by John Little which states that the long-term average number L of customers in a stationary system is equal to the long-term average effective arrival rate λ multiplied by the average time W that a customer spends in the system.
Notes:
- 45

## Slide 46: Why Roofline Model
- Why Roofline Model
- Why Roofline Model?
- Computing regime: Latency-limited  throughput-limited
- Original latency-oriented performance model does not work
- Roofline Model’s Two Perspectives?
- 1, Target processor’s perspective
- Showing inherent hardware limitations (or bound), in term of compute and memory
- 2, Compute kernel’s perspective
- Showing the priority of optimizations for a given compute kernel running on a given processor
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 46

## Slide 47: Key Term in Roofline Model
- Key Term in Roofline Model
- Arithmetic intensity (AI)
- Definition: AI = Total Flops / Total Memory Bytes
- Arithmetic intensity describes the characteristics of a compute kernel running on a given processor
- Large AI  Compute-bound
- Small AI  Memory-bound
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 47

## Slide 48: Roofline Model’s 3 Steps
- Roofline Model’s 3 Steps
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 48

## Slide 49: Roofline Model’s Roof
- Roofline Model’s Roof
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
- Roofline model’s 3 Steps:
- 1, Machine characterization:
- Memory bandwidth,
- Peak compute;
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 49

## Slide 50: How to Compute Roofline
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 50

## Slide 51: How to Compute Roofline
- How to Compute Roofline
- 9
- Peak Flop/s
- Throughput (Flop/s)
- DRAM GB/s
- Arithmetic Intensity (Flop:Byte)
- Memory-bound
- Compute-bound
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 51

## Slide 52: Compute Roofline Model
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 52

## Slide 53: HBM GB/s
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 53

## Slide 54: Roofline Model’s 3 Steps
- Roofline Model’s 3 Steps
- Roofline model’s 3 Steps:
- 1, Machine characterization:
- Memory bandwidth,
- Peak compute;
- 2, Application Characterization:
- Arithmetic intensity = Compute/Bytes;
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 54

## Slide 55: Roofline Model: Examples
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 55

## Slide 56: Roofline Model: Examples
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
Notes:
- 56

## Slide 57: Roofline Model’s 3 Steps
- Roofline Model’s 3 Steps
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
Notes:
- All these works rely on many different methodology's to identify memory bottlenecks in a system. Often, such methodologies are intuitively used as a indication of NDP suitability for a given application
- [CLICK] However, as I will show next, none of those models are comprehensive enough to identify memory bottlenecks and NDP suitability. This happens because these models are built targeting to identify specific sources of data movement bottlenecks, and often their definitions of compute and memory bound are not enough to indicate NDP suitability.
- [CLICK] For that, we will analyze two commonly used approaches: the roofline model, which correlates the arithmetic intensity of an application with performance,
- [CLICK] and identifying application that has high misses-per-kilo instructions or MPKI.
- [NEXT]
- 57

## Slide 58: Roofline Model: Application Monitoring
- Roofline Model: Application Monitoring
- 9
- Williams, Waterman, Patterson, “Roofline: An Insightful Visual Performance Model for Multicore Architectures”, CACM, 2009
- Peak Flop/s
- Attainable Flop/s
- DRAM GB/s
- 7-point
- Stencil
- Real Gflop/s ≤
- AI * DRAM GB/s
- TRIAD
- Arithmetic Intensity (Flop:Byte)
- 0.083
- 0.44
- Which one is more optimized?
- TRIAD
Notes:
- 58

## Slide 65: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Processing Cycle
- Single-Cycle CPU
- Multi-Cycle CPU
- Pipelined CPU

## Slide 66: The Von Neumann Model
- The Von Neumann Model

## Slide 67: Where Are We?
- Where Are We?

## Slide 68: The von Neumann Model
- The von Neumann Model
- John von Neumann proposed a fundamental model in 1946
- In order to build a computer, we need an execution model for processing computer programs.
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

## Slide 69: The von Neumann Model
- The von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 70: The von Neumann Model
- The von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 71: A Memory Array (4 locations X 3 bits)
- A Memory Array (4 locations X 3 bits)
- Di[2]
- Di[1]
- Di[0]
- D[2]
- D[1]
- D[0]
- Addr[1:0]
- WE
- Address Decoder
- Multiplexer

## Slide 72: Memory
- Memory
- Memory stores
- Programs
- Data
- Memory contains bits
- Bits are logically grouped into bytes (8 bits) and words (e.g., 8, 16, 32 bits)
- Address space: Total number of uniquely identifiable locations in memory
- In MIPS, the address space is 232
- 32-bit addresses
- In x86-64, the address space is (up to) 248
- 48-bit addresses
- Addressability: How many bits are stored in each location (address)
- E.g., 8-bit addressable (or byte-addressable)
- E.g., word-addressable
- A given instruction can operate on a byte or a word
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- 72

## Slide 73: A Simple Example
- A Simple Example
- A representation of memory with 8 locations
- Each location contains 8 bits (one byte)
- Byte addressable memory; address space of 8
- Value 6 is stored in address 4 & value 4 is stored in address 6
- Address
- Data Value

## Slide 74: The von Neumann Model
- The von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 75: Processing Unit (PU)
- Processing Unit (PU)
- PU: performs the actual computation(s)
- Processing unit consists of:
- Arithmetic and Logic Unit (ALU):
- Executing computation and logic operations
- For example MIPS (add, sub, mult, and, nor, sll, slr, slt…)
- Temporary Storage:
- Register File
Notes:
- 32 bits (Pentium IV) or 64 bits (Itanium, IA-64) in real systems
- 75

## Slide 76: ALU (Arithmetic Logic Unit)
- ALU (Arithmetic Logic Unit)
- ALU: Combines a variety of arithmetic and logical operations into a single unit
- ALU performs only one function at a time
- Usually denoted with this symbol:
Notes:
- 76

## Slide 77: Example ALU (Arithmetic Logic Unit)
- Example ALU (Arithmetic Logic Unit)

## Slide 78: Fast Temporary Storage: Registers
- Fast Temporary Storage: Registers
- Motivation of Registers:
- Memory is large but slow
- Registers in the Processing Unit
- Ensure fast access to values to be processed in the ALU
- Typically one register contains one word (same as word length)
- Register Set (Register File)
- Defination: Set of registers that can be manipulated by instructions
- MIPS has 32 general purpose registers
- R0 to R31: 5-bit register number (or Register ID)
- Register size = Word length = 32 bits

## Slide 79: MIPS Register File: Application Binary Interface
- MIPS Register File: Application Binary Interface
- TABLE:
  | Name | Register Number | Usage |
  | $0 | 0 | the constant value 0 |
  | $at | 1 | assembler temporary |
  | $v0-$v1 | 2-3 | function return value |
  | $a0-$a3 | 4-7 | function arguments |
  | $t0-$t7 | 8-15 | temporary variables |
  | $s0-$s7 | 16-23 | saved variables |
  | $t8-$t9 | 24-25 | temporary variables |
  | $k0-$k1 | 26-27 | OS temporaries |
  | $gp | 28 | global pointer |
  | $sp | 29 | stack pointer |
  | $fp | 30 | frame pointer |
  | $ra | 31 | function return address |
Notes:
- ”Dollar 0” or ”Register 0”
- 79

## Slide 80: The Von Neumann Model
- The Von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 81: Input and Output
- Input and Output
- Input and output enables information to get into and out of a computer.
- Input and output are called peripherals
- Input
- Keyboard
- Mouse
- Scanner
- Disks
- Network
- Etc.
- Output
- Monitor
- Printer
- Disks
- Network
- Etc.
Notes:
- 81

## Slide 82: The Von Neumann Model
- The Von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 83: Control Unit
- Control Unit
- Intuition: control unit is like the conductor of an orchestra
- Control unit:
- conducts the step-by-step process of executing (every instruction in) a program.
- Keeps track of which instruction being processed, via Instruction Register (IR), which contains the instruction.
- Keeps track of which instruction to process next, via Program Counter (PC) or Instruction Pointer (IP), another register that contains the address of the (next) instruction to process.

## Slide 84: Programmer Visible (Architectural) States
- Programmer Visible (Architectural) States
- M[0]
- M[1]
- M[2]
- M[3]
- M[4]
- M[N-1]
- Memory:
- array of storage locations
- indexed by an address
- Program Counter
- Registers:
- - given special names in the ISA
- (as opposed to addresses)
- - general vs. special purpose
- Instructions (e.g., programs) specify how to transform
- the values of programmer visible states
- Program Counter:
- memory address
- of the current (or next) instruction
Notes:
- 有编制的。。。
- 84

## Slide 85: The von Neumann Model
- The von Neumann Model
- CONTROL UNIT
- PC or IP
- Inst Register
- PROCESSING UNIT
- ALU
- TEMP
- MEMORY
- Mem Addr Reg
- Mem Data Reg
- INPUT
- Keyboard,
- Mouse,
- Disk…
- OUTPUT
- Monitor,
- Printer,
- Disk…

## Slide 86: von Neumann Model: Two Key Properties
- von Neumann Model: Two Key Properties
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
Notes:
- Every application can be descripted by this complete design von Neumann
- 86

## Slide 87: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Processing Cycle
- Single-Cycle CPU
- Multi-Cycle CPU

## Slide 88: Instruction Set Architectures
- Instruction Set Architectures

## Slide 89: Intuition: The Instruction Set
- Intuition: The Instruction Set
- Intuition of instruction set
- Instructions are words in the language of a computer
- Instruction Set Architecture (ISA) is the vocabulary
- The language of the computer can be written as
- Machine language: Computer-readable representation (that is, 0’s and 1’s)
- Assembly language: Human-readable representation
- High level language: C, C++, Python
- We will study MIPS instructions

## Slide 90: Instruction Set Architecture
- Instruction Set Architecture
- The ISA is the interface between what the software commands and what the hardware carries out.
- The ISA specifies three components:
- The memory organization
- Address space (MIPS: 232)
- Addressability (MIPS: 8 bits)
- Word- or Byte-addressable
- The register set
- 32 registers in MIPS
- The instruction set: cover all the tasks needed
- Opcodes
- Data types
- Addressing modes
- Microarchitecture
- ISA
- Program
- Algorithm
- Problem
- Circuits
- Electrons
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- * Register set:
- 16 GPR, including RBP (stack base pointer) and RSP (stack pointer).
- + floating point, multimedia
- 90

## Slide 91: Memory Organization: A Simple Example
- Memory Organization: A Simple Example
- A representation of memory with 8 locations, Each location contains 8 bits (one byte)
- Byte addressable memory; address space of 8
- Value 6 is stored in address 4 & value 4 is stored in address 6
- Address
- Data Value

## Slide 92: Word-Addressable Memory
- Word-Addressable Memory
- Each data word has a unique address
- In MIPS, a unique address for each 32-bit data word
- 00000000
- 00000001
- 00000002
- 00000003
- . . .
- Word Address
- 8 9 A B C D E F
- F 2 F 1 F 0 F 7
- 1 3 C 8 1 7 5 5
- D 1 6 1 7 A 1 C
- Word 3
- Word 2
- Word 1
- Word 0
- . . .
- . . .
- Data
- MIPS memory
Notes:
- 92

## Slide 93: Each byte has a unique address
- Each byte has a unique address
- MIPS is actually byte-addressable
- Word 3
- Word 2
- Word 1
- Word 0
- . . .
- . . .
- Data
- 8 9
- A B
- C D
- E F
- F 2
- F 1
- F 0
- F 7
- 1 3
- C 8
- 1 7
- 5 5
- D 1
- 6 1
- 7 A
- 1 C
- MIPS memory
- Byte-Addressable Memory
- 00000000
- 00000004
- 00000008
- 0000000C
- . . .
- Byte Address
- of the Word
Notes:
- 93

## Slide 94: Instruction Set Architecture
- Instruction Set Architecture
- The ISA is the interface between what the software commands and what the hardware carries out.
- The ISA specifies
- The memory organization
- Address space (MIPS: 232)
- Addressability (MIPS: 8 bits)
- Word- or Byte-addressable
- The register set
- 32 registers in MIPS
- The instruction set: cover all the tasks needed
- Opcodes
- Data types
- Addressing modes
- Microarchitecture
- ISA
- Program
- Algorithm
- Problem
- Circuits
- Electrons
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- * Register set:
- 16 GPR, including RBP (stack base pointer) and RSP (stack pointer).
- + floating point, multimedia
- 94

## Slide 95: MIPS Register File + Application Binary Interface
- MIPS Register File + Application Binary Interface
- TABLE:
  | Name | Register Number | Usage |
  | $0 | 0 | the constant value 0 |
  | $at | 1 | assembler temporary |
  | $v0-$v1 | 2-3 | function return value |
  | $a0-$a3 | 4-7 | function arguments |
  | $t0-$t7 | 8-15 | temporary variables |
  | $s0-$s7 | 16-23 | saved variables |
  | $t8-$t9 | 24-25 | temporary variables |
  | $k0-$k1 | 26-27 | OS temporaries |
  | $gp | 28 | global pointer |
  | $sp | 29 | stack pointer |
  | $fp | 30 | frame pointer |
  | $ra | 31 | function return address |
Notes:
- ”Dollar 0” or ”Register 0”
- 95

## Slide 96: Application Binary Interface
- Application Binary Interface
- An application binary interface (ABI) is an interface between two binary program modules.
- If you are programming with high level languages, like C, C++, you do not need to be aware of ABI.
- If you are programming with assembler, please to be aware of ABI.
- Analogical to traffic light.
Notes:
- ”Dollar 0” or ”Register 0”
- 96

## Slide 97: The Instruction Set Architecture
- The Instruction Set Architecture
- The ISA is the interface between what the software commands and what the hardware carries out.
- The ISA specifies
- The memory organization
- Address space (MIPS: 232)
- Addressability (MIPS: 8 bits)
- Word- or Byte-addressable
- The register set
- 32 registers in MIPS
- The instruction set: cover all the tasks needed
- Opcodes
- Data types
- Addressing modes
- Microarchitecture
- ISA
- Program
- Algorithm
- Problem
- Circuits
- Electrons
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- * Register set:
- 16 GPR, including RBP (stack base pointer) and RSP (stack pointer).
- + floating point, multimedia
- 97

## Slide 98: Addressing Modes
- Addressing Modes
- An addressing mode is a mechanism for specifying where an operand is located
- There are five addressing modes in MIPS
- Immediate or literal (constant)
- The operand is in some bits of the instruction
- Register
- The operand is in one register
- Three memory addressing modes
- PC-relative
- Pseudo-direct addressing
- Base+offset
Notes:
- How about in the context of AI chip?
- 98

## Slide 99: Why Have Different Addressing Modes?
- Why Have Different Addressing Modes?
- Another example of programmer vs. microarchitect tradeoff
- Advantages of more addressing modes:
- Enables better mapping of high-level programming constructs to hardware.
- Reduces the number of instructions and code size.
- Benefits various applications:
- Pointer-based accesses (indirection)
- Sparse matrix accesses
- Array indexing
- Disadvantages:
- More work for the compiler
- More work for the microarchitect

## Slide 100: The Instruction Set Architecture
- The Instruction Set Architecture
- The ISA is the interface between what the software commands and what the hardware carries out.
- The ISA specifies
- The memory organization
- Address space (MIPS: 232)
- Addressability (MIPS: 8 bits)
- Word- or Byte-addressable
- The register set
- 32 registers in MIPS
- The instruction set: cover all the tasks needed
- Opcodes
- Data types
- Addressing modes
- Microarchitecture
- ISA
- Program
- Algorithm
- Problem
- Circuits
- Electrons
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- * Register set:
- 16 GPR, including RBP (stack base pointer) and RSP (stack pointer).
- + floating point, multimedia
- 100

## Slide 101: Instruction Set: Data Types
- Instruction Set: Data Types
- An ISA supports one or several data types
- MIPS supports
- 2’s complement integers
- Unsigned integers
- Floating point
Notes:
- AI accelerator has a lot of large registers…
- 101

## Slide 102: Instruction Set: Data Type Tradeoffs
- Instruction Set: Data Type Tradeoffs
- Comparison of Two examples:
- Early RISC machines: Only integer data type
- AI chip: tensor data type
- Concept of semantic gap
- Data types coupled tightly to the semantic level, or complexity of instructions
- How close are instrs. to high-level languages
- Disadvantage and Advantage of having more or high-level data types in the ISA?
- Think compiler/programmer vs. microarchitect
Notes:
- Semantic level = how close are the instructions to the constructs of the program.
- How about in the context of AI chip?
- 102

## Slide 103: The Instruction Set Architecture
- The Instruction Set Architecture
- The ISA is the interface between what the software commands and what the hardware carries out.
- The ISA specifies
- The memory organization
- Address space (MIPS: 232)
- Addressability (MIPS: 8 bits)
- Word- or Byte-addressable
- The register set
- 32 registers in MIPS
- The instruction set: cover all the tasks needed
- Opcodes
- Data types
- Addressing modes
- Microarchitecture
- ISA
- Program
- Algorithm
- Problem
- Circuits
- Electrons
Notes:
- x86-64:
- * Memory organization:
- - Address space: up to 2^48.
- - Addressability: up to 48 bits. The actual length of the address is 64 bits, but bits 48 to 63 are sign extended.
- * Register set:
- 16 GPR, including RBP (stack base pointer) and RSP (stack pointer).
- + floating point, multimedia
- 103

## Slide 104: The Instruction: Opcode & Operands
- The Instruction: Opcode & Operands
- An instruction is made up of: Opcode and Operands
- Opcode: specifies what the instruction does
- Operands: specify who the instruction is to do it to
- Both are specified in instruction format (or instr. encoding)
- An MIPS instruction consists of 32 bits (bits [31:0])
- Bits [31:26] specify the opcode
- Bits [25:11] are used to figure out where the operands are
- R-type
- 0
- 6-bit
- rs
- 5-bit
- rt
- 5-bit
- rd
- 5-bit
- shamt
- 5-bit
- funct
- 6-bit
Notes:
- Opcode:
- 操作码
- Operand:
- 操作数
- 104

## Slide 105: Instruction: Opcodes
- Instruction: Opcodes
- A large or small set of opcodes could be defined
- E.g, HP Precision Architecture: an instruction for A*B+C
- E.g, x86 ISA: multimedia extensions (MMX), later SSE and AVX
- E.g, VAX ISA: opcode to save all information of one program prior to switching to another program
- Three types of opcodes in MIPS:
- Operate
- Data movement
- Control
Notes:
- From computer architecture’s perspective, ISA is not important,
- 105

## Slide 106: MIPS: Three Main Instruction Types
- MIPS: Three Main Instruction Types
- 1, Operate instructions
- Execute instructions in the ALU
- 2, Data movement instructions
- Read from or write to memory
- 3, Control flow instructions
- Change the sequence of execution

## Slide 107: An Example Program in MIPS
- An Example Program in MIPS
- a = A[0];
- c = a + b - 5;
- B[0] = c;
- A = $s0
- b = $s2
- B = $s1
- High-level code
- MIPS registers
- lw $t0, 0($s0)
- add $t1, $t0, $s2
- addi $t2, $t1, -5
- sw $t2, 0($s1)
- MIPS assembly?
Notes:
- 107

## Slide 108: Operate Instructions
- Operate Instructions

## Slide 109: An Example Operate Instruction
- An Example Operate Instruction
- Addition
- add: mnemonic to indicate the operation to perform
- b, c: source operands
- a: destination operand
- a ← b + c
- a = b + c;
- add a, b, c
- High-level code
- Assembly?

## Slide 110: Addition
- Addition
- From Assembly to Machine Code in MIPS
- 0
- 17
- 18
- 16
- 0
- 32
- op
- rs
- rt
- rd
- shamt
- funct
- add $s0, $s1, $s2
- MIPS assembly
- Field Values?
- 0x02328020
- 000000
- 10001
- 10010
- 10000
- 00000
- 100000
- op
- rs
- rt
- rd
- shamt
- funct
- Machine Code (Instruction Encoding)
- 15
- 11
- 10
- 6
- 0
- 5
- 16
- 20
- 21
- 25
- 26
- 31
- rd ← rs + rt
Notes:
- 110

## Slide 111: Add immediate
- Add immediate
- Add with one Literal in MIPS
- 0
- 17
- 16
- 5
- op
- rs
- rt
- imm
- addi $s0, $s1, 5
- MIPS assembly
- Field Values:
- 001000
- 10001
- 10010
- 0000 0000 0000 0101
- op
- rs
- rt
- imm
- Machine Code?
- 0x22300005
- rt ← rs + sign-extend(imm)
Notes:
- 111

## Slide 112: For efficiency reason, where to put destination operand in an instruction?
- For efficiency reason, where to put destination operand in an instruction?
- The operand slot close to opcode, because it is fixed for all instructions.
Notes:
- Better ISA eases the hardware implementation.
- 112

## Slide 113: Operate Instructions
- Operate Instructions
- In MIPS, there are many more operate intstructions:
- Most of R-type instructions (they are binary operations)
- E.g., add, and, nor, xor…
- I-type versions (i.e., with one immediate operand) of the R-type operate instructions
- F-type operations, i.e., floating-point operations

## Slide 114: Data Movement Instructions
- Data Movement Instructions

## Slide 115: Motivation: Reading Operands from Memory
- Motivation: Reading Operands from Memory
- Operate instructions, such as addition, tells the computer to execute arithmetic (or logic) computations in the ALU.
- Memory instructions accesses the operands from memory:
- Load them from memory to registers
- Store them from registers to memory
- Next, we see how to read (or load) from memory

## Slide 116: Reading Word-Addressable Memory
- Reading Word-Addressable Memory
- Load word
- load: mnemonic to indicate the load word operation
- A: base address
- i: offset
- E.g., immediate or literal (a constant)
- a: destination operand
- Semantics: a ← Memory[A + i]
- a = A[i];
- load a, A, i
- High-level code
- Assembly

## Slide 117: Load Word in MIPS
- Load Word in MIPS
- MIPS assembly
- a = A[2];
- lw $s3, 2($s0)
- High-level code
- MIPS assembly
- $s3 ← Memory[$s0 + 2]
- These instructions use a base+offset addressing mode
- (i.e., the way the address is calculated).
Notes:
- 117

## Slide 118: Load Word in Byte-Addressable MIPS
- Load Word in Byte-Addressable MIPS
- MIPS assembly
- a = A[2];
- lw $s3, 8($s0)
- High-level code
- MIPS assembly
- $s3 ← Memory[$s0 + 8]
Notes:
- 118

## Slide 119: Store Instruction in MIPS
- Store Instruction in MIPS
- In MIPS, lw and sw use base+offset mode (or base addressing mode)
- imm is the 16-bit offset, which is sign-extended to 32 bits
- A[2] = a;
- sw $s3, 8($s0)
- High-level code
- MIPS assembly?
- Memory[$s0 + 8] ← $s3
- 43
- 16
- 19
- 8
- op
- rs
- rt
- imm
- Field Values:

## Slide 120: Control Flow Instructions
- Control Flow Instructions

## Slide 121: Control Flow Instructions
- Control Flow Instructions
- A computer program executes in sequence (i.e., in program order)
- First instruction, second instruction, third instruction and so on.
- Unless we change the sequence of execution.
- Control instructions allow a program to execute out of sequence
- Changing the PC by loading it during the EXECUTE phase
- Instead of using the incremented PC (loaded during the FETCH phase)

## Slide 122: Control Flow Instructions
- Control Flow Instructions
- Control flow instructions has two types:
- 1, Conditional branches: used to make decisions
- E.g., if-else statement
- 2, Unconditional jumps: used to implement semantics like
- Loops
- Function calls
- j in MIPS
Notes:
- 122

## Slide 123: Jump in MIPS
- Jump in MIPS
- Unconditional branch or jump
- MIPS
- 2 = opcode
- target = target address
- Variations
- jal: jump and link (function calls)
- jr: jump register
- 2
- target
- 6 bits
- 26 bits
- j target
- J-Type
- jr $s0
- j uses pseudo-direct addressing mode
- ✝This is the incremented PC
- jr uses register addressing mode
Notes:
- jr is R-Type
- 123

## Slide 124: Conditional Branches in MIPS
- Conditional Branches in MIPS
- beq (Branch if Equal)
- 4 = opcode
- rs, rt = source registers
- offset = immediate or constant value
- if rs == rt
- then PC ← PC✝ + sign-extend(offset) * 4
- Variations: beq, bne, blez, bgtz
- 4
- rs
- rt
- offset
- 6 bits
- 5 bits
- 5 bits
- 16 bits
- beq $s0, $s1, offset
- ✝This is the incremented PC
Notes:
- 124

## Slide 125: Many Different ISAs Over Decades
- Many Different ISAs Over Decades
- x86
- PDP-x: Programmed Data Processor (PDP-11)
- VAX
- IBM 360
- CDC 6600
- SIMD ISAs: CRAY-1, Connection Machine
- VLIW ISAs: Multiflow, Cydrome, IA-64 (EPIC)
- PowerPC, POWER
- RISC ISAs: Alpha, MIPS, SPARC, ARM, RISC-V, …
- What are the fundamental differences?
- E.g., how instructions are specified and what they do
- E.g., how complex are the instructions
Notes:
- 但本质上是一致的
- 125

## Slide 126: Complex vs. Simple Instructions
- Complex vs. Simple Instructions
- Complex instruction: An instruction does a lot of work, e.g. many operations
- Insert in a doubly linked list
- Compute FFT
- Matrix multiplication
- …
- Simple instruction: An instruction does little work -- it is a primitive using which complex operations can be built
- Add
- XOR
- Multiply
- …

## Slide 127: Complex vs. Simple Instructions
- Complex vs. Simple Instructions
- Advantages of Complex instructions
- + Denser encoding  smaller code size  better memory utilization, saves off-chip bandwidth, better cache hit rate (better packing of instructions)
- + Simpler compiler: no need to optimize small instructions as much
- Disadvantages of Complex Instructions
- - Larger chunks of work  compiler has less opportunity to optimize (limited in fine-grained optimizations it can do)
- - More complex hardware  translation from a high level to control signals and optimization needs to be done by hardware

## Slide 128: ISA-level Tradeoffs: Number of Registers
- ISA-level Tradeoffs: Number of Registers
- Register number affects:
- Number of bits used for encoding register address
- Number of values kept in fast storage (register file)
- (uarch) Size, access time, power consumption of register file
- Large number of registers:
- + Enables better register allocation (and optimizations) by compiler  fewer saves/restores
- -- Larger instruction size
- -- Larger register file size
Notes:
- 128

## Slide 129: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Cycle
- Single-Cycle CPU
- Multi-Cycle CPU
Notes:
- Microarchitecture…
- 129

## Slide 130: Instruction (Processing) Cycle
- Instruction (Processing) Cycle
Notes:
- Microarchitecture
- 方面了。。。
- 130

## Slide 131: How Are These Instructions Executed?
- How Are These Instructions Executed?
- By using instructions we can speak the language of the computer and implement any functionality.
- Thus, we now know how to tell the computer to
- Execute computations in the ALU by using, for instance, an addition
- Access operands from memory by using the load word instruction
- But, how are these instructions executed on the computer?
- The process of executing an instruction is called is the instruction cycle (or, instruction processing cycle)

## Slide 132: The Instruction Cycle
- The Instruction Cycle
- The instruction cycle is a sequence of steps or phases, that an instruction goes through to be executed
- INSN. FETCH (IF)
- INSN. DECODE (ID)
- EXECUTE (EXE)
- ACCESS MEMORY (MEM)
- WRITE BACK (WB)
- Not all instructions have the five phases
- LDR does not require EXECUTE
- ADD does not require ACCESS MEMORY
- Intel x86 instruction ADD [eax], edx is an example of instruction with five phases

## Slide 133: The Instruction Cycle
- The Instruction Cycle
- INSN. FETCH (IF)
- INSN. DECODE (ID)
- EXECUTE (EXE)
- ACCESS MEMORY (MEM)
- WRITE BACK (WB)
- After WB, a New IF

## Slide 134: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Cycle
- Single-Cycle CPU
- Multi-Cycle CPU
- Pipeline

## Slide 135: Where Are We?
- Where Are We?

## Slide 136: A Single-Cycle MicroarchitectureA Closer Look
- A Single-Cycle MicroarchitectureA Closer Look

## Slide 137: Single-cycle Machine
- Single-cycle Machine
- AS
- Sequential
- Logic
- (State)
- Combinational
- Logic
- AS’
- AS: Architectural State

## Slide 138: A Very Basic Instruction Processing Engine
- A Very Basic Instruction Processing Engine
- Each instruction takes a single clock cycle to execute.
- Only combinational logic is used to implement instruction execution.
- No intermediate, programmer-invisible state updates
- AS = Architectural (programmer visible) state
- at the beginning of a clock cycle
- Process instruction in one clock cycle
- AS’ = Architectural (programmer visible) state
- at the end of a clock cycle

## Slide 139: Programmer Visible (Architectural) States
- Programmer Visible (Architectural) States
- M[0]
- M[1]
- M[2]
- M[3]
- M[4]
- M[N-1]
- Memory:
- array of storage locations
- indexed by an address
- Program Counter
- Registers:
- - given special names in the ISA
- (as opposed to addresses)
- - general vs. special purpose
- Instructions (e.g., programs) specify how to transform
- the values of programmer visible states
- Program Counter:
- memory address
- of the current (or next) instruction

## Slide 140: “Process Instruction” Step: Single-cycle CPU
- “Process Instruction” Step: Single-cycle CPU
- Given an instruction and AS (Architectural State),
- ISA specifies abstractly what AS’ should be.
- It defines an abstract finite state machine where
- State = programmer-visible state
- Next-state logic = instruction execution specification
- From ISA point of view, there are no “intermediate states” between AS and AS’ during instruction execution
- One state transition per instruction
- Microarchitecture implements how AS is transformed to AS’
- There are many choices in implementation
- We can have programmer-invisible state to optimize the speed of instruction execution: multiple state transitions per instruction
- Single-cycle: AS  AS’ (transform AS to AS’ in a single clock cycle)
Notes:
- AS=architecture state
- 140

## Slide 141: Let’s Start with the State Elements
- Let’s Start with the State Elements
- Data and control inputs
- **Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 142: MIPS State Elements
- MIPS State Elements
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
Notes:
- 142

## Slide 143: Assumption of Memory and Register File
- Assumption of Memory and Register File
- “Magic” memory:
- Single-cycle, synchronous memory: Contrast this with memory that tells when the data is ready
- i.e., Ready signal: indicating the read or write is done
- “Magic” register file:
- Combinational read: output of the read data port is a combinational function of the register file contents and the corresponding read select port
- Synchronous write: the selected register is updated on the positive edge clock transition when write enable is asserted
- Cannot affect read output in between clock edges
Notes:
- 143

## Slide 144: Instruction Processing
- Instruction Processing
- Instruction Processing has 5 generic steps:
- Instruction fetch (IF)
- Instruction decode and register operand fetch (ID/RF)
- Execute/Evaluate memory address (EX/AG)
- Memory operand fetch (MEM)
- Store/writeback result (WB)
- IF
- ID/RF
- EX/AG
- MEM
- WB
- **Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 145: We Need to Provide the Datapath+Control Logic to Execute All ISA Instructions
- We Need to Provide the Datapath+Control Logic to Execute All ISA Instructions

## Slide 146: What Is To Come: The Full MIPS Datapath
- What Is To Come: The Full MIPS Datapath
- PCSrc2=Br Taken
- PCSrc1=Jump
- ALU operation
- bcond
- **Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]
- JAL, JR, JALR omitted

## Slide 147: A Single-Cycle Microarchitecture: Analysis
- A Single-Cycle Microarchitecture: Analysis
- Every instruction takes 1 cycle to execute
- CPI (Cycles per instruction) is strictly 1
- How long each instruction takes is determined by how long the slowest instruction takes to execute
- Even though many instructions do not need that long to execute
- Clock cycle time of the microarchitecture is determined by how long it takes to complete the slowest instruction
- Critical path of the design is determined by the processing time of the slowest instruction

## Slide 148: What is the Slowest Instruction to Process?
- What is the Slowest Instruction to Process?
- Let’s go back to the basics
- All five phases of the instruction processing cycle take a single machine clock cycle to complete
- Do each of the above phases take the same time (latency) for all instructions?
- 1. Instruction fetch (IF)
- 2. Instruction decode and
- register operand fetch (ID/RF)
- 3. Execute/Evaluate memory address (EX/AG)
- 4. Memory operand fetch (MEM)
- 5. Store/writeback result (WB)

## Slide 149: Let’s Find the Critical Path
- Let’s Find the Critical Path
- PCSrc2=Br Taken
- PCSrc1=Jump
- ALU operation
- bcond
- [Based on original figure from P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 150: Example Single-Cycle Datapath Analysis
- TABLE:
  | steps | IF | ID | EX | MEM | WB | Delay |
  | resources | mem | RF | ALU | mem | RF |  |
  | R-type | 200 | 50 | 100 |  | 50 | 400 |
  | I-type | 200 | 50 | 100 |  | 50 | 400 |
  | LW | 200 | 50 | 100 | 200 | 50 | 600 |
  | SW | 200 | 50 | 100 | 200 |  | 550 |
  | Branch | 200 | 50 | 100 |  |  | 350 |
  | Jump | 200 |  |  |  |  | 200 |
- Example Single-Cycle Datapath Analysis
- Assume (for the design in the previous slide)
- memory units (read or write): 200 ps
- ALU and adders: 100 ps
- register file (read or write): 50 ps
- other combinational logic: 0 ps

## Slide 151: Analysis of Single-cycle CPU
- Analysis of Single-cycle CPU
- Single-cycle CPU:
- All five phases of the instruction processing cycle take a single machine clock cycle to complete
- The slowest instruction determines the frequency.
- 不卷。

## Slide 152: Can We Do Better?
- Can We Do Better?

## Slide 153: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Cycle
- Single-Cycle CPU
- Multi-Cycle CPU
- Pipeline CPU

## Slide 154: Multi-Cycle Microarchitectures
- Multi-Cycle Microarchitectures

## Slide 155: Where Are We?
- Where Are We?

## Slide 156: Multi-Cycle Microarchitectures
- Multi-Cycle Microarchitectures
- Goal: Let each instruction take (close to) only as many cycles it really needs
- Ideas of multi-cycle CPU:
- 1, Decrease clock cycle time
- 2, Each instruction takes as many clock cycles as it needs to take
- Multiple state transitions per instruction
- The states followed by each instruction is different

## Slide 157: The “Process Instruction” Step of Multi-Cycle CPU
- The “Process Instruction” Step of Multi-Cycle CPU
- Microarchitecture implements how AS is transformed to AS’
- We can have programmer-invisible state to optimize the speed of instruction execution: multiple state transitions per instruction
- Single-cycle: AS  AS’ (transform AS to AS’ in a single clock cycle)
- Multi-cycle: AS  AS+MS1  AS+MS2  AS+MS3  AS’ (take multiple clock cycles to transform AS to AS’)

## Slide 158: Multi-Cycle Microarchitecture
- Multi-Cycle Microarchitecture
- AS = Architectural (programmer visible) state
- at the beginning of an instruction
- Step 1: Process a part of instruction in one clock cycle
- Step 2: Process next part of instruction in the next clock cycle
- …
- AS’ = Architectural (programmer visible) state
- at the end of a clock cycle

## Slide 159: FSM of Multi-Cycle CPU
- FSM of Multi-Cycle CPU

## Slide 160: Benefits of Multi-Cycle Design
- Benefits of Multi-Cycle Design
- 1, Critical path design
- Can keep reducing the critical path independently of the worst-case processing time of any instruction
- 2, Bread and butter (common case) design
- Can optimize the number of states it takes to execute “important” instructions that make up much of the execution time
- 3, Balanced design
- No need to provide more capability or resources than really needed
- An instruction that needs resource X multiple times does not require multiple X’s to be implemented
- Leads to more efficient hardware: Can reuse hardware components needed multiple times for an instruction

## Slide 161: Downsides of Multi-Cycle Design
- Downsides of Multi-Cycle Design
- Need to store the intermediate results at the end of each clock cycle
- Hardware overhead for registers
- Register setup/hold overhead paid multiple times for an instruction

## Slide 162: Performance Analysis
- Performance Analysis
- Execution time of a single instruction
- {CPI} x {clock cycle time}
- Execution time of an entire program
- Sum over all instructions [{CPI} x {clock cycle time}]
- {# of instructions} x {Average CPI} x {clock cycle time}
- Single-cycle microarchitecture：
- CPI = 1
- Clock cycle time = long
- Multi-cycle microarchitecture：
- CPI = different for each instruction
- Average CPI  hopefully small
- Clock cycle time = short
- CPI: Cycles Per Instruction
Notes:
- 周期
- 162

## Slide 163: A Multi-Cycle MicroarchitectureA Closer Look
- A Multi-Cycle MicroarchitectureA Closer Look

## Slide 164: Single-cycle CPU vs. Multi-cycle machine
- Single-cycle CPU vs. Multi-cycle machine
- Single-cycle CPU:
- All five phases of the instruction processing cycle take a single machine clock cycle to complete
- The slowest instruction determines the frequency.
- 不卷。
- Multi-cycle CPU:
- All five phases of the instruction processing cycle can take multiple machine clock cycles to complete．
- Each phase can take multiple clock cycles to complete.
- 开始卷

## Slide 165: Can We Do Better?
- Can We Do Better?

## Slide 166: Can We Do Better?
- Can We Do Better?
- What limitations do you see with the multi-cycle design?
- Reason: Limited concurrency
- Some hardware resources are idle during different phases of instruction processing cycle
- “Fetch” logic is idle when an instruction is being “decoded” or “executed”.
- Most of the datapath is idle when a memory access is happening.

## Slide 167: Outline
- Outline
- Von Neumann Model
- Instruction Set Architecture (ISA)
- Instruction Processing Cycle
- Single-Cycle CPU
- Multi-Cycle CPU
- Pipelined CPU

## Slide 168: Where Are We?
- Where Are We?

## Slide 169: Can We Use the Idle Hardware to Improve Concurrency?
- Can We Use the Idle Hardware to Improve Concurrency?
- Goal: More concurrency  Higher instruction throughput (i.e., more “work” completed in one cycle)
- Key Idea: When an instruction is using some resources in its processing phase, process other instructions on idle resources not needed by that instruction
- E.g., when an instruction is being decoded, fetch the next instruction
- E.g., when an instruction is being executed, decode another instruction
- E.g., when an instruction is accessing data memory (ld/st), execute the next instruction
- E.g., when an instruction is writing its result into the register file, access data memory for the next instruction

## Slide 170: Can Have Different Instructions in Different Stages
- Can Have Different Instructions in Different Stages
- 1. Instruction fetch (IF)
- 2. Instruction decode and
- register operand fetch (ID/RF)
- 3. Execute/Evaluate memory address (EX/AG)
- 4. Memory operand fetch (MEM)
- 5. Store/writeback result (WB)

## Slide 171: Can Have Different Instructions in Different Stages
- Can Have Different Instructions in Different Stages
- Insn 1
- Insn 2
- Insn 3
- Insn 4

## Slide 172: The Laundry Analogy: Pipeline
- The Laundry Analogy: Pipeline
- “place one dirty load of clothes in the washer”,
- “when the washer is finished, place the wet load in the dryer”,
- “when the dryer is finished, take out the dry load and fold”,
- “when folding is finished, put the clothes away”.
- Observations:
- 1, steps to do a load are sequentially dependent,
- 2, different steps do not share resources,
- 3, no dependence between different loads.
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 173: Pipelining Multiple Loads of Laundry
- Pipelining Multiple Loads of Laundry
- - latency per load is the same
- - throughput increased by 4X
- - 4 loads of laundry in parallel
- - no additional resources
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 174: Pipelining: Basic Idea
- Pipelining: Basic Idea
- Idea of pipelining:
- 1, Divide the instruction processing cycle into distinct “stages” of processing
- 2, Ensure enough hardware resources to process one instruction in each stage
- 3, Process a different instruction in each stage
- Instructions consecutive in program order are processed in consecutive stages
- Benefit: Increases instruction processing throughput (1/CPI)

## Slide 175: Example: Execution of Four Independent ADDs
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
- Is life always this beautiful?
- 1 instruction completed per cycle
Notes:
- No, multi-cycle execution, unpredictable memory access cycles
- 175

## Slide 176: An Ideal Pipeline
- An Ideal Pipeline
- Goal: Increase throughput with little increase in cost (hardware cost, in case of instruction processing)
- Assumptions:
- 1, Repetition of identical operations
- The same operation is repeated on a large number of different inputs (e.g., all laundry loads go through the same steps)
- 2, Repetition of independent operations
- No dependences between repeated operations
- 3, Uniformly partitionable suboperations
- Processing can be evenly divided into uniform-latency suboperations (that do not share resources)
- Fitting examples: automobile assembly line, doing laundry
- What about the instruction processing “cycle”?

## Slide 177: Ideal Pipelining
- Ideal Pipelining
- combinational logic (F,D,E,M,W)
- T psec
- BW=~(1/T)
- BW=~(2/T)
- T/2 ps (F,D,E)
- T/2 ps (M,W)
- BW=~(3/T)
- T/3
- ps (F,D)
- T/3
- ps (E,M)
- T/3
- ps (M,W)
- BW means Bandwidth,
- Same as Throughput (in this context)

## Slide 178: Pipelining: Dryer Takes One Hour, Not Half Hour
- Pipelining: Dryer Takes One Hour, Not Half Hour
- Observation: the slowest step (the dryer) decides throughput.
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 179: Pipelining Multiple Loads of Laundry: In Practice
- Pipelining Multiple Loads of Laundry: In Practice
- A
- B
- A
- B
- Outcome: throughput restored (2 loads per hour) using 2 dryers.
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]
- Solution: using 2 dryers

## Slide 180: Pipelining Instruction Processing
- Pipelining Instruction Processing

## Slide 181: Remember: The Instruction Processing Cycle
- Remember: The Instruction Processing Cycle
- Fetch
- Decode
- Evaluate Address
- Fetch Operands
- Execute
- Store Result
- 1. Instruction fetch (IF)
- 2. Instruction decode and
- register operand fetch (ID/RF)
- 3. Execute/Evaluate memory address (EX/AG)
- 4. Memory operand fetch (MEM)
- 5. Store/writeback result (WB)

## Slide 182: Remember the Single-Cycle Uarch
- Remember the Single-Cycle Uarch
- PCSrc2=Br Taken
- PCSrc1=Jump
- ALU operation:
- bcond
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]
- T
- BW=~(1/T)

## Slide 183: Dividing Into Stages
- Dividing Into Stages
- 200ps
- Is this the correct partitioning?
- Why not 4 or 6 stages? Why not different boundaries?
- 100ps
- 200ps
- 200ps
- 100ps
- RF
- write
- ignore
- for now
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 184: Instruction Pipeline Throughput
- Instruction Pipeline Throughput
- 200 400 600 800 1000 1200 1400 1600 1800
- 200 400 600 800 1000 1200 1400
- 800ps
- 800ps
- 800ps
- 200ps
- 200ps
- 200ps
- 200ps
- 200ps
- 200ps
- 200ps
- 5-stage speedup is 4, not 5 as predicted by the ideal model. Why?
Notes:
- Pipeline stages are not balanced.
- 184

## Slide 185: Enabling Pipelined Processing: Pipeline Registers
- Enabling Pipelined Processing: Pipeline Registers
- No resource is used by more than one stage.
- IRD
- PCF
- PCD+4
- PCE+4
- nPCM
- AE
- BE
- ImmE
- AoutM
- BM
- MDRW
- AoutW
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]
- T/k
- ps
- T/k
- ps

## Slide 186: Illustrating Pipeline Operation: Operation View
- Illustrating Pipeline Operation: Operation View
- MEM
- EX
- ID
- IF
- Inst4
- WB
- IF
- MEM
- IF
- MEM
- EX
- t0
- t1
- t2
- t3
- t4
- t5
- ID
- EX
- IF
- ID
- IF
- ID
- Inst0
- ID
- IF
- Inst1
- EX
- ID
- IF
- Inst2
- MEM
- EX
- ID
- IF
- Inst3
- WB
- WB
- MEM
- EX
- WB
- steady state
- (full pipeline)

## Slide 187: Illustrating Pipeline Operation: Resource View
- Illustrating Pipeline Operation: Resource View
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
- TABLE:
  |  | t0 | t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 | t9 | t10 |
  | IF |  |  |  |  |  |  |  |  |  |  |  |
  | ID |  |  |  |  |  |  |  |  |  |  |  |
  | EX |  |  |  |  |  |  |  |  |  |  |  |
  | MEM |  |  |  |  |  |  |  |  |  |  |  |
  | WB |  |  |  |  |  |  |  |  |  |  |  |

## Slide 188: Control Points in a Pipeline
- Control Points in a Pipeline
- Identical set of control points as the single-cycle datapath
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 189: Control Signals in a Pipeline
- Control Signals in a Pipeline
- For a given instruction
- same control signals as single-cycle, but
- control signals required at different cycles, depending on stage
- Option 1: decode once using the same logic as single-cycle and buffer signals until consumed
- Option 2: carry relevant “instruction word/field” down the pipeline and decode locally within each or in a previous stage
- Which one is better?
Notes:
- Based on the control bits vs.
- 189

## Slide 190: Pipelined Control Signals
- Pipelined Control Signals
- Based on original figure from [P&H CO&D, COPYRIGHT 2004 Elsevier. ALL RIGHTS RESERVED.]

## Slide 191: Remember: An Ideal Pipeline
- Remember: An Ideal Pipeline
- Goal: Increase throughput with little increase in cost (hardware cost, in case of instruction processing)
- Assumptions:
- 1, Repetition of identical operations
- The same operation is repeated on a large number of different inputs (e.g., all laundry loads go through the same steps)
- 2, Repetition of independent operations
- No dependences between repeated operations
- 3, Uniformly partitionable suboperations
- Processing can be evenly divided into uniform-latency suboperations (that do not share resources)
- Fitting examples: automobile assembly line, doing laundry
- What about the instruction processing “cycle”?

## Slide 192: Instruction Pipeline: Not An Ideal Pipeline
- Instruction Pipeline: Not An Ideal Pipeline
- Identical operations ... NOT!
-  different instructions  not all need the same stages
- Forcing different instructions to go through the same pipe stages
-  external fragmentation (some pipe stages idle for some instructions)
- Uniform suboperations ... NOT!
-  different pipeline stages  not the same latency
- Need to force each stage to be controlled by the same clock
-  internal fragmentation (some pipe stages are too fast but all take the same clock cycle time)
- Independent operations ... NOT!
-  instructions are not independent of each other
- Need to detect and resolve inter-instruction dependences to ensure the pipeline provides correct results
-  pipeline stalls (pipeline is not always moving)

## Slide 193: Issues in Pipeline Design
- Issues in Pipeline Design
- Balancing work in pipeline stages
- How many stages and what is done in each stage
- Keeping the pipeline correct, moving, and full in the presence of events that disrupt pipeline flow
- Handling dependences
- Data
- Control
- Handling resource contention
- Handling long-latency (multi-cycle) operations
- Handling exceptions, interrupts
- Advanced: Improving pipeline throughput
- Minimizing stalls