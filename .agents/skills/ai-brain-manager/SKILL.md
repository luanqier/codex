---
name: ai-brain-manager
description: Manage the user's Obsidian AI-Brain vault. Use when asked to沉淀本次对话, classify notes, organize fragments, update Inbox, create or revise Skills, append decision logs, identify automation candidates, update principles, or route information across AI-Brain folders.
---

# AI-Brain Manager

Use this skill to operate the user's Obsidian AI-Brain as a living memory and workflow system.

Default vault path:

`F:\0000Ai System\Obsidian\ObsidianCangku\AI-Brain`

## Start Here

1. Locate the AI-Brain vault. Use the default path unless the user provides another path.
2. Read these files when available:
   - `09_System_系统规则/AI总管工作协议.md`
   - `09_System_系统规则/原则库.md`
   - `01_Self_Model_自我模型/我是谁.md`
   - `02_Goals_目标系统/当前目标.md`
   - `05_Skills_能力模块/Skill索引.md`
3. Classify the user's content before writing.
4. Prefer appending dated sections. Preserve existing user content.
5. Report changed files and the next recommended step.

## Classification

Use this routing table:

| Content type | Destination |
| --- | --- |
| Raw idea, link, document clue, image/video clue, temporary note | `00_Inbox_碎片收集` |
| Project-specific material or project status | `03_Projects_项目库` |
| Choice, tradeoff, priority, tool selection, pause/delete decision | `04_Decisions_决策日志` |
| Reusable method with triggers, steps, output, checks | `05_Skills_能力模块` |
| Repeated stable workflow worth later automation | `06_Automations_自动化` |
| User preference, boundary, long-term working style | `01_Self_Model_自我模型` |
| General operating principle | `09_System_系统规则/原则库.md` |
| Weekly synthesis or progress review | `07_Reviews_复盘` |
| External source material for reference | `08_References_资料库` |

Default to Inbox if uncertain.

## Upgrade Rules

- Same type of fragment appears 3 times: propose a Skill draft.
- A Skill is used 5 times: consider automation.
- Important choices: append a decision log entry.
- Automation candidates must be stable, repeated, valuable, and low enough risk.
- Do not automate a workflow before it has been manually tested.

## Writing Patterns

### Inbox Entry

Append to `00_Inbox_碎片收集/今日收集.md` or create a dated note if the user asks for separate daily files.

Use:

```md
## YYYY-MM-DD 沉淀内容

### 原始来源

- 

### 摘要


### 标签

- 

### 关联项目

- 

### 行动项

1. 

### 可沉淀知识

- 

### 是否需要决策

- 

### 是否值得自动化

- 
```

### Decision Log Entry

Append to `04_Decisions_决策日志/决策日志.md`:

```md
### YYYY-MM-DD 决策标题

日期：YYYY-MM-DD

问题：

背景：

目标相关性：

可选方案：

1. 
2. 
3. 

推荐方案：

选择理由：

风险：

下一步小实验：

预期结果：

复盘日期：

实际结果：

经验沉淀：
```

### Skill Note

Create or update files under `05_Skills_能力模块`:

```md
# Skill 名称

## 触发条件

## 输入

## 处理步骤

## 输出格式

## 检查标准

## 可自动化方向

## 版本记录
```

Update `05_Skills_能力模块/Skill索引.md` when adding a new Skill.

### Automation Candidate

Append to `06_Automations_自动化/自动化候选池.md` with:

```md
## YYYY-MM-DD 自动化候选：流程名称

流程名称：
触发条件：
当前手动步骤：
频率：
价值：
复杂度：
出错成本：
推荐工具：
是否现在自动化：
下一步：
```

## Safety

- Do not delete, rename, or move existing vault content unless explicitly asked.
- Do not overwrite user-written sections unless the user asks for replacement.
- Ask before writing to external systems, sending messages, or exposing private content.
- Keep generated notes concise and useful; avoid storing low-value noise permanently.

## Final Response

After using this skill, answer with:

1. What was classified or written.
2. Files changed, if any.
3. New action items, decisions, Skill updates, or automation candidates.
4. The next single step.