# NO-BGM audio direction

## Scope and evidence

Adapted from the user-supplied `NO-BGM-mini-guide.md`, which describes a Cinema Director V3 house technique for Seedance / Higgsfield. Treat it as an authoring convention, not a verified model mechanism. `NO BGM`, early placement, and named exclusions communicate intent; they do not guarantee an output or prove that the model processes audio instructions in a particular order.

Use this reference when the user requests no background music, repairs unwanted music/pads/humming, asks for total silence, requests only supplied audio, or wants unaccompanied singing. Preserve an explicit scored soundtrack request. The presence of a video/audio attachment alone does not select source-only audio.

## Select the audio contract first

| User intent | Allowed audio | Contract |
| --- | --- | --- |
| NO BGM / no background music | Requested dialogue and named physical scene sounds | Diegetic mode; exclude background score and unrequested musical sounds |
| Completely silent / all sound off | None | Clean mode; exclude dialogue, music, foley, ambience, breath, and room tone |
| Attached track only / original audio unchanged | Only the selected source, including its existing contents | Source-transfer mode; no generated or layered audio |
| A cappella / singing without accompaniment | Requested vocal performance plus explicitly allowed scene sounds | Diegetic vocal performance; exclude backing track/instruments, retain singing |
| Music or scored soundtrack requested | Requested music and compatible scene sounds | Keep the main skill's scored mode; do not apply a blanket NO-BGM prohibition |

When “silent” is accompanied by requested footsteps or dialogue, those sounds make the intended mode NO-BGM/diegetic. When all sound is explicitly prohibited, do not fill the scene with room tone.

## NO-BGM compilation

1. State the allowed mix and `NO BGM` once as the scene-wide audio contract. When it is a priority requirement, a short NO-BGM flag near duration/cut policy may reinforce the audio block. Do not also add a routine third confirmation at the end; repeat across shot boundaries only where scope would otherwise be unclear or an observed failure requires it.
2. State what is audible positively using physical sources, materials, and action timing: shoes on wet concrete only while walking; canvas sleeve rustle; a latch click at closure; a stated breath. Include only sounds compatible with the user's allowed mix. For off-screen sounds, specify direction, distance, and change when they matter.
3. For a fresh prompt, a clear allowed mix plus NO BGM normally suffices. Add only relevant broad musical exclusions when the user explicitly requests detailed restrictions or a failed result contains unwanted score/pad/other musical forms. Preserve required exclusions in the requested language; do not paste the expanded vocabulary or repeat lists in every beat.
4. Scan every block, including negative clauses, using the sound-cue check below. Remove specific unwanted cues and their dependent timing; keep a requested physical appliance hum distinct from a forbidden musical tone bed.
5. On revision, retire the old audio choice and dependent timing cues, then recompile the complete active brief. Count audio text within the same 5,000-character 2.5 budget or active Fast budget. Compress repetition before removing the selected mode or necessary exclusions.

## Sound-cue check across positive and negative text

This check adapts the user's [2.5 lesson](seedance-25-writing-rules.md). Treat removal of extraneous cue names as a wording heuristic, not proof that naming a sound summons it or defeats all negation.

- Compare each auditory cue with the active allowed mix. Remove unrequested specific sound names, instrument cues, song titles, or motifs even inside a phrase such as `no distant church bells`; express the allowed mix instead. Do not retain the failed sound as a revision reminder.
- Keep necessary broad exclusions such as score, musical pad, drone, and backing track. Do not expand them into a catalogue of concrete unwanted instruments or sound sources.
- Preserve explicitly allowed dialogue, physical sounds, requested singing, and source-only contents. A requested bell ring stays audible under NO BGM; a-cappella lyrics stay permitted. Exact reference tags are never edited by the sound-name scan.
- Separate visual nouns from auditory instructions. A required bell tower may remain visible with a still bell, while the mix contains only footsteps. Do not remove the prop or location to eliminate an unwanted sound. Keep an explicitly supplied quote/tag verbatim when its content is required.
- Recheck sound timing after action edits. If the action has been removed, retire its exclusive sound cue; if it remains visual in total silence, retain the action without audible foley.

For detailed exclusions or repair in a scene with no requested vocal music, this is a vocabulary bank. Select relevant terms; do not paste the entire block by default:

```text
Only the explicitly listed diegetic sounds and dialogue are audible. NO BGM — no background music of any kind: no score, soundtrack music, instrumental, underscore, ambient musical pad, musical drone, tone bed, swell, sting, humming, singing, whistling, or lyrics. NO BGM throughout.
```

The other mode examples below are also adaptable contracts, not mandatory lists: keep the chosen mode and meaningful source/permission boundaries while omitting redundant wording. Supply the actual permitted sounds and dialogue; omit dialogue permission for a no-dialogue scene. Remove any exclusion that would suppress an explicitly permitted physical or vocal sound. This block excludes singing and is therefore not the a-cappella block. A requested vocal performance uses the separate contract below.

## Complete silence

```text
AUDIO: complete silence throughout. NO BGM. No dialogue, singing, sound effects, foley, ambience, room tone, breath, or generated audio.
```

Retain visual actions but remove instructions to make their sounds audible. Do not add breathing or footsteps to “fill the silence.” Use a visible audio-off control when available and actually selected; prose alone does not prove a silent file.

## Source-only audio and lip sync

Use only when the user explicitly assigns a supplied source as the entire audio track. Preserve its exact tag, including spaces and case. The following example assumes the user actually supplied `@Video 1`:

```text
AUDIO: @Video 1 is the sole and complete audio source. Preserve its existing audio and internal timing. Generate no additional audio: no room tone, foley, ambience, breath, dialogue, voices, or added background music. NO ADDED BGM.
```

- Original speech and breath in the selected source remain; “no additional breath/voices” prohibits new layers.
- If the source contains music and the user wants the source unchanged, preserve that music and prohibit added BGM. Do not claim that unchanged source audio is music-free.
- If the user requests both unchanged original audio and removal of music already in it, identify the incompatible requirements. Establish whether they want an edited source or the original; do not promise source separation from a prompt.
- An audio/video reference used only for camera, motion, voice style, or rhythm is not automatically the sole audio source. State explicitly when its audio should not transfer.
- Source-driven lip sync follows the source's phrasing, syllables, rests, breaths, and tempo. Derive scene timing from measured source timing; do not invent per-beat syllable deadlines or stretch the take to a generic 30-second grid. Camera timings may be planned around known source events without moving them.
- If duration or the source is unavailable, describe source-relative timing and state what is unverified; do not invent a tag or source length. Source-audio transfer and exact lip sync remain UI-dependent capabilities/intents.

## A cappella / unheard-track performance

Requested singing is permitted foreground performance, not unwanted background music. Remove “no singing/no lyrics” from the generic block. Use user-provided or original words when needed. An unheard beat is optional performance direction, and is never an audible click track; preserve a supplied tempo without inventing one.

```text
AUDIO: NO BGM in the mix. The performer sings the requested line a cappella, with only the explicitly allowed breath, footfalls, and room tone. No backing track, instruments, musical pad, drone, tone bed, swell, sting, or added backing vocals. Any stated rehearsal beat guides body timing only and is not audible.
```

For a truly silent performance or dance, retain body choreography but omit audible singing, lyrics, song titles, and track-specific cues that contradict silence. For requested singing, retain the requested vocal content instead of applying the silent-scene exclusions.

## Repair check

| Observed issue | Prompt-layer repair |
| --- | --- |
| Specific unwanted sound persists | Remove its cue from positive and negative audio instructions; retain only the allowed mix and necessary visual props |
| Added score | Promote the selected NO-BGM contract; remove competing score language |
| Faint pad, tone bed, or musical hum | Name the unwanted form and specify the permitted physical ambience |
| Music in only some shots | Apply the same audio contract across the entire sequence |
| Added sounds over a source-only take | Keep the sole-source lock and remove generated foley, ambience, and dialogue cues |
| Voice suppressed in a cappella | Use the vocal-performance contract; remove blanket singing/lyrics exclusions |
| Footsteps present in a silent clip | Use complete silence; remove diegetic fill instructions |

These are targeted authoring repairs, not proven diagnoses or guarantees. Do not launch generation or repeated retries merely because this reference suggests a repair.
