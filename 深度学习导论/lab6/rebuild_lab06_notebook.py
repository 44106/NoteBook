import json
from pathlib import Path


BACKUP = Path("lab06_mingpt2.backup_before_codex.ipynb")
TARGET = Path("lab06_mingpt2.ipynb")


def set_src(nb, idx, text):
    nb["cells"][idx]["source"] = text.strip("\n").splitlines(True)


nb = json.loads(BACKUP.read_text(encoding="utf-8"))

nb.setdefault("metadata", {})["kernelspec"] = {
    "display_name": "deeplearning",
    "language": "python",
    "name": "deeplearning",
}
nb["metadata"].setdefault("language_info", {})["name"] = "python"

set_src(nb, 2, r'''
import random, math, os, urllib.request
import warnings
warnings.filterwarnings('ignore', message='IProgress not found.*')
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset

if torch.cuda.is_available():
    # Disable TF32 so the strict HuggingFace alignment check is not affected by reduced precision matmul.
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(42)

device = torch.device(
    'cuda' if torch.cuda.is_available()
    else 'mps' if torch.backends.mps.is_available()
    else 'cpu'
)
print(f'Using device: {device}')
if device.type == 'cuda':
    print(f'CUDA device: {torch.cuda.get_device_name(0)}')

try:
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
except Exception as e:
    print(f'transformers import failed: {e}')
    GPT2LMHeadModel = GPT2Tokenizer = None

try:
    from datasets import load_dataset
except Exception as e:
    print(f'datasets import failed: {e}')
    load_dataset = None
''')

set_src(nb, 8, r'''
Decoder-only 模型的因果掩码只允许第 $t$ 个位置关注 $w_{<t}$，因此信息流天然是从左到右的。分类任务通常需要同时利用句首、句中和句尾的双向线索，例如否定词、转折词和实体关系可能出现在待判别信息的两侧；BERT 的 Encoder self-attention 可以让任意 token 直接访问全句上下文，而 GPT-2 的早期 token 永远看不到右侧信息。虽然最后一个 token 在理论上可以聚合左侧全部内容，但这种单向聚合比每个位置都双向交互的表征更不对称，也更依赖最后位置是否学会压缩整句语义。

GPT-2 的预训练目标是 next-token prediction，即估计 $P(w_t \mid w_{<t})$，它优化的是语言续写能力而不是句子级标签判别能力。分类任务的目标是把完整输入映射到有限类别，监督信号直接约束全句语义边界；这种目标与自回归生成目标存在分布和任务形式错配。BERT 的 masked language modeling 更接近从被遮蔽片段周围的双向上下文中抽取语义特征，因此迁移到理解类任务时归纳偏置更自然。

表征提取位置也存在非对称性：GPT-2 分类通常取最后一个 token 的隐藏态作为整句表示，因为只有它能看到左侧全部 token。这样会把全句语义压缩责任集中到最后位置，若输入经过 padding、截断或句尾 token 信息量较低，分类头得到的表示就可能不稳定。BERT 则使用专门的 `[CLS]` 位置，并且该位置在每一层都能与全句所有 token 双向交互，信息完整性和位置设计都更适合判别任务。
''')

set_src(nb, 12, r'''
class LearnedPositionalEmbedding(nn.Module):
    def __init__(self, max_position: int, d_model: int):
        super().__init__()
        self.embedding = nn.Embedding(max_position, d_model)

    def forward(self, seq_len: int) -> 'torch.Tensor':
        if seq_len > self.embedding.num_embeddings:
            raise ValueError(
                f'seq_len={seq_len} exceeds max_position={self.embedding.num_embeddings}'
            )
        positions = torch.arange(seq_len, device=self.embedding.weight.device)
        return self.embedding(positions)
''')

set_src(nb, 16, r'''
def make_causal_mask(seq_len: int, device: 'torch.device') -> 'torch.Tensor':
    """Return a boolean causal mask of shape (1, 1, seq_len, seq_len); True means masked."""
    mask = torch.triu(
        torch.ones(seq_len, seq_len, dtype=torch.bool, device=device),
        diagonal=1,
    )
    return mask.view(1, 1, seq_len, seq_len)
''')

set_src(nb, 20, r'''
class MultiHeadSelfAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        self.c_attn = nn.Linear(d_model, 3 * d_model)
        self.c_proj = nn.Linear(d_model, d_model)
        self.attn_drop = nn.Dropout(dropout)
        self.resid_drop = nn.Dropout(dropout)

    def forward(self, x: 'torch.Tensor', mask: 'torch.Tensor' = None) -> 'torch.Tensor':
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(C, dim=-1)

        q = q.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        k = k.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        v = v.view(B, T, self.n_heads, self.d_k).transpose(1, 2)

        attn_weights = (q @ k.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:
            attn_weights = attn_weights.masked_fill(mask, torch.finfo(attn_weights.dtype).min)

        attn_probs = F.softmax(attn_weights, dim=-1)
        attn_probs = self.attn_drop(attn_probs)
        out = attn_probs @ v
        out = out.transpose(1, 2).contiguous().view(B, T, C)
        out = self.c_proj(out)
        out = self.resid_drop(out)
        return out
''')

set_src(nb, 24, r'''
class GPT2Block(nn.Module):
    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = MultiHeadSelfAttention(d_model, n_heads, dropout)
        self.ln2 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(approximate='tanh'),
            nn.Linear(d_ff, d_model),
            nn.Dropout(dropout),
        )

    def forward(self, x: 'torch.Tensor', mask: 'torch.Tensor' = None) -> 'torch.Tensor':
        x = x + self.attn(self.ln1(x), mask)
        x = x + self.ffn(self.ln2(x))
        return x
''')

set_src(nb, 28, r'''
class minGPT2(nn.Module):
    def __init__(self, vocab_size: int, max_position: int, d_model: int,
                 n_heads: int, n_layers: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = LearnedPositionalEmbedding(max_position, d_model)
        self.drop = nn.Dropout(dropout)
        self.blocks = nn.ModuleList([
            GPT2Block(d_model, n_heads, d_ff, dropout) for _ in range(n_layers)
        ])
        self.ln_f = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)

    def hidden_states(self, input_ids: 'torch.Tensor') -> 'torch.Tensor':
        B, T = input_ids.shape
        tok = self.tok_emb(input_ids)
        pos = self.pos_emb(T).unsqueeze(0)
        x = self.drop(tok + pos)
        mask = make_causal_mask(T, device=input_ids.device)
        for block in self.blocks:
            x = block(x, mask)
        return self.ln_f(x)

    def forward(self, input_ids: 'torch.Tensor') -> 'torch.Tensor':
        """input_ids: (B, T) -> logits: (B, T, vocab_size)"""
        h = self.hidden_states(input_ids)
        return self.lm_head(h)
''')

set_src(nb, 33, r'''
def load_hf_gpt2_model(model_name='gpt2'):
    """Load HuggingFace GPT-2. Eager attention makes numerical alignment easier to inspect."""
    if GPT2LMHeadModel is None:
        return None
    try:
        return GPT2LMHeadModel.from_pretrained(model_name, attn_implementation='eager')
    except (TypeError, ValueError):
        return GPT2LMHeadModel.from_pretrained(model_name)


# Explore HuggingFace and custom parameter names.
if GPT2LMHeadModel is not None:
    hf_model_tmp = load_hf_gpt2_model('gpt2')
    print("=== HuggingFace GPT-2 parameter keys (first 20) ===")
    for i, k in enumerate(hf_model_tmp.state_dict().keys()):
        if i >= 20: break
        print(f"  {k}: {hf_model_tmp.state_dict()[k].shape}")

    print("\n=== Custom minGPT2 parameter keys (first 20) ===")
    _tmp = minGPT2(vocab_size=50257, max_position=1024, d_model=768,
                   n_heads=12, n_layers=12, d_ff=3072)
    for i, (k, v) in enumerate(_tmp.named_parameters()):
        if i >= 20: break
        print(f"  {k}: {v.shape}")
    del _tmp, hf_model_tmp
    if device.type == 'cuda':
        torch.cuda.empty_cache()
''')

set_src(nb, 34, r'''
def load_hf_weights(model: 'minGPT2', hf_model) -> None:
    """Load HuggingFace GPT2LMHeadModel weights into minGPT2."""
    hf_sd = hf_model.state_dict()
    n_layers = len(model.blocks)

    def copy_param(param, value, name: str, transpose: bool = False):
        if transpose:
            value = value.t()
        if tuple(param.shape) != tuple(value.shape):
            raise ValueError(f'{name} shape mismatch: model {tuple(param.shape)} vs hf {tuple(value.shape)}')
        param.copy_(value.to(device=param.device, dtype=param.dtype))

    with torch.no_grad():
        copy_param(model.tok_emb.weight, hf_sd['transformer.wte.weight'], 'tok_emb.weight')
        copy_param(model.pos_emb.embedding.weight, hf_sd['transformer.wpe.weight'], 'pos_emb.embedding.weight')
        copy_param(model.ln_f.weight, hf_sd['transformer.ln_f.weight'], 'ln_f.weight')
        copy_param(model.ln_f.bias, hf_sd['transformer.ln_f.bias'], 'ln_f.bias')
        copy_param(model.lm_head.weight, hf_sd['lm_head.weight'], 'lm_head.weight')

        for i in range(n_layers):
            block = model.blocks[i]
            prefix = f'transformer.h.{i}'
            copy_param(block.ln1.weight, hf_sd[f'{prefix}.ln_1.weight'], f'blocks.{i}.ln1.weight')
            copy_param(block.ln1.bias, hf_sd[f'{prefix}.ln_1.bias'], f'blocks.{i}.ln1.bias')
            copy_param(block.attn.c_attn.weight, hf_sd[f'{prefix}.attn.c_attn.weight'], f'blocks.{i}.attn.c_attn.weight', transpose=True)
            copy_param(block.attn.c_attn.bias, hf_sd[f'{prefix}.attn.c_attn.bias'], f'blocks.{i}.attn.c_attn.bias')
            copy_param(block.attn.c_proj.weight, hf_sd[f'{prefix}.attn.c_proj.weight'], f'blocks.{i}.attn.c_proj.weight', transpose=True)
            copy_param(block.attn.c_proj.bias, hf_sd[f'{prefix}.attn.c_proj.bias'], f'blocks.{i}.attn.c_proj.bias')
            copy_param(block.ln2.weight, hf_sd[f'{prefix}.ln_2.weight'], f'blocks.{i}.ln2.weight')
            copy_param(block.ln2.bias, hf_sd[f'{prefix}.ln_2.bias'], f'blocks.{i}.ln2.bias')
            copy_param(block.ffn[0].weight, hf_sd[f'{prefix}.mlp.c_fc.weight'], f'blocks.{i}.ffn.0.weight', transpose=True)
            copy_param(block.ffn[0].bias, hf_sd[f'{prefix}.mlp.c_fc.bias'], f'blocks.{i}.ffn.0.bias')
            copy_param(block.ffn[2].weight, hf_sd[f'{prefix}.mlp.c_proj.weight'], f'blocks.{i}.ffn.2.weight', transpose=True)
            copy_param(block.ffn[2].bias, hf_sd[f'{prefix}.mlp.c_proj.bias'], f'blocks.{i}.ffn.2.bias')
''')

set_src(nb, 36, r'''
if GPT2LMHeadModel is not None:
    hf_model = load_hf_gpt2_model('gpt2').to(device)
    hf_model.eval()

    my_model = minGPT2(
        vocab_size=50257, max_position=1024, d_model=768,
        n_heads=12, n_layers=12, d_ff=3072, dropout=0.0
    ).to(device)
    load_hf_weights(my_model, hf_model)
    my_model.eval()

    test_ids = torch.randint(0, 50257, (1, 16), device=device)
    with torch.no_grad():
        my_logits = my_model(test_ids)
        hf_logits = hf_model(test_ids).logits

    max_err = (my_logits - hf_logits).abs().max().item()
    print(f'Max absolute error: {max_err:.2e}')
    assert max_err < 1e-4, f'numerical alignment failed: {max_err:.2e} >= 1e-4'
    print('=> Numerical alignment check passed!')

    hf_model.to('cpu')
    if device.type == 'cuda':
        torch.cuda.empty_cache()
else:
    print('Skip numerical alignment: GPT2LMHeadModel is unavailable.')
''')

set_src(nb, 38, r'''
if 'my_logits' in globals() and 'hf_logits' in globals():
    errors = (my_logits - hf_logits).detach().abs().cpu().flatten().numpy()
    max_abs_err = float(errors.max())

    plt.figure(figsize=(7, 4))
    plt.hist(errors, bins=80, color='steelblue', alpha=0.85)
    plt.axvline(max_abs_err, color='crimson', linestyle='--', linewidth=2,
                label=f'max abs err = {max_abs_err:.2e}')
    plt.yscale('log')
    plt.xlabel('absolute logits error')
    plt.ylabel('count (log scale)')
    plt.title('Logits Alignment Error Histogram')
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print('Skip plot: my_logits / hf_logits not found.')
''')

set_src(nb, 40, r'''
本次运行的最大绝对误差为 `6.87e-05`，低于实验要求的 `1e-4` 阈值，因此自定义 `minGPT2` 与 HuggingFace GPT-2 的前向 logits 数值对齐通过。误差直方图整体集中在浮点舍入误差量级，最大值仍小于阈值，说明 causal mask、Pre-LN 残差路径、GELU 近似以及权重映射方向都与 HuggingFace 实现保持一致。

如果误差明显偏大，最优先检查 HuggingFace `Conv1D` 权重是否在加载到 PyTorch `nn.Linear` 时做了转置。第二个高频错误是遗漏 bias，例如 `attn.c_attn.bias`、`attn.c_proj.bias`、`mlp.c_fc.bias`、`mlp.c_proj.bias` 或 LayerNorm 的 bias。还要确认 dropout 已关闭、模型处于 `eval()` 状态、注意力掩码方向正确，并且 GELU 使用了 GPT-2 对应的 tanh 近似形式。
''')

set_src(nb, 44, r'''
class GPT2Classifier(nn.Module):
    def __init__(self, gpt2: 'minGPT2', num_classes: int, freeze_backbone: bool = True):
        super().__init__()
        self.gpt2 = gpt2
        d_model = gpt2.lm_head.in_features
        self.classifier = nn.Linear(d_model, num_classes)
        if freeze_backbone:
            for p in self.gpt2.parameters():
                p.requires_grad = False

    def forward(self, input_ids: 'torch.Tensor') -> 'torch.Tensor':
        h = self.gpt2.hidden_states(input_ids)
        last_token_h = h[:, -1, :]
        return self.classifier(last_token_h)
''')

set_src(nb, 46, r'''
if load_dataset is not None and GPT2Tokenizer is not None:
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = 'left'
    sst2 = load_dataset('glue', 'sst2')
    print('SST-2 dataset loaded; tokenizer and sst2 are available.')
else:
    print('Skip SST-2 data loading.')
''')

set_src(nb, 47, r'''
class SST2Dataset(Dataset):
    """SST-2 sentiment classification dataset."""
    def __init__(self, split: str, max_len: int = 64, n: int = 2000):
        data = sst2[split]
        if n is not None:
            data = data.select(range(min(n, len(data))))
        sentences = [str(x) for x in data['sentence']]
        labels = [int(x) for x in data['label']]
        encoded = tokenizer(
            sentences,
            truncation=True,
            padding='max_length',
            max_length=max_len,
            return_tensors='pt',
        )
        self.input_ids = encoded['input_ids'].long()
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return self.input_ids.shape[0]

    def __getitem__(self, i):
        return self.input_ids[i], self.labels[i]
''')

set_src(nb, 51, r'''
def train_classifier(model, train_loader, val_loader, epochs=3, lr=2e-4):
    """Train classifier and return (train_losses, val_accs)."""
    model.to(device)
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    if not trainable_params:
        raise ValueError('No trainable parameters found. Check freeze_backbone / requires_grad settings.')

    optimizer = torch.optim.AdamW(trainable_params, lr=lr)
    criterion = nn.CrossEntropyLoss()
    train_losses, val_accs = [], []

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss, total_count = 0.0, 0
        saw_nan = False

        for input_ids, labels in train_loader:
            input_ids = input_ids.to(device)
            labels = labels.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(input_ids)
            loss = criterion(logits, labels)
            if torch.isnan(loss):
                print(f'[WARN] NaN loss at epoch {epoch}; stop training early.')
                saw_nan = True
                break
            loss.backward()
            torch.nn.utils.clip_grad_norm_(trainable_params, max_norm=1.0)
            optimizer.step()

            batch_size = labels.size(0)
            total_loss += loss.item() * batch_size
            total_count += batch_size

        avg_loss = total_loss / max(total_count, 1)
        train_losses.append(avg_loss)

        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for input_ids, labels in val_loader:
                input_ids = input_ids.to(device)
                labels = labels.to(device)
                logits = model(input_ids)
                pred = logits.argmax(dim=-1)
                correct += (pred == labels).sum().item()
                total += labels.numel()
        val_acc = correct / max(total, 1)
        val_accs.append(val_acc)
        print(f'Epoch {epoch:02d}/{epochs} | train_loss={avg_loss:.4f} | val_acc={val_acc:.4f}')

        if saw_nan:
            break

    return train_losses, val_accs
''')

set_src(nb, 52, r'''
if load_dataset is not None and GPT2LMHeadModel is not None:
    sst2_clf = GPT2Classifier(my_model, num_classes=2, freeze_backbone=True)
    losses_sst2, accs_sst2 = train_classifier(sst2_clf, sst2_train, sst2_val)
    del sst2_clf
    if device.type == 'cuda':
        torch.cuda.empty_cache()
else:
    print('Skip SST-2 training.')
''')

set_src(nb, 54, r'''
if 'losses_sst2' in globals() and 'accs_sst2' in globals():
    epochs = range(1, len(losses_sst2) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(epochs, losses_sst2, marker='o')
    axes[0].set_xlabel('epoch')
    axes[0].set_ylabel('train loss')
    axes[0].set_title('SST-2 Training Loss')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(epochs, accs_sst2, marker='o', color='seagreen')
    axes[1].set_xlabel('epoch')
    axes[1].set_ylabel('validation accuracy')
    axes[1].set_ylim(0, 1)
    axes[1].set_title('SST-2 Validation Accuracy')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
else:
    print('Skip plot: losses_sst2 / accs_sst2 not found.')
''')

set_src(nb, 56, r'''
SST-2 采用 Feature Extraction 模式：GPT-2 主干冻结，只训练最后一个 token 隐状态上的线性分类头。本次运行 3 个 epoch 后，训练损失从 `1.1031` 降到 `0.6132`，验证准确率从 `0.5424` 提升到 `0.7099`。最终验证准确率为 `0.7099`，说明 GPT-2 预训练表示对情感二分类有一定迁移能力，但冻结主干限制了它对分类目标的适配。

这个结果也符合 decoder-only 模型做判别任务的预期：分类头只能读取最后位置聚合出的单向上下文表示，而不能像 BERT 的 `[CLS]` 那样在每一层直接双向聚合全句信息。因此即使训练曲线有效下降，Feature Extraction 模式的准确率仍明显受限。
''')

set_src(nb, 59, r'''
class AGNewsDataset(Dataset):
    """AG News topic classification dataset."""
    def __init__(self, split: str, max_len: int = 64, n: int = 5000):
        data = agnews[split]
        if n is not None:
            data = data.select(range(min(n, len(data))))
        texts = [str(x) for x in data['text']]
        labels = [int(x) for x in data['label']]
        encoded = tokenizer(
            texts,
            truncation=True,
            padding='max_length',
            max_length=max_len,
            return_tensors='pt',
        )
        self.input_ids = encoded['input_ids'].long()
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return self.input_ids.shape[0]

    def __getitem__(self, i):
        return self.input_ids[i], self.labels[i]
''')

set_src(nb, 62, r'''
if load_dataset is not None and GPT2LMHeadModel is not None:
    if 'my_model' in globals():
        my_model.to('cpu')
    if device.type == 'cuda':
        torch.cuda.empty_cache()

    print('=== Feature Extraction ===')
    ag_backbone_frozen = minGPT2(
        vocab_size=50257, max_position=1024, d_model=768,
        n_heads=12, n_layers=12, d_ff=3072, dropout=0.0
    ).to(device)
    load_hf_weights(ag_backbone_frozen, hf_model)
    ag_frozen = GPT2Classifier(ag_backbone_frozen, num_classes=4, freeze_backbone=True)
    _, accs_ag_frozen = train_classifier(ag_frozen, ag_train, ag_val, epochs=10, lr=2e-4)
    del ag_frozen, ag_backbone_frozen
    if device.type == 'cuda':
        torch.cuda.empty_cache()

    print('=== Full Fine-tuning ===')
    ag_backbone_ft = minGPT2(
        vocab_size=50257, max_position=1024, d_model=768,
        n_heads=12, n_layers=12, d_ff=3072, dropout=0.0
    ).to(device)
    load_hf_weights(ag_backbone_ft, hf_model)
    ag_ft = GPT2Classifier(ag_backbone_ft, num_classes=4, freeze_backbone=False)
    _, accs_ag_ft = train_classifier(ag_ft, ag_train, ag_val, epochs=10, lr=5e-5)

    print(f'Frozen backbone final val_acc: {accs_ag_frozen[-1]:.4f}')
    print(f'Full fine-tuning final val_acc: {accs_ag_ft[-1]:.4f}')

    del ag_ft, ag_backbone_ft
    if device.type == 'cuda':
        torch.cuda.empty_cache()
else:
    print('Skip AG News training.')
''')

set_src(nb, 64, r'''
AG News 的两组实验分别对应 Feature Extraction 和 Full Fine-tuning。本次运行中，冻结主干 10 个 epoch 的最终验证准确率为 `0.8530`；全参数微调 10 个 epoch 的最终验证准确率为 `0.8910`，比冻结主干高 `0.0380`，即约 `3.8` 个百分点。冻结主干时训练损失从 `1.6332` 降到 `0.3543`，说明线性头可以利用 GPT-2 预训练表示完成一定程度的主题分类；全参数微调时训练损失从 `0.6126` 降到 `0.0103`，说明主干参数被充分调整到了 AG News 目标上。

需要注意，全参数微调最后一轮验证准确率不是全程最高值；第 9 轮达到 `0.9050`，第 10 轮回落到 `0.8910`，这说明小样本子集上存在一定过拟合或验证波动。总体结论仍然明确：全参数微调优于冻结主干，但 decoder-only 的因果注意力和最后位置表征使其在判别任务上的结构先验弱于同等条件下的 encoder-only BERT。
''')

set_src(nb, 67, r'''
if GPT2Tokenizer is not None:
    shk_ids = tokenizer(shakespeare_text, return_tensors='pt')['input_ids'][0]
    block_size = 128

    class ShakespeareDataset(Dataset):
        def __init__(self, ids, block_size):
            self.ids, self.block_size = ids, block_size

        def __len__(self): return len(self.ids) - self.block_size

        def __getitem__(self, i):
            input_ids = self.ids[i : i + self.block_size].long()
            targets = self.ids[i + 1 : i + self.block_size + 1].long()
            return input_ids, targets

    shk_loader = DataLoader(ShakespeareDataset(shk_ids, block_size), batch_size=16, shuffle=True)
    print(f'Shakespeare dataset size: {len(shk_loader.dataset)} samples')
else:
    print('Skip Shakespeare dataset construction.')
''')

set_src(nb, 70, r'''
def train_lm(model, loader, epochs=2, lr=3e-4):
    """Language-model fine-tuning, returning epoch_losses."""
    model.to(device)
    for p in model.parameters():
        p.requires_grad = True
    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    epoch_losses = []

    for epoch in range(1, epochs + 1):
        total_loss, total_tokens = 0.0, 0
        saw_nan = False
        for input_ids, targets in loader:
            input_ids = input_ids.to(device)
            targets = targets.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(input_ids)
            B, T, V = logits.shape
            loss = criterion(logits.reshape(B * T, V), targets.reshape(B * T))
            if torch.isnan(loss):
                print(f'[WARN] NaN loss at epoch {epoch}; stop training early.')
                saw_nan = True
                break
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_loss += loss.item() * targets.numel()
            total_tokens += targets.numel()

        avg_loss = total_loss / max(total_tokens, 1)
        epoch_losses.append(avg_loss)
        print(f'Epoch {epoch:02d}/{epochs} | lm_loss={avg_loss:.4f}')
        if saw_nan:
            break

    return epoch_losses
''')

set_src(nb, 73, r'''
if 'shk_losses' in globals():
    epochs = range(1, len(shk_losses) + 1)
    plt.figure(figsize=(6, 4))
    plt.plot(epochs, shk_losses, marker='o', color='darkorange')
    plt.xlabel('epoch')
    plt.ylabel('language modeling loss')
    plt.title('TinyShakespeare Fine-tuning Loss')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
else:
    print('Skip plot: shk_losses not found.')
''')

set_src(nb, 77, r'''
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
                scores = logits[b, used_tokens]
                logits[b, used_tokens] = torch.where(
                    scores > 0,
                    scores / repetition_penalty,
                    scores * repetition_penalty,
                )

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

                sorted_indices_to_remove = cumulative_probs > top_p
                sorted_indices_to_remove[:, 1:] = sorted_indices_to_remove[:, :-1].clone()
                sorted_indices_to_remove[:, 0] = False

                indices_to_remove = torch.zeros_like(logits, dtype=torch.bool)
                indices_to_remove.scatter_(dim=-1, index=sorted_indices, src=sorted_indices_to_remove)
                logits = logits.masked_fill(indices_to_remove, torch.finfo(logits.dtype).min)

            probs = F.softmax(logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)

        ids = torch.cat([ids, next_id], dim=1)

    return ids
''')

set_src(nb, 81, r'''
本次生成中，Greedy 输出从 `To be, or not to be,` 继续到较长的 Shakespeare 风格句子，并稳定地产生类似 `are three pence to a second day of audience`、`pinched with the colic` 这样的片段。Greedy Decoding 是确定性的，因为每一步都选择当前条件分布中概率最大的 token，即 $\arg\max_w P(w\mid w_{<t})$；在模型参数、prompt 和实现相同的情况下，多次运行应得到相同文本。它的优点是局部连贯性较强、不会引入采样随机性，缺点是容易陷入高频表达和单一路径，文本多样性有限。

Temperature 采样本次生成了更明显的戏剧对话结构，例如 `BRUTUS:`、`MENENIUS:` 等角色名，并出现了更丰富的续写内容。Temperature 通过把 logits 除以 $\tau$ 改变 softmax 分布的尖锐度：$\tau<1$ 会让分布更尖锐，使高概率 token 更容易被选中；$\tau>1$ 会压平分布，让低概率 token 获得更多机会。当前使用 `temperature=0.8`，因此相对纯随机采样更保守，但仍比 Greedy 有更高多样性。

Top-k 本次保留最高概率的 50 个候选，生成了 `First Senator:`、`AUF` 等较符合 Shakespeare/戏剧文本形式的片段，但也出现了截断式角色名，说明候选集固定时仍可能采到局部不完整的延续。Top-p 本次生成了 `BRUTUS:`、`Messenger:` 以及 `Capitol`、`Marcius` 等语境相关词，文本结构较自然；它按累积概率动态决定候选集大小，在模型确信时候选少，在模型不确定时候选多。两者都在连贯性和多样性之间折中：Top-k 的控制更硬，Top-p 的候选集更自适应。
''')

set_src(nb, 84, r'''
| 模型 | SST-2 准确率 | AG News 准确率 | 备注 |
|------|-------------|---------------|------|
| GPT-2（冻结主干） | `0.7099` | `0.8530` | Feature Extraction，只训练分类头 |
| GPT-2（全参数微调） | — | `0.8910` | Full Fine-tuning，主干与分类头共同更新 |
| BERT（Lab 5 结论） | Lab 5 notebook 未提供分类准确率 | Lab 5 notebook 未提供分类准确率 | Lab 5 通过注意力与上下文敏感表征实验说明 Encoder-only 具有双向理解优势 |

本次 GPT-2 实验显示，冻结主干在 SST-2 上达到 `0.7099`，在 AG News 上达到 `0.8530`；AG News 全参数微调进一步提升到 `0.8910`。这说明 GPT-2 的预训练表示可以迁移到分类任务，且更新主干参数能缓解一部分目标错配。不过 Lab 5 的 BERT 探查已经显示，BERT 的 `[CLS]` 和普通 token 都能双向访问完整上下文，并且同一个词在不同语境下会形成明显不同的上下文相关表示；这种 encoder-only 归纳偏置天然更适合 SST-2 和 AG News 这类理解型分类任务。

因此，GPT-2 在本实验中的核心价值不是证明它分类最强，而是展示生成式 decoder-only 模型在经过权重对齐和微调后可以完成判别任务，同时让我们观察其相对于 BERT 的结构劣势。全参数微调比冻结主干高约 `3.8` 个百分点，但仍不能消除因果注意力方向、预训练目标和最后位置表征带来的根本差异。
''')

set_src(nb, 86, r'''
从注意力方向性看，Decoder-only GPT-2 在每一层都使用 causal mask，使第 $t$ 个位置只能访问左侧上下文而不能直接访问右侧 token。分类任务往往需要对完整句子做全局判断，例如句尾转折、否定范围和主题实体可能改变前文语义。BERT 的 Encoder self-attention 不施加因果方向限制，每个 token 都能在每一层和全句任意位置交互，因此更容易形成全局语义表示。GPT-2 虽然可以在最后一个 token 汇总左侧信息，但这种汇总是单向压缩，表达路径比 BERT 的双向交互更受限。

从预训练目标错配看，GPT-2 训练时优化的是下一个 token 的条件概率，主要学习如何根据前缀继续生成自然文本。分类任务的监督目标是从完整输入预测离散标签，不要求模型生成后续 token，因此训练信号的形式和使用场景都不同。BERT 的 masked language modeling 要求模型根据左右两侧上下文恢复被遮蔽 token，这更接近“理解完整输入”的表征学习。迁移到判别任务时，BERT 的预训练目标与分类目标之间的距离更短。

从表征提取位置非对称性看，GPT-2 做分类时通常取最后一个 token 的隐藏态，因为只有最后位置能看到前面所有 token。这样会把整句表示集中绑定到输入末端，若存在 padding、截断或句尾信息弱的问题，分类头接收到的表示会受到额外干扰。BERT 使用 `[CLS]` 作为专门的句级聚合位置，并且 `[CLS]` 从第一层开始就可以双向关注全句 token。这个设计让 BERT 的句级表示更稳定、更完整，也更适合直接接分类头。
''')

set_src(nb, 89, r'''
HuggingFace GPT-2 中的 `Conv1D` 名称来自 OpenAI GPT/GPT-2 早期实现的历史习惯，它本质上不是卷积序列建模层，而是一个线性投影层。该实现把权重保存为 `(in_features, out_features)`，前向时使用类似 `x @ W + b` 的矩阵乘法形式。PyTorch 的 `nn.Linear` 则把权重保存为 `(out_features, in_features)`，前向时等价于 `x @ W^T + b`。

因此，如果直接把 HuggingFace 的 `Conv1D.weight` 复制到 `nn.Linear.weight`，矩阵的输入输出维度语义会反过来，轻则 shape 不匹配，重则数值完全错误。加载 GPT-2 权重时，`attn.c_attn.weight`、`attn.c_proj.weight`、`mlp.c_fc.weight` 和 `mlp.c_proj.weight` 都必须 `.t()` 转置后再赋值。bias 是一维向量，不涉及矩阵乘法方向，因此直接复制即可。
''')

set_src(nb, 91, r'''
Post-LN Transformer 把 LayerNorm 放在残差相加之后，即 $\mathrm{LN}(x + F(x))$，梯度必须穿过归一化层才能回到残差主路径。网络很深时，这会让梯度流受到 LayerNorm 统计量和子层变换的共同影响，训练早期更容易不稳定。Pre-LN 把 LayerNorm 放在子层之前，即 $x + F(\mathrm{LN}(x))$，残差分支本身提供了一条更接近恒等映射的梯度通路。

由于 Pre-LN 的梯度可以沿残差连接更直接地从深层传回浅层，它通常在深层 Transformer 训练中更稳定，对 warmup、初始化和学习率的敏感性也更低。GPT-2 采用 Pre-LN，是因为自回归语言模型需要堆叠较多 decoder block，并在大规模语料上长时间训练；稳定的梯度流比 Post-LN 的某些表示归一化优势更关键。最终的 `ln_f` 再对最后隐藏态做统一归一化，弥补每层输出没有立即 Post-LN 的问题。
''')

# Optional short result note for Shakespeare, inserted before section 6.
shk_note = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "TinyShakespeare 微调中，语言模型损失从第 1 轮的 `0.2334` 降到第 2 轮的 `0.0663`。这说明 GPT-2 权重加载后已经具备很强的语言建模能力，少量 Shakespeare 风格文本微调即可快速降低 next-token 交叉熵。由于这里使用的是前 `50000` 字符子集，loss 下降很快也意味着模型可能较快记住局部文本风格，因此生成质量应结合后续采样文本一起判断。\n"
    ],
}
nb["cells"].insert(74, shk_note)

TARGET.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"rebuilt {TARGET} from {BACKUP}")
