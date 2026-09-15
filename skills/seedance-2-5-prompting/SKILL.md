---
name: seedance-2-5-prompting
description: Use when writing, reviewing, or repairing prompts for Seedance 2.5, 씨댄스 2.5, Seedance 2.0 Fast, 씨댄스 2.0 패스트, the latest Seedance workflow, emotional acting or micro-expression direction, 30-second generation, 15-second Fast generation, GODSTOUCH action/one-shot direction, R2V, white-model or green-screen references, localized video edits, multimodal reference packs, transferable visual effects for films, commercials and music videos, or camera-motion control; also use for version-unspecified current Seedance prompt requests, while other explicit Seedance 2.0 legacy requests stay on the 2.0 skill.
---

# Seedance 2.5 Prompting

## Core principle

Treat a Seedance 2.5 or explicit Seedance 2.0 Fast prompt as a compact director's brief with explicit reference roles and conflict priority, readable beat timing, separate subject and camera motion, and a defined final frame. Preserve the user's requested reference-label format and actual upload mapping; do not silently carry opaque tags from an older prompt into a portable @이미지1-style deliverable. Describe controllable intent; do not promise literal reproduction, frame-perfect timing, or hidden controls.

## Version routing

Use this skill for Seedance 2.5, the latest/current Seedance, an unspecified Seedance prompt, or a request that explicitly names Seedance 2.0 Fast. For explicit Seedance 2.0 Fast, select the custom Fast profile below. Treat that profile as a local authoring convention, not a public or official model specification. Route every other explicit Seedance 2.0 or legacy request to the 2.0 skill; duration alone never selects Fast. If the version is genuinely ambiguous and changes the prompt materially, state the 2.5 assumption once and proceed.

## Select instructions for this scene

Before loading optional directing references, identify the scene's primary purpose from the actual story/images or current active brief. Keep the latest explicit user choices and assigned reference locks, then select details that make the required action physically possible, express the intended emotion or composition, establish the allowed audio, or protect meaningful continuity. Use the scene-selection pass in the writing-rules reference; an applicable guide is a toolbox, not a list to paste in full.

For each added clause, ask: would removing it materially change the scene's key action, emotion, composition, allowed audio, or important continuity? Keep it if yes; otherwise omit decorative detail, duplicate locks, and unrelated technique or negative lists. Preserve explicit user choices even when elaborate: selection simplifies wording, not the requested scene. Keep necessary causal action and camera geometry in complex scenes; there is no fixed quota of techniques or acting cues.

State shared, unchanged camera and continuity rules once per continuous shot, then write only beat-specific changes. A simple scene still needs the complete functional brief, but it need not fill every camera field repeatedly or reach a target length. Keep this selection process internal rather than adding a planning table or score to the output.

For revisions, build the canonical active brief first and apply selection only to changed layers and their dependencies. Preserve unrelated direction. After an observed failure, strengthen the affected constraint from the first attempt and return a complete replacement; do not preemptively load every repair exclusion into a fresh prompt.

## Load references selectively

- For visual effects, surreal transformations, time-freeze, clones, environment deformation, or effect-driven film, commercial, brand-film, and music-video scenes, read [references/visual-effects-direction.md](references/visual-effects-direction.md) and use `video-effects`. Transfer the visible mechanism into the scene without requiring Higgsfield or its presets. Select effects for the scene's purpose; preserve requested duration, exact tags, camera/cut policy, and audio.

- For music videos, performance, dance, or instrumental prompts of any requested duration, read [references/music-video-direction.md](references/music-video-direction.md). Duration is a setting in this main skill, not a reason to select a separate 10-second or 30-second skill. Preserve the user's exact duration, tags, language, and cut policy.
- For Seedance 2.5 prompt creation or repair, read [references/seedance-25-writing-rules.md](references/seedance-25-writing-rules.md). Apply its scene-selection pass and relevant event, reference, camera, acting, audio, and submission rules; do not copy every example into each prompt. These are user-supplied authoring conventions; preserve explicit scene choices.
- For emotional acting, micro-expressions, reaction shots, gaze, breathing, restrained emotion, emotional transitions, or requests that name 감정 연기, read [감정 연기 카드 01–13](references/emotion-acting-catalog-01-13.md) and [감정 연기 카드 14–25](references/emotion-acting-catalog-14-25.md). Choose one primary performance pattern and adapt only the distinguishing cues to the scene's trigger, duration, dialogue, and final state. The 25 observed examples are an acting vocabulary, not a cast, location, lighting, or camera reference.
- For new Seedance 2.5 scene/prompt creation from a story, supplied images, or both, first read [references/story-image-scene-brief.md](references/story-image-scene-brief.md). Inspect the actual inputs, build a fitting scene, then choose camera direction. Story-only requests need no invented references; image-only requests need visual inspection; combined inputs use explicit story/image roles. Return a complete prompt, not only an input analysis or technique list.
- For Seedance 2.5 fights, chases, mecha, impacts, action reveals, continuous action one-shots, or an explicit GODSTOUCH request, read [references/godstouch-action-camera.md](references/godstouch-action-camera.md). Use its scene-specific camera candidates, event-motivated movement, and action timing after checking scene fit with EyeCandy. Distinguish true no-cut paths from hidden-cut fake oners; preserve the user's camera, duration, audio, and ending choices.
- When a Seedance 2.5 prompt needs scene-appropriate camera motion, framing, blocking, or transition selection, use `video-effects` and its [visual-technique references](../video-effects/references/visual-techniques.md). Eyecandy is source material inside the shared 영상 효과 연출 workflow, not a separately required user-facing step. Choose for the scene's intent and geometry; retain fixed framing or plain coverage when that serves the scene. Preserve already specified camera choices and skip reselection for unrelated edits.
- For a Seedance 2.5 request for cinematic, movie-like, 영화같은, 영화 느낌, or 시네마틱 direction, also use `seedance-25-cinematic`. Keep this skill authoritative for version routing, character budget, and revision handling; the cinematic skill supplies staging and the 2.0-to-2.5 film adaptation.
- Read [references/no-bgm.md](references/no-bgm.md) for no-background-music requests, unwanted score/pad/hum repairs, complete silence, source-only audio, or unaccompanied singing. Select the requested audio behavior; this reference does not make every cinematic prompt music-free.
- Read [references/model-differences.md](references/model-differences.md) for feature, limit, beta, 2.0-versus-2.5, or UI questions.
- Read [references/camera-motion.md](references/camera-motion.md) for camera movement, locked-off constraints, camera repair, R2V paths, or camera vocabulary requests.
- Read [references/prompt-patterns.md](references/prompt-patterns.md) for generation, rewrite, mode selection, local edit, extension, or full prompt output.
- Read [references/revision-workflow.md](references/revision-workflow.md) whenever the user revises, replaces, deletes, reorders, retimes, or reports a failed result, including the first failure.
- Read [references/sources.md](references/sources.md) when a claim needs verification or official attribution.
- Read [references/community-api-prompts-analysis.md](references/community-api-prompts-analysis.md) when adapting examples or claims from awesome-seedance-2.5-api-prompts, another community prompt library, or a third-party API guide.

## Workflow

1. Identify the profile first: Seedance 2.5 or explicit Seedance 2.0 Fast. For a new 2.5 scene, understand the story/images using the input reference before choosing the mode: T2V, I2V, R2V, white-model transfer, extension, or localized edit. Read images rather than inferring their contents from filenames.
2. Declare the deliverable: duration, aspect/output intent, single-shot or multi-shot, audio mode, and final-frame purpose.
3. Build an asset-role map. Give every reference one primary role, permitted secondary role if needed, and priority for conflicts. If concept art, a character sheet, and one or more storyboards are present, keep their jobs distinct: the concept art may control world/style, the sheet identity, and each storyboard only its assigned events, shot order, composition, or transitions. Do not merge separate boards into one vague reference or let a board override a user's style lock. In every copy-ready prompt with supplied references, include a concise REF LOCK for each active source: its exact tag, controlled attributes, conflict priority, and untransferred attributes. The asset-role summary outside the prompt cannot replace this lock.
4. Preserve the actual non-negotiables and select supporting instructions for the scene purpose. Identity, geometry, layout, action order, eyeline, light, screen direction, and audio sync are candidates when relevant, not mandatory additions to every scene.
5. Divide the duration into readable beats. For a sparsely specified 30-second narrative, 6–8-second beats and a short resolution can be useful defaults. For an explicitly edited teaser, approved storyboard, or requested rapid microcuts, preserve the active shot order and requested timing density; group shared direction once and retain fine timecodes where they carry mystery, action, synchronization, or reveal. Do not turn an edited sequence into a continuous-shot template or stretch opening shots to satisfy a default beat count.
6. Compile a coherent camera direction across the beats; state shared shot rules once and write changes where they occur. For 2.5, use the EyeCandy scene-selection reference when the camera choice is open or needs repair; translate the selected direction into the camera compiler below, including a deliberate static shot when appropriate.
7. Write observable subject action and physical state separately from camera movement. For an emotional beat, order the trigger, first visible change, primary face/breath/posture response, and held or released end state using the emotion-acting reference. Use the minimum meaningful body-part/action/count or speed cues; one readable response can be enough. Order contact, force, and object response from the actual starting state.
8. Add lighting, atmosphere, audio, and output intent only when they affect the shot.
9. State desired outcomes positively first. Use concise exclusions for active hard constraints; expand only relevant alternatives for an explicit detailed restriction or observed failure. In an edited mystery, preserve the active reveal logic as causal rules: what the audience learns early, what remains concealed, and what physical image proves the ending. Do not add an explanatory rule or a substitute blackout. Treat camera, focus, playback, editing, and audio separately; scan positive and negative clauses for unwanted specific sound cues.
10. Draft the copy-ready prompt in the requested language, measure its exact character count, and apply the language fallback below when required.
11. Validate, then return the final bounded prompt.

## Camera compiler

Use these fields to check that each important beat is understandable: narrative purpose; start framing; one primary move; path/direction; speed profile; subject blocking; lens/focus; end framing; and continuity or edit behavior. Supply relevant values through shared shot rules plus beat-specific changes; do not repeat unchanged fields or invent irrelevant travel/speed for a locked shot. Keep translation, aim rotation, lens, focus, rig behavior, and subject motion in separate clauses.

```text
purpose → start framing → primary move → path/direction → speed → subject blocking → lens/focus → end framing → continuity/edit
```

Use one primary camera move per beat; keep a continuous shot on one primary route by default, with any requested phases physically connected. For 2.5, render the CAMERA clause with the selected focal length and LOCKED OFF or primary move first; keep that focal length within the shot unless an intentional zoom is requested. Distinguish pan from trucking, tilt from pedestal/crane travel, dolly from optical zoom, and camera orbit from subject rotation. Prefer a clean uploaded path or white-model reference over coordinate formulas when precision matters. Use exact numeric camera settings only as soft intent unless a visible control or reference makes them enforceable.

## Reference hierarchy

Assign identity, motion, spatial layout, camera path, style/lighting, audio, and shot-order evidence separately. Preserve the user's latest requested tag syntax and every active exact tag, including capitalization. When the user requests upload-order labels such as @이미지1, map each label to a specified source and order before writing; do not substitute UUIDs from an older prompt. If a UI requires different actual tags, explain that mapping outside the prompt rather than claiming the prose label is a verified UI field. For R2V, green-screen, or white-model work, say what each source controls and what it must not transfer. A white-model reference normally supplies geometry/path, while its people, materials, and lighting may be replaced.

Replace blanket `완전히 참조` language with the source's role, preserved attributes, allowed changes, and priority. Resolve conflicts explicitly rather than silently blending sources. REF LOCK is mandatory inside the copy-ready prompt whenever an active reference is supplied; keep it even when tightening the character budget or rewriting a 30-second timeline. For a story-only prompt with no source, do not invent a reference or tag.

## Duration and timeline

For Seedance 2.5, preserve the user's requested duration. A 10-, 15-, 20-, or 30-second request uses this same workflow. Do not round, pad, or split it into fixed-duration parts unless the user requests segmentation; a verified interface limit must be explained and reconciled with the requested result. Scale the number of beats and the final settle to the actual length. When 30 seconds is requested and that mode is visible, use one complete 30-second generation prompt with the user's one-shot or edited cut policy; do not split it into two legacy 15-second stages. For explicit Seedance 2.0 Fast, use the same director-brief structure, asset-role hierarchy, camera compiler, audio selection, and final-frame contract as 2.5, but compile a custom 15-second timeline with three to five readable beats. Do not shorten Fast prompts by deleting the role map, subject/camera separation, camera start/path/end, audio mode, or final frame. Treat the Fast duration as part of this local authoring profile rather than a platform-wide official claim. Treat 5–180-second extended/long-video paths as Beta/UI-dependent and confirm the active interface before promising them. Give each beat a readable end state and make the final frame usable as a handoff for an extension or repair.

Mark beta, rollout-, account-, region-, or UI-dependent capabilities as qualified. Ask for visible controls or a screenshot when a specific setting determines the result.

## Audio selection

Choose one deliberate mode: clean visual, diegetic sound, scored soundtrack, or source-audio transfer. State silence, dialogue, music, effects, and sync points so they do not conflict. In revisions, carry the latest explicit score/BGM choice into timed beats; an old NO BGM clause or a no-BGM reference consulted for a different scene is not the default. If an active audio asset is supplied, add an AUDIO LOCK inside the prompt: exact audio tag, whether it is the soundtrack, dialogue/performance timing, sound-effects source, or mood reference; what must remain (timing, rhythm, melody, voice, phrasing, mix, or sync points as applicable); what must not transfer; and its priority against generated score and scene sounds. A mood-only audio reference does not automatically become a sole track. Do not silently drop an active audio tag, replace its track with invented BGM, or declare source-only audio without user authorization; qualify UI-dependent transfer by checking whether the current UI accepts and tags the asset.

`NO BGM` excludes background music, not automatically dialogue, requested singing, or physical scene sounds. Complete silence excludes all audio. Only an explicit source-only request makes an uploaded track the sole audio source; a camera/motion reference does not acquire that role. For source-driven lip sync, derive mouth movement and timing from the source rather than inventing a conflicting beat grid. Compile the applicable contract in [references/no-bgm.md](references/no-bgm.md), and preserve the latest active audio choice during revisions.

## Multi-turn revision compiler

Whenever the user revises an existing prompt, treat the previous prompt as evidence of the current brief, not as prose to patch. First build a canonical active brief containing only the latest active profile, asset roles, constraints, subject beats, camera beats, lighting, audio, and final frame. Apply the latest user instruction to that brief before drafting. The latest user instruction replaces an older value in the same control layer unless the user explicitly says to add, combine, keep both, or preserve it.

Classify the requested change as `ADD`, `REPLACE`, `DELETE`, `REORDER`, `RETIME`, `PRESERVE`, or `RESET` using [references/revision-workflow.md](references/revision-workflow.md). Retire superseded values and remove their dependent camera, focus, audio, prop, timing, continuity, and exclusion clauses. Rebuild every affected dependency; a subject-action change must trigger a camera/timing check, and a camera replacement must recompile that beat's start, move, path, speed, blocking, focus, and end as one compatible route.

Recompile the same full director-brief structure from the canonical active brief on every revision, including the first revision. Return one complete replacement prompt and never append revision history, patch notes, retired values, or contradictory “not the old move” language to the copy-ready prompt. A localized edit may have a narrow edit boundary, but its returned prompt must still be the complete active edit brief.

## Repair workflow

Start from the first failed result using the [first-failure repair loop](references/revision-workflow.md#first-failure-repair-loop). Inspect the supplied result or use the user's described failure, form a narrow repair hypothesis, and return the complete corrected prompt. Do not require unchanged resubmission, wait for a fixed failure count, or automatically adopt an older take. Generation retries follow the actual production authorization and budget, not the existence of a prompting guide.

Classify the failure first: identity/product drift, subject motion, camera path/speed, framing, collision/continuity, lighting/style, audio/timing, or unwanted text/music. Repair the failed layer first; use localized editing when the interface exposes it and the remainder is usable. Narrow repair determines the changed scope, not the output format: rebuild and return the full active brief even when only one layer changes. Strengthen or replace a reference when prose is insufficient.

Replace unsupported coordinate formulas with a readable physical path, landmarks, start/end states, or a clean path reference. For a moving-camera repair, preserve only active start, target, route tangent, focus, and end values that the user did not replace, delete, reset, reorder, or retime. Never use preservation language to revive a retired value.

## Prompt length contract

Treat the copy-ready prompt code block as a bounded deliverable. Count Unicode characters in that block only, including spaces and logical line breaks. Select the active budget before drafting:

- Seedance 2.5: target 4,300–4,800 characters for a complex 30-second or multimodal prompt; hard maximum 5,000.
- Explicit Seedance 2.0 Fast: aim for about 3,500 characters for the custom 15-second profile; hard maximum 4,000.

Use fewer characters whenever the brief is already complete and never pad to reach a target. Fast keeps the same complete prompt structure as 2.5; its smaller budget comes from fewer and tighter 15-second beats, not from dropping functional blocks.

Write the first draft in the user's requested language. Measure Seedance 2.5 with `scripts/count_prompt_chars.py` and Fast with `scripts/count_prompt_chars.py PROMPT_PATH --limit 4000` when tools are available. For Fast, if the draft is above the 3,500-character target but at or below 4,000, compress redundant wording in the requested language toward 3,500 while preserving the full structure.

If a draft exceeds its active hard maximum, rewrite the entire prompt code block in concise Simplified Chinese. Translate only the canonical active brief. Preserve every exact active reference tag, timeline, camera path, final frame, and functional constraint, then measure and compress until the active hard maximum is met: 5,000 for 2.5 or 4,000 for Fast. Retain the exact set of active supplied timecode ranges after applying the latest revision; when the user explicitly reorders or retimes beats, retire the old ranges and preserve the new ranges instead. If the user explicitly forbids translation, keep the requested language and compress it instead.

Before compression, remove all retired or superseded instructions and their dependencies. Then compress in this order: redundant style adjectives; repeated continuity locks; duplicated negative clauses; explanatory restatements; then low-priority decorative detail. Preserve active asset roles and priorities, REF LOCK for every active source, AUDIO LOCK for any active audio asset, exact tags, required beats, separate subject and camera action, camera start/path/end, audio mode, final handoff, and every necessary UI-dependent qualification.

Report `프롬프트 길이: {N}/{ACTIVE_LIMIT}자` immediately after the code block, using 5,000 for Seedance 2.5 and 4,000 for Fast. The settings note, length line, asset-role map, rationale, and retry guidance are outside the prompt budget.
## Output contract

Return in this order:

1. A one-line assumption/settings note only when needed.
2. One copy-ready prompt code block in the user's language, or in Simplified Chinese when the fallback above applies.
3. The exact prompt length line.
4. A compact asset-role map when references exist.
5. A two-to-four-line camera rationale.
6. One narrow retry instruction only when repairing an existing result.

Keep exact user tags and avoid unnecessary explanation. For review-only requests, use the optional one-line note to name the strongest failure when needed, then preserve the return order above and provide the corrected prompt as item 2.

## Final checklist

Before returning, verify that the prompt contains:

- A declared mode, duration, and output intent.
- Every referenced asset's role and priority, with REF LOCK inside the code block for each active source.
- A visible subject-action arc, separate from camera action.
- When emotion is central, a visible trigger-to-response sequence and a readable final expression, gaze, breath, or posture.
- A camera start state and end state, with one primary move per beat.
- A deliberate audio mode; when an active audio asset exists, an AUDIO LOCK inside the code block with its tag, job, retained properties, sync and conflict priority.
- A final-frame or handoff description.
- Qualified wording for every beta/UI-dependent feature.
- A copy-ready prompt code block within the active hard limit: 5,000 characters for Seedance 2.5 or 4,000 for explicit Seedance 2.0 Fast.
- For Fast, the same complete structural blocks as 2.5 and an approximately 3,500-character target without padding.
- A concise Simplified Chinese rewrite, rechecked against the active limit, when the requested-language draft exceeded that profile's hard maximum.
- For a revision, one complete replacement prompt compiled from the canonical active brief, with every superseded value and dependency absent.
- The exact active timecode-range set preserved during an over-limit rewrite; if the latest request explicitly retimed or reordered the scene, only the new range set remains.

Run the deletion check against the scene purpose: retain explicit choices and necessary causal/continuity detail; remove duplicate or decorative instructions that do not support the result. Remove unsupported absolutes, pseudo-controls, conflicting moves, accidental cuts, and unassigned reference inheritance. Confirm that any one-shot route is physically contiguous and that every permitted edit has an explicit boundary.
