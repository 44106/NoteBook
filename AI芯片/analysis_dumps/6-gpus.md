# 6-gpus-architecture.pptx selected slides

## Slide 15: Agenda for Today
- Agenda for Today
- Why GPU?
- Hardware Execution Model
- Programming Model
- SISD vs. SIMD vs. SPMD
- GPU Programming Example
- Advance
- SIMT (Hardware) & Warp (Software)
Notes:
- 15

## Slide 16: Motivation of In-network Computing
- Motivation of In-network Computing
- Why GPU?
- Need More Computing Power.

## Slide 17: OpenAI: Compute Power Needed by NN Model
- OpenAI: Compute Power Needed by NN Model
- TABLE:
  | Model | Model Size | Compute/iteration
(OPs) |
  | VGG 19 | 114M | ~19.6 B |
  | “GPT-3” | 175B | ~250 T |
- One Forward Pass of Model:
Notes:
- 17
- KB MB GB TB
- K M B T
- 1B=10
- 亿

## Slide 18: CPU:
- CPU:
- Few complex cores
- Larger cache for low memory latency
- Large and slow memory
- CPU vs GPU： Compute Perspective
- GPU:
- Lots of simple cores
- Small cache for low memory latency
- Small and fast memory

## Slide 19: State-of-the-art CPU GPU and FPGA
- State-of-the-art CPU GPU and FPGA
- TABLE:
  |  | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network |
  | CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), 
1.4 (FP64) | 512GB 
(80GB/s) | 32.0GB/s 
(PCIe 4.0 X16) | No |
  | GPU (Nvidia H100) | 18432 (128K) | 67 (FP32),
34 (FP64),
989 (FP32, Tensor),
1979 (FP16, Tensor) | 80GB 
(3350GB/s) | 64.0GB/s 
(PCIe 5.0 X16) | No |
  | FPGA (U280) | 9,024 
(25x18 MULs) | 1.8 (FP32) | 40GB 
(460GB/s) | 16.0GB/s 
(PCIe 4.0 X8) | Yes |
Notes:
- 19
- KB MB GB TB
- K M B T E P
- 1B=10
- 亿

## Slide 20: Relationship between CPU and GPU
- Relationship between CPU and GPU
- PCI Bus
- CPU
- GPU

## Slide 21: Motivation of In-network Computing
- Motivation of In-network Computing
- More cores  More trouble
- Challenge: How to manipulate them?
Notes:
- 之前千核项目 很多，只活了英伟达。
- 21

## Slide 22: GPU Computing
- GPU Computing
- Key Idea:
- Computation is offloaded to the GPU
- Three steps:
- CPU-GPU data transfer (1)
- GPU kernel execution (2)
- GPU-CPU data transfer (3)
Notes:
- 22

## Slide 23: CPU-GPU Co-processing:
- CPU-GPU Co-processing:
- CPU: Sequential or modestly parallel sections
- GPU: Massively parallel sections
- Serial Code (CPU):
- . . .
- . . .
- Parallel Kernel (GPU):
- KernelA<<<nBlk, nThr>>>(args);
- Serial Code (CPU):
- Parallel Kernel (GPU):
- KernelB<<<nBlk, nThr>>>(args);
- Programming Model: CPU and GPU

## Slide 24: Recall: Amdahl’s Law
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

## Slide 25: GPUs are SIMD Engines Underneath
- GPUs are SIMD Engines Underneath
- The instruction pipeline operates like a SIMD pipeline (e.g., an array processor)
- However, the programming is done using threads, NOT SIMD instructions
- To understand this, let’s go back to our parallelizable code example
- But, before that, let’s distinguish between
- Programming Model (Software)
- vs.
- Execution Model (Hardware)

## Slide 26: Programming Model vs. Hardware Execution Model
- Programming Model vs. Hardware Execution Model
- Programming Model： how the programmer expresses the code
- E.g., Sequential (von Neumann), Data Parallel (SIMD), Dataflow, Multi-threaded (MIMD, SPMD), …
- Hardware Execution Model： how the hardware executes the code underneath
- E.g., Out-of-order execution, Vector processor, Array processor, Dataflow processor, Multiprocessor, Multithreaded processor, …
- Discussion: Execution Model can be very different from Programming Model
- E.g., von Neumann model implemented by an OoO processor
- E.g., SPMD model implemented by a SIMD processor (a GPU)

## Slide 27: GPU: Programming Model vs. Hardware Execution Model
- GPU: Programming Model vs. Hardware Execution Model
- Hardware Execution Model
- CUDA Programming Model
- Streaming
- Multi-processor
- GPU
- CUDA core
- Thread
- Thread block
- Grid
- ...
Notes:
- 27

## Slide 28: Agenda for Today
- Agenda for Today
- Where is GPU? & Key Message
- Hardware Execution Model
- Programming Model
- SISD vs. SIMD vs. SPMD
- GPU Programming Example
- Advance
- SIMT (Hardware) & Warp (Software)
Notes:
- 28

## Slide 29: A Many-core GPU (Hardware Execution Model)
- A Many-core GPU (Hardware Execution Model)
Notes:
- 29

## Slide 30: NVIDIA GeForce GTX 285
- NVIDIA GeForce GTX 285
- NVIDIA-speak:
- 240 stream processors (CUDA cores)
- “SIMT execution”
- Generic speak:
- 30 cores
- 8 SIMD functional units per core
- NVIDIA, “NVIDIA GeForce GTX 200 GPU. Architectural Overview. White Paper,” 2008.
- Slide credit: Kayvon Fatahalian
Notes:
- Link to the GTX 200 series white paper:
- https://
- www.nvidia.com
- /docs/IO/55506/GeForce_GTX_200_GPU_Technical_Brief.pdf
- The NVIDIA GeForce GTX 285 was launched on January 2009.
- 30

## Slide 31: NVIDIA GeForce GTX 285 “core”(SM)
- NVIDIA GeForce GTX 285 “core”(SM)
- …
- = instruction stream decode
- = SIMD functional unit, control
- shared across 8 units
- = execution context storage
- = multiply-add
- = multiply
- 64 KB of storage
- for thread contexts (registers)
- Slide credit: Kayvon Fatahalian
Notes:
- 30 * 32 * 32 = 30 * 1024 = 30K fragments
- 64KB register file = 16 32-bit registers per thread = 64B (1/32 that of LRB)
- 16KB of shared scratch
- 80KB / core available to software
- 31

## Slide 32: NVIDIA GeForce GTX 285
- NVIDIA GeForce GTX 285
- Tex
- Tex
- Tex
- Tex
- Tex
- Tex
- Tex
- Tex
- Tex
- Tex
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- …
- 30 cores on the GTX 285: 30K threads
- Slide credit: Kayvon Fatahalian
Notes:
- If you
- ’
- re running a CUDA program, and your not launching 30K threads, you are certainly not getting full latency hiding, and you might not be using the GPU well
- 32

## Slide 33: Evolution of NVIDIA GPUs: Compute
- Evolution of NVIDIA GPUs: Compute
Notes:
- 33

## Slide 34: NVIDIA V100
- NVIDIA V100
- NVIDIA-speak:
- 5120 stream processors (CUDA cores)
- “SIMT execution”
- Generic speak:
- 80 cores
- 64 SIMD functional units per core
- Tensor cores for Machine Learning
- NVIDIA, “NVIDIA Tesla V100 GPU Architecture. White Paper,” 2017.
Notes:
- CUDA core
- ：
- stream processor
- 34

## Slide 35: NVIDIA V100 Block Diagram
- NVIDIA V100 Block Diagram
- 80 cores on the V100
- https://devblogs.nvidia.com/inside-volta/
Notes:
- 35

## Slide 36: NVIDIA A100
- NVIDIA A100
- NVIDIA-speak:
- 6912 stream processors (CUDA cores)
- “SIMT execution”
- Generic speak:
- 108 cores
- 64 SIMD functional units per core
- Tensor cores for Machine Learning
- Support for sparsity
- New floating point data type (TF32)
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
Notes:
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
- 36

## Slide 37: NVIDIA A100 Block Diagram
- NVIDIA A100 Block Diagram
- 108 cores on the A100
- (Up to 128 cores in the full-blown chip)
- 40MB L2 cache
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
Notes:
- The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2
- cache.The
- L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see
- https://
- developer.nvidia.com
- /blog/
- nvidia
- -ampere-architecture-in-depth/
- ).
- 37

## Slide 38: NVIDIA H100
- NVIDIA H100
- NVIDIA-speak:
- 8448 stream processors (CUDA cores)
- “SIMT execution”
- Generic speak:
- 132 cores
- 64 SIMD functional units per core
- Tensor cores for Machine Learning
- Support for sparsity
- Support for transformer
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
Notes:
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
- 38

## Slide 39: NVIDIA H100 Block Diagram
- NVIDIA H100 Block Diagram
- https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
Notes:
- The A100 GPU includes 40 MB of L2 cache, which is 6.7x larger than V100 L2
- cache.The
- L2 cache is divided into two partitions to enable higher bandwidth and lower latency memory access. Each L2 partition localizes and caches data for memory accesses from SMs in the GPCs directly connected to the partition. This structure enables A100 to deliver a 2.3x L2 bandwidth increase over V100 (see
- https://
- developer.nvidia.com
- /blog/
- nvidia
- -ampere-architecture-in-depth/
- ).
- 39

## Slide 40: GPU Trend: H100 vs. A100
- GPU Trend: H100 vs. A100
- TABLE:
  |  | FP8 | FP16 | FP32 | FP64 | Memory bandwidth | Memory capacity |
  | H100 | 4000T | 2000T | 1000T | 60T | 3TB/s | 80GB |
  | A100 | 666T | 666T | 333T | 20T | 2TB/s | 80GB |
- Compute power scales well.
- GPU memory capacity does not scale well.
Notes:
- 军迷：
- 算力：武器 坦克等
- 内存：后勤
- 40

## Slide 41: Agenda for Today
- Agenda for Today
- Where is GPU? & Key Message
- Hardware Execution Model
- Programming Model
- SISD vs. SIMD vs. SPMD
- GPU Programming Example
- Advance
- SIMT (Hardware) & Warp (Software)
Notes:
- 41

## Slide 42: How Can You Exploit Parallelism Here?
- How Can You Exploit Parallelism Here?
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
- Scalar Sequential Code
- Let’s examine three programming options to exploit instruction-level parallelism present in this sequential code:
- 1. Sequential (SISD)
- 2. Data-Parallel (SIMD)
- 3. Multithreaded (SPMD)

## Slide 43: Prog. Model 1: Sequential (SISD)
- Prog. Model 1: Sequential (SISD)
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
- Scalar Sequential Code
- Can be executed on thee processors:
- 1, Pipelined processor
- 2, Out-of-order execution processor
- Independent instructions executed when ready
- Different iterations are present in the instruction window and can execute in parallel in multiple functional units
- 3, Superscalar or VLIW processor
- Can fetch and execute multiple instructions per cycle
- for (i=0; i < N; i++)
- C[i] = A[i] + B[i];

## Slide 44: load
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
- Scalar Sequential Code
- Prog. Model 2: Data Parallel (SIMD)
- for (i=0; i < N; i++)
- C[i] = A[i] + B[i];
- Vector Instruction
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
- Vectorized Code
- Motivation: Each iteration is independent
- Idea: Programmer or compiler generates a SIMD instruction to execute the same instruction from all iterations across different data
- VLD A  V1
- VLD B  V2
- VADD V1 + V2  V3
- VST V3  C

## Slide 45: load
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
- Scalar Sequential Code
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
- Motivation: Each iteration is independent
- Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)

## Slide 46: Prog. Model 3: Multithreaded
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

## Slide 47: SPMD
- SPMD
- SPMD: Single procedure/program, multiple data
- This is a programming model rather than computer organization
- Each processing element executes the same procedure, except on different data elements
- Procedures can synchronize at certain points in program, e.g. barriers
- Key Idea of SPMD: multiple instruction streams execute the same program
- Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
- Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
- Modern GPUs programmed in a similar way on a SIMD hardware

## Slide 48: Agenda for Today
- Agenda for Today
- Where is GPU? & Key Message
- Hardware Execution Model
- Programming Model
- SISD vs. SIMD vs. SPMD
- GPU Programming Example
- Advance
- SIMT (Hardware) & Warp (Software)
Notes:
- 48

## Slide 49: CUDA/OpenCL Programming Model
- CUDA/OpenCL Programming Model
- Single Program Multiple Data (SPMD), e.g., CUDA
- Bulk synchronous programming: Global (coarse-grain) synchronization between kernels
- The device (typically GPU) executes CUDA kernels
- Grid
- Thread Block
- CUDA runtime schedules at granularity of thread block.
- A thread block is a programming abstraction that represents a group of threads that can be executed in parallel.
- Within a block, shared memory, and synchronization.
- Thread
- A thread corresponds to an iteration.

## Slide 50: GPU: Programming Model vs. Hardware Execution Model
- GPU: Programming Model vs. Hardware Execution Model
- Hardware Execution Model
- CUDA Programming Model
- Streaming
- Multi-processor
- GPU
- CUDA core
- Thread
- Thread block
- Grid
- ...
Notes:
- Wrap
- 50

## Slide 51: CUDA: Memory Hierarchy
- CUDA: Memory Hierarchy

## Slide 52: Function prototypes
- Function prototypes
- float serialFunction(…);
- __global__ void kernel(…);
- main()
- 1) Allocate memory space on the device – cudaMalloc(&d_in, bytes);
- 2) Transfer data from host to device – cudaMemCpy(d_in, h_in, …);
- 3) Execution configuration setup: #blocks and #threads
- 4) Kernel call – kernel<<<execution configuration>>>(args…);
- 5) Transfer results from device to host – cudaMemCpy(h_out, d_out, …);
- Kernel – __global__ void kernel(type args,…)
- Automatic variables transparently assigned to registers
- Shared memory: __shared__
- Intra-block synchronization: __syncthreads();
- Repeat as needed
- Traditional Program Structure in CUDA
- Slide credit: Hwu & Kirk
Notes:
- 52

## Slide 53: CUDA Programming Language
- CUDA Programming Language
- Memory allocation
- cudaMalloc((void**)&d_in, #bytes);
- Memory copy
- cudaMemcpy(d_in, h_in, #bytes, cudaMemcpyHostToDevice);
- Kernel launch
- kernel<<< #blocks, #threads >>>(args);
- Memory deallocation
- cudaFree(d_in);
- Explicit synchronization
- cudaDeviceSynchronize();

## Slide 54: First GPU Example: Vector Addition (I)
- First GPU Example: Vector Addition (I)
- Key Idea: one GPU thread to each element-wise addition

## Slide 55: First GPU Example: Vector Addition (II)
- First GPU Example: Vector Addition (II)
- A grid: the whole set of threads
- We need a way to assign threads to GPU cores

## Slide 56: First GPU Example: Vector Addition (III)
- First GPU Example: Vector Addition (III)
- We group threads into blocks
- Block 0
- Block 1
- Block 2
- Block 3
- blockIdx = 0
- blockIdx = 1
- blockIdx = 2
- blockIdx = 3
- threadIdx = 0
- threadIdx = 1
- threadIdx = 2
- threadIdx = 2
- blockDim = 4
Notes:
- 每个
- block
- 有四个
- threads
- 。
- blockIdx
- = 0
- 56

## Slide 57: GPU: Programming Model vs. Hardware Execution Model
- GPU: Programming Model vs. Hardware Execution Model
- Hardware Execution Model
- CUDA Programming Model
- Streaming
- Multi-processor
- GPU
- CUDA core
- Thread
- Thread block
- Grid
- ...
Notes:
- Wrap
- 57

## Slide 58: Host Code Example: Vector Addition
- Host Code Example: Vector Addition
- void vecadd(float* A, float* B, float* C, int N) {
- //1, Allocate GPU memory
- float *A_d, *B_d, *C_d;
- cudaMalloc((void**) &A_d, N*sizeof(float));
- cudaMalloc((void**) &B_d, N*sizeof(float));
- cudaMalloc((void**) &C_d, N*sizeof(float));
- //2, Copy data to GPU memory
- cudaMemcpy(A_d, A, N*sizeof(float), cudaMemcpyHostToDevice);
- cudaMemcpy(B_d, B, N*sizeof(float), cudaMemcpyHostToDevice);
- //3, Perform computation on GPU
- ...
- //4, Copy data from GPU memory
- cudaMemcpy(C, C_d, N*sizeof(float), cudaMemcpyDeviceToHost);
- //5, Deallocate GPU memory
- cudaFree(A_d);
- cudaFree(B_d);
- cudaFree(C_d);
- }
- Slide credit: Izzat El Hajj
- const unsigned int numThreadsPerBlock = 512;
- const unsigned int numBlocks = N/numThreadsPerBlock;
- vecadd_kernel<<<numBlocks, numThreadsPerBlock>>>(A_d, B_d, C_d, N);

## Slide 59: Kernel Code Example: Vector Addition
- Kernel Code Example: Vector Addition
- Slide credit: Izzat El Hajj
- __global__ void vecadd_kernel(float* A, float* B, float* C, int N) {
- int i = blockDim.x*blockIdx.x + threadIdx.x;
- C[i] = A[i] + B[i];
- }
- blockDim: block dimension
- blockIdx: block index within a grid
- threadIdx: thread index within a block

## Slide 60: Boundary Conditions
- Boundary Conditions
- Question: What if the size of the input is not a multiple of the number of threads per block?
- Solution: use the ceiling to launch extra threads then omit the threads after the boundary
- Host code:
- Kernel code:
- const unsigned int numBlocks = (N +numThreadsPerBlock – 1)/numThreadsPerBlock;
- __global__ void vecadd_kernel(float* A, float* B, float* C, int N) {
- int i = blockDim.x*blockIdx.x + threadIdx.x;
- if(i < N) {
- C[i] = A[i] + B[i]; }
- }
- vecadd_kernel<<<numBlocks, numThreadsPerBlock>>>(A_d, B_d, C_d, N);

## Slide 61: Sample GPU Program: Matrix Multiplication
- Sample GPU Program: Matrix Multiplication
- Slide credit: Hyesoon Kim

## Slide 62: Indexing and Memory Access
- Indexing and Memory Access
- Images are 2D data structures
- height x width
- Image[j][i], where 0 ≤ j < height, and 0 ≤ i < width
- Image[0][1]
- Image[1][2]
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
Notes:
- 62

## Slide 63: Image Layout in Memory
- Image Layout in Memory
- Row-major layout
- Image[j][i] = Image[j x width + i]
- Image[0][1] = Image[0 x 8 + 1]
- Image[1][2] = Image[1 x 8 + 2]
- Stride = width
Notes:
- 63

## Slide 64: Indexing and Memory Access: 1D Grid
- Indexing and Memory Access: 1D Grid
- One GPU thread per pixel
- Grid of Blocks of Threads
- gridDim.x, blockDim.x
- blockIdx.x, threadIdx.x
- Block 0
- Block 0
- Thread 0
- Thread 1
- Thread 2
- Thread 3
- blockIdx.x
- threadIdx.x
- blockIdx.x * blockDim.x + threadIdx.x
- 6 * 4 + 1 = 25
Notes:
- 64

## Slide 65: Agenda for Today
- Agenda for Today
- Where is GPU? & Key Message
- Hardware Execution Model
- Programming Model
- SISD vs. SIMD vs. SPMD
- GPU Programming Example
- Advance
- SIMT (Hardware) & Warp (Software)
Notes:
- 65

## Slide 66: GPU: Programming Model vs. Hardware Execution Model
- GPU: Programming Model vs. Hardware Execution Model
- Hardware Execution Model
- CUDA Programming Model
- Streaming
- Multi-processor
- GPU
- CUDA core
- Thread
- Thread block
- Grid
- ...
- Wrap
- SIMT
Notes:
- SIMD Wrap
- 66

## Slide 67: SIMT (Hardware) & Warp (Software)
- SIMT (Hardware) & Warp (Software)
- SIMT: Single Instruction Multiple Thread
- Key Feature: 16 CUDA cores in a SM are executed in a lock step.
- Warp:
- A warp, a basic execution unit, consists of 32 consecutive threads
- A thread block is divided into warps for SIMT execution.
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

## Slide 68: Motivation of In-network Computing
- Motivation of In-network Computing
- Why SIMT and Warp?
- Reduce GPU scheduling overhead

## Slide 69: Warp 0 at PC X+3
- Warp 0 at PC X+3
- Warp 0 at PC X+2
- Warp 0 at PC X+1
- How to Form Warps?
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
- Warp 0 at PC X
- Warp: A set of threads that execute
- the same instruction (i.e., at the same PC)
- Iter. 32

## Slide 70: Mapping Warps on a SIMT Hardware
- Mapping Warps on a SIMT Hardware
- Warp:
- A thread block is divided into warps.
- A warp executes the same instruction on different data elements
- SIMT Pipeline:
- 16 CUDA cores are executed in a lock step to serve each warp.
- Thread Warp 0
- Thread Warp 8
- Thread Warp 7
- Thread Warp
- Scalar
- Thread
- 0
- Scalar
- Thread
- 1
- Scalar
- Thread
- 2
- Scalar
- Thread
- 31
- Common PC
- SIMT Pipeline
- Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.
Notes:
- In SIMD, you need to specify the data array + an instruction (on which to operate the data on) + THE INSTRUCTION WIDTH.
- Eg: You might want to add 2 integer arrays of length 16, then a SIMD instruction would look like (the instruction has been cooked-up by me for demo)
- add.16 arr1 arr2
- However, SIMT doesn't bother about the instruction width. So, essentially, you could write the above example as:
- arr1[i] + arr2[i]
- and then launch as many threads as the length of the array, as you want.
- Note that, if the array size was, let us say, 32, then SIMD EXPECTS you to explicitly call two such 'add.16' instructions!
- Whereas, this is not the case with SIMT.
- 70

## Slide 71: GPU Execution with Warps
- GPU Execution with Warps
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
- Warp 0 at PC X
- Assume: a warp consists of 32 threads
- If you have 32K iterations, and 1 iteration/thread  1K warps
- Warps can be interleaved on the same pipeline  Fine grained multithreading of warps.
- Warp 1 at PC X
- Iter. 33
- Iter. 34
- Warp 20 at PC X+2
- Iter.
- 20*32 + 1
- Iter.
- 20*32 + 2

## Slide 72: Warp Instruction Level Parallelism
- Warp Instruction Level Parallelism
- Can overlap execution of multiple instructions
- Example machine has 32 threads per warp and 8 lanes
- Completes 24 operations/cycle while issuing 1 warp/cycle
- W3
- W0
- W1
- W4
- W2
- W5
- Load Unit
- Multiply Unit
- Add Unit
- time
- Warp issue
- Slide credit: Krste Asanovic

## Slide 73: Motivation of In-network Computing
- Motivation of In-network Computing
- SIMT is not SIMD!

## Slide 74: SIMD vs. SIMT Execution Model
- SIMD vs. SIMT Execution Model
- SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
- [VLD, VLD, VADD, VST], VLEN
- SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
- [LD, LD, ADD, ST], NumThreads
- Two Major SIMT Advantages:
- Can treat each thread separately  i.e., can execute each thread independently on any type of scalar pipeline  MIMD processing
- Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

## Slide 75: Slide credit: Hyesoon Kim
- Slide credit: Hyesoon Kim
- GPUs were invented and gpus are a kind vector computer which is really wild because while gpus have big vectors they essentially run scalar programs on each element and you can think of them as running a vector of scalar programs which by the way was a genius abstraction because everybody can write a scalar program almost nobody can write a vector program but suddenly we had all kinds of people doing vector programs on GPUs”
- --- Jim Keller @DAC’24
- SPMD: Genius Abstraction

## Slide 76: SIMT Code vs. SIMD Code
- SIMT Code vs. SIMD Code
- for (ii = 0; ii < 100000; ++ii) {
- C[ii] = A[ii] + B[ii];
- }
- // there are 100000 threads
- __global__ void KernelFunction(…) {
- int tid = blockDim.x * blockIdx.x + threadIdx.x;
- int varA = aa[tid];
- int varB = bb[tid];
- C[tid] = varA + varB;
- }
- CPU scalar code
- CUDA code
- Slide credit: Hyesoon Kim
- // there are 25000 loops with SIMD=4
- …
- v_A = vec_load (A);
- v_B = vec_load (B);
- v_C = vec_add(v_A, v_B);
- Vec_store(v_C, C)
- …
- }
- CPU vector code

## Slide 77: Warp-based SIMD vs. Traditional SIMD
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

## Slide 78: Threads Can Take Different Paths in Warp-based SIMD
- Threads Can Take Different Paths in Warp-based SIMD
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

## Slide 79: Control Flow Problem in GPUs/SIMT
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
Notes:
- 79

## Slide 80: SIMD Utilization
- SIMD Utilization
- Intra-warp divergence
- Compute(threadIdx.x);
- if (threadIdx.x % 2 == 0){
- Do_this(threadIdx.x);
- }
- else{
- Do_that(threadIdx.x);
- }

## Slide 81: Increasing SIMD Utilization
- Increasing SIMD Utilization
- Divergence-free execution
- Compute(threadIdx.x);
- if (threadIdx.x < 32){
- Do_this(threadIdx.x * 2);
- }
- else{
- Do_that((threadIdx.x%32)*2+1);
- }

## Slide 82: Vector Reduction: Naïve Mapping (I)
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

## Slide 83: Vector Reduction: Naïve Mapping (II)
- Vector Reduction: Naïve Mapping (II)
- Program with low SIMD utilization
- __shared__ float partialSum[]
- unsigned int t = threadIdx.x;
- for (int stride = 1; stride < blockDim.x; stride *= 2) {
- __syncthreads();
- if (t % (2*stride) == 0)
- partialSum[t] += partialSum[t + stride];
- }

## Slide 84: Divergence-Free Mapping (I)
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

## Slide 85: Divergence-Free Mapping (II)
- Divergence-Free Mapping (II)
- Program with high SIMD utilization
- __shared__ float partialSum[]
- unsigned int t = threadIdx.x;
- for (int stride = blockDim.x; stride > 0; stride >> 1){
- __syncthreads();
- if (t < stride)
- partialSum[t] += partialSum[t + stride];
- }

## Slide 86: Programming Model vs. Hardware Execution Model
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

## Slide 87: NVIDIA H100 Block Diagram
- NVIDIA H100 Block Diagram
- 144 cores on the full GH100
- 60MB L2 cache
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
Notes:
- 87

## Slide 88: NVIDIA H100 Core
- NVIDIA H100 Core
- 48 TFLOPS Single Precision*
- 24 TFLOPS Double Precision*
- 800 TFLOPS (FP16, Tensor Cores)*
- https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- * Preliminary performance estimates
Notes:
- 88

## Slide 89: Asynchronous memory copy with LDGSTS instruction vs. TMA
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
- 89

## Slide 90: Shared memory virtual address space distributed across the blocks of a cluster
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
- 90

## Slide 91: NVIDIA GeForce GTX 285 “core”
- NVIDIA GeForce GTX 285 “core”
- …
- 64 KB of storage
- for thread contexts (registers)
- Groups of 32 threads share instruction stream (each group is a Warp)
- Up to 32 warps are simultaneously interleaved
- Up to 1024 thread contexts can be stored
- Slide credit: Kayvon Fatahalian
Notes:
- To get maximal latency hiding:
- Run 1/32 of the time
- 16 words per thread = 64B
- 91