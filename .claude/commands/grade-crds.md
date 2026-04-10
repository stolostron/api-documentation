# Grade CRD Descriptions

Produce a quality grading report for CRD `description` fields in this repository.

## Goal

Create `grading/crd-descriptions-YYYY-MM-DD.md` (today's date) grading every `description` field found in CRD YAML files.

---

## Step 1 — Locate CRDs

Check for CRD YAML files in this order:

1. `acm-crds/` — ACM CRDs (available after `make setup-core`)
2. `mce-crds/` — MCE CRDs (available after `make setup-core`)
3. `tests/test_data/` — Always present; synthetic fixtures only

If `acm-crds/` and `mce-crds/` are absent, grade `tests/test_data/` and add a prominent note:
> **Note:** Real CRDs not found. Run `make setup-core` to download ACM/MCE CRDs for a meaningful grade. This report covers synthetic test fixtures only.

For each directory present, record which branch it was generated from (check for a `.branch` file or note it as unknown).

---

## Step 2 — Extract Descriptions

For each `.yaml` or `.yml` file in the CRD directories:

1. Parse it as YAML
2. Navigate to `spec.versions[*].schema.openAPIV3Schema` (use the first served/storage version if multiple exist)
3. Recursively walk all `properties` at every nesting level
4. For each field, record:
   - **File path** (relative to repo root)
   - **CRD kind** (from `spec.names.kind`)
   - **Field path** in dot-notation (e.g., `spec.hubSize`, `status.conditions[].type`)
   - **Description text** — the value of the `description` key, or `*(absent)*` if missing
   - **Type** (string, integer, boolean, object, array, etc.)
   - **Constraints** present (enum values, minimum, maximum, pattern) — used to inform grading

Also check if the root `openAPIV3Schema` itself has a `description`.

---

## Step 3 — Apply the Grading Rubric

Grade each field using the following rubric:

### Good
All of these apply:
- Explains **what** the field does and **why/when** to use it (or the consequence of setting it)
- For numeric fields: specifies **units** (seconds, bytes, percentage, count)
- For enum fields: **references valid values** or explains what each means
- Does **not** just repeat the field name
- Is specific enough to be actionable

Examples: `"Timeout in seconds before the reconciliation attempt is aborted"`, `"Maximum number of managed clusters; set to 0 for unlimited"`, `"Phase of the resource lifecycle. One of: Pending, Running, Completed, Failed"`

### Passable
- Correct and unambiguous but minimal
- Missing units, enum context, or behavioral rationale
- Slightly redundant but still useful

Examples: `"Number of retries to run"`, `"Whether the feature is enabled"`, `"Current phase of the resource"`

### Needs Improvement
Any of these apply:
- Absent or empty string
- Just repeats or restates the field name (`"Name is the name"`, `"Items"`)
- Too generic to be useful (`"Configuration object"`, `"Spec"`, `"Status"`, `"List of items"`)
- Misleading or incorrect

Examples: `"Configuration object"`, `"retries"`, *(absent)*

---

## Step 4 — Write the Report

Create `grading/crd-descriptions-YYYY-MM-DD.md` (use today's date). Structure:

```
# CRD API Description Grading Report

**Date:** YYYY-MM-DD
**Grader:** Claude Code
**Scope:** [list dirs graded, e.g., "acm-crds/ (release-2.16), mce-crds/ (backplane-2.11)"]
**CRD files graded:** N
**Total fields graded:** N

---

## Grading Rubric
[embed the full rubric from Step 3]

---

## Aggregate Summary

| CRD Kind | File | Good | Passable | Needs Improvement | Total |
|---|---|---|---|---|---|
| MultiClusterHub | acm-crds/... | 12 | 34 | 8 | 54 |
...
| **TOTAL** | | N | N | N | N |

---

## Per-CRD Results

### `KindName` (`path/to/file.yaml`)

| Field | Type | Description | Grade | Notes |
|---|---|---|---|---|
| `spec` | object | "..." | Passable | ... |
...

[one section per CRD kind]

---

## Cross-CRD Patterns

Common anti-patterns observed across all graded CRDs:
1. ...
2. ...

---

## Recommendations

Top 5 improvements by impact:
1. **[Pattern]** — [specific fields affected, suggested fix]
...
```

Create the `grading/` directory if it does not exist.

---

## Step 5 — Report Back

Tell the user:
- The path to the grading report
- Total counts: Good / Passable / Needs Improvement
- The 3–5 specific fields most in need of improvement (with their current descriptions and suggested improvements)
