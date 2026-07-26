# 08 · Supporting skills — what you didn't ask for but need

← [[README]] · Hours: ~40 · Spread across all phases

Your list covers the interview surface well. These are the gaps I'd expect to cost you points — either in the loop itself or in the first six months of the job.

---

## 1. Operating systems (asked directly at Google — genuinely)

Process vs thread (address space, what's shared) · context switching cost · virtual memory, paging, page faults, TLB · stack vs heap · memory allocation and fragmentation · scheduling (preemptive, round robin, CFS, priorities) · IPC (pipes, shared memory, sockets, signals) · syscalls and user/kernel mode · file descriptors, blocking vs non-blocking IO, **select/poll/epoll** (this is *why* async servers work — it comes up in HTTP and design rounds) · zero-copy · mmap · file systems (inodes, journaling) · caching layers in the OS.

Minimum: be able to answer "what happens when your process runs out of memory", "why is a context switch expensive", and "how does an event loop serve 10k connections with one thread".

---

## 2. Python mastery (your primary weapon — sharpen it)

Data model: `__init__`, `__repr__`, `__eq__`/`__hash__`, `__iter__`, `__enter__/__exit__`, `__slots__`, descriptors `[stretch]` · mutable vs immutable and identity vs equality · shallow vs deep copy · generators and lazy evaluation (memory-efficient stream processing — a good answer in design rounds) · comprehensions vs `map`/`filter` · decorators and `functools.wraps` · closures and late binding · context managers · `dataclass`, `Enum`, `NamedTuple`, `Protocol`, `TypedDict` · typing and `mypy` · exceptions and custom hierarchies · `asyncio` properly (event loop, coroutines, `gather`, `TaskGroup`, blocking-call hazard) · GIL and when to use processes · profiling (`cProfile`, `timeit`, `memory_profiler`) · `pytest` (fixtures, parametrize, mocking, coverage) · packaging (`pyproject.toml`, virtualenv, `uv`/`pip`, pinned deps).

Consider learning **Go** or **C++** at reading level `[stretch]` — Google is heavily C++/Java/Go internally, and being able to read a Go snippet in a team match is a small but real edge. Do not switch your interview language.

---

## 3. Git & workflow

Beyond add/commit/push: `rebase -i` vs merge (and when each is right), cherry-pick, `reflog` (the undo button people don't know about), `bisect` (find the breaking commit — great story material), stash, worktrees, `blame`, resolving conflicts calmly, branching models (trunk-based vs GitFlow), writing a good commit message, small reviewable PRs, code review etiquette.

Housekeeping for this repo: your `.gitignore` should cover `__pycache__/`, `*.pyc`, `.idea/`, `.vscode/`, and `.obsidian/workspace.json` — right now there's a tracked `.pyc` and IDE files in the index, and that's the first thing a reviewer sees on your GitHub. Also make the [README.md](../README.md) actually sell the repo: what patterns are covered, how it's organized, how to run the tests.

---

## 4. Infra & cloud fluency

Docker (image vs container, layers, Dockerfile, volumes, networks, compose) · Kubernetes concepts (pod, deployment, service, ingress, configmap/secret, HPA, resource requests/limits, liveness vs readiness probes) — you don't need to run a cluster, you need to speak it · CI/CD (GitHub Actions: build, test, lint, deploy; branch protection) · IaC awareness (Terraform) · Linux CLI (`grep`, `awk`, `sed`, `find`, `xargs`, `ps`, `top`, `df`, `netstat`/`ss`, `curl`, `dig`, `tcpdump` basics, `journalctl`, pipes and redirection) · **GCP mapping**, since this is Google: Compute Engine, GKE, Cloud Run, Cloud Storage, Cloud SQL, Spanner, Bigtable, BigQuery, Pub/Sub, Dataflow, Memorystore, Cloud Load Balancing, Vertex AI. Know which GCP service maps to each building block in [[04-hld]].

---

## 5. Debugging & production sense

A systematic debugging method (reproduce → bisect the space → form a hypothesis → test one variable → verify the fix and *why* it works). Reading stack traces and logs. Profiling before optimizing. Common production failure classes: memory leak, connection-pool exhaustion, N+1 query, unbounded queue, missing timeout, retry storm, clock skew, thread starvation. Writing a **blameless postmortem** (timeline, impact, root cause, contributing factors, action items) — and having lived one is a top-tier behavioural story.

---

## 6. Communication & writing (the most underrated multiplier)

Google runs on written design docs. Practise: a one-page design doc (context, goals, non-goals, proposed design, alternatives considered, risks, rollout plan). Explaining a technical decision to a non-technical stakeholder. Giving code review feedback that isn't personal. Estimating work honestly and communicating slippage early.

Concrete practice: write up each [[04-hld]] problem as a mini design doc, and blog 4 posts over the 24 weeks (a pattern you learned, a paper you read, your RAG project's eval results, a debugging war story). Writing is how you find out you don't actually understand something — and a public trail helps recruiters find you.

---

## 7. Career hygiene (parallel track, ~1 hr/week)

- **Brag document:** a running log of what you shipped with numbers. Update it weekly, forever. It writes your resume, your promo packet, and your story bank ([[07-google-interview-playbook]]).
- GitHub as a portfolio: pinned repos, real READMEs, green-ish activity. This repo + the GenAI project are your two showpieces.
- LinkedIn: headline with keywords, experience in XYZ format, open to recruiters.
- Network before you need it: 2 meaningful professional conversations a month.
- Read one engineering blog a week (Google Research, Cloudflare, Netflix, Discord, Uber, Stripe, Anthropic engineering) — this is where design-round vocabulary comes from cheaply.
- Health and sustainability: this is a 6-month plan; a burnout week costs more than a skipped topic. Deliberately schedule one rest day per week and take it.

---

## 8. Book shortlist (finish 3, don't buy 12)

*Designing Data-Intensive Applications* — Kleppmann (the highest-value technical book on this list) · *Elements of Programming Interviews in Python* — Aziz et al. · *Clean Code* (skim ch. 1–7) / *A Philosophy of Software Design* — Ousterhout (shorter and better) · *Site Reliability Engineering* — Google, free online · *Hands-On Machine Learning* — Géron · *Staff Engineer* — Larson `[stretch, post-offer]`.
