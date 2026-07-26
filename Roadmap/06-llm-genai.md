# 06 · LLMs, transformers, LangChain, GenAI

← [[README]] · Hours: ~55 · Phase 3 (W11–W16), maintained after

Two distinct goals here, and they need different work:
1. **Depth** — explain a transformer at the level of matrix shapes. This is what an interviewer probes.
2. **Evidence** — one shipped project with real evaluation numbers. This is what gets you the interview.

Do both. Skipping (1) makes you a "prompt person"; skipping (2) makes it unverifiable.

---

## 1. Foundations

- **Tokenization:** characters → words → subwords. **BPE** / WordPiece / SentencePiece; vocabulary size tradeoff; why token counts ≠ word counts; why arithmetic and rare names are hard; why non-English text costs more tokens; special tokens (BOS/EOS/pad).
- **Embeddings:** token embedding matrix (`vocab × d_model`), tied input/output embeddings, what "vector space semantics" actually means, cosine similarity.
- **Language modeling objective:** next-token prediction, cross-entropy loss, perplexity, teacher forcing, autoregressive generation. **The core insight to be able to state: everything an LLM does emerges from compressing the training distribution into next-token prediction.**

---

## 2. The transformer — know this at shape level

**Self-attention:**
```
Q = X·W_q    K = X·W_k    V = X·W_v          # X: (seq, d_model), W: (d_model, d_head)
scores = Q·Kᵀ / √d_k                          # (seq, seq)
scores = scores + causal_mask                 # -inf above the diagonal (decoders)
attn   = softmax(scores) · V                  # (seq, d_head)
```
Be able to answer: **why divide by √d_k?** (dot products grow with dimension → softmax saturates → gradients vanish). **Why is it O(n²)?** (the seq×seq score matrix — the reason long context is expensive). **What does the causal mask do?** (prevents attending to the future, so all positions train in parallel).

**Multi-head attention:** h heads of dimension `d_model/h`, concatenated then projected by `W_o`. Why multiple heads: different heads learn different relations (syntax, coreference, position patterns) in different subspaces.

**Positional information:** attention is permutation-invariant, so position must be injected. Sinusoidal (original) → learned absolute → **RoPE** (rotary, the modern default, rotates Q/K by position so attention depends on relative offset, extrapolates better) → ALiBi (linear bias). Know why RoPE won.

**The block:** `x = x + Attn(LN(x))` then `x = x + FFN(LN(x))` — **pre-norm** (stable at depth) vs post-norm (original). FFN = `Linear(d → 4d) → GELU/SwiGLU → Linear(4d → d)`; note ~2/3 of parameters live in the FFN, not attention. Residual stream as the model's "working memory".

**Architecture families:** encoder-only (BERT — bidirectional, masked LM, for classification/embeddings) · decoder-only (GPT/Claude/Llama — causal, generative; today's default) · encoder-decoder (T5, translation, with cross-attention). Be able to say which you'd pick for classification vs generation vs retrieval embeddings.

**Efficiency mechanisms — asked constantly in 2026 interviews:**
- **KV cache:** cache K and V for past tokens so generation is O(n) per token, not O(n²) re-computation. Memory cost = `2 × layers × heads × d_head × seq × batch × bytes` — this, not compute, is what limits your batch size. Then: **MQA/GQA** (share K/V heads to shrink the cache), paged attention (vLLM), sliding-window/local attention, **FlashAttention** (IO-aware tiling — same math, far less HBM traffic), **MoE** (sparse experts: many parameters, few active per token), speculative decoding (small draft model + verification), quantized KV cache.

**Deliverable (do not skip):** work through Karpathy's *Let's build GPT* and implement a small GPT from scratch (~300 lines) that trains on a text file. Nothing else produces this level of understanding per hour spent.

---

## 3. Training pipeline

| Stage | What happens | Key terms |
|---|---|---|
| **Pretraining** | Next-token prediction on trillions of tokens | Data mixture, dedup, curriculum, compute budget, **scaling laws** (Chinchilla-optimal tokens-per-param), loss curves |
| **Continued pretraining** | Domain adaptation | Catastrophic forgetting |
| **SFT / instruction tuning** | Learn to follow instructions from (prompt, response) pairs | Dataset quality > quantity, chat templates |
| **Preference alignment** | Learn human preferences | **RLHF** (reward model → PPO), **DPO** (no reward model, simpler, now common), RLAIF/Constitutional AI, reward hacking |
| **Reasoning training** | RL on verifiable outcomes; long chains of thought | Test-time compute, thinking budgets, self-consistency |
| **Efficient adaptation** | Adapt without full fine-tuning | **LoRA** (low-rank ΔW = BA; rank, alpha, which modules), QLoRA (4-bit base), adapters, prefix tuning |
| **Compression** | Cheaper serving | Quantization (INT8/INT4, GPTQ/AWQ, weight vs activation), distillation, pruning |

**The question you will be asked: "prompt engineering vs RAG vs fine-tuning — pick one."** The correct decision framework: prompting for behaviour/format; **RAG for knowledge** (facts change, need citations, need access control); fine-tuning for **style, format adherence, latency/cost reduction, or a narrow specialized task** — and note fine-tuning does *not* reliably inject new facts. Always: start with prompting, add retrieval, fine-tune last.

---

## 4. Inference & generation

- Decoding: greedy · beam search (why it's bad for open-ended text) · **temperature** (logit scaling) · **top-k** · **top-p/nucleus** · min-p · repetition penalty. Know that temperature 0 ≠ fully deterministic in practice (batching/hardware nondeterminism).
- **Structured output:** JSON mode, schema-constrained decoding, grammars, tool/function-call schemas, retry-on-parse-failure. In production, always validate against a schema (Pydantic) — never trust the parse.
- Latency anatomy: **TTFT** (prefill, compute-bound, parallel) vs **TPOT/inter-token** (decode, memory-bandwidth-bound, sequential). Continuous batching, throughput vs latency tradeoff, streaming responses.
- Context window: what actually fits, cost scaling, "lost in the middle" positional degradation, why longer context isn't free even when it's supported.
- **Cost math you should be able to do live:** tokens in + tokens out × per-token price; caching cuts repeated prefixes dramatically; a 50k-token system prompt on every request at 1 M requests/day is a budget disaster — quantify it.
- Serving stacks: vLLM, TGI, TensorRT-LLM, Ollama/llama.cpp for local; API vs self-host tradeoff (cost, latency, data residency, control, ops burden).

---

## 5. Prompting & context engineering

Zero-shot → few-shot (example selection matters) → **chain-of-thought** → self-consistency (sample n, majority vote) → **ReAct** (reason + act + observe) → reflection/self-critique → plan-and-execute → least-to-most decomposition. Techniques that matter in practice: clear role and task framing, delimiters/XML tags for structure, output format specification, negative examples, decomposition into multiple calls instead of one mega-prompt, and putting instructions *after* long context.

**Context engineering** (the 2026 framing that replaced "prompt engineering"): the job is deciding what goes into the limited window — system instructions, retrieved chunks, tool schemas, conversation history (and how you compact it), scratchpad. Failure modes: context rot from bloated history, contradictory instructions, retrieved noise crowding out signal, tool-schema sprawl.

---

## 6. RAG — build one properly

Pipeline: **ingest → chunk → embed → index → retrieve → rerank → assemble context → generate → cite → evaluate.**

Decisions and their tradeoffs:
- **Chunking:** fixed-size vs recursive-by-structure vs semantic vs parent-document (retrieve small, feed large). Overlap. Preserve headings/metadata. **Bad chunking causes more RAG failures than bad models.**
- **Embeddings:** model choice, dimension, domain fit, max input length, cost, whether asymmetric (query vs document) encoding is needed.
- **Vector store:** FAISS (local), pgvector (you already have SQL — usually the right first answer), Chroma, Pinecone/Weaviate/Qdrant/Milvus. ANN algorithms: **HNSW** (graph, fast, memory-heavy) vs IVF-PQ (compressed). Recall vs latency knobs.
- **Retrieval quality:** **hybrid search** (BM25 keyword + dense vector, fused with RRF) beats pure vector search in most real corpora. Then **reranking with a cross-encoder** — the single highest-ROI upgrade to a mediocre RAG system. Plus: query rewriting/expansion, HyDE, multi-query, metadata filtering, MMR for diversity, recursive/graph retrieval.
- **Generation:** grounding instructions, citation requirements, "say you don't know" behaviour, refusal on insufficient context.
- **Evaluation (this is what makes your project credible):** build a golden set of 50–100 Q/A pairs. Measure **retrieval** (recall@k, MRR, NDCG) separately from **generation** (faithfulness/groundedness, answer relevance, citation accuracy). Tools: RAGAS, or your own LLM-as-judge with a rubric. Track a regression suite across prompt changes.
- **Failure modes to be able to enumerate:** retrieved-but-ignored, not-retrieved (chunking/embedding mismatch), conflicting sources, stale index, no access control on chunks (a real security bug — permissions must be enforced at retrieval, not in the prompt), multi-hop questions single-shot retrieval can't answer, tables and images.

---

## 7. Agents

- Definition worth using: an LLM in a loop with tools and a termination condition. Contrast with a fixed workflow — and know that **most production "agents" should be workflows**; only use an agent loop when the path genuinely can't be predetermined.
- Components: tool/function calling (schemas, descriptions as prompts, error messages as feedback), planning, memory (short-term context, long-term store, summarization/compaction), reflection, termination and step limits.
- **MCP (Model Context Protocol):** the standard for exposing tools/resources to models — servers, tools, resources, transports. Worth hands-on: build one small MCP server.
- Multi-agent: orchestrator–worker, evaluator–optimizer, routing, parallel fan-out; the honest tradeoff — cost and error compounding vs parallel coverage.
- Reliability: sandboxing, tool allowlists, human-in-the-loop for irreversible actions, timeouts, budget caps, retries, deterministic replay/tracing.
- **Security — assume you'll be asked:** prompt injection (direct and *indirect*, via retrieved documents or web pages), the lethal trifecta (private data + untrusted content + external communication), data exfiltration via tool calls, jailbreaks, PII leakage, output sanitization before rendering (markdown image exfil), least-privilege tool credentials.

---

## 8. Frameworks — use them, don't worship them

| Tool | What it actually is | When to use | When not to |
|---|---|---|---|
| **LangChain** | Integrations + chains/LCEL over models, retrievers, tools | Prototyping, when you need 20 connectors | Simple single-call apps — the abstraction costs more than it saves |
| **LangGraph** | Explicit stateful graph: nodes, edges, state, checkpointing, human-in-loop | Multi-step agents where you need control, resumability, and observability | Linear pipelines |
| **LlamaIndex** | Data/ingestion-and-retrieval-centric | Document-heavy RAG, many loaders | Non-RAG apps |
| **LangSmith / Langfuse** | Tracing, evals, prompt versioning, cost tracking | Anything in production | Throwaway scripts |
| Raw SDK (Anthropic/OpenAI) | HTTP + a loop | Most production systems — clearer, fewer surprises | When you'd rewrite 20 connectors |
| Pydantic / instructor | Schema-validated outputs | Always | — |

**Interview stance to have ready:** "I've built with LangChain/LangGraph and I know what they abstract — for a two-call pipeline I use the SDK directly, because the framework's indirection makes debugging and token accounting harder. I reach for LangGraph when I need persistent state, branching, and checkpoint/resume." That answer signals judgement; "I use LangChain because it's the standard" doesn't.

Also know the terrain: vector DBs, orchestration (Airflow/Temporal for durable workflows), guardrail libraries, observability, model gateways/routers, prompt-caching, embeddings services, fine-tuning platforms.

---

## 9. Projects — build 2 of these, ship 1 well

1. **"Chat with my codebase/notes" RAG** — use *this* repo or your Obsidian vault as the corpus. Hybrid retrieval + reranker, citations, a 60-question golden set, measured before/after each change. The eval table is the whole point.
2. **Agentic DSA coach** — an MCP server + agent that reads your `Patterns/` folder, quizzes you from your own "Mistake I made" lines, and schedules spaced repetition. Directly compounds with [[01-dsa]].
3. **nanoGPT from scratch** — trained on your own text, with a writeup of the shapes and the loss curve.
4. **LLM eval harness** — golden set, LLM-as-judge rubric, regression runs in CI, cost/latency dashboard. Unsexy and the most credible of the four.
5. `[stretch]` **Fine-tune with LoRA** on a narrow task; compare against prompting + RAG on the same eval set and report which won and why.

Each project needs: a README with architecture diagram, the eval numbers, cost/latency, and an explicit "what I'd do differently" section. That last section is what interviewers quote back at you.

**Design-round variant to prepare (see [[04-hld]]):** "Design an enterprise RAG platform for 100k employees" — multi-tenancy, per-document ACLs enforced at retrieval, ingestion pipeline with incremental updates, embedding-model version migration, caching, cost controls, evals, PII handling, prompt-injection defence, and observability.

---

## 10. Question bank

**Transformers**
1. Walk me through self-attention with shapes. Why the √d_k?
2. Why is attention O(n²), and what do the modern workarounds actually change?
3. What is the KV cache, how big does it get, and why does that determine batch size?
4. MHA vs MQA vs GQA — what's traded for what?
5. Why do transformers need positional encodings at all? Why RoPE over sinusoidal?
6. Pre-norm vs post-norm; why layer norm rather than batch norm?
7. Encoder-only vs decoder-only vs encoder-decoder: pick one for classification, generation, and embeddings.
8. Where are most of the parameters in a transformer block?
9. What does FlashAttention change — the math or the memory movement?
10. How does MoE give you more parameters without more per-token compute?

**Training & adaptation**
11. Pretraining vs SFT vs RLHF vs DPO — what does each buy?
12. Why is DPO replacing PPO-based RLHF in many pipelines?
13. Explain LoRA in terms of matrix ranks, and why it's so cheap.
14. Fine-tuning vs RAG for "our internal docs changed yesterday"?
15. What are scaling laws, and what did Chinchilla correct?
16. How does quantization affect quality, and where does it break first?
17. What is reward hacking? Give an example.

**Inference & product**
18. Temperature vs top-p — when do you use which?
19. Why is TTFT compute-bound but per-token latency memory-bound?
20. Your app costs $40k/month in tokens. Give five levers, ordered by ROI.
21. How do you guarantee valid JSON output?
22. How do you make an LLM feature fast enough for a 300 ms budget?
23. How do you handle nondeterminism when writing tests for LLM output?

**RAG & agents**
24. Design a RAG system for 10 M internal documents with per-user permissions.
25. Retrieval returns the right chunk and the answer is still wrong. Diagnose.
26. Why does hybrid search usually beat pure vector search?
27. What does a cross-encoder reranker do that the embedding model can't?
28. How do you evaluate RAG without human labels for every query?
29. How do you chunk a 200-page PDF with tables?
30. When should an agent loop be a fixed workflow instead?
31. What is indirect prompt injection, and how do you defend a document-reading agent?
32. How do you stop an agent from spending $500 or deleting a table?
33. What goes in the context window on turn 40 of a long agent run?
34. Would you use LangChain in production? Defend your answer either way.
35. How would you A/B test a change to a prompt in a live product?
