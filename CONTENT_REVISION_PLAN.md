# Content Revision Plan — Full Site

**Guide:** `CONTENT_FRAMEWORK.md` (v2.0, active). Every piece rewritten under this plan must pass
that framework's Quality Gate and score ≥90/100 on its rubric before it ships.

**Scope:** all content in this repository — identity layer, project showcases, blog index, all blog
posts, GitHub README, hardware guides, and SEO/structured-data assets.

---

## 1. Current-state audit (evidence, Aug 12 2026)

| # | Finding | Evidence | Failure (per framework) |
|---|---|---|---|
| 1 | README.md is generic cliché | "I'm a passionate developer focused on building clean, efficient, and scalable code." | Banned phrase ("passionate"), no metrics, no problem statement |
| 2 | index.html stat charts are unverified | "Citation Accuracy 96%", "Setup Time Reduction 90%", "Search Recall 94%" (Lawyer Assistant); 93%/96%/100%/5→1 (GPT Calendar); 85%/78%/92%/95% (GGUFLoader) | "Contains unverified claims" → quality gate reject |
| 3 | Blog index copy is formulaic | Boilerplate "Guides, tutorials, and deep dives on local AI, private RAG…" repeated on index.html, blog.html, simple-portfolio.html; ~140 card descriptions follow the same "X explained: noun — and how to verb" pattern | Repeated phrases + require_unique_wording |
| 4 | Blog posts share recycled skeletons | Top-10 posts all use identical H2 sequence ("How to Read This List" / "Top 10…" / "Where to Get Them" / "FAQ" / "Sources"); "Quick Takeaways" box recurs | require_unique_structure |
| 5 | simple-portfolio.html duplicates index.html | Same skills grid, same projects, same boilerplate, no canonical URL | Duplicate content; SEO conflict |
| 6 | SEO scaffolding nearly complete | 124 posts: 1 missing og:title, 1 missing canonical, 1 missing FAQPage; sitemap has 128 `<loc>` for 127 HTML files + index | Fix the 3 stragglers; verify parity |
| 7 | Hardware guides are evidence-grade | `ai-inference-hardware/*.md` carry sources, prices, benchmarks, methodology | Not a rewrite target — the role model |
| 8 | No evidence ledger exists | Metrics appear in index.html with no source or method anywhere in the repo | Blocking: claims can't be verified |

---

## 2. Design decisions (do once, before editing)

1. **URLs never change.** Filenames, slugs, and canonical URLs are frozen — rewriting copy must not
   break sitemap, links, or search equity. Titles can change; filenames cannot.
2. **Create `EVIDENCE.md`** — a running ledger: claim → source URL or method → date → verified-by.
   Every metric used on any page gets a row. Unverifiable numbers get removed or reframed as
   *"internal benchmark — N samples, method: …"* with the method stated inline.
3. **simple-portfolio.html:** recommend consolidation — either (a) delete it and update any inbound
   links (index.html is the canonical profile), or (b) keep it only as an intentionally minimal
   single-page variant with *distinct* copy and its own canonical + meta. Do not maintain two
   near-identical portfolios.
4. **Batch by cluster** (reuse BLOG_PLAN.md clusters) so research compounds across posts.
5. **Per-post differentiation rule:** each post gets a unique opening line and a unique section
   skeleton. Before writing, check 2–3 existing posts and avoid their structure and wording.

---

## 3. Phased execution plan

### Phase 0 — Foundation (≈30 min) ✅ start here
- Commit `CONTENT_FRAMEWORK.md` as the active guide.
- Create `EVIDENCE.md`; import every metric currently on index.html (the 11 stat-chart numbers)
  and mark each as *verified / sourceable / remove-or-reframe*.
- Run banned-phrase grep on the whole repo (baseline list above).

### Phase 1 — Identity layer (≈2–4 h)
- **README.md:** full rewrite per §4 of the framework — problem (what this profile is for, who
  reads it), evidence-backed claims, real project list with links, no emoji-cliché intro, no
  "passionate/hardworking". GitHub README = hero_headline + results + links.
- **index.html:** rewrite meta description, title, hero headline + subheadline for uniqueness
  (current "AI Engineer & Builder / Local-first LLM systems, shipped end-to-end" is a decent base —
  sharpen with a specific claim and an evidence hook). Sweep the About section for filler
  ("turns emerging AI research into practical business solutions" is a tell — replace with concrete
  systems and their outcomes).
- **simple-portfolio.html:** apply decision 3.

### Phase 2 — Project showcases on index.html (≈3–5 h)
For each flagship (Lawyer Assistant, GPT Calendar, GGUFLoader) and each grid project
(Mobile AI Assistant, raw-pytorch-minigpt, LLM-Toolkit, Offline AI Assistant, and the 5 SEO sites):
- Run the full workflow: project analysis (read the actual repo where possible) → evidence →
  competitor positioning → story → generate the §4 arc (Problem/Challenge/Solution/Architecture/
  Technologies/Results/Impact/Differentiation).
- **Metrics:** every stat gets an EVIDENCE.md row. If a number can't be supported, reframe it
  ("internal evaluation, 40-document test set — 96% of answers carried a correct citation") or drop it.
- GGUFLoader section currently has no results narrative — add measurable outcomes (setup-time
  comparison vs CLI, memory footprint, model count supported) or remove the bare percentage bars.
- Add a case-study block and a real call-to-action per flagship (current CTAs are generic
  "Visit Website").

### Phase 3 — Blog index (≈4–6 h, highly batchable)
- Rewrite the intro paragraph on blog.html once (remove the repeated boilerplate).
- Rewrite **every card description** with a problem-first, evidence-forward, unique opening
  (framework: require_unique_opening + unique_wording). Keep title, category, date, link intact.
- Update BlogPosting JSON-LD `headline`/`description` only where the title changed.

### Phase 4 — Blog posts (≈the bulk; ~25–35 h total across tiers)
Tier by business value, each tier runs the full workflow + 3 rewrite passes + quality gate:

| Tier | Posts | Action |
|---|---|---|
| A — Flagship case studies (5–10) | lawyer-assistant deep dive, ai-mvp-lessons, portfolio-ai-search-optimization, answer-engine-optimization, gdpr posts | Full §4 arc, unique structure, evidence with sources. The Lawyer Assistant post is the current gold standard — match, don't copy. |
| B — Tutorials / how-to (~40) | ollama installs, rag builds, gguf conversion, quant guides | Verify every command/version; add "why this works" context; state real limits and measured outcomes (tok/s, RAM, time); unique openings. |
| C — List posts / top-10 (~30) | all "Top 10…", "Best…", "8 Best…" | Add ranking methodology + context per item (framework: no feature lists without context); vary H2 skeletons; keep Download column + Sources sections. |
| D — News / comparisons (~30) | model roundups, glm-vs-deepseek, mistral-vs-qwen, LFM, Ant Lab | Refresh facts, date + source every claim, tie to portfolio projects where relevant. |

Rules for every post rewrite: 1 internal link + 1 real project link (unchanged rule from
BLOG_PLAN.md); sources section; meta description ≤160 chars; no repeated sentences across posts
(check against the 2–3 most similar posts before writing).

### Phase 5 — Structured data & site assets (≈2 h)
- Fix the 3 posts missing og:title / canonical / FAQPage (identified in audit).
- Re-run sitemap parity check; reconcile 128 `<loc>` vs file list.
- Ensure Person JSON-LD on index.html stays consistent with rewritten About copy.
- robots.txt: verify no accidental blocks on new pages.

### Phase 6 — Quality review & scoring (≈2–4 h)
- Automated: banned-phrase grep; duplicate-sentence scan across edited files; filler-word scan
  ("just", "simply", "basically", "actually").
- Manual: claim audit against EVIDENCE.md; technical-accuracy spot check.
- Score every edited page on the rubric (uniqueness 25 / depth 25 / clarity 20 / credibility 20 /
  storytelling 10). Anything <90 goes back to rewrite passes.

---

## 4. Effort & sequencing summary

| Phase | Effort | When |
|---|---|---|
| 0 Foundation | ~0.5 h | Immediately (unblocks everything) |
| 1 Identity | 2–4 h | Next — highest visibility |
| 2 Showcases | 3–5 h | Next |
| 3 Blog index | 4–6 h | Can run parallel with 2 |
| 4 Posts Tier A | 4–6 h | After 2–3 (template-setting) |
| 4 Posts Tiers B–D | 15–25 h | Ongoing batches by cluster |
| 5 Assets | ~2 h | After copy settles |
| 6 Review | 2–4 h | Continuous + final gate |

**Total: ~35–50 focused hours.** Phases 0–3 + Tier A (~15 h) deliver the visible quality jump;
Tiers B–D are the long tail and should be scheduled in cluster batches of 4–8 posts.

## 5. Definition of done (per content piece)

- [ ] Passes the §6 quality gate (no banned phrases, no unverified claims, no repeats, has metrics,
      has problem statement, has technical depth)
- [ ] Scores ≥90 on the rubric
- [ ] Every metric logged in EVIDENCE.md
- [ ] SEO metadata unique and ≤160-char description; canonical intact; JSON-LD updated
- [ ] URL/filename unchanged; internal + project links present
- [ ] blog-tracker.csv / sitemap status unchanged or updated where copy-only edits apply
