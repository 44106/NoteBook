# 5_memory.pptx selected slides

## Slide 10: Memory (Programmer’s View)
- Memory (Programmer’s View)

## Slide 11: Computing Architecture Idealism
- Computing Architecture Idealism
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

## Slide 12: Ideal Memory
- Ideal Memory
- Four properties of ideal memory:
- Zero latency: zero access time
- Infinite capacity: no swap out
- Infinite bandwidth: to support multiple accesses in parallel
- Zero cost: provide as many as needed

## Slide 13: The Problem of Ideal Memory
- The Problem of Ideal Memory
- Ideal memory’s requirements oppose each other
- Bigger is slower
- Bigger  Takes longer to determine the location
- Faster is more expensive
- Memory technology: SRAM vs. DRAM vs. SSD vs. Disk vs. Tape
- Higher bandwidth is more expensive
- Need more banks, more ports, more channels, higher frequency or faster technology
Notes:
- 全班点名 和全校点名 花时间是不同的
- 13

## Slide 14: The Problem of Ideal Memory
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
- These sample values (circa ~2021) scale with time.
Notes:
- 14

## Slide 15: The Problem (Table View)
- The Problem (Table View)
- TABLE:
  | Memory Device | Capacity | Latency | Cost per Megabyte |
  | SRAM | 512 Bytes | sub-nanosec |  |
  | SRAM | KByte~MByte | ~nanosec | < 0.3$ |
  | DRAM | Gigabyte | ~50 nanosec | < 0.03$ |
  | PCM-DIMM
(Intel Optane DC DIMM) | Gigabyte | ~200 nanosec | < 0.004$ |
  | PCM-SSD
(Intel Optane SSD) | Gigabyte
~Terabyte | ~10 µs | < 0.001$ |
  | Flash memory | Gigabyte
~Terabyte | ~100 µs | < 0.00008$ |
  | Hard Disk | Terabyte | ~10 millisec | < 0.00003$ |
- These sample values (circa ~2021) scale with time
- Bigger is slower
- Faster is more expensive
- (dollars and chip area)

## Slide 16: Comparison of Memories
- Comparison of Memories
- SRAM
- HBM
- DDR
- SSD
- DISK
- Capacity
- SRAM
- HBM
- DDR
- SSD
- DISK
- Latency
- Bandwidth
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DDR
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 17: FF vs. SRAM vs. DRAM vs. SSD
- FF vs. SRAM vs. DRAM vs. SSD
- Flip-Flops (~K)
- Very fast, parallel access
- Very expensive (one bit costs tens of transistors)
- Static RAM (~M)
- Relatively fast, only one data word at a time
- Expensive (one bit costs 6+ transistors)
- Dynamic RAM (~G)
- Slow, one data word at a time, reading destroys content (refresh), needs special process for manufacturing
- Cheap (one bit costs only one transistor plus one capacitor)
- Flash Memory (~T)
- Much slower, access takes a long time, non-volatile
- Very cheap (one transistor stores 16 bits or no transistors involved)
Notes:
- 17

## Slide 18: Outline
- Outline
- SRAM
- DRAM:
- HBM
- DDR
- SSD
- Hard Disk

## Slide 19: Cerebras’s Wafer Scale Engine (2019)
- Cerebras’s Wafer Scale Engine (2019)
- Cerebras WSE
- 1.2 Trillion transistors
- 46,225 mm2
- Largest GPU
- 21.1 Billion transistors
- 815 mm2
- The largest ML accelerator chip
- 400,000 cores
- 18 GB of on-chip memory
- 9 PB/s memory bandwidth
- NVIDIA TITAN V
- https://www.anandtech.com/show/14758/hot-chips-31-live-blogs-cerebras-wafer-scale-deep-learning
- https://www.cerebras.net/cerebras-wafer-scale-engine-why-we-need-big-chips-for-deep-learning/
Notes:
- The Wafer-Scale Engine is the most massive AI chip ever produced and packs a whopping 400,000 cores in a 46,225mm2 footprint.
- 19

## Slide 20: Cerebras’s Wafer Scale Engine-2 (2021)
- Cerebras’s Wafer Scale Engine-2 (2021)
- Cerebras WSE-2
- 2.6 Trillion transistors
- 46,225 mm2
- Largest GPU
- 54.2 Billion transistors
- 826 mm2
- NVIDIA Ampere GA100
- https://cerebras.net/product/#overview
- The largest ML accelerator chip
- 850,000 cores
- 40 GB of on-chip memory
- 20 PB/s memory bandwidth
Notes:
- 20

## Slide 21: Cerebras’s Wafer Scale Engine-3 (2024)
- Cerebras’s Wafer Scale Engine-3 (2024)
- Cerebras WSE-3
- 4 Trillion transistors
- 46,225 mm2
- Largest GPU B100
- 204.8 Billion transistors
- 826 mm2
- NVIDIA Blackwell
- https://cerebras.net/product/#overview
- The largest ML accelerator chip
- 900,000 cores
- 44 GB of on-chip memory
- 21 PB/s memory bandwidth
Notes:
- 21

## Slide 22: Memory in a Modern System
- Memory in a Modern System
- CORE 1
- L2 CACHE 0
- SHARED L3 CACHE
- DRAM INTERFACE
- CORE 0
- CORE 2
- CORE 3
- L2 CACHE 1
- L2 CACHE 2
- L2 CACHE 3
- DRAM BANKS
- DRAM MEMORY CONTROLLER

## Slide 23: Memory System: A Shared Resource View
- Memory System: A Shared Resource View
- Storage
- Most of the system is dedicated to storing and moving data

## Slide 24: SRAM (Programmer’s View)
- SRAM (Programmer’s View)

## Slide 25: Quick Overview of Memory Arrays
- Quick Overview of Memory Arrays
Notes:
- 25

## Slide 26: Array Organization of Memories
- Array Organization of Memories
- Goal: Efficiently store large amounts of data
- A memory array (stores data)
- Address selection logic (selects one row of the array)
- Readout circuitry (reads data out)
- An M-bit value can be read or written at each unique N-bit address
- All values can be accessed, but only M-bits at a time
- Access restriction allows more compact organization
Notes:
- 26

## Slide 27: Recall: A Bigger Memory Array (4 locations X 3 bits)
- Recall: A Bigger Memory Array (4 locations X 3 bits)
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

## Slide 28: Memory Arrays
- Memory Arrays
- Two-dimensional array of bit cells
- Each bit cell stores one bit
- An array with N address bits and M data bits:
- 2N rows and M columns
- Depth: number of rows (number of words)
- Width: number of columns (size of word)
- Array size: depth × width = 2N × M
Notes:
- 28

## Slide 29: 22 × 3-bit array:
- 22 × 3-bit array:
- Number of words: 4
- Word size: 3-bits
- For example, the 3-bit word stored at address 10 is 100
- Memory Array Example
Notes:
- 29

## Slide 30: Larger and Wider Memory Array Example
- Larger and Wider Memory Array Example
Notes:
- 30

## Slide 31: Memory Array Organization (I)
- Memory Array Organization (I)
- Memory Array:
- Bitline: Storage nodes in one column connected to one bitline
- Wordline: Address decoder activates only ONE wordline, content of one line of storage available at output
Notes:
- 31

## Slide 32: Memory Array Organization (II)
- Memory Array Organization (II)
- Memory Array:
- Bitline: Storage nodes in one column connected to one bitline
- Wordline: Address decoder activates only ONE wordline, content of one line of storage available at output
- 10
- 1
- 0
- 0
- Active wordline
Notes:
- 32

## Slide 33: General Architecture of SRAM
- General Architecture of SRAM
- Access transistors (that are configured as switches) connect the bit storage to the bitline
- Access controlled by the wordline
- SRAM bit
Notes:
- 33

## Slide 34: A Bit of static random access memory (SRAM)
- A Bit of static random access memory (SRAM)
- Two cross coupled inverters store a single bit
- Feedback path enables the stored value to persist in the “cell”
- 4 transistors for storage
- 2 transistors for access
- A SRAM Bit
- row enable
- bitline
- _bitline
Notes:
- 34

## Slide 35: SRAM
- SRAM
- Goal: buffering data on chip to reduce external memory traffic
- Advantage: random access still keeps high performance
- Disadvantage: low capacity (multiple MBs)
- Where to Use SRAM?
- Cache in CPU
- Shared memory in GPU
- On-chip buffer in AI accelerator
- How to Use SRAM?
- Multiple small separate SRAMs: low latency and high throughput
- Banked design: wide access ports
- Summary of SRAM
Notes:
- 35

## Slide 36: Memory Banking
- Memory Banking
- Memory is divided into banks that can be accessed independently; banks share address and data buses (to minimize pin cost)
- Can start and complete one bank access per cycle
- Can sustain N concurrent accesses if all N go to different banks
- Bank
- 0
- Bank
- 1
- MDR
- MAR
- Bank
- 2
- Bank
- 15
- MDR
- MAR
- MDR
- MAR
- MDR
- MAR
- Data bus
- Address bus
- CPU
- Picture credit: Derek Chiou

## Slide 37: Memory Bank Organization and Operation
- Memory Bank Organization and Operation
- Read access sequence:
- 1. Decode row address & drive word-lines
- 2. Selected bits drive bit-lines
- • Entire row read
- 3. Amplify row data
- 4. Decode column address & select subset of row
- • Send to output
- 5. Precharge bit-lines
- • For next access

## Slide 38: SRAM (Static Random Access Memory)
- SRAM (Static Random Access Memory)
- bit-cell array
- 2n row x 2m-col
- (nm to minimize
- overall latency)
- sense amp and mux
- 2m diff pairs
- 2n
- n
- m
- 1
- row enable
- bitline
- _bitline
- n+m
- Read Sequence:
- 1. address decode
- 2. drive row select
- 3. selected bit-cells drive bitlines
- (entire row is read together)
- 4. differential sensing and column select
- (data is ready)
- 5. precharge all bitlines
- (for next read or write)
- Access latency dominated by steps 2 and 3
- Cycling time dominated by steps 2, 3 and 5
- step 2 proportional to 2m
- step 3 and 5 proportional to 2n

## Slide 39: A Large Fraction of CPU Chips is SRAM
- A Large Fraction of CPU Chips is SRAM
- SRAM (Cache) in a CPU
- Half chip area is occupied by cache
- 10MB (2.5MB/core * 4 cores)

## Slide 40: Comparison of Memories
- Comparison of Memories
- Capacity
- SRAM
- HBM
- DRAM
- SSD
- DISK
- Latency
- Bandwidth
- SRAM
- HBM
- DRAM
- SSD
- DISK
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DRAM
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 41: Outline
- Outline
- SRAM
- DRAM:
- HBM
- DDR
- SSD
- Hard Disk

## Slide 42: Comparison of Memories
- Comparison of Memories
- Capacity
- SRAM
- HBM
- DDR
- SSD
- DISK
- Latency
- Bandwidth
- SRAM
- HBM
- DDR
- SSD
- DISK
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DDR
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 43: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Performance Characteristics of Memory
- Refresh

## Slide 44: A Computing System
- A Computing System
- Three key components
- Computation
- Communication
- Storage/memory
- Burks, Goldstein, von Neumann, “Preliminary discussion of the
- logical design of an electronic computing instrument,” 1946.
- Image source: https://lbsitbytes2010.wordpress.com/2013/03/29/john-von-neumann-roll-no-15/

## Slide 45: What is A Computer?
- What is A Computer?
- We will cover all three components
- Memory
- (program
- and data)
- I/O
- Processing
- control
- (sequencing)
- datapath

## Slide 46: The Main Memory System
- The Main Memory System
- Main memory is a critical component of all computing systems: server, mobile, embedded, desktop, sensor
- Main memory system must scale (in size, technology, efficiency, cost, and management algorithms) to maintain performance growth and technology scaling benefits
- Processors
- and caches
- Main Memory
- Storage (SSD/HDD)

## Slide 47: The Main Memory System
- The Main Memory System
- Main memory is a critical component of all computing systems: server, mobile, embedded, desktop, sensor
- Main memory system must scale (in size, technology, efficiency, cost, and management algorithms) to maintain performance growth and technology scaling benefits
- Main Memory
- Storage (SSD/HDD)
- FPGAs

## Slide 48: The Main Memory System
- The Main Memory System
- Main memory is a critical component of all computing systems: server, mobile, embedded, desktop, sensor
- Main memory system must scale (in size, technology, efficiency, cost, and management algorithms) to maintain performance growth and technology scaling benefits
- Main Memory
- Storage (SSD/HDD)
- GPUs

## Slide 49: Memory Is Very Important
- Memory Is Very Important
Notes:
- 49

## Slide 50: Computation is Bottlenecked by Memory
- Computation is Bottlenecked by Memory
- Important workloads, e.g., AI, are all data intensive
- They require rapid and efficient processing of large amounts of data
- Data is increasing
- We can generate more than we can process

## Slide 51: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 52: Application Perspective
- Application Perspective
Notes:
- 52

## Slide 53: Memory Is Critical for Performance (I)
- Memory Is Critical for Performance (I)
- In-Memory Data Analytics
- [Clapp+ (Intel), IISWC’15;
- Awan+, BDCloud’15]
- Datacenter Workloads [Kanev+ (Google), ISCA’15]
- In-memory Databases
- [Mao+, EuroSys’12; Clapp+ (Intel), IISWC’15]
- Graph/Tree Processing
- [Xu+, IISWC’12; Umuroglu+, FPL’15]
Notes:
- 53

## Slide 54: Memory Is Critical for Performance (I)
- Memory Is Critical for Performance (I)
- In-Memory Data Analytics
- [Clapp+ (Intel), IISWC’15;
- Awan+, BDCloud’15]
- Datacenter Workloads [Kanev+ (Google), ISCA’15]
- In-memory Databases
- [Mao+, EuroSys’12; Clapp+ (Intel), IISWC’15]
- Graph/Tree Processing
- [Xu+, IISWC’12; Umuroglu+, FPL’15]
- Memory → bottleneck
Notes:
- 54

## Slide 55: Memory Is Critical for Performance (II)
- Memory Is Critical for Performance (II)
- Chrome
- Google’s web browser
- TensorFlow Mobile
- Google’s machine learning framework
- Video Playback
- Google’s video codec
- Video Capture
- Google’s video codec
Notes:
- In this work, we take
- a look at widely-used
- google
- consumer workloads, to figure out the major sources of energy consumption.
- We look at Google Chrome web
- brower
- . We take a look at
- Tensorflow
- , Google’s machine learning framework, and we also take a look at two important video related workloads, video playback and video capture, both rely on Google’s vp9 codec technology.
- 55

## Slide 56: Memory Is Critical for Performance (II)
- Memory Is Critical for Performance (II)
- Chrome
- Google’s web browser
- TensorFlow Mobile
- Google’s machine learning framework
- Video Playback
- Google’s video codec
- Video Capture
- Google’s video codec
- Memory → bottleneck
Notes:
- In this work, we take
- a look at widely-used
- google
- consumer workloads, to figure out the major sources of energy consumption.
- We look at Google Chrome web
- brower
- . We take a look at
- Tensorflow
- , Google’s machine learning framework, and we also take a look at two important video related workloads, video playback and video capture, both rely on Google’s vp9 codec technology.
- 56

## Slide 57: Genome Analysis
- Genome Analysis
- 1
- 2
- Sequencing
- Read Mapping
- 3
- 4
- Variant Calling
- Scientific Discovery
Notes:
- Genome analysis starts with sequencing random short DNA fragments of copies of the original molecule.
- Unfortunately,
- these reads
- lack information about their order and which part of genome they are originated from.
- Hence
- the second step is to map these reads to a long reference genome.
- 57

## Slide 58: Genome Analysis
- Genome Analysis
- 1
- 2
- Sequencing
- Read Mapping
- 3
- 4
- Variant Calling
- Scientific Discovery
- Memory → bottleneck
Notes:
- Genome analysis starts with sequencing random short DNA fragments of copies of the original molecule.
- Unfortunately,
- these reads
- lack information about their order and which part of genome they are originated from.
- Hence
- the second step is to map these reads to a long reference genome.
- 58

## Slide 59: Memory Is Critical for DNN
- Memory Is Critical for DNN
- Google’s web browser
- Memory Capacity → bottleneck
Notes:
- In this work, we take
- a look at widely-used
- google
- consumer workloads, to figure out the major sources of energy consumption.
- We look at Google Chrome web
- brower
- . We take a look at
- Tensorflow
- , Google’s machine learning framework, and we also take a look at two important video related workloads, video playback and video capture, both rely on Google’s vp9 codec technology.
- 59

## Slide 60: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 61: Performance Perspective
- Performance Perspective
Notes:
- 61

## Slide 62: Memory Bottleneck
- Memory Bottleneck
- “It’s the Memory, Stupid!” (Richard Sites, MPR, 1996)
- Mutlu+, “Runahead Execution: An Alternative to Very Large Instruction Windows for Out-of-Order Processors,” HPCA 2003.

## Slide 63: The Memory Bottleneck
- The Memory Bottleneck
- http://cva.stanford.edu/classes/cs99s/papers/architects_look_to_future.pdf

## Slide 64: The Memory Bottleneck
- The Memory Bottleneck
- All of Google’s Data Center Workloads (2015):
- Kanev+, “Profiling a Warehouse-Scale Computer,” ISCA 2015.

## Slide 65: The Memory Bottleneck
- The Memory Bottleneck
- All of Google’s Data Center Workloads (2015):
- Kanev+, “Profiling a Warehouse-Scale Computer,” ISCA 2015.

## Slide 66: Energy Perspective
- Energy Perspective
Notes:
- 66

## Slide 67: Data Movement vs. Computation Energy
- Data Movement vs. Computation Energy
- Dally, HiPEAC 2015

## Slide 68: Data Movement vs. Computation Energy
- Data Movement vs. Computation Energy
- Dally, HiPEAC 2015
- A memory access consumes ~100-1000X
- the energy of a complex addition

## Slide 69: Data Movement vs. Computation Energy
- Data Movement vs. Computation Energy
- Han+, “EIE: Efficient Inference Engine on Compressed Deep Neural Network,” ISCA 2016.

## Slide 70: Data Movement vs. Computation Energy
- Data Movement vs. Computation Energy
- Han+, “EIE: Efficient Inference Engine on Compressed Deep Neural Network,” ISCA 2016.
- A memory access consumes ~6400X
- the energy of an integer addition
- 6400X

## Slide 71: Data Movement vs. Computation Energy
- Data Movement vs. Computation Energy
- TABLE:
  | 32-bit Operation | Energy (pJ) | ADD (int) Relative Cost |
  | ADD (int) | 0.1 | 1 |
  | ADD (float) | 0.9 | 9 |
  | Register File | 1 | 10 |
  | MULT (int) | 3.1 | 31 |
  | MULT (float) | 3.7 | 37 |
  | SRAM Cache | 5 | 50 |
  | DRAM | 640 | 6400 |
- Han+, “EIE: Efficient Inference Engine on Compressed Deep Neural Network,” ISCA 2016.
- A memory access consumes ~6400X
- the energy of an integer addition

## Slide 72: Memory is Critical for Energy
- Memory is Critical for Energy
- Amirali Boroumand, Saugata Ghose, Youngsok Kim, Rachata Ausavarungnirun, Eric Shiu, Rahul Thakur, Daehyun Kim, Aki Kuusela, Allan Knies, Parthasarathy Ranganathan, and Onur Mutlu,"Google Workloads for Consumer Devices: Mitigating Data Movement Bottlenecks" Proceedings of the 23rd International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Williamsburg, VA, USA, March 2018.
- 62.7% of the total system energy
- is spent on data movement

## Slide 73: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 74: Reliability Perspective
- Reliability Perspective
Notes:
- 74

## Slide 75: Memory is Critical for Reliability
- Memory is Critical for Reliability
- Data from all of Facebook’s servers worldwide
- Meza+, “Revisiting Memory Errors in Large-Scale Production Data Centers,” DSN’15.
- As memory
- capacity increases, system reliability reduces

## Slide 76: Outline of DRAM
- Outline of DRAM
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 77: Abstraction: Virtual vs. Physical Memory
- Abstraction: Virtual vs. Physical Memory
- Programmer sees virtual memory
- Can assume the memory is “infinite”
- Reality: Physical memory size is much smaller than what the programmer assumes
- The system (system software + hardware, cooperatively) maps virtual memory addresses to physical memory
- The system automatically manages the physical memory space transparently to the programmer
- + Programmer does not need to know the physical size of memory nor manage it  A small physical memory can appear as a huge one to the programmer  Life is easier for the programmer
- -- More complex system software and architecture
- A classic example of the programmer/(micro)architect tradeoff

## Slide 78: Idealism
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

## Slide 79: DRAM Capacity, Bandwidth & Latency
- DRAM Capacity, Bandwidth & Latency
- 128x
- 20x
- 1.3x
Notes:
- 79

## Slide 80: Key Messages behind Memory
- Key Messages behind Memory
- Memory Optimizations aim at size, bandwidth, not latency.
- A memory read/write may need a few DDR operations, e.g., ACTIVATE, column, Prechange, within a memory chip…
- Different access sequence leads to different throughput, sequential > random.
- Random access is slow is the output, low row buffer miss rate is the source.

## Slide 81: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 82: Memory Technology: DRAM
- Memory Technology: DRAM
- Dynamic random access memory (DRAM)
- Capacitor charge state indicates stored value
- Whether the capacitor is charged or discharged indicates storage of 1 or 0
- 1 capacitor
- 1 access transistor
- Capacitor leaks through the RC path
- DRAM cell loses charge over time
- DRAM cell needs to be refreshed
- row enable
- bitline

## Slide 83: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 84: Building Larger Memories
- Building Larger Memories
- Goal: Requires larger memory arrays
- Challenge: Large memory  slow
- How do we make the memory large without making it too slow?
- Idea: Divide the memory into smaller arrays and interconnect the arrays to input/output buses
- Large memories are hierarchical array structures
- DRAM: Channel  Rank  Bank  Subarrays  Mats

## Slide 85: General Principle: Interleaving (Banking)
- General Principle: Interleaving (Banking)
- Interleaving (banking)
- Problem: a single monolithic large memory array takes long to access and does not enable multiple accesses in parallel
- Goal: Reduce the latency of memory array access and enable multiple accesses in parallel
- Idea: Divide a large array into multiple banks that can be accessed independently (in the same cycle or in consecutive cycles)
- Each bank is smaller than the entire memory storage
- Accesses to different banks can be overlapped
- A Key Issue: How do you map data to different banks? (i.e., how do you interleave data across banks?)

## Slide 86: Recall: Memory Banking
- Recall: Memory Banking
- Memory is divided into banks that can be accessed independently; banks share address and data buses (to minimize pin cost)
- Can start and complete one bank access per cycle
- Can sustain N concurrent accesses if all N go to different banks
- Bank
- 0
- Bank
- 1
- MDR
- MAR
- Bank
- 2
- Bank
- 15
- MDR
- MAR
- MDR
- MAR
- MDR
- MAR
- Data bus
- Address bus
- CPU
- Picture credit: Derek Chiou

## Slide 87: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 88: The DRAM SubsystemThe Top-Down View
- The DRAM SubsystemThe Top-Down View
Notes:
- 88

## Slide 89: DRAM Subsystem Organization
- DRAM Subsystem Organization
- Channel
- DIMM
- Rank
- Chip
- Bank
- Row/Column

## Slide 90: The DRAM Subsystem
- The DRAM Subsystem
- Memory channel
- Memory channel
- DIMM (Dual in-line memory module)
- Processor
- “Channel”

## Slide 91: Breaking down a DIMM (module)
- Breaking down a DIMM (module)
- DIMM (Dual in-line memory module)
- Side view
- Front of DIMM
- Back of DIMM

## Slide 92: Breaking down a DIMM (module)
- Breaking down a DIMM (module)
- DIMM (Dual in-line memory module)
- Side view
- Front of DIMM
- Back of DIMM
- Rank 0: collection of 8 chips
- Rank 1

## Slide 93: Rank
- Rank
- Rank 0 (Front)
- Rank 1 (Back)
- Data <0:63>
- CS <0:1>
- Addr/Cmd
- <0:63>
- <0:63>
- Memory channel

## Slide 94: Breaking down a Rank
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

## Slide 95: Breaking down a Chip
- Breaking down a Chip
- Chip 0
- <0:7>
- TABLE:
  |  |  |  |  |  |  |
  |  |  |  |  |  |  |
  |  |  |  |  |  |  |
  |  |  |  |  |  |  |
  |  |  |  |  |  |  |
  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |
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

## Slide 96: Breaking down a Bank
- Breaking down a Bank
- Bank 0
- <0:7>
- row 0
- row 32k-1
- ...
- 2kB
- 1B
- 1B (column)
- TABLE:
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
- 1B
- Row-buffer
- 1B
- ...
- <0:7>

## Slide 97: DRAM Subsystem Organization
- DRAM Subsystem Organization
- Channel
- DIMM
- Rank
- Chip
- Bank
- Row/Column

## Slide 98: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Channel 0
- DIMM 0
- Rank 0
- Mapped to

## Slide 99: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- . . .

## Slide 100: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- Row 0
- Col 0
- . . .

## Slide 101: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- 8B
- Row 0
- Col 0
- . . .
- 8B

## Slide 102: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- 8B
- Row 0
- Col 1
- . . .

## Slide 103: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- 8B
- 8B
- Row 0
- Col 1
- . . .
- 8B

## Slide 104: Example: Transferring a cache block
- Example: Transferring a cache block
- 0xFFFF…F
- 0x00
- 0x40
- ...
- 64B
- cache block
- Physical memory space
- Rank 0
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Chip 0
- Chip 1
- Chip 7
- <0:7>
- <8:15>
- <56:63>
- Data <0:63>
- 8B
- 8B
- Row 0
- Col 1
- A 64B cache block takes 8 I/O cycles to transfer.
- During the process, 8 columns are read sequentially.
- . . .

## Slide 105: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Address Bits
- Memory Access
- Refresh

## Slide 106: Address Bits of Memory
- Address Bits of Memory
- Address Bits of SRAM
- SRAM always exists in the same chip with compute units.
- Relatively small number of address bits due its small capacity.
- Address Bits of DRAM
- DRAM has separate chips from compute units, so pin numbers can become bottleneck due to physical limitation.
- Large number of address bits in direct mapping due to large memory capacity
- Solution: Multiplex the address bits for channel, bank, row, column Causing performance issue…

## Slide 107: Micron’s 8Gb x8 DDR3 chip
- Micron’s 8Gb x8 DDR3 chip

## Slide 108: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Address Bits
- Memory Access
- Refresh

## Slide 109: Memory Bank Organization and Operation
- Memory Bank Organization and Operation
- Read access sequence:
- 1. Decode row address & drive word-lines
- 2. Selected bits drive bit-lines
- • Entire row read
- 3. Amplify row data
- 4. Decode column address & select subset of row
- • Send to output
- 5. Precharge bit-lines
- • For next access

## Slide 110: DRAM (Dynamic Random Access Memory)
- DRAM (Dynamic Random Access Memory)
- row enable
- _bitline
- bit-cell array
- 2n row x 2m-col
- (nm to minimize
- overall latency)
- sense amp and mux
- 2m
- 2n
- n
- m
- 1
- RAS
- CAS
- A DRAM die comprises
- of multiple such arrays
- Read Sequence:
- 1. address decode
- 2. drive row select
- 3. selected bit-cells drive bitlines
- 4. a “flip-flopping” sense amp amplifies and regenerates the bitline, data bit is mux’ed out
- 5. precharge all bitlines
- Destructive reads
- Charge loss over time
- Refresh: A DRAM controller must periodically read each row within the allowed refresh time (10s of ms) such that charge is restored

## Slide 111: Digging Deeper: DRAM Bank Operation
- Digging Deeper: DRAM Bank Operation
- Row Buffer
- (Row 0, Column 0)
- Row decoder
- Column mux
- Row address 0
- Column address 0
- Data
- Row 0
- Empty
- (Row 0, Column 1)
- Column address 1
- (Row 0, Column 85)
- Column address 85
- (Row 1, Column 0)
- HIT
- HIT
- Row address 1
- Row 1
- Column address 0
- CONFLICT !
- Columns
- Rows
- Access Address:
- This view of a bank is an abstraction.
- Internally, a bank consists of many cells (transistors & capacitors) and other structures that enable access
- to cells

## Slide 112: Three DRAM Access States
- Three DRAM Access States
- Page Hit:
- Occurs when a memory transaction accesses a row that is open in its bank, so no Precharge and Activate commands are required before the column access, resulting in minimum latency.
- Page Closed:
- Occurs when a memory transaction accesses a row whose corresponding bank is closed, so the row Activate command is required before the column access.
- Page Miss:
- Occurs when a memory transaction accesses a row that does not match the active row in the bank, so one Precharge command and one Activate command are issued before the column access, resulting in maximum latency.

## Slide 113: Take-away Message
- Take-away Message
- row 0
- row 32k-1
- ...
- 2kB
- 1B
- 1B (column)
- TABLE:
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
- 1B
- Row-buffer
- 1B
- ...
- <0:7>
- App address to memory address: channel, DIMM, rank, row, column
- Sequential: column, column
- Random: pre-charge previous row, activate new row, column
- Sequential > Random:
- Row buffer hit vs. Row buffer miss.

## Slide 114: Key Messages behind Memory
- Key Messages behind Memory
- Memory Optimizations aim at size, bandwidth, not latency.
- A memory read/write may need a few DDR operations, e.g., ACTIVATE, Column, Prechange, within a memory chip…
- Different access sequence leads to different throughput, sequential (mainly row buffer hit) > random (mainly row buffer miss).
- Random access is slow is the output, low row buffer miss rate is the source.

## Slide 115: DRAM vs. SRAM
- DRAM vs. SRAM
- DRAM
- Slower access (capacitor)
- Higher density (1T 1C cell)
- Lower cost
- Requires refresh (power, performance, circuitry)
- Manufacturing requires putting capacitor and logic together
- SRAM
- Faster access (no capacitor)
- Lower density (6T cell)
- Higher cost
- No need for refresh
- Manufacturing compatible with logic process (no capacitor)

## Slide 116: Outline
- Outline
- Motivation and Goals
- Application Perspective
- Performance Perspective
- Reliability Perspective
- Background and Architecture of Memory
- High Level Abstraction
- SRAM vs. DRAM
- Banking
- Architecture of DRAM
- Performance Characteristics of Memory
- Memory Access
- Address Bits
- Refresh

## Slide 117: DRAM Refresh
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

## Slide 118: Refresh Overhead: Performance
- Refresh Overhead: Performance
- 8%
- 46%
- Liu et al., “RAIDR: Retention-Aware Intelligent DRAM Refresh,” ISCA 2012.

## Slide 119: Refresh Overhead: Energy
- Refresh Overhead: Energy
- 15%
- 47%
- Liu et al., “RAIDR: Retention-Aware Intelligent DRAM Refresh,” ISCA 2012.

## Slide 120: High Bandwidth Memory (HBM)
- High Bandwidth Memory (HBM)
Notes:
- 120

## Slide 121: HBM
- HBM
- HBM stack:
- It is used in conjunction with high-end GPUs, AI ASICs and FPGAs.
- Each stack has 4/8 DRAM dies and a logic die.
Notes:
- Substrate:
- 底座
- Interposer:
- 插入式选样
- 121

## Slide 122: HBM in Nvidia A100
- HBM in Nvidia A100
- A100 GPU: 6 HBM2 stacks at the left/right side.

## Slide 123: HBM in Nvidia A100
- HBM in Nvidia A100
- A100 GPU: 6 HBM2 stacks at the left/right side.

## Slide 124: Advantage and Disadvantage of HBM
- Advantage and Disadvantage of HBM
- Advantage of HBM:
- High bandwidth: ~500GB/s per stack.
- Low power consumption: due to running without termination.
- Disadvantage of HBM:
- Less flexibility: fixed, in the same package with compute chip.
- Low capacity: really close to compute chip.
- High cost: strict condition.
Notes:
- Termination is needed when CPU is long away from memory. However, HBM is close to accelerator,
- so
- termination
- is
- not
- needed.
- 124

## Slide 125: HBM Trend
- HBM Trend
Notes:
- 速度在增长，但芯片密度没增长，是严重问题
- https://mp.weixin.qq.com/s/6HrH_Fpm2fGUHXnHNxfW5g
- 125

## Slide 126: HBM Trend
- HBM Trend
Notes:
- 速度在增长，但芯片密度没增长，是严重问题
- https://mp.weixin.qq.com/s/6HrH_Fpm2fGUHXnHNxfW5g
- 126

## Slide 127: Memory Benchmarking Tool on FPGA
- Memory Benchmarking Tool on FPGA
- CPU
- FPGA
- Latency
- Parameter
- PCIe
- ...
- AXI
- AXI
- AXI
- AXI
- 32 AXI channels
- Engine 2
- Write
- Read
- Engine 1
- Write
- Read
- Engine 32
- Write
- Read
- Engine 31
- Write
- Read
- HBM:450MHz
- PCIe:250MHz
- Latency
- Latency
- Latency
- Software Code
- Parameter & Latency:
- run-time parameters & latency numbers
- Read/Write Engine:
- one for each AXI channel
- Shuhai: a benchmarking tool that allows to demystify details of memory, e.g., DDR4.
- Wang et al., “Shuhai: Benchmarking High Bandwidth Memory on FPGAs,” FCCM 2020.
Notes:
- To this end, we propose
- Shuhai
- ,
- a benchmarking tool that allows to demystify details of memory, e.g., HBM and DDR4. The architecture of
- is shown at the left.
- has three parts.
- The first part is read/write engine, which is directly attached to the targeted memory whose interface is AXI. An engine is associated with a memory channel such that the performance potential of each memory channel is fully explored.
- The second part is parameter and latency modules, where one latency module is associated with an engine module and the parameter module is used to pass parameters to benchmarking engines.
- The third part is the CPU code, which runs C++ code to bring the flexibility of running various benchmarking tasks.
- 127

## Slide 128: Why Benchmarking on FPGA?
- Why Benchmarking on FPGA?
- 1, Benchmark memory: FPGA > CPU/GPU
- Memory
- FPGA
- ALU
- Memory
- CPU/GPU
- ALU
- Cache
Notes:
- Why we need
- Shuhai
- , there can summarize two reasons.
- First, in terms of benchmarking memory, it can be done better on FPGA, rather than on CPU/GPU.
- In particular, when benchmarking memory on
- cpu
- or
- gpu
- , we cannot get rid of the negative effect of cache in the CPU/GPU. So there is a lot of work about benchmarking cache on the
- /
- , rather than benchmarking memory.
- In contrast, when benchmarking memory on the FPGA, the benchmarking engine can directly attach to the memory such that there is no noise between memory and benchmarking engine.
- 128

## Slide 129: Effect of Refresh
- Effect of Refresh
- X-axis: index of read transaction,
- Y-axis: latency of read transaction
- Observations:
- We Use Latency Tester:
- B=32, S=64, W=0x100000, N =1024
- 1, The memory transaction that coincides a refresh has obviously long latency.
Notes:
- First we examine the effect of DRAM refresh. When a memory channel is operating, memory cells should be refreshed repetitively such that the information in each memory cell is not lost. Normal memory read/write transactions are not allowed during a refresh, so a memory transaction that coincides a refresh will have a obviously longer latency.
- To this end, we use the latency tester in an engine to illustrate the effect of refresh, with the parameters: B=32, S=64, N=1024.
- The result shows in the left figure, where X-axis is the index of read transaction and Y-axis is the latency of read transaction. From the figure, we can have two observations.
- First, the memory transaction that coincides a refresh has obviously long latency.
- 129

## Slide 130: Effect of Refresh
- Effect of Refresh
- X-axis: index of read transaction,
- Y-axis: latency of read transaction
- Observations:
- Configuration:
- B=32, S=64, W=0x100000, N =1024
- 1, The transaction that coincides a refresh has obviously long latency.
- 2, The Interval between any two consecutive refresh commands is roughly the same.
Notes:
- Second, the interval between any two consecutive refresh commands is roughly the same.
- 130

## Slide 131: Comparison of Memories
- Comparison of Memories
- Capacity
- SRAM
- HBM
- DDR
- SSD
- DISK
- Latency
- Bandwidth
- SRAM
- HBM
- DDR
- SSD
- DISK
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DDR
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 132: Outline
- Outline
- SRAM
- DRAM:
- HBM
- DDR
- SSD
- Hard Disk

## Slide 133: NVME SSD
- NVME SSD
- Advantage: Large memory size, e.g., 16TB per SSD
- Disadvantage: Low throughput, high latency, hard to use
- Samsung PM853T 960GB Enterprise SSD (from https://www.tweaktown.com/reviews/6695/samsung-pm853t-960gb-enterprise-ssd-review/index.html)
- Core
- Core
- Core
- HW
- Flash Ctrl.
- HW
- Flash Ctrl.
- HW
- Flash Ctrl.
- HW
- Flash Ctrl.
- Request Handler
- ECC/Randomizer
- Encryption Engine
- SSD Controller
- NAND Packages
- 8×128 GB = 1 TB
- LPDDR DRAM
- 0.001×1,024 = 1 GB

## Slide 134: SSD
- SSD
- Host Processor
- (CPU, GPU)
- Main
- Memory
- Write
- Read
- Storage
- Write
- Read
- Memory Bandwidth tens to hundreds of GB/s
- Storage I/O Bandwidth ~ 8 GB/s
- Data Movement Bottleneck
- Computation

## Slide 135: Comparison of Memories
- Comparison of Memories
- Capacity
- SRAM
- HBM
- DDR
- SSD
- DISK
- Latency
- Bandwidth
- SRAM
- HBM
- DDR
- SSD
- DISK
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~100GB/s
- DISK
- SSD
- DDR
- HBM
- SRAM
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~1TB/s

## Slide 136: Intel Optane Persistent Memory (2019)
- Intel Optane Persistent Memory (2019)
- Non-volatile main memory
- Based on 3D-XPoint Technology
- https://www.storagereview.com/intel_optane_dc_persistent_memory_module_pmm

## Slide 137: An Aside: Phase Change Memory
- An Aside: Phase Change Memory
- Phase change material (chalcogenide glass) exists in two states:
- Amorphous: Low optical reflexivity and high electrical resistivity
- Crystalline: High optical reflexivity and low electrical resistivity
- PCM is resistive memory: High resistance (0), Low resistance (1)
- Lee, Ipek, Mutlu, Burger, “Architecting Phase Change Memory as a Scalable DRAM Alternative,” ISCA 2009.

## Slide 138: Outline
- Outline
- Motivation and Goals
- Background and Architecture of Memory
- Performance Characteristics of Memory

## Slide 139: Key Messages behind Memory
- Key Messages behind Memory
- Memory Optimizations aim at size, bandwidth, not latency.
- A memory read/write may need a few operations within a memory chip…
- Different access sequence leads to different throughput, sequential > random.
- Random access is slow due to low row buffer miss rate.

## Slide 140: Mystery #3: DRAM Refresh
- Mystery #3: DRAM Refresh

## Slide 141: DRAM in the System
- DRAM in the System
- CORE 1
- L2 CACHE 0
- SHARED L3 CACHE
- DRAM INTERFACE
- CORE 0
- CORE 2
- CORE 3
- L2 CACHE 1
- L2 CACHE 2
- L2 CACHE 3
- DRAM BANKS
- Multi-Core
- Chip
- *Die photo credit: AMD Barcelona
- DRAM MEMORY CONTROLLER
Notes:
- 141

## Slide 142: A DRAM Cell
- A DRAM Cell
- A DRAM cell consists of a capacitor and an access transistor
- It stores data in terms of charge status of the capacitor
- A DRAM chip consists of (10s of 1000s of) rows of such cells
- wordline
- bitline
- bitline
- bitline
- bitline
- bitline
- (row enable)
Notes:
- 142

## Slide 143: How Do We Solve the Problem?
- How Do We Solve the Problem?
- Observation: All DRAM rows are refreshed every 64ms.
- Critical thinking: Do we need to refresh all rows every 64ms?
- What if we knew what happened underneath and exposed that information to upper layers?

## Slide 144: Underneath: Retention Time Profile of DRAM
- Underneath: Retention Time Profile of DRAM
- Liu et al., “RAIDR: Retention-Aware Intelligent DRAM Refresh,” ISCA 2012.

## Slide 145: Aside: Why Do We Have Such a Profile?
- Aside: Why Do We Have Such a Profile?
- Answer: Manufacturing is not perfect
- Not all DRAM cells are exactly the same
- Some are leakier than others
- This is called Manufacturing Process Variation

## Slide 146: Opportunity: Taking Advantage of This Profile
- Opportunity: Taking Advantage of This Profile
- Assume we know the retention time of each row exactly
- What can we do with this information?
- Who do we expose this information to?
- How much information do we expose?
- Affects hardware/software overhead, power consumption, verification complexity, cost
- How do we determine this profile information?
- Also, who determines it?
- Microarchitecture
- ISA (Architecture)
- Program/Language
- Algorithm
- Problem
- Logic
- Devices
- Runtime System
- (VM, OS, MM)
- Electrons

## Slide 147: Retention Time of DRAM Rows
- Retention Time of DRAM Rows
- Observation: Overwhelming majority of DRAM rows can be refreshed much less often without losing data
- Can we exploit this to reduce refresh operations at low cost?
- Only ~1000 rows in 32GB DRAM need refresh every 64 ms,
- but we refresh all rows every 64ms
- Key Idea of RAIDR: Refresh weak rows more frequently,
- all other rows less frequently
- Liu et al., “RAIDR: Retention-Aware Intelligent DRAM Refresh,” ISCA 2012.

## Slide 148: RAIDR: Eliminating Unnecessary DRAM Refreshes
- RAIDR: Eliminating Unnecessary DRAM Refreshes
- Liu, Jaiyen, Veras, Mutlu,
- RAIDR: Retention-Aware Intelligent DRAM Refresh
- ISCA 2012.

## Slide 149: 1. Profiling: Identify the retention time of all DRAM rows
- 1. Profiling: Identify the retention time of all DRAM rows
-  can be done at design time or during operation
- 2. Binning: Store rows into bins by retention time
-  use Bloom Filters for efficient and scalable storage
- 3. Refreshing: Memory controller refreshes rows in different bins at different rates
-  check the bins to determine refresh rate of a row
- RAIDR: Mechanism
- 1.25KB storage in controller for 32GB DRAM memory
- Liu et al., “RAIDR: Retention-Aware Intelligent DRAM Refresh,” ISCA 2012.

## Slide 150: RAIDR: Results and Takeaways
- RAIDR: Results and Takeaways
- System: 32GB DRAM, 8-core; Various workloads
- RAIDR hardware cost: 1.25 kB (2 Bloom filters)
- Refresh reduction: 74.6%
- Dynamic DRAM energy reduction: 16%
- Idle DRAM power reduction: 20%
- Performance improvement: 9%
- Benefits increase as DRAM scales in density

## Slide 151: Takeaway
- Takeaway
- Breaking the abstraction layers (between components and transformation hierarchy levels)
- and knowing what is underneath
- enables you to understand and solve problems

## Slide 152: Reading for the Really Interested
- Reading for the Really Interested
- Jamie Liu, Ben Jaiyen, Richard Veras, and Onur Mutlu,"RAIDR: Retention-Aware Intelligent DRAM Refresh"Proceedings of the 39th International Symposium on Computer Architecture (ISCA), Portland, OR, June 2012. Slides (pdf)

## Slide 153: Really Interested? … Further Readings
- Really Interested? … Further Readings
- Onur Mutlu,"Memory Scaling: A Systems Architecture Perspective"Technical talk at MemCon 2013 (MEMCON), Santa Clara, CA, August 2013. Slides (pptx) (pdf) Video
- Kevin Chang, Donghyuk Lee, Zeshan Chishti, Alaa Alameldeen, Chris Wilkerson, Yoongu Kim, and Onur Mutlu,"Improving DRAM Performance by Parallelizing Refreshes with Accesses" Proceedings of the 20th International Symposium on High-Performance Computer Architecture (HPCA), Orlando, FL, February 2014. Slides (pptx) (pdf)

## Slide 154: Detailed Lectures on Memory Refresh
- Detailed Lectures on Memory Refresh
- Computer Architecture, Fall 2020, Lecture 2b
- Data Retention and Memory Refresh (ETH Zürich, Fall 2020)
- https://www.youtube.com/watch?v=v702wUnaWGE&list=PL5Q2soXY2Zi9xidyIgBxUz7xRPS-wisBN&index=3
- Computer Architecture, Fall 2020, Lecture 3b
- Memory Systems: Challenges & Opportunities (ETH Zürich, Fall 2020)
- https://www.youtube.com/watch?v=Q2FbUxD7GHs&list=PL5Q2soXY2Zi9xidyIgBxUz7xRPS-wisBN&index=6
- Computer Architecture, Fall 2020, Lecture 4a
- Memory Systems: Solution Directions (ETH Zürich, Fall 2020)
- https://www.youtube.com/watch?v=PANTCVTYe8M&list=PL5Q2soXY2Zi9xidyIgBxUz7xRPS-wisBN&index=7
- https://www.youtube.com/onurmutlulectures

## Slide 155: Memory Refresh Lecture …
- Memory Refresh Lecture …
- Computer Architecture, Fall 2020, Lecture 2b
- Data Retention and Memory Refresh (ETH Zürich, Fall 2020)
- https://www.youtube.com/watch?v=v702wUnaWGE&list=PL5Q2soXY2Zi9xidyIgBxUz7xRPS-wisBN&index=3

## Slide 156: Mystery #4: Memory Performance Attacks
- Mystery #4: Memory Performance Attacks

## Slide 157: Multi-Core Systems
- Multi-Core Systems
- CORE 1
- L2 CACHE 0
- SHARED L3 CACHE
- DRAM INTERFACE
- CORE 0
- CORE 2
- CORE 3
- L2 CACHE 1
- L2 CACHE 2
- L2 CACHE 3
- DRAM BANKS
- Multi-Core
- Chip
- *Die photo credit: AMD Barcelona
- DRAM MEMORY CONTROLLER
Notes:
- 157

## Slide 158: A Trend: Many Cores on Chip
- A Trend: Many Cores on Chip
- Simpler and lower power than a single large core
- Parallel processing on single chip  faster, new applications
- IBM Cell BE8+1 cores
- Intel Core i78 cores
- Tilera TILE Gx
- 100 cores, networked
- IBM POWER7
- 8 cores
- Intel SCC
- 48 cores, networked
- Nvidia Fermi
- 448 “cores”
- AMD Barcelona
- 4 cores
- Sun Niagara II
- 8 cores

## Slide 159: Many Cores on Chip
- Many Cores on Chip
- What we want:
- N times the system performance with N times the cores
- What do we get today?

## Slide 160: Unexpected Slowdowns in Multi-Core
- Unexpected Slowdowns in Multi-Core
- Memory Performance Hog
- Low priority
- High priority
- (Core 0)
- (Core 1)
- Moscibroda and Mutlu, “Memory performance attacks: Denial of memory service
- in multi-core systems,” USENIX Security 2007.
Notes:
- What kind of performance do we expect when we run two applications on a multi-core system? To answer this question, we performed an experiment. We took two applications we cared about, ran them together on different cores in a dual-core system, and measured their slowdown compared to when each is run alone on the same system. This graph shows the slowdown each app experienced. (DATA explanation…)
- Why do we get such a large disparity in the slowdowns?
- Is it the priorities? No. We went back and gave high priority to gcc and low priority to matlab. The slowdowns did not change at all. Neither the software or the hardware enforced the priorities.
- Is it the contention in the disk? We checked for this possibility, but found that these applications did not have any disk accesses in the steady state. They both fit in the physical memory and therefore did not interfere in the disk.
- What is it then? Why do we get such large disparity in slowdowns in a dual core system?
- I will call such an application a
- “
- memory performance hog
- ”
- Now, let me tell you why this disparity in slowdowns happens.
- Is it that there are other applications or the OS interfering with gcc, stealing its time quantums? No.
- 160

## Slide 161: Three Questions
- Three Questions
- Can you figure out why the applications slow down if you do not know the underlying system and how it works?
- Can you figure out why there is a disparity in slowdowns if you do not know how the system executes the programs?
- Can you fix the problem without knowing what is happening “underneath”?

## Slide 162: Three Questions
- Three Questions
- Why is there any slowdown?
- Why is there a disparity in slowdowns?
- How can we solve the problem if we do not want that disparity?
- What do we want (the system to provide)?

## Slide 163: Why Is This Important?
- Why Is This Important?
- We want to execute applications in parallel in multi-core systems  consolidate more and more
- Cloud computing
- Mobile phones
- We want to mix different types of applications together
- those requiring QoS guarantees (e.g., video, pedestrian detection)
- those that are important but less so
- those that are less important
- We want the system to be controllable and high performance

## Slide 164: Why the Disparity in Slowdowns?
- Why the Disparity in Slowdowns?
- CORE 1
- CORE 2
- L2
- CACHE
- L2
- CACHE
- DRAM MEMORY CONTROLLER
- DRAM
- Bank 0
- DRAM
- Bank 1
- DRAM
- Bank 2
- Shared DRAM
- Memory System
- Multi-Core
- Chip
- INTERCONNECT
- DRAM
- Bank 3
Notes:
- 164

## Slide 165: Why the Disparity in Slowdowns?
- Why the Disparity in Slowdowns?
- CORE 1
- CORE 2
- L2
- CACHE
- L2
- CACHE
- DRAM MEMORY CONTROLLER
- DRAM
- Bank 0
- DRAM
- Bank 1
- DRAM
- Bank 2
- Shared DRAM
- Memory System
- Multi-Core
- Chip
- unfairness
- INTERCONNECT
- matlab
- gcc
- DRAM
- Bank 3
Notes:
- 165
- -In a multi-core chip, different cores share some hardware resources. In particular, they share the DRAM memory system. The shared memory system consists of this and that.
- When we run matlab on one core, and gcc on another core, both cores generate memory requests to access the DRAM banks. When these requests arrive at the DRAM controller, the controller favors matlab
- ’
- s requests over gcc
- s requests. As a result, matlab can make progress and continues generating memory requests. These requests are again favored by the DRAM controller over gcc
- s requests. Therefore, gcc starves waiting for its requests to be serviced in DRAM whereas matlab makes very quick progress as if it were running alone.
- Why does this happen? This is because the algorithms employed by the DRAM controller are unfair.
- But, why are these algorithms unfair? Why do they unfairly prioritize matlab accesses?
- To understand this, we need to understand how a DRAM bank operates.
- Almost all systems today contain multi-core chips
- Multi-core systems consist of multiple on-chip cores and caches
- Cores share the DRAM memory system
- DRAM memory system consists of
- DRAM banks that store data (multiple banks to allow parallel accesses)
- DRAM memory controller that mediates between cores and DRAM memory
- It schedules memory operations generated by cores to DRAM
- This talk is about exploiting the unfair algorithms in the memory controllers to perform denial of service to running threads
- To understand how this happens, we need to know about how each DRAM bank operates

## Slide 166: DRAM Controllers
- DRAM Controllers
- A row-conflict memory access takes significantly longer than a row-hit access
- Current controllers take advantage of this fact
- Commonly used scheduling policy (FR-FCFS) [Rixner 2000]*
- (1) Row-hit first: Service row-hit memory accesses first
- (2) Oldest-first: Then service older accesses first
- This scheduling policy aims to maximize DRAM throughput
- *Rixner et al., “Memory Access Scheduling,” ISCA 2000.
- *Zuravleff and Robinson, “Controller for a synchronous DRAM …,” US Patent 5,630,096, May 1997.
Notes:
- 166

## Slide 167: The Problem
- The Problem
- Multiple applications share the DRAM controller
- DRAM controllers designed to maximize DRAM data throughput
- DRAM scheduling policies are unfair to some applications
- Row-hit first: unfairly prioritizes apps with high row buffer locality
- Threads that keep on accessing the same row
- Oldest-first: unfairly prioritizes memory-intensive applications
- DRAM controller vulnerable to denial of service attacks
- Can write programs to exploit unfairness
Notes:
- 167

## Slide 168: // initialize large arrays A, B
- // initialize large arrays A, B
- for (j=0; j<N; j++) {
- index = rand();
- A[index] = B[index];
- …
- }
- A Memory Performance Hog
- STREAM
- Sequential memory access
- Very high row buffer locality (96% hit rate)
- Memory intensive
- RANDOM
- Random memory access
- Very low row buffer locality (3% hit rate)
- Similarly memory intensive
- // initialize large arrays A, B
- for (j=0; j<N; j++) {
- index = j*linesize;
- A[index] = B[index];
- …
- }
- streaming
- (in sequence)
- random
- Moscibroda and Mutlu, “Memory Performance Attacks,” USENIX Security 2007.
Notes:
- 168
- Streaming through memory by performing operations on two 1D arrays.
- Sequential memory access
- Each access is a cache miss (elements of array larger than a cache line size)
-  hence, very memory intensive
- Link to the real code…

## Slide 169: What Does the Memory Hog Do?
- What Does the Memory Hog Do?
- Row Buffer
- Row decoder
- Column mux
- Data
- Row 0
- T0: Row 0
- Row 0
- T1: Row 16
- T0: Row 0
- T1: Row 111
- T0: Row 0
- T0: Row 0
- T1: Row 5
- T0: Row 0
- T0: Row 0
- T0: Row 0
- T0: Row 0
- T0: Row 0
- Memory Request Buffer
- T0: STREAM
- T1: RANDOM
- Row size: 8KB, request size: 64B
- 128 (8KB/64B) requests of STREAM serviced before a single request of RANDOM
- Moscibroda and Mutlu, “Memory Performance Attacks,” USENIX Security 2007.
Notes:
- 169
- Pictorially demonstrate how stream denies memory service to rdarray
- Stream continuously accesses columns in row 0 in a streaming manner (streams through a row after opening it)
- In other words almost all its requests are row-hits
- RDarray
- ’
- s requests are row-conflicts (no locality)
- The DRAM controller reorders streams requests to the open row over other requests (even older ones) to maximize DRAM throughput
- Hence, rdarray
- s requests do not get serviced as long as stream is issuing requests at a fast-enough rate
- In this example, the red thread
- s request to another row will not get serviced until stream stops issuing a request to row 0
- With those parameters, 128 requests of stream would be serviced before 1 from rdarray
- As row-buffer size increases, which is the industry trend, this problem will become more severe
- This is not the worst case, but it is easy to construct and understand
- Stream falls off the row buffer at some point
- I leave it to the listeners to construct a case worse than this (it is possible)

## Slide 170: Now That We Know What Happens Underneath
- Now That We Know What Happens Underneath
- How would you solve the problem?
- What is the right place to solve the problem?
- Programmer?
- System software?
- Compiler?
- Hardware (Memory controller)?
- Hardware (DRAM)?
- Circuits?
- Two major goals of this course:
- Enable you to think critically
- Enable you to think broadly
- Microarchitecture
- ISA (Architecture)
- Program/Language
- Algorithm
- Problem
- Logic
- Devices
- Runtime System
- (VM, OS, MM)
- Electrons

## Slide 171: Why Is Memory So Important? (Especially Today)
- Why Is Memory So Important? (Especially Today)
Notes:
- 171

## Slide 172: State of the Main Memory System
- State of the Main Memory System
- Recent technology, architecture, and application trends
- lead to new requirements
- exacerbate old requirements
- DRAM and memory controllers, as we know them today, are (will be) unlikely to satisfy all requirements
- Some emerging non-volatile memory technologies (e.g., PCM) enable new opportunities: memory + storage merging
- Rethink the main memory system, especially for AI.
- to fix DRAM issues and enable emerging technologies
- to satisfy all requirements

## Slide 173: Major Trends Affecting Main Memory (I)
- Major Trends Affecting Main Memory (I)
- Need for main memory capacity, bandwidth, QoS increasing
- Main memory energy/power is a key system design concern
- DRAM technology scaling is ending

## Slide 174: Major Trends Affecting Main Memory (II)
- Major Trends Affecting Main Memory (II)
- Need for main memory capacity, bandwidth, QoS increasing
- Multi-core: increasing number of cores/agents
- Data-intensive applications: increasing demand for data
- Consolidation: cloud computing, GPUs, mobile, heterogeneity
- Main memory energy/power is a key system design concern
- DRAM technology scaling is ending

## Slide 175: Consequence: The Memory Capacity Gap
- Consequence: The Memory Capacity Gap
- Memory capacity per core expected to drop by 30% every two years
- Trends worse for memory bandwidth per core !
- Core count doubling ~ every 2 years
- DRAM DIMM capacity doubling ~ every 3 years
- Lim et al., ISCA 2009

## Slide 176: Computation is Bottlenecked by Memory
- Computation is Bottlenecked by Memory
- Important workloads are all data intensive
- They require rapid and efficient processing of large amounts of data
- Data is increasing
- We can generate more than we can process

## Slide 177: Outline
- Outline
- Motivation and Goals
- Background and Architecture of Memory
- Performance Characteristics of Memory

## Slide 178: Micron’s 8Gb x8 DDR3 chip
- Micron’s 8Gb x8 DDR3 chip
- Dynamic random access memory
- Capacitor charge state indicates stored value
- Whether the capacitor is charged or discharged indicates storage of 1 or 0
- Capacitor leaks through the RC path
- DRAM cell loses charge over time
- DRAM cell needs to be refreshed

## Slide 179: Micron’s 8Gb x8 DDR3 chip
- Micron’s 8Gb x8 DDR3 chip
- Dynamic random access memory
- Capacitor charge state indicates stored value
- Whether the capacitor is charged or discharged indicates storage of 1 or 0
- Capacitor leaks through the RC path
- DRAM cell loses charge over time
- DRAM cell needs to be refreshed

## Slide 180: Comparison of Memories
- Comparison of Memories
- Three key components
- Computation
- Communication
- Storage/memory
- SRAM
- HBM
- DDR
- SSD
- DISK
- Capacity
- SRAM
- HBM
- DDR
- SSD
- DISK
- Latency
- DISK
- SSD
- DDR
- HBM
- SRAM
- Bandwidth
- ~10MB
- ~10GB
- ~100GB
- ~1TB
- ~10TB
- ~1ns
- ~100ns
- ~100ns
- ~1us
- ~1ms
- ~10MB/s
- ~1GB/s
- ~10GB/s
- ~100GB/s
- ~1TB/s