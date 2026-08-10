# 15-flashattention43.pptx

- Slides: 27

## Slide 1: Computer Arch. & AI ChipLecture 15: Flash Attention

### Extracted Shape Text
- Computer Arch. & AI ChipLecture 15: Flash Attention
- Prof. Zeke Wang
- Zhejiang University
- June 1 2026

### Notes
- 1

## Slide 2: Outline

### Extracted Shape Text
- Outline
- Zero
- FlashAttention

## Slide 3: Networking

### Extracted Shape Text
- Networking
- Storage
- Computing
- Model
- Training
- Compiling
- AI System: Four Components

## Slide 4: AI System: Storage

- Images: 1; Tables: 0

### Extracted Shape Text
- AI System: Storage

## Slide 5: ZeRO: Zero Redundancy Optimizer

- Images: 1; Tables: 0

### Extracted Shape Text
- ZeRO: Zero Redundancy Optimizer
- Key Idea:
- Each GPU stores a subset of optimizer states, rather than the whole states like data parallel.

## Slide 6: ZeRO: Zero Redundancy Optimizer

- Images: 1; Tables: 0

### Extracted Shape Text
- ZeRO: Zero Redundancy Optimizer
- Benefit:
- Training a larger model.

## Slide 7: Overhead of ZeRO: More Communication

- Images: 1; Tables: 0

### Extracted Shape Text
- Overhead of ZeRO: More Communication
- Typical PyTorch step:
- Forward:
- Backward:
- Optimizer:
- Overhead: more collectives

## Slide 8: Summary

### Extracted Shape Text
- Summary
- Networks and dataset are getting larger to set new state of art results
- Scale-out enables these neural networks to be trained
- Success requires many optimized components:
- Hardware:
- Fast accelerators for DL
- High-bandwidth, low-latency interconnects
- Topologies matter (must match communication patterns)
- Network switches with math capabilities free up DL accelerators to do compute
- SmartNIC for offloaded compression/decompression
- Software:
- Math libraries (CUDNN, CUBLAS, MKL, CANN …)
- Collective communication libraries (NCCL, Horovod, …)
- Training frameworks (MindSpore, PyTorch, TensoFlow, HugeCTR, …)
- Proper choice of parallelism (manual, MeshTensorFlow, Gshard, ZeRO)

## Slide 9: Batch Size Limitation of LLM Training

### Extracted Shape Text
- Batch Size Limitation of LLM Training
- Batch Size Limitation of LLM Training
- Llama: 4M token,
- Seq length: 4K,
- Batch size: 1K
- How to choose the parallel training strategy?
- When you have 1K NPU/GPU?
- When you have 10K NPU/GPU?

## Slide 10: Outline

### Extracted Shape Text
- Outline
- Zero
- FlashAttention

## Slide 11: Why FlashAttention？

- Images: 1; Tables: 0

### Extracted Shape Text
- Why FlashAttention？
- Why FlashAttention？
- Normal attention is bound by IO
- GPU utilization is low

### Notes
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 11

## Slide 12: Naïve Attention

### Extracted Shape Text
- Naïve Attention
- Naïve Attention O = Softmax(QKT) V
- 1, A = QKT A: Load Q K from HBM, compute A, write A to HBM
- 2, A = Softmax (A) : Load A from HBM, compute A, write A to HBM
- 3, O = AV: Load A V from HBM, compute O, write O to HBM
- Q
- (S x D)
- A = softmax(A)
- (S x S)
- V
- (S x D)
- O = AV
- (S x D)
- A = QKT
- (S x S)
- K
- (S x D)

## Slide 13: Two Issues of Naïve Attention

### Extracted Shape Text
- Two Issues of Naïve Attention
- Q
- (S x D)
- A = softmax(A)
- (S x S)
- V
- (S x D)
- O = AV
- (S x D)
- A = QKT
- (S x S)
- K
- (S x D)
- Two Issues of Naïve Attention
- Large intermediate results O(S2) with a long sequence
- Repeated reads/writes from GPU device memory

## Slide 14: Two Challenges of Naïve Attention

### Extracted Shape Text
- Two Challenges of Naïve Attention
- Q
- (S x D)
- A = softmax(A)
- (S x S)
- V
- (S x D)
- O = AV
- (S x D)
- A = QKT
- (S x S)
- K
- (S x D)
- Two Challenges of Naïve Attention
- Low precision of the fp16 elements of A easily overflow
-  Safe Softmax
- A = softmax(A) is not a streaming algorithm
-  Online Softmax

### Notes
- 14

## Slide 15: Softmax  Safe Softmax

### Extracted Shape Text
- Softmax  Safe Softmax
- Given a row of {x1, x2, …, xN}), Softmax({x1, x2, …, xN}) =

## Slide 16: Details of Safe Softmax

### Extracted Shape Text
- Details of Safe Softmax
- Goal: Given a row of {x1, x2, …, xN}), Softmax({x1, x2, …, xN}) = ({a1, a2, …, aN})

## Slide 17: Details of Online Softmax

### Extracted Shape Text
- Details of Online Softmax
- Goal: Given a row of {x1, x2, …, xN}), Softmax({x1, x2, …, xN}) = ({a1, a2, …, aN})

## Slide 18: FlashAttention -1

### Extracted Shape Text
- FlashAttention -1
- Two key ideas of FlashAttention-1
- 1, Tiling: Compute the attention weights block by block so that we don’t have to load everything into SRAM at once
- 2, Recomputation: don’t ever store the full attention matrix, but just recompute the parts of it you need during the backward pass

## Slide 19: FlashAttention -1

- Images: 1; Tables: 0

### Extracted Shape Text
- FlashAttention -1
- Inter-Tile: parallelize over batch size and heads  low parallelism
- Intra-Tile:  extra access to HBM from O
- Outer loop: K V
- Inner loop: Q
- Outer loop
- Inner loop

## Slide 20: FlashAttention -2

- Images: 1; Tables: 0

### Extracted Shape Text
- FlashAttention -2
- Inter-Tile: parallelize over Q and batch size  high parallelism
- Intra-Tile:  no extra access to HBM from O
- Outer loop: Q
- Inner loop: K V
- Outer loop
- Inner loop

## Slide 21: FlashAttention -2

- Images: 1; Tables: 0

### Extracted Shape Text
- FlashAttention -2
- Inter-Tile: parallelize over Q and batch size  high parallelism
- Intra-Tile:  no extra access to HBM from O
- Outer loop: Q
- Inner loop: K V
- One thread block
- for a subset of Q
- Iterate over K and V
- Accumulate to O

## Slide 22: FlashAttention -3

### Extracted Shape Text
- FlashAttention -3
- Two key ideas of FlashAttention-3
- Optimized for Hopper GPU
- 1, Warp Specialization: producer consumer model
- 2, Intra-warpgroup overlapping: overlap softmax and GEMM
- Issues of FlashAttention-2
- Serial Execution of GEMM, softmax, and HBM
- Low GPU utilizaton

## Slide 23: Producer and Consumer Model

- Images: 1; Tables: 0

### Extracted Shape Text
- Producer and Consumer Model
- One key idea of FlashAttention-3
- 1, Warp Specialization: producer consumer model
- Due to async memory access (DMA)

## Slide 24: Intra-warpgroup overlapping

- Images: 2; Tables: 0

### Extracted Shape Text
- Intra-warpgroup overlapping
- One key idea of FlashAttention-3
- Intra-warpgroup overlapping: overlap softmax and GEMM

## Slide 25: FlashAttention -3

- Images: 1; Tables: 0

### Extracted Shape Text
- FlashAttention -3
- Real Mapping of FlashAttention-3
- Epilogue is softmax

## Slide 26: FlashAttention -4

### Extracted Shape Text
- FlashAttention -4
- Two key ideas of FlashAttention-4
- Goal: Optimized for Blackwell GPU
- 1, Deeper Warp Specialization
- Issues of FlashAttention-2
- Unaware of Blackwell GPU

## Slide 27: 算子融合-PyTorch版Attention

- Images: 1; Tables: 0

### Extracted Shape Text
- 算子融合-PyTorch版Attention

### Notes
- 这里只有在第三步是实实在在的计算动作，其余步骤都是在为计算做准备工作。
- 在性能优化工作中，宏观角度通常是通过更好的算法、数学方法来减少总计算量。
- 而在微观角度上，则是尽可能的使处理器的计算单元“忙”起来，即增大计算单元的计算时间占总运行时间的比重。
- 27
