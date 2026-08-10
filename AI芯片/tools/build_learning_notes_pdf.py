from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_course_pdfs import NOTES, OUT, STY, header_footer
from build_single_lecture_pdf import markdown_to_flowables_text, strip_link_noise
from build_full_detail_pdf import (
    is_admin,
    is_explicitly_excluded,
    is_extension,
    load_deck,
    normalize,
    visible_slide_text,
)
import build_visual_review_notes as visual


SOURCE_MD = NOTES / "10_完整细致学习笔记版.md"
OUTPUT_PDF = OUT / "人工智能芯片与系统_完整细致学习笔记版.pdf"


LECTURE_SECTION_TITLES = [
    "第1讲：从系统到 CPU 微结构",
    "第2讲：Pipeline Hazard 与 ROB",
    "第3讲：Tomasula、RAT、RS",
    "第4讲：Superscalar、SIMD、多线程、多核",
    "第5讲：Memory Overview、DRAM、HBM、Refresh",
    "第6讲：GPU Architecture",
    "第7讲：GPU Optimization",
    "第8讲：Memory Hierarchy and Caches",
    "第9讲：Cache Policies and Coherence",
    "第10讲：Coherence + Consistency",
    "第11讲：为什么需要 AI 加速器",
    "第12讲：DaVinci、TPU、Systolic Array",
    "第13讲：AI Chip + Runtime + Framework",
    "第14讲：Parallel Training",
    "第15讲：ZeRO 与 FlashAttention 的考试边界",
    "第16讲：总复习和四类例题",
]


def read_note(name: str) -> str:
    return (NOTES / name).read_text(encoding="utf-8")


def replace_top_heading(text: str, heading: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    replaced = False
    for line in lines:
        if line.startswith("# ") and not replaced:
            out.append("# " + heading)
            replaced = True
        else:
            out.append(line)
    return "\n".join(out)


def extract_visual_section(index: int) -> str:
    text = read_note("04_逐讲图示与细节补充讲义.md")
    heading = f"## {index + 2}. {LECTURE_SECTION_TITLES[index]}"
    start = text.find(heading)
    if start < 0:
        return ""
    next_match = re.search(r"\n## \d+\. ", text[start + 1 :])
    end = start + 1 + next_match.start() if next_match else len(text)
    section = strip_link_noise(text[start:end]).strip()
    section = re.sub(r"^## \d+\. ", "### 图表和结构该怎么理解：", section)
    return section


def prose_join(parts: list[str]) -> str:
    text = "；".join(p for p in parts if p)
    text = re.sub(r"；{2,}", "；", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def flatten_learning_item(item) -> list[str]:
    if item is None:
        return []
    if isinstance(item, str):
        return [normalize(item)]
    if isinstance(item, dict):
        if "table" in item:
            rows: list[str] = []
            for row in item["table"]:
                cells = [normalize(c) for c in row if normalize(c)]
                if cells:
                    rows.append(" | ".join(cells))
            return ["表格：" + "；".join(rows)] if rows else []
        out: list[str] = []
        for value in item.values():
            out.extend(flatten_learning_item(value))
        return out
    if isinstance(item, list):
        out: list[str] = []
        for value in item:
            out.extend(flatten_learning_item(value))
        return out
    return [normalize(item)]


def visible_slide_text_learning(slide: dict) -> str:
    raw: list[str] = []
    for item in slide.get("shape_items", []):
        raw.extend(flatten_learning_item(item))
    if not raw:
        for item in slide.get("all_text", []):
            raw.extend(flatten_learning_item(item))

    title = normalize(slide.get("title", ""))
    seen: set[str] = set()
    kept: list[str] = []
    for piece in raw:
        piece = normalize(piece)
        if not piece or piece == title or re.fullmatch(r"\d{1,3}", piece):
            continue
        key = piece.lower()
        if key in seen:
            continue
        seen.add(key)
        kept.append(piece)

    text = "；".join(kept)
    text = re.sub(r"；{2,}", "；", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:3200]


def is_title_only_slide(slide: dict, body: str) -> bool:
    n = int(slide["number"])
    if n != 1:
        return False
    blob = (normalize(slide.get("title", "")) + " " + body).lower()
    return "prof." in blob or "zhejiang university" in blob or "浙大" in blob


def slide_learning_paragraph(stem: str, deck_title: str, slide: dict, key_pages: set[int]) -> str | None:
    n = int(slide["number"])
    if is_explicitly_excluded(stem, n) or is_admin(slide):
        return None

    title = normalize(slide.get("title", "")) or f"第 {n} 页"
    body = visible_slide_text(slide)
    if not body and n not in key_pages:
        return None

    lead = f"围绕《{title}》（原 PPT 第 {n} 页）"
    emphasis: list[str] = []
    if n in key_pages:
        emphasis.append("这是本讲需要重点理解的一页")
    image_count = int(slide.get("image_count", 0))
    table_count = int(slide.get("table_count", 0))
    if image_count:
        emphasis.append(f"页面包含 {image_count} 个图形元素，读的时候要关注层次、箭头、数据流、状态变化或硬件模块之间的连接")
    if table_count:
        emphasis.append(f"页面包含 {table_count} 个表格，表格里的字段名、状态名、通信阶段或硬件参数都应当作为细节记住")

    if is_extension(slide):
        prefix = (
            f"{lead}，课程把它作为拓展边界来帮助理解系统瓶颈。这里不要求把具体型号、论文结果或历史参数当作考试主背内容，"
            "但它仍然服务于课程主线：说明某类系统瓶颈为什么重要。"
        )
        detail = body
    else:
        prefix = f"{lead}，课程讲解的具体内容是"
        detail = body

    extra = prose_join(emphasis)
    if extra:
        return f"{prefix}：{detail}。这部分的读图/读表要求是：{extra}。"
    return f"{prefix}：{detail}。"


def slide_learning_fragment(stem: str, slide: dict, key_pages: set[int], position: int) -> str | None:
    n = int(slide["number"])
    if is_explicitly_excluded(stem, n) or is_admin(slide):
        return None

    title = normalize(slide.get("title", "")) or "这一页"
    body = visible_slide_text_learning(slide)
    if is_title_only_slide(slide, body):
        return None
    if not body and n not in key_pages:
        return None

    starters = [
        "课程先把",
        "接着 PPT 把",
        "随后这一页把",
        "这一小段继续说明",
        "再往下，材料把",
    ]
    starter = starters[position % len(starters)]
    if body:
        fragment = f"{starter}“{title}”展开为：{body}"
    else:
        fragment = f"{starter}“{title}”作为重点图页，需要结合前后文理解其中的数据流和状态变化"

    details: list[str] = []
    if n in key_pages:
        details.append("这一页在总复习或图示补充中被标为重点，读完后要能不用原图复述它的因果关系")
    image_count = int(slide.get("image_count", 0))
    table_count = int(slide.get("table_count", 0))
    if image_count:
        details.append(f"图中有 {image_count} 个图形元素，重点不是背形状，而是读出模块、箭头、数据生产者/消费者和瓶颈")
    if table_count:
        details.append(f"表格有 {table_count} 个，字段名、状态名、轮次、tag/value/valid 或通信阶段都可能直接变成题目条件")
    if is_extension(slide):
        details.append("这一页属于拓展边界，考试一般不背论文或型号参数，但要知道它想说明哪类系统瓶颈")

    if details:
        fragment += "；读图/读表时要同时记住：" + "；".join(details)
    return fragment + "。"


def make_slide_groups(stem: str, slides: list[dict], key_pages: set[int]) -> list[list[dict]]:
    groups: list[list[dict]] = []
    current: list[dict] = []
    current_len = 0

    for slide in slides:
        fragment = slide_learning_fragment(stem, slide, key_pages, len(current))
        if not fragment:
            continue
        projected = current_len + len(fragment)
        if current and (len(current) >= 3 or projected > 5200):
            groups.append(current)
            current = []
            current_len = 0
        current.append(slide)
        current_len += len(fragment)

    if current:
        groups.append(current)
    return groups


def page_span(group: list[dict]) -> str:
    nums = [int(slide["number"]) for slide in group]
    if len(nums) == 1:
        return f"p.{nums[0]}"
    if nums == list(range(nums[0], nums[-1] + 1)):
        return f"p.{nums[0]}-p.{nums[-1]}"
    return "p." + "、".join(str(n) for n in nums)


def slide_group_paragraph(stem: str, group: list[dict], key_pages: set[int], group_index: int) -> str:
    titles = [normalize(slide.get("title", "")) for slide in group if normalize(slide.get("title", ""))]
    title_text = "、".join(titles[:3])
    if len(titles) > 3:
        title_text += "等"
    openings = [
        "这一组内容可以按一条连续链来读",
        "接下来这一组页要连起来理解",
        "这里 PPT 从一个角度转到另一个角度",
        "这一段讲义把几页内容合在一起看",
    ]
    opening = openings[group_index % len(openings)]
    fragments = [
        slide_learning_fragment(stem, slide, key_pages, i) or ""
        for i, slide in enumerate(group)
    ]
    body = " ".join(fragments)
    return f"{opening}，主题是“{title_text}”。{body}（对应 {page_span(group)}。）"


def build_review_spine() -> str:
    return """# 第三部分：第 16 讲总复习先搭起来的主线

第 16 讲不是单独的一次新课，而是把前 15 讲重新压缩成期末复习主线。读完整讲时，要把它当成“哪些内容会被老师认为是课程骨架”的提示：它反复出现的 Amdahl、Roofline、Little、CPI、AMAT，对应第 1 讲和存储/cache 讲里的性能分析；它复习的 single-cycle、multi-cycle、pipeline、hazard、ROB 和 Tomasula，对应第 1-3 讲的 CPU 微结构；它复习的 SIMD、SIMT、warp、coalescing、bank conflict、tiling、occupancy，对应第 4、6、7 讲；它复习的 DRAM、HBM、cache mapping、replacement、write policy、coherence、consistency，对应第 5、8、9、10 讲；它复习的 buffer、dataflow、systolic array、Ascend/TPU/Cambricon、CANN/MindSpore，对应第 11-13 讲；它复习的 data parallel、pipeline parallel、tensor parallel、AllReduce、ReduceScatter、AllGather、Alternative/Alternating Partitioning 和 ZeRO，对应第 14-15 讲。

最后一讲的四类例题也要这样读：Roofline 题不是背某一张图，而是会把 total FLOPs、total memory bytes、AI、peak compute 和 bandwidth 放进同一个上界判断；pipelined CPU 题不是背某个周期表，而是会按 IF/ID/EX/MEM/WB、stall、bubble、forwarding、ROB/Tomasula 状态更新去推；performance analysis 题不是只套一个公式，而是会区分 latency、throughput、CPI、Little 定律、Amdahl 定律分别回答什么问题；cache 题不是只会算 tag/index/offset，而是会把 placement、replacement、write policy、AMAT、coherence/consistency 和状态转移连起来。考试不一定出原题，但一定会考这种“把图读成公式、把表读成状态更新、把结构读成瓶颈”的能力。
"""


def build_lecture_notes() -> str:
    lines: list[str] = [
        "# 第四部分：按 16 次课顺序学习的完整细致笔记",
        "",
        "这一部分按 PPT 原始讲课顺序写成连续学习笔记。相邻页会被合并成一段来讲，页内文字、表格字段、图示标签和状态变化会融进正文，目的是让你像重新听课一样，从课程动机、概念、图示、表格、公式、硬件结构、状态更新和通信过程一路学下来。",
    ]
    for idx, (stem, deck_title) in enumerate(visual.DECKS):
        data = load_deck(stem)
        key_pages = set(visual.KEY_SLIDES.get(stem, []))
        lines.extend(["", f"## {deck_title}", ""])

        visual_section = extract_visual_section(idx)
        if visual_section:
            lines.append(visual_section)
            lines.append("")

        lines.append(
            "下面进入这一讲的顺序笔记。凡是涉及图或表，都按“结构是什么、数据怎么流、状态什么时候更新、瓶颈在哪里、考试会怎么问”来读；明显拓展内容只保留其说明的瓶颈，不展开成主背知识。"
        )
        lines.append("")

        for group_index, group in enumerate(make_slide_groups(stem, data["slides"], key_pages)):
            lines.append(slide_group_paragraph(stem, group, key_pages, group_index))
            lines.append("")

        if stem == "15-flashattention43":
            lines.append(
                "第 15 讲后半部分的 FlashAttention 主体按照老师说明不考，所以学习笔记只保留 ZeRO、AI system 组成、batch size limitation 和并行训练衔接。FlashAttention 的 IO-bound attention、tiling、online softmax、recomputation、Hopper/Blackwell 优化等内容不作为期末主背。"
            )

    return "\n".join(lines).strip()


def build_markdown() -> str:
    intro = """# 人工智能芯片与系统：完整细致学习笔记版

这版不是清单，也不是索引，而是一份从零开始读的课程学习笔记。它保留 08 版的体系化讲解、04 版的图示解释、02 版的例题方法，并把 PPT 逐页抽取出的细碎知识点改写成按讲课顺序展开的连续笔记。

考试边界仍按老师说明执行：第 15 讲 FlashAttention 主体不考；明显研究拓展只保留它说明的系统瓶颈，不要求背论文细节、型号参数或历史参数。除此之外，课程主线中的概念、公式、图中标签、表格字段、状态变化、通信过程和易错点都尽量融入正文。
"""

    core = replace_top_heading(strip_link_noise(read_note("01_完整零基础讲义.md")), "第一部分：先建立全课程知识骨架")
    examples = replace_top_heading(strip_link_noise(read_note("02_重点题型与例题详解.md")), "第二部分：考试题型中的知识如何使用")
    review_spine = build_review_spine()
    lectures = build_lecture_notes()
    final = """# 第五部分：读完以后如何确认自己真的学会了

读这份笔记时，不要只看“覆盖了哪些页”，而要检查自己能不能把每一块知识讲出来。性能模型部分要能解释 Amdahl、Roofline、Little、CPI 和 AMAT 的使用场景；CPU 部分要能从单周期、多周期、流水线走到 ROB 和 Tomasula；存储部分要能从 SRAM/DRAM/HBM 走到 cache、coherence 和 consistency；GPU 部分要能把 SIMT、warp、coalescing、bank conflict、tiling、occupancy 串起来；AI 加速器部分要能解释 buffer、dataflow、systolic array、低精度、Ascend/TPU/CANN/MindSpore；并行训练部分要能把 data parallel、pipeline parallel、tensor parallel、AllReduce、ReduceScatter、AllGather、Alternative/Alternating Partitioning 和 ZeRO 讲清楚。
"""
    text = "\n\n".join([intro, core, examples, review_spine, lectures, final])
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def build_pdf(markdown: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=14 * mm,
        leftMargin=14 * mm,
        topMargin=15 * mm,
        bottomMargin=17 * mm,
        title="人工智能芯片与系统完整细致学习笔记版",
        author="Codex",
    )
    max_w = A4[0] - doc.leftMargin - doc.rightMargin
    story = [
        Paragraph("人工智能芯片与系统", STY["title"]),
        Paragraph("完整细致学习笔记版", STY["title"]),
        Spacer(1, 10),
        Paragraph("从零开始学习用：按课程顺序连续讲解，细碎知识点融入正文，不作为逐页查找清单。", STY["body"]),
        Spacer(1, 12),
    ]
    story.extend(markdown_to_flowables_text(markdown, max_w))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return OUTPUT_PDF


def main() -> int:
    markdown = build_markdown()
    SOURCE_MD.write_text(markdown, encoding="utf-8")
    print(SOURCE_MD)
    print(build_pdf(markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
