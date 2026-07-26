# 01 · DSA — the primary gate

← [[README]] · Hours: ~180 · Phases 1–4

Google's coding rounds are 2–4 of your 4–5 onsite rounds. Everything else in this roadmap is a multiplier on a number that DSA sets.

---

## 1. What Google actually grades

Four axes, scored independently. You can write a working optimal solution and still get a "no hire":

| Axis | What it means | How you lose it |
|---|---|---|
| **Problem solving** | Do you find a viable approach and improve it? | Jumping to code; not exploring brute force → optimal |
| **Coding** | Clean, compiling, idiomatic, decomposed | Monolithic function, no helper names, mutating while iterating |
| **Verification** | Do you test yourself? | "I think it works." Google's editor doesn't run code — you *are* the compiler |
| **Communication** | Can the interviewer follow you? | Silence, or narrating keystrokes instead of reasoning |

Google-specific mechanics:
- **No autocomplete, no execution.** A shared doc-like editor. Practice in Notepad / a bare `.txt`.
- **Follow-ups are the point.** Expect "now the input doesn't fit in memory", "now it's streaming", "now make it concurrent". The first solution is the setup.
- **Interviewer hints are data, not charity.** Take them fast; ignoring a hint is a strong negative signal.

---

## 2. Language: Python (correct choice — with conditions)

Know these cold, because "what's the complexity of your own line of code" is a real failure mode:

| Operation | Complexity | Trap |
|---|---|---|
| `list.append` / `pop()` | O(1) amortized | `pop(0)` is O(n) → use `collections.deque` |
| `list.insert(0, x)` | O(n) | Same |
| `x in list` | O(n) | `x in set` is O(1) — interviewers watch for this |
| `dict` / `set` ops | O(1) average | Worst case O(n); mention it if asked |
| `sorted()` / `list.sort()` | O(n log n) | Timsort, stable, O(n) space for `sorted` |
| `heapq` push/pop | O(log n) | Min-heap only — negate for max-heap |
| String concatenation in loop | O(n²) | Use `''.join(parts)` |
| Slicing `a[i:j]` | O(j−i) time and space | Hidden cost inside loops |
| `str`/`tuple` immutability | — | Enables use as dict keys / memo keys |

Must-know stdlib: `collections` (`deque`, `defaultdict`, `Counter`, `OrderedDict`), `heapq` (incl. `nlargest`, `heapify`), `bisect` (`bisect_left/right` — a huge time-saver), `functools.lru_cache`, `itertools`, `math.inf`, `sys.setrecursionlimit`.

Python-specific interview hazards: mutable default arguments; recursion depth ~1000 (say "I'd convert to iterative in production"); integer division `//` with negatives; closures capturing loop variables; deep copy vs shallow copy of nested lists (`[[0]*n]*m` is a classic bug).

---

## 3. Pattern index — the real curriculum

Target ~250 problems. Distribution: 20% Easy, 55% Medium, 25% Hard. The unit of learning is the **pattern**, not the problem.

| #   | Pattern                                           | Count | Signature triggers                                    | Canonical problems                                                                          |
| --- | ------------------------------------------------- | ----- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1   | Two pointers                                      | 12    | Sorted array, pair/triplet, in-place partition        | 3Sum, Container With Most Water, Trapping Rain Water, Sort Colors                           |
| 2   | Sliding window                                    | 12    | "longest/shortest substring/subarray with…"           | Longest Substring w/o Repeat, Min Window Substring, Max Sliding Window                      |
| 3   | Prefix sum / difference array                     | 8     | Range sums, subarray count, "divisible by k"          | Subarray Sum Equals K, Product of Array Except Self, Range Sum 2D                           |
| 4   | Hashing                                           | 12    | Count, group, dedup, complement lookup                | Group Anagrams, Two Sum, Longest Consecutive Sequence                                       |
| 5   | Binary search (array)                             | 8     | Sorted, rotated, boundary                             | Search Rotated, Find First/Last, Median of Two Sorted Arrays                                |
| 6   | **Binary search on the answer**                   | 8     | "minimum maximum X", monotone feasibility             | Koko Eating Bananas, Split Array Largest Sum, Capacity to Ship                              |
| 7   | Sorting + greedy                                  | 10    | Intervals, scheduling, exchange argument              | Merge Intervals, Meeting Rooms II, Non-overlapping Intervals, Task Scheduler                |
| 8   | Linked list                                       | 10    | In-place pointer surgery                              | Reverse in k-Groups, Cycle II, Merge k Sorted, Copy w/ Random Pointer                       |
| 9   | Stack / monotonic stack                           | 10    | "next greater", nesting, parsing                      | Daily Temperatures, Largest Rectangle in Histogram, Valid Parentheses, Basic Calculator     |
| 10  | Heap / top-K / two heaps                          | 10    | K-th, streaming median, merge k                       | Kth Largest, Find Median from Data Stream, Merge k Lists, Top K Frequent                    |
| 11  | Trees — traversal & recursion                     | 16    | Any binary tree                                       | Level Order, Diameter, LCA, Serialize/Deserialize, Validate BST, Right Side View            |
| 12  | Trie                                              | 6     | Prefix, word dictionary, autocomplete                 | Implement Trie, Word Search II, Design Add/Search Words                                     |
| 13  | Graphs — BFS/DFS/grid                             | 14    | Grid, islands, shortest unweighted path               | Number of Islands, Rotting Oranges, Word Ladder, Clone Graph, Pacific Atlantic              |
| 14  | Topological sort                                  | 6     | Dependencies, ordering, cycle in DAG                  | Course Schedule I/II, Alien Dictionary                                                      |
| 15  | Union-Find (DSU)                                  | 8     | Connectivity, merging groups, cycle in undirected     | Redundant Connection, Accounts Merge, Number of Provinces, Kruskal MST                      |
| 16  | Shortest path (Dijkstra / Bellman-Ford / 0-1 BFS) | 6     | Weighted graph, "cheapest", "min effort"              | Network Delay Time, Cheapest Flights K Stops, Path With Minimum Effort                      |
| 17  | Backtracking                                      | 12    | Enumerate all, permutations/combinations, constraints | Subsets, Permutations, N-Queens, Word Search, Sudoku, Combination Sum                       |
| 18  | DP 1D                                             | 12    | Choice per index, "ways to", "max profit"             | Climbing Stairs, House Robber, Coin Change, Word Break, LIS, Decode Ways                    |
| 19  | DP 2D / grid / strings                            | 14    | Two sequences, grid paths                             | Edit Distance, LCS, Unique Paths, Regex Matching, Interleaving String                       |
| 20  | DP on intervals / trees / bitmask `[stretch]`     | 8     | Merge ranges, tree subproblems, subset state          | Burst Balloons, Binary Tree Cameras, TSP-style                                              |
| 21  | Bit manipulation                                  | 6     | XOR tricks, masks, counting bits                      | Single Number I/II/III, Counting Bits, Subsets via masks                                    |
| 22  | Math / number theory                              | 6     | Primes, GCD, overflow, base conversion                | Sieve, Pow(x,n), Excel Column, Happy Number                                                 |
| 23  | Design / data-structure build                     | 10    | "Design a X that supports Y in O(1)"                  | LRU Cache, LFU Cache, Insert Delete GetRandom, Design Twitter, Rate Limiter, Snapshot Array |
| 24  | String matching                                   | 4     | Pattern search, rolling hash                          | Implement strStr (KMP), Repeated Substring, Rabin–Karp                                      |
| 25  | Segment tree / BIT `[stretch]`                    | 4     | Range query + point update                            | Range Sum Mutable, Count of Smaller After Self                                              |
| 26  | Sampling / reservoir / randomized `[stretch]`     | 3     | Streams, unknown length, quickselect                  | Random Pick with Weight, Kth Largest via quickselect, Linked List Random Node               |

**Google flavour note:** Google leans toward graphs, grids/matrix simulation, string parsing, binary search on answer, and "design a data structure with these invariants". It leans *away* from long chains of obscure DP compared to Meta/Amazon. Weight accordingly — but DP is still ~15% of what you'll see.

### 3.1 Resource sequencing: Structy → LeetCode

**Structy is the teaching resource; LeetCode is the testing resource.** They're not substitutes.

| Phase | Use | Why |
|---|---|---|
| W1–W10 | **Structy modules in order**, plus 3–5 LeetCode problems/week on the same pattern | Structy's strength is teaching you to *derive* — decision trees, recursive structure, why an invariant holds. Best-sequenced graph and DP progressions available |
| W11–W16 | **LeetCode random mixed sets**, Hard tier, `Patterns/` notes as your reference | Volume, difficulty ceiling, and pattern *recognition* with no topic label |
| W17–W20 | LeetCode timed, plain no-autocomplete `.txt` editor | Interview simulation ([[07-google-interview-playbook]] §4) |

Structy's four gaps, and the fix for each:
1. **Volume/difficulty ceiling** — its set won't reach 250 problems or 60 Hards. LeetCode covers the tail from W11.
2. **Every problem arrives labeled with its pattern.** This is the big one: it trains recall of a known technique, not recognition of an unknown one. Fix: after each lesson, solve one LeetCode problem of the same pattern *without rereading the lesson*. If you can't, you learned the solution, not the pattern. From W11, only random mixed sets.
3. **No timed or randomized mode, no bare editor.** Supply that yourself from W17.
4. **Google-flavoured areas are underweighted** — grid/matrix simulation, string parsing, binary search on the answer, and pattern 23 (design a data structure). Top those up directly from the table above; patterns 6, 23, 24 and 25 in particular will need LeetCode.

Also unaffected: SQL ([[10-sql]]) has no Structy coverage and runs on its own 2 hrs/week track.

---

## 4. Study method (this is where the leverage is)

**The solve loop, every single problem:**
1. **Restate + clarify** (30s): input ranges, duplicates, empty, negatives, sorted?, return format.
2. **2–3 examples by hand**, including one edge case. Write them down.
3. **Brute force out loud**, with complexity. Never skip this — it's a graded step.
4. **Find the bottleneck**, then name the pattern that removes it ("repeated lookup → hash", "repeated range recompute → prefix sum", "monotone predicate → binary search").
5. **State the plan in 3–5 sentences before typing.** If you can't, you're not ready to type.
6. **Code**, with real names and a helper function or two.
7. **Dry-run your own code** on the example line by line — Google gives you no interpreter.
8. **Edge cases + complexity + "how would this change if the input were 10 TB / streaming / concurrent?"**

**After every problem, write into the solution file:**
```python
# Problem: <name> · <difficulty> · <url>
# Pattern: sliding window
# Time: O(n) — each index enters and leaves the window once
# Space: O(k) — window contents only
# Key insight: shrink from the left only while the invariant is violated
# Mistake I made: forgot to shrink before recording the answer
```
That `Mistake I made` line is the highest-value line in this whole roadmap. It becomes your personal review deck.

**Spaced repetition:** re-solve at day 1 → day 7 → day 30. Track in [[09-progress-tracker]]. Retire after 3 clean independent solves. Anything solved by recall-not-understanding stays in the queue.

**Timing targets (by end of Phase 3):** Easy ≤10 min · Medium ≤25 min · Hard ≤40 min, including narration and dry-run.

---

## 5. Repo hygiene (use what you already have)

Your current layout is `Easy/<Topic>/` and `Medium/<Topic>/`. Difficulty-first fights the way you actually recall things. Suggested evolution — **pattern-first**, difficulty as a tag in the header:

```
Patterns/
  01-two-pointers/
  02-sliding-window/
  ...
  23-design/
Notes/            # one .md per pattern: template, triggers, pitfalls
Review/           # spaced-repetition queue + failure log
```

Keep the existing folders as-is (don't burn a weekend on a migration) — add `Patterns/` going forward and symlink/copy the good old solutions in as you re-solve them. You're in an Obsidian vault, so per-pattern notes will graph nicely against these roadmap files.

Also worth doing, because it's cheap and it's a code-quality signal if anyone reads your GitHub: keep the `unittest` template you already have in [NoteBook/uniTest_template.py](../NoteBook/uniTest_template.py) and add a test to every new solution. Two asserts is enough.

---

## 6. Communication script for the coding round

Memorize this skeleton; it makes you look senior in the first 90 seconds:

> "Let me make sure I have the problem: given ___, return ___. Can I assume ___? What are the input sizes?"
> "Here's a small example: ___ → ___. And an edge case: ___."
> "The brute force is ___, which is O(n²) time because ___. The bottleneck is ___."
> "I can remove that with ___ because ___. That gives O(n log n) / O(n)."
> "Plan: (1) ___ (2) ___ (3) ___. I'll write a helper for ___. Sound reasonable before I code?"
> *[code, narrating intent per block, not per keystroke]*
> "Let me trace my code on the example: i=0 ___, i=1 ___ … returns ___. Correct."
> "Edge cases: empty input → ___, single element → ___, all duplicates → ___."
> "Final complexity: ___. If the input didn't fit in memory I'd ___."

---

## 7. Anti-patterns to kill early

- Reading solutions before a real 20-minute attempt (feels productive, teaches nothing)
- Solving by topic label — the interview doesn't tell you the pattern. Do **random mixed sets** from Phase 2 onward.
- Optimizing before a correct baseline exists
- Practicing with autocomplete/AI assistance. Turn Copilot **off** for practice files.
- Counting problems instead of counting *patterns you can derive from scratch*
- Never being uncomfortable. If you're not failing ~30% of new problems, the difficulty is too low.

---

## 8. Milestones

| End of | Problems | Capability |
|---|---|---|
| W4 | 60 | All Easy patterns automatic; Medium arrays/strings/hashing solid |
| W10 | 150 | Every pattern 1–17 attempted; unseen Medium ≤25 min at 70% |
| W16 | 210 | DP + design + advanced graphs; first Hards landing consistently |
| W20 | 250 | Mock-interview performance, no-autocomplete editor, 60% Hard approach rate |
