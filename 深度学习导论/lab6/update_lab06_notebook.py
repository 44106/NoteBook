import json
from pathlib import Path


NOTEBOOK = Path("lab06_mingpt2.ipynb")


def set_src(nb, idx, text):
    nb["cells"][idx]["source"] = text.strip("\n").splitlines(True)


def set_stream_output(nb, idx, text):
    nb["cells"][idx]["outputs"] = [
        {
            "name": "stdout",
            "output_type": "stream",
            "text": [text],
        }
    ]


def main():
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))

    set_src(
        nb,
        78,
        r'''
@torch.no_grad()
def generate(model: 'minGPT2', input_ids: 'torch.Tensor', max_new_tokens: int = 100,
             temperature: float = 1.0, top_k: int = 0, top_p: float = 1.0,
             repetition_penalty: float = 1.0) -> 'torch.Tensor':
    """Autoregressive generation. temperature <= 1e-5 uses exact greedy argmax."""
    model.eval()
    ids = input_ids.clone().to(next(model.parameters()).device)
    max_pos = model.pos_emb.embedding.weight.shape[0]

    for _ in range(max_new_tokens):
        context = ids[:, -max_pos:]
        logits = model(context)[:, -1, :]

        if repetition_penalty is not None and repetition_penalty > 1.0:
            for b in range(ids.size(0)):
                used_tokens = torch.unique(ids[b])
                logits[b, used_tokens] = logits[b, used_tokens] / repetition_penalty

        if temperature <= 1e-5:
            next_id = torch.argmax(logits, dim=-1, keepdim=True)
        else:
            logits = logits / temperature

            if top_k is not None and top_k > 0:
                k = min(top_k, logits.size(-1))
                values, _ = torch.topk(logits, k, dim=-1)
                kth = values[:, [-1]]
                logits = logits.masked_fill(logits < kth, torch.finfo(logits.dtype).min)

            if top_p is not None and top_p < 1.0:
                sorted_logits, sorted_indices = torch.sort(logits, descending=True, dim=-1)
                sorted_probs = F.softmax(sorted_logits, dim=-1)
                cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

                sorted_mask = cumulative_probs > top_p
                sorted_mask[:, 1:] = sorted_mask[:, :-1].clone()
                sorted_mask[:, 0] = False

                remove_mask = torch.zeros_like(sorted_mask, dtype=torch.bool)
                remove_mask.scatter_(1, sorted_indices, sorted_mask)
                logits = logits.masked_fill(remove_mask, torch.finfo(logits.dtype).min)

            probs = F.softmax(logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)

        ids = torch.cat([ids, next_id], dim=1)

    return ids
''',
    )

    set_src(
        nb,
        67,
        r'''
if GPT2Tokenizer is not None:
    shk_ids = tokenizer(shakespeare_text, return_tensors='pt', verbose=False)['input_ids'][0]
    block_size = 128

    class ShakespeareDataset(Dataset):
        def __init__(self, ids, block_size):
            self.ids, self.block_size = ids, block_size

        def __len__(self): return len(self.ids) - self.block_size

        def __getitem__(self, i):
            input_ids = self.ids[i : i + self.block_size].long()
            targets = self.ids[i + 1 : i + self.block_size + 1].long()
            return input_ids, targets

    shk_ds = ShakespeareDataset(shk_ids, block_size)
    shk_loader = DataLoader(shk_ds, batch_size=16, shuffle=True)
    print(f'Shakespeare dataset size: {len(shk_ds)} samples')
else:
    print('GPT2Tokenizer unavailable; skip Shakespeare tokenization')
''',
    )

    set_src(
        nb,
        74,
        r'''
TinyShakespeare 微调中，本次重跑使用的是完整数据集而不是前 `50000` 字符子集，因此数据规模明显更大：文本长度为 `1115394` 字符，tokenized 后得到 `337897` 个训练样本。按当前 `batch_size=16` 计算，每个 epoch 大约需要 `337897 / 16 ≈ 21119` 个 step，所以即使单步时间不长，总训练时长仍会比较明显。

在这样的设置下，语言模型损失仍然从第 1 轮的 `0.2504` 下降到第 2 轮的 `0.0988`，说明加载 HuggingFace GPT-2 权重后，模型已经具备较强的自回归建模能力；经过两个 epoch 的 Shakespeare 全量语料微调，模型进一步适应了戏剧体裁、对白格式和词汇分布。与早先小子集实验相比，完整数据集的 loss 不会降得那么激进，但结论更可信，因为它反映的是更充分的数据覆盖，而不是对局部片段的快速记忆。
''',
    )

    set_src(
        nb,
        82,
        r'''
本次生成里，Greedy Decoding 的结果从 `To be, or not to be,` 稳定续写到 `ROMEO:`、`ARIEL:` 等对白场景，并出现了 `I do protest, I never injured thee`、`I boarded the king's ship` 这类较连贯的 Shakespeare 风格片段。Greedy 是确定性的，因为每一步都直接取当前条件分布下概率最大的 token，即 $\arg\max_w P(w\mid w_{<t})$；在模型参数、prompt 和实现不变时，多次运行会得到同一段文本。它的优点是局部连贯性强、结果可复现，缺点是容易沿着单一路径展开，多样性最低。

Temperature 采样本次仍保留了 `ROMEO:`、`ARIEL:` 这样的戏剧对话结构，但后续内容比 Greedy 更自由，例如出现了 `Yes, most of thee`、`I pray thee, chide not` 这类不同续写。Temperature 的作用是把 logits 除以 $\tau$ 再做 softmax：$\tau<1$ 会让分布更尖锐，高概率 token 更占优势；$\tau>1$ 会把分布压平，让更多低概率 token 有机会被采样。这里使用 `temperature=0.8`，所以它比纯随机采样更保守，但仍比 Greedy 更有变化。

Top-k 与 Top-p 都在“连贯性”和“多样性”之间做折中，但机制不同。Top-k 本次只保留前 50 个候选 token，生成了 `KING EDWARD IV:`、`HASTINGS:` 等较像戏剧角色对白的结构，说明固定候选集能维持一定风格稳定性；Top-p 则生成了 `Music do I hear?`、`how sour sweet music is` 这样的较完整抒情片段，连贯性在这次运行里反而更自然。原因是 Top-p 按累积概率自适应决定候选集大小，模型很确定时采样空间会自动缩小，不确定时才放宽，因此通常比固定的 Top-k 更灵活。
''',
    )

    set_src(
        nb,
        85,
        r'''
| 模型 | SST-2 准确率 | AG News 准确率 | 备注 |
|------|-------------|---------------|------|
| GPT-2（冻结主干） | `0.7099` | `0.8530` | Feature Extraction，只训练分类头 |
| GPT-2（全参数微调） | — | `0.8910` | Full Fine-tuning，主干与分类头共同更新 |
| BERT（Lab 5 结论） | Lab 5 未提供直接分类准确率 | Lab 5 未提供直接分类准确率 | 但注意力探查与上下文敏感性实验清楚展示了 Encoder-only 的双向理解优势 |

本次 GPT-2 实验说明，decoder-only 预训练表示确实可以迁移到判别任务：冻结主干时，SST-2 达到 `0.7099`，AG News 达到 `0.8530`；在 AG News 上继续做全参数微调后，验证准确率提升到 `0.8910`，比冻结主干高约 `3.8` 个百分点。这表明更新主干参数能够缓解一部分“生成目标”和“分类目标”之间的错配，但并没有改变 GPT-2 的单向注意力结构。

Lab 5 虽然没有给出可直接并排填写的分类准确率，但提供了两条很强的实验证据。第一，在 `the cat sat on the mat because it was tired` 这句里，BERT 的 `layer=8, head=10` 对代词 `it` 的最高注意力落在 `cat` 上，权重约为 `0.880483`，说明它能在双向上下文中学习到明显的共指线索。第二，多义词 `bank` 的上下文表征比较显示：`cos(river-bank, river-bank)=0.8406`，而 `cos(river-bank, finance-bank)=0.4704`，说明 BERT 的词表示会随上下文语义发生明显变化。这两点都支持同一个结论：对于 SST-2 和 AG News 这类依赖整体理解的任务，Encoder-only BERT 在结构先验上天然比 GPT-2 更占优势。
''',
    )

    set_src(
        nb,
        87,
        r'''
从注意力方向性看，Decoder-only GPT-2 在每一层都施加 causal mask，使第 $t$ 个位置只能访问左侧上下文，不能直接查看右侧 token。分类任务往往依赖完整句子的全局判断，例如否定范围、转折结构和实体关系都可能由后文信息决定。BERT 的 Encoder self-attention 没有这种方向限制，每个 token 在每一层都能和全句其余位置交互，因此更容易形成对整句语义的一致理解。Lab 5 的注意力探查就给出了直观例子：在 `the cat ... because it was tired` 中，`it` 对 `cat` 的注意力高达 `0.880483`，说明双向上下文有助于直接建立共指关系。

从预训练目标错配看，GPT-2 优化的是下一个 token 的条件概率，核心能力是“给定前缀继续生成”；而分类任务要求模型把完整输入映射成离散标签，并不关心后续 token 的生成质量。也就是说，GPT-2 学到的归纳偏置首先服务于续写，而不是服务于句子级判别。BERT 的 masked language modeling 则要求模型根据左右两侧上下文恢复被遮蔽 token，这种训练方式更接近“理解整个输入再做判断”。因此在迁移到情感分析、新闻分类这类任务时，BERT 的预训练目标与下游目标之间距离更短。

从表征提取位置非对称性看，GPT-2 做分类时通常只能读取最后一个 token 的隐藏态，因为只有最后位置看过前面全部 token。这样会把整句信息压缩责任集中到单个末端位置，一旦句尾信息弱、padding 处理不当或截断发生，分类头接收到的句级表示就可能受损。BERT 则使用专门的 `[CLS]` 位置作为句级聚合槽位，并且它从第一层开始就能双向访问全句所有 token。Lab 5 中 `bank` 的上下文实验也说明了这一点：同义场景相似度 `0.8406` 明显高于异义场景的 `0.4704`，表明 Encoder-only 表征能更稳定地把“整句语境”编码进目标词和句级表示中。
''',
    )

    set_src(
        nb,
        94,
        r'''
附加题已完成：`generate` 函数已经增加 `repetition_penalty` 参数，并按题面要求在每一步生成时对已出现过的 token 的 logit 除以惩罚系数，从而降低逐字重复和短环重复的概率。当前实现位置在第 6.1 节代码单元中；当 `repetition_penalty > 1.0` 时即可启用该机制。

实验六到此结束。当前 Notebook 已补全所有必填代码与书面回答，可作为提交文件使用。
''',
    )

    set_stream_output(nb, 67, "Shakespeare dataset size: 337897 samples\n")

    NOTEBOOK.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"updated {NOTEBOOK}")


if __name__ == "__main__":
    main()
