# 07 · Google interview playbook

← [[README]] · Hours: ~30 · Start W1 (resume/referral), heavy in Phase 4

Details of Google's process shift over time and vary by org, region, and level — verify specifics with your recruiter when you get one. What's below is the stable shape.

---

## 1. The pipeline

| Stage | What it is | Typical duration |
|---|---|---|
| **Application / referral** | Resume screen by recruiter + keyword/level match | 1–4 weeks (or silence) |
| **Recruiter call** | Level calibration, timeline, comp range, team interest | 20–30 min |
| **Phone/video screen** | 1–2 coding rounds, 45 min each, shared editor | 1–2 weeks after |
| **Onsite loop ("virtual onsite")** | 4–5 rounds: 2–3 coding, 0–1 system design (level-dependent), 1 Googlyness & Leadership | 1 day or split over days |
| **Hiring committee (HC)** | Independent committee reads written feedback packets; you're not present | 1–3 weeks |
| **Team matching** | Conversations with hiring managers; you can be HC-approved but unmatched | 2 weeks–3 months |
| **Offer review / comp committee → offer** | SVP-level sign-off | 1–3 weeks |

Total: commonly 6–12 weeks, sometimes longer. Plan a Phase-5 start no later than mid-December to be through by ~February. **The single biggest process lesson: your interviewers write detailed notes, and the HC decides from those notes — so make your reasoning explicit and quotable. Anything you thought but didn't say does not exist.**

---

## 2. Levels

| Level | Rough profile | Loop emphasis |
|---|---|---|
| L3 (SWE I) | New grad / <1 yr | Coding-heavy, no design |
| **L4 (SWE II)** | ~2–5 yrs, owns features independently | Coding-heavy; sometimes a lighter design round; strong ownership stories |
| L5 (Senior) | ~5–8+ yrs, owns systems, influences others | **Full system design round**, leadership/impact stories, ambiguity handling |
| L6 (Staff) | Cross-team scope | Design + org-level influence |

Levelling is set from the resume and calibrated in the loop. Don't undersell: if your work included design ownership, cross-team collaboration, or mentoring, say so in the resume — it changes the level you're interviewed at, which changes the comp band substantially. Check [levels.fyi](https://levels.fyi) for your location before the recruiter call.

---

## 3. What Google grades (their four attributes)

| Attribute | What it means | How to feed it |
|---|---|---|
| **General Cognitive Ability (GCA)** | How you think through ambiguity, structure problems, back reasoning with logic | Structure everything out loud: "there are three approaches; here's the tradeoff axis" |
| **Role-Related Knowledge (RRK)** | Depth in the craft: coding, systems, domain | [[01-dsa]], [[04-hld]], [[02-http-and-internet]] |
| **Leadership** | Emergent leadership — stepping up without the title, stepping back when someone else should lead | Stories about ambiguity, influence without authority, conflict, mentoring |
| **Googlyness** | Bias to action, comfort with ambiguity, intellectual humility, collaboration, doing the right thing | Behavioural round; also how you take hints in coding rounds |

Each round scores 1–4 on some subset. Consistency across rounds matters more than one brilliant round — HC looks for a coherent signal.

---

## 4. The coding rounds — mechanics

- 45 min: ~5 min intro, ~35 min on 1–2 problems, ~5 min your questions.
- **The editor doesn't run code.** No autocomplete, no syntax highlighting to lean on, no tests. From W17, all practice happens in a plain `.txt` file — this alone is worth several points of performance.
- Expect **layered follow-ups** more than trick questions. The pattern: solve it → "now the array doesn't fit in memory" → "now it's a stream" → "now 1000 threads call it".
- Write **compiling-quality** code: real names, helper functions, no pseudocode drift, correct Python syntax from memory (no `dict.get` guesswork).
- **Verify yourself.** Trace your code on an example line by line, out loud. Interviewers explicitly score this.
- Use the script in [[01-dsa]] §6. Ask before you code: *"Plan sounds like this — shall I go ahead?"*
- If you're stuck: say what you know, what you've ruled out and why, and what you'd try next. Visible structured struggle scores far better than silence.

---

## 5. The behavioural / Googlyness round — build the story bank

12 stories, written once, reused across every prompt. Use **STAR** but weight it: Situation 15%, Task 10%, **Action 60%**, Result 15% — with numbers in the result. Target 2.5 minutes spoken.

| # | Story slot | Prompts it answers |
|---|---|---|
| 1 | Hardest technical problem you solved | Depth, GCA |
| 2 | Project you led end-to-end | Ownership, leadership |
| 3 | Disagreed with a teammate/manager | Conflict, humility |
| 4 | You were wrong / shipped a bug to prod | Humility, learning, integrity |
| 5 | Ambiguous requirements, no clear owner | Googlyness, bias to action |
| 6 | Tight deadline, had to cut scope | Prioritization, tradeoffs |
| 7 | Influenced without authority | Leadership |
| 8 | Mentored or unblocked someone | Collaboration |
| 9 | Improved a process/system nobody asked you to | Initiative |
| 10 | Learned something hard, fast | Learning agility (use the GenAI work from [[06-llm-genai]]) |
| 11 | Handled negative feedback | Growth mindset |
| 12 | Made a decision with incomplete data | Judgement |

For each story write: context (2 sentences), your specific decisions and *why*, the tradeoff you rejected, the measurable result, and what you'd do differently. That last part is what makes story 4 and 11 land instead of sounding defensive.

Rules: always "I" for your contribution and "we" for team context — never claim the team's work; never blame a named person; always quantify (%, ms, $, users, hours saved); pick recent stories (last 2–3 years).

---

## 6. Getting the interview (start this in W1, not W14)

Ranked by conversion rate:
1. **Referral from a current Googler.** Warm > cold by a wide margin. Sources: ex-colleagues, college alumni, open-source contributors you've interacted with, meetups. Ask well: a 3-line message with the exact job ID, your resume, and 2 bullets on why you match — make it a 60-second favour, not a research project.
2. **Recruiter contact** via LinkedIn, when your profile actually matches the JD keywords.
3. **Direct application** on careers.google.com — apply to a small number of well-matched roles rather than dozens; there's a cap on active applications and shotgunning reads badly.
4. Adjacent paths: contractor/vendor roles, Google Summer of Code (if eligible), open-source contributions to Google projects, conference/community visibility.

**Resume — one page, XYZ format:** *"Accomplished [X] as measured by [Y] by doing [Z]."* e.g. "Cut p99 API latency 40% (820 ms → 490 ms) for 2 M daily requests by adding a Redis read-through cache and eliminating an N+1 query." Every bullet gets a number. Put the GenAI project ([[06-llm-genai]]) and any distributed-systems work above older CRUD work. ATS-friendly: plain layout, no columns, no icons, keywords lifted from the JD, single PDF.

**Timing:** resume v1 in W2, referral asks in W12–W14, apply W14–W16. Loops take 6–12 weeks, so W14 applications land your onsite in Phase 4/5 — which is exactly the plan.

Interview elsewhere first, deliberately. Two real loops at other companies in W15–W18 will make the Google loop feel routine, and a competing offer is the only real negotiation leverage.

---

## 7. Offer, negotiation, and the reset case

- Comp = base + bonus (target %) + **equity (GSU, 4-yr vest, front-loaded in some bands)** + sign-on. The equity band is where the negotiation range actually lives.
- Never give a number first: "I'd rather focus on fit; I'm sure you'll make a competitive offer once you've calibrated my level." If pressed, give a researched range from levels.fyi for your location and level.
- The two things that move an offer: a **competing offer**, and **level**. Argue level with evidence (scope owned, systems designed, people influenced), not with seniority claims.
- Team match matters more than 5% comp. Ask about: on-call load, what the team shipped last quarter, how promotions actually work there, tech-debt reality, whether the team is growing or backfilling.
- **If it doesn't land:** cooldown is typically ~6–12 months, and reapplying is normal and common. Get whatever feedback the recruiter will share, map it to the exact failed dimension, and fix that one thing. Meanwhile take the other offer — Google interviews better from a position of employment at a strong company.

---

## 8. Questions to ask your interviewers (pick 2 per round)

What does the first 90 days look like on this team? · What's the hardest technical problem the team is facing right now? · How are design decisions made and documented? · What's the on-call rotation and how noisy is it? · How does the team use AI tooling day to day? · What separates a strong L4 from a strong L5 here? · What would make you say a new hire had a great first year?

---

## 9. Last four weeks (Phase 4 checklist)

- [ ] 12+ mocks logged, with written feedback per round ([[09-progress-tracker]])
- [ ] All coding practice in a plain no-autocomplete editor
- [ ] 12 stories written, spoken, timed
- [ ] 5 design problems rehearsed end-to-end on a whiteboard/blank page
- [ ] Rapid-fire banks in [[02-http-and-internet]] §9, [[04-hld]] §9, [[06-llm-genai]] §10 answerable in <60 s each
- [ ] Failure log re-solved to zero
- [ ] Resume + LinkedIn final; referral in flight
- [ ] Logistics: quiet room, wired internet, backup hotspot, charged laptop, water, a paper notebook for scratch work
- [ ] Sleep. Two nights of good sleep beats two nights of cramming — this is not a motivational note, it's the highest-EV item on this list.
