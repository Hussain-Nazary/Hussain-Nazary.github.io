# Apple Silicon (Macs — the local-LLM favorite)

Apple's CPU/GPU/Neural Engine share **one pool of unified memory**, so a Mac can hold an entire large model in RAM — no PCIe transfer bottleneck. That, plus high memory bandwidth and the excellent **MLX** framework, makes Macs the most popular hardware for serious local inference. The deciding spec is **unified memory** (how big a model fits) and **bandwidth** (how fast it decodes). **All model picks lead with the newest releases (Aug 2026).**

---

## M4 family (2024–2025)

| Spec | M4 | M4 Pro | M4 Max |
|---|---|---|---|
| CPU | 10-core | 14-core (12/14 in late refresh) | 16-core |
| GPU | 10-core | 20-core | 40-core |
| Neural Engine | 16-core | 16-core | 16-core |
| Memory | up to 32 GB | up to 64 GB | up to 128 GB |
| Bandwidth | ~120 GB/s | ~273 GB/s | ~546 GB/s |
| Devices | MacBook Pro 14, iMac, Mac mini, iPad Pro | MacBook Pro, Mac mini | MacBook Pro, Mac Studio |

**Best for:** Excellent local AI on a laptop; the 128 GB M4 Max MacBook Pro became the 2025 reference machine for running big models.

**Recommended AI models (newest first):**
- **M4 base (16–32 GB):** **Ministral 3 8B Q4** (Dec 2025) → 40–60 tok/s; **Qwen3.5 / Gemma 4 sub-12B** (2026) → 35–55 tok/s; Gemma 3 12B Q4 → 25–35 tok/s; Ministral 3 14B Q4 tight on 32 GB; **Voxtral Transcribe 2** (on-device STT, Feb 2026).
- **M4 Pro (24–64 GB):** Ministral 3 14B Q4 → 30–40 tok/s; **Devstral 2 Q4** (24B coding) → 20–25 tok/s; **Gemma 3 27B Q4** (~16.5 GB) on 48 GB+ → 18–25 tok/s; **GLM-4.7-Flash Q4** on 48 GB+ → 15–20 tok/s.
- **M4 Max (128 GB):** **Mistral Medium 3** (Jul 2026) → **8–10 tok/s**; **gpt-oss-120B Q4** (~70 GB) → 5–7 tok/s; Gemma 3 27B → 30–35 tok/s; GLM-4.7-Flash → 35–40 tok/s; multiple models resident at once. **MiniMax M2.5** (230B) is just over the edge — Q3 or API.
- **Vision:** **Gemma 3 27B** (native multimodal, Jul 2026) on Pro/Max; MiniCPM-V (smaller Macs); **Image:** Qwen Image 3.0 via MPS/ComfyUI; **Audio:** Voxtral Transcribe 2 real-time, Whisper large-v3 fallback.

---

## M5 (October 2025)

| Spec | Value |
|---|---|
| CPU | 12-core (MacBook Pro/Air configs; 10-core in Air) |
| GPU | 16-core (10-core in Air) |
| Neural Engine | 16-core |
| Bandwidth | ~153 GB/s (Air) up to ~250 GB/s (Pro) |
| Process | TSMC N3 (2nd-gen) |
| Devices | MacBook Pro 14, MacBook Air, iPad Pro |
| Price (Aug 2026) | MacBook Air from $1,099 (up $100 from M4); MacBook Pro 14 from ~$1,599 |

**Best for:** The mainstream upgrade — Apple's ML research measured **19–27% faster LLM throughput than M4** on the same workloads, driven by greater memory bandwidth.

**Recommended AI models (newest first):**
- **16–24 GB:** Ministral 3 8B Q4 → 45–65 tok/s; Qwen3.5 / Gemma 4 sub-12B (2026) → 40–60 tok/s; Gemma 3 12B → 30–40 tok/s; Voxtral Transcribe 2; Kokoro TTS.
- **32 GB:** Devstral 2 Q4 → 25–30 tok/s; Gemma 3 27B Q4 (tight, ~16.5 GB + context).

---

## M5 Pro / M5 Max (March 2026)

| Spec | M5 Pro | M5 Max |
|---|---|---|
| CPU | 15-core (5 super + 10 perf) or 18-core (6 super + 12 perf) | 18-core |
| GPU | 16-core or 20-core | 40-core (each GPU core has a Neural Accelerator) |
| Neural Engine | 16-core | 16-core |
| Memory | up to 48 GB (reported) | up to 128 GB |
| Bandwidth | ~256 GB/s class | ~700 GB/s (~28% over M4 Max) |
| Devices | MacBook Pro 14/16 | MacBook Pro 14/16 |
| Price (Aug 2026) | 14″ from $2,199 (up $200 from M4); 16″ from $2,699 | 14″ from $3,599; 16″ from $3,899 (Amazon record lows to ~$1,984 for 24 GB M5 Pro) |

**Best for:** The best laptop for local LLMs in 2026. Apple claims **up to 4× faster LLM prompt processing** than M4 Pro/Max and up to 8× AI image generation vs M1 Pro/Max.

**Recommended AI models (newest first):**
- **M5 Pro (36–48 GB):** **Gemma 3 27B Q4** → 20–30 tok/s; **GLM-4.7-Flash Q4** → 15–25 tok/s; **Devstral 2 Q4** → 30–40 tok/s; Ministral 3 14B → 40–50 tok/s.
- **M5 Max (128 GB):** **Mistral Medium 3** (Jul 2026) → **12–16 tok/s**; **gpt-oss-120B Q4** → 8–10 tok/s; Gemma 3 27B → 40–50 tok/s; GLM-4.7-Flash → 45–55 tok/s; Ministral 3 14B → 60–80 tok/s; Qwen3.5 / Gemma 4 sub-12B → 90–120 tok/s.
- **Vision:** Gemma 3 27B (multimodal); **Image:** Qwen Image 3.0 / Muse Spark 1.2 via MPS/MLX; **Audio:** Voxtral Transcribe 2, Kokoro voice pipelines at real-time ×3–5.

---

## M5 Ultra (Mac Studio, 2026)

| Spec | Value (reported) |
|---|---|
| CPU | 36-core |
| GPU | 84-core |
| Neural Engine | 32-core |
| Memory | up to 512 GB (768 GB per latest 2026 reports) |
| Bandwidth | ~1 TB/s class (reported) |
| Storage | up to 16 TB |
| Price | from ~$4,000+ (reported) |

**Best for:** The extreme end of local inference — the only mainstream desktop that holds **the newest frontier open models** entirely in memory.

**Recommended AI models (newest first):**
- **Flagship (512 GB):** **MiniMax M2.5 Q4** (230B → ~130 GB) → **15–20 tok/s**; **Mistral Large 3 Q4** (675B → ~380 GB) → 5–8 tok/s; **GLM-5.2 Q4** (~744B → ~420 GB) → 4–6 tok/s; **DeepSeek V4 Flash / Kimi K3** (open-weight MoE giants) at Q2–Q3 → slow but real. No other desktop runs these.
- **Practical (70B class):** Mistral Medium 3 → ~25–30 tok/s; gpt-oss-120B Q4 → 20–30 tok/s; multiple 27–120B models resident simultaneously (e.g., one coder + one general + one vision model).
- **Fine-tuning:** QLoRA on 70B-class fits comfortably.

---

## Quick decision table

| Mac | Memory ceiling | Newest picks that fit (Q4) | 70B-class speed |
|---|---|---|---|
| M4/M5 (base) | 24–32 GB | Ministral 3 8B/14B, Qwen3.5, Gemma 4 | — |
| M4 Pro / M5 Pro | 48–64 GB | Gemma 3 27B, GLM-4.7-Flash, Devstral 2 | ~8–10 tok/s (Q3) |
| M4 Max | 128 GB | Mistral Medium 3, gpt-oss-120B | 8–12 tok/s |
| M5 Max | 128 GB | Mistral Medium 3, gpt-oss-120B | 12–16 tok/s |
| M5 Ultra (Studio) | 512 GB+ | MiniMax M2.5, Mistral Large 3, GLM-5.2 | ~20–25 tok/s |

**Bottom line:** Buy the most unified memory you can afford — it's the single spec that decides which of the newest models you can run at all. Speeds are bandwidth-bound; MLX/llama.cpp/Ollama all work great.
