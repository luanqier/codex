# START HERE - AI-Brain 使用入口

如果你以后找不到原来的对话，从这里开始。这个仓库本身就是系统说明书。

## 这是什么

AI-Brain 是一个 Obsidian + Codex 的个人 AI 工作团队系统，用来：

- 收集碎片信息
- 整理资料、链接、图片、视频、文档
- 辅助决策
- 沉淀 Skill
- 识别可自动化流程
- 做每日整理和每周复盘
- 未来接入 n8n、LangGraph、Letta/Mem0 等工具

## 当前系统路径

```text
F:\0000Ai System\Obsidian\ObsidianCangku\AI-Brain
```

如果迁移到新位置，请更新这些文件里的路径：

- `START_HERE.md`
- `AGENTS.md`
- `.agents/skills/ai-brain-manager/SKILL.md`
- `09_System_系统规则/系统迁移与恢复指南.md`

## 第一次打开时怎么做

1. 用 Obsidian 打开这个文件夹。
2. 用 Codex 打开同一个文件夹作为 workspace。
3. 对 Codex 说：

```text
请按 AGENTS.md 工作，并使用 $ai-brain-manager 管理我的 AI-Brain。先读取 START_HERE.md，然后告诉我当前系统状态和下一步建议。不要先修改文件。
```

## 核心入口文件

按这个顺序读：

1. `START_HERE.md`：总入口。
2. `AGENTS.md`：Codex 工作规则。
3. `09_System_系统规则/AI-Brain完整运行流程.md`：完整工作流。
4. `09_System_系统规则/信息分流与升级规则.md`：判断内容该放哪里。
5. `09_System_系统规则/Codex日常口令手册.md`：日常怎么喊 Codex。
6. `09_System_系统规则/系统迁移与恢复指南.md`：换电脑/换工具/恢复系统怎么做。

## 目录怎么理解

| 目录 | 作用 |
| --- | --- |
| `00_Inbox_碎片收集` | 原始碎片、链接、临时资料入口 |
| `01_Self_Model_自我模型` | 你是谁、偏好、边界、长期画像 |
| `02_Goals_目标系统` | 当前目标、90 天目标、判断标准 |
| `03_Projects_项目库` | 长期项目和项目资料 |
| `04_Decisions_决策日志` | 工具选择、方向判断、项目取舍 |
| `05_Skills_能力模块` | 可复用工作方法 |
| `06_Automations_自动化` | 候选自动化和实施蓝图 |
| `07_Reviews_复盘` | 每日整理、每周复盘、阶段总结 |
| `08_References_资料库` | 外部资料、研究材料、背景文档 |
| `09_System_系统规则` | 系统说明、规则、协议、迁移指南 |
| `_Templates` | 可复用模板 |
| `.agents/skills/ai-brain-manager` | Codex 可用的 AI-Brain 管理 Skill |

## 日常怎么用

### 整理碎片

```text
用 $ai-brain-manager 整理下面这些碎片。先给写入建议，不要直接改文件：
...
```

### 沉淀对话

```text
用 $ai-brain-manager 沉淀本次对话到 AI-Brain。
```

### 判断该放哪里

```text
用 $ai-brain-manager 判断这段内容应该进入 Inbox、项目库、决策日志、Skill、自动化候选池、原则库还是复盘：
...
```

### 每周复盘

```text
用 $ai-brain-manager 根据本周 AI-Brain 内容生成每周复盘。先给草稿，确认后写入。
```

## 自动化原则

当前推荐：先半自动，后全自动。

1. 先让 Codex 给写入建议。
2. 你确认后写入。
3. 一个流程手动跑过 3 次，才考虑自动化。
4. Skill 使用 5 次后，才考虑自动化。
5. 重要决策、自我模型、原则库更新，需要人工确认。

## 迁移时只要带走什么

必须带走：

- 全部 Markdown 文件
- `.agents/skills/ai-brain-manager`
- `AGENTS.md`
- `_Templates`

可以不带走或后续清理：

- `.tmp_pdf_images`
- `.tmp_pdf_pages`
- `.vs`
- `outputs`
- 其他临时渲染或生成产物

## 系统当前阶段

当前是“可运行的半自动 AI-Brain”。

下一步优先级：

1. 每天继续沉淀碎片。
2. 每周继续复盘。
3. 从 `06_Automations_自动化/自动化候选池.md` 里选第一个值得实施的自动化。
4. 后续再接 n8n 或 Codex Automations。


## 完整上下文包

如果新智能体读取 `START_HERE.md` 后仍然缺少最初架构、n8n/Hermes 判断、紧急减负流程等上下文，请让它优先读取：

```text
09_System_系统规则/AI-Brain完整上下文包_给新智能体读取.md
```

新对话推荐口令：

```text
请读取 09_System_系统规则/AI-Brain完整上下文包_给新智能体读取.md，并据此恢复我整个 AI-Brain 系统的上下文。先不要修改文件。
```