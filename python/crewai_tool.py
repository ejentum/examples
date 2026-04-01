"""
Ejentum Logic API -- CrewAI Tool

Defines Ejentum as a tool for CrewAI agents. Each crew member can call
the Logic API before executing its task. The scaffold is injected into
the agent's reasoning context via the backstory or tool result.
"""

import requests
from crewai.tools import BaseTool
from pydantic import Field


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"


class EjentumScaffoldTool(BaseTool):
    name: str = "ejentum_scaffold"
    description: str = (
        "Retrieve a reasoning scaffold from Ejentum's Logic API. "
        "Call this before making complex judgments. Returns suppression signals "
        "that block cognitive shortcuts and a reasoning topology to follow. "
        "Input: a 1-2 sentence description of your current reasoning challenge."
    )

    def _run(self, query: str) -> str:
        try:
            r = requests.post(
                EJENTUM_URL,
                headers={
                    "Authorization": f"Bearer {EJENTUM_KEY}",
                    "Content-Type": "application/json",
                },
                json={"query": query, "mode": "single"},
                timeout=5,
            )
            r.raise_for_status()
            return r.json()[0]["single_ability"]
        except Exception as e:
            return f"Scaffold unavailable: {e}. Proceed with native reasoning."


# Usage with CrewAI:
#
# from crewai import Agent, Task, Crew
#
# scaffold_tool = EjentumScaffoldTool()
#
# analyst = Agent(
#     role="Senior Production Analyst",
#     goal="Identify root cause of system failures with rigorous causal reasoning",
#     backstory="You are a production analyst. Before making judgments, use the ejentum_scaffold tool.",
#     tools=[scaffold_tool],
#     llm=your_llm,
# )
#
# task = Task(
#     description="Why did our deployment fail after the config change?",
#     agent=analyst,
# )
#
# crew = Crew(agents=[analyst], tasks=[task])
# result = crew.kickoff()
