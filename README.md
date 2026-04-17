# Ejentum Integration Examples

Runnable code examples for integrating [Ejentum's Logic API](https://ejentum.com) into your agent, framework, or workflow.

The Logic API retrieves engineered cognitive operations and returns structured cognitive injections. One POST request. These examples show how to make that call from every major environment.

---

## Quick Start

```bash
curl -X POST "https://ejentum-main-ab125c3.zuplo.app/logicv1/" \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Why did deployment fail after the config change?", "mode": "reasoning"}'
```

**7 modes:** `reasoning`, `reasoning-multi`, `code`, `code-multi`, `anti-deception`, `memory`, `memory-multi`

Get your free API key (100 calls, no card): [ejentum.com/dashboard](https://ejentum.com/dashboard)

---

## Examples by Environment

### Language Basics

| File | What it does |
|------|-------------|
| [python/basic.py](python/basic.py) | Minimal POST, parse response, print injection |
| [python/inject_into_agent.py](python/inject_into_agent.py) | Full flow: get injection, prepend to system prompt, call LLM |
| [typescript/basic.ts](typescript/basic.ts) | Fetch-based minimal example |
| [curl/single.sh](curl/single.sh) | Single-mode one-liner (reasoning, code, anti-deception, or memory) |
| [curl/multi.sh](curl/multi.sh) | Multi-mode one-liner (reasoning-multi, code-multi, or memory-multi) |
| [python/graceful_degradation.py](python/graceful_degradation.py) | Production pattern: timeout, retry, fallback |

### Agent Frameworks

| File | Framework | What it does |
|------|-----------|-------------|
| [python/langchain_tool.py](python/langchain_tool.py) | LangChain / LangGraph | `@tool` decorator wrapping Logic API call |
| [python/openai_agents_tool.py](python/openai_agents_tool.py) | OpenAI Agents SDK | Function tool for the Responses API |
| [python/claude_agent_sdk.py](python/claude_agent_sdk.py) | Anthropic Claude SDK | `tool_use` definition for Claude agents |
| [python/crewai_tool.py](python/crewai_tool.py) | CrewAI | `BaseTool` subclass for multi-agent crews |
| [python/pydantic_ai_tool.py](python/pydantic_ai_tool.py) | Pydantic AI | Type-safe tool with async support |
| [python/google_adk_tool.py](python/google_adk_tool.py) | Google ADK | `FunctionTool` for Gemini agents |
| [typescript/vercel_ai_tool.ts](typescript/vercel_ai_tool.ts) | Vercel AI SDK | `tool()` with Zod schema validation |

### IDEs (via MCP or Skill File)

| File | Environment | What it does |
|------|------------|-------------|
| [mcp/ejentum_server.py](mcp/ejentum_server.py) | **All MCP clients** (Cursor, Claude Code, Windsurf, Continue, Cline, Copilot) | MCP server exposing Logic API as a tool. One server, all IDEs. |
| [skill-files/ejentum_logic_api.md](skill-files/ejentum_logic_api.md) | Cursor, Windsurf, Claude Code, Codex | Unified skill file: all 4 harnesses, autonomous routing |
| [skill-files/skill_reasoning.md](skill-files/skill_reasoning.md) | Any agent | Reasoning-only skill file (311 abilities, 6 dimensions) |
| [skill-files/skill_code.md](skill-files/skill_code.md) | Any agent | Code-only skill file (128 abilities, 13 disciplines) |
| [skill-files/skill_anti_deception.md](skill-files/skill_anti_deception.md) | Any agent | Anti-Deception-only skill file (139 abilities) |
| [skill-files/skill_memory.md](skill-files/skill_memory.md) | Any agent | Memory-only skill file (101 abilities, two-pass protocol) |
| [skill-files/.cursorrules](skill-files/.cursorrules) | Cursor | Cursor-specific condensed rules file |

### No-Code

| File | Platform | What it does |
|------|----------|-------------|
| [n8n/ejentum_workflow.json](n8n/ejentum_workflow.json) | n8n | Importable workflow with HTTP Request + AI Agent nodes |
| [make-com/](make-com/) | Make.com | Step-by-step HTTP module setup guide |
| [zapier/](zapier/) | Zapier | Webhooks by Zapier POST setup guide |

---

## How It Works

1. Your agent sends a task description to the Logic API
2. The API returns a structured cognitive injection (~400-900 tokens)
3. You inject it into your agent's context window BEFORE the task
4. The agent reasons with suppression signals active, blocking cognitive shortcuts

```
[REASONING CONTEXT]
{injection from Logic API}
[END REASONING CONTEXT]

{your agent's actual task}
```

**Four product layers:** Reasoning (311 abilities), Code (128), Anti-Deception (139), Memory (101). Choose the mode that matches your task.

---

## Skill Files

Skill files teach an agent how to call the Logic API autonomously. Drop one into your IDE or agent and it handles mode selection, injection, and multi-turn drift monitoring.

- **[Ejentum Skill File (all modes)](skill-files/ejentum_logic_api.md)**. autonomous routing across all 4 harnesses, mode stacking, multi-turn drift monitoring
- **[Reasoning](skill-files/skill_reasoning.md)** · **[Code](skill-files/skill_code.md)** · **[Anti-Deception](skill-files/skill_anti_deception.md)** · **[Memory](skill-files/skill_memory.md)**. product-specific skill files

---

## Builder's Field Notes

28 screenshots from real work sessions. Full guide with images at [ejentum/builders_playbook](https://github.com/ejentum/builders_playbook).

---

## Links

- **Docs:** [ejentum.com/docs](https://ejentum.com/docs)
- **API Reference:** [ejentum.com/docs/api_reference](https://ejentum.com/docs/api_reference)
- **Product Layers:** [Reasoning](https://ejentum.com/docs/reasoning_harness) · [Code](https://ejentum.com/docs/code_harness) · [Anti-Deception](https://ejentum.com/docs/anti_deception) · [Memory](https://ejentum.com/docs/memory_harness)
- **Injection Examples:** [ejentum.com/docs/examples](https://ejentum.com/docs/examples)
- **Benchmarks:** [github.com/ejentum/benchmarks](https://github.com/ejentum/benchmarks)

## License

MIT
