# 10 · SQL — query fluency to interview standard

← [[README]] · Hours: ~30 · Phases 1–2 (2 hrs/week drip), revised in Phase 4

**Calibration target:** [Adhoc/hackerrank_questions.md](../Adhoc/hackerrank_questions.md) Q3 (auction lot winners). That question is a fair benchmark — it requires *latest-row-per-group*, *aggregate-without-join-fan-out*, *LEFT JOIN + NULL handling*, and it comes with probes on `COUNT(*)` vs `COUNT(col)`, tie-breaking, and indexing. Everything below is aimed at making that question a 6-minute problem, and its harder cousins solvable too.

You should be able to solve every such question **twice** — once with window functions, once without. Interviewers ask for the other version (that file literally lists it as a probe).

---

## 1. Logical execution order (the key to half of all SQL confusion)

```
FROM → JOIN → WHERE → GROUP BY → HAVING → WINDOW → SELECT → DISTINCT → ORDER BY → LIMIT
```

Consequences you must be able to state:
- A `SELECT` alias is unusable in `WHERE`/`GROUP BY`/`HAVING` (it doesn't exist yet) but works in `ORDER BY`.
- `WHERE` filters rows, `HAVING` filters groups. `WHERE` before aggregation, `HAVING` after.
- **Window functions cannot appear in `WHERE`** — they're computed after it. To filter on `ROW_NUMBER()`, you must wrap it in a CTE/subquery. This is exactly why the auction solution has a `ranked` CTE.
- `DISTINCT` runs after `SELECT`, so `SELECT DISTINCT x, y` dedupes the *pair*, not `x`.
- `LIMIT` runs last, so `LIMIT` + no `ORDER BY` = nondeterministic results.

---

## 2. Joins — where the real bugs live

| Join | Keeps | Use for |
|---|---|---|
| `INNER` | Matches only | Default |
| `LEFT` | All left rows + matches | "All lots, even with no bids" ← the auction question |
| `RIGHT` | Mirror of LEFT | Rarely; rewrite as LEFT |
| `FULL OUTER` | Both sides | Reconciliation/diffing (not in MySQL — emulate with `UNION`) |
| `CROSS` | Cartesian product | Date spines, generating combinations |
| Self-join | Table to itself | Pairs, manager/employee, consecutive rows |
| Semi-join (`EXISTS`/`IN`) | Left rows that have a match, no duplication | "Customers who ordered" |
| Anti-join (`NOT EXISTS`/`LEFT JOIN … IS NULL`) | Left rows with no match | "Customers who never ordered" |

**The four join bugs that get asked about:**

1. **LEFT JOIN silently becomes INNER JOIN.** Putting a condition on the right table in `WHERE` filters out the NULL-extended rows:
   ```sql
   -- WRONG: drops lots with no bids
   FROM lots l LEFT JOIN bids b ON b.lot_id = l.id WHERE b.dt > '2024-01-01'
   -- RIGHT: condition belongs in ON
   FROM lots l LEFT JOIN bids b ON b.lot_id = l.id AND b.dt > '2024-01-01'
   ```
   Rule: for outer joins, filters on the *optional* side go in `ON`; filters on the driving table go in `WHERE`.

2. **Fan-out inflating aggregates.** Joining a 1:many table multiplies rows, so `SUM(l.starting_price)` counts the price once per bid. Fixes: aggregate in a subquery/CTE *before* joining, or use `SUM(DISTINCT …)` (fragile), or window functions.

3. **`COUNT(*)` vs `COUNT(col)` after a LEFT JOIN.** `COUNT(*)` counts rows — a zero-bid lot yields **1**, not 0. `COUNT(b.lot_id)` ignores NULLs and correctly yields **0**. This is the auction question's probe; get it right reflexively.

4. **Joining on a nullable column** — NULL never matches NULL, so those rows vanish.

---

## 3. NULL semantics (three-valued logic)

`TRUE / FALSE / UNKNOWN`. `NULL = NULL` → UNKNOWN, and `WHERE UNKNOWN` filters the row out. Therefore:

- Always `IS NULL` / `IS NOT NULL`. (`<=>` in MySQL, `IS NOT DISTINCT FROM` in Postgres for null-safe equality.)
- **`NOT IN` with a NULL in the subquery returns zero rows.** Ever. Use `NOT EXISTS` instead — this is the single most common silent SQL bug and a very common interview question.
- Aggregates skip NULLs: `AVG(col)` divides by the non-null count; `SUM` of an empty/all-null set is `NULL`, not `0` → wrap in `COALESCE(SUM(x), 0)`.
- `COALESCE`, `NULLIF`, `IFNULL`/`NVL`, `CASE WHEN … IS NULL`.
- `ORDER BY` null placement differs by dialect (`NULLS FIRST/LAST` in Postgres/Oracle; MySQL sorts NULLs first ascending).
- `NULL` in `CHECK`, `UNIQUE` (multiple NULLs usually allowed), and string concatenation (`NULL || 'x'` is NULL in Postgres, `CONCAT` differs in MySQL).

---

## 4. Aggregation

`COUNT / SUM / AVG / MIN / MAX`, `COUNT(DISTINCT x)`, `GROUP BY` on multiple columns, `HAVING`, `GROUP BY` with expressions.

- **Conditional aggregation** — the workhorse for pivots, funnels, and cohort tables:
  ```sql
  SELECT lot_id,
         COUNT(*)                                        AS bids,
         SUM(CASE WHEN dt >= '2024-01-01' THEN 1 ELSE 0 END) AS bids_2024,
         COUNT(DISTINCT buyer_id)                        AS unique_bidders
  FROM bids GROUP BY lot_id;
  ```
- String aggregation: `GROUP_CONCAT` (MySQL) / `STRING_AGG` (Postgres, SQL Server) / `LISTAGG` (Oracle).
- `ROLLUP` / `CUBE` / `GROUPING SETS` for subtotals `[stretch]`.
- MySQL's `ONLY_FULL_GROUP_BY`: selecting a non-aggregated, non-grouped column is an error in strict mode (and silently arbitrary without it). Know that "which row did MySQL pick?" is "undefined".
- `FILTER (WHERE …)` in Postgres — cleaner than `CASE`.

---

## 5. Window functions — the core skill for this question class

```sql
<fn>() OVER (PARTITION BY <cols> ORDER BY <cols> <frame>)
```
Windows compute per-row *without collapsing rows* — that's the whole point, and the answer to "why not GROUP BY?"

| Function | Returns | Classic use |
|---|---|---|
| `ROW_NUMBER()` | 1,2,3,4 — no ties | **Latest/top row per group**, dedup |
| `RANK()` | 1,2,2,4 — gaps | Competition ranking |
| `DENSE_RANK()` | 1,2,2,3 — no gaps | "Nth highest salary" |
| `NTILE(n)` | Bucket number | Quartiles, deciles |
| `LAG/LEAD(col, n, default)` | Prior/next row's value | Deltas, growth %, sessionization, gaps |
| `FIRST_VALUE/LAST_VALUE/NTH_VALUE` | Value at frame position | First purchase, latest status |
| `SUM/COUNT/AVG/MIN/MAX … OVER` | Aggregate alongside detail | Running totals, moving averages, group total per row |
| `PERCENT_RANK`, `CUME_DIST` | Relative position | Percentiles |

**Frames** — the part people skip and then get wrong:
- Default with `ORDER BY` is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` → running total.
- Default with **no** `ORDER BY` is the whole partition → `COUNT(*) OVER (PARTITION BY lot_id)` gives the group total on every row. That's the trick the auction solution uses to get `bid_count` and `rn` in one pass.
- `ROWS` counts physical rows; `RANGE` groups peer values (ties share a frame) — a real difference in running totals over duplicate dates.
- `LAST_VALUE(x) OVER (ORDER BY dt)` returns the *current* row, not the last one, because of the default frame. Fix with `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, or use `FIRST_VALUE` with `DESC`.
- Moving 7-day average: `AVG(x) OVER (PARTITION BY id ORDER BY d ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`.

Filtering on a window result requires a wrapper (CTE/subquery); some dialects offer `QUALIFY` (Snowflake/BigQuery/Teradata).

---

## 6. CTEs, subqueries, and set operations

- **CTE (`WITH`)**: readability, reuse, and the standard vehicle for "compute ranks, then filter". Multiple CTEs chain. Note: Postgres ≤11 materialized CTEs as an optimization fence (`MATERIALIZED`/`NOT MATERIALIZED` since 12); MySQL 8 merges them. Worth one sentence in an interview.
- **Recursive CTE**: `WITH RECURSIVE t AS (anchor UNION ALL recursive_member)` — org hierarchies, bill-of-materials, graph paths, generating a date spine, cumulative chains. Always bound the recursion (depth column) and know it exists to avoid infinite loops.
- **Subquery types:** scalar (returns one value — usable in `SELECT`), row, table (in `FROM`, a derived table needing an alias), **correlated** (re-evaluated per outer row — the second reference solution in that file; simple to write, potentially O(n) subquery executions).
- `EXISTS` vs `IN` vs `JOIN`: `EXISTS` short-circuits and is NULL-safe; `IN` with a large or NULL-containing list is risky; a `JOIN` can duplicate rows. Modern optimizers often equalize `EXISTS`/`IN`, but the *NULL* difference is semantic, not an optimization detail.
- `LATERAL` (Postgres) / `CROSS APPLY` (SQL Server): a correlated subquery in `FROM` — the neatest "top 3 bids per lot" and often the fastest.
- `UNION` (dedupes — costs a sort) vs `UNION ALL` (doesn't — default choice), `INTERSECT`, `EXCEPT`/`MINUS`.

---

## 7. Pattern catalog — the actual interview currency

Learn these as templates. Roughly 90% of SQL interview questions are one of these, or two composed.

| # | Pattern | Technique | Trigger phrase |
|---|---|---|---|
| 1 | **Latest row per group** | `ROW_NUMBER() … ORDER BY dt DESC` + `= 1`; or correlated `ORDER BY dt DESC LIMIT 1`; or join to `MAX(dt)` subquery | "current winner", "most recent status", "last login" |
| 2 | **Top-N per group** | `ROW_NUMBER() <= N`, or `LATERAL`/`CROSS APPLY` | "top 3 products per category" |
| 3 | Nth highest value | `DENSE_RANK() = N`, or `LIMIT 1 OFFSET N-1` | "second highest salary" |
| 4 | Aggregate + keep detail | `SUM/COUNT … OVER (PARTITION BY …)` | "each row with its group total / % of total" |
| 5 | **Aggregate without fan-out** | Pre-aggregate in a CTE, then join | Multiple 1:many children |
| 6 | Running total / cumulative | `SUM(x) OVER (ORDER BY d)` | "cumulative revenue" |
| 7 | Moving average | `AVG(x) OVER (… ROWS n PRECEDING)` | "7-day rolling" |
| 8 | Period-over-period | `LAG(x) OVER (ORDER BY month)` then `(x - prev)/prev` | "MoM growth", "vs previous" |
| 9 | Find duplicates / dedupe | `GROUP BY … HAVING COUNT(*) > 1`; delete with `ROW_NUMBER() > 1` | "remove duplicate emails" |
| 10 | **Gaps and islands** | `ROW_NUMBER()` minus a date/int sequence → constant per island | "consecutive days", "3+ in a row", "streaks" |
| 11 | Sessionization | `LAG(ts)` → gap flag → `SUM() OVER` as session id | "group events into sessions" |
| 12 | Pivot / crosstab | `SUM(CASE WHEN cat = 'x' THEN v END)` per column | "one column per month" |
| 13 | Unpivot | `UNION ALL` per column, or `CROSS JOIN` a values list | Wide → long |
| 14 | Anti-join | `NOT EXISTS` (not `NOT IN`) | "who has never…" |
| 15 | Self-join comparison | Join a table to itself on a relation | "earns more than their manager" |
| 16 | Hierarchy / graph walk | Recursive CTE | "all reports under X", "path to root" |
| 17 | Date spine / fill gaps | Recursive CTE or calendar table `LEFT JOIN` facts | "show zero for days with no sales" |
| 18 | Median / percentile | `PERCENTILE_CONT` (Postgres/Oracle), or `ROW_NUMBER` from both ends | "median salary per dept" |
| 19 | Funnel / conversion | Conditional aggregation over stage flags | "view → cart → purchase rates" |
| 20 | Retention cohorts | First-event month per user, then `DATEDIFF` bucketing | "month-N retention" |
| 21 | Histogram / bucketing | `CASE`/`FLOOR(x/bucket)` + `GROUP BY`, or `NTILE` | "distribution of order sizes" |
| 22 | Ratio to total | `x / SUM(x) OVER ()` | "% of overall" |
| 23 | Deterministic tie-break | Multiple `ORDER BY` keys, last one unique | "if tied, fewest stops" ← that file's Q2 tiebreak, in SQL form |
| 24 | Pairs without duplication | Self-join with `a.id < b.id` | "all pairs of users who…" |
| 25 | Upsert / merge | `ON CONFLICT DO UPDATE` (Postgres) / `ON DUPLICATE KEY UPDATE` (MySQL) / `MERGE` | Idempotent loads |

---

## 8. Solving the auction question class, step by step

A repeatable recipe. Say these steps out loud in an interview — the process is graded, same as [[01-dsa]].

1. **State the output grain.** "One row per lot." That single sentence determines that `lots` is the driving table and that every join must not multiply it.
2. **Pick the driving table and join direction.** All lots must appear, including zero-bid ones → `FROM lots LEFT JOIN …`. Say why.
3. **Compute per-group facts at the child grain first** (in a CTE), so the join back is 1:1: bid count per lot, and the latest bid per lot.
4. **Latest-per-group via `ROW_NUMBER()`** partitioned by `lot_id`, ordered by `dt DESC`; join with `AND rn = 1`. Notice you can get the count in the *same* CTE with `COUNT(*) OVER (PARTITION BY lot_id)` — no extra pass.
5. **Handle NULLs at the boundary.** `COALESCE(bid_count, 0)` for the count, and again inside the price arithmetic, because `starting_price + bid_step * NULL` is NULL. Leave `current_winner` as NULL — the spec asks for it.
6. **Order deterministically** (`ORDER BY l.name ASC`) and only select the requested columns, in the requested order.
7. **Then volunteer the tradeoffs before being asked:**
   - `COUNT(*)` vs `COUNT(b.lot_id)` after the outer join (see §2.3).
   - **Ties on `dt`:** with no primary key on `bids`, `ROW_NUMBER` picks arbitrarily and is not stable across runs. Fix: add a tie-break column (`buyer_id`), or an `id`/insert-order surrogate key — and note the schema flaw, since the probe list rewards it.
   - **Index:** `bids(lot_id, dt DESC)` serves both the partitioned count and the ordered pick; add `buyers(id)` (already the PK).
   - **Window vs correlated subquery:** the correlated version runs 3 subqueries per lot (2 of which are the identical `COUNT`, so at minimum hoist it); the window version scans `bids` once. Prefer the window function, and note the correlated version is the required fallback on MySQL 5.7 / older engines.
   - Rewrite without windows: `GROUP BY` CTE for the count + a `MAX(dt)` join (and how *that* version breaks on duplicate `dt` by returning two rows — a genuinely good thing to point out).

---

## 9. Performance & internals

- **Read a plan.** `EXPLAIN` / `EXPLAIN ANALYZE` (Postgres) / `EXPLAIN FORMAT=JSON` (MySQL). Look for: estimated vs actual rows, seq/full scan on a big table, nested loop with a high row count, sort spilling to disk, and the wrong join order.
- **Index basics** ([[04-hld]] §3 has the B+tree detail): index on join keys and on high-selectivity filters; **composite index leftmost-prefix rule** — `(a, b, c)` serves `a`, `a,b`, `a,b,c`, not `b` alone; column order should be equality-filters first, then range/sort; covering/index-only scans; index on `(partition_col, sort_col DESC)` for window queries.
- **Sargability:** `WHERE YEAR(dt) = 2024` can't use an index — rewrite as a range `dt >= '2024-01-01' AND dt < '2025-01-01'`. Same for `WHERE col + 0 = x`, leading-wildcard `LIKE '%foo'`, and implicit type casts.
- Other classics: `SELECT *` over a wide table, `OFFSET 100000` pagination (→ keyset/cursor pagination), `DISTINCT` masking a join bug, `OR` preventing index use (→ `UNION ALL`), N+1 queries from the application layer, stale statistics, over-indexing slowing writes.
- Transactions and isolation levels, locking, deadlocks, MVCC → all in [[04-hld]] §3. SQL interviews increasingly ask "what isolation level does this need?" — know that read-modify-write needs `SELECT … FOR UPDATE` or an optimistic version check.

---

## 10. Dialect differences (HackerRank lets you pick; know at least two)

| Concept | MySQL 8 | PostgreSQL | SQL Server | Oracle |
|---|---|---|---|---|
| Row limit | `LIMIT n` | `LIMIT n` | `TOP n` / `OFFSET…FETCH` | `FETCH FIRST n ROWS` / `ROWNUM` |
| Null default | `IFNULL` | `COALESCE` | `ISNULL` | `NVL` |
| String concat | `CONCAT(a,b)` | `a \|\| b` | `a + b` | `a \|\| b` |
| Group string | `GROUP_CONCAT` | `STRING_AGG` | `STRING_AGG` | `LISTAGG` |
| Full outer join | ✗ (emulate) | ✓ | ✓ | ✓ |
| Window functions | 8.0+ | ✓ | 2012+ | ✓ |
| Date diff | `DATEDIFF(a,b)` | `a - b` / `AGE()` | `DATEDIFF(unit,a,b)` | `a - b` / `MONTHS_BETWEEN` |
| Upsert | `ON DUPLICATE KEY UPDATE` | `ON CONFLICT DO UPDATE` | `MERGE` | `MERGE` |
| Case sensitivity | Usually insensitive collation | Sensitive | Depends on collation | Sensitive |

Pick **MySQL 8** as your default for HackerRank-style screens (most common), and know Postgres for real work. State your dialect at the top of an interview answer.

---

## 11. Practice plan (2 hrs/week, W1–W10)

| Weeks | Focus | Source |
|---|---|---|
| W1–W2 | `SELECT`/joins/NULLs/aggregation; execution order | HackerRank SQL Basic + Intermediate track |
| W3–W4 | Subqueries, `EXISTS`, set ops, CTEs | LeetCode Database Easy/Medium |
| W5–W6 | **Window functions** — every function in §5, all frames | LeetCode DB Medium/Hard, DataLemur/StrataScratch |
| W7–W8 | Patterns 1–25 from §7, one template each | Mixed, plus rewrite each without windows |
| W9–W10 | Recursive CTEs, performance/`EXPLAIN`, dialect quirks | PGExercises, *Advanced SQL Puzzles* |
| Phase 4 | Timed: 3 problems in 30 min, no docs | Random mixed sets |

**Targets:** HackerRank SQL Advanced certificate; LeetCode DB 50 complete; a Medium window-function question in ≤8 min, written correctly on the first run.

**Deliverable — do this in W1, it makes everything else concrete:** create a `SQL/` folder in this repo with
```
SQL/
  schema/auction.sql        -- the buyers/lots/bids schema from Adhoc/hackerrank_questions.md + seed rows
  schema/<others>.sql       -- employees/orders/events for the other patterns
  patterns/01-latest-per-group.sql   -- one file per §7 pattern: problem, 2 solutions, EXPLAIN notes
  solutions/                -- HackerRank/LeetCode solutions with the pattern named in a comment
```
Use SQLite or a local Postgres/MySQL in Docker (`docker run -e POSTGRES_PASSWORD=… -p 5432:5432 postgres`) so you actually *run* the queries. Reading SQL you never executed is how the NULL and fan-out bugs survive.

Header convention for every solution file, mirroring your DSA one:
```sql
-- Problem: Auction lot winners  ·  Source: Adhoc/hackerrank_questions.md Q3
-- Pattern: latest-row-per-group + aggregate-without-fan-out
-- Dialect: MySQL 8
-- Indexes assumed: bids(lot_id, dt DESC)
-- Mistake I made: used COUNT(*) after the LEFT JOIN → zero-bid lots showed 1
```

---

## 12. Rapid-fire bank (answer each in <60 s)

1. Give the logical execution order and explain why a `SELECT` alias fails in `WHERE`.
2. Why can't you put `ROW_NUMBER() > 1` in a `WHERE` clause?
3. `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)` after a `LEFT JOIN`.
4. Why does `NOT IN (subquery)` return nothing when the subquery has a NULL?
5. `WHERE` vs `ON` for a condition on the right table of a `LEFT JOIN` — what changes?
6. `RANK` vs `DENSE_RANK` vs `ROW_NUMBER` on the values 10, 20, 20, 30.
7. Write "second highest salary per department" two ways.
8. Latest status per order — three approaches and their tradeoffs.
9. Why does `LAST_VALUE()` usually return the wrong thing?
10. `ROWS` vs `RANGE` in a window frame — construct a case where they differ.
11. Running total and 7-day moving average in one query.
12. Find users with 3+ consecutive days of activity.
13. Delete duplicate rows keeping the newest, with no primary key available.
14. `UNION` vs `UNION ALL` — which is faster, and why?
15. `EXISTS` vs `IN` vs `JOIN` for a semi-join.
16. What is a correlated subquery and when is it a performance trap?
17. Turn 12 monthly rows into 12 columns.
18. Why is `WHERE YEAR(created_at) = 2024` slow?
19. You have `INDEX(a, b, c)` — which of these use it: filter on `b`; filter on `a` + sort on `b`; filter on `a` + `c`?
20. Aggregating a parent with two 1:many children gives inflated sums. Why, and two fixes?
21. Show all 30 days including days with zero orders.
22. Median per group without a percentile function.
23. `HAVING` without `GROUP BY` — legal? What does it do?
24. What does `GROUP BY` do to NULLs?
25. Recursive CTE: print an org chart with depth.
26. Write a query that's correct on Postgres and wrong (or invalid) on MySQL.
27. When would you use a materialized view over a query?
28. Two concurrent transactions both do read-modify-write on a counter. What goes wrong and how do you fix it in SQL?
29. Cursor vs offset pagination — write the cursor version.
30. Your query got 100× slower after a deploy and the SQL didn't change. Give five hypotheses.

---

## 13. Resources (one primary, don't collect)

- **Primary practice:** HackerRank SQL track (matches the screen format you're benchmarking against) → LeetCode Database 50.
- **Window functions:** Postgres docs tutorial on window functions (short and the clearest thing written on the topic) + `use-the-index-luke.com` for indexing.
- **Depth:** *SQL Performance Explained* (Winand) for indexes; *SQL Antipatterns* (Karwin) for design; *Advanced SQL Puzzles* for the hard pattern work.
- Also: mode.com/sql-tutorial, pgexercises.com, DataLemur/StrataScratch for interview-shaped analytics questions.
