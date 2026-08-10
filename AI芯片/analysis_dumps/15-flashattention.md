# 15-flashattention43.pptx selected slides

## Slide 1: Computer Arch. & AI ChipLecture 15: Flash Attention
- Computer Arch. & AI ChipLecture 15: Flash Attention
- Prof. Zeke Wang
- Zhejiang University
- June 1 2026
Notes:
- 1

## Slide 2: Outline
- Outline
- Zero
- FlashAttention

## Slide 3: Networking
- Networking
- Storage
- Computing
- Model
- Training
- Compiling
- AI System: Four Components

## Slide 4: AI System: Storage
- AI System: Storage

## Slide 5: ZeRO: Zero Redundancy Optimizer
- ZeRO: Zero Redundancy Optimizer
- Key Idea:
- Each GPU stores a subset of optimizer states, rather than the whole states like data parallel.

## Slide 6: ZeRO: Zero Redundancy Optimizer
- ZeRO: Zero Redundancy Optimizer
- Benefit:
- Training a larger model.

## Slide 7: Overhead of ZeRO: More Communication
- Overhead of ZeRO: More Communication
- Typical PyTorch step:
- Forward:
- Backward:
- Optimizer:
- Overhead: more collectives

## Slide 8: Summary
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
- Batch Size Limitation of LLM Training
- Batch Size Limitation of LLM Training
- Llama: 4M token,
- Seq length: 4K,
- Batch size: 1K
- How to choose the parallel training strategy?
- When you have 1K NPU/GPU?
- When you have 10K NPU/GPU?

## Slide 10: Outline
- Outline
- Zero
- FlashAttention