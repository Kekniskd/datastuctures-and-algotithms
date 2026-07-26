# 03 · LLD — object design, patterns, concurrency

← [[README]] · Hours: ~45 · Phase 2 (W5–W10)

LLD shows up three ways: an explicit "design these classes" round, the *code-quality* score inside a coding round, and follow-ups like "now make this thread-safe". Google weights this less than Amazon/Uber do, but code quality is graded in **every** round.

---

## 1. Foundations

**OOP for real:** encapsulation, abstraction, inheritance, polymorphism — plus the parts that actually get discussed: composition vs inheritance (default to composition), interface vs abstract class, coupling/cohesion, Law of Demeter, dependency injection, immutability as a concurrency strategy.

**SOLID — with the failure each one prevents:**

| Principle | One-line test | Smell when violated |
|---|---|---|
| **S**ingle responsibility | One reason to change | "…and" in the class description; 800-line service |
| **O**pen/closed | Extend without editing | `if isinstance(...)` chains, growing switch on type |
| **L**iskov substitution | Subclass honours the contract | `Square extends Rectangle`; subclass throws `NotImplemented` |
| **I**nterface segregation | No client depends on unused methods | Fat interface with 12 methods, half raising errors |
| **D**ependency inversion | Depend on abstractions | `PaymentService` constructs `StripeClient` directly |

Also: DRY vs premature abstraction (rule of three), YAGNI, KISS, composition root, the difference between an entity, a value object, a DTO, and a service.

---

## 2. Design patterns — the ones that come up

**Creational:** Factory Method / Abstract Factory (pluggable families), Builder (many optional params — the Python answer is often keyword args or a dataclass; say so), Singleton (say "and I'd inject it instead, because singletons wreck testability"), Prototype `[stretch]`, Object Pool (connection pools).

**Structural:** Adapter (wrap a third-party API), Decorator (layered behaviour — Python `@decorator`, retry/logging/caching wrappers), Facade (simplify a subsystem), Proxy (lazy load, access control, remote), Composite (trees: file systems, UI, org charts), Bridge `[stretch]`, Flyweight `[stretch]`.

**Behavioural:** **Strategy** (interchangeable algorithms — the single most useful pattern in interviews: pricing rules, eviction policies, matching), **Observer** (event/pub-sub, notifications), **State** (elevator, order lifecycle, vending machine), Command (undo, job queues), Template Method, Chain of Responsibility (middleware, approval chains), Iterator, Mediator, Memento, Visitor `[stretch]`.

**Architectural/concurrency patterns worth naming:** Repository, Unit of Work, MVC/MVVM, CQRS, Event Sourcing, Producer–Consumer, Thread Pool, Read-Write Lock, Circuit Breaker, Retry with exponential backoff + jitter, Bulkhead, Rate Limiter (token bucket), Sidecar.

Rule: **never name a pattern you can't implement in 15 lines.** Interviewers probe. Implement each one in this repo once — a `Patterns/` folder of 20 small Python files is a strong artifact.

---

## 3. Concurrency (the most common LLD follow-up)

- Process vs thread vs coroutine; when each is the right tool.
- Race conditions, critical sections, mutex, semaphore, condition variable, monitor, barrier, latch.
- Deadlock: the four Coffman conditions; prevention (lock ordering, timeouts, try-lock), detection, livelock, starvation, priority inversion.
- Atomics, CAS, memory visibility, lock-free vs blocking queues.
- Thread pools: sizing (CPU-bound ≈ cores; IO-bound ≈ much higher), queue policy, rejection, graceful shutdown.
- **Python specifics:** the GIL (threads help IO-bound, not CPU-bound), `threading.Lock/RLock/Condition/Semaphore`, `queue.Queue` (thread-safe), `concurrent.futures` (`ThreadPoolExecutor` vs `ProcessPoolExecutor`), `multiprocessing`, `asyncio` (event loop, `await`, `gather`, `TaskGroup`, why one blocking call stalls everything), free-threaded/no-GIL builds as the direction of travel. Be ready for: "your LRU cache is used by 100 threads — make it safe" (lock around get+move, or per-shard locks, and discuss contention).
- Idempotency, at-most-once vs at-least-once, and optimistic (version/CAS) vs pessimistic locking — these bridge directly into [[04-hld]].

---

## 4. The LLD interview process (45 min)

1. **Clarify scope** (5 min): which flows are in scope, single-machine or distributed, scale, read/write mix. Explicitly park what's out of scope.
2. **Nail down use cases / actors** (3 min): list them as bullet points, get agreement.
3. **Core entities + relationships** (7 min): classes, fields, cardinality. Draw it.
4. **Interfaces / APIs** (7 min): method signatures with types, return values, error cases. This is where seniority shows.
5. **State machine** if there is one (order, booking, elevator) — states + transitions + illegal transitions.
6. **Walk one end-to-end flow through your classes** (5 min): "user books a seat → `BookingService.reserve()` → `SeatLock` → `PaymentGateway` → `Booking` created". Prove the design works.
7. **Concurrency + failure modes** (5 min): double booking, partial payment, retries, cache staleness.
8. **Extensibility** (3 min): "if we added surge pricing, only `PricingStrategy` changes."
9. **Testing** (2 min): what you'd unit test, what you'd fake/mock.

Two habits that separate strong candidates: **say the invariant out loud** ("no two bookings for the same seat ever exist") and **name the pattern with a reason** ("Strategy here so a new pricing rule is a new class, not an `if`").

---

## 5. Problem list — implement these, don't just read them

Tier 1 (do all 6, with tests, committed to this repo):
1. **LRU cache** — O(1) get/put, dict + doubly-linked list, then thread-safe.
2. **Rate limiter** — token bucket, leaky bucket, fixed vs sliding window; per-user; then distributed (bridges to [[04-hld]]).
3. **Parking lot** — the canonical one: spot types, pricing strategy, ticketing, concurrency on allocation.
4. **Elevator system** — state machine, scheduling strategy (SCAN/look), multi-car dispatch.
5. **In-memory key-value store with TTL** — expiry (lazy + background sweep), eviction policy as a Strategy, optional persistence.
6. **Tic-tac-toe / Chess board** — clean board abstraction, move validation, undo via Command.

Tier 2 (design on paper, implement 3):
7. Splitwise / expense sharing (settlement algorithm)
8. BookMyShow / ticket booking (seat locking, expiry, payment)
9. Notification service (channels via Strategy, templates, retries, preference rules)
10. Logging framework (levels, appenders, async buffer, rotation)
11. Vending machine / ATM (State pattern, cash dispensing as coin-change)
12. File system representation (Composite, path resolution, `find` traversal)
13. Job scheduler / cron (priority queue, delays, retries, at-least-once)
14. Snake & ladder, Deck of cards, Library management (fast warm-ups)

Tier 3 `[stretch]`: connection pool, circuit breaker, dependency-injection container, pub-sub broker, undo/redo text editor, calendar with recurring events (RRULE), URL shortener LLD, food delivery / cab booking domain model.

---

## 6. Clean code + testing (graded silently in every round)

- Names: intention-revealing, no `data`/`temp`/`obj`. Functions do one thing, ≤20 lines, ≤3 params.
- Guard clauses over nesting. No magic numbers. Errors: raise specific exceptions, never swallow, fail fast at boundaries.
- Type hints everywhere (`dataclass`, `Enum`, `Protocol`, `Optional`) — cheap, and reads as senior in Python.
- Testing: unit vs integration vs e2e; the test pyramid; AAA structure; one assert-concept per test; fakes vs mocks vs stubs; `pytest` fixtures and `parametrize`; edge-case-first thinking; property-based testing with `hypothesis` `[stretch]`; what *not* to test.
- Refactoring vocabulary: extract method/class, replace conditional with polymorphism, introduce parameter object, guard clause, strangler fig for legacy.
- Code review: what you look for, how you give feedback — this is a real Google interview question, and it's also part of Googlyness ([[07-google-interview-playbook]]).
