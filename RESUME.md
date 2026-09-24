# Taha Zarif

## Systems, Robotics & AI Software Engineer

**Mashhad, Iran**  
**GitHub:** [github.com/tahazarif10](https://github.com/tahazarif10) · **LinkedIn:** [linkedin.com/in/taha-zarif-bba94b397](https://www.linkedin.com/in/taha-zarif-bba94b397/) · **Evidence:** [EVIDENCE.md](./EVIDENCE.md)

### Profile

Systems, robotics, and applied-AI developer building deterministic, testable software across **C/C++, Python, ROS 2, Zephyr RTOS, LLM/RAG systems, PyTorch/OpenCV, and industrial automation**. Public engineering work includes **11 merged upstream pull requests across 7 external repositories**, including **Zephyr RTOS, Apache NuttX, Robotics Toolbox for Python, and Motrix**. Engineering emphasis: explicit failure handling, bounded resources, reproducible evaluation, CI, fault injection, sanitizers/static analysis, and hardware/software debugging.

### Selected Engineering Projects

- **[Grounded LLM Platform](https://github.com/tahazarif10/grounded-llm-platform)** — Python/FastAPI RAG platform with deterministic BM25 retrieval, bounded ingestion with source/line provenance, typed OpenAI-compatible provider integration, strict structured-output validation, citation allow-listing, fail-closed abstention, prompt/data trust boundaries, Docker, and Python 3.11/3.12 CI. Added a reproducible external-corpus retrieval benchmark pinned to exact Zephyr documentation inputs with SHA-256 verification and machine-readable reports. On the current 12-case **development benchmark**, Recall@5, MRR, nDCG@5, and negative zero-hit rate are all **1.0** and enforced as regression gates; this is explicitly not presented as general RAG-quality evidence.
- **[Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)** — C++20 differential-drive planning/control library with occupancy-grid A*, obstacle inflation, collision-safe path shaping, PID, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry. Verified with GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, deterministic benchmarks, installable CMake packaging, and an independent `find_package` consumer.
- **[ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)** — ROS 2 Jazzy/Nav2 AMR stack with lifecycle control, explicit TF/QoS contracts, deterministic rosbag2 replay, diagnostics, fault injection, and fail-closed zero-command behavior for stale/non-finite inputs and missing global TF.
- **[Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)** — C/Zephyr RTOS sensor hub with static threads, bounded `k_msgq` pipelines, synchronization, software heartbeat supervision, bounded retries, sequence/timestamp integrity checks, and deterministic fault injection; **12/12 Twister cases pass** on `native_sim`.
- **[Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector)** — Python/OpenCV/PyTorch defect-classification pipeline with deterministic dataset preparation, SHA-256 manifests, TinyCNN/ResNet-18 model paths, checkpointed inference, confusion-matrix/per-class evaluation, and calibration-aware metrics including NLL, multiclass Brier score, ECE, and reliability diagrams.
- **[Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)** — privacy-first Windows/.NET systems foundation with RAM-only sensing, identity-first privacy gates, capability-gated UI Automation, bounded orchestration, stale-result rejection, and measured provider-isolation recovery.

### Open-Source Engineering

**11 merged upstream PRs across 7 external repositories.** Selected:

- **Zephyr RTOS — [PR #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971):** added `native_sim` tests for public Bluetooth identity APIs through the real host path with a fake HCI driver; expanded boundary coverage in response to maintainer review before merge.
- **Robotics Toolbox for Python — [PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667):** fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before a potentially singular solver update; added regression coverage.
- **GPS-Denied UAV Navigation — [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28):** preserved fail-closed localization behavior so invalid/non-finite TDOA data cannot raise confidence or claim a recovery/fusion source.
- **Motrix — [PR #2138](https://github.com/agalwood/Motrix/pull/2138):** restored the macOS Menu Bar Only Dock-state invariant after main-window dismissal with focused regression coverage.
- **Apache NuttX — [PR #20147](https://github.com/apache/nuttx/pull/20147):** documented the Python lint/format contributor workflow and merged after maintainer review.

Additional merged work includes **Zephyr #118636, Robotics Toolbox #644, Motrix #1885, DQ QuestionBank #127/#128, and Orchestrator MCP #11**. Full evidence: [EVIDENCE.md](./EVIDENCE.md#upstream-open-source-contributions).

### Technical Skills

**Languages:** C, C++20, Python, C#/.NET, JavaScript/TypeScript  
**Robotics:** ROS 2 Jazzy, Nav2, TF2, lifecycle nodes, rosbag2, differential-drive navigation, fault handling  
**Embedded / RTOS:** Zephyr RTOS, ztest/Twister, threads, `k_msgq`, mutexes, semaphores, bounded retry/recovery  
**AI / LLM Engineering:** RAG, BM25, grounded generation, structured outputs, citation validation, abstention, FastAPI, Pydantic, HTTPX, OpenAI-compatible APIs, reproducible evaluation  
**AI / Computer Vision:** OpenCV, PyTorch, CNNs, ResNet-18, transfer learning, dataset manifests, classification/error analysis, NLL/Brier/ECE calibration  
**Verification / Tooling:** Linux, Git, CMake, CTest, GitHub Actions, Docker, CodeQL, ASan/UBSan, deterministic replay, fault injection  
**Industrial Automation:** Delta AS PLCs, Modbus TCP, pulse/direction servo motion, homing/jog/state logic, limits, alarms, interlocks, CNC automation

### Hands-On Automation

Built and debugged Python/PyQt machine-control logic with **Delta AS228T-series PLCs over Modbus TCP**, including mm-to-pulse conversion, pulse/direction servo positioning, homing, jog, state handling, limits, alarms, readiness, safety interlocks, and physical PLC/I/O troubleshooting.

### Education, Competition & Training

- **Secondary School — Grade 10, Mathematics Track** · Mashhad, Iran
- **4th place — FIRA RoboWorld Cup 2024**, São Luís, Brazil · Kamaan Shahriar Iran · Cliff Hanger Lightweight (U14)
- Linux Foundation course completions (Sep 2026): **Open Source RT-Thread RTOS on RISC-V (LFD123)**, **Getting Started with Rust (LFEL1002)**, **A Beginner's Guide to Open Source Software Development (LFD102)**

---

*Public version intentionally excludes private contact details. Performance, safety, hardware, and credential claims are evidence-scoped; claim-level sources are maintained in [EVIDENCE.md](./EVIDENCE.md).*
