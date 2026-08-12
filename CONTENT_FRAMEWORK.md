# AI Portfolio Content Generation Framework (v2.0)

**Status: ACTIVE.** This is the standing guide for every content modification in this repository
(portfolio pages, blog posts, README, project showcases, markdown guides). Any content written or
rewritten here must pass the Quality Gate at the end of this document before it is considered done.

---

## 1. Objective

Generate elite portfolio content that reads like it was written by a senior software engineer,
AI engineer, startup founder, and technical writer. The system must avoid generic AI-generated
language and instead produce content based on **evidence, research, technical depth, business
value, and measurable impact.**

## 2. Global rules

### 2.1 Never use (banned phrases)

| Banned | Why |
|---|---|
| "passionate developer" / "hardworking engineer" | Empty self-praise, tells nothing |
| "cutting-edge" / "state-of-the-art" | Claims quality without evidence |
| "innovative solution" | Meaningless without specifics |
| "revolutionary" | Exaggeration, unverifiable |
| "seamless", "robust", "game-changer", "unleash", "delve", "empower" | AI-cliché / filler vocabulary |
| Any feature list without context | Forbidden — every feature needs a why |

### 2.2 Writing style

- **Tone:** technical founder — confident, direct, first-person ownership of trade-offs.
- **Reading level:** professional; plain English over jargon, but never dumbs down mechanics.
- **Avoid:** marketing fluff, AI clichés, repetition, empty claims.
- **Show, don't tell:** a sentence like "citations link to the exact page and paragraph" beats
  "high-quality answers". Specifics are evidence; adjectives are not.
- **Explain engineering decisions** — what was chosen, what was rejected, and why.
- **Keep claims evidence-based** — every number traceable to a source or a documented measurement.

### 2.3 Uniqueness requirements

- Unique structure per piece (no recycled H2 skeletons across posts).
- Unique opening — first paragraph must commit to a specific problem or result.
- Unique story — the specific constraints, failures, and decisions of *this* project.
- Unique wording — never copy a paragraph from one page to another.

## 3. Workflow (per content piece)

| Step | Actions |
|---|---|
| 1. Project analysis | Read the project files, README, docs, source; identify features, architecture, the real problem |
| 2. Evidence collection | Find metrics, benchmarks, performance numbers, languages, frameworks, real results — and their *sources* |
| 3. Competitor research | Analyze similar projects/products; identify differentiators and the market gap |
| 4. Story extraction | Determine: user problem → technical challenge → solution → business value → unique advantage |
| 5. Content generation | Produce the sections from the output schema (§5) |
| 6. Quality review | Remove generic phrases, duplicate sentences, AI patterns; verify claims, metrics, technical accuracy |
| 7. Rewrite pass 1 | Increase clarity |
| 8. Rewrite pass 2 | Increase uniqueness |
| 9. Rewrite pass 3 | Increase authority |
| 10. Final scoring | Score against §7 rubric; minimum 90/100 to ship |

## 4. Content requirements — every project description must answer

1. **Problem** — what existed before this project?
2. **Challenge** — what made solving it difficult?
3. **Solution** — what was built?
4. **Architecture** — how does it work internally?
5. **Technologies** — which ones, and why those?
6. **Results** — what measurable outcomes were achieved?
7. **Impact** — how did users or businesses benefit?
8. **Differentiation** — what makes it different from similar solutions?

## 5. Output schema (checklist per content piece)

- `hero_headline` — specific, owns a niche, no clichés
- `hero_subheadline` — one sentence, names the outcome
- `problem_statement` — the pain before, concrete
- `solution_summary` — what was built, one or two sentences
- `technical_overview` — real mechanics, real stack
- `architecture_description` — components, data flow, decisions
- `results` — list of measurable outcomes
- `key_metrics` — numbers with context and source
- `project_story` — constraints, failures, decisions
- `case_study` — full problem → solution → results arc
- `seo_title` / `seo_description` — unique, ≤160 chars for description
- `linkedin_version` / `github_version` / `portfolio_version` — same story, three formats

## 6. Quality gate — REJECT the content if ANY of these is true

- Contains generic AI phrases (§2.1 list or style violations)
- Contains unverified claims (no source, no methodology, no measurement)
- Contains repeated sentences (across the piece or across other pages)
- Contains filler words ("just", "simply", "basically", "actually" as padding)
- Lacks metrics (no measurable outcome anywhere)
- Lacks a problem statement (starts with the solution, not the pain)
- Lacks technical depth (no mechanics, no stack, no trade-offs)

## 7. Final scoring rubric

| Criterion | Weight | Score (0–10) |
|---|---|---|
| Uniqueness | 25% | |
| Technical depth | 25% | |
| Clarity | 20% | |
| Credibility (evidence) | 20% | |
| Storytelling | 10% | |
| **Minimum to ship** | | **90/100** |

## 8. How this applies to THIS repository

| Content type | Files | Framework emphasis |
|---|---|---|
| Identity layer | `README.md`, `index.html` (hero/about/meta), `simple-portfolio.html` | Never-use list, unique opening, evidence over adjectives |
| Project showcases | `index.html` flagship sections (Lawyer Assistant, GPT Calendar, GGUFLoader) + projects grid | Full §4 arc; every metric must be verified or honestly framed as internal eval with method |
| Blog index | `blog.html` | Unique per-card copy; kill repeated boilerplate ("Guides, tutorials, and deep dives…") |
| Blog posts | ~124 `*.html` posts | Unique structure/opening per post; sources; download links; one internal + one project link |
| Hardware guides | `ai-inference-hardware/*.md` | Already evidence-grade — role model, not rewrite target |
| Site assets | `sitemap.xml`, structured data, `robots.txt` | Keep URL/SEO parity when copy changes |

**Evidence ledger:** claims made anywhere in this repo must be logged in `EVIDENCE.md`
(source URL, measurement method, date, or "internal benchmark — method described inline").
A claim without a ledger entry fails the quality gate.
