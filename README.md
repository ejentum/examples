# Ejentum Integration Examples

Runnable code examples for integrating [Ejentum's Logic API](https://ejentum.com) into your agent, framework, or workflow.

The Logic API retrieves engineered cognitive operations and returns structured reasoning scaffolds. One POST request. These examples show how to make that call from every major environment.

---

## Quick Start

```bash
curl -X POST "https://ejentum-main-ab125c3.zuplo.app/logicv1/" \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Why did deployment fail after the config change?", "mode": "single"}'
```

Get your free API key (100 calls, no card): [ejentum.com/dashboard](https://ejentum.com/dashboard)

---

## Examples by Environment

### Language Basics

| File | What it does |
|------|-------------|
| [python/basic.py](python/basic.py) | Minimal POST, parse response, print scaffold |
| [python/inject_into_agent.py](python/inject_into_agent.py) | Full flow: get scaffold, prepend to system prompt, call LLM |
| [typescript/basic.ts](typescript/basic.ts) | Fetch-based minimal example |
| [curl/single.sh](curl/single.sh) | Ki mode one-liner |
| [curl/multi.sh](curl/multi.sh) | Haki mode one-liner |
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
| [skill-files/ejentum_logic_api.md](skill-files/ejentum_logic_api.md) | Cursor, Windsurf, Claude Code, Codex | Drop-in rules/skill file |
| [skill-files/.cursorrules](skill-files/.cursorrules) | Cursor | Cursor-specific rules file |

### No-Code

| File | Platform | What it does |
|------|----------|-------------|
| [n8n/ejentum_workflow.json](n8n/ejentum_workflow.json) | n8n | Importable workflow with HTTP Request + AI Agent nodes |
| [make-com/](make-com/) | Make.com | Step-by-step HTTP module setup guide |
| [zapier/](zapier/) | Zapier | Webhooks by Zapier POST setup guide |

---

## How It Works

1. Your agent sends a task description to the Logic API
2. The API returns a structured reasoning scaffold (Ki: ~500 tokens, Haki: ~900 tokens)
3. You inject the scaffold into your agent's system prompt BEFORE the task
4. The agent reasons with suppression signals active, blocking cognitive shortcuts

```
[REASONING CONTEXT]
{scaffold from Logic API}
[END REASONING CONTEXT]

{your agent's actual task}
```

---

## Builder's Field Notes

28 screenshots from real work sessions. Full guide with images at [ejentum/builders_playbook](https://github.com/ejentum/builders_playbook).

---

## Links

- **Docs:** [ejentum.com/docs](https://ejentum.com/docs)
- **API Reference:** [ejentum.com/docs/api_reference](https://ejentum.com/docs/api_reference)
- **Injection Examples:** [ejentum.com/docs/examples](https://ejentum.com/docs/examples)
- **Response Examples:** [ejentum.com/docs/response_examples](https://ejentum.com/docs/response_examples)
- **Benchmarks:** [github.com/ejentum/benchmarks](https://github.com/ejentum/benchmarks)
- **Field Notes:** [ejentum.com/docs/field_notes](https://ejentum.com/docs/field_notes)

## License

MIT
