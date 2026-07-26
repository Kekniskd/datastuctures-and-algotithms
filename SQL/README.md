# SQL practice

The 2 hrs/week track from [10-sql.md](../Roadmap/10-sql.md) §11. Every query gets
**executed**, never just read — unrun SQL is how NULL and fan-out bugs survive.

## Running it

No installs. Python's stdlib bundles SQLite (3.50 on Python 3.14).

```
python SQL/init.py                                   # rebuild auction.db from schema/
python SQL/init.py SQL/solutions/some-query.sql      # rebuild, then run a file
python SQL/init.py -k SQL/solutions/some-query.sql   # keep the db, just run the file
python SQL/init.py -i                                # rebuild, then a REPL
```

`init.py` drops and reloads everything in `schema/`, so the DB is disposable —
mangle it freely.

## Layout

```
schema/     one .sql per practice dataset: DDL + seed rows + expected output
patterns/   one file per §7 pattern — see _TEMPLATE.sql. Both solutions, EXPLAIN notes
solutions/  HackerRank / LeetCode answers, pattern named in the header comment
auction.db  generated, gitignored
```

## Dialect caveats

SQLite is the zero-friction choice, not the realistic one. Three things differ
from the MySQL 8 / Postgres you'll be asked about:

- **No real `DECIMAL`.** `DECIMAL(6,2)` gets REAL (float) affinity —
  `SELECT 0.1 + 0.2` returns `0.30000000000000004`. Wrap money in `ROUND(x, 2)`.
- **No `DATETIME` type.** `dt` is ISO-8601 TEXT. Lexical order equals
  chronological order, so `ORDER BY dt DESC` behaves — but date *functions*
  differ (`strftime` here, not `DATE_SUB` / `INTERVAL`).
- **`EXPLAIN QUERY PLAN`, not `EXPLAIN`,** and it's far less detailed. Good
  enough for "did it use the index"; not for real cost analysis.

Write the target dialect in every file header. When W9–W10 hits performance work
([10-sql.md](../Roadmap/10-sql.md) §11), switch to Postgres in Docker — by then
`EXPLAIN (ANALYZE, BUFFERS)` is the thing being learned and SQLite can't teach it.

## Datasets

| File | Tables | Covers |
|---|---|---|
| `schema/auction.sql` | buyers, lots, bids | latest-row-per-group, aggregate-without-fan-out, left-join NULLs, tie-breaks, anti-join |

The auction schema is the Q3 benchmark from
[hackerrank_questions.md](../Adhoc/hackerrank_questions.md) — the one
[09-progress-tracker.md](../Roadmap/09-progress-tracker.md) wants solved cold in
≤6 min, both ways. Its seed data is built to punish the obvious mistakes: one lot
with zero bids, buyers who outbid themselves, and a buyer who never bids.
