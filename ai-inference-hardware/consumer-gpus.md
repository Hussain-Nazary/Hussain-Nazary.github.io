# Consumer & Prosumer GPUs for Local Inference

Desktop GPUs for running LLMs, image models, and audio models on your own machine. **Remember:** for LLMs, VRAM capacity + memory bandwidth matter far more than raw TOPS (see README fitting math). **All model picks below lead with the newest releases (Aug 2026); older models are fallbacks.**

---

## NVIDIA GeForce RTX 5090

**The flagship consumer Blackwell card — the fastest local-inference GPU money can buy.**

| Spec | Value |
|---|---|
| Architecture | Blackwell (GB202), 5th-gen Tensor Cores, FP4 support |
| CUDA cores | 21,760 |
| VRAM | 32 GB GDDR7 (512-bit) |
| Memory bandwidth | ~1,792 GB/s |
| TDP | 575 W |
| Price (Aug 2026) | $1,999 MSRP; **street ~$3,600–4,800** |
| AI compute (marketing) | ~3,352 TOPS (FP4-class) |
| Ecosystem | CUDA — best support: vLLM, llama.cpp, TensorRT-LLM, PyTorch |

**Best for:** Running the newest 27–30B models at high speed, image/video generation, and serious local AI work without a data center. ~1.5–1.8× the inference throughput of an RTX 4090 (bandwidth-driven).

**Recommended AI models (newest first):**
- **LLMs (fit fully in 32 GB):** **Gemma 3 27B Q4** (~16.5 GB, Jul 2026) → **60–90 tok/s**; **GLM-4.7-Flash Q4** (30B-A3B MoE, ~19 GB, Jan 2026) → 55–80 tok/s — the strongest models you can run at speed on consumer hardware; **Devstral 2 Q4** (24B coding, Dec 2025) → 70–100 tok/s; **MiniMax M2.5** is too big (230B) — API/enterprise only.
- **Mid-size (fast):** Ministral 3 14B Q4 (Dec 2025) → 100–130 tok/s; Gemma 3 12B → 120+ tok/s.
- **Tight — 70B-class only at Q3:** Mistral Medium 3 (Jul 2026) / gpt-oss-120B need 48 GB+; a 70B Q3 (~31 GB) squeeze is possible but quality suffers — a Mac or DGX Spark fits these properly.
- **Multimodal (vision):** **Gemma 3 27B** (native multimodal, Jul 2026); Qwen2.5-VL-32B Q4 as workhorse fallback.
- **Image generation (newest):** **Qwen Image 3.0 / 3.0 Pro** (Aug 2026, open weights) and **Muse Spark 1.2** (Tencent, Aug 2026); FLUX.1-dev (fp8 ~12 GB) as the established fallback.
- **Speech:** **Voxtral Transcribe 2** (Feb 2026, on-device STT with diarization) → real-time ×20+; Whisper large-v3 as fallback; Kokoro / F5-TTS for TTS.
- **Embeddings/RAG:** Qwen3-Embedding, bge-m3, jina-reranker.

---

## NVIDIA GeForce RTX 5080

**16 GB Blackwell — the sweet spot if $2,000 is too much.**

| Spec | Value |
|---|---|
| Architecture | Blackwell (GB203) |
| CUDA cores | 10,752 |
| VRAM | 16 GB GDDR7 (256-bit) |
| Memory bandwidth | ~960 GB/s |
| TDP | 360 W |
| Price (Aug 2026) | $999 MSRP; street ~$1,150–1,480 |

**Best for:** Fast 8–14B models, 27B at Q4 with care, and solid image generation — at roughly half the price of the 5090.

**Recommended AI models (newest first):**
- **Fits comfortably (16 GB):** **Ministral 3 14B Q4** (~8.6 GB, Dec 2025) → **55–75 tok/s**; **Devstral Small 2 Q4** (local coding, Dec 2025) → 60–80 tok/s; **Gemma 3 27B Q4** (~16.5 GB) → 35–45 tok/s with limited context — it *just* fits; the **Qwen3.5 / Gemma 4 sub-12B line** (2026) → 90–120 tok/s.
- **Fits tight:** GLM-4.7-Flash Q4 (~19 GB) needs Q3 or offload — not ideal; prefer the 4090 for this one.
- **Won't fit (70B+):** Mistral Medium 3 and anything larger — no.
- **Vision:** Gemma 3 27B (tight), Qwen2.5-VL-7B fallback.
- **Image gen:** Qwen Image 3.0 (smaller variant), SDXL, FLUX.1-schnell fp8 (~12 GB).
- **Audio:** Voxtral Transcribe 2, Whisper large-v3, Kokoro TTS.

---

## NVIDIA GeForce RTX 5070 Ti / RTX 5070

**The value picks — 16 GB and 12 GB Blackwell.**

| Spec | RTX 5070 Ti | RTX 5070 |
|---|---|---|
| Architecture | Blackwell (GB203) | Blackwell (GB205) |
| CUDA cores | 8,960 | 6,144 |
| VRAM | 16 GB GDDR7 | 12 GB GDDR7 |
| Memory bandwidth | ~896 GB/s | ~672 GB/s |
| TDP | 300 W | 250 W |
| Price (Aug 2026) | $749 MSRP; street ~$870–1,420 (used ~$870) | $549 MSRP; street ~$610–750 (used ~$490) |

**Best for:** Budget local AI — the newest 8–14B models run great; 27B is a stretch on the Ti.

**Recommended AI models (newest first):**
- **5070 Ti (16 GB):** same picks as the 5080, slightly slower: Ministral 3 14B Q4 → ~50–65 tok/s; Devstral Small 2 → ~55–70 tok/s; Gemma 3 27B Q4 tight; Qwen3.5 / Gemma 4 sub-12B → 80–100 tok/s.
- **5070 (12 GB):** **Ministral 3 8B** and the **Qwen3.5 / Gemma 4 sub-12B line** (2026) → 60–90 tok/s; Ministral 3 14B Q4 (~8.6 GB) → ~40–55 tok/s with tight context; Devstral Small 2 for coding.
- **Vision:** MiniCPM-V / Qwen2.5-VL-7B (fallback), Gemma 3 12B (multimodal).
- **Image:** SDXL, Qwen Image 3.0 (smaller variant), FLUX.1-schnell fp8.
- **Audio:** Voxtral Transcribe 2, Whisper small/medium.

---

## NVIDIA GeForce RTX 4090

**The 24 GB community favorite — still extremely relevant on the used market.**

| Spec | Value |
|---|---|
| Architecture | Ada Lovelace (AD102) |
| CUDA cores | 16,384 |
| VRAM | 24 GB GDDR6X (384-bit) |
| Memory bandwidth | ~1,008 GB/s |
| TDP | 450 W |
| Price (Aug 2026) | $1,599 MSRP; **used ~$2,200–2,400** |

**Best for:** The cheapest way to 24 GB — and 24 GB is exactly what the newest local-friendly models (Gemma 3 27B, GLM-4.7-Flash) want. Many local-AI users still prefer a used 4090 over a new 5070 Ti.

**Recommended AI models (newest first):**
- **Comfortable (24 GB):** **Gemma 3 27B Q4** (~16.5 GB, Jul 2026) → **40–55 tok/s**; **GLM-4.7-Flash Q4** (~19 GB, Jan 2026) → 35–50 tok/s; **Devstral 2 Q4** (24B, Dec 2025) → 45–60 tok/s; Ministral 3 14B → 60–75 tok/s.
- **Tight:** 70B-class (Mistral Medium 3, gpt-oss-120B) only at Q2/Q3 with offload — quality suffers; better on 48 GB+ machines.
- **Vision:** Gemma 3 27B (multimodal), Qwen2.5-VL-32B Q4 fallback.
- **Image gen:** Qwen Image 3.0 Pro (Aug 2026), Muse Spark 1.2, FLUX.1-dev fp8.
- **Audio:** Voxtral Transcribe 2 real-time, Whisper large-v3, voice pipelines (Whisper + Kokoro).

---

## AMD Radeon RX 9070 XT

**Best-value 16 GB card — but CUDA's absence matters.**

| Spec | Value |
|---|---|
| Architecture | RDNA 4 (Navi 48), FP4/FP8 support |
| Stream processors | 4,096 |
| VRAM | 16 GB GDDR6 (256-bit) |
| Memory bandwidth | ~644 GB/s |
| TDP | 304 W |
| Price (Aug 2026) | $599 MSRP; street ~$650–710 (deals to $549) |

**Best for:** Budget AI on a full-AMD build. ROCm support for llama.cpp is now quite usable, but the vLLM/PyTorch ecosystem still trails CUDA significantly.

**Recommended AI models (newest first):**
- **LLMs:** Ministral 3 14B Q4 → ~40–50 tok/s; Devstral Small 2; Qwen3.5 / Gemma 4 sub-12B → 60–80 tok/s; Gemma 3 27B Q4 tight (16.5 GB on 16 GB card — limited context). (llama.cpp has solid ROCm/HIP support.)
- **Vision:** Gemma 3 12B (multimodal); **Image:** Qwen Image 3.0 / SDXL via the (still maturing) ROCm/ComfyUI path.
- **Avoid for:** CUDA-only tooling (TensorRT-LLM, some vLLM features, many fine-tuning stacks).

---

## Intel Arc B580 / B570 / B50 (Battlemage)

**The budget champions — 12 GB for $250.**

| Spec | Arc B580 | Arc B570 | Arc B50 (announced) |
|---|---|---|---|
| Architecture | Xe2 Battlemage | Xe2 | Xe2 |
| Xe cores | 20 | 18 | — |
| VRAM | 12 GB GDDR6 | 10 GB GDDR6 | 16 GB |
| Memory bandwidth | ~456 GB/s | ~380 GB/s | — |
| TDP | 190 W | 150 W | ~100 W (est.) |
| Price (Aug 2026) | $249 MSRP; street ~$250–310 | $219 MSRP; street ~$230–280 (est.) | ~$300 (est., not yet shipping) |

**Best for:** Extremely cheap local inference — llama.cpp and IPEX-LLM both support Intel GPUs. **Caveat:** no CUDA, so anything requiring CUDA-only libraries is out.

**Recommended AI models (newest first):**
- **B580 (12 GB):** Ministral 3 8B (Dec 2025) → 25–40 tok/s; Qwen3.5 / Gemma 4 sub-12B (2026) → 20–35 tok/s; Ministral 3 14B Q4 tight (~8.6 GB); Voxtral Transcribe 2 / Whisper medium for transcription.
- **B570 (10 GB):** same small models, slightly slower; sub-12B line fine.
- **B50 (16 GB):** bumps you to Ministral 3 14B Q4 and Devstral Small 2 comfortably.
- **Vision (all):** YOLOv11/v12, MobileNet, Gemma 3 4B (multimodal); for images: SDXL (via IPEX-LLM/OpenVINO) works but is slower than NVIDIA/AMD.

---

## Comparison at a glance

| GPU | VRAM | Bandwidth | Price | Fits (Q4) | Newest-model pick | Decode speed (8B) |
|---|---|---|---|---|---|---|
| RTX 5090 | 32 GB | 1,792 GB/s | ~$3,600–4,800 | GLM-4.7-Flash, Gemma 3 27B | Gemma 3 27B | ~150+ tok/s |
| RTX 5080 | 16 GB | 960 GB/s | ~$1,150–1,480 | Ministral 3 14B (27B tight) | Ministral 3 14B | ~90–110 tok/s |
| RTX 5070 Ti | 16 GB | 896 GB/s | ~$870–1,420 | Ministral 3 14B | Ministral 3 14B | ~70–90 tok/s |
| RTX 5070 | 12 GB | 672 GB/s | ~$610–750 | 8B (14B tight) | Ministral 3 8B | ~60–80 tok/s |
| RTX 4090 | 24 GB | 1,008 GB/s | ~$2,200–2,400 used | Gemma 3 27B, GLM-4.7-Flash | Gemma 3 27B | ~100–120 tok/s |
| RX 9070 XT | 16 GB | 644 GB/s | ~$650–710 | Ministral 3 14B | Ministral 3 14B | ~50–70 tok/s |
| Arc B580 | 12 GB | 456 GB/s | ~$250–310 | 8B | Ministral 3 8B | ~30–45 tok/s |

*Decode speeds are rough single-stream estimates; see README for the bandwidth math.*
