"""
Ejentum Logic API -- Inject Scaffold Into Agent

Full flow: retrieve a reasoning scaffold and inject it into an LLM call.
The scaffold tells the model what patterns to follow and what failure modes to block.
"""

import requests
from openai import OpenAI  # or any LLM client

EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"

# Step 1: Get the reasoning scaffold
task = "A clinical trial shows treatment appears harmful in raw data but beneficial after adjusting for severity. Determine the true causal direction."

try:
    r = requests.post(
        EJENTUM_URL,
        headers={"Authorization": f"Bearer {EJENTUM_KEY}", "Content-Type": "application/json"},
        json={"query": task, "mode": "single"},
        timeout=5,
    )
    scaffold = r.json()[0]["single_ability"]
except Exception:
    scaffold = ""  # Graceful degradation: agent continues without scaffold

# Step 2: Inject scaffold BEFORE the task in the system message
system_message = f"""[REASONING CONTEXT]
{scaffold}
[END REASONING CONTEXT]

You are a senior analyst. Analyze the following task."""

# Step 3: Call your LLM with the scaffolded prompt
client = OpenAI()  # or Anthropic(), or any provider
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": task},
    ],
)

print(response.choices[0].message.content)
