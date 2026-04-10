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

### Files

| File | Lines | Description |
|---|---|---|
| `cmd/mcp-server.py` | 231 | Single-file stdio MCP server |
| `plans/2026-04-08-mcp-server.md` | this file | Plan and implementation record |

Makefile targets added to the existing `Makefile` (no new file):

| Target | Command | Description |
|---|---|---|
| `install-mcp` | `python3 -m pip install --user mcp` | Install MCP Python SDK |
| `run-mcp` | `python3 cmd/mcp-server.py` | Run server for manual testing |

Both targets are listed under `make help`.

---

### Code structure

```
cmd/mcp-server.py
├── Constants
│   ├── KNOWN_RELEASES   — hard-coded list ["release-2.14", "release-2.15", "release-2.16"]
│   ├── DEFAULT_RELEASE  — KNOWN_RELEASES[-1] (latest)
│   └── RAW_BASE         — GitHub raw content URL template
├── HTTP helpers
│   ├── _fetch_json()    — urllib.request, 15s timeout, returns parsed dict
│   ├── _fetch_text()    — urllib.request, 15s timeout, returns decoded str
│   ├── _cache           — module-level dict keyed by (release, kind|"index")
│   ├── _get_index()     — fetch/cache index.json for a release
│   └── _get_schema()    — fetch/cache {Kind}.json for a release
├── Tool helpers
│   ├── _resolve_release() — validates release against KNOWN_RELEASES, falls back to DEFAULT_RELEASE
│   └── _release_arg()     — returns reusable inputSchema fragment for the release parameter
├── Server (mcp.Server("acm-api-docs"))
│   ├── list_tools()     — registers all four tools with JSON Schema inputSchema
│   ├── call_tool()      — top-level dispatcher; catches HTTPError, URLError, KeyError → text error
│   └── _dispatch()      — synchronous per-tool logic
└── Entry point — asyncio.run(main()) via stdio_server()
```

---

### Tool implementations

**`list_releases`**

Returns `{"releases": [...], "default": "release-2.16"}`. No network call.

**`list_crds`**

Fetches `index.json` for the resolved release. Projects each CRD entry to `{kind, apiVersion, scope, description}`. Returns `{"release": ..., "count": N, "crds": [...]}`.

**`get_crd_schema`**

1. Resolves kind case-insensitively against `index.json` (e.g. `managedcluster` → `ManagedCluster`)
2. Fetches `{Kind}.json`
3. Returns the full JSON schema as a pretty-printed string

Not-found error enumerates all available kinds so the caller can correct the name without a separate `list_crds` call.

**`get_crd_example`**

Same kind resolution as `get_crd_schema`. Returns `schema["exampleYAML"]` (a string). Returns a descriptive message if `exampleYAML` is absent or empty rather than raising.

---

### Caching

`_cache` is a module-level `dict[tuple[str, str], object]`. The key is `(release, "index")` for the index and `(release, Kind)` for schemas. Populated lazily on first access per session; never invalidated (the server process is short-lived per MCP client session).

---

### Error handling

`call_tool()` wraps `_dispatch()` in a try/except that catches:

| Exception | Response |
|---|---|
| `urllib.error.HTTPError` | `"Error fetching data from GitHub: HTTP {code} — {reason}"` |
| `urllib.error.URLError` | `"Network error: {reason}"` |
| `KeyError` | `"Not found: {message}"` — used for missing kind, missing field, unknown tool |

Errors are returned as `TextContent` strings, not raised — MCP clients handle them as normal tool results.

---

### Deviations from plan

- `urllib.request` used exclusively — no `httpx` added (as preferred in plan)
- `_fetch_text()` implemented but not called by any current tool — retained as it will be needed if a raw-YAML endpoint is added later
- Case-insensitive kind lookup added (not in plan) — improves UX when callers use lowercase or mixed-case kind names

---

### Alternatives considered and rejected

**Go binary** — evaluated for easier distribution (single downloadable binary). Rejected: the server fetches from raw GitHub URLs at runtime; Go and Python reach those URLs equally well. A rewrite would add `go.mod` and Go toolchain to a Python-only repo with no benefit for the current audience. Revisit if there is demand to distribute this outside the repo.

**`make sync` + local files** — fetch docs to disk first, serve locally. Rejected: adds steps (clone → sync → run) rather than removing them. Fetch-at-runtime is simpler and matches the goal of requiring no local copy of the generated docs.

---

### Usage

Install the dependency:

```sh
make install-mcp
# or: pip install --user mcp
```

Add to `.claude/settings.json` (or equivalent for Cursor / Claude Desktop):

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

Test manually:

```sh
make run-mcp   # starts server on stdio; send JSON-RPC manually or use an MCP inspector
```

---

### Verification

- [x] `make lint` passes (flake8 — no unused imports, correct blank lines)
- [x] `make install-mcp` installs `mcp` package via pip
- [x] `make run-mcp` starts the server process without error
- [x] `make help` lists `install-mcp` and `run-mcp` under the correct section
- [ ] End-to-end test via Claude Code MCP client — connect and call all four tools against `release-2.16`
