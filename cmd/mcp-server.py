#!/usr/bin/env python3
"""
MCP stdio server for ACM/MCE API documentation.

Fetches CRD schemas from published api-docs/ai/ output on GitHub.
No local copy of generated docs required.

Usage (Claude Code):
  {
    "mcpServers": {
      "acm-api-docs": {
        "command": "python3",
        "args": ["/path/to/api-documentation/cmd/mcp-server.py"]
      }
    }
  }
"""

import asyncio
import json
import urllib.request
import urllib.error

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ── Release configuration ────────────────────────────────────────────────────

KNOWN_RELEASES = [
    "release-2.14",
    "release-2.15",
    "release-2.16",
]
DEFAULT_RELEASE = KNOWN_RELEASES[-1]

RAW_BASE = "https://raw.githubusercontent.com/stolostron/api-documentation/{release}/api-docs/ai"

# ── HTTP helpers ─────────────────────────────────────────────────────────────


def _fetch_json(url: str) -> dict:
    """Fetch and parse JSON from a URL. Raises urllib.error.HTTPError on failure."""
    with urllib.request.urlopen(url, timeout=15) as resp:
        return json.loads(resp.read())


def _fetch_text(url: str) -> str:
    """Fetch raw text from a URL."""
    with urllib.request.urlopen(url, timeout=15) as resp:
        return resp.read().decode("utf-8")


# Per-session in-memory cache: (release, kind|"index") -> data
_cache: dict[tuple[str, str], object] = {}


def _get_index(release: str) -> dict:
    key = (release, "index")
    if key not in _cache:
        url = RAW_BASE.format(release=release) + "/index.json"
        _cache[key] = _fetch_json(url)
    return _cache[key]  # type: ignore[return-value]


def _get_schema(release: str, kind: str) -> dict:
    key = (release, kind)
    if key not in _cache:
        url = RAW_BASE.format(release=release) + f"/{kind}.json"
        _cache[key] = _fetch_json(url)
    return _cache[key]  # type: ignore[return-value]


# ── Tool helpers ─────────────────────────────────────────────────────────────

def _resolve_release(release: str | None) -> str:
    return release if release in KNOWN_RELEASES else DEFAULT_RELEASE


def _release_arg() -> dict:
    return {
        "release": {
            "type": "string",
            "description": (
                f"Release branch name (e.g. 'release-2.16'). "
                f"Defaults to '{DEFAULT_RELEASE}'. "
                f"Known values: {', '.join(KNOWN_RELEASES)}."
            ),
        }
    }


# ── Server setup ─────────────────────────────────────────────────────────────

server = Server("acm-api-docs")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="list_releases",
            description="List the known ACM/MCE release branches that have published API documentation.",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        types.Tool(
            name="list_crds",
            description=(
                "List all CRDs available in the API documentation index for a given release. "
                "Returns kind, apiVersion, scope, and a short description for each CRD."
            ),
            inputSchema={
                "type": "object",
                "properties": _release_arg(),
                "required": [],
            },
        ),
        types.Tool(
            name="get_crd_schema",
            description=(
                "Return the full JSON schema for a named CRD, including all spec and status fields "
                "with types, descriptions, and validation constraints."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "description": "The CRD kind name, e.g. 'ManagedCluster'.",
                    },
                    **_release_arg(),
                },
                "required": ["kind"],
            },
        ),
        types.Tool(
            name="get_crd_example",
            description=(
                "Return an example YAML manifest for a named CRD with representative field values."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "description": "The CRD kind name, e.g. 'ManagedCluster'.",
                    },
                    **_release_arg(),
                },
                "required": ["kind"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    try:
        result = _dispatch(name, arguments)
    except urllib.error.HTTPError as e:
        result = f"Error fetching data from GitHub: HTTP {e.code} — {e.reason}"
    except urllib.error.URLError as e:
        result = f"Network error: {e.reason}"
    except KeyError as e:
        result = f"Not found: {e}"
    return [types.TextContent(type="text", text=result)]


def _dispatch(name: str, args: dict) -> str:
    if name == "list_releases":
        return json.dumps({"releases": KNOWN_RELEASES, "default": DEFAULT_RELEASE}, indent=2)

    release = _resolve_release(args.get("release"))

    if name == "list_crds":
        index = _get_index(release)
        rows = [
            {
                "kind": c["kind"],
                "apiVersion": c["apiVersion"],
                "scope": c.get("scope", ""),
                "description": c.get("description", ""),
            }
            for c in index["crds"]
        ]
        return json.dumps({"release": release, "count": len(rows), "crds": rows}, indent=2)

    if name in ("get_crd_schema", "get_crd_example"):
        kind = args.get("kind", "").strip()
        if not kind:
            raise KeyError("'kind' argument is required")

        # Case-insensitive kind lookup via index
        index = _get_index(release)
        match = next(
            (c for c in index["crds"] if c["kind"].lower() == kind.lower()),
            None,
        )
        if match is None:
            available = ", ".join(c["kind"] for c in index["crds"])
            raise KeyError(
                f"Kind '{kind}' not found in {release}. Available: {available}"
            )

        schema = _get_schema(release, match["kind"])

        if name == "get_crd_schema":
            return json.dumps(schema, indent=2)

        # get_crd_example
        example = schema.get("exampleYAML", "")
        if not example:
            return f"No example YAML available for {match['kind']} in {release}."
        return example

    raise KeyError(f"Unknown tool: {name}")


# ── Entry point ──────────────────────────────────────────────────────────────

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
