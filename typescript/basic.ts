/**
 * Ejentum Logic API -- Basic TypeScript Example
 *
 * Minimal example: send a task, get a reasoning scaffold, print it.
 */

const EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/";
const API_KEY = "YOUR_EJENTUM_API_KEY"; // Get yours at ejentum.com/dashboard

async function getScaffold(query: string, mode: "single" | "multi" = "single") {
  const response = await fetch(EJENTUM_URL, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query, mode }),
  });

  const data = await response.json();
  const key = mode === "single" ? "single_ability" : "multi_ability";
  return data[0][key];
}

// Usage
const scaffold = await getScaffold(
  "Why did our conversion rate drop 40% after the checkout redesign?"
);

console.log(scaffold);
