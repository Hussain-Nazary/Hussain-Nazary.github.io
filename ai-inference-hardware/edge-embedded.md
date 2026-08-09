# Edge & Embedded Inference Hardware

For cameras, robots, kiosks, vehicles, drones, and on-device AI with no cloud connection. Selection is driven by **power budget** (watts) and **model class** (tiny vision nets vs on-device LLMs). **All model picks lead with the newest releases (Aug 2026) — Ministral 3 is the edge-native LLM line, Voxtral the edge-native STT.**

---

## NVIDIA Jetson Thor

**The flagship edge module for robotics / "physical AI".**

| Spec | Value |
|---|---|
| AI compute | 2,070 FP4 TFLOPS (~7.5× AGX Orin; ~3.5× efficiency) |
| Memory | 128 GB LPDDR5x |
| Power | 40–130 W (configurable) |
| Module | Jetson T5000; developer kit available |
| Software | JetPack, Isaac (robotics), CUDA |

**Best for:** Autonomous robots, drones, industrial inspection, and **on-device LLM/VLM agents** — it's a DGX-Spark-class compute in an embedded form factor.

**Recommended AI models (newest first):**
- **LLM/VLM on device:** **Ministral 3 3B/8B/14B** (Dec 2025 — Mistral explicitly optimized it for Jetson) → 8B: 20–40 tok/s, 14B: 12–18 tok/s; **GLM-4.7-Flash Q4** (30B-A3B, Jan 2026) → ~8–12 tok/s; **Gemma 3 27B** (Jul 2026, native multimodal) → ~10 tok/s — vision-language for robots.
- **Bigger (slow but fits 128 GB):** Mistral Medium 3 (Jul 2026) → ~5–6 tok/s; gpt-oss-120B Q4 → ~4–5 tok/s.
- **Classic vision:** YOLOv11/v12 (real-time at 100+ FPS), DeepLab, EfficientDet for detection/segmentation pipelines.
- **Speech:** **Voxtral Transcribe 2** (Feb 2026, on-device STT with diarization — beats Whisper on FLEURS), Kokoro TTS for robot voice.

---

## NVIDIA Jetson AGX Orin (64 GB)

| Spec | Value |
|---|---|
| AI compute | 275 TOPS (INT8) |
| Memory | 64 GB LPDDR5 |
| Power | 15–60 W |
| Price | ~$2,000 (dev kit / module) |

**Best for:** Production edge AI — the workhorse of industrial/retail/agriculture deployments.

**Recommended AI models (newest first):**
- **Vision:** YOLOv11/v12 (real-time), DeepStream pipelines for multi-camera, PoseNet, OCR (PaddleOCR).
- **Language:** **Ministral 3 3B/8B** (Dec 2025) → 8B: 10–25 tok/s; **GLM-4.7-Flash Q4** (Jan 2026) → ~6–10 tok/s; Gemma 3 12B → 10–15 tok/s.
- **Audio:** **Voxtral Transcribe 2**; F5-TTS (small).

---

## NVIDIA Jetson Orin Nano Super ($249 dev kit)

| Spec | Value |
|---|---|
| AI compute | 67 TOPS (INT8) — "Super" mode |
| Memory | 8 GB LPDDR5 |
| Power | 7–25 W |
| Price | ~$249 (dev kit) |

**Best for:** The budget entry point into edge AI — hobbyists, students, small products.

**Recommended AI models (newest first):**
- **Vision:** YOLOv8n/s/v11n (real-time), MobileNet, EfficientNet-Lite, PoseNet, FaceNet.
- **Language (small only):** **Ministral 3 3B Q4** (Dec 2025) → 5–10 tok/s; Qwen3.5 sub-12B smallest variant; Gemma 4 sub-12B tiny.
- **Audio:** **Voxtral Transcribe 2** (tiny profile) or Whisper tiny/base/small.
- **Embeddings:** bge-small-en — fast enough for on-device RAG.

---

## Hailo-8 / Hailo-8L / Hailo-10

**Ultra-low-power NPU accelerator cards (M.2 / USB / PCIe).**

| Spec | Hailo-8 | Hailo-8L | Hailo-10 |
|---|---|---|---|
| AI compute | 26 TOPS (INT8) | 13 TOPS | 40 TOPS |
| Power | ~2.5 W | ~1.5 W | ~2.5 W |
| Use | M.2 card, NVRs, cameras | Raspberry Pi AI Kit, laptops | 2025+ — laptops, edge boxes |

**Best for:** Adding cheap NPU acceleration to existing PCs, NVRs, and the Raspberry Pi 5. Great at vision; transformer support (including small LLMs) has improved steadily.

**Recommended AI models (newest first):**
- **Vision (primary):** YOLOv11/v12, ResNet, MobileNet, EfficientDet, FaceNet, pose estimation — 30–200 FPS depending on model size.
- **Language (Hailo-8/10):** **Ministral 3 3B** (edge-optimized), Gemma 4 / Qwen3.5 sub-12B smallest variants (via Hailo's transformer support — more limited than GPU options).
- **Audio:** **Voxtral Transcribe 2** (tiny) or Whisper tiny/base.

---

## Google Coral (Edge TPU)

| Spec | Value |
|---|---|
| AI compute | ~4 TOPS (INT8) |
| Power | ~2 W |
| Form factors | USB accelerator, M.2, dev board |
| Price | ~$25–150 |

**Best for:** The cheapest, most power-efficient way to run lightweight vision models continuously (battery-powered cameras, always-on sensing).

**Recommended AI models:**
- MobileNetV2/V3, EfficientNet-Lite, SSD-MobileNet, PoseNet, DeepLab — all at 30–100 FPS on 2 W.
- **Not for:** LLMs or anything beyond tiny vision nets — 4 TOPS is a hard ceiling.

---

## Raspberry Pi 5 + AI Kit (Hailo-8L)

| Spec | Value |
|---|---|
| AI compute | 13 TOPS (Hailo-8L) |
| CPU | Quad-core Cortex-A76 (Pi 5) |
| RAM | 4/8/16 GB |
| Price | ~$80 (Pi) + ~$70 (AI Kit) |

**Best for:** The ultimate hobbyist local-AI box — this repo's `run-llm-raspberry-pi.html` covers it in depth.

**Recommended AI models (newest first):**
- **Vision:** YOLOv11n (real-time), MobileNet, pose estimation.
- **Language:** **Ministral 3 3B** (Dec 2025) → 2–5 tok/s (slow but real); Qwen3.5 sub-12B smallest variant; **Voxtral Transcribe 2** for voice.
- **Practical use:** voice assistants, smart-home agents, on-device photo classification, tiny RAG.

---

## Quick decision table

| Device | TOPS | Power | Price | Model class | Newest-model sweet spot |
|---|---|---|---|---|---|
| Jetson Thor | 2,070 FP4 | 40–130 W | ~$2K+ (module) | 3–120B LLM/VLM | Ministral 3 14B, GLM-4.7-Flash, Gemma 3 27B |
| Jetson AGX Orin | 275 | 15–60 W | ~$2K | 1–30B + vision | Ministral 3 8B, GLM-4.7-Flash |
| Orin Nano Super | 67 | 7–25 W | $249 | 1–3B + vision | Ministral 3 3B |
| Hailo-8/8L/10 | 13–40 | 1.5–2.5 W | $30–100 | Vision + small LLM | YOLOv11/v12, Ministral 3 3B |
| Coral Edge TPU | 4 | 2 W | $25–150 | Tiny vision | MobileNet/EfficientNet-Lite |
| Pi 5 + AI Kit | 13 | ~10 W total | ~$150 | 1–3B + vision | Ministral 3 3B, Voxtral |

**Bottom line:** pick by power budget first (watts decide everything at the edge), then by model class. Jetson = real compute, Hailo/Coral = ultra-efficient vision, Pi + AI Kit = the $150 tinkerer's dream — and on all of them, **Ministral 3** and **Voxtral** are the newest models built for exactly this class of hardware.
