# Claude Code 命令参考

> 在 Claude Code 中输入 `/help` 可查看最新的完整命令列表。
> 官方文档：https://code.claude.com/docs/en/slash-commands

---

## 一、会话管理

| 命令 | 说明 |
|------|------|
| `/clear` | 清空对话历史 |
| `/compact` | 压缩/摘要对话以释放上下文窗口 |
| `/context` | 查看当前上下文使用统计 |
| `/init` | 为项目初始化 `CLAUDE.md` 文件 |
| `/resume` | 恢复之前的对话 |
| `/plan` | 进入计划模式，先设计实现方案再动手写代码 |
| `/fork` | 将当前会话分叉（fork）到新会话，保留上下文但独立继续 |
| `/fast` | 切换快速模式（使用 Opus 更快输出） |

## 二、配置

| 命令 | 说明 |
|------|------|
| `/config` | 打开或修改设置文件（`.claude/settings.json`） |
| `/model` | 切换 Claude 模型（Haiku / Sonnet / Opus） |
| `/theme` | 切换终端主题（light / dark / auto） |
| `/status` | 查看当前会话状态（模型、Token、MCP 服务器） |
| `/doctor` | 运行健康检查 / 故障排查 |

## 三、文件与代码

| 命令 | 说明 |
|------|------|
| `/add-dir` | 将目录添加到 Claude Code 的工作上下文 |
| `/memory` | 打开或编辑全局记忆/偏好文件 |

## 四、权限与安全

| 命令 | 说明 |
|------|------|
| `/permissions` | 管理权限规则（允许/拒绝工具调用） |

## 五、GitHub 集成

| 命令 | 说明 |
|------|------|
| `/review` | 审查 GitHub Pull Request |
| `/pr-comment` | 管理或发布 PR 评论 |

## 六、MCP 与扩展

| 命令 | 说明 |
|------|------|
| `/mcp` | 管理 MCP（Model Context Protocol）服务器 |
| `/hooks` | 管理命令 Hook（pre/post 执行脚本） |
| `/agents` | 管理子代理（详见下方 [Agents 详解](#agents-详解)） |
| `/plugin` | 管理插件/扩展 |
| `/ide` | 管理 IDE 集成（VS Code、JetBrains） |

## 七、工作流与任务

| 命令 | 说明 |
|------|------|
| `/workflows` | 查看多代理工作流的实时进度 |
| `/tasks` | 查看/管理后台运行的任务 |

## 八、帮助与反馈

| 命令 | 说明 |
|------|------|
| `/help` | 显示帮助和可用命令 |
| `/feedback` | 发送反馈或报告 Bug |
| `/release-notes` | 查看发布说明 |
| `/cost` | 查看当前会话的 Token 消耗和费用 |
| `/export` | 导出对话或产物 |

---

## 九、可用技能（Skills）

### 代码质量

| 技能 | 说明 |
|------|------|
| `/code-review` | 审查当前 diff，检查正确性 Bug 和简化/效率优化 |
| `/simplify` | 仅做代码简化与效率优化（不找 Bug） |
| `/security-review` | 对当前分支的改动进行安全审查 |
| `/verify` | 端到端验证代码改动是否达到预期效果 |

### 研究与分析

| 技能 | 说明 |
|------|------|
| `/deep-research` | 深度研究：多渠道搜索、获取来源、对抗性验证、合成引用报告 |

### 数据可视化

| 技能 | 说明 |
|------|------|
| `/dataviz` | 创建图表、图形、仪表盘等数据可视化 |

### 配置与工作流

| 技能 | 说明 |
|------|------|
| `/update-config` | 通过 `settings.json` 配置 Claude Code（Hook、权限、环境变量） |
| `/keybindings-help` | 自定义键盘快捷键 |
| `/fewer-permission-prompts` | 扫描历史记录，为常见只读操作添加允许列表，减少权限弹窗 |
| `/loop` | 按固定间隔重复执行某个指令 |

### 项目操作

| 技能 | 说明 |
|------|------|
| `/run` | 启动并驱动项目 App 以验证改动 |
| `/init` | 初始化项目的 `CLAUDE.md` 文档 |

### API 参考

| 技能 | 说明 |
|------|------|
| `/claude-api` | Claude API / Anthropic SDK 参考（模型 ID、定价、参数、流式、工具调用、MCP、Agent 等） |

---

## 十、已配置的 MCP 服务器

| 服务器 | 用途 |
|--------|------|
| `memory` | 持久化记忆 / 知识图谱 |
| `fetch` | HTTP 请求与网页抓取 |
| `sequential-thinking` | 结构化逐步推理 |
| `context7` | 编程库/框架文档实时查询 |

---

## 十一、如何查看 Skill 源码

Claude Code 没有内置查看 Skill 源码的 `/` 命令，但 Skill 本身就是 Markdown 文件，可以直接打开。

### 来源分布

| 来源 | 路径 | 说明 |
|------|------|------|
| 插件 Skill | `~/.claude/plugins/.../skills/<skill名>/SKILL.md` | 从插件市场安装的 Skill |
| 项目 Skill | `<项目>/.claude/skills/<skill名>/SKILL.md` | 项目自己定义的 Skill |
| 内置 Skill | 编译在 CLI 二进制中 | 如 `/deep-research`、`/verify`，无独立文件可查看 |

### 示例

已安装的插件 Skill 路径（以 code-review 为例）：

```
C:\Users\<用户名>\.claude\plugins\marketplaces\claude-plugins-official\plugins\code-review\commands\code-review.md
```

### 创建自己的 Skill

在项目 `.claude/skills/` 下新建 Markdown 文件，使用 YAML frontmatter 定义即可：

```markdown
---
name: my-skill
description: 一句话描述
---

# Skill 正文内容（给 Claude 的指令）
```

---

## 十二、Agents 详解

Agent（子代理）是独立的 Claude 实例，拥有自己的上下文窗口和工具权限，可并行运行以分摊任务。

### 管理命令

| 命令/操作 | 说明 |
|-----------|------|
| `/agents` | 列出/管理当前项目的子代理 |
| 创建 Agent 文件 | 在 `.claude/agents/` 下新建 `.md` 文件即可 |

### Agent 文件结构

```markdown
---
name: code-reviewer
description: 触发条件描述
model: inherit          # haiku | sonnet | opus | inherit（跟随主会话）
color: blue
tools: ["Read", "Grep", "Glob"]
---

你是 [角色描述]，专门负责 [任务说明]。

## When to invoke
- 触发场景 1
- 触发场景 2

## Process
1. 步骤 1
2. 步骤 2

## Output Format
[输出格式要求]
```

### 配置字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `name` | ✅ | Agent 名称，kebab-case 格式 |
| `description` | ✅ | 描述及触发条件，用于自动匹配 |
| `model` | ❌ | 模型选择，默认 `inherit`（跟随主会话） |
| `color` | ❌ | 终端显示颜色 |
| `tools` | ❌ | 工具白名单，不填 = 全部可用 |

### 模型选择

| 模型 | 适用场景 |
|------|----------|
| `haiku` | 简单、重复性检查（快、便宜） |
| `sonnet` | 大多数审查/分析任务（推荐默认） |
| `opus` | 复杂迁移、架构设计（深入但较慢） |

### 工具权限

| 级别 | 工具 | 适用场景 |
|------|------|----------|
| 只读 | `Read`, `Grep`, `Glob` | 代码审查、分析 |
| 写入 | `+ Write` | 代码生成、文档 |
| 完整 | `+ Bash` | 迁移、测试执行 |

### 常用 Agent 模板

| Agent | 用途 | 推荐工具 |
|-------|------|----------|
| `code-reviewer` | 代码质量审查 | Read, Grep, Glob |
| `security-reviewer` | 安全检查（OWASP、注入、鉴权） | Read, Grep, Glob |
| `test-writer` | 生成测试用例 | Read, Write, Grep, Glob |
| `api-documenter` | API 文档生成 | Read, Write, Grep, Glob |
| `performance-analyzer` | 性能瓶颈分析 | Read, Grep, Glob, Bash |
| `ui-reviewer` | 前端可访问性 & UX 审查 | Read, Grep, Glob |
| `migration-helper` | 框架/版本迁移 | Read, Write, Grep, Glob, Bash |

### Agent 目录结构

```
.claude/
└── agents/
    ├── code-reviewer.md
    ├── security-reviewer.md
    └── test-writer.md
```
