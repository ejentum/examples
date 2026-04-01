"""
Ejentum Logic API -- Graceful Degradation Pattern

Production pattern: call the Logic API with timeout and fallback.
If the API is unreachable, the agent continues on native reasoning.
Ejentum is an enhancement layer, not a critical-path dependency.
"""

import time
import requests


EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/"
EJENTUM_KEY = "YOUR_EJENTUM_API_KEY"
TIMEOUT_SECONDS = 3
MAX_RETRIES = 1


def get_scaffold(query: str, mode: str = "single") -> str | None:
    """Retrieve scaffold with timeout and retry. Returns None on failure."""

    for attempt in range(MAX_RETRIES + 1):
        try:
            r = requests.post(
                EJENTUM_URL,
                headers={
                    "Authorization": f"Bearer {EJENTUM_KEY}",
                    "Content-Type": "application/json",
                },
                json={"query": query, "mode": mode},
                timeout=TIMEOUT_SECONDS,
            )
            r.raise_for_status()
            key = "single_ability" if mode == "single" else "multi_ability"
            scaffold = r.json()[0][key]

            if scaffold and len(scaffold) > 50:
                return scaffold

            return None  # Empty or malformed response

        except requests.Timeout:
            if attempt < MAX_RETRIES:
                time.sleep(0.5)
                continue
            return None

        except requests.RequestException:
            return None


def build_system_prompt(base_prompt: str, task: str, mode: str = "single") -> str:
    """Build system prompt with optional scaffold injection."""

    scaffold = get_scaffold(task, mode)

    if scaffold:
        return f"[REASONING CONTEXT]\n{scaffold}\n[END REASONING CONTEXT]\n\n{base_prompt}"

    # Graceful degradation: no scaffold, no change
    return base_prompt


# Usage:
#
# base = "You are a senior analyst."
# task = "Why did our deployment fail after the config change?"
#
# system_prompt = build_system_prompt(base, task)
#
# # system_prompt now contains the scaffold if available,
# # or just the base prompt if the API was unreachable.
# # Your agent works either way.
