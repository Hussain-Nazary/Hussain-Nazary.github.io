# Master Compatibility Matrix

**Every model from the Aug 2026 cheat-sheet × every device in this folder** — fit, quantization, and rough speed in one place. Last updated: August 2026.

This is the lookup file: category docs ([consumer-gpus.md](consumer-gpus.md), [ai-desktops.md](ai-desktops.md), [ai-pc-processors.md](ai-pc-processors.md), [apple-silicon.md](apple-silicon.md), [datacenter-gpus.md](datacenter-gpus.md), [inference-asics.md](inference-asics.md), [hyperscaler-silicon.md](hyperscaler-silicon.md), [edge-embedded.md](edge-embedded.md)) have the specs and rationale; this file has the answers.

---

## How to read this

**Cell format: `quant · tok/s`** — e.g. `Q4 · 60–90` = fits at 4-bit quantization, ~60–90 tokens/sec single-stream decode.

| Code | Meaning |
|---|---|
| `Q4 / Q3 / Q2` | Quantization level that fits (Q4_K_M ≈ 0.55–0.6 GB/billion params; Q3 ≈ 0.43; Q2 ≈ 0.33) |
| `✓` | Fits comfortably |
| `⚠` | Fits but tight — limited context, offload, or barely over capacity |
| `✖` | Doesn't fit / impractical on this hardware |
| `—` | API / enterprise only (weights impractical for this class) |
| `n× FP8` | Spans n GPUs at FP8 (datacenter table) |

**Speeds** are single-user, single-stream decode (bandwidth-bound); batched serving is 10–100× higher. See [README.md](README.md) for the bandwidth math. **Q4 sizes** assume Q4_K_M GGUF.

---

## Device key

| Short name | Device | Capacity | Bandwidth |
|---|---|---|---|
| RTX 5090 (32G) | NVIDIA RTX 5090 | 32 GB GDDR7 | 1,792 GB/s |
| RTX 4090 (24G) | NVIDIA RTX 4090 | 24 GB GDDR6X | 1,008 GB/s |
| 16G GPU | RTX 5080 / 5070 Ti / RX 9070 XT | 16 GB | 644–960 GB/s |
| 12G GPU | RTX 5070 / Arc B580 | 12 GB | 456–672 GB/s |
| DGX Spark | NVIDIA DGX Spark | 128 GB unified | 273 GB/s |
| Mini-PC | AI mini-PC / Ryzen AI 400 desktop | 16–96 GB | DDR5-class |
| Mac base | M4 / M5 (MacBook/Air/mini) | 16–32 GB | 120–250 GB/s |
| Mac Pro | M4 Pro / M5 Pro | 24–64 GB | 256–273 GB/s |
| Mac Max | M4 Max / M5 Max | 128 GB | 546–700 GB/s |
| Mac Ultra | M5 Ultra (Mac Studio) | 512 GB | ~1 TB/s |
| Jetson Thor | NVIDIA Jetson Thor | 128 GB | 273 GB/s |
| AGX Orin | Jetson AGX Orin | 64 GB | ~200 GB/s |
| Nano/Pi | Orin Nano Super / Pi 5 + AI Kit | 8–16 GB | ~68 GB/s |

---

## Part 1 — LLMs × local devices

| Model (Q4 size) | RTX 5090 32G | RTX 4090 24G | 16G GPU | 12G GPU | DGX Spark | Mini-PC | Mac base | Mac Pro | Mac Max | Mac Ultra | Jetson Thor | AGX Orin | Nano/Pi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Gemma 3 27B** (16.5 GB) | Q4 · 60–90 | Q4 · 40–55 | Q3 · 30–40 ⚠ | Q3 ⚠ | Q4 · 15 | Q4 · 5–10 ⚠ (32G+) | Q3 ⚠ (32G) | Q4 · 18–25 | Q4 · 30–50 | Q4 · 50–70 | Q4 · 10–12 | Q4 · 5–8 ⚠ | ✖ |
| **GLM-4.7-Flash** 30B-A3B (17–19 GB) | Q4 · 55–80 | Q4 · 35–50 | Q3 · 30–40 ⚠ | ✖ | Q4 · 12–15 | Q4 · 5–10 ⚠ (64G+) | Q3 ⚠ (32G) | Q4 · 15–20 | Q4 · 35–55 | Q4 · 50–70 | Q4 · 8–12 | Q4 · 4–6 ⚠ | ✖ |
| **Devstral 2** 24B (14 GB) | Q4 · 70–100 | Q4 · 45–60 | Q4 · 35–45 ⚠ | Q3 ⚠ | Q4 · 18 | Q4 · 5–10 ⚠ (32G+) | Q3 ⚠ (32G) | Q4 · 20–25 | Q4 · 30–40 | Q4 · 50–70 | Q4 · 14–18 | Q4 · 4–6 ⚠ | ✖ |
| **Devstral Small 2** (~8 GB) | Q4 · 150+ | Q4 · 100–120 | Q4 · 80–110 | Q4 · 30–90 | Q4 · 30–40 | Q4 · 15–25 | Q4 · 40–60 | Q4 · 50–70 | Q4 · 90–120 | Q4 · 120–150 | Q4 · 25–40 | Q4 · 10–25 | Q4 · 2–4 ⚠ |
| **Ministral 3 14B** (8.6 GB) | Q4 · 100–130 | Q4 · 60–75 | Q4 · 50–75 | Q4 · 40–55 ⚠ | Q4 · 20–25 | Q4 · 10–20 | Q4 · 30–40 (32G) | Q4 · 30–40 | Q4 · 50–70 | Q4 · 80–100 | Q4 · 12–18 | Q4 · 6–10 | ✖ |
| **Ministral 3 8B** (5 GB) | Q4 · 150+ | Q4 · 100–120 | Q4 · 80–110 | Q4 · 30–90 | Q4 · 30–40 | Q4 · 20–40 | Q4 · 40–60 | Q4 · 50–70 | Q4 · 90–120 | Q4 · 120+ | Q4 · 20–40 | Q4 · 10–25 | Q4 · 2–4 ⚠ |
| **Ministral 3 3B** (1.9 GB) | Q4 · 150+ | Q4 · 150+ | Q4 · 150+ | Q4 · 100+ | Q4 · 60–100 | Q4 · 30–60 | Q4 · 60–100 | Q4 · 80–120 | Q4 · 120+ | Q4 · 150+ | Q4 · 40–60 | Q4 · 20–40 | Q4 · 5–15 |
| **Qwen3.5 sub-12B** (~5 GB) | Q4 · 150+ | Q4 · 100–120 | Q4 · 80–110 | Q4 · 30–90 | Q4 · 30–40 | Q4 · 20–40 | Q4 · 40–60 | Q4 · 50–70 | Q4 · 90–120 | Q4 · 120+ | Q4 · 20–40 | Q4 · 10–25 | Q4 · 2–4 ⚠ |
| **Gemma 4 sub-12B** (~5 GB) | Q4 · 150+ | Q4 · 100–120 | Q4 · 80–110 | Q4 · 30–90 | Q4 · 30–40 | Q4 · 20–40 | Q4 · 40–60 | Q4 · 50–70 | Q4 · 90–120 | Q4 · 120+ | Q4 · 20–40 | Q4 · 10–25 | Q4 · 2–4 ⚠ |
| **Mistral Medium 3** (~28 GB) | Q4 · 40–50 ⚠ | ✖ | ✖ | ✖ | Q4 · 6–8 | ✖ | ✖ | Q4 · 10–14 | Q4 · 12–16 | Q4 · 25–30 | Q4 · 5–6 | Q4 · 4–5 ⚠ | ✖ |
| **gpt-oss-120B** (~70 GB) | ✖ (offload ⚠) | ✖ | ✖ | ✖ | Q4 · 4–6 | ✖ | ✖ | Q3 ⚠ (64G) | Q4 · 8–10 | Q4 · 20–30 | Q4 · 4–5 | ✖ | ✖ |
| **Qwen2.5-VL-7B** (4.7 GB, vision) | Q4 · 150+ | Q4 · 100–120 | Q4 · 80–110 | Q4 · 30–90 | Q4 · 30–40 | Q4 · 20–40 | Q4 · 40–60 | Q4 · 50–70 | Q4 · 90–120 | Q4 · 120+ | Q4 · 20–40 | Q4 · 10–25 | Q4 · 2–4 ⚠ |
| **Qwen2.5-VL-32B** (~19 GB, vision) | Q4 · 55–80 | Q4 · 35–50 | Q3 ⚠ | ✖ | Q4 · 12–15 | ⚠ (64G+) | ✖ | Q4 · 15–20 | Q4 · 35–55 | Q4 · 50–70 | Q4 · 8–12 | Q4 ⚠ | ✖ |
| **Qwen2.5-VL-72B** (~41 GB, vision) | Q3 · 25–35 ⚠ | ✖ | ✖ | ✖ | Q4 · 5–6 | ✖ | ✖ | Q3 ⚠ | Q4 · 8–12 | Q4 · 20–25 | Q4 · 4–5 | ✖ | ✖ |

**Notes:**
- **Frontier MoE giants (MiniMax M2.5, Mistral Large 3, GLM-5.2, DeepSeek V4 Flash, Kimi K3)** don't fit any consumer/local machine except the big-memory workstations — see Part 2.
- **Hailo-8/10 and Coral** can't meaningfully run LLMs: Hailo-8/10 handles Ministral 3 3B and the tiniest sub-12B variants at 5–20 tok/s; Coral is vision-only (4 TOPS).
- `⚠ (32G)` / `(64G+)` / `(32G+)` = needs that much RAM; on lower-RAM units of the same class it's ✖.
- Vision speeds assume the vision encoder overhead on top of the listed decode rate.

---

## Part 2 — Frontier models × data-center & cloud

| Model (Q4 size) | DGX Station 748G | B300 288G | MI355X 288G | B200 192G | Crescent 160G | H200 141G | Gaudi 3 128G | RTX PRO 6000 96G | Trainium2 UltraServer | TPU v7 pod | SambaNova SN50 | Cerebras (44G SRAM) | Groq LPU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **MiniMax M2.5** (230B, ~130 GB Q4) | ✓ Q4 | ✓ Q4 1 GPU | ✓ Q4 1 card | ✓ Q4 1 GPU | ✓ Q4 ⚠ | ✓ Q4 ⚠ | ✖ (130 vs 128) | ✖ | ✓ | ✓ | ✓ | ✖ | ✖ |
| **Mistral Large 3** (675B, ~380 GB Q4) | ✓ Q4 | 2× Q4 | 2× Q4 | 3× Q4 | 3× Q4 | 3× Q4 | 6× Q4 | ✖ | ✓ | ✓ | ✓ | ✖ | ✖ |
| **GLM-5.2** (~744B, ~420 GB Q4) | ✓ Q4 | 2× Q4 | 2× Q4 | 3× Q4 | 3× Q4 | 3× Q4 | 4× Q4 | ✖ | ✓ | ✓ | ✓ | ✖ | ✖ |
| **DeepSeek V4 Flash** (~600B+ est., API-first) | ✓ Q3–Q4 | 2× Q4 | 2× Q4 | 3× Q4 | 3× Q4 | 3× Q4 | 5× Q4 | ✖ | ✓ | ✓ | ✓ | ✖ | ✖ |
| **Kimi K3** (~1T est.) | ✓ Q3 ⚠ | 3× Q4 | 3× Q4 | 4× Q4 | 4× Q4 | 4× Q4 | 8× Q4 | ✖ | ✓ | ✓ | ✓ | ✖ | ✖ |
| **Qwen3-Coder-Next** (MoE, size TBD) | ✓ | small: 1–2× | small: 1–2× | 1–2× | 1× ⚠ | 1× ⚠ | 2× | 1× ⚠ | ✓ | ✓ | ✓ | ⚠ (small variant) | ⚠ (small variant) |
| **gpt-oss-120B** (~70 GB Q4) | ✓ | ✓ 1 GPU | ✓ 1 card | ✓ 1 GPU | ✓ | ✓ | ✓ ⚠ | ✓ | ✓ | ✓ | ✓ | ✓* | ✓ (476 tok/s)* |
| **Mistral Medium 3** (~28 GB) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Notes:**
- **`n× Q4`** = spans n GPUs at Q4 (per-GPU capacities: B300/MI355X 288 GB, B200 192 GB, Crescent 160 GB, H200 141 GB, Gaudi 128 GB).
- **`*` on gpt-oss-120B (Cerebras/Groq):** vendor-reported support (3,000 tok/s Cerebras, 476 tok/s Groq) — exceeds Cerebras' stated 44 GB on-chip SRAM budget, so treat as vendor-verified rather than spec-derived.
- **Trainium2 / TPU v7 / SambaNova** column = the whole pod/system, not one chip — all frontier models fit at pod scale; these win on cost-per-token.
- **H200 / Gaudi 3** cells are `⚠` where Q4 barely fits (capacity minus context overhead); drop to Q3 for headroom.
- **Inferentia3** is not for these giants — it serves embeddings/ASR/rerankers (Part 3).
- **Maia 200 & MTIA** are internal/indirect — you get them through Azure OpenAI / Meta services, not by choosing a model (see Part 4).

---

## Part 3 — Non-LLM workloads × device classes

| Workload / model | 32G GPU | 24G GPU | 16G GPU | 12G GPU | Mac 64G+ | DGX Spark | Mini-PC | Jetson Thor/AGX | Nano/Pi | Hailo/Coral |
|---|---|---|---|---|---|---|---|---|---|---|
| **Qwen Image 3.0 / 3.0 Pro** (image, Aug 2026) | ✓ fast | ✓ | ✓ | ✓ fp8 | ✓ | ⚠ slow | ✖ | ⚠ (Thor) | ✖ | ✖ |
| **Muse Spark 1.2** (image, Aug 2026) | ✓ | ✓ | ✓ | ✓ fp8 | ✓ | ⚠ | ✖ | ⚠ (Thor) | ✖ | ✖ |
| **FLUX.1-dev** (image, fallback) | ✓ | ✓ | ✓ | ✓ fp8 | ✓ | ⚠ | ✖ | ⚠ (Thor) | ✖ | ✖ |
| **SDXL** (image, fallback) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slow | ⚠ | ✓ (Thor) / ⚠ (Orin) | ✖ | ✖ |
| **Voxtral Transcribe 2** (ASR, Feb 2026) | ✓ real-time ×20 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ⚠ tiny profile |
| **Whisper large-v3** (ASR, fallback) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ⚠ (small) | ⚠ (tiny) |
| **Kokoro / F5-TTS** (TTS) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (Kokoro) | ⚠ |
| **Qwen3-Embedding** (RAG) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **bge-m3** (RAG, fallback) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **YOLOv11/v12** (vision) | ✓ 100+ FPS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (Thor/Orin real-time) | ✓ | ✓ 30–200 FPS |
| **Gemma 3 27B** (VLM — see Part 1) | ✓ | ✓ | Q3 ⚠ | ✖ | ✓ | ✓ | ⚠ | ✓ | ✖ | ✖ |

**Notes:** image-gen models are VRAM-hungry in fp16 — use fp8/Q8 on 16–24 GB and Q4 on 12 GB. ASR/TTS/embeddings run everywhere, which is why they dominate mini-PC and edge use. Coral (4 TOPS) = tiny vision only (MobileNet-class, YOLOv*n* at low res).

---

## Part 4 — Closed API models (no local hardware)

These are the newest *closed* frontier models — cloud-only, no weights, so no hardware row exists. They matter as benchmarks/references (and as what hyperscaler silicon *serves* — Maia serves GPT-class, TPU serves Gemini-class).

| Model | Developer | Released | Access | Serves on |
|---|---|---|---|---|
| **GPT-5.3-Codex** | OpenAI | Feb 5, 2026 | API | Azure/Microsoft Maia infrastructure |
| **Claude Opus 4.6** (+ Fast mode) | Anthropic | Feb 2026 | API (Anthropic, Bedrock, Vertex) | rented NVIDIA fleets |
| **Gemini 3 Deep Think** | Google | Feb 2026 | API / Ultra | Google TPU v7 Ironwood |

**Takeaway:** if you want these locally, you can't — the closest open equivalents are GLM-5.2 (agentic coding), DeepSeek V4 Flash (value), and Kimi K3 (multimodal agents), all in Part 2.

---

## Quantization quick reference (Q4_K_M, GGUF)

| Model | Params | Q4 size | Q3 size |
|---|---|---|---|
| Ministral 3 3B | 3B | 1.9 GB | 1.5 GB |
| Ministral 3 8B / Qwen3.5 / Gemma 4 sub-12B | 8B | 5 GB | 3.8 GB |
| Ministral 3 14B | 14B | 8.6 GB | 6.5 GB |
| Devstral 2 | 24B | 14 GB | 11 GB |
| Gemma 3 27B | 27B | 16.5 GB | 12.4 GB |
| GLM-4.7-Flash | 30B-A3B | 17–19 GB | ~14 GB |
| Mistral Medium 3 | 48B class | ~28 GB | ~21 GB |
| gpt-oss-120B | 120B | ~70 GB | ~52 GB |
| MiniMax M2.5 | 230B | ~130 GB | ~98 GB |
| Mistral Large 3 | 675B | ~380 GB | ~290 GB |
| GLM-5.2 | ~744B | ~420 GB | ~320 GB |

*Add ~1–2 GB for context/KV cache and runtime overhead. Frontier MoE sizes (DeepSeek V4 Flash, Kimi K3) are estimates until official numbers ship.*
