# Taha Zarif

## Robotics, Embedded Software & Computer Vision

**Mashhad, Iran**  
**GitHub:** [github.com/tahazarif10](https://github.com/tahazarif10) · **LinkedIn:** [linkedin.com/in/taha-zarif-bba94b397](https://www.linkedin.com/in/taha-zarif-bba94b397/) · **Evidence:** [EVIDENCE.md](./EVIDENCE.md)

### Profile

Grade 10 student focused on robotics, embedded software, computer vision, and industrial automation. Builds testable C/C++ and Python systems with deterministic regression evidence, bounded-resource design, CI, fault injection, and hardware/software debugging. Public work includes **6 merged upstream pull requests**, ROS 2/Zephyr projects, a Python/OpenCV/PyTorch industrial-vision pipeline, and hands-on PLC/servo/CNC integration.

### Education

**Secondary School — Grade 10** · Mashhad, Iran

### Selected Engineering Projects

- **[Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector)** — Python/OpenCV/PyTorch surface-defect classification pipeline with classical image-quality metrics, CLAHE/denoise preprocessing, deterministic NEU-CLS data preparation with SHA-256 manifests, TinyCNN and ResNet-18 model paths, standard classification metrics, checkpointed inference, and annotated prediction output. **7/7 local tests passed**; synthetic smoke results are explicitly separated from real-dataset performance claims.
- **[Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)** — C++20 differential-drive navigation/control library with occupancy-grid A*, obstacle inflation, collision-safe smoothing, PID, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry. GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, CMake packaging, deterministic benchmarks.
- **[ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)** — ROS 2 Jazzy / Ubuntu 24.04 AMR stack with lifecycle control, Nav2, TF/QoS contracts, diagnostics, fault injection, rosbag2 replay, missing-TF fail-closed verification, and isolated integration tests.
- **[Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)** — C / Zephyr RTOS 4.4.2 sensor hub using static threads, bounded `k_msgq`, semaphores/mutexes, heartbeat supervision, bounded retries, sequence/timestamp checks, deterministic fault injection, and **12/12 ztest/Twister** cases on `native_sim`.

### Industrial Automation & CNC

- Developed Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP.
- Implemented and debugged pulse/direction servo motion for CNC saw and clamp axes, including mm-to-pulse conversion, homing, jog, busy/done states, limits, alarms, readiness, and safety interlocks.

### Open-Source Contributions

**6 merged upstream PRs** across robotics, desktop software, frontend, orchestration, and localization projects.

- **Robotics Toolbox for Python — [PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644):** restored a missing distance-transform diagonal and added regression coverage.
- **Motrix — [PR #1885](https://github.com/agalwood/Motrix/pull/1885):** restored tray left-click window toggling and strengthened cross-platform tests after maintainer review.
- **GPS-Denied UAV Navigation — [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28):** preserved fail-closed behavior for invalid/non-finite TDOA localization data.
- Additional merged work: DQ QuestionBank Core [#127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) / [#128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128), Orchestrator MCP [#11](https://github.com/crAK1644/orchestrator-mcp/pull/11).

**Under upstream review — not counted as merged:** Zephyr RTOS [#118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636) and Robotics Toolbox for Python [#667](https://github.com/petercorke/robotics-toolbox-python/pull/667).

### Robotics Competition Experience

- **4th place — FIRA RoboWorld Cup 2024, São Luís, Brazil** · Kamaan Shahriar Iran · Cliff Hanger Lightweight (U14). See [competition evidence](./EVIDENCE.md#fira-roboworld-cup-2024--brazil).
- **Iran 2026 FIRA Open Competition** · Kamaan · Air Autonomous Race (U19).
- **Iran 2025 FIRA Open Competition** · Kamaan 3 · Cliff Hanger Lightweight (U19).
- **3rd-place national FIRA Iran finish** — participant-provided result; exact public award-page mapping is still being identified.

### Training & Credentials

Linux Foundation Training course completions, September 2026:

- **Open Source RT-Thread RTOS on RISC-V (LFD123)** — Certificate ID `LF-o5csrgydp9`
- **Getting Started with Rust (LFEL1002)** — Certificate ID `LF-f1vb0tcc5k`
- **A Beginner's Guide to Open Source Software Development (LFD102)** — Certificate ID `LF-x7xjzo6yvn`

### Technical Skills

**Languages:** C, C++20, Python, C#  
**AI / Computer Vision:** OpenCV, PyTorch, CNNs, ResNet-18, image preprocessing, transfer-learning workflow, classification, accuracy/precision/recall/F1 evaluation  
**Robotics:** ROS 2 Jazzy, Nav2, TF2, lifecycle nodes, rosbag2, differential-drive navigation  
**Embedded / RTOS:** Zephyr RTOS, ztest/Twister, `k_msgq`, threads, mutexes, semaphores, bounded retries, fault injection  
**Systems:** Linux, Git, CMake, GitHub Actions, Docker, CodeQL, ASan/UBSan  
**Industrial:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation

---

*Public version intentionally excludes private contact details. Claim-level sources and scope are maintained in [EVIDENCE.md](./EVIDENCE.md).*
