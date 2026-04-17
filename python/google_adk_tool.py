"""
Ejentum Logic API -- Google Agent Development Kit (ADK)

Defines Ejentum as a function tool for Google ADK agents.
The agent decides when to call for reasoning augmentation.
"""

import requests
from google.adk.agents import Agent
from google.adk.tools import FunctionTool


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"


def ejentum_injection(query: str, mode: str = "reasoning") -> str:
    """Retrieve a cognitive injection from Ejentum's Logic API.

    Call this before making complex judgments. Returns suppression signals
    that block cognitive shortcuts and a reasoning topology to follow.

    Args:
        query: Describe your current reasoning challenge in 1-2 sentences.
        mode: "reasoning", "code", "anti-deception", "memory", or multi variants.

    Returns:
        A structured cognitive injection to absorb into your reasoning context.
    """
    try:
        r = requests.post(
            EJENTUM_URL,
            headers={
                "Authorization": f"Bearer {EJENTUM_KEY}",
                "Content-Type": "application/json",
            },
            json={"query": query, "mode": mode},
            timeout=5,
        )
        r.raise_for_status()
        key = mode  # response key matches mode name
        return r.json()[0][key]
    except Exception as e:
        return f"Injection unavailable: {e}. Proceed with native reasoning."


# Create the tool and agent
injection_tool = FunctionTool(func=ejentum_injection)

agent = Agent(
    name="analyst",
    model="gemini-2.0-flash",
    instruction=(
        "You are a senior analyst. Before making complex judgments, "
        "call the ejentum_injection tool to get a cognitive injection. "
        "Apply the injection's suppression signals before answering."
    ),
    tools=[injection_tool],
)
