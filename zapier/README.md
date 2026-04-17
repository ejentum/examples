# Ejentum Logic API -- Zapier Integration

No-code integration using Zapier's Webhooks action.

## Setup

### 1. Add a "Webhooks by Zapier" action

Choose **POST** as the action event.

### 2. Configure the webhook

| Field | Value |
|-------|-------|
| **URL** | `https://ejentum-main-ab125c3.zuplo.app/logicv1/` |
| **Payload Type** | json |
| **Data** | `query`: your task description from a previous step |
| **Data** | `mode`: `reasoning` (or any mode — see table below) |
| **Headers** | `Authorization`: `Bearer YOUR_EJENTUM_API_KEY` |
| **Headers** | `Content-Type`: `application/json` |

### 3. Use the response

The webhook returns a JSON array. The response key matches the mode name:

- `reasoning` mode → access `reasoning` from the first item
- `code` mode → access `code` from the first item
- `anti-deception` mode → access `anti-deception` from the first item
- `memory` mode → access `memory` from the first item

### 4. Inject into your AI step

In your next Zap step (ChatGPT, Claude, or any AI action), prepend the injection to the prompt:

```
[REASONING CONTEXT]
{{injection from webhook step}}
[END REASONING CONTEXT]

Your original prompt here.
```

## Modes

| Mode | Plan Required | What it returns |
|------|--------------|-----------------|
| `reasoning` | Free / Ki | One reasoning ability (~500 tokens) |
| `code` | Free / Ki | One engineering ability (~500 tokens) |
| `anti-deception` | Free / Ki | One protective ability (~500 tokens) |
| `memory` | Free / Ki | One perceptual ability (~500 tokens) |
| `reasoning-multi` | Haki | Primary + cross-domain guards (~900 tokens) |
| `code-multi` | Haki | Primary + cross-domain guards (~900 tokens) |
| `memory-multi` | Haki | Primary + cross-domain guards (~900 tokens) |

## Links

- [Get your API key](https://ejentum.com/dashboard) (100 free calls, no card)
- [Full integration guide](https://ejentum.com/docs/integrations)
- [Product layers](https://ejentum.com/docs/reasoning_harness)
