"""
Ejentum Logic API -- LangChain / LangGraph Tool

Defines Ejentum as a tool that any LangChain or LangGraph agent can call.
The agent decides when it needs reasoning augmentation and calls the tool itself.
"""

import requests
from langchain_core.tools import tool


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"


@tool
def ejentum_injection(query: str, mode: str = "reasoning") -> str:
    """Retrieve a cognitive injection from Ejentum's Logic API.

    Call this before making complex judgments. The injection provides:
    - A failure pattern to avoid (Negative Gate)
    - Suppression signals that block cognitive shortcuts
    - A falsification test to verify your reasoning

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


# Usage with a LangChain agent:
#
# from langchain_openai import ChatOpenAI
# from langgraph.prebuilt import create_react_agent
#
# llm = ChatOpenAI(model="gpt-4o")
# agent = create_react_agent(llm, tools=[ejentum_injection])
# result = agent.invoke({"messages": [("user", "Analyze this causal chain...")]})
