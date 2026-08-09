# Laptop AI Buying Guide (August 2026)

**Three best-value laptops for local LLMs — Apple M5 Max, Snapdragon X2 Elite, and AMD Ryzen AI 400 — picked and priced at real August 2026 street prices.** All model recommendations are the newest from the [cheat-sheet](README.md#-newest-models-cheat-sheet-august-2026): Ministral 3, Qwen3.5 / Gemma 4 sub-12B, Gemma 3 27B, GLM-4.7-Flash, Mistral Medium 3, Devstral Small 2, Voxtral Transcribe 2. Speeds are single-stream decode from the [compatibility matrix](compatibility-matrix.md).

## What actually matters on a laptop

1. **Unified memory is everything.** RAM decides which models fit; bandwidth decides speed. The NPU TOPS number mostly buys battery-efficient *always-on* AI (voice, transcription), not bigger models.
2. **Apple's MLX + llama.cpp** is still the smoothest local-LLM laptop experience; Windows on Arm (llama.cpp ARM builds) caught up but CUDA-only tools won't run.
3. **The RAMpocalypse hits BTO configs hard** — every 16 → 32 GB step costs far more than it did in 2024, so pick your RAM ceiling deliberately.

---

## Pick 1 — The local-LLM flagship: M5 Max MacBook Pro 16″ (128 GB)

**The only laptop that runs 70–120B-class models comfortably — and the fastest one for everything below that.**

| Spec | Value |
|---|---|
| Chip | Apple M5 Max (18-core CPU, 40-core GPU, 16-core Neural Engine, ~700 GB/s) |
| Memory | up to **128 GB unified** (48/64/128 GB options) |
| Price (Aug 2026) | 16″ base (48 GB/1 TB) $3,899; **128 GB ≈ $5,500–5,900** (128 GB = +$1,600 over base; 2 TB +$400; 8 TB configs $6,949+) |
| Cheaper path | 14″ M5 Max 128 GB ≈ **$5,200** (36 GB base $3,599) |
| Ecosystem | MLX, llama.cpp, Ollama — the best-supported local-LLM stack anywhere |

**Newest-model stack:**
- **Mistral Medium 3 Q4** (Jul 2026) → **12–16 tok/s** — the only laptop-class hardware that runs it
- **gpt-oss-120B Q4** → 8–10 tok/s; **Qwen2.5-VL-72B Q4** → 8–12 tok/s (vision at 72B on a laptop!)
- **Gemma 3 27B Q4** → 40–50 tok/s; **GLM-4.7-Flash Q4** → 45–55 tok/s — the marquee newest models at full speed
- **Ministral 3 14B Q4** → 60–80 tok/s; **Ministral 3 8B / Qwen3.5 / Gemma 4 sub-12B** → 90–120 tok/s
- **Devstral Small 2** (coding) → 90–120 tok/s; **Voxtral 2**, **Qwen3-Embedding**, **Kokoro** → instant

**Who it's for:** serious local inference on the go — running the newest 27–30B models at speed, 70–120B models at all, plus 72B vision. If you also live in macOS, this is the obvious pick.
**Skip it if:** $5,500 is overkill for occasional 8B use, or you need Windows/CUDA-specific tooling.

---

## Pick 2 — The on-device AI workhorse: Snapdragon X2 Elite (ASUS Vivobook S16 / Surface Laptop 8)

**The 80–85 TOPS NPU machine — runs 8B-class models on the NPU and lasts all day doing it.**

| Spec | ASUS Vivobook S16 (X2 Elite) | Surface Laptop 13.8″ (8th Ed) |
|---|---|---|
| Chip | Snapdragon X2 Elite 18-core (up to 80–85 TOPS NPU) | Snapdragon X2 Elite 12-core (80 TOPS NPU) |
| Memory | 16 GB ($1,299–1,460); **18c Extreme 48 GB ≈ $1,599** | 16 GB from ~$1,400; 32 GB ~$1,800–2,100 (deals) |
| Battery | class-leading (X2 = the efficiency king) | class-leading |
| Price (Aug 2026) | **~$1,300–1,600** | ~$1,400–2,100 |
| Ecosystem | Windows on Arm — llama.cpp, Ollama, QNN/ONNX for NPU | same |

**Newest-model stack:**
- **On NPU (unique to this class):** **Ministral 3 8B** and **Qwen3.5 / Gemma 4 sub-12B** at usable speed on-device — always-on voice (Voxtral 2), transcription, background agents without draining battery
- **On CPU/GPU (llama.cpp ARM):** Ministral 3 8B Q4 → 25–35 tok/s; Ministral 3 14B Q4 → 20–30 tok/s (on 32/48 GB units); Devstral Small 2 → 25–35 tok/s
- **Not on X2:** Gemma 3 27B / GLM-4.7-Flash (need far more memory bandwidth) — that's the Mac's job

**Who it's for:** Windows users who want the best *on-device* AI — 8B models running on battery all day, Copilot+ features, and the strongest NPU you can buy in 2026. The **Vivobook S16 48 GB Extreme at ~$1,599 is the value pick** (48 GB RAM on a $1.6K laptop is rare in the RAMpocalypse).
**Skip it if:** you need >14B local models (bandwidth caps it), or CUDA/x86-only ML tooling.

---

## Pick 3 — The budget Copilot+: ASUS Zenbook 14 (Ryzen AI 9 465)

**The cheapest 60-TOPS Copilot+ machine — the best local-AI value per dollar in 2026.**

| Spec | Value |
|---|---|
| Chip | AMD Ryzen AI 9 465 (Zen 5, 60 TOPS XDNA2 NPU, RDNA iGPU) |
| Memory | 16 GB (32 GB configs exist but RAMpocalypse-priced) |
| Display | 14″ 2K OLED touch |
| Price (Aug 2026) | list $1,199; **street ~$900–1,150** (recent deals to $899; open-box from ~$714) |
| Ecosystem | Windows x86 — llama.cpp/Ollama native, AMD Ryzen AI (ONNX) for NPU |

**Newest-model stack:**
- **On iGPU (fast path):** **Ministral 3 8B Q4** → 25–40 tok/s; **Qwen3.5 / Gemma 4 sub-12B** → 30–50 tok/s; **Devstral Small 2** → 25–40 tok/s
- **On NPU:** Ministral 3 3B/8B, Voxtral 2, Copilot+ features — efficient and quiet
- **Tight:** Ministral 3 14B Q4 → 15–22 tok/s on 32 GB units only
- **Not on this:** 27B+ models — that's the mid/high desktop tier

**Who it's for:** the budget buy — a full Copilot+ AI laptop under $1,000 that runs the newest sub-14B models, real-time transcription, and RAG without breaking the bank.
**Skip it if:** you want big-model speed or 32 GB RAM without paying the RAMpocalypse tax — then step up to Pick 2.

---

## Honorable mentions

| Machine | Price (Aug 2026) | Why |
|---|---|---|
| **M5 Pro MacBook Pro 14″** (24–48 GB) | from $2,199 (deals to ~$1,984) | The "Mac but cheaper" path — runs Gemma 3 27B Q4 and GLM-4.7-Flash at 18–25 tok/s on 48 GB |
| **M5 Max 14″** (128 GB) | ≈ $5,200 | Same flagship capability as the 16″, lighter |
| **M4 Max MacBook Pro** (128 GB, 2025 stock) | ~$3,500–4,500 (discounted) | Previous-gen 128 GB Macs are the 2026 value play if you find stock — ~8–12 tok/s on Mistral Medium 3 |
| **Ryzen AI 400 + Strix Halo laptops** | ~$2,200+ (Strix Halo, 128 GB) | Big unified memory on Windows — a budget DGX-Spark-ish option, but pricey |

---

## Comparison at a glance

| | M5 Max 16″ (128 GB) | Vivobook S16 X2 Elite 48 GB | Zenbook 14 Ryzen AI 9 465 |
|---|---|---|---|
| Price (Aug 2026) | **~$5,500–5,900** | **~$1,599** | **~$900–1,150** |
| NPU / memory bandwidth | 16-core NE / ~700 GB/s | 80–85 TOPS / LPDDR5X-class | 60 TOPS / LPDDR5X-class |
| Top newest model | Mistral Medium 3 (12–16 tok/s), gpt-oss-120B | Ministral 3 14B (20–30 tok/s) | Ministral 3 8B (25–40 tok/s) |
| Sweet spot | Gemma 3 27B / GLM-4.7-Flash at Q4 (40–55 tok/s) | 8B on NPU, all-day battery | 8B + Voxtral under $1K |
| Best for | Serious local LLMs, 72B vision, macOS | Windows on-device AI, battery king | Budget Copilot+ |
| Can't do | — (only GPU laptops beat it on TOPS) | >14B models, CUDA tools | 27B+, 14B needs 32 GB |

## Which to buy

- **Local LLMs are your main thing** → M5 Max 128 GB (~$5,200–5,900). Nothing else on a laptop runs the newest 70–120B models or matches its 27–30B speed.
- **Windows + always-on AI + battery** → Vivobook S16 X2 Elite 48 GB (~$1,599) — the best NPU you can buy, with 48 GB RAM to grow into.
- **Budget Copilot+ / first AI laptop** → Zenbook 14 Ryzen AI 9 465 (~$900–1,150) — the cheapest 60-TOPS machine, runs the whole newest sub-14B stack.
- **Want the Mac experience for less** → M5 Pro 14″ (~$2,199, deals ~$1,984) — 24–48 GB is enough for Gemma 3 27B Q4.

## Sources (Aug 9, 2026)

- Apple newsroom (M5 Pro/Max launch pricing, Mar 2026); Apple store configurator (128 GB = +$1,600); 9to5Mac deal roundup (128 GB/8 TB $6,949); MacRumors Amazon record lows (~$1,984 M5 Pro)
- Microsoft Store (Surface Laptop 8th Ed pricing: 13.8″ from $1,399, 32 GB from $1,799 deal); ABT; Reddit r/Surface launch thread
- ASUS (Vivobook S16 X2 Elite listings; Smartprix $1,459 16 GB/1 TB; Reddit Amazon $1,299 / 48 GB Extreme $1,599)
- Best Buy / Newegg / Walmart / Digital Citizen (Zenbook 14 Ryzen AI 9 465: list $1,199, deals $899–1,000, open-box from $714)

*Prices are US street as of Aug 9, 2026 and move weekly — re-check [prices.md](prices.md) §8 before buying. The RAMpocalypse means RAM upgrades are the most volatile line.*
