# Project Asset Layout

## Project structure

Use one project root for the full novel:

```text
<小说名>_分镜项目/
├── 项目制作设定.md
├── 总资产/
│   ├── 人物人设图/
│   │   ├── 顾长烬_首次出现第001章_main_v1.png
│   │   ├── 云清璃_首次出现第001章_main_v1.png
│   │   └── 顾长烬_首次出现第037章_persistent-world-stage_上界_v2.png
│   ├── 场景图/
│   │   ├── 云海石台_首次出现第001章_v1.png
│   │   └── 上界天门_首次出现第037章_上界_v1.png
│   └── 资产索引.md
├── 第001章/
│   ├── 分镜图/
│   │   ├── 第01段/
│   │   ├── 第02段/
│   │   └── ...
│   ├── 角色音色档案.md
│   ├── 第001章_生产索引.md
│   └── 第001章_全部Segment.zip
└── 第002章/
```

## Master character filenames

Use:

```text
<人物名>_首次出现第<NNN>章_<版本类型>[_<版本标签>]_v<数字>.<扩展名>
```

Examples:

```text
顾长烬_首次出现第001章_main_v1.png
顾长烬_首次出现第012章_single-scene_宗门大典_v1.png
顾长烬_首次出现第037章_persistent-world-stage_上界_v2.png
```

- `首次出现第NNN章` refers to the first chapter where this exact visual version appears.
- Use `main` for the original persistent design.
- Use `single-scene` for a temporary special-occasion version.
- Use `persistent-world-stage` for a lasting world, identity, or major life-stage redesign.
- Keep the canonical character name first so files sort and search by person.
- Use at least three digits for chapter numbers.
- Never overwrite an approved file; increment `vN`.

## Master scene filenames

Use:

```text
<场景名>_首次出现第<NNN>章[_<世界或阶段标签>]_v<数字>.<扩展名>
```

Examples:

```text
云海石台_首次出现第001章_v1.png
上界天门_首次出现第037章_上界_v1.png
```

- `首次出现第NNN章` refers to the first chapter where this exact scene design or stage version appears.
- Use the stable canonical scene name first.
- Save a new version when the layout, world stage, era, or persistent state changes materially; do not overwrite the old design.

## Asset index

Maintain `总资产/资产索引.md` with:

```text
资产名称｜类型｜首次出现章节｜版本类型/标签｜当前版本｜主文件路径｜适用章节/场景｜状态
```

Record every approved master character and scene reference. Segment folders contain numbered working copies; the index always points to the master file.

## Chapter archive

Create exactly one archive per completed chapter:

```text
第NNN章_全部Segment.zip
```

Place at the chapter root. Include:

- every `第NN段/` Segment folder with its TXT and numbered images;
- `角色音色档案.md`;
- `第NNN章_生产索引.md`.

Do not include:

- other chapters;
- `总资产` or its full master library;
- draft, rejected, repair, cache, API-log, or temporary files;
- a duplicate combined chapter script.

The Segment folders already contain the character references required to generate each clip, so the chapter archive remains portable without duplicating the full project library.

## Project settings

Keep the user's confirmed editable defaults in `<项目根目录>/项目制作设定.md`.

- Create it after the one-time initial setup card is confirmed.
- Record `每章预计时长` as either `自动适配原文` or a user-confirmed approximate value or range; treat it as a soft production target.
- Read it before producing every later chapter.
- Do not ask the same setup questions again unless the user requests a change or a new requirement conflicts materially with the saved settings.
- When settings change, record the activation chapter and preserve the prior setting in project history or the relevant chapter production index.
- Never allow project settings to disable the fixed content-safety gate, identity continuity, required Segment folder structure, or blocking QA.
