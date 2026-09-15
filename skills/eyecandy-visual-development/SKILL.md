---
name: eyecandy-visual-development
description: Use when directing key visuals, visual development, storyboards, music videos, brand films, fashion films, short-form narratives, product films, or AI films and the shot needs a deliberate camera/blocking/scale/transition technique — reveal, tension, escalation, spatial expansion, motif-linked scene connection, or climax. Built on the eyecannndy.com visual technique taxonomy with derived production directing rules.
---

# EYECANDY Visual Development

## Shared entrypoint

The shared [analyzed example library](../video-effects/references/prompt-library/index.md) contains the actual 132 local gallery examples with frame evidence and complete scene prompts. Use the specific card for observed motion; the taxonomy remains a concept index.

User-facing effect direction lives in [영상 효과 연출](../video-effects/SKILL.md). This directory preserves the Eyecandy taxonomy and detailed technique references for that shared library; the source name is not a separate required user workflow. Read only the relevant technique files when the shared library has already selected this branch.

## What this skill is

A technique-selection and direction-conversion system. It reads a creative brief,
image set, music structure, or scene purpose, decides WHICH visual technique serves
the scene's intent, and converts that choice into concrete directing language:
camera, blocking, scale, composition, and transition relationships.

It is NOT a prompt collection, NOT a camera-move dictionary, and NOT a requirement
to inject a technique into every shot. A neutral documentary-style cut with no
technique is a valid outcome.

## Source authority

Two strictly separated layers live in every file here:

1. **SOURCE-GROUNDED** — the eyecannndy.com taxonomy: category names, slugs,
   sub-types, and (where captured) official one-line definitions. The site itself
   states it is "forever WIP" and "never 100% accurate", so treat its categories as
   a shared naming vocabulary, not as physics.
2. **DERIVED** — every Use When / Avoid When / Directing Rule / Translation /
   Failure Mode / Preservation Rule in `techniques/*.md`. These are this skill's
   structured production rules, written for generative-image and generative-video
   workflows. They are ours to revise; never present them as Eyecandy canon.

Canonical taxonomy index: `references/taxonomy.md` (130 verified categories + slug registry).

Never invent an EYECANDY category that is not in `taxonomy.md`. If a needed
technique has no category there, name it as plain film grammar without attributing
it to Eyecandy.

## Seedance 2.5 camera-direction integration

For a Seedance 2.5 prompt needing scene-appropriate camera, framing, blocking, or transition choices, use [the integration guide](../seedance-2-5-prompting/references/eyecandy-camera-direction.md). Use this skill to select a direction that serves the action, emotion, and space; then use `seedance-2-5-prompting` to compile its start/path/speed/focus/end into the final prompt. A fixed shot or plain coverage can be the best decision. Preserve the user's existing camera choices when only unrelated wording or audio changes.

## Workflow

### Step 1 — Analyze scene intent

Before choosing anything, determine what the scene must DO:

`reveal · tension · escalation · elegance · impact · spatial-expansion · transition · visual-hook · climax · scale-perception · motif-linkage · isolation`

A scene may carry two intents at most (e.g., tension + spatial-expansion). If more
seem needed, reduce the active intents or separate the action within the permitted cut policy. For a requested one-take, simplify or use consecutive beats without adding a cut.

### Step 2 — Select technique(s)

Open `references/intent-routing.md`, map each intent to candidate techniques, then
read the full file of each candidate in `techniques/`. Selection rules:

- One PRIMARY technique per shot. Add a SUPPORTING technique only when it solves a
  different problem than the primary (e.g., Scale Shift primary + Match Cut support).
- Never stack two techniques that compete for the same job (two transition devices
  in one cut = neither reads).
- If no technique beats plain coverage for the intent, direct plain coverage.

### Step 3 — Emit the direction chain

For standalone direction requests, report every selected technique in this logical order. When feeding a final Seedance 2.5 prompt, use the chain as an internal selection plan; the integration guide defines the final prompt and concise camera rationale:

```
Scene Intent        → one or two intents from the fixed vocabulary
Selected Technique  → EYECANDY category name + slug from techniques/
Reason              → why this technique serves this intent HERE, one sentence
Visual Motif        → the recurring element carried by the shot (may be "none")
Camera/Blocking/    → concrete rule: movement path, subject position,
  Scale Rule          frame geometry, scale relationship
Storyboard          → setup frame / transition frame / reveal frame
  Translation         (or hook frame / beat frames / punctuation frame)
```

The storyboard translation format per technique lives inside its technique file.
For multi-shot sequences, chain shots through their `visual link to next shot`.

### Step 4 — Motif linkage (when sequence work)

If the brief involves multiple connected scenes, do NOT invent a new motif system.
Read the bundled [Visual Motif Sequence Director](references/visual-motif-sequence-director.md)
and reuse its Visual Motif Map (motif evolution, match-cut engine, callback system).
Use it only for motif-linked sequence work, within the active duration and cut policy;
for Seedance prompts, keep its planning map internal and retain the main skill's output contract.
EYECANDY techniques then CONSUME motifs: a motif enters a Match Cut, mutates under
Scale Shift, hides behind Pass Through occlusion, returns in the final callback.
Target structure:

`Visual Motif → Match / Mutation / Scale change / Occlusion → Scene Connection → New Shot`

### Step 5 — Preservation gate

Before emitting any final direction, verify the chosen technique does not sacrifice:

- face identity / character likeness
- product form, label, logo legibility
- wardrobe continuity across cuts
- spatial continuity (screen direction, geography of the set)
- brand tone constraints supplied by the user
- user-specified camera position, framing, path, shot duration, and cut policy

If a technique conflicts with preservation, downgrade the technique (reduce speed,
increase clearance between foreground and subject, replace occlusion with framing)
rather than dropping the constraint. Brand Film default: preservation outranks
spectacle, always.

## Hard rules

- Keep the EYECANDY direction layer and technique files model-agnostic: describe
  motion, time, and composition without generation tags or vendor controls.
  A downstream prompting skill owns model-specific syntax and final output.
  In the Seedance 2.5 integration, its exact reference tags and prompt contract
  belong to that downstream layer, not to EYECANDY technique definitions.
- Maximum two techniques per shot, one primary.
- Every technique use needs a Reason line. No reason, no technique.
- Do not repeat the same technique on consecutive shots unless the repetition is
  itself the device (deliberate rhythm), and say so explicitly. Timed beats within
  one continuous shot are not separate shots for this diversity rule.
- Cite the EYECANDY category name exactly as in `references/taxonomy.md`.

## File map

```
SKILL.md                      ← you are here (orchestrator)
agents/openai.yaml            ← Codex interface registration
references/taxonomy.md        ← SOURCE: all 130 EYECANDY categories + slugs + sub-types
references/intent-routing.md  ← DERIVED: scene intent → technique selection table
references/motif-system-link.md ← DERIVED: how techniques consume the existing motif system
techniques/_template.md       ← canonical section contract for technique files
techniques/<slug>.md          ← one file per deep-documented technique (16 files)
tests/test_technique_contract.py ← structural validator (run after any edit)
tests/scenarios.md            ← validation walkthroughs (Tests A–E)
```

## Validate after editing

```powershell
python tests/test_technique_contract.py
```

All green before delivering any output built on edited files.
