# 09 · Progress tracker

← [[README]] · Update every Sunday. This file is the only one that proves the roadmap is real.

---

## Dashboard (update weekly)

| Metric | Target | Current | Updated |
|---|---|---|---|
| Problems solved (total) | 250 | 0 | — |
| — of which Hard | 60 | 0 | — |
| Patterns fully covered (of 26) | 26 | 0 | — |
| Design problems written up | 25 | 0 | — |
| SQL patterns templated (of 25) | 25 | 0 | — |
| SQL problems solved | 100 | 0 | — |
| LLD builds committed | 6 | 0 | — |
| Papers read (Google list) | 10 | 0 | — |
| Mocks completed | 15 | 0 | — |
| GenAI projects shipped | 1 | 0 | — |
| Failure-log items open | 0 | 0 | — |

---

## Phase gates

- [ ] **Gate 1 (W4, ~23 Aug 2026)** — 60 problems; URL→render walkthrough from memory; JWT vs session tradeoffs in 3 min; auction SQL query from scratch
- [ ] **Gate 2 (W10, ~4 Oct 2026)** — 150 problems; unseen Medium ≤25 min at 70%; 3 LLD builds with tests; every SQL pattern solved with *and* without window functions
- [ ] **Gate 3 (W16, ~15 Nov 2026)** — 200+ problems; 5 design problems end-to-end; RAG project shipped; applications sent
- [ ] **Gate 4 (W20, ~13 Dec 2026)** — 12 mocks with feedback; 250 problems; story bank timed; no-autocomplete practice standard
- [ ] **Gate 5 (W24, ~10 Jan 2027)** — loop in progress or complete

---

## Weekly log

Copy this block each week.

```
### W__ (dates)
Hours planned / actual:   14 / __
Problems: __ new, __ re-solved   (running total: __)
Track studied:
Wins:
Failures (→ failure log):
Mock(s):
Next week's one priority:
```

| Week | Dates | Problems | Hours | Gate progress | Notes |
|---|---|---|---|---|---|
| W1 | Jul 27–Aug 2 | | | | |
| W2 | Aug 3–9 | | | | |
| W3 | Aug 10–16 | | | | |
| W4 | Aug 17–23 | | | Gate 1 | |
| W5 | Aug 24–30 | | | | |
| W6 | Aug 31–Sep 6 | | | | |
| W7 | Sep 7–13 | | | | |
| W8 | Sep 14–20 | | | | |
| W9 | Sep 21–27 | | | | |
| W10 | Sep 28–Oct 4 | | | Gate 2 | |
| W11 | Oct 5–11 | | | | |
| W12 | Oct 12–18 | | | | |
| W13 | Oct 19–25 | | | | |
| W14 | Oct 26–Nov 1 | | | apply | |
| W15 | Nov 2–8 | | | | |
| W16 | Nov 9–15 | | | Gate 3 | |
| W17 | Nov 16–22 | | | | |
| W18 | Nov 23–29 | | | | |
| W19 | Nov 30–Dec 6 | | | | |
| W20 | Dec 7–13 | | | Gate 4 | |
| W21 | Dec 14–20 | | | | |
| W22 | Dec 21–27 | | | | |
| W23 | Dec 28–Jan 3 | | | | |
| W24 | Jan 4–10 | | | Gate 5 | |

---

## Problem log

Log every problem. `Result`: ✅ solved independently · 🟡 solved with a hint · ❌ read the solution.

| Date | Problem | Pattern | Diff | Time | Result | Mistake / insight | Next review |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Spaced repetition:** every 🟡 or ❌ gets scheduled at +1 day, then +7, then +30. Three consecutive ✅ from a blank editor retires it.

---

## Failure log (the highest-value table here)

Every bug you actually made, in one line. Read this list before every mock. Patterns will repeat — those repeats are your real weaknesses.

| Date | Problem | What went wrong | Category (off-by-one / wrong DS / missed edge case / complexity / syntax / panic) | Fixed? |
|---|---|---|---|---|
| | | | | |

---

## Pattern coverage

| # | Pattern | Problems done | Can derive from scratch? | Last reviewed |
|---|---|---|---|---|
| 1 | Two pointers | | ☐ | |
| 2 | Sliding window | | ☐ | |
| 3 | Prefix sum / diff array | | ☐ | |
| 4 | Hashing | | ☐ | |
| 5 | Binary search (array) | | ☐ | |
| 6 | Binary search on answer | | ☐ | |
| 7 | Sorting + greedy / intervals | | ☐ | |
| 8 | Linked list | | ☐ | |
| 9 | Stack / monotonic stack | | ☐ | |
| 10 | Heap / top-K / two heaps | | ☐ | |
| 11 | Trees | | ☐ | |
| 12 | Trie | | ☐ | |
| 13 | Graph BFS/DFS/grid | | ☐ | |
| 14 | Topological sort | | ☐ | |
| 15 | Union-Find | | ☐ | |
| 16 | Shortest path | | ☐ | |
| 17 | Backtracking | | ☐ | |
| 18 | DP 1D | | ☐ | |
| 19 | DP 2D / strings | | ☐ | |
| 20 | DP intervals/tree/bitmask | | ☐ | |
| 21 | Bit manipulation | | ☐ | |
| 22 | Math / number theory | | ☐ | |
| 23 | Design data structures | | ☐ | |
| 24 | String matching | | ☐ | |
| 25 | Segment tree / BIT | | ☐ | |
| 26 | Randomized / sampling | | ☐ | |

---

## Design problem log ([[04-hld]] §4)

| # | System | Written up | Deep dives covered | Rehearsed aloud | Weakest area |
|---|---|---|---|---|---|
| 1 | URL shortener | ☐ | | ☐ | |
| 2 | Pastebin / file share | ☐ | | ☐ | |
| 3 | Distributed rate limiter | ☐ | | ☐ | |
| 4 | Web crawler | ☐ | | ☐ | |
| 5 | Key-value store | ☐ | | ☐ | |
| 6 | Twitter timeline | ☐ | | ☐ | |
| 7 | Instagram | ☐ | | ☐ | |
| 8 | Chat / WhatsApp | ☐ | | ☐ | |
| 9 | Notification system | ☐ | | ☐ | |
| 10 | Feed ranking | ☐ | | ☐ | |
| 11 | YouTube / Netflix | ☐ | | ☐ | |
| 12 | Drive / Dropbox | ☐ | | ☐ | |
| 13 | Uber | ☐ | | ☐ | |
| 14 | Ticket booking | ☐ | | ☐ | |
| 15 | Payment system | ☐ | | ☐ | |
| 16 | Google Search | ☐ | | ☐ | |
| 17 | Google Docs | ☐ | | ☐ | |
| 18 | Google Maps | ☐ | | ☐ | |
| 19 | Job scheduler | ☐ | | ☐ | |
| 20 | Distributed cache | ☐ | | ☐ | |
| 21 | Metrics system | ☐ | | ☐ | |
| 22 | Log pipeline | ☐ | | ☐ | |
| 23 | Ad click aggregation | ☐ | | ☐ | |
| 24 | Autocomplete | ☐ | | ☐ | |
| 25 | Authorization (Zanzibar) | ☐ | | ☐ | |
| 26 | Enterprise RAG platform | ☐ | | ☐ | |
| 27 | ML: recommendations | ☐ | | ☐ | |

---

## SQL pattern coverage ([[10-sql]] §7)

| # | Pattern | Template written | Solved w/ window fn | Solved w/o window fn | Problems done |
|---|---|---|---|---|---|
| 1 | Latest row per group | ☐ | ☐ | ☐ | |
| 2 | Top-N per group | ☐ | ☐ | ☐ | |
| 3 | Nth highest value | ☐ | ☐ | ☐ | |
| 4 | Aggregate + keep detail | ☐ | ☐ | ☐ | |
| 5 | Aggregate without fan-out | ☐ | ☐ | ☐ | |
| 6 | Running total | ☐ | ☐ | ☐ | |
| 7 | Moving average | ☐ | ☐ | ☐ | |
| 8 | Period-over-period (LAG) | ☐ | ☐ | ☐ | |
| 9 | Find / delete duplicates | ☐ | ☐ | ☐ | |
| 10 | Gaps and islands | ☐ | ☐ | ☐ | |
| 11 | Sessionization | ☐ | ☐ | ☐ | |
| 12 | Pivot / crosstab | ☐ | ☐ | ☐ | |
| 13 | Unpivot | ☐ | ☐ | ☐ | |
| 14 | Anti-join (NOT EXISTS) | ☐ | ☐ | ☐ | |
| 15 | Self-join comparison | ☐ | ☐ | ☐ | |
| 16 | Hierarchy (recursive CTE) | ☐ | ☐ | ☐ | |
| 17 | Date spine / fill gaps | ☐ | ☐ | ☐ | |
| 18 | Median / percentile | ☐ | ☐ | ☐ | |
| 19 | Funnel / conversion | ☐ | ☐ | ☐ | |
| 20 | Retention cohorts | ☐ | ☐ | ☐ | |
| 21 | Histogram / bucketing | ☐ | ☐ | ☐ | |
| 22 | Ratio to total | ☐ | ☐ | ☐ | |
| 23 | Deterministic tie-break | ☐ | ☐ | ☐ | |
| 24 | Pairs without duplication | ☐ | ☐ | ☐ | |
| 25 | Upsert / merge | ☐ | ☐ | ☐ | |

Benchmark problem: [Adhoc/hackerrank_questions.md](../Adhoc/hackerrank_questions.md) Q3 — solved cold in ≤6 min, both ways, with the index and tie-break caveats volunteered unprompted: ☐

---

## Mock interview log

| # | Date | Type | Interviewer / platform | Problem | Self-score /4 | Their feedback | Action taken |
|---|---|---|---|---|---|---|---|
| 1 | | coding | | | | | |
| 2 | | design | | | | | |
| 3 | | behavioural | | | | | |

Score honestly against the [[01-dsa]] §1 axes: problem solving, coding, verification, communication.

---

## Story bank status ([[07-google-interview-playbook]] §5)

| # | Story slot | Written | Quantified result | Timed ≤3 min | Used in mock |
|---|---|---|---|---|---|
| 1 | Hardest technical problem | ☐ | ☐ | ☐ | ☐ |
| 2 | Led end-to-end | ☐ | ☐ | ☐ | ☐ |
| 3 | Disagreement | ☐ | ☐ | ☐ | ☐ |
| 4 | I was wrong | ☐ | ☐ | ☐ | ☐ |
| 5 | Ambiguity | ☐ | ☐ | ☐ | ☐ |
| 6 | Deadline / scope cut | ☐ | ☐ | ☐ | ☐ |
| 7 | Influence w/o authority | ☐ | ☐ | ☐ | ☐ |
| 8 | Mentoring | ☐ | ☐ | ☐ | ☐ |
| 9 | Unasked initiative | ☐ | ☐ | ☐ | ☐ |
| 10 | Learned fast | ☐ | ☐ | ☐ | ☐ |
| 11 | Negative feedback | ☐ | ☐ | ☐ | ☐ |
| 12 | Decision w/ incomplete data | ☐ | ☐ | ☐ | ☐ |

---

## Application tracker

| Company | Role / level | Applied | Referral | Recruiter call | Screen | Onsite | Outcome | Notes |
|---|---|---|---|---|---|---|---|---|
| Google | SWE L4 | | | | | | | |

---

## Reading log

| Item | Type | Done | 5-bullet summary written | Where I'd cite it |
|---|---|---|---|---|
| DDIA ch. 1–3 | book | ☐ | ☐ | |
| MapReduce | paper | ☐ | ☐ | |
| GFS | paper | ☐ | ☐ | |
| Bigtable | paper | ☐ | ☐ | |
| Spanner | paper | ☐ | ☐ | |
| Chubby | paper | ☐ | ☐ | |
| Dapper | paper | ☐ | ☐ | |
| Borg | paper | ☐ | ☐ | |
| The Tail at Scale | paper | ☐ | ☐ | |
| MillWheel / Dataflow | paper | ☐ | ☐ | |
| Zanzibar | paper | ☐ | ☐ | |
| Attention Is All You Need | paper | ☐ | ☐ | |
