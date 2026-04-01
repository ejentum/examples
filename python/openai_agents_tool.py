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
def ejentum_scaffold(query: str, mode: str = "single") -> str:
    """Retrieve a reasoning scaffold from Ejentum's Logic API.

    Call this before making complex judgments. Returns suppression signals
    that block cognitive shortcuts and a reasoning topology to follow.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "single" for focused tasks, "multi" for cross-domain analysis.
    """
    try:
        r = requests.post(
            EJENTUM_URL,
            headers={"Authorization": f"Bearer {EJENTUM_KEY}", "Content-Type": "application/json"},
            json={"query": query, "mode": mode},
            timeout=5,
        )
        key = "single_ability" if mode == "single" else "multi_ability"
        return r.json()[0][key]
    except Exception as e:
        return f"Scaffold unavailable: {e}. Proceed with native reasoning."


agent = Agent(
    name="Analyst",
    instructions=(
        "You are a senior analyst. Before making complex judgments, "
        "call the ejentum_scaffold tool to get a reasoning scaffold. "
        "Inject the scaffold into your reasoning process before answering."
    ),
    tools=[ejentum_scaffold],
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
