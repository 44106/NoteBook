from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "期末复习资料"
RENDERED = ROOT / "rendered_slides"


S = {
    "L1": "1_intro_course-neuman_isa-single-multi-cycle-pipeline",
    "L2": "2-pipelining-reorder-buffer",
    "L3": "3-tomasula",
    "L4": "4-superscalar-cores-SIMD",
    "L5": "5_memory",
    "L6": "6-gpus-architecture",
    "L7": "7-gpus-optimization",
    "L8": "8-cache",
    "L9": "9-cache-coherence",
    "L10": "10-cache-coherence-consistency",
    "L11": "11--accelerator_motivation",
    "L12": "12-davinci-tpu_自动保存的_",
    "L13": "13-hwj-cann-mindspore",
    "L14": "14-parallel-training",
    "L15": "15-flashattention43",
    "L16": "16_overview_DESKTOP-H8IOQ49_s_conflicted_copy_2025-06-11_",
}


def rel(path: Path) -> str:
    return "../" + path.relative_to(ROOT).as_posix()


def slide(stem: str, n: int, label: str | None = None) -> str:
    p = RENDERED / stem / f"slide_{n:03d}.png"
    text = label or f"{n:03d}"
    if p.exists():
        return f"[{text}]({rel(p)})"
    return text


def slides(key: str, nums: list[int]) -> str:
    return "、".join(slide(S[key], n) for n in nums)


SECTIONS = [
    {
        "title": "1. 系统定位、课程总问题、transformation hierarchy",
        "overview": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "source": [
            ("第1讲", "L1", [3, 4, 5, 17, 19, 20, 21, 22, 30, 34]),
        ],
        "must": [
            "AI 芯片不是孤立硬件；它位于算法、编程模型、运行时、ISA、微结构、存储和器件之间。",
            "系统优化要看整条链，不能只看算子 FLOPs。",
            "第 16 讲把这部分放在开头，说明它是答解释题时的总框架。",
        ],
        "exam": "可能考简答：为什么 AI 芯片课要学体系结构；为什么 Nvidia/系统软件/硬件共同决定 AI 性能。",
    },
    {
        "title": "2. Amdahl、Roofline、Little、LLM compute 和性能上限",
        "overview": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "source": [
            ("第1讲", "L1", [43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 63, 64, 199, 200]),
            ("第6讲", "L6", [17, 19, 24]),
            ("第11讲", "L11", [19, 20, 21, 22, 39, 40, 41, 43]),
        ],
        "must": [
            "Amdahl：串行部分限制总加速比，优化要看全程序比例。",
            "Roofline：`AI = FLOPs / Bytes`，`attainable = min(peak, AI * bandwidth)`。",
            "Roofline 图上斜线是带宽上限，水平线是算力上限；HBM/cache 会抬高 memory roof。",
            "Little：高延迟要靠高并发隐藏，GPU warp/occupancy 的直觉来自这里。",
            "LLM compute estimation 说明参数数、token 数和训练总计算量的数量级关系。",
        ],
        "exam": "一定要会计算 Roofline；能解释 memory-bound/compute-bound；能把 Little 定律用于内存并发请求。",
    },
    {
        "title": "3. 冯诺依曼、ISA、单周期、多周期、流水线",
        "overview": [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
        "source": [
            ("第1讲", "L1", [65, 68, 69, 70, 71, 72, 73, 78, 84, 86, 88, 90, 98, 104, 107, 118, 119, 120, 126, 129, 130, 137, 141, 146, 150, 151, 156, 159, 160, 161, 170, 172, 173, 175, 176, 185, 187, 189, 190, 191, 192, 193]),
        ],
        "must": [
            "冯诺依曼五组成：memory、processing unit、control unit、input、output；stored program 和顺序语义。",
            "ISA 是软件可见接口；microarchitecture 是实现方式。",
            "单周期 CPI=1，但 cycle time 被最慢指令决定。",
            "多周期缩短 cycle time，不同指令用不同周期，但控制更复杂。",
            "流水线提高吞吐，不一定降低单条指令 latency；真实流水线会被 hazard 打断。",
        ],
        "exam": "可能给 datapath 或指令问数据流、控制信号、CPI/cycle time 权衡。",
    },
    {
        "title": "4. 依赖、ROB、Tomasula 和期末 CPU 例题",
        "overview": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62],
        "source": [
            ("第2讲", "L2", [10, 11, 13, 17, 18, 19, 22, 27, 28, 31, 35, 37, 47, 48, 49, 50, 52, 56, 58, 62, 63, 64, 66, 70, 71, 72, 73, 74, 75, 76]),
            ("第3讲", "L3", [13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 48, 51, 56, 62]),
            ("第4讲", "L4", [2, 3, 4, 5, 6]),
        ],
        "must": [
            "RAW 是真依赖；WAR/WAW 是名字造成的 false dependence，可由 renaming 消除。",
            "ROB：乱序完成、顺序提交，保证 precise exception。",
            "RS：等待区/调度窗口，保存 op、source valid/tag/value，源 ready 后发射。",
            "RAT：把 architectural register 映射到当前最新 producer tag 或 ready value。",
            "CDB 广播 `(tag,value)` 后，RS 中匹配 tag 的源变 ready；RAT 只有 tag 仍匹配才更新。",
            "第 16 讲 61-62 页 CPU 调度题对应第 3 讲 cycle 表，必须会自己画时序。",
        ],
        "exam": "高概率考 Tomasula 表格更新、ROB/precise exception、pipelined/OOO schedule。",
    },
    {
        "title": "5. Performance analysis 例题和 CPI/AMAT",
        "overview": [63, 64],
        "source": [
            ("第1讲", "L1", [147, 150, 151, 156, 160, 164, 184]),
            ("第8讲", "L8", [42, 43, 48, 49, 52, 53]),
            ("第9讲", "L9", [27, 28, 29, 30, 31, 42, 43, 44]),
        ],
        "must": [
            "`CPU time = IC * CPI * cycle time`。",
            "`Average CPI = sum(fraction_i * CPI_i)`。",
            "`AMAT = hit time + miss rate * miss penalty`，但如果题目写 miss access time，要注意是否已包含 hit time。",
            "比较两个 cache/processor 配置时，必须同时考虑 miss rate 和 cycle time/hit time。",
        ],
        "exam": "老师点名例题之一；`02_重点题型与例题详解.md` 已给完整计算。",
    },
    {
        "title": "6. SIMD、SIMT、GPU 架构、A100/H100 和 GPU 编程模型",
        "overview": [65, 66, 67, 68, 69, 70, 71, 72, 73, 74],
        "source": [
            ("第4讲", "L4", [18, 20, 24, 27, 31, 32, 34, 38, 42, 43, 44]),
            ("第6讲", "L6", [20, 22, 23, 25, 26, 29, 34, 35, 36, 37, 38, 39, 40, 49, 51, 54, 55, 56, 58, 59, 60, 62, 64, 67, 70, 71, 72, 73, 74, 80, 81, 87, 88, 89, 90]),
            ("第7讲", "L7", [90, 93, 94, 95, 100, 104, 110, 113, 114]),
        ],
        "must": [
            "SIMD 是一条指令处理多个数据；SIMT 是多线程编程模型在 SIMD-like 硬件上执行。",
            "SPMD：每个线程执行同一 kernel，用 thread/block id 选择数据。",
            "warp 是 SIMT 执行粒度；branch divergence 会降低 lane utilization。",
            "A100/H100 框图要服务于理解 SM、L2、HBM、tensor core、shared memory，不必死背所有型号参数。",
        ],
        "exam": "可能考 SIMD vs SIMT、warp divergence、CUDA indexing、GPU 为什么能隐藏延迟。",
    },
    {
        "title": "7. 存储系统、DRAM/HBM、memory hierarchy",
        "overview": [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93],
        "source": [
            ("第5讲", "L5", [12, 13, 14, 15, 17, 22, 23, 28, 31, 32, 34, 36, 37, 38, 40, 50, 53, 59, 62, 67, 70, 71, 72, 75, 77, 79, 80, 82, 86, 90, 91, 92, 95, 96, 98, 99, 100, 101, 102, 103, 104, 107, 109, 113, 118, 119, 121, 122, 123, 125, 129, 130, 133, 136, 137, 141, 144, 147, 149, 150, 175, 178, 179, 180]),
            ("第7讲", "L7", [21, 22, 23, 24, 27, 28, 32, 33]),
        ],
        "must": [
            "理想内存四目标互相冲突：zero latency、infinite capacity、infinite bandwidth、zero cost。",
            "DRAM 层次：channel/DIMM/rank/chip/bank/row buffer/column。",
            "Page hit/page closed/page miss 对延迟影响不同。",
            "HBM 的核心价值是高带宽，不是低成本或无限容量。",
            "数据搬移能耗常远大于计算能耗，是后续 buffer/tiling/dataflow 的原因。",
        ],
        "exam": "可能作为解释题、Roofline 背景题或 cache/AI accelerator 设计理由。",
    },
    {
        "title": "8. GPU 优化：occupancy、coalescing、bank conflict、tiling",
        "overview": [94, 95],
        "source": [
            ("第7讲", "L7", [14, 15, 16, 17, 18, 19, 32, 33, 35, 36, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 49, 52, 53, 54, 56, 60, 63, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 78, 81, 82, 84, 85, 88, 115, 117, 118]),
        ],
        "must": [
            "Occupancy 是 SM 上活跃 warp/block 的程度，用来隐藏内存延迟，但不是越高一定越好。",
            "Coalescing：同一 warp 连续线程访问连续地址，减少 memory transactions。",
            "Shared memory bank conflict：同一 warp 多线程访问同 bank 不同地址会串行化。",
            "Tiling：把 A/B tile 搬到 shared memory 多次复用，减少 HBM 访问。",
            "Atomic 冲突会串行化；streams 可尝试重叠拷贝和计算。",
        ],
        "exam": "可能考代码片段判断访存是否合并、为什么 tiling 提速、bank conflict 怎么避免。",
    },
    {
        "title": "9. Cache：locality、组织方式、地址划分、替换和写策略",
        "overview": [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111],
        "source": [
            ("第8讲", "L8", [16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]),
            ("第9讲", "L9", [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]),
        ],
        "must": [
            "Locality：temporal 和 spatial。",
            "`B=C/b`，`S=B/N`，offset/index/tag 位数会算。",
            "direct-mapped、fully associative、N-way set-associative 的映射规则和 tradeoff。",
            "LRU/random/FIFO/optimal 的含义和硬件成本。",
            "write-back/write-through、write-allocate/no-write-allocate 的组合。",
            "compulsory/capacity/conflict miss 的区分。",
        ],
        "exam": "老师点名 cache 例题；必须能手算地址序列 hit/miss。",
    },
    {
        "title": "10. Coherence、MSI/MESI、snoop/directory、consistency",
        "overview": [110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
        "source": [
            ("第9讲", "L9", [45, 48, 49, 50, 51, 52, 53, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 86]),
            ("第10讲", "L10", [11, 13, 16, 18, 22, 24, 25, 26, 27, 28, 29, 31, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 65]),
        ],
        "must": [
            "Coherence 是同一地址的可见顺序；consistency 是所有地址的全局内存顺序约定。",
            "MSI 三态和 MESI 的 E 状态意义。",
            "Snoop：广播简单、天然序列化但扩展性差。",
            "Directory：记录 sharers/owner，定向通信更可扩展但状态和协议复杂。",
            "SC 强、容易理解但性能差；TSO 加 store buffer；PSO 加 write coalescing。",
            "Memory barrier 分 Load-Load、Load-Store、Store-Store、Store-Load。",
        ],
        "exam": "可能考状态转换、coherence vs consistency 区分、store buffer 例子。",
    },
    {
        "title": "11. AI 加速器设计原则、Ascend、TPU、systolic array",
        "overview": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138],
        "source": [
            ("第11讲", "L11", [14, 16, 20, 21, 22, 24, 30, 31, 32, 36, 37, 38, 39, 40, 41, 43, 46, 47, 48, 49, 50, 52, 55, 58, 59, 62, 63, 66, 70, 72, 74, 80, 84, 88, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 102, 104, 106, 107, 133, 135]),
            ("第12讲", "L12", [6, 7, 11, 12, 13, 18, 19, 20, 21, 22, 23, 26, 27, 28, 35, 39, 40, 41, 42, 44, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 82, 83, 84, 90, 96, 97, 98, 100, 101, 112, 113, 114, 115, 116]),
            ("第13讲", "L13", [14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 35, 36, 37, 38, 39, 41, 43]),
        ],
        "must": [
            "AI accelerator 设计原则：global buffer/scratchpad、简化控制、并行计算模块、低精度、数据复用。",
            "Cache vs buffer：cache 透明但有 tag/replacement/coherence 开销；buffer 显式管理、适合规则张量。",
            "Ascend Cube/Vector/Scalar/MTE 各自职责。",
            "TPU systolic array：PE 阵列局部通信、节奏化数据流、高复用。",
            "WS/OS/IS/RS dataflow 的 stationary 对象和减少哪类访存。",
        ],
        "exam": "可能考模块职责、为什么 buffer 适合 AI、systolic array 怎么工作。",
    },
    {
        "title": "12. CANN、算子、图优化、MindSpore",
        "overview": [139, 140, 141, 142, 143, 144, 145, 146, 147],
        "source": [
            ("第13讲", "L13", [49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 71, 72, 73, 74, 75, 79, 80, 82, 83, 88]),
        ],
        "must": [
            "AI architecture 层次：AI chip、CANN/runtime、framework、parallel training。",
            "Tensor 的 shape/dtype/format，attribute 是算子静态参数。",
            "TBE DSL、TIK、AI CPU 三种算子开发方式的抽象层次和取舍。",
            "GE 做图准备和优化；CSE 消除公共子表达式；operator fusion 减少中间结果 HBM 往返。",
            "MindSpore 逻辑架构不必死背所有模块，但要知道 framework/runtime/compiler/operator 的关系。",
        ],
        "exam": "可能考 CANN 的上下承接作用、算子融合为什么提升性能。",
    },
    {
        "title": "13. 并行训练：data/pipeline/tensor parallel、AllReduce、ZeRO",
        "overview": [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174],
        "source": [
            ("第14讲", "L14", [10, 11, 12, 15, 17, 18, 19, 20, 21, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 79, 81, 82, 83, 84, 85]),
            ("第15讲", "L15", [3, 4, 5, 6, 7, 8, 9]),
        ],
        "must": [
            "Data parallel：每卡完整模型、不同数据，梯度 AllReduce。",
            "Ring AllReduce：ReduceScatter `N-1` 轮 + AllGather `N-1` 轮；每轮 `M/N`；每 worker 通信 `2M(N-1)/N`。",
            "Pipeline parallel：相邻 stage 传 activation 和 activation gradient；GPipe bubble 公式要会。",
            "Tensor parallel row-wise：每卡算一部分 output，层间常 AllGather。",
            "Tensor parallel column-wise：partial output 需要 ReduceScatter/合并。",
            "Alternating Partitioning：row-wise 和 column-wise 交替，减少相邻两层之间同步；边界仍可能 AllReduce。",
            "ZeRO：切分 optimizer states/gradients/parameters，省显存但增加 collectives。",
            "第 15 讲 FlashAttention 主体不考；第 3-9 页作为 ZeRO/系统存储通信衔接保留。",
        ],
        "exam": "高概率考老师点名的 tensor parallel、AllReduce 轮数/通信量、每种切法对应通信。",
    },
    {
        "title": "14. 课程行政页和实验页",
        "overview": [175, 176],
        "source": [
            ("第1讲", "L1", [39, 40, 41]),
        ],
        "must": [
            "这两页不是主要知识点，但说明 final exam 是闭卷且可带一张 A4 memo。",
            "实验内容反向提示考试重点：pipelined CPU、SIMD、GPU programming、AI chip programming。",
        ],
        "exam": "不作为知识点背诵，但用来安排复习策略。",
    },
]


def build() -> str:
    lines: list[str] = [
        "# 第16讲总复习到前15讲重点映射",
        "",
        "第 16 讲总复习 PPT 是期末复习的最高优先级脉络。本文件把第 16 讲出现的所有主要知识点显式映射回前 1-15 讲对应 PPT 页，目的有两个：第一，确保总复习里出现的内容都被升级为重点；第二，复习时能从总复习页快速回到原讲义细节和原图。",
        "",
        "使用方法：先看本文件的第 16 讲页码，再点开对应前置讲次截图；如果某个知识点在 `01` 或 `04` 里已经讲过，本文件相当于把它标成“总复习确认重点”。",
        "",
    ]
    for sec in SECTIONS:
        lines.append(f"## {sec['title']}")
        lines.append("")
        lines.append(f"- 第16讲页：{slides('L16', sec['overview'])}")
        lines.append("- 对应前面课程页：")
        for name, key, nums in sec["source"]:
            lines.append(f"  - {name}：{slides(key, nums)}")
        lines.append("- 必须掌握：")
        for item in sec["must"]:
            lines.append(f"  - {item}")
        lines.append(f"- 常见考法：{sec['exam']}")
        lines.append("")
    lines.extend(
        [
            "## 总复习页优先级",
            "",
            "最高优先级：第 16 讲 16-25、48-62、64、96-111、148-174 页。这些直接对应老师点名题型和额外重点。",
            "",
            "高优先级：第 16 讲 30-47、65-95、110-124、125-147 页。这些覆盖性能模型、CPU/GPU/存储/cache/coherence/AI accelerator/runtime 的主线。",
            "",
            "中优先级：第 16 讲 2-15、26-29、175-176 页。它们用于建立系统视角、数量级直觉和考试安排。",
            "",
            "## 与现有资料的对应",
            "",
            "- `01_完整零基础讲义.md`：负责从零解释上述概念。",
            "- `02_重点题型与例题详解.md`：负责第 16 讲四类例题。",
            "- `04_逐讲图示与细节补充讲义.md`：负责图示、状态表、结构图、通信图。",
            "- `05_逐页图文索引.md`：负责逐页查漏。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    out = OUT / "07_第16讲总复习到前15讲重点映射.md"
    out.write_text(build(), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
