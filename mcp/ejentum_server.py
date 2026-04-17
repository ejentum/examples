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
async def query_logic_api(query: str, mode: str = "reasoning") -> str:
    """Retrieve a cognitive injection from Ejentum's Logic API.

    Call this before making complex judgments, debugging, code review,
    or any task where reasoning quality matters. The injection provides
    suppression signals that block cognitive shortcuts.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: One of: "reasoning", "reasoning-multi", "code", "code-multi",
              "anti-deception", "memory", "memory-multi".

    Returns:
        A structured cognitive injection to absorb into your reasoning context.
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
        key = mode  # response key matches mode name
        return r.json()[0][key]


@mcp.tool()
async def query_logic_api_multi(query: str, mode: str = "reasoning-multi") -> str:
    """Retrieve a compound cognitive injection (multi mode: primary + cross-domain guards).

    Use this for complex, cross-domain tasks that span multiple reasoning
    dimensions. Returns merged suppression vectors from multiple abilities.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: One of: "reasoning-multi", "code-multi", "memory-multi".
    """
    return await query_logic_api(query, mode=mode)


if __name__ == "__main__":
    mcp.run()
