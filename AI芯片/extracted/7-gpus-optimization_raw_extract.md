# Raw Extract: 7-gpus-optimization.pptx

- Slides: 120

## Slide 1

### Shape 1 Rectangle 4

AI Chip & Systems.Lecture 7: GPU Optimization

### Alt/Text Metadata 1

Rectangle 4

### Shape 2 Rectangle 5

Prof. Zeke Wang
Zhejiang University
April 20 2026

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- 1

## Slide 2

### Shape 1 Marcador de contenido 2

CPU:
Few complex cores
Larger cache for low memory latency
Large and slow memory

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 134

Recall: CPU vs GPU： Compute Perspective

### Alt/Text Metadata 2

Título 134

### Shape 3 Marcador de número de diapositiva 1

2

### Alt/Text Metadata 3

Marcador de número de diapositiva 1

### Alt/Text Metadata 4

object 4

### Relationships 4

- rId2: image:../media/image2.png

### Alt/Text Metadata 5

object 5

### Relationships 5

- rId3: image:../media/image3.png

### Shape 6 Marcador de contenido 2

GPU:
Lots of simple cores
Small cache for low memory latency
Small and fast memory

### Notes XML fallback texts

- SIMD Wrap
- 5

### Slide media/diagram relationships

- rId3: image:../media/image3.png
- rId2: image:../media/image2.png

## Slide 3

### Shape 1 Título 134

Recall: Relationship between CPU and GPU

### Alt/Text Metadata 1

Título 134

### Shape 2 Marcador de número de diapositiva 1

3

### Alt/Text Metadata 2

Marcador de número de diapositiva 1

### Alt/Text Metadata 3

object 5

### Relationships 3

- rId2: image:../media/image4.png

### Alt/Text Metadata 4

object 6

### Shape 5 object 7

PCI Bus

### Alt/Text Metadata 5

object 7

### Shape 6 文本框 4

CPU

### Alt/Text Metadata 6

文本框 4

### Shape 7 文本框 140

GPU

### Alt/Text Metadata 7

文本框 140

### Alt/Text Metadata 8

图片 5

### Relationships 8

- rId3: image:../media/image5.emf

### Alt/Text Metadata 9

Picture 1

### Relationships 9

- rId4: image:../media/image6.jpg

### Notes XML fallback texts

- In SIMD, you need to specify the data array + an instruction (on which to operate the data on) + THE INSTRUCTION WIDTH.
- Eg: You might want to add 2 integer arrays of length 16, then a SIMD instruction would look like (the instruction has been cooked-up by me for demo)
- add.16 arr1 arr2
- However, SIMT doesn't bother about the instruction width. So, essentially, you could write the above example as:
- arr1[i] + arr2[i]
- and then launch as many threads as the length of the array, as you want.
- Note that, if the array size was, let us say, 32, then SIMD EXPECTS you to explicitly call two such 'add.16' instructions!
- Whereas, this is not the case with SIMT.
- 8

### Slide media/diagram relationships

- rId3: image:../media/image5.emf
- rId2: image:../media/image4.png
- rId4: image:../media/image6.jpg

## Slide 4

### Shape 1 Title 1

Recall: SPMD

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

SPMD: Single procedure/program, multiple data
This is a programming model rather than computer organization
Each processing element executes the same procedure, except on different data elements
Procedures can synchronize at certain points in program, e.g. barriers
Key Idea of SPMD: multiple instruction streams execute the same program
Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
Modern GPUs programmed in a similar way on a SIMD hardware

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

4

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Notes XML fallback texts

- 13

## Slide 5

### Shape 1 Title 1

Recall Programming Model vs. Hardware Execution Model

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

5

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 矩形 1

Hardware Execution Model

### Alt/Text Metadata 3

矩形 1

### Shape 4 矩形 3

CUDA Programming Model

### Alt/Text Metadata 4

矩形 3

### Shape 5 矩形 5

Streaming
 Multi-processor

### Alt/Text Metadata 5

矩形 5

### Shape 6 矩形 6

GPU

### Alt/Text Metadata 6

矩形 6

### Shape 7 矩形 25

CUDA core

### Alt/Text Metadata 7

矩形 25

### Shape 8 矩形 28

Thread

### Alt/Text Metadata 8

矩形 28

### Shape 9 矩形 29

Thread block

### Alt/Text Metadata 9

矩形 29

### Shape 10 矩形 33

Grid

### Alt/Text Metadata 10

矩形 33

### Alt/Text Metadata 11

object 3

### Alt/Text Metadata 12

object 18

### Alt/Text Metadata 13

object 19

### Alt/Text Metadata 14

object 20

### Relationships 14

- rId3: image:../media/image7.png

### Alt/Text Metadata 15

object 21

### Relationships 15

- rId3: image:../media/image7.png

### Alt/Text Metadata 16

object 22

### Alt/Text Metadata 17

object 23

### Alt/Text Metadata 18

object 24

### Alt/Text Metadata 19

object 25

### Alt/Text Metadata 20

object 30

### Alt/Text Metadata 21

object 31

### Alt/Text Metadata 22

object 32

### Alt/Text Metadata 23

object 33

### Relationships 23

- rId4: image:../media/image8.png

### Alt/Text Metadata 24

object 34

### Alt/Text Metadata 25

object 35

### Alt/Text Metadata 26

object 36

### Alt/Text Metadata 27

object 37

### Alt/Text Metadata 28

object 38

### Alt/Text Metadata 29

object 39

### Alt/Text Metadata 30

object 40

### Relationships 30

- rId5: image:../media/image9.png

### Alt/Text Metadata 31

object 41

### Alt/Text Metadata 32

object 42

### Alt/Text Metadata 33

object 43

### Alt/Text Metadata 34

object 44

### Alt/Text Metadata 35

object 45

### Alt/Text Metadata 36

object 46

### Alt/Text Metadata 37

object 47

### Relationships 37

- rId6: image:../media/image10.png

### Alt/Text Metadata 38

object 48

### Alt/Text Metadata 39

object 49

### Alt/Text Metadata 40

object 50

### Alt/Text Metadata 41

object 51

### Alt/Text Metadata 42

object 52

### Alt/Text Metadata 43

object 53

### Alt/Text Metadata 44

object 54

### Alt/Text Metadata 45

object 55

### Relationships 45

- rId7: image:../media/image11.png

### Alt/Text Metadata 46

object 56

### Alt/Text Metadata 47

object 57

### Alt/Text Metadata 48

object 58

### Alt/Text Metadata 49

object 59

### Alt/Text Metadata 50

object 60

### Alt/Text Metadata 51

object 61

### Alt/Text Metadata 52

object 62

### Relationships 52

- rId8: image:../media/image12.png

### Alt/Text Metadata 53

object 63

### Alt/Text Metadata 54

object 64

### Alt/Text Metadata 55

object 65

### Alt/Text Metadata 56

object 66

### Alt/Text Metadata 57

object 67

### Alt/Text Metadata 58

object 68

### Alt/Text Metadata 59

object 69

### Relationships 59

- rId6: image:../media/image10.png

### Alt/Text Metadata 60

object 70

### Alt/Text Metadata 61

object 71

### Alt/Text Metadata 62

object 72

### Alt/Text Metadata 63

object 73

### Alt/Text Metadata 64

object 6

### Alt/Text Metadata 65

object 8

### Alt/Text Metadata 66

object 9

### Alt/Text Metadata 67

object 10

### Alt/Text Metadata 68

object 11

### Alt/Text Metadata 69

object 12

### Alt/Text Metadata 70

object 13

### Alt/Text Metadata 71

object 14

### Alt/Text Metadata 72

object 15

### Alt/Text Metadata 73

object 16

### Alt/Text Metadata 74

object 17

### Alt/Text Metadata 75

object 74

### Alt/Text Metadata 76

object 75

### Alt/Text Metadata 77

object 76

### Alt/Text Metadata 78

object 77

### Alt/Text Metadata 79

object 78

### Alt/Text Metadata 80

object 79

### Alt/Text Metadata 81

object 80

### Alt/Text Metadata 82

object 81

### Alt/Text Metadata 83

object 82

### Alt/Text Metadata 84

object 83

### Alt/Text Metadata 85

object 84

### Alt/Text Metadata 86

object 85

### Alt/Text Metadata 87

object 86

### Alt/Text Metadata 88

object 87

### Alt/Text Metadata 89

object 88

### Alt/Text Metadata 90

object 89

### Alt/Text Metadata 91

object 90

### Alt/Text Metadata 92

object 91

### Alt/Text Metadata 93

object 92

### Alt/Text Metadata 94

object 93

### Alt/Text Metadata 95

object 94

### Alt/Text Metadata 96

object 95

### Shape 97 object 96

...

### Alt/Text Metadata 97

object 96

### Alt/Text Metadata 98

直接连接符 7

### Shape 99 矩形 119

Warp

### Alt/Text Metadata 99

矩形 119

### Alt/Text Metadata 100

组合 2 | 矩形 120 | object 3

### Shape 100.1 矩形 120

SIMT

### Alt/Text Metadata 100.1

矩形 120

### Speaker notes

SIMD Wrap

### Slide media/diagram relationships

- rId8: image:../media/image12.png
- rId3: image:../media/image7.png
- rId7: image:../media/image11.png
- rId6: image:../media/image10.png
- rId5: image:../media/image9.png
- rId4: image:../media/image8.png

## Slide 6

### Shape 1 Title 1

Recall: SIMT (Hardware) & Warp (Software)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

SIMT: Single Instruction Multiple Thread
More precisely, SIMD (Single Instruction Multiple Data)
Key Feature: 16 CUDA cores in a SM are executed in a lock step.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

6

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 Content Placeholder 2

Warp:
A warp, a basic execution unit, consists of 32 consecutive threads
A thread block is divided into warps for SIMT execution.

### Alt/Text Metadata 5

Rectangle 73

### Shape 6 Rectangle 74

…

### Alt/Text Metadata 6

Rectangle 74

### Alt/Text Metadata 7

Group 75 | Text Box 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80 | Freeform 81 | Freeform 82 | Freeform 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87

### Shape 7.1 Text Box 76

t0 t1 t2 … t31

### Alt/Text Metadata 7.1

Text Box 76

### Alt/Text Metadata 7.2

Freeform 77

### Alt/Text Metadata 7.3

Freeform 78

### Alt/Text Metadata 7.4

Freeform 79

### Alt/Text Metadata 7.5

Freeform 80

### Alt/Text Metadata 7.6

Freeform 81

### Alt/Text Metadata 7.7

Freeform 82

### Alt/Text Metadata 7.8

Freeform 83

### Alt/Text Metadata 7.9

Freeform 84

### Alt/Text Metadata 7.10

Freeform 85

### Alt/Text Metadata 7.11

Freeform 86

### Alt/Text Metadata 7.12

Freeform 87

### Alt/Text Metadata 8

Text Box 88

### Alt/Text Metadata 9

Rectangle 89

### Alt/Text Metadata 10

Rectangle 90

### Alt/Text Metadata 11

Group 91 | Text Box 92 | Freeform 93 | Freeform 94 | Freeform 95 | Freeform 96 | Freeform 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103

### Alt/Text Metadata 11.1

Text Box 92

### Alt/Text Metadata 11.2

Freeform 93

### Alt/Text Metadata 11.3

Freeform 94

### Alt/Text Metadata 11.4

Freeform 95

### Alt/Text Metadata 11.5

Freeform 96

### Alt/Text Metadata 11.6

Freeform 97

### Alt/Text Metadata 11.7

Freeform 98

### Alt/Text Metadata 11.8

Freeform 99

### Alt/Text Metadata 11.9

Freeform 100

### Alt/Text Metadata 11.10

Freeform 101

### Alt/Text Metadata 11.11

Freeform 102

### Alt/Text Metadata 11.12

Freeform 103

### Alt/Text Metadata 12

Text Box 104

### Shape 13 Text Box 105

Block 0’s warps

### Alt/Text Metadata 13

Text Box 105

### Shape 14 Text Box 106

Block 1’s warps

### Alt/Text Metadata 14

Text Box 106

### Alt/Text Metadata 15

Rectangle 135

### Alt/Text Metadata 16

Rectangle 136

### Alt/Text Metadata 17

Group 137 | Text Box 138 | Freeform 139 | Freeform 140 | Freeform 141 | Freeform 142 | Freeform 143 | Freeform 144 | Freeform 145 | Freeform 146 | Freeform 147 | Freeform 148 | Freeform 149

### Alt/Text Metadata 17.1

Text Box 138

### Alt/Text Metadata 17.2

Freeform 139

### Alt/Text Metadata 17.3

Freeform 140

### Alt/Text Metadata 17.4

Freeform 141

### Alt/Text Metadata 17.5

Freeform 142

### Alt/Text Metadata 17.6

Freeform 143

### Alt/Text Metadata 17.7

Freeform 144

### Alt/Text Metadata 17.8

Freeform 145

### Alt/Text Metadata 17.9

Freeform 146

### Alt/Text Metadata 17.10

Freeform 147

### Alt/Text Metadata 17.11

Freeform 148

### Alt/Text Metadata 17.12

Freeform 149

### Alt/Text Metadata 18

Text Box 150

### Shape 19 Text Box 151

Block 2’s warps

### Alt/Text Metadata 19

Text Box 151

### Notes XML fallback texts

- 15

## Slide 7

### Shape 1 矩形 25

Motivation of In-network Computing

### Alt/Text Metadata 1

矩形 25

### Alt/Text Metadata 2

Rectangle 2

### Shape 3 TextBox 3

Why SIMT and Warp?

### Alt/Text Metadata 3

TextBox 3

### Shape 4 TextBox 3

Reduce GPU scheduling overhead

### Notes XML fallback texts

- HBM3 memory subsystem
- provides nearly a 2x bandwidth increase over the previous generation. The H100 SXM5 GPU is the world’s first GPU with HBM3 memory delivering a class-leading 3 TB/sec of memory bandwidth.
- 50 MB L2 cache architecture
- caches large portions of models and datasets for repeated access, reducing trips to HBM3.
- SM
- ：
- streaming multiprocessor
- 16

## Slide 8

### Shape 1 Title 1

Recall: Mapping Warps on a SIMT Hardware

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Warp:
A thread block is divided into warps.
A warp executes the same instruction on different data elements
SIMT Pipeline:
16 CUDA cores are executed in a lock step to serve each warp.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

8

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

AutoShape 25

### Alt/Text Metadata 5

Rectangle 27

### Alt/Text Metadata 6

Rectangle 28

### Alt/Text Metadata 7

Rectangle 29

### Alt/Text Metadata 8

Rectangle 30

### Shape 9 Rectangle 31

Thread Warp 0

### Alt/Text Metadata 9

Rectangle 31

### Alt/Text Metadata 10

Rectangle 32

### Alt/Text Metadata 11

Rectangle 33

### Shape 12 Rectangle 34

Thread Warp 8

### Alt/Text Metadata 12

Rectangle 34

### Alt/Text Metadata 13

Freeform 35

### Alt/Text Metadata 14

Freeform 36

### Alt/Text Metadata 15

Freeform 37

### Alt/Text Metadata 16

Freeform 38

### Alt/Text Metadata 17

Freeform 39

### Alt/Text Metadata 18

Freeform 40

### Alt/Text Metadata 19

Rectangle 43

### Alt/Text Metadata 20

Rectangle 44

### Shape 21 Rectangle 45

Thread Warp 7

### Alt/Text Metadata 21

Rectangle 45

### Alt/Text Metadata 22

Freeform 46

### Alt/Text Metadata 23

Freeform 47

### Alt/Text Metadata 24

Rectangle 48

### Alt/Text Metadata 25

Rectangle 49

### Shape 26 Rectangle 50

Thread Warp

### Alt/Text Metadata 26

Rectangle 50

### Alt/Text Metadata 27

Rectangle 51

### Alt/Text Metadata 28

Rectangle 52

### Shape 29 Rectangle 53

Scalar

### Alt/Text Metadata 29

Rectangle 53

### Shape 30 Rectangle 54

Thread

### Alt/Text Metadata 30

Rectangle 54

### Shape 31 Rectangle 55

0

### Alt/Text Metadata 31

Rectangle 55

### Alt/Text Metadata 32

Rectangle 56

### Alt/Text Metadata 33

Rectangle 57

### Alt/Text Metadata 34

Rectangle 58

### Alt/Text Metadata 35

Rectangle 59

### Shape 36 Rectangle 60

1

### Alt/Text Metadata 36

Rectangle 60

### Alt/Text Metadata 37

Rectangle 61

### Alt/Text Metadata 38

Rectangle 62

### Alt/Text Metadata 39

Rectangle 63

### Alt/Text Metadata 40

Rectangle 64

### Shape 41 Rectangle 65

2

### Alt/Text Metadata 41

Rectangle 65

### Alt/Text Metadata 42

Rectangle 66

### Alt/Text Metadata 43

Rectangle 67

### Alt/Text Metadata 44

Rectangle 68

### Alt/Text Metadata 45

Rectangle 69

### Shape 46 Rectangle 70

31

### Alt/Text Metadata 46

Rectangle 70

### Alt/Text Metadata 47

Freeform 71

### Alt/Text Metadata 48

Freeform 72

### Alt/Text Metadata 49

Freeform 73

### Alt/Text Metadata 50

Freeform 74

### Alt/Text Metadata 51

Freeform 75

### Alt/Text Metadata 52

Freeform 76

### Alt/Text Metadata 53

Rectangle 77

### Alt/Text Metadata 54

Rectangle 78

### Shape 55 Rectangle 79

Common PC

### Alt/Text Metadata 55

Rectangle 79

### Alt/Text Metadata 56

组合 1 | Line 41 | Freeform 42 | Rectangle 80 | Rectangle 81 | Rectangle 82

### Alt/Text Metadata 56.1

Line 41

### Alt/Text Metadata 56.2

Freeform 42

### Alt/Text Metadata 56.3

Rectangle 80

### Alt/Text Metadata 56.4

Rectangle 81

### Shape 56.5 Rectangle 82

SIMT Pipeline

### Alt/Text Metadata 56.5

Rectangle 82

### Shape 57 TextBox 6

Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

### Alt/Text Metadata 57

TextBox 6

### Speaker notes

In SIMD, you need to specify the data array + an instruction (on which to operate the data on) + THE INSTRUCTION WIDTH.Eg: You might want to add 2 integer arrays of length 16, then a SIMD instruction would look like (the instruction has been cooked-up by me for demo)add.16 arr1 arr2However, SIMT doesn't bother about the instruction width. So, essentially, you could write the above example as:arr1[i] + arr2[i]and then launch as many threads as the length of the array, as you want.Note that, if the array size was, let us say, 32, then SIMD EXPECTS you to explicitly call two such 'add.16' instructions!Whereas, this is not the case with SIMT.

## Slide 9

### Alt/Text Metadata 1

AutoShape 30

### Alt/Text Metadata 2

AutoShape 29

### Shape 4 Title 1

Recall: GPU Execution with Warps

### Alt/Text Metadata 4

Title 1

### Shape 5 Slide Number Placeholder 3

9

### Alt/Text Metadata 5

Slide Number Placeholder 3

### Shape 6 Text Box 3

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

### Alt/Text Metadata 6

Text Box 3

### Alt/Text Metadata 7

Group 5 | AutoShape 33 | AutoShape 34 | AutoShape 35 | AutoShape 36 | Line 37 | Line 38 | Line 39 | AutoShape 47

### Shape 7.1 AutoShape 33

load

### Alt/Text Metadata 7.1

AutoShape 33

### Alt/Text Metadata 7.2

AutoShape 34

### Shape 7.3 AutoShape 35

add

### Alt/Text Metadata 7.3

AutoShape 35

### Shape 7.4 AutoShape 36

store

### Alt/Text Metadata 7.4

AutoShape 36

### Alt/Text Metadata 7.5

Line 37

### Alt/Text Metadata 7.6

Line 38

### Alt/Text Metadata 7.7

Line 39

### Alt/Text Metadata 7.8

AutoShape 47

### Alt/Text Metadata 8

Group 4 | AutoShape 40 | AutoShape 41 | AutoShape 42 | AutoShape 43 | Line 44 | Line 45 | Line 46 | AutoShape 48

### Alt/Text Metadata 8.1

AutoShape 40

### Alt/Text Metadata 8.2

AutoShape 41

### Alt/Text Metadata 8.3

AutoShape 42

### Alt/Text Metadata 8.4

AutoShape 43

### Alt/Text Metadata 8.5

Line 44

### Alt/Text Metadata 8.6

Line 45

### Alt/Text Metadata 8.7

Line 46

### Alt/Text Metadata 8.8

AutoShape 48

### Shape 9 Text Box 49

Iter. 1

### Alt/Text Metadata 9

Text Box 49

### Shape 10 Text Box 50

Iter. 2

### Alt/Text Metadata 10

Text Box 50

### Alt/Text Metadata 11

Line 55

### Shape 12 Text Box 32

Warp 0 at PC X

### Alt/Text Metadata 12

Text Box 32

### Shape 13 Content Placeholder 2

Assume: a warp consists of 32 threads
If you have 32K iterations, and 1 iteration/thread  1K warps
Warps can be interleaved on the same pipeline  Fine grained multithreading of warps.

### Alt/Text Metadata 13

Content Placeholder 2

### Shape 14 Text Box 32

Warp 1 at PC X

### Shape 15 Text Box 49

Iter. 33

### Shape 16 Text Box 50

Iter. 34

### Shape 17 Text Box 32

Warp 20 at PC X+2

### Shape 18 Text Box 49

Iter.
20*32 + 1

### Shape 19 Text Box 49

Iter.
20*32 + 2

### Notes XML fallback texts

- 21

## Slide 10

### Shape 1 Title 1

Recall: Warp Instruction Level Parallelism

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Can overlap execution of multiple instructions
Example machine has 32 threads per warp and 8 lanes
Completes 24 operations/cycle while issuing 1 warp/cycle

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

10

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 2 | Group 3 | Group 7 | Rectangle 5 | Oval 6 | Rectangle 7 | Group 8 | Rectangle 9 | Oval 10 | Group 11 | Rectangle 12 | Oval 13 | Group 14 | Rectangle 15 | Oval 16 | Group 17 | Rectangle 18 | Oval 19 | Group 20 | Rectangle 21 | Oval 22 | Group 23 | Rectangle 24 | Oval 25 | Group 26 | Rectangle 27 | Oval 28 | Group 29 | Rectangle 30 | Oval 31 | Group 32 | Rectangle 33 | Oval 34 | Group 35 | Rectangle 36 | Oval 37 | Group 38 | Rectangle 39 | Oval 40 | Group 41 | Rectangle 42 | Oval 43 | Group 44 | Rectangle 45 | Oval 46 | Group 47 | Rectangle 48 | Oval 49 | Group 50 | Rectangle 51 | Oval 52 | Group 53 | Rectangle 54 | Oval 55 | Group 56 | Rectangle 57 | Oval 58 | Group 59 | Rectangle 60 | Oval 61 | Group 62 | Rectangle 63 | Oval 64 | Group 65 | Rectangle 66 | Oval 67 | Group 68 | Rectangle 69 | Oval 70 | Group 71 | Rectangle 72 | Oval 73 | Group 74 | Rectangle 75 | Oval 76 | Group 77 | Rectangle 78 | Oval 79 | Group 80 | Rectangle 81 | Oval 82 | Group 83 | Rectangle 84 | Oval 85 | Group 86 | Rectangle 87 | Oval 88 | Group 89 | Rectangle 90 | Oval 91 | Group 92 | Rectangle 93 | Oval 94 | Group 95 | Rectangle 96 | Oval 97 | Group 98 | Rectangle 99 | Oval 100 | AutoShape 101

### Alt/Text Metadata 4.1

Group 3 | Group 7 | Rectangle 5 | Oval 6 | Rectangle 7 | Group 8 | Rectangle 9 | Oval 10 | Group 11 | Rectangle 12 | Oval 13 | Group 14 | Rectangle 15 | Oval 16 | Group 17 | Rectangle 18 | Oval 19 | Group 20 | Rectangle 21 | Oval 22 | Group 23 | Rectangle 24 | Oval 25 | Group 26 | Rectangle 27 | Oval 28 | Group 29 | Rectangle 30 | Oval 31 | Group 32 | Rectangle 33 | Oval 34 | Group 35 | Rectangle 36 | Oval 37 | Group 38 | Rectangle 39 | Oval 40 | Group 41 | Rectangle 42 | Oval 43 | Group 44 | Rectangle 45 | Oval 46 | Group 47 | Rectangle 48 | Oval 49 | Group 50 | Rectangle 51 | Oval 52 | Group 53 | Rectangle 54 | Oval 55 | Group 56 | Rectangle 57 | Oval 58 | Group 59 | Rectangle 60 | Oval 61 | Group 62 | Rectangle 63 | Oval 64 | Group 65 | Rectangle 66 | Oval 67 | Group 68 | Rectangle 69 | Oval 70 | Group 71 | Rectangle 72 | Oval 73 | Group 74 | Rectangle 75 | Oval 76 | Group 77 | Rectangle 78 | Oval 79 | Group 80 | Rectangle 81 | Oval 82 | Group 83 | Rectangle 84 | Oval 85 | Group 86 | Rectangle 87 | Oval 88 | Group 89 | Rectangle 90 | Oval 91 | Group 92 | Rectangle 93 | Oval 94 | Group 95 | Rectangle 96 | Oval 97 | Group 98 | Rectangle 99 | Oval 100

### Alt/Text Metadata 4.1.1

Group 7 | Rectangle 5 | Oval 6

### Alt/Text Metadata 4.1.1.1

Rectangle 5

### Alt/Text Metadata 4.1.1.2

Oval 6

### Alt/Text Metadata 4.1.2

Rectangle 7

### Alt/Text Metadata 4.1.3

Group 8 | Rectangle 9 | Oval 10

### Alt/Text Metadata 4.1.3.1

Rectangle 9

### Alt/Text Metadata 4.1.3.2

Oval 10

### Alt/Text Metadata 4.1.4

Group 11 | Rectangle 12 | Oval 13

### Alt/Text Metadata 4.1.4.1

Rectangle 12

### Alt/Text Metadata 4.1.4.2

Oval 13

### Alt/Text Metadata 4.1.5

Group 14 | Rectangle 15 | Oval 16

### Alt/Text Metadata 4.1.5.1

Rectangle 15

### Alt/Text Metadata 4.1.5.2

Oval 16

### Alt/Text Metadata 4.1.6

Group 17 | Rectangle 18 | Oval 19

### Alt/Text Metadata 4.1.6.1

Rectangle 18

### Alt/Text Metadata 4.1.6.2

Oval 19

### Alt/Text Metadata 4.1.7

Group 20 | Rectangle 21 | Oval 22

### Alt/Text Metadata 4.1.7.1

Rectangle 21

### Alt/Text Metadata 4.1.7.2

Oval 22

### Alt/Text Metadata 4.1.8

Group 23 | Rectangle 24 | Oval 25

### Alt/Text Metadata 4.1.8.1

Rectangle 24

### Alt/Text Metadata 4.1.8.2

Oval 25

### Alt/Text Metadata 4.1.9

Group 26 | Rectangle 27 | Oval 28

### Alt/Text Metadata 4.1.9.1

Rectangle 27

### Alt/Text Metadata 4.1.9.2

Oval 28

### Alt/Text Metadata 4.1.10

Group 29 | Rectangle 30 | Oval 31

### Alt/Text Metadata 4.1.10.1

Rectangle 30

### Alt/Text Metadata 4.1.10.2

Oval 31

### Alt/Text Metadata 4.1.11

Group 32 | Rectangle 33 | Oval 34

### Alt/Text Metadata 4.1.11.1

Rectangle 33

### Alt/Text Metadata 4.1.11.2

Oval 34

### Alt/Text Metadata 4.1.12

Group 35 | Rectangle 36 | Oval 37

### Alt/Text Metadata 4.1.12.1

Rectangle 36

### Alt/Text Metadata 4.1.12.2

Oval 37

### Alt/Text Metadata 4.1.13

Group 38 | Rectangle 39 | Oval 40

### Alt/Text Metadata 4.1.13.1

Rectangle 39

### Alt/Text Metadata 4.1.13.2

Oval 40

### Alt/Text Metadata 4.1.14

Group 41 | Rectangle 42 | Oval 43

### Alt/Text Metadata 4.1.14.1

Rectangle 42

### Alt/Text Metadata 4.1.14.2

Oval 43

### Alt/Text Metadata 4.1.15

Group 44 | Rectangle 45 | Oval 46

### Alt/Text Metadata 4.1.15.1

Rectangle 45

### Alt/Text Metadata 4.1.15.2

Oval 46

### Alt/Text Metadata 4.1.16

Group 47 | Rectangle 48 | Oval 49

### Alt/Text Metadata 4.1.16.1

Rectangle 48

### Alt/Text Metadata 4.1.16.2

Oval 49

### Alt/Text Metadata 4.1.17

Group 50 | Rectangle 51 | Oval 52

### Alt/Text Metadata 4.1.17.1

Rectangle 51

### Alt/Text Metadata 4.1.17.2

Oval 52

### Alt/Text Metadata 4.1.18

Group 53 | Rectangle 54 | Oval 55

### Alt/Text Metadata 4.1.18.1

Rectangle 54

### Alt/Text Metadata 4.1.18.2

Oval 55

### Alt/Text Metadata 4.1.19

Group 56 | Rectangle 57 | Oval 58

### Alt/Text Metadata 4.1.19.1

Rectangle 57

### Alt/Text Metadata 4.1.19.2

Oval 58

### Alt/Text Metadata 4.1.20

Group 59 | Rectangle 60 | Oval 61

### Alt/Text Metadata 4.1.20.1

Rectangle 60

### Alt/Text Metadata 4.1.20.2

Oval 61

### Alt/Text Metadata 4.1.21

Group 62 | Rectangle 63 | Oval 64

### Alt/Text Metadata 4.1.21.1

Rectangle 63

### Alt/Text Metadata 4.1.21.2

Oval 64

### Alt/Text Metadata 4.1.22

Group 65 | Rectangle 66 | Oval 67

### Alt/Text Metadata 4.1.22.1

Rectangle 66

### Alt/Text Metadata 4.1.22.2

Oval 67

### Alt/Text Metadata 4.1.23

Group 68 | Rectangle 69 | Oval 70

### Alt/Text Metadata 4.1.23.1

Rectangle 69

### Alt/Text Metadata 4.1.23.2

Oval 70

### Alt/Text Metadata 4.1.24

Group 71 | Rectangle 72 | Oval 73

### Alt/Text Metadata 4.1.24.1

Rectangle 72

### Alt/Text Metadata 4.1.24.2

Oval 73

### Alt/Text Metadata 4.1.25

Group 74 | Rectangle 75 | Oval 76

### Alt/Text Metadata 4.1.25.1

Rectangle 75

### Alt/Text Metadata 4.1.25.2

Oval 76

### Alt/Text Metadata 4.1.26

Group 77 | Rectangle 78 | Oval 79

### Alt/Text Metadata 4.1.26.1

Rectangle 78

### Alt/Text Metadata 4.1.26.2

Oval 79

### Alt/Text Metadata 4.1.27

Group 80 | Rectangle 81 | Oval 82

### Alt/Text Metadata 4.1.27.1

Rectangle 81

### Alt/Text Metadata 4.1.27.2

Oval 82

### Alt/Text Metadata 4.1.28

Group 83 | Rectangle 84 | Oval 85

### Alt/Text Metadata 4.1.28.1

Rectangle 84

### Alt/Text Metadata 4.1.28.2

Oval 85

### Alt/Text Metadata 4.1.29

Group 86 | Rectangle 87 | Oval 88

### Alt/Text Metadata 4.1.29.1

Rectangle 87

### Alt/Text Metadata 4.1.29.2

Oval 88

### Alt/Text Metadata 4.1.30

Group 89 | Rectangle 90 | Oval 91

### Alt/Text Metadata 4.1.30.1

Rectangle 90

### Alt/Text Metadata 4.1.30.2

Oval 91

### Alt/Text Metadata 4.1.31

Group 92 | Rectangle 93 | Oval 94

### Alt/Text Metadata 4.1.31.1

Rectangle 93

### Alt/Text Metadata 4.1.31.2

Oval 94

### Alt/Text Metadata 4.1.32

Group 95 | Rectangle 96 | Oval 97

### Alt/Text Metadata 4.1.32.1

Rectangle 96

### Alt/Text Metadata 4.1.32.2

Oval 97

### Alt/Text Metadata 4.1.33

Group 98 | Rectangle 99 | Oval 100

### Alt/Text Metadata 4.1.33.1

Rectangle 99

### Alt/Text Metadata 4.1.33.2

Oval 100

### Shape 4.2 AutoShape 101

W3

### Alt/Text Metadata 4.2

AutoShape 101

### Alt/Text Metadata 5

Group 104 | Group 105 | Group 106 | Rectangle 107 | Oval 108 | Rectangle 109 | Group 110 | Rectangle 111 | Oval 112 | Group 113 | Rectangle 114 | Oval 115 | Group 116 | Rectangle 117 | Oval 118 | Group 119 | Rectangle 120 | Oval 121 | Group 122 | Rectangle 123 | Oval 124 | Group 125 | Rectangle 126 | Oval 127 | Group 128 | Rectangle 129 | Oval 130 | Group 131 | Rectangle 132 | Oval 133 | Group 134 | Rectangle 135 | Oval 136 | Group 137 | Rectangle 138 | Oval 139 | Group 140 | Rectangle 141 | Oval 142 | Group 143 | Rectangle 144 | Oval 145 | Group 146 | Rectangle 147 | Oval 148 | Group 149 | Rectangle 150 | Oval 151 | Group 152 | Rectangle 153 | Oval 154 | Group 155 | Rectangle 156 | Oval 157 | Group 158 | Rectangle 159 | Oval 160 | Group 161 | Rectangle 162 | Oval 163 | Group 164 | Rectangle 165 | Oval 166 | Group 167 | Rectangle 168 | Oval 169 | Group 170 | Rectangle 171 | Oval 172 | Group 173 | Rectangle 174 | Oval 175 | Group 176 | Rectangle 177 | Oval 178 | Group 179 | Rectangle 180 | Oval 181 | Group 182 | Rectangle 183 | Oval 184 | Group 185 | Rectangle 186 | Oval 187 | Group 188 | Rectangle 189 | Oval 190 | Group 191 | Rectangle 192 | Oval 193 | Group 194 | Rectangle 195 | Oval 196 | Group 197 | Rectangle 198 | Oval 199 | Group 200 | Rectangle 201 | Oval 202 | AutoShape 203

### Alt/Text Metadata 5.1

Group 105 | Group 106 | Rectangle 107 | Oval 108 | Rectangle 109 | Group 110 | Rectangle 111 | Oval 112 | Group 113 | Rectangle 114 | Oval 115 | Group 116 | Rectangle 117 | Oval 118 | Group 119 | Rectangle 120 | Oval 121 | Group 122 | Rectangle 123 | Oval 124 | Group 125 | Rectangle 126 | Oval 127 | Group 128 | Rectangle 129 | Oval 130 | Group 131 | Rectangle 132 | Oval 133 | Group 134 | Rectangle 135 | Oval 136 | Group 137 | Rectangle 138 | Oval 139 | Group 140 | Rectangle 141 | Oval 142 | Group 143 | Rectangle 144 | Oval 145 | Group 146 | Rectangle 147 | Oval 148 | Group 149 | Rectangle 150 | Oval 151 | Group 152 | Rectangle 153 | Oval 154 | Group 155 | Rectangle 156 | Oval 157 | Group 158 | Rectangle 159 | Oval 160 | Group 161 | Rectangle 162 | Oval 163 | Group 164 | Rectangle 165 | Oval 166 | Group 167 | Rectangle 168 | Oval 169 | Group 170 | Rectangle 171 | Oval 172 | Group 173 | Rectangle 174 | Oval 175 | Group 176 | Rectangle 177 | Oval 178 | Group 179 | Rectangle 180 | Oval 181 | Group 182 | Rectangle 183 | Oval 184 | Group 185 | Rectangle 186 | Oval 187 | Group 188 | Rectangle 189 | Oval 190 | Group 191 | Rectangle 192 | Oval 193 | Group 194 | Rectangle 195 | Oval 196 | Group 197 | Rectangle 198 | Oval 199 | Group 200 | Rectangle 201 | Oval 202

### Alt/Text Metadata 5.1.1

Group 106 | Rectangle 107 | Oval 108

### Alt/Text Metadata 5.1.1.1

Rectangle 107

### Alt/Text Metadata 5.1.1.2

Oval 108

### Alt/Text Metadata 5.1.2

Rectangle 109

### Alt/Text Metadata 5.1.3

Group 110 | Rectangle 111 | Oval 112

### Alt/Text Metadata 5.1.3.1

Rectangle 111

### Alt/Text Metadata 5.1.3.2

Oval 112

### Alt/Text Metadata 5.1.4

Group 113 | Rectangle 114 | Oval 115

### Alt/Text Metadata 5.1.4.1

Rectangle 114

### Alt/Text Metadata 5.1.4.2

Oval 115

### Alt/Text Metadata 5.1.5

Group 116 | Rectangle 117 | Oval 118

### Alt/Text Metadata 5.1.5.1

Rectangle 117

### Alt/Text Metadata 5.1.5.2

Oval 118

### Alt/Text Metadata 5.1.6

Group 119 | Rectangle 120 | Oval 121

### Alt/Text Metadata 5.1.6.1

Rectangle 120

### Alt/Text Metadata 5.1.6.2

Oval 121

### Alt/Text Metadata 5.1.7

Group 122 | Rectangle 123 | Oval 124

### Alt/Text Metadata 5.1.7.1

Rectangle 123

### Alt/Text Metadata 5.1.7.2

Oval 124

### Alt/Text Metadata 5.1.8

Group 125 | Rectangle 126 | Oval 127

### Alt/Text Metadata 5.1.8.1

Rectangle 126

### Alt/Text Metadata 5.1.8.2

Oval 127

### Alt/Text Metadata 5.1.9

Group 128 | Rectangle 129 | Oval 130

### Alt/Text Metadata 5.1.9.1

Rectangle 129

### Alt/Text Metadata 5.1.9.2

Oval 130

### Alt/Text Metadata 5.1.10

Group 131 | Rectangle 132 | Oval 133

### Alt/Text Metadata 5.1.10.1

Rectangle 132

### Alt/Text Metadata 5.1.10.2

Oval 133

### Alt/Text Metadata 5.1.11

Group 134 | Rectangle 135 | Oval 136

### Alt/Text Metadata 5.1.11.1

Rectangle 135

### Alt/Text Metadata 5.1.11.2

Oval 136

### Alt/Text Metadata 5.1.12

Group 137 | Rectangle 138 | Oval 139

### Alt/Text Metadata 5.1.12.1

Rectangle 138

### Alt/Text Metadata 5.1.12.2

Oval 139

### Alt/Text Metadata 5.1.13

Group 140 | Rectangle 141 | Oval 142

### Alt/Text Metadata 5.1.13.1

Rectangle 141

### Alt/Text Metadata 5.1.13.2

Oval 142

### Alt/Text Metadata 5.1.14

Group 143 | Rectangle 144 | Oval 145

### Alt/Text Metadata 5.1.14.1

Rectangle 144

### Alt/Text Metadata 5.1.14.2

Oval 145

### Alt/Text Metadata 5.1.15

Group 146 | Rectangle 147 | Oval 148

### Alt/Text Metadata 5.1.15.1

Rectangle 147

### Alt/Text Metadata 5.1.15.2

Oval 148

### Alt/Text Metadata 5.1.16

Group 149 | Rectangle 150 | Oval 151

### Alt/Text Metadata 5.1.16.1

Rectangle 150

### Alt/Text Metadata 5.1.16.2

Oval 151

### Alt/Text Metadata 5.1.17

Group 152 | Rectangle 153 | Oval 154

### Alt/Text Metadata 5.1.17.1

Rectangle 153

### Alt/Text Metadata 5.1.17.2

Oval 154

### Alt/Text Metadata 5.1.18

Group 155 | Rectangle 156 | Oval 157

### Alt/Text Metadata 5.1.18.1

Rectangle 156

### Alt/Text Metadata 5.1.18.2

Oval 157

### Alt/Text Metadata 5.1.19

Group 158 | Rectangle 159 | Oval 160

### Alt/Text Metadata 5.1.19.1

Rectangle 159

### Alt/Text Metadata 5.1.19.2

Oval 160

### Alt/Text Metadata 5.1.20

Group 161 | Rectangle 162 | Oval 163

### Alt/Text Metadata 5.1.20.1

Rectangle 162

### Alt/Text Metadata 5.1.20.2

Oval 163

### Alt/Text Metadata 5.1.21

Group 164 | Rectangle 165 | Oval 166

### Alt/Text Metadata 5.1.21.1

Rectangle 165

### Alt/Text Metadata 5.1.21.2

Oval 166

### Alt/Text Metadata 5.1.22

Group 167 | Rectangle 168 | Oval 169

### Alt/Text Metadata 5.1.22.1

Rectangle 168

### Alt/Text Metadata 5.1.22.2

Oval 169

### Alt/Text Metadata 5.1.23

Group 170 | Rectangle 171 | Oval 172

### Alt/Text Metadata 5.1.23.1

Rectangle 171

### Alt/Text Metadata 5.1.23.2

Oval 172

### Alt/Text Metadata 5.1.24

Group 173 | Rectangle 174 | Oval 175

### Alt/Text Metadata 5.1.24.1

Rectangle 174

### Alt/Text Metadata 5.1.24.2

Oval 175

### Alt/Text Metadata 5.1.25

Group 176 | Rectangle 177 | Oval 178

### Alt/Text Metadata 5.1.25.1

Rectangle 177

### Alt/Text Metadata 5.1.25.2

Oval 178

### Alt/Text Metadata 5.1.26

Group 179 | Rectangle 180 | Oval 181

### Alt/Text Metadata 5.1.26.1

Rectangle 180

### Alt/Text Metadata 5.1.26.2

Oval 181

### Alt/Text Metadata 5.1.27

Group 182 | Rectangle 183 | Oval 184

### Alt/Text Metadata 5.1.27.1

Rectangle 183

### Alt/Text Metadata 5.1.27.2

Oval 184

### Alt/Text Metadata 5.1.28

Group 185 | Rectangle 186 | Oval 187

### Alt/Text Metadata 5.1.28.1

Rectangle 186

### Alt/Text Metadata 5.1.28.2

Oval 187

### Alt/Text Metadata 5.1.29

Group 188 | Rectangle 189 | Oval 190

### Alt/Text Metadata 5.1.29.1

Rectangle 189

### Alt/Text Metadata 5.1.29.2

Oval 190

### Alt/Text Metadata 5.1.30

Group 191 | Rectangle 192 | Oval 193

### Alt/Text Metadata 5.1.30.1

Rectangle 192

### Alt/Text Metadata 5.1.30.2

Oval 193

### Alt/Text Metadata 5.1.31

Group 194 | Rectangle 195 | Oval 196

### Alt/Text Metadata 5.1.31.1

Rectangle 195

### Alt/Text Metadata 5.1.31.2

Oval 196

### Alt/Text Metadata 5.1.32

Group 197 | Rectangle 198 | Oval 199

### Alt/Text Metadata 5.1.32.1

Rectangle 198

### Alt/Text Metadata 5.1.32.2

Oval 199

### Alt/Text Metadata 5.1.33

Group 200 | Rectangle 201 | Oval 202

### Alt/Text Metadata 5.1.33.1

Rectangle 201

### Alt/Text Metadata 5.1.33.2

Oval 202

### Shape 5.2 AutoShape 203

W0

### Alt/Text Metadata 5.2

AutoShape 203

### Alt/Text Metadata 6

Group 204 | Group 205 | Group 206 | Rectangle 207 | Freeform 208 | Rectangle 209 | Group 210 | Rectangle 211 | Freeform 212 | Group 213 | Rectangle 214 | Freeform 215 | Group 216 | Rectangle 217 | Freeform 218 | Group 219 | Rectangle 220 | Freeform 221 | Group 222 | Rectangle 223 | Freeform 224 | Group 225 | Rectangle 226 | Freeform 227 | Group 228 | Rectangle 229 | Freeform 230 | Group 231 | Rectangle 232 | Freeform 233 | Group 234 | Rectangle 235 | Freeform 236 | Group 237 | Rectangle 238 | Freeform 239 | Group 240 | Rectangle 241 | Freeform 242 | Group 243 | Rectangle 244 | Freeform 245 | Group 246 | Rectangle 247 | Freeform 248 | Group 249 | Rectangle 250 | Freeform 251 | Group 252 | Rectangle 253 | Freeform 254 | Group 255 | Rectangle 256 | Freeform 257 | Group 258 | Rectangle 259 | Freeform 260 | Group 261 | Rectangle 262 | Freeform 263 | Group 264 | Rectangle 265 | Freeform 266 | Group 267 | Rectangle 268 | Freeform 269 | Group 270 | Rectangle 271 | Freeform 272 | Group 273 | Rectangle 274 | Freeform 275 | Group 276 | Rectangle 277 | Freeform 278 | Group 279 | Rectangle 280 | Freeform 281 | Group 282 | Rectangle 283 | Freeform 284 | Group 285 | Rectangle 286 | Freeform 287 | Group 288 | Rectangle 289 | Freeform 290 | Group 291 | Rectangle 292 | Freeform 293 | Group 294 | Rectangle 295 | Freeform 296 | Group 297 | Rectangle 298 | Freeform 299 | Group 300 | Rectangle 301 | Freeform 302 | AutoShape 303

### Alt/Text Metadata 6.1

Group 205 | Group 206 | Rectangle 207 | Freeform 208 | Rectangle 209 | Group 210 | Rectangle 211 | Freeform 212 | Group 213 | Rectangle 214 | Freeform 215 | Group 216 | Rectangle 217 | Freeform 218 | Group 219 | Rectangle 220 | Freeform 221 | Group 222 | Rectangle 223 | Freeform 224 | Group 225 | Rectangle 226 | Freeform 227 | Group 228 | Rectangle 229 | Freeform 230 | Group 231 | Rectangle 232 | Freeform 233 | Group 234 | Rectangle 235 | Freeform 236 | Group 237 | Rectangle 238 | Freeform 239 | Group 240 | Rectangle 241 | Freeform 242 | Group 243 | Rectangle 244 | Freeform 245 | Group 246 | Rectangle 247 | Freeform 248 | Group 249 | Rectangle 250 | Freeform 251 | Group 252 | Rectangle 253 | Freeform 254 | Group 255 | Rectangle 256 | Freeform 257 | Group 258 | Rectangle 259 | Freeform 260 | Group 261 | Rectangle 262 | Freeform 263 | Group 264 | Rectangle 265 | Freeform 266 | Group 267 | Rectangle 268 | Freeform 269 | Group 270 | Rectangle 271 | Freeform 272 | Group 273 | Rectangle 274 | Freeform 275 | Group 276 | Rectangle 277 | Freeform 278 | Group 279 | Rectangle 280 | Freeform 281 | Group 282 | Rectangle 283 | Freeform 284 | Group 285 | Rectangle 286 | Freeform 287 | Group 288 | Rectangle 289 | Freeform 290 | Group 291 | Rectangle 292 | Freeform 293 | Group 294 | Rectangle 295 | Freeform 296 | Group 297 | Rectangle 298 | Freeform 299 | Group 300 | Rectangle 301 | Freeform 302

### Alt/Text Metadata 6.1.1

Group 206 | Rectangle 207 | Freeform 208

### Alt/Text Metadata 6.1.1.1

Rectangle 207

### Alt/Text Metadata 6.1.1.2

Freeform 208

### Alt/Text Metadata 6.1.2

Rectangle 209

### Alt/Text Metadata 6.1.3

Group 210 | Rectangle 211 | Freeform 212

### Alt/Text Metadata 6.1.3.1

Rectangle 211

### Alt/Text Metadata 6.1.3.2

Freeform 212

### Alt/Text Metadata 6.1.4

Group 213 | Rectangle 214 | Freeform 215

### Alt/Text Metadata 6.1.4.1

Rectangle 214

### Alt/Text Metadata 6.1.4.2

Freeform 215

### Alt/Text Metadata 6.1.5

Group 216 | Rectangle 217 | Freeform 218

### Alt/Text Metadata 6.1.5.1

Rectangle 217

### Alt/Text Metadata 6.1.5.2

Freeform 218

### Alt/Text Metadata 6.1.6

Group 219 | Rectangle 220 | Freeform 221

### Alt/Text Metadata 6.1.6.1

Rectangle 220

### Alt/Text Metadata 6.1.6.2

Freeform 221

### Alt/Text Metadata 6.1.7

Group 222 | Rectangle 223 | Freeform 224

### Alt/Text Metadata 6.1.7.1

Rectangle 223

### Alt/Text Metadata 6.1.7.2

Freeform 224

### Alt/Text Metadata 6.1.8

Group 225 | Rectangle 226 | Freeform 227

### Alt/Text Metadata 6.1.8.1

Rectangle 226

### Alt/Text Metadata 6.1.8.2

Freeform 227

### Alt/Text Metadata 6.1.9

Group 228 | Rectangle 229 | Freeform 230

### Alt/Text Metadata 6.1.9.1

Rectangle 229

### Alt/Text Metadata 6.1.9.2

Freeform 230

### Alt/Text Metadata 6.1.10

Group 231 | Rectangle 232 | Freeform 233

### Alt/Text Metadata 6.1.10.1

Rectangle 232

### Alt/Text Metadata 6.1.10.2

Freeform 233

### Alt/Text Metadata 6.1.11

Group 234 | Rectangle 235 | Freeform 236

### Alt/Text Metadata 6.1.11.1

Rectangle 235

### Alt/Text Metadata 6.1.11.2

Freeform 236

### Alt/Text Metadata 6.1.12

Group 237 | Rectangle 238 | Freeform 239

### Alt/Text Metadata 6.1.12.1

Rectangle 238

### Alt/Text Metadata 6.1.12.2

Freeform 239

### Alt/Text Metadata 6.1.13

Group 240 | Rectangle 241 | Freeform 242

### Alt/Text Metadata 6.1.13.1

Rectangle 241

### Alt/Text Metadata 6.1.13.2

Freeform 242

### Alt/Text Metadata 6.1.14

Group 243 | Rectangle 244 | Freeform 245

### Alt/Text Metadata 6.1.14.1

Rectangle 244

### Alt/Text Metadata 6.1.14.2

Freeform 245

### Alt/Text Metadata 6.1.15

Group 246 | Rectangle 247 | Freeform 248

### Alt/Text Metadata 6.1.15.1

Rectangle 247

### Alt/Text Metadata 6.1.15.2

Freeform 248

### Alt/Text Metadata 6.1.16

Group 249 | Rectangle 250 | Freeform 251

### Alt/Text Metadata 6.1.16.1

Rectangle 250

### Alt/Text Metadata 6.1.16.2

Freeform 251

### Alt/Text Metadata 6.1.17

Group 252 | Rectangle 253 | Freeform 254

### Alt/Text Metadata 6.1.17.1

Rectangle 253

### Alt/Text Metadata 6.1.17.2

Freeform 254

### Alt/Text Metadata 6.1.18

Group 255 | Rectangle 256 | Freeform 257

### Alt/Text Metadata 6.1.18.1

Rectangle 256

### Alt/Text Metadata 6.1.18.2

Freeform 257

### Alt/Text Metadata 6.1.19

Group 258 | Rectangle 259 | Freeform 260

### Alt/Text Metadata 6.1.19.1

Rectangle 259

### Alt/Text Metadata 6.1.19.2

Freeform 260

### Alt/Text Metadata 6.1.20

Group 261 | Rectangle 262 | Freeform 263

### Alt/Text Metadata 6.1.20.1

Rectangle 262

### Alt/Text Metadata 6.1.20.2

Freeform 263

### Alt/Text Metadata 6.1.21

Group 264 | Rectangle 265 | Freeform 266

### Alt/Text Metadata 6.1.21.1

Rectangle 265

### Alt/Text Metadata 6.1.21.2

Freeform 266

### Alt/Text Metadata 6.1.22

Group 267 | Rectangle 268 | Freeform 269

### Alt/Text Metadata 6.1.22.1

Rectangle 268

### Alt/Text Metadata 6.1.22.2

Freeform 269

### Alt/Text Metadata 6.1.23

Group 270 | Rectangle 271 | Freeform 272

### Alt/Text Metadata 6.1.23.1

Rectangle 271

### Alt/Text Metadata 6.1.23.2

Freeform 272

### Alt/Text Metadata 6.1.24

Group 273 | Rectangle 274 | Freeform 275

### Alt/Text Metadata 6.1.24.1

Rectangle 274

### Alt/Text Metadata 6.1.24.2

Freeform 275

### Alt/Text Metadata 6.1.25

Group 276 | Rectangle 277 | Freeform 278

### Alt/Text Metadata 6.1.25.1

Rectangle 277

### Alt/Text Metadata 6.1.25.2

Freeform 278

### Alt/Text Metadata 6.1.26

Group 279 | Rectangle 280 | Freeform 281

### Alt/Text Metadata 6.1.26.1

Rectangle 280

### Alt/Text Metadata 6.1.26.2

Freeform 281

### Alt/Text Metadata 6.1.27

Group 282 | Rectangle 283 | Freeform 284

### Alt/Text Metadata 6.1.27.1

Rectangle 283

### Alt/Text Metadata 6.1.27.2

Freeform 284

### Alt/Text Metadata 6.1.28

Group 285 | Rectangle 286 | Freeform 287

### Alt/Text Metadata 6.1.28.1

Rectangle 286

### Alt/Text Metadata 6.1.28.2

Freeform 287

### Alt/Text Metadata 6.1.29

Group 288 | Rectangle 289 | Freeform 290

### Alt/Text Metadata 6.1.29.1

Rectangle 289

### Alt/Text Metadata 6.1.29.2

Freeform 290

### Alt/Text Metadata 6.1.30

Group 291 | Rectangle 292 | Freeform 293

### Alt/Text Metadata 6.1.30.1

Rectangle 292

### Alt/Text Metadata 6.1.30.2

Freeform 293

### Alt/Text Metadata 6.1.31

Group 294 | Rectangle 295 | Freeform 296

### Alt/Text Metadata 6.1.31.1

Rectangle 295

### Alt/Text Metadata 6.1.31.2

Freeform 296

### Alt/Text Metadata 6.1.32

Group 297 | Rectangle 298 | Freeform 299

### Alt/Text Metadata 6.1.32.1

Rectangle 298

### Alt/Text Metadata 6.1.32.2

Freeform 299

### Alt/Text Metadata 6.1.33

Group 300 | Rectangle 301 | Freeform 302

### Alt/Text Metadata 6.1.33.1

Rectangle 301

### Alt/Text Metadata 6.1.33.2

Freeform 302

### Shape 6.2 AutoShape 303

W1

### Alt/Text Metadata 6.2

AutoShape 303

### Alt/Text Metadata 7

Group 304 | Group 305 | Group 306 | Rectangle 307 | Freeform 308 | Rectangle 309 | Group 310 | Rectangle 311 | Freeform 312 | Group 313 | Rectangle 314 | Freeform 315 | Group 316 | Rectangle 317 | Freeform 318 | Group 319 | Rectangle 320 | Freeform 321 | Group 322 | Rectangle 323 | Freeform 324 | Group 325 | Rectangle 326 | Freeform 327 | Group 328 | Rectangle 329 | Freeform 330 | Group 331 | Rectangle 332 | Freeform 333 | Group 334 | Rectangle 335 | Freeform 336 | Group 337 | Rectangle 338 | Freeform 339 | Group 340 | Rectangle 341 | Freeform 342 | Group 343 | Rectangle 344 | Freeform 345 | Group 346 | Rectangle 347 | Freeform 348 | Group 349 | Rectangle 350 | Freeform 351 | Group 352 | Rectangle 353 | Freeform 354 | Group 355 | Rectangle 356 | Freeform 357 | Group 358 | Rectangle 359 | Freeform 360 | Group 361 | Rectangle 362 | Freeform 363 | Group 364 | Rectangle 365 | Freeform 366 | Group 367 | Rectangle 368 | Freeform 369 | Group 370 | Rectangle 371 | Freeform 372 | Group 373 | Rectangle 374 | Freeform 375 | Group 376 | Rectangle 377 | Freeform 378 | Group 379 | Rectangle 380 | Freeform 381 | Group 382 | Rectangle 383 | Freeform 384 | Group 385 | Rectangle 386 | Freeform 387 | Group 388 | Rectangle 389 | Freeform 390 | Group 391 | Rectangle 392 | Freeform 393 | Group 394 | Rectangle 395 | Freeform 396 | Group 397 | Rectangle 398 | Freeform 399 | Group 400 | Rectangle 401 | Freeform 402 | AutoShape 403

### Alt/Text Metadata 7.1

Group 305 | Group 306 | Rectangle 307 | Freeform 308 | Rectangle 309 | Group 310 | Rectangle 311 | Freeform 312 | Group 313 | Rectangle 314 | Freeform 315 | Group 316 | Rectangle 317 | Freeform 318 | Group 319 | Rectangle 320 | Freeform 321 | Group 322 | Rectangle 323 | Freeform 324 | Group 325 | Rectangle 326 | Freeform 327 | Group 328 | Rectangle 329 | Freeform 330 | Group 331 | Rectangle 332 | Freeform 333 | Group 334 | Rectangle 335 | Freeform 336 | Group 337 | Rectangle 338 | Freeform 339 | Group 340 | Rectangle 341 | Freeform 342 | Group 343 | Rectangle 344 | Freeform 345 | Group 346 | Rectangle 347 | Freeform 348 | Group 349 | Rectangle 350 | Freeform 351 | Group 352 | Rectangle 353 | Freeform 354 | Group 355 | Rectangle 356 | Freeform 357 | Group 358 | Rectangle 359 | Freeform 360 | Group 361 | Rectangle 362 | Freeform 363 | Group 364 | Rectangle 365 | Freeform 366 | Group 367 | Rectangle 368 | Freeform 369 | Group 370 | Rectangle 371 | Freeform 372 | Group 373 | Rectangle 374 | Freeform 375 | Group 376 | Rectangle 377 | Freeform 378 | Group 379 | Rectangle 380 | Freeform 381 | Group 382 | Rectangle 383 | Freeform 384 | Group 385 | Rectangle 386 | Freeform 387 | Group 388 | Rectangle 389 | Freeform 390 | Group 391 | Rectangle 392 | Freeform 393 | Group 394 | Rectangle 395 | Freeform 396 | Group 397 | Rectangle 398 | Freeform 399 | Group 400 | Rectangle 401 | Freeform 402

### Alt/Text Metadata 7.1.1

Group 306 | Rectangle 307 | Freeform 308

### Alt/Text Metadata 7.1.1.1

Rectangle 307

### Alt/Text Metadata 7.1.1.2

Freeform 308

### Alt/Text Metadata 7.1.2

Rectangle 309

### Alt/Text Metadata 7.1.3

Group 310 | Rectangle 311 | Freeform 312

### Alt/Text Metadata 7.1.3.1

Rectangle 311

### Alt/Text Metadata 7.1.3.2

Freeform 312

### Alt/Text Metadata 7.1.4

Group 313 | Rectangle 314 | Freeform 315

### Alt/Text Metadata 7.1.4.1

Rectangle 314

### Alt/Text Metadata 7.1.4.2

Freeform 315

### Alt/Text Metadata 7.1.5

Group 316 | Rectangle 317 | Freeform 318

### Alt/Text Metadata 7.1.5.1

Rectangle 317

### Alt/Text Metadata 7.1.5.2

Freeform 318

### Alt/Text Metadata 7.1.6

Group 319 | Rectangle 320 | Freeform 321

### Alt/Text Metadata 7.1.6.1

Rectangle 320

### Alt/Text Metadata 7.1.6.2

Freeform 321

### Alt/Text Metadata 7.1.7

Group 322 | Rectangle 323 | Freeform 324

### Alt/Text Metadata 7.1.7.1

Rectangle 323

### Alt/Text Metadata 7.1.7.2

Freeform 324

### Alt/Text Metadata 7.1.8

Group 325 | Rectangle 326 | Freeform 327

### Alt/Text Metadata 7.1.8.1

Rectangle 326

### Alt/Text Metadata 7.1.8.2

Freeform 327

### Alt/Text Metadata 7.1.9

Group 328 | Rectangle 329 | Freeform 330

### Alt/Text Metadata 7.1.9.1

Rectangle 329

### Alt/Text Metadata 7.1.9.2

Freeform 330

### Alt/Text Metadata 7.1.10

Group 331 | Rectangle 332 | Freeform 333

### Alt/Text Metadata 7.1.10.1

Rectangle 332

### Alt/Text Metadata 7.1.10.2

Freeform 333

### Alt/Text Metadata 7.1.11

Group 334 | Rectangle 335 | Freeform 336

### Alt/Text Metadata 7.1.11.1

Rectangle 335

### Alt/Text Metadata 7.1.11.2

Freeform 336

### Alt/Text Metadata 7.1.12

Group 337 | Rectangle 338 | Freeform 339

### Alt/Text Metadata 7.1.12.1

Rectangle 338

### Alt/Text Metadata 7.1.12.2

Freeform 339

### Alt/Text Metadata 7.1.13

Group 340 | Rectangle 341 | Freeform 342

### Alt/Text Metadata 7.1.13.1

Rectangle 341

### Alt/Text Metadata 7.1.13.2

Freeform 342

### Alt/Text Metadata 7.1.14

Group 343 | Rectangle 344 | Freeform 345

### Alt/Text Metadata 7.1.14.1

Rectangle 344

### Alt/Text Metadata 7.1.14.2

Freeform 345

### Alt/Text Metadata 7.1.15

Group 346 | Rectangle 347 | Freeform 348

### Alt/Text Metadata 7.1.15.1

Rectangle 347

### Alt/Text Metadata 7.1.15.2

Freeform 348

### Alt/Text Metadata 7.1.16

Group 349 | Rectangle 350 | Freeform 351

### Alt/Text Metadata 7.1.16.1

Rectangle 350

### Alt/Text Metadata 7.1.16.2

Freeform 351

### Alt/Text Metadata 7.1.17

Group 352 | Rectangle 353 | Freeform 354

### Alt/Text Metadata 7.1.17.1

Rectangle 353

### Alt/Text Metadata 7.1.17.2

Freeform 354

### Alt/Text Metadata 7.1.18

Group 355 | Rectangle 356 | Freeform 357

### Alt/Text Metadata 7.1.18.1

Rectangle 356

### Alt/Text Metadata 7.1.18.2

Freeform 357

### Alt/Text Metadata 7.1.19

Group 358 | Rectangle 359 | Freeform 360

### Alt/Text Metadata 7.1.19.1

Rectangle 359

### Alt/Text Metadata 7.1.19.2

Freeform 360

### Alt/Text Metadata 7.1.20

Group 361 | Rectangle 362 | Freeform 363

### Alt/Text Metadata 7.1.20.1

Rectangle 362

### Alt/Text Metadata 7.1.20.2

Freeform 363

### Alt/Text Metadata 7.1.21

Group 364 | Rectangle 365 | Freeform 366

### Alt/Text Metadata 7.1.21.1

Rectangle 365

### Alt/Text Metadata 7.1.21.2

Freeform 366

### Alt/Text Metadata 7.1.22

Group 367 | Rectangle 368 | Freeform 369

### Alt/Text Metadata 7.1.22.1

Rectangle 368

### Alt/Text Metadata 7.1.22.2

Freeform 369

### Alt/Text Metadata 7.1.23

Group 370 | Rectangle 371 | Freeform 372

### Alt/Text Metadata 7.1.23.1

Rectangle 371

### Alt/Text Metadata 7.1.23.2

Freeform 372

### Alt/Text Metadata 7.1.24

Group 373 | Rectangle 374 | Freeform 375

### Alt/Text Metadata 7.1.24.1

Rectangle 374

### Alt/Text Metadata 7.1.24.2

Freeform 375

### Alt/Text Metadata 7.1.25

Group 376 | Rectangle 377 | Freeform 378

### Alt/Text Metadata 7.1.25.1

Rectangle 377

### Alt/Text Metadata 7.1.25.2

Freeform 378

### Alt/Text Metadata 7.1.26

Group 379 | Rectangle 380 | Freeform 381

### Alt/Text Metadata 7.1.26.1

Rectangle 380

### Alt/Text Metadata 7.1.26.2

Freeform 381

### Alt/Text Metadata 7.1.27

Group 382 | Rectangle 383 | Freeform 384

### Alt/Text Metadata 7.1.27.1

Rectangle 383

### Alt/Text Metadata 7.1.27.2

Freeform 384

### Alt/Text Metadata 7.1.28

Group 385 | Rectangle 386 | Freeform 387

### Alt/Text Metadata 7.1.28.1

Rectangle 386

### Alt/Text Metadata 7.1.28.2

Freeform 387

### Alt/Text Metadata 7.1.29

Group 388 | Rectangle 389 | Freeform 390

### Alt/Text Metadata 7.1.29.1

Rectangle 389

### Alt/Text Metadata 7.1.29.2

Freeform 390

### Alt/Text Metadata 7.1.30

Group 391 | Rectangle 392 | Freeform 393

### Alt/Text Metadata 7.1.30.1

Rectangle 392

### Alt/Text Metadata 7.1.30.2

Freeform 393

### Alt/Text Metadata 7.1.31

Group 394 | Rectangle 395 | Freeform 396

### Alt/Text Metadata 7.1.31.1

Rectangle 395

### Alt/Text Metadata 7.1.31.2

Freeform 396

### Alt/Text Metadata 7.1.32

Group 397 | Rectangle 398 | Freeform 399

### Alt/Text Metadata 7.1.32.1

Rectangle 398

### Alt/Text Metadata 7.1.32.2

Freeform 399

### Alt/Text Metadata 7.1.33

Group 400 | Rectangle 401 | Freeform 402

### Alt/Text Metadata 7.1.33.1

Rectangle 401

### Alt/Text Metadata 7.1.33.2

Freeform 402

### Shape 7.2 AutoShape 403

W4

### Alt/Text Metadata 7.2

AutoShape 403

### Alt/Text Metadata 8

Group 404 | Group 405 | Rectangle 406 | Group 407 | Rectangle 408 | Rectangle 409 | Group 410 | Rectangle 411 | Rectangle 412 | Group 413 | Rectangle 414 | Rectangle 415 | Group 416 | Rectangle 417 | Rectangle 418 | Group 419 | Rectangle 420 | Rectangle 421 | Group 422 | Rectangle 423 | Rectangle 424 | Group 425 | Rectangle 426 | Rectangle 427 | Group 428 | Rectangle 429 | Rectangle 430 | Group 431 | Rectangle 432 | Rectangle 433 | Group 434 | Rectangle 435 | Rectangle 436 | Group 437 | Rectangle 438 | Rectangle 439 | Group 440 | Rectangle 441 | Rectangle 442 | Group 443 | Rectangle 444 | Rectangle 445 | Group 446 | Rectangle 447 | Rectangle 448 | Group 449 | Rectangle 450 | Rectangle 451 | Group 452 | Rectangle 453 | Rectangle 454 | Group 455 | Rectangle 456 | Rectangle 457 | Group 458 | Rectangle 459 | Rectangle 460 | Group 461 | Rectangle 462 | Rectangle 463 | Group 464 | Rectangle 465 | Rectangle 466 | Group 467 | Rectangle 468 | Rectangle 469 | Group 470 | Rectangle 471 | Rectangle 472 | Group 473 | Rectangle 474 | Rectangle 475 | Group 476 | Rectangle 477 | Rectangle 478 | Group 479 | Rectangle 480 | Rectangle 481 | Group 482 | Rectangle 483 | Rectangle 484 | Group 485 | Rectangle 486 | Rectangle 487 | Group 488 | Rectangle 489 | Rectangle 490 | Group 491 | Rectangle 492 | Rectangle 493 | Group 494 | Rectangle 495 | Rectangle 496 | Group 497 | Rectangle 498 | Rectangle 499 | Group 500 | Rectangle 501 | Rectangle 502 | AutoShape 503

### Alt/Text Metadata 8.1

Group 405 | Rectangle 406 | Group 407 | Rectangle 408 | Rectangle 409 | Group 410 | Rectangle 411 | Rectangle 412 | Group 413 | Rectangle 414 | Rectangle 415 | Group 416 | Rectangle 417 | Rectangle 418 | Group 419 | Rectangle 420 | Rectangle 421 | Group 422 | Rectangle 423 | Rectangle 424 | Group 425 | Rectangle 426 | Rectangle 427 | Group 428 | Rectangle 429 | Rectangle 430 | Group 431 | Rectangle 432 | Rectangle 433 | Group 434 | Rectangle 435 | Rectangle 436 | Group 437 | Rectangle 438 | Rectangle 439 | Group 440 | Rectangle 441 | Rectangle 442 | Group 443 | Rectangle 444 | Rectangle 445 | Group 446 | Rectangle 447 | Rectangle 448 | Group 449 | Rectangle 450 | Rectangle 451 | Group 452 | Rectangle 453 | Rectangle 454 | Group 455 | Rectangle 456 | Rectangle 457 | Group 458 | Rectangle 459 | Rectangle 460 | Group 461 | Rectangle 462 | Rectangle 463 | Group 464 | Rectangle 465 | Rectangle 466 | Group 467 | Rectangle 468 | Rectangle 469 | Group 470 | Rectangle 471 | Rectangle 472 | Group 473 | Rectangle 474 | Rectangle 475 | Group 476 | Rectangle 477 | Rectangle 478 | Group 479 | Rectangle 480 | Rectangle 481 | Group 482 | Rectangle 483 | Rectangle 484 | Group 485 | Rectangle 486 | Rectangle 487 | Group 488 | Rectangle 489 | Rectangle 490 | Group 491 | Rectangle 492 | Rectangle 493 | Group 494 | Rectangle 495 | Rectangle 496 | Group 497 | Rectangle 498 | Rectangle 499 | Group 500 | Rectangle 501 | Rectangle 502

### Alt/Text Metadata 8.1.1

Rectangle 406

### Alt/Text Metadata 8.1.2

Group 407 | Rectangle 408 | Rectangle 409

### Alt/Text Metadata 8.1.2.1

Rectangle 408

### Alt/Text Metadata 8.1.2.2

Rectangle 409

### Alt/Text Metadata 8.1.3

Group 410 | Rectangle 411 | Rectangle 412

### Alt/Text Metadata 8.1.3.1

Rectangle 411

### Alt/Text Metadata 8.1.3.2

Rectangle 412

### Alt/Text Metadata 8.1.4

Group 413 | Rectangle 414 | Rectangle 415

### Alt/Text Metadata 8.1.4.1

Rectangle 414

### Alt/Text Metadata 8.1.4.2

Rectangle 415

### Alt/Text Metadata 8.1.5

Group 416 | Rectangle 417 | Rectangle 418

### Alt/Text Metadata 8.1.5.1

Rectangle 417

### Alt/Text Metadata 8.1.5.2

Rectangle 418

### Alt/Text Metadata 8.1.6

Group 419 | Rectangle 420 | Rectangle 421

### Alt/Text Metadata 8.1.6.1

Rectangle 420

### Alt/Text Metadata 8.1.6.2

Rectangle 421

### Alt/Text Metadata 8.1.7

Group 422 | Rectangle 423 | Rectangle 424

### Alt/Text Metadata 8.1.7.1

Rectangle 423

### Alt/Text Metadata 8.1.7.2

Rectangle 424

### Alt/Text Metadata 8.1.8

Group 425 | Rectangle 426 | Rectangle 427

### Alt/Text Metadata 8.1.8.1

Rectangle 426

### Alt/Text Metadata 8.1.8.2

Rectangle 427

### Alt/Text Metadata 8.1.9

Group 428 | Rectangle 429 | Rectangle 430

### Alt/Text Metadata 8.1.9.1

Rectangle 429

### Alt/Text Metadata 8.1.9.2

Rectangle 430

### Alt/Text Metadata 8.1.10

Group 431 | Rectangle 432 | Rectangle 433

### Alt/Text Metadata 8.1.10.1

Rectangle 432

### Alt/Text Metadata 8.1.10.2

Rectangle 433

### Alt/Text Metadata 8.1.11

Group 434 | Rectangle 435 | Rectangle 436

### Alt/Text Metadata 8.1.11.1

Rectangle 435

### Alt/Text Metadata 8.1.11.2

Rectangle 436

### Alt/Text Metadata 8.1.12

Group 437 | Rectangle 438 | Rectangle 439

### Alt/Text Metadata 8.1.12.1

Rectangle 438

### Alt/Text Metadata 8.1.12.2

Rectangle 439

### Alt/Text Metadata 8.1.13

Group 440 | Rectangle 441 | Rectangle 442

### Alt/Text Metadata 8.1.13.1

Rectangle 441

### Alt/Text Metadata 8.1.13.2

Rectangle 442

### Alt/Text Metadata 8.1.14

Group 443 | Rectangle 444 | Rectangle 445

### Alt/Text Metadata 8.1.14.1

Rectangle 444

### Alt/Text Metadata 8.1.14.2

Rectangle 445

### Alt/Text Metadata 8.1.15

Group 446 | Rectangle 447 | Rectangle 448

### Alt/Text Metadata 8.1.15.1

Rectangle 447

### Alt/Text Metadata 8.1.15.2

Rectangle 448

### Alt/Text Metadata 8.1.16

Group 449 | Rectangle 450 | Rectangle 451

### Alt/Text Metadata 8.1.16.1

Rectangle 450

### Alt/Text Metadata 8.1.16.2

Rectangle 451

### Alt/Text Metadata 8.1.17

Group 452 | Rectangle 453 | Rectangle 454

### Alt/Text Metadata 8.1.17.1

Rectangle 453

### Alt/Text Metadata 8.1.17.2

Rectangle 454

### Alt/Text Metadata 8.1.18

Group 455 | Rectangle 456 | Rectangle 457

### Alt/Text Metadata 8.1.18.1

Rectangle 456

### Alt/Text Metadata 8.1.18.2

Rectangle 457

### Alt/Text Metadata 8.1.19

Group 458 | Rectangle 459 | Rectangle 460

### Alt/Text Metadata 8.1.19.1

Rectangle 459

### Alt/Text Metadata 8.1.19.2

Rectangle 460

### Alt/Text Metadata 8.1.20

Group 461 | Rectangle 462 | Rectangle 463

### Alt/Text Metadata 8.1.20.1

Rectangle 462

### Alt/Text Metadata 8.1.20.2

Rectangle 463

### Alt/Text Metadata 8.1.21

Group 464 | Rectangle 465 | Rectangle 466

### Alt/Text Metadata 8.1.21.1

Rectangle 465

### Alt/Text Metadata 8.1.21.2

Rectangle 466

### Alt/Text Metadata 8.1.22

Group 467 | Rectangle 468 | Rectangle 469

### Alt/Text Metadata 8.1.22.1

Rectangle 468

### Alt/Text Metadata 8.1.22.2

Rectangle 469

### Alt/Text Metadata 8.1.23

Group 470 | Rectangle 471 | Rectangle 472

### Alt/Text Metadata 8.1.23.1

Rectangle 471

### Alt/Text Metadata 8.1.23.2

Rectangle 472

### Alt/Text Metadata 8.1.24

Group 473 | Rectangle 474 | Rectangle 475

### Alt/Text Metadata 8.1.24.1

Rectangle 474

### Alt/Text Metadata 8.1.24.2

Rectangle 475

### Alt/Text Metadata 8.1.25

Group 476 | Rectangle 477 | Rectangle 478

### Alt/Text Metadata 8.1.25.1

Rectangle 477

### Alt/Text Metadata 8.1.25.2

Rectangle 478

### Alt/Text Metadata 8.1.26

Group 479 | Rectangle 480 | Rectangle 481

### Alt/Text Metadata 8.1.26.1

Rectangle 480

### Alt/Text Metadata 8.1.26.2

Rectangle 481

### Alt/Text Metadata 8.1.27

Group 482 | Rectangle 483 | Rectangle 484

### Alt/Text Metadata 8.1.27.1

Rectangle 483

### Alt/Text Metadata 8.1.27.2

Rectangle 484

### Alt/Text Metadata 8.1.28

Group 485 | Rectangle 486 | Rectangle 487

### Alt/Text Metadata 8.1.28.1

Rectangle 486

### Alt/Text Metadata 8.1.28.2

Rectangle 487

### Alt/Text Metadata 8.1.29

Group 488 | Rectangle 489 | Rectangle 490

### Alt/Text Metadata 8.1.29.1

Rectangle 489

### Alt/Text Metadata 8.1.29.2

Rectangle 490

### Alt/Text Metadata 8.1.30

Group 491 | Rectangle 492 | Rectangle 493

### Alt/Text Metadata 8.1.30.1

Rectangle 492

### Alt/Text Metadata 8.1.30.2

Rectangle 493

### Alt/Text Metadata 8.1.31

Group 494 | Rectangle 495 | Rectangle 496

### Alt/Text Metadata 8.1.31.1

Rectangle 495

### Alt/Text Metadata 8.1.31.2

Rectangle 496

### Alt/Text Metadata 8.1.32

Group 497 | Rectangle 498 | Rectangle 499

### Alt/Text Metadata 8.1.32.1

Rectangle 498

### Alt/Text Metadata 8.1.32.2

Rectangle 499

### Alt/Text Metadata 8.1.33

Group 500 | Rectangle 501 | Rectangle 502

### Alt/Text Metadata 8.1.33.1

Rectangle 501

### Alt/Text Metadata 8.1.33.2

Rectangle 502

### Shape 8.2 AutoShape 503

W2

### Alt/Text Metadata 8.2

AutoShape 503

### Alt/Text Metadata 9

Group 504 | Group 505 | Rectangle 506 | Group 507 | Rectangle 508 | Rectangle 509 | Group 510 | Rectangle 511 | Rectangle 512 | Group 513 | Rectangle 514 | Rectangle 515 | Group 516 | Rectangle 517 | Rectangle 518 | Group 519 | Rectangle 520 | Rectangle 521 | Group 522 | Rectangle 523 | Rectangle 524 | Group 525 | Rectangle 526 | Rectangle 527 | Group 528 | Rectangle 529 | Rectangle 530 | Group 531 | Rectangle 532 | Rectangle 533 | Group 534 | Rectangle 535 | Rectangle 536 | Group 537 | Rectangle 538 | Rectangle 539 | Group 540 | Rectangle 541 | Rectangle 542 | Group 543 | Rectangle 544 | Rectangle 545 | Group 546 | Rectangle 547 | Rectangle 548 | Group 549 | Rectangle 550 | Rectangle 551 | Group 552 | Rectangle 553 | Rectangle 554 | Group 555 | Rectangle 556 | Rectangle 557 | Group 558 | Rectangle 559 | Rectangle 560 | Group 561 | Rectangle 562 | Rectangle 563 | Group 564 | Rectangle 565 | Rectangle 566 | Group 567 | Rectangle 568 | Rectangle 569 | Group 570 | Rectangle 571 | Rectangle 572 | Group 573 | Rectangle 574 | Rectangle 575 | Group 576 | Rectangle 577 | Rectangle 578 | Group 579 | Rectangle 580 | Rectangle 581 | Group 582 | Rectangle 583 | Rectangle 584 | Group 585 | Rectangle 586 | Rectangle 587 | Group 588 | Rectangle 589 | Rectangle 590 | Group 591 | Rectangle 592 | Rectangle 593 | Group 594 | Rectangle 595 | Rectangle 596 | Group 597 | Rectangle 598 | Rectangle 599 | Group 600 | Rectangle 601 | Rectangle 602 | AutoShape 603

### Alt/Text Metadata 9.1

Group 505 | Rectangle 506 | Group 507 | Rectangle 508 | Rectangle 509 | Group 510 | Rectangle 511 | Rectangle 512 | Group 513 | Rectangle 514 | Rectangle 515 | Group 516 | Rectangle 517 | Rectangle 518 | Group 519 | Rectangle 520 | Rectangle 521 | Group 522 | Rectangle 523 | Rectangle 524 | Group 525 | Rectangle 526 | Rectangle 527 | Group 528 | Rectangle 529 | Rectangle 530 | Group 531 | Rectangle 532 | Rectangle 533 | Group 534 | Rectangle 535 | Rectangle 536 | Group 537 | Rectangle 538 | Rectangle 539 | Group 540 | Rectangle 541 | Rectangle 542 | Group 543 | Rectangle 544 | Rectangle 545 | Group 546 | Rectangle 547 | Rectangle 548 | Group 549 | Rectangle 550 | Rectangle 551 | Group 552 | Rectangle 553 | Rectangle 554 | Group 555 | Rectangle 556 | Rectangle 557 | Group 558 | Rectangle 559 | Rectangle 560 | Group 561 | Rectangle 562 | Rectangle 563 | Group 564 | Rectangle 565 | Rectangle 566 | Group 567 | Rectangle 568 | Rectangle 569 | Group 570 | Rectangle 571 | Rectangle 572 | Group 573 | Rectangle 574 | Rectangle 575 | Group 576 | Rectangle 577 | Rectangle 578 | Group 579 | Rectangle 580 | Rectangle 581 | Group 582 | Rectangle 583 | Rectangle 584 | Group 585 | Rectangle 586 | Rectangle 587 | Group 588 | Rectangle 589 | Rectangle 590 | Group 591 | Rectangle 592 | Rectangle 593 | Group 594 | Rectangle 595 | Rectangle 596 | Group 597 | Rectangle 598 | Rectangle 599 | Group 600 | Rectangle 601 | Rectangle 602

### Alt/Text Metadata 9.1.1

Rectangle 506

### Alt/Text Metadata 9.1.2

Group 507 | Rectangle 508 | Rectangle 509

### Alt/Text Metadata 9.1.2.1

Rectangle 508

### Alt/Text Metadata 9.1.2.2

Rectangle 509

### Alt/Text Metadata 9.1.3

Group 510 | Rectangle 511 | Rectangle 512

### Alt/Text Metadata 9.1.3.1

Rectangle 511

### Alt/Text Metadata 9.1.3.2

Rectangle 512

### Alt/Text Metadata 9.1.4

Group 513 | Rectangle 514 | Rectangle 515

### Alt/Text Metadata 9.1.4.1

Rectangle 514

### Alt/Text Metadata 9.1.4.2

Rectangle 515

### Alt/Text Metadata 9.1.5

Group 516 | Rectangle 517 | Rectangle 518

### Alt/Text Metadata 9.1.5.1

Rectangle 517

### Alt/Text Metadata 9.1.5.2

Rectangle 518

### Alt/Text Metadata 9.1.6

Group 519 | Rectangle 520 | Rectangle 521

### Alt/Text Metadata 9.1.6.1

Rectangle 520

### Alt/Text Metadata 9.1.6.2

Rectangle 521

### Alt/Text Metadata 9.1.7

Group 522 | Rectangle 523 | Rectangle 524

### Alt/Text Metadata 9.1.7.1

Rectangle 523

### Alt/Text Metadata 9.1.7.2

Rectangle 524

### Alt/Text Metadata 9.1.8

Group 525 | Rectangle 526 | Rectangle 527

### Alt/Text Metadata 9.1.8.1

Rectangle 526

### Alt/Text Metadata 9.1.8.2

Rectangle 527

### Alt/Text Metadata 9.1.9

Group 528 | Rectangle 529 | Rectangle 530

### Alt/Text Metadata 9.1.9.1

Rectangle 529

### Alt/Text Metadata 9.1.9.2

Rectangle 530

### Alt/Text Metadata 9.1.10

Group 531 | Rectangle 532 | Rectangle 533

### Alt/Text Metadata 9.1.10.1

Rectangle 532

### Alt/Text Metadata 9.1.10.2

Rectangle 533

### Alt/Text Metadata 9.1.11

Group 534 | Rectangle 535 | Rectangle 536

### Alt/Text Metadata 9.1.11.1

Rectangle 535

### Alt/Text Metadata 9.1.11.2

Rectangle 536

### Alt/Text Metadata 9.1.12

Group 537 | Rectangle 538 | Rectangle 539

### Alt/Text Metadata 9.1.12.1

Rectangle 538

### Alt/Text Metadata 9.1.12.2

Rectangle 539

### Alt/Text Metadata 9.1.13

Group 540 | Rectangle 541 | Rectangle 542

### Alt/Text Metadata 9.1.13.1

Rectangle 541

### Alt/Text Metadata 9.1.13.2

Rectangle 542

### Alt/Text Metadata 9.1.14

Group 543 | Rectangle 544 | Rectangle 545

### Alt/Text Metadata 9.1.14.1

Rectangle 544

### Alt/Text Metadata 9.1.14.2

Rectangle 545

### Alt/Text Metadata 9.1.15

Group 546 | Rectangle 547 | Rectangle 548

### Alt/Text Metadata 9.1.15.1

Rectangle 547

### Alt/Text Metadata 9.1.15.2

Rectangle 548

### Alt/Text Metadata 9.1.16

Group 549 | Rectangle 550 | Rectangle 551

### Alt/Text Metadata 9.1.16.1

Rectangle 550

### Alt/Text Metadata 9.1.16.2

Rectangle 551

### Alt/Text Metadata 9.1.17

Group 552 | Rectangle 553 | Rectangle 554

### Alt/Text Metadata 9.1.17.1

Rectangle 553

### Alt/Text Metadata 9.1.17.2

Rectangle 554

### Alt/Text Metadata 9.1.18

Group 555 | Rectangle 556 | Rectangle 557

### Alt/Text Metadata 9.1.18.1

Rectangle 556

### Alt/Text Metadata 9.1.18.2

Rectangle 557

### Alt/Text Metadata 9.1.19

Group 558 | Rectangle 559 | Rectangle 560

### Alt/Text Metadata 9.1.19.1

Rectangle 559

### Alt/Text Metadata 9.1.19.2

Rectangle 560

### Alt/Text Metadata 9.1.20

Group 561 | Rectangle 562 | Rectangle 563

### Alt/Text Metadata 9.1.20.1

Rectangle 562

### Alt/Text Metadata 9.1.20.2

Rectangle 563

### Alt/Text Metadata 9.1.21

Group 564 | Rectangle 565 | Rectangle 566

### Alt/Text Metadata 9.1.21.1

Rectangle 565

### Alt/Text Metadata 9.1.21.2

Rectangle 566

### Alt/Text Metadata 9.1.22

Group 567 | Rectangle 568 | Rectangle 569

### Alt/Text Metadata 9.1.22.1

Rectangle 568

### Alt/Text Metadata 9.1.22.2

Rectangle 569

### Alt/Text Metadata 9.1.23

Group 570 | Rectangle 571 | Rectangle 572

### Alt/Text Metadata 9.1.23.1

Rectangle 571

### Alt/Text Metadata 9.1.23.2

Rectangle 572

### Alt/Text Metadata 9.1.24

Group 573 | Rectangle 574 | Rectangle 575

### Alt/Text Metadata 9.1.24.1

Rectangle 574

### Alt/Text Metadata 9.1.24.2

Rectangle 575

### Alt/Text Metadata 9.1.25

Group 576 | Rectangle 577 | Rectangle 578

### Alt/Text Metadata 9.1.25.1

Rectangle 577

### Alt/Text Metadata 9.1.25.2

Rectangle 578

### Alt/Text Metadata 9.1.26

Group 579 | Rectangle 580 | Rectangle 581

### Alt/Text Metadata 9.1.26.1

Rectangle 580

### Alt/Text Metadata 9.1.26.2

Rectangle 581

### Alt/Text Metadata 9.1.27

Group 582 | Rectangle 583 | Rectangle 584

### Alt/Text Metadata 9.1.27.1

Rectangle 583

### Alt/Text Metadata 9.1.27.2

Rectangle 584

### Alt/Text Metadata 9.1.28

Group 585 | Rectangle 586 | Rectangle 587

### Alt/Text Metadata 9.1.28.1

Rectangle 586

### Alt/Text Metadata 9.1.28.2

Rectangle 587

### Alt/Text Metadata 9.1.29

Group 588 | Rectangle 589 | Rectangle 590

### Alt/Text Metadata 9.1.29.1

Rectangle 589

### Alt/Text Metadata 9.1.29.2

Rectangle 590

### Alt/Text Metadata 9.1.30

Group 591 | Rectangle 592 | Rectangle 593

### Alt/Text Metadata 9.1.30.1

Rectangle 592

### Alt/Text Metadata 9.1.30.2

Rectangle 593

### Alt/Text Metadata 9.1.31

Group 594 | Rectangle 595 | Rectangle 596

### Alt/Text Metadata 9.1.31.1

Rectangle 595

### Alt/Text Metadata 9.1.31.2

Rectangle 596

### Alt/Text Metadata 9.1.32

Group 597 | Rectangle 598 | Rectangle 599

### Alt/Text Metadata 9.1.32.1

Rectangle 598

### Alt/Text Metadata 9.1.32.2

Rectangle 599

### Alt/Text Metadata 9.1.33

Group 600 | Rectangle 601 | Rectangle 602

### Alt/Text Metadata 9.1.33.1

Rectangle 601

### Alt/Text Metadata 9.1.33.2

Rectangle 602

### Shape 9.2 AutoShape 603

W5

### Alt/Text Metadata 9.2

AutoShape 603

### Shape 10 Text Box 604

Load Unit

### Alt/Text Metadata 10

Text Box 604

### Shape 11 Text Box 605

Multiply Unit

### Alt/Text Metadata 11

Text Box 605

### Shape 12 Text Box 606

Add Unit

### Alt/Text Metadata 12

Text Box 606

### Alt/Text Metadata 13

Line 607

### Shape 14 Text Box 608

time

### Alt/Text Metadata 14

Text Box 608

### Shape 15 AutoShape 609

Warp issue

### Alt/Text Metadata 15

AutoShape 609

### Shape 16 TextBox 610

Slide credit: Krste Asanovic

### Alt/Text Metadata 16

TextBox 610

### Notes XML fallback texts

- 27

## Slide 11

### Shape 1 矩形 25

Motivation of In-network Computing

### Alt/Text Metadata 1

矩形 25

### Alt/Text Metadata 2

Rectangle 2

### Shape 3 TextBox 3

SIMT is not SIMD!

### Alt/Text Metadata 3

TextBox 3

### Notes XML fallback texts

- 29

## Slide 12

### Shape 1 Title 2

Recall: SIMT Code vs. SIMD Code

### Alt/Text Metadata 1

Title 2

### Shape 2 Rounded Rectangle 20

for (ii = 0; ii < 100000; ++ii) {
C[ii] = A[ii] + B[ii];
}

### Alt/Text Metadata 2

Rounded Rectangle 20

### Shape 3 Rounded Rectangle 21

// there are 100000 threads
__global__ void KernelFunction(…) {
  int tid = blockDim.x * blockIdx.x + threadIdx.x;
  int varA = aa[tid];
  int varB = bb[tid];
  C[tid] = varA + varB;
}

### Alt/Text Metadata 3

Rounded Rectangle 21

### Alt/Text Metadata 4

Down Arrow 22

### Shape 5 TextBox 23

CPU scalar code

### Alt/Text Metadata 5

TextBox 23

### Shape 6 TextBox 24

CUDA code

### Alt/Text Metadata 6

TextBox 24

### Shape 7 TextBox 134

Slide credit: Hyesoon Kim

### Alt/Text Metadata 7

TextBox 134

### Shape 8 Slide Number Placeholder 3

12

### Alt/Text Metadata 8

Slide Number Placeholder 3

### Shape 9 Rounded Rectangle 21

// there are 25000 loops with SIMD=4
…
v_A = vec_load (A);
v_B = vec_load (B);
 v_C = vec_add(v_A, v_B);
Vec_store(v_C, C)
…
}

### Shape 10 TextBox 23

CPU vector code

### Notes XML fallback texts

- 31

## Slide 13

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

13

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

### Notes XML fallback texts

- With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread
- ’
- s warp from the pool of
- “
- ready
- ”
- warps and thereby allows other threads to proceed while the memory system processes its request.
- With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.
- 32

## Slide 14

### Shape 1 Rectangle 4

GPU Memories

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- 34

## Slide 15

### Shape 1 Title 1

Memory in the GPU Architecture

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

15

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Group 62 | TextBox 8 | Rectangle 82 | Rectangle 83 | Rectangle 84 | Rectangle 85 | Rectangle 86 | Rectangle 87 | Rectangle 88 | Rectangle 89 | Rectangle 90 | Rectangle 91 | Rectangle 92 | Rectangle 93 | Rectangle 94 | Rectangle 95 | Rectangle 96 | Rectangle 97 | Rectangle 98 | Rectangle 99 | Rectangle 100 | Rectangle 101 | Rectangle 102 | Rectangle 103 | Rectangle 104 | Rectangle 105 | Rectangle 106 | Rectangle 107 | Rectangle 108 | Rectangle 109 | Rectangle 110 | Rectangle 111

### Shape 3.1 TextBox 8

…

### Alt/Text Metadata 3.1

TextBox 8

### Shape 3.2 Rectangle 82

SM

### Alt/Text Metadata 3.2

Rectangle 82

### Shape 3.3 Rectangle 83

Core

### Alt/Text Metadata 3.3

Rectangle 83

### Shape 3.4 Rectangle 84

Control

### Alt/Text Metadata 3.4

Rectangle 84

### Alt/Text Metadata 3.5

Rectangle 85

### Alt/Text Metadata 3.6

Rectangle 86

### Alt/Text Metadata 3.7

Rectangle 87

### Alt/Text Metadata 3.8

Rectangle 88

### Alt/Text Metadata 3.9

Rectangle 89

### Alt/Text Metadata 3.10

Rectangle 90

### Alt/Text Metadata 3.11

Rectangle 91

### Alt/Text Metadata 3.12

Rectangle 92

### Alt/Text Metadata 3.13

Rectangle 93

### Alt/Text Metadata 3.14

Rectangle 94

### Alt/Text Metadata 3.15

Rectangle 95

### Alt/Text Metadata 3.16

Rectangle 96

### Alt/Text Metadata 3.17

Rectangle 97

### Alt/Text Metadata 3.18

Rectangle 98

### Alt/Text Metadata 3.19

Rectangle 99

### Alt/Text Metadata 3.20

Rectangle 100

### Alt/Text Metadata 3.21

Rectangle 101

### Alt/Text Metadata 3.22

Rectangle 102

### Alt/Text Metadata 3.23

Rectangle 103

### Alt/Text Metadata 3.24

Rectangle 104

### Alt/Text Metadata 3.25

Rectangle 105

### Alt/Text Metadata 3.26

Rectangle 106

### Alt/Text Metadata 3.27

Rectangle 107

### Alt/Text Metadata 3.28

Rectangle 108

### Alt/Text Metadata 3.29

Rectangle 109

### Alt/Text Metadata 3.30

Rectangle 110

### Alt/Text Metadata 3.31

Rectangle 111

### Shape 4 Rectangle 63

L2 Cache

### Alt/Text Metadata 4

Rectangle 63

### Shape 5 Rectangle 64

Global Memory

### Alt/Text Metadata 5

Rectangle 64

### Shape 6 Rectangle 65

Registers

### Alt/Text Metadata 6

Rectangle 65

### Shape 7 Rectangle 66

Shared Memory

### Alt/Text Metadata 7

Rectangle 66

### Shape 8 Rectangle 67

L1 Cache

### Alt/Text Metadata 8

Rectangle 67

### Shape 9 Rectangle 68

Constant Cache

### Alt/Text Metadata 9

Rectangle 68

### Alt/Text Metadata 10

Rectangle 69

### Alt/Text Metadata 11

Rectangle 70

### Alt/Text Metadata 12

Rectangle 71

### Alt/Text Metadata 13

Rectangle 72

### Alt/Text Metadata 14

Rectangle 73

### Alt/Text Metadata 15

Rectangle 74

### Alt/Text Metadata 16

Rectangle 75

### Alt/Text Metadata 17

Rectangle 76

### Shape 18 TextBox 2

≈1 cycle

### Alt/Text Metadata 18

TextBox 2

### Shape 19 TextBox 54

≈5 cycles

### Alt/Text Metadata 19

TextBox 54

### Alt/Text Metadata 20

TextBox 57

### Shape 21 TextBox 59

≈500 cycles

### Alt/Text Metadata 21

TextBox 59

### Shape 22 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 22

TextBox 610

### Notes XML fallback texts

- 40

## Slide 16

### Shape 1 Title 1

Memory in the GPU Architecture

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

16

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Group 62 | TextBox 8 | Rectangle 82 | Rectangle 83 | Rectangle 84 | Rectangle 85 | Rectangle 86 | Rectangle 87 | Rectangle 88 | Rectangle 89 | Rectangle 90 | Rectangle 91 | Rectangle 92 | Rectangle 93 | Rectangle 94 | Rectangle 95 | Rectangle 96 | Rectangle 97 | Rectangle 98 | Rectangle 99 | Rectangle 100 | Rectangle 101 | Rectangle 102 | Rectangle 103 | Rectangle 104 | Rectangle 105 | Rectangle 106 | Rectangle 107 | Rectangle 108 | Rectangle 109 | Rectangle 110 | Rectangle 111

### Shape 3.1 TextBox 8

…

### Alt/Text Metadata 3.1

TextBox 8

### Shape 3.2 Rectangle 82

SM

### Alt/Text Metadata 3.2

Rectangle 82

### Shape 3.3 Rectangle 83

Core

### Alt/Text Metadata 3.3

Rectangle 83

### Shape 3.4 Rectangle 84

Control

### Alt/Text Metadata 3.4

Rectangle 84

### Alt/Text Metadata 3.5

Rectangle 85

### Alt/Text Metadata 3.6

Rectangle 86

### Alt/Text Metadata 3.7

Rectangle 87

### Alt/Text Metadata 3.8

Rectangle 88

### Alt/Text Metadata 3.9

Rectangle 89

### Alt/Text Metadata 3.10

Rectangle 90

### Alt/Text Metadata 3.11

Rectangle 91

### Alt/Text Metadata 3.12

Rectangle 92

### Alt/Text Metadata 3.13

Rectangle 93

### Alt/Text Metadata 3.14

Rectangle 94

### Alt/Text Metadata 3.15

Rectangle 95

### Alt/Text Metadata 3.16

Rectangle 96

### Alt/Text Metadata 3.17

Rectangle 97

### Alt/Text Metadata 3.18

Rectangle 98

### Alt/Text Metadata 3.19

Rectangle 99

### Alt/Text Metadata 3.20

Rectangle 100

### Alt/Text Metadata 3.21

Rectangle 101

### Alt/Text Metadata 3.22

Rectangle 102

### Alt/Text Metadata 3.23

Rectangle 103

### Alt/Text Metadata 3.24

Rectangle 104

### Alt/Text Metadata 3.25

Rectangle 105

### Alt/Text Metadata 3.26

Rectangle 106

### Alt/Text Metadata 3.27

Rectangle 107

### Alt/Text Metadata 3.28

Rectangle 108

### Alt/Text Metadata 3.29

Rectangle 109

### Alt/Text Metadata 3.30

Rectangle 110

### Alt/Text Metadata 3.31

Rectangle 111

### Shape 4 Rectangle 63

L2 Cache

### Alt/Text Metadata 4

Rectangle 63

### Shape 5 Rectangle 64

Global Memory

### Alt/Text Metadata 5

Rectangle 64

### Shape 6 Rectangle 65

Registers

### Alt/Text Metadata 6

Rectangle 65

### Shape 7 Rectangle 66

Shared Memory

### Alt/Text Metadata 7

Rectangle 66

### Shape 8 Rectangle 67

L1 Cache

### Alt/Text Metadata 8

Rectangle 67

### Shape 9 Rectangle 68

Constant Cache

### Alt/Text Metadata 9

Rectangle 68

### Alt/Text Metadata 10

Rectangle 69

### Alt/Text Metadata 11

Rectangle 70

### Alt/Text Metadata 12

Rectangle 71

### Alt/Text Metadata 13

Rectangle 72

### Alt/Text Metadata 14

Rectangle 73

### Alt/Text Metadata 15

Rectangle 74

### Alt/Text Metadata 16

Rectangle 75

### Alt/Text Metadata 17

Rectangle 76

### Shape 18 TextBox 2

≈1 cycle

### Alt/Text Metadata 18

TextBox 2

### Shape 19 TextBox 54

≈5 cycles

### Alt/Text Metadata 19

TextBox 54

### Alt/Text Metadata 20

TextBox 57

### Shape 21 TextBox 59

≈500 cycles

### Alt/Text Metadata 21

TextBox 59

### Shape 22 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 22

TextBox 610

### Shape 23 TextBox 10

50 MB

### Alt/Text Metadata 23

TextBox 10

### Shape 24 TextBox 113

80 GB

### Alt/Text Metadata 24

TextBox 113

### Alt/Text Metadata 25

Group 12 | Straight Arrow Connector 2 | TextBox 115

### Alt/Text Metadata 25.1

Straight Arrow Connector 2

### Shape 25.2 TextBox 115

Direct copy

### Alt/Text Metadata 25.2

TextBox 115

### Alt/Text Metadata 26

Group 11 | TextBox 114 | Straight Arrow Connector 118 | Straight Arrow Connector 119 | Straight Arrow Connector 120 | Straight Arrow Connector 121

### Shape 26.1 TextBox 114

3 TB/s

### Alt/Text Metadata 26.1

TextBox 114

### Alt/Text Metadata 26.2

Straight Arrow Connector 118

### Alt/Text Metadata 26.3

Straight Arrow Connector 119

### Alt/Text Metadata 26.4

Straight Arrow Connector 120

### Alt/Text Metadata 26.5

Straight Arrow Connector 121

### Speaker notes

HBM3 memory subsystem provides nearly a 2x bandwidth increase over the previous generation. The H100 SXM5 GPU is the world’s first GPU with HBM3 memory delivering a class-leading 3 TB/sec of memory bandwidth.
50 MB L2 cache architecture caches large portions of models and datasets for repeated access, reducing trips to HBM3.
SM： streaming multiprocessor

## Slide 17

### Shape 1 Content Placeholder 2

Example of data movement between GPU global memory (DRAM) and GPU cores.

### Alt/Text Metadata 1

Content Placeholder 2

### Alt/Text Metadata 2

Picture 1

### Relationships 2

- rId3: image:../media/image13.emf

### Shape 3 Title 1

NVIDIA V100 & A100 Memory Hierarchy

### Alt/Text Metadata 3

Title 1

### Shape 4 Content Placeholder 2

A100 feature:
Direct copy from L2 to scratchpad, bypassing L1 and register file.

### Shape 5 Slide Number Placeholder 3

17

### Alt/Text Metadata 5

Slide Number Placeholder 3

### Shape 6 TextBox 10

https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf

### Alt/Text Metadata 6

TextBox 10

### Speaker notes

A100: New load instruction that copies from global memory (DRAM) to shared memory (scratchpad) directly, without having to use registers (i.e., no need to copy from global memory to register and then from register to shared memory).

### Slide media/diagram relationships

- rId3: image:../media/image13.emf

## Slide 18

### Shape 1 Rectangle 2

CUDA Variable Type Qualifiers

### Alt/Text Metadata 1

Rectangle 2

### Shape 2 Rectangle 3

__device__ is optional when used with __shared__, or  __constant__
Recall cudaMalloc(…) allocates memory from the host
Constant memory can also be allocated and initialized from the host
Automatic variables without any qualifier reside in a register
Except arrays that reside in global memory

### Alt/Text Metadata 2

Rectangle 3

### Table 3 Group 48

- Variable declaration | Memory | Scope | Lifetime
- int LocalVar; | register | thread | thread
- int localArr[N]; | global | thread | thread
- __device__ __shared__   int SharedVar; | shared | block | block
- __device__              int GlobalVar; | global | grid | application
- __device__ __constant__ int ConstantVar; | constant | grid | application

### Alt/Text Metadata 3

Group 48

### Shape 4 Marcador de número de diapositiva 5

18

### Alt/Text Metadata 4

Marcador de número de diapositiva 5

### XML fallback texts

- Variable declaration
- Memory
- Scope
- Lifetime
- int
- LocalVar
- ;
- thread
- localArr
- [N];
- SharedVar
- block
- GlobalVar
- grid
- application
- ConstantVar

### Notes XML fallback texts

- 48

## Slide 19

### Shape 1 Título 1

Memory Hierarchy in CUDA Programs

### Alt/Text Metadata 1

Título 1

### Alt/Text Metadata 2

Imagen 5 | CUDA_progmodel.eps

### Relationships 2

- rId2: image:../media/image14.emf

### Shape 3 Marcador de número de diapositiva 3

19

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Notes XML fallback texts

- 52

### Slide media/diagram relationships

- rId2: image:../media/image14.emf

## Slide 20

### Shape 1 Title 1

Recall: Comparison of Memories

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

20

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

等腰三角形 9

### Alt/Text Metadata 4

直接连接符 13

### Alt/Text Metadata 5

直接连接符 14

### Alt/Text Metadata 6

直接连接符 17

### Alt/Text Metadata 7

直接连接符 19

### Shape 8 文本框 28

SRAM

### Alt/Text Metadata 8

文本框 28

### Shape 9 文本框 29

HBM

### Alt/Text Metadata 9

文本框 29

### Shape 10 文本框 30

DDR

### Alt/Text Metadata 10

文本框 30

### Shape 11 文本框 31

SSD

### Alt/Text Metadata 11

文本框 31

### Shape 12 文本框 32

DISK

### Alt/Text Metadata 12

文本框 32

### Shape 13 文本框 33

Capacity

### Alt/Text Metadata 13

文本框 33

### Alt/Text Metadata 14

组合 45 | 等腰三角形 34 | 直接连接符 35 | 直接连接符 36 | 直接连接符 37 | 直接连接符 38 | 文本框 39 | 文本框 40 | 文本框 41 | 文本框 42 | 文本框 43 | 文本框 44

### Alt/Text Metadata 14.1

等腰三角形 34

### Alt/Text Metadata 14.2

直接连接符 35

### Alt/Text Metadata 14.3

直接连接符 36

### Alt/Text Metadata 14.4

直接连接符 37

### Alt/Text Metadata 14.5

直接连接符 38

### Alt/Text Metadata 14.6

文本框 39

### Alt/Text Metadata 14.7

文本框 40

### Alt/Text Metadata 14.8

文本框 41

### Alt/Text Metadata 14.9

文本框 42

### Alt/Text Metadata 14.10

文本框 43

### Shape 14.11 文本框 44

Latency

### Alt/Text Metadata 14.11

文本框 44

### Shape 15 文本框 57

Bandwidth

### Alt/Text Metadata 15

文本框 57

### Shape 16 文本框 58

~10MB

### Alt/Text Metadata 16

文本框 58

### Shape 17 文本框 59

~10GB

### Alt/Text Metadata 17

文本框 59

### Shape 18 文本框 60

~100GB

### Alt/Text Metadata 18

文本框 60

### Shape 19 文本框 61

~1TB

### Alt/Text Metadata 19

文本框 61

### Shape 20 文本框 62

~10TB

### Alt/Text Metadata 20

文本框 62

### Shape 21 文本框 63

~1ns

### Alt/Text Metadata 21

文本框 63

### Shape 22 文本框 64

~100ns

### Alt/Text Metadata 22

文本框 64

### Alt/Text Metadata 23

文本框 65

### Shape 24 文本框 66

~1us

### Alt/Text Metadata 24

文本框 66

### Shape 25 文本框 67

~1ms

### Alt/Text Metadata 25

文本框 67

### Alt/Text Metadata 26

组合 8 | 文本框 71 | 组合 7 | 组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51 | 文本框 52 | 文本框 53 | 文本框 54 | 文本框 55 | 文本框 56 | 文本框 68 | 文本框 69 | 文本框 70 | 文本框 72

### Shape 26.1 文本框 71

~100GB/s

### Alt/Text Metadata 26.1

文本框 71

### Alt/Text Metadata 26.2

组合 7 | 组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51 | 文本框 52 | 文本框 53 | 文本框 54 | 文本框 55 | 文本框 56 | 文本框 68 | 文本框 69 | 文本框 70 | 文本框 72

### Alt/Text Metadata 26.2.1

组合 5 | 等腰三角形 47 | 直接连接符 48 | 直接连接符 49 | 直接连接符 50 | 直接连接符 51

### Alt/Text Metadata 26.2.1.1

等腰三角形 47

### Alt/Text Metadata 26.2.1.2

直接连接符 48

### Alt/Text Metadata 26.2.1.3

直接连接符 49

### Alt/Text Metadata 26.2.1.4

直接连接符 50

### Alt/Text Metadata 26.2.1.5

直接连接符 51

### Alt/Text Metadata 26.2.2

文本框 52

### Alt/Text Metadata 26.2.3

文本框 53

### Alt/Text Metadata 26.2.4

文本框 54

### Alt/Text Metadata 26.2.5

文本框 55

### Alt/Text Metadata 26.2.6

文本框 56

### Shape 26.2.7 文本框 68

~10MB/s

### Alt/Text Metadata 26.2.7

文本框 68

### Shape 26.2.8 文本框 69

~1GB/s

### Alt/Text Metadata 26.2.8

文本框 69

### Shape 26.2.9 文本框 70

~10GB/s

### Alt/Text Metadata 26.2.9

文本框 70

### Shape 26.2.10 文本框 72

~1TB/s

### Alt/Text Metadata 26.2.10

文本框 72

### Notes XML fallback texts

- 64

## Slide 21

### Shape 1 Rectangle 4

The DRAM SubsystemThe Top-Down View

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- 66

## Slide 22

### Shape 1 Title 1

DRAM Subsystem Organization

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Channel
DIMM
Rank
Chip
Bank
Row/Column

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

22

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Flowchart: Merge 4

### Alt/Text Metadata 5

Flowchart: Merge 7

### Alt/Text Metadata 6

Flowchart: Merge 8

### Alt/Text Metadata 7

Flowchart: Merge 9

### Alt/Text Metadata 8

Flowchart: Merge 10

### Alt/Text Metadata 9

Flowchart: Merge 11

### Notes XML fallback texts

- 73

## Slide 23

### Shape 1 Title 1

The DRAM Subsystem

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Picture 4 | DIMM_crop.jpg

### Relationships 2

- rId2: image:../media/image15.jpeg

### Alt/Text Metadata 3

Picture 5 | nehalem.jpg

### Relationships 3

- rId3: image:../media/image16.jpeg

### Alt/Text Metadata 4

Picture 8 | DIMM_crop.jpg

### Relationships 4

- rId2: image:../media/image15.jpeg

### Alt/Text Metadata 5

Picture 9 | DIMM_crop.jpg

### Relationships 5

- rId2: image:../media/image15.jpeg

### Alt/Text Metadata 6

Picture 10 | DIMM_crop.jpg

### Relationships 6

- rId2: image:../media/image15.jpeg

### Alt/Text Metadata 7

Shape 12

### Alt/Text Metadata 8

Shape 13

### Alt/Text Metadata 9

Shape 16

### Shape 11 TextBox 22

Memory channel

### Alt/Text Metadata 11

TextBox 22

### Alt/Text Metadata 12

TextBox 23

### Shape 13 TextBox 24

DIMM (Dual in-line memory module)

### Alt/Text Metadata 13

TextBox 24

### Alt/Text Metadata 14

Rectangle 25

### Shape 15 TextBox 26

Processor

### Alt/Text Metadata 15

TextBox 26

### Alt/Text Metadata 16

Straight Connector 29

### Alt/Text Metadata 17

Straight Connector 31

### Alt/Text Metadata 18

Rectangle 33

### Shape 19 TextBox 34

“Channel”

### Alt/Text Metadata 19

TextBox 34

### Shape 20 Slide Number Placeholder 1

23

### Alt/Text Metadata 20

Slide Number Placeholder 1

### Notes XML fallback texts

- 74

### Slide media/diagram relationships

- rId3: image:../media/image16.jpeg
- rId2: image:../media/image15.jpeg

## Slide 24

### Shape 1 Title 1

Breaking down a DIMM (module)

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Picture 3 | DIMM_crop.jpg

### Relationships 2

- rId2: image:../media/image15.jpeg

### Shape 3 TextBox 4

DIMM (Dual in-line memory module)

### Alt/Text Metadata 3

TextBox 4

### Shape 4 Right Arrow 6

Side view

### Alt/Text Metadata 4

Right Arrow 6

### Alt/Text Metadata 5

Picture 7 | DIMM_side.png

### Relationships 5

- rId3: image:../media/image17.png

### Alt/Text Metadata 6

Picture 8 | DIMM_front.png

### Relationships 6

- rId4: image:../media/image18.png

### Alt/Text Metadata 7

Picture 9 | DIMM_back.png

### Relationships 7

- rId5: image:../media/image19.png

### Shape 8 TextBox 10

Front of DIMM

### Alt/Text Metadata 8

TextBox 10

### Shape 9 TextBox 11

Back of DIMM

### Alt/Text Metadata 9

TextBox 11

### Alt/Text Metadata 10

Straight Arrow Connector 13

### Alt/Text Metadata 11

Straight Arrow Connector 29

### Alt/Text Metadata 12

Rectangle 36

### Alt/Text Metadata 13

Rectangle 37

### Shape 14 TextBox 38

Rank 0: collection of 8 chips

### Alt/Text Metadata 14

TextBox 38

### Shape 15 TextBox 39

Rank 1

### Alt/Text Metadata 15

TextBox 39

### Alt/Text Metadata 16

Straight Arrow Connector 42

### Alt/Text Metadata 17

Straight Arrow Connector 45

### Shape 18 Slide Number Placeholder 1

24

### Alt/Text Metadata 18

Slide Number Placeholder 1

### Notes XML fallback texts

- 75

### Slide media/diagram relationships

- rId3: image:../media/image17.png
- rId2: image:../media/image15.jpeg
- rId5: image:../media/image19.png
- rId4: image:../media/image18.png

## Slide 25

### Shape 1 Title 1

Breaking down a Rank

### Alt/Text Metadata 1

Title 1

### Shape 2 Rectangle 3

Rank 0

### Alt/Text Metadata 2

Rectangle 3

### Alt/Text Metadata 3

Straight Connector 5

### Alt/Text Metadata 4

Shape 9

### Shape 5 TextBox 7

<0:63>

### Alt/Text Metadata 5

TextBox 7

### Alt/Text Metadata 6

Straight Connector 10

### Alt/Text Metadata 7

Straight Connector 12

### Shape 8 Rectangle 16

Chip 0

### Alt/Text Metadata 8

Rectangle 16

### Shape 9 Rectangle 17

Chip 1

### Alt/Text Metadata 9

Rectangle 17

### Shape 10 Rectangle 19

Chip 7

### Alt/Text Metadata 10

Rectangle 19

### Alt/Text Metadata 11

Oval 22

### Shape 12 TextBox 29

. . .

### Alt/Text Metadata 12

TextBox 29

### Shape 14 TextBox 31

<0:7>

### Alt/Text Metadata 14

TextBox 31

### Shape 16 TextBox 34

<8:15>

### Alt/Text Metadata 16

TextBox 34

### Shape 18 TextBox 36

<56:63>

### Alt/Text Metadata 18

TextBox 36

### Shape 21 TextBox 41

Data <0:63>

### Alt/Text Metadata 21

TextBox 41

### Alt/Text Metadata 22

Oval 42

### Shape 23 Slide Number Placeholder 1

25

### Alt/Text Metadata 23

Slide Number Placeholder 1

### Notes XML fallback texts

- 77

## Slide 26

### Alt/Text Metadata 1

Shape 9

### Shape 3 Title 1

Breaking down a Chip

### Alt/Text Metadata 3

Title 1

### Shape 4 Rectangle 3

Chip 0

### Alt/Text Metadata 4

Rectangle 3

### Shape 6 TextBox 6

<0:7>

### Alt/Text Metadata 6

TextBox 6

### Table 7 Table 4

-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 

### Alt/Text Metadata 7

Table 4

### Alt/Text Metadata 8

Rectangle 12

### Alt/Text Metadata 9

Rectangle 13

### Alt/Text Metadata 10

Rectangle 14

### Alt/Text Metadata 11

Rectangle 15

### Table 12 Table 17

-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 
-  |  |  |  |  | 

### Alt/Text Metadata 12

Table 17

### Alt/Text Metadata 13

Rectangle 18

### Alt/Text Metadata 14

Rectangle 19

### Alt/Text Metadata 15

Rectangle 20

### Alt/Text Metadata 16

Straight Arrow Connector 25

### Shape 17 TextBox 30

8 banks

### Alt/Text Metadata 17

TextBox 30

### Shape 19 Rectangle 21

Bank 0

### Alt/Text Metadata 19

Rectangle 21

### Alt/Text Metadata 20

Diagonal Stripe 31

### Alt/Text Metadata 21

TextBox 55

### Alt/Text Metadata 22

TextBox 56

### Alt/Text Metadata 23

TextBox 57

### Shape 24 TextBox 59

...

### Alt/Text Metadata 24

TextBox 59

### Alt/Text Metadata 26

TextBox 61

### Alt/Text Metadata 27

Oval 63

### Alt/Text Metadata 28

Oval 64

### Alt/Text Metadata 29

Straight Connector 65

### Alt/Text Metadata 30

Straight Connector 68

### Shape 31 Slide Number Placeholder 1

26

### Alt/Text Metadata 31

Slide Number Placeholder 1

### Notes XML fallback texts

- 79

## Slide 27

### Alt/Text Metadata 1

Rounded Rectangle 149

### Shape 2 Title 1

Inside a DRAM Chip

### Alt/Text Metadata 2

Title 1

### Alt/Text Metadata 3

Rounded Rectangle 4

### Alt/Text Metadata 4

Rounded Rectangle 6

### Alt/Text Metadata 5

Rounded Rectangle 7

### Alt/Text Metadata 6

Rounded Rectangle 8

### Alt/Text Metadata 7

Rounded Rectangle 9

### Alt/Text Metadata 8

Rounded Rectangle 10

### Alt/Text Metadata 9

Rounded Rectangle 11

### Alt/Text Metadata 10

Rounded Rectangle 12

### Alt/Text Metadata 11

Rounded Rectangle 13

### Alt/Text Metadata 12

Straight Connector 15

### Alt/Text Metadata 13

Straight Connector 16

### Alt/Text Metadata 14

Picture 17

### Relationships 14

- rId3: image:../media/image20.png

### Alt/Text Metadata 15

Rectangle 19

### Alt/Text Metadata 16

Rectangle 20

### Alt/Text Metadata 17

Rectangle 21

### Alt/Text Metadata 18

Straight Connector 23

### Alt/Text Metadata 19

Straight Connector 24

### Alt/Text Metadata 20

Straight Connector 25

### Alt/Text Metadata 21

Straight Connector 26

### Alt/Text Metadata 22

Straight Connector 27

### Alt/Text Metadata 23

Straight Connector 32

### Alt/Text Metadata 24

Straight Connector 35

### Alt/Text Metadata 25

Straight Connector 33

### Alt/Text Metadata 26

Straight Connector 34

### Alt/Text Metadata 27

Straight Connector 62

### Alt/Text Metadata 28

Group 167 | Oval 45 | Oval 46 | Oval 47 | Oval 48 | Oval 49 | Oval 50 | Oval 51 | Oval 52 | Oval 53 | Oval 54 | Oval 55 | Oval 56 | Oval 57 | Oval 58 | Oval 59 | Oval 71 | Oval 72 | Oval 73 | Oval 74 | Oval 75 | Oval 76 | Oval 77 | Oval 78 | Oval 79

### Alt/Text Metadata 28.1

Oval 45

### Alt/Text Metadata 28.2

Oval 46

### Alt/Text Metadata 28.3

Oval 47

### Alt/Text Metadata 28.4

Oval 48

### Alt/Text Metadata 28.5

Oval 49

### Alt/Text Metadata 28.6

Oval 50

### Alt/Text Metadata 28.7

Oval 51

### Alt/Text Metadata 28.8

Oval 52

### Alt/Text Metadata 28.9

Oval 53

### Alt/Text Metadata 28.10

Oval 54

### Alt/Text Metadata 28.11

Oval 55

### Alt/Text Metadata 28.12

Oval 56

### Alt/Text Metadata 28.13

Oval 57

### Alt/Text Metadata 28.14

Oval 58

### Alt/Text Metadata 28.15

Oval 59

### Alt/Text Metadata 28.16

Oval 71

### Alt/Text Metadata 28.17

Oval 72

### Alt/Text Metadata 28.18

Oval 73

### Alt/Text Metadata 28.19

Oval 74

### Alt/Text Metadata 28.20

Oval 75

### Alt/Text Metadata 28.21

Oval 76

### Alt/Text Metadata 28.22

Oval 77

### Alt/Text Metadata 28.23

Oval 78

### Alt/Text Metadata 28.24

Oval 79

### Alt/Text Metadata 29

Straight Connector 101

### Alt/Text Metadata 30

Straight Connector 102

### Shape 31 Rectangle 112

Access
Transistor

### Alt/Text Metadata 31

Rectangle 112

### Alt/Text Metadata 32

Curved Connector 113

### Shape 33 Rectangle 114

Storage
Capacitor

### Alt/Text Metadata 33

Rectangle 114

### Alt/Text Metadata 34

Curved Connector 115

### Alt/Text Metadata 35

Curved Connector 125

### Shape 36 Rectangle 126

Bitline

### Alt/Text Metadata 36

Rectangle 126

### Alt/Text Metadata 37

Curved Connector 127

### Shape 38 Rectangle 128

Wordline

### Alt/Text Metadata 38

Rectangle 128

### Alt/Text Metadata 39

Group 175 | Group 173 | Straight Connector 110 | Rectangle 111 | Rectangle 123 | Group 172 | Group 107 | Straight Connector 116 | Straight Connector 117 | Straight Connector 118 | Straight Connector 119 | Straight Connector 120 | Straight Connector 121 | Straight Connector 122 | Straight Connector 109 | Rectangle 135 | Group 174 | Straight Connector 108 | Rectangle 136

### Alt/Text Metadata 39.1

Group 173 | Straight Connector 110 | Rectangle 111 | Rectangle 123

### Alt/Text Metadata 39.1.1

Straight Connector 110

### Alt/Text Metadata 39.1.2

Rectangle 111

### Alt/Text Metadata 39.1.3

Rectangle 123

### Alt/Text Metadata 39.2

Group 172 | Group 107 | Straight Connector 116 | Straight Connector 117 | Straight Connector 118 | Straight Connector 119 | Straight Connector 120 | Straight Connector 121 | Straight Connector 122 | Straight Connector 109 | Rectangle 135

### Alt/Text Metadata 39.2.1

Group 107 | Straight Connector 116 | Straight Connector 117 | Straight Connector 118 | Straight Connector 119 | Straight Connector 120 | Straight Connector 121 | Straight Connector 122

### Alt/Text Metadata 39.2.1.1

Straight Connector 116

### Alt/Text Metadata 39.2.1.2

Straight Connector 117

### Alt/Text Metadata 39.2.1.3

Straight Connector 118

### Alt/Text Metadata 39.2.1.4

Straight Connector 119

### Alt/Text Metadata 39.2.1.5

Straight Connector 120

### Alt/Text Metadata 39.2.1.6

Straight Connector 121

### Alt/Text Metadata 39.2.1.7

Straight Connector 122

### Alt/Text Metadata 39.2.2

Straight Connector 109

### Alt/Text Metadata 39.2.3

Rectangle 135

### Alt/Text Metadata 39.3

Group 174 | Straight Connector 108 | Rectangle 136

### Alt/Text Metadata 39.3.1

Straight Connector 108

### Alt/Text Metadata 39.3.2

Rectangle 136

### Alt/Text Metadata 40

Straight Connector 140

### Alt/Text Metadata 41

Rounded Rectangle 2

### Alt/Text Metadata 42

Straight Connector 141

### Shape 43 TextBox 144

Subarray
(2D Array of DRAM Cells)

### Alt/Text Metadata 43

TextBox 144

### Shape 44 TextBox 145

Sense Amplifiers

### Alt/Text Metadata 44

TextBox 145

### Shape 45 TextBox 162

DRAM Module

### Alt/Text Metadata 45

TextBox 162

### Alt/Text Metadata 46

Straight Arrow Connector 147

### Shape 47 TextBox 163

DRAM Chips

### Alt/Text Metadata 47

TextBox 163

### Alt/Text Metadata 48

Straight Arrow Connector 164

### Shape 49 TextBox 166

DRAM Bank

### Alt/Text Metadata 49

TextBox 166

### Shape 50 Rectangle 169

DRAM Cells

### Alt/Text Metadata 50

Rectangle 169

### Shape 51 Slide Number Placeholder 2

8

### Alt/Text Metadata 51

Slide Number Placeholder 2

### Alt/Text Metadata 52

Rectangle 89

### Alt/Text Metadata 53

Rectangle 90

### Alt/Text Metadata 54

Rectangle 91

### Alt/Text Metadata 55

Rectangle 92

### Alt/Text Metadata 56

Rectangle 93

### Alt/Text Metadata 57

Rectangle 95

### Alt/Text Metadata 58

Rectangle 22

### Shape 59 TextBox 124

Row Buffer

### Alt/Text Metadata 59

TextBox 124

### Alt/Text Metadata 60

Curved Connector 30

### Notes XML fallback texts

- 80

### Slide media/diagram relationships

- rId3: image:../media/image20.png

## Slide 28

### Shape 1 Title 1

DRAM Bank Operation

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

28

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Rectangle 4

### Alt/Text Metadata 4

Line 5

### Alt/Text Metadata 5

Line 6

### Alt/Text Metadata 6

Line 7

### Alt/Text Metadata 7

Line 8

### Alt/Text Metadata 8

Line 9

### Alt/Text Metadata 9

Line 10

### Alt/Text Metadata 10

Rectangle 12

### Alt/Text Metadata 11

Line 13

### Shape 12 Text Box 14

Row Buffer

### Alt/Text Metadata 12

Text Box 14

### Shape 13 Text Box 15

(Row 0, Column 0)

### Alt/Text Metadata 13

Text Box 15

### Alt/Text Metadata 14

Rectangle 16

### Shape 15 Text Box 17

Row decoder

### Alt/Text Metadata 15

Text Box 17

### Shape 16 Text Box 19

Column mux

### Alt/Text Metadata 16

Text Box 19

### Alt/Text Metadata 17

Line 20

### Alt/Text Metadata 18

Line 21

### Alt/Text Metadata 19

Line 22

### Alt/Text Metadata 20

Line 23

### Alt/Text Metadata 21

Line 24

### Alt/Text Metadata 22

Line 25

### Alt/Text Metadata 23

Line 26

### Alt/Text Metadata 24

Line 27

### Alt/Text Metadata 25

Line 28

### Alt/Text Metadata 26

Line 39

### Shape 27 Text Box 40

Row address 0

### Alt/Text Metadata 27

Text Box 40

### Shape 28 Text Box 41

Column address 0

### Alt/Text Metadata 28

Text Box 41

### Alt/Text Metadata 29

Line 42

### Alt/Text Metadata 30

Line 43

### Shape 31 Text Box 44

Data

### Alt/Text Metadata 31

Text Box 44

### Alt/Text Metadata 32

Rectangle 45

### Alt/Text Metadata 33

Rectangle 47

### Alt/Text Metadata 34

Rectangle 48

### Shape 35 Text Box 49

Row 0

### Alt/Text Metadata 35

Text Box 49

### Shape 36 Text Box 50

Empty

### Alt/Text Metadata 36

Text Box 50

### Shape 37 Text Box 51

(Row 0, Column 1)

### Alt/Text Metadata 37

Text Box 51

### Shape 38 Text Box 52

Column address 1

### Alt/Text Metadata 38

Text Box 52

### Alt/Text Metadata 39

Rectangle 53

### Shape 40 Text Box 54

(Row 0, Column 85)

### Alt/Text Metadata 40

Text Box 54

### Alt/Text Metadata 41

Rectangle 55

### Shape 42 Text Box 56

Column address 85

### Alt/Text Metadata 42

Text Box 56

### Shape 43 Text Box 58

(Row 1, Column 0)

### Alt/Text Metadata 43

Text Box 58

### Shape 44 Text Box 59

HIT

### Alt/Text Metadata 44

Text Box 59

### Alt/Text Metadata 45

Text Box 60

### Shape 46 Text Box 61

Row address 1

### Alt/Text Metadata 46

Text Box 61

### Alt/Text Metadata 47

Rectangle 62

### Alt/Text Metadata 48

Rectangle 63

### Alt/Text Metadata 49

Rectangle 64

### Shape 50 Text Box 65

Row 1

### Alt/Text Metadata 50

Text Box 65

### Alt/Text Metadata 51

Text Box 66

### Shape 52 Text Box 67

CONFLICT !

### Alt/Text Metadata 52

Text Box 67

### Shape 53 Text Box 69

Columns

### Alt/Text Metadata 53

Text Box 69

### Shape 54 Text Box 70

Rows

### Alt/Text Metadata 54

Text Box 70

### Shape 55 Text Box 15

Access Address:

### Alt/Text Metadata 56

Trapezoid 57

### Notes XML fallback texts

- Computation is divided
- such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
- CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.
- 81

## Slide 29

### Shape 1 Rectangle 4

Long Global Memory Access Latency

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

### Notes XML fallback texts

- Computation is divided
- such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
- CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.
- 82

## Slide 30

### Shape 1 矩形 25

Motivation of In-network Computing

### Alt/Text Metadata 1

矩形 25

### Alt/Text Metadata 2

Rectangle 2

### Shape 3 TextBox 3

How to optimize global memory access?

### Alt/Text Metadata 3

TextBox 3

### Shape 4 TextBox 3

Multithreading

### Shape 5 TextBox 3

Shared Memory

### Shape 6 TextBox 3

Memory Coalescing

### Notes XML fallback texts

- 83

## Slide 31

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

31

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

### Notes XML fallback texts

- A
- number
- b
- of blocks per frame executes.
- Data transfers are overlapped with computation. Thus, some time can be saved.
- 84

## Slide 32

### Shape 1 Title 1

Latency Hiding via Warp-Level FGMT

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Warp: A set of threads that execute the same instruction (on different data elements)
Fine-grained multithreading
One instruction per thread in pipeline at a time (No interlocking)
Interleaving warp execution to hide latencies
Register values of all threads stay in register file
FGMT enables long latency tolerance
Millions of pixels

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

32

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 4 | AutoShape 5 | Rectangle 6 | Rectangle 7 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11 | Rectangle 12 | Rectangle 13 | Rectangle 14 | Rectangle 15 | Rectangle 16 | Rectangle 17 | Rectangle 18 | Rectangle 19 | Rectangle 20 | Rectangle 21 | Rectangle 22 | Line 23 | Freeform 24 | Rectangle 25 | Rectangle 26 | Rectangle 27 | Rectangle 28 | Rectangle 29 | Rectangle 30 | Rectangle 31 | Rectangle 32 | Rectangle 33 | Rectangle 34 | Rectangle 35 | Rectangle 36 | Rectangle 37 | Rectangle 38 | Rectangle 39 | Line 40 | Freeform 41 | Line 42 | Freeform 43 | Line 44 | Freeform 45 | Line 46 | Freeform 47 | Line 48 | Freeform 49 | Line 50 | Freeform 51 | Rectangle 52 | Rectangle 53 | Rectangle 54 | Line 55 | Freeform 56 | Line 57 | Freeform 58 | Line 59 | Freeform 60 | Freeform 61 | Line 62 | Freeform 63 | Rectangle 64 | Rectangle 65 | Rectangle 66 | Rectangle 67 | Rectangle 68 | Rectangle 69 | Rectangle 70 | Rectangle 71 | Rectangle 72 | Freeform 73 | Freeform 74 | Freeform 75 | Freeform 76 | Line 77 | Freeform 78 | Freeform 79 | Freeform 80 | Freeform 81 | Rectangle 82 | Rectangle 83 | Rectangle 84 | Freeform 85 | Freeform 86 | Freeform 87 | Freeform 88 | Rectangle 89 | Rectangle 90 | Rectangle 91 | Rectangle 92 | Rectangle 93 | Rectangle 94 | Rectangle 95 | Rectangle 96 | Rectangle 97 | Rectangle 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103 | Freeform 104 | Line 105 | Freeform 106 | Freeform 107 | Freeform 108 | Rectangle 109 | Rectangle 110 | Rectangle 111 | Rectangle 112 | Rectangle 113 | Freeform 114 | Freeform 115 | Freeform 116 | Freeform 117 | Freeform 118 | Freeform 119 | Freeform 120 | Freeform 121 | Freeform 122 | Freeform 123 | Freeform 124 | Freeform 125 | Rectangle 126 | Rectangle 127 | Rectangle 128 | Rectangle 129 | Rectangle 130 | Rectangle 131 | Rectangle 132 | Line 133

### Alt/Text Metadata 4.1

AutoShape 5

### Alt/Text Metadata 4.2

Rectangle 6

### Alt/Text Metadata 4.3

Rectangle 7

### Alt/Text Metadata 4.4

Rectangle 8

### Alt/Text Metadata 4.5

Rectangle 9

### Shape 4.6 Rectangle 10

Decode

### Alt/Text Metadata 4.6

Rectangle 10

### Alt/Text Metadata 4.7

Rectangle 11

### Alt/Text Metadata 4.8

Rectangle 12

### Shape 4.9 Rectangle 13

R

### Alt/Text Metadata 4.9

Rectangle 13

### Shape 4.10 Rectangle 14

F

### Alt/Text Metadata 4.10

Rectangle 14

### Alt/Text Metadata 4.11

Rectangle 15

### Alt/Text Metadata 4.12

Rectangle 16

### Alt/Text Metadata 4.13

Rectangle 17

### Alt/Text Metadata 4.14

Rectangle 18

### Alt/Text Metadata 4.15

Rectangle 19

### Alt/Text Metadata 4.16

Rectangle 20

### Alt/Text Metadata 4.17

Rectangle 21

### Alt/Text Metadata 4.18

Rectangle 22

### Alt/Text Metadata 4.19

Line 23

### Alt/Text Metadata 4.20

Freeform 24

### Alt/Text Metadata 4.21

Rectangle 25

### Alt/Text Metadata 4.22

Rectangle 26

### Shape 4.23 Rectangle 27

A

### Alt/Text Metadata 4.23

Rectangle 27

### Shape 4.24 Rectangle 28

L

### Alt/Text Metadata 4.24

Rectangle 28

### Shape 4.25 Rectangle 29

U

### Alt/Text Metadata 4.25

Rectangle 29

### Alt/Text Metadata 4.26

Rectangle 30

### Alt/Text Metadata 4.27

Rectangle 31

### Alt/Text Metadata 4.28

Rectangle 32

### Alt/Text Metadata 4.29

Rectangle 33

### Alt/Text Metadata 4.30

Rectangle 34

### Alt/Text Metadata 4.31

Rectangle 35

### Alt/Text Metadata 4.32

Rectangle 36

### Alt/Text Metadata 4.33

Rectangle 37

### Alt/Text Metadata 4.34

Rectangle 38

### Alt/Text Metadata 4.35

Rectangle 39

### Alt/Text Metadata 4.36

Line 40

### Alt/Text Metadata 4.37

Freeform 41

### Alt/Text Metadata 4.38

Line 42

### Alt/Text Metadata 4.39

Freeform 43

### Alt/Text Metadata 4.40

Line 44

### Alt/Text Metadata 4.41

Freeform 45

### Alt/Text Metadata 4.42

Line 46

### Alt/Text Metadata 4.43

Freeform 47

### Alt/Text Metadata 4.44

Line 48

### Alt/Text Metadata 4.45

Freeform 49

### Alt/Text Metadata 4.46

Line 50

### Alt/Text Metadata 4.47

Freeform 51

### Alt/Text Metadata 4.48

Rectangle 52

### Alt/Text Metadata 4.49

Rectangle 53

### Shape 4.50 Rectangle 54

D-Cache

### Alt/Text Metadata 4.50

Rectangle 54

### Alt/Text Metadata 4.51

Line 55

### Alt/Text Metadata 4.52

Freeform 56

### Alt/Text Metadata 4.53

Line 57

### Alt/Text Metadata 4.54

Freeform 58

### Alt/Text Metadata 4.55

Line 59

### Alt/Text Metadata 4.56

Freeform 60

### Alt/Text Metadata 4.57

Freeform 61

### Alt/Text Metadata 4.58

Line 62

### Alt/Text Metadata 4.59

Freeform 63

### Alt/Text Metadata 4.60

Rectangle 64

### Alt/Text Metadata 4.61

Rectangle 65

### Shape 4.62 Rectangle 66

Thread Warp 6

### Alt/Text Metadata 4.62

Rectangle 66

### Alt/Text Metadata 4.63

Rectangle 67

### Alt/Text Metadata 4.64

Rectangle 68

### Shape 4.65 Rectangle 69

Thread Warp 1

### Alt/Text Metadata 4.65

Rectangle 69

### Alt/Text Metadata 4.66

Rectangle 70

### Alt/Text Metadata 4.67

Rectangle 71

### Shape 4.68 Rectangle 72

Thread Warp 2

### Alt/Text Metadata 4.68

Rectangle 72

### Alt/Text Metadata 4.69

Freeform 73

### Alt/Text Metadata 4.70

Freeform 74

### Alt/Text Metadata 4.71

Freeform 75

### Alt/Text Metadata 4.72

Freeform 76

### Alt/Text Metadata 4.73

Line 77

### Alt/Text Metadata 4.74

Freeform 78

### Alt/Text Metadata 4.75

Freeform 79

### Alt/Text Metadata 4.76

Freeform 80

### Alt/Text Metadata 4.77

Freeform 81

### Shape 4.78 Rectangle 82

Data

### Alt/Text Metadata 4.78

Rectangle 82

### Shape 4.79 Rectangle 83

All Hit?

### Alt/Text Metadata 4.79

Rectangle 83

### Shape 4.80 Rectangle 84

Miss?

### Alt/Text Metadata 4.80

Rectangle 84

### Alt/Text Metadata 4.81

Freeform 85

### Alt/Text Metadata 4.82

Freeform 86

### Alt/Text Metadata 4.83

Freeform 87

### Alt/Text Metadata 4.84

Freeform 88

### Shape 4.85 Rectangle 89

Warps accessing

### Alt/Text Metadata 4.85

Rectangle 89

### Shape 4.86 Rectangle 90

memory hierarchy

### Alt/Text Metadata 4.86

Rectangle 90

### Alt/Text Metadata 4.87

Rectangle 91

### Alt/Text Metadata 4.88

Rectangle 92

### Alt/Text Metadata 4.89

Rectangle 93

### Alt/Text Metadata 4.90

Rectangle 94

### Shape 4.91 Rectangle 95

Thread Warp 3

### Alt/Text Metadata 4.91

Rectangle 95

### Alt/Text Metadata 4.92

Rectangle 96

### Alt/Text Metadata 4.93

Rectangle 97

### Shape 4.94 Rectangle 98

Thread Warp 8

### Alt/Text Metadata 4.94

Rectangle 98

### Alt/Text Metadata 4.95

Freeform 99

### Alt/Text Metadata 4.96

Freeform 100

### Alt/Text Metadata 4.97

Freeform 101

### Alt/Text Metadata 4.98

Freeform 102

### Alt/Text Metadata 4.99

Freeform 103

### Alt/Text Metadata 4.100

Freeform 104

### Alt/Text Metadata 4.101

Line 105

### Alt/Text Metadata 4.102

Freeform 106

### Alt/Text Metadata 4.103

Freeform 107

### Alt/Text Metadata 4.104

Freeform 108

### Alt/Text Metadata 4.105

Rectangle 109

### Alt/Text Metadata 4.106

Rectangle 110

### Shape 4.107 Rectangle 111

Writeback

### Alt/Text Metadata 4.107

Rectangle 111

### Shape 4.108 Rectangle 112

Warps available

### Alt/Text Metadata 4.108

Rectangle 112

### Shape 4.109 Rectangle 113

for scheduling

### Alt/Text Metadata 4.109

Rectangle 113

### Alt/Text Metadata 4.110

Freeform 114

### Alt/Text Metadata 4.111

Freeform 115

### Alt/Text Metadata 4.112

Freeform 116

### Alt/Text Metadata 4.113

Freeform 117

### Alt/Text Metadata 4.114

Freeform 118

### Alt/Text Metadata 4.115

Freeform 119

### Alt/Text Metadata 4.116

Freeform 120

### Alt/Text Metadata 4.117

Freeform 121

### Alt/Text Metadata 4.118

Freeform 122

### Alt/Text Metadata 4.119

Freeform 123

### Alt/Text Metadata 4.120

Freeform 124

### Alt/Text Metadata 4.121

Freeform 125

### Alt/Text Metadata 4.122

Rectangle 126

### Alt/Text Metadata 4.123

Rectangle 127

### Shape 4.124 Rectangle 128

Thread Warp 7

### Alt/Text Metadata 4.124

Rectangle 128

### Alt/Text Metadata 4.125

Rectangle 129

### Alt/Text Metadata 4.126

Rectangle 130

### Shape 4.127 Rectangle 131

I-Fetch

### Alt/Text Metadata 4.127

Rectangle 131

### Shape 4.128 Rectangle 132

SIMD Pipeline

### Alt/Text Metadata 4.128

Rectangle 132

### Alt/Text Metadata 4.129

Line 133

### Shape 5 TextBox 134

Slide credit: Tor Aamodt

### Alt/Text Metadata 5

TextBox 134

### Speaker notes

With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread’s warp from the pool of “ready” warps and thereby allows other threads to proceed while the memory system processes its request.
 With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.

## Slide 33

### Shape 1 Título 1

Latency Hiding and Occupancy

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

FGMT can hide long latency operations (e.g., memory accesses)
Occupancy: ratio of active warps to the maximum number of warps per GPU core

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Agrupar 29 | Imagen 7 | Multi_exec_1.eps | CuadroTexto 8

### Relationships 3

- rId2: image:../media/image21.emf

### Alt/Text Metadata 3.1

Imagen 7 | Multi_exec_1.eps

### Relationships 3.1

- rId2: image:../media/image21.emf

### Shape 3.2 CuadroTexto 8

4 active warps

### Alt/Text Metadata 3.2

CuadroTexto 8

### Alt/Text Metadata 4

Agrupar 30 | Imagen 10 | Multi_exec_1.eps | CuadroTexto 11

### Relationships 4

- rId2: image:../media/image21.emf

### Alt/Text Metadata 4.1

Imagen 10 | Multi_exec_1.eps

### Relationships 4.1

- rId2: image:../media/image21.emf

### Shape 4.2 CuadroTexto 11

2 active warps

### Alt/Text Metadata 4.2

CuadroTexto 11

### Alt/Text Metadata 5

Imagen 12 | Multi_exec_2.eps

### Relationships 5

- rId3: image:../media/image22.emf

### Alt/Text Metadata 6

Imagen 13 | Multi_exec_3.eps

### Relationships 6

- rId4: image:../media/image23.emf

### Alt/Text Metadata 7

Imagen 14 | Multi_exec_4.eps

### Relationships 7

- rId5: image:../media/image24.emf

### Alt/Text Metadata 8

Imagen 15 | Multi_exec_5.eps

### Relationships 8

- rId6: image:../media/image25.emf

### Alt/Text Metadata 9

Imagen 16 | Multi_exec_6.eps

### Relationships 9

- rId7: image:../media/image26.emf

### Alt/Text Metadata 10

Imagen 17 | Multi_exec_7.eps

### Relationships 10

- rId8: image:../media/image27.emf

### Alt/Text Metadata 11

Imagen 18 | Multi_exec_2.eps

### Relationships 11

- rId3: image:../media/image22.emf

### Alt/Text Metadata 12

Imagen 19 | Multi_exec_3.eps

### Relationships 12

- rId4: image:../media/image23.emf

### Alt/Text Metadata 13

Imagen 20 | Multi_exec_6.eps

### Relationships 13

- rId7: image:../media/image26.emf

### Alt/Text Metadata 14

Imagen 21 | Multi_exec_7.eps

### Relationships 14

- rId8: image:../media/image27.emf

### Shape 15 Marcador de número de diapositiva 3

33

### Alt/Text Metadata 15

Marcador de número de diapositiva 3

### Notes XML fallback texts

- 86
- KB MB GB TB
- K M B T E P
- 1B=10
- 亿

### Slide media/diagram relationships

- rId8: image:../media/image27.emf
- rId3: image:../media/image22.emf
- rId7: image:../media/image26.emf
- rId2: image:../media/image21.emf
- rId6: image:../media/image25.emf
- rId5: image:../media/image24.emf
- rId4: image:../media/image23.emf

## Slide 34

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

34

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

### Notes XML fallback texts

- 88

## Slide 35

### Shape 1 Title 1

Memory Coalescing (I)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Memory Coalescing：
When threads in the same warp access consecutive memory locations in the same burst, the accesses can be combined and served by one burst
 Only one DRAM transaction is needed.
Memory Divergence：
If threads in the same warp access locations not in the same burst, accesses cannot be combined
Multiple memory transactions are needed
Takes longer to service data to the warp

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 3

TextBox 610

### Shape 4 Marcador de número de diapositiva 1

35

### Alt/Text Metadata 4

Marcador de número de diapositiva 1

### Notes XML fallback texts

- Thread block is the key innovation to scale-up GPU architecture. T
- h
- e software code stays the same and enjoys performance speedup while GPU hardware evolves.
- 89

## Slide 36

### Shape 1 Rectangle 3

Memory Coalescing:
When accessing global memory, memory coalescing makes sure that concurrent threads access nearby memory locations
Peak bandwidth utilization occurs when all threads in a warp access one cache line (or several consecutive cache lines)

### Alt/Text Metadata 1

Rectangle 3

### Alt/Text Metadata 2

Freeform 4

### Alt/Text Metadata 3

Rectangle 5

### Shape 4 Rectangle 6

Md

### Alt/Text Metadata 4

Rectangle 6

### Alt/Text Metadata 5

Freeform 7

### Alt/Text Metadata 6

Rectangle 8

### Shape 7 Rectangle 9

Nd

### Alt/Text Metadata 7

Rectangle 9

### Alt/Text Metadata 8

Freeform 10

### Alt/Text Metadata 9

Freeform 11

### Shape 10 Rectangle 12

W

### Alt/Text Metadata 10

Rectangle 12

### Shape 11 Rectangle 13

I

### Alt/Text Metadata 11

Rectangle 13

### Shape 12 Rectangle 14

D

### Alt/Text Metadata 12

Rectangle 14

### Shape 13 Rectangle 15

T

### Alt/Text Metadata 13

Rectangle 15

### Shape 14 Rectangle 16

H

### Alt/Text Metadata 14

Rectangle 16

### Shape 15 Rectangle 17

WIDTH

### Alt/Text Metadata 15

Rectangle 17

### Alt/Text Metadata 16

Freeform 18

### Alt/Text Metadata 17

Line 19

### Shape 18 Text Box 20

Thread 1

### Alt/Text Metadata 18

Text Box 20

### Shape 19 Text Box 21

Thread 2

### Alt/Text Metadata 19

Text Box 21

### Alt/Text Metadata 20

Freeform 22

### Shape 21 Text Box 23

Not coalesced

### Alt/Text Metadata 21

Text Box 23

### Alt/Text Metadata 22

Line 24

### Shape 23 Text Box 25

Coalesced

### Alt/Text Metadata 23

Text Box 25

### Shape 24 Título 2

Memory Coalescing (II)

### Alt/Text Metadata 24

Título 2

### Shape 25 Marcador de número de diapositiva 1

36

### Alt/Text Metadata 25

Marcador de número de diapositiva 1

### Shape 26 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 26

CuadroTexto 26

### Notes XML fallback texts

- 97

## Slide 37

### Shape 1 Título 1

Uncoalesced Memory Accesses

### Alt/Text Metadata 1

Título 1

### Alt/Text Metadata 2

Rectangle 2

### Alt/Text Metadata 3

Rectangle 3

### Shape 4 Rectangle 4

M2,0

### Alt/Text Metadata 4

Rectangle 4

### Alt/Text Metadata 5

Rectangle 5

### Shape 6 Rectangle 6

M1,1

### Alt/Text Metadata 6

Rectangle 6

### Shape 7 Rectangle 7

M1,0

### Alt/Text Metadata 7

Rectangle 7

### Shape 8 Rectangle 8

M0,0

### Alt/Text Metadata 8

Rectangle 8

### Shape 9 Rectangle 9

M0,1

### Alt/Text Metadata 9

Rectangle 9

### Alt/Text Metadata 10

Rectangle 10

### Shape 11 Rectangle 11

M3,0

### Alt/Text Metadata 11

Rectangle 11

### Alt/Text Metadata 12

Rectangle 12

### Alt/Text Metadata 13

Rectangle 13

### Shape 14 Rectangle 14

M2,1

### Alt/Text Metadata 14

Rectangle 14

### Alt/Text Metadata 15

Rectangle 15

### Alt/Text Metadata 16

Rectangle 16

### Shape 17 Rectangle 17

M3,1

### Alt/Text Metadata 17

Rectangle 17

### Alt/Text Metadata 18

Rectangle 19

### Alt/Text Metadata 19

Rectangle 20

### Alt/Text Metadata 20

Rectangle 21

### Alt/Text Metadata 21

Rectangle 22

### Alt/Text Metadata 22

Rectangle 23

### Alt/Text Metadata 23

Rectangle 24

### Alt/Text Metadata 24

Rectangle 25

### Alt/Text Metadata 25

Rectangle 26

### Alt/Text Metadata 26

Rectangle 27

### Alt/Text Metadata 27

Rectangle 28

### Alt/Text Metadata 28

Rectangle 29

### Alt/Text Metadata 29

Rectangle 30

### Alt/Text Metadata 30

Rectangle 31

### Alt/Text Metadata 31

Rectangle 32

### Alt/Text Metadata 32

Rectangle 33

### Alt/Text Metadata 33

Rectangle 34

### Alt/Text Metadata 34

Rectangle 35

### Alt/Text Metadata 35

Rectangle 36

### Alt/Text Metadata 36

Rectangle 37

### Alt/Text Metadata 37

Rectangle 38

### Shape 38 Rectangle 39

M1,2

### Alt/Text Metadata 38

Rectangle 39

### Shape 39 Rectangle 40

M0,2

### Alt/Text Metadata 39

Rectangle 40

### Shape 40 Rectangle 41

M2,2

### Alt/Text Metadata 40

Rectangle 41

### Shape 41 Rectangle 42

M3,2

### Alt/Text Metadata 41

Rectangle 42

### Alt/Text Metadata 42

Rectangle 43

### Alt/Text Metadata 43

Rectangle 44

### Alt/Text Metadata 44

Rectangle 45

### Alt/Text Metadata 45

Rectangle 46

### Alt/Text Metadata 46

Rectangle 47

### Alt/Text Metadata 47

Rectangle 48

### Alt/Text Metadata 48

Rectangle 49

### Alt/Text Metadata 49

Rectangle 50

### Alt/Text Metadata 50

Rectangle 51

### Alt/Text Metadata 51

Rectangle 52

### Alt/Text Metadata 52

Rectangle 53

### Alt/Text Metadata 53

Rectangle 54

### Shape 54 Rectangle 55

M1,3

### Alt/Text Metadata 54

Rectangle 55

### Shape 55 Rectangle 56

M0,3

### Alt/Text Metadata 55

Rectangle 56

### Shape 56 Rectangle 57

M2,3

### Alt/Text Metadata 56

Rectangle 57

### Shape 57 Rectangle 58

M3,3

### Alt/Text Metadata 57

Rectangle 58

### Alt/Text Metadata 58

Rectangle 59

### Alt/Text Metadata 59

Rectangle 60

### Alt/Text Metadata 60

Rectangle 61

### Alt/Text Metadata 61

Rectangle 62

### Alt/Text Metadata 62

Rectangle 63

### Alt/Text Metadata 63

Rectangle 64

### Alt/Text Metadata 64

Rectangle 65

### Alt/Text Metadata 65

Rectangle 66

### Alt/Text Metadata 66

Rectangle 67

### Alt/Text Metadata 67

Rectangle 68

### Alt/Text Metadata 68

Rectangle 69

### Alt/Text Metadata 69

Rectangle 70

### Alt/Text Metadata 70

Line 71

### Shape 71 Text Box 72

M

### Alt/Text Metadata 71

Text Box 72

### Shape 72 Text Box 73

T1

### Alt/Text Metadata 72

Text Box 73

### Shape 73 Text Box 74

T2

### Alt/Text Metadata 73

Text Box 74

### Shape 74 Text Box 75

T3

### Alt/Text Metadata 74

Text Box 75

### Shape 75 Text Box 76

T4

### Alt/Text Metadata 75

Text Box 76

### Alt/Text Metadata 76

Line 77

### Shape 77 Text Box 78

Warp 1

### Alt/Text Metadata 77

Text Box 78

### Alt/Text Metadata 78

Text Box 79

### Alt/Text Metadata 79

Text Box 80

### Alt/Text Metadata 80

Text Box 81

### Alt/Text Metadata 81

Text Box 82

### Shape 82 Text Box 83

Warp 2

### Alt/Text Metadata 82

Text Box 83

### Shape 83 Text Box 84

Access direction of each thread

### Alt/Text Metadata 83

Text Box 84

### Alt/Text Metadata 84

Line 85

### Alt/Text Metadata 85

Line 86

### Alt/Text Metadata 86

Line 87

### Alt/Text Metadata 87

Line 88

### Alt/Text Metadata 88

Line 89

### Alt/Text Metadata 89

Line 90

### Alt/Text Metadata 90

Line 91

### Alt/Text Metadata 91

Line 92

### Alt/Text Metadata 92

Rectangle 93

### Alt/Text Metadata 93

Rectangle 94

### Shape 94 Text Box 95

…

### Alt/Text Metadata 94

Text Box 95

### Shape 95 Marcador de número de diapositiva 3

37

### Alt/Text Metadata 95

Marcador de número de diapositiva 3

### Shape 96 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 96

CuadroTexto 26

### Notes XML fallback texts

- With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread
- ’
- s warp from the pool of
- “
- ready
- ”
- warps and thereby allows other threads to proceed while the memory system processes its request.
- With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.
- 100

## Slide 38

### Shape 1 Título 1

Coalesced Memory Accesses

### Alt/Text Metadata 1

Título 1

### Alt/Text Metadata 2

Rectangle 2

### Alt/Text Metadata 3

Rectangle 3

### Shape 4 Rectangle 4

M2,0

### Alt/Text Metadata 4

Rectangle 4

### Alt/Text Metadata 5

Rectangle 5

### Shape 6 Rectangle 6

M1,1

### Alt/Text Metadata 6

Rectangle 6

### Shape 7 Rectangle 7

M1,0

### Alt/Text Metadata 7

Rectangle 7

### Shape 8 Rectangle 8

M0,0

### Alt/Text Metadata 8

Rectangle 8

### Shape 9 Rectangle 9

M0,1

### Alt/Text Metadata 9

Rectangle 9

### Alt/Text Metadata 10

Rectangle 10

### Shape 11 Rectangle 11

M3,0

### Alt/Text Metadata 11

Rectangle 11

### Alt/Text Metadata 12

Rectangle 12

### Alt/Text Metadata 13

Rectangle 13

### Shape 14 Rectangle 14

M2,1

### Alt/Text Metadata 14

Rectangle 14

### Alt/Text Metadata 15

Rectangle 15

### Alt/Text Metadata 16

Rectangle 16

### Shape 17 Rectangle 17

M3,1

### Alt/Text Metadata 17

Rectangle 17

### Alt/Text Metadata 18

Rectangle 19

### Alt/Text Metadata 19

Rectangle 20

### Alt/Text Metadata 20

Rectangle 21

### Alt/Text Metadata 21

Rectangle 22

### Alt/Text Metadata 22

Rectangle 23

### Alt/Text Metadata 23

Rectangle 24

### Alt/Text Metadata 24

Rectangle 25

### Alt/Text Metadata 25

Rectangle 26

### Alt/Text Metadata 26

Rectangle 27

### Alt/Text Metadata 27

Rectangle 28

### Alt/Text Metadata 28

Rectangle 29

### Alt/Text Metadata 29

Rectangle 30

### Alt/Text Metadata 30

Rectangle 31

### Alt/Text Metadata 31

Rectangle 32

### Alt/Text Metadata 32

Rectangle 33

### Alt/Text Metadata 33

Rectangle 34

### Alt/Text Metadata 34

Rectangle 35

### Alt/Text Metadata 35

Rectangle 36

### Alt/Text Metadata 36

Rectangle 37

### Alt/Text Metadata 37

Rectangle 38

### Shape 38 Rectangle 39

M1,2

### Alt/Text Metadata 38

Rectangle 39

### Shape 39 Rectangle 40

M0,2

### Alt/Text Metadata 39

Rectangle 40

### Shape 40 Rectangle 41

M2,2

### Alt/Text Metadata 40

Rectangle 41

### Shape 41 Rectangle 42

M3,2

### Alt/Text Metadata 41

Rectangle 42

### Alt/Text Metadata 42

Rectangle 43

### Alt/Text Metadata 43

Rectangle 44

### Alt/Text Metadata 44

Rectangle 45

### Alt/Text Metadata 45

Rectangle 46

### Alt/Text Metadata 46

Rectangle 47

### Alt/Text Metadata 47

Rectangle 48

### Alt/Text Metadata 48

Rectangle 49

### Alt/Text Metadata 49

Rectangle 50

### Alt/Text Metadata 50

Rectangle 51

### Alt/Text Metadata 51

Rectangle 52

### Alt/Text Metadata 52

Rectangle 53

### Alt/Text Metadata 53

Rectangle 54

### Shape 54 Rectangle 55

M1,3

### Alt/Text Metadata 54

Rectangle 55

### Shape 55 Rectangle 56

M0,3

### Alt/Text Metadata 55

Rectangle 56

### Shape 56 Rectangle 57

M2,3

### Alt/Text Metadata 56

Rectangle 57

### Shape 57 Rectangle 58

M3,3

### Alt/Text Metadata 57

Rectangle 58

### Alt/Text Metadata 58

Rectangle 59

### Alt/Text Metadata 59

Rectangle 60

### Alt/Text Metadata 60

Rectangle 61

### Alt/Text Metadata 61

Rectangle 62

### Alt/Text Metadata 62

Rectangle 63

### Alt/Text Metadata 63

Rectangle 64

### Alt/Text Metadata 64

Rectangle 65

### Alt/Text Metadata 65

Rectangle 66

### Alt/Text Metadata 66

Rectangle 67

### Alt/Text Metadata 67

Rectangle 68

### Alt/Text Metadata 68

Rectangle 69

### Alt/Text Metadata 69

Rectangle 70

### Alt/Text Metadata 70

Line 71

### Shape 71 Text Box 72

M

### Alt/Text Metadata 71

Text Box 72

### Shape 72 Text Box 73

T1

### Alt/Text Metadata 72

Text Box 73

### Shape 73 Text Box 74

T2

### Alt/Text Metadata 73

Text Box 74

### Shape 74 Text Box 75

T3

### Alt/Text Metadata 74

Text Box 75

### Shape 75 Text Box 76

T4

### Alt/Text Metadata 75

Text Box 76

### Alt/Text Metadata 76

Line 77

### Shape 77 Text Box 78

Warp 1

### Alt/Text Metadata 77

Text Box 78

### Alt/Text Metadata 78

Text Box 79

### Alt/Text Metadata 79

Text Box 80

### Alt/Text Metadata 80

Text Box 81

### Alt/Text Metadata 81

Text Box 82

### Shape 82 Text Box 83

Warp 2

### Alt/Text Metadata 82

Text Box 83

### Alt/Text Metadata 83

Line 85

### Alt/Text Metadata 84

Line 86

### Alt/Text Metadata 85

Line 87

### Alt/Text Metadata 86

Line 88

### Alt/Text Metadata 87

Line 89

### Alt/Text Metadata 88

Line 90

### Alt/Text Metadata 89

Line 91

### Alt/Text Metadata 90

Line 92

### Alt/Text Metadata 91

Rectangle 93

### Alt/Text Metadata 92

Rectangle 94

### Shape 93 Text Box 95

…

### Alt/Text Metadata 93

Text Box 95

### Shape 94 Marcador de número de diapositiva 3

38

### Alt/Text Metadata 94

Marcador de número de diapositiva 3

### Shape 95 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 95

CuadroTexto 26

### Shape 96 Text Box 84

Access direction of each thread

### Alt/Text Metadata 96

Text Box 84

### Notes XML fallback texts

- 112

## Slide 39

### Shape 1 Content Placeholder 1

Same instruction in different threads uses thread id to index and access different data elements

### Alt/Text Metadata 1

Content Placeholder 1

### Shape 2 Title 2

SIMT Memory Access

### Alt/Text Metadata 2

Title 2

### Shape 3 Content Placeholder 2

Let’s assume N=16, 4 threads per warp  4 warps

### Alt/Text Metadata 3

Content Placeholder 2

### Shape 4 Rectangle 4

0

### Alt/Text Metadata 4

Rectangle 4

### Shape 5 Rectangle 5

1

### Alt/Text Metadata 5

Rectangle 5

### Shape 6 Rectangle 6

2

### Alt/Text Metadata 6

Rectangle 6

### Shape 7 Rectangle 7

3

### Alt/Text Metadata 7

Rectangle 7

### Alt/Text Metadata 8

Rectangle 8

### Alt/Text Metadata 9

Rectangle 9

### Alt/Text Metadata 10

Rectangle 10

### Alt/Text Metadata 11

Rectangle 11

### Alt/Text Metadata 12

Rectangle 12

### Alt/Text Metadata 13

Rectangle 13

### Alt/Text Metadata 14

Rectangle 14

### Alt/Text Metadata 15

Rectangle 15

### Alt/Text Metadata 16

Rectangle 16

### Alt/Text Metadata 17

Rectangle 17

### Alt/Text Metadata 18

Rectangle 18

### Alt/Text Metadata 19

Rectangle 19

### Alt/Text Metadata 20

Rectangle 20

### Alt/Text Metadata 21

Rectangle 21

### Alt/Text Metadata 22

Rectangle 22

### Alt/Text Metadata 23

Rectangle 23

### Shape 24 Rectangle 24

4

### Alt/Text Metadata 24

Rectangle 24

### Shape 25 Rectangle 25

5

### Alt/Text Metadata 25

Rectangle 25

### Shape 26 Rectangle 26

6

### Alt/Text Metadata 26

Rectangle 26

### Shape 27 Rectangle 27

7

### Alt/Text Metadata 27

Rectangle 27

### Shape 28 Rectangle 28

8

### Alt/Text Metadata 28

Rectangle 28

### Shape 29 Rectangle 29

9

### Alt/Text Metadata 29

Rectangle 29

### Shape 30 Rectangle 30

10

### Alt/Text Metadata 30

Rectangle 30

### Shape 31 Rectangle 31

11

### Alt/Text Metadata 31

Rectangle 31

### Shape 32 Rectangle 32

12

### Alt/Text Metadata 32

Rectangle 32

### Shape 33 Rectangle 33

13

### Alt/Text Metadata 33

Rectangle 33

### Shape 34 Rectangle 34

14

### Alt/Text Metadata 34

Rectangle 34

### Shape 35 Rectangle 35

15

### Alt/Text Metadata 35

Rectangle 35

### Alt/Text Metadata 36

Rectangle 36

### Alt/Text Metadata 37

Rectangle 37

### Alt/Text Metadata 38

Rectangle 38

### Alt/Text Metadata 39

Rectangle 39

### Alt/Text Metadata 40

Rectangle 40

### Alt/Text Metadata 41

Rectangle 41

### Alt/Text Metadata 42

Rectangle 42

### Alt/Text Metadata 43

Rectangle 43

### Alt/Text Metadata 44

Rectangle 44

### Alt/Text Metadata 45

Rectangle 45

### Alt/Text Metadata 46

Rectangle 46

### Alt/Text Metadata 47

Rectangle 47

### Alt/Text Metadata 48

Rectangle 48

### Alt/Text Metadata 49

Rectangle 49

### Alt/Text Metadata 50

Rectangle 50

### Alt/Text Metadata 51

Rectangle 51

### Alt/Text Metadata 52

Rectangle 52

### Alt/Text Metadata 53

Rectangle 53

### Alt/Text Metadata 54

Rectangle 54

### Alt/Text Metadata 55

Rectangle 55

### Alt/Text Metadata 56

Rectangle 56

### Alt/Text Metadata 57

Rectangle 57

### Alt/Text Metadata 58

Rectangle 58

### Alt/Text Metadata 59

Rectangle 59

### Alt/Text Metadata 60

Rectangle 60

### Alt/Text Metadata 61

Rectangle 61

### Alt/Text Metadata 62

Rectangle 62

### Alt/Text Metadata 63

Rectangle 63

### Alt/Text Metadata 64

Rectangle 64

### Alt/Text Metadata 65

Rectangle 65

### Alt/Text Metadata 66

Rectangle 66

### Alt/Text Metadata 67

Rectangle 67

### Shape 68 TextBox 70

+

### Alt/Text Metadata 68

TextBox 70

### Alt/Text Metadata 69

TextBox 73

### Alt/Text Metadata 70

Freeform 10

### Alt/Text Metadata 71

Freeform 11

### Alt/Text Metadata 72

Freeform 12

### Alt/Text Metadata 73

Freeform 14

### Alt/Text Metadata 74

TextBox 79

### Alt/Text Metadata 79

TextBox 84

### Alt/Text Metadata 84

TextBox 89

### Alt/Text Metadata 89

Straight Connector 94

### Alt/Text Metadata 90

Straight Connector 95

### Alt/Text Metadata 91

Straight Connector 96

### Alt/Text Metadata 92

Straight Connector 97

### Alt/Text Metadata 93

Straight Connector 98

### Alt/Text Metadata 94

Straight Connector 99

### Alt/Text Metadata 95

Straight Connector 100

### Alt/Text Metadata 96

Straight Connector 101

### Shape 97 TextBox 134

Slide credit: Hyesoon Kim

### Alt/Text Metadata 97

TextBox 134

### Shape 98 TextBox 1

Threads

### Alt/Text Metadata 98

TextBox 1

### Shape 99 TextBox 102

Data elements

### Alt/Text Metadata 99

TextBox 102

### Shape 100 TextBox 103

Warp 0

### Alt/Text Metadata 100

TextBox 103

### Shape 101 TextBox 104

Warp 1

### Alt/Text Metadata 101

TextBox 104

### Shape 102 TextBox 105

Warp 2

### Alt/Text Metadata 102

TextBox 105

### Shape 103 TextBox 106

Warp 3

### Alt/Text Metadata 103

TextBox 106

### Shape 104 Slide Number Placeholder 3

39

### Alt/Text Metadata 104

Slide Number Placeholder 3

### Notes XML fallback texts

- 113

## Slide 40

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

40

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

### Notes XML fallback texts

- Distributed shared memory
- allows direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks.
- Distributed shared memory
- enables direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks
- 114

## Slide 41

### Shape 1 Título 1

Shared Memory

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Shared memory is an interleaved (banked) memory
Each bank can service one address per cycle
Typically, 32 banks in NVIDIA GPUs
Successive 32-bit words are assigned to successive banks
Bank = Address % 32
Bank conflicts are only possible within a warp
No bank conflicts between different warps

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

41

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Notes XML fallback texts

- 117

## Slide 42

### Shape 1 Título 1

Shared Memory Bank Conflicts (I)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Bank conflict free

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Group 6 | AutoShape 7 | AutoShape 8 | AutoShape 9 | AutoShape 10 | AutoShape 11 | AutoShape 12 | AutoShape 13 | AutoShape 14 | AutoShape 15 | Group 16 | Oval 17 | Oval 18 | Oval 19

### Shape 3.1 AutoShape 7

Bank 15

### Alt/Text Metadata 3.1

AutoShape 7

### Shape 3.2 AutoShape 8

Bank 7

### Alt/Text Metadata 3.2

AutoShape 8

### Shape 3.3 AutoShape 9

Bank 6

### Alt/Text Metadata 3.3

AutoShape 9

### Shape 3.4 AutoShape 10

Bank 5

### Alt/Text Metadata 3.4

AutoShape 10

### Shape 3.5 AutoShape 11

Bank 4

### Alt/Text Metadata 3.5

AutoShape 11

### Shape 3.6 AutoShape 12

Bank 3

### Alt/Text Metadata 3.6

AutoShape 12

### Shape 3.7 AutoShape 13

Bank 2

### Alt/Text Metadata 3.7

AutoShape 13

### Shape 3.8 AutoShape 14

Bank 1

### Alt/Text Metadata 3.8

AutoShape 14

### Shape 3.9 AutoShape 15

Bank 0

### Alt/Text Metadata 3.9

AutoShape 15

### Alt/Text Metadata 3.10

Group 16 | Oval 17 | Oval 18 | Oval 19

### Alt/Text Metadata 3.10.1

Oval 17

### Alt/Text Metadata 3.10.2

Oval 18

### Alt/Text Metadata 3.10.3

Oval 19

### Alt/Text Metadata 4

Group 20 | AutoShape 21 | AutoShape 22 | AutoShape 23 | AutoShape 24 | AutoShape 25 | AutoShape 26 | AutoShape 27 | AutoShape 28 | AutoShape 29 | Group 30 | Oval 31 | Oval 32 | Oval 33

### Shape 4.1 AutoShape 21

Thread 15

### Alt/Text Metadata 4.1

AutoShape 21

### Shape 4.2 AutoShape 22

Thread 7

### Alt/Text Metadata 4.2

AutoShape 22

### Shape 4.3 AutoShape 23

Thread 6

### Alt/Text Metadata 4.3

AutoShape 23

### Shape 4.4 AutoShape 24

Thread 5

### Alt/Text Metadata 4.4

AutoShape 24

### Shape 4.5 AutoShape 25

Thread 4

### Alt/Text Metadata 4.5

AutoShape 25

### Shape 4.6 AutoShape 26

Thread 3

### Alt/Text Metadata 4.6

AutoShape 26

### Shape 4.7 AutoShape 27

Thread 2

### Alt/Text Metadata 4.7

AutoShape 27

### Shape 4.8 AutoShape 28

Thread 1

### Alt/Text Metadata 4.8

AutoShape 28

### Shape 4.9 AutoShape 29

Thread 0

### Alt/Text Metadata 4.9

AutoShape 29

### Alt/Text Metadata 4.10

Group 30 | Oval 31 | Oval 32 | Oval 33

### Alt/Text Metadata 4.10.1

Oval 31

### Alt/Text Metadata 4.10.2

Oval 32

### Alt/Text Metadata 4.10.3

Oval 33

### Alt/Text Metadata 5

AutoShape 34

### Alt/Text Metadata 6

AutoShape 35

### Alt/Text Metadata 7

AutoShape 36

### Alt/Text Metadata 8

AutoShape 37

### Alt/Text Metadata 9

AutoShape 38

### Alt/Text Metadata 10

AutoShape 39

### Alt/Text Metadata 11

AutoShape 40

### Alt/Text Metadata 12

AutoShape 41

### Alt/Text Metadata 13

AutoShape 42

### Alt/Text Metadata 14

Group 44 | AutoShape 45 | AutoShape 46 | AutoShape 47 | AutoShape 48 | AutoShape 49 | AutoShape 50 | AutoShape 51 | AutoShape 52 | AutoShape 53 | Group 54 | Oval 55 | Oval 56 | Oval 57

### Alt/Text Metadata 14.1

AutoShape 45

### Alt/Text Metadata 14.2

AutoShape 46

### Alt/Text Metadata 14.3

AutoShape 47

### Alt/Text Metadata 14.4

AutoShape 48

### Alt/Text Metadata 14.5

AutoShape 49

### Alt/Text Metadata 14.6

AutoShape 50

### Alt/Text Metadata 14.7

AutoShape 51

### Alt/Text Metadata 14.8

AutoShape 52

### Alt/Text Metadata 14.9

AutoShape 53

### Alt/Text Metadata 14.10

Group 54 | Oval 55 | Oval 56 | Oval 57

### Alt/Text Metadata 14.10.1

Oval 55

### Alt/Text Metadata 14.10.2

Oval 56

### Alt/Text Metadata 14.10.3

Oval 57

### Alt/Text Metadata 15

Group 58 | AutoShape 59 | AutoShape 60 | AutoShape 61 | AutoShape 62 | AutoShape 63 | AutoShape 64 | AutoShape 65 | AutoShape 66 | AutoShape 67 | Group 68 | Oval 69 | Oval 70 | Oval 71

### Alt/Text Metadata 15.1

AutoShape 59

### Alt/Text Metadata 15.2

AutoShape 60

### Alt/Text Metadata 15.3

AutoShape 61

### Alt/Text Metadata 15.4

AutoShape 62

### Alt/Text Metadata 15.5

AutoShape 63

### Alt/Text Metadata 15.6

AutoShape 64

### Alt/Text Metadata 15.7

AutoShape 65

### Alt/Text Metadata 15.8

AutoShape 66

### Alt/Text Metadata 15.9

AutoShape 67

### Alt/Text Metadata 15.10

Group 68 | Oval 69 | Oval 70 | Oval 71

### Alt/Text Metadata 15.10.1

Oval 69

### Alt/Text Metadata 15.10.2

Oval 70

### Alt/Text Metadata 15.10.3

Oval 71

### Alt/Text Metadata 16

AutoShape 72

### Alt/Text Metadata 17

AutoShape 73

### Alt/Text Metadata 18

AutoShape 74

### Alt/Text Metadata 19

AutoShape 75

### Alt/Text Metadata 20

AutoShape 76

### Alt/Text Metadata 21

AutoShape 77

### Alt/Text Metadata 22

AutoShape 78

### Alt/Text Metadata 23

AutoShape 79

### Alt/Text Metadata 24

AutoShape 80

### Shape 25 CuadroTexto 80

Linear addressing: stride = 1

### Alt/Text Metadata 25

CuadroTexto 80

### Shape 26 CuadroTexto 81

Random addressing 1:1

### Alt/Text Metadata 26

CuadroTexto 81

### Shape 27 Marcador de número de diapositiva 3

42

### Alt/Text Metadata 27

Marcador de número de diapositiva 3

### Shape 28 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 28

CuadroTexto 26

### Notes XML fallback texts

- 118

## Slide 43

### Shape 1 Título 1

Shared Memory Bank Conflicts (II)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

N-way bank conflicts

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 80

2-way bank conflict: stride = 2

### Alt/Text Metadata 3

CuadroTexto 80

### Shape 4 CuadroTexto 81

8-way bank conflict: stride = 8

### Alt/Text Metadata 4

CuadroTexto 81

### Shape 5 AutoShape 6

Thread 11

### Alt/Text Metadata 5

AutoShape 6

### Shape 6 AutoShape 7

Thread 10

### Alt/Text Metadata 6

AutoShape 7

### Shape 7 AutoShape 8

Thread 9

### Alt/Text Metadata 7

AutoShape 8

### Shape 8 AutoShape 9

Thread 8

### Alt/Text Metadata 8

AutoShape 9

### Shape 9 AutoShape 10

Thread 4

### Alt/Text Metadata 9

AutoShape 10

### Shape 10 AutoShape 11

Thread 3

### Alt/Text Metadata 10

AutoShape 11

### Shape 11 AutoShape 12

Thread 2

### Alt/Text Metadata 11

AutoShape 12

### Shape 12 AutoShape 13

Thread 1

### Alt/Text Metadata 12

AutoShape 13

### Shape 13 AutoShape 14

Thread 0

### Alt/Text Metadata 13

AutoShape 14

### Alt/Text Metadata 14

Group 15 | Oval 16 | Oval 17 | Oval 18

### Alt/Text Metadata 14.1

Oval 16

### Alt/Text Metadata 14.2

Oval 17

### Alt/Text Metadata 14.3

Oval 18

### Alt/Text Metadata 15

AutoShape 19

### Alt/Text Metadata 16

AutoShape 20

### Alt/Text Metadata 17

AutoShape 21

### Alt/Text Metadata 18

AutoShape 22

### Alt/Text Metadata 19

AutoShape 23

### Alt/Text Metadata 20

AutoShape 24

### Alt/Text Metadata 21

AutoShape 25

### Alt/Text Metadata 22

AutoShape 26

### Alt/Text Metadata 23

AutoShape 27

### Shape 24 AutoShape 29

Bank 15

### Alt/Text Metadata 24

AutoShape 29

### Shape 25 AutoShape 30

Bank 7

### Alt/Text Metadata 25

AutoShape 30

### Shape 26 AutoShape 31

Bank 6

### Alt/Text Metadata 26

AutoShape 31

### Shape 27 AutoShape 32

Bank 5

### Alt/Text Metadata 27

AutoShape 32

### Shape 28 AutoShape 33

Bank 4

### Alt/Text Metadata 28

AutoShape 33

### Shape 29 AutoShape 34

Bank 3

### Alt/Text Metadata 29

AutoShape 34

### Shape 30 AutoShape 35

Bank 2

### Alt/Text Metadata 30

AutoShape 35

### Shape 31 AutoShape 36

Bank 1

### Alt/Text Metadata 31

AutoShape 36

### Shape 32 AutoShape 37

Bank 0

### Alt/Text Metadata 32

AutoShape 37

### Alt/Text Metadata 33

Group 38 | Oval 39 | Oval 40 | Oval 41

### Alt/Text Metadata 33.1

Oval 39

### Alt/Text Metadata 33.2

Oval 40

### Alt/Text Metadata 33.3

Oval 41

### Alt/Text Metadata 34

Group 43 | AutoShape 44 | AutoShape 45 | AutoShape 46 | AutoShape 47 | AutoShape 48 | AutoShape 49 | AutoShape 50 | AutoShape 51 | AutoShape 52 | Group 53 | Oval 54 | Oval 55 | Oval 56

### Shape 34.1 AutoShape 44

Thread 15

### Alt/Text Metadata 34.1

AutoShape 44

### Shape 34.2 AutoShape 45

Thread 7

### Alt/Text Metadata 34.2

AutoShape 45

### Shape 34.3 AutoShape 46

Thread 6

### Alt/Text Metadata 34.3

AutoShape 46

### Shape 34.4 AutoShape 47

Thread 5

### Alt/Text Metadata 34.4

AutoShape 47

### Alt/Text Metadata 34.5

AutoShape 48

### Alt/Text Metadata 34.6

AutoShape 49

### Alt/Text Metadata 34.7

AutoShape 50

### Alt/Text Metadata 34.8

AutoShape 51

### Alt/Text Metadata 34.9

AutoShape 52

### Alt/Text Metadata 34.10

Group 53 | Oval 54 | Oval 55 | Oval 56

### Alt/Text Metadata 34.10.1

Oval 54

### Alt/Text Metadata 34.10.2

Oval 55

### Alt/Text Metadata 34.10.3

Oval 56

### Alt/Text Metadata 35

AutoShape 57

### Alt/Text Metadata 36

AutoShape 58

### Alt/Text Metadata 37

AutoShape 59

### Alt/Text Metadata 38

AutoShape 60

### Alt/Text Metadata 39

AutoShape 61

### Alt/Text Metadata 40

AutoShape 62

### Alt/Text Metadata 41

AutoShape 63

### Alt/Text Metadata 42

AutoShape 64

### Alt/Text Metadata 43

AutoShape 65

### Shape 44 AutoShape 67

Bank 9

### Alt/Text Metadata 44

AutoShape 67

### Shape 45 AutoShape 68

Bank 8

### Alt/Text Metadata 45

AutoShape 68

### Alt/Text Metadata 46

AutoShape 69

### Alt/Text Metadata 47

AutoShape 70

### Alt/Text Metadata 48

AutoShape 71

### Alt/Text Metadata 49

AutoShape 72

### Alt/Text Metadata 50

AutoShape 73

### Alt/Text Metadata 51

Group 74 | Oval 75 | Oval 76 | Oval 77

### Alt/Text Metadata 51.1

Oval 75

### Alt/Text Metadata 51.2

Oval 76

### Alt/Text Metadata 51.3

Oval 77

### Alt/Text Metadata 52

Group 78 | Oval 79 | Oval 80 | Oval 81

### Alt/Text Metadata 52.1

Oval 79

### Alt/Text Metadata 52.2

Oval 80

### Alt/Text Metadata 52.3

Oval 81

### Shape 53 Text Box 82

x8

### Alt/Text Metadata 53

Text Box 82

### Alt/Text Metadata 54

Text Box 83

### Shape 55 Marcador de número de diapositiva 3

43

### Alt/Text Metadata 55

Marcador de número de diapositiva 3

### Shape 56 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 56

CuadroTexto 26

### Notes XML fallback texts

- 120

## Slide 44

### Shape 1 Rectangle 2

Use Shared Memory to Improve Coalescing

### Alt/Text Metadata 1

Rectangle 2

### Alt/Text Metadata 2

Line 3

### Alt/Text Metadata 3

Freeform 5

### Alt/Text Metadata 4

Rectangle 6

### Shape 5 Rectangle 7

Md

### Alt/Text Metadata 5

Rectangle 7

### Alt/Text Metadata 6

Freeform 8

### Alt/Text Metadata 7

Rectangle 9

### Shape 8 Rectangle 10

Nd

### Alt/Text Metadata 8

Rectangle 10

### Alt/Text Metadata 9

Freeform 11

### Alt/Text Metadata 10

Freeform 12

### Alt/Text Metadata 11

Freeform 13

### Alt/Text Metadata 12

Freeform 14

### Alt/Text Metadata 13

Freeform 15

### Alt/Text Metadata 14

Freeform 16

### Shape 15 Rectangle 17

W

### Alt/Text Metadata 15

Rectangle 17

### Shape 16 Rectangle 18

I

### Alt/Text Metadata 16

Rectangle 18

### Shape 17 Rectangle 19

D

### Alt/Text Metadata 17

Rectangle 19

### Shape 18 Rectangle 20

T

### Alt/Text Metadata 18

Rectangle 20

### Shape 19 Rectangle 21

H

### Alt/Text Metadata 19

Rectangle 21

### Shape 20 Rectangle 22

WIDTH

### Alt/Text Metadata 20

Rectangle 22

### Alt/Text Metadata 21

Freeform 23

### Alt/Text Metadata 22

Rectangle 24

### Alt/Text Metadata 23

Rectangle 25

### Alt/Text Metadata 24

Freeform 26

### Alt/Text Metadata 25

Rectangle 27

### Alt/Text Metadata 26

Rectangle 28

### Alt/Text Metadata 27

Freeform 31

### Alt/Text Metadata 28

Freeform 32

### Alt/Text Metadata 29

Freeform 33

### Alt/Text Metadata 30

Freeform 34

### Shape 31 Rectangle 67

Original

### Alt/Text Metadata 31

Rectangle 67

### Shape 32 Rectangle 68

Access

### Alt/Text Metadata 32

Rectangle 68

### Shape 33 Rectangle 69

Pattern

### Alt/Text Metadata 33

Rectangle 69

### Shape 34 Rectangle 70

Tiled

### Alt/Text Metadata 34

Rectangle 70

### Alt/Text Metadata 35

Rectangle 71

### Alt/Text Metadata 36

Rectangle 72

### Alt/Text Metadata 37

Freeform 73

### Alt/Text Metadata 38

Freeform 74

### Alt/Text Metadata 39

Freeform 76

### Shape 40 Rectangle 77

Copy into

### Alt/Text Metadata 40

Rectangle 77

### Shape 41 Rectangle 78

scratchpad

### Alt/Text Metadata 41

Rectangle 78

### Shape 42 Rectangle 79

memory

### Alt/Text Metadata 42

Rectangle 79

### Shape 43 Rectangle 80

Perform

### Alt/Text Metadata 43

Rectangle 80

### Shape 44 Rectangle 81

multiplication

### Alt/Text Metadata 44

Rectangle 81

### Shape 45 Rectangle 82

with scratchpad

### Alt/Text Metadata 45

Rectangle 82

### Shape 46 Rectangle 83

values

### Alt/Text Metadata 46

Rectangle 83

### Shape 47 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 47

CuadroTexto 26

### Shape 48 Marcador de número de diapositiva 3

44

### Alt/Text Metadata 48

Marcador de número de diapositiva 3

### Alt/Text Metadata 49

Freeform 30

### Alt/Text Metadata 50

Rectangle 53

### Alt/Text Metadata 51

Rectangle 57

### Alt/Text Metadata 52

Rectangle 61

### Alt/Text Metadata 53

Rectangle 65

### Alt/Text Metadata 54

Rectangle 41

### Alt/Text Metadata 55

Rectangle 45

### Alt/Text Metadata 56

Rectangle 49

### Alt/Text Metadata 57

Freeform 75

### Alt/Text Metadata 58

Freeform 29

### Alt/Text Metadata 59

Rectangle 37

## Slide 45

### Shape 1 Título 1

Reducing Shared Memory Bank Conflicts

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Bank conflicts are only possible within a warp
No bank conflicts between different warps
If strided accesses are needed, some optimization techniques can help
Padding
Randomized mapping
Rau, “Pseudo-randomly interleaved memory,” ISCA 1991
Hash functions
V.d.Braak+, “Configurable XOR Hash Functions for Banked Scratchpad Memories in GPUs,” IEEE TC, 2016

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

45

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

## Slide 46

### Shape 1 Título 1

No Data Reuse

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

No Data reuse:
Each thread reads its only elements.

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 6

for (int i = 0; i < 3; i++){
    for (int j = 0; j < 3; j++){
        sum += gauss[i][j] * Image[(i+row-1)*width + (j+col-1)];
    }
}

### Alt/Text Metadata 3

CuadroTexto 6

### Alt/Text Metadata 4

Imagen 7

### Relationships 4

- rId3: image:../media/image28.emf

### Shape 5 Marcador de número de diapositiva 3

46

### Alt/Text Metadata 5

Marcador de número de diapositiva 3

### Shape 6 文本框 4

Loading Amount:
9 elements per thread

### Alt/Text Metadata 6

文本框 4

### Speaker notes

对每一个row，col,计算一个sum。

### Slide media/diagram relationships

- rId3: image:../media/image28.emf

## Slide 47

### Shape 1 Título 1

Data Reuse: Tiling

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

For data reuse, we divide the input into tiles, each of which loads L_SIZE chunks together into shared memory, then compute together

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 8

### Relationships 3

- rId3: image:../media/image29.emf

### Shape 4 CuadroTexto 9

__shared__ int l_data[(L_SIZE+2)*(L_SIZE+2)];
…
Load tile into shared memory l_data
__syncthreads();
for (int i = 0; i < 3; i++){
  for (int j = 0; j < 3; j++){
    sum += gauss[i][j] * l_data[(i+l_row-1)*(L_SIZE+2)+j+l_col-1];
  }
}

### Alt/Text Metadata 4

CuadroTexto 9

### Shape 5 Marcador de número de diapositiva 3

47

### Alt/Text Metadata 5

Marcador de número de diapositiva 3

### Shape 6 文本框 6

Loading Amount:
(L_SIZE+2)2/L_SIZE2
elements per thread

### Alt/Text Metadata 6

文本框 6

### Shape 7 文本框 6

Compute Amount:
The same

### Speaker notes

L_SIZE: number of points together…

### Slide media/diagram relationships

- rId3: image:../media/image29.emf

## Slide 48

### Shape 1 Rectangle 3

void __syncthreads();
Synchronizes all threads in a block
Once all threads in a block have reached this point, execution resumes normally
Used to avoid RAW / WAR / WAW hazards when accessing shared or global memory

### Alt/Text Metadata 1

Rectangle 3

### Shape 2 Marcador de número de diapositiva 5

48

### Alt/Text Metadata 2

Marcador de número de diapositiva 5

### Shape 3 Title 2

Synchronization Function

### Alt/Text Metadata 3

Title 2

## Slide 49

### Shape 1 Title 1

Tiling/Blocking in On-chip Memories

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Tiling or Blocking
Divide loops operating on arrays into computation chunks so that each chunk can hold its data in the on-chip RAM (or other on-chip memory, e.g., scratchpad)
Avoids on-chip RAM conflicts between different chunks of computation
Essentially: Divide the working set so that each piece fits in the on-chip RAMs

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

49

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 50

### Shape 1 Title 1

CPU: Naïve Matrix Multiplication (I)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Matrix multiplication: C = A x B
Consider two input matrices A and B in row-major layout
A size is M x P
B size is P x N
C size is M x N

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

50

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 5 | Shape 104 | Shape 105 | Shape 106 | Shape 107 | Shape 108 | Shape 109 | Shape 110 | Shape 115 | Shape 116 | Shape 117 | Shape 118 | Shape 119 | Shape 120 | Shape 121 | Shape 122 | Shape 123 | Shape 124 | Shape 125 | Shape 126 | Shape 127

### Shape 4.1 Shape 104

A

### Alt/Text Metadata 4.1

Shape 104

### Shape 4.2 Shape 105

B

### Alt/Text Metadata 4.2

Shape 105

### Shape 4.3 Shape 106

C

### Alt/Text Metadata 4.3

Shape 106

### Alt/Text Metadata 4.4

Shape 107

### Alt/Text Metadata 4.5

Shape 108

### Alt/Text Metadata 4.6

Shape 109

### Alt/Text Metadata 4.7

Shape 110

### Alt/Text Metadata 4.8

Shape 115

### Alt/Text Metadata 4.9

Shape 116

### Alt/Text Metadata 4.10

Shape 117

### Shape 4.11 Shape 118

P

### Alt/Text Metadata 4.11

Shape 118

### Shape 4.12 Shape 119

M

### Alt/Text Metadata 4.12

Shape 119

### Alt/Text Metadata 4.13

Shape 120

### Shape 4.14 Shape 121

N

### Alt/Text Metadata 4.14

Shape 121

### Shape 4.15 Shape 122

i

### Alt/Text Metadata 4.15

Shape 122

### Shape 4.16 Shape 123

j

### Alt/Text Metadata 4.16

Shape 123

### Alt/Text Metadata 4.17

Shape 124

### Alt/Text Metadata 4.18

Shape 125

### Alt/Text Metadata 4.19

Shape 126

### Alt/Text Metadata 4.20

Shape 127

### Shape 4.21 Shape 123

k

## Slide 51

### Shape 1 Title 1

CPU: Naïve Matrix Multiplication (II)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Naïve implementation of matrix multiplication
Poor access locality

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

51

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 1

#define A(i,j) matrix_A[i * P + j]
#define B(i,j) matrix_B[i * N + j]
#define C(i,j) matrix_C[i * N + j]
for (i = 0; i < M; i++){ // i = row index
    for (j = 0; j < N; j++){ // j = column index
        C(i, j) = 0; // Set to zero
        for (k = 0; k < P; k++) // Row x Col
            C(i, j) += A(i, k) * B(k, j);
    }
}

### Alt/Text Metadata 4

TextBox 1

### Alt/Text Metadata 5

Group 5 | Shape 104 | Shape 105 | Shape 106 | Shape 107 | Shape 108 | Shape 109 | Shape 110 | Shape 115 | Shape 116 | Shape 117 | Shape 118 | Shape 119 | Shape 120 | Shape 121 | Shape 122 | Shape 123 | Shape 124 | Shape 125 | Shape 126 | Shape 127

### Shape 5.1 Shape 104

A

### Alt/Text Metadata 5.1

Shape 104

### Shape 5.2 Shape 105

B

### Alt/Text Metadata 5.2

Shape 105

### Shape 5.3 Shape 106

C

### Alt/Text Metadata 5.3

Shape 106

### Alt/Text Metadata 5.4

Shape 107

### Alt/Text Metadata 5.5

Shape 108

### Alt/Text Metadata 5.6

Shape 109

### Alt/Text Metadata 5.7

Shape 110

### Alt/Text Metadata 5.8

Shape 115

### Alt/Text Metadata 5.9

Shape 116

### Alt/Text Metadata 5.10

Shape 117

### Shape 5.11 Shape 118

P

### Alt/Text Metadata 5.11

Shape 118

### Shape 5.12 Shape 119

M

### Alt/Text Metadata 5.12

Shape 119

### Alt/Text Metadata 5.13

Shape 120

### Shape 5.14 Shape 121

N

### Alt/Text Metadata 5.14

Shape 121

### Shape 5.15 Shape 122

i

### Alt/Text Metadata 5.15

Shape 122

### Shape 5.16 Shape 123

j

### Alt/Text Metadata 5.16

Shape 123

### Alt/Text Metadata 5.17

Shape 124

### Alt/Text Metadata 5.18

Shape 125

### Alt/Text Metadata 5.19

Shape 126

### Alt/Text Metadata 5.20

Shape 127

### Shape 5.21 Shape 123

k

### Alt/Text Metadata 6

Oval 2

### Alt/Text Metadata 7

Straight Arrow Connector 4

### Shape 8 TextBox 31

Consecutive accesses to B are far from each other, in different memory lines.
Every access to B is likely to cause a row buffer miss

### Alt/Text Metadata 8

TextBox 31

## Slide 52

### Shape 1 Title 1

CPU: Tiled Matrix Multiplication (I)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Tiled Matrix Multiplication:
Achieve better on-chip RAM locality by computing on smaller tiles or blocks that fit in the RAMs

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

52

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 Shape 104

A

### Alt/Text Metadata 4

Shape 104

### Shape 5 Shape 105

B

### Alt/Text Metadata 5

Shape 105

### Shape 6 Shape 106

C

### Alt/Text Metadata 6

Shape 106

### Alt/Text Metadata 7

Shape 107

### Alt/Text Metadata 8

Shape 108

### Alt/Text Metadata 9

Shape 109

### Alt/Text Metadata 10

Shape 110

### Alt/Text Metadata 11

Shape 115

### Alt/Text Metadata 12

Shape 116

### Alt/Text Metadata 13

Shape 117

### Shape 14 Shape 118

P

### Alt/Text Metadata 14

Shape 118

### Shape 15 Shape 119

M

### Alt/Text Metadata 15

Shape 119

### Alt/Text Metadata 16

Shape 120

### Shape 17 Shape 121

N

### Alt/Text Metadata 17

Shape 121

### Alt/Text Metadata 18

Shape 124

### Alt/Text Metadata 19

Shape 125

### Alt/Text Metadata 20

Shape 126

### Alt/Text Metadata 21

Shape 127

### Alt/Text Metadata 22

Shape 216

### Shape 26 Shape 123

k

### Alt/Text Metadata 26

Shape 123

### Shape 32 Shape 120

tile_dim

### Shape 36 Shape 122

i

### Alt/Text Metadata 36

Shape 122

### Shape 37 Shape 123

j

### Shape 38 TextBox 65

Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4

### Alt/Text Metadata 38

TextBox 65

## Slide 53

### Shape 1 Title 1

CPU: Tiled Matrix Multiplication (II)

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Tiled implementation operates on submatrices (tiles or blocks) that fit fast RAMs (cache, scratchpad, RF)

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

53

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 1

#define A(i,j) matrix_A[i * P + j]
#define B(i,j) matrix_B[i * N + j]
#define C(i,j) matrix_C[i * N + j]
for (I = 0; I < M; I += tile_dim){
    for (J = 0; J < N; J += tile_dim){
        Set_to_zero(&C(I, J)); // Set to zero
        for (K = 0; K < P; K += tile_dim)
            Multiply_tiles(&C(I, J), &A(I, K), &B(K, J));
    }
}

### Alt/Text Metadata 4

TextBox 1

### Alt/Text Metadata 5

Straight Arrow Connector 4

### Shape 6 TextBox 31

Multiply small submatrices (tiles or blocks) of size tile_dim x tile_dim

### Alt/Text Metadata 6

TextBox 31

### Alt/Text Metadata 7

Group 3 | Shape 104 | Shape 105 | Shape 106 | Shape 107 | Shape 108 | Shape 109 | Shape 110 | Shape 115 | Shape 116 | Shape 117 | Shape 118 | Shape 119 | Shape 120 | Shape 121 | Shape 124 | Shape 125 | Shape 126 | Shape 127 | Shape 216 | Shape 123 | Shape 122

### Shape 7.1 Shape 104

A

### Alt/Text Metadata 7.1

Shape 104

### Shape 7.2 Shape 105

B

### Alt/Text Metadata 7.2

Shape 105

### Shape 7.3 Shape 106

C

### Alt/Text Metadata 7.3

Shape 106

### Alt/Text Metadata 7.4

Shape 107

### Alt/Text Metadata 7.5

Shape 108

### Alt/Text Metadata 7.6

Shape 109

### Alt/Text Metadata 7.7

Shape 110

### Alt/Text Metadata 7.8

Shape 115

### Alt/Text Metadata 7.9

Shape 116

### Alt/Text Metadata 7.10

Shape 117

### Shape 7.11 Shape 118

P

### Alt/Text Metadata 7.11

Shape 118

### Shape 7.12 Shape 119

M

### Alt/Text Metadata 7.12

Shape 119

### Alt/Text Metadata 7.13

Shape 120

### Shape 7.14 Shape 121

N

### Alt/Text Metadata 7.14

Shape 121

### Alt/Text Metadata 7.15

Shape 124

### Alt/Text Metadata 7.16

Shape 125

### Alt/Text Metadata 7.17

Shape 126

### Alt/Text Metadata 7.18

Shape 127

### Alt/Text Metadata 7.19

Shape 216

### Shape 7.23 Shape 123

k

### Alt/Text Metadata 7.23

Shape 123

### Shape 7.29 Shape 120

tile_dim

### Shape 7.33 Shape 122

i

### Alt/Text Metadata 7.33

Shape 122

### Shape 7.34 Shape 123

j

### Alt/Text Metadata 8

Rounded Rectangle 30

### Shape 9 TextBox 67

Lam+, "The cache performance and optimizations of blocked algorithms," ASPLOS 1991. https://doi.org/10.1145/106972.106981
Bansal+, "Chapter 15 - Fast Matrix Computations on Heterogeneous Streams," in "High Performance Parallelism Pearls", 2015. https://doi.org/10.1016/B978-0-12-803819-2.00011-2
Kirk & Hwu, "Chapter 5 - Performance considerations," in "Programming Massively Parallel Processors (Third Edition)", 2017. https://doi.org/10.1016/B978-0-12-811986-0.00005-4

### Alt/Text Metadata 9

TextBox 67

## Slide 54

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Matrix-Matrix Multiplication (I)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 6

C = A x B

### Alt/Text Metadata 5

TextBox 6

### Shape 6 TextBox 7

A

### Alt/Text Metadata 6

TextBox 7

### Shape 7 TextBox 8

B

### Alt/Text Metadata 7

TextBox 8

### Shape 8 TextBox 9

C

### Alt/Text Metadata 8

TextBox 9

### Alt/Text Metadata 9

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 9.1

Straight Arrow Connector 22

### Alt/Text Metadata 9.2

TextBox 23

### Alt/Text Metadata 10

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 10.1

Straight Arrow Connector 25

### Alt/Text Metadata 10.2

TextBox 26

### Table 11 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 27

### Table 12 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 12

Table 28

### Alt/Text Metadata 13

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 13.1

Straight Arrow Connector 45

### Alt/Text Metadata 13.2

TextBox 46

### Alt/Text Metadata 14

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 14.1

Straight Arrow Connector 48

### Alt/Text Metadata 14.2

TextBox 49

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 Slide Number Placeholder 3

54

### Alt/Text Metadata 16

Slide Number Placeholder 3

## Slide 55

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Matrix-Matrix Multiplication (II)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 TextBox 50

Parallelization approach: assign one thread to each element in the output matrix (C)

### Alt/Text Metadata 14

TextBox 50

### Table 15 Table 30

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 15

Table 30

### Shape 16 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 16

TextBox 610

### Shape 17 TextBox 31

C = A x B

### Alt/Text Metadata 17

TextBox 31

### Shape 18 Slide Number Placeholder 3

55

### Alt/Text Metadata 18

Slide Number Placeholder 3

## Slide 56

### Shape 1 Title 1

GPU: Matrix-Matrix Multiplication (III)

### Alt/Text Metadata 1

Title 1

### Shape 2 Rectangle 2

__global__ void mm_kernel(float* A, float* B, float* C, unsigned int N) {
    unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
    unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
    float sum = 0.0f;
    for(unsigned int i = 0; i < N; ++i) {
        sum += A[row*N + i]*B[i*N + col];
    }
    C[row*N + col] = sum;
}

### Alt/Text Metadata 2

Rectangle 2

### Shape 3 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 3

TextBox 610

### Shape 4 Slide Number Placeholder 3

56

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 5

### Relationships 5

- rId2: image:../media/image30.emf

### Slide media/diagram relationships

- rId2: image:../media/image30.emf

## Slide 57

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Reuse in Matrix-Matrix Multiplication (I)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 Rectangle 33

Some of the threads in the same thread block use the same input data

### Alt/Text Metadata 14

Rectangle 33

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 TextBox 30

C = A x B

### Alt/Text Metadata 16

TextBox 30

### Shape 17 Slide Number Placeholder 3

57

### Alt/Text Metadata 17

Slide Number Placeholder 3

## Slide 58

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Reuse in Matrix-Matrix Multiplication (II)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 Rectangle 33

Some of the threads in the same thread block use the same input data

### Alt/Text Metadata 14

Rectangle 33

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 TextBox 30

C = A x B

### Alt/Text Metadata 16

TextBox 30

### Shape 17 Slide Number Placeholder 3

58

### Alt/Text Metadata 17

Slide Number Placeholder 3

## Slide 59

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Tiled Matrix-Matrix Multiplication (I)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 Rectangle 29

Step 1: Load the first tile of each input matrix to shared memory (each thread loads one element)

### Alt/Text Metadata 14

Rectangle 29

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 TextBox 31

Ctile = Atile1 x Btile1

### Alt/Text Metadata 16

TextBox 31

### Shape 17 Slide Number Placeholder 3

59

### Alt/Text Metadata 17

Slide Number Placeholder 3

## Slide 60

### Table 1 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 1

Table 27

### Table 2 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 2

Table 11

### Shape 3 Title 1

GPU: Tiled Matrix-Matrix Multiplication (II)

### Alt/Text Metadata 3

Title 1

### Shape 4 TextBox 6

Ctile += Atile2 x Btile2

### Alt/Text Metadata 4

TextBox 6

### Shape 5 TextBox 7

Atile2

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

Btile2

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

Ctile

### Alt/Text Metadata 7

TextBox 9

### Table 8 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 8

Table 28

### Shape 9 Rectangle 29

Step 2: Each thread computes its partial sum from the tiles in shared memory (threads wait for each other to finish)

### Alt/Text Metadata 9

Rectangle 29

### Shape 10 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 10

TextBox 610

### Shape 11 Slide Number Placeholder 3

60

### Alt/Text Metadata 11

Slide Number Placeholder 3

## Slide 61

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Tiled Matrix-Matrix Multiplication (III)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 Rectangle 29

…accumulate the second tile

### Alt/Text Metadata 14

Rectangle 29

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 TextBox 31

Ctile += Atile2 x Btile2

### Alt/Text Metadata 16

TextBox 31

### Shape 17 Slide Number Placeholder 3

61

### Alt/Text Metadata 17

Slide Number Placeholder 3

## Slide 62

### Alt/Text Metadata 1

Group 15 | Straight Arrow Connector 13 | TextBox 14

### Alt/Text Metadata 1.1

Straight Arrow Connector 13

### Shape 1.2 TextBox 14

N

### Alt/Text Metadata 1.2

TextBox 14

### Alt/Text Metadata 2

Group 20 | Straight Arrow Connector 17 | TextBox 19

### Alt/Text Metadata 2.1

Straight Arrow Connector 17

### Alt/Text Metadata 2.2

TextBox 19

### Table 3 Table 11

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 3

Table 11

### Shape 4 Title 1

GPU: Tiled Matrix-Matrix Multiplication (IV)

### Alt/Text Metadata 4

Title 1

### Shape 5 TextBox 7

A

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 8

B

### Alt/Text Metadata 6

TextBox 8

### Shape 7 TextBox 9

C

### Alt/Text Metadata 7

TextBox 9

### Alt/Text Metadata 8

Group 21 | Straight Arrow Connector 22 | TextBox 23

### Alt/Text Metadata 8.1

Straight Arrow Connector 22

### Alt/Text Metadata 8.2

TextBox 23

### Alt/Text Metadata 9

Group 24 | Straight Arrow Connector 25 | TextBox 26

### Alt/Text Metadata 9.1

Straight Arrow Connector 25

### Alt/Text Metadata 9.2

TextBox 26

### Table 10 Table 27

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 10

Table 27

### Table 11 Table 28

-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 
-  |  |  |  |  |  |  |  |  |  |  | 

### Alt/Text Metadata 11

Table 28

### Alt/Text Metadata 12

Group 44 | Straight Arrow Connector 45 | TextBox 46

### Alt/Text Metadata 12.1

Straight Arrow Connector 45

### Alt/Text Metadata 12.2

TextBox 46

### Alt/Text Metadata 13

Group 47 | Straight Arrow Connector 48 | TextBox 49

### Alt/Text Metadata 13.1

Straight Arrow Connector 48

### Alt/Text Metadata 13.2

TextBox 49

### Shape 14 Rectangle 30

…and accumulate the third tile

### Alt/Text Metadata 14

Rectangle 30

### Shape 15 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 15

TextBox 610

### Shape 16 TextBox 31

Ctile += Atile3 x Btile3

### Alt/Text Metadata 16

TextBox 31

### Shape 17 Slide Number Placeholder 3

62

### Alt/Text Metadata 17

Slide Number Placeholder 3

## Slide 63

### Shape 1 Title 1

GPU: Tiled Matrix-Matrix Multiplication (V)

### Alt/Text Metadata 1

Title 1

### Shape 2 Rectangle 4

__shared__ float A_s[TILE_DIM][TILE_DIM];
__shared__ float B_s[TILE_DIM][TILE_DIM];
unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;
float sum = 0.0f;
for(unsigned int tile = 0; tile < N/TILE_DIM; ++tile) {
    // Load tile to shared memory
    A_s[threadIdx.y][threadIdx.x] = A[row*N + tile*TILE_DIM + threadIdx.x];
    B_s[threadIdx.y][threadIdx.x] = B[(tile*TILE_DIM + threadIdx.y)*N + col];
    __syncthreads();
    // Compute with tile
    for(unsigned int i = 0; i < TILE_DIM; ++i) {
        sum += A_s[threadIdx.y][i]*B_s[i][threadIdx.x];
    }
    __syncthreads();
}
C[row*N + col] = sum;

### Alt/Text Metadata 2

Rectangle 4

### Shape 3 TextBox 5

Declare arrays in shared memory

### Alt/Text Metadata 3

TextBox 5

### Shape 4 TextBox 6

Threads wait for each other to finish loading before computing

### Alt/Text Metadata 4

TextBox 6

### Shape 5 TextBox 7

Threads wait for each other to finish computing before loading

### Alt/Text Metadata 5

TextBox 7

### Shape 6 TextBox 610

Slide credit: Izzat El Hajj

### Alt/Text Metadata 6

TextBox 610

### Shape 7 Slide Number Placeholder 3

63

### Alt/Text Metadata 7

Slide Number Placeholder 3

## Slide 64

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

64

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

## Slide 65

### Shape 1 Title 1

Threads Can Take Different Paths in Warp-based SIMT

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Each thread can have conditional control flow instructions
Threads can execute different control flow paths

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

65

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 82 | Rectangle 74 | Rectangle 75 | Rectangle 76

### Alt/Text Metadata 4.1

Rectangle 74

### Shape 4.2 Rectangle 75

Thread Warp

### Alt/Text Metadata 4.2

Rectangle 75

### Shape 4.3 Rectangle 76

Common PC

### Alt/Text Metadata 4.3

Rectangle 76

### Shape 5 Rectangle 51

Thread
2

### Alt/Text Metadata 5

Rectangle 51

### Shape 6 Rectangle 52

Thread
3

### Alt/Text Metadata 6

Rectangle 52

### Shape 7 Rectangle 53

Thread
4

### Alt/Text Metadata 7

Rectangle 53

### Shape 8 Rectangle 55

Thread
1

### Alt/Text Metadata 8

Rectangle 55

### Alt/Text Metadata 9

Group 85 | Rectangle 6 | Rectangle 9 | Rectangle 12 | Rectangle 15 | Rectangle 30 | Rectangle 33 | Rectangle 40 | AutoShape 57 | AutoShape 58 | AutoShape 59 | AutoShape 60 | AutoShape 61 | AutoShape 62 | AutoShape 63 | AutoShape 64 | AutoShape 66

### Shape 9.1 Rectangle 6

B

### Alt/Text Metadata 9.1

Rectangle 6

### Shape 9.2 Rectangle 9

C

### Alt/Text Metadata 9.2

Rectangle 9

### Shape 9.3 Rectangle 12

D

### Alt/Text Metadata 9.3

Rectangle 12

### Shape 9.4 Rectangle 15

E

### Alt/Text Metadata 9.4

Rectangle 15

### Shape 9.5 Rectangle 30

F

### Alt/Text Metadata 9.5

Rectangle 30

### Shape 9.6 Rectangle 33

A

### Alt/Text Metadata 9.6

Rectangle 33

### Shape 9.7 Rectangle 40

G

### Alt/Text Metadata 9.7

Rectangle 40

### Alt/Text Metadata 9.8

AutoShape 57

### Alt/Text Metadata 9.9

AutoShape 58

### Alt/Text Metadata 9.10

AutoShape 59

### Alt/Text Metadata 9.11

AutoShape 60

### Alt/Text Metadata 9.12

AutoShape 61

### Alt/Text Metadata 9.13

AutoShape 62

### Alt/Text Metadata 9.14

AutoShape 63

### Alt/Text Metadata 9.15

AutoShape 64

### Alt/Text Metadata 9.16

AutoShape 66

### Alt/Text Metadata 10

Freeform 68

### Alt/Text Metadata 11

Freeform 71

### Alt/Text Metadata 12

Freeform 72

### Alt/Text Metadata 13

Freeform 84

### Alt/Text Metadata 14

Line 86

### Alt/Text Metadata 15

Line 87

### Shape 16 TextBox 35

Slide credit: Tor Aamodt

### Alt/Text Metadata 16

TextBox 35

## Slide 66

### Shape 1 Title 1

Control Flow Problem in GPUs/SIMT

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

A GPU uses a SIMT pipeline to save area on control logic
Groups scalar threads into warps
Branch divergence occurs when threads inside warps branch to different execution paths

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

66

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 94 | Rectangle 12 | Line 4 | Line 5 | Line 6 | Line 7 | Line 8 | Line 9 | Line 10 | Line 11

### Alt/Text Metadata 4.1

Rectangle 12

### Alt/Text Metadata 4.2

Line 4

### Alt/Text Metadata 4.3

Line 5

### Alt/Text Metadata 4.4

Line 6

### Alt/Text Metadata 4.5

Line 7

### Alt/Text Metadata 4.6

Line 8

### Alt/Text Metadata 4.7

Line 9

### Alt/Text Metadata 4.8

Line 10

### Alt/Text Metadata 4.9

Line 11

### Alt/Text Metadata 5

Group 95 | Rectangle 13 | Line 14 | Line 15 | Line 16 | Line 17 | Line 18 | Line 19 | Line 20 | Line 21

### Alt/Text Metadata 5.1

Rectangle 13

### Alt/Text Metadata 5.2

Line 14

### Alt/Text Metadata 5.3

Line 15

### Alt/Text Metadata 5.4

Line 16

### Alt/Text Metadata 5.5

Line 17

### Alt/Text Metadata 5.6

Line 18

### Alt/Text Metadata 5.7

Line 19

### Alt/Text Metadata 5.8

Line 20

### Alt/Text Metadata 5.9

Line 21

### Alt/Text Metadata 6

Group 96 | Rectangle 31 | Line 32 | Line 34 | Line 35 | Line 39

### Alt/Text Metadata 6.1

Rectangle 31

### Alt/Text Metadata 6.2

Line 32

### Alt/Text Metadata 6.3

Line 34

### Alt/Text Metadata 6.4

Line 35

### Alt/Text Metadata 6.5

Line 39

### Alt/Text Metadata 7

Group 97 | Rectangle 40 | Line 42 | Line 45 | Line 46 | Line 47

### Alt/Text Metadata 7.1

Rectangle 40

### Alt/Text Metadata 7.2

Line 42

### Alt/Text Metadata 7.3

Line 45

### Alt/Text Metadata 7.4

Line 46

### Alt/Text Metadata 7.5

Line 47

### Alt/Text Metadata 8

Group 98 | Rectangle 49 | Line 50 | Line 51 | Line 52 | Line 53 | Line 54 | Line 55 | Line 56 | Line 57

### Alt/Text Metadata 8.1

Rectangle 49

### Alt/Text Metadata 8.2

Line 50

### Alt/Text Metadata 8.3

Line 51

### Alt/Text Metadata 8.4

Line 52

### Alt/Text Metadata 8.5

Line 53

### Alt/Text Metadata 8.6

Line 54

### Alt/Text Metadata 8.7

Line 55

### Alt/Text Metadata 8.8

Line 56

### Alt/Text Metadata 8.9

Line 57

### Alt/Text Metadata 9

Rectangle 58

### Alt/Text Metadata 10

Group 79 | Rectangle 59 | Rectangle 64 | Rectangle 65 | Rectangle 66 | Rectangle 67 | AutoShape 68 | AutoShape 75 | AutoShape 76 | AutoShape 77 | AutoShape 78

### Alt/Text Metadata 10.1

Rectangle 59

### Shape 10.2 Rectangle 64

Branch

### Alt/Text Metadata 10.2

Rectangle 64

### Shape 10.3 Rectangle 65

Path A

### Alt/Text Metadata 10.3

Rectangle 65

### Shape 10.4 Rectangle 66

Path B

### Alt/Text Metadata 10.4

Rectangle 66

### Alt/Text Metadata 10.5

Rectangle 67

### Alt/Text Metadata 10.6

AutoShape 68

### Alt/Text Metadata 10.7

AutoShape 75

### Alt/Text Metadata 10.8

AutoShape 76

### Alt/Text Metadata 10.9

AutoShape 77

### Alt/Text Metadata 10.10

AutoShape 78

### Alt/Text Metadata 11

Rectangle 84

### Alt/Text Metadata 12

Rectangle 85

### Alt/Text Metadata 13

Rectangle 86

### Alt/Text Metadata 14

Rectangle 87

### Alt/Text Metadata 15

Rectangle 88

### Alt/Text Metadata 16

Group 102 | AutoShape 100 | AutoShape 101

### Alt/Text Metadata 16.1

AutoShape 100

### Alt/Text Metadata 16.2

AutoShape 101

### Shape 17 TextBox 67

Slide credit: Tor Aamodt

### Alt/Text Metadata 17

TextBox 67

## Slide 67

### Shape 1 Título 1

SIMT Utilization

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Intra-warp divergence

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 6

Compute(threadIdx.x);
if (threadIdx.x % 2 == 0){
  Do_this(threadIdx.x);
}
else{
  Do_that(threadIdx.x);
}

### Alt/Text Metadata 3

CuadroTexto 6

### Alt/Text Metadata 4

Imagen 4

### Relationships 4

- rId2: image:../media/image31.emf

### Shape 5 Marcador de número de diapositiva 3

67

### Alt/Text Metadata 5

Marcador de número de diapositiva 3

### Slide media/diagram relationships

- rId2: image:../media/image31.emf

## Slide 68

### Shape 1 Título 1

Increasing SIMT Utilization

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Divergence-free execution

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 6

Compute(threadIdx.x);
if (threadIdx.x < 32){
  Do_this(threadIdx.x * 2);
}
else{
  Do_that((threadIdx.x%32)*2+1);
}

### Alt/Text Metadata 3

CuadroTexto 6

### Alt/Text Metadata 4

Imagen 4

### Relationships 4

- rId2: image:../media/image32.emf

### Shape 5 Marcador de número de diapositiva 3

68

### Alt/Text Metadata 5

Marcador de número de diapositiva 3

### Slide media/diagram relationships

- rId2: image:../media/image32.emf

## Slide 69

### Shape 1 Título 1

Vector Reduction: Naïve Mapping (I)

### Alt/Text Metadata 1

Título 1

### Alt/Text Metadata 2

Rectangle 2

### Alt/Text Metadata 3

Rectangle 3

### Alt/Text Metadata 4

Rectangle 4

### Alt/Text Metadata 5

Rectangle 5

### Alt/Text Metadata 6

Rectangle 6

### Alt/Text Metadata 7

Rectangle 7

### Shape 8 Rectangle 9

0

### Alt/Text Metadata 8

Rectangle 9

### Shape 9 Rectangle 10

1

### Alt/Text Metadata 9

Rectangle 10

### Shape 10 Rectangle 11

2

### Alt/Text Metadata 10

Rectangle 11

### Shape 11 Rectangle 12

3

### Alt/Text Metadata 11

Rectangle 12

### Shape 12 Rectangle 13

4

### Alt/Text Metadata 12

Rectangle 13

### Shape 13 Rectangle 14

5

### Alt/Text Metadata 13

Rectangle 14

### Shape 14 Rectangle 15

7

### Alt/Text Metadata 14

Rectangle 15

### Shape 15 Rectangle 16

6

### Alt/Text Metadata 15

Rectangle 16

### Shape 16 Rectangle 17

10

### Alt/Text Metadata 16

Rectangle 17

### Shape 17 Rectangle 18

9

### Alt/Text Metadata 17

Rectangle 18

### Shape 18 Rectangle 19

8

### Alt/Text Metadata 18

Rectangle 19

### Shape 19 Rectangle 20

11

### Alt/Text Metadata 19

Rectangle 20

### Shape 20 Rectangle 21

0+1

### Alt/Text Metadata 20

Rectangle 21

### Alt/Text Metadata 21

Rectangle 22

### Shape 22 Rectangle 23

2+3

### Alt/Text Metadata 22

Rectangle 23

### Alt/Text Metadata 23

Rectangle 24

### Shape 24 Rectangle 25

4+5

### Alt/Text Metadata 24

Rectangle 25

### Alt/Text Metadata 25

Rectangle 26

### Alt/Text Metadata 26

Rectangle 27

### Shape 27 Rectangle 28

6+7

### Alt/Text Metadata 27

Rectangle 28

### Shape 28 Rectangle 29

10+11

### Alt/Text Metadata 28

Rectangle 29

### Alt/Text Metadata 29

Rectangle 30

### Shape 30 Rectangle 31

8+9

### Alt/Text Metadata 30

Rectangle 31

### Alt/Text Metadata 31

Rectangle 32

### Shape 32 Rectangle 33

0...3

### Alt/Text Metadata 32

Rectangle 33

### Alt/Text Metadata 33

Rectangle 34

### Alt/Text Metadata 34

Rectangle 35

### Alt/Text Metadata 35

Rectangle 36

### Shape 36 Rectangle 37

4..7

### Alt/Text Metadata 36

Rectangle 37

### Alt/Text Metadata 37

Rectangle 38

### Alt/Text Metadata 38

Rectangle 39

### Alt/Text Metadata 39

Rectangle 40

### Alt/Text Metadata 40

Rectangle 41

### Alt/Text Metadata 41

Rectangle 42

### Shape 42 Rectangle 43

8..11

### Alt/Text Metadata 42

Rectangle 43

### Alt/Text Metadata 43

Rectangle 44

### Shape 44 Rectangle 45

0..7

### Alt/Text Metadata 44

Rectangle 45

### Alt/Text Metadata 45

Rectangle 46

### Alt/Text Metadata 46

Rectangle 47

### Alt/Text Metadata 47

Rectangle 48

### Alt/Text Metadata 48

Rectangle 49

### Alt/Text Metadata 49

Rectangle 50

### Alt/Text Metadata 50

Rectangle 51

### Alt/Text Metadata 51

Rectangle 52

### Alt/Text Metadata 52

Rectangle 53

### Alt/Text Metadata 53

Rectangle 54

### Shape 54 Rectangle 55

8..15

### Alt/Text Metadata 54

Rectangle 55

### Alt/Text Metadata 55

Rectangle 56

### Alt/Text Metadata 56

Line 57

### Alt/Text Metadata 57

Line 58

### Alt/Text Metadata 58

Line 59

### Alt/Text Metadata 59

Line 60

### Alt/Text Metadata 60

Line 61

### Alt/Text Metadata 61

Line 62

### Alt/Text Metadata 62

Line 63

### Alt/Text Metadata 63

Line 64

### Alt/Text Metadata 64

Line 65

### Alt/Text Metadata 65

Line 66

### Alt/Text Metadata 66

Line 67

### Alt/Text Metadata 67

Line 68

### Alt/Text Metadata 68

Line 69

### Alt/Text Metadata 69

Line 70

### Alt/Text Metadata 70

Line 71

### Alt/Text Metadata 71

Line 72

### Alt/Text Metadata 72

Line 73

### Alt/Text Metadata 73

Line 74

### Alt/Text Metadata 74

Line 75

### Alt/Text Metadata 75

Line 76

### Alt/Text Metadata 76

Text Box 77

### Alt/Text Metadata 77

Text Box 78

### Alt/Text Metadata 78

Text Box 79

### Alt/Text Metadata 79

Line 81

### Alt/Text Metadata 80

Line 82

### Alt/Text Metadata 81

Line 83

### Alt/Text Metadata 82

Line 84

### Shape 83 Text Box 87

iterations

### Alt/Text Metadata 83

Text Box 87

### Alt/Text Metadata 84

Line 88

### Shape 85 Text Box 89

Thread 0

### Alt/Text Metadata 85

Text Box 89

### Shape 86 Text Box 90

Thread 8

### Alt/Text Metadata 86

Text Box 90

### Shape 87 Text Box 91

Thread 2

### Alt/Text Metadata 87

Text Box 91

### Shape 88 Text Box 92

Thread 4

### Alt/Text Metadata 88

Text Box 92

### Shape 89 Text Box 93

Thread 6

### Alt/Text Metadata 89

Text Box 93

### Shape 90 Text Box 94

Thread 10

### Alt/Text Metadata 90

Text Box 94

### Shape 91 Marcador de número de diapositiva 3

69

### Alt/Text Metadata 91

Marcador de número de diapositiva 3

### Shape 92 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 92

CuadroTexto 26

### Shape 93 TextBox 2

…

### Alt/Text Metadata 93

TextBox 2

## Slide 70

### Shape 1 Título 1

Vector Reduction: Naïve Mapping (II)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Program with low SIMD utilization

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 4

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = 1; stride < blockDim.x; stride *= 2) {
  __syncthreads();
  if (t % (2*stride) == 0)
    partialSum[t] += partialSum[t + stride];
}

### Alt/Text Metadata 3

CuadroTexto 4

### Shape 4 Marcador de número de diapositiva 3

70

### Alt/Text Metadata 4

Marcador de número de diapositiva 3

## Slide 71

### Shape 1 Título 1

Divergence-Free Mapping (I)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

All active threads belong to the same warp

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Rectangle 6

### Alt/Text Metadata 4

Rectangle 7

### Alt/Text Metadata 5

Rectangle 8

### Alt/Text Metadata 6

Rectangle 9

### Alt/Text Metadata 7

Rectangle 10

### Alt/Text Metadata 8

Rectangle 11

### Alt/Text Metadata 9

Rectangle 12

### Alt/Text Metadata 10

Rectangle 13

### Shape 11 Text Box 14

Thread 0

### Alt/Text Metadata 11

Text Box 14

### Shape 12 Rectangle 16

0

### Alt/Text Metadata 12

Rectangle 16

### Shape 13 Rectangle 17

1

### Alt/Text Metadata 13

Rectangle 17

### Shape 14 Rectangle 18

2

### Alt/Text Metadata 14

Rectangle 18

### Shape 15 Rectangle 19

3

### Alt/Text Metadata 15

Rectangle 19

### Shape 16 Rectangle 20

…

### Alt/Text Metadata 16

Rectangle 20

### Shape 17 Rectangle 21

13

### Alt/Text Metadata 17

Rectangle 21

### Shape 18 Rectangle 22

15

### Alt/Text Metadata 18

Rectangle 22

### Shape 19 Rectangle 23

14

### Alt/Text Metadata 19

Rectangle 23

### Shape 20 Rectangle 24

18

### Alt/Text Metadata 20

Rectangle 24

### Shape 21 Rectangle 25

17

### Alt/Text Metadata 21

Rectangle 25

### Shape 22 Rectangle 26

16

### Alt/Text Metadata 22

Rectangle 26

### Shape 23 Rectangle 27

19

### Alt/Text Metadata 23

Rectangle 27

### Shape 24 Rectangle 28

0+16

### Alt/Text Metadata 24

Rectangle 28

### Alt/Text Metadata 25

Rectangle 29

### Alt/Text Metadata 26

Rectangle 30

### Alt/Text Metadata 27

Rectangle 31

### Alt/Text Metadata 28

Rectangle 32

### Alt/Text Metadata 29

Rectangle 33

### Shape 30 Rectangle 34

15+31

### Alt/Text Metadata 30

Rectangle 34

### Alt/Text Metadata 31

Rectangle 35

### Alt/Text Metadata 32

Rectangle 36

### Alt/Text Metadata 33

Rectangle 37

### Alt/Text Metadata 34

Rectangle 38

### Alt/Text Metadata 35

Rectangle 39

### Alt/Text Metadata 36

Rectangle 40

### Alt/Text Metadata 37

Rectangle 41

### Alt/Text Metadata 38

Rectangle 42

### Alt/Text Metadata 39

Rectangle 43

### Alt/Text Metadata 40

Rectangle 44

### Alt/Text Metadata 41

Rectangle 45

### Alt/Text Metadata 42

Rectangle 46

### Alt/Text Metadata 43

Rectangle 47

### Alt/Text Metadata 44

Rectangle 48

### Alt/Text Metadata 45

Rectangle 49

### Alt/Text Metadata 46

Rectangle 50

### Alt/Text Metadata 47

Rectangle 51

### Alt/Text Metadata 48

Rectangle 52

### Alt/Text Metadata 49

Rectangle 53

### Alt/Text Metadata 50

Rectangle 54

### Alt/Text Metadata 51

Rectangle 55

### Alt/Text Metadata 52

Rectangle 56

### Alt/Text Metadata 53

Rectangle 57

### Alt/Text Metadata 54

Rectangle 58

### Alt/Text Metadata 55

Rectangle 59

### Alt/Text Metadata 56

Rectangle 60

### Alt/Text Metadata 57

Rectangle 61

### Alt/Text Metadata 58

Rectangle 62

### Alt/Text Metadata 59

Rectangle 63

### Alt/Text Metadata 60

Line 64

### Alt/Text Metadata 61

Line 65

### Alt/Text Metadata 62

Line 66

### Alt/Text Metadata 63

Line 67

### Alt/Text Metadata 64

Line 68

### Alt/Text Metadata 65

Line 69

### Alt/Text Metadata 66

Line 70

### Alt/Text Metadata 67

Line 71

### Alt/Text Metadata 68

Line 72

### Alt/Text Metadata 69

Line 73

### Alt/Text Metadata 70

Line 74

### Alt/Text Metadata 71

Line 75

### Alt/Text Metadata 72

Line 76

### Alt/Text Metadata 73

Line 77

### Alt/Text Metadata 74

Line 78

### Alt/Text Metadata 75

Line 79

### Alt/Text Metadata 76

Line 80

### Alt/Text Metadata 77

Text Box 81

### Alt/Text Metadata 78

Text Box 82

### Alt/Text Metadata 79

Text Box 83

### Alt/Text Metadata 80

Line 84

### Alt/Text Metadata 81

Line 85

### Alt/Text Metadata 82

Line 86

### Alt/Text Metadata 83

Line 87

### Alt/Text Metadata 84

Line 88

### Alt/Text Metadata 85

Line 89

### Alt/Text Metadata 86

Line 90

### Alt/Text Metadata 87

Line 91

### Shape 88 Text Box 92

Thread 1

### Alt/Text Metadata 88

Text Box 92

### Shape 89 Text Box 93

Thread 2

### Alt/Text Metadata 89

Text Box 93

### Shape 90 Text Box 94

Thread 14

### Alt/Text Metadata 90

Text Box 94

### Shape 91 Text Box 95

Thread 15

### Alt/Text Metadata 91

Text Box 95

### Shape 92 Text Box 87

iterations

### Alt/Text Metadata 92

Text Box 87

### Shape 94 Marcador de número de diapositiva 3

71

### Alt/Text Metadata 94

Marcador de número de diapositiva 3

### Shape 95 CuadroTexto 26

Slide credit: Hwu & Kirk

### Alt/Text Metadata 95

CuadroTexto 26

## Slide 72

### Shape 1 Título 1

Divergence-Free Mapping (II)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Program with high SIMD utilization

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 CuadroTexto 4

__shared__ float partialSum[]
unsigned int t = threadIdx.x;
for (int stride = blockDim.x; stride > 0;  stride >> 1){
  __syncthreads();
  if (t < stride)
    partialSum[t] += partialSum[t + stride];
}

### Alt/Text Metadata 3

CuadroTexto 4

### Shape 4 Marcador de número de diapositiva 3

72

### Alt/Text Metadata 4

Marcador de número de diapositiva 3

## Slide 73

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

73

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

## Slide 74

### Shape 1 Rectangle 4

Atomic Operations

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

## Slide 75

### Shape 1 Título 1

Atomic Operations (I)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

CUDA provides atomic instructions on shared memory and global memory
They perform read-modify-write operations atomically
Arithmetic functions
Add, sub, max, min, exch, inc, dec, CAS
int atomicAdd(int*, int);
Bitwise functions
And, or, xor
Datatypes: int, uint, ull, float (half, single, double)*

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Slide Number Placeholder 3

75

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 3

Pointer to shared memory or global memory

### Alt/Text Metadata 4

TextBox 3

### Shape 5 TextBox 5

Value to add

### Alt/Text Metadata 5

TextBox 5

### Shape 6 TextBox 6

Return value (old value)

### Alt/Text Metadata 6

TextBox 6

### Alt/Text Metadata 7

Straight Arrow Connector 8

### Alt/Text Metadata 8

Straight Arrow Connector 11

### Alt/Text Metadata 9

Straight Arrow Connector 13

### Shape 10 TextBox 16

* Datatypes for different atomic operations in https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#atomic-functions

### Alt/Text Metadata 10

TextBox 16

## Slide 76

### Shape 1 Marcador de contenido 2

Atomic operations serialize the execution if there are atomic conflicts

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 1

Atomic Operations (II)

### Alt/Text Metadata 2

Título 1

### Alt/Text Metadata 3

Imagen 6 | Atomics_th0.eps

### Relationships 3

- rId2: image:../media/image33.emf

### Alt/Text Metadata 4

Imagen 10 | Atomics_th1.eps

### Relationships 4

- rId3: image:../media/image34.emf

### Alt/Text Metadata 5

Agrupar 24 | CuadroTexto 13 | Cerrar llave 14 | CuadroTexto 15 | Cerrar llave 16

### Shape 5.1 CuadroTexto 13

tbase

### Alt/Text Metadata 5.1

CuadroTexto 13

### Alt/Text Metadata 5.2

Cerrar llave 14

### Shape 5.3 CuadroTexto 15

tconflict

### Alt/Text Metadata 5.3

CuadroTexto 15

### Alt/Text Metadata 5.4

Cerrar llave 16

### Alt/Text Metadata 6

Agrupar 50 | Imagen 18 | Atomics_posth01.eps | Agrupar 26 | Imagen 20 | Atomics_mempos.eps | CuadroTexto 21

### Relationships 6

- rId4: image:../media/image35.emf
- rId5: image:../media/image36.emf

### Alt/Text Metadata 6.1

Imagen 18 | Atomics_posth01.eps

### Relationships 6.1

- rId4: image:../media/image35.emf

### Alt/Text Metadata 6.2

Agrupar 26 | Imagen 20 | Atomics_mempos.eps | CuadroTexto 21

### Relationships 6.2

- rId5: image:../media/image36.emf

### Alt/Text Metadata 6.2.1

Imagen 20 | Atomics_mempos.eps

### Relationships 6.2.1

- rId5: image:../media/image36.emf

### Shape 6.2.2 CuadroTexto 21

Shared memory

### Alt/Text Metadata 6.2.2

CuadroTexto 21

### Alt/Text Metadata 7

Agrupar 49 | Agrupar 30 | Imagen 25 | Atomics_mempos02.eps | CuadroTexto 26 | Imagen 24 | Atomics_bankth02.eps

### Relationships 7

- rId6: image:../media/image37.emf
- rId7: image:../media/image38.emf

### Alt/Text Metadata 7.1

Agrupar 30 | Imagen 25 | Atomics_mempos02.eps | CuadroTexto 26

### Relationships 7.1

- rId6: image:../media/image37.emf

### Alt/Text Metadata 7.1.1

Imagen 25 | Atomics_mempos02.eps

### Relationships 7.1.1

- rId6: image:../media/image37.emf

### Alt/Text Metadata 7.1.2

CuadroTexto 26

### Alt/Text Metadata 7.2

Imagen 24 | Atomics_bankth02.eps

### Relationships 7.2

- rId7: image:../media/image38.emf

### Alt/Text Metadata 8

Agrupar 37 | Imagen 28 | Atomics_th0.eps | Imagen 29 | Atomics_th1.eps

### Relationships 8

- rId2: image:../media/image33.emf
- rId3: image:../media/image34.emf

### Alt/Text Metadata 8.1

Imagen 28 | Atomics_th0.eps

### Relationships 8.1

- rId2: image:../media/image33.emf

### Alt/Text Metadata 8.2

Imagen 29 | Atomics_th1.eps

### Relationships 8.2

- rId3: image:../media/image34.emf

### Alt/Text Metadata 9

Agrupar 38 | CuadroTexto 31 | Cerrar llave 32

### Alt/Text Metadata 9.1

CuadroTexto 31

### Alt/Text Metadata 9.2

Cerrar llave 32

### Alt/Text Metadata 10

Agrupar 31 | CuadroTexto 34 | CuadroTexto 35

### Shape 10.1 CuadroTexto 34

No atomic conflict = concurrent updates

### Alt/Text Metadata 10.1

CuadroTexto 34

### Shape 10.2 CuadroTexto 35

Atomic conflict = serialized updates

### Alt/Text Metadata 10.2

CuadroTexto 35

### Shape 11 Slide Number Placeholder 3

76

### Alt/Text Metadata 11

Slide Number Placeholder 3

### Slide media/diagram relationships

- rId3: image:../media/image34.emf
- rId7: image:../media/image38.emf
- rId2: image:../media/image33.emf
- rId6: image:../media/image37.emf
- rId5: image:../media/image36.emf
- rId4: image:../media/image35.emf

## Slide 77

### Shape 1 Título 1

Uses of Atomic Operations

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Use atomic operations to prevent data races when more than one thread need to update the same memory location
Computation
Atomics on an array that will be the output of the kernel
Example
Histogram, reduction
Synchronization
Atomics on memory locations that are used for synchronization or coordination
Example
Counters, locks, flags…

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Slide Number Placeholder 3

77

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 78

### Shape 1 Marcador de contenido 2

Histograms are widely used in image processing
Some computation before voting in the histogram may be needed
Parallel threads frequently incur atomic conflicts in image histogram computation

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Text Box 2

For (each pixel i in image I){
Pixel = I[i]			// Read pixel
Pixel’ = Computation(Pixel)	// Optional computation
Histogram[Pixel’]++		// Vote in histogram bin
}

### Alt/Text Metadata 2

Text Box 2

### Alt/Text Metadata 3

Imagen 10 | Apps_histogram.eps

### Relationships 3

- rId2: image:../media/image39.emf

### Shape 4 Título 1

Image Histogram

### Alt/Text Metadata 4

Título 1

### Shape 5 Slide Number Placeholder 3

78

### Alt/Text Metadata 5

Slide Number Placeholder 3

### Slide media/diagram relationships

- rId2: image:../media/image39.emf

## Slide 79

### Shape 1 Título 1

Agenda for Today

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

SIMT (Hardware) & Warp (Software)
Optimization of Memory System
Multi-threading
Memory Coalescing
Shared Memory
SIMT Efficiency
Divergency
Atomic
CPU-GPU Transfer

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

79

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Rectangle 4

## Slide 80

### Shape 1 Rectangle 4

Asynchronous Data Transfers between CPU and GPU

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

## Slide 81

### Shape 1 Título 1

CUDA Streams

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

CUDA streams (command queues in OpenCL)
Sequence of operations that are performed in order
1. Data transfer CPU-GPU
2. Kernel execution
D input data instances, B blocks
#Streams: (D / #Streams) data instances, (B / #Streams) blocks
3. Data transfer GPU-CPU

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 12 | Stream_best_streams.eps

### Relationships 3

- rId3: image:../media/image40.emf

### Shape 4 Slide Number Placeholder 3

81

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Speaker notes

Computation is divided such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.

### Slide media/diagram relationships

- rId3: image:../media/image40.emf

## Slide 82

### Shape 1 Título 1

Asynchronous Transfers between CPU & GPU

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Computation divided into #Streams
D input data instances, B blocks
#Streams
D/#Streams data instances
B/#Streams blocks
Estimates

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 12 | Stream_best_streams.eps

### Relationships 3

- rId3: image:../media/image40.emf

### Shape 4 CuadroTexto 4

tE >= tT (dominant kernel)

### Alt/Text Metadata 4

CuadroTexto 4

### Shape 5 CuadroTexto 7

tT > tE (dominant transfers)

### Alt/Text Metadata 5

CuadroTexto 7

### Shape 6 Marcador de número de diapositiva 3

82

### Alt/Text Metadata 6

Marcador de número de diapositiva 3

### Shape 7 TextBox 8

Default stream

### Alt/Text Metadata 7

TextBox 8

### Shape 8 TextBox 10

Several streams

### Alt/Text Metadata 8

TextBox 10

### Speaker notes

Computation is divided such that if D data instances need B blocks to be processed… The kernel is therefore #Streams times launched.
CUDA literature gives only two rough estimates, but does not give any hint of the optimal number of streams in which a given data set should be preferably divided.

### Slide media/diagram relationships

- rId3: image:../media/image40.emf
- rId5: image:../media/image93.png
- rId4: image:../media/image80.png

## Slide 83

### Shape 1 Marcador de número de diapositiva 8

83

### Alt/Text Metadata 1

Marcador de número de diapositiva 8

### Shape 2 Title 4

Overlap of Data Transfers and Kernel Execution

### Alt/Text Metadata 2

Title 4

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 2

// Create streams
int number_of_streams = 32;
cudaStream_t stream[number_of_streams]; // Stream declaration
for(int i = 0; i < number_of_streams; ++i)
    cudaStreamCreate(&stream[i]); // Stream creation
// CPU-GPU data transfers
for (int i = 0; i < number_of_streams; ++i)
    cudaMemcpyAsync(inputDevPtr + i * size, hostPtr + i * size, size,
                    cudaMemcpyHostToDevice, stream[i]);
// Kernel launches
for (int i = 0; i < number_of_streams; ++i)
    MyKernel<<<num_blocks / number_of_streams, num_threads, 0, stream[i]>>>
                              (outputDevPtr + i * size, inputDevPtr + i * size, size);
// GPU-CPU data transfers
for (int i = 0; i < number_of_streams; ++i)
    cudaMemcpyAsync(hostPtr + i * size, outputDevPtr + i * size, size,
                    cudaMemcpyDeviceToHost, stream[i]);
cudaDeviceSynchronize(); // Explicit synchronization
// Destroy streams
for (int i = 0; i < number_of_streams; ++i)
    cudaStreamDestroy(stream[i]); // Stream destruction

### Alt/Text Metadata 4

TextBox 2

### Shape 5 TextBox 9

Code for devices that do not support concurrent data transfers

### Alt/Text Metadata 5

TextBox 9

### Shape 6 TextBox 272

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

### Alt/Text Metadata 6

TextBox 272

### Shape 7 TextBox 10

Check CUDA programming guide
https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#streams

### Alt/Text Metadata 7

TextBox 10

## Slide 84

### Shape 1 Marcador de contenido 2

Applications with independent computation on different data instances can benefit from asynchronous transfers
For instance, video processing

### Alt/Text Metadata 1

Marcador de contenido 2

### Alt/Text Metadata 2

Imagen 14 | Stream_video_streams.eps

### Relationships 2

- rId3: image:../media/image41.emf

### Shape 3 Título 1

Use Case: Video Processing

### Alt/Text Metadata 3

Título 1

### Shape 4 Marcador de número de diapositiva 3

84

### Alt/Text Metadata 4

Marcador de número de diapositiva 3

### Shape 5 TextBox 6

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

### Alt/Text Metadata 5

TextBox 6

### Speaker notes

A number b of blocks per frame executes.
Data transfers are overlapped with computation. Thus, some time can be saved.

### Slide media/diagram relationships

- rId3: image:../media/image41.emf

## Slide 85

### Shape 1 Content Placeholder 2

Asynchronous memory copy with LDGSTS instruction vs. TMA

### Alt/Text Metadata 1

Content Placeholder 2

### Shape 2 Title 1

NVIDIA H100 Tensor Memory Accelerator

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

85

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 10

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

### Alt/Text Metadata 4

TextBox 10

### Alt/Text Metadata 5

Picture 3

### Relationships 5

- rId4: image:../media/image42.jpg

### Alt/Text Metadata 6

Picture 7

### Relationships 6

- rId5: image:../media/image43.jpg

### Shape 7 Content Placeholder 2

TMA unit reduces addressing overhead
A single thread per warp issues the TMA operation
Support for different tensor layouts (1D-5D)

### Speaker notes

New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can transfer large blocks of data efficiently between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.
New asynchronous execution features include a new Tensor Memory Accelerator (TMA) unit that can efficiently transfer large blocks of data between global memory and shared memory. TMA also supports asynchronous copies between thread blocks in a cluster. There is also a new asynchronous transaction barrier for doing atomic data movement and synchronization.

### Slide media/diagram relationships

- rId5: image:../media/image43.jpg
- rId4: image:../media/image42.jpg

## Slide 86

### Shape 1 Rectangle 2

State-of-the-art CPU GPU and FPGA

### Alt/Text Metadata 1

Rectangle 2

### Table 2 Table 5

-  | Cores (Threads) | TFLOPS | Memory Size (Bandwidth) | PCIe | Network
- CPU (AMD Threadripper 3995WX) | 64 (128) | 2.8 (FP32), / 1.4 (FP64) | 512GB / (80GB/s) | 32.0GB/s / (PCIe 4.0 X16) | No
- GPU (Nvidia A100) | 8192 (128K) | 19.5 (FP32), / 9.7 (FP64), / 156 (FP32, Tensor), / 312 (FP16, Tensor) | 40/80GB / (1935GB/s) | 32.0GB/s / (PCIe 4.0 X16) | No
- FPGA (U280) | 9,024 / (25x18 MULs) | 1.8 (FP32) | 40GB / (460GB/s) | 16.0GB/s / (PCIe 4.0 X8) | Yes

### Alt/Text Metadata 2

Table 5

### XML fallback texts

- Cores (Threads)
- TFLOPS
- Memory Size (Bandwidth)
- PCIe
- Network
- CPU (
- AMD
- Threadripper
- 3995WX
- )
- 64 (128)
- 2.8 (FP32),
- 1.4 (FP64)
- 512GB
- (
- 80
- GB/s)
- 3
- .0GB/s
- (PCIe 4.0
- X
- 16
- No
- GPU (Nvidia A100)
- 8192
- (128K)
- 19.5 (FP32),
- 9.7 (FP64),
- 156 (FP32, Tensor),
- 312 (FP16, Tensor)
- 40/80GB
- (1935GB/s)
- FPGA (U280)
- 9,024
- (25x18
- MULs
- 1.8 (FP32)
- 40GB
- 460
- 1
- 6
- 8
- Yes

### Speaker notes

KB MB GB TB
K M B T E P
1B=10亿

## Slide 87

### Shape 1 Title 1

Limitation of GPU

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

87

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

object 4

### Relationships 3

- rId2: image:../media/image44.png

### Alt/Text Metadata 4

object 5

### Relationships 4

- rId3: image:../media/image4.png

### Alt/Text Metadata 5

object 6

### Shape 6 object 13

CPU

### Alt/Text Metadata 6

object 13

### Shape 7 object 13

GPU

### Shape 8 object 13

PCIe

### Shape 9 object 13

32.0GB/s

### Shape 10 object 13

1935GB/s

### Slide media/diagram relationships

- rId3: image:../media/image4.png
- rId2: image:../media/image44.png

## Slide 88

### Shape 1 Slide Number Placeholder 3

88

### Alt/Text Metadata 1

Slide Number Placeholder 3

### Shape 2 Rectangle 6

Serial Code of Prefix sum:

### Alt/Text Metadata 2

Rectangle 6

### Alt/Text Metadata 3

Picture 2 | Parallel Prefix Sum Scan GPU Graphics Gary J

### Relationships 3

- rId3: image:../media/image45.jpeg

### Shape 4 Rectangle 9

GPU Code of Prefix sum:
    Multi-pass (ISSUE)

### Alt/Text Metadata 4

Rectangle 9

### Shape 5 Title 1

Limitation of GPU

### Alt/Text Metadata 5

Title 1

### Shape 6 Rectangle 7

// Fills prefix sum array
void fillPrefixSum(int arr[], int n, int prefixSum[])
{ prefixSum[0] = arr[0];
  // Adding present element
  for (int i = 1; i < n; i++)
   prefixSum[i] = prefixSum[i-1] + arr[i]; }

### Alt/Text Metadata 6

Rectangle 7

### Slide media/diagram relationships

- rId3: image:../media/image45.jpeg

## Slide 89

### Shape 1 Título 1

Nvidia’s Success: Transparent Scalability

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Hardware is free to schedule thread blocks

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Group 5 | Text Box 6 | Text Box 7 | Text Box 8

### Shape 3.1 Text Box 6

Device

### Alt/Text Metadata 3.1

Text Box 6

### Alt/Text Metadata 3.2

Text Box 7

### Alt/Text Metadata 3.3

Text Box 8

### Alt/Text Metadata 4

Group 9 | Line 10 | Group 11 | Text Box 12 | Group 13 | Text Box 14 | Text Box 15 | Group 16 | Text Box 17 | Text Box 18 | Group 19 | Text Box 20 | Group 21 | Text Box 22 | Text Box 23 | Group 24 | Text Box 25 | Text Box 26 | Group 27 | Text Box 28 | Group 29 | Text Box 30 | Text Box 31 | Group 32 | Text Box 33 | Text Box 34 | Group 35 | Text Box 36 | Group 37 | Text Box 38 | Text Box 39 | Group 40 | Text Box 41 | Text Box 42

### Alt/Text Metadata 4.1

Line 10

### Alt/Text Metadata 4.2

Group 11 | Text Box 12 | Group 13 | Text Box 14 | Text Box 15 | Group 16 | Text Box 17 | Text Box 18

### Alt/Text Metadata 4.2.1

Text Box 12

### Alt/Text Metadata 4.2.2

Group 13 | Text Box 14 | Text Box 15

### Alt/Text Metadata 4.2.2.1

Text Box 14

### Shape 4.2.2.2 Text Box 15

Block 0

### Alt/Text Metadata 4.2.2.2

Text Box 15

### Alt/Text Metadata 4.2.3

Group 16 | Text Box 17 | Text Box 18

### Alt/Text Metadata 4.2.3.1

Text Box 17

### Shape 4.2.3.2 Text Box 18

Block 1

### Alt/Text Metadata 4.2.3.2

Text Box 18

### Alt/Text Metadata 4.3

Group 19 | Text Box 20 | Group 21 | Text Box 22 | Text Box 23 | Group 24 | Text Box 25 | Text Box 26

### Alt/Text Metadata 4.3.1

Text Box 20

### Alt/Text Metadata 4.3.2

Group 21 | Text Box 22 | Text Box 23

### Alt/Text Metadata 4.3.2.1

Text Box 22

### Shape 4.3.2.2 Text Box 23

Block 2

### Alt/Text Metadata 4.3.2.2

Text Box 23

### Alt/Text Metadata 4.3.3

Group 24 | Text Box 25 | Text Box 26

### Alt/Text Metadata 4.3.3.1

Text Box 25

### Shape 4.3.3.2 Text Box 26

Block 3

### Alt/Text Metadata 4.3.3.2

Text Box 26

### Alt/Text Metadata 4.4

Group 27 | Text Box 28 | Group 29 | Text Box 30 | Text Box 31 | Group 32 | Text Box 33 | Text Box 34

### Alt/Text Metadata 4.4.1

Text Box 28

### Alt/Text Metadata 4.4.2

Group 29 | Text Box 30 | Text Box 31

### Alt/Text Metadata 4.4.2.1

Text Box 30

### Shape 4.4.2.2 Text Box 31

Block 4

### Alt/Text Metadata 4.4.2.2

Text Box 31

### Alt/Text Metadata 4.4.3

Group 32 | Text Box 33 | Text Box 34

### Alt/Text Metadata 4.4.3.1

Text Box 33

### Shape 4.4.3.2 Text Box 34

Block 5

### Alt/Text Metadata 4.4.3.2

Text Box 34

### Alt/Text Metadata 4.5

Group 35 | Text Box 36 | Group 37 | Text Box 38 | Text Box 39 | Group 40 | Text Box 41 | Text Box 42

### Alt/Text Metadata 4.5.1

Text Box 36

### Alt/Text Metadata 4.5.2

Group 37 | Text Box 38 | Text Box 39

### Alt/Text Metadata 4.5.2.1

Text Box 38

### Shape 4.5.2.2 Text Box 39

Block 6

### Alt/Text Metadata 4.5.2.2

Text Box 39

### Alt/Text Metadata 4.5.3

Group 40 | Text Box 41 | Text Box 42

### Alt/Text Metadata 4.5.3.1

Text Box 41

### Shape 4.5.3.2 Text Box 42

Block 7

### Alt/Text Metadata 4.5.3.2

Text Box 42

### Alt/Text Metadata 5

Group 43 | Text Box 44 | Group 45 | Group 46 | Text Box 47 | Text Box 48 | Group 49 | Text Box 50 | Text Box 51 | Group 52 | Text Box 53 | Text Box 54 | Group 55 | Text Box 56 | Text Box 57

### Shape 5.1 Text Box 44

Kernel grid

### Alt/Text Metadata 5.1

Text Box 44

### Alt/Text Metadata 5.2

Group 45 | Group 46 | Text Box 47 | Text Box 48 | Group 49 | Text Box 50 | Text Box 51 | Group 52 | Text Box 53 | Text Box 54 | Group 55 | Text Box 56 | Text Box 57

### Alt/Text Metadata 5.2.1

Group 46 | Text Box 47 | Text Box 48

### Alt/Text Metadata 5.2.1.1

Text Box 47

### Alt/Text Metadata 5.2.1.2

Text Box 48

### Alt/Text Metadata 5.2.2

Group 49 | Text Box 50 | Text Box 51

### Alt/Text Metadata 5.2.2.1

Text Box 50

### Alt/Text Metadata 5.2.2.2

Text Box 51

### Alt/Text Metadata 5.2.3

Group 52 | Text Box 53 | Text Box 54

### Alt/Text Metadata 5.2.3.1

Text Box 53

### Alt/Text Metadata 5.2.3.2

Text Box 54

### Alt/Text Metadata 5.2.4

Group 55 | Text Box 56 | Text Box 57

### Alt/Text Metadata 5.2.4.1

Text Box 56

### Alt/Text Metadata 5.2.4.2

Text Box 57

### Alt/Text Metadata 6

Group 59 | Text Box 60 | Text Box 61 | Text Box 62 | Text Box 63 | Text Box 64

### Alt/Text Metadata 6.1

Text Box 60

### Alt/Text Metadata 6.2

Text Box 61

### Alt/Text Metadata 6.3

Text Box 62

### Alt/Text Metadata 6.4

Text Box 63

### Alt/Text Metadata 6.5

Text Box 64

### Alt/Text Metadata 7

Group 65 | Text Box 66 | Group 67 | Text Box 68 | Text Box 69 | Group 70 | Text Box 71 | Text Box 72 | Group 73 | Text Box 74 | Text Box 75 | Group 76 | Text Box 77 | Text Box 78

### Alt/Text Metadata 7.1

Text Box 66

### Alt/Text Metadata 7.2

Group 67 | Text Box 68 | Text Box 69

### Alt/Text Metadata 7.2.1

Text Box 68

### Alt/Text Metadata 7.2.2

Text Box 69

### Alt/Text Metadata 7.3

Group 70 | Text Box 71 | Text Box 72

### Alt/Text Metadata 7.3.1

Text Box 71

### Alt/Text Metadata 7.3.2

Text Box 72

### Alt/Text Metadata 7.4

Group 73 | Text Box 74 | Text Box 75

### Alt/Text Metadata 7.4.1

Text Box 74

### Alt/Text Metadata 7.4.2

Text Box 75

### Alt/Text Metadata 7.5

Group 76 | Text Box 77 | Text Box 78

### Alt/Text Metadata 7.5.1

Text Box 77

### Alt/Text Metadata 7.5.2

Text Box 78

### Alt/Text Metadata 8

Group 79 | Text Box 80 | Group 81 | Text Box 82 | Text Box 83 | Group 84 | Text Box 85 | Text Box 86 | Group 87 | Text Box 88 | Text Box 89 | Group 90 | Text Box 91 | Text Box 92

### Alt/Text Metadata 8.1

Text Box 80

### Alt/Text Metadata 8.2

Group 81 | Text Box 82 | Text Box 83

### Alt/Text Metadata 8.2.1

Text Box 82

### Alt/Text Metadata 8.2.2

Text Box 83

### Alt/Text Metadata 8.3

Group 84 | Text Box 85 | Text Box 86

### Alt/Text Metadata 8.3.1

Text Box 85

### Alt/Text Metadata 8.3.2

Text Box 86

### Alt/Text Metadata 8.4

Group 87 | Text Box 88 | Text Box 89

### Alt/Text Metadata 8.4.1

Text Box 88

### Alt/Text Metadata 8.4.2

Text Box 89

### Alt/Text Metadata 8.5

Group 90 | Text Box 91 | Text Box 92

### Alt/Text Metadata 8.5.1

Text Box 91

### Alt/Text Metadata 8.5.2

Text Box 92

### Alt/Text Metadata 9

Line 93

### Alt/Text Metadata 10

Line 94

### Alt/Text Metadata 11

Line 95

### Shape 12 Text Box 96

Each block can execute in any order relative to other blocks.

### Alt/Text Metadata 12

Text Box 96

### Shape 13 Text Box 97

time

### Alt/Text Metadata 13

Text Box 97

### Shape 14 Marcador de número de diapositiva 3

89

### Alt/Text Metadata 14

Marcador de número de diapositiva 3

### Shape 15 CuadroTexto 97

Slide credit: Hwu & Kirk

### Alt/Text Metadata 15

CuadroTexto 97

### Shape 17 Rectangle 4

Gen 1

### Alt/Text Metadata 17

Rectangle 4

### Shape 18 Rectangle 99

Gen 2

### Alt/Text Metadata 18

Rectangle 99

### Shape 19 Text Box 96

The CUDA code stays the same and enjoys performance improvement while GPU hardware evolves.

### Speaker notes

Thread block is the key innovation to scale-up GPU architecture. The software code stays the same and enjoys performance speedup while GPU hardware evolves.

## Slide 90

### Shape 1 Title 1

Key Messages:

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Programming model is the key success of Nvidia, rather than the GPU itself.
GPU has an order of magnitude higher memory bandwidth and compute power than CPU.
Offloading a task to GPU pays off only when the task has enough compute intensity.
AI task needs compute-intensive accelerators, e.g., GPU and AI processor.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

90

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 91

### Shape 1 Title 1

Prog. Model 3: Multithreaded

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

91

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Text Box 3

for (i=0; i < N; i++)
    C[i] = A[i] + B[i];

### Alt/Text Metadata 3

Text Box 3

### Alt/Text Metadata 4

Group 5 | AutoShape 33 | AutoShape 34 | AutoShape 35 | AutoShape 36 | Line 37 | Line 38 | Line 39 | AutoShape 47

### Shape 4.1 AutoShape 33

load

### Alt/Text Metadata 4.1

AutoShape 33

### Alt/Text Metadata 4.2

AutoShape 34

### Shape 4.3 AutoShape 35

add

### Alt/Text Metadata 4.3

AutoShape 35

### Shape 4.4 AutoShape 36

store

### Alt/Text Metadata 4.4

AutoShape 36

### Alt/Text Metadata 4.5

Line 37

### Alt/Text Metadata 4.6

Line 38

### Alt/Text Metadata 4.7

Line 39

### Alt/Text Metadata 4.8

AutoShape 47

### Alt/Text Metadata 5

Group 4 | AutoShape 40 | AutoShape 41 | AutoShape 42 | AutoShape 43 | Line 44 | Line 45 | Line 46 | AutoShape 48

### Alt/Text Metadata 5.1

AutoShape 40

### Alt/Text Metadata 5.2

AutoShape 41

### Alt/Text Metadata 5.3

AutoShape 42

### Alt/Text Metadata 5.4

AutoShape 43

### Alt/Text Metadata 5.5

Line 44

### Alt/Text Metadata 5.6

Line 45

### Alt/Text Metadata 5.7

Line 46

### Alt/Text Metadata 5.8

AutoShape 48

### Shape 6 Text Box 49

Iter. 1

### Alt/Text Metadata 6

Text Box 49

### Shape 7 Text Box 50

Iter. 2

### Alt/Text Metadata 7

Text Box 50

### Alt/Text Metadata 8

Line 55

### Shape 9 Text Box 26

Realization: Each iteration is independent
Idea: Programmer or compiler generates a thread to execute each iteration. Each thread does the same thing (but on different data)

### Alt/Text Metadata 9

Text Box 26

### Shape 10 TextBox 2

This programming model (software) is called:
SPMD: Single Program Multiple Data

### Alt/Text Metadata 10

TextBox 2

### Shape 11 TextBox 52

Executed on a SIMT machine (hardware)
Single Instruction Multiple Thread

### Alt/Text Metadata 11

TextBox 52

## Slide 92

### Shape 1 Title 1

A GPU is a SIMD (SIMT) Machine

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Except it is not programmed using SIMD instructions
It is programmed using threads (SPMD programming model)
Each thread executes the same code but operates a different piece of data
Each thread has its own context (i.e., can be treated/restarted/executed independently)
A set of threads executing the same instruction are dynamically grouped into a warp (wavefront) by the hardware
A warp is essentially a SIMD operation formed by hardware!

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

92

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 93

### Shape 1 Title 1

SIMD vs. SIMT Execution Model

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
[VLD, VLD, VADD, VST], VLEN
SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
[LD, LD, ADD, ST], NumThreads
Two Major SIMT Advantages:
Can treat each thread separately  i.e., can execute each thread independently on any type of scalar pipeline
Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

93

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Rounded Rectangle 130

## Slide 94

### Shape 1 Título 1

Brief Review of GPU Architecture (I)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Streaming Processor Array
Tesla architecture (G80/GT200)

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 8 | CUDA_SM1x.eps

### Relationships 3

- rId2: image:../media/image46.emf

### Shape 4 Marcador de número de diapositiva 3

94

### Alt/Text Metadata 4

Marcador de número de diapositiva 3

### Slide media/diagram relationships

- rId2: image:../media/image46.emf

## Slide 95

### Shape 1 Título 1

Brief Review of GPU Architecture (II)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Streaming Multiprocessors (SM)
Streaming Processors (SP)
Blocks are divided into warps
SIMD unit (32 threads)

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 8 | CUDA_SM2x.eps

### Relationships 3

- rId2: image:../media/image47.emf

### Alt/Text Metadata 4

Rectangle 73

### Shape 5 Rectangle 74

…

### Alt/Text Metadata 5

Rectangle 74

### Alt/Text Metadata 6

Group 75 | Text Box 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80 | Freeform 81 | Freeform 82 | Freeform 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87

### Shape 6.1 Text Box 76

t0 t1 t2 … t31

### Alt/Text Metadata 6.1

Text Box 76

### Alt/Text Metadata 6.2

Freeform 77

### Alt/Text Metadata 6.3

Freeform 78

### Alt/Text Metadata 6.4

Freeform 79

### Alt/Text Metadata 6.5

Freeform 80

### Alt/Text Metadata 6.6

Freeform 81

### Alt/Text Metadata 6.7

Freeform 82

### Alt/Text Metadata 6.8

Freeform 83

### Alt/Text Metadata 6.9

Freeform 84

### Alt/Text Metadata 6.10

Freeform 85

### Alt/Text Metadata 6.11

Freeform 86

### Alt/Text Metadata 6.12

Freeform 87

### Alt/Text Metadata 7

Text Box 88

### Alt/Text Metadata 8

Rectangle 89

### Alt/Text Metadata 9

Rectangle 90

### Alt/Text Metadata 10

Group 91 | Text Box 92 | Freeform 93 | Freeform 94 | Freeform 95 | Freeform 96 | Freeform 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103

### Alt/Text Metadata 10.1

Text Box 92

### Alt/Text Metadata 10.2

Freeform 93

### Alt/Text Metadata 10.3

Freeform 94

### Alt/Text Metadata 10.4

Freeform 95

### Alt/Text Metadata 10.5

Freeform 96

### Alt/Text Metadata 10.6

Freeform 97

### Alt/Text Metadata 10.7

Freeform 98

### Alt/Text Metadata 10.8

Freeform 99

### Alt/Text Metadata 10.9

Freeform 100

### Alt/Text Metadata 10.10

Freeform 101

### Alt/Text Metadata 10.11

Freeform 102

### Alt/Text Metadata 10.12

Freeform 103

### Alt/Text Metadata 11

Text Box 104

### Shape 12 Text Box 105

Block 0’s warps

### Alt/Text Metadata 12

Text Box 105

### Shape 13 Text Box 106

Block 1’s warps

### Alt/Text Metadata 13

Text Box 106

### Alt/Text Metadata 14

Rectangle 135

### Alt/Text Metadata 15

Rectangle 136

### Alt/Text Metadata 16

Group 137 | Text Box 138 | Freeform 139 | Freeform 140 | Freeform 141 | Freeform 142 | Freeform 143 | Freeform 144 | Freeform 145 | Freeform 146 | Freeform 147 | Freeform 148 | Freeform 149

### Alt/Text Metadata 16.1

Text Box 138

### Alt/Text Metadata 16.2

Freeform 139

### Alt/Text Metadata 16.3

Freeform 140

### Alt/Text Metadata 16.4

Freeform 141

### Alt/Text Metadata 16.5

Freeform 142

### Alt/Text Metadata 16.6

Freeform 143

### Alt/Text Metadata 16.7

Freeform 144

### Alt/Text Metadata 16.8

Freeform 145

### Alt/Text Metadata 16.9

Freeform 146

### Alt/Text Metadata 16.10

Freeform 147

### Alt/Text Metadata 16.11

Freeform 148

### Alt/Text Metadata 16.12

Freeform 149

### Alt/Text Metadata 17

Text Box 150

### Shape 18 Text Box 151

Block 2’s warps

### Alt/Text Metadata 18

Text Box 151

### Shape 19 Marcador de número de diapositiva 3

95

### Alt/Text Metadata 19

Marcador de número de diapositiva 3

### Shape 20 TextBox 4

NVIDIA Fermi architecture

### Alt/Text Metadata 20

TextBox 4

### Slide media/diagram relationships

- rId2: image:../media/image47.emf

## Slide 96

### Shape 1 Título 1

Brief Review of GPU Architecture (III)

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Streaming Multiprocessors (SM) or Compute Units (CU)
SIMD pipelines
Streaming Processors (SP) or CUDA ”cores”
Vector lanes
Number of SMs x SPs across generations
Tesla (2007): 30 x 8
Fermi (2010): 16 x 32
Kepler (2012): 15 x 192
Maxwell (2014): 24 x 128
Pascal (2016): 56 x 64
Volta (2017): 80 x 64

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

96

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

## Slide 97

### Shape 1 Rectangle 4

Graphics Processing UnitsSIMD not Exposed to Programmer (SIMT)

### Alt/Text Metadata 1

Rectangle 4

### Alt/Text Metadata 2

Rectangle 5

## Slide 98

### Shape 1 Title 1

SIMD vs. SIMT Execution Model

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

SIMD: A single sequential instruction stream of SIMD instructions  each instruction specifies multiple data inputs
[VLD, VLD, VADD, VST], VLEN
SIMT: Multiple instruction streams of scalar instructions  threads grouped dynamically into warps
[LD, LD, ADD, ST], NumThreads
Two Major SIMT Advantages:
Can treat each thread separately  i.e., can execute each thread independently (on any type of scalar pipeline)  MIMD processing
Can group threads into warps flexibly  i.e., can group threads that are supposed to truly execute the same instruction  dynamically obtain and maximize benefits of SIMD processing

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

98

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Rounded Rectangle 130

## Slide 99

### Shape 1 Title 1

High-Level View of a GPU

### Alt/Text Metadata 1

Title 1

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

99

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId2: image:../media/image48.png

### Shape 5 TextBox 6

Lindholm et al., "NVIDIA Tesla: A Unified Graphics and Computing Architecture," IEEE Micro 2008.

### Alt/Text Metadata 5

TextBox 6

### Slide media/diagram relationships

- rId2: image:../media/image48.png

## Slide 100

### Shape 1 Title 1

Latency Hiding via Warp-Level FGMT

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Warp: A set of threads that execute the same instruction (on different data elements)
Fine-grained multithreading
No interlocking: One instruction per thread in pipeline at a time.
Interleave warp execution to hide latencies
Register values of all threads stay in register file
FGMT enables long latency tolerance
Millions of pixels

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

100

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 4 | AutoShape 5 | Rectangle 6 | Rectangle 7 | Rectangle 8 | Rectangle 9 | Rectangle 10 | Rectangle 11 | Rectangle 12 | Rectangle 13 | Rectangle 14 | Rectangle 15 | Rectangle 16 | Rectangle 17 | Rectangle 18 | Rectangle 19 | Rectangle 20 | Rectangle 21 | Rectangle 22 | Line 23 | Freeform 24 | Rectangle 25 | Rectangle 26 | Rectangle 27 | Rectangle 28 | Rectangle 29 | Rectangle 30 | Rectangle 31 | Rectangle 32 | Rectangle 33 | Rectangle 34 | Rectangle 35 | Rectangle 36 | Rectangle 37 | Rectangle 38 | Rectangle 39 | Line 40 | Freeform 41 | Line 42 | Freeform 43 | Line 44 | Freeform 45 | Line 46 | Freeform 47 | Line 48 | Freeform 49 | Line 50 | Freeform 51 | Rectangle 52 | Rectangle 53 | Rectangle 54 | Line 55 | Freeform 56 | Line 57 | Freeform 58 | Line 59 | Freeform 60 | Freeform 61 | Line 62 | Freeform 63 | Rectangle 64 | Rectangle 65 | Rectangle 66 | Rectangle 67 | Rectangle 68 | Rectangle 69 | Rectangle 70 | Rectangle 71 | Rectangle 72 | Freeform 73 | Freeform 74 | Freeform 75 | Freeform 76 | Line 77 | Freeform 78 | Freeform 79 | Freeform 80 | Freeform 81 | Rectangle 82 | Rectangle 83 | Rectangle 84 | Freeform 85 | Freeform 86 | Freeform 87 | Freeform 88 | Rectangle 89 | Rectangle 90 | Rectangle 91 | Rectangle 92 | Rectangle 93 | Rectangle 94 | Rectangle 95 | Rectangle 96 | Rectangle 97 | Rectangle 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103 | Freeform 104 | Line 105 | Freeform 106 | Freeform 107 | Freeform 108 | Rectangle 109 | Rectangle 110 | Rectangle 111 | Rectangle 112 | Rectangle 113 | Freeform 114 | Freeform 115 | Freeform 116 | Freeform 117 | Freeform 118 | Freeform 119 | Freeform 120 | Freeform 121 | Freeform 122 | Freeform 123 | Freeform 124 | Freeform 125 | Rectangle 126 | Rectangle 127 | Rectangle 128 | Rectangle 129 | Rectangle 130 | Rectangle 131 | Rectangle 132 | Line 133

### Alt/Text Metadata 4.1

AutoShape 5

### Alt/Text Metadata 4.2

Rectangle 6

### Alt/Text Metadata 4.3

Rectangle 7

### Alt/Text Metadata 4.4

Rectangle 8

### Alt/Text Metadata 4.5

Rectangle 9

### Shape 4.6 Rectangle 10

Decode

### Alt/Text Metadata 4.6

Rectangle 10

### Alt/Text Metadata 4.7

Rectangle 11

### Alt/Text Metadata 4.8

Rectangle 12

### Shape 4.9 Rectangle 13

R

### Alt/Text Metadata 4.9

Rectangle 13

### Shape 4.10 Rectangle 14

F

### Alt/Text Metadata 4.10

Rectangle 14

### Alt/Text Metadata 4.11

Rectangle 15

### Alt/Text Metadata 4.12

Rectangle 16

### Alt/Text Metadata 4.13

Rectangle 17

### Alt/Text Metadata 4.14

Rectangle 18

### Alt/Text Metadata 4.15

Rectangle 19

### Alt/Text Metadata 4.16

Rectangle 20

### Alt/Text Metadata 4.17

Rectangle 21

### Alt/Text Metadata 4.18

Rectangle 22

### Alt/Text Metadata 4.19

Line 23

### Alt/Text Metadata 4.20

Freeform 24

### Alt/Text Metadata 4.21

Rectangle 25

### Alt/Text Metadata 4.22

Rectangle 26

### Shape 4.23 Rectangle 27

A

### Alt/Text Metadata 4.23

Rectangle 27

### Shape 4.24 Rectangle 28

L

### Alt/Text Metadata 4.24

Rectangle 28

### Shape 4.25 Rectangle 29

U

### Alt/Text Metadata 4.25

Rectangle 29

### Alt/Text Metadata 4.26

Rectangle 30

### Alt/Text Metadata 4.27

Rectangle 31

### Alt/Text Metadata 4.28

Rectangle 32

### Alt/Text Metadata 4.29

Rectangle 33

### Alt/Text Metadata 4.30

Rectangle 34

### Alt/Text Metadata 4.31

Rectangle 35

### Alt/Text Metadata 4.32

Rectangle 36

### Alt/Text Metadata 4.33

Rectangle 37

### Alt/Text Metadata 4.34

Rectangle 38

### Alt/Text Metadata 4.35

Rectangle 39

### Alt/Text Metadata 4.36

Line 40

### Alt/Text Metadata 4.37

Freeform 41

### Alt/Text Metadata 4.38

Line 42

### Alt/Text Metadata 4.39

Freeform 43

### Alt/Text Metadata 4.40

Line 44

### Alt/Text Metadata 4.41

Freeform 45

### Alt/Text Metadata 4.42

Line 46

### Alt/Text Metadata 4.43

Freeform 47

### Alt/Text Metadata 4.44

Line 48

### Alt/Text Metadata 4.45

Freeform 49

### Alt/Text Metadata 4.46

Line 50

### Alt/Text Metadata 4.47

Freeform 51

### Alt/Text Metadata 4.48

Rectangle 52

### Alt/Text Metadata 4.49

Rectangle 53

### Shape 4.50 Rectangle 54

D-Cache

### Alt/Text Metadata 4.50

Rectangle 54

### Alt/Text Metadata 4.51

Line 55

### Alt/Text Metadata 4.52

Freeform 56

### Alt/Text Metadata 4.53

Line 57

### Alt/Text Metadata 4.54

Freeform 58

### Alt/Text Metadata 4.55

Line 59

### Alt/Text Metadata 4.56

Freeform 60

### Alt/Text Metadata 4.57

Freeform 61

### Alt/Text Metadata 4.58

Line 62

### Alt/Text Metadata 4.59

Freeform 63

### Alt/Text Metadata 4.60

Rectangle 64

### Alt/Text Metadata 4.61

Rectangle 65

### Shape 4.62 Rectangle 66

Thread Warp 6

### Alt/Text Metadata 4.62

Rectangle 66

### Alt/Text Metadata 4.63

Rectangle 67

### Alt/Text Metadata 4.64

Rectangle 68

### Shape 4.65 Rectangle 69

Thread Warp 1

### Alt/Text Metadata 4.65

Rectangle 69

### Alt/Text Metadata 4.66

Rectangle 70

### Alt/Text Metadata 4.67

Rectangle 71

### Shape 4.68 Rectangle 72

Thread Warp 2

### Alt/Text Metadata 4.68

Rectangle 72

### Alt/Text Metadata 4.69

Freeform 73

### Alt/Text Metadata 4.70

Freeform 74

### Alt/Text Metadata 4.71

Freeform 75

### Alt/Text Metadata 4.72

Freeform 76

### Alt/Text Metadata 4.73

Line 77

### Alt/Text Metadata 4.74

Freeform 78

### Alt/Text Metadata 4.75

Freeform 79

### Alt/Text Metadata 4.76

Freeform 80

### Alt/Text Metadata 4.77

Freeform 81

### Shape 4.78 Rectangle 82

Data

### Alt/Text Metadata 4.78

Rectangle 82

### Shape 4.79 Rectangle 83

All Hit?

### Alt/Text Metadata 4.79

Rectangle 83

### Shape 4.80 Rectangle 84

Miss?

### Alt/Text Metadata 4.80

Rectangle 84

### Alt/Text Metadata 4.81

Freeform 85

### Alt/Text Metadata 4.82

Freeform 86

### Alt/Text Metadata 4.83

Freeform 87

### Alt/Text Metadata 4.84

Freeform 88

### Shape 4.85 Rectangle 89

Warps accessing

### Alt/Text Metadata 4.85

Rectangle 89

### Shape 4.86 Rectangle 90

memory hierarchy

### Alt/Text Metadata 4.86

Rectangle 90

### Alt/Text Metadata 4.87

Rectangle 91

### Alt/Text Metadata 4.88

Rectangle 92

### Alt/Text Metadata 4.89

Rectangle 93

### Alt/Text Metadata 4.90

Rectangle 94

### Shape 4.91 Rectangle 95

Thread Warp 3

### Alt/Text Metadata 4.91

Rectangle 95

### Alt/Text Metadata 4.92

Rectangle 96

### Alt/Text Metadata 4.93

Rectangle 97

### Shape 4.94 Rectangle 98

Thread Warp 8

### Alt/Text Metadata 4.94

Rectangle 98

### Alt/Text Metadata 4.95

Freeform 99

### Alt/Text Metadata 4.96

Freeform 100

### Alt/Text Metadata 4.97

Freeform 101

### Alt/Text Metadata 4.98

Freeform 102

### Alt/Text Metadata 4.99

Freeform 103

### Alt/Text Metadata 4.100

Freeform 104

### Alt/Text Metadata 4.101

Line 105

### Alt/Text Metadata 4.102

Freeform 106

### Alt/Text Metadata 4.103

Freeform 107

### Alt/Text Metadata 4.104

Freeform 108

### Alt/Text Metadata 4.105

Rectangle 109

### Alt/Text Metadata 4.106

Rectangle 110

### Shape 4.107 Rectangle 111

Writeback

### Alt/Text Metadata 4.107

Rectangle 111

### Shape 4.108 Rectangle 112

Warps available

### Alt/Text Metadata 4.108

Rectangle 112

### Shape 4.109 Rectangle 113

for scheduling

### Alt/Text Metadata 4.109

Rectangle 113

### Alt/Text Metadata 4.110

Freeform 114

### Alt/Text Metadata 4.111

Freeform 115

### Alt/Text Metadata 4.112

Freeform 116

### Alt/Text Metadata 4.113

Freeform 117

### Alt/Text Metadata 4.114

Freeform 118

### Alt/Text Metadata 4.115

Freeform 119

### Alt/Text Metadata 4.116

Freeform 120

### Alt/Text Metadata 4.117

Freeform 121

### Alt/Text Metadata 4.118

Freeform 122

### Alt/Text Metadata 4.119

Freeform 123

### Alt/Text Metadata 4.120

Freeform 124

### Alt/Text Metadata 4.121

Freeform 125

### Alt/Text Metadata 4.122

Rectangle 126

### Alt/Text Metadata 4.123

Rectangle 127

### Shape 4.124 Rectangle 128

Thread Warp 7

### Alt/Text Metadata 4.124

Rectangle 128

### Alt/Text Metadata 4.125

Rectangle 129

### Alt/Text Metadata 4.126

Rectangle 130

### Shape 4.127 Rectangle 131

I-Fetch

### Alt/Text Metadata 4.127

Rectangle 131

### Shape 4.128 Rectangle 132

SIMD Pipeline

### Alt/Text Metadata 4.128

Rectangle 132

### Alt/Text Metadata 4.129

Line 133

### Shape 5 TextBox 134

Slide credit: Tor Aamodt

### Alt/Text Metadata 5

TextBox 134

### Speaker notes

With a large number of shader threads multiplexed on the same execution re- sources, our architecture employs fine-grained multithreading  where individual threads are interleaved by the fetch unit to proactively hide the potential latency of stalls before they occur. As illustrated by Figure, warps are issued fairly in a round-robin queue. When a thread is blocked by a memory request, shader core simply removes that thread’s warp from the pool of “ready” warps and thereby allows other threads to proceed while the memory system processes its request.
 With a large number of threads (1024 per shader core) interleaved on the same pipeline, FGMT effectively hides the latency of most memory operations since the pipeline is occupied with instructions from other threads while memory operations complete. also hides the pipeline latency so that data bypassing logic can potentially be omitted to save area with minimal impact on performance. simplify the dependency check logic design by restricting each thread to have at most one instruction running in the pipeline at any time.

## Slide 101

### Shape 1 Title 1

Warp Execution (Recall the Slide)

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

101

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Shape 3 Text Box 3

32-thread warp executing ADD A[tid],B[tid]  C[tid]

### Alt/Text Metadata 3

Text Box 3

### Alt/Text Metadata 4

Group 4 | Group 5 | Freeform 6 | Group 10 | Rectangle 8 | Freeform 9 | Line 10 | Group 11 | Rectangle 12 | Freeform 13 | Line 14 | Group 15 | Rectangle 16 | Freeform 17 | Line 18 | Text Box 19 | Text Box 20 | Text Box 21 | Line 22 | Line 23 | Line 24 | Text Box 25 | Text Box 26 | Text Box 27 | Text Box 28 | Text Box 29 | Text Box 30 | Text Box 31 | Text Box 32 | Line 33 | Oval 34

### Alt/Text Metadata 4.1

Group 5 | Freeform 6 | Group 10 | Rectangle 8 | Freeform 9 | Line 10 | Group 11 | Rectangle 12 | Freeform 13 | Line 14 | Group 15 | Rectangle 16 | Freeform 17 | Line 18 | Text Box 19 | Text Box 20 | Text Box 21 | Line 22 | Line 23 | Line 24 | Text Box 25 | Text Box 26 | Text Box 27 | Text Box 28 | Text Box 29 | Text Box 30 | Text Box 31 | Text Box 32

### Alt/Text Metadata 4.1.1

Freeform 6

### Alt/Text Metadata 4.1.2

Group 10 | Rectangle 8 | Freeform 9 | Line 10

### Alt/Text Metadata 4.1.2.1

Rectangle 8

### Alt/Text Metadata 4.1.2.2

Freeform 9

### Alt/Text Metadata 4.1.2.3

Line 10

### Alt/Text Metadata 4.1.3

Group 11 | Rectangle 12 | Freeform 13 | Line 14

### Alt/Text Metadata 4.1.3.1

Rectangle 12

### Alt/Text Metadata 4.1.3.2

Freeform 13

### Alt/Text Metadata 4.1.3.3

Line 14

### Alt/Text Metadata 4.1.4

Group 15 | Rectangle 16 | Freeform 17 | Line 18

### Alt/Text Metadata 4.1.4.1

Rectangle 16

### Alt/Text Metadata 4.1.4.2

Freeform 17

### Alt/Text Metadata 4.1.4.3

Line 18

### Shape 4.1.5 Text Box 19

C[1]

### Alt/Text Metadata 4.1.5

Text Box 19

### Shape 4.1.6 Text Box 20

C[2]

### Alt/Text Metadata 4.1.6

Text Box 20

### Shape 4.1.7 Text Box 21

C[0]

### Alt/Text Metadata 4.1.7

Text Box 21

### Alt/Text Metadata 4.1.8

Line 22

### Alt/Text Metadata 4.1.9

Line 23

### Alt/Text Metadata 4.1.10

Line 24

### Shape 4.1.11 Text Box 25

A[3]

### Alt/Text Metadata 4.1.11

Text Box 25

### Shape 4.1.12 Text Box 26

B[3]

### Alt/Text Metadata 4.1.12

Text Box 26

### Shape 4.1.13 Text Box 27

A[4]

### Alt/Text Metadata 4.1.13

Text Box 27

### Shape 4.1.14 Text Box 28

B[4]

### Alt/Text Metadata 4.1.14

Text Box 28

### Shape 4.1.15 Text Box 29

A[5]

### Alt/Text Metadata 4.1.15

Text Box 29

### Shape 4.1.16 Text Box 30

B[5]

### Alt/Text Metadata 4.1.16

Text Box 30

### Shape 4.1.17 Text Box 31

A[6]

### Alt/Text Metadata 4.1.17

Text Box 31

### Shape 4.1.18 Text Box 32

B[6]

### Alt/Text Metadata 4.1.18

Text Box 32

### Alt/Text Metadata 4.2

Line 33

### Shape 4.3 Oval 34

Execution using one pipelined functional unit

### Alt/Text Metadata 4.3

Oval 34

### Alt/Text Metadata 5

Group 35 | Group 36 | Freeform 37 | Group 38 | Rectangle 39 | Freeform 40 | Line 41 | Group 42 | Rectangle 43 | Freeform 44 | Line 45 | Group 46 | Rectangle 47 | Freeform 48 | Line 49 | Text Box 50 | Text Box 51 | Text Box 52 | Line 53 | Line 54 | Line 55 | Text Box 56 | Text Box 57 | Text Box 58 | Text Box 59 | Text Box 60 | Text Box 61 | Text Box 62 | Text Box 63 | Group 64 | Freeform 65 | Group 66 | Rectangle 67 | Freeform 68 | Line 69 | Group 70 | Rectangle 71 | Freeform 72 | Line 73 | Group 74 | Rectangle 75 | Freeform 76 | Line 77 | Text Box 78 | Text Box 79 | Text Box 80 | Line 81 | Line 82 | Line 83 | Text Box 84 | Text Box 85 | Text Box 86 | Text Box 87 | Text Box 88 | Text Box 89 | Text Box 90 | Text Box 91 | Group 92 | Freeform 93 | Group 94 | Rectangle 95 | Freeform 96 | Line 97 | Group 98 | Rectangle 99 | Freeform 100 | Line 101 | Group 102 | Rectangle 103 | Freeform 104 | Line 105 | Text Box 106 | Text Box 107 | Text Box 108 | Line 109 | Line 110 | Line 111 | Text Box 112 | Text Box 113 | Text Box 114 | Text Box 115 | Text Box 116 | Text Box 117 | Text Box 118 | Text Box 119 | Group 120 | Freeform 121 | Group 122 | Rectangle 123 | Freeform 124 | Line 125 | Group 126 | Rectangle 127 | Freeform 128 | Line 129 | Group 130 | Rectangle 131 | Freeform 132 | Line 133 | Text Box 134 | Text Box 135 | Text Box 136 | Line 137 | Line 138 | Line 139 | Text Box 140 | Text Box 141 | Text Box 142 | Text Box 143 | Text Box 144 | Text Box 145 | Text Box 146 | Text Box 147 | Line 148 | Oval 149

### Alt/Text Metadata 5.1

Group 36 | Freeform 37 | Group 38 | Rectangle 39 | Freeform 40 | Line 41 | Group 42 | Rectangle 43 | Freeform 44 | Line 45 | Group 46 | Rectangle 47 | Freeform 48 | Line 49 | Text Box 50 | Text Box 51 | Text Box 52 | Line 53 | Line 54 | Line 55 | Text Box 56 | Text Box 57 | Text Box 58 | Text Box 59 | Text Box 60 | Text Box 61 | Text Box 62 | Text Box 63

### Alt/Text Metadata 5.1.1

Freeform 37

### Alt/Text Metadata 5.1.2

Group 38 | Rectangle 39 | Freeform 40 | Line 41

### Alt/Text Metadata 5.1.2.1

Rectangle 39

### Alt/Text Metadata 5.1.2.2

Freeform 40

### Alt/Text Metadata 5.1.2.3

Line 41

### Alt/Text Metadata 5.1.3

Group 42 | Rectangle 43 | Freeform 44 | Line 45

### Alt/Text Metadata 5.1.3.1

Rectangle 43

### Alt/Text Metadata 5.1.3.2

Freeform 44

### Alt/Text Metadata 5.1.3.3

Line 45

### Alt/Text Metadata 5.1.4

Group 46 | Rectangle 47 | Freeform 48 | Line 49

### Alt/Text Metadata 5.1.4.1

Rectangle 47

### Alt/Text Metadata 5.1.4.2

Freeform 48

### Alt/Text Metadata 5.1.4.3

Line 49

### Shape 5.1.5 Text Box 50

C[4]

### Alt/Text Metadata 5.1.5

Text Box 50

### Shape 5.1.6 Text Box 51

C[8]

### Alt/Text Metadata 5.1.6

Text Box 51

### Alt/Text Metadata 5.1.7

Text Box 52

### Alt/Text Metadata 5.1.8

Line 53

### Alt/Text Metadata 5.1.9

Line 54

### Alt/Text Metadata 5.1.10

Line 55

### Shape 5.1.11 Text Box 56

A[12]

### Alt/Text Metadata 5.1.11

Text Box 56

### Shape 5.1.12 Text Box 57

B[12]

### Alt/Text Metadata 5.1.12

Text Box 57

### Shape 5.1.13 Text Box 58

A[16]

### Alt/Text Metadata 5.1.13

Text Box 58

### Shape 5.1.14 Text Box 59

B[16]

### Alt/Text Metadata 5.1.14

Text Box 59

### Shape 5.1.15 Text Box 60

A[20]

### Alt/Text Metadata 5.1.15

Text Box 60

### Shape 5.1.16 Text Box 61

B[20]

### Alt/Text Metadata 5.1.16

Text Box 61

### Shape 5.1.17 Text Box 62

A[24]

### Alt/Text Metadata 5.1.17

Text Box 62

### Shape 5.1.18 Text Box 63

B[24]

### Alt/Text Metadata 5.1.18

Text Box 63

### Alt/Text Metadata 5.2

Group 64 | Freeform 65 | Group 66 | Rectangle 67 | Freeform 68 | Line 69 | Group 70 | Rectangle 71 | Freeform 72 | Line 73 | Group 74 | Rectangle 75 | Freeform 76 | Line 77 | Text Box 78 | Text Box 79 | Text Box 80 | Line 81 | Line 82 | Line 83 | Text Box 84 | Text Box 85 | Text Box 86 | Text Box 87 | Text Box 88 | Text Box 89 | Text Box 90 | Text Box 91

### Alt/Text Metadata 5.2.1

Freeform 65

### Alt/Text Metadata 5.2.2

Group 66 | Rectangle 67 | Freeform 68 | Line 69

### Alt/Text Metadata 5.2.2.1

Rectangle 67

### Alt/Text Metadata 5.2.2.2

Freeform 68

### Alt/Text Metadata 5.2.2.3

Line 69

### Alt/Text Metadata 5.2.3

Group 70 | Rectangle 71 | Freeform 72 | Line 73

### Alt/Text Metadata 5.2.3.1

Rectangle 71

### Alt/Text Metadata 5.2.3.2

Freeform 72

### Alt/Text Metadata 5.2.3.3

Line 73

### Alt/Text Metadata 5.2.4

Group 74 | Rectangle 75 | Freeform 76 | Line 77

### Alt/Text Metadata 5.2.4.1

Rectangle 75

### Alt/Text Metadata 5.2.4.2

Freeform 76

### Alt/Text Metadata 5.2.4.3

Line 77

### Shape 5.2.5 Text Box 78

C[5]

### Alt/Text Metadata 5.2.5

Text Box 78

### Shape 5.2.6 Text Box 79

C[9]

### Alt/Text Metadata 5.2.6

Text Box 79

### Alt/Text Metadata 5.2.7

Text Box 80

### Alt/Text Metadata 5.2.8

Line 81

### Alt/Text Metadata 5.2.9

Line 82

### Alt/Text Metadata 5.2.10

Line 83

### Shape 5.2.11 Text Box 84

A[13]

### Alt/Text Metadata 5.2.11

Text Box 84

### Shape 5.2.12 Text Box 85

B[13]

### Alt/Text Metadata 5.2.12

Text Box 85

### Shape 5.2.13 Text Box 86

A[17]

### Alt/Text Metadata 5.2.13

Text Box 86

### Shape 5.2.14 Text Box 87

B[17]

### Alt/Text Metadata 5.2.14

Text Box 87

### Shape 5.2.15 Text Box 88

A[21]

### Alt/Text Metadata 5.2.15

Text Box 88

### Shape 5.2.16 Text Box 89

B[21]

### Alt/Text Metadata 5.2.16

Text Box 89

### Shape 5.2.17 Text Box 90

A[25]

### Alt/Text Metadata 5.2.17

Text Box 90

### Shape 5.2.18 Text Box 91

B[25]

### Alt/Text Metadata 5.2.18

Text Box 91

### Alt/Text Metadata 5.3

Group 92 | Freeform 93 | Group 94 | Rectangle 95 | Freeform 96 | Line 97 | Group 98 | Rectangle 99 | Freeform 100 | Line 101 | Group 102 | Rectangle 103 | Freeform 104 | Line 105 | Text Box 106 | Text Box 107 | Text Box 108 | Line 109 | Line 110 | Line 111 | Text Box 112 | Text Box 113 | Text Box 114 | Text Box 115 | Text Box 116 | Text Box 117 | Text Box 118 | Text Box 119

### Alt/Text Metadata 5.3.1

Freeform 93

### Alt/Text Metadata 5.3.2

Group 94 | Rectangle 95 | Freeform 96 | Line 97

### Alt/Text Metadata 5.3.2.1

Rectangle 95

### Alt/Text Metadata 5.3.2.2

Freeform 96

### Alt/Text Metadata 5.3.2.3

Line 97

### Alt/Text Metadata 5.3.3

Group 98 | Rectangle 99 | Freeform 100 | Line 101

### Alt/Text Metadata 5.3.3.1

Rectangle 99

### Alt/Text Metadata 5.3.3.2

Freeform 100

### Alt/Text Metadata 5.3.3.3

Line 101

### Alt/Text Metadata 5.3.4

Group 102 | Rectangle 103 | Freeform 104 | Line 105

### Alt/Text Metadata 5.3.4.1

Rectangle 103

### Alt/Text Metadata 5.3.4.2

Freeform 104

### Alt/Text Metadata 5.3.4.3

Line 105

### Shape 5.3.5 Text Box 106

C[6]

### Alt/Text Metadata 5.3.5

Text Box 106

### Shape 5.3.6 Text Box 107

C[10]

### Alt/Text Metadata 5.3.6

Text Box 107

### Alt/Text Metadata 5.3.7

Text Box 108

### Alt/Text Metadata 5.3.8

Line 109

### Alt/Text Metadata 5.3.9

Line 110

### Alt/Text Metadata 5.3.10

Line 111

### Shape 5.3.11 Text Box 112

A[14]

### Alt/Text Metadata 5.3.11

Text Box 112

### Shape 5.3.12 Text Box 113

B[14]

### Alt/Text Metadata 5.3.12

Text Box 113

### Shape 5.3.13 Text Box 114

A[18]

### Alt/Text Metadata 5.3.13

Text Box 114

### Shape 5.3.14 Text Box 115

B[18]

### Alt/Text Metadata 5.3.14

Text Box 115

### Shape 5.3.15 Text Box 116

A[22]

### Alt/Text Metadata 5.3.15

Text Box 116

### Shape 5.3.16 Text Box 117

B[22]

### Alt/Text Metadata 5.3.16

Text Box 117

### Shape 5.3.17 Text Box 118

A[26]

### Alt/Text Metadata 5.3.17

Text Box 118

### Shape 5.3.18 Text Box 119

B[26]

### Alt/Text Metadata 5.3.18

Text Box 119

### Alt/Text Metadata 5.4

Group 120 | Freeform 121 | Group 122 | Rectangle 123 | Freeform 124 | Line 125 | Group 126 | Rectangle 127 | Freeform 128 | Line 129 | Group 130 | Rectangle 131 | Freeform 132 | Line 133 | Text Box 134 | Text Box 135 | Text Box 136 | Line 137 | Line 138 | Line 139 | Text Box 140 | Text Box 141 | Text Box 142 | Text Box 143 | Text Box 144 | Text Box 145 | Text Box 146 | Text Box 147

### Alt/Text Metadata 5.4.1

Freeform 121

### Alt/Text Metadata 5.4.2

Group 122 | Rectangle 123 | Freeform 124 | Line 125

### Alt/Text Metadata 5.4.2.1

Rectangle 123

### Alt/Text Metadata 5.4.2.2

Freeform 124

### Alt/Text Metadata 5.4.2.3

Line 125

### Alt/Text Metadata 5.4.3

Group 126 | Rectangle 127 | Freeform 128 | Line 129

### Alt/Text Metadata 5.4.3.1

Rectangle 127

### Alt/Text Metadata 5.4.3.2

Freeform 128

### Alt/Text Metadata 5.4.3.3

Line 129

### Alt/Text Metadata 5.4.4

Group 130 | Rectangle 131 | Freeform 132 | Line 133

### Alt/Text Metadata 5.4.4.1

Rectangle 131

### Alt/Text Metadata 5.4.4.2

Freeform 132

### Alt/Text Metadata 5.4.4.3

Line 133

### Shape 5.4.5 Text Box 134

C[7]

### Alt/Text Metadata 5.4.5

Text Box 134

### Shape 5.4.6 Text Box 135

C[11]

### Alt/Text Metadata 5.4.6

Text Box 135

### Shape 5.4.7 Text Box 136

C[3]

### Alt/Text Metadata 5.4.7

Text Box 136

### Alt/Text Metadata 5.4.8

Line 137

### Alt/Text Metadata 5.4.9

Line 138

### Alt/Text Metadata 5.4.10

Line 139

### Shape 5.4.11 Text Box 140

A[15]

### Alt/Text Metadata 5.4.11

Text Box 140

### Shape 5.4.12 Text Box 141

B[15]

### Alt/Text Metadata 5.4.12

Text Box 141

### Shape 5.4.13 Text Box 142

A[19]

### Alt/Text Metadata 5.4.13

Text Box 142

### Shape 5.4.14 Text Box 143

B[19]

### Alt/Text Metadata 5.4.14

Text Box 143

### Shape 5.4.15 Text Box 144

A[23]

### Alt/Text Metadata 5.4.15

Text Box 144

### Shape 5.4.16 Text Box 145

B[23]

### Alt/Text Metadata 5.4.16

Text Box 145

### Shape 5.4.17 Text Box 146

A[27]

### Alt/Text Metadata 5.4.17

Text Box 146

### Shape 5.4.18 Text Box 147

B[27]

### Alt/Text Metadata 5.4.18

Text Box 147

### Alt/Text Metadata 5.5

Line 148

### Shape 5.6 Oval 149

Execution using four pipelined functional units

### Alt/Text Metadata 5.6

Oval 149

### Shape 6 TextBox 151

Slide credit: Krste Asanovic

### Alt/Text Metadata 6

TextBox 151

### Alt/Text Metadata 7

Straight Arrow Connector 86

### Shape 8 TextBox 87

Time

### Alt/Text Metadata 8

TextBox 87

### Alt/Text Metadata 9

Straight Arrow Connector 121

### Shape 10 TextBox 123

Space

### Alt/Text Metadata 10

TextBox 123

### Alt/Text Metadata 11

Straight Arrow Connector 124

## Slide 102

### Shape 1 Slide Number Placeholder 3

102

### Alt/Text Metadata 1

Slide Number Placeholder 3

### Alt/Text Metadata 2

Freeform 3

### Alt/Text Metadata 3

Group 4 | Rectangle 5 | Freeform 6 | Line 7

### Alt/Text Metadata 3.1

Rectangle 5

### Alt/Text Metadata 3.2

Freeform 6

### Alt/Text Metadata 3.3

Line 7

### Alt/Text Metadata 4

Group 8 | Rectangle 9 | Freeform 10 | Line 11

### Alt/Text Metadata 4.1

Rectangle 9

### Alt/Text Metadata 4.2

Freeform 10

### Alt/Text Metadata 4.3

Line 11

### Alt/Text Metadata 5

Group 12 | Rectangle 13 | Freeform 14 | Line 15

### Alt/Text Metadata 5.1

Rectangle 13

### Alt/Text Metadata 5.2

Freeform 14

### Alt/Text Metadata 5.3

Line 15

### Alt/Text Metadata 6

Line 16

### Alt/Text Metadata 7

Line 17

### Alt/Text Metadata 8

Freeform 18

### Alt/Text Metadata 9

Group 19 | Rectangle 20 | Freeform 21 | Line 22

### Alt/Text Metadata 9.1

Rectangle 20

### Alt/Text Metadata 9.2

Freeform 21

### Alt/Text Metadata 9.3

Line 22

### Alt/Text Metadata 10

Group 23 | Rectangle 24 | Freeform 25 | Line 26

### Alt/Text Metadata 10.1

Rectangle 24

### Alt/Text Metadata 10.2

Freeform 25

### Alt/Text Metadata 10.3

Line 26

### Alt/Text Metadata 11

Group 27 | Rectangle 28 | Freeform 29 | Line 30

### Alt/Text Metadata 11.1

Rectangle 28

### Alt/Text Metadata 11.2

Freeform 29

### Alt/Text Metadata 11.3

Line 30

### Alt/Text Metadata 12

Line 31

### Alt/Text Metadata 13

Line 32

### Alt/Text Metadata 14

Rectangle 33

### Alt/Text Metadata 15

Freeform 34

### Alt/Text Metadata 16

Freeform 35

### Alt/Text Metadata 17

Line 36

### Alt/Text Metadata 18

Line 37

### Alt/Text Metadata 19

Freeform 38

### Alt/Text Metadata 20

Group 39 | Rectangle 40 | Freeform 41 | Line 42

### Alt/Text Metadata 20.1

Rectangle 40

### Alt/Text Metadata 20.2

Freeform 41

### Alt/Text Metadata 20.3

Line 42

### Alt/Text Metadata 21

Group 43 | Rectangle 44 | Freeform 45 | Line 46

### Alt/Text Metadata 21.1

Rectangle 44

### Alt/Text Metadata 21.2

Freeform 45

### Alt/Text Metadata 21.3

Line 46

### Alt/Text Metadata 22

Group 47 | Rectangle 48 | Freeform 49 | Line 50

### Alt/Text Metadata 22.1

Rectangle 48

### Alt/Text Metadata 22.2

Freeform 49

### Alt/Text Metadata 22.3

Line 50

### Alt/Text Metadata 23

Line 51

### Alt/Text Metadata 24

Line 52

### Alt/Text Metadata 25

Freeform 53

### Alt/Text Metadata 26

Group 54 | Rectangle 55 | Freeform 56 | Line 57

### Alt/Text Metadata 26.1

Rectangle 55

### Alt/Text Metadata 26.2

Freeform 56

### Alt/Text Metadata 26.3

Line 57

### Alt/Text Metadata 27

Group 58 | Rectangle 59 | Freeform 60 | Line 61

### Alt/Text Metadata 27.1

Rectangle 59

### Alt/Text Metadata 27.2

Freeform 60

### Alt/Text Metadata 27.3

Line 61

### Alt/Text Metadata 28

Group 62 | Rectangle 63 | Freeform 64 | Line 65

### Alt/Text Metadata 28.1

Rectangle 63

### Alt/Text Metadata 28.2

Freeform 64

### Alt/Text Metadata 28.3

Line 65

### Alt/Text Metadata 29

Line 66

### Alt/Text Metadata 30

Line 67

### Alt/Text Metadata 31

Rectangle 68

### Alt/Text Metadata 32

Freeform 69

### Alt/Text Metadata 33

Freeform 70

### Alt/Text Metadata 34

Line 71

### Alt/Text Metadata 35

Line 72

### Alt/Text Metadata 36

Freeform 73

### Alt/Text Metadata 37

Group 74 | Rectangle 75 | Freeform 76 | Line 77

### Alt/Text Metadata 37.1

Rectangle 75

### Alt/Text Metadata 37.2

Freeform 76

### Alt/Text Metadata 37.3

Line 77

### Alt/Text Metadata 38

Group 78 | Rectangle 79 | Freeform 80 | Line 81

### Alt/Text Metadata 38.1

Rectangle 79

### Alt/Text Metadata 38.2

Freeform 80

### Alt/Text Metadata 38.3

Line 81

### Alt/Text Metadata 39

Group 82 | Rectangle 83 | Freeform 84 | Line 85

### Alt/Text Metadata 39.1

Rectangle 83

### Alt/Text Metadata 39.2

Freeform 84

### Alt/Text Metadata 39.3

Line 85

### Alt/Text Metadata 40

Line 86

### Alt/Text Metadata 41

Line 87

### Alt/Text Metadata 42

Freeform 88

### Alt/Text Metadata 43

Group 89 | Rectangle 90 | Freeform 91 | Line 92

### Alt/Text Metadata 43.1

Rectangle 90

### Alt/Text Metadata 43.2

Freeform 91

### Alt/Text Metadata 43.3

Line 92

### Alt/Text Metadata 44

Group 93 | Rectangle 94 | Freeform 95 | Line 96

### Alt/Text Metadata 44.1

Rectangle 94

### Alt/Text Metadata 44.2

Freeform 95

### Alt/Text Metadata 44.3

Line 96

### Alt/Text Metadata 45

Group 97 | Rectangle 98 | Freeform 99 | Line 100

### Alt/Text Metadata 45.1

Rectangle 98

### Alt/Text Metadata 45.2

Freeform 99

### Alt/Text Metadata 45.3

Line 100

### Alt/Text Metadata 46

Line 101

### Alt/Text Metadata 47

Line 102

### Alt/Text Metadata 48

Rectangle 103

### Alt/Text Metadata 49

Freeform 104

### Alt/Text Metadata 50

Freeform 105

### Alt/Text Metadata 51

Line 106

### Alt/Text Metadata 52

Line 107

### Alt/Text Metadata 53

Freeform 108

### Alt/Text Metadata 54

Group 109 | Rectangle 110 | Freeform 111 | Line 112

### Alt/Text Metadata 54.1

Rectangle 110

### Alt/Text Metadata 54.2

Freeform 111

### Alt/Text Metadata 54.3

Line 112

### Alt/Text Metadata 55

Group 113 | Rectangle 114 | Freeform 115 | Line 116

### Alt/Text Metadata 55.1

Rectangle 114

### Alt/Text Metadata 55.2

Freeform 115

### Alt/Text Metadata 55.3

Line 116

### Alt/Text Metadata 56

Group 117 | Rectangle 118 | Freeform 119 | Line 120

### Alt/Text Metadata 56.1

Rectangle 118

### Alt/Text Metadata 56.2

Freeform 119

### Alt/Text Metadata 56.3

Line 120

### Alt/Text Metadata 57

Line 121

### Alt/Text Metadata 58

Line 122

### Alt/Text Metadata 59

Freeform 123

### Alt/Text Metadata 60

Group 124 | Rectangle 125 | Freeform 126 | Line 127

### Alt/Text Metadata 60.1

Rectangle 125

### Alt/Text Metadata 60.2

Freeform 126

### Alt/Text Metadata 60.3

Line 127

### Alt/Text Metadata 61

Group 128 | Rectangle 129 | Freeform 130 | Line 131

### Alt/Text Metadata 61.1

Rectangle 129

### Alt/Text Metadata 61.2

Freeform 130

### Alt/Text Metadata 61.3

Line 131

### Alt/Text Metadata 62

Group 132 | Rectangle 133 | Freeform 134 | Line 135

### Alt/Text Metadata 62.1

Rectangle 133

### Alt/Text Metadata 62.2

Freeform 134

### Alt/Text Metadata 62.3

Line 135

### Alt/Text Metadata 63

Line 136

### Alt/Text Metadata 64

Line 137

### Alt/Text Metadata 65

Rectangle 138

### Alt/Text Metadata 66

Freeform 139

### Alt/Text Metadata 67

Freeform 140

### Alt/Text Metadata 68

Line 141

### Alt/Text Metadata 69

Line 142

### Alt/Text Metadata 70

Group 143 | AutoShape 144 | Line 145 | Text Box 146

### Alt/Text Metadata 70.1

AutoShape 144

### Alt/Text Metadata 70.2

Line 145

### Shape 70.3 Text Box 146

Lane

### Alt/Text Metadata 70.3

Text Box 146

### Alt/Text Metadata 71

Group 147 | AutoShape 148 | Line 149 | Text Box 150

### Alt/Text Metadata 71.1

AutoShape 148

### Alt/Text Metadata 71.2

Line 149

### Shape 71.3 Text Box 150

Functional Unit

### Alt/Text Metadata 71.3

Text Box 150

### Shape 72 Text Box 151

Registers
for each
Thread

### Alt/Text Metadata 72

Text Box 151

### Alt/Text Metadata 73

Line 152

### Shape 74 Rectangle 153

Memory Subsystem

### Alt/Text Metadata 74

Rectangle 153

### Shape 75 Text Box 154

Registers for thread IDs
0, 4, 8, …

### Alt/Text Metadata 75

Text Box 154

### Shape 76 Text Box 155

Registers for thread IDs
1, 5, 9, …

### Alt/Text Metadata 76

Text Box 155

### Shape 77 Text Box 156

Registers for thread IDs
2, 6, 10, …

### Alt/Text Metadata 77

Text Box 156

### Shape 78 Text Box 157

Registers for thread IDs
3, 7, 11, …

### Alt/Text Metadata 78

Text Box 157

### Shape 79 TextBox 161

Slide credit: Krste Asanovic

### Alt/Text Metadata 79

TextBox 161

### Shape 92 Title 1

SIMD Execution Unit Structure

### Alt/Text Metadata 92

Title 1

## Slide 103

### Shape 1 Marcador de contenido 2

CPU threads and GPU kernels
Sequential or modestly parallel sections on CPU
Massively parallel sections on GPU: Blocks of threads

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Text Box 4

Serial Code (host)

### Alt/Text Metadata 2

Text Box 4

### Alt/Text Metadata 3

Group 5 | Rectangle 6 | Text Box 7 | Group 8 | Text Box 9 | Group 10 | Freeform 11 | Freeform 12 | Freeform 13 | Freeform 14 | Freeform 15 | Freeform 16 | Freeform 17 | Freeform 18 | Freeform 19 | Freeform 20 | Freeform 21 | Group 22 | Text Box 23 | Group 24 | Freeform 25 | Freeform 26 | Freeform 27 | Freeform 28 | Freeform 29 | Freeform 30 | Freeform 31 | Freeform 32 | Freeform 33 | Freeform 34 | Freeform 35 | Group 36 | Text Box 37 | Group 38 | Freeform 39 | Freeform 40 | Freeform 41 | Freeform 42 | Freeform 43 | Freeform 44 | Freeform 45 | Freeform 46 | Freeform 47 | Freeform 48 | Freeform 49 | Group 50 | Text Box 51 | Group 52 | Freeform 53 | Freeform 54 | Freeform 55 | Freeform 56 | Freeform 57 | Freeform 58 | Freeform 59 | Freeform 60 | Freeform 61 | Freeform 62 | Freeform 63

### Alt/Text Metadata 3.1

Rectangle 6

### Shape 3.2 Text Box 7

. . .

### Alt/Text Metadata 3.2

Text Box 7

### Alt/Text Metadata 3.3

Group 8 | Text Box 9 | Group 10 | Freeform 11 | Freeform 12 | Freeform 13 | Freeform 14 | Freeform 15 | Freeform 16 | Freeform 17 | Freeform 18 | Freeform 19 | Freeform 20 | Freeform 21

### Alt/Text Metadata 3.3.1

Text Box 9

### Alt/Text Metadata 3.3.2

Group 10 | Freeform 11 | Freeform 12 | Freeform 13 | Freeform 14 | Freeform 15 | Freeform 16 | Freeform 17 | Freeform 18 | Freeform 19 | Freeform 20 | Freeform 21

### Alt/Text Metadata 3.3.2.1

Freeform 11

### Alt/Text Metadata 3.3.2.2

Freeform 12

### Alt/Text Metadata 3.3.2.3

Freeform 13

### Alt/Text Metadata 3.3.2.4

Freeform 14

### Alt/Text Metadata 3.3.2.5

Freeform 15

### Alt/Text Metadata 3.3.2.6

Freeform 16

### Alt/Text Metadata 3.3.2.7

Freeform 17

### Alt/Text Metadata 3.3.2.8

Freeform 18

### Alt/Text Metadata 3.3.2.9

Freeform 19

### Alt/Text Metadata 3.3.2.10

Freeform 20

### Alt/Text Metadata 3.3.2.11

Freeform 21

### Alt/Text Metadata 3.4

Group 22 | Text Box 23 | Group 24 | Freeform 25 | Freeform 26 | Freeform 27 | Freeform 28 | Freeform 29 | Freeform 30 | Freeform 31 | Freeform 32 | Freeform 33 | Freeform 34 | Freeform 35

### Alt/Text Metadata 3.4.1

Text Box 23

### Alt/Text Metadata 3.4.2

Group 24 | Freeform 25 | Freeform 26 | Freeform 27 | Freeform 28 | Freeform 29 | Freeform 30 | Freeform 31 | Freeform 32 | Freeform 33 | Freeform 34 | Freeform 35

### Alt/Text Metadata 3.4.2.1

Freeform 25

### Alt/Text Metadata 3.4.2.2

Freeform 26

### Alt/Text Metadata 3.4.2.3

Freeform 27

### Alt/Text Metadata 3.4.2.4

Freeform 28

### Alt/Text Metadata 3.4.2.5

Freeform 29

### Alt/Text Metadata 3.4.2.6

Freeform 30

### Alt/Text Metadata 3.4.2.7

Freeform 31

### Alt/Text Metadata 3.4.2.8

Freeform 32

### Alt/Text Metadata 3.4.2.9

Freeform 33

### Alt/Text Metadata 3.4.2.10

Freeform 34

### Alt/Text Metadata 3.4.2.11

Freeform 35

### Alt/Text Metadata 3.5

Group 36 | Text Box 37 | Group 38 | Freeform 39 | Freeform 40 | Freeform 41 | Freeform 42 | Freeform 43 | Freeform 44 | Freeform 45 | Freeform 46 | Freeform 47 | Freeform 48 | Freeform 49

### Alt/Text Metadata 3.5.1

Text Box 37

### Alt/Text Metadata 3.5.2

Group 38 | Freeform 39 | Freeform 40 | Freeform 41 | Freeform 42 | Freeform 43 | Freeform 44 | Freeform 45 | Freeform 46 | Freeform 47 | Freeform 48 | Freeform 49

### Alt/Text Metadata 3.5.2.1

Freeform 39

### Alt/Text Metadata 3.5.2.2

Freeform 40

### Alt/Text Metadata 3.5.2.3

Freeform 41

### Alt/Text Metadata 3.5.2.4

Freeform 42

### Alt/Text Metadata 3.5.2.5

Freeform 43

### Alt/Text Metadata 3.5.2.6

Freeform 44

### Alt/Text Metadata 3.5.2.7

Freeform 45

### Alt/Text Metadata 3.5.2.8

Freeform 46

### Alt/Text Metadata 3.5.2.9

Freeform 47

### Alt/Text Metadata 3.5.2.10

Freeform 48

### Alt/Text Metadata 3.5.2.11

Freeform 49

### Alt/Text Metadata 3.6

Group 50 | Text Box 51 | Group 52 | Freeform 53 | Freeform 54 | Freeform 55 | Freeform 56 | Freeform 57 | Freeform 58 | Freeform 59 | Freeform 60 | Freeform 61 | Freeform 62 | Freeform 63

### Alt/Text Metadata 3.6.1

Text Box 51

### Alt/Text Metadata 3.6.2

Group 52 | Freeform 53 | Freeform 54 | Freeform 55 | Freeform 56 | Freeform 57 | Freeform 58 | Freeform 59 | Freeform 60 | Freeform 61 | Freeform 62 | Freeform 63

### Alt/Text Metadata 3.6.2.1

Freeform 53

### Alt/Text Metadata 3.6.2.2

Freeform 54

### Alt/Text Metadata 3.6.2.3

Freeform 55

### Alt/Text Metadata 3.6.2.4

Freeform 56

### Alt/Text Metadata 3.6.2.5

Freeform 57

### Alt/Text Metadata 3.6.2.6

Freeform 58

### Alt/Text Metadata 3.6.2.7

Freeform 59

### Alt/Text Metadata 3.6.2.8

Freeform 60

### Alt/Text Metadata 3.6.2.9

Freeform 61

### Alt/Text Metadata 3.6.2.10

Freeform 62

### Alt/Text Metadata 3.6.2.11

Freeform 63

### Alt/Text Metadata 4

Group 64 | Rectangle 65 | Text Box 66 | Group 67 | Text Box 68 | Group 69 | Freeform 70 | Freeform 71 | Freeform 72 | Freeform 73 | Freeform 74 | Freeform 75 | Freeform 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80 | Group 81 | Text Box 82 | Group 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87 | Freeform 88 | Freeform 89 | Freeform 90 | Freeform 91 | Freeform 92 | Freeform 93 | Freeform 94 | Group 95 | Text Box 96 | Group 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103 | Freeform 104 | Freeform 105 | Freeform 106 | Freeform 107 | Freeform 108 | Group 109 | Text Box 110 | Group 111 | Freeform 112 | Freeform 113 | Freeform 114 | Freeform 115 | Freeform 116 | Freeform 117 | Freeform 118 | Freeform 119 | Freeform 120 | Freeform 121 | Freeform 122

### Alt/Text Metadata 4.1

Rectangle 65

### Alt/Text Metadata 4.2

Text Box 66

### Alt/Text Metadata 4.3

Group 67 | Text Box 68 | Group 69 | Freeform 70 | Freeform 71 | Freeform 72 | Freeform 73 | Freeform 74 | Freeform 75 | Freeform 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80

### Alt/Text Metadata 4.3.1

Text Box 68

### Alt/Text Metadata 4.3.2

Group 69 | Freeform 70 | Freeform 71 | Freeform 72 | Freeform 73 | Freeform 74 | Freeform 75 | Freeform 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80

### Alt/Text Metadata 4.3.2.1

Freeform 70

### Alt/Text Metadata 4.3.2.2

Freeform 71

### Alt/Text Metadata 4.3.2.3

Freeform 72

### Alt/Text Metadata 4.3.2.4

Freeform 73

### Alt/Text Metadata 4.3.2.5

Freeform 74

### Alt/Text Metadata 4.3.2.6

Freeform 75

### Alt/Text Metadata 4.3.2.7

Freeform 76

### Alt/Text Metadata 4.3.2.8

Freeform 77

### Alt/Text Metadata 4.3.2.9

Freeform 78

### Alt/Text Metadata 4.3.2.10

Freeform 79

### Alt/Text Metadata 4.3.2.11

Freeform 80

### Alt/Text Metadata 4.4

Group 81 | Text Box 82 | Group 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87 | Freeform 88 | Freeform 89 | Freeform 90 | Freeform 91 | Freeform 92 | Freeform 93 | Freeform 94

### Alt/Text Metadata 4.4.1

Text Box 82

### Alt/Text Metadata 4.4.2

Group 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87 | Freeform 88 | Freeform 89 | Freeform 90 | Freeform 91 | Freeform 92 | Freeform 93 | Freeform 94

### Alt/Text Metadata 4.4.2.1

Freeform 84

### Alt/Text Metadata 4.4.2.2

Freeform 85

### Alt/Text Metadata 4.4.2.3

Freeform 86

### Alt/Text Metadata 4.4.2.4

Freeform 87

### Alt/Text Metadata 4.4.2.5

Freeform 88

### Alt/Text Metadata 4.4.2.6

Freeform 89

### Alt/Text Metadata 4.4.2.7

Freeform 90

### Alt/Text Metadata 4.4.2.8

Freeform 91

### Alt/Text Metadata 4.4.2.9

Freeform 92

### Alt/Text Metadata 4.4.2.10

Freeform 93

### Alt/Text Metadata 4.4.2.11

Freeform 94

### Alt/Text Metadata 4.5

Group 95 | Text Box 96 | Group 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103 | Freeform 104 | Freeform 105 | Freeform 106 | Freeform 107 | Freeform 108

### Alt/Text Metadata 4.5.1

Text Box 96

### Alt/Text Metadata 4.5.2

Group 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103 | Freeform 104 | Freeform 105 | Freeform 106 | Freeform 107 | Freeform 108

### Alt/Text Metadata 4.5.2.1

Freeform 98

### Alt/Text Metadata 4.5.2.2

Freeform 99

### Alt/Text Metadata 4.5.2.3

Freeform 100

### Alt/Text Metadata 4.5.2.4

Freeform 101

### Alt/Text Metadata 4.5.2.5

Freeform 102

### Alt/Text Metadata 4.5.2.6

Freeform 103

### Alt/Text Metadata 4.5.2.7

Freeform 104

### Alt/Text Metadata 4.5.2.8

Freeform 105

### Alt/Text Metadata 4.5.2.9

Freeform 106

### Alt/Text Metadata 4.5.2.10

Freeform 107

### Alt/Text Metadata 4.5.2.11

Freeform 108

### Alt/Text Metadata 4.6

Group 109 | Text Box 110 | Group 111 | Freeform 112 | Freeform 113 | Freeform 114 | Freeform 115 | Freeform 116 | Freeform 117 | Freeform 118 | Freeform 119 | Freeform 120 | Freeform 121 | Freeform 122

### Alt/Text Metadata 4.6.1

Text Box 110

### Alt/Text Metadata 4.6.2

Group 111 | Freeform 112 | Freeform 113 | Freeform 114 | Freeform 115 | Freeform 116 | Freeform 117 | Freeform 118 | Freeform 119 | Freeform 120 | Freeform 121 | Freeform 122

### Alt/Text Metadata 4.6.2.1

Freeform 112

### Alt/Text Metadata 4.6.2.2

Freeform 113

### Alt/Text Metadata 4.6.2.3

Freeform 114

### Alt/Text Metadata 4.6.2.4

Freeform 115

### Alt/Text Metadata 4.6.2.5

Freeform 116

### Alt/Text Metadata 4.6.2.6

Freeform 117

### Alt/Text Metadata 4.6.2.7

Freeform 118

### Alt/Text Metadata 4.6.2.8

Freeform 119

### Alt/Text Metadata 4.6.2.9

Freeform 120

### Alt/Text Metadata 4.6.2.10

Freeform 121

### Alt/Text Metadata 4.6.2.11

Freeform 122

### Shape 5 Text Box 123

Parallel Kernel (device)
KernelA<<<nBlk, nThr>>>(args);

### Alt/Text Metadata 5

Text Box 123

### Alt/Text Metadata 6

Freeform 124

### Alt/Text Metadata 7

Text Box 125

### Alt/Text Metadata 8

Freeform 126

### Shape 9 Text Box 127

Parallel Kernel (device)
KernelB<<<nBlk, nThr>>>(args);

### Alt/Text Metadata 9

Text Box 127

### Shape 10 Título 134

Warps not Exposed to GPU Programmers

### Alt/Text Metadata 10

Título 134

### Shape 11 Marcador de número de diapositiva 1

103

### Alt/Text Metadata 11

Marcador de número de diapositiva 1

### Shape 12 CuadroTexto 135

Slide credit: Hwu & Kirk

### Alt/Text Metadata 12

CuadroTexto 135

## Slide 104

### Shape 1 Título 1

From Blocks to Warps

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

GPU cores: SIMD pipelines
Streaming Multiprocessors (SM)
Streaming Processors (SP)
Blocks are divided into warps
SIMD unit (32 threads)

### Alt/Text Metadata 2

Marcador de contenido 2

### Alt/Text Metadata 3

Imagen 8 | CUDA_SM2x.eps

### Relationships 3

- rId2: image:../media/image47.emf

### Alt/Text Metadata 4

Rectangle 73

### Shape 5 Rectangle 74

…

### Alt/Text Metadata 5

Rectangle 74

### Alt/Text Metadata 6

Group 75 | Text Box 76 | Freeform 77 | Freeform 78 | Freeform 79 | Freeform 80 | Freeform 81 | Freeform 82 | Freeform 83 | Freeform 84 | Freeform 85 | Freeform 86 | Freeform 87

### Shape 6.1 Text Box 76

t0 t1 t2 … t31

### Alt/Text Metadata 6.1

Text Box 76

### Alt/Text Metadata 6.2

Freeform 77

### Alt/Text Metadata 6.3

Freeform 78

### Alt/Text Metadata 6.4

Freeform 79

### Alt/Text Metadata 6.5

Freeform 80

### Alt/Text Metadata 6.6

Freeform 81

### Alt/Text Metadata 6.7

Freeform 82

### Alt/Text Metadata 6.8

Freeform 83

### Alt/Text Metadata 6.9

Freeform 84

### Alt/Text Metadata 6.10

Freeform 85

### Alt/Text Metadata 6.11

Freeform 86

### Alt/Text Metadata 6.12

Freeform 87

### Alt/Text Metadata 7

Text Box 88

### Alt/Text Metadata 8

Rectangle 89

### Alt/Text Metadata 9

Rectangle 90

### Alt/Text Metadata 10

Group 91 | Text Box 92 | Freeform 93 | Freeform 94 | Freeform 95 | Freeform 96 | Freeform 97 | Freeform 98 | Freeform 99 | Freeform 100 | Freeform 101 | Freeform 102 | Freeform 103

### Alt/Text Metadata 10.1

Text Box 92

### Alt/Text Metadata 10.2

Freeform 93

### Alt/Text Metadata 10.3

Freeform 94

### Alt/Text Metadata 10.4

Freeform 95

### Alt/Text Metadata 10.5

Freeform 96

### Alt/Text Metadata 10.6

Freeform 97

### Alt/Text Metadata 10.7

Freeform 98

### Alt/Text Metadata 10.8

Freeform 99

### Alt/Text Metadata 10.9

Freeform 100

### Alt/Text Metadata 10.10

Freeform 101

### Alt/Text Metadata 10.11

Freeform 102

### Alt/Text Metadata 10.12

Freeform 103

### Alt/Text Metadata 11

Text Box 104

### Shape 12 Text Box 105

Block 0’s warps

### Alt/Text Metadata 12

Text Box 105

### Shape 13 Text Box 106

Block 1’s warps

### Alt/Text Metadata 13

Text Box 106

### Alt/Text Metadata 14

Rectangle 135

### Alt/Text Metadata 15

Rectangle 136

### Alt/Text Metadata 16

Group 137 | Text Box 138 | Freeform 139 | Freeform 140 | Freeform 141 | Freeform 142 | Freeform 143 | Freeform 144 | Freeform 145 | Freeform 146 | Freeform 147 | Freeform 148 | Freeform 149

### Alt/Text Metadata 16.1

Text Box 138

### Alt/Text Metadata 16.2

Freeform 139

### Alt/Text Metadata 16.3

Freeform 140

### Alt/Text Metadata 16.4

Freeform 141

### Alt/Text Metadata 16.5

Freeform 142

### Alt/Text Metadata 16.6

Freeform 143

### Alt/Text Metadata 16.7

Freeform 144

### Alt/Text Metadata 16.8

Freeform 145

### Alt/Text Metadata 16.9

Freeform 146

### Alt/Text Metadata 16.10

Freeform 147

### Alt/Text Metadata 16.11

Freeform 148

### Alt/Text Metadata 16.12

Freeform 149

### Alt/Text Metadata 17

Text Box 150

### Shape 18 Text Box 151

Block 2’s warps

### Alt/Text Metadata 18

Text Box 151

### Shape 19 Marcador de número de diapositiva 3

104

### Alt/Text Metadata 19

Marcador de número de diapositiva 3

### Shape 20 TextBox 4

NVIDIA Fermi architecture

### Alt/Text Metadata 20

TextBox 4

### Slide media/diagram relationships

- rId2: image:../media/image47.emf

## Slide 105

### Shape 1 Title 1

SPMD

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Single procedure/program, multiple data
This is a programming model rather than computer organization
Each processing element executes the same procedure, except on different data elements
Procedures can synchronize at certain points in program, e.g. barriers
Essentially, multiple instruction streams execute the same program
Each program/procedure 1) works on different data, 2) can execute a different control-flow path, at run-time
Many scientific applications are programmed this way and run on MIMD hardware (multiprocessors)
Modern GPUs programmed in a similar way on a SIMD hardware

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

105

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 106

### Shape 1 Title 1

Dynamic Warp Formation/Merging

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Idea: Dynamically merge threads executing the same instruction (after branch divergence)
Form new warps from warps that are waiting
Enough threads branching to each path enables the creation of full new warps

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

106

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 39 | Rectangle 40 | Line 41 | Line 42 | Line 43 | Line 44 | Line 45

### Alt/Text Metadata 4.1

Rectangle 40

### Alt/Text Metadata 4.2

Line 41

### Alt/Text Metadata 4.3

Line 42

### Alt/Text Metadata 4.4

Line 43

### Alt/Text Metadata 4.5

Line 44

### Alt/Text Metadata 4.6

Line 45

### Alt/Text Metadata 5

Group 46 | Rectangle 47 | Line 48 | Line 49 | Line 50 | Line 51

### Alt/Text Metadata 5.1

Rectangle 47

### Alt/Text Metadata 5.2

Line 48

### Alt/Text Metadata 5.3

Line 49

### Alt/Text Metadata 5.4

Line 50

### Alt/Text Metadata 5.5

Line 51

### Alt/Text Metadata 6

Group 113 | Rectangle 62 | Line 56 | Line 57 | Line 58 | Line 63 | Line 64 | Line 65 | Line 66

### Alt/Text Metadata 6.1

Rectangle 62

### Alt/Text Metadata 6.2

Line 56

### Alt/Text Metadata 6.3

Line 57

### Alt/Text Metadata 6.4

Line 58

### Alt/Text Metadata 6.5

Line 63

### Alt/Text Metadata 6.6

Line 64

### Alt/Text Metadata 6.7

Line 65

### Alt/Text Metadata 6.8

Line 66

### Alt/Text Metadata 7

Line 68

### Alt/Text Metadata 8

Group 96 | Rectangle 70 | Line 71 | Line 72 | Line 73

### Alt/Text Metadata 8.1

Rectangle 70

### Alt/Text Metadata 8.2

Line 71

### Alt/Text Metadata 8.3

Line 72

### Alt/Text Metadata 8.4

Line 73

### Alt/Text Metadata 9

Group 76 | Rectangle 77 | Line 78 | Line 79 | Line 80 | Line 81

### Alt/Text Metadata 9.1

Rectangle 77

### Alt/Text Metadata 9.2

Line 78

### Alt/Text Metadata 9.3

Line 79

### Alt/Text Metadata 9.4

Line 80

### Alt/Text Metadata 9.5

Line 81

### Alt/Text Metadata 10

Group 95 | Rectangle 83 | Line 85 | Line 86 | Line 87 | Line 90 | Line 91 | Line 92 | Line 93

### Alt/Text Metadata 10.1

Rectangle 83

### Alt/Text Metadata 10.2

Line 85

### Alt/Text Metadata 10.3

Line 86

### Alt/Text Metadata 10.4

Line 87

### Alt/Text Metadata 10.5

Line 90

### Alt/Text Metadata 10.6

Line 91

### Alt/Text Metadata 10.7

Line 92

### Alt/Text Metadata 10.8

Line 93

### Alt/Text Metadata 11

Line 94

### Alt/Text Metadata 12

Group 104 | Rectangle 98 | Line 99 | Line 100 | Line 101 | Line 102 | Line 103

### Alt/Text Metadata 12.1

Rectangle 98

### Alt/Text Metadata 12.2

Line 99

### Alt/Text Metadata 12.3

Line 100

### Alt/Text Metadata 12.4

Line 101

### Alt/Text Metadata 12.5

Line 102

### Alt/Text Metadata 12.6

Line 103

### Alt/Text Metadata 13

Group 121 | Rectangle 115 | Line 119 | Line 120

### Alt/Text Metadata 13.1

Rectangle 115

### Alt/Text Metadata 13.2

Line 119

### Alt/Text Metadata 13.3

Line 120

### Alt/Text Metadata 14

Group 112 | Rectangle 55 | Line 59 | Line 60 | Line 107 | Line 108 | Line 109 | Line 110 | Line 111

### Alt/Text Metadata 14.1

Rectangle 55

### Alt/Text Metadata 14.2

Line 59

### Alt/Text Metadata 14.3

Line 60

### Alt/Text Metadata 14.4

Line 107

### Alt/Text Metadata 14.5

Line 108

### Alt/Text Metadata 14.6

Line 109

### Alt/Text Metadata 14.7

Line 110

### Alt/Text Metadata 14.8

Line 111

### Shape 15 TextBox 4

Warp X

### Alt/Text Metadata 15

TextBox 4

### Shape 16 TextBox 69

Warp Y

### Alt/Text Metadata 16

TextBox 69

### Shape 17 TextBox 70

Warp Z

### Alt/Text Metadata 17

TextBox 70

## Slide 107

### Shape 1 Title 1

Dynamic Warp Formation/Merging

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

Idea: Dynamically merge threads executing the same instruction (after branch divergence)
Fung et al., “Dynamic Warp Formation and Scheduling for Efficient GPU Control Flow,” MICRO 2007.

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

107

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Alt/Text Metadata 4

Group 157 | Rectangle 78 | Line 79 | Line 80 | Line 82 | Line 154 | Line 155

### Alt/Text Metadata 4.1

Rectangle 78

### Alt/Text Metadata 4.2

Line 79

### Alt/Text Metadata 4.3

Line 80

### Alt/Text Metadata 4.4

Line 82

### Alt/Text Metadata 4.5

Line 154

### Alt/Text Metadata 4.6

Line 155

### Alt/Text Metadata 5

Group 93 | Rectangle 5 | Line 6 | Line 7 | Line 8 | Line 9 | Line 10 | Line 11 | Line 12 | Line 13

### Alt/Text Metadata 5.1

Rectangle 5

### Alt/Text Metadata 5.2

Line 6

### Alt/Text Metadata 5.3

Line 7

### Alt/Text Metadata 5.4

Line 8

### Alt/Text Metadata 5.5

Line 9

### Alt/Text Metadata 5.6

Line 10

### Alt/Text Metadata 5.7

Line 11

### Alt/Text Metadata 5.8

Line 12

### Alt/Text Metadata 5.9

Line 13

### Alt/Text Metadata 6

Group 94 | Rectangle 14 | Line 15 | Line 16 | Line 17 | Line 18 | Line 19 | Line 20 | Line 21 | Line 22

### Alt/Text Metadata 6.1

Rectangle 14

### Alt/Text Metadata 6.2

Line 15

### Alt/Text Metadata 6.3

Line 16

### Alt/Text Metadata 6.4

Line 17

### Alt/Text Metadata 6.5

Line 18

### Alt/Text Metadata 6.6

Line 19

### Alt/Text Metadata 6.7

Line 20

### Alt/Text Metadata 6.8

Line 21

### Alt/Text Metadata 6.9

Line 22

### Alt/Text Metadata 7

Group 95 | Rectangle 55 | Line 56 | Line 57 | Line 58 | Line 59 | Line 60 | Line 61 | Line 62 | Line 63

### Alt/Text Metadata 7.1

Rectangle 55

### Alt/Text Metadata 7.2

Line 56

### Alt/Text Metadata 7.3

Line 57

### Alt/Text Metadata 7.4

Line 58

### Alt/Text Metadata 7.5

Line 59

### Alt/Text Metadata 7.6

Line 60

### Alt/Text Metadata 7.7

Line 61

### Alt/Text Metadata 7.8

Line 62

### Alt/Text Metadata 7.9

Line 63

### Alt/Text Metadata 8

Group 96 | Rectangle 64 | Line 65 | Line 66 | Line 67 | Line 68 | Line 69 | Line 70 | Line 71 | Line 72

### Alt/Text Metadata 8.1

Rectangle 64

### Alt/Text Metadata 8.2

Line 65

### Alt/Text Metadata 8.3

Line 66

### Alt/Text Metadata 8.4

Line 67

### Alt/Text Metadata 8.5

Line 68

### Alt/Text Metadata 8.6

Line 69

### Alt/Text Metadata 8.7

Line 70

### Alt/Text Metadata 8.8

Line 71

### Alt/Text Metadata 8.9

Line 72

### Alt/Text Metadata 9

Group 100 | Rectangle 23 | Line 24 | Line 25 | Line 26 | Line 27

### Alt/Text Metadata 9.1

Rectangle 23

### Alt/Text Metadata 9.2

Line 24

### Alt/Text Metadata 9.3

Line 25

### Alt/Text Metadata 9.4

Line 26

### Alt/Text Metadata 9.5

Line 27

### Alt/Text Metadata 10

Group 128 | Rectangle 129 | Rectangle 130 | Rectangle 131 | Rectangle 132 | Rectangle 133 | AutoShape 134 | AutoShape 135 | AutoShape 136 | AutoShape 137 | AutoShape 138

### Alt/Text Metadata 10.1

Rectangle 129

### Shape 10.2 Rectangle 130

Branch

### Alt/Text Metadata 10.2

Rectangle 130

### Shape 10.3 Rectangle 131

Path A

### Alt/Text Metadata 10.3

Rectangle 131

### Shape 10.4 Rectangle 132

Path B

### Alt/Text Metadata 10.4

Rectangle 132

### Alt/Text Metadata 10.5

Rectangle 133

### Alt/Text Metadata 10.6

AutoShape 134

### Alt/Text Metadata 10.7

AutoShape 135

### Alt/Text Metadata 10.8

AutoShape 136

### Alt/Text Metadata 10.9

AutoShape 137

### Alt/Text Metadata 10.10

AutoShape 138

### Alt/Text Metadata 11

Rectangle 143

### Alt/Text Metadata 12

Rectangle 144

### Alt/Text Metadata 13

Rectangle 145

### Alt/Text Metadata 14

Rectangle 153

### Alt/Text Metadata 15

Rectangle 156

### Alt/Text Metadata 16

Group 159 | Rectangle 160 | Line 161 | Line 162 | Line 163 | Line 164 | Line 165 | Line 166 | Line 167

### Alt/Text Metadata 16.1

Rectangle 160

### Alt/Text Metadata 16.2

Line 161

### Alt/Text Metadata 16.3

Line 162

### Alt/Text Metadata 16.4

Line 163

### Alt/Text Metadata 16.5

Line 164

### Alt/Text Metadata 16.6

Line 165

### Alt/Text Metadata 16.7

Line 166

### Alt/Text Metadata 16.8

Line 167

### Alt/Text Metadata 17

Group 168 | Rectangle 169 | Line 170 | Line 171

### Alt/Text Metadata 17.1

Rectangle 169

### Alt/Text Metadata 17.2

Line 170

### Alt/Text Metadata 17.3

Line 171

### Alt/Text Metadata 18

Line 181

## Slide 108

### Shape 1 Title 1

Dynamic Warp Formation Example

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

108

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Group 586 | Rectangle 12 | Rectangle 14 | Line 15 | Freeform 16 | Line 17 | Freeform 18 | Line 19 | Freeform 20 | Line 21 | Freeform 22

### Alt/Text Metadata 3.1

Rectangle 12

### Shape 3.2 Rectangle 14

A

### Alt/Text Metadata 3.2

Rectangle 14

### Alt/Text Metadata 3.3

Line 15

### Alt/Text Metadata 3.4

Freeform 16

### Alt/Text Metadata 3.5

Line 17

### Alt/Text Metadata 3.6

Freeform 18

### Alt/Text Metadata 3.7

Line 19

### Alt/Text Metadata 3.8

Freeform 20

### Alt/Text Metadata 3.9

Line 21

### Alt/Text Metadata 3.10

Freeform 22

### Alt/Text Metadata 4

Group 587 | Rectangle 23 | Rectangle 25 | Line 26 | Freeform 27 | Line 28 | Freeform 29 | Line 30 | Freeform 31 | Line 32 | Freeform 33

### Alt/Text Metadata 4.1

Rectangle 23

### Alt/Text Metadata 4.2

Rectangle 25

### Alt/Text Metadata 4.3

Line 26

### Alt/Text Metadata 4.4

Freeform 27

### Alt/Text Metadata 4.5

Line 28

### Alt/Text Metadata 4.6

Freeform 29

### Alt/Text Metadata 4.7

Line 30

### Alt/Text Metadata 4.8

Freeform 31

### Alt/Text Metadata 4.9

Line 32

### Alt/Text Metadata 4.10

Freeform 33

### Alt/Text Metadata 5

Group 588 | Rectangle 34 | Rectangle 36 | Line 37 | Freeform 38 | Line 41 | Freeform 42 | Line 43 | Freeform 44

### Alt/Text Metadata 5.1

Rectangle 34

### Shape 5.2 Rectangle 36

B

### Alt/Text Metadata 5.2

Rectangle 36

### Alt/Text Metadata 5.3

Line 37

### Alt/Text Metadata 5.4

Freeform 38

### Alt/Text Metadata 5.5

Line 41

### Alt/Text Metadata 5.6

Freeform 42

### Alt/Text Metadata 5.7

Line 43

### Alt/Text Metadata 5.8

Freeform 44

### Alt/Text Metadata 6

Group 589 | Rectangle 45 | Rectangle 47 | Line 50 | Freeform 51 | Line 54 | Freeform 55

### Alt/Text Metadata 6.1

Rectangle 45

### Alt/Text Metadata 6.2

Rectangle 47

### Alt/Text Metadata 6.3

Line 50

### Alt/Text Metadata 6.4

Freeform 51

### Alt/Text Metadata 6.5

Line 54

### Alt/Text Metadata 6.6

Freeform 55

### Alt/Text Metadata 7

Group 598 | Rectangle 56 | Rectangle 58 | Line 59 | Freeform 60 | Line 61 | Freeform 62 | Line 63 | Freeform 64 | Line 65 | Freeform 66

### Alt/Text Metadata 7.1

Rectangle 56

### Shape 7.2 Rectangle 58

G

### Alt/Text Metadata 7.2

Rectangle 58

### Alt/Text Metadata 7.3

Line 59

### Alt/Text Metadata 7.4

Freeform 60

### Alt/Text Metadata 7.5

Line 61

### Alt/Text Metadata 7.6

Freeform 62

### Alt/Text Metadata 7.7

Line 63

### Alt/Text Metadata 7.8

Freeform 64

### Alt/Text Metadata 7.9

Line 65

### Alt/Text Metadata 7.10

Freeform 66

### Alt/Text Metadata 8

Group 599 | Rectangle 67 | Rectangle 69 | Line 70 | Freeform 71 | Line 72 | Freeform 73 | Line 74 | Freeform 75 | Line 76 | Freeform 77

### Alt/Text Metadata 8.1

Rectangle 67

### Alt/Text Metadata 8.2

Rectangle 69

### Alt/Text Metadata 8.3

Line 70

### Alt/Text Metadata 8.4

Freeform 71

### Alt/Text Metadata 8.5

Line 72

### Alt/Text Metadata 8.6

Freeform 73

### Alt/Text Metadata 8.7

Line 74

### Alt/Text Metadata 8.8

Freeform 75

### Alt/Text Metadata 8.9

Line 76

### Alt/Text Metadata 8.10

Freeform 77

### Alt/Text Metadata 9

Group 600 | Rectangle 78 | Rectangle 80 | Line 81 | Freeform 82 | Line 83 | Freeform 84 | Line 85 | Freeform 86 | Line 87 | Freeform 88

### Alt/Text Metadata 9.1

Rectangle 78

### Alt/Text Metadata 9.2

Rectangle 80

### Alt/Text Metadata 9.3

Line 81

### Alt/Text Metadata 9.4

Freeform 82

### Alt/Text Metadata 9.5

Line 83

### Alt/Text Metadata 9.6

Freeform 84

### Alt/Text Metadata 9.7

Line 85

### Alt/Text Metadata 9.8

Freeform 86

### Alt/Text Metadata 9.9

Line 87

### Alt/Text Metadata 9.10

Freeform 88

### Alt/Text Metadata 10

Group 601 | Rectangle 89 | Rectangle 91 | Line 92 | Freeform 93 | Line 94 | Freeform 95 | Line 96 | Freeform 97 | Line 98 | Freeform 99

### Alt/Text Metadata 10.1

Rectangle 89

### Alt/Text Metadata 10.2

Rectangle 91

### Alt/Text Metadata 10.3

Line 92

### Alt/Text Metadata 10.4

Freeform 93

### Alt/Text Metadata 10.5

Line 94

### Alt/Text Metadata 10.6

Freeform 95

### Alt/Text Metadata 10.7

Line 96

### Alt/Text Metadata 10.8

Freeform 97

### Alt/Text Metadata 10.9

Line 98

### Alt/Text Metadata 10.10

Freeform 99

### Alt/Text Metadata 11

Group 590 | Rectangle 100 | Rectangle 102 | Line 103 | Freeform 104

### Alt/Text Metadata 11.1

Rectangle 100

### Shape 11.2 Rectangle 102

C

### Alt/Text Metadata 11.2

Rectangle 102

### Alt/Text Metadata 11.3

Line 103

### Alt/Text Metadata 11.4

Freeform 104

### Alt/Text Metadata 12

Group 591 | Rectangle 111 | Rectangle 113 | Line 120 | Freeform 121

### Alt/Text Metadata 12.1

Rectangle 111

### Alt/Text Metadata 12.2

Rectangle 113

### Alt/Text Metadata 12.3

Line 120

### Alt/Text Metadata 12.4

Freeform 121

### Alt/Text Metadata 13

Group 592 | Rectangle 122 | Rectangle 124 | Line 129 | Freeform 130 | Line 131 | Freeform 132

### Alt/Text Metadata 13.1

Rectangle 122

### Shape 13.2 Rectangle 124

D

### Alt/Text Metadata 13.2

Rectangle 124

### Alt/Text Metadata 13.3

Line 129

### Alt/Text Metadata 13.4

Freeform 130

### Alt/Text Metadata 13.5

Line 131

### Alt/Text Metadata 13.6

Freeform 132

### Alt/Text Metadata 14

Group 593 | Rectangle 133 | Rectangle 135 | Line 138 | Freeform 139

### Alt/Text Metadata 14.1

Rectangle 133

### Alt/Text Metadata 14.2

Rectangle 135

### Alt/Text Metadata 14.3

Line 138

### Alt/Text Metadata 14.4

Freeform 139

### Alt/Text Metadata 15

Group 594 | Rectangle 144 | Rectangle 146 | Line 147 | Freeform 148 | Line 151 | Freeform 152 | Line 153 | Freeform 154

### Alt/Text Metadata 15.1

Rectangle 144

### Shape 15.2 Rectangle 146

E

### Alt/Text Metadata 15.2

Rectangle 146

### Alt/Text Metadata 15.3

Line 147

### Alt/Text Metadata 15.4

Freeform 148

### Alt/Text Metadata 15.5

Line 151

### Alt/Text Metadata 15.6

Freeform 152

### Alt/Text Metadata 15.7

Line 153

### Alt/Text Metadata 15.8

Freeform 154

### Alt/Text Metadata 16

Group 595 | Rectangle 155 | Rectangle 157 | Line 160 | Freeform 161 | Line 164 | Freeform 165

### Alt/Text Metadata 16.1

Rectangle 155

### Alt/Text Metadata 16.2

Rectangle 157

### Alt/Text Metadata 16.3

Line 160

### Alt/Text Metadata 16.4

Freeform 161

### Alt/Text Metadata 16.5

Line 164

### Alt/Text Metadata 16.6

Freeform 165

### Alt/Text Metadata 17

Group 596 | Rectangle 166 | Rectangle 168 | Line 171 | Freeform 172

### Alt/Text Metadata 17.1

Rectangle 166

### Shape 17.2 Rectangle 168

F

### Alt/Text Metadata 17.2

Rectangle 168

### Alt/Text Metadata 17.3

Line 171

### Alt/Text Metadata 17.4

Freeform 172

### Alt/Text Metadata 18

Group 597 | Rectangle 177 | Rectangle 179 | Line 180 | Freeform 181 | Line 184 | Freeform 185

### Alt/Text Metadata 18.1

Rectangle 177

### Alt/Text Metadata 18.2

Rectangle 179

### Alt/Text Metadata 18.3

Line 180

### Alt/Text Metadata 18.4

Freeform 181

### Alt/Text Metadata 18.5

Line 184

### Alt/Text Metadata 18.6

Freeform 185

### Alt/Text Metadata 19

Freeform 188

### Alt/Text Metadata 20

Freeform 189

### Alt/Text Metadata 21

Freeform 190

### Alt/Text Metadata 22

Freeform 191

### Shape 23 Rectangle 192

Time

### Alt/Text Metadata 23

Rectangle 192

### Alt/Text Metadata 24

Group 602 | Rectangle 211 | Rectangle 213 | Line 214 | Freeform 215 | Line 216 | Freeform 217 | Line 218 | Freeform 219 | Line 220 | Freeform 221

### Alt/Text Metadata 24.1

Rectangle 211

### Alt/Text Metadata 24.2

Rectangle 213

### Alt/Text Metadata 24.3

Line 214

### Alt/Text Metadata 24.4

Freeform 215

### Alt/Text Metadata 24.5

Line 216

### Alt/Text Metadata 24.6

Freeform 217

### Alt/Text Metadata 24.7

Line 218

### Alt/Text Metadata 24.8

Freeform 219

### Alt/Text Metadata 24.9

Line 220

### Alt/Text Metadata 24.10

Freeform 221

### Alt/Text Metadata 25

Group 603 | Rectangle 222 | Rectangle 224 | Line 225 | Freeform 226 | Line 227 | Freeform 228 | Line 229 | Freeform 230 | Line 231 | Freeform 232

### Alt/Text Metadata 25.1

Rectangle 222

### Alt/Text Metadata 25.2

Rectangle 224

### Alt/Text Metadata 25.3

Line 225

### Alt/Text Metadata 25.4

Freeform 226

### Alt/Text Metadata 25.5

Line 227

### Alt/Text Metadata 25.6

Freeform 228

### Alt/Text Metadata 25.7

Line 229

### Alt/Text Metadata 25.8

Freeform 230

### Alt/Text Metadata 25.9

Line 231

### Alt/Text Metadata 25.10

Freeform 232

### Alt/Text Metadata 26

Group 643 | Rectangle 233 | Rectangle 235 | Line 236 | Freeform 237 | Line 240 | Freeform 241 | Line 242 | Freeform 243 | Line 249 | Freeform 250

### Alt/Text Metadata 26.1

Rectangle 233

### Alt/Text Metadata 26.2

Rectangle 235

### Alt/Text Metadata 26.3

Line 236

### Alt/Text Metadata 26.4

Freeform 237

### Alt/Text Metadata 26.5

Line 240

### Alt/Text Metadata 26.6

Freeform 241

### Alt/Text Metadata 26.7

Line 242

### Alt/Text Metadata 26.8

Freeform 243

### Alt/Text Metadata 26.9

Line 249

### Alt/Text Metadata 26.10

Freeform 250

### Alt/Text Metadata 27

Group 644 | Rectangle 244 | Rectangle 246 | Line 253 | Freeform 254

### Alt/Text Metadata 27.1

Rectangle 244

### Alt/Text Metadata 27.2

Rectangle 246

### Alt/Text Metadata 27.3

Line 253

### Alt/Text Metadata 27.4

Freeform 254

### Alt/Text Metadata 28

Group 611 | Rectangle 255 | Rectangle 257 | Line 258 | Freeform 259 | Line 260 | Freeform 261 | Line 262 | Freeform 263 | Line 264 | Freeform 265

### Alt/Text Metadata 28.1

Rectangle 255

### Alt/Text Metadata 28.2

Rectangle 257

### Alt/Text Metadata 28.3

Line 258

### Alt/Text Metadata 28.4

Freeform 259

### Alt/Text Metadata 28.5

Line 260

### Alt/Text Metadata 28.6

Freeform 261

### Alt/Text Metadata 28.7

Line 262

### Alt/Text Metadata 28.8

Freeform 263

### Alt/Text Metadata 28.9

Line 264

### Alt/Text Metadata 28.10

Freeform 265

### Alt/Text Metadata 29

Group 612 | Rectangle 266 | Rectangle 268 | Line 269 | Freeform 270 | Line 271 | Freeform 272 | Line 273 | Freeform 274 | Line 275 | Freeform 276

### Alt/Text Metadata 29.1

Rectangle 266

### Alt/Text Metadata 29.2

Rectangle 268

### Alt/Text Metadata 29.3

Line 269

### Alt/Text Metadata 29.4

Freeform 270

### Alt/Text Metadata 29.5

Line 271

### Alt/Text Metadata 29.6

Freeform 272

### Alt/Text Metadata 29.7

Line 273

### Alt/Text Metadata 29.8

Freeform 274

### Alt/Text Metadata 29.9

Line 275

### Alt/Text Metadata 29.10

Freeform 276

### Alt/Text Metadata 30

Group 613 | Rectangle 277 | Rectangle 279 | Line 280 | Freeform 281 | Line 282 | Freeform 283 | Line 284 | Freeform 285 | Line 286 | Freeform 287

### Alt/Text Metadata 30.1

Rectangle 277

### Alt/Text Metadata 30.2

Rectangle 279

### Alt/Text Metadata 30.3

Line 280

### Alt/Text Metadata 30.4

Freeform 281

### Alt/Text Metadata 30.5

Line 282

### Alt/Text Metadata 30.6

Freeform 283

### Alt/Text Metadata 30.7

Line 284

### Alt/Text Metadata 30.8

Freeform 285

### Alt/Text Metadata 30.9

Line 286

### Alt/Text Metadata 30.10

Freeform 287

### Alt/Text Metadata 31

Group 614 | Rectangle 288 | Rectangle 290 | Line 291 | Freeform 292 | Line 293 | Freeform 294 | Line 295 | Freeform 296 | Line 297 | Freeform 298

### Alt/Text Metadata 31.1

Rectangle 288

### Alt/Text Metadata 31.2

Rectangle 290

### Alt/Text Metadata 31.3

Line 291

### Alt/Text Metadata 31.4

Freeform 292

### Alt/Text Metadata 31.5

Line 293

### Alt/Text Metadata 31.6

Freeform 294

### Alt/Text Metadata 31.7

Line 295

### Alt/Text Metadata 31.8

Freeform 296

### Alt/Text Metadata 31.9

Line 297

### Alt/Text Metadata 31.10

Freeform 298

### Alt/Text Metadata 32

Group 606 | Rectangle 299 | Rectangle 301 | Line 302 | Freeform 303 | Line 308 | Freeform 309

### Alt/Text Metadata 32.1

Rectangle 299

### Alt/Text Metadata 32.2

Rectangle 301

### Alt/Text Metadata 32.3

Line 302

### Alt/Text Metadata 32.4

Freeform 303

### Alt/Text Metadata 32.5

Line 308

### Alt/Text Metadata 32.6

Freeform 309

### Alt/Text Metadata 33

Group 607 | Rectangle 310 | Rectangle 312 | Line 315 | Freeform 316 | Line 317 | Freeform 318 | Line 319 | Freeform 320

### Alt/Text Metadata 33.1

Rectangle 310

### Alt/Text Metadata 33.2

Rectangle 312

### Alt/Text Metadata 33.3

Line 315

### Alt/Text Metadata 33.4

Freeform 316

### Alt/Text Metadata 33.5

Line 317

### Alt/Text Metadata 33.6

Freeform 318

### Alt/Text Metadata 33.7

Line 319

### Alt/Text Metadata 33.8

Freeform 320

### Alt/Text Metadata 34

Group 646 | Rectangle 321 | Rectangle 323 | Line 324 | Freeform 325 | Line 328 | Freeform 329 | Line 330 | Freeform 331 | Line 337 | Freeform 338

### Alt/Text Metadata 34.1

Rectangle 321

### Alt/Text Metadata 34.2

Rectangle 323

### Alt/Text Metadata 34.3

Line 324

### Alt/Text Metadata 34.4

Freeform 325

### Alt/Text Metadata 34.5

Line 328

### Alt/Text Metadata 34.6

Freeform 329

### Alt/Text Metadata 34.7

Line 330

### Alt/Text Metadata 34.8

Freeform 331

### Alt/Text Metadata 34.9

Line 337

### Alt/Text Metadata 34.10

Freeform 338

### Alt/Text Metadata 35

Group 645 | Rectangle 332 | Rectangle 334 | Line 341 | Freeform 342

### Alt/Text Metadata 35.1

Rectangle 332

### Alt/Text Metadata 35.2

Rectangle 334

### Alt/Text Metadata 35.3

Line 341

### Alt/Text Metadata 35.4

Freeform 342

### Alt/Text Metadata 36

Group 610 | Rectangle 343 | Rectangle 345 | Line 346 | Freeform 347 | Line 348 | Freeform 349 | Line 350 | Freeform 351

### Alt/Text Metadata 36.1

Rectangle 343

### Alt/Text Metadata 36.2

Rectangle 345

### Alt/Text Metadata 36.3

Line 346

### Alt/Text Metadata 36.4

Freeform 347

### Alt/Text Metadata 36.5

Line 348

### Alt/Text Metadata 36.6

Freeform 349

### Alt/Text Metadata 36.7

Line 350

### Alt/Text Metadata 36.8

Freeform 351

### Alt/Text Metadata 37

Freeform 354

### Alt/Text Metadata 38

Freeform 355

### Alt/Text Metadata 39

Freeform 356

### Alt/Text Metadata 40

Freeform 357

### Alt/Text Metadata 41

Rectangle 358

### Alt/Text Metadata 42

AutoShape 488

### Alt/Text Metadata 43

AutoShape 489

### Alt/Text Metadata 44

AutoShape 490

### Alt/Text Metadata 45

AutoShape 491

### Alt/Text Metadata 46

AutoShape 492

### Alt/Text Metadata 47

AutoShape 493

### Alt/Text Metadata 48

AutoShape 494

### Alt/Text Metadata 49

AutoShape 495

### Alt/Text Metadata 50

AutoShape 496

### Alt/Text Metadata 51

Rectangle 486

### Shape 52 Text Box 556

x/1111

### Alt/Text Metadata 52

Text Box 556

### Shape 53 Text Box 558

y/1111

### Alt/Text Metadata 53

Text Box 558

### Alt/Text Metadata 54

Rectangle 563

### Shape 55 Text Box 564

x/1110

### Alt/Text Metadata 55

Text Box 564

### Shape 56 Text Box 565

y/0011

### Alt/Text Metadata 56

Text Box 565

### Alt/Text Metadata 57

Rectangle 567

### Shape 58 Text Box 568

x/1000

### Alt/Text Metadata 58

Text Box 568

### Shape 59 Text Box 569

y/0010

### Alt/Text Metadata 59

Text Box 569

### Alt/Text Metadata 60

Rectangle 571

### Shape 61 Text Box 572

x/0110

### Alt/Text Metadata 61

Text Box 572

### Shape 62 Text Box 573

y/0001

### Alt/Text Metadata 62

Text Box 573

### Alt/Text Metadata 63

Rectangle 575

### Shape 64 Text Box 576

x/0001

### Alt/Text Metadata 64

Text Box 576

### Shape 65 Text Box 577

y/1100

### Alt/Text Metadata 65

Text Box 577

### Alt/Text Metadata 66

Rectangle 579

### Alt/Text Metadata 67

Text Box 580

### Alt/Text Metadata 68

Text Box 581

### Alt/Text Metadata 69

Rectangle 583

### Alt/Text Metadata 70

Text Box 584

### Alt/Text Metadata 71

Text Box 585

### Alt/Text Metadata 72

Group 648 | Rectangle 400 | Group 647 | Rectangle 412 | Rectangle 413 | Rectangle 414 | Line 417 | Freeform 418 | Line 419 | Freeform 420 | Line 421 | Freeform 422

### Shape 72.1 Rectangle 400

A new warp created from scalar threads of both Warp x and y executing at Basic Block D

### Alt/Text Metadata 72.1

Rectangle 400

### Alt/Text Metadata 72.2

Group 647 | Rectangle 412 | Rectangle 413 | Rectangle 414 | Line 417 | Freeform 418 | Line 419 | Freeform 420 | Line 421 | Freeform 422

### Alt/Text Metadata 72.2.1

Rectangle 412

### Alt/Text Metadata 72.2.2

Rectangle 413

### Alt/Text Metadata 72.2.3

Rectangle 414

### Alt/Text Metadata 72.2.4

Line 417

### Alt/Text Metadata 72.2.5

Freeform 418

### Alt/Text Metadata 72.2.6

Line 419

### Alt/Text Metadata 72.2.7

Freeform 420

### Alt/Text Metadata 72.2.8

Line 421

### Alt/Text Metadata 72.2.9

Freeform 422

### Alt/Text Metadata 73

Group 650 | Rectangle 409 | Group 649 | Rectangle 396 | Rectangle 397 | Rectangle 398 | Rectangle 399 | Line 410 | Rectangle 411 | Group 619 | Rectangle 620 | Rectangle 621 | Line 622 | Freeform 623 | Line 624 | Freeform 625 | Line 626 | Freeform 627 | Line 628 | Freeform 629 | Group 630 | Rectangle 631 | Rectangle 632 | Line 633 | Freeform 634 | Line 635 | Freeform 636 | Line 637 | Freeform 638 | Line 639 | Freeform 640

### Alt/Text Metadata 73.1

Rectangle 409

### Alt/Text Metadata 73.2

Group 649 | Rectangle 396 | Rectangle 397 | Rectangle 398 | Rectangle 399 | Line 410 | Rectangle 411 | Group 619 | Rectangle 620 | Rectangle 621 | Line 622 | Freeform 623 | Line 624 | Freeform 625 | Line 626 | Freeform 627 | Line 628 | Freeform 629 | Group 630 | Rectangle 631 | Rectangle 632 | Line 633 | Freeform 634 | Line 635 | Freeform 636 | Line 637 | Freeform 638 | Line 639 | Freeform 640

### Shape 73.2.1 Rectangle 396

Execution of Warp x

### Alt/Text Metadata 73.2.1

Rectangle 396

### Shape 73.2.2 Rectangle 397

at Basic Block A

### Alt/Text Metadata 73.2.2

Rectangle 397

### Shape 73.2.3 Rectangle 398

Execution of Warp y

### Alt/Text Metadata 73.2.3

Rectangle 398

### Alt/Text Metadata 73.2.4

Rectangle 399

### Alt/Text Metadata 73.2.5

Line 410

### Shape 73.2.6 Rectangle 411

Legend

### Alt/Text Metadata 73.2.6

Rectangle 411

### Alt/Text Metadata 73.2.7

Group 619 | Rectangle 620 | Rectangle 621 | Line 622 | Freeform 623 | Line 624 | Freeform 625 | Line 626 | Freeform 627 | Line 628 | Freeform 629

### Alt/Text Metadata 73.2.7.1

Rectangle 620

### Alt/Text Metadata 73.2.7.2

Rectangle 621

### Alt/Text Metadata 73.2.7.3

Line 622

### Alt/Text Metadata 73.2.7.4

Freeform 623

### Alt/Text Metadata 73.2.7.5

Line 624

### Alt/Text Metadata 73.2.7.6

Freeform 625

### Alt/Text Metadata 73.2.7.7

Line 626

### Alt/Text Metadata 73.2.7.8

Freeform 627

### Alt/Text Metadata 73.2.7.9

Line 628

### Alt/Text Metadata 73.2.7.10

Freeform 629

### Alt/Text Metadata 73.2.8

Group 630 | Rectangle 631 | Rectangle 632 | Line 633 | Freeform 634 | Line 635 | Freeform 636 | Line 637 | Freeform 638 | Line 639 | Freeform 640

### Alt/Text Metadata 73.2.8.1

Rectangle 631

### Alt/Text Metadata 73.2.8.2

Rectangle 632

### Alt/Text Metadata 73.2.8.3

Line 633

### Alt/Text Metadata 73.2.8.4

Freeform 634

### Alt/Text Metadata 73.2.8.5

Line 635

### Alt/Text Metadata 73.2.8.6

Freeform 636

### Alt/Text Metadata 73.2.8.7

Line 637

### Alt/Text Metadata 73.2.8.8

Freeform 638

### Alt/Text Metadata 73.2.8.9

Line 639

### Alt/Text Metadata 73.2.8.10

Freeform 640

### Alt/Text Metadata 74

Line 651

### Alt/Text Metadata 75

Group 663 | Rectangle 616 | Rectangle 652 | Line 659

### Alt/Text Metadata 75.1

Rectangle 616

### Alt/Text Metadata 75.2

Rectangle 652

### Alt/Text Metadata 75.3

Line 659

### Alt/Text Metadata 76

Group 664 | Rectangle 617 | Rectangle 656 | Line 660

### Alt/Text Metadata 76.1

Rectangle 617

### Alt/Text Metadata 76.2

Rectangle 656

### Alt/Text Metadata 76.3

Line 660

### Alt/Text Metadata 77

Group 665 | Rectangle 618 | Rectangle 661 | Line 662

### Alt/Text Metadata 77.1

Rectangle 618

### Alt/Text Metadata 77.2

Rectangle 661

### Alt/Text Metadata 77.3

Line 662

### Shape 78 Text Box 666

Baseline

### Alt/Text Metadata 78

Text Box 666

### Shape 79 Text Box 667

Dynamic
Warp
Formation

### Alt/Text Metadata 79

Text Box 667

### Shape 80 TextBox 357

Slide credit: Tor Aamodt

### Alt/Text Metadata 80

TextBox 357

## Slide 109

### Shape 1 Title 1

Hardware Constraints Limit Flexibility of Warp Grouping

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

109

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Alt/Text Metadata 3

Freeform 3

### Alt/Text Metadata 4

Group 4 | Rectangle 5 | Freeform 6 | Line 7

### Alt/Text Metadata 4.1

Rectangle 5

### Alt/Text Metadata 4.2

Freeform 6

### Alt/Text Metadata 4.3

Line 7

### Alt/Text Metadata 5

Group 8 | Rectangle 9 | Freeform 10 | Line 11

### Alt/Text Metadata 5.1

Rectangle 9

### Alt/Text Metadata 5.2

Freeform 10

### Alt/Text Metadata 5.3

Line 11

### Alt/Text Metadata 6

Group 12 | Rectangle 13 | Freeform 14 | Line 15

### Alt/Text Metadata 6.1

Rectangle 13

### Alt/Text Metadata 6.2

Freeform 14

### Alt/Text Metadata 6.3

Line 15

### Alt/Text Metadata 7

Line 16

### Alt/Text Metadata 8

Line 17

### Alt/Text Metadata 9

Freeform 18

### Alt/Text Metadata 10

Group 19 | Rectangle 20 | Freeform 21 | Line 22

### Alt/Text Metadata 10.1

Rectangle 20

### Alt/Text Metadata 10.2

Freeform 21

### Alt/Text Metadata 10.3

Line 22

### Alt/Text Metadata 11

Group 23 | Rectangle 24 | Freeform 25 | Line 26

### Alt/Text Metadata 11.1

Rectangle 24

### Alt/Text Metadata 11.2

Freeform 25

### Alt/Text Metadata 11.3

Line 26

### Alt/Text Metadata 12

Group 27 | Rectangle 28 | Freeform 29 | Line 30

### Alt/Text Metadata 12.1

Rectangle 28

### Alt/Text Metadata 12.2

Freeform 29

### Alt/Text Metadata 12.3

Line 30

### Alt/Text Metadata 13

Line 31

### Alt/Text Metadata 14

Line 32

### Alt/Text Metadata 15

Rectangle 33

### Alt/Text Metadata 16

Freeform 34

### Alt/Text Metadata 17

Freeform 35

### Alt/Text Metadata 18

Line 36

### Alt/Text Metadata 19

Line 37

### Alt/Text Metadata 20

Freeform 38

### Alt/Text Metadata 21

Group 39 | Rectangle 40 | Freeform 41 | Line 42

### Alt/Text Metadata 21.1

Rectangle 40

### Alt/Text Metadata 21.2

Freeform 41

### Alt/Text Metadata 21.3

Line 42

### Alt/Text Metadata 22

Group 43 | Rectangle 44 | Freeform 45 | Line 46

### Alt/Text Metadata 22.1

Rectangle 44

### Alt/Text Metadata 22.2

Freeform 45

### Alt/Text Metadata 22.3

Line 46

### Alt/Text Metadata 23

Group 47 | Rectangle 48 | Freeform 49 | Line 50

### Alt/Text Metadata 23.1

Rectangle 48

### Alt/Text Metadata 23.2

Freeform 49

### Alt/Text Metadata 23.3

Line 50

### Alt/Text Metadata 24

Line 51

### Alt/Text Metadata 25

Line 52

### Alt/Text Metadata 26

Freeform 53

### Alt/Text Metadata 27

Group 54 | Rectangle 55 | Freeform 56 | Line 57

### Alt/Text Metadata 27.1

Rectangle 55

### Alt/Text Metadata 27.2

Freeform 56

### Alt/Text Metadata 27.3

Line 57

### Alt/Text Metadata 28

Group 58 | Rectangle 59 | Freeform 60 | Line 61

### Alt/Text Metadata 28.1

Rectangle 59

### Alt/Text Metadata 28.2

Freeform 60

### Alt/Text Metadata 28.3

Line 61

### Alt/Text Metadata 29

Group 62 | Rectangle 63 | Freeform 64 | Line 65

### Alt/Text Metadata 29.1

Rectangle 63

### Alt/Text Metadata 29.2

Freeform 64

### Alt/Text Metadata 29.3

Line 65

### Alt/Text Metadata 30

Line 66

### Alt/Text Metadata 31

Line 67

### Alt/Text Metadata 32

Rectangle 68

### Alt/Text Metadata 33

Freeform 69

### Alt/Text Metadata 34

Freeform 70

### Alt/Text Metadata 35

Line 71

### Alt/Text Metadata 36

Line 72

### Alt/Text Metadata 37

Freeform 73

### Alt/Text Metadata 38

Group 74 | Rectangle 75 | Freeform 76 | Line 77

### Alt/Text Metadata 38.1

Rectangle 75

### Alt/Text Metadata 38.2

Freeform 76

### Alt/Text Metadata 38.3

Line 77

### Alt/Text Metadata 39

Group 78 | Rectangle 79 | Freeform 80 | Line 81

### Alt/Text Metadata 39.1

Rectangle 79

### Alt/Text Metadata 39.2

Freeform 80

### Alt/Text Metadata 39.3

Line 81

### Alt/Text Metadata 40

Group 82 | Rectangle 83 | Freeform 84 | Line 85

### Alt/Text Metadata 40.1

Rectangle 83

### Alt/Text Metadata 40.2

Freeform 84

### Alt/Text Metadata 40.3

Line 85

### Alt/Text Metadata 41

Line 86

### Alt/Text Metadata 42

Line 87

### Alt/Text Metadata 43

Freeform 88

### Alt/Text Metadata 44

Group 89 | Rectangle 90 | Freeform 91 | Line 92

### Alt/Text Metadata 44.1

Rectangle 90

### Alt/Text Metadata 44.2

Freeform 91

### Alt/Text Metadata 44.3

Line 92

### Alt/Text Metadata 45

Group 93 | Rectangle 94 | Freeform 95 | Line 96

### Alt/Text Metadata 45.1

Rectangle 94

### Alt/Text Metadata 45.2

Freeform 95

### Alt/Text Metadata 45.3

Line 96

### Alt/Text Metadata 46

Group 97 | Rectangle 98 | Freeform 99 | Line 100

### Alt/Text Metadata 46.1

Rectangle 98

### Alt/Text Metadata 46.2

Freeform 99

### Alt/Text Metadata 46.3

Line 100

### Alt/Text Metadata 47

Line 101

### Alt/Text Metadata 48

Line 102

### Alt/Text Metadata 49

Rectangle 103

### Alt/Text Metadata 50

Freeform 104

### Alt/Text Metadata 51

Freeform 105

### Alt/Text Metadata 52

Line 106

### Alt/Text Metadata 53

Line 107

### Alt/Text Metadata 54

Freeform 108

### Alt/Text Metadata 55

Group 109 | Rectangle 110 | Freeform 111 | Line 112

### Alt/Text Metadata 55.1

Rectangle 110

### Alt/Text Metadata 55.2

Freeform 111

### Alt/Text Metadata 55.3

Line 112

### Alt/Text Metadata 56

Group 113 | Rectangle 114 | Freeform 115 | Line 116

### Alt/Text Metadata 56.1

Rectangle 114

### Alt/Text Metadata 56.2

Freeform 115

### Alt/Text Metadata 56.3

Line 116

### Alt/Text Metadata 57

Group 117 | Rectangle 118 | Freeform 119 | Line 120

### Alt/Text Metadata 57.1

Rectangle 118

### Alt/Text Metadata 57.2

Freeform 119

### Alt/Text Metadata 57.3

Line 120

### Alt/Text Metadata 58

Line 121

### Alt/Text Metadata 59

Line 122

### Alt/Text Metadata 60

Freeform 123

### Alt/Text Metadata 61

Group 124 | Rectangle 125 | Freeform 126 | Line 127

### Alt/Text Metadata 61.1

Rectangle 125

### Alt/Text Metadata 61.2

Freeform 126

### Alt/Text Metadata 61.3

Line 127

### Alt/Text Metadata 62

Group 128 | Rectangle 129 | Freeform 130 | Line 131

### Alt/Text Metadata 62.1

Rectangle 129

### Alt/Text Metadata 62.2

Freeform 130

### Alt/Text Metadata 62.3

Line 131

### Alt/Text Metadata 63

Group 132 | Rectangle 133 | Freeform 134 | Line 135

### Alt/Text Metadata 63.1

Rectangle 133

### Alt/Text Metadata 63.2

Freeform 134

### Alt/Text Metadata 63.3

Line 135

### Alt/Text Metadata 64

Line 136

### Alt/Text Metadata 65

Line 137

### Alt/Text Metadata 66

Rectangle 138

### Alt/Text Metadata 67

Freeform 139

### Alt/Text Metadata 68

Freeform 140

### Alt/Text Metadata 69

Line 141

### Alt/Text Metadata 70

Line 142

### Alt/Text Metadata 71

Group 143 | AutoShape 144 | Line 145 | Text Box 146

### Alt/Text Metadata 71.1

AutoShape 144

### Alt/Text Metadata 71.2

Line 145

### Shape 71.3 Text Box 146

Lane

### Alt/Text Metadata 71.3

Text Box 146

### Alt/Text Metadata 72

Group 147 | AutoShape 148 | Line 149 | Text Box 150

### Alt/Text Metadata 72.1

AutoShape 148

### Alt/Text Metadata 72.2

Line 149

### Shape 72.3 Text Box 150

Functional Unit

### Alt/Text Metadata 72.3

Text Box 150

### Shape 73 Text Box 151

Registers
for each
Thread

### Alt/Text Metadata 73

Text Box 151

### Alt/Text Metadata 74

Line 152

### Shape 75 Rectangle 153

Memory Subsystem

### Alt/Text Metadata 75

Rectangle 153

### Shape 76 Text Box 154

Registers for thread IDs
0, 4, 8, …

### Alt/Text Metadata 76

Text Box 154

### Shape 77 Text Box 155

Registers for thread IDs
1, 5, 9, …

### Alt/Text Metadata 77

Text Box 155

### Shape 78 Text Box 156

Registers for thread IDs
2, 6, 10, …

### Alt/Text Metadata 78

Text Box 156

### Shape 79 Text Box 157

Registers for thread IDs
3, 7, 11, …

### Alt/Text Metadata 79

Text Box 157

### Shape 80 TextBox 161

Slide credit: Krste Asanovic

### Alt/Text Metadata 80

TextBox 161

## Slide 110

### Shape 1 Title 1

Clarification of Some GPU Terms

### Alt/Text Metadata 1

Title 1

### Shape 2 Slide Number Placeholder 3

110

### Alt/Text Metadata 2

Slide Number Placeholder 3

### Table 3 Table 3

- Generic Term | NVIDIA Term | AMD Term | Comments
- Vector length | Warp size | Wavefront size | Number of threads that run in parallel (lock-step) on a SIMD functional unit
- Pipelined functional unit / / Scalar pipeline | Streaming processor / / CUDA core | - | Functional unit that executes instructions for one GPU thread
- SIMD functional unit / / SIMD pipeline | Group of N streaming processors (e.g., N=8 in GTX 285, N=16 in Fermi) | Vector ALU | SIMD functional unit that executes instructions for an entire warp
- GPU core | Streaming multiprocessor | Compute unit | It contains one or more warp schedulers and one or several SIMD pipelines

### Alt/Text Metadata 3

Table 3

### XML fallback texts

- Generic Term
- NVIDIA Term
- AMD Term
- Comments
- Vector length
- Warp size
- Wavefront
- size
- Number of threads that run in parallel (lock-step) on a SIMD functional unit
- Pipelined functional unit /
- Scalar pipeline
- Streaming processor /
- CUDA core
- -
- Functional unit that executes instructions for one GPU thread
- SIMD functional unit /
- SIMD pipeline
- Group of N streaming processors (e.g., N=8 in GTX 285, N=16 in Fermi)
- Vector ALU
- SIMD functional unit that executes instructions for an entire warp
- GPU core
- Streaming multiprocessor
- Compute unit
- It contains one or more warp schedulers and one or several SIMD pipelines

## Slide 111

### Alt/Text Metadata 1

矩形 9

### Shape 2 Title 1

Programming Model vs. Hardware Execution Model

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

111

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 矩形 1

Hardware Programming Model

### Alt/Text Metadata 4

矩形 1

### Shape 5 矩形 3

Programming Model

### Alt/Text Metadata 5

矩形 3

### Shape 6 矩形: 圆角 4

Core

### Alt/Text Metadata 6

矩形: 圆角 4

### Alt/Text Metadata 7

矩形: 圆角 8

### Shape 8 矩形 5

Streaming
 Multi-processor

### Alt/Text Metadata 8

矩形 5

### Shape 9 矩形 6

GPU

### Alt/Text Metadata 9

矩形 6

### Alt/Text Metadata 10

矩形: 圆角 11

### Alt/Text Metadata 11

矩形: 圆角 13

### Alt/Text Metadata 12

矩形: 圆角 14

### Alt/Text Metadata 13

矩形: 圆角 15

### Alt/Text Metadata 14

矩形: 圆角 16

### Alt/Text Metadata 15

矩形: 圆角 17

### Alt/Text Metadata 16

矩形: 圆角 18

### Alt/Text Metadata 17

矩形: 圆角 19

### Alt/Text Metadata 18

矩形 21

### Alt/Text Metadata 19

矩形 22

### Alt/Text Metadata 20

矩形 23

### Alt/Text Metadata 21

矩形 24

### Shape 22 矩形 25

CUDA core:

### Alt/Text Metadata 22

矩形 25

### Shape 23 矩形 28

Thread

### Alt/Text Metadata 23

矩形 28

### Shape 24 矩形 29

Thread block (s)

### Alt/Text Metadata 24

矩形 29

### Shape 25 矩形 32

Wrap

### Alt/Text Metadata 25

矩形 32

### Shape 26 矩形 33

Thread blocks

### Alt/Text Metadata 26

矩形 33

## Slide 112

### Shape 1 Title 1

NVIDIA H100 Block Diagram

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

144 cores on the full GH100
60MB L2 cache

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 TextBox 2

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

### Alt/Text Metadata 3

TextBox 2

### Shape 4 Slide Number Placeholder 3

112

### Alt/Text Metadata 4

Slide Number Placeholder 3

### Alt/Text Metadata 5

Picture 3

### Relationships 5

- rId4: image:../media/image49.png

### Slide media/diagram relationships

- rId4: image:../media/image49.png

## Slide 113

### Shape 1 Title 1

NVIDIA H100 Core

### Alt/Text Metadata 1

Title 1

### Shape 2 Content Placeholder 2

48 TFLOPS Single Precision*
24 TFLOPS Double Precision*
800 TFLOPS (FP16, Tensor Cores)*

### Alt/Text Metadata 2

Content Placeholder 2

### Shape 3 Slide Number Placeholder 3

113

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 10

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
* Preliminary performance estimates

### Alt/Text Metadata 4

TextBox 10

### Alt/Text Metadata 5

Picture 2

### Relationships 5

- rId4: image:../media/image50.png

### Alt/Text Metadata 6

Picture 5

### Relationships 6

- rId5: image:../media/image51.jpg

### Alt/Text Metadata 7

Oval 3

### Alt/Text Metadata 8

Straight Arrow Connector 6

### Slide media/diagram relationships

- rId5: image:../media/image51.jpg
- rId4: image:../media/image50.png

## Slide 114

### Shape 1 Content Placeholder 2

Shared memory virtual address space distributed across the blocks of a cluster
Load, store, and atomic operations to other SM’s shared memory

### Alt/Text Metadata 1

Content Placeholder 2

### Shape 2 Title 1

NVIDIA H100 Distributed Shared Memory

### Alt/Text Metadata 2

Title 1

### Shape 3 Slide Number Placeholder 3

114

### Alt/Text Metadata 3

Slide Number Placeholder 3

### Shape 4 TextBox 10

https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/

### Alt/Text Metadata 4

TextBox 10

### Shape 5 Content Placeholder 2

Thread block clusters and distributed shared memory (DSMEM) are leveraged via cooperative_groups API
TMA unit supports copies across thread blocks in a cluster
Asynchronous transaction barriers

### Alt/Text Metadata 6

Picture 2

### Relationships 6

- rId4: image:../media/image52.jpg

### Speaker notes

Distributed shared memory allows direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks.
Distributed shared memory enables direct SM-to-SM communications for loads, stores, and atomics across multiple SM shared memory blocks

### Slide media/diagram relationships

- rId4: image:../media/image52.jpg

## Slide 115

### Shape 1 Marcador de contenido 2

7 versions in CUDA samples: Tree-based reduction in shared memory
Version 0: No whole warps active
Version 1: Contiguous threads, but many bank conflicts
Version 2: No bank conflicts
Version 3: First level of reduction when reading from global memory
Version 4: Warp shuffle or unrolling of final warp
Version 5: Warp shuffle or complete unrolling
Version 6: Multiple elements per thread sequentially

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 1

Optimized Parallel Reduction

### Alt/Text Metadata 2

Título 1

### Shape 3 TextBox 4

https://docs.nvidia.com/cuda/cuda-samples/index.html#cuda-parallel-reduction
Harris, “Optimizing Parallel Reduction in CUDA,” https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf

### Alt/Text Metadata 3

TextBox 4

### Shape 4 Slide Number Placeholder 3

115

### Alt/Text Metadata 4

Slide Number Placeholder 3

## Slide 116

### Shape 1 Marcador de contenido 2

3 new versions of reduction based on 3 previous versions
Version 0: No whole warps active
Version 3: First level of reduction when reading from global memory
Version 6: Multiple elements per thread sequentially
New versions 7, 8, and 9
Replace the for loop (tree-based reduction) with one shared memory atomic operation per thread

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 1

Reduction with Atomic Operations

### Alt/Text Metadata 2

Título 1

### Shape 3 Slide Number Placeholder 3

116

### Alt/Text Metadata 3

Slide Number Placeholder 3

## Slide 117

### Shape 1 Marcador de contenido 2

256-bin histogram calculation

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 1

Video Processing: Performance Results (I)

### Alt/Text Metadata 2

Título 1

### Shape 3 Marcador de número de diapositiva 3

117

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Shape 4 TextBox 6

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

### Alt/Text Metadata 4

TextBox 6

### Alt/Text Metadata 5

Imagen 13 | Stream_histo_280480_final.eps

### Relationships 5

- rId3: image:../media/image53.emf

### Alt/Text Metadata 6

Group 10 | TextBox 4 | Straight Arrow Connector 9

### Shape 6.1 TextBox 4

44%

### Alt/Text Metadata 6.1

TextBox 4

### Alt/Text Metadata 6.2

Straight Arrow Connector 9

### Alt/Text Metadata 7

Group 11 | TextBox 8 | Straight Arrow Connector 12

### Shape 7.1 TextBox 8

21%

### Alt/Text Metadata 7.1

TextBox 8

### Alt/Text Metadata 7.2

Straight Arrow Connector 12

### Slide media/diagram relationships

- rId3: image:../media/image53.emf

## Slide 118

### Shape 1 Marcador de contenido 2

RGB-to-grayscale conversion

### Alt/Text Metadata 1

Marcador de contenido 2

### Shape 2 Título 1

Video Processing: Performance Results (II)

### Alt/Text Metadata 2

Título 1

### Shape 3 Marcador de número de diapositiva 3

118

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Shape 4 TextBox 6

Gomez-Luna+, “Performance Models for Asynchronous Data Transfers on Consumer Graphics Processing Units,”
JPDC, 2012

### Alt/Text Metadata 4

TextBox 6

### Alt/Text Metadata 5

Imagen 12 | Stream_rgb_280480_final.eps

### Relationships 5

- rId3: image:../media/image54.emf

### Alt/Text Metadata 6

Group 8 | TextBox 9 | Straight Arrow Connector 10

### Shape 6.1 TextBox 9

63%

### Alt/Text Metadata 6.1

TextBox 9

### Alt/Text Metadata 6.2

Straight Arrow Connector 10

### Alt/Text Metadata 7

Group 11 | TextBox 12 | Straight Arrow Connector 13

### Shape 7.1 TextBox 12

18%

### Alt/Text Metadata 7.1

TextBox 12

### Alt/Text Metadata 7.2

Straight Arrow Connector 13

### Slide media/diagram relationships

- rId3: image:../media/image54.emf

## Slide 119

### Shape 1 Título 1

Performance Considerations

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Main bottlenecks
CPU-GPU data transfers
Global memory access
Memory access
Latency hiding
Occupancy
Memory coalescing
Data reuse
Shared memory usage
SIMD (Warp) Utilization: Divergence
Other considerations
Atomic operations: Serialization
Data transfers between CPU and GPU
Overlap of communication and computation

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

119

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

## Slide 120

### Shape 1 Título 1

Recommended Readings

### Alt/Text Metadata 1

Título 1

### Shape 2 Marcador de contenido 2

Hwu and Kirk, “Programming Massively Parallel Processors,” Third Edition, 2017
Chapter 5: Performance considerations
Chapter 18 - Programming
a heterogeneous computing cluster,
Section 18.5

### Alt/Text Metadata 2

Marcador de contenido 2

### Shape 3 Marcador de número de diapositiva 3

120

### Alt/Text Metadata 3

Marcador de número de diapositiva 3

### Alt/Text Metadata 4

Picture 4

### Relationships 4

- rId3: image:../media/image55.tiff

### Slide media/diagram relationships

- rId3: image:../media/image55.tiff
