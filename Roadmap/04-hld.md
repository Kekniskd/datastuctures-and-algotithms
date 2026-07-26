# 04 · HLD — distributed systems, queues, databases

← [[README]] · Hours: ~70 · Phase 3 (W11–W16), maintained through Phase 5

Your stated goal: *"I should be able to answer all the questions."* That means depth-on-demand, not a memorized script. The structure below is built for that: a framework, the numbers, the building blocks, then 25 problems and a 60-question rapid-fire bank.

Google note: Google invented much of this field. Citing the actual papers (§8) with a real understanding is a differentiator here that it isn't elsewhere. Also expect **Spanner-style strong consistency** and **Borg/K8s-style scheduling** to be fair game.

---

## 1. The 45-minute framework

| Min | Step | Output | Common failure |
|---|---|---|---|
| 0–5 | **Requirements** | Functional list (3–5 core flows), non-functional (scale, latency SLO, consistency, availability), explicit out-of-scope | Starting to draw boxes immediately |
| 5–9 | **Back-of-envelope** | DAU → QPS (avg + peak), read:write ratio, storage/yr, bandwidth, cache size | Made-up numbers with no derivation |
| 9–13 | **API + data model** | 4–6 endpoints with signatures; tables/collections with keys and indexes; **the partition key** | Skipping the schema — this is where deep-dives come from |
| 13–25 | **High-level design** | Boxes and arrows: client → LB → services → cache → DB → queue → workers. Trace one write and one read | Drawing 20 boxes and explaining none |
| 25–38 | **Deep dive (2 areas)** | Let the interviewer pick, or offer: "the hot-partition problem, or the fan-out?" | Staying shallow everywhere |
| 38–43 | **Bottlenecks & failure** | Single points of failure, hot keys, thundering herd, cascading failure, backpressure, what happens when component X dies | Assuming everything works |
| 43–45 | **Tradeoffs + wrap** | "I chose X over Y because ___; if the requirement changed to ___, I'd switch" | No explicit tradeoff statement |

Say these out loud during the round — they're scored: *consistency vs availability choice and why*, *the partition key and its hot-key risk*, *what's cached and how it's invalidated*, *what's async and why*, *how it degrades under 10× load*, *how you'd monitor it*.

---

## 2. Numbers to memorize

**Latency (order of magnitude — the point is the ratios):**

| Operation | ~Time |
|---|---|
| L1 cache reference | 1 ns |
| Main memory reference | 100 ns |
| Read 1 MB sequentially from memory | ~10 µs |
| SSD random read | ~100 µs |
| Read 1 MB from SSD | ~200 µs–1 ms |
| Datacenter round trip | ~0.5 ms |
| Disk (HDD) seek | ~10 ms |
| Read 1 MB from HDD | ~20 ms |
| CA → Netherlands round trip | ~150 ms |

Derived intuitions: memory is ~100× faster than SSD, ~10,000× faster than a disk seek. Cross-region is ~100× a datacenter hop → chatty cross-region calls are fatal. A single sequential 1 MB memory read beats an SSD random read by ~10×.

**Capacity rules of thumb:** 1 M writes/day ≈ 12 writes/s. 100 M DAU × 10 requests/day ≈ 11.5 k QPS avg, peak ≈ 2–3× ≈ 30 k QPS. 1 KB × 1 B rows = 1 TB. A commodity SQL node: ~1–5 k writes/s, ~10–50 k reads/s with replicas. Redis: ~100 k ops/s/node. Kafka: ~100 k–1 M msgs/s/cluster. One app server: ~1–10 k QPS depending on work. Rule: seconds in a day ≈ 86,400 ≈ **10⁵**; use that for every division.

---

## 3. Building blocks

### Load balancing & routing
L4 vs L7; round robin / least connections / consistent hashing / power-of-two-choices; health checks; connection draining; sticky sessions (and why to avoid them); global LB (DNS, Anycast, Maglev); service discovery; sidecar/service mesh; API gateway responsibilities.

### Caching
- **Where:** client, CDN, API gateway, application (in-process), distributed (Redis/Memcached), DB buffer pool, materialized views.
- **Patterns:** cache-aside (most common), read-through, write-through, write-back, write-around, refresh-ahead.
- **Eviction:** LRU, LFU, FIFO, TTL, random. Know the LRU implementation ([[03-lld]]).
- **Failure modes and fixes — these are the deep-dive questions:** cache stampede/thundering herd (request coalescing, probabilistic early expiry, locks), hot key (replicate the key, local L1 cache, jittered TTL), cache penetration (negative caching, Bloom filter), consistency (TTL vs explicit invalidation vs versioned keys vs CDC), cold start, cache-warming.
- **Consistent hashing:** ring, virtual nodes, why plain `hash % N` collapses on resize, rebalancing cost.

### Databases
> Query-level SQL (joins, window functions, `EXPLAIN`, index selection) lives in [[10-sql]]. This section is the storage-engine and distribution layer.

- **Relational:** normalization vs denormalization, joins, **B+tree indexes** (structure, why depth ~3–4, covering index, composite index column order, index-only scan, write amplification), query planning, connection pooling.
- **ACID + isolation levels:** read uncommitted → read committed → repeatable read → serializable; the anomalies (dirty read, non-repeatable read, phantom, write skew, lost update); **MVCC** and snapshot isolation; 2PL; deadlock detection; optimistic vs pessimistic locking.
- **NoSQL families:** key-value (DynamoDB, Redis), wide-column (Bigtable, Cassandra — **LSM tree**: memtable → WAL → SSTables → compaction, why writes are fast and reads need Bloom filters), document (MongoDB), graph (Neo4j), time-series (Monarch, Prometheus), search (Elasticsearch: inverted index, tokenization, relevance/BM25).
- **B+tree vs LSM:** read-optimized/in-place vs write-optimized/append + compaction; read amp vs write amp vs space amp. Be able to say which you'd pick for a feed store vs a ledger.
- **Scaling:** vertical → read replicas (replication lag, read-your-writes) → **sharding** (range vs hash vs directory vs geo; hot shards; resharding; cross-shard joins and transactions; the partition-key decision is *the* design decision) → federation → CQRS + materialized read models.
- **Replication:** single-leader, multi-leader (conflict resolution: LWW, vector clocks, CRDTs), leaderless/quorum (Dynamo-style: `R + W > N`), sync vs async vs semi-sync, failover and split-brain, WAL shipping, change data capture.
- **Distributed transactions:** 2PC (and its blocking coordinator problem), 3PC, **saga** (orchestration vs choreography, compensating actions), **transactional outbox**, TCC, Spanner's TrueTime + Paxos for external consistency, Percolator-style snapshot isolation.

### Queues & streaming (you called this out — go deep)
- **Why async at all:** decoupling, load levelling/buffering, retries, fan-out, batching, temporal decoupling.
- **Kafka model:** topic → partitions → offsets, ordered *within a partition only*, consumer groups + rebalancing, retention (time/size/compacted), replication factor, ISR, leader per partition, exactly-once semantics via idempotent producer + transactions, `min.insync.replicas` vs `acks`.
- **Broker comparison:** Kafka (log, high throughput, replay, streams) · RabbitMQ (AMQP broker, routing/exchanges, per-message ack, priority) · SQS (managed, at-least-once, visibility timeout; FIFO variant) · Pub/Sub (Google's, push/pull, global) · Redis Streams (light) · Beam/Dataflow, Flink, Spark Streaming for processing.
- **Delivery semantics:** at-most-once, at-least-once, effectively/exactly-once. **The key insight to state in an interview: exactly-once end-to-end is achieved with at-least-once delivery + idempotent consumers**, not by magic in the broker.
- **Consumer concerns:** idempotency keys / dedup store, ordering (partition by entity ID), poison messages → retry with backoff → **dead-letter queue**, consumer lag as the #1 metric, backpressure, batch size vs latency, long-running work with heartbeats/visibility extension, priority queues, delayed/scheduled messages.
- **Patterns:** work queue, pub-sub fan-out, event sourcing, CQRS, event-carried state transfer vs thin events, outbox, choreographed sagas, stream joins, windowing (tumbling/sliding/session) + watermarks for late data, exactly-once sinks.

### Consensus & coordination
CAP (and why "CP vs AP" is only about behaviour during a partition), **PACELC** (else-latency-vs-consistency — the more useful model), consistency spectrum (linearizable → sequential → causal → read-your-writes → monotonic reads → eventual), quorums, **Raft** (leader election, log replication, terms, safety) vs Paxos/Multi-Paxos, ZooKeeper/etcd/Chubby (locks, leader election, config, watches), leases and fencing tokens (why a distributed lock needs a fencing token), clock skew, logical/Lamport clocks, vector clocks, gossip, failure detection (heartbeats, phi-accrual), split-brain.

### Reliability & operations
Idempotency, retries with **exponential backoff + jitter** (and retry budgets/amplification), timeouts everywhere, **circuit breaker**, bulkhead, load shedding, graceful degradation, rate limiting (token bucket, leaky bucket, fixed window, sliding window log/counter — and the distributed version with Redis), request hedging, autoscaling (and why it's too slow for a spike), capacity planning, multi-region (active-active vs active-passive, failover, data residency), disaster recovery (RTO/RPO, backups vs replicas, restore testing), chaos engineering.

### Observability
Metrics vs logs vs traces (the three pillars) + events; RED (rate/errors/duration) and USE (utilization/saturation/errors) methods; **p50/p95/p99/p99.9 — and why averages lie**; distributed tracing (Dapper lineage: spans, trace context propagation, sampling); structured logging; cardinality problems; SLI → SLO → **error budget** → alerting on symptoms not causes; on-call, runbooks, blameless postmortems.

### Delivery
Blue-green, canary, rolling, feature flags, dark launching, shadow traffic, DB migrations without downtime (expand-migrate-contract, dual writes, backfill), schema evolution/compatibility, rollback strategy.

---

## 4. Design problem set (25)

Do them in this order; write each one up in one page.

**Tier 1 — core vocabulary**
1. URL shortener (ID generation: hash vs counter vs Snowflake, custom aliases, redirect 301 vs 302, analytics)
2. Pastebin / file-sharing (object storage, presigned URLs, TTL)
3. Rate limiter, distributed (Redis token bucket, sync across nodes, fail-open vs fail-closed)
4. Web crawler (frontier, politeness, dedup via Bloom filter, DNS caching, traps, distributed workers)
5. Key-value store (partitioning, replication, quorum, gossip, anti-entropy, Merkle trees)

**Tier 2 — the classics**
6. Twitter/X timeline (fan-out on write vs read, celebrity problem, hybrid, feed cache)
7. Instagram (media pipeline, CDN, thumbnails, followers graph)
8. WhatsApp/chat (WebSocket gateways, presence, delivery receipts, offline queue, ordering, E2E encryption)
9. Notification system (multi-channel, templates, preferences, dedup, throttling, priority)
10. News feed ranking (candidate generation → ranking → re-rank; bridges to [[05-ai-ml-basics]])
11. YouTube/Netflix (upload → transcode pipeline, ABR streaming/HLS, CDN economics, recommendations)
12. Google Drive / Dropbox (chunking, dedup, delta sync, conflict resolution, metadata DB)
13. Uber/Lyft (geospatial indexing: geohash/S2/QuadTree, matching, real-time location, surge)
14. Ticketmaster/BookMyShow (seat locking, inventory correctness, flash-sale surge, queueing)
15. Payment system (idempotency, ledger with double-entry, exactly-once, reconciliation, PCI scope)

**Tier 3 — Google-flavoured / harder**
16. Google Search (crawl → index → serve; inverted index, sharding by document, query fan-out, ranking, caching)
17. Google Docs (collaborative editing: OT vs CRDT, presence, cursor sync, versioning)
18. Google Maps (map tiles, routing graph + contraction hierarchies, ETA with traffic)
19. Distributed job scheduler / cron at scale (leader election, at-least-once fire, dedup, backfill)
20. Distributed cache (like Memcached at scale: consistent hashing, client-side routing, hot keys)
21. Metrics/monitoring system (Monarch/Prometheus-style: ingest, downsampling, TSDB, cardinality, query)
22. Log aggregation & search pipeline (ingest → buffer → index → retention tiers)
23. Ad click aggregation (stream processing, exactly-once counting, late events, watermarks, fraud)
24. Autocomplete / typeahead (trie shards, top-K per prefix, real-time updates, personalization)
25. Authorization service (Zanzibar-style relationship tuples, consistency vs latency, caching with zookies)

**Also prepare the ML-systems variant** (see [[05-ai-ml-basics]] §6) and the **GenAI variant** (RAG/LLM serving platform — see [[06-llm-genai]] §9). In 2026 loops, "design a RAG system for internal docs" is a live question.

---

## 5. Written deliverable per problem

One page, same shape every time — this becomes your revision deck:
`Requirements` · `Scale math` · `API` · `Schema + partition key` · `Diagram (ASCII is fine)` · `2 deep dives` · `Failure modes` · `Tradeoffs & what I'd change at 10×`.

---

## 6. Anti-patterns

Naming technologies instead of properties ("I'd use Kafka" before "I need durable ordered replay"); no scale math; ignoring the write path; never mentioning consistency; designing for infinite scale on day one; forgetting monitoring/ops; monologuing for 20 minutes without checking in; and drawing a single DB box with no partition key.

---

## 7. Books & courses

*Designing Data-Intensive Applications* (Kleppmann) — read ch. 1–9 properly, it covers 70% of this file. Then MIT 6.824 lectures (free) for consensus, and *Database Internals* (Petrov) for B+tree/LSM depth. ByteByteGo/Alex Xu vol. 1–2 for problem-shaped practice. Skim, don't collect.

## 8. Google papers (read 10 of these — 1/week in Phases 3–4)

| Paper | What it teaches | Why for Google |
|---|---|---|
| MapReduce (2004) | Batch parallelism, fault tolerance via re-execution | The founding abstraction |
| GFS (2003) / Colossus | Chunked distributed FS, single-master metadata | Storage layer thinking |
| Bigtable (2006) | Wide-column, SSTables, tablets, LSM | Cassandra/HBase ancestor |
| Chubby (2006) | Lock service, Paxos in practice, leases | Why coordination services exist |
| Spanner (2012) | TrueTime, external consistency, Paxos groups | Breaks the "you can't have both" assumption |
| Percolator (2010) | Distributed transactions over Bigtable | Snapshot isolation at scale |
| Dremel (2010) | Columnar + tree execution → BigQuery | Analytics architecture |
| Borg (2015) | Cluster scheduling, bin packing, priorities | K8s's parent; scheduling questions |
| Dapper (2010) | Distributed tracing, sampling | Observability answers |
| Monarch (2020) | In-memory global TSDB | Monitoring design problem |
| Maglev (2016) | Software LB, consistent hashing | Load balancer depth |
| MillWheel / Dataflow (2013/15) | Stream processing, watermarks, exactly-once | Every streaming question |
| Zanzibar (2019) | Global authorization, zookies | Auth design problem |
| The Tail at Scale (2013) | p99 latency, hedged requests | Latency reasoning |
| Site Reliability Engineering (book, free) | SLO/error budget culture | Googlyness + ops answers |

For each: write 5 bullets — problem, key idea, tradeoff, what it replaced, where you'd cite it in a design round.

---

## 9. Rapid-fire bank — 60 questions (target: 60 s each)

**Fundamentals**
1. CAP: what does "choosing C" actually mean for a client during a partition?
2. Why is PACELC a better model than CAP?
3. Linearizable vs sequential vs causal consistency — give an observable difference.
4. What breaks when you have read replicas and a user updates their profile?
5. Quorum with N=5: which (R,W) pairs give strong consistency, and what's the availability cost?
6. Why does a distributed lock need a fencing token?
7. Two nodes both think they're leader. How did that happen and how do you prevent it?
8. Explain Raft leader election in 60 seconds.
9. Why can't you just use timestamps to order events across machines?
10. What does Spanner's TrueTime actually buy you?

**Databases**
11. When would you pick LSM over B+tree? Give the write/read amplification tradeoff.
12. Composite index `(a, b, c)` — which queries can use it and which can't?
13. Repeatable read vs snapshot isolation — what's write skew?
14. You need a monotonically increasing global ID at 100 k/s. Options and tradeoffs?
15. Your shard key is `user_id` and one user is 5% of traffic. Fix it.
16. How do you do a zero-downtime column type change on a 500 GB table?
17. Sync vs async replication: what do you lose in a failover with each?
18. When is denormalization the right call, and what's the cost?
19. How do you implement pagination over a sharded dataset?
20. Cross-shard transaction — 2PC vs saga: pick one and defend it.

**Caching**
21. Cache-aside vs write-through: which gives stale reads and when?
22. A popular key expires and 50 k requests hit the DB at once. Three fixes.
23. How do you invalidate a cache when the DB is updated by another service?
24. Why do virtual nodes exist in consistent hashing?
25. Redis as a cache vs as a database — what changes?

**Queues**
26. Guarantee ordering of a user's events across a partitioned topic. How?
27. Explain exactly-once processing without hand-waving.
28. Consumer lag is growing linearly. Diagnose it — 5 possible causes.
29. What is the transactional outbox pattern solving?
30. A message keeps failing forever. Design the full retry/DLQ policy.
31. Kafka vs SQS vs RabbitMQ for: audit log replay, task fan-out, order-processing workflow.
32. Your consumer crashes after side-effect but before ack. What happens, and how do you make that safe?
33. How do watermarks handle events that arrive 3 hours late?
34. Push vs pull consumption — tradeoffs.
35. How do you implement a delayed message (deliver in 24h) on a system that has no delay feature?

**Scale & reliability**
36. Estimate storage for 500 M users × 200 photos × 2 MB, with 3× replication.
37. Compute peak QPS for 50 M DAU making 20 requests/day, and size the fleet.
38. Everything retries on failure and the outage gets worse. Name the effect and the fixes.
39. Design a global rate limiter accurate to ±5% at 1 M req/s.
40. p99 is 2 s while p50 is 40 ms. Walk the diagnosis.
41. What is a hedged request and when does it hurt?
42. Circuit breaker: states, thresholds, and what you return when open.
43. How do you shed load gracefully instead of falling over?
44. Blue-green vs canary — when is canary mandatory?
45. Define SLI/SLO/error budget and how the budget changes a release decision.
46. Single-region → multi-region active-active: what are the three hardest problems?
47. RTO vs RPO; how do they drive your backup architecture?
48. How do you test that your backups actually restore?
49. A downstream dependency is 10× slower. How does your service behave, ideally?
50. What's the thundering-herd risk in autoscaling and in cache warming?

**Design judgement**
51. When is eventual consistency unacceptable? Give two concrete features.
52. Fan-out on write vs read for a feed: pick and justify, then handle celebrities.
53. Geospatial "find drivers within 2 km" — geohash vs S2 vs quadtree.
54. Idempotency for a payment API — design the key, the store, and the TTL.
55. When would you *not* use microservices?
56. How do you migrate from a monolith DB to a service-owned DB with no downtime?
57. Design search-as-you-type for 1 B queries/day.
58. Store 10 years of metrics at 1-second resolution without going bankrupt.
59. Cheapest correct way to count unique daily visitors at 1 B events/day? (HyperLogLog — know the error bound)
60. Where would you put a Bloom filter in a system you've designed, and what's the failure mode?
