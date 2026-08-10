# 10-cache-coherence-consistency.pptx selected slides

## Slide 11: Memory Consistency vs. Cache Coherence
- Memory Consistency vs. Cache Coherence
- Coherence is about ordering of operations from different processors to the same memory location
- Local ordering of accesses to each cache block
- Consistency is about ordering of all memory operations from different processors (i.e., to different memory locations)
- Global ordering of accesses to all memory locations
Notes:
- Coherence;
- 一致性
- Consistency:
- 连贯性
- 11

## Slide 12: Cache Coherence
- Cache Coherence

## Slide 13: Features of Cache Coherence
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

## Slide 14: Recall: Hardware Arch. for Cache Coherence
- Recall: Hardware Arch. for Cache Coherence
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

## Slide 15: Recall: Cache Coherence: Cache Tags
- Recall: Cache Coherence: Cache Tags
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
Notes:
- Singe Core? Valid bit, tag…
- 15

## Slide 16: Cache Coherence: Cache Tags
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
- Input:
- CPU action of one requested core
- Output:
- Bus action of one requested core
- Changed States:
- Modified cache tag
Notes:
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 16

## Slide 17: Recall: Single Core’s Cache
- Recall: Single Core’s Cache
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
- 17

## Slide 18: State Diagrams for CPU and Bus Requests
- State Diagrams for CPU and Bus Requests
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
- Core’s memory read/write  Cache states, Bus action:
- 1, Miss in local cache
- 2, Hit in local cache
- Bus action  Cache states:
- 1, Invalidate
- 2, Write miss
- 3, Read miss
- I
- S
- M
- Invalidate/Write miss
- Read miss
- Read miss
- Write back block to requesting cache and memory
- Invalidate/ Write miss
- Write back block to requesting cache and memory
- Bus action
- Cache blocks
- Tags
- Cache response
- Cache
- Starter
- CPU action
- Bus action
- Cache blocks
- Tags
- Core
- Starter
Notes:
- CPU request
- 
- Cache states
-  Bus request
- 18

## Slide 19: Recall: The Problem with MSI
- Recall: The Problem with MSI
- A block is not in cache at the beginning. On a read, the block immediately goes to the “Shared” state.
- Problem: Core issues a bus action “invalidate” before writing the block to cache, even when only one cache copy exists.
- TABLE:
  | Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
  | t0 |  |  | I | I |  |
  | t1 | Read A |  | S | I | Read miss A |
  | t2 | Write A |  | M | I | Invalidate |
  | t3 |  | Read B | M | S | Read miss B |
  | t4 |  | Write B | M | M | Invalidate |

## Slide 20: Recall: MESI Protocol
- Recall: MESI Protocol
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
Notes:
- 大三有很多课，假如
- 10
- 门课，你跟你室友都选了人工智能芯片与系统专业课，这样人工智能专业课的信息大家有兴趣去了解（
- update
- 比较好）；但有选修课，不是所有人都选了，这个时候
- 就不好，
- invalidate
- 就比较好。
- 20

## Slide 21: Recall: MESI over MSI
- Recall: MESI over MSI
- TABLE:
  | Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
  | t0 |  |  | I | I |  |
  | t1 | Read A |  | S | I | Read miss A |
  | t2 | Write A |  | M | I | Invalidate |
  | t3 |  | Read B | M | S | Read miss B |
  | t4 |  | Write B | M | M | Invalidate |
- MSI:
- TABLE:
  | Time | P1 op. | P2 op. | State A in P1 | State B in P2 | Bus action |
  | t0 |  |  | I | I |  |
  | t1 | Read A |  | E | I | Read miss A |
  | t2 | Write A |  | M | I |  |
  | t3 |  | Read B | M | E | Read miss B |
  | t4 |  | Write B | M | M |  |
- MESI:

## Slide 22: Cache Coherence Protocols
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

## Slide 23: Snoop-Based Cache Coherence
- Snoop-Based Cache Coherence

## Slide 24: Cache Snoop Protocol
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

## Slide 25: Example: How Snoop/Direct Works?
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

## Slide 26: How Snoop Works? (C1: X = 888)
- How Snoop Works? (C1: X = 888)
- C1(local) Bus C3(remote) C4(remote) …
- GetEx X
- Invalidate X
- Invalidate X
- Ack
- Ack
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
Notes:
- Bus also broadcasts to C2…
- 26

## Slide 27: How Bus Works? (C3 reads X)
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

## Slide 28: Why Needing a Bus?
- Why Needing a Bus?
- Ordering
- Bus serializes requests, ordering some before others.
- However: coherence does not require ordering of requests to different address.
- Communication
- Simple, fast broadcast medium
- However: coherence does not require broadcast
- Only need to communicate with sharers
- Observation: most data is not shared by every cache.

## Slide 29: Cache Coherence Protocols
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

## Slide 30: Directory-Based Cache Coherence
- Directory-Based Cache Coherence

## Slide 31: Directory Based Coherence: Goal and Idea
- Directory Based Coherence: Goal and Idea
- Goal: address the lack of scalability of snooping protocols.
- All-to-all broadcast will not scale
- Idea: A logically-central directory keeps track of where the copies of each cache block reside. Caches consult this directory to ensure coherence.
- Coherence still requires single point of serialization (for write serialization)
- Serialization location can be different for every block (striped across nodes/memory-controllers)

## Slide 32: Cache
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

## Slide 33: Directory: Basic Operations
- Directory: Basic Operations
- Local node:
- On a bus read: send out getS request to home node, after receiving the data, set the cache’s bit.
- On a bus write: send out getEx request to home node
- invalidate all caches that have the block and reset their bits
- Have an “exclusive bit” associated with each block in each cache
- Directory node:
- 1, Receives getS, getEx requests from nodes
- 2, Based on different cache states:
- 2a, Sends Invalidate messages to sharers if “Shared”
- 2b, Forwards request to memory if “Not valid”
- 3, Replies to requestor and updates sharing states
Notes:
- Protocol design is flexible
- Exact forwarding paths depend on implementation
- For example, do cache-to-cache transfer?
- 33

## Slide 34: Directory for Each Cache Line
- Directory for Each Cache Line
- Detailed directory for each cache line:
- Each cache block needs N+log2N + 2 bits for its directory, which resides at the home node.
- 2-bit cache states: a block is owned by the directory unless the block is in a cache in state M. State M means a node writes to it.
- One shared bit for each cache: indicating whether the block is shared in a cache
- log2N owner bit: indicates that the cache that has the only copy of the block and can update it without notifying others
- TABLE:
  | states | Owner | Sharer list (one-hot bit vector) |
- 2-bit log2N-bit N-bit

## Slide 35: How Directory Works?
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

## Slide 36: How Directory Works? (C1: X = 888)
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

## Slide 37: How Directory Works? (C3 reads X)
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

## Slide 38: Memory Consistency vs. Cache Coherence
- Memory Consistency vs. Cache Coherence
- Coherence is about ordering of operations from different processors to the same memory location
- Local ordering of accesses to each cache block
- Write serialization: all cores see the same write ordering
- Consistency is about ordering of all memory operations from different processors (i.e., to different memory locations).
- Global ordering of accesses to all memory locations
Notes:
- Coherence;
- 一致性
- Consistency:
- 连贯性
- 38

## Slide 39: Cache Consistency
- Cache Consistency

## Slide 40: Ordering of Operations
- Ordering of Operations
- Operations: A, B, C, D
- In what order should the hardware execute (and report the results of) these operations?
- Consistency： A contract between programmer and microarchitect.
- Preserving an “expected” (more accurately, “agreed upon”) order simplifies programmer’s life
- Ease of debugging; ease of state recovery, exception handling
- Preserving an “expected” order usually makes the hardware designer’s life difficult
- Especially if the goal is to design a high performance processor: Recall load-store queues in out of order execution and their complexity

## Slide 41: Memory Ordering in a Single Processor
- Memory Ordering in a Single Processor
- Specified by the von Neumann model
- Sequential order
- Hardware executes the load and store operations in the order specified by the sequential program
- Out-of-order execution does not change the semantics
- Hardware retires (reports to software the results of) the load and store operations in the order specified by the sequential program
- Advantages: 1) Architectural state is precise within an execution. 2) Architectural state is consistent across different runs of the program  Easier to debug programs.
- Disadvantage: Preserving order adds overhead, reduces performance, increases complexity, reduces scalability

## Slide 42: Memory Ordering in a MIMD Processor
- Memory Ordering in a MIMD Processor
- Each processor’s memory operations are in sequential order with respect to the “thread” running on that processor (assume each processor obeys the von Neumann model)
- Multiple processors execute memory operations concurrently
- How does the memory see the order of operations from all processors?
- In other words, what is the ordering of operations across different processors?

## Slide 43: Example of Multi-threaded Program
- Example of Multi-threaded Program
- Is it possible for both cores to enter critical section and to print “Hello” and “ZJU” on real hardware?
- A = B = 0 initially.
- Core 1:
- (1) A = 1
- if (B == 0)
- （2） print “Hello”: <critical section>
- Core 2:
- (3) B = 1
- if (A == 0)
- (4) print “ZJU” : <critical section>
Notes:
- 有可能的哈。
- 43

## Slide 44: The Challenge
- The Challenge
- Challenge: The two processors did NOT see the same order of operations to memory
- The “happened before” relationship between multiple updates to memory was inconsistent between the two processors’ points of view
- As a result, each processor thought the other was not in the critical section

## Slide 45: Four Types of Memory Barrier
- Four Types of Memory Barrier
- Load-Load:
- Effectively prevents ordering of loads performed before the barrier with loads performed after the barrier
- Load-Store:
- Effectively prevents ordering of loads performed before the barrier with writes performed after the barrier
- Store-Store:
- Effectively prevents ordering of stores performed before the barrier with stores performed after the barrier
- Store-Load:
- Effectively prevents ordering of stores performed before the barrier with loads performed after the barrier

## Slide 46: Four Memory Barriers vs. Consistence Model
- Four Memory Barriers vs. Consistence Model
- Comparison of memory models:
- The stronger memory model leads to lower performance/higher overhead
- The stronger memory model makes programmers’ life easier
- TABLE:
  | Load-Load | Load-Store | Store-Store | Store-Load | Consistence Model | CPU |
  | √ | √ | √ | √ | Sequential Consistency | Dual 386 |
  | √ | √ | √ |  | Total Store Order | X86/64 |
  | √ | √ |  |  | Partial Store Order | Arm |
  |  |  |  |  | Really weak memory model | DEC Alpha |

## Slide 47: Sequential Consistency
- Sequential Consistency
- Sequential Consistency:
- Load-Load
- Load-Store
- Store-Store
- Store-Load
- Sequential Consistency in a multiprocessor system if:
- In uniprocessor: the operations of each individual processor appear in this sequence in the order specified by its program
- AND
- In multiprocessor: the result of any execution is the same as if the operations of all the processors were executed in some sequential order, as if they were manipulating a single shared memory
- Lamport, “How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs,” IEEE Transactions on Computers, 1979

## Slide 48: Sequential Consistency
- Sequential Consistency
- Sequential Consistency: Memory is a switch that services one load or store at a time from any processor
- All processors see the currently serviced load or store at the same time
- Each processor’s operations are serviced in program order
- MEMORY
- P1
- P3
- P2
- Pn

## Slide 49: Example under Sequential Consistency
- Example under Sequential Consistency
- What is the reasonable execution order?
- (1)  (2)  (3)  (4) “Hello”
- (3)  (4)  (1)  (2) “ZJU”
- (1)  (3)  (2)  (4) or (1)  (3)  (4)  (2)
- (3)  (1)  (2)  (4) or (3)  (1)  (4)  (2)
- Is it possible to print “Hello” and “ZJU” on real hardware?
- A = B = 0 initially.
- Core 1:
- (1) A = 1
- if (B == 0)
- （2） print “Hello”: <critical section>
- Core 2:
- (3) B = 1
- if (A == 0)
- (4) print “ZJU” : <critical section>
Notes:
- 有可能的哈。
- 49

## Slide 50: Problem of Sequential Consistency
- Problem of Sequential Consistency
- Problem of Sequential Consistency: low performance
- Two instructions do not conflict, but the second instruction still needs have to wait for the first one to finish before executing.
- Writing to memory is really slow, e.g., 100 cycles
- MEMORY
- P1
- P3
- P2
- Pn

## Slide 51: Four Memory Barriers vs. Consistence Model
- Four Memory Barriers vs. Consistence Model
- Comparison of memory models:
- The stronger memory model leads to lower performance/higher overhead
- The stronger memory model makes programmers’ life easier
- TABLE:
  | Load-Load | Load-Store | Store-Store | Store-Load | Consistence Model | CPU |
  | √ | √ | √ | √ | Sequential Consistency | Dual 386 |
  | √ | √ | √ |  | Total Store Order | X86/64 |
  | √ | √ |  |  | Partial Store Order | Arm |
  |  |  |  |  | Really weak memory model | DEC Alpha |

## Slide 52: Total Store Order
- Total Store Order
- Total Store Order:
- Load-Load
- Load-Store
- Store-Store
- Total Store Order == SC + Store buffer
- Committing a store instruction means the data is stored in store buffer, rather than cache hierarchy.
- The store instruction writes in a local store buffer and then proceed to next instruction (e.g., load) immediately.
- The cache will pull writes out of the store buffer when ready.
- Store-load order is not preserved.
- C1
- X:
- I

## Slide 53: Store Buffer
- Store Buffer
- Idea of store buffer
- Overlap memory accesses with other accesses and computation.
- Hide long write latency in the core
- Reordering read before store
- C1
- Cache
- store buffer
- Writes
- Reads

## Slide 54: Example under Total Store Order
- Example under Total Store Order
- A = B = 0 initially.
- Core 1:
- (1) A = 1
- if (B == 0)
- （2） print “Hello”: <critical section>
- Core 2:
- (3) B = 1
- if (A == 0)
- (4) print “ZJU” : <critical section>
- What is the reasonable execution order?
- (1)  (2)  (3)  (4) “Hello”
- (3)  (4)  (1)  (2) “ZJU”
- (1)  (3)  (2)  (4) or (1)  (3)  (4)  (2)
- (3)  (1)  (2)  (4) or (3)  (1)  (4)  (2)
- Is it possible to print “Hello” and “ZJU” on real hardware?
- (2)  (4)  (3)  (1) or (2)  (4)  (1)  (3)
Notes:
- 有可能的哈。
- <critical section>
- 54

## Slide 55: Four Memory Barriers vs. Consistence Model
- Four Memory Barriers vs. Consistence Model
- Comparison of memory models:
- The stronger memory model leads to lower performance/higher overhead
- The stronger memory model makes programmers’ life easier
- TABLE:
  | Load-Load | Load-Store | Store-Store | Store-Load | Consistence Model | CPU |
  | √ | √ | √ | √ | Sequential Consistency | Dual 386 |
  | √ | √ | √ |  | Total Store Order | X86/64 |
  | √ | √ |  |  | Partial Store Order | Arm |
  |  |  |  |  | Really weak memory model | DEC Alpha |

## Slide 56: Partial Store Order
- Partial Store Order
- Total Store Order:
- Load-Load
- Load-Store
- Partial Store Order == Total Store Order + Write coalescing
- Write coalescing: merge writes to the same cache line inside the write buffer to save memory bandwidth
- Store-store order is not preserved.

## Slide 57: Intuitive Example of Write Coalescing
- Intuitive Example of Write Coalescing
- Code:
- A[0] = 8
- A[5] = 8
- A[11] = 8
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Write buffer:
- A[0] = 8
- A[5] = 8
- A[11] = 8
- Executed:
- A[0] = 8
- A[5] = 8
- A[11] = 8
- Writing to A[3] and A[5] is re-ordered
- Code:
- A[0] = 8
- A[5] = 8
- A[3] = 8
- TABLE:
  |  |  |  |  |
  |  |  |  |  |
  |  |  |  |  |
- Write buffer:
- A[0] = 8
- A[5] = 8
- A[3] = 8
- Executed:
- A[0] = 8
- A[5] = 8
- A[3] = 8

## Slide 58: Example under Partial Store Order
- Example under Partial Store Order
- What is the reasonable execution order?
- (1)  (2)  (3)  (4) “Hello”
- (3)  (4)  (1)  (2) “ZJU”
- (1)  (3)  (2)  (4) or (1)  (3)  (4)  (2)
- (3)  (1)  (2)  (4) or (3)  (1)  (4)  (2)
- Is it possible to print “Hello” and “ZJU” on real hardware?
- (2)  (4)  (3)  (1) or (2)  (4)  (1)  (3)
- A = B = 0 initially.
- Core 1:
- (1) A = 1
- if (B == 0)
- （2） print “Hello”: <critical section>
- Core 2:
- (3) B = 1
- if (A == 0)
- (4) print “ZJU” : <critical section>
Notes:
- 有可能的哈。
- 58

## Slide 59: Why Cache Consistency Even Matter?
- Why Cache Consistency Even Matter?
- Ease of debugging
- It is nice to have the same execution done at different times to have the same order of execution  Repeatability
- Correctness
- Can we have incorrect execution if the order of memory operations is different from the point of view of different processors?
- Performance and overhead
- Enforcing a strict “sequential ordering” can make life harder for the hardware designer in implementing performance enhancement techniques (e.g., OoO execution, caches)

## Slide 60: When Could Order Affect Correctness?
- When Could Order Affect Correctness?
- When protecting shared data

## Slide 61: Protecting Shared Data
- Protecting Shared Data
- Threads are not allowed to update shared data concurrently
- For correctness purposes
- Accesses to shared data are encapsulated inside critical sections or protected via synchronization constructs (locks, semaphores, condition variables)
- Mutual exclusion principle: Only one thread can execute a critical section at a given time.
- A multiprocessor should provide the correct execution of synchronization primitives to enable the programmer to protect shared data

## Slide 62: Supporting Mutual Exclusion
- Supporting Mutual Exclusion
- Programmer relies on hardware primitives to support correct synchronization
- If hardware primitives are not correct (or unpredictable), programmer’s life is tough
- If hardware primitives are correct but not easy to reason about or use, programmer’s life is still tough
- Programmer needs to make sure mutual exclusion (synchronization) is correctly implemented
- But, correct parallel programming is an important topic
- Coherence is cheaper than OS-level barrier

## Slide 63: Memory Model in the GPU Architecture
- Memory Model in the GPU Architecture
- …
- SM
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- L2 Cache
- Global Memory
- Registers
- Shared Memory
- L1 Cache
- ≈5 cycles
- ≈5 cycles
- ≈500 cycles
- Slide credit: Izzat El Hajj
- SM
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- Registers
- Shared Memory
- L1 Cache
- SM
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- Registers
- Shared Memory
- L1 Cache
- Cache Consistency Issue
- Each SM writes data to its L1 cache, which does not affect shared L2 cache immediately.
- Manually use PTX instructions to write data to L2 or global memory.
Notes:
- HBM3 memory subsystem
- provides nearly a 2x bandwidth increase over the previous generation. The H100 SXM5 GPU is the world’s first GPU with HBM3 memory delivering a class-leading 3 TB/sec of memory bandwidth.
- 50 MB L2 cache architecture
- caches large portions of models and datasets for repeated access, reducing trips to HBM3.
- SM
- ：
- streaming multiprocessor
- 63

## Slide 64: Recall: Cache Hierarchy
- Recall: Cache Hierarchy
- Kim & Mutlu, “Memory Systems,” Computing Handbook, 2014
- https://people.inf.ethz.ch/omutlu/pub/memory-systems-introduction_computing-handbook14.pdf

## Slide 65: Multi-level Caching in a Pipelined Design
- Multi-level Caching in a Pipelined Design
- First-level caches (instruction and data)
- Decisions very much affected by cycle time
- Small, lower associativity; latency is critical
- Tag store and data store usually accessed in parallel
- Second-level caches
- Decisions need to balance hit rate and access latency
- Usually large and highly associative; latency not as important
- Tag store and data store can be accessed serially
- Serial vs. Parallel access of levels
- Serial: Second level cache accessed only if first-level misses
- Second level does not see the same accesses as the first
- First level acts as a filter (filters some temporal and spatial locality)
- Management policies are therefore different

## Slide 66: Deeper and Larger Cache Hierarchies
- Deeper and Larger Cache Hierarchies
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

## Slide 67: Deeper and Larger Cache Hierarchies
- Deeper and Larger Cache Hierarchies
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

## Slide 68: Deeper and Larger Cache Hierarchies
- Deeper and Larger Cache Hierarchies
- https://www.tomshardware.com/news/infrared-photographer-photos-nvidia-ga102-ampere-silicon
- Nvidia Ampere, 2020
- Cores:
- 128 Streaming Multiprocessors
- L1 Cache or Scratchpad:
- 192KB per SM
- Can be used as L1 Cache and/or Scratchpad
- L2 Cache:
- 40 MB shared