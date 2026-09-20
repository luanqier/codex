---
name: novel-storyboard-producer-v5
description: "Convert serialized novel chapters into continuity-first Chinese AI-video production packages, including timed Segments, storyboard grids, Seedance prompts, reusable assets, QA, and packaging. Use for 小说分镜、宫格图、角色图、场景图、章节续作、Seedance prompts, complete novel-video packaging, or action/fight Segments that need precise choreography without changing the story."
---

# Novel Storyboard Producer V5

将小说章节转为连续、可生成、可交付的中文分镜；在动作或打斗 Segment 中按需调用专业动作导演，同时保持原作、生产结构与交付格式不变。

## 工作入口

每次使用本 Skill，先完整读取 [references/core-workflow.md](references/core-workflow.md)。它原样保留 V4 的小说→Segment→宫格图→Seedance→资产→QA→封包流程，是所有任务的基础规则。

只执行核心流程当前路由到的模式，不因 V5 的动作能力扩大交付范围。

## 动作 Segment 路由

当目标 Segment 含有打斗、追逐、对抗、演武、人兽交锋、武器/法术攻防，或其可读性依赖明确的闪避、格挡、落空、受力、位移与动作镜头时：

1. 读取 [references/fight-adapter.md](references/fight-adapter.md)。
2. 按适配层指引读取 [vendor/fight-prompt-director/SKILL.md](vendor/fight-prompt-director/SKILL.md)。
3. 只有需要具体动作骨架、摄影规则或失败修正时，才分别读取 vendored 模块的 `references/fight-design.md`、`references/camera-guide.md` 或 `references/diagnostics.md`。

普通对白、情绪、说明、静态建立、无攻防关系的移动或转场 Segment 不读取打斗模块。

## 不可变合同

动作模块只能细化：动作设计、攻防因果、站位、距离、接触/格挡/落空、受力、位移、武器/能量连续性、动作摄影，以及有画面来源的动作声音。

动作模块不得改变：

- 原小说的事件、因果、动机、知识状态、胜负、关键结果或章节钩子；
- 原对白、人物关系、人物能力、境界、术法、武器或资源上限；
- Segment 数量、每个 Segment 的时长或既定章节总时长；
- 核心流程规定的段级信息、声明行与每镜六字段格式。

不得把 vendored 模块的独立输出模板、默认三方案、默认时长、速度追问或模型格式带入成品。所有动作细化必须回填到 V4 的 `主体 / 动作 / 运镜 / 风格 / 对白/旁白 / 声音与同步` 六字段，且每镜时长之和仍精确等于 Segment 时长。

## 冲突优先级

发生冲突时依次遵循：用户明确要求与原小说证据 → 核心 V4 流程与已批准项目资产/索引 → [fight-adapter.md](references/fight-adapter.md) → vendored 打斗模块。无法在不可变合同内解决时，保留原内容并按核心流程报告阻断项，不擅自改剧情或结构。
