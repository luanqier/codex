---
name: novel-storyboard-producer
description: Convert serialized novel chapters into continuity-first, safety-first AI-video production packages from as little as a novel source plus visual style, using source-driven chapter timing, 15-second default segments, compact Chinese Seedance-style prompts, embodied character performance, voice profiles, synchronized sound design, AI-generated character references, storyboard grids, per-chapter QA, packaging, and cross-chapter state tracking. Use when the user asks to turn a novel or web-novel chapter into 分镜脚本、宫格分镜图、角色图、场景图、Seedance 2.0 segments, continue producing later chapters, preserve character faces across images, direct expressions and emotions through visible acting, inspect completed chapter assets, or batch a novel into chapter folders.
---

# Novel Storyboard Producer

Turn novel chapters into production-ready storyboard packages while preserving the original event chain, visual identity, and cross-segment continuity. Treat plot fidelity as the primary constraint and visual spectacle as a supporting layer.

## Load Context

1. Read `references/intake-and-defaults.md` and resolve the minimum input contract. Require only the novel source. Treat visual style as optional initial input and confirm it through the one-time setup card when absent.
2. Read the requested chapter in full and enough of the previous and next chapter to identify the incoming state and outgoing hook.
3. Locate the project production rules, progress file, continuity ledger, character bible, scene bible, and existing reference images when available.
4. Read only the references needed for the current task:
   - Always read `references/content-safety.md`, `references/intake-and-defaults.md`, `references/production-rules.md`, `references/dialogue-and-combat-timing.md`, `references/performance-direction.md`, `references/seedance-visual-audio.md`, and `references/qa-rubric.md`.
   - Read `references/continuity-method.md` when splitting or continuing chapters.
   - Read `references/character-consistency.md` when characters appear or images are generated.
   - Read `references/image-grid-rules.md` when generating storyboard grids.
   - Read `references/segment-delivery-rules.md` when writing clean scripts, organizing storyboard outputs, or packaging a chapter.
   - Read `references/project-asset-layout.md` when initializing a project, creating character or scene references, naming master assets, or packaging chapters.
5. Treat project-specific rules as overrides. Do not import characters, costumes, or story facts from another novel.

## Resolve Inputs Without Burdening the User

- Minimum input is the novel source. Visual style may be supplied immediately or confirmed through the one-time setup card.
- On the first upload for a new project, inspect enough source material to propose defaults, then present the concise one-time setup card from `references/intake-and-defaults.md`. Show the current default beside every option and wait for the user's answer before production unless the user explicitly says to use defaults or skip setup.
- Let the user reply `全部默认` or change only selected item numbers. Do not require a complete form.
- Save the confirmed choices as `项目制作设定.md` at the project root. Reuse them for later chapters without asking again.
- If the user later says `修改项目设定`, show only the current settings and requested or relevant options, update the file, and record the chapter from which the change becomes active.
- Infer chapter scope, approximate chapter-length target, final source-driven runtime, pacing, script schema, dialogue policy, output layout, aspect ratio, asset policy, and QA behavior from the confirmed setup and `references/intake-and-defaults.md` when unspecified.
- Accept optional overrides naturally from the user's request; do not force the user to complete a form.
- After initial setup, ask only when a missing choice is blocking or would materially change the result.
- If no project exists, initialize a lightweight project state as work proceeds instead of asking the user to design the production system.

## Select the Requested Layer

- If asked for analysis only, report the event chain, risks, and recommendations without generating assets.
- If asked for script only, stop after script and continuity QA.
- If asked for characters or scenes first, create and inspect references before storyboards.
- If asked for a full chapter, complete every stage through QA and packaging.
- If asked to continue multiple chapters, finish and validate each chapter before starting the next.

## Produce a Chapter

### 1. Build the source event ledger

List every causally necessary event in source order. Mark dialogue that should be preserved, unsafe source material that requires automatic artistic substitution, incoming state from the prior chapter, and the final hook. Do not copy prohibited source wording into notes intended for delivery. Do not draft shots before this ledger is complete.

### 2. Plan the chapter arc

Assign each segment one story task. Make every segment change at least one state: information, objective, location, relationship, threat, possession, or emotional pressure. Use conflict and effects only where the source event requires them.

Use the confirmed `每章预计时长` as a soft pacing and scope target. When it is `自动适配原文`, derive the chapter duration entirely from the source. When the user supplies an approximate value or range, plan toward it but do not treat it as a hard cap: preserve required events, safe meaningful dialogue, natural performance, and required confrontation scale, and record the reason when the final runtime must exceed or fall outside the estimate. Use 15 seconds as the default duration of each generation segment unless the user specifies another value. Budget enough time to retain safe dialogue at a natural speaking pace and to show required reactions, pauses, actions, and transitions. When the source contains a fight, reserve a 30–45 second large-scale xuanhuan/xianxia cultivation-level high-dynamic confrontation for each story-significant fight, normally divided into two or three linked 15-second segments. Express it through non-graphic energy contests, evasion, defensive techniques, formations, spatial pressure, and environmental response without bodily harm. Follow `references/dialogue-and-combat-timing.md`.

Before writing the timed script, create or update `角色音色档案.md` at the project or chapter root for every major speaking character. Define vocal age impression, pitch, resonance, texture, cadence, articulation, emotional range, and prohibited drift. Follow `references/seedance-visual-audio.md`.

### 3. Write the timed script

Follow the user's or project's duration, segment, pacing, output-schema, and target-model settings. Default every segment to 15 seconds; accept a user-specified segment duration as the override. When no total duration is specified, do not impose a chapter cap: calculate the duration from dialogue speaking time, dramatic pauses, visible actions, transitions, and any required 30–45 second safely adapted confrontation sequence. Ask only when different choices would materially change the result. Choose shot count by story task, speaking time, action complexity, and model limits. Make shot durations sum exactly to each segment duration and make the segment durations sum to the derived chapter duration.

Use compact Chinese structured Seedance 2.0-style prompt blocks. Calculate and state the planned chapter runtime before segment drafting, compare it with `每章预计时长`, and record any justified deviation in the chapter production index. Define `本段统一风格` and `本段声音基线` once per Segment. Make every shot contain only six fields: `主体`, `动作`, `运镜`, `风格`, `对白/旁白`, and `声音与同步`. Merge material, lighting, atmosphere, and motion texture into `风格`; merge music, ambience, SFX, dialogue priority, and synchronization into `声音与同步`. Use a format such as:

```text
本段统一风格：
本段声音基线：

镜号1（3.0s）
主体：
动作：
运镜：
风格：
对白/旁白：
声音与同步：
```

Keep descriptions precise, visible, micro-detailed, and literary without becoming vague. In `动作`, translate emotion into observable performance: reaction timing, gaze, micro-expression, breath, hands, posture, weight shift, interpersonal distance, object interaction, and recovery. Never use a bare label such as happy, sad, angry, or nervous as the performance direction. Select only the two to four cues that materially change in the shot rather than listing every possible cue. Follow `references/performance-direction.md`. Preserve safe source dialogue as fully as practical; automatically rewrite prohibited wording into safe, dignified, artistic expression while preserving narrative function. Remove or compress other dialogue only when it is repetitive, non-visual, or explicitly authorized, and never change its intent or information. Do not add unrelated production commentary inside the clean script.

Write every segment as a separate TXT file inside that segment's delivery folder. Make the first non-empty line a reference declaration in this exact sequence: `@图1是参考分镜图，@图2是人物名，@图3是人物名`. Reserve `图1` for the segment's approved storyboard grid, then declare every distinct visible story character from `图2` onward in first-appearance order. Omit off-screen speakers and anonymous crowd extras unless they require an individual locked reference. The declaration order and names must match the numbered image files in the same folder one-to-one. Treat this declaration as required generation input, not production commentary.

### 4. Run script QA

Run content-safety and prohibited-term checks before all other QA. Then check source-event coverage, chronology, segment-to-segment causality, safe dialogue fidelity, the saved approximate chapter-length target, justified runtime deviation, source-driven duration math, the default or user-specified segment duration, the compact six-field Chinese schema, embodied performance, voice-profile coverage, audio synchronization, crowd load, confrontation continuity, and AI-generation feasibility. Reject emotion-only labels, implausible gestures, repeated stock expressions, and performance discontinuity. Confirm that any story-significant fight receives a coherent 30–45 second large-scale xuanhuan/xianxia cultivation-level high-dynamic but non-graphic sequence without padding, repeated actions, invented powers, bodily harm, or loss of required safe dialogue. Fix failures before making images.

### 5. Lock visual assets

Reuse established reference images. Store every approved master character design under `总资产/人物人设图` and every approved master scene design under `总资产/场景图`. Name each master file with the character or scene name, the chapter where that exact asset version first appears, its version class when applicable, and its version number. For every new major character, extract a distinctive character lock record from the source, let the available image model create an original reference image, inspect it, and approve or repair it before generating storyboards. Keep the main character design stable across ordinary scenes. Use a temporary single-scene variant only for a source-supported special occasion, and create a persistent redesign only after a world, identity, or major life-stage transition that justifies long-term change. Create a new scene or prop reference only for a recurring major setting, plot-critical prop, or justified stage redesign. Record master reference paths, version names, first-appearance chapters, allowed scenes, and persistence rules in the project bible and `总资产/资产索引.md`. Follow `references/character-consistency.md` and `references/project-asset-layout.md`; do not ask the user to design characters unless they explicitly want control or the source is materially ambiguous.

### 6. Generate storyboard grids

Generate one composite grid per segment when requested. The number of panels must equal the number of scripted shots. Each panel represents exactly one shot and uses the project's requested aspect ratio. Keep panel order explicit and consistent. Save the approved grid as that segment's `图1_参考分镜图_宫格数.*`. Copy the approved active-version reference for every distinct visible story character into the same folder as `图2_人物名.*`, `图3_人物名.*`, and subsequent numbers in first-appearance order.

### 7. Inspect immediately

After each image, inspect panel count, shot correspondence, face identity, costume, stage version, group differentiation, spatial continuity, and forbidden styles. Regenerate or edit failures before proceeding.

### 8. Validate and package

Organize each Segment in its own folder containing exactly one Segment TXT, that Segment's numbered storyboard grid, and all numbered character references declared by the TXT. Validate the loose chapter structure first. Then create exactly one chapter archive named `第NNN章_全部Segment.zip` containing all Segment folders, `角色音色档案.md`, and the chapter production index; validate the completed archive with `scripts/validate_chapter.py --zip`. Do not include the project's `总资产` master library in every chapter archive because the necessary character references are already copied into the Segment folders. Do not require a duplicate clean script at the ZIP root; the Segment TXT files are authoritative. Validate the master asset library separately with `scripts/validate_project_assets.py`. Do not report completion while required checks fail. Follow `references/segment-delivery-rules.md` and `references/project-asset-layout.md` exactly.

### 9. Update project state

Record the chapter-ending state, unresolved hooks, new assets, costume or power-stage changes, and the next chapter's required opening state. Append execution results and user corrections to the project's learning log or execution log.

## Evolution Loop

Do not silently rewrite the Skill after every complaint.

1. Record one-off feedback as an execution-log observation.
2. Add a repeated or high-impact failure to evaluation cases.
3. Propose a rule change when the same failure recurs or when the user explicitly says “以后都这样”.
4. Test the proposed change against at least one completed chapter and one new chapter.
5. Promote the Skill version only after the outputs pass QA and the user accepts the behavior.

Keep universal production rules in this Skill, novel-specific facts in the project, and model/tool-specific syntax in separate references.

## Hard Priorities

Resolve tradeoffs in this order:

1. Content safety, public decency, and prohibited-term exclusion.
2. Story fidelity and causal continuity after safe adaptation.
3. Character, prop, and scene identity.
4. Readable action, emotion, and sound-image synchronization.
5. Effects and visual spectacle.
6. Decorative composition.

Never improve a lower-priority layer by breaking a higher-priority layer.
