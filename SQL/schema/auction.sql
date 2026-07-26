-- Schema: auction (buyers / lots / bids)
-- Source:  Adhoc/hackerrank_questions.md Q3
-- Dialect: SQLite 3.50  (see SQL/README.md for DECIMAL + DATETIME caveats)

DROP TABLE IF EXISTS bids;
DROP TABLE IF EXISTS lots;
DROP TABLE IF EXISTS buyers;

CREATE TABLE buyers (
    id       INTEGER      PRIMARY KEY,
    username VARCHAR(255) NOT NULL
);

CREATE TABLE lots (
    id             INTEGER      PRIMARY KEY,
    name           VARCHAR(255) NOT NULL,
    starting_price DECIMAL(6,2) NOT NULL,
    bid_step       DECIMAL(6,2) NOT NULL
);

-- Deliberately no primary key -- that absence is the tie-break probe.
CREATE TABLE bids (
    buyer_id INTEGER  NOT NULL REFERENCES buyers(id),
    lot_id   INTEGER  NOT NULL REFERENCES lots(id),
    dt       DATETIME NOT NULL
);


-- ---------------------------------------------------------------- seed data

INSERT INTO buyers (id, username) VALUES
    (1, 'vdanielovitch0'),
    (2, 'shanford1'),
    (3, 'mkrolik2'),
    (4, 'jbeardsell3'),
    (5, 'tnoseworthy4');   -- never bids: exercises anti-join (pattern 14)

INSERT INTO lots (id, name, starting_price, bid_step) VALUES
    (1, '24-Hour All Day Allergy', 2963.05,  29.63),   -- zero bids
    (2, 'Pro-Den Rx',              9375.49, 281.26),
    (3, 'Soapy Hands',              550.86,  16.53),
    (4, 'TISSEEL',                 6601.09,  66.01);

-- Lot 1 gets no bids at all -- the row a plain INNER JOIN silently drops.

-- Lot 3, 3 bids, last by vdanielovitch0
INSERT INTO bids (buyer_id, lot_id, dt) VALUES
    (2, 3, '2026-07-20 09:14:02'),
    (3, 3, '2026-07-21 11:30:45'),
    (1, 3, '2026-07-22 16:05:19');

-- Lot 2, 8 bids, last by shanford1. Rows 3-4 are the same buyer twice in a row.
INSERT INTO bids (buyer_id, lot_id, dt) VALUES
    (1, 2, '2026-07-15 08:02:11'),
    (3, 2, '2026-07-15 08:47:33'),
    (1, 2, '2026-07-16 10:21:07'),
    (1, 2, '2026-07-16 10:22:55'),
    (4, 2, '2026-07-18 13:44:29'),
    (2, 2, '2026-07-19 19:03:50'),
    (3, 2, '2026-07-23 07:55:12'),
    (2, 2, '2026-07-24 21:10:04');

-- Lot 4, 9 bids, last by vdanielovitch0 (also a self-outbid at the end)
INSERT INTO bids (buyer_id, lot_id, dt) VALUES
    (2, 4, '2026-07-10 12:00:00'),
    (4, 4, '2026-07-11 09:31:44'),
    (2, 4, '2026-07-12 14:18:26'),
    (3, 4, '2026-07-13 15:02:09'),
    (4, 4, '2026-07-14 18:40:37'),
    (2, 4, '2026-07-17 11:11:11'),
    (3, 4, '2026-07-20 20:25:58'),
    (1, 4, '2026-07-22 08:09:33'),
    (1, 4, '2026-07-25 17:47:21');


-- ------------------------------------------------------------ expected output
--
-- name                     | starting_price | bid_step | bids | current_price | current_winner
-- 24-Hour All Day Allergy  |        2963.05 |    29.63 |    0 |       2963.05 | NULL
-- Pro-Den Rx               |        9375.49 |   281.26 |    8 |      11625.57 | shanford1
-- Soapy Hands              |         550.86 |    16.53 |    3 |        600.45 | vdanielovitch0
-- TISSEEL                  |        6601.09 |    66.01 |    9 |       7195.18 | vdanielovitch0
--
-- These four rows happen to land clean, but SQLite has no true DECIMAL --
-- DECIMAL(6,2) gets REAL storage, and `SELECT 0.1 + 0.2` returns
-- 0.30000000000000004. Wrap money arithmetic in ROUND(..., 2) by habit.


-- ------------------------------------------------------- optional extra runs
--
-- Tie-break probe: uncomment to give lot 3 two bids at the identical instant.
-- ROW_NUMBER() then picks arbitrarily and the result is non-deterministic --
-- which is the point. bids has no PK and no tie-break column to fall back on.
--
-- INSERT INTO bids (buyer_id, lot_id, dt) VALUES (4, 3, '2026-07-22 16:05:19');
--
-- Index probe: compare EXPLAIN QUERY PLAN before and after.
--
-- CREATE INDEX idx_bids_lot_dt ON bids (lot_id, dt DESC);
