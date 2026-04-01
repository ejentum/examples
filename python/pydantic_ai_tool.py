"""
Ejentum Logic API -- Pydantic AI Tool

Type-safe tool definition for Pydantic AI agents. Uses Pydantic models
for input validation and structured output.
"""

import httpx
from pydantic_ai import Agent, RunContext, Tool
from pydantic import BaseModel


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"


class ScaffoldRequest(BaseModel):
    query: str
    mode: str = "single"


async def get_scaffold(ctx: RunContext[None], query: str, mode: str = "single") -> str:
    """Retrieve a reasoning scaffold from Ejentum's Logic API.

    Call this before making complex judgments. The scaffold provides
    suppression signals that block cognitive shortcuts.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "single" for Ki (1 ability), "multi" for Haki (4 abilities).
    """
    async with httpx.AsyncClient(timeout=5) as client:
        try:
            r = await client.post(
                EJENTUM_URL,
                headers={
                    "Authorization": f"Bearer {EJENTUM_KEY}",
                    "Content-Type": "application/json",
                },
                json={"query": query, "mode": mode},
            )
            r.raise_for_status()
            key = "single_ability" if mode == "single" else "multi_ability"
            return r.json()[0][key]
        except Exception as e:
            return f"Scaffold unavailable: {e}. Proceed with native reasoning."


agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You are a senior analyst. Before making complex judgments, "
        "call the get_scaffold tool to retrieve a reasoning scaffold. "
        "Apply the scaffold's suppression signals before answering."
    ),
    tools=[Tool(get_scaffold)],
)


async def main():
    result = await agent.run(
        "Why did our conversion rate drop 40% after the checkout redesign?"
    )
    print(result.data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
