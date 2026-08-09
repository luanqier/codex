# Production Rules

## Parameter contract

Use `intake-and-defaults.md` as the fallback contract. The user normally supplies only the novel source and visual style. Resolve all other parameters from project state or defaults, and ask only for a materially consequential missing choice.

For a new project, run the one-time setup card before production and save the confirmed result to `项目制作设定.md`. For later chapters, read that file and do not repeat the questionnaire unless the user requests a change.

Resolve these parameters from the current request or project before production:

- Source scope: chapter, scene, excerpt, or full work.
- Target deliverable: analysis, script, storyboard, prompts, references, images, video, or full package.
- Saved approximate chapter-length target, source-derived final duration, default 15-second segment duration, and target model limit. Treat `每章预计时长` as a soft target; treat an explicitly exact total duration as a hard override only when the user clearly requests exact timing.
- Pacing, dynamic shot-count logic, and per-shot timing basis.
- Script schema and naming convention.
- Visual style, aspect ratio, audience, platform, and safety boundary.
- Dialogue policy: exact preservation, light compression, or adaptation.
- Asset policy: reference reuse, redesign threshold, and version convention.
- QA and packaging requirements.

Do not carry these values from a different novel or prior project. If a parameter is absent, infer a reversible working assumption and record it; ask only when the choice would materially alter the story or deliverable.

## Universal priorities

1. Enforce content safety, public decency, and prohibited-term exclusion before all other goals.
2. Preserve the source story, event order, motivations, outcomes, and hooks through safe adaptation unless further adaptation is explicitly authorized.
3. Preserve causal and emotional continuity across segments.
4. Keep recurring characters, scenes, props, and voices identifiable.
5. Make actions, visual detail, sound layers, and synchronization readable and feasible for the selected generation tool.
6. Use effects, spectacle, music, and decorative composition to support the story rather than replace it.

## Script rules

- Build a source-event ledger before writing shots.
- Give each segment a clear story task and state change.
- Read `每章预计时长` from project settings. If it is an approximate value or range, plan toward it without sacrificing required events, safe meaningful dialogue, natural acting, transitions, or confrontation scale. State the planned runtime before drafting and document any justified deviation in the chapter production index.
- Derive total chapter duration from retained dialogue, natural pauses, visible actions, transitions, and combat needs; never default to a fixed chapter runtime.
- Use 15 seconds per segment by default. Change the segment duration only when the user specifies another value or the target tool makes 15 seconds unavailable; if tool availability forces a change, state the applied value.
- Choose each Segment's shot count from its actual visual beats, dialogue composition changes, reactions, action phases, reveals, spatial reorientation, and transitions. Do not impose a fixed range, favorite count, or preferred grid size; target-tool limits are feasibility constraints only.
- Estimate every shot independently from dialogue speaking time, action completion, visible performance, camera travel, information-reading time, and transition or sound decay. Never obtain shot timing by evenly dividing the Segment duration or by repeating a uniform duration template.
- Make duration arithmetic exact when timed output is required.
- Preserve safe source dialogue as fully as practical according to the current dialogue policy. Prefer adding justified runtime over deleting meaningful dialogue. Automatically replace prohibited wording without quoting it in the deliverable.
- Compress exposition through visible action, reaction, props, environment, or motivated montage without inventing a new story branch.
- Give every story-significant source fight a 30–45 second large-scale xuanhuan/xianxia cultivation-level high-dynamic but non-graphic confrontation, normally spanning two or three consecutive 15-second segments. Preserve geography, action causality, character identity, props, power stages, techniques, and the safely adapted outcome.
- Save every segment as its own TXT and make the first non-empty line `@图1是参考分镜图` followed by `@图N是人物名` declarations for every distinct visible story character in first-appearance order. Keep the declaration synchronized one-to-one with the numbered images in the segment folder.
- Define `本段统一风格` and `本段声音基线` once per Segment. Write every shot with only six Chinese fields: `主体`, `动作`, `运镜`, `风格`, `对白/旁白`, and `声音与同步`.
- Put stable visual and audio information at Segment level. In shot-level `风格` and `声音与同步`, write only changes, triggers, and exceptions.
- Translate emotion into playable behavior inside `动作`: use a motivated subset of reaction delay, gaze, micro-expression, breath, hands, posture, weight, distance, object interaction, tempo, and settled pose. Never use a bare emotion label, and avoid repeating stock gestures.
- Create or update `角色音色档案.md` for major speaking characters before scripting. Keep voice identity stable and specify layered music, ambience, foreground SFX, dialogue priority, and frame-level synchronization cues.

## Visual rules

- Lock the requested art direction; explicitly exclude likely style drift.
- Give major characters a distinctive and appealing design by default. Make important characters immediately recognizable through face, silhouette, costume hierarchy, motif, posture, and movement habit; avoid interchangeable attractive templates.
- Match visual opulence to story status. High-status, noble, divine, royal, sect-leader, wealthy, ceremonial, or otherwise important characters should receive ornate, layered, high-quality clothing, accessories, materials, color hierarchy, and symbolic details when compatible with the source and safety rules.
- Make important settings feel grand and lavish when the story supports it. Palaces, sect halls, divine domains, ancestral grounds, banquets, ceremonies, battle arenas, capitals, and major reveals should use large spatial scale, architectural depth, layered lighting, rich materials, crowds or attendants when appropriate, and environmental details that communicate status without crowding the shot.
- For episode 1, chapter 1, Segment 1, create a strong opening hook when it does not conflict with the source, continuity, safety, or project style. Prefer an immediate visual question, high-status reveal, striking atmosphere, looming threat, contrast, symbolic object, aftermath, or character entrance drawn from the source instead of adding a new plot branch.
- Keep groups only as large as the story requires and differentiate visible individuals.
- Strengthen action and effects at story-supported nodes.
- Build cultivation-level spectacle through readable escalation, aerial and ground-scale movement when source-supported, non-contact technique contests, spiritual-force or energy-pressure interaction, safe environmental transformation, large spatial depth, reversals, camera-energy variation, and a decisive non-injurious resolution. Use only abilities, cultivation stages, artifacts, summons, formations, environments, and consequences supported by the source or project bible; do not invent new lore for spectacle. Do not use random effects, repeated exchanges, bodily impact, suffering, or motion blur to simulate intensity.
- Replace sensitive outcomes automatically with safe, dignified, artistic equivalents according to `content-safety.md`.
- Separate universal character identity from temporary costume, disguise, age, location, power stage, or alternate-world versions.
- Preserve the approved main character design in ordinary scenes. Use temporary `single-scene` variants only for source-supported special occasions, and permit a persistent redesign only after a lasting world, identity, or major life-stage transition.
- Keep protagonists identifiable without relying on clothing alone. Preserve distinctive face geometry, hair contour, body proportion, posture, movement, palette relationships, and recurring motifs across variants.

## Delivery rules

- Produce only the layers requested by the user.
- When delivering multiple units, validate each completed unit before proceeding if the project requires incremental QA.
- Keep project-specific rules, characters, paths, chapter progress, and continuity state in the project, not in this Skill.
- Keep confirmed editable defaults in the project-level `项目制作设定.md`, including the chapter from which later changes become active.
- Put each formal storyboard grid in its own segment folder as `图1`, together with one segment TXT and all declared visible-character images from `图2` onward. Preserve that structure in the chapter ZIP and do not require a duplicate chapter-level script.
- Store canonical master character and scene references once under the project-level `总资产` library, using filenames that include asset name, first-appearance chapter for that exact version, and version number.
- Create exactly one `第NNN章_全部Segment.zip` per completed chapter for sharing. Include all Segment folders, `角色音色档案.md`, and the chapter production index; exclude project-wide master assets, drafts, rejected images, and unrelated chapters.
