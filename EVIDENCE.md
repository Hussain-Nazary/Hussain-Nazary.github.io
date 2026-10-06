# Evidence Ledger

Every metric, benchmark, or performance claim published on the portfolio must be logged here with a
source or measurement method before it ships (see CONTENT_FRAMEWORK.md §6 — "contains unverified
claims" rejects a piece).

**Status values**

- `VERIFIED` — public source, reproducible measurement, or architectural fact documented in the repo
- `PARTIAL` — owner-confirmed number; methodology documented but not independently reproducible
- `REMOVED` — no source or method on file; removed from the public site (blocked from publication)

---

## index.html — flagship stat charts

### Lawyer Assistant ("Lawyer Assistant Performance")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Citation accuracy | 96% | PARTIAL | Owner's benchmark suite, public repo `backend/benchmark/`: 200-question runner (`python -m benchmark.runner`), 40-question golden eval (`run_golden_eval.py`), CUAD runner; README claims "200-question dataset + charts" and "Tested with 500+ documents". Value reported as "own benchmarks" in blog posts (private-legal-research-local-ai.html, rag-citations-table-stakes.html, rag-answers-from-documents-proves-it.html). Result artifacts are runtime-generated and not committed — re-running the harness is required to reproduce. | Kept on index.html; footnote now cites the benchmark suite |
| Data privacy (no cloud path) | 100% | VERIFIED | Architectural fact — offline mode has no cloud path (lawyer-assistant-rag-pipeline-privacy-first-legal-ai.html; GitHub README "Local Mode (100% Private)") | None |
| Search recall | 94% | PARTIAL | Same benchmark suite as citation accuracy; value claimed in blog posts (hybrid-search-keyword-semantic.html: "Its search recall benchmark is 94%"). | Kept on index.html; footnote now cites the benchmark suite |
| Setup time reduction | 90% | REMOVED | No source, method, or comparison baseline anywhere (repo, site, blog). | Removed from index.html Aug 12, 2026 |

### GPT Calendar ("Smart Calendar Performance")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Voice command accuracy | 93% | REMOVED | No source or method (repo README, product site, blog) — no test set on file. | Removed from index.html Aug 12, 2026 |
| SMS parsing accuracy | 96% | REMOVED | No source or method — no test set on file. | Removed from index.html Aug 12, 2026 |
| On-device privacy | 100% | VERIFIED | Architectural fact — on-device AI mode (Ollama local option documented in repo README). | None |
| Apps replaced | 5 → 1 | VERIFIED | Product scope — calendar, reminders, finance, location alerts, tasks in one app (repo README + site). | None |

### GGUFLoader ("GGUF Loader Performance" → "GGUF Loader by the Numbers")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Setup time reduction | 85% | REMOVED | No source or method anywhere (repo README, docs, site). | Removed from index.html Aug 12, 2026 |
| Memory efficiency | 78% | REMOVED | No source or method anywhere. | Removed from index.html Aug 12, 2026 |
| Multilingual accuracy | 92% | REMOVED | No source or method anywhere. | Removed from index.html Aug 12, 2026 |
| Plugin compatibility | 95% | REMOVED | No source or method anywhere. | Removed from index.html Aug 12, 2026 |

---

## Resolution applied in this pass (Aug 12, 2026 — second pass)

1. **Promoted to PARTIAL** — Lawyer Assistant Citation accuracy (96%) and Search recall (94%).
   The public repo (github.com/hussainnazary2/Lawyer-Assistant) documents a runnable benchmark
   suite under `backend/benchmark/` (200-question runner, 40-question golden eval, CUAD runner,
   Recall@K / MRR / Precision@K metrics) that the numbers are claimed against. The values are
   owner-reported (blog posts) and result artifacts are not committed, so they stay PARTIAL until
   someone re-runs the harness and commits the results.
2. **Removed from index.html** — the 7 metrics with no source or method anywhere:
   Lawyer Assistant Setup time reduction (90%); GPT Calendar Voice command accuracy (93%) and
   SMS parsing accuracy (96%); and all four GGUFLoader metrics (85% / 78% / 92% / 95%).
3. **index.html footnotes updated** — the Lawyer Assistant chart now reads "Benchmark figures
   from the project's own evaluation suite — backend/benchmark in the GitHub repo." The GPT
   Calendar footnote was removed (only VERIFIED facts remain) and the GGUFLoader chart was
   replaced with a sourced facts panel (100% local inference, 4GB RAM minimum, cross-platform,
   CPU/GPU) drawn from the public repo README.

## persian-ai-2026-local-models.html — 2026 Persian benchmark figures (rewritten Oct 7, 2026)

Post was fully rewritten to cover the 2026 model generation only. All figures quoted from 2026
peer-reviewed sources. Status: VERIFIED.

| Claim | Value | Source / method | Action |
|---|---|---|---|
| Gemma 3 12B — DivanBench factual Persian knowledge | 87% | Sakhaeirad et al. (2026), arXiv:2602.17623, Table 2 (leader of 7 models, 7–12B) | Cited inline + sources note |
| Gemma 3 12B — DivanBench cultural reasoning (scenario) | 66% | same, Table 2 | same |
| Dorna2 8B — DivanBench factual / scenario | 73% / 54% | same, Table 2 | same |
| DivanBench factual→scenario gap (average) | 21 percentage points | same | Cited inline |
| Parse — Persian Boolean QA, 24B+ models (negation/simple) | ~0.88–0.96 zero-shot | Mozafari et al. (2026), SIGIR 2026, arXiv:2602.01246, Table 4 | Cited inline |
| Parse — comparative multi-hop | ~0.57 | same, Table 4 | same |
| Qwen3.5 9B — MEA multilingual benchmark (incl. Persian) | strongest model overall | Ryu et al. (2026), arXiv:2606.01252, Table 1 | Cited inline |
| gpt-oss-20b / Tiny-Aya-Global — MEA | benchmarked; Tiny-Aya-Global strongest small model on low-resource | same, Table 1 | same |
| Gemini 2.5 Flash — PMWP Persian math accuracy | 72.02% (highest) | Abdolmaleki et al. (2026), SilkRoadNLP @ EACL 2026 | Cited inline |
| LLaMA-3-8B / Qwen-2.5-7B — PMWP after LoRA | >91% exact equation match | same | Cited inline |

Notes / limits of what is asserted:

- DivanBench models are labelled unsized in prose but sized in Table 2 ("Gemma3-12B", "Dorna2-8B");
  the post uses those sizes.
- MEA covers 24 target languages including Persian (fa), but Table 1 aggregates by *resource level*,
  not per language. The post therefore says Qwen3.5-9B was "strongest overall" on that benchmark and
  does **not** claim a Persian-only score.
- Parse Table 4 reports per-subtype Boolean accuracy; the post quotes ranges (~0.88–0.96, ~0.57)
  rather than presenting a fabricated single Persian score.
- The superseded 2025 figures (Cherakhloo arXiv:2510.12807; MELAC arXiv:2508.00673) were removed from
  the post in this rewrite and are no longer cited anywhere on the site.

## Rules going forward

- Any new metric added to any page gets a row here **in the same edit** — no orphan claims.
- A metric with no source or method may not be republished; it must be re-added as PARTIAL with
  the methodology documented or as VERIFIED with a public source.
- Metrics with no row in this ledger fail the framework quality gate and are rejected.
- This file is internal documentation; it is not linked from public pages.
