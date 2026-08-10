# 14-parallel-training.pptx selected slides

## Slide 9: Networking
- Networking
- Storage
- Computing
- Model
- Training
- Compiling
- AI System: Four Components

## Slide 10: Neural Network Training: An Example
- Neural Network Training: An Example
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- 1, Start with randomly initialized weights
- 2, Iterate through your data a mini-batch of training data samples at a time:
- Forward pass
- Backward pass
- Weight update
- Linear
- Linear
- Linear
- Input

## Slide 11: An example: Network of 3 Linear Layers
- An example: Network of 3 Linear Layers
- Linear
- Linear
- Linear
- Input
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each layer:
- Input: vector
- Output: vector
- Learned parameters (weights): projection matrix
- Operations:
- 1, Multiply the input vector with the matrix
- 2, Apply a point-wise nonlinearity, say, ReLU

## Slide 12: Network of 3 Linear Layers: Forward Pass
- Network of 3 Linear Layers: Forward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each layer:
- Input: vector
- Output: vector
- Learned parameters (weights): projection matrix
- Operations:
- 1, Multiply the input vector with the matrix
- 2, Apply a point-wise nonlinearity, say, ReLU
- Linear
- Linear
- Linear

## Slide 13: Network of 3 Linear Layers: Forward Pass
- Network of 3 Linear Layers: Forward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each layer:
- Input: vector
- Output: vector
- Learned parameters (weights): projection matrix
- Operations:
- 1, Multiply the input vector with the matrix
- 2, Apply a point-wise nonlinearity, say, ReLU
- Linear
- Linear
- Linear

## Slide 14: Network of 3 Linear Layers: Forward Pass
- Network of 3 Linear Layers: Forward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each layer:
- Input: vector
- Output: vector
- Learned parameters (weights): projection matrix
- Operations:
- 1, Multiply the input vector with the matrix
- 2, Apply a point-wise nonlinearity, say, ReLU
- Linear
- Linear
- Linear
- Output

## Slide 15: Forward Pass: A Minibatch of 2 Samples
- Forward Pass: A Minibatch of 2 Samples
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Linear
- Linear
- Linear
- Input
- Output
- Matrix-vector multiplies
-  Matrix-matrix multiplies
- A minibatch of 1 sample

## Slide 16: Forward Pass: A Minibatch of 2 Samples
- Forward Pass: A Minibatch of 2 Samples
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Output
- Input
- Linear
- Linear
- Linear
- × =
- Weights
- Input Activations
- Output Activations
- W
- X
- Y
- Matrix-matrix multiplies

## Slide 17: Forward Pass: Compute Loss
- Forward Pass: Compute Loss
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Loss function:
- Produces a loss value that indicates how “wrong” the network was
- Compares the output to the ground truth for each sample
- Exact function math varies by task
- Goal of training: minimize the loss value
- Update network weights so the predicted output closely matches ground truth
- Input
- Linear Linear Linear
- Loss Value
- Loss
- Function
- Ground Truth
- Output

## Slide 18: Backward Pass
- Backward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Goal: compute the gradients to the layer weights
- Implementation: “back propagating” the loss through layers
- Each layer computes weight gradient, used to update the weights
- Each layer computes activation gradient, to be backpropagated to preceding layer
- Linear
- Linear
- Linear
- Loss Function
- Loss Value

## Slide 19: Backward Pass: Compute dW
- Backward Pass: Compute dW
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Linear
- Linear
- Linear
- Loss Function
- Loss Value
- × =
- dX
- dY
- W T
- ×
- =
- dW
- dY
- X T
- W
- X
- Y
- Compute the weight gradient dw
- dW: weight gradient (to update weights)
- dY: incoming activation gradient
- X: input activations (from fwd pass)
- Compute the activation gradient dx
- dX: output activation gradient
- to backpropagate to the preceding layer

## Slide 20: Weight Update
- Weight Update
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- =
- W
- W
- dW
- -
- lr×
- SGD
- Weight update (SGD)
- Input: Weight W, gradient dW
- Output: updated weight
- Operation:
- Increment each weight with the corresponding gradient value
- Weight update (Momentum)
- Input: Weight W, gradient dW
- States: 1 momenta (～model)
- Output: updated weight
- Operation:
- Update internal state with weight gradient, then update weights using internal state
- Weight update (Adam)
- States: 1 momenta, 1 variance
- (reading and updating momenta/variance/parameters)
- =
- v
- v
- dW
- -
- lr×
- =
- W
- W
- v
- +
- SGD with momentum
- µ×
Notes:
- Usually fp32 in reduced precision (FP16/BF16) training
- Optimizer may need 2-6x more memory than just the model
- 20

## Slide 21: One Iteration for a Layer
- One Iteration for a Layer
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- ×
- =
- W
- X
- Y
- 1, Forward Pass:
- ×
- =
- dW
- dY
- X T
- 2, Backward Pass:
- weight gradients
- × =
- dX
- dY
- W T
- 2, Backward Pass:
- activation gradients
- 3, Weight update:
- + … =
- W
- W
- dW
- +
- One iteration:
- Backward pass:
- Its compute is ~2x of forward
- requires activations computed during the fwd pass
- Read After Write (RAW) Dependency Regarding the Model w

## Slide 22: Outline
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline
- Intra-layer
- Communication Pattern Review
- Summary

## Slide 23: Why Distributed Training?
- Why Distributed Training?
- Challenge from Model Side: Larger models
- Language models (GPT-3): 175B parameters
- Recommender models: largest ones are reaching O(1B) parameters
- Vision models: deeper and wider Resnets and ResNeXTs
- Challenge from Dataset Side: Larger datasets
- Recommender data (user behavior): terabytes to petabytes
- Image data: 1B Instagram dataset, JFT (300M images)
- Challenge from System Side:
- The memory size of a single accelerator, e.g., GPU, is 80GB.

## Slide 24: Why GPU memory size is 80GB?
- Why GPU memory size is 80GB?
Notes:
- 内存的速度跟容量只能要一个。。。
- 24

## Slide 25: NVIDIA A100 Block Diagram
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
- 25

## Slide 26: Why Distributed Training?
- Why Distributed Training?
- Challenge from Model Side: Larger models
- Language models: in the past 2 years grew from 340M (BERT-large) to 175B (GPT-3) parameters
- Recommender models: largest ones are reaching O(1B) parameters
- Vision models: deeper and wider Resnets and ResNeXTs
- Challenge from Dataset Side: Larger datasets
- Recommender data (user behavior): terabytes to petabytes
- Image data: 1B Instagram dataset, JFT (300M images)
- Challenge from System Side:
- The memory size of a single accelerator, e.g., GPU, is 40GB.
- Solution: scale out computing

## Slide 27: Outline
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline Parallelism
- Tensor Parallelism
- Communication Pattern Review
- Summary

## Slide 28: Parallelism Taxonomy
- Parallelism Taxonomy
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Parallel Training
- Data Parallel
- Model Parallel
- Intra Layer/
- Tensor
- Inter Layer/
- Pipeline

## Slide 29: Data Parallel Training
- Data Parallel Training
- Each worker:
- Model: has a copy of the entire neural network model
- Dataset: responsible for compute of a portion of data (training minibatch)
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]

## Slide 30: Data Parallel: Forward Pass
- Data Parallel: Forward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- W
- X
- Y
- ×
- =
- ×
- =
- ×
- =
- ×
- =
- Worker 0:
- Worker 1:
- Worker 2:
- Worker 3:
- Forward pass:
- Computes output activations for its portion of minibatch
- No communication is needed
- X : input activations
- W : model
- Y : output activations
- Whole Model
- Partial dataset

## Slide 31: Data Parallel: Backward Pass
- Data Parallel: Backward Pass
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- X : input activations
- W : model
- Y : output activations
- dW1
- X T
- dY
- ×
- =
- Worker 0:
- Worker 1:
- Worker 2:
- Worker 3:
- ×
- =
- ×
- =
- ×
- =
- Backward pass:
- Computes activation gradients for its portion of minibatch
- Computes contribution to the weight gradient based on its portion of minibatch
- All workers’ contributions must be summed before weight update
- dW2
- dW3
- dW4

## Slide 32: Data Parallel Training: Weight Update
- Data Parallel Training: Weight Update
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Weight update:
- 1, Each of N workers accumulates gradients:
- Summing 1/N gradients collected from (N – 1) peers
- 2, Each worker updates its model:
- Each worker updates its copy of the model with combined gradients from all 4 workers
- Worker a
- Worker b
- Worker c
- Worker d
- (a+b+c+d)/4

## Slide 33: Networking
- Networking
- Storage
- Computing
- Model
- Training
- Compiling
- AI System: Four Components

## Slide 34: Kernel Stack
- Kernel Stack
- TCP/UDP
- Userspace
- TCP/UDP
- On-NIC Stack
- RDMA
- Programmed by Unix Socket
- Programmed by DPDK, running network stack in userspace program
- RDMA engine or TCP offload engine, usually programmed by IB Verbs
- Scale Out
- Network
- Scale Up
- Network
- 100us
- 10Gbps
- 3us
- 400Gbps
- 10us
- 100Gbps
- NCCL
- Collective primitive
- eBPF
- In-network computing
- PCIe
- 1us
- 512Gbps
- NVLink
- 1us
- 900GBps
- PCI
- 2us
- 4Gbps
- Differential Signaling
- Serialization/Deserialization
- CXL
- CXL based on PCIe, can direct LD/ST remote device memory, even can cross Node by CXL Switch
- Serial Bus, endpoint to endpoint transfer, provide up to 32Gbit/s serial data rate per lane
- Transaction Layer
- Network
- Layer
- IP/ARP/ICMP
- MAC/CSMA
- Data Link Layer
- Application Layer
- Parallels Bus, transfer 64 bit data in a clock cycle, bandwidth limited by frequent (33MHZ)
- Process on CPU
- Process on NIC
- OffloadedNCCL
- AI System: Network

## Slide 35: AllReduce Implementation Choices
- AllReduce Implementation Choices
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- “Ring” AllReduce (Baidu)
- For any topology that contains a 1D torus (ring)
- Each worker communicates with 2 neighbors
- 2(N – 1) steps, worker sends/receives 1/N of all bytes
- Each step requires a synchronization -> 2(N – 1) syncs total
- Each worker needs CPU and GPU cycles to do ring AllReduce

## Slide 36: “Ring” AllReduce: Initial States
- “Ring” AllReduce: Initial States
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0
- c0
- d0
- GPU1
- a1
- b1
- c1
- d1
- GPU2
- a2
- b2
- c2
- d2
- GPU3
- a3
- b3
- c3
- d3

## Slide 37: “Ring” AllReduce: Results
- “Ring” AllReduce: Results
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU1
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU2
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3

## Slide 38: “Ring” AllReduce
- “Ring” AllReduce
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- “Ring” AllReduce (Baidu) has two stages:
- 1, Reduce_scatter: N-1 rounds, M/N data per round
- 2, Allgather: N-1 rounds, M/N data per round
- N: number of GPUs (4), M: data size
- GPU0
- GPU3
- GPU1
- GPU2

## Slide 39: “Ring” AllReduce: Initial States
- “Ring” AllReduce: Initial States
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0
- c0
- d0
- GPU1
- a1
- b1
- c1
- d1
- GPU2
- a2
- b2
- c2
- d2
- GPU3
- a3
- b3
- c3
- d3
- Partitioning of an array into N=4 chunks

## Slide 40: “Ring” AllReduce: Reduce_scatter iter. 0
- “Ring” AllReduce: Reduce_scatter iter. 0
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0
- c0
- d0
- GPU1
- a1
- b1
- c1
- d1
- GPU2
- a2
- b2
- c2
- d2
- GPU3
- a3
- b3
- c3
- d3

## Slide 41: “Ring” AllReduce: Reduce_scatter iter. 1
- “Ring” AllReduce: Reduce_scatter iter. 1
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0
- c0
- d0+d3
- GPU1
- a0+a1
- b1
- c1
- d1
- GPU2
- a2
- b1+b2
- c2
- d2
- GPU3
- a3
- b3
- c2+c3
- d3

## Slide 42: “Ring” AllReduce: Reduce_scatter iter. 2
- “Ring” AllReduce: Reduce_scatter iter. 2
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0
- c0+c2+c3
- d0+d3
- GPU1
- a0+a1
- b1
- c1
- d0+d1+d3
- GPU2
- a0+a1+a2
- b1+b2
- c2
- d2
- GPU3
- a3
- b1+b2+b3
- c2+c3
- d3

## Slide 43: “Ring” AllReduce: Reduce_scatter iter. 3
- “Ring” AllReduce: Reduce_scatter iter. 3
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0+b1+b2+b3
- c0+c2+c3
- d0+d3
- GPU1
- a0+a1
- b1
- c0+c1+c2+c3
- d0+d1+d3
- GPU2
- a0+a1+a2
- b1+b2
- c2
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b1+b2+b3
- c2+c3
- d3

## Slide 44: “Ring” AllReduce: Allgather iter. 0
- “Ring” AllReduce: Allgather iter. 0
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0
- b0+b1+b2+b3
- c0+c2+c3
- d0+d3
- GPU1
- a0+a1
- b1
- c0+c1+c2+c3
- d0+d1+d3
- GPU2
- a0+a1+a2
- b1+b2
- c2
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b1+b2+b3
- c2+c3
- d3

## Slide 45: “Ring” AllReduce: Allgather iter. 1
- “Ring” AllReduce: Allgather iter. 1
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c2+c3
- d0+d3
- GPU1
- a0+a1
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d3
- GPU2
- a0+a1+a2
- b1+b2
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b1+b2+b3
- c2+c3
- d0+d1+d2+d3

## Slide 46: “Ring” AllReduce: Allgather iter. 2
- “Ring” AllReduce: Allgather iter. 2
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c2+c3
- d0+d1+d2+d3
- GPU1
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d3
- GPU2
- a0+a1+a2
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3

## Slide 47: “Ring” AllReduce: Allgather iter. 3
- “Ring” AllReduce: Allgather iter. 3
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU1
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU2
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3

## Slide 48: “Ring” AllReduce: Results
- “Ring” AllReduce: Results
- [https://zhuanlan.zhihu.com/p/69797852, 2020]
- GPU0
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU1
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU2
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3
- GPU3
- a0+a1+a2+a3
- b0+b1+b2+b3
- c0+c1+c2+c3
- d0+d1+d2+d3

## Slide 49: AllReduce Implementation Choices
- AllReduce Implementation Choices
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- “Ring” AllReduce (Baidu)
- For any topology that contains a 1D torus (ring)
- Each worker communicates with 2 neighbors
- 2(N – 1) steps, worker sends/receives 1/N of all bytes
- Each step requires a synchronization -> 2(N – 1) syncs total
- “In-switch” AllReduce
- Each worker communicates with the switch
- Only one step, a worker sends/receives N of all bytes
- All workers work in a lock step.

## Slide 50: Data Parallel: Challenges
- Data Parallel: Challenges
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Strong scaling (increase the number of workers, keep minibatch size constant)
- Certain layers require minimum minibatch sizes to properly operate
- Example: batch normalization (BN) generally requires 16+ samples
- Maybe lower GPU utilization
- Weak scaling (increase the number of workers, increase minibatch size)
- Training networks with large minibatches requires hyper-parameter adjustment
- Learning rate schedule, BN decay, …
- Example: R50 (SGD up to bs=16K, LARS above 16K, …)
- Often increase the amount of work required to reach the same model accuracy

## Slide 51: Workload Increasing with Batch Size
- Workload Increasing with Batch Size
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Epochs to reach the same model accuracy (from various submissions to MLPerf v0.7)
- Epoch = 1 processing pass through entire dataset

## Slide 52: Workload Increasing with Batch Size
- Workload Increasing with Batch Size
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Epochs to reach the same model accuracy (from various submissions to MLPerf v0.7)
- Epoch = 1 processing pass through entire dataset

## Slide 53: Outline
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline
- Intra-layer
- Communication Pattern Review
- Summary

## Slide 54: Parallelism Taxonomy
- Parallelism Taxonomy
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Parallel Training
- Data Parallel
- Model Parallel
- Intra Layer
- Inter Layer/
- Pipeline

## Slide 55: Model Parallel Training
- Model Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 1
- Worker 2
- Intra-layer Parallel
- (aka Tensor Parallel):
- A worker is responsible for its portion of each layer
- Worker 0
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 0
- Worker 1
- Worker 2
- Inter-layer Parallel (aka Pipeline Parallel):
- A worker is responsible for its portion of the layers

## Slide 56: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 57: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 58: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 59: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 60: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 61: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time

## Slide 62: Pipeline Parallel Training
- Pipeline Parallel Training
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |
- Forward
- Backward
- Loss
- Time
- Idle bubbles:
- 67%: 12/18 step-slots
- For N workers:
- (N – 1)/N idle slots
Notes:
- N: number of workers, devices.
- 62

## Slide 63: Pipeline Parallel Training: GPipe
- Pipeline Parallel Training: GPipe
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Forward
- Backward
- Loss
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  |  |
- 2 subminibatches
- 2x more steps
- Each step is ½ compute
- Key Idea: Subminibatches
- Idle bubbles: 50%
- 12/24 steps-slots

## Slide 64: Pipeline Parallel Training: GPipe
- Pipeline Parallel Training: GPipe
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- N workers, K subminibatches:
- 2(N + K – 1) steps for fwd/bwd
- Total step-slots: 2N(N + K – 1)
- Idle step-slots: 2N(N – 1)
- Fraction of idle slots: (N – 1)/(N + K – 1)
- Forward
- Backward
- Loss
- TABLE:
  | Layer 1

Layer 2 | Worker | 0 |  |  |  |  |  |  |  |  |  |  |
  | Layer 3

Layer 4 | Worker | 1 |  |  |  |  |  |  |  |  |  |  |
  | Layer 5 | Worker | 2 |  |  |  |  |  |  |  |  |  |  |
- As N grows:
- K = N → 50% idle slots
- K = 4N → 20% idle slots

## Slide 65: Pipeline Parallel: Communication
- Pipeline Parallel: Communication
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- A worker communicates with its 2 neighbors
- 1D mesh topology
- 1D torus when interleaving layers
- Communication in each step of the fwd and bwd pass
- Activations in fwd, activation gradients in bwd
- Overlap communication with computation
- Very hard

## Slide 66: Pipeline Parallel: Challenges
- Pipeline Parallel: Challenges
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Load balancing workload across workers is difficult
- Different layers of a network can take different amounts of time
- Leads to even busy slots for other workers idling for portions of time
- Lots of computation to hide communication
- Idle slots reduce scaling efficiency
- Many subminibatches help with this, but run into the same problems as strong-scaling of data-parallel.

## Slide 67: Outline
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline
- Tensor Parallelism
- Communication Pattern Review
- Summary

## Slide 68: Tensor Parallel
- Tensor Parallel
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Partition a given layer’s weights among the workers
- Addresses some of the Pipeline Parallel challenges
- Idle slots, load imbalance
- Layer 1
- Layer 2
- Layer 3
- Layer 4
- Layer 5
- Worker 0
- Worker 1
- Worker 2
- ×
- ×
- Row-wise partitioning:
- Column-wise partitioning:
- Two variants:
- Row-wise partitioning
- Column-wise partitioning

## Slide 69: Row-wise Partitioning: Allgather between Layers
- Row-wise Partitioning: Allgather between Layers
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each worker:
- W: Has a portion of weight rows
- X: All of input activations X
- Y: Computes a portion of output activations
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- Fwd communication: Allgather
- Layer K fwd
- Layer (K + 1) fwd
- Worker 0
- Worker 1
- Worker 2
- X
- W
- Y

## Slide 70: Column-wise Partitioning: ReduceScatter between Layers
- Column-wise Partitioning: ReduceScatter between Layers
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Each worker:
- W: Has a portion of weight rows
- X: All of input activations X
- Y: Computes a portion of output activations
- Fwd communication: ReduceScatter
- × =
- × =
- TABLE:
  |  |  |  |
- × =
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- Layer K fwd
- Layer (K + 1) fwd
- Worker 0
- Worker 1
- Worker 2
- +
- +
- +
- X
- W
- Y
Notes:
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 70

## Slide 71: Reducing Synchronization By Alternating Partitioning
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |  |  |
- × =
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- Layer (K + 1) fwd
- TABLE:
  |  |
  |  |
  |  |
- Row-wise partitioning Column-wise partitioning
- Note: no communication is needed for two matrices
- Worker i produces output, which is its input for the next layer
- W
- W
Notes:
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 71

## Slide 72: Reducing Synchronization By Alternating Partitioning
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |  |  |
- × =
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- Layer (K + 1) fwd
- TABLE:
  |  |
  |  |
  |  |
- Row-wise partitioning Column-wise partitioning
- Note: no communication is needed for two matrices
- Worker i produces output, which is its input for the next layer
- W
- W
- +Next two?
Notes:
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 72

## Slide 73: Reducing Synchronization By Alternating Partitioning
- Reducing Synchronization By Alternating Partitioning
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- Layer K fwd
- Worker 0
- Worker 1
- Worker 2
- TABLE:
  |  |
  |  |
  |  |
- × =
- × =
- TABLE:
  |  |  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |  |  |
- TABLE:
  |  |  |  |
- Communication: Allreduce
- Layer (K + 1) fwd
- +
- +
- +
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- TABLE:
  |  |
  |  |
  |  |
- × =
- Layer (K + 2) fwd
- Row-wise partitioning Column-wise partitioning Row-wise partitioning
- TABLE:
  |  |
  |  |
  |  |
Notes:
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 73

## Slide 74: Intra-Layer Parallel: Communication
- Intra-Layer Parallel: Communication
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Row-wise in forward becomes Col-wise in backward
- Col-wise in forward becomes Row-wise in backward
- Row-wise:
- Fwd: allgather
- Bwd: reduce_scatter
- Col-wise:
- Fwd: reduce_scatter
- Bwd: allgather
- When row- and col- are alternated:
- Allreduce every two layers, in fwd and bwd
- Halves the synchronizations compared to not alternating
Notes:
- Fwd
- communication:
- Reduce_scatter
- : each worker needs partial
- activations at
- next layer
- 74

## Slide 75: Tensor Parallelism for Transformer Block
- Tensor Parallelism for Transformer Block
- [Micikevicius, Fundamentals of Scaling Out DL Training, 2020]
- Tensor Parallelism:
- Attention: column-wise + row-wise.
- MLP: column-wise + row-wise.
- Column-wise
- Column-wise
- Row-wise
- Row-wise

## Slide 76: Outline
- Outline
- Why Distributed Training？
- Data Parallelism
- Model Parallelism
- Pipeline
- Intra-layer
- Communication Pattern Review
- Summary

## Slide 77: Communication Pattern Summary
- Communication Pattern Summary
- Data Parallel:
- Allreduce of weights
- Can be overlapped with computation
- Pipeline Parallel:
- Point-wise communication of activations and activation gradients
- Hard to overlap with computation
- Hard to load-balance
- Tensor Parallel:
- Allgather, Reduce_scatter of activations and activation gradients
- Allreduce if row-wise and col-wise partitioning is alternated
- Hard to overlap with computation

## Slide 78: Memory Size for a Huge Model
- Memory Size for a Huge Model
- Memory Size Needed when Training GPT3-175B
- Optimizer: 3259 GB
- Parameters
- Gradients
- Optimizer states
- Activation (without checkpoint): 360 GB （seq=1024，bsz=8）
- Activation (with checkpoint): 3.75 GB （seq=1024，bsz=8， each block ）

## Slide 79: 基于transformer的模型的显存占用
- 基于transformer的模型的显存占用
- Transformer layer
- param : 12 * hid * hid
- activation : 20 * bsz * seq * hid + n_h * bsz * seq * seq （QK乘积）
- Embedding
- param : voc * hid
- activation : bsz * seq * hid
- 混合精度训练： FP32的参数，梯度和优化器参数（动量，方差） 4 * 4(byte)
- FP16的参数和梯度 2 * 2(byte)
- activation都是FP16的

## Slide 80: Networking
- Networking
- Storage
- Computing
- Model
- Training
- Compiling
- AI System: Four Components

## Slide 81: AI System: Storage
- AI System: Storage

## Slide 82: ZeRO: Zero Redundancy Optimizer
- ZeRO: Zero Redundancy Optimizer
- Key Idea:
- Each GPU stores a subset of optimizer states, rather than the whole states like data parallel.

## Slide 83: ZeRO: Zero Redundancy Optimizer
- ZeRO: Zero Redundancy Optimizer
- Benefit:
- Training a larger model.

## Slide 84: Overhead of ZeRO: More Communication
- Overhead of ZeRO: More Communication
- Typical PyTorch step:
- Forward:
- Backward:
- Optimizer:
- Overhead: more collectives

## Slide 85: Summary
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

## Slide 86: Batch Size Limitation of LLM Training
- Batch Size Limitation of LLM Training
- Batch Size Limitation of LLM Training
- Llama: 4M token,
- Seq length: 4K,
- Batch size: 1K
- How to choose the parallel training strategy?
- When you have 1K NPU/GPU?
- When you have 10K NPU/GPU?