# Career Roadmap → Google Software Engineer

**Owner:** kedar · **Created:** 2026-07-26 · **Target:** offer at Google (or equivalent bar: Meta / Amazon / Microsoft / Stripe / Databricks)

---

## 0. How this roadmap is built

Six phases across **24 weeks (Mon 27 Jul 2026 → Sun 10 Jan 2027)**, assuming **~14 hrs/week** (2 hrs weekdays + 4 hrs weekend). Every phase ends with a **measurable exit gate** — you do not advance on calendar, you advance on the gate.

Stated assumptions (adjust and the plan still holds):

| Assumption | Value | If different |
|---|---|---|
| Target level | L4 (SWE II / mid) | L5 → double weight on [[04-hld]] + leadership stories in [[07-google-interview-playbook]] |
| Current DSA level | Easy solid, Medium in progress (per this repo) | Already at Medium-fluent → compress Phase 1 to 3 weeks |
| Weekly hours | 14 | 7 hrs/week → stretch to 40 weeks. 25 hrs/week → compress to 14 weeks |
| Primary language | Python | Fine for Google. Know your stdlib complexities cold ([[01-dsa]]) |

**The single most important structural fact:** Google loops are ~55% coding, ~20% design, ~25% behavioural/GCA — but *AI/ML and GenAI are what get you the interview* (resume differentiation) more than what get you the offer. So DSA gets the most hours; GenAI gets the most *visible artifacts*.

---

## 1. Topic map

| #   | Track                                   | File                             | Hours | Why it matters at Google                                                                                                         |
| --- | --------------------------------------- | -------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1   | DSA                                     | [[01-dsa]]                       | 180   | 2–4 rounds of your loop. Non-negotiable gate.                                                                                    |
| 2   | HTTP + Internet fundamentals            | [[02-http-and-internet]]         | 35    | Feeds design rounds; asked directly in phone screens                                                                             |
| 3   | LLD / OOD / concurrency                 | [[03-lld]]                       | 45    | "Design this class hierarchy", code-quality signal in coding rounds                                                              |
| 4   | HLD / distributed systems / queues / DB | [[04-hld]]                       | 70    | L5 gate; L4 differentiator. Google *wrote* these papers                                                                          |
| 4b  | **SQL**                                 | [[10-sql]]                       | 30    | Screens ask it directly (see [Adhoc/hackerrank_questions.md](../Adhoc/hackerrank_questions.md) Q3); underpins the DB half of HLD |
| 5   | AI/ML basics                            | [[05-ai-ml-basics]]              | 45    | ML-adjacent teams, ML systems design round                                                                                       |
| 6   | LLM / transformers / GenAI / LangChain  | [[06-llm-genai]]                 | 55    | Resume magnet; almost every 2026 team touches this                                                                               |
| 7   | Google interview playbook               | [[07-google-interview-playbook]] | 30    | Process, Googlyness, story bank, referrals, negotiation                                                                          |
| 8   | Supporting skills (my additions)        | [[08-supporting-skills]]         | 40    | OS, networking, Python mastery, git, Docker/K8s, writing                                                                         |
| —   | Tracker                                 | [[09-progress-tracker]]          | —     | Where you actually log the work                                                                                                  |

Total ≈ 530 hrs ≈ 24 weeks × ~22 hrs. That is above 14 hrs/week — so the plan below **prunes deliberately**: items marked `[stretch]` are cut first.

---

## 2. The 24-week plan

### Phase 1 · Foundations rebuild (W1–W4, 27 Jul → 23 Aug)
Goal: stop being an "Easy problems" solver. Build the daily machine.

| Week | DSA (8h) | Systems (3h) | AI (2h) | Meta (1h) |
|---|---|---|---|---|
| W1 (Jul 27–Aug 2) | Arrays, two pointers, prefix sums — 15 problems | [[02-http-and-internet]]: OSI, DNS, TCP, TLS, "type a URL" walkthrough | Python for data: numpy/pandas refresher | Set up [[09-progress-tracker]]; resume v0 |
| W2 (Aug 3–9) | Hashing, strings, sliding window — 15 problems | HTTP/1.1 → 2 → 3, methods, status codes, caching headers | Math floor: linear algebra + probability essentials | Fix repo structure; add complexity comments |
| W3 (Aug 10–16) | Binary search incl. *search on answer*, sorting — 15 problems | Cookies, sessions, JWT, OAuth2/OIDC, SOAP vs REST vs gRPC | Bias–variance, train/val/test, metrics | LinkedIn profile rewrite |
| W4 (Aug 17–23) | Linked lists, stacks, queues, monotonic stack — 15 problems | OWASP top 10, CORS, CSRF, XSS, SSRF | Linear + logistic regression from scratch | **Gate 1** review |

**Plus SQL, 2 hrs/week throughout W1–W10** ([[10-sql]] §11): W1–W2 joins/NULLs/aggregation, W3–W4 subqueries/CTEs. Set up the local `SQL/` folder + auction schema in W1 so every query gets actually executed.

**Gate 1:** 60 problems logged. Can whiteboard the full URL→render path including TLS handshake and cache decisions. Can explain JWT vs session with revocation tradeoffs, unprompted, in 3 minutes. Can write the [Adhoc/hackerrank_questions.md](../Adhoc/hackerrank_questions.md) Q3 auction query correctly from scratch.

### Phase 2 · Pattern mastery (W5–W10, 24 Aug → 4 Oct)
Goal: pattern recognition under time pressure.

| Week | DSA (9h) | Systems (3h) | AI (2h) |
|---|---|---|---|
| W5 (Aug 24–30) | Trees: traversals, BST, LCA, serialize — 15 | [[03-lld]]: OOP, SOLID, composition | Trees/ensembles: RF, GBM, XGBoost |
| W6 (Aug 31–Sep 6) | Heaps, top-K, intervals — 15 | Design patterns: strategy, factory, observer, decorator, builder | Clustering, PCA, kNN, naive Bayes |
| W7 (Sep 7–13) | Graphs I: BFS/DFS, grids, topo sort — 15 | Concurrency: threads, locks, deadlock, GIL, thread pools | Neural nets: MLP + backprop by hand |
| W8 (Sep 14–20) | Graphs II: union-find, Dijkstra, MST — 15 | LLD build #1: parking lot + LRU cache (real Python, tested) | Optimizers, regularization, batch/layer norm |
| W9 (Sep 21–27) | Recursion + backtracking — 15 | LLD build #2: rate limiter + elevator | CNNs, embeddings, RNN/LSTM |
| W10 (Sep 28–Oct 4) | Bit manipulation, math, randomized — 12 | LLD build #3: in-memory KV store with TTL | **Gate 2** review |

**Plus SQL, 2 hrs/week:** W5–W6 window functions (every function and frame), W7–W8 the 25 patterns in [[10-sql]] §7, W9–W10 recursive CTEs + `EXPLAIN`/indexing.

**Gate 2:** 150 problems total. Solve a random unseen Medium in ≤25 min, talking aloud, ≥70% of attempts. Three LLD builds committed with unit tests. SQL: any window-function Medium in ≤8 min, and every §7 pattern solved **both** with and without window functions.

### Phase 3 · Hard DSA + distributed systems (W11–W16, 5 Oct → 15 Nov)
Goal: the L4/L5 differentiators. **Start applying in W14.**

| Week | DSA (8h) | HLD (4h) | GenAI (2h) |
|---|---|---|---|
| W11 (Oct 5–11) | DP I: 1D, knapsack, LIS — 12 | Numbers to memorize, back-of-envelope, LB, CDN, caching | Tokenization, embeddings, attention math |
| W12 (Oct 12–18) | DP II: 2D, grids, strings, intervals — 12 | DB: SQL vs NoSQL, B+tree vs LSM, indexes, ACID, isolation | Full transformer block; encoder vs decoder |
| W13 (Oct 19–25) | DP III: tree DP, bitmask `[stretch]`, digit `[stretch]` — 10 | Replication, sharding, consistent hashing, CAP/PACELC, quorum | Pretraining → SFT → RLHF/DPO, LoRA, quantization |
| W14 (Oct 26–Nov 1) | Tries, string matching (KMP/rolling hash) — 10 | Queues: Kafka, delivery semantics, ordering, DLQ, outbox, saga | Inference: sampling, KV cache, batching, cost math |
| W15 (Nov 2–8) | Design problems: LRU, median stream, iterators — 10 | Consensus (Raft), coordination, leader election, Bloom filters | **RAG project build** (see [[06-llm-genai]]) |
| W16 (Nov 9–15) | Mixed hard set — 10 | Observability, SLO/error budget, canary, multi-region | Agents, tool calling, LangGraph, evals |

**Gate 3:** 200+ problems. Can drive a 45-min design round end-to-end on 5 canonical systems. One shipped RAG/agent project with a README and eval numbers. **Applications submitted + referral requested.**

### Phase 4 · Interview simulation (W17–W20, 16 Nov → 13 Dec)
Goal: convert knowledge → performance. This is where most strong engineers lose the offer.

- **3 mock interviews/week minimum** (1 coding, 1 design, 1 behavioural), rotating peers/Pramp/interviewing.io.
- All coding practice moves to a **plain text editor, no autocomplete, no run button** — Google's tool has no execution. Practice in a `.txt` file.
- Build the **12-story behavioural bank** ([[07-google-interview-playbook]]) — written, then spoken, then timed to 2.5 min.
- Weekly: 10 problems (timed, 2 in one 45-min sitting), 2 design deep-dives, 1 paper from the Google reading list.
- Re-solve every problem you failed twice (spaced-repetition queue in [[09-progress-tracker]]).

**Gate 4:** 12 mocks done with written feedback. Zero "I froze" incidents in the last 4. Stories all under 3 min with quantified impact.

### Phase 5 · Loop execution (W21–W24, 14 Dec → 10 Jan)
- Recruiter screen → phone screen → onsite (4–5 rounds) → hiring committee → team match.
- Maintenance mode only: 5 problems/week, 1 design/week, daily 20-min flashcard review. **Do not learn new topics during a live loop.**
- Post-round: write a debrief within 2 hrs while memory is fresh.
- Negotiation prep in W23 ([[07-google-interview-playbook]] §7).

### Phase 6 · Continuous (post-offer or reset)
If it lands: keep 3 problems/week + 1 design/month forever — the tax is small, the option value is huge.
If it doesn't: Google's cooldown is typically ~6–12 months. Use the debriefs to target the exact failed dimension, and interview elsewhere immediately — offers are the best practice and the best leverage.

---

## 3. Weekly cadence (the actual machine)

| Day     | Block     | Content                                                                               |
| ------- | --------- | ------------------------------------------------------------------------------------- |
| Mon–Fri | 45 min AM | 2 problems: 1 new, 1 spaced-repetition re-solve                                       |
| Mon–Fri | 60 min PM | Track of the week (systems / AI / LLD) — read, then **write notes in your own words** |
| Sat     | 3 hrs     | 1 timed 45-min mock-style coding sitting + 1 design problem written out               |
| Sun     | 2 hrs     | Review: update [[09-progress-tracker]], re-solve failures, plan next week             |

Rules that do the heavy lifting:
1. **20-minute rule.** Stuck 20 min on a new problem → read the solution, understand it fully, then re-implement from blank. Never grind 2 hrs.
2. **3-strike retirement.** A problem leaves the repetition queue after 3 clean independent solves.
3. **Always talk aloud.** Silent solving trains the wrong skill. The interview grades your narration.
4. **Write the complexity before you code.** Every solution file gets a `# Time: O(...) Space: O(...)` header with a one-line justification.
5. **One artifact per phase.** Something public: a repo, a blog post, a design doc. Interviews reward evidence over claims.

---

## 4. Definition of "ready"

You are Google-ready when all of these are true:

- [ ] 250+ problems solved, ≥60 of them Hard, with a written pattern index
- [ ] Random unseen Medium: working code + complexity + tests, ≤25 min, narrated
- [ ] Random unseen Hard: correct approach articulated within 10 min, ≥60% of attempts
- [ ] 45-min design round on any of the 25 systems in [[04-hld]], with 2 deep-dives and explicit tradeoffs
- [ ] Can answer any rapid-fire question in [[04-hld]] §9, [[02-http-and-internet]] §9 and [[10-sql]] §12 in under 60 seconds
- [ ] SQL: latest-row-per-group, gaps-and-islands, pivots and running totals written correctly first try, in two dialects' worth of awareness
- [ ] 12 STAR stories, quantified, each usable for 3+ different prompts
- [ ] 1 shipped GenAI project you can defend at implementation depth
- [ ] 15+ mock interviews with written feedback, trend improving

---

## 5. Resource shortlist (don't buy more than this)

| Track | Primary | Secondary |
|---|---|---|
| DSA — learning (W1–W10) | **Structy** (owned) — work the modules in order | *Algorithm Design Manual* (Skiena) ch. 1–8 |
| DSA — testing (W11–W20) | **LeetCode**, random mixed sets + Hard tier | *Elements of Programming Interviews (Python)*, Codeforces Div3 for speed |
| HTTP/web | MDN HTTP docs, `roadmap.sh/backend` | *High Performance Browser Networking* (free online) |
| LLD | refactoring.guru | *Head First Design Patterns*, *Clean Code* (skim) |
| HLD | *Designing Data-Intensive Applications* (Kleppmann) — the one book to actually finish | ByteByteGo, Google papers list in [[04-hld]] §8 |
| SQL | HackerRank SQL track → LeetCode Database 50 | Postgres window-function docs, *SQL Performance Explained*, use-the-index-luke.com |
| ML | *Hands-On ML* (Géron) ch. 1–11 | Andrew Ng ML Specialization; *Designing ML Systems* (Huyen) |
| LLM/GenAI | Karpathy "Zero to Hero" + `nanoGPT`, *The Illustrated Transformer* | Anthropic + OpenAI cookbooks, LangGraph docs |
| Behavioural | *Cracking the Coding Interview* ch. 1–6 (process only) | Google careers site, levels.fyi |

Rule: **one primary resource per track at a time.** Resource-hopping is the most common failure mode of self-study plans.

---

Next: open [[01-dsa]] and [[09-progress-tracker]], and block the W1 calendar slots today.
