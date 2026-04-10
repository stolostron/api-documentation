# ACM/MCE API Documentation — Gemini Project Context

This file is auto-loaded by Gemini CLI when run from this repository root. It provides context for working with this codebase.

---

## What This Repo Does

Generates API reference documentation for Red Hat Advanced Cluster Management (ACM) and Multicluster Engine (MCE) from Kubernetes Custom Resource Definitions (CRDs).

The main script (`cmd/gen-api-docs.py`) reads CRD YAML files and Go `_types.go` structs, extracts field descriptions, validation constraints, and enum values, then produces:
- Markdown API reference tables (`api-docs/`)
- JSON schemas for AI consumption (`api-docs/ai/`)
- Example YAML files and an index for discovery

**CRD descriptions flow unchanged from source to output.** The generator does not augment them — description quality in the CRDs directly determines documentation quality.

---

## Key Paths

| Path | Purpose |
|---|---|
| `cmd/gen-api-docs.py` | Main documentation generator |
| `acm-crds/` | ACM CRDs (not committed; downloaded by `make setup-core`) |
| `mce-crds/` | MCE CRDs (not committed; downloaded by `make setup-core`) |
| `tests/test_data/` | Synthetic CRD fixtures for unit tests |
| `api-docs/` | Generated documentation (not committed) |
| `grading/` | CRD description quality reports |
| `plans/` | Implementation plans |
| `prompts/` | Reusable prompt files for Gemini CLI |

---

## External CRD Sources

Real CRDs are cloned from:
- `stolostron/multiclusterhub-operator` (`RELEASE_BRANCH`) → `acm-crds/`
- `stolostron/backplane-operator` (`BACKPLANE_BRANCH`) → `mce-crds/`
- `stolostron/ocm` (`BACKPLANE_BRANCH`) → `mce-crds/` (merged)

---

## Common Commands

```sh
make setup-core                    # Download real CRDs (required before grading or generating)
make generate                      # Generate API docs (prompts for branch numbers)
make test                          # Run all tests
make help                          # Show all available targets
```

---

## Recipe: Grade CRD Descriptions

When asked to grade CRD description quality, follow this workflow.

**Recommended invocation:**
```sh
gemini -m gemini-3-fast < prompts/grade-crd-descriptions.md
```

Or interactively: ask Gemini to "grade the CRD descriptions and write a report to grading/".

### Grading Rubric

| Grade | Criteria | Example |
|---|---|---|
| **Good** | Explains what AND why/when; units for numeric fields; enum values referenced; non-redundant | `"Timeout in seconds before the reconciliation attempt is aborted"` |
| **Passable** | Correct but minimal; missing units/enum context or slightly redundant | `"Number of retries to run"` |
| **Needs Improvement** | Absent, repeats field name, or too generic | `"Configuration object"`, *(absent)* |

### Step 1 — Locate CRDs

Check in order:
1. `acm-crds/` and `mce-crds/` — real CRDs (require `make setup-core`)
2. `tests/test_data/` — fall back with a note that these are synthetic fixtures

### Step 2 — Extract Descriptions

For each `.yaml` file, navigate to `spec.versions[*].schema.openAPIV3Schema` and walk all `properties` recursively. Record:
- Field path (dot-notation, e.g., `spec.hubSize`)
- Description text (or "absent")
- Type and any constraints (enum, min, max, pattern)

### Step 3 — Grade Each Field

Apply the rubric above. Pay special attention to:
- Numeric fields without units → at most Passable
- Enum fields that don't reference valid values → at most Passable
- Absent or purely generic descriptions → Needs Improvement

### Step 4 — Write the Report

Output to `grading/crd-descriptions-YYYY-MM-DD.md` (today's date). Include:
- Header: date, scope, total counts
- Aggregate summary table: CRD | Good | Passable | Needs Improvement | Total
- Per-CRD detail table: Field | Type | Description | Grade | Notes
- Cross-CRD patterns: common anti-patterns observed
- Recommendations: top 5 improvements by impact

### Step 5 — Report Back

Summarize: total counts, the grading file path, and the 3–5 specific fields most needing improvement with suggested rewrites.
