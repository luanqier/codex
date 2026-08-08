# Image Grid Rules

## Panel count

Use one panel per scripted shot. If a segment contains N shots, generate an N-panel grid. Never pad, merge, or duplicate panels to reach a preferred grid size.

After approval, save the grid inside its segment folder as `图1_参考分镜图_N宫格.*`, using the actual Chinese grid count such as `五宫格`. The segment TXT must declare it first as `@图1是参考分镜图`.

## Composition

- Treat every panel as a separate frame using the project's requested aspect ratio.
- State the reading order and follow it consistently.
- Use clear, consistent gutters or borders.
- Do not add text, shot numbers, subtitles, logos, or watermarks.
- One panel represents one shot, not a collage within a panel.

## Prompt recipe

Include:

1. Chapter and segment identifier.
2. Exact panel count and reading order.
3. Global visual style and explicit exclusions.
4. Reference-lock description for recurring characters and scenes.
5. One concise description per panel matching the script.
6. Shared light, time, geography, and action-axis requirements.
7. Crowd differentiation rule when relevant.
8. Safety treatment and negative constraints.

## Inspection

Reject or repair images when:

- Any visual contains graphic harm, sexual or vulgar presentation, abusive text, self-destructive behavior, extremist ritualization, cannibalistic horror, criminal gang warfare, or a semantic equivalent prohibited by `content-safety.md`.
- Panel count is wrong.
- A panel contains two scripted shots or omits a shot.
- A recurring face, costume, age, or stage version changes.
- Multiple group members share the same face.
- Location layout or light changes without motivation.
- Generated text appears.
- The output becomes live-action, 2D, or another unintended style.
