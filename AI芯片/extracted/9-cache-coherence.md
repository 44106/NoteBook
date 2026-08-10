# 9-cache-coherence.pptx

- Slides: 89

## Slide 1: Computer Arch. & AI ChipLecture 9: Cache and Cache Coherence

### Extracted Shape Text
- Computer Arch. & AI ChipLecture 9: Cache and Cache Coherence
- Prof. Zeke Wang
- Zhejiang University
- 25 April 2025

### Notes
- 1

## Slide 2: HBM GB/s

### Extracted Shape Text
- HBM GB/s
- Recall: Memory Roofline Model
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
- 2

## Slide 3: Recall: The Problem of Memory

### Extracted Shape Text
- Recall: The Problem of Memory
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
- 3

## Slide 4: Recall: The Memory Hierarchy

### Extracted Shape Text
- Recall: The Memory Hierarchy
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

## Slide 5: Recall: Cache Abstraction and Metrics

### Extracted Shape Text
- Recall: Cache Abstraction and Metrics
- Cache hit rate = (# hits) / (# hits + # misses) = (# hits) / (# accesses)
- Address
- Tag Store
- (Valid bit +
- Address tag +
- Replacement policy bits)
- Data Store
- (stores
- memory
- blocks)
- Hit/miss?
- Data

### Notes
- Reducing AMAT is not always beneficial for performance. The direct metric is instruction throughput, which might be orthogonal to latency.
- 5

## Slide 6: Recall: Addressing the Cache

- Images: 4; Tables: 0

### Extracted Shape Text
- Recall: Addressing the Cache
- Cache access:
- 1) index into the tag and data stores with index bits in address;
- 2) checks valid bit in tag store;
- 3) compares tag bits in address with the stored tag in tag store;
- 4) If a block is in the cache (cache hit), the stored tag should be valid and match the tag of the block, and read out data.

### Notes
- 6

## Slide 7: Recall: Three Cache Organization Methods

- Images: 1; Tables: 0

### Extracted Shape Text
- Recall: Three Cache Organization Methods
- Fully-associative:
- A chunk can go to any cache block in the cache. (One extreme)
- Direct-mapped:
- A chunk can go to only one cache block in the cache. (Another extreme)
- Set-associative:
- A chunk can go to N cache blocks in the N-way set-associative cache. (Best choice)
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014

## Slide 8: Direct-Mapped Cache: Placement and Access

### Extracted Shape Text
- Direct-Mapped Cache: Placement and Access
- Direct-mapped (A block can go to only one location)
- Assume memory: 256 bytes, 8-byte blocks  32 blocks
- Assume cache: 64 bytes, 8 blocks
- Blocks with same set contend for the same cache location
- Cause conflict misses when accessing blocks in green consecutively
- Tag store
- Data store
- Address
- tag
- set
- byte in block
- 3 bits
- 3 bits
- 2b
- V
- tag
- =?
- MUX
- byte in block
- Hit?
- Data
- Block: 00000
- Block: 00001
- Block: 00010
- Block: 00011
- Block: 00100
- Block: 00101
- Block: 00110
- Block: 00111
- Block: 01000
- Block: 01001
- Block: 01010
- Block: 01011
- Block: 01100
- Block: 01101
- Block: 01110
- Block: 01111
- Block: 10000
- Block: 10001
- Block: 10010
- Block: 10011
- Block: 10100
- Block: 10101
- Block: 10110
- Block: 10111
- Block: 11000
- Block: 11001
- Block: 11010
- Block: 11011
- Block: 11100
- Block: 11101
- Block: 11110
- Block: 11111
- Main memory:

## Slide 9: Full Associativity

### Extracted Shape Text
- Full Associativity
- Fully-associative cache
- A block can be placed in any cache location
- Tag store
- Data store
- =?
- =?
- =?
- =?
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
- byte in block
- 3 bits
- 5 bits

## Slide 10: Set-Associative Cache

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
- set
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

## Slide 11: Where Are We?

- Images: 1; Tables: 0

### Extracted Shape Text
- Where Are We?

## Slide 12: Caching Basics

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

## Slide 13: Replacement in Set-Associative Caches

### Extracted Shape Text
- Replacement in Set-Associative Caches
- Key Challenge:
- Which cache block in a set be replaced once new block comes?

## Slide 14: Cache Block Replacement Policy

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

## Slide 15: Implementing LRU

### Extracted Shape Text
- Implementing LRU
- Idea: Evict the least recently accessed block
- Problem: Need to keep track of access ordering of blocks
- Question: 2-way set associative cache:
- What do you need to implement LRU perfectly?
- Question: 4-way (or 16-way) set associative cache:
- What do you need to implement LRU perfectly?
- Extremely challenging to implement LRU in hardware.

### Notes
- 2-way: use one bit to indicate
- 4-way: 3 bit
- 8-way: 7-bit.
- 8-way: 8
- 路
- Set-associative:
- 组相关
- 15

## Slide 16: Approximations of LRU

### Extracted Shape Text
- Approximations of LRU
- Most modern processors do not implement “true LRU” (also called “perfect LRU”) in highly-associative caches
- Instead, approximate LRU is chosen. Why?
- True LRU is complex
- LRU is an approximation to predict locality anyway (i.e., not the best possible cache management policy)

## Slide 17: One Implementation of LRU

- Images: 2; Tables: 0

### Extracted Shape Text
- One Implementation of LRU
- Pseudo LRU for 8-way set-associated cache:
- Assume 8 blocks (L0~L7) for a set, 7 rule bits (B0~B6).
- PLRU Replacement Way Selection: choosing the suitable way (L0~L7) based on the PLRU bits.
- PLRU Bits Updating Rule: updating PLRU bits after replacing the way (L0~L7).
- PLRU Replacement Way Selection:
- PLRU Bits Updating Rule:

## Slide 18: Cache Replacement Policy: LRU or Random

### Extracted Shape Text
- Cache Replacement Policy: LRU or Random
- LRU vs. Random: LRU is not always better.
- Example: 4-way cache, cyclic references to A, B, C, D, E
- 0% hit rate with LRU policy
- Set thrashing: When the “program working set” in a set is larger than set associativity
- Random replacement policy is better when thrashing occurs
- Which one is better in practice?
- Depends on workload
- Average hit rate of LRU and Random are similar
- Best of both Worlds: Hybrid of LRU and Random
- How to choose between the two?
- Intel CPU uses the hybrid approach.

## Slide 19: What Is the Optimal Replacement Policy?

### Extracted Shape Text
- What Is the Optimal Replacement Policy?
- Belady’s OPT (Optimal Replacement)
- Replace the block that is going to be referenced furthest in the future by the program
- Belady, “A study of replacement algorithms for a virtual-storage computer,” IBM Systems Journal, 1966.
- How do we implement this? Simulate?
- No possibility to implement in theory.
- Lots of potential in practice

### Notes
- Application knows…
- 19

## Slide 20: Caching Basics

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

## Slide 21: Cache Policies: Handling Memory Write

### Extracted Shape Text
- Cache Policies: Handling Memory Write
- Where should you write the result of a store? One policy for each step.
- Step 1: store insn.  cache, either policy works:
- Write-allocate policy (memory, default):
- Allocate the cache line (put it in the cache).
- Issue: Read an entire cache block from memory
- Write-no-allocate policy (PCIe/IO):
- Write it directly to memory without allocation in cache.
- Ignore cache.
- Step 2: cache  memory, either policy works:
- Write-back policy (default):
- Writes it to the cache and wait until the cache kicks the cache block out
- Write-through policy (streaming write instruction):
- Writes it to the cache and memory right away

### Notes
- 4 combinations…
- 21

## Slide 22: Cache: Write-back vs. Write-through

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

## Slide 23: Caching Basics

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

## Slide 24: Instruction vs. Data Caches

### Extracted Shape Text
- Instruction vs. Data Caches
- Core question: Separate or Unified?
- Pros and Cons of Unified Cache:
- + Dynamic sharing of cache space: no overprovisioning that might happen with static partitioning (i.e., separate I and D caches)
- -- Instructions and data can thrash each other (i.e., no guaranteed space for either)
- -- I and D are accessed in different places in the pipeline. Where do we place the unified cache for fast access?
- Modern CPU:
- First level caches are almost always split
- Higher level caches are almost always unified

## Slide 25: Classification of Cache Misses

### Extracted Shape Text
- Classification of Cache Misses
- Compulsory miss
- Defined as the first reference to an address (block), always resulting in a miss
- Capacity miss
- defined as the misses that would occur even in a fully-associative cache (with optimal replacement) of the same capacity
- Cause: cache is too small to hold everything needed
- Conflict miss
- defined as any miss that is neither a compulsory nor a capacity miss

### Notes
- Miss:
- 缺失
- 25

## Slide 26: How to Reduce Each Miss Type

### Extracted Shape Text
- How to Reduce Each Miss Type
- Compulsory miss
- Caching cannot help
- Prefetching can: Anticipate which blocks will be needed soon
- Conflict miss
- More associativity
- Other ways to get more associativity without making the cache associative
- Victim cache
- Better, randomized indexing
- Software hints?
- Capacity miss
- Utilize cache space better: keep blocks that will be referenced
- Software management: divide working set and computation such that each “computation phase” fits in cache

### Notes
- 26

## Slide 27: Cache Performance

### Extracted Shape Text
- Cache Performance

### Notes
- 27

## Slide 28: Cache Parameters vs. Miss/Hit Rate

### Extracted Shape Text
- Cache Parameters vs. Miss/Hit Rate
- Cache size
- Block size
- Associativity
- Replacement policy
- Insertion/Placement policy

## Slide 29: How to Improve Cache Performance

### Extracted Shape Text
- How to Improve Cache Performance
- Three fundamental goals
- Reducing miss rate
- Caveat: reducing miss rate can reduce performance if more costly-to-refetch blocks are evicted
- Reducing miss latency or miss cost
- Reducing hit latency or hit cost
- The above three together affect performance

## Slide 30: Cache Terminology

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
- 30

## Slide 31: Cache Organization Recap

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
- 31

## Slide 32: How is data found?

### Extracted Shape Text
- How is data found?
- Cache organized into S sets
- Each memory address maps to exactly one set
- Caches categorized by number of blocks in a set:
- Direct mapped: 1 block per set
- N-way set associative: N blocks per set
- Fully associative: all cache blocks are in a single set
- Examine each organization for a cache with:
- Capacity (C = 8 words)
- Block size (b = 1 word)
- So, number of blocks (B = 8)

### Notes
- 32

## Slide 33: Direct Mapped Cache

### Extracted Shape Text
- Direct Mapped Cache

### Notes
- 33

## Slide 34: Direct Mapped Cache Hardware

### Extracted Shape Text
- Direct Mapped Cache Hardware

### Notes
- 34

## Slide 35: Direct Mapped Cache Performance

### Extracted Shape Text
- Direct Mapped Cache Performance
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0xC($0)
- lw $t3, 0x8($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate =

### Notes
- 35

## Slide 36: Direct Mapped Cache Performance

### Extracted Shape Text
- Direct Mapped Cache Performance
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0xC($0)
- lw $t3, 0x8($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate = 3/15 = 20%
- Temporal LocalityCompulsory Misses

## Slide 37: Direct Mapped Cache: Conflict

### Extracted Shape Text
- Direct Mapped Cache: Conflict
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0x24($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate =

## Slide 38: Direct Mapped Cache: Conflict

### Extracted Shape Text
- Direct Mapped Cache: Conflict
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0x24($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate = 10/10 = 100%
- Conflict Misses

## Slide 39: N-Way Set Associative Cache

### Extracted Shape Text
- N-Way Set Associative Cache

### Notes
- 39

## Slide 40: N-way Set Associative Performance

### Extracted Shape Text
- N-way Set Associative Performance
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0x24($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate =

### Notes
- N
- 路组相关映射
- 40

## Slide 41: N-way Set Associative Performance

### Extracted Shape Text
- N-way Set Associative Performance
- # MIPS assembly code
- addi $t0, $0, 5
- loop: beq $t0, $0, done
- lw $t1, 0x4($0)
- lw $t2, 0x24($0)
- addi $t0, $t0, -1
- j loop
- done:
- Miss Rate = 2/10
- = 20%
- Associativity reduces conflict misses

## Slide 42: Cache Size

### Extracted Shape Text
- Cache Size
- Cache size: total data (not including tag) capacity
- bigger can exploit temporal locality better
- not ALWAYS better
- Too large a cache adversely affects hit and miss latency
- smaller is faster => bigger is slower
- access time may degrade critical path
- Too small a cache
- doesn’t exploit temporal locality well
- useful data replaced often
- Working set: the whole set of data the executing application references
- Within a time interval
- hit rate
- cache size
- “working set”
- size

## Slide 43: Block size is the data that is associated with an address tag

### Extracted Shape Text
- Block size is the data that is associated with an address tag
- Too small blocks
- don’t exploit spatial locality well
- have larger tag overhead
- Too large blocks
- too few total # of blocks  less
- temporal locality exploitation
- waste of cache space and bandwidth/energy
- if spatial locality is not high
- Block Size
- hit rate
- block
- size

## Slide 44: Associativity

### Extracted Shape Text
- Associativity
- How many blocks can be present in the same index (i.e., set)?
- Larger associativity
- lower miss rate (reduced conflicts)
- higher hit latency and area cost (plus diminishing returns)
- Smaller associativity
- lower hit rate
- lower cost
- lower hit latency
- Especially important for L1 caches
- associativity
- hit rate

### Notes
- 44

## Slide 45: Cache in a Multi-Core CPU

### Extracted Shape Text
- Cache in a Multi-Core CPU

### Notes
- 45

## Slide 46: Recall: Multi-Core over Large Superscalar

### Extracted Shape Text
- Recall: Multi-Core over Large Superscalar
- Technology push
- Instruction issue queue size limits the cycle time of the superscalar, OoO processor  diminishing performance
- Quadratic increase in complexity with issue width
- Large, multi-ported register files to support large instruction windows and issue widths  more resources, reduced frequency or longer RF access, diminishing performance
- Application pull
- Multiple applications run together on your CPU
- Olukotun et al., “The Case for a Single-Chip Multiprocessor,” ASPLOS 1996.

### Notes
- What does application pull mean?
- 46

## Slide 47: Challenge from Multi-core CPU

### Extracted Shape Text
- Challenge from Multi-core CPU
- Cache is needed to relieve the negative effect of long memory latency.
- How to design cache for multiple cores?
- Cores want a consistent view of memory.

### Notes
- What does application pull mean?
- 47

## Slide 48: Caches in a Multi-Core System

- Images: 2; Tables: 0

### Extracted Shape Text
- Caches in a Multi-Core System
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

## Slide 49: Caches in Multi-Core CPU

### Extracted Shape Text
- Caches in Multi-Core CPU
- Cache efficiency becomes even more important in a multi-core/multi-threaded system
- Memory bandwidth is at premium
- Cache space is a limited resource across cores/threads
- How do we design the caches in a multi-core system?
- Many decisions:
- Shared vs. private caches
- How to preserve coherence and consistence?

### Notes
- Premium:
- 49

## Slide 50: Private vs. Shared Caches

### Extracted Shape Text
- Private vs. Shared Caches
- Private cache:
- Cache belongs to one core (a shared block can be in multiple caches)
- Shared cache:
- Cache is shared by multiple cores.
- CORE 0
- CORE 1
- CORE 2
- CORE 3
- L2
- CACHE
- L2
- CACHE
- L2
- CACHE
- DRAM MEMORY CONTROLLER
- L2
- CACHE
- CORE 0
- CORE 1
- CORE 2
- CORE 3
- DRAM MEMORY CONTROLLER
- L2
- CACHE

## Slide 51: Resource Sharing Concept and Advantages

### Extracted Shape Text
- Resource Sharing Concept and Advantages
- Idea: Instead of dedicating a hardware resource to a hardware context, allow multiple contexts to use it
- Example resources: functional units, pipeline, caches, buses, memory
- Why?
- + Resource sharing improves utilization/efficiency  throughput
- When a resource is left idle by one thread, another thread can use it; no need to replicate shared data
- + Reduces communication latency
- For example, data shared between multiple threads can be kept in the same cache in multithreaded processors
- + Compatible with the shared memory programming model

## Slide 52: Resource Sharing Disadvantages

### Extracted Shape Text
- Resource Sharing Disadvantages
- Resource sharing results in contention for resources
- When the resource is not idle, another thread cannot use it
- If space is occupied by one thread, another thread needs to re-occupy it
- - Sometimes reduces each or some thread’s performance
- - Thread performance can be worse than when it is run alone
- - Eliminates performance isolation  inconsistent performance across runs
- - Thread performance depends on co-executing threads
- - Uncontrolled (free-for-all) sharing degrades QoS
- - Causes unfairness, starvation
- Need to efficiently and fairly utilize shared resources

## Slide 53: Shared Caches Between Cores

### Extracted Shape Text
- Shared Caches Between Cores
- Advantages:
- High effective capacity
- Dynamic partitioning of available cache space
- No fragmentation due to static partitioning
- If one core does not utilize some space, another core can
- Easier to maintain coherence (a cache block is in a single location)
- Disadvantages
- Slower access (cache not tightly coupled with the core)
- Cores incur conflict misses due to other cores’ accesses
- Misses due to inter-core interference
- Some cores can destroy the hit rate of other cores
- Guaranteeing a minimum level of service (or fairness) to each core is harder (how much space, how much bandwidth?)

## Slide 54: Caches in Multi-Core CPU

### Extracted Shape Text
- Caches in Multi-Core CPU
- Cache efficiency becomes even more important in a multi-core/multi-threaded system
- Memory bandwidth is at premium
- Cache space is a limited resource across cores/threads
- How do we design the caches in a multi-core system?
- Many decisions:
- Shared vs. private caches
- How to preserve coherence and consistence?

### Notes
- Premium:
- 54

## Slide 55: Memory Consistency vs. Cache Coherence

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
- 55

## Slide 56: Cache Coherence

### Extracted Shape Text
- Cache Coherence

## Slide 57: Features of Cache Coherence

### Extracted Shape Text
- Features of Cache Coherence
- Cache Coherence: Multiple cores have a consistent state of the last written value from any core to a memory address.
- Program order preservation: core C writes to the address and then reads from the same address, C gets value written.
- Coherent memory view: if C1 performs “mem[X] = 1”, after a sufficient time, C2 will read 1 from “mem[X]”.
- Write serialization: writes to the same address by different processors are seen in same order by all processors.
- C
- Memory
- Write 1
- Read 1
- C1
- Memory
- Write 1
- Read 1
- C2
- C1
- Memory
- Write 1
- Write 2
- C2

## Slide 58: Hardware Architecture for Cache Coherence

### Extracted Shape Text
- Hardware Architecture for Cache Coherence
- Hardware architecture for Cache Coherence:
- Cores, caches, interconnect, memory work together to achieve cache coherence from core’s point of view.
- Cache Tags: MESI (CPU action  Bus action, Tags)
- Cache Updating: invl./update (Bus action)
- Interconnect: Bus/Switch
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

## Slide 59: Cache Coherence: Interconnect

### Extracted Shape Text
- Cache Coherence: Interconnect
- Cache Interconnect: cores communicate with each other.
- Bus:
- One valid at a time
- Typically used by Snooping
- Switch:
- Peer-to-peer communication
- Typically used by directory
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
- 59

## Slide 60: Cache Interconnect: Bus-based Protocol

### Extracted Shape Text
- Cache Interconnect: Bus-based Protocol
- Core
- Bus (One trans. a time)
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
- Bus-based protocol:
- 1, A cache arbitrates for bus access, waiting until 2 happens
- 2, A cache is granted bus access
- 3, A cache places command on bus, waiting until 4 happens
- 4, Other caches place responses on bus

## Slide 61: Cache Interconnect: Switch-based Protocol

### Extracted Shape Text
- Cache Interconnect: Switch-based Protocol
- Core
- Switch (P2P)
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
- Switch-based protocol:
- Each core pair can independently communicate with each other.

## Slide 62: Cache Coherence: Cache Updating

### Extracted Shape Text
- Cache Coherence: Cache Updating
- Hardware architecture for Cache Coherence:
- Cores, caches, interconnect, memory work together to achieve cache coherence from core’s point of view.
- Cache Tags: MESI (CPU action  Bus action, Tags)
- Cache Updating: invl./update (Bus action)
- Interconnect: Bus/Switch
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

## Slide 63: Cache Coherence: Updating Policy

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
- 63

## Slide 64: Bus Action: Update vs. Invalidate

### Extracted Shape Text
- Bus Action: Update vs. Invalidate
- Where and When: On a bus action write miss:
- 1, Update Protocol:
- Broadcast written data and address to cores
- Cores update the data in their caches if block is present
- 2, Invalidate Protocol:
- Broadcast invalidation of address to sharers
- Cores invalidate block in their caches if block is present

## Slide 65: Tradeoffs: Update vs. Invalidate

### Extracted Shape Text
- Tradeoffs: Update vs. Invalidate
- Which do we want?
- Write frequency and sharing behavior are critical
- Update Protocol
- + If sharer set is constant and updates are infrequent, avoids the cost of invalidate-reacquire (broadcast update pattern)
- - If data is rewritten without intervening reads by other cores, updates would be useless
- - Write-through cache policy  bus becomes bottleneck
- Invalidate Protocol
- + After invalidation broadcast, core has exclusive access rights
- + Only cores that keep reading after each write retain a copy
- - If write contention is high, leads to ping-ponging (rapid invalidation-reacquire traffic from different processors)

### Notes
- Invalidate Protocol is main stream.
- 65

## Slide 66: Cache Coherence: Cache Tags

### Extracted Shape Text
- Cache Coherence: Cache Tags
- Hardware architecture for Cache Coherence:
- Cores, caches, interconnect, memory work together to achieve cache coherence from core’s point of view.
- Cache Tags: MESI (CPU action  Bus action, Tags)
- Cache Updating: invl./update (Bus action)
- Interconnect: Bus/Switch
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

## Slide 67: Cache Coherence: Cache Tags

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
- 67

## Slide 68: State Diagrams for CPU Requests

### Extracted Shape Text
- State Diagrams for CPU Requests
- I
- S
- M
- Core read miss
- Read miss on bus
- Core write miss
- Write miss on bus
- Core read hit
- Core read hit
- Core write hit
- Core write hit
- Invalidate on bus
- Core memory read/write  Cache states, Bus action:
- Miss in local cache
- Hit in local cache
- Bus action (Outside)  Cache states:
- Invalidate
- Write miss
- Read miss
- CPU action
- Bus action
- Cache blocks
- Tags
- Bus actions affects the overall performance of multi-core CPU.
- Core
- Starter

## Slide 69: State Diagrams for Bus Requests

### Extracted Shape Text
- State Diagrams for Bus Requests
- I
- S
- M
- Core read miss
- Read miss on bus
- Core write miss
- Write miss on bus
- Core read hit
- Core read hit
- Core write hit
- Core write hit
- Invalidate on bus
- Core memory read/write  Cache states, Bus action:
- Miss in local cache
- Hit in local cache
- Bus action (Outside)  Cache states:
- Invalidate
- Write miss
- Read miss
- I
- S
- M
- Invalidate/Write miss
- Read miss
- Bus action
- Cache blocks
- Tags
- Read miss
- Cache response
- Write back block to requesting cache and memory
- Write miss
- Write back block to requesting cache and memory
- Bus actions affects the overall performance of multi-core CPU.
- Cache
- Starter

## Slide 70: The Problem with MSI

- Images: 0; Tables: 1

### Extracted Shape Text
- The Problem with MSI
- A block is not in cache at the beginning. On a read, the block immediately goes to the “Shared” state.
- Problem: The core issues a bus action invalidate before writing the block to cache, even when only one cache copy exists.

| Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
| --- | --- | --- | --- | --- | --- |
| t0 |  |  | I | I |  |
| t1 | Read A |  | S | I | Read miss A |
| t2 | Write A |  | M | I | Invalidate |
| t3 |  | Read B | M | S | Read miss B |
| t4 |  | Write B | M | M | Invalidate |


## Slide 71: MESI Protocol

### Extracted Shape Text
- MESI Protocol
- MESI Protocol: Illinois protocol (ISCA, 84)
- I(nvalid): block is not in cache, need to fetch from memory or other cache
- S(hared): in >1 caches, clean, local cores directly reads it w/o bus action
- M(odified): in 1 cache, local core can read/write it w/o bus action
- E(xclusive): in 1 cache, clean, local core reads/writes it w/o bus action
- Key Differences from MSI Protocol:
- Local core reads block in state E, the state holds
- Local core writes block in state E  state M, without bus action
- Remote core reads, via read miss on bus, block in state E  state S
- Remote core writes, via write miss on bus, block in state E  state I
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
- 71

## Slide 72: MESI over MSI

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

## Slide 73: Sophisticated Cache Coherence Protocols

### Extracted Shape Text
- Sophisticated Cache Coherence Protocols
- Intel i7: MESIF
- F: forward (read from remote shared instead of memory)
- AMD: MOESI
- O: owned (read from remote shared instead of memory)
- The protocol can be optimized with more states and prediction mechanisms to
- + Reduce unnecessary invalidates and transfers of blocks
- However, more states and optimizations
- -- Are more difficult to design and verify (lead to more cases to take care of, race conditions)
- -- Provide diminishing returns

### Notes
- 这个方向的研究没啥意义
- 。
- 73

## Slide 74: Cache Coherence Protocols

### Extracted Shape Text
- Cache Coherence Protocols
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
- Cache Coherence
- Snoop: [Goodman ISCA 1983]
- Bus-based, each bus action broadcasts on the bus, one action at a time.
- Each to implement
- Single point of serialization for all memory requests.

## Slide 75: Snoop-Based Cache Coherence

### Extracted Shape Text
- Snoop-Based Cache Coherence

## Slide 76: Cache Snoop Protocol

### Extracted Shape Text
- Cache Snoop Protocol
- Core
- Bus (One trans. a time)
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
- Snoop: [Goodman ISCA 1983]
- Single point of serialization for all memory requests
- One outstanding memory request per processor
- System interconnect is an atomic shared bus (one cache communicates at a time)

## Slide 77: Example: How Snoop/Direct Works?

### Extracted Shape Text
- Example: How Snoop/Direct Works?
- C2
- Interconnect
- C1
- C4
- C3
- X:
- X: I
- I
- X: S
- X: S
- …
- Initial states:
- X is only shared by C3 and C4
- Operations:
- C1:X=888
- C3: reads X

## Slide 78: How Snoop Works? (C1: X = 888)

### Extracted Shape Text
- How Snoop Works? (C1: X = 888)
- C1(local) Bus C3(remote) C4(remote) …
- GetEx X
- Invalidate X
- Invalidate X
- Ack
- Reply X=111
- C2
- C1
- C4
- C3
- X:
- X: S
- X: I
- X: S
- M, 888
- I
- X: I
- X: I
- X = 888
- …
- Bus (One transaction active at a time)

### Notes
- Bus also broadcasts to C2…
- 78

## Slide 79: How Bus Works? (C3 reads X)

### Extracted Shape Text
- How Bus Works? (C3 reads X)
- GetS X
- Reply X=888
- C2
- Bus (One transaction active at a time)
- C1
- C4
- C3
- X:
- X: S
- X: I
- M, 888
- S, 888
- X: I
- X: I
- …
- GetS X
- C1(M) Bus C3(local) C4(remote)
- Write X to memory
- GetS X
- Ack

## Slide 80: Why Needing a Bus?

### Extracted Shape Text
- Why Needing a Bus?
- Ordering
- Bus serializes requests, ordering some before others.
- However: coherence does not require ordering of requests to different address.
- Communication
- Simple, fast broadcast medium
- However: coherence does not require broadcast
- Only need to communicate with sharers
- Observation: most data is not shared by every cache.

## Slide 81: Cache Coherence Protocols

### Extracted Shape Text
- Cache Coherence Protocols
- Cache Coherence
- Snoop: [Goodman ISCA 1983]
- Bus-based, each bus action broadcasts on the bus, one action at a time.
- Single point of serialization for all memory requests.
- Directory:[Censier, ToC 1978]
- Cores make explicit requests for blocks
- Directory tracks which caches have each block
- Directory coordinates invalidation and updates
- Single point of serialization per block, distributed among nodes
- Long processing latency
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

## Slide 82: Directory-Based Cache Coherence

### Extracted Shape Text
- Directory-Based Cache Coherence

## Slide 83: Directory Based Coherence: Goal and Idea

### Extracted Shape Text
- Directory Based Coherence: Goal and Idea
- Goal: address the lack of scalability of snooping protocols.
- All-to-all broadcast will not scale
- Idea: A logically-central directory keeps track of where the copies of each cache block reside. Caches consult this directory to ensure coherence.
- Coherence still requires single point of serialization (for write serialization)
- Serialization location can be different for every block (striped across nodes/memory-controllers)

## Slide 84: Cache

### Extracted Shape Text
- Cache
- Directory: Node Definition
- Regarding a cache block:
- Home Node: the node owns the corresponding directory, each cache block can have different home node.
- Local Node: the node initiates the cache read/write requests
- Remote Node: the node passively responses to the action from the home node
- C2
- Switch (peer to peer)
- Cache
- C1
- Cache
- C4
- Cache
- C3
- …

## Slide 85: Directory: Basic Operations

### Extracted Shape Text
- Directory: Basic Operations
- Local node:
- On a bus read: send out getS request to directory node, after receiving the data, set the cache’s bit.
- On a bus write: send out getEx request to directory node
- invalidate all caches that have the block and reset their bits
- Have an “exclusive bit” associated with each block in each cache
- Directory node:
- 1, Receives getS, getEx requests from nodes
- 2, Based on different cache states:
- 2a, Sends Invalidate messages to sharers if needed
- 2b, Forwards request to memory if needed
- 3, Replies to requestor and updates sharing state

### Notes
- Protocol design is flexible
- Exact forwarding paths depend on implementation
- For example, do cache-to-cache transfer?
- 85

## Slide 86: Directory for Each Cache Line

- Images: 0; Tables: 1

### Extracted Shape Text
- Directory for Each Cache Line
- Detailed directory for each cache line:
- Each cache block needs N+log2N + 2 bits for its directory, which resides at the home node.
- 2-bit cache states: a block is owned by the directory unless the block is in a cache in state M. State M means a node writes to it.
- One shared bit for each cache: indicating whether the block is shared in a cache
- log2N owner bit: indicates that the cache that has the only copy of the block and can update it without notifying others

| states | Owner | Sharer list (one-hot bit vector) |
| --- | --- | --- |

- 2-bit log2N-bit N-bit

## Slide 87: How Directory Works?

### Extracted Shape Text
- How Directory Works?
- C2
- Switch (peer to peer)
- C1
- C4
- C3
- X:
- X: S{C3, C4}
- I
- X: S
- X: S
- …
- Initial states:
- Directory stays in C2
- X is only shared by C3 and C4
- Operations:
- C1:X=888
- C3: reads X

## Slide 88: How Directory Works? (C1: X = 888)

### Extracted Shape Text
- How Directory Works? (C1: X = 888)
- C1(local) C2(home) C3(remote) C4(remote)
- GetEx X
- Invalidate X
- Invalidate X
- Ack
- Ack
- Reply X=111
- C2
- Switch (peer to peer)
- C1
- C4
- C3
- X:
- X: S
- X: S{C3, C4}
- X: S
- M, 888
- I
- X: I
- X: I
- X: E{C1}
- X = 888
- …

## Slide 89: How Directory Works? (C3 reads X)

### Extracted Shape Text
- How Directory Works? (C3 reads X)
- GetS X
- Ack
- Reply X=888
- C2
- Switch (peer to peer)
- C1
- C4
- C3
- X:
- X: S
- X: S{C1, C3}
- M, 888
- S, 888
- X: I
- X: I
- X: E{C1}
- …
- Fwd-GetS X to C1
- C1(owned) C2(home) C3(local) C4(remote)
- Write X to memory
