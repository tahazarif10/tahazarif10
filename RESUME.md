# Taha Zarif

## Systems, Robotics & Applied AI Software

**Mashhad, Iran**  
**GitHub:** [github.com/tahazarif10](https://github.com/tahazarif10) · **LinkedIn:** [linkedin.com/in/taha-zarif-bba94b397](https://www.linkedin.com/in/taha-zarif-bba94b397/) · **Evidence:** [EVIDENCE.md](./EVIDENCE.md)

### Profile

Systems, robotics, and applied-AI developer focused on **C/C++, Python, ROS 2, Zephyr RTOS, PyTorch/OpenCV, privacy-aware Windows systems, and verification-driven engineering**. Builds deterministic, testable software with bounded-resource design, explicit failure handling, CI, fault injection, reproducible ML/data pipelines, model evaluation, and hardware/software debugging. Public work includes **11 merged upstream pull requests across 7 external repositories**, including two contributions to **Zephyr RTOS** plus merged work in **Apache NuttX, Robotics Toolbox for Python, Motrix**, and safety-oriented robotics/localization projects.

### Selected Engineering Projects

- **[Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)** — C++20 differential-drive navigation/control library with occupancy-grid A*, obstacle inflation, collision-safe path shaping, PID, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry. Verified with GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, installable CMake packaging, and deterministic benchmarks.
- **[Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)** — privacy-first Windows/.NET systems foundation with explicit Arm/Disarm lifecycle ownership, identity-first privacy gates, RAM-only Windows Graphics Capture, capability-gated UI Automation, bounded semantic snapshots/orchestration, provider-isolation measurement, and deterministic recovery verification. OCR, model inference, voice, and autonomous actions remain outside the accepted implementation boundary.
- **[ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)** — ROS 2 Jazzy / Ubuntu 24.04 AMR stack with lifecycle control, Nav2, TF/QoS contracts, deterministic rosbag2 replay, diagnostics, fault injection, missing-TF fail-closed verification, and isolated integration tests.
- **[Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)** — C / Zephyr RTOS 4.4.2 sensor hub using static threads, bounded `k_msgq`, semaphores/mutexes, heartbeat supervision, bounded retries, sequence/timestamp integrity checks, deterministic fault injection, and **12/12 ztest/Twister** cases on `native_sim`.
- **[Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector)** — Python/OpenCV/PyTorch surface-defect inspection pipeline with classical image-quality metrics, reproducible dataset preparation with SHA-256 manifests, TinyCNN/ResNet-18 model paths, standard classification metrics, checkpointed inference, and explicit separation of synthetic smoke evidence from real-data performance claims.

### Applied AI Engineering\n\n- **Computer vision / ML:** end-to-end PyTorch classification workflow with deterministic dataset preparation, transfer-learning path, model checkpointing, held-out evaluation tooling, confusion matrices, per-class metrics, and explicit model-card/evidence boundaries.\n- **Local AI systems:** privacy-first desktop sensing and semantic-context foundation with capability gates, epoch-bound stale-result rejection, bounded orchestration, provider-isolation measurement, and a defined next milestone for real local-model inference, typed structured outputs, and reproducible evals.\n- **Engineering standard:** synthetic/smoke results are kept separate from real-dataset or hardware performance claims; model/runtime quality is not promoted into the resume until measured evidence exists.\n\n### Open-Source Contributions

**11 merged upstream PRs across 7 external repositories.** Selected contributions:

- **Zephyr RTOS — [PR #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971):** added `native_sim` tests for public Bluetooth identity-management APIs (`bt_id_create/reset/delete/get`) through the real host path with a fake HCI driver rather than host-internal mocks.
- **Robotics Toolbox for Python — [PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667):** fixed numerical IK convergence ordering so an exact/already-converged initial configuration is accepted before a potentially singular solver update; added regression coverage.
- **Motrix — [PR #2138](https://github.com/agalwood/Motrix/pull/2138):** restored the macOS Menu Bar Only Dock-state invariant after main-window dismissal and added focused regression coverage; fork CI covered macOS, Windows, and Linux.
- **GPS-Denied UAV Navigation — [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28):** kept invalid/non-finite TDOA data fail-closed so it cannot raise localization confidence or claim a recovery/fusion source.
- **DQ QuestionBank Core — [PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) / [#128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128):** added draft autosave/crash recovery and fixed table round-trip preservation for ragged/trailing-empty rows.
- **Apache NuttX — [PR #20147](https://github.com/apache/nuttx/pull/20147):** documented the Python `black` / `isort` / `flake8` and `checkpatch.sh` contributor workflow; merged after maintainer approvals.

Additional merged work includes **Zephyr #118636**, **Robotics Toolbox #644**, **Motrix #1885**, and **Orchestrator MCP #11**. The complete contribution ledger is in [EVIDENCE.md](./EVIDENCE.md#upstream-open-source-contributions).

### Industrial Automation & CNC

- Developed Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP.
- Implemented and debugged pulse/direction servo motion for CNC saw and clamp axes, including mm-to-pulse conversion, homing, jog, busy/done states, limits, alarms, readiness, and safety interlocks.
- Performed physical PLC/I/O, sensor, servo, and machine-behavior debugging on CNC equipment.

### Robotics Competition Experience

- **4th place — FIRA RoboWorld Cup 2024, São Luís, Brazil** · Kamaan Shahriar Iran · Cliff Hanger Lightweight (U14). See [competition evidence](./EVIDENCE.md#robotics-competition-experience--fira).
- **Iran 2026 FIRA Open Competition** · Kamaan · Air Autonomous Race (U19).
- **Iran 2025 FIRA Open Competition** · Kamaan 3 · Cliff Hanger Lightweight (U19).
- **3rd-place national FIRA Iran finish** — participant-provided result; exact public award-page mapping is still being identified.

### Training & Credentials

Linux Foundation Training course completions, September 2026:

- **Open Source RT-Thread RTOS on RISC-V (LFD123)** — Certificate ID `LF-o5csrgydp9`
- **Getting Started with Rust (LFEL1002)** — Certificate ID `LF-f1vb0tcc5k`
- **A Beginner's Guide to Open Source Software Development (LFD102)** — Certificate ID `LF-x7xjzo6yvn`

A **Zephyr Technical Contributor** badge application has been submitted based on merged Zephyr contributions; it is pending review and is not listed as an earned credential yet.

### Technical Skills

**Languages:** C, C++20, Python, C#/.NET, JavaScript/TypeScript  
**Robotics:** ROS 2 Jazzy, Nav2, TF2, lifecycle nodes, rosbag2, differential-drive navigation, localization/fault handling  
**Embedded / RTOS:** Zephyr RTOS, ztest/Twister, `k_msgq`, threads, mutexes, semaphores, bounded retries, fault injection  
**Windows / Systems:** WinUI 3, Windows Graphics Capture, UI Automation, bounded concurrency/lifecycle design  
**AI / Computer Vision:** OpenCV, PyTorch, CNNs, ResNet-18, image preprocessing, transfer learning, train/evaluate/infer pipelines, model cards, reproducible dataset manifests, classification/error analysis  
**Tooling:** Linux, Git, CMake, GitHub Actions, Docker, CodeQL, ASan/UBSan  
**Industrial:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation

### Education

**Secondary School — Grade 10** · Mashhad, Iran

---

*Public version intentionally excludes private contact details. Performance, safety, hardware, and credential claims are evidence-scoped; claim-level sources are maintained in [EVIDENCE.md](./EVIDENCE.md).*
