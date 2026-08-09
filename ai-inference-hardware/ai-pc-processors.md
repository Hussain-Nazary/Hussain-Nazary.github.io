# AI PC Processors & NPUs (Laptops)

The "AI PC" generation is defined by the **NPU** (Neural Processing Unit) — a low-power accelerator that runs small models continuously (background agents, always-on voice, Copilot+ features) without draining the battery. Microsoft's **Copilot+** bar is a **40+ TOPS NPU**.

> **Honest caveat:** for *serious* LLM work (8B+ models), the NPU matters less than CPU/GPU/RAM. The GPU and unified memory do the heavy lifting; the NPU is for always-on, low-power workloads. **All model picks lead with the newest releases (Aug 2026).**

---

## Current generation (2025)

### Intel Core Ultra 200V "Lunar Lake"

| Spec | Value |
|---|---|
| NPU | 48 TOPS (NPU4) |
| CPU | 8 cores (4 P-core + 4 E-core), ~5.1 GHz max boost |
| GPU | 8 Xe2 (Battlemage) cores |
| Memory | 16–32 GB LPDDR5X-8533 (on-package) |
| Total platform AI | ~48+ TOPS |
| Process | TSMC N3B |
| Availability | Laptops since Sept 2024–2025 |
| Price (Aug 2026) | ~$600–1,400 — 2024–25 stock is deeply discounted (budget units ~$600, mid-tier ~$900); premium configs $1,400+ |

**Best for:** Battery-efficient Copilot+ laptops; the first Intel chips to clear the 40 TOPS bar.

**Recommended AI models (newest first):**
- **NPU:** **Ministral 3 3B** (Dec 2025), the **Qwen3.5 / Gemma 4 sub-12B line** (2026), **Voxtral Transcribe 2** (Feb 2026, on-device STT) via Intel OpenVINO/NPU runtime; on-device Copilot+ features (Live Captions, Cocreator).
- **iGPU/CPU (llama.cpp):** **Ministral 3 8B Q4** → 15–25 tok/s; Gemma 3 12B Q4 → 12–18 tok/s; Qwen3.5 sub-12B → 20–30 tok/s.
- **Tight:** Ministral 3 14B Q4 on 32 GB units.

### AMD Ryzen AI 300 "Strix Point" (Ryzen AI 9 HX 370 / 365)

| Spec | Value |
|---|---|
| NPU | 50 TOPS (XDNA2) |
| CPU | HX 370: 12 cores (4 Zen 5 + 8 Zen 5c); HX 365: 10 cores |
| GPU | Radeon 890M / 880M (RDNA 3.5, 16/12 CU) |
| Memory | LPDDR5X-7500 / DDR5 |
| Price (Aug 2026) | ~$900–1,500 (HX 370 mid-tier ~$900–1,200; premium/creator configs $1,400+) |

**Best for:** 2025's best all-round AI laptop platform — the most powerful NPU of its generation plus a strong iGPU that also accelerates LLMs.

**Recommended AI models (newest first):**
- **NPU:** Ministral 3 3B, Qwen3.5 / Gemma 4 sub-12B (2026), Voxtral Transcribe 2 via AMD Ryzen AI / ONNX runtime.
- **iGPU (fast path):** Ministral 3 8B Q4 → 25–40 tok/s; Gemma 3 12B Q4 → 15–25 tok/s; **Ministral 3 14B Q4** → 12–18 tok/s (32 GB units).
- **Tight:** Gemma 3 27B Q4 on 32 GB units at reduced context.

### Qualcomm Snapdragon X Elite / X Plus

| Spec | Value |
|---|---|
| NPU | 45 TOPS (Hexagon) |
| CPU | Up to 12 Oryon cores, up to 4.6 GHz |
| GPU | Adreno X1 |
| Memory | LPDDR5X-8448 |
| Process | 4 nm |
| Availability | Laptops since mid-2024 |
| Price (Aug 2026) | ~$600–1,000 mainstream (Qualcomm lists 'from $599'; Dell from ~$1,000); premium $1,400–1,700 (Surface Laptop 7 ~$1,690) |

**Best for:** Outstanding NPU efficiency and battery life; the original Copilot+ platform. Arm-based, so x86 app compatibility needs checking (Windows on Arm has matured a lot by 2026).

**Recommended AI models (newest first):**
- **NPU:** Ministral 3 3B, Qwen3.5 sub-12B, Voxtral Transcribe 2 — very power-efficient.
- **CPU/GPU (llama.cpp, ARM build):** Ministral 3 8B Q4 → 15–25 tok/s; Gemma 4 sub-12B → 20–30 tok/s.
- **Note:** some AI libraries are x86/CUDA-centric — verify support before buying for ML *development*.

---

## Next generation (2026)

### Intel Core Ultra 300V "Panther Lake"

| Spec | Value |
|---|---|
| NPU | ~50 TOPS |
| CPU | Up to 18 cores (8 P + 8 E + 2 LP E), Panther Cove cores |
| GPU | Xe3 (Celestial), up to 12 cores |
| Process | Intel 18A |
| Availability | Laptops from late 2025–2026 (CES 2026 wave) |
| Price (Aug 2026) | ~$999–2,400 (mainstream ~$1,100–1,500; high-end >$2,000) |

**Best for:** The 2026 Intel answer — combines the fast P-cores with a bigger NPU; leads in single-thread perf among 2026 AI chips.

**Recommended AI models (newest first):**
- **NPU:** same small-model class as Lunar Lake but faster (Copilot+ features, local search/summaries): Ministral 3 3B, Qwen3.5 / Gemma 4 sub-12B, Voxtral Transcribe 2.
- **GPU/CPU:** Ministral 3 8B Q4 → 20–35 tok/s; Gemma 3 12B Q4 → 15–22 tok/s on 32 GB units.

### AMD Ryzen AI 400 "Medusa Point"

| Spec | Value |
|---|---|
| NPU | 60 TOPS (XDNA2 refresh) |
| CPU | Zen 5 (up to 12 cores) |
| GPU | RDNA (up to 16 CU) |
| Availability | Laptops + first Copilot+ desktops, early 2026 |
| Price (Aug 2026) | ~$750–1,500 (mainstream ~$900–1,200) |

**Best for:** Highest NPU throughput in the AMD lineup; also powers the desktop PCs covered in [ai-desktops.md](ai-desktops.md).

**Recommended AI models (newest first):**
- **NPU:** 3–8B models at high efficiency (Ministral 3 8B, Qwen3.5 / Gemma 4 sub-12B); two concurrent NPU workloads (e.g., voice + vision) without stutter.
- **GPU/CPU:** Ministral 3 14B Q4 → 15–22 tok/s; Gemma 3 27B Q4 → 10–15 tok/s on 32 GB units.

### Qualcomm Snapdragon X2 Elite / X2 Plus ("Glymur")

| Spec | Value |
|---|---|
| NPU | 80 TOPS (Hexagon) — Elite Extreme up to 80–85 TOPS |
| CPU | Elite: up to 18 Oryon v3 cores (12 Prime + 6 Perf), up to 5.0 GHz; Plus: 10 cores |
| GPU | Adreno X2-90 (~1.85 GHz) |
| Process | 3 nm |
| Availability | Laptops from late 2025–2026 (CES 2026 wave) |
| Price (Aug 2026) | ~$1,080–2,050 (Surface 13.8″ from $1,399; premium 16″ ~$1,600–1,700; HP first X2 Elite from ~$2,050; deals to ~$1,080) |

**Best for:** The **fastest consumer NPU in 2026** — the Extreme config leads the Copilot+ class, and battery life remains class-leading.

**Recommended AI models (newest first):**
- **NPU:** **8B-class models on-device at usable speed** (unique at this power level) — Ministral 3 8B, Qwen3.5 / Gemma 4 sub-12B; **Voxtral Transcribe 2** for always-on voice; concurrent multimodal workloads.
- **CPU/GPU:** Ministral 3 14B Q4 → 20–30 tok/s; Gemma 3 12B Q4 → 20–25 tok/s; Devstral Small 2 for coding.
- **Note:** same Arm compatibility caveat as X Elite, though the ecosystem improved markedly by 2026.

---

## NPU comparison & model guidance

| Chip (gen) | NPU TOPS | Year | Newest NPU sweet-spot models | 8B Q4 speed (iGPU/CPU) | Laptop street price (Aug 2026) |
|---|---|---|---|---|---|
| Lunar Lake | 48 | 2024–25 | Ministral 3 3B, Qwen3.5/Gemma 4 sub-12B, Voxtral | 15–25 tok/s | ~$600–1,400 |
| Strix Point | 50 | 2024–25 | Ministral 3 3B/8B, Qwen3.5/Gemma 4 sub-12B | 25–40 tok/s | ~$900–1,500 |
| Snapdragon X Elite | 45 | 2024–25 | Ministral 3 3B, Qwen3.5 sub-12B | 15–25 tok/s | ~$600–1,700 |
| Panther Lake | ~50 | 2025–26 | Ministral 3 3B/8B | 20–35 tok/s | ~$999–2,400 |
| Ryzen AI 400 | 60 | 2026 | Ministral 3 8B, dual workloads | 25–40 tok/s | ~$750–1,500 |
| Snapdragon X2 | 80–85 | 2026 | **up to 8B on NPU** | 25–35 tok/s | ~$1,080–2,050 |

**Rule of thumb:** if your goal is **local LLMs**, prioritize RAM (16 GB minimum, 32 GB ideal) and memory bandwidth over NPU TOPS — and load the newest small models (Ministral 3, Qwen3.5, Gemma 4). If your goal is **always-on AI assistants** (voice, transcription, background agents), the NPU number is what matters — that's where Snapdragon X2 and Ryzen AI 400 shine.
