# Validation Scenarios — Tests A through E

<!-- DERIVED -->
Each scenario walks the full SKILL.md workflow (intent analysis → routing →
direction chain → preservation gate) on a realistic brief. Structural integrity of
every referenced technique file is enforced by `test_technique_contract.py`
(ALL GREEN at build time); this document validates the DECISION LOGIC.

Status legend: PASS / PASS-with-downgrade (preservation gate fired).

---

## Test A — Product Reveal

**Brief:** "We have one hero shot of the perfume bottle on white. Make it cinematic."

**Step 1 Intent:** `reveal` + `scale-perception`. The shot currently shows everything;
cinematic requires hiding then granting. Two intents, allowed maximum.

**Step 2 Selection:** intent-routing reveal row → candidates object-portal,
pass-through, scale-shift. Required inputs check: no interior world asset exists for
object-portal (fail), no occluding layer staged for pass-through (fail), scale-shift
needs only reference objects with known sizes (PASS). Primary: **Scale Shift**
(Giant sub-type). Supporting: none needed.

**Direction chain:**

```
Scene Intent       → reveal + scale-perception
Selected Technique → Scale Shift (/technique/scale-shift, Giant)
Reason             → monumentality IS the premium cue; forced perspective grants
                     it without any second location or set.
Visual Motif       → none yet (single-shot job) — bottle silhouette itself becomes
                     the seed motif for later sequence work.
Camera/Blocking/   → true-scale calibration frame first (bottle among everyday
  Scale Rule         objects); then Giant staging: bottle spans building façades,
                     deep focus both planes sharp, silhouette contact precise,
                     camera locked during alignment, known-size anchor (door) visible.
Storyboard         → setup: bottle true-scale on vanity / transition: alignment
  Translation        moment, bottle edge kisses rooftop line / reveal: bottle as
                     tower over miniature street, door anchor bottom-left.
```

**Preservation gate:** label plane stays perpendicular to camera at giant scale;
proportions internally exact — context lies, product doesn't. No conflict. **PASS**

---

## Test B — Suspense

**Brief:** "A woman stands alone in a hallway. It's static and boring. Give it dread
and make the space feel endless."

**Step 1 Intent:** `tension` + `spatial-expansion`.

**Step 2 Selection:** tension row → dolly-zoom, locked-on, snorricam. Inputs: subject
static (dolly-zoom ideal), corridor has converging lines (background structure ✓).
spatial-expansion row → parallax, pass-through, set-transition. Combination rule:
primary solves ONE problem — dolly-zoom handles tension; supporting pass-through
handles expansion (doorway at corridor's end). Two different problems, legal stack.

**Direction chain (shot 1):**

```
Scene Intent       → tension + spatial-expansion
Selected Technique → Dolly Zoom (push-in + widen) primary; Pass Through support at exit
Reason             → world stretching around an unchanged figure = dread made
                     visual; exiting through the far doorway converts dread into space.
Visual Motif       → corridor's repeated door rectangles (declared motif).
Camera/Blocking/   → subject chest-up centered, size locked across effect; push along
  Scale Rule         axis while background stretches 3s, hold 1s; walk to doorway,
                     partial occlusion ≤60%, threshold breath, exit into second corridor.
Storyboard         → setup: natural-perspective baseline / transition: warped
  Translation        background vs identical subject crop / reveal: doorway crossing
                     frame split 1/3 old, 2/3 new corridor.
```

**Preservation gate:** dolly-zoom failure mode "subject size creep" flagged → first/last
frame likeness check mandated; face never covered by door edge during pass-through.
No downgrade needed. **PASS**

---

## Test C — Music Video

**Brief:** "Motif = circular ring. Connect four scenes without repeating the same move."

**Workflow:** motif ownership lives in `visual-motif-sequence-director.md`; ring evolution
declared there: `pearl → moon → stage light ring → zero mark`. This skill assigns
consumption verbs per cut:

| Cut link | Verb | Technique | Direction kernel |
|---|---|---|---|
| 1→2 | Match (position) | Match Cut | pearl macro centered → moon at identical screen position |
| 2→3 | Scale change | Scale Shift | moon-scale ring shrinks into handheld stage-light seen from behind performer |
| 3→4 | Occlusion | Pass Through | performer crosses through light-ring; new warehouse revealed on other side |

Repetition check: three different verbs, three different techniques, motion grammar
varies (cut / re-stage / continuous move). Anti-forcing ledger confirms no technique
twice in the run. Ring recognizability preserved per Preservation Rules (silhouette
class consistent). **PASS**

---

## Test D — Brand Film

**Brief:** "Luxury watchmaker. Brand tone: restrained, precise. Logo must stay legible.
Make the launch film dynamic."

**Selection pressure test:** intent-routing suggests crash-transition + whip-pan for
"dynamic". Preservation gate fires:

- Crash cut Avoid When: "brand-serene contexts unless deliberately aggressive" → HIT.
- Whip pan smear reads cheap against restrained tone → downgrade.

Resolution per SKILL.md Step 5: downgrade techniques, keep constraints:

```
Scene Intent       → elegance + escalation (restrained dynamics)
Selected Technique → Arc (X-Axis, ≤120° travel) primary; Speed Ramp support on clasp macro
Reason             → orbit grants motion luxury without cuts; one slow-motion clasp
                     beat supplies the single accent the tone allows.
Visual Motif       → watch dial's circle (brand geometry as centerpiece).
Camera/Blocking/   → arc radius 2× case width, ease-in/out, logo face dedicated
  Scale Rule         frame at end azimuth; ramp only at apex, label-side never slowed mid-read.
Storyboard         → setup: watch at rest, crown toward camera / transition:
  Translation        mid-orbit proof frame, landmark B behind / reveal: logo face
                     frontal, held ≥2s.
```

Technique served brand; brand was never sacrificed. **PASS-with-downgrade**
(crash/whip rejected by gate — documented).

---

## Test E — Storyboard

**Brief:** "Convert the Test A perfume direction into board cuts."

Requirement: selection results convert to a real 3–6 cut storyboard direction.

```
CUT 01  True-scale establish. Vanity, daylight. Bottle small among ordinary objects
        (calibration). Static central framing. [key art: no]
CUT 02  Alignment. Bottle edge meets rooftop line of distant model skyline — sizes
        now ambiguous. Locked camera. Deep focus. [transition frame]
CUT 03  Giant reveal. Bottle towers over miniature street; door anchor lower-left.
        Hold 2s. [key art: YES — poster frame]
CUT 04  Mist motif enters at tower base (seeded motif from chain).
CUT 05  Match-cut out: bottle cap circle → sun disc, same screen position, upper third.
        [hands off to next sequence via match-cut contract]
```

Five cuts, each with setup/transition/reveal logic, scale rhythm alternates
(small→ambiguous→monumental→textured→graphic), cut count earned not defaulted,
standalone prompts derivable per hera storyboard contract. **PASS**

---

## Coverage summary

| Test | Focus | Result |
|---|---|---|
| A | Product reveal + identity | PASS |
| B | Tension + spatial expansion combo | PASS |
| C | Motif linkage without repetition | PASS |
| D | Preservation outranks spectacle | PASS (downgrade path exercised) |
| E | 3–6 cut storyboard conversion | PASS |

Structural layer: `python tests/test_technique_contract.py` → ALL GREEN (706 checks).
