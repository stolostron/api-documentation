# MCP Server for ACM/MCE API Documentation

**Date:** 2026-04-08  
**Status:** Implemented

---

## Goal

Create a minimal stdio MCP server that exposes ACM/MCE CRD schemas to any MCP-compatible client (Claude Code, Claude Desktop, Cursor, etc.) by fetching data from the published `api-docs/ai/` output on GitHub raw content URLs. The server lives in this repo and requires no local copy of the generated docs.

---

## Data Sources

The generated `api-docs/ai/` directory is committed to each release branch (not `main`) and accessible via:

```
https://raw.githubusercontent.com/stolostron/api-documentation/{release}/api-docs/ai/index.json
https://raw.githubusercontent.com/stolostron/api-documentation/{release}/api-docs/ai/{Kind}.json
```

Supported releases: `release-2.14`, `release-2.15`, `release-2.16` (and future branches).

---

## Plan

### Phase 1 — Minimal stdio MCP server (Python)

**File:** `cmd/mcp-server.py`

Single-file implementation using the MCP Python SDK (`mcp`) over stdio transport.

#### Tools to expose

| Tool | Description | Args |
|---|---|---|
| `list_crds` | List all CRDs in the index with kind, apiVersion, scope, and description | `release` (optional, default: latest) |
| `get_crd_schema` | Return full JSON schema for a named CRD | `kind` (required), `release` (optional) |
| `get_crd_example` | Return example YAML for a named CRD | `kind` (required), `release` (optional) |
| `list_releases` | Return known release branch names | — |

#### Design decisions

- **No local cache on startup** — fetch on first call per session, then cache in-memory for the session lifetime
- **Release defaulting** — `list_releases` returns known branches; default is the latest known release
- **Error handling** — return a descriptive error string (not raise) if GitHub fetch fails; caller can retry with a different release
- **No auth** — raw GitHub content for public repos requires no token

#### Release list

Hard-coded initially: `["release-2.14", "release-2.15", "release-2.16"]`. New releases are added here when a new workflow is created.

---

### Phase 2 — Makefile integration

Add targets:
```makefile
install-mcp    # pip install mcp dependency
run-mcp        # python3 cmd/mcp-server.py (for manual testing)
```

---

### Phase 3 — Claude Code config snippet

Add a usage note to README (or a new `MCP.md`) showing the config block users add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "acm-api-docs": {
      "command": "python3",
      "args": ["/path/to/api-documentation/cmd/mcp-server.py"]
    }
  }
}
```

---

## File Layout

```
cmd/
  gen-api-docs.py       (existing)
  mcp-server.py         (new — Phase 1)
```

---

## Dependencies

- Python 3.11+  
- `mcp` PyPI package (MCP Python SDK)  
- `httpx` or `urllib.request` (stdlib) for HTTP fetching  

Prefer stdlib `urllib.request` for fetching to avoid adding a dependency beyond `mcp`.

---

## Out of Scope (for now)

- HTTP/SSE transport (stdio only for v1)
- Search across fields within a CRD
- Serving local `api-docs/ai/` as fallback
- Auto-detecting the latest release from GitHub API

---

## Implementation

### What was built

**`cmd/mcp-server.py`** — single-file Python, ~160 lines. All four planned tools implemented.

### Deviations from plan

- `list_releases` added as a first-class tool (was implicit in plan, not listed as a named tool)
- `urllib.request` used for HTTP (as preferred); no `httpx` dependency
- Case-insensitive kind lookup via index — `managedcluster` resolves to `ManagedCluster`; not-found error includes the full list of available kinds

### Alternatives considered and rejected

**Go binary** — evaluated for easier distribution (single downloadable binary). Rejected: the server fetches from raw GitHub URLs at runtime; Go and Python reach those URLs equally well. A rewrite would add `go.mod` and Go toolchain to a Python-only repo with no benefit for the current audience. Revisit if there is demand to distribute this outside the repo.

**`make sync` + local files** — fetch docs to disk first, serve locally. Rejected: adds steps (clone → sync → run) rather than removing them. Fetch-at-runtime is simpler.

### Usage

Install the dependency:
```sh
make install-mcp
# or: pip install --user mcp
```

Add to `.claude/settings.json`:
```json
{
  "mcpServers": {
    "acm-api-docs": {
      "command": "python3",
      "args": ["/path/to/api-documentation/cmd/mcp-server.py"]
    }
  }
}
```
