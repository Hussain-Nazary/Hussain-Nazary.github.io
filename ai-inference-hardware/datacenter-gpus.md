# Data-Center GPUs & Accelerators

The cloud/server workhorses for training and serving AI. For pure *inference*, the 2025–2026 generation added **FP4 support** and much larger HBM — inference is now a first-class design goal, not an afterthought. **All model picks lead with the newest releases (Aug 2026): the open MoE giants — GLM-5.2, Kimi K3, DeepSeek V4 Flash, MiniMax M2.5, Mistral Large 3 — are what this class of hardware serves.**

---

## NVIDIA Blackwell B200 / B300 (HGX)

**The incumbent standard for cloud inference and training.**

| Spec | B200 | B300 (Blackwell Ultra) |
|---|---|---|
| Memory | 192 GB HBM3e | 288 GB HBM3e |
| Memory bandwidth | ~8 TB/s | ~8 TB/s |
| Compute (FP8 dense) | ~2.25 PFLOPS | ~2× B200 inference (FP4) |
| FP4 support | Yes | Yes |
| Interconnect | NVLink 5 / NVSwitch | NVLink 5 / NVSwitch |
| Availability | Shipping since 2025 | GA 2025–2026 |
| Typical price (per GPU, cloud) | ~$25–40/hr rental (8-GPU DGX) | higher |

**Best for:** Serving the newest frontier open models and GPT-scale workloads where the software ecosystem (vLLM, TensorRT-LLM, Triton) is the safest bet. A single 8× Blackwell DGX set a world record at GTC 2025: **>250 tok/s per user and >30,000 tok/s aggregate on DeepSeek-R1**.

**Recommended AI models (newest first):**
- **Serving (frontier open):** **DeepSeek V4 Flash 0731** (Jul 2026), **GLM-5.2** (Jun 2026), **Kimi K3** (Jul 2026), **MiniMax M2.5** (Feb 2026), **Mistral Large 3** (Dec 2025), **Qwen3-Coder-Next** (Feb 2026) — all served in production with vLLM/SGLang at FP8.
- **Per-GPU fit:** B300's 288 GB fits **MiniMax M2.5 Q4 (~130 GB)** or **gpt-oss-120B FP8 (~120 GB)** on a *single* GPU; **Mistral Large 3 FP8 (675B)** spans ~3 GPUs; **GLM-5.2 (744B)** spans ~3–4 GPUs.
- **Low latency:** FP4 quantization (native support) roughly doubles throughput vs FP8 for chat workloads.

---

## NVIDIA H200 (previous generation, still widely rented)

| Spec | Value |
|---|---|
| Memory | 141 GB HBM3e |
| Bandwidth | 4.8 TB/s |
| Compute | ~990 TFLOPS FP8 (dense); ~1.98 PFLOPS with sparsity |
| TDP | 700 W |
| Status | Prior-gen; the most common cheap-rental inference GPU in 2025–26 |

**Best for:** Budget-friendly cloud inference — excellent price/perf for 70B-class serving.

**Recommended AI models (newest first):**
- **MiniMax M2.5 Q4** (~130 GB) fits on one H200; **Mistral Medium 3** (Jul 2026) easily; **gpt-oss-120B FP8** fits; **GLM-4.7-Flash** and **Gemma 3 27B** fly; 675B-class (Mistral Large 3) needs 5+ GPUs.

---

## NVIDIA RTX PRO 6000 Blackwell (workstation)

| Spec | Value |
|---|---|
| Memory | 96 GB GDDR7 |
| Bandwidth | ~1.8 TB/s |
| Form factor | single-slot workstation card |
| Price | ~$8,000–10,000 |

**Best for:** On-prem inference workstations where 96 GB in a single PCIe card beats consumer cards (96 GB fits Mistral Medium 3, gpt-oss-120B Q4, and GLM-4.7-Flash with huge headroom).

**Recommended AI models (newest first):**
- **Mistral Medium 3** (Jul 2026) FP8 → very fast; **gpt-oss-120B Q4** (~70 GB) fully on-card → ~50–70 tok/s; **GLM-4.7-Flash** Q4 → ~100+ tok/s; **Gemma 3 27B** fp8; fine-tuning LoRA on 70B.

---

## AMD Instinct MI355X (CDNA 4)

**AMD's strongest inference play yet — 288 GB with FP4/FP6 support.**

| Spec | Value |
|---|---|
| Architecture | CDNA 4 |
| Memory | 288 GB HBM3E |
| Bandwidth | 8 TB/s |
| Compute | ~2.3 PFLOPS FP8; MXFP6/MXFP4 datatypes |
| TDP | 1,400 W |
| Availability | GA October 2025 |
| Price | ~$30–40K (est., less than comparable NVIDIA) |

**Best for:** High-capacity, high-bandwidth inference at aggressive pricing; AMD's vLLM/ROCm results on the MI355X match or beat the B200 on several LLM workloads (independent Signal65 + AMD benchmarks).

**Recommended AI models (newest first):**
- **Serving (vLLM):** **MiniMax M2.5 Q4 (~130 GB)** fits on a *single* card; **Mistral Medium 3** FP8; **gpt-oss-120B FP8**; **DeepSeek V4 Flash / GLM-5.2** FP8 across 3–4 cards; **Kimi K3** across 4+.
- **Edge case:** 288 GB means most open models fit on **one** card — simplifies serving clusters.
- **Note:** ROCm ecosystem is narrower than CUDA — verify your stack (vLLM supported; some tools aren't).

---

## AMD Instinct MI450 / MI400 series (2026)

| Spec | Value |
|---|---|
| Architecture | CDNA Next |
| Memory | HBM4 (announced) — large capacity + higher bandwidth |
| Status | Expected 2026 |

**Best for:** Next-gen price/performance — HBM4 delivers a major bandwidth jump that directly benefits inference.

**Recommended AI models:** same family as MI355X (all newest open models via vLLM); watch for FP4-era optimizations.

---

## Intel Gaudi 3 (HL-338)

**The cost-effective NVIDIA alternative — Ethernet-connected, no NVLink lock-in.**

| Spec | Value |
|---|---|
| Memory | 128 GB HBM2e (8 stacks) |
| Bandwidth | 3.7 TB/s |
| Compute | 1,835 TFLOPS BF16/FP8 |
| On-die SRAM | 96 MB |
| Networking | 24× 200 GbE RoCE v2 ports (built-in) |
| TDP | 600 W (PCIe card; 900 W air-cooled OAM) |
| Price | ~$12–15K — roughly half an H100's price |
| Form factor | PCIe Gen5 card + 8-card OAM server |

**Best for:** Price-sensitive inference/training at 70B scale with standard Ethernet fabrics.

**Recommended AI models (newest first):**
- **Mistral Medium 3** (Jul 2026) BF16 → 1–2 cards; **gpt-oss-120B Q4 (~70 GB)** on one card; **GLM-4.7-Flash** and **Gemma 3 27B** at high batch; **MiniMax M2.5 Q4 (~130 GB)** tight on one card. HPU Graph Compiler + vLLM support is good; smaller tooling ecosystem than CUDA.

---

## Intel Crescent Island (announced Oct 2025) & Jaguar Shores

| Spec | Crescent Island | Jaguar Shores |
|---|---|---|
| Architecture | Xe3P-based, **inference-optimized** | Next-gen follow-on |
| Memory | 160 GB LPDDR5X | TBD |
| Status | Customer sampling H2 2026 | Expected 2027 |

**Best for:** Intel's reboot of the data-center AI line (Falcon Shores was cancelled in 2025) — a dedicated inference GPU using cheaper LPDDR5X instead of HBM, targeting inference cost-per-token.

**Recommended AI models:** gpt-oss-120B Q4 (~70 GB) fits in 160 GB; Mistral Medium 3; expected to serve the newest open models (Gemma 3, GLM-4.7-Flash, MiniMax M2.5 at Q4) at low cost per token when it ships.

---

## Comparison at a glance

| Accelerator | Memory | Bandwidth | FP8 compute | Price class | Newest-model fit |
|---|---|---|---|---|---|
| B200 | 192 GB HBM3e | 8 TB/s | 2.25 PF | $$$$ | MiniMax M2.5 Q4, gpt-oss-120B FP8 |
| B300 | 288 GB HBM3e | 8 TB/s | ~2× B200 (FP4) | $$$$$ | MiniMax M2.5 single-GPU; GLM-5.2 across 3–4 |
| H200 | 141 GB HBM3e | 4.8 TB/s | ~1 PF | $$$ | MiniMax M2.5 Q4, Mistral Medium 3 |
| MI355X | 288 GB HBM3E | 8 TB/s | ~2.3 PF | $$$ | MiniMax M2.5 single-card; DeepSeek V4 Flash |
| Gaudi 3 | 128 GB HBM2e | 3.7 TB/s | 1.84 PF | $$ | Mistral Medium 3, gpt-oss-120B Q4 |
| Crescent Island | 160 GB LPDDR5X | — | — | $ (est.) | Inference-optimized (2026) |
