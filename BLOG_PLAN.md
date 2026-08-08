# Blog Growth Plan — 1,000 Posts in 2 Months

Goal: publish portfolio-matched blog posts that make people find Hussain Nazary through search, AI answer engines, and local-AI communities — then convert that traffic into project stars, downloads, and client leads.

---

## 1. Honest math first

- 2 months ≈ 60 days → **1,000 posts = ~17 posts/day**.
- A genuinely researched, quality post takes a human **1–3 hours** (search, sources, writing, SEO, linking). 17/day is not sustainable by hand — that pace either burns out quality or produces thin content that Google and AI engines won't rank.
- **Recommended approach (hybrid):** build a *production system* — batch research (one research session feeds 3–5 posts), template-driven structure, assisted drafting, then human review and factual verification. That makes **8–12 posts/day** achievable with a focused routine, and **600–700 posts in 60 days** realistic. If you insist on the full 1,000, we run a second "quick-win" track (150–200 short how-tos / list posts drafted from templates).
- Quality bar stays non-negotiable: **no fabricated facts, no AI-slop filler, no fake expertise claims** (per your earlier instruction). Every post links to a real source or a real project of yours.

---

## 2. Portfolio-matched keyword clusters (the "why people find you")

Every cluster maps to a real project/skill, so each post doubles as product marketing. ~14 clusters × ~70 posts ≈ 1,000.

| # | Cluster | Search intent (what people type) | Maps to | Share |
|---|---------|----------------------------------|---------|-------|
| 1 | Run LLMs locally (GGUF, llama.cpp, Ollama) | "run llama locally", "run gguf model", "ollama guide" | GGUF Loader, Local AI Zone | 12% |
| 2 | GGUF models & quantization | "what is gguf", "q4_k_m vs q8_0", "convert model to gguf" | Local AI Zone | 12% |
| 3 | RAG & knowledge systems | "build rag", "hybrid search", "chromadb tutorial", "embeddings" | Lawyer Assistant, Haal Lab | 10% |
| 4 | Privacy-first / offline AI | "private llm", "offline ai", "data sovereignty", "local ai for business" | Lawyer Assistant, Haal Lab | 10% |
| 5 | Legal AI / AI for lawyers | "ai contract review", "legal ai", "ai for lawyers" | Lawyer Assistant | 8% |
| 6 | AI agents & automation | "ai agent workflow", "agentic rag", "build an ai assistant" | Haal Lab, skills | 8% |
| 7 | Mobile AI assistants | "voice assistant android", "on-device ai", "ai calendar app" | GPT Calendar, Mobile AI Assistant | 6% |
| 8 | AI product & startup | "build an ai product", "ai startup mvp", "pitch ai startup" | GPT Calendar | 6% |
| 9 | SEO · GEO · AEO | "generative engine optimization", "answer engine optimization", "structured data seo" | This portfolio (skill) | 8% |
| 10 | Multilingual / low-resource NLP | "pashto nlp", "dari translation", "multilingual llm" | Skills, Book Translator | 6% |
| 11 | AI model news & comparisons | "latest ai models", "gemini vs claude", "best local llm 2026" | Existing blog (already 2 posts) | 10% |
| 12 | Tutorials / under the hood | "transformer from scratch", "pytorch minigpt", "tokenizer bpe" | raw-pytorch-minigpt | 4% |
| 13 | Local AI for business/enterprise | "on-prem llm", "private rag enterprise", "ai for regulated industries" | Haal Lab | 4% |
| 14 | Local AI community quick wins | "llama.cpp vs ollama", "best gui for local llm", "mistral vs deepseek local" | GGUF Loader | 2% |

**Traffic reality:** clusters 1–4, 9, 11 are the highest-volume, lowest-competition sweet spots for a new blog. Cluster 5 (legal AI) is low volume but extremely high intent — those readers become Lawyer Assistant users/leads. Clusters 10 and 12 are low volume but build authority and unique credibility (nobody else writes Pashto/Dari NLP).

---

## 3. Cadence (60-day sample rhythm)

Batch by day so research effort compounds:

- **Research days** (Mon/Wed/Fri): 2× 1-hour sessions → produce outlines + source lists for 10–15 posts.
- **Writing days** (Tue/Thu/Sat/Sun): draft 8–12 posts from the batch (each 600–1,200 words), reuse structure templates per cluster.
- Daily cluster mix (example): 2× local-AI, 2× GGUF/quantization, 1× RAG, 1× privacy, 1× SEO/GEO/AEO, 1× legal AI, 1× model news, 1× rotating (agents/mobile/multilingual/product).
- Every post: 1 primary keyword + 2 secondary + internal link to 1 existing post + link to 1 real project site.

Week-1 starter calendar (see `blog-tracker.csv` for the full list):

| Day | Posts (topics) |
|-----|----------------|
| 1 | Run GGUF locally (✓ done) · What is GGUF |
| 2 | Ollama vs llama.cpp · Best local LLM tools 2026 |
| 3 | Q4_K_M vs Q8_0 · Convert a model to GGUF |
| 4 | Build RAG in 30 min · What is hybrid search |
| 5 | Private LLM for business · AI contract review basics |
| 6 | GEO/AEO intro · Structured data for AI engines |
| 7 | GPT-OSS vs Qwen local · Models for 8GB RAM |

---

## 4. Research → write workflow (per post, ~30–45 min once batched)

1. **Keyword** — pick from tracker; check SERP intent (information vs tutorial vs comparison).
2. **Research** — web search for current facts (tool versions, model names, benchmarks). Save 3–5 authoritative sources. **Never publish a fact you didn't verify.**
3. **Outline** — H1 + 4–6 H2 sections + table (if comparison/tutorial) + FAQ (3–6 Q&As).
4. **Write** — 600–1,200 words, plain English, concrete steps. Match the existing post style (`lawyer-assistant-rag-pipeline-privacy-first-legal-ai.html` is the template).
5. **SEO pack** — title, meta description, keywords, canonical, OG/Twitter card, `BlogPosting` + `FAQPage` JSON-LD. Filename = slug.
6. **Internal links** — 1 link to another blog post + 1 to the relevant project site (lawyers-assistant.github.io, ggufloader.github.io, local-ai-zone.github.io, haal-lab.solutions, gpt-calendar.github.io).
7. **Publish** — add card to `index.html` (and `simple-portfolio.html`) blog section, add URL to `sitemap.xml`, mark row in `blog-tracker.csv` as published.

---

## 5. Anti-patterns (what kills this plan)

- Posting 17 identical-structure AI-slop articles → Google helpful-content demotion, no citations from answer engines.
- Fabricated benchmarks or fake user numbers → destroys trust (and you asked for zero lies).
- Keyword stuffing in titles/meta.
- Publishing everything in one day → no crawl cadence; space 4–8/day.
- Internal links to the same anchor text repeatedly.

---

## 6. Files

- `blog-tracker.csv` — master list (cluster, title, keyword, status, date, URL). Expand by copying rows.
- `BLOG_PLAN.md` — this file.
- `lawyer-assistant-rag-pipeline-privacy-first-legal-ai.html` — style/SEO template for all posts.
- `how-to-run-gguf-models-locally-2026-guide.html` — first post of the 1,000 (done).
