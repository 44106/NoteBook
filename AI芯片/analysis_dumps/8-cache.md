# 8-cache.pptx selected slides

## Slide 16: The Memory Hierarchy
- The Memory Hierarchy
Notes:
- 16

## Slide 17: Memory Hierarchy in a Modern System (I)
- Memory Hierarchy in a Modern System (I)
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
- AMD Barcelona, circa 2006

## Slide 18: Memory Hierarchy in a Modern System (II)
- Memory Hierarchy in a Modern System (II)
- https://wccftech.com/amd-ryzen-5000-zen-3-vermeer-undressed-high-res-die-shots-close-ups-pictured-detailed/
- AMD Ryzen 5000, 2020
- Core Count:
- 8 cores/16 threads
- L1 Caches:
- 32 KB per core
- L2 Caches:
- 512 KB per core
- L3 Cache:
- 32 MB shared

## Slide 19: Memory Hierarchy in a Modern System (III)
- Memory Hierarchy in a Modern System (III)
- https://www.it-techblog.de/ibm-power10-prozessor-mehr-speicher-mehr-tempo-mehr-sicherheit/09/2020/
- IBM POWER10,
- 2020
- Cores:
- 15-16 cores,
- 8 threads/core
- L2 Caches:
- 2 MB per core
- L3 Cache:
- 120 MB shared

## Slide 20: Memory Hierarchy in a Modern System (IV)
- Memory Hierarchy in a Modern System (IV)
- https://www.tomshardware.com/news/infrared-photographer-photos-nvidia-ga102-ampere-silicon
- Nvidia Ampere, 2020
- Cores:
- 108 Streaming Multiprocessors
- L1 Cache or Scratchpad:
- 192KB per SM
- Can be used as L1 Cache and/or Scratchpad
- L2 Cache:
- 40 MB shared

## Slide 21: Ideal Memory
- Ideal Memory
- Properties of ideal memory:
- Zero access time (latency)
- Infinite capacity
- Infinite bandwidth (to support multiple accesses in parallel)
- Zero cost

## Slide 22: The Problem of Ideal Memory
- The Problem of Ideal Memory
- Ideal memory’s requirements oppose each other
- Bigger is slower
- Bigger  Takes longer to determine the location
- Faster is more expensive
- Memory technology: SRAM vs. DRAM vs. SSD vs. Disk vs. Tape
- Higher bandwidth is more expensive
- Need more banks, more ports, more channels, higher frequency or faster technology

## Slide 23: The Problem of Ideal Memory
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
- These sample values (circa ~2021) scale with time
- Other technologies have their place as well
- MRAM, RRAM, STT-MRAM, … (not mature yet)
Notes:
- 23

## Slide 24: The Problem (Table View)
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

## Slide 25: Aside: The Problem (2011 Version)
- Aside: The Problem (2011 Version)
- Bigger is slower
- SRAM, 512 Bytes, sub-nanosec
- SRAM, KByte~MByte, ~nanosec
- DRAM, Gigabyte, ~50 nanosec
- Hard Disk, Terabyte, ~10 millisec
- Faster is more expensive (dollars and chip area)
- SRAM, < 10$ per Megabyte
- DRAM, < 1$ per Megabyte
- Hard Disk < 1$ per Gigabyte
- These sample values (circa ~2011) scale with time
- Other technologies have their place as well
- Flash memory (mature), PC-RAM, MRAM, RRAM (not mature yet)

## Slide 26: Why Cache?
- Why Cache?
- Challenge: DRAM latency is ~100ns, slightly decreasing over time.
- Our Goal: CPU wants both fast (~1ns) and large memory (GB) without modifying user code.
Notes:
- 九品芝麻官电影
- 26

## Slide 27: DRAM Capacity, Bandwidth & Latency
- DRAM Capacity, Bandwidth & Latency
- 128x
- 20x
- 1.3x
Notes:
- Latency issue is still there…
- 27

## Slide 28: Why Cache?
- Why Cache?
- Observation: we cannot achieve both with a single level of memory
- Idea:
- Have multiple levels of storage (progressively bigger and slower as the levels are farther from the processor) and
- Ensure most of the data the processor needed is kept in the fast(er) level(s).

## Slide 29: Memory Hierarchy
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

## Slide 30: The Memory Hierarchy
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

## Slide 31: Memory Hierarchy Example
- Memory Hierarchy Example
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014
- https://people.inf.ethz.ch/omutlu/pub/memory-systems-introduction_computing-handbook14.pdf

## Slide 32: Why Cache Works? Locality
- Why Cache Works? Locality
- Locality: One’s recent past is a very good predictor of his/her near future.
- Temporal Locality: If you just did something, it is very likely that you will do the same thing again soon
- since you are here today, there is a good chance you will be here again and again regularly
- Spatial Locality: If you did something, it is very likely you will do something similar/related (in space)
- every time I find you in this room, you are probably sitting close to the same people

## Slide 33: Why Cache Works? Memory Locality
- Why Cache Works? Memory Locality
- A “typical” program has a lot of locality in memory references
- typical programs are composed of “loops”
- Temporal Locality: A program tends to reference the same memory location many times and all within a small window of time
- Spatial Locality: A program tends to reference nearby memory locations within a window of time
- most notable examples:
- 1. instruction memory references  most sequential/streaming
- 2. references to arrays/vectors  often streaming/strided

## Slide 34: Caching Basics: Exploit Temporal Locality
- Caching Basics: Exploit Temporal Locality
- Idea: Store recently accessed data in automatically-managed fast memory (called cache)
- Anticipation: same mem. location will be accessed again soon
- Temporal locality principle
- Recently accessed data will be again accessed in the near future
- This is what Maurice Wilkes had in mind:
- “The use is discussed of a fast core memory of, say 32000 words as a slave to a slower core memory of, say, one million words in such a way that in practical cases the effective access time is nearer that of the fast memory than that of the slow memory.”
- Wilkes, “Slave Memories and Dynamic Storage Allocation,” IEEE Trans. On Electronic Computers, 1965.

## Slide 35: Caching Basics: Exploit Spatial Locality
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

## Slide 36: The Bookshelf Analogy
- The Bookshelf Analogy
- Book in your hand
- Desk
- Bookshelf
- Boxes at home
- Boxes in storage
- Recently-used books tend to stay on desk
- Comp Arch books, books for classes you are currently taking
- Until the desk gets full
- Adjacent books in the shelf needed around the same time
- If I have organized/categorized my books well in the shelf

## Slide 37: Caching in a Pipelined Design
- Caching in a Pipelined Design
- The cache needs to be tightly integrated into the pipeline
- Ideally, access in 1-cycle so that load-dependent operations do not stall
- High frequency pipeline  Cannot make the cache large
- But, we want a large cache AND a pipelined design
- Idea: Cache hierarchy
- CPU
- Main
- Memory
- (DRAM)
- RF
- Level1
- Cache
- Level 2
- Cache

## Slide 38: A Note on Manual vs. Automatic Management
- A Note on Manual vs. Automatic Management
- Manual: Programmer manages data movement across levels
- -- too painful for programmers on substantial programs
- “core” vs “drum” memory in the 1950s
- done in embedded processors (on-chip scratchpad SRAM in lieu of a cache), GPUs (called “shared memory”), ML accelerators, …
- Automatic: Hardware manages data movement across levels, transparently to the programmer
- ++ programmer’s life is easier
- the average programmer doesn’t need to know about caches
- You don’t need to know how big the cache is and how it works to write a “correct” program! (What if you want a “fast” program?)

## Slide 39: Automatic Management in Memory Hierarchy
- Automatic Management in Memory Hierarchy
- Wilkes, “Slave Memories and Dynamic Storage Allocation,” IEEE Trans. On Electronic Computers, 1965.
- “By a slave memory I mean one which automatically accumulates to itself words that come from a slower main memory, and keeps them available for subsequent use without it being necessary for the penalty of main memory access to be incurred again.”

## Slide 40: Cache in 1962 (Bloom, Cohen, Porter)
- Cache in 1962 (Bloom, Cohen, Porter)

## Slide 41: A Modern Memory Hierarchy
- A Modern Memory Hierarchy
- Register File
- 32 words, sub-nsec
- L1 cache
- ~10s of KB, ~nsec
- L2 cache
- 100s of KB ~ few MB, many nsec
- L3 cache,
- many MBs, even more nsec
- Main memory (DRAM),
- Many GBs, ~100 nsec
- Swap Disk
- ~100 GB or few TB, ~10s of usec-msec
- manual/compiler
- register spilling
- automatic
- demand
- paging
- automatic
- HW cache
- management
- Memory
- Abstraction

## Slide 42: Hierarchical Latency Analysis
- Hierarchical Latency Analysis
- For a given memory hierarchy level i it has a technology-intrinsic access time of ti, The perceived access time Ti is longer than ti
- Except for the outer-most hierarchy, when looking for a given address there is
- a chance (hit-rate hri) you “hit” and access time is ti
- a chance (miss-rate mri) you “miss” and access time ti + Ti+1
- hri + mri = 1
- Thus
- Ti = hri·ti + mri·(ti + Ti+1)
- Ti = ti + mri ·Ti+1
- hri and mri are defined to be the hit-rate and miss-rate of just the references that missed at Li-1

## Slide 43: Hierarchy Design Considerations
- Hierarchy Design Considerations
- Recursive latency equation
- Ti = ti + mri ·Ti+1
- The goal: achieve desired Ti within allowed cost
- Ti  ti is desirable, when we
- Keep mri low
- increasing capacity Ci lowers mri, but beware of increasing ti
- lower mri by smarter cache management (replacement::anticipate what you don’t need, prefetching::anticipate what you will need)
- Keep Ti+1 low
- faster lower hierarchies, but beware of increasing cost
- introduce intermediate hierarchies as a compromise

## Slide 44: Memory Bottleneck
- Memory Bottleneck
- “It’s the Memory, Stupid!” (Richard Sites, MPR, 1996)
- Mutlu+, “Runahead Execution: An Alternative to Very Large Instruction Windows for Out-of-Order Processors,” HPCA 2003.

## Slide 45: Comparison of Latency: L1 of Intel CPU
- Comparison of Latency: L1 of Intel CPU
- Addr
- Data
- Memory
- L2
- L1
- L1: 1 cycle
- Really fast

## Slide 46: Comparison of Latency: L2 of Intel CPU
- Comparison of Latency: L2 of Intel CPU
- Addr
- Data
- Memory
- L2
- L1
- L1: 1 cycle
- Really fast
- Memory
- L2
- L1
- Addr
- Data
- Moderate
- L2: 14 cycles

## Slide 47: Comparison of Latency: Memory of Intel CPU
- Comparison of Latency: Memory of Intel CPU
- Addr
- Data
- Memory
- L2
- L1
- L1: 1 cycle
- Really fast
- Memory
- L2
- L1
- Addr
- Data
- Moderate
- L2: 14 cycles
- Addr
- Data
- Memory
- L2
- L1
- Extremely slow
- Memory: 200 cycles

## Slide 48: Cache Basics and Operation
- Cache Basics and Operation
Notes:
- 48
- ISCA: international Symposium of cache architecture

## Slide 49: Cache
- Cache
- Any structure that “memorizes” frequently used results/data
- to avoid repeating the long-latency operations required to reproduce/fetch the results/data from scratch
- e.g., a web cache
- Most commonly in the processor design context: an automatically-managed memory structure
- e.g., memorize in fast SRAM the most frequently or recently accessed DRAM memory locations to avoid repeatedly paying for the DRAM access latency

## Slide 50: Blocks
- Blocks
- Main memory logically divided into fixed-size chunks (blocks)
- Cache can house only a limited number of blocks
- Each block address maps to a potential location in the cache, determined by the index bits in the address
- used to index into the tag and data stores
- 8-bit address
- tag
- index
- byte in block
- 3 bits
- 3 bits
- 2b

## Slide 51: Conceptual Picture of a Cache
- Conceptual Picture of a Cache
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014
- https://people.inf.ethz.ch/omutlu/pub/memory-systems-introduction_computing-handbook14.pdf

## Slide 52: Cache Abstraction and Metrics
- Cache Abstraction and Metrics
- Cache hit rate = (# hits) / (# hits + # misses) = (# hits) / (# accesses)
- Average memory access time (AMAT)
- = ( hit-rate * hit-latency ) + ( miss-rate * miss-latency )
- Important Aside: Is reducing AMAT always beneficial for performance?
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
Notes:
- Reducing AMAT is not always beneficial for performance. The direct metric is instruction throughput, which might be orthogonal to latency.
- 52

## Slide 53: Addressing the Cache
- Addressing the Cache
- Cache access:
- 1) index into the tag and data stores with index bits in address;
- 2) checks valid bit in tag store;
- 3) compares tag bits in address with the stored tag in tag store;
- 4) If a block is in the cache (cache hit), the stored tag should be valid and match the tag of the block, and read out data.
Notes:
- 53

## Slide 54: A Toy Example for Cache
- A Toy Example for Cache
- Toy example:
- 256-byte memory,
-  8-bit address
- 64-byte cache, 8-byte blocks
-  least significant 3 bits within a line
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014

## Slide 55: Caching Basics
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

## Slide 56: Cache: Placement
- Cache: Placement
- A key question: How to map chunks of the main memory address space to blocks in the cache?
- Which location in cache can a given “main memory chunk” be placed in?

## Slide 57: Three Cache Organization Methods
- Three Cache Organization Methods
- Direct-mapped:
- A chunk can go to only one cache block in the cache. (Another extreme)
- Fully-associative:
- A chunk can go to any cache block in the cache. (One extreme)
- Set-associative:
- A chunk can go to N cache blocks in the N-way set-associative cache. (Best choice)
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014

## Slide 58: Direct-Mapped Cache: Placement and Access
- Direct-Mapped Cache: Placement and Access
- Direct-mapped (A block can go to only one location)
- Assume memory: 256 bytes, 8-byte blocks  32 blocks
- Assume cache: 64 bytes, 8 blocks
- Blocks with same index contend for the same cache location
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

## Slide 59: Advantage and Issue of Direct-Mapped Caches
- Advantage and Issue of Direct-Mapped Caches
- Direct-mapped cache:
- Two blocks in memory that map to the same index in the cache cannot be present in the cache at the same time.
- One index  one entry
- Main advantage of direct-mapped cache:
- Easy to implement
- Main issue of direct-mapped cache:
- Can lead to 0% hit rate if more than one block accessed in an interleaved manner map to the same index
- Assume addresses A and B have the same index bits but different tag bits
- A, B, A, B, A, B, A, B, …  conflict in the cache index
- All accesses are conflict misses

## Slide 60: Three Cache Organization Methods
- Three Cache Organization Methods
- Direct-mapped:
- A chunk can go to only one cache block in the cache. (Another extreme)
- Fully-associative:
- A chunk can go to any cache block in the cache. (One extreme)
- Set-associative:
- A chunk can go to N cache blocks in the N-way set-associative cache. (Best choice)
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014

## Slide 61: Full Associativity
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

## Slide 62: Advantage and Issue of Fully-associative Caches
- Advantage and Issue of Fully-associative Caches
- Fully-associative cache:
- A block can be placed in any cache block.
- Main advantage of fully-associative cache:
- Highly utilization of cache blocks (global view)
- Main issue of fully-associative cache:
- Can lead to extremely difficult to implement when the number of cache blocks in the cache is large.
- Number of cache blocks in modern CPU reaches 32M/64=512K.
- Choosing one out of 512K cache lines is extremely costly.

## Slide 63: Three Cache Organization Methods
- Three Cache Organization Methods
- Direct-mapped:
- A chunk can go to only one cache block in the cache. (Another extreme)
- Fully-associative:
- A chunk can go to any cache block in the cache. (One extreme)
- Set-associative:
- A chunk can go to N cache blocks in the N-way set-associative cache. (Best choice)
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014
Notes:
- 相连
- 63

## Slide 64: Set-Associative Cache
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

## Slide 65: 4-way Set Associativity
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
- set
- bytes
- 3 bits
- 1 b
- 4 bits
- V
- tag
- V
- tag
- V
- tag
- V
- tag

## Slide 66: Set-Associative Cache
- Set-Associative Cache
- Key Idea: Associative memory within the set
- Advantage of Set-Associative Cache
- Accommodates conflicts better (fewer conflict misses)
- Assume addresses A and B have the same index bits but different tag bits
- A, B, A, B, A, B, A, B, …  store in the cache set
- All accesses are cache hit
- Issue of Set-Associative Cache
- More complex, slower access, larger tag store
- How about in Deep Learning application？
- Set-Associative Cache: Advantage and Issue

## Slide 67: Associativity (and Tradeoffs)
- Associativity (and Tradeoffs)
- Degree of associativity:
- How many blocks can map to the same index (or set)?
- Higher associativity
- ++ Higher hit rate
- -- Slower cache access time (hit latency and data access latency)
- -- More expensive hardware (more comparators)
- Diminishing returns from higher
- associativity
- associativity
- hit rate

## Slide 68: HBM GB/s
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
- 68