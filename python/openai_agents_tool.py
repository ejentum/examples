"""
Ejentum Logic API -- OpenAI Agents SDK Tool

Defines Ejentum as a function tool for OpenAI's Agents SDK (Responses API).
The agent calls this tool when it needs reasoning augmentation.
"""

import requests
from agents import Agent, Runner, function_tool


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"


@function_tool
def ejentum_injection(query: str, mode: str = "reasoning") -> str:
    """Retrieve a cognitive injection from Ejentum's Logic API.

    Call this before making complex judgments. Returns suppression signals
    that block cognitive shortcuts and a reasoning topology to follow.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "reasoning", "code", "anti-deception", "memory", or multi variants.
    """
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


agent = Agent(
    name="Analyst",
    instructions=(
        "You are a senior analyst. Before making complex judgments, "
        "call the ejentum_injection tool to get a cognitive injection. "
        "Absorb the injection into your reasoning process before answering."
    ),
    tools=[ejentum_injection],
)


async def main():
    result = await Runner.run(
        agent,
        input="Why did our deployment fail after the config change?",
    )
    print(result.final_output)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
