# 7-gpus-optimization.pptx selected slides

## Slide 13: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 13

## Slide 14: GPU Memories
- GPU Memories
Notes:
- 14

## Slide 15: Memory in the GPU Architecture
- Memory in the GPU Architecture
- …
- SM
- Core
- Control
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- SM
- Core
- Control
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- SM
- Core
- Control
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
- Constant Cache
- Registers
- Shared Memory
- L1 Cache
- Constant Cache
- Registers
- Shared Memory
- L1 Cache
- Constant Cache
- ≈1 cycle
- ≈5 cycles
- ≈5 cycles
- ≈500 cycles
- Slide credit: Izzat El Hajj
Notes:
- 15

## Slide 16: Memory in the GPU Architecture
- Memory in the GPU Architecture
- …
- SM
- Core
- Control
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- SM
- Core
- Control
- Core
- Core
- Core
- Core
- Core
- Core
- Core
- SM
- Core
- Control
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
- Constant Cache
- Registers
- Shared Memory
- L1 Cache
- Constant Cache
- Registers
- Shared Memory
- L1 Cache
- Constant Cache
- ≈1 cycle
- ≈5 cycles
- ≈5 cycles
- ≈500 cycles
- Slide credit: Izzat El Hajj
- 50 MB
- 80 GB
- Direct copy
- 3 TB/s
Notes:
- HBM3 memory subsystem
- provides nearly a 2x bandwidth increase over the previous generation. The H100 SXM5 GPU is the world’s first GPU with HBM3 memory delivering a class-leading 3 TB/sec of memory bandwidth.
- 50 MB L2 cache architecture
- caches large portions of models and datasets for repeated access, reducing trips to HBM3.
- SM
- ：
- streaming multiprocessor
- 16

## Slide 17: Example of data movement between GPU global memory (DRAM) and GPU cores.
- Example of data movement between GPU global memory (DRAM) and GPU cores.
- NVIDIA V100 & A100 Memory Hierarchy
- A100 feature:
- Direct copy from L2 to scratchpad, bypassing L1 and register file.
- https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf
Notes:
- A100: New load instruction that copies from global memory (DRAM) to shared memory (scratchpad) directly, without having to use registers (i.e., no need to copy from global memory to register and then from register to shared memory).
- 17

## Slide 18: CUDA Variable Type Qualifiers
- CUDA Variable Type Qualifiers
- __device__ is optional when used with __shared__, or __constant__
- Recall cudaMalloc(…) allocates memory from the host
- Constant memory can also be allocated and initialized from the host
- Automatic variables without any qualifier reside in a register
- Except arrays that reside in global memory
- TABLE:
  | Variable declaration | Memory | Scope | Lifetime |
  | int LocalVar; | register | thread | thread |
  | int localArr[N]; | global | thread | thread |
  | __device__ __shared__ int SharedVar; | shared | block | block |
  | __device__ int GlobalVar; | global | grid | application |
  | __device__ __constant__ int ConstantVar; | constant | grid | application |

## Slide 19: Memory Hierarchy in CUDA Programs
- Memory Hierarchy in CUDA Programs

## Slide 20: Recall: Comparison of Memories
- Recall: Comparison of Memories
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

## Slide 21: The DRAM SubsystemThe Top-Down View
- The DRAM SubsystemThe Top-Down View
Notes:
- 21

## Slide 22: DRAM Subsystem Organization
- DRAM Subsystem Organization
- Channel
- DIMM
- Rank
- Chip
- Bank
- Row/Column

## Slide 23: The DRAM Subsystem
- The DRAM Subsystem
- Memory channel
- Memory channel
- DIMM (Dual in-line memory module)
- Processor
- “Channel”

## Slide 24: Breaking down a DIMM (module)
- Breaking down a DIMM (module)
- DIMM (Dual in-line memory module)
- Side view
- Front of DIMM
- Back of DIMM
- Rank 0: collection of 8 chips
- Rank 1

## Slide 25: Breaking down a Rank
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

## Slide 26: Breaking down a Chip
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

## Slide 27: Inside a DRAM Chip
- Inside a DRAM Chip
- Access
- Transistor
- Storage
- Capacitor
- Bitline
- Wordline
- Wordline
- Bitline
- Subarray
- (2D Array of DRAM Cells)
- Sense Amplifiers
- DRAM Module
- DRAM Chips
- DRAM Bank
- DRAM Cells
- 8
- Row Buffer
Notes:
- 27

## Slide 28: DRAM Bank Operation
- DRAM Bank Operation
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

## Slide 29: Long Global Memory Access Latency
- Long Global Memory Access Latency
Notes:
- 29

## Slide 30: Motivation of In-network Computing
- Motivation of In-network Computing
- How to optimize global memory access?
- Multithreading
- Shared Memory
- Memory Coalescing

## Slide 31: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 31

## Slide 32: Latency Hiding via Warp-Level FGMT
- Latency Hiding via Warp-Level FGMT
- Warp: A set of threads that execute the same instruction (on different data elements)
- Fine-grained multithreading
- One instruction per thread in pipeline at a time (No interlocking)
- Interleaving warp execution to hide latencies
- Register values of all threads stay in register file
- FGMT enables long latency tolerance
- Millions of pixels
- Decode
- R
- F
- R
- F
- R
- F
- A
- L
- U
- A
- L
- U
- A
- L
- U
- D-Cache
- Thread Warp 6
- Thread Warp 1
- Thread Warp 2
- Data
- All Hit?
- Miss?
- Warps accessing
- memory hierarchy
- Thread Warp 3
- Thread Warp 8
- Writeback
- Warps available
- for scheduling
- Thread Warp 7
- I-Fetch
- SIMD Pipeline
- Slide credit: Tor Aamodt
Notes:
- With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread
- ’
- s warp from the pool of
- “
- ready
- ”
- warps and thereby allows other threads to proceed while the memory system processes its request.
- With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.
- 32

## Slide 33: Latency Hiding and Occupancy
- Latency Hiding and Occupancy
- FGMT can hide long latency operations (e.g., memory accesses)
- Occupancy: ratio of active warps to the maximum number of warps per GPU core
- 4 active warps
- 2 active warps

## Slide 34: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 34

## Slide 35: Memory Coalescing (I)
- Memory Coalescing (I)
- Memory Coalescing：
- When threads in the same warp access consecutive memory locations in the same burst, the accesses can be combined and served by one burst
- Only one DRAM transaction is needed.
- Memory Divergence：
- If threads in the same warp access locations not in the same burst, accesses cannot be combined
- Multiple memory transactions are needed
- Takes longer to service data to the warp
- Slide credit: Izzat El Hajj

## Slide 36: Memory Coalescing:
- Memory Coalescing:
- When accessing global memory, memory coalescing makes sure that concurrent threads access nearby memory locations
- Peak bandwidth utilization occurs when all threads in a warp access one cache line (or several consecutive cache lines)
- Md
- Nd
- W
- I
- D
- T
- H
- WIDTH
- Thread 1
- Thread 2
- Not coalesced
- Coalesced
- Memory Coalescing (II)
- Slide credit: Hwu & Kirk

## Slide 37: Uncoalesced Memory Accesses
- Uncoalesced Memory Accesses
- M2,0
- M1,1
- M1,0
- M0,0
- M0,1
- M3,0
- M2,1
- M3,1
- M2,0
- M1,0
- M0,0
- M3,0
- M1,1
- M0,1
- M2,1
- M3,1
- M1,2
- M0,2
- M2,2
- M3,2
- M1,2
- M0,2
- M2,2
- M3,2
- M1,3
- M0,3
- M2,3
- M3,3
- M1,3
- M0,3
- M2,3
- M3,3
- M
- T1
- T2
- T3
- T4
- Warp 1
- T1
- T2
- T3
- T4
- Warp 2
- Access direction of each thread
- …
- Slide credit: Hwu & Kirk

## Slide 38: Coalesced Memory Accesses
- Coalesced Memory Accesses
- M2,0
- M1,1
- M1,0
- M0,0
- M0,1
- M3,0
- M2,1
- M3,1
- M2,0
- M1,0
- M0,0
- M3,0
- M1,1
- M0,1
- M2,1
- M3,1
- M1,2
- M0,2
- M2,2
- M3,2
- M1,2
- M0,2
- M2,2
- M3,2
- M1,3
- M0,3
- M2,3
- M3,3
- M1,3
- M0,3
- M2,3
- M3,3
- M
- T1
- T2
- T3
- T4
- Warp 1
- T1
- T2
- T3
- T4
- Warp 2
- …
- Slide credit: Hwu & Kirk
- Access direction of each thread

## Slide 39: Same instruction in different threads uses thread id to index and access different data elements
- Same instruction in different threads uses thread id to index and access different data elements
- SIMT Memory Access
- Let’s assume N=16, 4 threads per warp  4 warps
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- +
- +
- +
- +
- +
- Slide credit: Hyesoon Kim
- Threads
- Data elements
- Warp 0
- Warp 1
- Warp 2
- Warp 3

## Slide 40: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 40

## Slide 41: Shared Memory
- Shared Memory
- Shared memory is an interleaved (banked) memory
- Each bank can service one address per cycle
- Typically, 32 banks in NVIDIA GPUs
- Successive 32-bit words are assigned to successive banks
- Bank = Address % 32
- Bank conflicts are only possible within a warp
- No bank conflicts between different warps

## Slide 42: Shared Memory Bank Conflicts (I)
- Shared Memory Bank Conflicts (I)
- Bank conflict free
- Bank 15
- Bank 7
- Bank 6
- Bank 5
- Bank 4
- Bank 3
- Bank 2
- Bank 1
- Bank 0
- Thread 15
- Thread 7
- Thread 6
- Thread 5
- Thread 4
- Thread 3
- Thread 2
- Thread 1
- Thread 0
- Bank 15
- Bank 7
- Bank 6
- Bank 5
- Bank 4
- Bank 3
- Bank 2
- Bank 1
- Bank 0
- Thread 15
- Thread 7
- Thread 6
- Thread 5
- Thread 4
- Thread 3
- Thread 2
- Thread 1
- Thread 0
- Linear addressing: stride = 1
- Random addressing 1:1
- Slide credit: Hwu & Kirk

## Slide 43: Shared Memory Bank Conflicts (II)
- Shared Memory Bank Conflicts (II)
- N-way bank conflicts
- 2-way bank conflict: stride = 2
- 8-way bank conflict: stride = 8
- Thread 11
- Thread 10
- Thread 9
- Thread 8
- Thread 4
- Thread 3
- Thread 2
- Thread 1
- Thread 0
- Bank 15
- Bank 7
- Bank 6
- Bank 5
- Bank 4
- Bank 3
- Bank 2
- Bank 1
- Bank 0
- Thread 15
- Thread 7
- Thread 6
- Thread 5
- Thread 4
- Thread 3
- Thread 2
- Thread 1
- Thread 0
- Bank 9
- Bank 8
- Bank 15
- Bank 7
- Bank 2
- Bank 1
- Bank 0
- x8
- x8
- Slide credit: Hwu & Kirk

## Slide 44: Use Shared Memory to Improve Coalescing
- Use Shared Memory to Improve Coalescing
- Md
- Nd
- W
- I
- D
- T
- H
- WIDTH
- Md
- Nd
- Original
- Access
- Pattern
- Tiled
- Access
- Pattern
- Copy into
- scratchpad
- memory
- Perform
- multiplication
- with scratchpad
- values
- Slide credit: Hwu & Kirk

## Slide 45: Reducing Shared Memory Bank Conflicts
- Reducing Shared Memory Bank Conflicts
- Bank conflicts are only possible within a warp
- No bank conflicts between different warps
- If strided accesses are needed, some optimization techniques can help
- Padding
- Randomized mapping
- Rau, “Pseudo-randomly interleaved memory,” ISCA 1991
- Hash functions
- V.d.Braak+, “Configurable XOR Hash Functions for Banked Scratchpad Memories in GPUs,” IEEE TC, 2016

## Slide 46: No Data Reuse
- No Data Reuse
- No Data reuse:
- Each thread reads its only elements.
- for (int i = 0; i < 3; i++){
- for (int j = 0; j < 3; j++){
- sum += gauss[i][j] * Image[(i+row-1)*width + (j+col-1)];
- }
- }
- Loading Amount:
- 9 elements per thread
Notes:
- 对每一个
- row
- ，
- col,
- 计算一个
- sum
- 。
- 46

## Slide 47: Data Reuse: Tiling
- Data Reuse: Tiling
- For data reuse, we divide the input into tiles, each of which loads L_SIZE chunks together into shared memory, then compute together
- __shared__ int l_data[(L_SIZE+2)*(L_SIZE+2)];
- …
- Load tile into shared memory l_data
- __syncthreads();
- for (int i = 0; i < 3; i++){
- for (int j = 0; j < 3; j++){
- sum += gauss[i][j] * l_data[(i+l_row-1)*(L_SIZE+2)+j+l_col-1];
- }
- }
- Loading Amount:
- (L_SIZE+2)2/L_SIZE2
- elements per thread
- Compute Amount:
- The same
Notes:
- L_SIZE: number of points together…
- 47

## Slide 48: void __syncthreads();
- void __syncthreads();
- Synchronizes all threads in a block
- Once all threads in a block have reached this point, execution resumes normally
- Used to avoid RAW / WAR / WAW hazards when accessing shared or global memory
- Synchronization Function
Notes:
- 48

## Slide 49: Tiling/Blocking in On-chip Memories
- Tiling/Blocking in On-chip Memories
- Tiling or Blocking
- Divide loops operating on arrays into computation chunks so that each chunk can hold its data in the on-chip RAM (or other on-chip memory, e.g., scratchpad)
- Avoids on-chip RAM conflicts between different chunks of computation
- Essentially: Divide the working set so that each piece fits in the on-chip RAMs

## Slide 50: CPU: Naïve Matrix Multiplication (I)
- CPU: Naïve Matrix Multiplication (I)
- Matrix multiplication: C = A x B
- Consider two input matrices A and B in row-major layout
- A size is M x P
- B size is P x N
- C size is M x N
- A
- B
- C
- P
- M
- P
- N
- i
- j
- k
- k

## Slide 51: CPU: Naïve Matrix Multiplication (II)
- CPU: Naïve Matrix Multiplication (II)
- Naïve implementation of matrix multiplication
- Poor access locality
- #define A(i,j) matrix_A[i * P + j]
- #define B(i,j) matrix_B[i * N + j]
- #define C(i,j) matrix_C[i * N + j]
- for (i = 0; i < M; i++){ // i = row index
- for (j = 0; j < N; j++){ // j = column index
- C(i, j) = 0; // Set to zero
- for (k = 0; k < P; k++) // Row x Col
- C(i, j) += A(i, k) * B(k, j);
- }
- }
- A
- B
- C
- P
- M
- P
- N
- i
- j
- k
- k
- Consecutive accesses to B are far from each other, in different memory lines.
- Every access to B is likely to cause a row buffer miss

## Slide 52: CPU: Tiled Matrix Multiplication (I)
- CPU: Tiled Matrix Multiplication (I)
- Tiled Matrix Multiplication:
- Achieve better on-chip RAM locality by computing on smaller tiles or blocks that fit in the RAMs
- A
- B
- C
- P
- M
- P
- N
- k
- k
- tile_dim
- tile_dim
- i
- j
- Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
- Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
- Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4
Notes:
- 52

## Slide 53: CPU: Tiled Matrix Multiplication (II)
- CPU: Tiled Matrix Multiplication (II)
- Tiled implementation operates on submatrices (tiles or blocks) that fit fast RAMs (cache, scratchpad, RF)
- #define A(i,j) matrix_A[i * P + j]
- #define B(i,j) matrix_B[i * N + j]
- #define C(i,j) matrix_C[i * N + j]
- for (I = 0; I < M; I += tile_dim){
- for (J = 0; J < N; J += tile_dim){
- Set_to_zero(&C(I, J)); // Set to zero
- for (K = 0; K < P; K += tile_dim)
- Multiply_tiles(&C(I, J), &A(I, K), &B(K, J));
- }
- }
- Multiply small submatrices (tiles or blocks) of size tile_dim x tile_dim
- A
- B
- C
- P
- M
- P
- N
- k
- k
- tile_dim
- tile_dim
- i
- j
- Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
- Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
- Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4

## Slide 54: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Matrix-Matrix Multiplication (I)
- C = A x B
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- Slide credit: Izzat El Hajj

## Slide 55: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Matrix-Matrix Multiplication (II)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- Parallelization approach: assign one thread to each element in the output matrix (C)
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- Slide credit: Izzat El Hajj
- C = A x B

## Slide 56: GPU: Matrix-Matrix Multiplication (III)
- GPU: Matrix-Matrix Multiplication (III)
- __global__ void mm_kernel(float* A, float* B, float* C, unsigned int N) {
- unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
- unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
- float sum = 0.0f;
- for(unsigned int i = 0; i < N; ++i) {
- sum += A[row*N + i]*B[i*N + col];
- }
- C[row*N + col] = sum;
- }
- Slide credit: Izzat El Hajj

## Slide 57: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Reuse in Matrix-Matrix Multiplication (I)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- Some of the threads in the same thread block use the same input data
- Slide credit: Izzat El Hajj
- C = A x B

## Slide 58: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Reuse in Matrix-Matrix Multiplication (II)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- Some of the threads in the same thread block use the same input data
- Slide credit: Izzat El Hajj
- C = A x B

## Slide 59: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Tiled Matrix-Matrix Multiplication (I)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- Step 1: Load the first tile of each input matrix to shared memory (each thread loads one element)
- Slide credit: Izzat El Hajj
- Ctile = Atile1 x Btile1

## Slide 60: GPU: Tiled Matrix-Matrix Multiplication (II)
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Tiled Matrix-Matrix Multiplication (II)
- Ctile += Atile2 x Btile2
- Atile2
- Btile2
- Ctile
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- Step 2: Each thread computes its partial sum from the tiles in shared memory (threads wait for each other to finish)
- Slide credit: Izzat El Hajj

## Slide 61: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Tiled Matrix-Matrix Multiplication (III)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- …accumulate the second tile
- Slide credit: Izzat El Hajj
- Ctile += Atile2 x Btile2

## Slide 62: N
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- GPU: Tiled Matrix-Matrix Multiplication (IV)
- A
- B
- C
- N
- N
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- TABLE:
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |
- N
- N
- …and accumulate the third tile
- Slide credit: Izzat El Hajj
- Ctile += Atile3 x Btile3

## Slide 63: GPU: Tiled Matrix-Matrix Multiplication (V)
- GPU: Tiled Matrix-Matrix Multiplication (V)
- __shared__ float A_s[TILE_DIM][TILE_DIM];
- __shared__ float B_s[TILE_DIM][TILE_DIM];
- unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
- unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
- float sum = 0.0f;
- for(unsigned int tile = 0; tile < N/TILE_DIM; ++tile) {
- // Load tile to shared memory
- A_s[threadIdx.y][threadIdx.x] = A[row*N + tile*TILE_DIM + threadIdx.x];
- B_s[threadIdx.y][threadIdx.x] = B[(tile*TILE_DIM + threadIdx.y)*N + col];
- __syncthreads();
- // Compute with tile
- for(unsigned int i = 0; i < TILE_DIM; ++i) {
- sum += A_s[threadIdx.y][i]*B_s[i][threadIdx.x];
- }
- __syncthreads();
- }
- C[row*N + col] = sum;
- Declare arrays in shared memory
- Threads wait for each other to finish loading before computing
- Threads wait for each other to finish computing before loading
- Slide credit: Izzat El Hajj

## Slide 64: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 64

## Slide 65: Threads Can Take Different Paths in Warp-based SIMT
- Threads Can Take Different Paths in Warp-based SIMT
- Each thread can have conditional control flow instructions
- Threads can execute different control flow paths
- Thread Warp
- Common PC
- Thread
- 2
- Thread
- 3
- Thread
- 4
- Thread
- 1
- B
- C
- D
- E
- F
- A
- G
- Slide credit: Tor Aamodt

## Slide 66: Control Flow Problem in GPUs/SIMT
- Control Flow Problem in GPUs/SIMT
- A GPU uses a SIMT pipeline to save area on control logic
- Groups scalar threads into warps
- Branch divergence occurs when threads inside warps branch to different execution paths
- Branch
- Path A
- Path B
- Branch
- Path A
- Path B
- Slide credit: Tor Aamodt
Notes:
- 66

## Slide 67: SIMT Utilization
- SIMT Utilization
- Intra-warp divergence
- Compute(threadIdx.x);
- if (threadIdx.x % 2 == 0){
- Do_this(threadIdx.x);
- }
- else{
- Do_that(threadIdx.x);
- }

## Slide 68: Increasing SIMT Utilization
- Increasing SIMT Utilization
- Divergence-free execution
- Compute(threadIdx.x);
- if (threadIdx.x < 32){
- Do_this(threadIdx.x * 2);
- }
- else{
- Do_that((threadIdx.x%32)*2+1);
- }

## Slide 69: Vector Reduction: Naïve Mapping (I)
- Vector Reduction: Naïve Mapping (I)
- 0
- 1
- 2
- 3
- 4
- 5
- 7
- 6
- 10
- 9
- 8
- 11
- 0+1
- 2+3
- 4+5
- 6+7
- 10+11
- 8+9
- 0...3
- 4..7
- 8..11
- 0..7
- 8..15
- 1
- 2
- 3
- iterations
- Thread 0
- Thread 8
- Thread 2
- Thread 4
- Thread 6
- Thread 10
- Slide credit: Hwu & Kirk
- …

## Slide 70: Vector Reduction: Naïve Mapping (II)
- Vector Reduction: Naïve Mapping (II)
- Program with low SIMD utilization
- __shared__ float partialSum[]
- unsigned int t = threadIdx.x;
- for (int stride = 1; stride < blockDim.x; stride *= 2) {
- __syncthreads();
- if (t % (2*stride) == 0)
- partialSum[t] += partialSum[t + stride];
- }

## Slide 71: Divergence-Free Mapping (I)
- Divergence-Free Mapping (I)
- All active threads belong to the same warp
- Thread 0
- 0
- 1
- 2
- 3
- …
- 13
- 15
- 14
- 18
- 17
- 16
- 19
- 0+16
- 15+31
- 1
- 2
- 3
- Thread 1
- Thread 2
- Thread 14
- Thread 15
- iterations
- Slide credit: Hwu & Kirk
- …

## Slide 72: Divergence-Free Mapping (II)
- Divergence-Free Mapping (II)
- Program with high SIMD utilization
- __shared__ float partialSum[]
- unsigned int t = threadIdx.x;
- for (int stride = blockDim.x; stride > 0; stride >> 1){
- __syncthreads();
- if (t < stride)
- partialSum[t] += partialSum[t + stride];
- }

## Slide 73: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 73

## Slide 74: Atomic Operations
- Atomic Operations
Notes:
- 74

## Slide 75: Atomic Operations (I)
- Atomic Operations (I)
- CUDA provides atomic instructions on shared memory and global memory
- They perform read-modify-write operations atomically
- Arithmetic functions
- Add, sub, max, min, exch, inc, dec, CAS
- int atomicAdd(int*, int);
- Bitwise functions
- And, or, xor
- Datatypes: int, uint, ull, float (half, single, double)*
- Pointer to shared memory or global memory
- Value to add
- Return value (old value)
- * Datatypes for different atomic operations in https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#atomic-functions
Notes:
- 75

## Slide 76: Atomic operations serialize the execution if there are atomic conflicts
- Atomic operations serialize the execution if there are atomic conflicts
- Atomic Operations (II)
- tbase
- tconflict
- Shared memory
- Shared memory
- tbase
- No atomic conflict = concurrent updates
- Atomic conflict = serialized updates

## Slide 77: Uses of Atomic Operations
- Uses of Atomic Operations
- Use atomic operations to prevent data races when more than one thread need to update the same memory location
- Computation
- Atomics on an array that will be the output of the kernel
- Example
- Histogram, reduction
- Synchronization
- Atomics on memory locations that are used for synchronization or coordination
- Example
- Counters, locks, flags…
Notes:
- 77

## Slide 78: Histograms are widely used in image processing
- Histograms are widely used in image processing
- Some computation before voting in the histogram may be needed
- Parallel threads frequently incur atomic conflicts in image histogram computation
- For (each pixel i in image I){
- Pixel = I[i] // Read pixel
- Pixel’ = Computation(Pixel) // Optional computation
- Histogram[Pixel’]++ // Vote in histogram bin
- }
- Image Histogram

## Slide 79: Agenda for Today
- Agenda for Today
- SIMT (Hardware) & Warp (Software)
- Optimization of Memory System
- Multi-threading
- Memory Coalescing
- Shared Memory
- SIMT Efficiency
- Divergency
- Atomic
- CPU-GPU Transfer
Notes:
- 79

## Slide 80: Asynchronous Data Transfers between CPU and GPU
- Asynchronous Data Transfers between CPU and GPU
Notes:
- 80

## Slide 81: CUDA Streams
- CUDA Streams
- CUDA streams (command queues in OpenCL)
- Sequence of operations that are performed in order
- 1. Data transfer CPU-GPU
- 2. Kernel execution
- D input data instances, B blocks
- #Streams: (D / #Streams) data instances, (B / #Streams) blocks
- 3. Data transfer GPU-CPU
Notes:
- Computation is divided
- such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
- CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.
- 81

## Slide 82: Asynchronous Transfers between CPU & GPU
- Asynchronous Transfers between CPU & GPU
- Computation divided into #Streams
- D input data instances, B blocks
- #Streams
- D/#Streams data instances
- B/#Streams blocks
- Estimates
- tE >= tT (dominant kernel)
- tT > tE (dominant transfers)
- Default stream
- Several streams
Notes:
- Computation is divided
- such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
- CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.
- 82

## Slide 83: Overlap of Data Transfers and Kernel Execution
- Overlap of Data Transfers and Kernel Execution
- // Create streams
- int number_of_streams = 32;
- cudaStream_t stream[number_of_streams]; // Stream declaration
- for(int i = 0; i < number_of_streams; ++i)
- cudaStreamCreate(&stream[i]); // Stream creation
- // CPU-GPU data transfers
- for (int i = 0; i < number_of_streams; ++i)
- cudaMemcpyAsync(inputDevPtr + i * size, hostPtr + i * size, size,
- cudaMemcpyHostToDevice, stream[i]);
- // Kernel launches
- for (int i = 0; i < number_of_streams; ++i)
- MyKernel<<<num_blocks / number_of_streams, num_threads, 0, stream[i]>>>
- (outputDevPtr + i * size, inputDevPtr + i * size, size);
- // GPU-CPU data transfers
- for (int i = 0; i < number_of_streams; ++i)
- cudaMemcpyAsync(hostPtr + i * size, outputDevPtr + i * size, size,
- cudaMemcpyDeviceToHost, stream[i]);
- cudaDeviceSynchronize(); // Explicit synchronization
- // Destroy streams
- for (int i = 0; i < number_of_streams; ++i)
- cudaStreamDestroy(stream[i]); // Stream destruction
- Code for devices that do not support concurrent data transfers
- Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
- JPDC, 2012
- Check CUDA programming guide
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#streams
Notes:
- 83

## Slide 84: Applications with independent computation on different data instances can benefit from asynchronous transfers
- Applications with independent computation on different data instances can benefit from asynchronous transfers
- For instance, video processing
- Use Case: Video Processing
- Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
- JPDC, 2012
Notes:
- A
- number
- b
- of blocks per frame executes.
- Data transfers are overlapped with computation. Thus, some time can be saved.
- 84

## Slide 85: Asynchronous memory copy with LDGSTS instruction vs. TMA
- Asynchronous memory copy with LDGSTS instruction vs. TMA
- NVIDIA H100 Tensor Memory Accelerator
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- TMA unit reduces addressing overhead
- A single thread per warp issues the TMA operation
- Support for different tensor layouts (1D-5D)
Notes:
- New
- asynchronous execution
- features include a new
- Tensor Memory Accelerator (TMA)
- unit that can transfer large blocks of data efficiently between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new
- asynchronous transaction barrier
- for doing atomic data movement and synchronization.
- unit that can efficiently transfer large blocks of data between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new
- 85

## Slide 86: State-of-the-art CPU GPU and FPGA
- State-of-the-art CPU GPU and FPGA
- TABLE:
  |  | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network |
  | CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), 
1.4 (FP64) | 512GB 
(80GB/s) | 32.0GB/s 
(PCIe 4.0 X16) | No |
  | GPU (Nvidia A100) | 8192 (128K) | 19.5 (FP32),
9.7 (FP64),
156 (FP32, Tensor),
312 (FP16, Tensor) | 40/80GB 
(1935GB/s) | 32.0GB/s 
(PCIe 4.0 X16) | No |
  | FPGA (U280) | 9,024 
(25x18 MULs) | 1.8 (FP32) | 40GB 
(460GB/s) | 16.0GB/s 
(PCIe 4.0 X8) | Yes |
Notes:
- 86
- KB MB GB TB
- K M B T E P
- 1B=10
- 亿

## Slide 87: Limitation of GPU
- Limitation of GPU
- CPU
- GPU
- PCIe
- 32.0GB/s
- 1935GB/s

## Slide 88: Serial Code of Prefix sum:
- Serial Code of Prefix sum:
- GPU Code of Prefix sum:
- Multi-pass (ISSUE)
- Limitation of GPU
- // Fills prefix sum array
- void fillPrefixSum(int arr[], int n, int prefixSum[])
- { prefixSum[0] = arr[0];
- // Adding present element
- for (int i = 1; i < n; i++)
- prefixSum[i] = prefixSum[i-1] + arr[i]; }
Notes:
- 88

## Slide 89: Nvidia’s Success: Transparent Scalability
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
Notes:
- Thread block is the key innovation to scale-up GPU architecture. T
- h
- e software code stays the same and enjoys performance speedup while GPU hardware evolves.
- 89

## Slide 90: Key Messages:
- Key Messages:
- Programming model is the key success of Nvidia, rather than the GPU itself.
- GPU has an order of magnitude higher memory bandwidth and compute power than CPU.
- Offloading a task to GPU pays off only when the task has enough compute intensity.
- AI task needs compute-intensive accelerators, e.g., GPU and AI processor.

## Slide 91: Prog. Model 3: Multithreaded
- Prog. Model 3: Multithreaded
- for (i=0; i < N; i++)
- C[i] = A[i] + B[i];
- load
- load
- add
- store
- load
- load
- add
- store
- Iter. 1
- Iter. 2
- Realization: Each iteration is independent
- Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)
- This programming model (software) is called:
- SPMD: Single Program Multiple Data
- Executed on a SIMT machine (hardware)
- Single Instruction Multiple Thread

## Slide 92: A GPU is a SIMD (SIMT) Machine
- A GPU is a SIMD (SIMT) Machine
- Except it is not programmed using SIMD instructions
- It is programmed using threads (SPMD programming model)
- Each thread executes the same code but operates a different piece of data
- Each thread has its own context (i.e., can be treated/restarted/executed independently)
- A set of threads executing the same instruction are dynamically grouped into a warp (wavefront) by the hardware
- A warp is essentially a SIMD operation formed by hardware!

## Slide 93: SIMD vs. SIMT Execution Model
- SIMD vs. SIMT Execution Model
- SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
- [VLD, VLD, VADD, VST], VLEN
- SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
- [LD, LD, ADD, ST], NumThreads
- Two Major SIMT Advantages:
- Can treat each thread separately  i.e., can execute each thread independently on any type of scalar pipeline
- Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

## Slide 94: Brief Review of GPU Architecture (I)
- Brief Review of GPU Architecture (I)
- Streaming Processor Array
- Tesla architecture (G80/GT200)

## Slide 95: Brief Review of GPU Architecture (II)
- Brief Review of GPU Architecture (II)
- Streaming Multiprocessors (SM)
- Streaming Processors (SP)
- Blocks are divided into warps
- SIMD unit (32 threads)
- …
- t0 t1 t2 … t31
- …
- …
- t0 t1 t2 … t31
- …
- Block 0’s warps
- Block 1’s warps
- …
- t0 t1 t2 … t31
- …
- Block 2’s warps
- NVIDIA Fermi architecture

## Slide 96: Brief Review of GPU Architecture (III)
- Brief Review of GPU Architecture (III)
- Streaming Multiprocessors (SM) or Compute Units (CU)
- SIMD pipelines
- Streaming Processors (SP) or CUDA ”cores”
- Vector lanes
- Number of SMs x SPs across generations
- Tesla (2007): 30 x 8
- Fermi (2010): 16 x 32
- Kepler (2012): 15 x 192
- Maxwell (2014): 24 x 128
- Pascal (2016): 56 x 64
- Volta (2017): 80 x 64

## Slide 97: Graphics Processing UnitsSIMD not Exposed to Programmer (SIMT)
- Graphics Processing UnitsSIMD not Exposed to Programmer (SIMT)
Notes:
- 97

## Slide 98: SIMD vs. SIMT Execution Model
- SIMD vs. SIMT Execution Model
- SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
- [VLD, VLD, VADD, VST], VLEN
- SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
- [LD, LD, ADD, ST], NumThreads
- Two Major SIMT Advantages:
- Can treat each thread separately  i.e., can execute each thread independently (on any type of scalar pipeline)  MIMD processing
- Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

## Slide 99: High-Level View of a GPU
- High-Level View of a GPU
- Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

## Slide 100: Latency Hiding via Warp-Level FGMT
- Latency Hiding via Warp-Level FGMT
- Warp: A set of threads that execute the same instruction (on different data elements)
- Fine-grained multithreading
- No interlocking: One instruction per thread in pipeline at a time.
- Interleave warp execution to hide latencies
- Register values of all threads stay in register file
- FGMT enables long latency tolerance
- Millions of pixels
- Decode
- R
- F
- R
- F
- R
- F
- A
- L
- U
- A
- L
- U
- A
- L
- U
- D-Cache
- Thread Warp 6
- Thread Warp 1
- Thread Warp 2
- Data
- All Hit?
- Miss?
- Warps accessing
- memory hierarchy
- Thread Warp 3
- Thread Warp 8
- Writeback
- Warps available
- for scheduling
- Thread Warp 7
- I-Fetch
- SIMD Pipeline
- Slide credit: Tor Aamodt
Notes:
- With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread
- ’
- s warp from the pool of
- “
- ready
- ”
- warps and thereby allows other threads to proceed while the memory system processes its request.
- With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.
- 100

## Slide 101: Warp Execution (Recall the Slide)
- Warp Execution (Recall the Slide)
- 32-thread warp executing ADD A[tid],B[tid]  C[tid]
- C[1]
- C[2]
- C[0]
- A[3]
- B[3]
- A[4]
- B[4]
- A[5]
- B[5]
- A[6]
- B[6]
- Execution using one pipelined functional unit
- C[4]
- C[8]
- C[0]
- A[12]
- B[12]
- A[16]
- B[16]
- A[20]
- B[20]
- A[24]
- B[24]
- C[5]
- C[9]
- C[1]
- A[13]
- B[13]
- A[17]
- B[17]
- A[21]
- B[21]
- A[25]
- B[25]
- C[6]
- C[10]
- C[2]
- A[14]
- B[14]
- A[18]
- B[18]
- A[22]
- B[22]
- A[26]
- B[26]
- C[7]
- C[11]
- C[3]
- A[15]
- B[15]
- A[19]
- B[19]
- A[23]
- B[23]
- A[27]
- B[27]
- Execution using four pipelined functional units
- Slide credit: Krste Asanovic
- Time
- Space
- Time

## Slide 102: Lane
- Lane
- Functional Unit
- Registers
- for each
- Thread
- Memory Subsystem
- Registers for thread IDs
- 0, 4, 8, …
- Registers for thread IDs
- 1, 5, 9, …
- Registers for thread IDs
- 2, 6, 10, …
- Registers for thread IDs
- 3, 7, 11, …
- Slide credit: Krste Asanovic
- SIMD Execution Unit Structure

## Slide 103: CPU threads and GPU kernels
- CPU threads and GPU kernels
- Sequential or modestly parallel sections on CPU
- Massively parallel sections on GPU: Blocks of threads
- Serial Code (host)
- . . .
- . . .
- Parallel Kernel (device)
- KernelA<<<nBlk, nThr>>>(args);
- Serial Code (host)
- Parallel Kernel (device)
- KernelB<<<nBlk, nThr>>>(args);
- Warps not Exposed to GPU Programmers
- Slide credit: Hwu & Kirk

## Slide 104: From Blocks to Warps
- From Blocks to Warps
- GPU cores: SIMD pipelines
- Streaming Multiprocessors (SM)
- Streaming Processors (SP)
- Blocks are divided into warps
- SIMD unit (32 threads)
- …
- t0 t1 t2 … t31
- …
- …
- t0 t1 t2 … t31
- …
- Block 0’s warps
- Block 1’s warps
- …
- t0 t1 t2 … t31
- …
- Block 2’s warps
- NVIDIA Fermi architecture

## Slide 105: SPMD
- SPMD
- Single procedure/program, multiple data
- This is a programming model rather than computer organization
- Each processing element executes the same procedure, except on different data elements
- Procedures can synchronize at certain points in program, e.g. barriers
- Essentially, multiple instruction streams execute the same program
- Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
- Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
- Modern GPUs programmed in a similar way on a SIMD hardware

## Slide 106: Dynamic Warp Formation/Merging
- Dynamic Warp Formation/Merging
- Idea: Dynamically merge threads executing the same instruction (after branch divergence)
- Form new warps from warps that are waiting
- Enough threads branching to each path enables the creation of full new warps
- Warp X
- Warp Y
- Warp Z

## Slide 107: Dynamic Warp Formation/Merging
- Dynamic Warp Formation/Merging
- Idea: Dynamically merge threads executing the same instruction (after branch divergence)
- Fung et al., “Dynamic Warp Formation and Scheduling for Efficient GPU Control Flow,” MICRO 2007.
- Branch
- Path A
- Path B
- Branch
- Path A

## Slide 108: Dynamic Warp Formation Example
- Dynamic Warp Formation Example
- A
- A
- B
- B
- G
- G
- A
- A
- C
- C
- D
- D
- E
- E
- F
- F
- Time
- A
- A
- B
- B
- G
- G
- A
- A
- C
- D
- E
- E
- F
- Time
- A
- x/1111
- y/1111
- B
- x/1110
- y/0011
- C
- x/1000
- y/0010
- D
- x/0110
- y/0001
- F
- x/0001
- y/1100
- E
- x/1110
- y/0011
- G
- x/1111
- y/1111
- A new warp created from scalar threads of both Warp x and y executing at Basic Block D
- D
- Execution of Warp x
- at Basic Block A
- Execution of Warp y
- at Basic Block A
- Legend
- A
- A
- Baseline
- Dynamic
- Warp
- Formation
- Slide credit: Tor Aamodt

## Slide 109: Hardware Constraints Limit Flexibility of Warp Grouping
- Hardware Constraints Limit Flexibility of Warp Grouping
- Lane
- Functional Unit
- Registers
- for each
- Thread
- Memory Subsystem
- Registers for thread IDs
- 0, 4, 8, …
- Registers for thread IDs
- 1, 5, 9, …
- Registers for thread IDs
- 2, 6, 10, …
- Registers for thread IDs
- 3, 7, 11, …
- Slide credit: Krste Asanovic

## Slide 110: Clarification of Some GPU Terms
- Clarification of Some GPU Terms
- TABLE:
  | Generic Term | NVIDIA Term | AMD Term | Comments |
  | Vector length | Warp size | Wavefront size | Number of threads that run in parallel (lock-step) on a SIMD functional unit |
  | Pipelined functional unit /
Scalar pipeline | Streaming processor /
CUDA core | - | Functional unit that executes instructions for one GPU thread |
  | SIMD functional unit /
SIMD pipeline | Group of N streaming processors (e.g., N=8 in GTX 285, N=16 in Fermi) | Vector ALU | SIMD functional unit that executes instructions for an entire warp |
  | GPU core | Streaming multiprocessor | Compute unit | It contains one or more warp schedulers and one or several SIMD pipelines |

## Slide 111: Programming Model vs. Hardware Execution Model
- Programming Model vs. Hardware Execution Model
- Hardware Programming Model
- Programming Model
- Core
- Streaming
- Multi-processor
- GPU
- CUDA core:
- Thread
- Thread block (s)
- Wrap
- Thread blocks

## Slide 112: NVIDIA H100 Block Diagram
- NVIDIA H100 Block Diagram
- 144 cores on the full GH100
- 60MB L2 cache
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
Notes:
- 112

## Slide 113: NVIDIA H100 Core
- NVIDIA H100 Core
- 48 TFLOPS Single Precision*
- 24 TFLOPS Double Precision*
- 800 TFLOPS (FP16, Tensor Cores)*
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- * Preliminary performance estimates
Notes:
- 113

## Slide 114: Shared memory virtual address space distributed across the blocks of a cluster
- Shared memory virtual address space distributed across the blocks of a cluster
- Load, store, and atomic operations to other SM’s shared memory
- NVIDIA H100 Distributed Shared Memory
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- Thread block clusters and distributed shared memory (DSMEM) are leveraged via cooperative_groups API
- TMA unit supports copies across thread blocks in a cluster
- Asynchronous transaction barriers
Notes:
- Distributed shared memory
- allows direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks.
- enables direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks
- 114

## Slide 115: 7 versions in CUDA samples: Tree-based reduction in shared memory
- 7 versions in CUDA samples: Tree-based reduction in shared memory
- Version 0: No whole warps active
- Version 1: Contiguous threads, but many bank conflicts
- Version 2: No bank conflicts
- Version 3: First level of reduction when reading from global memory
- Version 4: Warp shuffle or unrolling of final warp
- Version 5: Warp shuffle or complete unrolling
- Version 6: Multiple elements per thread sequentially
- Optimized Parallel Reduction
- https://docs.nvidia.com/cuda/cuda-samples/index.html#cuda-parallel-reduction
- Harris, “Optimizing Parallel Reduction in CUDA,” https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf

## Slide 116: 3 new versions of reduction based on 3 previous versions
- 3 new versions of reduction based on 3 previous versions
- Version 0: No whole warps active
- Version 3: First level of reduction when reading from global memory
- Version 6: Multiple elements per thread sequentially
- New versions 7, 8, and 9
- Replace the for loop (tree-based reduction) with one shared memory atomic operation per thread
- Reduction with Atomic Operations

## Slide 117: 256-bin histogram calculation
- 256-bin histogram calculation
- Video Processing: Performance Results (I)
- Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
- JPDC, 2012
- 44%
- 21%
Notes:
- 117

## Slide 118: RGB-to-grayscale conversion
- RGB-to-grayscale conversion
- Video Processing: Performance Results (II)
- Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
- JPDC, 2012
- 63%
- 18%
Notes:
- 118

## Slide 119: Performance Considerations
- Performance Considerations
- Main bottlenecks
- CPU-GPU data transfers
- Global memory access
- Memory access
- Latency hiding
- Occupancy
- Memory coalescing
- Data reuse
- Shared memory usage
- SIMD (Warp) Utilization: Divergence
- Other considerations
- Atomic operations: Serialization
- Data transfers between CPU and GPU
- Overlap of communication and computation

## Slide 120: Recommended Readings
- Recommended Readings
- Hwu and Kirk, “Programming Massively Parallel Processors,” Third Edition, 2017
- Chapter 5: Performance considerations
- Chapter 18 - Programming
- a heterogeneous computing cluster,
- Section 18.5
Notes:
- 120