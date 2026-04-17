# Ejentum Logic API -- Make.com Integration

No-code integration using Make.com's HTTP module.

## Setup

### 1. Create a new scenario

Add an **HTTP > Make a request** module.

### 2. Configure the HTTP module

| Field | Value |
|-------|-------|
| **URL** | `https://ejentum-main-ab125c3.zuplo.app/logicv1/` |
| **Method** | POST |
| **Headers** | `Authorization: Bearer YOUR_EJENTUM_API_KEY` |
| **Headers** | `Content-Type: application/json` |
| **Body type** | Raw |
| **Content type** | JSON (application/json) |
| **Request content** | `{"query": "{{task_description}}", "mode": "reasoning"}` |

Replace `{{task_description}}` with a variable from a previous module (e.g., a webhook trigger, a form submission, or an AI module's input).

### 3. Parse the response

Add a **JSON > Parse JSON** module after the HTTP request. Map the output:

- The response key matches the mode name: `reasoning`, `code`, `anti-deception`, `memory`, etc.

### 4. Inject into your AI module

In your next module (OpenAI, Claude, or any AI module), prepend the injection to the system message:

```
[REASONING CONTEXT]
{{injection from previous module}}
[END REASONING CONTEXT]

Your original system prompt here.
```

### 5. Modes

| Mode | What it does | Plan required |
|------|-------------|---------------|
| `reasoning` | General reasoning ability (311 abilities) | Free / Ki |
| `code` | Code generation, refactoring, architecture (128 abilities) | Free / Ki |
| `anti-deception` | Blocks sycophancy, hallucination, injection (139 abilities) | Free / Ki |
| `memory` | Perception sharpening, state tracking (101 abilities) | Free / Ki |
| `reasoning-multi` | Primary + cross-domain failure guards | Haki |
| `code-multi` | Primary + cross-domain engineering guards | Haki |
| `memory-multi` | Primary + cross-domain perceptual guards | Haki |

## Graceful Degradation

Add an **Error Handler** after the HTTP module. If the request fails, route to your AI module without the injection. Your agent continues on native reasoning.

## Links

- [Get your API key](https://ejentum.com/dashboard) (100 free calls, no card)
- [Full integration guide](https://ejentum.com/docs/integrations)
- [Product layers](https://ejentum.com/docs/reasoning_harness)
