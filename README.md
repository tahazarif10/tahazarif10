# Taha Zarif

## Robotics & Embedded Software

I build software for robotics, embedded systems, real-time applications, and industrial automation, with a focus on deterministic behavior, reliability, testing, fault handling, and hardware/software debugging.

[**Technical Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [**GitHub Projects**](https://github.com/tahazarif10?tab=repositories)

### Core Focus

- Robotics & autonomous systems
- Embedded / real-time software
- C / C++ systems programming
- ROS 2 / Nav2
- Zephyr RTOS
- Industrial automation, PLCs, servo motion, and CNC control
- Deterministic testing, CI, fault injection, and root-cause analysis

### Featured Engineering Work

#### [Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)
Middleware-independent **C++20** navigation/control library for differential-drive robots with occupancy-grid A*, obstacle inflation, collision-safe path smoothing, PID, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry.

**Evidence:** installable CMake package, GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, deterministic regression fixtures, package-consumer verification, and benchmark documentation.

#### [ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)
Reproducible **ROS 2 Jazzy / Ubuntu 24.04** AMR stack with lifecycle control, Nav2 integration, diagnostics, fault injection, rosbag2 replay, TF/QoS verification, fail-closed behavior, and isolated integration tests.

#### [Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)
**C / Zephyr RTOS 4.4.2** sensor-hub project using statically defined threads, bounded queues, synchronization primitives, software heartbeat supervision, bus retry policies, deterministic fault injection, and **12/12 ztest/Twister tests** on `native_sim`.

#### [Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)
Privacy-first Windows desktop software project focused on bounded context sensing, deterministic behavior, explicit privacy constraints, reproducible testing, and system architecture.

### Open-Source Contributions

I contribute focused fixes and regression tests to existing projects, with an emphasis on reproducible defects and reviewable changes.

**Merged upstream:**

- [Robotics Toolbox for Python — PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644) — restored a missing distance-transform diagonal and added regression coverage.
- [Motrix — PR #1885](https://github.com/agalwood/Motrix/pull/1885) — restored tray left-click window toggling and strengthened cross-platform tests after maintainer review.
- [DQ QuestionBank Core — PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) — editor draft autosave and crash recovery.
- [DQ QuestionBank Core — PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128) — preserved table-row shape in the editor.
- [Orchestrator MCP — PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11) — fixed delegated review-synthesis input.
- [GPS-Denied UAV Navigation — PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28) — preserved fail-closed handling for invalid TDOA localization data.

**Currently under upstream review:**

- [Zephyr RTOS — PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636)
- [Robotics Toolbox for Python — PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)

These are not counted as merged achievements until upstream merges them.

### Industrial Engineering Work

Hands-on CNC and industrial automation work includes:

- Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP
- Servo-axis motion for saw and clamp mechanisms
- Millimetre-to-pulse conversion, homing, jog, busy/done state logic, limits, alarms, and readiness/safety interlocks
- PLC I/O, pulse/direction motion, and physical machine debugging

### Robotics Competition Experience

- **FIRA RoboWorld Cup 2024 — São Luís, Maranhão, Brazil (5–9 August 2024)** — competed with **Kamaan Shahriar Iran** in **Cliff Hanger Lightweight (U14)**; team result: **4th place**.
- **FIRA Iran** — national-level **3rd-place finish**.
- **Iran 2026 FIRA Open Competition** — **Kamaan**, **Air Autonomous Race (U19)**.
- **Iran 2025 FIRA Open Competition** — **Kamaan 3**, **Cliff Hanger Lightweight (U19)**.

Competition details and evidence links are maintained in [EVIDENCE.md](./EVIDENCE.md).

### Tech

**Languages:** C, C++, Python, C#  
**Robotics:** ROS 2, Nav2, TF2, rosbag2, differential-drive navigation  
**Embedded:** Zephyr RTOS, ztest/Twister, bounded queues, fault injection, simulated I2C/SPI contracts  
**Systems:** Linux, Git, CMake, GitHub Actions, Docker, CodeQL, ASan/UBSan  
**Industrial:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation

### Current Direction

Embedded telemetry transport · backpressure/recovery · physical sensor/bus qualification · hardware watchdogs · autonomous navigation/control · upstream robotics/embedded contributions

---

For claim-level reproducibility, CI links, competition records, and benchmark scope, see [**Engineering Evidence**](./EVIDENCE.md).
