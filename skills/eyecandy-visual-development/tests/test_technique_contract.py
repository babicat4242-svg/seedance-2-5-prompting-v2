"""Structural contract validator for the eyecandy-visual-development skill.

Validation-first: this must FAIL before any skill content exists and PASS only
when every technique file honors the full section contract, source/derived
separation, model-agnosticism rule, and taxonomy cross-references.

Run from the skill root:
    python tests/test_technique_contract.py
Exit code 0 = all checks green.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    "Technique Identity",
    "Use When",
    "Avoid When",
    "Required Inputs",
    "Directing Rule",
    "Storyboard Translation",
    "Image Generation Translation",
    "Video Generation Translation",
    "Failure Modes",
    "Preservation Rules",
]

REQUIRED_FRONTMATTER_FIELDS = ["technique", "source", "source_status", "family", "intents"]

VALID_FAMILIES = {
    "reveal",
    "transition",
    "camera-movement",
    "subject-bound",
    "time",
    "composition",
}

VALID_INTENTS = {
    "reveal",
    "tension",
    "escalation",
    "elegance",
    "impact",
    "spatial-expansion",
    "transition",
    "visual-hook",
    "climax",
    "scale-perception",
    "motif-linkage",
    "isolation",
}

VALID_SOURCE_STATUS = {"page-definition", "taxonomy-verified"}

# Techniques must stay model-agnostic: no generation-API grammar allowed.
FORBIDDEN_MODEL_TOKENS = [
    "@image1",
    "@video1",
    "@audio1",
    "$imagegen",
    "seedance",
    "Seedance",
    "midjourney",
    "Midjourney",
    "nano-banana",
    "GPT Image",
    "--ar ",
    "--cref",
    "Veo ",
    "Sora",
    "Kling",
    "Runway Gen",
]

MARKER_SOURCE_GROUNDED = "<!-- SOURCE-GROUNDED -->"
MARKER_DERIVED = "<!-- DERIVED -->"

failures: list[str] = []
checks = 0


def check(condition: bool, message: str) -> bool:
    global checks
    checks += 1
    if not condition:
        failures.append(message)
    return condition


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML-ish frontmatter parser for flat `key: value` fields."""
    meta: dict[str, str] = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return meta
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def validate_skill_md() -> None:
    skill_md = SKILL_ROOT / "SKILL.md"
    if not check(skill_md.is_file(), "SKILL.md exists at skill root"):
        return
    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    check(meta.get("name") == "eyecandy-visual-development", "SKILL.md frontmatter name is correct")
    check(
        len(meta.get("description", "")) >= 40,
        "SKILL.md frontmatter description is substantive (>= 40 chars)",
    )
    for token in ["eyecannndy.com", "Scene Intent", "Avoid"]:
        check(token in text, f"SKILL.md mentions '{token}'")
    check("techniques/" in text, "SKILL.md routes to techniques/ directory")


def validate_openai_yaml() -> None:
    yaml_path = SKILL_ROOT / "agents" / "openai.yaml"
    if not check(yaml_path.is_file(), "agents/openai.yaml exists (Codex interface convention)"):
        return
    text = yaml_path.read_text(encoding="utf-8")
    for field in ["display_name", "short_description", "default_prompt"]:
        check(field in text, f"openai.yaml contains {field}")


def validate_taxonomy() -> None:
    taxonomy = SKILL_ROOT / "references" / "taxonomy.md"
    if not check(taxonomy.is_file(), "references/taxonomy.md exists"):
        return
    text = taxonomy.read_text(encoding="utf-8")
    check(text.count("/technique/") >= 130, "taxonomy.md lists at least 130 category slugs")
    check("forever WIP" in text, "taxonomy.md preserves the site's own WIP disclaimer")
    # Every deep technique file must be cross-referenced from the taxonomy.
    for tech_file in sorted((SKILL_ROOT / "techniques").glob("*.md")):
        if tech_file.name.startswith("_"):
            continue
        slug = tech_file.stem
        check(
            f"/technique/{slug}" in text,
            f"taxonomy.md contains /technique/{slug} referenced by {tech_file.name}",
        )


def validate_technique_file(path: Path) -> None:
    name = path.name
    text = path.read_text(encoding="utf-8")

    meta = parse_frontmatter(text)
    for field in REQUIRED_FRONTMATTER_FIELDS:
        check(field in meta, f"{name}: frontmatter has '{field}'")
    if not meta:
        return

    slug = path.stem
    check(
        f"https://eyecannndy.com/technique/{slug}" in meta.get("source", ""),
        f"{name}: source URL matches https://eyecannndy.com/technique/{slug}",
    )
    check(
        meta.get("source_status") in VALID_SOURCE_STATUS,
        f"{name}: source_status is one of {sorted(VALID_SOURCE_STATUS)}",
    )
    check(meta.get("family") in VALID_FAMILIES, f"{name}: family is valid ({meta.get('family')})")

    raw_intents = meta.get("intents", "")
    intents = [i.strip() for i in raw_intents.strip("[]").split(",") if i.strip()]
    check(len(intents) >= 1, f"{name}: at least one intent declared")
    bad_intents = [i for i in intents if i not in VALID_INTENTS]
    check(not bad_intents, f"{name}: intents valid, found invalid {bad_intents}")

    for section in REQUIRED_SECTIONS:
        check(f"## {section}" in text, f"{name}: has '## {section}' section")

    check(
        MARKER_SOURCE_GROUNDED in text,
        f"{name}: contains {MARKER_SOURCE_GROUNDED} marker separating source material",
    )
    check(
        MARKER_DERIVED in text,
        f"{name}: contains {MARKER_DERIVED} marker separating derived rules",
    )

    lowered_tail = text
    for token in FORBIDDEN_MODEL_TOKENS:
        check(token not in lowered_tail, f"{name}: free of model-specific token '{token.strip()}'")

    check(
        re.search(r"[Ff]oreground|subject|camera", text) is not None,
        f"{name}: directing language present (camera/subject/foreground terms)",
    )


def validate_template() -> None:
    template = SKILL_ROOT / "techniques" / "_template.md"
    check(template.is_file(), "techniques/_template.md exists as canonical section contract")
    if template.is_file():
        text = template.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            check(f"## {section}" in text, f"_template.md documents '## {section}'")


def main() -> int:
    validate_skill_md()
    validate_openai_yaml()
    validate_taxonomy()
    validate_template()

    techniques_dir = SKILL_ROOT / "techniques"
    technique_files = []
    if techniques_dir.is_dir():
        technique_files = [
            p for p in sorted(techniques_dir.glob("*.md")) if not p.name.startswith("_")
        ]
    check(len(technique_files) >= 15, f"at least 15 technique files exist (found {len(technique_files)})")
    for path in technique_files:
        validate_technique_file(path)

    print(f"eyecandy-visual-development contract validation: {checks - len(failures)}/{checks} checks passed")
    if failures:
        print("\nFAILURES:")
        for failure in failures:
            print(f"  [FAIL] {failure}")
        return 1
    print("ALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
