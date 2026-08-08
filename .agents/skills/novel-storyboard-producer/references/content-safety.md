# Content Safety

## Highest-priority rule

Treat content safety as the highest-priority constraint. It overrides source fidelity, dialogue fidelity, spectacle, visual design, and user-provided style when they conflict.

Do not reproduce, quote, transliterate, translate, or visually describe prohibited material in any deliverable, including scripts, prompts, filenames, captions, dialogue, voice directions, negative prompts, production indexes, and QA summaries.

## Prohibited material

Exclude all graphic bodily harm, gore, sexual or vulgar material, abusive or insulting language, self-harm, suicide, extremist or cult ritualization, cannibalistic horror, and criminal gang warfare.

Block the following Chinese expressions and their English equivalents in deliverables. Treat close variants, inflections, spacing variants, and euphemistic attempts as prohibited as well:

- 血液飞溅、喷血、血池、断头血、内脏出血、血腥场面、流血。
- 分尸、斩首、虐杀、酷刑、断肢、爆头、撕咬、屠杀、尸横遍野、骨裂。
- 全裸、露点、一丝不挂、性交易、乱伦、恋童、兽交、性暗示、色情互动，以及对敏感身体部位的露骨描述。
- 邪教仪式、食人恶鬼、自残、自杀、黑帮火拼。
- Blood splatter, spraying blood, pool of blood, severed-head blood, internal bleeding, gory scene, bleeding.
- Dismemberment, decapitation, torture killing, torture, severed limb, headshot, mauling, massacre, bodies everywhere, bone fracture.
- Full nudity, explicit exposure, completely naked, sexual transaction, incest, pedophilia, bestiality, sexual innuendo, erotic interaction, and explicit naming or depiction of intimate anatomy.
- Cult ritual, cannibal demon, self-harm, suicide, gang shootout.

Maintain a broader semantic check beyond the literal lexicon. A technically different word does not make the same unsafe image acceptable.

## Automatic safe adaptation

Do not stop merely because the source contains prohibited material. Preserve the narrative function through an automatic safe rewrite:

- Replace bodily injury imagery with damaged armor emitting sparks, torn fabric, dimmed protective light, scattered petals, dust, cracked terrain, fading energy, or a character safely losing balance.
- Replace lethal or torturous action with disarming, containment, forced retreat, barrier collapse, surrender, rescue, separation, or a non-contact energy contest.
- Replace horror imagery with shadow, weather, architecture, symbolic silhouettes, sound, empty space, or restrained suspense.
- Replace sexualized presentation with dignified beauty, costume craftsmanship, posture, expression, and cinematic presence.
- Replace insults with firm disagreement, restrained confrontation, silence, or neutral paraphrase that preserves the relationship change.
- Replace self-destructive acts with withdrawal from danger, intervention, support, recovery, or symbolic release.

Do not repeat the prohibited source wording while explaining the rewrite. Record only the safe replacement and the preserved narrative purpose.

## Safe large-scale confrontation

Keep xuanhuan/xianxia spectacle non-graphic and non-injurious. Use technique displays, barrier contests, evasion, defensive formations, energy-pressure fields, light-and-shadow collisions, weather response, terrain transformation without people being harmed, weapon disarming, containment, and decisive but safe separation.

Do not show impact on bodies, visible wounds, suffering, cruelty, humiliation, or fatal outcomes. Communicate defeat through lowered aura, extinguished formation, dropped token, retreat, surrender, or safe immobilization.

## Output gate

Before delivery:

1. Scan every text deliverable against the literal prohibited-term list in both languages.
2. Run a semantic safety review for equivalent unsafe meaning.
3. Inspect every image for unsafe visual content even when the prompt text is clean.
4. Rewrite and regenerate until both text and visuals pass.
5. Never include prohibited terms in a user-facing failure report; identify the category and state that it was safely rewritten.
