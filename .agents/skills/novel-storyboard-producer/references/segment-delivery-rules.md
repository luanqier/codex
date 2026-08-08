# Segment Delivery Rules

## Authoritative delivery unit

Treat each Segment folder as a self-contained generation package. Store exactly one TXT script and one numbered reference-image set in that folder.

Use this layout:

```text
分镜图/
├── 第01段/
│   ├── 第01段.txt
│   ├── 图1_参考分镜图_五宫格.png
│   ├── 图2_顾长烬.png
│   └── 图3_云清璃.png
├── 第02段/
│   ├── 第02段.txt
│   ├── 图1_参考分镜图_四宫格.png
│   └── 图2_顾长烬.png
└── 草稿/
```

Do not place a second formal copy of the segment TXT or storyboard grid at the chapter or `分镜图` root. The Segment folder is authoritative.

## TXT reference declaration

Make the first non-empty line of every Segment TXT the complete reference declaration:

```text
@图1是参考分镜图，@图2是顾长烬，@图3是云清璃

# 第01段
本段统一风格：国漫三维电影质感，青石与玉器材质清晰，冷暖体积光交叠，云雾和能量流动柔和连贯。
本段声音基线：高空风声与低音弦乐铺底，对白保持前景清晰，空间混响宽阔而克制。

镜号1（3.0s）
主体：……
动作：……
运镜：……
风格：……
对白/旁白：……
声音与同步：……
```

Apply these rules:

- Reserve `图1` for the approved storyboard grid.
- Start characters at `图2` and number them consecutively without gaps.
- Include every distinct visible story character in the Segment, ordered by first visible appearance.
- Use each character's canonical name. If the source provides only a stable role name, use that role name consistently.
- Do not include an off-screen speaker, absent character, anonymous crowd, non-character scene reference, or prop in this declaration.
- Include an individually distinguishable crowd member only when the shot requires a locked identity reference.
- Do not cap the number of declared characters. Reduce unnecessary crowd complexity in the script instead of omitting required visible-character references.
- Keep the first line limited to the numbered reference declarations. Put style, sound, negative prompts, and other instructions on later lines.
- Define `本段统一风格` and `本段声音基线` once after the Segment heading.
- Write all prompt fields in Chinese. Every shot must contain only `主体`, `动作`, `运镜`, `风格`, `对白/旁白`, and `声音与同步`.
- In `动作`, convert emotion into two to four motivated visible performance cues. Do not use a bare emotion label or restate unchanged baseline mannerisms.
- In `风格`, inherit the Segment baseline and write only shot-specific material, lighting, atmosphere, and motion changes.
- In `声音与同步`, inherit the Segment baseline and write only shot-specific music, ambience, SFX, dialogue-priority, and synchronization changes.
- Use the approved voice profiles for dialogue direction.
- Run the content-safety scan before approving the TXT; never place prohibited wording in the declaration, dialogue, prompt fields, filename, or explanatory note.

## Numbered image files

- Save exactly one approved grid as `图1_参考分镜图_N宫格.*`, where `N宫格` matches the scripted shot count.
- Save each declared character as `图N_人物名.*` using the same number and canonical name as the TXT declaration.
- Copy the approved active character version; never substitute a crop from the storyboard when a locked character reference exists.
- Keep character reference content synchronized with the active `main`, `single-scene`, or `persistent-world-stage` version for that Segment.
- Reusing the same approved character file across multiple Segment folders is expected.
- Do not add unnumbered alternate references, rejected images, or extra formal grids to the Segment folder.

Migration-only exception: when reorganizing an already approved chapter, a one-off character has no standalone reference, and avoiding new API traffic is an explicit constraint, extract one clear lossless panel from that chapter's approved formal storyboard. Save it under the required `图N_人物名.*` filename, record its source segment and panel in the production index, and never promote it to a reusable canonical lock for new generation.

## ZIP package

- Create exactly one archive for every completed chapter and name it `第NNN章_全部Segment.zip`.
- Package every formal Segment folder with its TXT and numbered reference images.
- Include one chapter-level `角色音色档案.md` and `第NNN章_生产索引.md` at the ZIP root.
- Preserve `第01段/`, `第02段/`, and subsequent relative paths inside the ZIP.
- Treat the per-Segment TXT files as the authoritative scripts; do not require a duplicate clean script at the ZIP root.
- Exclude `总资产`, other chapters, `草稿`, API request logs, rejected images, repair candidates, caches, and unrelated assets.
- Create the ZIP only after every Segment folder passes QA.

## QA

Block delivery when any Segment:

- lacks exactly one `第NN段.txt` file;
- does not begin with `@图1是参考分镜图`;
- uses non-consecutive `图N` numbers;
- lacks exactly one `图1_参考分镜图_N宫格` file;
- has a grid count that differs from the TXT shot count;
- lacks a matching `图N_人物名` image for any declared character;
- contains a numbered image that is not declared in the TXT;
- omits a distinct visible story character who needs identity consistency;
- uses the wrong character version for the Segment;
- contains a prohibited term or semantically unsafe equivalent;
- has a shot missing a required Chinese visual or audio field;
- uses an emotion label without playable action, or breaks performance continuity;
- repeats stable Segment-level style or sound content across every shot;
- lacks actionable sound-image synchronization;
- ships without the chapter or project `角色音色档案.md`;
- ships without `第NNN章_生产索引.md`, or the archive filename is not `第NNN章_全部Segment.zip`;
- is absent from the ZIP or has a different internal path.
