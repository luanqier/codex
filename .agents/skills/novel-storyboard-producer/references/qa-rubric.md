# Chapter QA Rubric

## Blocking checks

A production unit cannot ship if any applicable item fails:

- Any text or image contains prohibited graphic, sexual, vulgar, insulting, self-harm, extremist, cannibalistic-horror, or criminal-gang material, including a Chinese or English prohibited term from `content-safety.md` or a semantic equivalent.
- Unsafe source material is quoted in a deliverable instead of being automatically rewritten into a safe, dignified, artistic equivalent.
- Required source events are missing or reordered incorrectly.
- A character acts on information they have not learned.
- A segment cannot be causally connected to the prior state.
- Required duration arithmetic is wrong.
- A Segment uses a preset or preferred shot count instead of deriving its shots from the actual dialogue, action, reaction, reveal, spatial, or transition beats.
- A Segment with two or more shots assigns the same duration to every shot, evenly divides the Segment by shot count, or repeats a mechanical timing template without independent per-shot justification.
- A segment is not exactly 15 seconds when the user did not specify another duration, or it does not match the user's explicit segment-duration override.
- A fixed chapter-duration template overrides the source-driven runtime without an explicit user or project requirement.
- A saved `每章预计时长` is ignored without comparison, or the final runtime falls outside a user-provided estimate without a reason recorded in the chapter production index.
- Required story events, safe meaningful dialogue, natural performance, transitions, or required confrontation scale are damaged merely to force the chapter into an approximate length target.
- Meaningful source dialogue is removed merely to hit an arbitrary duration.
- A story-significant confrontation is not planned as a coherent 30–45 second large-scale xuanhuan/xianxia cultivation-level high-dynamic but non-graphic sequence, or its linked segments break action geography, identity, prop, technique, power-stage, energy-state, or outcome continuity.
- Confrontation spectacle invents an unsupported cultivation stage, ability, technique, artifact, summon, formation, transformation, harmful result, winner, or consequence.
- Storyboard panel count differs from scripted shot count.
- A recurring character, scene, or prop uses the wrong identity or stage version.
- An ordinary scene unnecessarily changes the main character design or creates a new persistent version.
- A temporary special-occasion design persists beyond its authorized scene, or the prior active version is not restored afterward.
- A persistent redesign occurs without a lasting world, identity, power-stage, or life-stage transition.
- A protagonist becomes difficult to recognize after changing clothing because the design lacks stable facial, hair, proportion, posture, movement, palette, or motif anchors.
- An adult female character's intended mature, full-figured overall proportions drift between references and storyboards, become anatomically implausible, use explicit intimate-anatomy emphasis, or are applied to a minor or age-ambiguous character.
- Required deliverables are missing or unreadable.
- A segment TXT does not begin with `@图1是参考分镜图`, or its subsequent `@图N是人物名` declarations do not match the numbered character-reference files one-to-one.
- A segment omits a distinct visible story character from its declaration and reference-image set, or includes an off-screen or irrelevant character as a numbered reference.
- A formal storyboard grid is not numbered as `图1` inside its segment folder, a segment lacks exactly one TXT, or the ZIP flattens the segment structure.
- A completed chapter lacks exactly one `第NNN章_全部Segment.zip`, the archive omits any Segment folder, or it contains unrelated chapters or the full project master-asset library.
- The project root lacks `总资产/人物人设图`, `总资产/场景图`, or `总资产/资产索引.md`.
- A new project begins production without one-time setup confirmation or lacks `项目制作设定.md`.
- A later chapter silently changes an editable default, repeats the entire setup questionnaire unnecessarily, or ignores the saved activation chapter.
- A project setting attempts to disable content safety, identity continuity, Segment folder structure, or blocking QA.
- A master character or scene filename omits the asset name, first-appearance chapter for that exact version, or version number.
- A Segment lacks `本段统一风格` or `本段声音基线`, or repeats their stable content unnecessarily in every shot.
- A shot is not written in Chinese or lacks any required compact field: `主体`, `动作`, `运镜`, `风格`, `对白/旁白`, or `声音与同步`.
- `动作` uses only an emotion label, lacks visible motivated performance, repeats a stock gesture, contradicts the voice/dialogue, or breaks gaze, posture, hand, prop, distance, or tempo continuity.
- `角色音色档案.md` is missing, a major speaking character lacks a voice profile before scripting, or the voice identity drifts without a recorded story reason.
- Music, dialogue, ambience, foreground SFX, and visible actions lack explicit synchronization cues or conflict in timing.

## Scored checks

Score each applicable category from 1 to 5:

1. Source fidelity.
2. Cross-segment continuity.
3. Character, scene, and prop consistency.
4. Visual readability.
5. Dialogue fidelity and timing.
6. Safe conflict and emotional pressure.
7. Visual micro-detail, lighting, dynamics, and artistic quality.
8. Voice identity, audio layering, and sound-image synchronization.
9. File completeness and naming.

Require at least 4 in the first three categories and no blocking failure unless the project defines a stricter threshold.

## Generic regression classes

- Local segments work independently but fail to form a causal sequence.
- A fixed template overrides the number of story beats or shots actually needed.
- Shot durations are mechanically uniform even though dialogue length, action complexity, performance, camera travel, or transition needs differ.
- An arbitrary total runtime forces dialogue loss or compresses a confrontation below its required dramatic scale.
- A long confrontation pads runtime with repeated exchanges, disconnected effects, or unclear action instead of escalation and reversals.
- Literal term filtering passes while the output still conveys semantically equivalent unsafe material.
- Visual prompts use generic adjectives but omit the relevant physical texture, material behavior, lighting mechanics, or motion trajectory from the Segment baseline or shot-specific `风格`.
- `声音与同步` omits relevant sources, layers, timing, spatial placement, dialogue priority, or synchronization.
- Stable style, sound, character baseline, or emotion is redundantly restated in every shot instead of being inherited.
- Art direction drifts between references and generated outputs.
- Recurring identities change across segments or project stages.
- Group members become visual clones.
- Effects, action, or added dialogue displace required story information.
- Validation happens too late to prevent repeated errors.
- Project-specific assumptions leak into another work.

Turn repeated failures into project evaluation cases first. Promote them into this universal rubric only when they generalize across projects.
