# Hyperscaler Custom Silicon

Google, AWS, Microsoft, and Meta built their own inference chips to escape NVIDIA pricing. These are **cloud-only** — you consume them via the provider's cloud, not by buying hardware. They win on **cost per token** and, increasingly, raw speed. **All model picks lead with the newest releases (Aug 2026) — these clouds are where the open MoE giants get served cheaply.**

---

## Google TPU v7 "Ironwood"

**The first TPU explicitly designed for inference.**

| Spec | Value |
|---|---|
| Architecture | 7th-gen TPU; each chip: 2 TensorCores + 4 SparseCores |
| Memory | 192 GB HBM3E per chip |
| Bandwidth | 7.37 TB/s per chip |
| Compute | 4.61 PFLOPS FP8 per chip |
| Scale | Up to 9,216 chips per pod (10,000+ chip "Ironwood Pod") |
| Efficiency | 10× peak performance vs TPU v5p; >4× perf-per-chip for training *and* inference |
| Availability | GA November 2025 (Google Cloud) |

**Best for:** Serving "thinking" models (long reasoning traces = inference-heavy) and Gemini-scale workloads; extremely strong at batched, high-throughput inference.

**Recommended AI models (newest first):**
- **Cloud serving (Vertex AI / GKE):** **Gemma 3 27B** (Jul 2026, Google's newest open model), **GLM-5.2**, **DeepSeek V4 Flash**, **MiniMax M2.5**, **Kimi K3**, **Mistral Large 3** — via vLLM/JAX on TPU.
- **Best workloads:** high-volume embedding generation, batch RAG pipelines, multimodal serving, reasoning models — where cost-per-inference dominates.
- **Note:** JAX/TPU ecosystem differs from CUDA; most OSS inference stacks now support TPU, but expect friction vs NVIDIA.

---

## AWS Trainium2 / Trainium3 & Inferentia

**AWS's answer: best price-performance for inference at scale.**

| Spec | Trainium2 | Trainium3 (Dec 2025) | Inferentia3 |
|---|---|---|---|
| Memory | 96 GB HBM3e | 144 GB HBM3e | for inference (specs TBD) |
| Bandwidth | 2.9 TB/s | 4.9 TB/s | — |
| Compute | 1.3 PFLOPS FP8 (5.2 PF sparse) | 2.52 PFLOPS FP8 | — |
| Process | — | 3 nm | — |
| Availability | GA Dec 2024 (Trn2, Trn2 UltraServers) | 2025–26 | announced 2025, rolling out |

**Systems:** Trn2 instance = 16 chips (1.5 TB HBM, 46 TB/s); Trn2 UltraServer = 64 chips. AWS claims 30–40% better price-performance than comparable GPU instances.

**Recommended AI models (newest first):**
- **Trn2 (Neuron + vLLM):** **MiniMax M2.5** (230B — fits across 16 chips), **Mistral Medium 3**, **GLM-4.7-Flash**, **Gemma 3 27B**, **DeepSeek V4 Flash** — served at very low $/token.
- **Trn2 UltraServer:** **GLM-5.2** (744B), **Kimi K3**, **Mistral Large 3** (675B), **DeepSeek V4 Flash** at production scale.
- **Inferentia:** lightweight serving — embeddings (Qwen3-Embedding, bge-m3), rerankers, **Voxtral Transcribe 2** ASR, small diffusion — at the cheapest rates in AWS.

---

## Microsoft Maia 200

| Spec | Value |
|---|---|
| Memory | 216 GB HBM3e |
| Bandwidth | ~7 TB/s |
| Process | TSMC 3 nm |
| Claim | Microsoft says ~3× the power of Google's TPU v7 |
| Status | In production; powers internal + Azure OpenAI inference |

**Best for:** Microsoft's internal GPT-family serving and Azure OpenAI capacity (not directly purchasable; you get it via Azure AI services).

**Recommended models:** the newest Azure OpenAI models (GPT-5.3-class, o-series reasoning) and Microsoft's MAI open-model work — Maia is the silicon behind them.

---

## Meta MTIA (v2)

| Spec | Value |
|---|---|
| Focus | Inference for Meta's recommendation/ranking systems |
| Status | v1 deployed 2024; v2 in deployment 2025–26 |
| Access | Not sold — internal only |

**Best for:** Meta's own massive-scale recommendation inference (not accessible to developers).

---

## Which hyperscaler chip for you?

| Chip | Access | Strength | Best for |
|---|---|---|---|
| TPU v7 Ironwood | Google Cloud | Speed + efficiency, huge pods | Thinking models, Gemma 3, batch serving |
| Trainium2/3 | AWS (Trn2) | Cost per token | Production open-MoE serving (M2.5, GLM-5.2) |
| Inferentia3 | AWS | Cheap light workloads | Embeddings, reranking, ASR |
| Maia 200 | Azure (indirect) | GPT-class serving | Azure OpenAI users |
| MTIA | internal | Rec systems | — |

**Bottom line:** if you're choosing a cloud for open-model serving in 2026, benchmark your exact workload on Trn2 vs GPU instances — the cost gap is real, and vLLM/Neuron support is now production-grade for the newest MoE giants. If you need Gemini/GPT ecosystem features, you get TPU/Maia as part of the platform either way.
