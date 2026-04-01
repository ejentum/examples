"""
Ejentum Logic API -- MCP Server

A Model Context Protocol server that exposes Ejentum's Logic API as a tool.
Works with ALL MCP-compatible clients: Cursor, Claude Code, Windsurf,
Continue, Cline, GitHub Copilot, Roo Code.

Install:
    pip install mcp httpx

Configure in your IDE:
    Cursor:      .cursor/mcp.json
    Claude Code: ~/.claude/claude_desktop_config.json
    Windsurf:    .windsurf/mcp.json

Example config:
    {
        "mcpServers": {
            "ejentum": {
                "command": "python",
                "args": ["path/to/ejentum_server.py"],
                "env": {
                    "EJENTUM_API_KEY": "YOUR_KEY"
                }
            }
        }
    }
"""

import os
import httpx
from mcp.server.fastmcp import FastMCP

EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
API_KEY = os.environ.get("EJENTUM_API_KEY", "YOUR_EJENTUM_API_KEY")

mcp = FastMCP("ejentum")


@mcp.tool()
async def query_logic_api(query: str, mode: str = "single") -> str:
    """Retrieve a reasoning scaffold from Ejentum's Logic API.

    Call this before making complex judgments, debugging, code review,
    or any task where reasoning quality matters. The scaffold provides
    suppression signals that block cognitive shortcuts.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "single" for Ki (1 focused ability), "multi" for Haki (4 synergized abilities).

    Returns:
        A structured reasoning scaffold to inject into your reasoning context.
    """
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            EJENTUM_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={"query": query, "mode": mode},
        )
        r.raise_for_status()
        key = "single_ability" if mode == "single" else "multi_ability"
        return r.json()[0][key]


@mcp.tool()
async def query_logic_api_haki(query: str) -> str:
    """Retrieve a compound reasoning scaffold (Haki mode: 4 synergized abilities).

    Use this for complex, cross-domain tasks that span multiple reasoning
    dimensions (e.g., causal + temporal + spatial). Returns merged suppression
    vectors from 4 abilities: primary, dependency, amplifier, alternative.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
    """
    return await query_logic_api(query, mode="multi")


if __name__ == "__main__":
    mcp.run()
