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


class InjectionRequest(BaseModel):
    query: str
    mode: str = "reasoning"


async def get_injection(ctx: RunContext[None], query: str, mode: str = "reasoning") -> str:
    """Retrieve a cognitive injection from Ejentum's Logic API.

    Call this before making complex judgments. The injection provides
    suppression signals that block cognitive shortcuts.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "reasoning", "code", "anti-deception", "memory", or multi variants.
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
            key = mode  # response key matches mode name
            return r.json()[0][key]
        except Exception as e:
            return f"Injection unavailable: {e}. Proceed with native reasoning."


agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You are a senior analyst. Before making complex judgments, "
        "call the get_injection tool to retrieve a cognitive injection. "
        "Apply the injection's suppression signals before answering."
    ),
    tools=[Tool(get_injection)],
)


async def main():
    result = await agent.run(
        "Why did our conversion rate drop 40% after the checkout redesign?"
    )
    print(result.data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
