<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Robotics & Embedded Software" width="100%">
</p>

# Taha Zarif

### Robotics, Embedded Software & Computer Vision

Grade 10 student building software for **robotics, embedded systems, computer vision, real-time applications, and industrial automation**, with a focus on deterministic behavior, reliability, testing, fault handling, and hardware/software debugging.

[**Recruiter Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [**Repositories**](https://github.com/tahazarif10?tab=repositories)

## Open-Source Contributions

**6 merged upstream pull requests** across robotics, desktop software, frontend, orchestration, and localization projects.

- [**Robotics Toolbox for Python — PR #644**](https://github.com/petercorke/robotics-toolbox-python/pull/644) — restored a missing distance-transform diagonal and added regression coverage.
- [**Motrix — PR #1885**](https://github.com/agalwood/Motrix/pull/1885) — restored tray left-click window toggling and strengthened cross-platform tests after maintainer review.
- [**DQ QuestionBank Core — PR #127**](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) — editor draft autosave and crash recovery.
- [**DQ QuestionBank Core — PR #128**](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128) — preserved table-row shape in the editor.
- [**Orchestrator MCP — PR #11**](https://github.com/crAK1644/orchestrator-mcp/pull/11) — fixed delegated review-synthesis input.
- [**GPS-Denied UAV Navigation — PR #28**](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28) — preserved fail-closed handling for invalid TDOA localization data.

**Currently under upstream review — not counted as merged:**

- [Zephyr RTOS — PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636)
- [Robotics Toolbox for Python — PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)

## Selected Engineering Projects

| Project | Engineering focus | Public evidence |
| --- | --- | --- |
| [**Industrial Vision Inspector**](https://github.com/tahazarif10/industrial-vision-inspector) | Python · OpenCV · PyTorch · CNN / ResNet-18 · deterministic NEU-CLS preparation · image-quality metrics | **7/7 local tests** · deterministic synthetic smoke verification · evidence-scoped model card |
| [**Robotics Control Core**](https://github.com/tahazarif10/robotics-control-core) | C++20 · A* · path smoothing · PID · pure pursuit · kinematics · SE(2) odometry | Multi-compiler CI · ASan/UBSan · CodeQL · deterministic benchmarks |
| [**ROS 2 Autonomous Mobile Robot**](https://github.com/tahazarif10/ros2-autonomous-mobile-robot) | ROS 2 Jazzy · Nav2 · lifecycle control · TF/QoS · rosbag2 replay · fault injection | `colcon` CI · fail-closed tests · replay equality · integration-test isolation |
| [**Embedded RTOS Sensor Hub**](https://github.com/tahazarif10/embedded-rtos-sensor-hub) | C · Zephyr RTOS 4.4.2 · bounded queues · supervision · bus retries · fault injection | `native_sim` · **12/12 ztest/Twister** · hosted CI |
| [**Local AI Desktop Copilot**](https://github.com/tahazarif10/local-ai-desktop-copilot) | C#/.NET · WinUI · bounded context sensing · privacy gates · deterministic system design | Automated CI · explicit acceptance gates · architecture/privacy documentation |

For exact benchmark scope, CI runs, and verification links, see [**Engineering Evidence**](./EVIDENCE.md).

## Industrial Engineering Work

Hands-on CNC and industrial automation work includes:

- Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP
- Servo-axis motion for saw and clamp mechanisms
- Millimetre-to-pulse conversion, homing, jog, busy/done state logic, limits, alarms, and readiness/safety interlocks
- PLC I/O, pulse/direction motion, and physical machine debugging

## Robotics Competition Experience

- **4th place — FIRA RoboWorld Cup 2024**, São Luís, Maranhão, Brazil — **Kamaan Shahriar Iran**, **Cliff Hanger Lightweight (U14)**. [Official AVIS roster](https://events.avisengine.com/events/fira-2024/teams) lists **Taha Zarif** as a Youth Member of the team.
- **3rd-place national finish — FIRA Iran robotics competition** — exact public award-page mapping still being identified.
- **Iran 2026 FIRA Open Competition** — **Kamaan**, **Air Autonomous Race (U19)**. [Team record](https://events.avisengine.com/dashboard/teams/787559c0-d862-45a4-987f-343b13a0690f)
- **Iran 2025 FIRA Open Competition** — **Kamaan 3**, **Cliff Hanger Lightweight (U19)**. [Team record](https://events.avisengine.com/dashboard/teams/dcdcb284-d966-4060-9ae5-48a20081cb94)

Competition sources and evidence notes are maintained in [EVIDENCE.md](./EVIDENCE.md#robotics-competition-experience--fira).

## Training

Linux Foundation Training course completions: **LFD123 Open Source RT-Thread RTOS on RISC-V**, **LFEL1002 Getting Started with Rust**, and **LFD102 A Beginner's Guide to Open Source Software Development**.

## Core Focus

**Languages:** C, C++, Python, C#  
**AI / Computer Vision:** OpenCV, PyTorch, CNNs, ResNet-18, image preprocessing, classification, model evaluation  
**Robotics:** ROS 2, Nav2, TF2, rosbag2, differential-drive navigation  
**Embedded / RTOS:** Zephyr RTOS, ztest/Twister, bounded queues, synchronization, fault injection  
**Systems:** Linux, Git, CMake, GitHub Actions, Docker, CodeQL, ASan/UBSan  
**Industrial:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation

## Current Direction

Industrial computer vision · autonomous navigation/control · embedded telemetry transport · physical sensor/bus qualification · hardware watchdogs · upstream robotics/embedded contributions

---

I keep performance and hardware claims deliberately scoped. Reproducibility links and claim-level notes are in [**Engineering Evidence**](./EVIDENCE.md).
