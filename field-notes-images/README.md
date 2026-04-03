# How the Builder Uses It on an Agentic IDE
### 28 Moments from Inside the IDE

*by Frank Brsrk, Ejentum founder, solo developer, the only user who's been running this product every day since it existed.*

---

I built the Logic API because I needed it. Not as a product idea, but as a tool I couldn't stop reaching for. Every screenshot in this guide is from a real work session. Not staged. Not cleaned up. Not *"here's what the demo looks like."* This is what it looks like when the person who built the reasoning engine uses it to build everything else.

What you're about to see is 28 moments across weeks of work: backend infrastructure, benchmark design, website copy, security auditing, blog writing, ability dataset purification, and research. Different tasks. Different days. **Same tool.**

I use Claude Code as my IDE. The Logic API is configured as a skill file: one Markdown file dropped into the project. Claude calls it automatically when it needs reasoning structure, or I tell it to. One curl call, one JSON response, injected *before* the agent reasons. That's the entire integration.

Here's what that looks like in practice.

---

## Part 1: The First Call

### "Retrieve an ability before you start."

**[ejentum_prompts]**

This is where every session starts. I'm about to plan the backend infrastructure: Stripe webhooks, Supabase auth, Zuplo gateway, n8n orchestration. Four services that need to talk to each other without dropping data or creating race conditions.

Before Claude writes a single line of code, I tell it to retrieve a *multi* ability. The API returns a 4-ability synergy chain with compound suppression vectors. Claude absorbs them and outputs its [REASONING CONTEXT]: *suppress ad_hoc_solutions, suppress implicit_compatibility_assumption, verify data shape at every handoff point.*

The suppress signals are where the value lives. *"Don't optimize for happy path only. Failed payments, expired cards, webhook retries must all be handled."* That's not something I wrote in a system prompt. That's what the scaffold injected, and it's specific to exactly the kind of architectural work I'm about to do.

Claude hasn't written any code yet. **It's loading its cognitive operating system for this task.**

---

### "I have the document and the reasoning ability. Let me inject the context and then explore."

**[ejentum2]**

Now I'm analyzing the n8n workflow. I ask for a single Ki ability. The API returns an ability with trigger `AGENT_HANDOFF_LINEARIZATION`. It detected from "n8n workflow analysis" that the risk was data shape inconsistency between pipeline nodes.

This is the part that surprises people: I didn't tell the API about n8n specifically. I said *"workflow analysis."* The API routed to handoff validation because that's the structural failure mode of *any* multi-step pipeline. The ability doesn't know about n8n. **It knows about handoffs.**

Claude says *"Let me inject the reasoning context and then explore the codebase."* The ability gets loaded BEFORE the exploration, not after. That order matters. The scaffold shapes what the agent looks *for*, not just what it does with what it finds.

---

### "The ability isn't a perfect match, but the core principle is potent."

**[ejentum3]**

This is the screenshot I show people who ask about the 62% wrong-domain finding.

I asked for an ability to help with naming inconsistency resolution. The API returned an ability about *failure mode classification*. Wrong domain. But Claude read the scaffold and said: *"Not a perfect match for naming inconsistency, but the core principle is potent: don't apply a generic one-size-fits-all response. Instead: enumerate, classify, and match specifically."*

The agent *transferred* the principle. The suppression signal (don't apply generic solutions without first classifying the actual situation) is domain-agnostic. It works for failure mode classification. It works for naming conventions. It works for debugging, content planning, security analysis.

**This is the asymmetry in action.** The suppression signal is more important than the domain match. A wrong-domain ability with the right suppression *still improves reasoning.*

---

## Part 2: Going Deeper

### "Got a 4-ability synergy chain. Injecting now."

**[ejentum5]**

I'm reorganizing the entire documentation directory. This is **Haki mode**: 4 abilities merged. The compound amplification is intense: *semantic_hashing, dense_abstraction, credence_distribution_tracking, context_drift_detection, frame_transition_management.*

But the suppress signals are what make it work: *verbose_retention* (don't keep everything just because it exists), *premature_certainty_crystallization* (don't commit to an organizational scheme before you've seen all the content), *uncontrolled_context_bleed* (don't let one document's context contaminate your judgment of the next).

People ask: *"4 abilities for organizing docs, isn't that overkill?"* It's not. Document reorganization is a multi-dimensional judgment task. You need to compress (Ki-1), track what's credible vs aspirational (Ki-2), detect when your organizational frame is drifting (Ki-3), and prevent premature commitment to a structure (Ki-4). Each ability covers a different failure mode. **Single Ki handles single-failure tasks. Haki handles compound ones.**

This session is actually where I first noticed the Cognitive Scaffolding Thesis: the agent referenced the abilities *50+ tool calls later* without being re-prompted. The scaffold persisted.

---

## Part 3: The Product Examining Itself

### "The API routed here twice, which means this is the dominant cognitive need."

**[ejentum6]** → **[ejentum7]**

This is a before/after pair. I'm doing a deep self-exploration of Ejentum's identity, not marketing copy, but understanding what the project actually *is* and what it *proved*.

I retrieved 3 single abilities one by one. Ability 1: *Recursive Self-Model.* Ability 2: *Meta Memory Management.* Ability 3: *Recursive Self-Model* (again).

The API returned the same ability *twice* out of three calls. Claude noticed this and interpreted it: *"The API routed here twice, which means this is the dominant cognitive need. The codebase reorganization IS fundamentally about self-image calibration."*

The agent reasoned about *why* the API gave it specific abilities. That's meta-cognition about meta-cognition. I didn't ask for that interpretation. The scaffold created the conditions for the agent to observe its own retrieval patterns.

In ejentum7, you can see the execution: *"Now let me read deeply across the codebase to understand Ejentum's actual identity, not what it says it is, but what it proved."* The Recursive Self-Model suppression (*naive_self, single_configuration_fixation*) prevented the agent from accepting the marketing narrative. **It forced evidence-based self-assessment.**

Why did I switch from Haki to 3 separate Ki calls? Because single mode returns the full reasoning topology: the complete DAG with all gates and loops. Multi mode returns a merged, condensed version. When I need the full execution structure for each ability, I call single three times.

---

## Part 4: Writing with Discipline

### "Let me absorb the four subfunctions."

**[ejentum8]**

I'm writing the first blog post about benchmark results. The Haki returns 4 abilities with specific roles:
- **PRIMARY:** *Narrative Synthesizer* (turn numbers into story)
- **DEPENDENCY:** *Assumption Interrogator* (challenge every premise before using it)
- **AMPLIFIER:** *Bias Detector* (catch the writer's own bias toward positive framing)
- **ALTERNATIVE:** *Evidence Arbitrator* (when two claims conflict, resolve by evidence weight, not narrative convenience)

The DEPENDENCY and PRIMARY are in *deliberate tension*. The narrative voice wants to tell a compelling story. The interrogator wants to break every assumption in that story. That tension is the point: it produces writing that survives scrutiny because it was scrutinized during generation.

---

### "Execute. Retrieve a single ability to keep u focused."

**[ejentum9]**

After the Haki scaffold for planning, I switch to Ki for actual execution. One focused ability: *suppress burying_the_key_message_under_unexplained_technical_terms, suppress delivering_all_information_in_one_undifferentiated_block.*

The directive: **"Lead with finding. Layer: summary → narrative → data."**

Then Claude does something I didn't ask for: it launches sub-agents to verify every number against the source benchmark files *before writing*. The ability told it to lead with findings. The agent interpreted "lead with findings" as *"I'd better make sure my findings are correct before I lead with them."*

This is the Ki vs Haki pattern in practice. Haki for planning: load 4 perspectives, create tension, explore the problem space. Ki for execution: one sharp directive, stay focused, verify before you publish. **More abilities doesn't mean better. It means different.**

---

### "Am I presenting the correctness flat result as 'not a problem' because I want the product to look good?"

**[ejentum10]**

*This is my favorite screenshot.*

Claude is writing about the EjBench results and the Haki scaffold forces it to confront its own bias. The DEPENDENCY ability literally asks: *"Check my own biases: am I presenting the correctness flat result as 'not a problem' because I want the product to look good? Am I anchoring on the positive quality numbers?"*

The agent is questioning whether it's being genuinely analytical or *performing* analysis. The AMPLIFIER adds: *"Don't lock onto 'quality improved = success.' The correctness regression is real data. Give it proportional weight."*

I'm the founder. I want the product to look good. The scaffold prevents my agent from unconsciously serving that desire. The Bias Detection ability doesn't know it's writing about its own system. It applies the same adversarial self-check regardless.

**The blog post that came out of this session includes the correctness dip front and center, not buried in a footnote.** That's the scaffold working.

---

## Part 5: Content as Precision

### "KI 1: detect the traces the homepage planted. KI 2: lead with the most powerful sentence. KI 3: anchor in a named, specific act."

**[ejentum13]** → **[ejentum14]**

A before/after pair. This is website copy refinement, and the clearest example of cross-domain ability transfer in the entire guide.

In ejentum13, I retrieve 3 Ki abilities, one for each editorial lens:
- **KI 1** *(Stagnancy Trace Detection):* *"The homepage already modified the visitor's mental model. The About page inherits that context. Don't repeat what the homepage planted; detect the traces and build on them."*
- **KI 2** *(Vision Inversion):* *"Lead with the most powerful sentence. The audience's core question is 'will this matter?' Answer it in the opening of the vision section, not the closing."*
- **KI 3** *(Landmark Navigation):* *"The founder section needs a temporal landmark that projects forward. Not a vague promise, but a named, specific act of ongoing work."*

The output: **"Refinement Strategy: 4 Edits."** Surgical. Each edit has entry/exit criteria.

In ejentum14, I'm executing those edits. The Ki returns a *compression* ability: *"Each edit is a macro gesture. Compress to entry state → exit state → net causal effect. Don't flood with micro-changes."* A compression ability for editorial precision. The scaffold treats website copy the same way it treats a 47,000-line server log: compress to causal essence, preserve what matters, discard noise.

> Edit 1: "Tighten header. Entry: 2 sentences. Exit: 1 sentence."

That's the product operating outside its "intended" domain. A compression ability designed for log analysis, applied to website copywriting, and it works. **because compression is a cognitive operation, not a domain skill.**

---

## Part 6: The Benchmark Sessions

### "Design metrics that track trajectories across the game, not just endpoints."

**[ejentum16]**

I'm building the ARC-AGI-3 evaluation framework. The Ki returns an ability with a specific directive: *track trajectories, not snapshots.* "Each metric should capture a trend, not a point measurement."

This ability directly shaped the methodology that produced our most important finding. Because the scaffold told the agent to design trajectory metrics, the agent built measurements for scaffold persistence over time, which is how we discovered the **24-step half-life**. The ability to track reasoning as a time series came from a reasoning ability about longitudinal monitoring.

The scaffold shaped the methodology. The methodology produced the evidence. **The evidence validated the scaffold.**

---

### "Those are the two claims that make RA²R unique and we're not measuring either of them."

**[ejentum17]**

*This is where the Cognitive Scaffolding Thesis was born.*

I'm in a live discussion with Claude about what to measure. Claude identifies the gap: *"Reasoning consistency: does the model maintain coherent reasoning across steps? Scaffolding compounding: does the scaffold's influence persist into steps 2, 3, 4? Neither is captured by RHAE or the interactive metrics."*

Then I retrieve a Ki for trace analysis design. The scaffold: *suppress treating_each_checkpoint_as_first_encounter.* Amplify: *longitudinal_tracing, trend_surfacing.* "Track reasoning as a time series, detect deviations, measure whether each step builds on or forgets prior steps."

This is recursive in a way that still surprises me. The scaffold's suppression signal (*"don't treat each checkpoint as a first encounter"*) is literally the decay pattern we're trying to study. The ability is preventing the failure mode that the benchmark is designed to measure. The product is validating itself by being used to design the test that validates it.

Is that circular? I've thought about it a lot. The answer is no, because the benchmark then runs on *raw model output*, not scaffolded output. The scaffold designs the methodology. The methodology measures unscaffolded vs scaffolded behavior. **The scaffold doesn't grade itself.**

---

## Part 7: Purifying the Dataset

### "Kill the mechanical template ending in all 311 mechanisms."

**[ejentum18]**

*The product improving the product.*

I'm using 3 Ki abilities to audit and clean the 311 ability dataset itself:
- **Ki 1** *(Template Elimination):* *"Measure the marginal value of each 'At each decision gate' repetition. It's zero after the 3rd ability. Terminates the pattern."*
- **Ki 2** *(Visual Hierarchy):* *"Compress the dense mechanism paragraph into semantic clusters. Don't flood with equal-weight operations."*
- **Ki 3** *(Failure Mode Quality):* *"Classify each failure hook as vivid or flat. Apply mode-specific fix: per type, not a generic rewrite."*

Below: **PRIORITY 1**. *"Kill the mechanical template ending in all 311 mechanisms."* This is the v3.6 Cognitive OS Purification where 96 abilities got rewritten. **31% of the entire dataset.**

Same circularity question from Part 6 applies, same answer. The Ki gives me a framework for cleaning. The benchmark tells me whether the cleaning worked. If the rewritten version scores lower, it gets reverted.

---

## Part 8: The Deep Exploration

### "I have both Ki and Haki abilities. Let me inject them into my reasoning before proceeding."

**[ejentum19]**

This is maximum cognitive load with maximum scaffolding. **Both Ki and Haki active simultaneously**. 5 abilities total.

The Ki is for cross-domain structural analysis: amplify *distal_analogies, structural_isomorphisms, cross_domain_bridges.* Suppress: *functional_fixedness, domain_lock.* The Haki is for fractal depth audit: suppress *"Don't assume patterns hold across scales without verification."*

Then Claude maps out a comprehensive multi-axis exploration across the website, use cases, product structure, pricing, and content layers. It spins up parallel exploration agents to systematically work through each axis.

Can you stack Ki and Haki? Yes. Does it always help? No. This was a genuine "explore everything" task: multi-dimensional, multi-scale, multi-domain. That's when stacking works. For a focused task like *"write this paragraph"* or *"fix this bug,"* single Ki is better. **Know when each applies.**

---

### "Every claim must trace to measured data. No conclusions beyond what the steps support."

**[ejentum20]**

I'm grounding the 15 use case documents in actual benchmark evidence. The Ki suppresses *post_hoc_rationalization* and *performative_reasoning*.

The difference between those two: post_hoc_rationalization is finding evidence to support a conclusion you've already reached. Performative reasoning is going through the *motions* of rigor without actually being rigorous: citing numbers without checking them, listing limitations without weighing them.

This Ki forces the agent to trace every claim to measured data and **stop writing when the evidence runs out.** For 4 of the 11 remaining use cases, the agent found no supporting benchmark evidence. Those 4 got flagged as *"claimed but unmeasured"* instead of receiving fabricated support.

Most marketing teams make claims first and find evidence later. This is the reverse: evidence first, claims only where evidence supports them. That's not the ability's influence. That's my philosophy. **The ability enforces it.**

The same tool that enforces evidence discipline for content creation can flip to adversarial mode in one call. The scaffold doesn't have a personality. **it has a posture**, and the posture changes with the task.

---

## Part 9: Systems Thinking

### "Ejentum is a system of interacting components. Map the loops, not just the parts."

**[ejentum29]** → **[ejentum30]**

Before the security arc, one more pattern. Ejentum29 shows 3 Ki abilities being loaded: *Abstraction Ladder Navigator* (traverse concrete→category→principle→meta-principle), *Longitudinal Progress Monitor* (build on what's in memory, not rediscover it), *Systems Dynamics Mapper* (map reinforcing loops and balancing loops, not just parts).

ejentum30 shows the same 3 abilities compiled into a formal merged topology: the actual **CHAIN OF THOUGHT** under compound suppression. You can see the DAG notation: S-nodes for steps, N{} gates for failure mode suppression, compound suppression combining all three abilities' constraints.

This is what a reasoning topology looks like when it's been merged from multiple abilities. It's not a list of instructions. **It's an executable graph.** The agent traverses it, step by step, gate by gate, loop by loop, while reasoning about whatever task I gave it.

The agent used this merged topology to map Ejentum as a system of feedback loops: *dataset quality → retrieval quality → user outcomes → user feedback → dataset improvement.* Not a product. **A system.** The scaffold gave it the cognitive tools to see the loops.

That systems view leads directly to what came next: the most intense use of the product in this entire guide.

---

## Part 10: The Security Ritual

### "Can u scan for more security issues still, build a test suite!"

**[ejentum21]**

The pivot from content work to security auditing happens in one message. The Ki flips the agent's posture instantly: amplify *adversarial_perspective, threat_vector_enumeration, plan_fragility_exposure.* Suppress: *cooperative_world_assumption, optimistic_scenario_lock.*

That suppress signal, *cooperative_world_assumption*, is the single most important thing in a security context. Every standard code review assumes the code is trying to work. Security review assumes someone is trying to break it. The ability doesn't add security knowledge. **It removes the assumption of cooperation.**

Claude saves my manual action items to memory and starts *"Puttering..."*, launching deep scans. The switch from "writing helpful blog posts" to "hunting vulnerabilities" took **one API call.**

---

### "Classify each claim as KNOWN, KNOWABLE, or UNKNOWABLE."

**[ejentum22]** → **[ejentum23]**

Before/after pair. ejentum22 is preparation for going public: three Ki abilities for redaction (strip secrets), structure (strongest version of evidence), and credibility (classify certainty levels). The **KNOWN / KNOWABLE / UNKNOWABLE** framework forced the agent to audit its own epistemic state. Claims backed by benchmark data: *KNOWN.* Claims that could be tested but haven't been: *KNOWABLE.* Claims about mechanism that may be unfalsifiable at current capability: *UNKNOWABLE.*

ejentum23 is the security deep dive that followed. Same 3-Ki pattern, completely different task. Now the abilities are: *Perceptual Spatial* ("Map each agent's information position: attacker, Supabase, Stripe, Zuplo, n8n each see different slices"), *Adversarial Simulation* ("The vulnerability I ranked lowest because I already know the fix is the one a real adversary exploits first"), and a compound suppression: *cooperative_world_assumption, optimistic_scenario_lock, granting_agents_knowledge_they_cannot_access, analyst_omniscience.*

*"Analyst omniscience"*: the assumption that because you built it, you can see all the attack paths. You can't. The agent can't either, unless the scaffold explicitly blocks that assumption.

> "Hunt second-order bugs CREATED by the 27 fixes."

That's the scaffold looking for regressions from the security audit itself. The fixes introduce new code. New code has new bugs. **The agent is hunting bugs created by its own previous work.**

---

### "5th round. We proceed with the ritual. Think in set theory, state machines, cryptography, and game theory. Get Haki."

**[ejentum24]**

*This is the peak.*

I pushed the agent to round 5 of the security audit and requested Haki. What came back is the most sophisticated scaffold in the entire collection. Four mental paradigm shifts:

**Think in SET THEORY:** *Security_Controls ⊂ All_Attacks.* What's in the complement? Every control you implemented is a subset of all possible attacks. The scaffold asks: what's in the set of attacks you *didn't* control for?

**Think in STATE MACHINES:** Map every valid transition. Find the *unreachable-but-reachable* states. States the architecture says are impossible but that a carefully crafted request sequence can reach anyway.

**Think in CRYPTOGRAPHY:** Entropy, collision, nonce reuse. Not just "is the crypto right" but *"where are the entropy assumptions violated."*

**Think in GAME THEORY:** Cheapest attack vs most expensive defense. The attacker optimizes for cost. The scaffold forces the agent to think *economically* about vulnerability: which attack gives the best return for the least effort?

The agent didn't just check a list. It analyzed the codebase through four fundamentally different mathematical lenses, each finding different classes of vulnerabilities. Set theory finds coverage gaps. State machines find impossible paths. Cryptography finds implementation flaws. **Game theory finds economic incentives.**

---

### "For each invariant → GUARD → HALT on violation."

**[ejentum25]**

The agent started generating *its own* reasoning topologies: formal security invariants with mathematical predicates and halt conditions:
- **B-1:** *Invariant Vigilance* (auth assertions at every step)
- **B-2:** *Lifecycle Expiry Monitoring* (timestamp comparisons against decay thresholds)
- **B-3:** *Context Immunity* (quarantine anomalous inputs regardless of source trust)

Then it composed all three into a **SUPERMULTI** topology: a compound structure where each invariant feeds the next. The agent is creating ability-like structures on the fly, using the patterns it learned from the injected scaffolds.

---

### "Multi-stage attack chains. Credential stuffing → API."

**[ejentum26]**

The agent generated 4 attack scenarios against our stack. It loaded them as a supermulti topology and identified one dead node. KI-2: *"Infrastructure probing via Netlify calls. Can never be our case."* The scaffold didn't just generate attacks. **It filtered impossible ones.** Honest threat modeling includes knowing which threats *don't* apply to your architecture.

The three live attacks: credential stuffing → API endpoint exploitation, DoS amplification through undefined action paths, and business logic exploitation through webhook settlement flows.

---

### "Individual abilities find individual bugs. Composed topologies find emergent vulnerabilities at the intersection."

**[ejentum27]**

Round 16 complete. The Supermulti Attack Simulation found what individual rounds couldn't: an SSRF where a crafted consumer name could manipulate the Supabase REST API query through the service_role key. This vulnerability existed at the **intersection** of the login flow and the Supabase service role; it wasn't in either component individually. It only appeared when the compound topology traced the data flow across both.

That's the thesis of composition. Individual abilities find individual bugs. **Composed topologies find vulnerabilities that emerge from the interaction between components**: the kind standard testing misses because it tests components in isolation.

---

### "17 Rounds. 101 Fixes. 107 Tests."

**[ejentum28]**

*The scoreboard.*

**17 rounds** of Ki and Haki-guided security auditing. **101 fixes.** **107 tests.** Security fixes: 68. Performance fixes: 8. Code quality fixes: 11. Infrastructure fixes: 8. Frontend fixes: 6.

The headline finding: the longitudinal Ki caught an orphan cleanup bug in the regenerate endpoint: the *exact same bug pattern* fixed in round 12 for POST /api-keys, but the fix was never propagated to the regenerate path. A fix-propagation failure. The classic *"when a bug exists in two code paths and only one gets fixed."*

Standard testing doesn't catch this because it doesn't have cross-round memory. Each test run starts fresh. The longitudinal Ki maintained context across 17 rounds: it remembered what was fixed in round 12 and checked whether the fix propagated.

**That's the scaffold persistence thesis in practice.** The ability's influence survived across 17 rounds of complex, multi-dimensional work. It didn't forget. It didn't drift. It didn't let me ship a bug I'd already fixed once.

> One API. One injection. 101 fixes later, the scaffold was still working.

---

## What This Shows

28 screenshots. Weeks of real work. The same tool applied to backend infrastructure, workflow analysis, documentation reorganization, identity exploration, blog writing, website refinement, benchmark design, dataset purification, systems mapping, and a 17-round security audit that produced 101 fixes.

**One API endpoint. One curl call. One injection before the agent reasons.**

The patterns that emerged:

**Ki for execution, Haki for planning.** When the task has one failure mode, single Ki gives you one sharp scaffold. When the task spans multiple dimensions, Haki gives you 4 perspectives in compound suppression. I switch between them constantly, sometimes within the same session.

**The suppression signals matter more than the domain match.** An ability about failure mode classification worked for naming conventions. A compression ability worked for editorial precision. Suppression is domain-agnostic because it targets universal reasoning shortcuts, not domain-specific knowledge.

**The scaffold persists.** 50+ tool calls later, 17 security rounds later, the agent still references abilities injected at the start. Half-life of 24 steps, measured on ARC-AGI-3. The scaffold doesn't fire once and disappear. **It becomes a persistent attention anchor in the agent's context.**

**The product improves the product.** I use Ki abilities to purify Ki abilities. I use the scaffold to design the benchmark that validates the scaffold. I use the Haki to write honestly about the Haki results, *including the regressions.* The dogfooding is recursive and genuine.

**You don't need a playground.** You have your IDE. Drop the skill file. The first call takes 5 seconds. The first *"that's different"* moment takes one task.

---

*I built this because I needed it. 28 moments later, I still need it. Every day.*

---

## Get Started

1. Get an API key at [ejentum.com](https://ejentum.com). 100 free calls, no card required.
2. Drop the [skill file](https://ejentum.com/docs/skill) into your agentic IDE project.
3. Tell your agent to retrieve an ability before it reasons.

**That's the entire integration. One file. One call. One injection.**

*ejentum.com*
