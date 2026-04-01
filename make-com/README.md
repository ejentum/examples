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
| **Request content** | `{"query": "{{task_description}}", "mode": "single"}` |

Replace `{{task_description}}` with a variable from a previous module (e.g., a webhook trigger, a form submission, or an AI module's input).

### 3. Parse the response

Add a **JSON > Parse JSON** module after the HTTP request. Map the output:

- `single_ability` contains the scaffold (for Ki mode)
- `multi_ability` contains the scaffold (for Haki mode)

### 4. Inject into your AI module

In your next module (OpenAI, Claude, or any AI module), prepend the scaffold to the system message:

```
[REASONING CONTEXT]
{{scaffold from previous module}}
[END REASONING CONTEXT]

Your original system prompt here.
```

### 5. Modes

- Use `"mode": "single"` for focused tasks (Ki)
- Use `"mode": "multi"` for complex, cross-domain tasks (Haki, requires Haki plan)

## Graceful Degradation

Add an **Error Handler** after the HTTP module. If the request fails, route to your AI module without the scaffold. Your agent continues on native reasoning.

## Links

- [Get your API key](https://ejentum.com/dashboard) (100 free calls, no card)
- [Full integration guide](https://ejentum.com/docs/integrations#makecom)
