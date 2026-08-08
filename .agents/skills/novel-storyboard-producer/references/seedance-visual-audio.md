# Seedance Visual and Audio Design

## Chinese structured shot prompt

Define two Segment-level inheritance lines first:

```text
本段统一风格：视觉风格、核心材质、基础光线、空间介质与动态基调。
本段声音基线：环境底声、音乐基调、空间混响与对白优先级。
```

Then write every shot in Chinese with these exact compact fields:

```text
镜号1（3.0s）
主体：人物、物体与空间主体。
动作：主要行动，以及由触发、目光、微表情、呼吸、手部、姿态、距离和节奏体现的必要表演变化。
运镜：景别、机位、路径、速度与焦点变化。
风格：继承本段统一风格，并只补充本镜头发生变化的纹理、材质、光影、体积光、丁达尔效应和动态轨迹。
对白/旁白：使用角色音色档案的安全对白、旁白或“无”。
声音与同步：继承本段声音基线，并合并音乐变化、环境声、SFX声源与空间位置、对白避让，以及动作和镜头的同步节点。
```

Keep the prompt directly generatable. Use literary language to sharpen sensory specificity, not to replace visible information with abstraction.

## Micro-visual detail

- Put stable texture, material, light, and motion behavior in `本段统一风格`; repeat only shot-specific changes in `风格`.
- Describe surface texture and material behavior only when visible and story-relevant: cloth weave, lacquer reflection, jade translucency, metal brushing, stone powder, mist density, water tension, dust granularity, or energy refraction as applicable.
- Define lighting changes physically: source direction, softness, falloff, volumetric depth, rim separation, reflected color, atmospheric scattering, and motivated change.
- Describe meaningful motion as a trajectory with origin, direction, acceleration, interaction, and decay; place character performance in `动作` and environmental motion in `风格`.
- Maintain spatial geography and screen direction across shots.
- Keep every detail consistent with the approved visual style, character version, scene bible, and content-safety rules.

## Voice-profile record

Before scripting dialogue, create or update `角色音色档案.md` at the project or chapter root for every major speaking character:

```text
角色：
声线年龄感：
音高区间：
共鸣位置：
音色质感：
语速与节奏：
咬字与停连：
情绪范围：
标志性表达：
禁止漂移：
```

Use distinctive but non-caricatured profiles, such as a low, magnetic mature male voice or a cool, intelligent mature female voice. Keep the profile stable across chapters unless age, health, identity, or world transition justifies a recorded change.

## Music and SFX layers

Put stable ambience, music base, spatial acoustics, and dialogue priority in `本段声音基线`. Use `声音与同步` for shot-specific changes across these layers:

1. Dialogue or narration as the intelligibility anchor.
2. Foreground SFX tied to visible actions and materials.
3. Environmental ambience defining space, distance, and scale.
4. Music supporting narrative rhythm without masking dialogue or SFX.
5. Silence or reduced layers for emphasis, reveal, or emotional pressure.

For every cue, state the sound source, onset, duration or decay, spatial position, distance, material character, and relationship to the current frame. Avoid generic phrases such as “震撼音乐” without timing or layer detail.

## Synchronization QA

- Make each visible action's primary SFX occur at the correct frame or described beat.
- Align camera acceleration, cuts, reveals, and scale changes with music phrasing or deliberate counterpoint.
- Duck music under dialogue and restore it only after the line or critical syllable clears.
- Carry ambience continuously across shots in the same space unless a motivated transition occurs.
- Preserve each character's voice identity across Segments and chapters.
- Keep all audio descriptions within the content-safety rules.
