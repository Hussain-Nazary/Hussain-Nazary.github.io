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

## persian-ai-2026-local-models.html — Persian benchmark figures (added Oct 7, 2026)

All figures quoted from a public, peer-reviewed benchmark. Status: VERIFIED.

| Claim | Value | Source / method | Action |
|---|---|---|---|
| Gemma 2 — overall few-shot Persian avg | 0.61 | Cherakhloo et al. (2025), arXiv:2510.12807, Table 5 | Cited inline + sources note |
| GLM-4 — overall few-shot | 0.53 | same | same |
| Qwen2.5 — overall few-shot | 0.50 | same | same |
| Qwen2 — overall few-shot / NER | 0.48 / 0.82 | same (Table 5 / Table 1) | same |
| Llama 3.1 / 3.2 — overall few-shot | 0.30 / 0.21 | same | same |
| Gemma 2 — PersianQA / Persian-SQuAD | 0.67 / 0.58 | same, Table 2 | same |
| Aya Expanse 32B — cultural alignment | up to ~94 across MELAC categories | MELAC, arXiv:2508.00673 | Cited inline |
| Gemma 3 — included in MELAC recent-model set | qualitative (tested, 41-model study) | MELAC, arXiv:2508.00673 | Cited inline |
| Qwen3 / Llama 4 / GPT-OSS — Persian numbers | "thinner verified Persian-specific numbers" | no dedicated Persian benchmark found in review | Flagged in post, not asserted |

Note: the benchmark paper labels models as "gemma2", "glm4", "qwen2.5", "qwen2" without size suffixes; the post follows that naming and mentions 7–9B only as a local-sizing guideline, not a claim about the tested model size. MELAC scores for Aya Expanse were read from the paper's results; the post phrases them as "up to ~94" rather than a full ranking because the complete table was not reproduced.

## Rules going forward

- Any new metric added to any page gets a row here **in the same edit** — no orphan claims.
- A metric with no source or method may not be republished; it must be re-added as PARTIAL with
  the methodology documented or as VERIFIED with a public source.
- Metrics with no row in this ledger fail the framework quality gate and are rejected.
- This file is internal documentation; it is not linked from public pages.
