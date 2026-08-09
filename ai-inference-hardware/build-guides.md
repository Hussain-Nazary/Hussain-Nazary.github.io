# Local-AI Build Guides (August 2026)

**Three builds — Budget, Mid, High — tuned for the newest models from the Aug 2026 cheat-sheet, priced at real August 2026 street prices.** Every model below is a current-gen pick (Gemma 3 27B, GLM-4.7-Flash, Devstral 2/Small 2, Ministral 3, Qwen3.5/Gemma 4 sub-12B, Mistral Medium 3, Voxtral Transcribe 2, Qwen Image 3.0). Speeds are single-stream decode from the [compatibility matrix](compatibility-matrix.md).

## ⚠️ Read this first: the 2026 hardware market

Prices below are **August 2026 US street prices**, not MSRPs — and the 2026 market is defined by three shortages:

- **GPU prices are 50–150% above MSRP.** GDDR7 memory shortages pushed the RTX 5090 to ~$3,600–4,800 street (MSRP $1,999), the RTX 5080 to ~$1,150–1,480 ($999 MSRP), and the 5070 Ti to ~$870–1,420 ($749 MSRP). Used RTX 4090s now cost ~$2,200–2,400. Sources: bestvaluegpu.com price trackers (Aug 2026), Tom's Hardware, Tech Insider GPU price report.
- **The RAMpocalypse.** AI memory demand tripled–quadrupled DRAM prices: 32 GB DDR4 went ~$70 → ~$150–260, 32 GB DDR5-6000 went <$90 → ~$380–530, 64 GB DDR5 went ~$150 → ~$600–1,000. Sources: Tom's Hardware RAM price index, TechPowerUp.
- **NAND/SSD prices doubled+.** 1 TB NVMe went ~$55 → ~$150–330. Sources: Tom's Hardware SSD pricing report, Tech Insider.

**What this means for these guides:** the pre-shortage "$500 build" is now ~$650; the "24 GB for $1,500" dream (used 4090) now costs ~$3,000. The guides below are honest about that — and the [DGX Spark](ai-desktops.md) has quietly become the best $5K capacity buy of 2026 because a 128 GB unified system now undercuts a 32 GB DIY build.

---

## Build 1 — Budget: "The Starter" (~$650; was ~$500 pre-shortage)

**Goal:** run the newest sub-14B models at usable speed + full voice/RAG/vision stack on a 12 GB card.

| Part | Pick | Price (Aug 2026) |
|---|---|---|
| GPU | **Used RTX 3060 12 GB** (used, eBay avg ~$230; range $205–250) | $230 |
| CPU | AMD Ryzen 5 5600 (new $130 / used ~$95) | $130 |
| Motherboard | B550 (new ~$85 / used ~$60) | $85 |
| RAM | 16 GB (2×8) DDR4-3200 — RAMpocalypse pricing | $90 |
| SSD | 500 GB NVMe (NAND shortage pricing) | $100 |
| PSU | 550 W 80+ Bronze | $50 |
| Case | mATX case | $50 |
| **Total** | | **~$735** (new parts) / **~$665** (used CPU + board) |

**Getting closer to $500:** buy the CPU, board, and case used (~$665 total); drop the SSD to 250 GB (~$70); or accept an 8 GB card (used RTX 3050, ~$140) — but that locks you out of Ministral 3 14B. **Honest note:** the memory shortage is what broke $500; RAM and SSDs won't fall before 2027.

**Newest-model stack (what this runs):**
- **Ministral 3 14B Q4** (8.6 GB) → 40–55 tok/s — the flagship pick for this tier
- **Ministral 3 8B** + **Qwen3.5 / Gemma 4 sub-12B** (2026 line) → 60–90 tok/s
- **Devstral Small 2** (coding) → 60–80 tok/s
- **Voxtral Transcribe 2** (on-device ASR) + **Qwen3-Embedding / bge-m3** (RAG) — instant
- **YOLOv11n** (vision) → 100+ FPS; **SDXL / FLUX.1-schnell fp8** (image, bonus)

**What it can't run:** Gemma 3 27B and GLM-4.7-Flash (need 16–24 GB); Devstral 2 Q4 (14 GB needs 16 GB); Mistral Medium 3 (needs 48 GB+). That's the mid build.

**Setup:** Ollama + Open WebUI (or llama.cpp), ComfyUI. Alternative GPU: used RTX 2080 Ti 11 GB (~$220, more bandwidth, 1 GB less VRAM) or new Arc B580 12 GB (~$250–310, but no CUDA — llama.cpp/IPEX-LLM only, ~30–45 tok/s on 8B).

**Upgrade path:** +$800 to the mid build (used 5060 Ti 16 GB + 32 GB DDR5).

---

## Build 2 — Mid: "The 16 GB Value" (~$1,500)

**Goal:** run the newest models at their practical consumer tier — 14B at Q4, and Gemma 3 27B / GLM-4.7-Flash at Q3.

| Part | Pick | Price (Aug 2026) |
|---|---|---|
| GPU | **Used RTX 5060 Ti 16 GB** (Blackwell, FP4; used ~$370–420; new ~$580–680) | $400 |
| CPU | AMD Ryzen 5 7600 | $200 |
| Motherboard | B650 | $130 |
| RAM | **32 GB (2×16) DDR5-6000** — RAMpocalypse pricing | $420 |
| SSD | 1 TB NVMe | $170 |
| PSU | 650 W 80+ Bronze | $75 |
| Case | mid-tower | $70 |
| **Total** | | **~$1,465** |

**Why the used 5060 Ti 16 GB:** in the 2026 market it's the cheapest way to 16 GB of *Blackwell* VRAM with CUDA (~$400 used). Alternatives: RX 9070 XT 16 GB new (~$650–710 — more compute, same VRAM, but ROCm not CUDA), or used 5070 Ti 16 GB (~$870 — faster, same VRAM, not worth +$470 for AI).

**Newest-model stack:**
- **Gemma 3 27B Q3** (Jul 2026) → 30–40 tok/s — runs, but only at Q3 on 16 GB (Q4 needs 24 GB)
- **GLM-4.7-Flash Q3** (30B-A3B) → 30–40 tok/s — same Q3 caveat
- **Devstral 2 Q4** (24B coding, Dec 2025) → 45–60 tok/s — fits 16 GB
- **Ministral 3 14B Q4** → 60–75 tok/s; **8B / Qwen3.5 / Gemma 4 sub-12B** → 100–120 tok/s
- **Qwen Image 3.0 / Muse Spark 1.2** (Aug 2026) → comfortable image generation
- **Voxtral Transcribe 2**, **Qwen3-Embedding**, **Kokoro** → instant

**What it can't run (the honest 2026 gap):** Gemma 3 27B and GLM-4.7-Flash **at Q4** — that needs 24 GB, and 24 GB (used 4090) now costs ~$2,200–2,400, pushing a 24 GB build to **~$3,000–3,200**. If 24 GB is the goal, that's the real price of admission in Aug 2026; wait for memory prices to normalize (2027+) if you can.

**Setup:** Ollama/llama.cpp + Open WebUI; ComfyUI; TensorRT-LLM or vLLM for batched serving.

**Upgrade path:** the used 4090 swap (+~$1,900) is the only path to the full Q4 experience; alternatively add 32 GB more RAM for CPU offload of 27–30B models.

---

## Build 3 — High: "The Flagship" (~$5,500; range $5,300–6,300)

**Goal:** max speed on every newest model that fits 32 GB, plus a turnkey capacity alternative that beats it on model size.

| Part | Pick | Price (Aug 2026) |
|---|---|---|
| GPU | **RTX 5090 32 GB** — street ~$3,600–4,800 (MSRP $1,999; Microcenter ~$3,300–3,700, used ~$3,590) | $3,700 |
| CPU | AMD Ryzen 7 9800X3D (back-to-school low ~$380–415) | $390 |
| Motherboard | X870E (2× PCIe 5.0 x16 — room for a second GPU later) | $300 |
| RAM | 32 GB (2×16) DDR5-6000 — 64 GB costs ~$700–1,000 in 2026, see note | $420 |
| SSD | 2 TB Gen4 NVMe (NAND shortage pricing) | $350 |
| PSU | 1200 W ATX 3.0 (headroom for a second GPU) | $220 |
| Case + cooler | full-tower + 360 AIO | $280 |
| **Total** | | **~$5,660** (~$5,300 at a $3,600 5090 deal; ~$6,300 at $4,800) |

**Why this shape:** the 5090's 32 GB + 1.79 TB/s is the fastest consumer inference setup — every newest model ≤32 GB runs at full speed. The X870E + 1200 W PSU leave a clear second-GPU upgrade path (though a used 4090 now costs ~$2,300 — as much as the entire mid build).

**Newest-model stack:**
- **Gemma 3 27B Q4** → 60–90 tok/s; **GLM-4.7-Flash Q4** → 55–80 tok/s; **Devstral 2** → 70–100 tok/s — all at Q4, full speed
- **Mistral Medium 3 Q4** (~28 GB, Jul 2026) → 40–50 tok/s ⚠ (limited context — 28 GB model on a 32 GB card)
- **Qwen Image 3.0 Pro / Muse Spark 1.2** → seconds per image; **Voxtral 2**, **Qwen3-Embedding**, **Kokoro** → instant
- **MiniMax M2.5** (230B): API-only here (Q4 ≈ 130 GB) — at ~$1/hour it's a speed question, not a cost one

**What it can't run:** gpt-oss-120B Q4 (70 GB — needs 96 GB+, RTX PRO 6000/DGX Station territory); Qwen2.5-VL-72B (41 GB — needs the second-GPU path); GLM-5.2 / Mistral Large 3 / DeepSeek V4 Flash / Kimi K3 (API/enterprise).

**RAM note:** 32 GB system RAM is enough for everything above (the GPU holds the models). 64 GB DDR5 at $700–1,000 only pays off for CPU offload of 70B-class — probably not worth it in 2026; wait for prices to fall.

**Turnkey alternative — NVIDIA DGX Spark ($4,699 official, retail $4,000–5,600):** 128 GB unified memory trades speed for capacity — and in the 2026 market it now *undercuts* a 32 GB DIY build while running bigger models: **Mistral Medium 3** (6–8 tok/s), **gpt-oss-120B Q4** (4–6 tok/s), **MiniMax M2.5 Q4** right at the edge (~130 GB), plus every sub-30B model at 15–40 tok/s. Zero building, CUDA everywhere, 200 W silent.

**Honest verdict for $5K in Aug 2026:** buy the **5090 desktop** if you want max speed on 27–30B models plus gaming/image-gen versatility. Buy the **DGX Spark** if you want to run the *biggest* newest models (up to 120B) out of the box — it's cheaper than the 5090 build and holds 4× the model.

---

## Three builds at a glance

| | Budget ~$665–735 | Mid ~$1,465 | High ~$5,300–6,300 |
|---|---|---|---|
| GPU / VRAM | Used 3060 12 GB | Used 5060 Ti 16 GB | 5090 32 GB |
| Top newest model | Ministral 3 14B Q4 (40–55 tok/s) | Devstral 2 Q4; 27B/30B at Q3 | Gemma 3 27B + GLM-4.7-Flash Q4; Mistral Medium 3 ⚠ |
| Fastest daily driver | Ministral 3 8B / Qwen3.5 (60–90 tok/s) | Ministral 3 14B (60–75 tok/s) | Gemma 3 27B (60–90 tok/s) |
| Image gen | SDXL / FLUX-schnell fp8 | Qwen Image 3.0 | Qwen Image 3.0 Pro |
| Voice | Voxtral 2, Kokoro | Voxtral 2, Kokoro | Voxtral 2, Kokoro |
| Can't run | 27B+, Devstral 2 Q4 | 27B/30B at Q4 (needs 24 GB = ~$3K) | gpt-oss-120B, 72B vision (second GPU), MoE giants |
| Power draw | ~350 W | ~450 W | ~800 W |
| Biggest 2026 gotcha | RAM/SSD shortage ate the $500 budget | 24 GB used 4090 now ~$2,300 | 5090 street price swings $3,600–4,800 |

## Software stack (all builds)

- **LLMs:** Ollama or llama.cpp + Open WebUI / anything-LLM
- **Vision/image:** ComfyUI (Qwen Image 3.0, SDXL), YOLO via Ultralytics
- **Voice:** Voxtral Transcribe 2 (on-device STT), Kokoro TTS
- **RAG:** Qwen3-Embedding or bge-m3 + your vector DB of choice
- **Serving (power users):** vLLM or TensorRT-LLM for batched throughput

## The upgrade ladder (Aug 2026 prices)

1. **~$665–735** → 12 GB: newest ≤14B models (Ministral 3, Qwen3.5, Gemma 4)
2. **~$1,465** → 16 GB: Devstral 2 at Q4; Gemma 3 27B / GLM-4.7-Flash at Q3
3. **~$3,000–3,200** → 24 GB (used 4090 ~$2,300 + rest): **the full Q4 experience** — Gemma 3 27B and GLM-4.7-Flash at Q4
4. **~$5,300–6,300** → 32 GB (5090): max speed on everything ≤32 GB + Mistral Medium 3
5. **~$4,700** (alternative) → DGX Spark: 128 GB capacity up to 120B out of the box, slower decode
6. **~$70K+** → DGX Station: the newest MoE giants (GLM-5.2, Mistral Large 3, MiniMax M2.5) locally

## Price sources (August 2026)

- bestvaluegpu.com US price trackers (RTX 5090/5080/5070 Ti/5070/5060 Ti/4090/3060/B580, RX 9070 XT) — Aug 2026
- Tom's Hardware: RAM price index (Aug 2026), SSD pricing report (Jul 2026), GPU street-price coverage
- TechPowerUp: DDR4 price surge thread (Jan 2026); Tech Insider: Gaming GPU Prices 2026 (Jul 2026)
- NVIDIA marketplace (DGX Spark $4,699), Best Buy listings, camelcamelcamel price history

*Prices are US street estimates and move weekly in this market — re-check [consumer-gpus.md](consumer-gpus.md) and the trackers above before buying. Non-GPU commodity parts (PSU, case, cooler) are stable estimates.*
