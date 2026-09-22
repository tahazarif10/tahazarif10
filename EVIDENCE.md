# Engineering Evidence

This page maps public profile and resume claims to reproducible evidence. Performance, safety, hardware, and credential claims are deliberately scoped to the exact evidence available.

[Profile](./README.md) · [Technical Resume](./RESUME.md) · [LinkedIn](https://www.linkedin.com/in/taha-zarif-bba94b397/)

## Evidence policy

- Upstream contribution counts include only pull requests merged into repositories **outside** the `tahazarif10` account.
- Self-repository pull requests are project-development evidence, not upstream contribution count.
- Simulation/hosted-CI results are not presented as physical-hardware performance.
- Synthetic computer-vision smoke results are not presented as real-dataset accuracy.
- Pending badges or credentials are not presented as earned until formally issued.

## Applied AI Engineering — current evidence and boundary

The applied-AI portfolio is intentionally split into two independent public tracks:

- **Grounded LLM Platform** — LLM/RAG systems engineering: deterministic BM25 retrieval, bounded ingestion with source/line provenance, typed provider integration, strict structured-output validation, citation allow-listing, fail-closed abstention, prompt/data trust boundaries, FastAPI serving, Docker, and reproducible evaluation contracts.
- **Industrial Vision Inspector** — computer vision / ML engineering: deterministic dataset preparation, PyTorch training/inference, transfer learning, model-card boundaries, classification/error analysis, and calibration-aware evaluation.

The LLM track is **not** derived from or coupled to Local AI Desktop Copilot. Local AI Desktop Copilot remains a separate Windows systems/privacy project documented independently below.

The Grounded LLM Platform currently makes no real-corpus accuracy, hallucination-rate, or production-readiness claim. Those remain gated on its public-corpus benchmark milestone.

## Grounded LLM Platform — Python / FastAPI / RAG

Repository: [grounded-llm-platform](https://github.com/tahazarif10/grounded-llm-platform)

Verified v0.1 engineering foundation:

- deterministic in-memory BM25 retrieval baseline
- bounded document/chunk ingestion with source ID and line provenance
- narrow LLM provider protocol plus OpenAI-compatible HTTP implementation
- strict Pydantic validation of structured model output
- fail-closed abstention when retrieval has no usable evidence
- citation allow-listing against the exact chunks supplied to the provider
- source/line provenance attached from trusted application state rather than model-generated metadata
- retrieved-text trust boundary: evidence is treated as untrusted data, not instructions
- deterministic evaluation harness covering task success, abstention, citation validity, and latency percentiles
- FastAPI index/query adapter
- non-root Docker image
- Ruff, mypy, and pytest verification on Python 3.11 and 3.12

Evidence:

- [foundation PR #1](https://github.com/tahazarif10/grounded-llm-platform/pull/1) — merged
- merge commit `4fe0f609328775a7aefd1408b4cd603ae4335d00`
- [CI run #1](https://github.com/tahazarif10/grounded-llm-platform/actions/runs/35743466716) — Python 3.11 and 3.12 jobs both passed Ruff, mypy, and pytest
- pytest result on Python 3.11: **9 passed**
- [M1 benchmark issue #3](https://github.com/tahazarif10/grounded-llm-platform/issues/3) tracks the first real public-corpus retrieval/grounded-answer benchmark

Scope boundary: v0.1 establishes software/system contracts. It does not establish real-document retrieval quality, factual accuracy, low hallucination rate, prompt-injection resistance, production latency, or Internet-facing production readiness.

## Local AI Desktop Copilot — Windows / .NET / WinUI 3

Repository: [local-ai-desktop-copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)

Verified engineering foundation includes:

- event-driven foreground observation and identity-first privacy evaluation
- explicit Arm/Disarm lifecycle ownership
- RAM-only Windows Graphics Capture and bounded latest-wins sensing
- capability-based privacy, epoch invalidation, and stale-result rejection
- dedicated COM MTA UI Automation worker
- bounded non-text structural snapshots and separately authorized semantic snapshots
- bounded M3.4 orchestration admission with debounce, deduplication, priority, and one-active/one-pending limits
- controlled provider-isolation measurement and recovery evidence on physical Windows

Provider-isolation evidence:

- [M3.4 provider-isolation PR #23](https://github.com/tahazarif10/local-ai-desktop-copilot/pull/23) — merged
- behavior-bearing head `44d4752864372116a911de2ae3acf611ef033c1e`
- [CI #87](https://github.com/tahazarif10/local-ai-desktop-copilot/actions/runs/34899915173) — portable/Windows Core tests, PowerShell validation, controlled raw-provider cross-process smoke gate, and strict Windows build passed
- physical measurement observed real provider entry, recovery on the existing worker before the 10-second request deadline, bounded shutdown, `joined=True`, and a clean randomized prohibited-content sentinel scan
- ADR 0011 selected the existing in-process MTA UIA worker for the measured failure mode

Scope boundary: this is still an engineering foundation rather than a complete AI assistant. OCR, model inference, voice, autonomous actions, elevation/`uiAccess`, and implicit cloud egress are not claimed as implemented capabilities.

## Robotics Control Core — C++20

Repository: [robotics-control-core](https://github.com/tahazarif10/robotics-control-core)

Implemented and verified:

- occupancy-grid A*
- obstacle inflation and collision-safe path shaping
- PID and interpolated-lookahead pure pursuit
- differential-drive forward/inverse kinematics
- SE(2) odometry
- installable CMake package `robotics::control`
- independent `find_package` consumer verification
- GCC / Clang / MSVC CI
- ASan / UBSan and CodeQL

### Deterministic v0.2 fixture

| Controller | Waypoints | Steps | Travel | Max cross-track | Final error | Collision-free |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| PID baseline | 26 | 545 | 7.158981 m | 0.063708 m | 0.099468 m | yes |
| Pure pursuit + smoothed path | 5 | 479 | 6.905655 m | 0.052827 m | 0.097605 m | yes |

Evidence:

- [v0.2 PR #7](https://github.com/tahazarif10/robotics-control-core/pull/7)
- [multi-compiler CI](https://github.com/tahazarif10/robotics-control-core/actions/runs/34357410837)
- [CodeQL](https://github.com/tahazarif10/robotics-control-core/actions/runs/34357411019)
- [verification record](https://github.com/tahazarif10/robotics-control-core/blob/main/docs/VERIFICATION.md)

These numbers are deterministic regression-fixture results, not universal controller or hardware-performance claims.

## ROS 2 Autonomous Mobile Robot

Repository: [ros2-autonomous-mobile-robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

Verified software/system-integration capabilities:

- C++20 ROS 2 lifecycle control adapter consuming `robotics-control-core` at a pinned commit
- bounded `cmd_vel` and safe-stop behavior for missing, stale, and non-finite inputs
- ROS 2 Jazzy / Ubuntu 24.04 Nav2 fixture with explicit TF/QoS contracts
- deterministic static-map obstacle-detour integration test
- lifecycle diagnostics and stable stop reasons
- NaN/stale-input fault injection
- real rosbag2 sqlite3 generation and deterministic replay through the live lifecycle adapter
- missing-global-TF fail-closed verification with no non-zero `cmd_vel`
- ROS graph isolation fix after diagnosing cross-test contamination in hosted CI

Evidence:

- [lifecycle adapter PR #6](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/6)
- [Nav2 fixture PR #8](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/8)
- [TF/QoS PR #9](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/9)
- [diagnostics/fault injection PR #10](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/10)
- [rosbag replay PR #11](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/11)
- [missing-TF + metrics PR #12](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/12)
- [test-graph isolation PR #13](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/13)
- [final v0.4 merged-main CI](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34395404807)
- [verification record](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/blob/main/docs/VERIFICATION.md)

These are deterministic software/system-integration results, not physical safety certification or real-robot performance claims.

## Embedded RTOS Sensor Hub — C / Zephyr

Repository: [embedded-rtos-sensor-hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)

Baseline: Zephyr **v4.4.2**, Ubuntu 24.04 hosted CI, `native_sim/native`, ztest/Twister.

Verified capabilities:

- five statically defined threads
- bounded `k_msgq` producer/consumer pipeline
- `k_sem` startup synchronization and `k_mutex` protected metrics
- fixed-size messages with no application data-path heap allocation
- software heartbeat supervision
- queue drop/high-watermark accounting and deterministic producer-stall injection
- abstract bus-read boundary used by producer threads
- simulated I2C-style temperature and SPI-style vibration transactions
- bounded retry policy and deterministic transient bus-fault injection
- sequence-gap and timestamp-regression rejection/recovery
- normal, producer-stall, and bus-fault hosted builds
- **12/12 Twister test cases passed** on merged `main`

Evidence:

- [v0.1 PR #1](https://github.com/tahazarif10/embedded-rtos-sensor-hub/pull/1)
- [v0.2 PR #3](https://github.com/tahazarif10/embedded-rtos-sensor-hub/pull/3)
- [merged-main CI](https://github.com/tahazarif10/embedded-rtos-sensor-hub/actions/runs/34493673687)
- [verification record](https://github.com/tahazarif10/embedded-rtos-sensor-hub/blob/main/docs/VERIFICATION.md)

This is native-simulation software evidence. It does not establish physical I2C/SPI timing, electrical behavior, sensor accuracy, ISR latency, hardware-watchdog behavior, or safety certification.

## Industrial Vision Inspector — Python / OpenCV / PyTorch

Repository: [industrial-vision-inspector](https://github.com/tahazarif10/industrial-vision-inspector)

Implemented portfolio pipeline:

- classical image-quality metrics and deterministic preprocessing
- reproducible NEU-CLS preparation path with SHA-256 manifests
- TinyCNN and ResNet-18 model paths
- train/evaluate/infer CLI
- accuracy, top-2 accuracy, macro precision/recall/F1, confusion matrix, training history, and annotated inference output\n- probability-quality evaluation with mean confidence, negative log-likelihood, multiclass Brier score, expected calibration error (ECE), calibration bins, and reliability diagrams
- deterministic synthetic generator used for unit/smoke verification

The calibration-aware evaluation path was merged in [PR #4](https://github.com/tahazarif10/industrial-vision-inspector/pull/4); [CI #17](https://github.com/tahazarif10/industrial-vision-inspector/actions/runs/35741143007) passed the repository test/smoke workflow on the PR head.\n\nThe checked synthetic smoke result is intentionally **not** represented as real NEU-CLS or manufacturing performance. Real held-out dataset benchmarking remains a separate evidence gate.

## Upstream Open-Source Contributions

**11 merged upstream pull requests across 7 external repositories, verified as of 2026-09-17.**

### Zephyr RTOS — 2 merged PRs

1. **[PR #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971) — Bluetooth: Host: add native_sim identity API tests**  
   Added `native_sim` coverage for public Bluetooth identity-management APIs using `bt_enable()` and `bt_id_create()`, `bt_id_reset()`, `bt_id_delete()`, and `bt_id_get()` through the real Bluetooth host with a fake HCI driver rather than host-internal mocks.

2. **[PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636) — Bluetooth: HCI: clarify pairing error scope**  
   Clarified that HCI status `0x29` (`Pairing with Unit Key Not Supported`) is valid for BR/EDR connections only and aligned public disconnect/test-helper documentation with that scope.

**Recognition status:** an application for the **Zephyr Technical Contributor** badge has been submitted. Review is pending; the badge is not claimed as earned until formally issued.

### Robotics Toolbox for Python — 2 merged PRs

3. **[PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)** — fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before a potentially singular solver update; updated solver residual handling and added regression coverage.

4. **[PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644)** — restored the missing `[-1, 1]` distance-transform neighbor and added a regression for the unique shortest diagonal step.

### Motrix — 2 merged PRs

5. **[PR #2138](https://github.com/agalwood/Motrix/pull/2138)** — restored the macOS Menu Bar Only Dock-state invariant after main-window dismissal and added focused regression coverage. Fork CI covered macOS, Windows, and Linux.

6. **[PR #1885](https://github.com/agalwood/Motrix/pull/1885)** — restored Windows tray left-click main-window toggling while preserving right-click and non-Windows menu behavior; regression coverage was strengthened in response to maintainer review.

### DQ QuestionBank Core — 2 merged PRs

7. **[PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127)** — added collection-scoped editor draft autosave/crash recovery, dirty-state unload protection, restore/discard flow, and focused regression coverage.

8. **[PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128)** — fixed a round-trip data-preservation bug so ragged rows and trailing empty rows retain their canonical table shape; added DOM-level regression coverage.

### Apache NuttX — 1 merged PR

9. **[PR #20147](https://github.com/apache/nuttx/pull/20147)** — documented Python linting/formatting requirements (`black`, `isort`, `flake8`), `checkpatch.sh` verification/auto-format paths, and the existing pre-commit workflow; merged after maintainer approvals.

### Orchestrator MCP — 1 merged PR

10. **[PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11)** — fixed delegated synthesis so machine-readable review outcomes are provided from review storage while reviewer prose/usage is omitted; added end-to-end regression coverage.

### GPS-Denied UAV Navigation — 1 merged PR

11. **[PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28)** — carried TDOA validity through confidence-floor and recovery/fusion paths so non-finite position/confidence data remains fail-closed; added focused regressions.

## Industrial Automation Experience

Public profile summary:

- Python/PyQt control software with Delta AS228T-series PLC over Modbus TCP
- pulse/direction servo motion for CNC saw/clamp axes
- millimetre-to-pulse conversion
- homing and jog logic
- busy/done state handling
- limits, alarms, readiness, and safety interlocks
- physical PLC/I/O, sensor, servo, and machine-behavior debugging

These are experience statements, not public hardware-performance benchmarks.

## Robotics Competition Experience — FIRA

### FIRA RoboWorld Cup 2024 — Brazil

- Event: **FIRA RoboWorld Cup 2024**
- Location: **São Luís, Maranhão, Brazil**
- Dates: **5–9 August 2024**
- Participant: **Taha Zarif**
- Team: **Kamaan Shahriar Iran**
- League: **Cliff Hanger Lightweight (U14)**
- Team result: **4th place**

Public evidence:

- [Official AVIS FIRA 2024 team roster](https://events.avisengine.com/events/fira-2024/teams) lists **Kamaan Shahriar Iran** under Cliff Hanger Lightweight (U14) and **Taha Zarif** as a Youth Member.
- [Pooria Noori — public LinkedIn profile](https://ir.linkedin.com/in/pooria-noori-782869280) publicly lists 4th place in FIRA RoboWorld Cup 2024 Brazil as coach in the Cliff Hanger league.
- A physical FIRA RoboWorld Cup 2024 participant badge retained by Taha shows Taha Zarif, Kamaan Shahriar Iran, São Luís, Brazil, and the event dates.

The current AVIS historical awards endpoint does not expose the placement, so the roster confirms participation/team/league while the 4th-place result is corroborated separately by the coach's public record.

### FIRA Iran

- **Iran 2026 FIRA Open Competition** — Kamaan · Air Autonomous Race (U19) · Tehran · 17–21 July 2026.
- **Iran 2025 FIRA Open Competition** — Kamaan 3 · Cliff Hanger Lightweight (U19) · Tehran · 15–18 April 2025.
- A **3rd-place national FIRA Iran finish** is retained from participant-provided competition records; the exact public award-page mapping has not yet been identified, so it is not attached here to a specific year/league.

## Training / Credential Evidence

Linux Foundation Training course completions, September 2026:

- **Open Source RT-Thread RTOS on RISC-V (LFD123)** — Certificate ID `LF-o5csrgydp9`
- **Getting Started with Rust (LFEL1002)** — Certificate ID `LF-f1vb0tcc5k`
- **A Beginner's Guide to Open Source Software Development (LFD102)** — Certificate ID `LF-x7xjzo6yvn`

The Zephyr Technical Contributor badge application is tracked separately above because it is still pending review.
