-- Problem: Auction lot winners  ·  Source: Adhoc/hackerrank_questions.md Q3
-- Pattern: latest-row-per-group + aggregate-without-fan-out
-- Dialect: SQLite 3.50
-- Indexes assumed: bids(lot_id, dt DESC)
-- Mistake I made:
--
-- Benchmark (09-progress-tracker): cold, both ways, <= 6 min, with the index
-- and tie-break caveats volunteered unprompted. Time yourself. Don't peek at
-- the reference in Adhoc/hackerrank_questions.md until you've committed an
-- attempt -- reading it first converts a benchmark into a reading exercise.
--
--   python SQL/init.py SQL/solutions/q3-auction-lot-winners.sql
--
-- Expected output is at the bottom of SQL/schema/auction.sql.


-- Version A -- window functions




-- Version B -- no window functions (correlated subquery or group-by join)




-- Self-check, answer each in one line before you look anything up:
--   1. LEFT JOIN vs INNER JOIN -- trace lot 1 through both.
--   2. COUNT(*) vs COUNT(b.lot_id) after a left join -- which one lies, and why?
--   3. Two bids on one lot share a dt. What does your query return? Should it?
--   4. Which version wins on a 10M-row bids table, and what index makes it win?
--   5. What does DECIMAL(6,2) actually store in SQLite, and where would that
--      diverge from MySQL on money arithmetic?

SELECT name FROM sqlite_master WHERE type='table';
SELECT * FROM lots;
SELECT * FROM buyers;
SELECT * FROM bids;