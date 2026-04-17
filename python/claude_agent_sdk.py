"""
Ejentum Logic API -- Anthropic Claude Agent SDK

Defines Ejentum as a tool for Claude agents using the Anthropic SDK.
The agent decides when to call for reasoning augmentation.
"""

import json
import requests
import anthropic


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"

# Define the Ejentum tool for Claude
ejentum_tool = {
    "name": "ejentum_injection",
    "description": (
        "Retrieve a cognitive injection from Ejentum's Logic API. "
        "Call this before making complex judgments. Returns suppression signals "
        "that block cognitive shortcuts and a reasoning topology to follow."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Describe your current reasoning challenge in 1-2 sentences.",
            },
            "mode": {
                "type": "string",
                "enum": ["reasoning", "reasoning-multi", "anti-deception", "code", "code-multi", "memory", "memory-multi"],
                "description": "reasoning for general tasks. Also: code, anti-deception, memory, and multi variants.",
            },
        },
        "required": ["query"],
    },
}


def call_ejentum(query: str, mode: str = "reasoning") -> str:
    """Execute the Ejentum API call."""
    try:
        r = requests.post(
            EJENTUM_URL,
            headers={"Authorization": f"Bearer {EJENTUM_KEY}", "Content-Type": "application/json"},
            json={"query": query, "mode": mode},
            timeout=5,
        )
        key = mode  # response key matches mode name
        return r.json()[0][key]
    except Exception as e:
        return f"Injection unavailable: {e}. Proceed with native reasoning."


def run_agent(task: str):
    client = anthropic.Anthropic()

    messages = [{"role": "user", "content": task}]

    # First call: Claude may decide to use the Ejentum tool
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=(
            "You are a senior analyst. Before making complex judgments, "
            "call the ejentum_injection tool to get a cognitive injection. "
            "Absorb the injection into your reasoning process."
        ),
        tools=[ejentum_tool],
        messages=messages,
    )

    # Handle tool use loop
    while response.stop_reason == "tool_use":
        tool_block = next(b for b in response.content if b.type == "tool_use")
        tool_input = tool_block.input

        # Call Ejentum
        injection = call_ejentum(
            query=tool_input["query"],
            mode=tool_input.get("mode", "reasoning"),
        )

        # Return injection to Claude
        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_block.id,
                    "content": injection,
                }
            ],
        })

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=(
                "You are a senior analyst. Apply the cognitive injection you received."
            ),
            tools=[ejentum_tool],
            messages=messages,
        )

    # Extract final text
    text = next((b.text for b in response.content if hasattr(b, "text")), "")
    print(text)


if __name__ == "__main__":
    run_agent("Why did our conversion rate drop 40% after the checkout redesign?")
