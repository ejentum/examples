/**
 * Ejentum Logic API -- Vercel AI SDK Tool
 *
 * Defines Ejentum as a tool for agents built with the Vercel AI SDK.
 * Uses Zod for input validation. Works with any Vercel AI provider.
 */

import { tool } from "ai";
import { z } from "zod";

const EJENTUM_URL = "https://ejentum-main-ab125c3.zuplo.app/logicv1/";
const EJENTUM_KEY = "YOUR_EJENTUM_API_KEY";

export const ejentumScaffold = tool({
  description:
    "Retrieve a reasoning scaffold from Ejentum's Logic API. " +
    "Call this before making complex judgments. Returns suppression signals " +
    "that block cognitive shortcuts and a reasoning topology to follow.",
  parameters: z.object({
    query: z
      .string()
      .describe("Describe your current reasoning challenge in 1-2 sentences."),
    mode: z
      .enum(["single", "multi"])
      .default("single")
      .describe("single for Ki (1 ability), multi for Haki (4 abilities)."),
  }),
  execute: async ({ query, mode }) => {
    try {
      const response = await fetch(EJENTUM_URL, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${EJENTUM_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query, mode }),
        signal: AbortSignal.timeout(5000),
      });

      const data = await response.json();
      const key = mode === "single" ? "single_ability" : "multi_ability";
      return data[0][key];
    } catch (e) {
      return `Scaffold unavailable: ${e}. Proceed with native reasoning.`;
    }
  },
});

// Usage with Vercel AI SDK:
//
// import { generateText } from "ai";
// import { openai } from "@ai-sdk/openai";
//
// const result = await generateText({
//   model: openai("gpt-4o"),
//   tools: { ejentumScaffold },
//   system: "You are a senior analyst. Before complex judgments, call ejentumScaffold.",
//   prompt: "Why did our conversion rate drop 40% after the checkout redesign?",
// });
