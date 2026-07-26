# Technical Interview Question Set

Three questions covering string logic, REST API consumption, and SQL aggregation.

---

## Question 1 — Username Strength Classifier

### Description

A registration system rates each requested username as `strong` or `weak`. A username is **weak** if any of the following hold:

1. It contains any word from a given blocklist as a substring (case-sensitive).
2. It is shorter than 6 characters.
3. All of its characters belong to a single class — all digits, all uppercase letters, or all lowercase letters.

Otherwise it is **strong**. Classify every username in the input.

### Input

- `usernames`: array of `n` strings
- `commonWords`: array of `m` blocklisted strings

### Output

An array of `n` strings, each `"strong"` or `"weak"`, in the same order as the input.

### Sample 1

```
usernames   = ["hello", "chargeR", "pass123"]
commonWords = ["hello", "123", "password", "xyz", "999"]

→ weak      (contains "hello")
  strong
  weak      (contains "123")
```

### Sample 2

```
usernames   = ["12345", "YUIOYES", "qwertyuiop"]
commonWords = ["ty", "xyz"]

→ weak      (digits only, too short)
  weak      (uppercase only)
  weak      (lowercase only; also contains "ty")
```

> **Note:** the minimum-length threshold isn't pinned down by the samples alone — `12345` fails at 5 characters and `chargeR` passes at 7. State your threshold explicitly to the candidate.

### Reference solution

```python
def getUsernameStrength(usernames, commonWords):
    out = []
    for u in usernames:
        weak = (
            len(u) < 6
            or any(w in u for w in commonWords)
            or u.isdigit()
            or u.isupper()
            or u.islower()
        )
        out.append("weak" if weak else "strong")
    return out
```

### Probes

- Why is substring matching the right check rather than equality?
- `isupper()` on `"ABC1"` returns `True` — is that the behavior you want?
- Complexity in terms of n, m, and string length? Where would this break at scale?

---

## Question 2 — Find the Speedster (REST API)

### Description

Given a marathon name and a runner sex, find the fastest runner matching both. Fastest means highest `top_speed`. Query the runner database over HTTP GET.

Endpoint: `https://jsonmock.hackerrank.com/api/marathon?sex=<sex>`

Results are paginated; add `&page=<num>`. The response contains `page`, `per_page`, `total`, `total_pages`, and `data` (array of runner objects).

Each runner object includes `name`, `sex`, `top_speed`, `stops_taken`, `marathon_name`, and other fields not relevant here.

If two runners tie on `top_speed`, return the one with fewer `stops_taken`. If no runner matches, return an empty string.

### Input

- `marathon`: string — the marathon name to filter on
- `sex`: string — the sex to filter on (passed as a query parameter)

### Output

A string: the name of the matching runner, or `""` if none.

### Sample

```
Input:  Cityscape Marathon / female
Output: Gretchen Cummings        (top speed 14.79)

Input:  Cityscape Marathon / male
Output: Laura Schultz Sr.        (top speed 13.79)
```

### Reference solution

```python
import requests

def findSpeedster(marathon, sex):
    base = "https://jsonmock.hackerrank.com/api/marathon"
    best = None
    page, total_pages = 1, 1

    while page <= total_pages:
        r = requests.get(base, params={"sex": sex, "page": page}).json()
        total_pages = r["total_pages"]
        for run in r["data"]:
            if run["marathon_name"] != marathon:
                continue
            key = (run["top_speed"], -run["stops_taken"])
            if best is None or key > best[0]:
                best = (key, run["name"])
        page += 1

    return best[1] if best else ""
```

### Probes

- Why filter `sex` server-side but `marathon_name` client-side? The API supports arbitrary `fieldname=value` — a strong candidate notices they could filter both server-side and cut the transfer.
- The tiebreak is a tuple with a negated second element. Can they explain why negation works, or do they reach for an explicit comparison?
- What if `total_pages` were 500? Sequential vs. concurrent fetching, and does the max even need all pages held in memory?
- Error handling: non-200 responses, malformed JSON, network timeout.

---

## Question 3 — Auction Lot Winners (SQL)

### Description

An auction service uses a "bid over starting price" model. Buyers can raise a lot's price any number of times, each bid adding a fixed increment set by the seller. The buyer who placed the **most recent** bid is the current winner.

Return every available lot with its bid count, current price, and current winner.

### Schema

```
buyers
  id        INT           PRIMARY KEY
  username  VARCHAR(255)

lots
  id              INT           PRIMARY KEY
  name            VARCHAR(255)
  starting_price  DECIMAL(6,2)
  bid_step        DECIMAL(6,2)

bids
  buyer_id  INT       FOREIGN KEY → buyers.id
  lot_id    INT       FOREIGN KEY → lots.id
  dt        DATETIME
```

Notes: some lots have no bids at all, and a buyer may outbid their own bid.

### Output

Columns `name | starting_price | bid_step | bids | current_price | current_winner`, sorted ascending by `name`.

- `bids` — total number of bids on the lot
- `current_price` — `starting_price + (bid_step * number_of_bids)`
- `current_winner` — username of the buyer who placed the last bid; `NULL` when the lot has no bids

### Sample output

| name | starting_price | bid_step | bids | current_price | current_winner |
|---|---|---|---|---|---|
| 24-Hour All Day Allergy | 2963.05 | 29.63 | 0 | 2963.05 | NULL |
| Pro-Den Rx | 9375.49 | 281.26 | 8 | 11625.57 | shanford1 |
| Soapy Hands | 550.86 | 16.53 | 3 | 600.45 | vdanielovitch0 |
| TISSEEL | 6601.09 | 66.01 | 9 | 7195.18 | vdanielovitch0 |

### Reference solution — window function

```sql
WITH ranked AS (
    SELECT
        b.lot_id,
        b.buyer_id,
        COUNT(*)     OVER (PARTITION BY b.lot_id)                     AS bid_count,
        ROW_NUMBER() OVER (PARTITION BY b.lot_id ORDER BY b.dt DESC)  AS rn
    FROM bids b
)
SELECT
    l.name,
    l.starting_price,
    l.bid_step,
    COALESCE(r.bid_count, 0)                                  AS bids,
    l.starting_price + l.bid_step * COALESCE(r.bid_count, 0)   AS current_price,
    bu.username                                               AS current_winner
FROM lots l
LEFT JOIN ranked r  ON r.lot_id = l.id AND r.rn = 1
LEFT JOIN buyers bu ON bu.id = r.buyer_id
ORDER BY l.name ASC;
```

### Reference solution — correlated subquery

```sql
SELECT
    l.name,
    l.starting_price,
    l.bid_step,
    (SELECT COUNT(*) FROM bids b WHERE b.lot_id = l.id) AS bids,
    l.starting_price + l.bid_step *
        (SELECT COUNT(*) FROM bids b WHERE b.lot_id = l.id) AS current_price,
    (SELECT bu.username
       FROM bids b
       JOIN buyers bu ON bu.id = b.buyer_id
      WHERE b.lot_id = l.id
      ORDER BY b.dt DESC
      LIMIT 1) AS current_winner
FROM lots l
ORDER BY l.name ASC;
```

### Probes

- Why `LEFT JOIN` rather than `INNER JOIN`? Have them trace the zero-bid lot.
- `COUNT(*)` vs. `COUNT(b.lot_id)` after a left join — do they know the difference?
- How would they break the tie if two bids on the same lot shared an identical `dt`? `bids` has no primary key, which is itself worth discussing.
- Which version performs better, and what indexes would they add? (`bids(lot_id, dt DESC)`)
- Ask them to write it without window functions if they used them, and vice versa.