# 02 · HTTP & Internet fundamentals

← [[README]] · Hours: ~35 · Phase 1 (W1–W4)

This is the cheapest track to get to *interview-proof* depth, and it's load-bearing for [[04-hld]]. Feed it into one deliverable: **be able to draw the full "type a URL and press Enter" path from memory in 10 minutes.**

---

## 1. The stack under HTTP

- **Layers:** physical → link (Ethernet/WiFi, MAC, ARP) → network (IP, routing, NAT, ICMP) → transport (TCP, UDP) → application (HTTP, DNS, TLS sits between).
- **IP:** IPv4 vs IPv6, CIDR notation, private ranges, public vs private, NAT, why `10.0.0.0/8` matters in cloud VPCs.
- **TCP:** 3-way handshake (SYN, SYN-ACK, ACK), sequence numbers, ACKs, retransmission, sliding window, flow control vs **congestion control** (slow start, AIMD, cwnd), Nagle's algorithm, head-of-line blocking, TIME_WAIT, connection teardown (FIN), keep-alive.
- **UDP:** no handshake/ordering/retransmit → used by DNS, QUIC, video, gaming. When you'd choose it.
- **DNS:** recursive resolver → root → TLD → authoritative. Record types (A, AAAA, CNAME, MX, TXT, NS, SRV), TTL and caching layers (browser → OS → resolver), negative caching, DNS-based load balancing and its limits (TTL staleness), Anycast, GeoDNS, DoH/DoT.
- **TLS 1.3 handshake:** ClientHello (+ key share) → ServerHello + cert → Finished. 1-RTT, 0-RTT resumption. Certificate chain, CA trust, SNI, ALPN, forward secrecy (ECDHE), symmetric vs asymmetric split (asymmetric to agree a key, symmetric for the data). Know why TLS 1.3 is 1-RTT while 1.2 was 2-RTT.

---

## 2. HTTP versions

| | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---|---|---|---|
| Transport | TCP | TCP | **QUIC over UDP** |
| Multiplexing | No — 1 request/connection at a time (pipelining unusable) | Yes, streams over one connection | Yes |
| Head-of-line blocking | Application level | Removed at app level, **remains at TCP level** | Removed entirely (per-stream loss recovery) |
| Headers | Plain text, repeated | Binary + HPACK compression | QPACK |
| Push | No | Server push (deprecated in practice) | — |
| Handshake | TCP + TLS separately | TCP + TLS | Combined, 0–1 RTT |
| Workarounds it kills | domain sharding, sprite sheets, concat | — | — |

Also: connection keep-alive, browser's ~6 connections per host limit in H1, why H2 made sharding an anti-pattern.

---

## 3. HTTP semantics

- **Methods:** GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS. Two properties that get asked constantly:
  - **Safe** (no side effects): GET, HEAD, OPTIONS.
  - **Idempotent** (same result if repeated): GET, HEAD, PUT, DELETE, OPTIONS — **not** POST, **not** PATCH (in general).
  - Why it matters: retries, load-balancer replays, at-least-once delivery ([[04-hld]]).
- **Status codes** — know the semantics, not the list: 200/201/202/204 · 301 vs 302 vs 307/308 (method preservation!) · 304 · 400/401 vs 403/404/405/409/410/415/**422**/429 · 500/502/503/504. Know exactly when to use 401 vs 403 and 409 vs 422.
- **Headers worth knowing by heart:** `Host`, `Content-Type`, `Accept`, `Authorization`, `Cookie`/`Set-Cookie`, `Cache-Control`, `ETag`/`If-None-Match`, `Last-Modified`/`If-Modified-Since`, `Vary`, `Content-Encoding` (gzip/br), `Transfer-Encoding: chunked`, `Location`, `Retry-After`, `X-Forwarded-For`, `Strict-Transport-Security`, `Content-Security-Policy`.
- **Caching:** `Cache-Control: no-store` vs `no-cache` vs `private` vs `public, max-age=…, s-maxage=…, stale-while-revalidate`. Strong vs weak validators. Cache hierarchy: browser → CDN → reverse proxy → app cache. Cache busting via content-hash filenames. **Know `no-cache` ≠ don't cache** (it means revalidate) — a classic gotcha.
- **Content negotiation, ranges** (`Range`, 206 — resumable downloads), compression tradeoffs, chunked transfer + streaming responses.

---

## 4. Identity: cookies, sessions, tokens

**Cookies** — attributes are the whole interview:

| Attribute | Effect | Interview point |
|---|---|---|
| `HttpOnly` | JS can't read it | Mitigates XSS token theft |
| `Secure` | HTTPS only | Prevents plaintext leak |
| `SameSite=Strict/Lax/None` | Cross-site send rules | Primary CSRF defence; `None` requires `Secure` |
| `Domain` / `Path` | Scope | Subdomain leakage risk |
| `Max-Age` / `Expires` | Session vs persistent | — |
| `__Host-` prefix | Locks to host, no domain | Hardening |

**Server-side sessions:** session ID in cookie → server-side store. Pros: instant revocation, small cookie, opaque. Cons: stateful → needs sticky sessions or a shared store (Redis) → the store becomes a scaling and availability dependency. Session fixation and rotation-on-login.

**JWT:** `header.payload.signature`, base64url — **encoded, not encrypted** (JWE if you need encryption). Claims: `iss, sub, aud, exp, nbf, iat, jti`. Algorithms: HS256 (shared secret) vs RS256/ES256 (private signs, public verifies → good for multi-service). Known attacks: `alg: none`, algorithm confusion (RS256→HS256 with the public key as HMAC secret), missing `aud`/`exp` validation, weak secret.

**The JWT question you will get: "how do you revoke one?"** Correct answer covers: you fundamentally can't with a stateless token, so — short TTL (5–15 min) access token + long-lived refresh token in an `HttpOnly` cookie, refresh-token rotation with reuse detection, a denylist keyed on `jti` (which reintroduces state, but only for the small revoked set), or a `token_version` claim checked against the user record. Then state the tradeoff explicitly: stateless scale vs revocation latency.

**Session vs JWT — the honest comparison:**

| | Session cookie | JWT |
|---|---|---|
| State | Server-side | Client-side |
| Revocation | Immediate | Hard (needs TTL or denylist) |
| Scale | Shared store required | Verify locally, no lookup |
| Payload size | ~32 bytes | 200 B–1 KB on every request |
| Mobile/multi-service | Awkward | Natural |
| Default recommendation | Browser-only monolith → sessions | Multi-service/mobile → short JWT + refresh |

**Auth protocols:**
- **OAuth 2.0** — *authorization*, not authentication. Roles: resource owner, client, auth server, resource server. Flows: **Authorization Code + PKCE** (the only right answer for web/SPA/mobile today), Client Credentials (service-to-service), Device Code (TVs/CLI); Implicit and Password grants are deprecated — know *why* (token in URL fragment; credential handling).
- **OIDC** — the identity layer on top of OAuth2: adds `id_token` (a JWT), `nonce`, userinfo endpoint, discovery document, JWKS endpoint for key rotation.
- **SAML** — XML, enterprise SSO, IdP/SP, assertions, redirect/POST bindings. Know it exists and why enterprises still use it.
- Others: API keys (and why they're weak), HMAC request signing (AWS SigV4 style), **mTLS** (service mesh), opaque tokens + introspection.

---

## 5. API styles

- **REST:** resources not verbs, plural nouns, correct status codes, HATEOAS (Richardson maturity model — know that level 3 is rare in practice). Real-world design: pagination (offset vs **cursor/keyset** — know why offset breaks at scale), filtering/sorting conventions, versioning (URL path vs header vs media type), partial responses, bulk endpoints, **idempotency keys** for POST, error envelope design (RFC 7807 problem+json), rate-limit headers, long-running jobs via 202 + polling/callback.
- **SOAP:** XML envelope (Header/Body/Fault), WSDL contract, XSD schemas, WS-Security, WS-* stack, strict typing, built-in transactions/reliable messaging. Where it survives: banking, insurance, telecom, government, legacy enterprise. Interview answer for "REST vs SOAP": SOAP = protocol with a formal contract and built-in security/transaction standards, transport-agnostic, verbose; REST = architectural style over HTTP, lightweight, cacheable, human-debuggable. Choose SOAP when a formal contract, WS-Security, or an existing enterprise integration demands it.
- **GraphQL:** single endpoint, client-specified queries, schema/SDL, resolvers, over/under-fetching solved — new problems: N+1 (DataLoader), query-cost limiting, caching is hard, no HTTP caching for free.
- **gRPC:** HTTP/2 + Protobuf, IDL-first, codegen, 4 modes (unary, server/client/bidi streaming), deadlines, interceptors, backward-compatible schema evolution rules (never reuse field numbers). Google's internal default → **know this one properly for a Google interview.**
- **Realtime:** short polling → long polling → **SSE** (one-way, HTTP, auto-reconnect, `Last-Event-ID`) → **WebSocket** (bidirectional, `Upgrade` handshake, sticky/stateful, scaling with a pub-sub backplane). Plus **webhooks** (server→server callbacks: signature verification, retries with backoff, idempotency, replay protection).

Decision table you should be able to reproduce: public API → REST; internal high-throughput microservices → gRPC; aggregating many backends for a flexible mobile client → GraphQL; server→client stream → SSE; chat/collab → WebSocket.

---

## 6. Web security (assume you'll be asked at least two of these)

| Attack | Mechanism | Defence |
|---|---|---|
| XSS (stored/reflected/DOM) | Injected script runs in your origin | Output encoding, CSP, `HttpOnly`, framework auto-escaping, avoid `innerHTML` |
| CSRF | Browser auto-sends cookies cross-site | `SameSite`, CSRF tokens, double-submit, check `Origin` |
| SQL injection | String-concatenated queries | Parameterized queries, least-privilege DB user |
| SSRF | Server fetches attacker-controlled URL | Allowlist, block link-local `169.254.169.254`, no redirects |
| Clickjacking | Invisible iframe | `X-Frame-Options` / CSP `frame-ancestors` |
| Insecure direct object reference | `/api/orders/123` with no ownership check | Authorization on every object access |
| Replay | Reuse a captured request | Nonces, timestamps, short TTL |
| Credential stuffing | Reused passwords | Rate limiting, MFA, breach lists, bcrypt/argon2 |
| Man-in-the-middle | Plaintext / cert trust failure | TLS, HSTS, cert pinning |
| Prompt injection | See [[06-llm-genai]] | Input isolation, output constraints, tool allowlists |

Also: same-origin policy and how **CORS** relaxes it (simple vs preflighted requests, `Access-Control-Allow-Origin/Credentials`, why `*` + credentials is forbidden); password storage (bcrypt/scrypt/argon2 + per-user salt, never SHA-256 alone); secrets management; TLS termination points; rate limiting as a security control.

---

## 7. Infrastructure between client and code

- **CDN:** edge PoPs, cache keys, TTL vs purge, origin shield, cache-hit ratio, dynamic acceleration, signed URLs.
- **Load balancers:** L4 (TCP, fast, no payload awareness) vs L7 (HTTP-aware routing, TLS termination, retries, header-based routing). Algorithms: round robin, least connections, consistent hashing, weighted, power-of-two-choices. Health checks (active vs passive), draining, DNS LB vs anycast vs Google's Maglev.
- **Reverse proxy vs forward proxy vs API gateway** (auth, rate limit, routing, transformation, quotas).
- **Web server ↔ app server:** why nginx sits in front of gunicorn/uvicorn; workers vs threads vs async event loop; connection limits; slow-loris and buffering.

---

## 8. Deliverable: "type a URL, press Enter"

Write this out once by hand, then be able to say it in 10 min:
URL parse → HSTS check → browser/OS/resolver DNS lookup (with TTLs) → ARP/route → TCP handshake (or QUIC) → TLS 1.3 handshake, ALPN → HTTP request with cookies + cache validators → CDN edge decision (hit/miss/revalidate) → L7 LB → app server → auth (session/JWT) → DB/cache reads → response with cache headers + compression → browser parse: HTML → CSSOM + DOM → render tree → layout → paint → composite; JS blocking, `defer`/`async`, preload; subresource requests reusing the H2 connection → `Set-Cookie` stored → metrics/logs/traces emitted server-side.

---

## 9. Rapid-fire question bank (answer each in <60 s)

1. What exactly happens in a TLS 1.3 handshake, and why is asymmetric crypto only used at the start?
2. HTTP/2 fixed head-of-line blocking — so why does HTTP/3 exist?
3. Difference between `no-cache`, `no-store`, and `max-age=0`?
4. `SameSite=Lax` vs `Strict` — which breaks what real feature?
5. Your JWT is stolen. Walk me through blast radius and mitigation.
6. Why is `Authorization Code + PKCE` needed if you already have a client secret?
7. When is PATCH not idempotent, and why does that matter for retries?
8. 401 vs 403; 409 vs 422 — give a concrete example of each.
9. Cursor pagination vs offset pagination at 100M rows?
10. Client retries a POST after a timeout. How do you avoid a double charge?
11. Why can't you use `Access-Control-Allow-Origin: *` with credentials?
12. Cookie-based auth for a mobile app + web + third-party API — what do you actually choose?
13. gRPC vs REST for an internal service: 3 concrete tradeoffs.
14. SSE vs WebSocket for a live dashboard of 100k viewers?
15. How does a CDN serve personalized content without leaking it across users?
16. What's in a WSDL and why would anyone want one?
17. DNS TTL is 300s and you need to fail over in 10s. Options?
18. How do you design webhook delivery that's reliable but doesn't hammer a dead endpoint?
19. Where does TLS terminate in a typical cloud deployment, and what sees plaintext?
20. Why is `169.254.169.254` the classic SSRF target?
