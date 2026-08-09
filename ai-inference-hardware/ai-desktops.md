# AI Desktops & Workstations

Whole systems built (or repurposed) for local AI: turnkey AI supercomputers, NPU-powered mini-PCs, and the Mac Studio. **All model picks lead with the newest releases (Aug 2026).**

---

## NVIDIA DGX Spark

**"An AI supercomputer on your desk" — the easiest way to run 100B+ models locally.**

| Spec | Value |
|---|---|
| Chip | GB10 Grace Blackwell superchip (20-core Arm CPU: 10× Cortex-X925 + 10× Cortex-A725) |
| AI compute | 1 PFLOPS FP4 (~1,000 AI TOPS), 5th-gen Tensor Cores |
| Memory | 128 GB unified LPDDR5x (256-bit, 273 GB/s) — shared CPU/GPU |
| Storage | 4 TB NVMe SSD |
| Networking | ConnectX-7 Smart NIC (200 GbE) |
| Power | ~200 W (fanless, desktop form factor) |
| Price | $4,699 (was $3,999 at announcement, Mar 2025; rose late 2025) |
| Software | DGX OS (Linux), preloaded NVIDIA AI stack (NIM, CUDA, PyTorch) |

**Best for:** Running up to **200B-parameter models** out of the box, prototyping/agent workloads, and teams that want CUDA without buying a server. Mistral Medium 3 and gpt-oss-120B fit fully in memory.

**Recommended AI models (newest first):**
- **Flagship fit (128 GB):** **Mistral Medium 3** (Jul 2026, 48GB-class → fits with room to spare) → ~6–8 tok/s decode (bandwidth-limited) but excellent for agents/batching; **gpt-oss-120B Q4** (~70 GB) → ~5–6 tok/s; **MiniMax M2.5** (230B, Q4 ~130 GB) is right at the edge — Q3 or API instead; **DeepSeek V4 Flash / GLM-5.2 / Kimi K3** are MoE giants → API/enterprise only.
- **Sweet spot (speed):** **GLM-4.7-Flash Q4** (30B-A3B, Jan 2026) → ~12–15 tok/s; **Gemma 3 27B Q4** (Jul 2026) → ~15 tok/s; **Devstral 2 Q4** (24B coding) → ~18 tok/s; Ministral 3 14B → ~25 tok/s.
- **Multimodal:** **Gemma 3 27B** (native multimodal, Jul 2026); Qwen2.5-VL-72B Q4 (~41 GB) — vision at scale, slow but capable.
- **Batch/agent workloads:** run vLLM with multiple concurrent requests — the 128 GB unified pool shines for multi-user serving of the newest small models.

---

## NVIDIA DGX Station (GB300)

**Workstation-grade: a desktop that competes with a rack of GPUs.**

| Spec | Value |
|---|---|
| Chip | GB300 Grace Blackwell Ultra superchip (72-core Arm Neoverse V2 CPU + Blackwell Ultra GPU) |
| AI compute | 20 PFLOPS FP4 |
| Memory | 748 GB coherent total: 496 GB LPDDR5x (396 GB/s) + 252 GB HBM3e (8 TB/s) |
| Networking | ConnectX-8 (800 GbE) |
| Price | ~$70,000–110,000 (NVIDIA list ~$69.9K; OEM/reseller pricing higher) |

**Best for:** Teams/researchers running **today's frontier open models** (GLM-5.2, Mistral Large 3, MiniMax M2.5, Kimi K3, DeepSeek V4 Flash) fully locally with data privacy, or fine-tuning at workstation scale.

**Recommended AI models (newest first):**
- **Frontier open (fits 748 GB):** **GLM-5.2 Q4** (~744B total → ~420 GB) → ~6–10 tok/s; **Mistral Large 3 Q4** (675B total / 41B active, Dec 2025) → ~10–14 tok/s (its 41B active params make it efficient); **MiniMax M2.5 Q4** (230B → ~130 GB) → ~15–25 tok/s; **DeepSeek V4 Flash** and **Kimi K3** (open weights, MoE) → Q2/Q3 fit, slow but real.
- **Workhorse (fast):** Gemma 3 27B → 150+ tok/s (HBM path); GLM-4.7-Flash → 180+ tok/s; gpt-oss-120B Q4 → 60–80 tok/s.
- **Fine-tuning:** LoRA/QLoRA on 70B-class fits comfortably in 748 GB.
- **Embeddings/reranking at scale:** Qwen3-Embedding, bge-m3, jina-reranker — huge batch sizes.

---

## AMD Ryzen AI 400 Desktops (Medusa Point)

**The first desktop chips officially supporting Microsoft Copilot+ (announced MWC 2026).**

| Spec | Value |
|---|---|
| CPU | Zen 5 (Medusa Point), up to 8 cores |
| NPU | XDNA2, up to 60 TOPS |
| iGPU | RDNA (up to 16 CU) |
| Memory | DDR5 (standard desktop DIMMs), 32–128 GB |
| Price (Aug 2026) | OEM desktops ~$500–1,700 (entry pricing from ~$499; loaded 16 GB/512 GB systems ~$1,660) — sold as complete PCs, no retail CPUs |

**Best for:** Everyday AI in an office/home tower — on-device Copilot+, local transcription, background agents, small models. Not for big LLMs (memory bandwidth is DDR5-class).

**Recommended AI models (newest first):**
- **On-NPU (fast, low power):** the **Qwen3.5 / Gemma 4 sub-12B line** (2026), **Ministral 3 3B/8B** (Dec 2025), **Voxtral Transcribe 2** (Feb 2026, on-device STT with diarization); Windows Copilot+ features.
- **On-GPU/CPU (bigger):** Ministral 3 14B Q4 via llama.cpp (iGPU, ~15–25 tok/s depending on RAM speed); Gemma 3 27B Q4 slow but possible on 32 GB+.
- **Best pairing:** add a discrete GPU (e.g., RX 9070 XT) — the NPU handles always-on tasks, the dGPU handles heavy inference.

---

## AI Mini-PCs (Core Ultra / Ryzen AI boxes)

**Cheap, quiet, always-on local AI boxes.**

| Spec | Value |
|---|---|
| Processors | Intel Core Ultra 200V (Lunar Lake) / 300V (Panther Lake), AMD Ryzen AI 300/400 |
| NPU | 48–60 TOPS |
| Memory | 16–96 GB LPDDR5x/DDR5 |
| Form factor | 0.5–2 L mini-PC |
| Price (Aug 2026) | ~$400–1,000 mainstream (16–32 GB); $1,000–3,000 loaded (64–128 GB Strix Halo-class); flagship AI boxes: Ryzen AI Halo $3,999, DGX Spark $4,699 |

**Best for:** Home servers, privacy-focused assistants, transcription/voice agents, and light RAG. Many folks run Ollama + Open WebUI on these 24/7.

**Recommended AI models (newest first):**
- **Comfortable:** **Ministral 3 3B/8B** (Dec 2025) → 20–40 tok/s; **Qwen3.5 / Gemma 4 sub-12B** (2026) → 15–35 tok/s; **Voxtral Transcribe 2** (on-device STT) — the standout voice pick; Gemma 3 12B on 32 GB units.
- **Stretch:** Ministral 3 14B Q4 → 10–20 tok/s (depends on memory config); GLM-4.7-Flash Q4 only on 64 GB+ units.
- **Embeddings/RAG:** Qwen3-Embedding, bge-small, nomic-embed-text.
- **TTS:** Kokoro, Piper — instant.

---

## Apple Mac Studio (M4 Max / M5 Ultra)

*See [apple-silicon.md](apple-silicon.md) for the chips; the Studio is the "big memory" chassis.*

| Spec | M4 Max Studio | M5 Ultra Studio (reported) |
|---|---|---|
| CPU / GPU | 16-core / 40-core | 36-core / 84-core (reports) |
| Neural Engine | 16-core | 32-core (reports) |
| Unified memory | up to 128 GB | up to 512 GB (768 GB per latest reports) |
| Memory bandwidth | 546 GB/s | ~1 TB/s class (reports) |
| Storage | up to 8 TB | up to 16 TB |
| Price | from ~$2,000 (base) | from ~$4,000+ (reported) |

**Best for:** The 512 GB M5 Ultra Studio is the **only mainstream machine that can hold the newest frontier open models** (Mistral Large 3, GLM-5.2, MiniMax M2.5) entirely in memory — the local-inference extreme.

**Recommended AI models (newest first):**
- **M5 Ultra (512 GB):** **MiniMax M2.5 Q4** (230B → ~130 GB) → ~15–20 tok/s; **Mistral Large 3 Q4** (675B → ~380 GB) → ~5–8 tok/s; **GLM-5.2 Q4** (~744B → ~420 GB) → ~4–6 tok/s — all *run locally*, which no other desktop can claim; gpt-oss-120B Q4 → ~20–30 tok/s; multiple 70B-class models loaded simultaneously.
- **M4 Max / M5 Max (128 GB):** **MiniMax M2.5 Q4** right at the edge (~130 GB) — Q3 or API; **Mistral Medium 3** (Jul 2026) → ~10–14 tok/s; **gpt-oss-120B Q4** (~70 GB) → ~8–10 tok/s; Gemma 3 27B → ~25–30 tok/s; GLM-4.7-Flash → ~30 tok/s; several 7–30B models at once.
- **Small/fast:** Ministral 3 14B Q4 → 50–70 tok/s; Qwen3.5 / Gemma 4 sub-12B → 80–120 tok/s.
- **Tools:** MLX (Apple's framework), llama.cpp, Ollama — all well supported.
