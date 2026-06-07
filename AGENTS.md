# AI-Brain Codex Instructions

This repository is the user's Obsidian-based AI-Brain vault.

Default vault path:

`F:\0000Ai System\Obsidian\ObsidianCangku\AI-Brain`

## First Context To Read

Before doing AI-Brain management work, read these files when available:

1. `09_System_系统规则/AI总管工作协议.md`
2. `09_System_系统规则/原则库.md`
3. `01_Self_Model_自我模型/我是谁.md`
4. `02_Goals_目标系统/当前目标.md`
5. `05_Skills_能力模块/Skill索引.md`

Use them to understand the user's goals, preferences, current priorities, routing rules, and existing Skills.

## Canonical Folders

Use these folders as the stable routing targets:

- `00_Inbox_碎片收集`: raw fragments, links, temporary ideas, unprocessed notes
- `01_Self_Model_自我模型`: user identity, preferences, boundaries, long-term self model
- `02_Goals_目标系统`: current goals, priorities, judging criteria
- `03_Projects_项目库`: project indexes, project-specific notes, project status
- `04_Decisions_决策日志`: important choices, tradeoffs, tool selection, project continuation decisions
- `05_Skills_能力模块`: reusable methods, Skill index, Skill drafts and upgrades
- `06_Automations_自动化`: repeatable workflows that may later be automated
- `07_Reviews_复盘`: weekly reviews and periodic synthesis
- `08_References_资料库`: source materials, external references, research notes
- `09_System_系统规则`: operating rules, principles, prompts, system protocols
- `_Templates`: reusable note templates

## Routing Rules

Classify information before writing:

- One-off ideas, links, notes, media clues, or raw material -> Inbox
- Information tied to a continuing project -> Projects
- Choices about direction, priorities, tools, investment, pause/delete decisions -> Decisions
- Reusable repeated methods with stable steps -> Skills
- Repeated, stable, time-consuming workflows -> Automations
- General rules about how the user thinks or wants AI to behave -> Self Model or Principles
- Weekly summaries and progress checks -> Reviews

Default to Inbox when uncertain.

Upgrade rules:

- Similar fragments appear 3 times -> propose a Skill draft.
- A Skill is used 5 times -> consider automation.
- Major decisions must leave a decision-log entry.
- Automation should wait until the manual workflow is stable.

## Editing Rules

- Preserve user-written content.
- Prefer appending new dated sections over overwriting existing notes.
- Do not delete, rename, or move important user files unless explicitly asked.
- Use UTF-8 Markdown that works well in Obsidian.
- Keep writing concise, structured, and easy to scan.
- When changing files, report exactly which files changed.

## Common User Commands

When the user says:

- "沉淀本次对话" -> summarize, classify, and write the useful parts into the appropriate AI-Brain notes.
- "判断放哪里" -> classify only unless asked to write.
- "整理碎片" -> use the information整理 Skill format.
- "形成 Skill" -> create or update a Skill note in `05_Skills_能力模块`.
- "记录决策" -> append to `04_Decisions_决策日志/决策日志.md`.
- "加入自动化候选" -> append to `06_Automations_自动化/自动化候选池.md`.

When the user explicitly asks to write, make the edits directly inside this vault and then summarize the changes.


## Full Workflow References

For complete operating procedures, read these files when relevant:

- `09_System_系统规则/AI-Brain完整运行流程.md`
- `09_System_系统规则/信息分流与升级规则.md`
- `09_System_系统规则/Codex日常口令手册.md`
- `06_Automations_自动化/自动化实施路线图.md`
- `06_Automations_自动化/Codex自动化任务清单.md`
- `06_Automations_自动化/n8n接入蓝图.md`


## Recovery Entry Point

`START_HERE.md` is the human recovery entry point for this AI-Brain. If the user has lost the original conversation or is migrating tools, read `START_HERE.md` first, then read `09_System_系统规则/系统迁移与恢复指南.md`.


## Complete Context Package

If a new agent needs to recover the full original architecture, current workflows, n8n integration plan, Hermes comparison, urgent reduction workflow, and current Skill system, read:

`09_System_系统规则/AI-Brain完整上下文包_给新智能体读取.md`

Read this before making major architecture suggestions.