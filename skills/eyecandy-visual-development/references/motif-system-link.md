# Motif System Link

<!-- DERIVED -->
This skill reuses the existing HERA motif reference, bundled here for portable installation:

[Bundled Visual Motif Sequence Director](visual-motif-sequence-director.md)

That file owns: Visual Motif Map (sections A–K), Visual Rhyme Chain, the match-cut
engine's nine match types, scale transformation ladder, contrast rhythm, callback
system, and scene-invention engine. Read it before any multi-scene job.

## Division of labor

| Concern | Owner |
|---|---|
| Which motif exists, how it evolves, when it callbacks | visual-motif-sequence-director (hera storyboard skill) |
| Which camera/blocking/scale/transition device carries the motif between scenes | THIS skill (`techniques/`) |

## How EYECANDY techniques consume a motif

The four consumption verbs, mapped to technique files here:

1. **Match** — the motif survives the cut unchanged in one property.
   → `techniques/match-cut.md`, `techniques/match-motion.md`
2. **Mutation** — the motif changes material or form while staying recognizable.
   → `techniques/scale-shift.md` (size mutation), `transformation` category (taxonomy-only)
3. **Scale change** — the motif travels the size ladder
   `object → costume → room → architecture → landscape`.
   → `techniques/scale-shift.md`, `techniques/dolly-zoom.md`
4. **Occlusion** — the motif hides, then re-invents the next scene on reveal.
   → `techniques/pass-through.md`, `techniques/object-portal.md`

## Required chain for every motif-linked cut

```
Visual Motif (from motif map)
  → Match / Mutation / Scale change / Occlusion  (pick ONE verb per cut)
    → Scene Connection (what survives: shape, position, motion, color, silhouette…)
      → New Shot (the destination scene is INVENTED from the surviving property)
```

Rule: the destination scene must not exist independently of the surviving motif
property. If you could swap the destination scene without breaking anything, the
motif linkage is decorative — redo it.

## Worked pattern

Motif: circular ring (from hera motif map, evolution: pearl → moon → doorway)

- Cut 4→5: pearl macro → moon at identical frame position. Verb: **Match**
  (position). Technique: match-cut.
- Cut 7→8: moon → circular doorway the subject walks through. Verb: **Scale
  change**. Technique: scale-shift supporting pass-through.
- Cut 10→11: doorway light wipes frame as subject passes through — new corridor
  revealed. Verb: **Occlusion**. Technique: pass-through.

Each verb names its technique; each technique file supplies the camera/blocking/
translation detail; the hera reference supplies motif evolution and callback order.
