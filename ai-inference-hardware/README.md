# AI Inference Hardware Guide (2025–2026)

*A complete reference on recent PCs, GPUs, and specialized chips built for AI inference — with full specs and an AI model recommendation for every device. Last updated: August 2026.*

## How to use this guide

Each category has its own file with full specifications and per-device **model recommendations** (which models fit in memory, which quantizations to use, and roughly how fast they run):

| File | Covers |
|---|---|
| **[compatibility-matrix.md](compatibility-matrix.md)** | **The master lookup: every model × every device, with fit/quantization/speed** |
| **[build-guides.md](build-guides.md)** | **Three concrete builds (Budget ~$665–735 / Mid ~$1,465 / High ~$5,300–6,300) for the newest models** |
| **[prices.md](prices.md)** | **Live price tracker: MSRP vs Aug 2026 street price for every component, with sources & check dates** |
| **[laptop-ai-guide.md](laptop-ai-guide.md)** | **Best-value laptops for local LLMs: M5 Max, Snapdragon X2, Ryzen AI 400 at Aug 2026 prices** |
| [consumer-gpus.md](consumer-gpus.md) | RTX 50-series, RTX 4090, AMD RX 9070 XT, Intel Arc |
| [ai-desktops.md](ai-desktops.md) | DGX Spark, DGX Station, AI mini-PCs, Mac Studio |
| [ai-pc-processors.md](ai-pc-processors.md) | Laptop NPUs: Lunar Lake, Strix Point, Snapdragon X/X2, Panther Lake, Ryzen AI 400 |
| [apple-silicon.md](apple-silicon.md) | M4, M5, M5 Pro/Max/Ultra |
| [datacenter-gpus.md](datacenter-gpus.md) | NVIDIA B200/B300/H200, AMD MI355X, Intel Gaudi 3, Crescent Island |
| [inference-asics.md](inference-asics.md) | Cerebras, Groq, SambaNova (inference-first chips) |
| [hyperscaler-silicon.md](hyperscaler-silicon.md) | Google TPU v7 Ironwood, AWS Trainium/Inferentia, Microsoft Maia, Meta MTIA |
| [edge-embedded.md](edge-embedded.md) | Jetson Thor/Orin, Hailo, Google Coral, Raspberry Pi AI Kit |

**🌐 Web versions (one page per pick, blog format):** [the $665 AI machine](../the-665-dollar-ai-machine.html) · [the $900 AI laptop](../the-900-dollar-ai-laptop-60-tops.html) · [the $1,465 AI tower](../the-1465-dollar-16gb-ai-tower.html) · [the 48 GB AI laptop](../the-48gb-ai-laptop-that-runs-all-day.html) · [the $3,000 24 GB machine](../the-3000-dollar-24gb-q4-sweet-spot.html) · [the $6,300 speed monster](../the-6300-dollar-ai-speed-monster.html) · [the only laptop that runs 120B models](../the-only-laptop-that-runs-120b-models.html) · [the $4,700 AI supercomputer](../the-4700-dollar-ai-supercomputer-on-your-desk.html)

## Model recommendation policy: newest first

**Every recommendation in this guide leads with the most recently launched models** that fit the hardware, with older generation models listed only as fallbacks. The open-model release cadence in 2026 is relentless (nine open launches in twelve days in July alone), so check the cheat-sheet below and refresh monthly.

## 🌟 Newest models cheat-sheet (August 2026)

*The current generation to recommend first, by tier. Older models (Llama 3.3, Qwen2.5, DeepSeek-R1-Distill, Phi-4, SDXL/FLUX) are now second choices.*

| Tier | Newest picks | Launched | Notes |
|---|---|---|---|
| **Frontier open (API/datacenter)** | DeepSeek V4 Flash 0731 | Jul 31, 2026 | Value king: ~79% SWE-bench Verified, 91.6% LiveCodeBench, dirt cheap (MoE, API-first) |
| | GLM-5.2 | Jun 13, 2026 | Open agentic leader (~744B total MoE) |
| | Kimi K3 | Jul 27, 2026 (weights) | Moonshot flagship — strong open coding/reasoning, native multimodal |
| | MiniMax M2.5 | Feb 12, 2026 | 230B total / 10B active MoE, open weights, ~$1/hour — "intelligence too cheap to meter" |
| | Mistral Large 3 | Dec 2, 2025 | 675B total / 41B active MoE, Apache 2.0, #2 open on LMArena |
| | Qwen3-Coder-Next | Feb 2026 | Open MoE coder, 256K context |
| **Mid-size local (24–48 GB)** | Gemma 3 27B | Jul 2026 | **The practical self-host pick** — Q4 fits a 24 GB GPU, multimodal |
| | Mistral Medium 3 | Jul 2026 | 48GB-class machine, or API |
| | GLM-4.7-Flash | Jan 20, 2026 | 30B-A3B MoE — strongest in the 30B class, 128K context, local-friendly |
| | Devstral 2 / Devstral Small 2 | Dec 10, 2025 | 24B open coding model (beats Qwen3-Coder-30B) |
| **Small / edge (≤14B)** | Qwen3.5 sub-12B line | 2026 | The recent practical laptop-class option |
| | Gemma 4 sub-12B line | 2026 | Same tier, Google's latest small models |
| | Ministral 3 (3B/8B/14B) | Dec 2, 2025 | Optimized for RTX PCs, DGX Spark, Jetson; 14B reasoning = 85% AIME 2025 |
| **Vision/multimodal** | Gemma 3 27B, Kimi K3 | 2026 | Newest open multimodal; Qwen2.5-VL as workhorse fallback |
| **Image generation** | Qwen Image 3.0 / 3.0 Pro, Muse Spark 1.2 | Aug 2026 | Open text-to-image, latest releases |
| **Speech (ASR)** | Voxtral Transcribe 2 | Feb 4, 2026 | On-device STT with real-time diarization — beats Whisper on FLEURS; Whisper as fallback |
| **Coding (local)** | Devstral 2 / Small 2, GLM-4.7-Flash | Dec 2025–Jan 2026 | Newest open coding models that fit consumer hardware |
| **Embeddings/RAG** | Qwen3-Embedding, bge-m3 | 2025 | Still the standard for RAG |
| **Closed API (no local)** | GPT-5.3-Codex, Claude Opus 4.6, Gemini 3 Deep Think | Feb 2026 | Cloud-only; benchmark references |

---

## Quick picks (August 2026)

- **Best local-LLM desktop GPU:** NVIDIA RTX 5090 (32 GB GDDR7 — ~$3,600–4,800 street in the Aug 2026 shortage, MSRP $1,999) — runs Gemma 3 27B / GLM-4.7-Flash at speed; biggest consumer models.
- **Best local-LLM laptop:** Apple MacBook Pro M5 Max (up to 128 GB unified) or Snapdragon X2 Elite for pure NPU throughput.
- **Best turnkey AI desktop:** NVIDIA DGX Spark (128 GB unified, ~$4.7K) — runs up to 200B-parameter models out of the box.
- **Best budget GPU for AI (Aug 2026):** used RTX 3060 12 GB (~$220) or Arc B580 (~$280) under $300; best 16 GB value is a used RTX 5060 Ti (~$400); the 24 GB tier (used 4090) now runs ~$2,200–2,400. See [build-guides.md](build-guides.md) for full builds.
- **Fastest cloud inference:** Cerebras (2,000–3,000+ tok/s) and Groq LPUs; best cost-per-token at scale: AWS Trainium, Google TPU v7 (both serve the newest open MoE giants).
- **Best edge module:** NVIDIA Jetson Thor (2,070 FP4 TFLOPS, 128 GB — runs Ministral 3 and GLM-4.7-Flash on-device); Jetson Orin Nano Super (~$250) for budget edge AI.

### Cheapest laptop per NPU tier (Aug 2026)

| NPU tier (chip) | NPU TOPS | Cheapest realistic pick | Street price (Aug 2026) |
|---|---|---|---|
| Snapdragon X2 Elite / Plus ("Glymur") | 80–85 | Microsoft Surface Laptop 13.8″ (8th Ed); deals to ~$1,080 | ~$1,080–1,400 |
| Ryzen AI 400 (Medusa Point) | 60 | ASUS Zenbook 14 (Ryzen AI 9 465; open-box from ~$714) | ~$750–1,200 |
| Strix Point (Ryzen AI 300, HX 370) | 50 | mid-tier HX 370 ultrabooks | ~$900–1,200 |
| Intel Panther Lake (Core Ultra 300) | ~50 | HP OmniBook X Flip (Walmart listing) | ~$999 |
| Intel Lunar Lake (Core Ultra 200V) | 48 | 2024–25 budget stock (deep discounts) | ~$600 |
| Snapdragon X Elite / X Plus | 45 | budget X Plus stock (Qualcomm "from $599"); X Elite from ~$1,000 | ~$600–1,000 |
| Apple M5 / M4 (Neural Engine) | ~38 | MacBook Air M5 (16-core NE) | ~$1,099 (M4 Air from $999) |

*Prices are cheapest street configs (typically 16–32 GB RAM; the RAMpocalypse taxes higher capacities). All tiers run the same newest small-model stack (Ministral 3, Qwen3.5, Gemma 4) — the NPU number mostly decides battery life for always-on AI, not which models fit. Sources & full ranges: [prices.md](prices.md) §8.*

### Laptop vs desktop at each budget (Aug 2026)

| Budget | Desktop pick (from [build-guides.md](build-guides.md)) | Laptop pick (from [laptop-ai-guide.md](laptop-ai-guide.md)) | The honest trade-off | Form factor (battery / noise / power / repairability) |
|---|---|---|---|---|
| ~$700–1,000 | Budget tower — used RTX 3060 12 GB (~$665–735): Ministral 3 14B Q4 @ 40–55 tok/s | Zenbook 14, Ryzen AI 9 465 (~$900–1,150): 8B @ 25–40 tok/s + 60 TOPS NPU | Desktop runs one tier bigger and ~35% faster per dollar; laptop is portable and battery-efficient | Desktop: none / fans audible under load / ~12 W idle, ~275 W load / **9/10** — full ATX: socketed CPU, DIMM slots, PCIe GPU, standard PSU. Laptop: 8–12 h light, ~3 h sustained LLM / quiet / 65 W charger / **4/10 est.** — RAM soldered; SSD & battery swappable |
| ~$1,500 | Mid tower — used RTX 5060 Ti 16 GB (~$1,465): Devstral 2 Q4, 27B/30B at Q3 | Vivobook S16 X2 Elite 48 GB (~$1,599): 14B @ 20–30 tok/s, 8B on NPU | Desktop unlocks the 24–30B tier (Q3/Q4); laptop caps at 14B but gives all-day on-device AI | Desktop: none / moderate fan noise / ~400 W / **9/10** — full ATX. Laptop: 15–20 h light, all-day on NPU / near-silent / 65 W charger / **4/10 est.** — 48 GB RAM soldered fixed; SSD & battery swappable |
| ~$3,000 | **Desktop-only tier** — used RTX 4090 24 GB (~$3,000–3,200): Gemma 3 27B + GLM-4.7-Flash at full Q4 | — (no laptop equivalent) | The full-Q4 27–30B experience has no laptop answer in 2026 | Desktop: none / 4090 loud at 450 W (35 dBA) / ~7–33 W idle, ~650 W load / **9/10** — ATX; used card: plan repaste + check the 12VHPWR connector |
| ~$5,200–6,300 | High tower — RTX 5090 32 GB (~$5,300–6,300): 27–30B @ 60–90 tok/s, Mistral Medium 3 ⚠ | M5 Max 128 GB (~$5,200–5,900): 27–30B @ 40–55 tok/s, **plus** Mistral Medium 3, gpt-oss-120B, 72B vision | **The 2026 inversion:** the laptop holds *bigger* models (128 GB unified > 32 GB VRAM); the desktop is *faster* on what fits (1.79 TB/s vs ~700 GB/s) | Desktop: none / 5090 loud at 575 W (40 dBA) / ~30–46 W idle, ~800 W load / **9/10** — ATX, GPU swappable. Laptop: 15–20 h light, ~3–5 h sustained LLM / silent at idle, fans on under max load / 140 W charger, ~100 W sustained (147 W peak) / **4/10 (iFixit)** — RAM & SSD soldered, Apple repairs pricey |
| ~$4,700 (turnkey) | DGX Spark — 128 GB unified, capacity to 120B, slow decode | — | The Spark is the "desktop that holds laptop-class memory" — same 128 GB capacity class as the M5 Max | No battery / quiet SFF (minor coil whine) / ~25–45 W idle, ~150 W load / **4/10 est.** — 128 GB RAM soldered on-package; 2242 SSD user-swappable |

*Form factor cell format: battery life · noise · power draw · repairability (iFixit-style 0–10, 10 = easiest; "est." = scored from teardown reports, no official iFixit score). Power draw = system under sustained LLM load (GPU TDP + platform); noise notes assume a mid-tower case with decent fans.*

**Repairability scores & teardown sources:**
- **M5 MacBook Pro — 4/10 (official):** [iFixit M5 MacBook Pro teardown](https://www.ifixit.com/News/114046/m5-macbook-pro-teardown) · [9to5Mac summary](https://9to5mac.com/2025/10/24/ifixit-tears-down-the-m5-macbook-pro-and-finds-small-but-welcome-repairability-improvements/) · [iFixit device page (16″ 2026)](https://www.ifixit.com/Device/MacBook_Pro_16%22_2026)
- **DGX Spark — 4/10 (est.):** [ChargerLAB teardown](https://www.chargerlab.com/teardown-of-nvidia-dgx-spark-4tb) · [Level1Techs — SSD swap](https://forum.level1techs.com/t/nvidias-dgx-spark-review-and-first-impressions/238661) · [ASUS SSD-upgrade video](https://www.youtube.com/watch?v=T-PAmyJemno)
- **Zenbook 14 — 4/10 (est.):** [LaptopMedia disassembly (UM3402)](https://www.youtube.com/watch?v=65iEsDUERHw) · [iFixit Q&A — RAM soldered](https://www.ifixit.com/Answers/View/942180/Help+with+upgrading+Storage+and+RAM)
- **Vivobook S16 — 4/10 (est.):** [LaptopMedia Vivobook 16 (X1607) disassembly](https://laptopmedia.com/guides/how-to-open-asus-vivobook-16-x1607-disassembly-and-upgrade-options/) · [r/ASUS — soldered RAM](https://www.reddit.com/r/ASUS/comments/1od8p5g/ram_upgradability_on_the_vivobook_s16/)
- **ATX towers (all three builds) — 9/10:** the standard parts *are* the repairability — socketed CPU, DIMM slots, PCIe GPU, standard PSU, no glue; any part swaps in minutes and used replacements are cheap. GPU cards themselves aren't field-repairable beyond repaste/cleaning — the repair is a whole-card swap. On used 4090s, check the 12VHPWR connector and budget for repaste.

#### Measured power & noise (from 2025–26 reviews)

*Measured at the wall where noted; "GPU" figures are card-only, "system" figures include the rest of the PC. "est." = no direct measurement found, estimated from comparable hardware/reports.*

| Pick | Idle power | Load power | Noise | Sources |
|---|---|---|---|---|
| RTX 3060 12 GB (budget tower) | ~12 W (GPU) | ~175 W GPU · ~275 W system | 0 dBA idle (fans off) · ~28–32 dBA load (est.) | [igorslab review](https://www.igorslab.de/en/nvidia-geforce-rtx-3060-12-gb-in-test-with-a-board-partner-card-what-can-the-msi-rtx-3060-gaming-x-trio-be-an-ampere-entry-drug/12/) |
| RTX 4090 FE (24 GB tower) | ~7–33 W (GPU; display-count dependent) | ~450 W GPU (peak 461 W) · ~650 W system | **35 dBA** at full load | [TechPowerUp power](https://www.techpowerup.com/review/nvidia-geforce-rtx-4090-founders-edition/39.html) · [TechPowerUp noise](https://www.techpowerup.com/review/nvidia-geforce-rtx-4090-founders-edition/42.html) · [ServeTheHome](https://www.servethehome.com/nvidia-geforce-rtx-4090-founders-edition-review-the-gpu/7/) |
| RTX 5090 FE (high tower) | ~30 W (TPU) · ~46 W (GN desktop) | 575 W TDP · ~600–650 W measured · ~800 W system | **40 dBA** at full load | [TechPowerUp](https://www.techpowerup.com/review/nvidia-geforce-rtx-5090-founders-edition/46.html) · [GamersNexus](https://gamersnexus.net/gpus/nvidia-geforce-rtx-5090-founders-edition-review-benchmarks-gaming-thermals-power) · [LANOC](https://lanoc.org/review/video-cards/nvidia-rtx-5090-founders-edition?start=8) |
| DGX Spark | ~40–45 W at launch → **~25 W after Feb 2026 update** | ~135–145 W from the wall during LLM runs (240 W PSU) | quiet; minor coil whine reported | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-dgx-spark-update-cuts-idle-power-by-32-percent-or-more-hot-plug-detection-on-connectx-nic-makes-for-a-more-efficient-ai-workstation) · [ServeTheHome](https://www.servethehome.com/nvidia-dgx-spark-review-the-gb10-machine-is-so-freaking-cool/4/) · [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1o7gpr8/got_the_dgx_spark_ask_me_anything/) |
| M5 Max MacBook Pro 16″ | ~5–10 W (screen on; est.) | ~98 W sustained · ~147 W peak (140 W adapter) | 0 dB idle (fans off) · ~38–45 dBA max under heavy load (est.) | [Apple tech specs](https://support.apple.com/en-us/126319) · [power measurements (r/macbook)](https://www.reddit.com/r/macbook/comments/1rqgube/m5_max_with_inconsistent_performance_and/) · [Skorppio efficiency test](https://skorppio.com/blog/dgx-spark-vs-mac-studio-efficiency-benchmark) |

#### Cost per token & per watt (Aug 2026)

*Method: hardware price + electricity amortized over **2 h/day of sustained single-stream inference** at each pick's flagship speed (midpoint from [compatibility-matrix.md](compatibility-matrix.md)). Desktops amortized over 5 yr, laptops 4 yr (battery/soldered-RAM life); **$0.17/kWh** US average. Draw = sustained LLM-load figure from the form-factor column.*

| Pick | Price | Flagship run (tok/s) | System draw | $/M tokens | $/W | Tokens/kWh |
|---|---|---|---|---|---|---|
| Budget tower · RTX 3060 12 GB | ~$700 | Ministral 3 14B Q4 · 47 | ~275 W | **~$1.4** | $2.5 | ~0.62M |
| Zenbook 14 · Ryzen AI 9 465 | ~$1,025 | Ministral 3 8B · 32 | ~45 W | ~$3.1 | $23 | ~2.6M |
| Mid tower · RTX 5060 Ti 16 GB | ~$1,465 | Devstral 2 Q4 · 52 | ~400 W | ~$2.5 | $3.7 | ~0.47M |
| Vivobook S16 · X2 Elite 48 GB | ~$1,599 | 14B · 25 (8B on NPU · 30) | ~50 W | ~$5.1–6.2 | $32 | ~3.6M (NPU) |
| 24 GB tower · used RTX 4090 | ~$3,100 | Gemma 3 27B Q4 · 47 | ~650 W | ~$5.7 | $4.8 | ~0.26M |
| High tower · RTX 5090 | ~$5,800 | Gemma 3 27B Q4 · 75 | ~800 W | ~$6.5 | $7.3 | ~0.34M |
| M5 Max 128 GB | ~$5,550 | Gemma 3 27B Q4 · 47 | ~100 W | ~$11.3 | $56 | ~1.7M |
| DGX Spark | $4,699 | Gemma 3 27B · 15 | ~150 W | ~$24 | $31 | ~0.36M |

**What the numbers say:**
- The **used-3060 budget tower is the cheapest per token** (~$1.4/M) — every step up the price ladder pays for *capacity and quality* (full Q4 on 27–30B, bigger models, image gen), not token economy.
- **Same-model comparison:** Gemma 3 27B Q4 runs ~47 tok/s on both the 4090 tower and the M5 Max — but ~650 W vs ~100 W makes the Mac ~6.5× more energy-efficient (1.7M vs 0.26M tokens/kWh). At high electricity rates the Mac's per-token gap closes fast.
- **$/W is the "desktop value" metric:** ATX towers land at $2–7/W (dense, cheap); laptops **and the Spark** at $23–56/W — portability or miniaturization carries the premium. Low $/W = more machine per watt, not more tokens per watt.
- **DGX Spark is the worst cost-per-token** (~$24/M) — it's bought for 120B capacity and zero assembly, not speed or economy.
- **Sensitivity:** at $0.30–0.50/kWh (EU/California rates), the 800 W 5090 tower's 5-yr energy bill climbs from ~$500 to ~$880–1,460 and its $/M rises to ~$6.8–7.4; the laptops and M5 Max move <$0.50/M. High-rate regions favor the efficient machines.

**Bottom line:** under $5K the **desktop wins for LLMs per dollar** (VRAM > everything — see the [fitting math](README.md#model-fitting-math-read-this-before-the-category-files) below). At $5K+ the rules invert: the **M5 Max laptop and DGX Spark (128 GB unified) beat a 5090 tower on model capacity**, while the tower wins on speed and image gen. The 24 GB Q4 sweet spot (~$3,000) is desktop-only.

#### Cloud/API alternatives: same workload, cost per token (Aug 2026)

*Same usage envelope as the local table: **338K output tokens/day** (2 h/day at the budget tower's 47 tok/s), **3:1 input:output** ratio, cache-miss pricing. Sources: [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing/) · [OpenAI pricing](https://developers.openai.com/api/docs/pricing) · [Anthropic Opus 4.6 announcement](https://www.anthropic.com/news/claude-opus-4-6). Checked Aug 9, 2026.*

| API model | Input $/M | Output $/M | Cost/day | Cost/5 yr | vs budget tower (~$871/5 yr) |
|---|---|---|---|---|---|
| **DeepSeek V4 Flash 0731** (value king) | $0.14 | $0.28 | ~$0.24 | ~$430 | **API is cheaper than every local build** |
| **GPT-5.3-Codex** (closed) | $1.75 | $14.00 | ~$6.51 | ~$11,900 | local is 13.6× cheaper |
| **Claude Opus 4.6** (closed) | $5.00 | $25.00 | ~$13.54 | ~$24,700 | local is 28× cheaper |

| Local pick (5-yr amortized) | DeepSeek V4 Flash (~$430) | GPT-5.3-Codex (~$11,900) | Claude Opus 4.6 (~$24,700) |
|---|---|---|---|
| Budget tower · ~$871 | API ~2× cheaper | local ~14× cheaper | local ~28× cheaper |
| Mid tower · ~$1,713 | API ~4× cheaper | local ~7× cheaper | local ~14× cheaper |
| 24 GB tower · ~$3,503 | API ~8× cheaper | local ~3.4× cheaper | local ~7× cheaper |
| High tower · ~$6,296 | API ~15× cheaper | local ~1.9× cheaper | local ~4× cheaper |
| M5 Max · ~$5,600 | API ~13× cheaper | local ~2.1× cheaper | local ~4.4× cheaper |
| DGX Spark · ~$4,792 | API ~11× cheaper | local ~2.5× cheaper | local ~5.2× cheaper |

**Break-even (heavy daily use):** GPT-5.3-Codex pays for the budget tower in **~4.5 months** and the 5090 tower in **~2.6 years**; Claude Opus 4.6 pays for the budget tower in **~2 months** and the 5090 tower in **~15 months**. DeepSeek V4 Flash **never** breaks even — at this usage the API is simply cheaper for five straight years.

**What this means:**
- The cheapest *local* token (~$1.4/M on the used-3060 tower) is still ~2× pricier than the cheapest *API* token (DeepSeek at ~$0.21/M blended). **Local's value is not raw cost** — it's privacy, offline use, data residency, no rate limits, and predictable bills.
- **The frontier closed models are the opposite:** at heavy daily use, GPT-5.3-Codex and Opus 4.6 cost more than the 5090 tower's entire 5-year amortized price in 1–3 years. Heavy continuous users of frontier models are the ones local hardware pays for.
- **Quality caveat (honest):** this compares machine cost, not model quality — Opus 4.6 outclasses anything a 27B Q4 runs. If DeepSeek V4 Flash's quality suffices, the API is the cheapest option, period. If you need Opus-class quality, no consumer local build matches it at any price — the open equivalents (GLM-5.2, Kimi K3, Mistral Large 3) need DGX Station-class machines.
- **Consumers: don't pay API rates.** ~$20/mo subscriptions (ChatGPT Plus / Claude Pro) cover casual use; API rates are for developers/automation.
- **Caveats that cut API cost further:** DeepSeek cache-hit input is $0.0028/M (~50× cheaper — huge for agents/RAG with long reused contexts); OpenAI batch/flex pricing halves GPT rates. Scaling usage up favors local sooner.

### Decision tree: which one should you buy?

*Five plain-English questions — each answer points to the next. Full detail in the [build guides](build-guides.md) and [laptop guide](laptop-ai-guide.md).*

```
Q1  Do you need AI on the go (laptop, battery, portability)?
    ├─ YES ────────────────────────────────────► Q2
    └─ NO (it lives on a desk) ────────────────► Q4

Q2  Will you run BIG models (30B+, or up to 70–120B)?
    ├─ YES ──► M5 Max MacBook Pro 128 GB  (~$5,200–5,900)  · the only laptop that does
    └─ NO ───► Q3

Q3  What matters more: all-day battery + always-on AI, or lowest price?
    ├─ Battery / on-device AI (voice, Copilot+) ──► Vivobook S16 X2 Elite 48 GB (~$1,599)
    └─ Lowest price / best value ──────────────────► Zenbook 14 Ryzen AI 9 465 (~$900–1,150)

Q4  Desktop: what's your budget?
    ├─ under ~$1,000 ─────► Budget tower · used RTX 3060 12 GB  (~$665–735)  · newest ≤14B
    ├─ ~$1,000–1,800 ─────► Mid tower · used RTX 5060 Ti 16 GB (~$1,465)   · 27B/30B at Q3
    ├─ ~$1,800–3,500 ─────► 24 GB tower · used RTX 4090       (~$3,000–3,200) · full Q4
    └─ $3,500+ ───────────► Q5

Q5  At $3,500+: max speed on 27–30B, or biggest capacity / zero building?
    ├─ Speed (plus gaming & image gen) ──► RTX 5090 tower (~$5,300–6,300)
    └─ Capacity up to 120B / no building ─► DGX Spark ($4,699, turnkey)
```

**Shortcuts for common cases:**
- **"I just want the most model per dollar, fixed to a desk"** → mid tower (~$1,465); the 24 GB 4090 tower (~$3,000) is the biggest quality-per-dollar jump if you can stretch.
- **"I want a Mac but $5,500 is too much"** → M5 Pro MacBook 14″ (~$2,199, deals ~$1,984) — still runs Gemma 3 27B Q4 at 18–25 tok/s.
- **"I don't want to build anything"** → DGX Spark ($4,699) or the Vivobook X2 ($1,599) if you only need ≤14B.
- **"I need both a big-model machine and mobility"** → M5 Max 128 GB — it's the laptop that also covers the desktop's capacity job.

---

## Model-fitting math (read this before the category files)

Two rules of thumb dominate "can I run model X?" and "how fast?":

### 1. Does it fit in memory?
A **Q4_K_M (4-bit)** quantized model needs roughly **0.55–0.6 GB per billion parameters**, plus ~1–2 GB for context/KV cache and the runtime.

| Model (current examples) | Params | Q4_K_M size | Needs at least |
|---|---|---|---|
| Ministral 3 3B / Qwen3.5 & Gemma 4 sub-12B | 3–12B | 0.7–7 GB | 4–16 GB |
| Ministral 3 14B / Gemma 3 12B | 14B | ~8.6 GB | 12–16 GB |
| Devstral 2 / Gemma 3 27B | 24–27B | 14–16.5 GB | 16–24 GB |
| GLM-4.7-Flash (30B-A3B MoE) | 30B | ~19 GB | 24–32 GB |
| Mistral Medium 3 / gpt-oss-120B | 48–120B | 28–70 GB | 48–128 GB |
| MiniMax M2.5 | 230B | ~130 GB | 128–256 GB |
| Mistral Large 3 / GLM-5.2 | 675–744B | 380–420 GB | 512–748 GB+ |

### 2. How fast will it decode?
LLM generation is **memory-bandwidth-bound**: decode tokens/sec ≈ memory bandwidth ÷ model size (× ~0.7–0.8 efficiency). This is why a 32 GB RTX 5090 (1.79 TB/s) is so much faster than a 128 GB DGX Spark (273 GB/s) on the same small model — and why big-memory machines are great for *fitting* huge models but generate slowly.

**Example ceilings:** 8B Q4 on RTX 5090 → ~150+ tok/s; on DGX Spark → ~35–40 tok/s. Gemma 3 27B Q4 on DGX Spark → ~15 tok/s; MiniMax M2.5 Q4 on an M5 Ultra Studio → ~8–10 tok/s (slow but possible).

---

## Conventions & caveats

- **TOPS / token-per-second figures** are vendor-reported or marketing numbers unless a source is cited in the category file. Real results vary by model, quantization, batch size, and software stack (vLLM vs llama.cpp vs TensorRT-LLM, etc.).
- **Prices** are US MSRP at launch and shift with the market (especially used GPUs and the DGX Spark, which rose from $3,999 to ~$4,699 in late 2025).
- **Token-speed estimates** are for single-user, single-stream decode on LLMs; batched/cloud serving gets far higher aggregate throughput.
- **Model landscape moves monthly** — the cheat-sheet is a snapshot; your repo's `latest-ai-model-releases-august-2026.html` is the place to refresh it.

## Sources

- NVIDIA newsroom & developer blog (RTX 50 launch, GTC 2025 DeepSeek-R1 record, DGX Spark/Station, Jetson Thor)
- Apple newsroom (M5 Oct 2025; M5 Pro/Max Mar 2026), Apple ML Research (M5/MLX)
- AMD (Instinct MI355X, Ryzen AI 400), Intel newsroom (Gaudi 3, Crescent Island)
- Google Cloud blog (Ironwood), AWS (Trn2/Trainium2), Qualcomm (Snapdragon X2)
- Model releases: DeepSeek (V4 Flash 0731), Z.ai (GLM-5.2, GLM-4.7-Flash), Moonshot (Kimi K3), MiniMax (M2.5), Mistral (Large 3, Medium 3, Ministral 3, Devstral 2, Voxtral), Alibaba (Qwen Image 3.0), Tencent (Muse Spark 1.2)
- Independent roundups: Northflank, LocalAIMaster, Spheron, intuitionlabs.ai, chipsandcheese, gmicloud.ai
