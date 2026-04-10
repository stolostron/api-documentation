# Task: Grade CRD API Description Quality

> **Invocation:** `gemini -m gemini-3-fast < prompts/grade-crd-descriptions.md`

---

## Context

You are working in the `api-documentation` repository for Red Hat Advanced Cluster Management (ACM) and Multicluster Engine (MCE). This repo generates API reference documentation from Kubernetes CRD YAML files. CRD `description` fields flow **unchanged** from source to output — their quality directly determines documentation quality.

**Key paths:**
- `acm-crds/` — ACM CRDs (downloaded by `make setup-core`; not committed to git)
- `mce-crds/` — MCE CRDs (downloaded by `make setup-core`; not committed to git)
- `tests/test_data/` — Synthetic fixtures for unit tests (always present)
- `grading/` — Where quality reports are written

**Prerequisite:** Run `make setup-core` before this prompt to download real CRDs. Without it, only `tests/test_data/` is available (synthetic, not representative of production quality).

---

## Grading Rubric

| Grade | Criteria | Example |
|---|---|---|
| **Good** | Explains what AND why/when to use the field; units for numeric fields (seconds, bytes, etc.); enum values referenced or explained; non-redundant and specific | `"Timeout in seconds before the reconciliation attempt is aborted"` |
| **Passable** | Correct but minimal; missing units or enum context; slightly redundant but still useful | `"Number of retries to run"` |
| **Needs Improvement** | Absent or empty; repeats the field name; too generic ("Configuration object", "Spec", "List of items"); misleading | `"Configuration object"`, *(absent)* |

---

## Instructions

### Step 1 — Locate CRDs

Check for CRD files:
1. `acm-crds/` and `mce-crds/` — prefer these (real production CRDs)
2. `tests/test_data/` — fall back only if the above are absent

If falling back to test data, add a prominent note in the report:
> **Note:** Real CRDs not found. Run `make setup-core` to download ACM/MCE CRDs. This report covers synthetic test fixtures only.

### Step 2 — Extract Descriptions

For each `.yaml` file in the CRD directories:
1. Parse as YAML
2. Navigate to `spec.versions[*].schema.openAPIV3Schema` (first served/storage version)
3. Check the root schema for a `description`
4. Recursively walk all `properties` at every nesting level
5. Record for each field:
   - **CRD kind** (from `spec.names.kind`)
   - **Field path** in dot-notation (`spec.hubSize`, `status.conditions[].type`)
   - **Description** — the value of the `description` key, or `*(absent)*`
   - **Type** (string, integer, boolean, object, array)
   - **Constraints** — enum values, minimum, maximum, pattern (used to judge grading)

### Step 3 — Grade Each Field

Apply the rubric. Key heuristics:
- **Absent description** → always Needs Improvement
- **Description equals or just restates the field name** → Needs Improvement
- **Generic object/array description** with no specifics → Needs Improvement
- **Numeric field without units** → at most Passable
- **Enum field that doesn't mention valid values** → at most Passable
- **Mentions units, explains purpose, non-redundant** → Good

### Step 4 — Write the Report

Create `grading/crd-descriptions-YYYY-MM-DD.md` using today's date. Structure:

```markdown
# CRD API Description Grading Report

**Date:** YYYY-MM-DD
**Grader:** Gemini CLI (gemini-3-fast)
**Scope:** [acm-crds/ (release-X.Y), mce-crds/ (backplane-X.Y)] or [tests/test_data/ only]
**CRD files graded:** N
**Total fields graded:** N

---

## Grading Rubric
[embed the full rubric table]

---

## Aggregate Summary

| CRD Kind | File | Good | Passable | Needs Improvement | Total |
|---|---|---|---|---|---|
...
| **TOTAL** | | N | N | N | N |

---

## Per-CRD Results

### `KindName` (`relative/path/to/file.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
...

---

## Cross-CRD Patterns

[Common anti-patterns observed across all graded CRDs]

---

## Recommendations

[Top 5 improvements by impact, with specific fields and suggested rewrites]
```

Create the `grading/` directory if it does not exist.

### Step 5 — Report Back

After writing the file, output a summary:
- Path to the report
- Total counts: Good / Passable / Needs Improvement
- The 3–5 specific fields most needing improvement, with their current description and a suggested rewrite
