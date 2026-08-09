# Inference-First ASICs (the new challengers)

These chips reject the general-purpose GPU design and are built for **one job: pushing tokens out as fast as possible**. The trick: model weights live in **on-chip SRAM** instead of being fetched from HBM — removing the memory-bandwidth bottleneck that caps GPU inference. They're sold as **cloud services** (API + rental), not as hardware you buy. **All model picks lead with the newest releases (Aug 2026).**

---

## Cerebras WSE-3 (CS-3 systems)

**The speed king — a chip the size of a wafer with everything on-chip.**

| Spec | Value |
|---|---|
| Chip | Wafer-Scale Engine 3 — entire 300 mm wafer, single "chip" |
| AI cores | ~900,000 |
| On-chip SRAM | 44 GB (all model weights stay on-die) |
| Peak compute | 125 PFLOPS (marketing) |
| Memory bottleneck | None — no HBM, no paging |
| Status | Production; Cerebras IPO'd to a $40B+ market cap (2025–26) |
| Access | Cerebras Inference API / cloud rental |

**Why it's fast:** because there's no external memory, inference isn't bandwidth-bound — reported speeds of **2,000–3,000+ tokens/s** on large models (3,000 tok/s on gpt-oss-120B, independently verified).

**Recommended models (newest first):**
- **Sweet spot (≤44 GB on-chip):** **Gemma 3 27B** (Jul 2026), **GLM-4.7-Flash** (30B-A3B, Jan 2026), **Devstral 2 / Small 2** (Dec 2025 coding), **Ministral 3 14B** — all at thousands of tok/s; larger: **gpt-oss-120B**, DeepSeek-R1-Distill, Llama 3.3 70B.
- **Not on Cerebras (yet):** the MoE giants (DeepSeek V4 Flash, GLM-5.2, MiniMax M2.5, Kimi K3, Mistral Large 3) exceed the 44 GB on-chip budget — those go to GPU fleets or SambaNova.
- **Best workloads:** high-volume generation, batch summarization, agent loops that hammer an API.
- **Not for:** CUDA-specific code — you consume via API, you can't run arbitrary code.

---

## Groq LPU (Language Processing Unit)

**The deterministic-latency pioneer.**

| Spec | Value |
|---|---|
| Architecture | LPU (Language Processing Unit) — SRAM-based, software-defined tensor streaming |
| Memory | SRAM per chip (~230 MB class), large fast interconnects |
| Status | Production; Groq acquired for ~$20B (2025) |
| Access | GroqCloud API + on-prem racks for enterprises |

**Why it's fast:** deterministic, low-latency token delivery. Reported **250–750+ tok/s** depending on model (476 tok/s on gpt-oss-120B; ~750 tok/s decode on Llama 4 70B) — typically 5–20× faster than GPU endpoints.

**Recommended models (newest first):**
- **Fastest tier:** **Gemma 3 27B** (Jul 2026), **GLM-4.7-Flash** (Jan 2026), **Devstral 2 / Small 2**, **Ministral 3 14B/8B** (Dec 2025), plus **gpt-oss-120B/20B**, Llama 4 Scout, DeepSeek-R1-Distill, Qwen3 — the newest models that fit the LPU memory model.
- **Best workloads:** real-time chat UX, coding assistants, voice agents (low first-token latency).
- **Not for:** the 230–744B MoE giants (capacity) or massive batch throughput.

---

## SambaNova SN40L / SN50 (RDU)

**The reconfigurable dataflow option — and the ASIC home for the newest giants.**

| Spec | Value |
|---|---|
| Architecture | RDU (Reconfigurable Dataflow Unit) — compiler-mapped dataflow, huge on-chip SRAM |
| Capacity | SN40L: 104 GB total (HBM + SRAM) |
| Status | SN40L in production; SN50 "frontier" system deploying 2026 |
| Access | SambaNova Cloud / enterprise systems |

**Why it's fast:** dataflow architecture keeps weights on-chip like Cerebras/Groq, with flexible compiler mapping. Reported **~457 tok/s on Llama 3.1-70B** and ~198 tok/s per user on a 671B DeepSeek-class model (16-chip SN40L system).

**Recommended models (newest first):**
- **The giant-MoE specialists:** **DeepSeek V4 Flash 0731** (Jul 2026), **GLM-5.2** (Jun 2026), **Kimi K3** (Jul 2026), **Mistral Large 3** (Dec 2025) — SambaNova is one of the few services serving 600B+ open models at usable per-user speeds.
- **Mid:** Gemma 3 27B, GLM-4.7-Flash, MiniMax M2.5 (230B) on SN50.
- **Best workloads:** enterprise private deployments where data stays on-prem, plus giant-model serving without buying NVIDIA racks.

---

## Head-to-head

| Platform | Reported speed | Newest models it serves | Access model | Best for |
|---|---|---|---|---|
| Cerebras | 2,000–3,000+ tok/s | ≤44 GB: Gemma 3 27B, GLM-4.7-Flash, Devstral 2, gpt-oss-120B | API | Max throughput, batch generation |
| Groq | 250–750 tok/s | ≤120B via multi-LPU: Gemma 3 27B, GLM-4.7-Flash, gpt-oss-120B | API + on-prem | Lowest latency, real-time UX |
| SambaNova | ~200–460 tok/s/user | **Up to 744B: DeepSeek V4 Flash, GLM-5.2, Kimi K3, Mistral Large 3** | API + enterprise | Giant models on-prem |

**Bottom line:** these are the "fast inference" story of 2025–26 — typically 5–20× faster than GPU endpoints for the same open model. Cerebras and Groq own the sub-120B speed crown with the newest mid-size models; SambaNova is the ASIC answer for the newest 600B+ MoE giants. Trade-offs: API/cloud products (no arbitrary code), premium per-token pricing, and GPU fleets still win on flexibility and cost at very high batch volume.
