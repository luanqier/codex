# Intake and Defaults

## Minimum user input

Require only:

1. **Novel source**: pasted text, chapter text, or an accessible file path.

Treat **visual style** as optional initial input. When absent, infer one or two suitable proposals from the source and let the user confirm or replace them in the one-time setup card.

Do not present a long free-form questionnaire. Use the concise one-time setup card, show defaults, and let the user answer `全部默认` or only the item numbers they want to change.

## One-time project setup

After the first source upload for a new project, inspect the title, genre, chapter structure, dialogue density, likely action scale, and supplied visual references. Then present this setup card once and wait for the user's answer unless they explicitly requested immediate default production:

```text
项目初始设定确认

你可以回复“全部默认”，或者只写要修改的编号，例如：2改成10秒，3改成每章约3分钟，6改成竖屏9:16。

1. 画面风格
   当前：<用户提供的风格；未提供时给出基于原文的建议>

2. 每个Segment时长
   默认：15秒

3. 每章预计时长
   默认：自动适配原文，不设固定上限
   可改：填写大约时长或范围，例如“约3分钟”或“2–4分钟”

4. 对白策略
   默认：在安全改写前提下尽可能保留原文对白

5. 大场面对抗
   默认：重要对抗30–45秒，拆成连续2–3个Segment，采用玄幻修仙级大场面但保持安全表达

6. 画幅
   默认：横屏16:9

7. 人物与场景资产
   默认：AI自动设计并锁定；关键人物和长期场景进入总资产，特殊造型按版本管理

8. 交付范围
   默认：完整章节包，包含音色档案、每段TXT、宫格图、人物参考图、生产索引和章节ZIP

固定规则：内容安全红线、角色一致性、根据实际内容决定镜头数、逐镜计算非均匀时长、Segment文件夹结构和质检不可关闭。
```

Accept natural-language answers. The user may modify one item, several items, or all editable items. Do not ask them to repeat unchanged defaults.

Save the confirmed result to `<项目根目录>/项目制作设定.md` using:

```text
# 项目制作设定

- 生效范围：全项目 / 自第NNN章起
- 画面风格：
- Segment时长：
- 每章预计时长：自动适配原文 / 约N分钟 / N–N分钟
- 对白策略：
- 大场面对抗：
- 画幅：
- 人物与场景资产策略：
- 交付范围：
- 固定安全规则：启用，不可关闭
- 最近确认日期：
- 用户补充要求：
```

For later chapters, read this file and proceed without repeating the setup card. If the user changes a setting, preserve the prior value in project history or the production index and record the new activation chapter.

## Default production contract

When the user gives no override, use:

- Scope: the first unfinished chapter recorded by the project; otherwise the first complete chapter in the source.
- Delivery unit: one complete chapter at a time.
- Deliverable: content-safe timed Chinese structured script, major-character voice profiles, synchronized sound design, necessary AI-generated character/scene/prop references, one storyboard grid per Segment, continuity QA, production index, one ZIP containing all Segments of the chapter, and an updated project-level master character/scene asset library.
- Approximate chapter length: default to `自动适配原文，不设固定上限`. If the user specifies an approximate duration or range, treat it as a soft pacing target rather than a hard cap.
- Total duration: calculate the final runtime from retained dialogue, natural pauses, required action, transitions, and fight-set-piece needs. Aim for the saved approximate chapter length when feasible; never delete required story information or damage natural timing merely to hit it, and record a justified deviation in the chapter production index.
- Segment structure: dynamic segment count with a default duration of 15 seconds per segment. Let the user specify another segment duration; do not force a fixed number of segments.
- Shot count: determine it separately for every Segment from actual dialogue turns, action phases, reactions, reveals, spatial changes, transitions, and target-model feasibility. Do not use a preset range or preferred grid count.
- Shot timing: calculate each shot independently from natural speaking time, visible action completion, performance beats, camera travel, reading time, and sound or transition decay. Do not divide the Segment evenly; use deliberately non-uniform durations whose sum exactly matches the Segment duration.
- Script schema: start each Segment TXT with its `@图N` declaration, define `本段统一风格` and `本段声音基线` once, then write every timed shot in Chinese with only `主体`, `动作`, `运镜`, `风格`, `对白/旁白`, and `声音与同步`.
- Performance: express emotion through motivated, visible acting inside `动作`; never use an emotion label alone. Inherit stable mannerisms and write only the two to four cues that change in the shot.
- Dialogue: preserve safe source dialogue as fully as practical at a natural speaking pace; automatically rewrite prohibited wording, compress only repetition or non-visual exposition when necessary, and preserve narrative intent without repeating unsafe language.
- Fight timing: when the source contains a story-significant fight, allocate a coherent 30–45 second large-scale xuanhuan/xianxia cultivation-level high-dynamic but non-graphic confrontation, normally split into two or three linked 15-second segments. If the user overrides segment duration, repartition it without changing its required total scale.
- Voice and audio: create `角色音色档案.md` with stable profiles for major speaking characters before scripting, then design layered music, ambience, foreground SFX, dialogue priority, and synchronization cues.
- Story adaptation: compress expression, never change required events, motivations, outcomes, or hooks.
- Storyboard: one panel per shot, each panel composed as horizontal 16:9; composite canvas size is unrestricted.
- Reading order: left to right, then top to bottom; use clear gutters and no generated text.
- Art direction: obey the user's style and explicitly exclude likely drift from it.
- Asset policy: AI creates original reference images for new major characters and recurring major scenes or props; reuse approved versions afterward.
- QA: inspect every generated image immediately; validate and package each chapter before continuing.
- Output root: use an existing project root when present; otherwise create `<小说名>_分镜项目` with `总资产/人物人设图`, `总资产/场景图`, and numbered chapter folders in the current writable workspace.
- Safety: apply `content-safety.md` as the highest-priority gate, automatically rewrite prohibited source material, scan all text in both languages, inspect every image, and never sexualize a minor or age-ambiguous character.

Project-specific settings override these defaults. Do not copy settings from another novel merely because they were used previously.

## Optional overrides

Accept these when the user volunteers them, but do not require them:

- Chapter or scene range.
- Total duration, segment duration, or target video-model limit.
- Shot-density preference or pacing.
- Script schema and filename convention.
- Dialogue policy: exact, light compression, or adaptation.
- Audience, platform, rating, or stricter safety boundary.
- Aspect ratio or delivery resolution.
- Output location and folder naming.
- Existing character, scene, costume, or prop references.
- Target image/video model, API, or preferred generation tool.
- Deliverable subset such as analysis only, script only, references only, or prompts only.

## Ask only when necessary

After the one-time project setup, ask a concise follow-up only if:

- The novel source cannot be accessed or has no usable text.
- The visual style is missing or internally contradictory.
- The user requests an exact existing person or IP appearance but provides no usable reference or authorization context.
- No image-generation capability is available while actual images are required; offer prompt-only delivery or request a tool/API choice.
- Two plausible chapter boundaries or output targets would materially change what is produced.
- A requested platform, audience, or sensitive scene requires a materially different treatment.

Otherwise record the inferred assumptions and proceed.

## Minimal intake example

```text
小说原文：D:/novels/example.txt
画面风格：国漫3D动画电影风
```
