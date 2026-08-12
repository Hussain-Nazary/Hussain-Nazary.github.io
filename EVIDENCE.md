# Evidence Ledger

Every metric, benchmark, or performance claim published on the portfolio must be logged here with a
source or measurement method before it ships (see CONTENT_FRAMEWORK.md §6 — "contains unverified
claims" rejects a piece).

**Status values**

- `VERIFIED` — public source, reproducible measurement, or architectural fact documented in the repo
- `PARTIAL` — owner-confirmed number; methodology documented but not independently reproducible
- `UNVERIFIED` — number exists with no source or method on file; blocked from unqualified publication

---

## index.html — flagship stat charts

### Lawyer Assistant ("Lawyer Assistant Performance")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Citation accuracy | 96% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep "internal evaluation" label |
| Data privacy (no cloud path) | 100% | VERIFIED | Architectural fact — offline mode has no cloud path (see lawyer-assistant-rag-pipeline-privacy-first-legal-ai.html) | None |
| Search recall | 94% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep label |
| Setup time reduction | 90% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply comparison baseline, or keep label |

### GPT Calendar ("Smart Calendar Performance")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Voice command accuracy | 93% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep label |
| SMS parsing accuracy | 96% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep label |
| On-device privacy | 100% | VERIFIED | Architectural fact — on-device AI mode | None |
| Apps replaced | 5 → 1 | VERIFIED | Product scope — calendar, reminders, finance, location alerts, tasks in one app | None |

### GGUFLoader ("GGUF Loader Performance")

| Metric | Value | Status | Source / method | Action |
|---|---|---|---|---|
| Setup time reduction | 85% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply comparison baseline, or keep label |
| Memory efficiency | 78% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply measurement method, or keep label |
| Multilingual accuracy | 92% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep label |
| Plugin compatibility | 95% | UNVERIFIED | Internal figure; no methodology on file | Owner to supply test set + sample size, or keep label |

---

## Resolution applied in this pass (Aug 12, 2026)

1. All three stat charts on `index.html` now carry the footnote
   *"Internal evaluation figures from development testing."* — the numbers stay visible but are no
   longer presented as externally verifiable facts.
2. The 10 `UNVERIFIED` metrics above are blocked from unqualified publication. When the owner
   supplies a source or measurement method, update each row to `PARTIAL`/`VERIFIED`, reword the
   footnote on `index.html`, and this ledger is the record of that change.
3. All 10 numbers' exact locations are the `stat-value` spans in `index.html`
   (96% / 100% / 94% / 90% — Lawyer Assistant; 93% / 96% / 100% / 5 → 1 — GPT Calendar;
   85% / 78% / 92% / 95% — GGUFLoader).

## Rules going forward

- Any new metric added to any page gets a row here **in the same edit** — no orphan claims.
- Metrics with no row in this ledger fail the framework quality gate and are rejected.
- This file is internal documentation; it is not linked from public pages.
