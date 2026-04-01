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
| **Data** | `mode`: `single` (or `multi` for Haki) |
| **Headers** | `Authorization`: `Bearer YOUR_EJENTUM_API_KEY` |
| **Headers** | `Content-Type`: `application/json` |

### 3. Use the response

The webhook returns a JSON array. Access the scaffold:

- **Ki mode:** Use `single_ability` from the first item
- **Haki mode:** Use `multi_ability` from the first item

### 4. Inject into your AI step

In your next Zap step (ChatGPT, Claude, or any AI action), prepend the scaffold to the prompt:

```
[REASONING CONTEXT]
{{scaffold from webhook step}}
[END REASONING CONTEXT]

Your original prompt here.
```

## Modes

| Mode | Plan Required | What it returns |
|------|--------------|-----------------|
| `single` | Free or Ki | One reasoning scaffold (~500 tokens) |
| `multi` | Haki | Four synergized scaffolds (~900 tokens) |

## Links

- [Get your API key](https://ejentum.com/dashboard) (100 free calls, no card)
- [Full integration guide](https://ejentum.com/docs/integrations)
