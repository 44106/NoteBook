from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / "extracted"
RENDERED = ROOT / "rendered_slides"
CONTACT = ROOT / "slide_contact_sheets"
OUT = ROOT / "期末复习资料"


DECKS = [
    ("1_intro_course-neuman_isa-single-multi-cycle-pipeline", "第1讲 Introduction / ISA / 单周期-多周期-流水线"),
    ("2-pipelining-reorder-buffer", "第2讲 Pipeline Hazards / Reorder Buffer"),
    ("3-tomasula", "第3讲 Tomasula / RAT / RS"),
    ("4-superscalar-cores-SIMD", "第4讲 Superscalar / SIMD / Multithreading / Multicore"),
    ("5_memory", "第5讲 Memory Overview / DRAM / HBM / Refresh"),
    ("6-gpus-architecture", "第6讲 GPU Architecture / CUDA / SIMT"),
    ("7-gpus-optimization", "第7讲 GPU Optimization"),
    ("8-cache", "第8讲 Memory Hierarchy and Caches"),
    ("9-cache-coherence", "第9讲 Cache Policies / Coherence"),
    ("10-cache-coherence-consistency", "第10讲 Coherence / Consistency"),
    ("11--accelerator_motivation", "第11讲 Accelerator Motivation"),
    ("12-davinci-tpu_自动保存的_", "第12讲 DaVinci / TPU / Systolic Array"),
    ("13-hwj-cann-mindspore", "第13讲 AI Chip + Runtime + Framework"),
    ("14-parallel-training", "第14讲 Parallel Training"),
    ("15-flashattention43", "第15讲 ZeRO / FlashAttention"),
    ("16_overview_DESKTOP-H8IOQ49_s_conflicted_copy_2025-06-11_", "第16讲 Overview / Final Review"),
]


KEY_SLIDES: dict[str, list[int]] = {
    "1_intro_course-neuman_isa-single-multi-cycle-pipeline": [
        5, 20, 21, 22, 43, 44, 46, 47, 48, 49, 50, 51, 55, 56, 63, 64,
        68, 71, 78, 84, 90, 98, 104, 107, 118, 119, 126, 137, 141,
        146, 150, 156, 159, 170, 172, 173, 178, 179, 185, 187, 189, 199, 200,
    ],
    "2-pipelining-reorder-buffer": [
        10, 11, 13, 17, 18, 19, 22, 27, 28, 31, 35, 37, 47, 48, 49,
        50, 52, 56, 58, 62, 63, 64, 66, 70, 71, 72, 73, 74, 75, 76,
    ],
    "3-tomasula": [
        13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30, 32, 33,
        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 48, 51, 56, 62,
    ],
    "4-superscalar-cores-SIMD": [
        10, 11, 12, 13, 14, 15, 18, 20, 24, 27, 31, 32, 34, 38, 41,
        42, 43, 44, 45, 52, 54, 55, 56, 58, 59, 63, 70, 75, 76, 77,
        80, 88, 94,
    ],
    "5_memory": [
        12, 13, 14, 15, 17, 22, 23, 28, 31, 32, 34, 36, 37, 38, 40,
        50, 53, 59, 62, 67, 70, 71, 72, 75, 77, 79, 80, 82, 86,
        90, 91, 92, 95, 96, 98, 99, 100, 101, 102, 103, 104, 107,
        109, 113, 118, 119, 121, 122, 123, 125, 129, 130, 133, 136,
        137, 141, 144, 147, 149, 150, 175, 178, 179, 180,
    ],
    "6-gpus-architecture": [
        17, 19, 20, 22, 23, 24, 25, 26, 29, 30, 34, 35, 36, 37, 38,
        39, 40, 42, 43, 47, 49, 51, 54, 55, 56, 58, 59, 60, 61,
        62, 63, 64, 67, 70, 71, 72, 74, 80, 81, 87, 88, 89, 90,
    ],
    "7-gpus-optimization": [
        14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 27, 28, 32, 33,
        35, 36, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 49, 50,
        52, 53, 54, 56, 60, 63, 65, 66, 67, 68, 69, 70, 71, 72,
        75, 76, 78, 81, 82, 84, 85, 88, 90, 93, 94, 95, 100,
        104, 110, 113, 114, 115, 117, 118,
    ],
    "8-cache": [
        16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31,
        32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
        65, 66, 67, 68,
    ],
    "9-cache-coherence": [
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26,
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
        42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 55, 57, 58, 59,
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
        74, 75, 76, 86,
    ],
    "10-cache-coherence-consistency": [
        11, 13, 16, 18, 22, 24, 25, 26, 27, 28, 29, 31, 33, 34,
        35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50,
        52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 65, 66, 67, 68,
    ],
    "11--accelerator_motivation": [
        14, 16, 20, 21, 22, 24, 30, 31, 32, 36, 37, 38, 39, 40,
        41, 43, 46, 47, 48, 49, 50, 52, 55, 58, 59, 62, 63, 66,
        70, 72, 74, 80, 84, 88, 90, 91, 93, 94, 95, 96, 97,
        99, 100, 101, 102, 104, 106, 107, 109, 115, 120, 130,
        131, 133, 135,
    ],
    "12-davinci-tpu_自动保存的_": [
        6, 7, 11, 12, 13, 18, 19, 20, 21, 22, 23, 26, 27, 28,
        35, 39, 40, 41, 42, 44, 46, 47, 48, 50, 51, 52, 53,
        54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
        75, 82, 83, 84, 90, 96, 97, 98, 100, 101, 105, 112,
        113, 114, 115, 116, 117, 118, 121, 122,
    ],
    "13-hwj-cann-mindspore": [
        14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28,
        29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 41, 43, 49,
        50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63,
        64, 65, 66, 67, 68, 71, 72, 73, 74, 75, 79, 80, 82,
        83, 88, 91, 92, 93,
    ],
    "14-parallel-training": [
        10, 11, 12, 15, 17, 18, 19, 20, 21, 23, 24, 25, 26,
        28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41,
        42, 43, 44, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72,
        73, 74, 75, 79, 81, 82, 83, 84, 85,
    ],
    "15-flashattention43": [3, 4, 5, 6, 7, 8, 9],
    "16_overview_DESKTOP-H8IOQ49_s_conflicted_copy_2025-06-11_": [
        13, 14, 16, 17, 18, 19, 20, 23, 24, 30, 31, 33, 34,
        36, 37, 39, 41, 42, 43, 47, 48, 49, 50, 52, 56, 58,
        59, 60, 61, 62, 64, 70, 71, 72, 73, 79, 80, 81, 84,
        85, 86, 87, 90, 92, 96, 97, 98, 100, 102, 103, 105,
        106, 108, 109, 110, 111, 113, 116, 118, 119, 120, 123,
        124, 126, 130, 133, 134, 135, 136, 138, 140, 142, 144,
        146, 148, 150, 152, 156, 163, 164, 165, 169, 170, 171,
        172, 173,
    ],
}


def load_deck(stem: str) -> dict:
    return json.loads((EXTRACTED / f"{stem}.json").read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(OUT).as_posix() if path.is_relative_to(OUT) else ("../" + path.relative_to(ROOT).as_posix())


def slide_link(stem: str, n: int, text: str | None = None) -> str:
    p = RENDERED / stem / f"slide_{n:03d}.png"
    label = text or f"{n:03d}"
    if p.exists():
        return f"[{label}]({rel(p)})"
    return label


def contact_link(stem: str, text: str = "contact sheet") -> str:
    matches = sorted(CONTACT.glob(f"{stem}*_contact.jpg"))
    if not matches:
        return text
    return f"[{text}]({rel(matches[0])})"


def one_line(values: list, limit: int = 180) -> str:
    text = " ".join(str(v).replace("\n", " / ") for v in values)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "..."


def is_excluded_flash(stem: str, n: int) -> bool:
    return stem == "15-flashattention43" and n >= 11


def build_page_index() -> str:
    lines: list[str] = []
    lines.extend(
        [
            "# 逐页图文索引",
            "",
            "这个索引用来解决“是否漏页”的问题：每一页 PPT 都保留了标题、图表数量、截图链接和抽取文字摘要。真正的讲解请配合 `01_完整零基础讲义.md`、`02_重点题型与例题详解.md` 和 `04_逐讲图示与细节补充讲义.md` 使用。",
            "",
            "标记说明：",
            "",
            "- `重点图页`：本页在图示补充讲义中被重点解释，或者是期末高频结构/表格/计算页。",
            "- `含图/含表`：PPT 页面含图片或表格，复习时要打开截图看布局和箭头关系。",
            "- `不考`：按老师说明，第 15 讲 FlashAttention 主体部分不作为考试内容；这里仍列出页码，防止你误以为文件缺页。",
            "",
            "## 全局统计",
            "",
        ]
    )
    total = 0
    rendered = 0
    table_pages = 0
    image_pages = 0
    excluded = 0
    for stem, title in DECKS:
        deck = load_deck(stem)
        total += len(deck["slides"])
        rendered += len(list((RENDERED / stem).glob("slide_*.png")))
        table_pages += sum(1 for s in deck["slides"] if s.get("table_count", 0))
        image_pages += sum(1 for s in deck["slides"] if s.get("image_count", 0))
        excluded += sum(1 for s in deck["slides"] if is_excluded_flash(stem, s["number"]))
    lines.append(f"- PPT 总页数：{total}")
    lines.append(f"- 已渲染截图：{rendered}")
    lines.append(f"- 含图片页：{image_pages}")
    lines.append(f"- 含表格页：{table_pages}")
    lines.append(f"- 第 15 讲 FlashAttention 主体不考页：{excluded}")
    lines.append("")

    for stem, title in DECKS:
        deck = load_deck(stem)
        key = set(KEY_SLIDES.get(stem, []))
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- 原 PPT：`{deck['file']}`")
        lines.append(f"- 页数：{len(deck['slides'])}")
        lines.append(f"- 总览图：{contact_link(stem)}")
        lines.append("")
        lines.append("| 页 | 截图 | 标记 | 图片/表格 | 标题 | 摘要 |")
        lines.append("|---:|---|---|---|---|---|")
        for s in deck["slides"]:
            n = int(s["number"])
            marks = []
            if n in key:
                marks.append("重点图页")
            if s.get("image_count", 0) or s.get("table_count", 0):
                marks.append("含图/含表")
            if is_excluded_flash(stem, n):
                marks.append("不考")
            mark = "、".join(marks) if marks else ""
            img_tbl = f"{s.get('image_count', 0)}/{s.get('table_count', 0)}"
            title_text = str(s.get("title") or "").replace("|", "\\|")
            summary = one_line(s.get("all_text", [])[:12]).replace("|", "\\|")
            lines.append(f"| {n} | {slide_link(stem, n)} | {mark} | {img_tbl} | {title_text} | {summary} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def deck_stats_table() -> str:
    lines = ["| 讲次 | 页数 | 含图页 | 含表页 | contact sheet |", "|---|---:|---:|---:|---|"]
    for stem, title in DECKS:
        deck = load_deck(stem)
        img = sum(1 for s in deck["slides"] if s.get("image_count", 0))
        tbl = sum(1 for s in deck["slides"] if s.get("table_count", 0))
        lines.append(f"| {title} | {len(deck['slides'])} | {img} | {tbl} | {contact_link(stem)} |")
    return "\n".join(lines)


def key_links(stem: str, nums: list[int]) -> str:
    return "、".join(slide_link(stem, n) for n in nums)


def build_visual_notes() -> str:
    s1 = "1_intro_course-neuman_isa-single-multi-cycle-pipeline"
    s2 = "2-pipelining-reorder-buffer"
    s3 = "3-tomasula"
    s4 = "4-superscalar-cores-SIMD"
    s5 = "5_memory"
    s6 = "6-gpus-architecture"
    s7 = "7-gpus-optimization"
    s8 = "8-cache"
    s9 = "9-cache-coherence"
    s10 = "10-cache-coherence-consistency"
    s11 = "11--accelerator_motivation"
    s12 = "12-davinci-tpu_自动保存的_"
    s13 = "13-hwj-cann-mindspore"
    s14 = "14-parallel-training"
    s15 = "15-flashattention43"
    s16 = "16_overview_DESKTOP-H8IOQ49_s_conflicted_copy_2025-06-11_"

    return f"""# 逐讲图示与细节补充讲义

这份补充讲义专门弥补第一版资料的不足：PPT 中大量知识不是写成段落，而是藏在结构图、时间表、状态表、数据流箭头和硬件框图里。复习时不要只背文字，要能把图读成“谁产生数据、谁消费数据、什么时候通信、什么时候 stall、状态如何变化”。

## 0. 资料覆盖与使用方法

{deck_stats_table()}

阅读顺序建议：

1. 先读第 16 讲总复习对应图页，形成主线：{key_links(s16, [13, 19, 30, 47, 59, 64, 70, 79, 96, 110, 126, 140, 150, 169])}。
2. 遇到不懂的图，回到对应讲次的详细页：CPU 看第 1-4 讲，存储/cache 看第 5、8-10 讲，GPU 看第 6-7 讲，AI 加速器看第 11-13 讲，并行训练看第 14-15 讲。
3. 用 `05_逐页图文索引.md` 查漏：每页都有截图链接，含图/含表页必须至少扫一遍。

## 1. 读图总方法

### 1.1 系统分层图

典型页：第 1 讲 {key_links(s1, [5, 20, 21, 22])}，第 16 讲 {key_links(s16, [2, 10, 12])}。

系统分层图不是背景介绍，而是整门课的总逻辑。最上层是问题、算法和程序，最下层是逻辑门、器件和电子。中间依次经过编程语言、系统软件、ISA、微结构和硬件。考试中如果问“为什么学 AI 芯片要先学体系结构”，答案就是：AI 性能不是由单个矩阵乘公式决定，而是由算法、编译、运行时、微结构、存储和通信共同决定。

读这类图时要抓三件事：

- 上层给下层“需求”：例如 Transformer 需要大矩阵乘、Attention、AllReduce。
- 下层给上层“约束”：例如 HBM 带宽、cache miss、同步延迟、片上 buffer 容量。
- 课程每一讲都对应一层或一类约束：CPU 微结构解决指令级并行，存储层次解决容量/延迟矛盾，GPU/AI 加速器解决数据并行和矩阵计算，并行训练解决单卡算力/显存不够。

### 1.2 性能模型图

典型页：Roofline {key_links(s1, [46, 47, 48, 49, 50, 51, 55, 56])}，Little 定律 {key_links(s1, [63, 64])}，第 16 讲例题入口 {key_links(s16, [16, 17, 18, 19, 20, 23, 24, 30, 31])}。

Roofline 图横轴是 arithmetic intensity，纵轴是 throughput。斜线是内存带宽上限，水平线是峰值算力上限。读图步骤固定：

1. 算 `AI = FLOPs / Bytes`。
2. 算 `AI * bandwidth`。
3. 和 `peak compute` 取最小值。
4. 如果落在斜线段，是 memory-bound；落在水平段，是 compute-bound。
5. 如果真实性能远低于上限，说明还存在利用率、访存合并、同步、分支、occupancy 等问题。

Little 定律图用银行柜台类比：吞吐率固定、服务延迟很大时，需要足够多的并发请求才能填满系统。硬件里对应的是：DRAM/HBM 延迟几十到几百周期，GPU 必须有很多 warp 同时驻留，才能在一个 warp 等内存时切换到另一个 warp。

### 1.3 数据通路和流水线图

典型页：单周期 datapath {key_links(s1, [141, 146, 150])}，流水线洗衣类比和资源图 {key_links(s1, [172, 173, 178, 179, 185, 187, 189])}，第 16 讲复习页 {key_links(s16, [36, 37, 39, 41, 47])}。

读 datapath 图时按一条指令走数据：

- `lw`：PC 取指，寄存器读 base，ALU 算地址，data memory 读，写回 register file。
- `sw`：PC 取指，寄存器读 base 和待写数据，ALU 算地址，data memory 写，不写回寄存器。
- R-type：PC 取指，读两个寄存器，ALU 计算，写回寄存器，不访问 data memory。
- branch：PC 取指，读寄存器比较，决定 PC 是否跳转。

流水线图要区分 latency 和 throughput。单条指令要经过 IF/ID/EX/MEM/WB 多个阶段，流水线不一定缩短单条指令延迟，但理想情况下每个周期完成一条指令，提升吞吐。PPT 的洗衣图强调：瓶颈阶段决定节拍，阶段不均衡、资源冲突、依赖和分支都会让理想加速打折。

### 1.4 状态表和时序表

典型页：pipeline resource table {key_links(s1, [187])}，Tomasula cycle 表 {key_links(s3, [24, 25, 28, 30, 32, 33, 34, 47, 51])}，Ring AllReduce 每轮表 {key_links(s14, [36, 38, 40, 41, 42, 43, 44, 45, 46, 47])}。

读表的通用方法：

- 行通常表示对象：指令、寄存器、RS entry、GPU、cache line。
- 列通常表示时间、字段或状态：cycle、valid/tag/value、chunk、MSI/MESI state。
- 不要只看最后答案，要问“哪一格在什么时候被谁更新”：这正是期末会考的地方。

## 2. 第1讲：从系统到 CPU 微结构

本讲可考核心：系统分层、Amdahl、Roofline、Little、冯诺依曼模型、ISA、指令格式、单周期/多周期/流水线 CPU。

关键图页：{key_links(s1, KEY_SLIDES[s1])}。

系统和课程定位图说明：AI 训练和推理的性能问题不能只在模型层解决。深度学习长期没有爆发，PPT 用算法、数据、算力三因素说明：算法和数据成熟后，算力成为关键瓶颈。系统层把 PyTorch/TensorFlow/MindSpore、运行时、编译器、GPU/NPU/TPU、内存和互连连起来。

Roofline 图要会从图上读出两个屋顶：斜屋顶由内存带宽决定，平屋顶由峰值算力决定。PPT 里的 7-point stencil 和 STREAM Triad 是典型比较：stencil 的 AI 比 triad 高，但两者都可能远低于 peak compute，所以优化重点是访存复用而非盲目增加 ALU。图上的 HBM/cache roof 还说明：同一个 kernel 放到更高带宽层次，memory-bound 上限会抬高。

Little 定律页把“延迟隐藏”讲清楚：`需要并发量 = 目标吞吐率 * 延迟`。如果内存吞吐目标是 12GB/s、一次访问延迟 100ns，就必须允许大量 outstanding memory requests。这个思想后来直接对应 GPU occupancy 和 warp-level FGMT。

冯诺依曼图要背五部分：memory、processing unit、control unit、input、output。PPT 中强调 stored program 和 sequential instruction processing：程序和数据都存在内存中，指令按 PC 顺序取出执行。软件看到的是 architectural state，包括 PC、寄存器和内存；微结构可以内部流水、乱序，但最终必须保持 ISA 语义。

ISA 页要掌握三件事：内存组织、寄存器组织、指令集合/格式。MIPS 的例子体现 byte-addressable、base+offset load/store、R/I-type 编码、opcode 和 operands。ABI 表不太可能要求逐项背 `$at/$v0/$a0`，但要知道 ABI 是二进制模块之间关于寄存器使用、调用约定等的约定。

单周期 datapath 图的读法：所有组合逻辑必须在一个 clock cycle 内完成，所以 CPI=1 不代表快，因为周期被最慢指令决定。图里的 state elements 包括 PC、register file、memory；control logic 根据 opcode 产生 ALUOp、MemRead、MemWrite、RegWrite、MemtoReg、Branch 等信号。

多周期图的读法：一条指令拆成若干短阶段，每个阶段结束把中间结果存在内部寄存器。好处是周期变短，不同指令用不同周期数，并且硬件可复用；坏处是控制 FSM 更复杂，寄存器开销和 setup/hold 开销增加。

流水线图的读法：IF/ID/EX/MEM/WB 是时间重叠，不是把每条指令变短。PPT 中 `4 independent ADDs` 用来说明理想 steady state；resource view 用来检查同一周期有没有两条指令抢同一资源；control signal 图说明控制信号在 decode 后要随指令流过 pipeline registers，不能只在 ID 阶段使用。

LLM compute estimation 页属于系统动机。公式强调 Transformer 训练计算量和参数数 `N`、token 数 `D` 近似成正比，常见估算 `C_F+B ≈ 6ND`。考试若出现这类题，重点是会识别训练算力随模型和数据规模线性放大，而不是背某个模型表格。

## 3. 第2讲：Pipeline Hazard 与 ROB

本讲可考核心：三类 hazard、RAW/WAR/WAW、stall/forwarding/compiler scheduling、precise exception、ROB 的意义和字段。

关键图页：{key_links(s2, KEY_SLIDES[s2])}。

Pipeline hazard 定义页给出总分类：structural hazard 是资源冲突，data hazard 是前序结果未 ready，control hazard 是下一条 PC 未确定。考试常让你判断某段代码属于哪类 hazard。

Structural hazard 图要看“同一周期谁抢资源”。例如 unified memory 同时取指和访存会冲突，寄存器堆读写端口不足会冲突，功能单元没 fully pipelined 也会冲突。解决办法是复制资源、增加端口、让功能单元流水化。

Data dependence 图要严格区分：

- RAW / flow dependence：后指令读前指令写的值，是真依赖，不能靠改名消除。
- WAR / anti dependence：后指令写了前指令要读的名字，是假依赖。
- WAW / output dependence：两条指令写同一名字，是假依赖。

Stall 图里的硬件动作要会说：stall 时 PC 和 IF/ID 保持不变，被阻塞的指令留在原阶段；同时向后一级注入 bubble，即清空/禁用控制信号，让后面像执行 NOP。PPT 的 `StallF/StallD/FlushE` 就是在做这件事。

Forwarding 图要抓“结果还没写回 register file，但已经在 EX/MEM 或 MEM/WB pipeline register 里”。旁路网络把这个值直接送到 ALU 输入。易错点：load-use hazard 中 load 数据通常到 MEM 末尾才可用，紧跟下一条使用时仍可能需要一个 bubble。

Precise exception 图说明：异常发生时，机器状态必须像顺序执行到某条指令边界。多周期/流水线/乱序执行都可能让后面的指令先完成，所以必须有机制保证提交顺序。

ROB 图的核心：decode 时按程序顺序分配 entry，执行可以乱序完成，结果先写进 ROB；只有 ROB head ready 且无异常时，才把结果提交到 architectural state。ROB 同时解决三类问题：

- multi-cycle execution 中结果完成时间不同。
- exception/interrupt 需要 precise state。
- WAR/WAW false dependence 可通过把目的寄存器重命名到 ROB entry 消除。

ROB entry 常见字段：busy/valid、instruction type、destination register 或 store address、value、ready/done bit、exception bit。考试给表格时，不要把 ROB ready 和 register file valid 混为一谈。

## 4. 第3讲：Tomasula、RAT、RS

本讲是老师点名重点。必须能解释 RAT 和 RS 的字段含义、何时更新、如何更新。

关键图页：{key_links(s3, KEY_SLIDES[s3])}。

Two humps 图是整讲主线：第一个 hump 是 reservation stations/scheduling window，让指令 in-order issue 之后可以 out-of-order dispatch/execute；第二个 hump 是 reorder buffer/active window，让指令 out-of-order completion 之后仍然 in-order commit。图里 `TAG and VALUE Broadcast Bus` 对应 CDB，是唤醒等待者的关键。

Reservation Station 页的核心句子：把依赖指令移出主流水线，让独立指令绕过去。RS 不是寄存器文件，它是“等待区”。每个 RS entry 通常保存：

- op：要执行的操作。
- destination tag：本指令结果将以哪个 tag 广播。
- source1/source2 的 `V/tag/value`。
- busy/ready 状态。

RAT / Register Alias Table 页的核心：architectural register 不一定直接保存最新值，可能指向一个未来 producer。每个寄存器项可理解为：

- valid=1：寄存器文件中的 value 是最新 architectural/rename-visible 值。
- valid=0：最新值还没产生，要等 tag 对应的 RS/ROB entry 广播。
- tag：最新 producer 的名字。
- value：当 valid=1 时可直接读；当 valid=0 时通常旧值不能作为当前源操作数使用。

Tomasula issue/rename 规则：

1. 如果没有空闲 RS entry，不能 issue。
2. 为指令占用一个 RS entry，entry id 就是这条指令结果的 tag。
3. 对每个源寄存器查 RAT/RF：如果 valid=1，把 value 放入 RS.source.value 并设 `V=1`；如果 valid=0，把 producer tag 放入 RS.source.tag 并设 `V=0`。
4. 对目的寄存器，把 RAT[dest] 改成新 tag，valid 置 0。

CDB broadcast 规则：

1. 功能单元完成后广播 `(tag, value)`。
2. 所有 RS entry 的 source tag 若匹配，就填入 value 并设 `V=1`。
3. RAT 中如果某寄存器当前 tag 仍等于广播 tag，才把 value 写入并设 valid=1。
4. 如果 RAT tag 已被更年轻的 writer 改掉，则不能覆盖 RAT，因为这个广播值已不是该 architectural register 的最新名字。

Dispatch/wakeup 规则：RS 中所有源操作数 `V=1` 且对应 FU 可用时，该指令 ready，可以按数据流顺序 dispatch，而不是按程序顺序。PPT cycle 0-20 的表格就是这个规则的逐周期演示。读这些表时按三列走：RAT 哪些寄存器 valid 变 0，RS 哪些源等待 tag，CDB 广播后哪些 tag 被唤醒。

考试最容易错的是把 “register renaming table 更新” 和 “reservation station 更新” 混在一起：

- issue 时：RAT 的 dest 改成新 tag；RS 记录源的 value 或 tag。
- broadcast 时：RS 的等待源被唤醒；RAT 只有在 tag 仍匹配时才可 valid=1。
- commit 时：若有 ROB，则 architectural state 按 ROB 顺序更新；Tomasula 讲义页强调 CDB，但精确异常仍需要 ROB。

第 4 讲开头重复 RAT 组件图 {key_links(s4, [5, 6])}，复习时可把第 3、4 讲连起来看。

## 5. 第4讲：Superscalar、SIMD、多线程、多核

本讲可考核心：提高吞吐的几种路线及其瓶颈。

关键图页：{key_links(s4, KEY_SLIDES[s4])}。

Superscalar 图说明：N-wide superscalar 可以每周期 fetch/decode/execute/retire 多条指令，但依赖检查、端口、调度窗口、重命名、ROB 和 bypass 网络复杂度都上升。PPT 的 in-order superscalar 例子显示：没有足够独立指令时，理想 IPC 达不到。Roofline 问法中，superscalar 增加的是 peak compute，如果程序仍 memory-bound，性能上限可能不变。

Flynn taxonomy 和 SIMD 图要会比较 SISD、SIMD、MIMD、SPMD。SIMD 是一条指令操作多个数据元素，适合向量加、图像处理、科学计算和深度学习。支持 SIMD 需要 vector register file、vector ALU、vector memory 访问。局限是内存带宽和数据布局常成为瓶颈。

Fine-grained multithreading 图说明：硬件保存多个线程上下文，每个周期换一个线程取指/执行，让单线程的依赖和内存等待被其他线程填补。它简化依赖检查、提高延迟容忍，但单线程 latency 可能变差，而且需要足够线程。

Multicore 图说明：把更多晶体管用于多个较简单核心，而不是无限扩大单个 OoO superscalar。Piranha、Niagara、POWER 系列图体现不同设计点：小核多线程强调吞吐和能效，大核强调单线程性能。考题常问 tradeoff：多核提高并行程序吞吐，但需要软件有线程级并行，并会带来 cache coherence、memory bandwidth 和 synchronization 问题。

## 6. 第5讲：Memory Overview、DRAM、HBM、Refresh

本讲可考核心：理想内存四属性、存储技术层次、SRAM/DRAM 结构、DRAM hierarchy、HBM、refresh、能耗/可靠性瓶颈。

关键图页：{key_links(s5, KEY_SLIDES[s5])}。

Ideal memory 图提出四个互相冲突的目标：zero latency、infinite capacity、infinite bandwidth、zero cost。现实规律是 bigger is slower、faster is more expensive，所以必须分层。

存储技术比较图从快到慢大致是 FF、SRAM、HBM/DRAM、SSD、disk。FF 很快但面积/能耗昂贵；SRAM 快且可做 cache/buffer；DRAM 容量大但延迟高，需要 refresh；SSD/disk 容量更大但延迟跨数量级。

Memory array / SRAM 图要看 wordline、bitline、decoder、sense amplifier。读操作一般是 decoder 选中 wordline，整行 bit cell 影响 bitline，sense amplifier 放大，再由 mux 选择需要的列。Banking 图说明多个 bank 可独立访问，提升带宽，但共享总线/端口仍可能冲突。

Memory bottleneck 图从 performance、energy、reliability 三个角度说明内存重要。能耗表的核心信息是数据搬移常比计算贵得多，尤其片外 DRAM 访问远比片上计算耗能。这是 AI 加速器强调片上 buffer、tiling、data reuse 的根本原因。

DRAM subsystem 图层次：channel -> DIMM -> rank -> chip -> bank -> row/bank buffer -> column。访问状态：

- page hit：目标 row 已经 open，只需 column access，延迟最低。
- page closed：bank 没有 open row，需要 activate 后访问。
- page miss/conflict：另一个 row 已经 open，要 precharge 关闭旧 row，再 activate 新 row，再 column access，延迟最高。

Transferring a cache block 表格页说明一次 cache line 传输不是一个抽象动作，而是被 DRAM burst、channel width、chip/rank/bank 组织拆成多个周期。读图时要把“cache block 大小”和“每次 DRAM 数据总线能给多少字节”联系起来。

HBM 图强调高带宽来自 3D stacking、宽接口、多通道和靠近 compute。HBM 的优势是 bandwidth，高成本和容量限制仍存在。A100/HBM 图与 GPU/AI 加速器性能绑定很紧。

Refresh 图说明 DRAM 电容漏电，需要周期性刷新。刷新带来性能和能耗开销，并且容量越大越严重。RAIDR 思想是不同 row retention time 不同，不必所有行按最坏情况刷新；通过 profiling 找出保留时间短的行，减少刷新次数。老师若把这视为拓展，考试可能不考细节，但“refresh 是 DRAM 特有可靠性/性能开销”应掌握。

## 7. 第6讲：GPU Architecture

本讲可考核心：CPU-GPU 协处理、SPMD 编程模型、SIMT 硬件执行、CUDA grid/block/thread、memory hierarchy、warp、branch divergence。

关键图页：{key_links(s6, KEY_SLIDES[s6])}。

CPU-GPU relationship 图说明 CPU 负责串行/控制复杂部分，GPU 负责大规模数据并行 kernel。Amdahl 定律提醒：不能并行或必须留在 CPU 的部分会限制总加速比。

Programming model vs hardware execution model 图是本讲重点：程序员写的是 SPMD，多线程执行同一 kernel，每个线程用 `threadIdx/blockIdx` 处理不同数据；硬件底层把线程分组成 warp，用 SIMD/SIMT pipeline 执行。也就是说，GPU 是“用线程接口暴露的 SIMD 机器”。

CUDA memory hierarchy 图要掌握：global memory/HBM 容量大但慢；L2 全芯片共享；每个 SM 有 registers、shared memory/L1；constant/texture 等是特殊缓存。变量限定符 `__global__`、`__shared__`、local/register 的本质是控制数据放在哪个层次。

Vector addition 图和 kernel code 图要会把索引公式读出来：`i = blockIdx.x * blockDim.x + threadIdx.x`。边界条件页强调线程总数通常向上取整，kernel 内要判断 `i < N`，否则越界。

Matrix multiplication 图里，每个线程计算 C 的一个元素或一个 tile 内元素。地址计算要区分 row-major 下 `A[row * N + k]`、`B[k * N + col]`、`C[row * N + col]`。这为第 7 讲 tiling 做铺垫。

SIMT/warp 图的关键：

- warp 是一组执行同一指令的线程，NVIDIA 常见 32 threads。
- 每个线程有自己的寄存器上下文和 thread id。
- 同一 warp 走不同分支时，硬件要串行执行路径并 mask 掉不活跃线程，称 branch divergence。
- 传统 SIMD 的 vector length 暴露给软件；SIMT 把 SIMD lane 组织隐藏在 warp/thread 模型后面。

H100 图页中的 LDGSTS/TMA、distributed shared memory 属于较新架构细节。考试如果不考前沿，一般只需知道它们都是为了减少全局内存访问开销、提高异步数据搬运和片上数据共享效率。

## 8. 第7讲：GPU Optimization

本讲可考核心：latency hiding/occupancy、memory coalescing、shared memory bank conflict、tiling、SIMT divergence、atomic、streams/async transfer。

关键图页：{key_links(s7, KEY_SLIDES[s7])}。

Occupancy 图要读成“一个 SM 上同时驻留多少 warp”。occupancy 受 threads/block、registers/thread、shared memory/block、SM 最大 blocks/warps 等限制。高 occupancy 不自动等于高性能，但低 occupancy 可能无法隐藏长访存延迟。

Memory coalescing 图：同一 warp 内连续线程访问连续地址，硬件可合并成少数 memory transactions；如果 stride 大、地址散乱或未对齐，会变成多个 transactions，带宽利用率下降。考试常给 `A[threadIdx.x]`、`A[threadIdx.x * stride]` 判断是否 coalesced。

Shared memory bank conflict 图：shared memory 分 bank；同一 warp 多线程访问不同 bank 可并行，访问同一 bank 的不同地址会串行化。例外是 broadcast：多个线程读同一地址通常可广播。优化方法包括 padding、改变数据布局、让连续线程访问连续 bank。

Tiling 图是矩阵乘优化核心。Naive MM 每个 C 元素重复从 global memory 读 A 的一行和 B 的一列；tiled MM 把 A/B 的 tile 先搬到 shared memory，线程块内多次复用。图里的 `__syncthreads()` 用于保证 tile 加载完再计算，以及下一轮覆盖 shared memory 前所有线程都完成本轮计算。

SIMT utilization 图说明分支和 reduction 写法会影响活跃 lane。Naive reduction 用 `if (tid % (2*stride)==0)` 会让活跃线程分散，warp 利用率差；优化写法让活跃线程连续，减少 divergence。Atomic 图强调多个线程对同一地址 atomic 会串行化，histogram 是典型冲突场景。

CUDA streams 图说明一个 stream 内操作有序，不同 stream 可重叠 H2D/D2H transfer 和 kernel execution。是否能重叠取决于硬件 copy engine、数据依赖和任务划分。H100 TMA 属于异步搬运硬件，用于减少搬运指令开销。

## 9. 第8讲：Memory Hierarchy and Caches

本讲可考核心：memory hierarchy、locality、cache hit/miss、address decomposition、direct-mapped/fully-associative/set-associative。

关键图页：{key_links(s8, KEY_SLIDES[s8])}。

Memory hierarchy 图的读法：越靠近 CPU/GPU core 越快、越小、越贵；越远越慢、越大、越便宜。cache 让程序“看起来”拥有又快又大的内存，但前提是 locality。

Locality 图：

- temporal locality：刚访问过的数据很可能很快再次访问，所以 cache 保留最近用过的 block。
- spatial locality：访问某地址附近的数据概率高，所以 cache 按 block/cache line 搬运，而不是只搬一个字节。

Cache abstraction 图要掌握：memory 被分成 blocks，cache 存若干 blocks；访问时先查 tag，hit 则直接用，miss 则从下层取回并可能替换旧 block。

Addressing the cache 图是计算题核心。地址拆成：

```text
---------+-------+--------+
|  tag    | index | offset |
+---------+-------+--------+
```

- offset bits = `log2(block size)`。
- cache blocks `B = C / b`。
- associativity `N`。
- sets `S = B / N`。
- index bits = `log2(S)`。
- tag bits = address bits - index bits - offset bits。

三种组织图：

- direct-mapped：每个 memory block 只能去一个 cache line，硬件简单、命中快，但 conflict miss 多。
- fully associative：block 可放任意位置，冲突少，但要比较所有 tag，硬件复杂。
- set-associative：block 映射到一个 set，可放该 set 的 N 个 way，是折中。

Associativity tradeoff 图要记：提高 associativity 通常降低 conflict miss，但增加 comparator、mux、tag 延迟和能耗，可能拉长 cycle time。所以性能题要同时算 miss rate 和 hit time/cycle time。

## 10. 第9讲：Cache Policies and Coherence

本讲可考核心：replacement policy、write policy、miss classification、cache performance、多核 cache、coherence 基本问题、MSI/MESI、snoop/directory。

关键图页：{key_links(s9, KEY_SLIDES[s9])}。

Replacement 图：

- invalid block 优先替换。
- LRU 近似利用 temporal locality，但精确 LRU 在高 associativity 下硬件昂贵。
- Random/FIFO 简单，可能性能略差但硬件成本低。
- Optimal replacement 需要知道未来，只能作为理论下界。

Write policy 图：

- write-through：写 cache 同时写 lower level，简单、内存较新，但带宽压力大。
- write-back：只写 cache，置 dirty bit，evict 时写回，节省带宽但一致性和替换更复杂。
- write-allocate：write miss 时把 block 读入 cache 后再写，常配 write-back。
- no-write-allocate：write miss 直接写下层，常配 write-through。

Miss classification 图：

- compulsory/cold miss：第一次访问某 block，任何 cache 都避免不了。
- capacity miss：工作集超过 cache 容量，即使 fully associative 也会 miss。
- conflict miss：容量够，但映射到同一 set/line 互相挤掉，提高 associativity 可缓解。

Cache performance 图的题型：平均访问时间 `AMAT = hit time + miss rate * miss penalty`，或按题目措辞用 `hit_rate*hit_time + miss_rate*miss_access_time`。多级 cache 时要逐级展开。第 16 讲 performance/cache 例题已经在 `02` 中详细算过。

多核 cache 图说明 private cache 快但会有重复数据和 coherence 问题；shared cache 容量池化、减少重复，但可能延迟高、带宽争用、互相污染。resource sharing 优点和缺点都要会说。

Coherence 图要先区分两个问题：同一地址可能在多个 private cache 中有副本；一个 core 写后，其他 core 不能继续读旧值。硬件 coherence 要提供 write propagation 和 write serialization。

MSI 状态图：

- I invalid：本 cache 没有有效副本。
- S shared：可能多个 cache 有干净副本，可本地读。
- M modified：唯一且脏，本地可读写，memory 不是最新。

MESI 比 MSI 多 E/exclusive：本 cache 是唯一干净副本。读 miss 后如果没有别人共享，可进 E；E 状态下本地写可静默变 M，不必发 invalidation。这减少了单核/私有数据写时的 bus traffic。

Snoop 图：总线广播所有 coherence 请求，每个 cache 监听 bus。优点简单，bus 给出天然序列化；缺点是广播和单总线不可扩展。Directory 图：每个 cache line 的 directory 记录 sharers/owner/state，请求定向发送给相关节点，更可扩展，但 directory storage 和协议复杂。

## 11. 第10讲：Coherence + Consistency

本讲可考核心：snoop/directory 具体过程、coherence vs consistency、memory barriers、SC/TSO/PSO、store buffer、write coalescing、GPU memory model。

关键图页：{key_links(s10, KEY_SLIDES[s10])}。

Coherence vs consistency 图是必背：

- coherence：不同处理器对同一 memory location 的操作顺序。它是 per-location 的。
- consistency：不同处理器对所有 memory locations 的全局可见顺序。它是 whole-memory ordering contract。

Snoop/direct 例子图中，C1 写 `X=888` 后，其他 cache 对 X 的旧副本要失效或更新；C3 读 X 时可能从 owner cache 或 memory 得到最新值。Directory 例子图中，home node 记录 X 的 owner/sharers，GetS/GetM 请求通过 directory 定向转发，不需要全系统广播。

Sequential consistency 图：每个处理器内部顺序遵守程序顺序，整个多处理器执行结果等价于所有处理器操作按某个单一顺序交织执行。它最容易理解，但限制硬件优化。

Store buffer 图解释 TSO：store commit 到本地 store buffer 后，core 可继续执行后续 load，因此 Store->Load 顺序可能被打破。两个 core 都先 store 再 load 对方变量时，可能都读到旧值，于是两个 critical section 都进入。这不是 cache coherence 错，而是 memory consistency model 允许的重排。

PSO/write coalescing 图：同一 cache line 或 write buffer 中的多个 store 可合并，Store->Store 顺序也可能被打破，以节省带宽。barrier 表展示不同模型需要保留哪些 Load-Load、Load-Store、Store-Store、Store-Load 顺序。

GPU memory model 图说明每个 SM 有自己的 L1/shared memory 和全局 L2/HBM。一个 SM 的写入可能先停留在局部层次，不立即对其他 SM 可见，因此需要合适的 memory fence/barrier 或使用保证可见性的指令/内存空间。

Multi-level caching 图要记设计取舍：L1 小、快、低 associativity，tag/data 常并行访问，受 cycle time 影响大；L2/L3 大、可更高 associativity，延迟不那么关键，可能串行访问 tag/data。上级 cache 会过滤 locality，所以下级看到的访问流不同。

## 12. 第11讲：为什么需要 AI 加速器

本讲可考核心：深度学习算子的计算/访存特性、DSA、AI accelerator vs CPU、cache vs buffer、低精度。

关键图页：{key_links(s11, KEY_SLIDES[s11])}。

VGG19/卷积/全连接/Transformer 图说明深度学习工作负载有固定重复模式：卷积、矩阵乘、向量操作、attention/FFN。分析时看两件事：计算模式是否规则、数据是否可复用。卷积和 GEMM 规则且复用高，非常适合专用阵列和片上 buffer。

DSA 图的核心：CPU 面向通用性，很多面积和能耗用于 branch prediction、cache、复杂控制、异常、权限等；AI accelerator 面向特定领域，把更多资源给矩阵/向量计算、片上 buffer 和数据搬运。

AI accelerator vs CPU 表要掌握：

- on-chip memory：CPU 多用自动 cache，AI accelerator 多用 global buffer/scratchpad。
- instruction issue：CPU 强调 superscalar/OoO，AI accelerator 通常分 Cube/Vector/Scalar/MTE 队列，顺序 issue 较多。
- compute：CPU 有少量通用 ALU/SIMD，AI accelerator 有大量矩阵单元。
- programming：CPU 程序员不用显式管理数据搬运；AI accelerator 性能更依赖显式 tiling、buffer 管理和算子库。

Cache vs buffer 图要会解释：cache 对程序员透明，有 tag、replacement、coherence 等硬件开销，适合不规则访问；buffer/scratchpad 对软件可见，地址空间可与 DDR/HBM 不重合，软件显式搬运，适合规则张量计算，能减少 tag 和替换开销，提高可预测性。

低精度图的直觉：ML 任务对数值误差有一定容忍度，低精度减少存储、带宽和计算能耗。不同层/任务可能需要不同精度。MLWeaving/bit-serial 部分偏研究扩展，期末若不考细节，掌握“低精度提升吞吐和降低带宽压力，但要保证精度/收敛”即可。

## 13. 第12讲：DaVinci、TPU、Systolic Array

本讲可考核心：buffer 数据流、WS/OS/IS/RS、Ascend DaVinci 模块、TPU/systolic array。

关键图页：{key_links(s12, KEY_SLIDES[s12])}。

Cache or Buffer 图延续第 11 讲：AI accelerator 使用 on-chip buffer 的目标是减少 global buffer/HBM 访问。数据流页给出四种 stationary：

- Weight Stationary：weight 留在 PE/local storage 中，输入流过，减少权重读。
- Output Stationary：partial sum/output 留在 PE 中累加，减少中间结果写回。
- Input Stationary：input 留在本地，复用输入。
- Row Stationary：试图在卷积中同时利用 row 方向的 input、weight、partial sum 复用，是一种折中数据流。

Matrix multiplication unit 图：矩阵乘 `C=A*B` 的核心是大量 MAC。增加计算模块不够，必须让数据供得上；否则 roofline 仍会被 memory bandwidth 限制。

Ascend/DaVinci 图要会说模块职责：

- Cube：矩阵乘/卷积等张量核心计算，算力担当。
- Vector：激活、逐元素、归一化、格式转换等向量计算，多面手。
- Scalar：控制、分支、循环、地址和参数计算，司令部。
- MTE/BIU：负责 DDR/HBM、L2、L1/L0/UB 之间的数据搬运。
- Buffer：L0A/L0B/L0C、UB、L1/L2 等承载不同粒度数据复用。

TPU v1 图体现脉动阵列：数据在 PE 阵列中有节奏地流动，每个 PE 做 MAC 并把数据传给邻居。优势是局部通信、规则控制、高复用；缺点是灵活性较差，对数据布局和 tile 大小敏感。TPU v2/v3/v4/v5/v6 演进页如果作为拓展，不必背型号参数，但要知道趋势：训练支持、vector memory/unit、interconnect、更多芯片互连。

Systolic array 计算示例图要能口头模拟：A 的元素从一边流入，B 的元素从另一边流入，每个 PE 每拍接收输入、做乘加、传递数据，经过若干拍后得到 C 的不同元素。卷积转 GEMM 图说明 CNN 也可通过 im2col/矩阵化映射到矩阵乘单元。

Cerebras/WSE 等大芯片页偏拓展，建议知道它代表“把大量 SRAM/compute 放在 wafer-scale 上，减少跨芯片通信”，但考试若明确排除前沿研究，不作为主背内容。

## 14. 第13讲：AI Chip + Runtime + Framework

本讲可考核心：Cambricon DLP-S 架构、ISA 类型、CANN/算子库、Tensor/属性、算子开发方式、图优化、MindSpore 架构。

关键图页：{key_links(s13, KEY_SLIDES[s13])}。

Cambricon DLP-S 架构图要看控制模块、计算模块、SRAM 模块、DMA/访存路径之间的关系。控制模块负责取指、译码、issue queue；计算模块执行深度学习算子；SRAM 模块承载片上数据；执行流程 Step 1-7 展示从取指到数据搬运、计算、写回的顺序。

DLP ISA 图把指令分成 control、data movement、compute、logic。这个分类和 Ascend 的 Scalar/MTE/Cube/Vector 很像：AI 芯片 ISA 不只是算术指令，还要显式表达数据搬运和片上协同。

AI Architecture 图给出层次：AI chip 在底层，CANN/runtime/operator library 在中间，framework 和 parallel training 在上层。考试若问 CANN 作用：向下使能处理器并行加速，向上给框架/开发者提供算子、图引擎、编译和运行接口。

算子概念图要掌握：Tensor 是 n 维数组，具有 shape、dtype、format/layout；属性 attribute 是算子的静态参数；算子库封装常用 NN operator，避免用户每次手写底层搬运和调度。

CANN 算子开发方式比较：

- TBE DSL：Python/DSL，开发效率高，适合规则算子。
- TIK：更接近底层，控制更细，性能潜力高但开发复杂。
- AI CPU：跑在通用控制核上的算子，适合不规则/控制复杂但性能要求不高的部分。

GE/CSE/算子融合图：计算图引擎把框架图转成可优化图。CSE 消除公共子表达式；算子融合把 Conv/BatchNorm/ReLU 等连续算子合并，减少中间结果写回 HBM 再读回的访存开销。第 13 讲第 80 页用 compute complexity vs memory complexity 强调：很多优化不是减少 FLOPs，而是减少 HBM I/O。

MindSpore 架构图属于框架层：MindData、MindIR、MindCompiler、MindRT 等模块分别处理数据、IR、编译和运行。考试一般不要求背完整框图，但要理解框架和 CANN/runtime 的上下关系。

## 15. 第14讲：Parallel Training

本讲是老师点名重点。必须掌握 data/pipeline/tensor parallel 的通信，以及 Ring AllReduce 轮数和通信量。

关键图页：{key_links(s14, KEY_SLIDES[s14])}。

训练示例图从 3 个 linear layer 开始：forward 计算 `Y = XW`，loss 后 backward 计算 `dY`、`dW`，最后 optimizer 更新 W。理解 parallel training 前，必须知道训练中同步的对象通常是 gradient、activation、parameter/optimizer state。

Why distributed training 图：模型变大、batch/token 变多、单卡显存和算力有限，所以需要多卡/多机。A100 block 图用于提醒：单卡内部也有 SM、L2、HBM、NVLink/PCIe 等资源，跨卡通信会成为瓶颈。

Parallelism taxonomy 图：

- Data parallel：每卡有完整模型，处理不同 mini-batch shard；反向后需要合并梯度，典型通信是 AllReduce。
- Pipeline/inter-layer parallel：不同层放不同 worker；相邻 stage 传 activation 和 activation gradient。
- Tensor/intra-layer parallel：同一层权重切到多个 worker；通信取决于按行切还是按列切。

Data parallel weight update 图：每个 worker 本地算梯度，然后所有 worker 求平均/求和，之后每个 worker 用相同 combined gradients 更新自己的完整模型副本。通信可用 AllReduce。

Ring AllReduce 图必须会：

- 数据大小 `M`，GPU 数 `N`。
- 先把数据切成 N 个 chunk，每块 `M/N`。
- ReduceScatter：`N-1` 轮，每轮每 worker 向邻居发送/接收一个 chunk，并累加，结束后每个 worker 持有一个 reduce 完成的 chunk。
- AllGather：`N-1` 轮，每轮传播已 reduce 的 chunk，结束后每个 worker 拥有完整 reduce 结果。
- 总轮数 `2(N-1)`。
- 每个 worker 发送量/接收量都是 `2M(N-1)/N`。
- 每轮有同步，ring 适合有 1D torus/ring 的拓扑；in-switch AllReduce 可减少轮数但依赖网络交换机能力。

Pipeline parallel 图要会读 bubble。N 个 worker、K 个 microbatch/subminibatch 时，GPipe 公式：

```text
fwd+bwd steps = 2(N + K - 1)
total step-slots = 2N(N + K - 1)
idle step-slots = 2N(N - 1)
idle fraction = (N - 1)/(N + K - 1)
```

K 越大 bubble fraction 越小，但 activation memory 和调度复杂度增加。通信是相邻 stage 间的 activations 和 activation gradients，拓扑类似 1D mesh/torus。

Tensor parallel 图是重点中的重点。PPT 的 row-wise/column-wise 以线性层 `Y = XW` 为例：

- Row-wise partitioning：每个 worker 持有一部分 weight rows，输入 X 通常每卡都有完整副本，每卡计算一部分 output activations `Y_i`。下一层如果需要完整 Y，就要 AllGather。PPT 明确写：`Fwd communication: Allgather`。
- Column-wise partitioning：每个 worker 产生对输出的 partial contribution，需要把 partial sums 合并/分散。PPT 明确写：`Fwd communication: ReduceScatter`；如果后续每卡都要完整输出，也可能用 AllReduce/AllGather，按题目要求判断。
- Alternating Partitioning：连续两层交替使用 row-wise 和 column-wise，使 worker i 的输出分片正好成为下一层需要的输入分片，从而两个相邻 layer 之间不通信。到下一组边界仍可能需要 AllReduce。PPT 第 71-73 页就是这个过程。

Transformer memory 图提醒：训练显存不仅是 parameters，还有 gradients、optimizer states、activations。大模型训练常常先被 memory 卡住，再被通信卡住。

ZeRO 图在第 14、15 讲都出现。核心思想：数据并行下每卡冗余保存 optimizer states/gradients/parameters，ZeRO 把这些状态分片存储，减少每卡显存，使更大模型可训。代价是更多 collectives 和通信复杂度。

## 16. 第15讲：ZeRO 与 FlashAttention 的考试边界

关键图页：{key_links(s15, KEY_SLIDES[s15])}。

按老师说明，第 15 讲 FlashAttention 部分不考。因此第 11-27 页在 `05_逐页图文索引.md` 中标为不考，不应作为期末主背内容。

需要保留的是第 3-9 页和前面并行训练的衔接：

- AI system 四组件：storage、computing、model/training、compiling。
- ZeRO：每个 GPU 存 optimizer states 的子集，而不是像普通 data parallel 那样完整复制。
- ZeRO benefit：能训练更大模型。
- ZeRO overhead：典型 PyTorch step 中 forward/backward/optimizer 周围会增加 collectives。
- Batch size limitation：LLM 训练中 token 数、sequence length、batch size 共同决定显存和并行策略。

FlashAttention 页如果你自己感兴趣，可以作为“IO-bound attention 如何通过 tiling/recomputation 降低 HBM 访问”的例子，但不纳入考试重点。

## 17. 第16讲：总复习和四类例题

关键图页：{key_links(s16, KEY_SLIDES[s16])}。

第 16 讲是复习脉络。它把课程压缩成几条主线：

- 性能模型：Amdahl、Roofline、Little、CPI。
- CPU 微结构：single-cycle、multi-cycle、pipeline、hazard、ROB、Tomasula。
- GPU：SIMT、warp、memory hierarchy、coalescing、tiling、occupancy。
- Memory/cache：DRAM、HBM、cache organization、replacement、write policy、coherence、consistency。
- AI accelerator：buffer、dataflow、Ascend/TPU/Cambricon、operator/runtime/framework。
- Parallel training：data/pipeline/tensor parallel、AllReduce、ZeRO。

四道例题的图页入口：

- Roofline：{key_links(s16, [16, 17, 18, 19, 20, 23, 24])}。
- Pipelined/OOO CPU：{key_links(s16, [47, 48, 49, 50, 52, 56, 58, 59, 60, 61, 62])}。
- Performance analysis：{key_links(s16, [64])}。
- Cache：{key_links(s16, [96, 97, 108, 109, 111])}。

考试不会是原题，但稳定能力是：会把图转成公式、表格和状态更新过程。做题时先写约定，例如 miss access time 是否含 hit time、CDB 广播后消费者是否下一周期可执行、commit 是否必须 in-order。题目约定优先于你背的默认答案。

## 18. 面向期末的查漏清单

### 18.1 必须能闭卷解释

- Amdahl：为什么串行部分限制总加速比。
- Roofline：`AI = FLOPs/Bytes`，`Performance <= min(Peak, AI*Bandwidth)`。
- Little：为什么高延迟系统需要高并发。
- ISA vs microarchitecture：软件接口与硬件实现的区别。
- 单周期、多周期、流水线：CPI、cycle time、throughput 的权衡。
- 三类 hazard：structural/data/control。
- RAW/WAR/WAW：真依赖和假依赖。
- ROB：乱序完成、顺序提交、precise exception。
- Tomasula：RAT、RS、CDB、tag/value/valid 的更新规则。
- SIMD/SIMT/SPMD：编程模型和执行模型差异。
- GPU 优化：occupancy、coalescing、bank conflict、tiling、divergence、atomic。
- Memory hierarchy：locality、cache block、tag/index/offset。
- Cache organization：direct/full/set associative。
- Cache policy：LRU/random/FIFO、write-back/write-through、write-allocate/no-write-allocate。
- Coherence vs consistency：同一地址顺序 vs 全局内存顺序。
- MSI/MESI：状态含义与 E 状态优势。
- Snoop vs directory：广播简单但不可扩展；directory 定向可扩展但复杂。
- AI accelerator：DSA、buffer、dataflow、systolic array、低精度。
- Ascend：Cube/Vector/Scalar/MTE/Buffer。
- CANN/framework：operator library、Tensor/attribute、TBE/TIK/AI CPU、GE、operator fusion。
- Parallel training：data/pipeline/tensor parallel 的切分对象和通信对象。
- Ring AllReduce：`2(N-1)` 轮，每 worker `2M(N-1)/N` 发送/接收。
- ZeRO：切 optimizer/gradient/parameter 状态以省显存，代价是通信。

### 18.2 必须能看图做题

- 给 Roofline 图或机器参数，判断 memory-bound/compute-bound。
- 给流水线图，指出 stall、bubble、forwarding 的位置。
- 给 Tomasula RAT/RS 表，更新 issue 和 broadcast 后的字段。
- 给 cache 地址序列，算 block、set、tag、hit/miss 和 miss 类型。
- 给 MSI/MESI 状态转移表，判断 bus action。
- 给 Ring AllReduce 图，写出 ReduceScatter 和 AllGather 的轮数/通信量。
- 给 row-wise/column-wise tensor parallel 图，判断 AllGather、ReduceScatter 或 AllReduce。

### 18.3 可降优先级但不能完全陌生

- 具体芯片历史型号参数，如 Piranha/Niagara/POWER 的年份和所有规格。
- RAIDR、MLWeaving、Cerebras、FlashAttention 主体等研究拓展。老师说明显前沿拓展不考，但这些页常承载“为什么存储/通信重要”的直觉，所以至少知道它们在解决什么瓶颈。
"""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "04_逐讲图示与细节补充讲义.md").write_text(build_visual_notes(), encoding="utf-8")
    (OUT / "05_逐页图文索引.md").write_text(build_page_index(), encoding="utf-8")
    print("wrote", OUT / "04_逐讲图示与细节补充讲义.md")
    print("wrote", OUT / "05_逐页图文索引.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
