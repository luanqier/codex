# Character Consistency

## AI-first character design

Do not require the user to provide character art. For every new major or repeatedly visible character:

1. Extract canonical facts from the source: age or age band, sex, role, status, temperament, cultivation or power stage, culture, clothing context, signature object, and any explicit physical traits.
2. Fill unspecified visual details with an original design that supports the user's chosen style and the character's role.
3. Build the character lock record before image generation.
4. Generate a clean single-character reference image with a readable face, silhouette, costume, palette, and signature prop. Default to a three-quarter or full-body presentation on a simple compatible background; add a separate close portrait only when face consistency needs it.
5. Inspect face geometry, age, proportions, hands, costume logic, originality, and style. Repair or regenerate failures before storyboards.
6. Save an approved `v1` reference and reuse it. Never silently replace an approved reference.

Do not generate separate references for anonymous background extras unless a later scene makes one narratively important.

## Default design preferences

- Give every major character a distinctive face, body proportion, silhouette, palette, motif, prop, and movement habit. Make protagonists especially recognizable so a costume change cannot make them look like another character. Avoid the generic interchangeable xianxia hero or fairy look.
- Respect explicit source facts and role credibility before beautification. Do not import recognizable designs from existing films, games, animation, celebrities, or other projects.
- Adult major characters should be visually appealing when compatible with the source, but remain individually identifiable rather than sharing one beauty template.
- Adult female protagonists and major characters may be exceptionally beautiful, charismatic, mature, full-figured, and visually striking, with strong but believable overall proportions. Keep anatomy stable across views and scenes. Express attractiveness through distinctive facial design, silhouette, credible tailoring, material, posture, movement, and presence without naming or emphasizing intimate anatomy, excessive exposure, transparent fabric, impossible proportions, or suggestive posing. Never apply mature body-design preferences to minors or age-ambiguous characters.
- Major male characters must also differ in facial structure, age texture, build, hairline, costume silhouette, and temperament rather than becoming variations of one handsome face.

## Scene-based variation policy

Treat the approved main design as the default and preserve it through most scenes.

### Ordinary scene adjustment

Allow only reversible state changes required by the current scene, such as wet or dusty fabric, minor costume wear, travel layers, a cloak, practical equipment, lighting response, hairstyle looseness, fatigue, or safely portrayed reduced energy. Preserve the canonical face, body proportions, primary hair silhouette, palette relationship, motif, and identity anchors. Do not save a new long-term character version for these changes.

### Special-occasion single-scene variant

Use a temporary costume or styling variant only when the source or scene clearly requires a ceremony, banquet, wedding, disguise, infiltration, performance, formal audience, bath, sleep, medical treatment, imprisonment, battle preparation, or another special occasion.

Record the variant as `single-scene` with an explicit start scene and end scene. Preserve the canonical face, body proportions, core hair identity, and at least three stable identity anchors. After the authorized scene ends, return to the current main version unless the source explicitly makes the change persistent.

### Persistent world or identity redesign

Create a new long-term version only when the character enters a different world, lasting faction or identity, major life stage, enduring power stage, or another story transition that justifies a persistent visual change.

Preserve the canonical face and at least three prior identity anchors, including one facial anchor and one silhouette, palette, or motif anchor. Add only one to three new world- or stage-specific symbols. Save a new version instead of overwriting the prior design, and record the exact chapter or scene where it becomes active. Continue using the new version until another justified persistent transition occurs.

Do not treat ordinary location changes, mood changes, or costume changes as a new world-version redesign.

## Character lock record

For every recurring major character, record:

- Canonical name and story stage.
- Apparent age and body proportions.
- Face geometry: outline, brow, eye, nose, mouth, distinctive marks.
- Hair shape, color, layer, ornament.
- Costume silhouette, palette, material, fasteners, and footwear.
- Signature prop, motif, aura color, and movement habit.
- Master reference image path, version, and first-appearance chapter for that exact visual version.
- Allowed changes and forbidden changes.
- Movement habit, default expression range, and speech-presence cues when they affect posing.
- Chapters, worlds, identities, or scenes authorized to use this exact version.
- Version class: `main`, `single-scene`, or `persistent-world-stage`.
- Activation point, expiration point when temporary, and the version to restore afterward.

## Identity anchors

Give every major character at least three stable anchors, including at least one facial anchor and one silhouette or color anchor. Give each protagonist at least five stable anchors across face geometry, hair silhouette, body proportion, palette, motif, signature prop or aura, and movement habit. Preserve those anchors during costume or world changes.

Do not let clothing carry the whole identity. A protagonist must remain recognizable in neutral clothing, damaged clothing, formal clothing, disguise layers, and alternate-world costumes through face geometry, hair contour, body proportions, posture, movement, and recurring motifs.

When a persistent world, identity, or life-stage transition justifies redesign:

1. Keep the canonical face and at least three identity anchors.
2. Add only one to three new stage symbols.
3. Save a new version instead of overwriting the prior reference.
4. State exactly which chapters and scenes use each version.

For a single-scene variant, do not replace the active main reference. Save the temporary variant separately, define its exact scene boundary, and restore the prior main or persistent version immediately afterward.

## Group differentiation matrix

Before generating a crowd or group, assign visible differences:

| Person | Age band | Face shape | Hair | Height/build | Palette | Prop/role |
| --- | --- | --- | --- | --- | --- | --- |

Do not rely only on different clothing colors. Avoid cloned faces, identical hairlines, synchronized expressions, and uniform body proportions.

## Generation lock

- Reference every necessary recurring character, using the smallest complete reference set.
- Repeat canonical anchors in the prompt.
- State the exact stage version.
- State whether the reference is `main`, `single-scene`, or `persistent-world-stage` and enforce its activation boundary.
- Do not mix main-world, disguise, younger, older, fatigued, ceremonial, or alternate-world versions.
- After a single-scene variant expires, restore the prior active version; never let a temporary costume silently become permanent.
- Inspect faces after generation; a plausible but different face is still a failure.
