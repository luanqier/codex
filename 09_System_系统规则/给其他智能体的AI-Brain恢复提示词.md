# 给其他智能体的 AI-Brain 恢复提示词

把本文件内容复制给 Codex、Claude Code、Cursor、Windsurf、ChatGPT 或其他 AI Agent，它应该能理解并恢复这个 AI-Brain 系统的上下文。

---

## 直接发送给其他智能体的提示词

你现在要帮助我恢复、理解并继续维护一个叫 AI-Brain 的个人 AI 工作团队系统。

我的 AI-Brain 当前路径是：

```text
F:\0000Ai System\Obsidian\ObsidianCangku\AI-Brain
```

如果你无法直接访问这个路径，请让我提供或上传下面这些文件内容，不要凭空猜测。

### 请先读取这些文件

请按顺序读取：

1. `START_HERE.md`
2. `AGENTS.md`
3. `09_System_系统规则/系统迁移与恢复指南.md`
4. `09_System_系统规则/AI-Brain完整运行流程.md`
5. `09_System_系统规则/信息分流与升级规则.md`
6. `09_System_系统规则/Codex日常口令手册.md`
7. `05_Skills_能力模块/Skill索引.md`
8. `01_Self_Model_自我模型/我是谁.md`
9. `02_Goals_目标系统/当前目标.md`

如果你是 Codex，并且当前 workspace 是 AI-Brain，请同时使用：

```text
$ai-brain-manager
```

如果你不是 Codex，或者不支持 Skill，也没关系。请把下面这个文件当成普通工作说明读取：

```text
.agents/skills/ai-brain-manager/SKILL.md
```

### 你要先做什么

请先只做检查，不要修改文件。

请输出：

1. 这个 AI-Brain 系统是做什么的。
2. 每个目录的用途。
3. 当前系统是否完整。
4. 缺少哪些关键文件。
5. 是否有旧路径需要替换。
6. 日常应该怎么使用。
7. 自动化路线是什么。
8. 下一步最应该做什么。

### 这个系统的基本定位

AI-Brain 是一个 Obsidian + Codex 的个人 AI 工作团队系统，用来：

- 收集碎片信息
- 整理资料、链接、图片、视频、文档
- 辅助决策
- 沉淀 Skill
- 识别可自动化流程
- 做每日整理和每周复盘
- 后续接入 n8n、LangGraph、Letta/Mem0 等工具

### 目录用途

| 目录 | 作用 |
| --- | --- |
| `00_Inbox_碎片收集` | 原始碎片、链接、临时资料入口 |
| `01_Self_Model_自我模型` | 我的偏好、边界、长期画像 |
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

### 信息分流规则

请按下面规则判断内容写入哪里：

- 一次性的想法、链接、资料、图片、视频、临时问题 → `00_Inbox_碎片收集`
- 和长期项目直接相关 → `03_Projects_项目库`
- 涉及取舍、优先级、投入、暂停、删除、工具选择 → `04_Decisions_决策日志`
- 可复用的方法，未来会反复使用 → `05_Skills_能力模块`
- 重复、稳定、耗时、规则明确的流程 → `06_Automations_自动化`
- 用户偏好、边界、长期工作风格 → `01_Self_Model_自我模型`
- 可指导未来判断的经验 → `09_System_系统规则/原则库.md`
- 周期性总结、项目回顾、系统改进 → `07_Reviews_复盘`

默认规则：

- 不确定时，先进入 Inbox。
- 同类碎片出现 3 次以上，建议升级为 Skill。
- Skill 使用 5 次以上，建议考虑自动化。
- 重要选择必须进入决策日志。
- 自动化前先手动跑通流程。

### 安全规则

请严格遵守：

1. 先检查，再建议，最后才写入。
2. 不要未经确认删除文件。
3. 不要未经确认覆盖用户写过的重要内容。
4. 不要未经确认对外发送、发布或调用外部服务。
5. 修改文件时，必须说明改了哪些文件。
6. 优先追加 dated section，不要轻易重写整篇笔记。
7. 保持 Markdown 可在 Obsidian 中正常阅读。

### 如果路径变了

如果 AI-Brain 迁移到了新路径，请先检查这些文件中是否还有旧路径：

```text
START_HERE.md
AGENTS.md
.agents/skills/ai-brain-manager/SKILL.md
09_System_系统规则/系统迁移与恢复指南.md
09_System_系统规则/Codex日常口令手册.md
```

旧路径是：

```text
F:\0000Ai System\Obsidian\ObsidianCangku\AI-Brain
```

请先列出需要替换的位置，等待我确认后再替换。

### 日常使用口令

整理碎片：

```text
用 AI-Brain 规则整理下面这些碎片。先给写入建议，不要直接改文件：
...
```

沉淀对话：

```text
沉淀本次对话到 AI-Brain。先判断应该写入哪里，再告诉我建议。
```

判断是否形成 Skill：

```text
判断这件事是普通碎片，还是应该形成 Skill。如果应该，请给 Skill 草稿。
```

判断是否值得自动化：

```text
判断这个流程是否值得进入自动化候选池，并说明原因。
```

每周复盘：

```text
根据本周 AI-Brain 内容生成每周复盘。先给草稿，确认后再写入。
```

系统健康检查：

```text
请读取 START_HERE.md 和 AGENTS.md，检查 AI-Brain 的目录、关键文件、Skill、自动化蓝图是否完整。请只检查，不要修改文件，并告诉我下一步最应该做什么。
```

### 最小恢复包

如果我只给你部分文件，至少需要这些：

```text
START_HERE.md
AGENTS.md
.agents/skills/ai-brain-manager/SKILL.md
01_Self_Model_自我模型/我是谁.md
02_Goals_目标系统/当前目标.md
04_Decisions_决策日志/决策日志.md
05_Skills_能力模块/Skill索引.md
06_Automations_自动化/自动化候选池.md
09_System_系统规则/AI-Brain完整运行流程.md
09_System_系统规则/信息分流与升级规则.md
09_System_系统规则/Codex日常口令手册.md
09_System_系统规则/系统迁移与恢复指南.md
```

### 你的最终目标

你的目标不是只回答我的问题，而是帮助我维护一个会进化的 AI 工作团队系统。

每次处理信息时，请尽量判断它是否属于：

- 碎片
- 项目资料
- 决策
- Skill
- 自动化候选
- 原则
- 复盘

并且告诉我：

1. 应该写入哪里。
2. 为什么。
3. 是否需要形成 Skill。
4. 是否值得自动化。
5. 下一步最小行动是什么。

---

## 给我自己的提醒

下次换工具或新开对话时，直接把上面“直接发送给其他智能体的提示词”整段发给它。

如果对方能访问本地文件，就让它读取 AI-Brain。

如果对方不能访问本地文件，就上传或粘贴这些文件：

1. `START_HERE.md`
2. `AGENTS.md`
3. `09_System_系统规则/系统迁移与恢复指南.md`
4. `.agents/skills/ai-brain-manager/SKILL.md`