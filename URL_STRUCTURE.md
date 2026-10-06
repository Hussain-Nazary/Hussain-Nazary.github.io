# Hussain Nazary — Site Structure & Entity-Recognition Strategy

This document describes the URL structure and the entity-resolution strategy behind
this site. Its single goal: make search engines, AI answer engines, LLMs, and knowledge
graphs understand that **all common spellings of this name refer to one person —
Hussain Nazary**.

---

## 1. Canonical identity

| Field | Value |
| --- | --- |
| Canonical name | **Hussain Nazary** |
| Native script | حسین نظری (Persian/Dari) |
| Given name variants | Hussain, Hussein, Husain, Hossain, Hossein |
| Family name variants | Nazary, Nazari, Nizari |
| Primary URL | `https://hussain-nazary.github.io/` |
| Entity `@id` | `https://hussain-nazary.github.io/#person` |

The full list of alternate names carried in Schema.org `alternateName`:

Hussein Nazary · Husain Nazary · Hossain Nazary · Hossein Nazary ·
Hussain Nazari · Hussein Nazari · Husain Nazari · Hossain Nazari ·
Hossein Nazari · Hussain Nizari · Hussein Nizari

---

## 2. URL structure

All URLs are lowercase, hyphenated, and human-readable (descriptive, not parameterized).

| URL | Purpose | Priority |
| --- | --- | --- |
| `/` (`index.html`) | Portfolio home — services, process, selected work | 1.0 |
| `/about.html` | **Entity-rich About page** — canonical bio, name variations, transliteration explanation, name FAQ | 0.9 |
| `/blog.html` | Blog index — ~260 articles on local AI, RAG, agents, GGUF | 0.9 |
| `/ggufloader-project.html` | GGUF Loader (GGUFLoader) case study | 0.9 |
| `/lawyer-assistant-project.html` | Lawyer Assistant case study | 0.9 |
| `/gpt-calendar-project.html` | GPT Calendar case study | 0.9 |
| `/what-is-gguf.html` | GGUF explainer (keyword: GGUF Loader) | 0.8 |
| `/portfolio-ai-search-optimization.html` | AI-search optimization explainer | 0.8 |
| `/structured-data-jsonld.html` | JSON-LD explainer | 0.8 |
| `/answer-engine-optimization.html` | Answer-engine optimization explainer | 0.8 |
| `/robots.txt` | Crawler rules (incl. AI crawlers) | — |
| `/sitemap.xml` | Full URL inventory | — |

Suggested future URLs (reserve these names if the site grows):

```
/name-variations.html     — a standalone spelling/transliteration reference
/projects/                — project directory index (if case studies multiply)
/about/                   — directory form, redirecting to /about.html
```

---

## 3. Entity-recognition signals (what makes this work)

### 3.1 Schema.org (JSON-LD)

- **`Person`** with `@id`, `name`, `alternateName` (11 variants), `jobTitle`,
  `description`, `url`, `image`, `sameAs`, `knowsAbout`, `knowsLanguage`.
- **`ProfilePage`** on `/about.html` wrapping the `Person` as `mainEntity`.
- **`FAQPage`** whose questions *explicitly* state the identity equivalences
  ("Is Hussein Nazary the same person as Hussain Nazary? → Yes.").
- **`BreadcrumbList`** for hierarchical context.
- **`WebSite`** with `publisher` = the same `Person`.
- The `@id` (`#person`) is **identical on index.html and about.html**, which
  merges the two documents into one entity in a knowledge graph.

### 3.2 `sameAs` (external corroboration)

The Person entity links out to the same identity on other authoritative surfaces:

- `https://github.com/hussainnazary2`
- `https://x.com/HussainNazary`
- `https://lawyers-assistant.github.io`
- `https://gpt-calendar.github.io`
- `https://ggufloader.github.io`

`sameAs` is the strongest cross-site entity signal available — it tells resolvers
"this node and that node are the same thing."

### 3.3 Explicit in-page statements

AI systems reason over natural language, not just markup. The About page therefore
states the equivalence in plain sentences:

> "Hussein Nazary and Hussain Nazary are the same person."

> "Hussain Nazari and Hussain Nazary are the same person."

> "Hossein Nazary is the same person as Hussain Nazary."

These are deliberately unambiguous, self-contained claims an LLM can lift verbatim.

### 3.4 Internal linking

Every page links back to the canonical `Person` via navigation and contextual links,
reinforcing the entity graph:

- `index.html` → `about.html` (About nav + inline name note)
- `about.html` → 3 project pages + `blog.html` + `what-is-gguf.html` + `portfolio-ai-search-optimization.html`
- all project pages and `blog.html` → `about.html` (About nav)

### 3.5 Crawler access

`robots.txt` explicitly `Allow`s the AI-crawler user agents (GPTBot, OAI-SearchBot,
ChatGPT-User, ClaudeBot, Claude-Web, PerplexityBot, Google-Extended, Applebot-Extended,
CCBot) so answer engines can ingest the entity.

---

## 4. Keyword coverage (entity-first, not density)

Target terms are carried in schema `knowsAbout`, page copy, headings, and title/meta
— distributed naturally across the site rather than stuffed into one page:

- **AI developer / AI engineer / Python developer** — About hero, bio, expertise grid, meta.
- **GGUF Loader (GGUFLoader)** — About FAQ + project card + `/ggufloader-project.html` + `/what-is-gguf.html`.
- **Local AI / Local LLMs** — expertise grid, blog cluster (~60 articles).
- **AI agents** — expertise grid + `/build-ai-agent-langgraph-ollama.html` + `/multi-agent-systems.html`.
- **RAG systems** — expertise grid + `/how-to-build-rag-system-30-minutes.html` + `/evaluate-rag-system.html`.

---

## 5. Operational notes

- Canonical tags point to the **lowercase** host form (`hussain-nazary.github.io`).
  Host names are case-insensitive, so no redirect is required, but tags are consistent.
- `sitemap.xml` is regenerated whenever a page is added.
- Name-variation content lives on `/about.html`; if traffic warrants, promote it to a
  standalone `/name-variations.html` and keep the About page linking to it.
