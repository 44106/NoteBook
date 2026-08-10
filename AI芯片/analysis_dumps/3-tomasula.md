# 3-tomasula.pptx selected slides

## Slide 6: Out-of-Order Execution(Dynamic Instruction Scheduling)
- Out-of-Order Execution(Dynamic Instruction Scheduling)
Notes:
- 6

## Slide 7: Where Are We?
- Where Are We?

## Slide 8: An In-order Pipeline with only ROB
- An In-order Pipeline with only ROB
- Dispatch: Act of sending an instruction to a functional unit
- Renaming with ROB
- eliminates stalls due to false dependences
- Problem: A true data dependence stalls dispatch of younger instructions into functional (execution) units
- F
- D
- E
- R
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Cache miss
- W
- In order dispatch
- In order
- Out of order
Notes:
- I
- n-order issue, in-order dispaatch, out-of-order completion, in-order retirement.
- 8

## Slide 9: In order dispatch + precise exceptions:
- In order dispatch + precise exceptions:
- IO: 16
- Issue of In-order Dispatch
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R1  R6, R7
- IMUL R5  R6, R8
- ADD R7  R3, R5
- F
- D
- W
- E
- E
- E
- E
- R
- F
- D
- E
- R
- W
- STALL
- F
- D
- E
- R
- W
- STALL
- F
- D
- E
- R
- W
- E
- E
- E
- E
- F
- D
- E
- R
- W
- STALL
- IMUL: 4 cycles, ADD： 1 cycle
Notes:
- 假设有forward
- ，
- IMUL 4 cycles, ADD 1 cycle.
- 9

## Slide 10: Can We Do Better?
- Can We Do Better?

## Slide 11: How Can We Do Better?
- How Can We Do Better?
- What do the following two pieces of code have in common (with respect to execution in the previous design)?
- Answer: First ADD stalls the whole pipeline!
- ADD cannot dispatch because its source register R3 is unavailable
- Later independent instructions cannot get executed
- How are the above code portions different?
- Answer: Load latency is variable (unknown until runtime)
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9
- LD R3  R1 (0)
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9

## Slide 12: Preventing Dispatch Stalls
- Preventing Dispatch Stalls
- Problem: in-order dispatch (scheduling, or execution)
- Solution: out-of-order dispatch (scheduling, or execution)
- Goal of out-of-order dispatch:
- Like Dataflow, “fire” an instruction only when its inputs are ready
- LD R3  R1 (0)
- ADD R3  R3, R1
- ADD R4  R6, R7
- IMUL R5  R6, R8
- ADD R7  R9, R9
- The insn “ADD R3…” will not impede insns “ADD R4…, IMUL R5…, ADD R7…”.

## Slide 13: Reservation Station: Out-of-order Execution
- Reservation Station: Out-of-order Execution
- Key idea of reservation station: Move the dependent instructions out of the way of independent ones (s.t. independent ones can execute)
- Rest areas for dependent instructions: Reservation Stations
- Function of Reservation Station:
- Monitors the source “values” of each instruction in the resting area
- “Fires” (i.e. dispatch) the instruction, when all source “values” of an instruction are available
- Instructions dispatched in dataflow (not control-flow) order
- Benefit of Reservation Station:
- Latency tolerance: Allows independent instructions to execute and complete in the presence of a long-latency operation
Notes:
- O
- ne road with multiple ways…
- 高速路上的
- 13

## Slide 14: In order dispatch + precise exceptions:
- In order dispatch + precise exceptions:
- Out-of-order dispatch + precise exceptions:
- IO: 16 vs. OoO:12 cycles
- In-order vs. Out-of-order Dispatch
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R1  R6, R7
- IMUL R5  R6, R8
- ADD R7  R3, R5
- F
- D
- W
- E
- E
- E
- E
- R
- F
- D
- E
- R
- W
- STALL
- F
- D
- E
- R
- W
- STALL
- F
- D
- E
- R
- W
- E
- E
- E
- E
- F
- D
- E
- R
- W
- STALL
- F
- D
- W
- E
- E
- E
- E
- R
- F
- D
- E
- E
- E
- E
- R
- W
- F
- D
- E
- R
- W
- WAIT
- F
- D
- E
- R
- W
- WAIT
- F
- D
- E
- R
- W
- IMUL R3  R1, R2
- ADD R3  R3, R1
- ADD R1  R6, R7
- IMUL R5  R6, R8
- ADD R7  R3, R5
- IMUL: 4 cycles, ADD： 1 cycle
Notes:
- 假设有forward
- ，
- IMUL 4 cycles, ADD 1 cycle.
- 14

## Slide 15: Tomasulo’s Algorithm for OoO Execution
- Tomasulo’s Algorithm for OoO Execution
- OoO with register renaming invented by Robert Tomasulo
- Used in IBM 360/91 Floating Point Units
- Read: Tomasulo, “An Efficient Algorithm for Exploiting Multiple Arithmetic Units,” IBM Journal of R&D, Jan. 1967.
- OoO variants are used in most high-performance processors
- Initially in Intel Pentium Pro, AMD K5
- Alpha 21264, MIPS R10000, IBM POWER5, IBM z196, Oracle UltraSPARC T4, ARM Cortex A15, Apple M1, …
Notes:
- 360 is not commercially suceesful, without precious exception
- 15

## Slide 16: Two Humps in a Modern Pipeline
- Two Humps in a Modern Pipeline
- Hump 1: Reservation stations (enabling in-order issue and out-of-order dispatch/execution)
- Hump 2: Reorder buffer (enabling OoO completion, in-order commitment)
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- E
- O
- R
- D
- E
- R
- Reservation Station
- TAG and VALUE Broadcast Bus
- In order issue
- OoO dispatch
- In order commitment
- OoO execution

## Slide 17: Two Humps in a Modern Pipeline
- Two Humps in a Modern Pipeline
- Hump 1: Reservation stations (scheduling window)
- Hump 2: Reordering (reorder buffer, aka instruction window or active window)
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- E
- O
- R
- D
- E
- R
- S
- C
- H
- E
- D
- U
- L
- E
- TAG and VALUE Broadcast Bus
- in order
- out of order
- in order
- Photo credit: http://true-wildlife.blogspot.ch/2010/10/bactrian-camel.html

## Slide 18: Enabling OoO Execution
- Enabling OoO Execution
- 1. Need to link the consumer of a value to the producer
- Register renaming: Associate a “tag” with each data value
- 2. Need to buffer instructions until they are ready to execute
- Insert instruction into reservation stations after renaming
- 3. Instructions need to keep track of readiness of source values
- Broadcast the “tag” when the value is produced
- Instructions compare their “source tags” to the broadcast tag  if match, source value becomes ready
- 4. When all source values of an instruction are ready, need to dispatch the instruction to its functional unit (FU)
- Instruction wakes up if all sources are ready
- If multiple instructions are awake, need to select one per FU

## Slide 19: General Organization of an OOO Processor
- General Organization of an OOO Processor
- Smith and Sohi, “The Microarchitecture of Superscalar Processors,” Proc. IEEE, Dec. 1995.
Notes:
- I
- nstruction buffer: reservation station.
- 19

## Slide 20: Tomasulo’s Machine: IBM 360/91
- Tomasulo’s Machine: IBM 360/91
- FP FU
- FP FU
- from memory
- load
- buffers
- from instruction unit
- FP registers
- store buffers
- to memory
- operation bus
- reservation
- stations
- Common data bus
Notes:
- 20

## Slide 21: Recall Once More: Register Renaming
- Recall Once More: Register Renaming
- Output and anti dependences are not true dependences
- WHY? The same register refers to values that have nothing to do with each other
- They exist because not enough register ID’s (i.e. names) in the ISA
- The dest. register ID is renamed to the reservation station entry
- Destination register ID  RS entry ID
- After renaming, RS entry ID used to refer to the register for the following instructions before updating the register.
- This eliminates anti- and output- dependences
- Approximates the performance effect of a large number of registers even though ISA has a small number.
Notes:
- D
- estination id
- 21

## Slide 22: Register Rename Table (register alias table)
- Register Rename Table (register alias table)
- Tomasulo’s Algorithm: Three Components
- R0
- R1
- R2
- R3
- tag
- value
- valid?
- R4
- R5
- R6
- R7
- R8
- R9
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- Reservation Station
- rs.tag
- IF
- ID
- E
- W
- RS
- Common Data Bus:
- Broadcasts the tag and result to all FUs
- Updates the RF using the tag and result
Notes:
- RRT
- :
- T
- ag: reservation station entry ID
- Valid: 1 means the register is readable, 0 means the new value exists in a reservation station entry.
- Value: value in RF
- RS
- V: valid bit of this
- operand
- Tag: RS ID
- Value: value of this operand
- 22

## Slide 23: Tomasulo’s Algorithm
- Tomasulo’s Algorithm
- ID: If reservation station entry available before renaming dest. register
- Occupy a RS entry for the instruction
- For each source register in the RS entry: if the valid bit of source register in RF is 1, RS.source.v = 1 and RS.source.value=source register; else RS.source.v = 0 and RS.source.tag = source register.tag.
- For dest. register in RF: Rename to the tag of the corresponding RS entry, set the valid bit to 0.
- Else stall
- RS: While in reservation station, each instruction:
- Update: Watches common data bus (CDB) for tag of its sources. When tag seen, grab value for the source and keep it in the reservation station (.v = 1).
- Issue: When both operands available, instruction ready to be dispatched to FU
- EXE: Execute the instruction in FU, produce its broadcast tag and value
- WB: After instruction finishes in the Functional Unit
- a, Arbitrate for CDB
- b, Put broadcast tag and its broadcast value onto CDB (tag broadcast)
- c, Update register file connected to the CDB
- If the tag in the RF matches the broadcast tag, write broadcast value into register (and set valid bit)
- d, Update reservation station connected to the CDB
- If the broadcast tag matches the tag of any source in a RS entry, write the broadcast value to the source and set the valid bit of the source.
Notes:
- d, Reclaim rename tag
- no valid copy of tag in system!
- 23

## Slide 24: Our First OoO Machine Simulation
- Our First OoO Machine Simulation
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 3 |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 5 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x |  |  |  |  |  |  |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- Tag
- Value
- Tag
- Value
- RS for ADD Unit
- RS for MUL Unit
- Register Rename Table
- Program We Will Simulate
- ADD and MUL Execution Units
- have separate common data buses
- Initially:
- RS’s are all Invalid (Empty)
- All Registers are Valid
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 24

## Slide 25: Cycle 0
- Cycle 0
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 3 |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 5 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x |  |  |  |  |  |  |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 25

## Slide 26: Cycle 1
- Cycle 1
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 3 |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 5 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x |  |  |  |  |  |  |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 26

## Slide 27: Cycle 2
- Cycle 2
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 3 |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 5 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x |  |  |  |  |  |  |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- D
- 2
- F
- F
- 1
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- Cycle
- 1
- 2
- Step 2: Access the Register Alias Table
- Step 3: Put source registers into reservation station x.
- 1
- 1
- ~
- ~
- Step 4: Rename destination register R3  x
- 0
- x
- R3 is now renamed to x.
- Its new value will produced by the reservation station
- that is identified by tag x.
- MUL in RS x is ready to execute in the next cycle!
- Step 1: Check if reservation station available. Yes: x
- MUL gets decoded and allocated into RS x
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 27

## Slide 28: Cycle 3
- Cycle 3
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 5 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a |  |  |  |  |  |  |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- Check readiness (Both sources ready?)  Wakeup
- Ready  Dispatch the instruction to the MUL unit
- 6
- Cycles
- 0
- x
- 4
- 1
- ~
- 0
- a
- Same Steps 1-4 for ADD… Rename R5  a
- ADD in RS a cannot execute in the next cycle: one source is not valid
- 1. MUL in RS x starts executing
- 2. ADD gets decoded and allocated into RS a
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 28

## Slide 29: Cycle 4
- Cycle 4
- +
- ∗
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b |  |  |  |  |  |  |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | a |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 7 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- ADD in RS a waits because one source is not valid.
- 2
- 1
- ~
- 6
- 1
- ~
- Rename R7  b
- 0
- b
- ADD in RS b is ready to execute in the next cycle!
- It will be executed out of order in the next cycle.
Notes:
- 29

## Slide 30: Cycle 5
- Cycle 5
- +
- ∗
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | a |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 10 |
  | R11 | 1 |  | 11 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c |  |  |  |  |  |  |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- 8
- 1
- ~
- 9
- 1
- ~
- 4
- Cycles
- 0
- c
- ADD in RS c is ready to execute in the next cycle!
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 30

## Slide 31: Cycle 6
- Cycle 6
- +
- ∗
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | a |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 1 |  | 11 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y |  |  |  |  |  |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- 0
- y
- 0
- b
- 0
- c
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 31

## Slide 32: Cycle 7
- Cycle 7
- +
- ∗
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | a |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d |  |  |  |  |  |  |
- 0
- a
- 0
- y
- 0
- d
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 0 | b |  | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- All 6 instructions are now decoded and renamed
- Note what happened to R5!
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 32

## Slide 33: Cycle 8 (First Slide)
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- Cycle 8 (First Slide)
- +
- ∗
- E6
- 8
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 0 | b |  | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- Broadcast MUL’s tag (x)
- Check tag
- Check for invalidity
- 2
- MUL in RS x is done
- x
- Broadcast MUL’s result (2)
- 1
- x
- 1
- 2
- 2
- 2
- ADD in RS a is ready to execute in the next cycle!
Notes:
- 33

## Slide 34: Cycle 8 (Second Slide)
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- Cycle 8 (Second Slide)
- +
- ∗
- E6
- 8
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 0 | b |  | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- Broadcast ADD’s tag (b)
- Check tag
- Check for invalidity
- ADD in RS b is also done
- Broadcast ADD’s result (8)
- 1
- 1
- 8
- E4
- -
- 8
- b
- b
- 8
- 8
- MUL in RS y is still NOT ready to execute in the next cycle!
Notes:
- 34

## Slide 35: Cycle 8 (Third Slide)
- Cycle 8 (Third Slide)
- +
- ∗
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 | b | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 35

## Slide 36: Cycle 9
- Cycle 9
- +
- ∗
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- 17
- 1
- ~
- c
- 17
- 1
- 17
- Broadcast and Update
- MUL in RS y is ready to execute in the next cycle!
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 36

## Slide 37: Cycle 10
- Cycle 10
- +
- ∗
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 37

## Slide 38: Cycle 11
- Cycle 11
- +
- ∗
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 38

## Slide 39: Cycle 12
- Cycle 12
- +
- ∗
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 0 | a |  | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- a
- 6
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- 6
- 1
- ~
- Broadcast and Update
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 39

## Slide 40: Cycle 13
- Cycle 13
- +
- ∗
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 40

## Slide 41: Cycle 14
- Cycle 14
- +
- ∗
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 0 | y |  |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 41

## Slide 42: Cycle 15
- Cycle 15
- +
- ∗
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 0 | y |  |
- 1
- 136
- 136
- 1
- ~
- y
- 136
- Broadcast and Update
- ADD in RS d is ready to execute in the next cycle!
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 42

## Slide 43: Cycle 16
- Cycle 16
- +
- ∗
- 16
- W
- E1
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 1 | ~ | 136 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 1 |  | 136 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 43

## Slide 44: Cycle 17
- Cycle 17
- +
- ∗
- 17
- E2
- 16
- W
- E1
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 1 |  | 136 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 1 | ~ | 136 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 44

## Slide 45: Cycle 18
- Cycle 18
- +
- ∗
- 18
- E3
- 17
- E2
- 16
- W
- E1
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 1 |  | 136 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 1 | ~ | 136 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 45

## Slide 46: Cycle 19
- Cycle 19
- +
- ∗
- 19
- E4
- 18
- E3
- 17
- E2
- 16
- W
- E1
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 0 | d |  |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 1 |  | 136 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 1 | ~ | 136 |
- d
- 142
- 1
- 142
- Broadcast and Update
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 46

## Slide 47: Cycle 20
- Cycle 20
- +
- ∗
- 20
- W
- 19
- E4
- 18
- E3
- 17
- E2
- 16
- W
- E1
- 15
- E6
- -
- 14
- E5
- -
- 13
- W
- E4
- -
- 12
- E4
- E3
- -
- 11
- E3
- E2
- -
- 10
- E2
- W
- E1
- -
- W
- 9
- E1
- W
- E4
- -
- -
- E6
- 8
- -
- E4
- E3
- -
- -
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 1 | ~ | 8 | 1 | ~ | 17 |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 1 |  | 2 |
  | R4 | 1 |  | 4 |
  | R5 | 1 |  | 142 |
  | R6 | 1 |  | 6 |
  | R7 | 1 |  | 8 |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 1 |  | 17 |
  | R11 | 1 |  | 136 |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 1 | ~ | 2 | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d | 1 | ~ | 6 | 1 | ~ | 136 |
- MUL: 6 cycles, ADD： 4 cycle
Notes:
- 47

## Slide 48: Tomasulo’s Algorithm
- Tomasulo’s Algorithm
- ID: If reservation station entry available before renaming dest. register
- Occupy a RS entry for the instruction
- For each source register in the RS entry: if the valid bit of source register in RF is 1, RS.source.v = 1 and RS.source.value=source register; else RS.source.v = 0 and RS.source.tag = source register.tag.
- For dest. register in RF: Rename to the tag of the corresponding RS entry, set the valid bit to 0.
- Else stall
- RS: While in reservation station, each instruction:
- Update: Watches common data bus (CDB) for tag of its sources. When tag seen, grab value for the source and keep it in the reservation station (.v = 1).
- Issue: When both operands available, instruction ready to be dispatched to FU
- EXE: Execute the instruction in FU, produce its broadcast tag and value
- WB: After instruction finishes in the Functional Unit
- a, Arbitrate for CDB
- b, Put broadcast tag and its broadcast value onto CDB (tag broadcast)
- c, Update register file connected to the CDB
- If the tag in the RF matches the broadcast tag, write broadcast value into register (and set valid bit)
- d, Update reservation station connected to the CDB
- If the broadcast tag matches the tag of any source in a RS entry, write the broadcast value to the source and set the valid bit of the source.
Notes:
- d, Reclaim rename tag
- no valid copy of tag in system!
- 48

## Slide 49: Some Questions
- Some Questions
- What can potentially become the critical path?
- Tag broadcast  value capture  instruction wake up
- How can you reduce the potential critical paths?
- Break down the critical path

## Slide 50: Dataflow Graph for Our Example
- Dataflow Graph for Our Example
- MUL R3  R1, R2
- ADD R5  R3, R4
- ADD R7  R2, R6
- ADD R10  R8, R9
- MUL R11  R7, R10
- ADD R5  R5, R11

## Slide 51: State of RAT and RS in Cycle 7
- State of RAT and RS in Cycle 7
- +
- ∗
- E5
- 7
- -
- E3
- E2
- -
- D
- E4
- 6
- -
- E2
- E1
- D
- F
- E3
- 5
- -
- E1
- D
- F
- E2
- 4
- -
- D
- F
- E1
- 3
- D
- F
- D
- 2
- F
- F
- 1
- Cycle
- TABLE:
  | MUL | R1, R2 |  | R3 |
  | ADD | R3, R4 |  | R5 |
  | ADD | R2, R6 |  | R7 |
  | ADD | R8, R9 |  | R10 |
  | MUL | R7, R10 |  | R11 |
  | ADD | R5, R11 |  | R5 |
- TABLE:
  | Register | Valid | Tag | Value |
  | R1 | 1 |  | 1 |
  | R2 | 1 |  | 2 |
  | R3 | 0 | x |  |
  | R4 | 1 |  | 4 |
  | R5 | 0 | a |  |
  | R6 | 1 |  | 6 |
  | R7 | 0 | b |  |
  | R8 | 1 |  | 8 |
  | R9 | 1 |  | 9 |
  | R10 | 0 | c |  |
  | R11 | 0 | y |  |
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | a | 0 | x |  | 1 | ~ | 4 |
  | b | 1 | ~ | 2 | 1 | ~ | 6 |
  | c | 1 | ~ | 8 | 1 | ~ | 9 |
  | d |  |  |  |  |  |  |
- 0
- a
- 0
- y
- 0
- d
- TABLE:
  |  | Source 1 |  |  | Source 2 |  |  |
  |  | V | Tag | Value | V | Tag | Value |
  | x | 1 | ~ | 1 | 1 | ~ | 2 |
  | y | 0 | b |  | 0 | c |  |
  | z |  |  |  |  |  |  |
  | t |  |  |  |  |  |  |
Notes:
- 51

## Slide 52: Corresponding Dataflow Graph (Reverse Engineered)
- Corresponding Dataflow Graph (Reverse Engineered)
- MUL R3  R1, R2
- ADD R5  R3, R4
- ADD R7  R2, R6
- ADD R10  R8, R9
- MUL R11  R7, R10
- ADD R5  R5, R11
- *
- R1
- R2
- +
- +
- R6
- R8
- R9
- +
- R4
- *
- +
- R5 (d)
- R11 (y)
- R10 (c)
- R5 (a)
- R3 (x)
- R7 (b)

## Slide 53: Summary of OOO Execution Concepts
- Summary of OOO Execution Concepts
- Register renaming eliminates false dependences, enables linking of producer to consumers
- Buffering in reservation stations enables the pipeline to move for independent instructions
- Tag broadcast enables communication (of readiness of produced value) between instructions
- Wakeup and select enables out-of-order dispatch

## Slide 54: For You: An Exercise, wo/ Precise Exceptions
- For You: An Exercise, wo/ Precise Exceptions
- Assume
- ADD (4 cycle execute), MUL (6 cycle execute)
- One adder and one multiplier
- How many cycles
- in an in-order-dispatch pipelined machine wo reorder buffer (no forwarding and full forwarding)?
- in an out-of-order dispatch pipelined machine wo reorder buffer (full forwarding)?
- MUL R3  R1, R3
- ADD R5  R3, R4
- ADD R7  R2, R6
- ADD R10  R8, R9
- MUL R11  R5, R6
- ADD R5  R5, R3
- F
- D
- E
- W
Notes:
- 任务。。。
- 54

## Slide 55: Out-of-Order Execution with Precise Exceptions
- Out-of-Order Execution with Precise Exceptions
- Hump 1: Reservation stations (scheduling window)
- Hump 2: Reordering (reorder buffer, aka instruction window or active window)
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- E
- O
- R
- D
- E
- R
- Reservation
- Station
- TAG and VALUE Broadcast Bus
- in order
- out of order
- in order

## Slide 56: Two Humps in a Modern Pipeline
- Two Humps in a Modern Pipeline
- Hump 1: Reservation stations (scheduling window)
- Hump 2: Reordering (reorder buffer, aka instruction window or active window)
- F
- D
- E
- W
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- E
- . . .
- Integer add
- Integer mul
- FP mul
- Load/store
- R
- E
- O
- R
- D
- E
- R
- S
- C
- H
- E
- D
- U
- L
- E
- TAG and VALUE Broadcast Bus
- in order
- out of order
- in order
- Photo credit: http://true-wildlife.blogspot.ch/2010/10/bactrian-camel.html

## Slide 57: Modern OoO Execution w/ Precise Exceptions
- Modern OoO Execution w/ Precise Exceptions
- Most modern processors use the following
- Reorder buffer to support in-order retirement of instructions
- A single register file to store all registers
- Both speculative and architectural registers
- INT and FP are still separate
- Two register maps
- Future/frontend register map  used for renaming
- Architectural register map  used for maintaining precise state

## Slide 58: Out-of-Order Execution with Precise Exceptions
- Out-of-Order Execution with Precise Exceptions
- Idea: Use a reorder buffer to reorder instructions before committing them to architectural state
- An instruction updates the RAT when it completes execution
- Also called frontend register file
- An instruction updates a separate architectural register file when it retires
- i.e., when it is the oldest in the machine and has completed execution
- In other words, the architectural register file is always updated in program order
- On an exception: flush pipeline, copy architectural register file into frontend register file

## Slide 59: An Example from Modern Processors
- An Example from Modern Processors
- Boggs et al., “The Microarchitecture of the Pentium 4 Processor,” Intel Technology Journal, 2001.

## Slide 60: OOO Execution: Restricted Dataflow
- OOO Execution: Restricted Dataflow
- An out-of-order engine dynamically builds the dataflow graph of a piece of the program
- which piece?
- The dataflow graph is limited to the instruction window
- Instruction window: all decoded but not yet retired instructions
- Can we do it for the whole program?
- Why would we like to?
- In other words, how can we have a large instruction window?
- Can we do it efficiently with Tomasulo’s algorithm?

## Slide 61: Questions to Ponder
- Questions to Ponder
- Why is OoO execution beneficial?
- What if all operations take a single cycle?
- Latency tolerance: OoO execution tolerates the latency of multi-cycle operations by executing independent operations concurrently
- What if an instruction takes 1000 cycles?
- How large of an instruction window do we need to continue decoding?
- How many cycles of latency can OoO tolerate?
- What limits the latency tolerance scalability of Tomasulo’s algorithm?
- Instruction window size: how many decoded but not yet retired instructions you can keep in the machine.