/**
 * Ejentum Logic API -- Basic TypeScript Example
 *
 * Minimal example: send a task, get a cognitive injection, print it.
 */

const EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/";
const API_KEY = "YOUR_EJENTUM_API_KEY"; // Get yours at ejentum.com/dashboard

async function getInjection(query: string, mode: "reasoning" | "reasoning-multi" | "anti-deception" | "code" | "code-multi" | "memory" | "memory-multi" = "reasoning") {
  const response = await fetch(EJENTUM_URL, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query, mode }),
  });

  const data = await response.json();
  const key = mode  // response key matches mode name;
  return data[0][key];
}

// Usage
const injection = await getInjection(
  "Why did our conversion rate drop 40% after the checkout redesign?"
);

console.log(injection);
