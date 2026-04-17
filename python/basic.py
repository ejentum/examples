"""
Ejentum Logic API -- Basic Python Example

Minimal example: send a task, get a cognitive injection, print it.
"""

import requests

EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
API_KEY = "YOUR_EJENTUM_API_KEY"  # Get yours at ejentum.com/dashboard

response = requests.post(
    EJENTUM_URL,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "query": "Why did our conversion rate drop 40% after the checkout redesign?",
        "mode": "reasoning",  # or "code", "anti-deception", "memory", "reasoning-multi", etc.
    },
    timeout=5,
)

data = response.json()
injection = data[0]["reasoning"]  # response key matches mode name

print(injection)
