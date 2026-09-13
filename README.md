<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Robotics & Embedded Software" width="100%">
</p>

# Taha Zarif

### Robotics · Embedded Systems · Computer Vision · Industrial Automation

Grade 10 student building testable software for **robotics, embedded/real-time systems, computer vision, and industrial automation**. I focus on deterministic behavior, bounded-resource design, fault handling, CI, reproducible verification, and hardware/software debugging.

[**Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [**Repositories**](https://github.com/tahazarif10?tab=repositories)

## Highlights

- **8 merged upstream pull requests**, including contributions to **Zephyr RTOS** and **Robotics Toolbox for Python**.
- Built public robotics/embedded projects around **ROS 2, Nav2, Zephyr RTOS, C++20 control, OpenCV, and PyTorch**.
- Hands-on industrial work with **Delta AS228T-series PLCs, Modbus TCP, pulse/direction servo control, homing, interlocks, and CNC debugging**.
- **4th place — FIRA RoboWorld Cup 2024**, São Luís, Brazil, with Kamaan Shahriar Iran in Cliff Hanger Lightweight (U14).

## Upstream Open-Source Contributions

| Project | Merged contribution | Engineering impact |
| --- | --- | --- |
| **Zephyr RTOS** | [PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636) | Clarified Bluetooth HCI status `0x29` scope for BR/EDR-only use across public API/test documentation. |
| **Robotics Toolbox for Python** | [PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667) | Fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before solver update; added regression coverage. |
| **Robotics Toolbox for Python** | [PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644) | Restored a missing distance-transform diagonal and added focused regression coverage. |
| **Motrix** | [PR #1885](https://github.com/agalwood/Motrix/pull/1885) | Restored Windows tray left-click window toggling and strengthened regression tests after maintainer review. |
| **GPS-Denied UAV Navigation** | [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28) | Preserved fail-closed localization behavior for invalid/non-finite TDOA data. |
| **DQ QuestionBank Core** | [PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) | Added editor draft autosave and crash recovery. |
| **DQ QuestionBank Core** | [PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128) | Preserved ragged table-row shape during editor round trips. |
| **Orchestrator MCP** | [PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11) | Fixed delegated review-synthesis input and added regression coverage. |

## Selected Engineering Projects

| Project | Focus | Verification / evidence |
| --- | --- | --- |
| [**Industrial Vision Inspector**](https://github.com/tahazarif10/industrial-vision-inspector) | Python · OpenCV · PyTorch · CNN / ResNet-18 · deterministic NEU-CLS preparation · image-quality metrics | **7/7 local tests** · deterministic synthetic smoke verification · evidence-scoped model card |
| [**Robotics Control Core**](https://github.com/tahazarif10/robotics-control-core) | C++20 · A* · obstacle inflation · path smoothing · PID · pure pursuit · kinematics · SE(2) odometry | GCC/Clang/MSVC CI · ASan/UBSan · CodeQL · deterministic benchmarks |
| [**ROS 2 Autonomous Mobile Robot**](https://github.com/tahazarif10/ros2-autonomous-mobile-robot) | ROS 2 Jazzy · Nav2 · lifecycle control · TF/QoS · rosbag2 replay · fault injection | `colcon` CI · fail-closed tests · deterministic replay · integration-test isolation |
| [**Embedded RTOS Sensor Hub**](https://github.com/tahazarif10/embedded-rtos-sensor-hub) | C · Zephyr RTOS 4.4.2 · bounded queues · supervision · bus retries · fault injection | `native_sim` · **12/12 ztest/Twister** · hosted CI |
| [**Local AI Desktop Copilot**](https://github.com/tahazarif10/local-ai-desktop-copilot) | C#/.NET · WinUI · bounded context sensing · privacy gates · deterministic system design | Cross-platform core CI · strict Windows builds · explicit physical acceptance gates |

For exact benchmark scope, CI runs, limitations, and claim-level references, see [**Engineering Evidence**](./EVIDENCE.md).

## Industrial Automation & CNC

Hands-on engineering work includes:

- Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP
- pulse/direction servo motion for CNC saw and clamp axes
- millimetre-to-pulse conversion, homing, jog, busy/done state logic, limits, alarms, and readiness/safety interlocks
- PLC I/O and physical machine debugging

## Robotics Competition Experience

- **4th place — FIRA RoboWorld Cup 2024**, São Luís, Maranhão, Brazil — **Kamaan Shahriar Iran**, **Cliff Hanger Lightweight (U14)**. [Official AVIS roster](https://events.avisengine.com/events/fira-2024/teams) lists **Taha Zarif** as a Youth Member of the team.
- **Iran 2026 FIRA Open Competition** — Kamaan · Air Autonomous Race (U19).
- **Iran 2025 FIRA Open Competition** — Kamaan 3 · Cliff Hanger Lightweight (U19).
- **3rd-place national FIRA Iran finish** — retained as participant-provided competition history; exact public award-page mapping is still being identified.

Competition evidence and sourcing notes are maintained in [EVIDENCE.md](./EVIDENCE.md#robotics-competition-experience--fira).

## Training

Linux Foundation Training completions:

- **LFD123 — Open Source RT-Thread RTOS on RISC-V**
- **LFEL1002 — Getting Started with Rust**
- **LFD102 — A Beginner's Guide to Open Source Software Development**

## Technical Focus

**Languages:** C, C++20, Python, C#  
**Robotics:** ROS 2 Jazzy, Nav2, TF2, lifecycle nodes, rosbag2, differential-drive navigation  
**Embedded / RTOS:** Zephyr RTOS, ztest/Twister, bounded queues, synchronization, retries, fault injection  
**AI / Computer Vision:** OpenCV, PyTorch, CNNs, ResNet-18, preprocessing, classification, evaluation  
**Systems:** Linux, Git, CMake, GitHub Actions, Docker, CodeQL, ASan/UBSan  
**Industrial:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation

---

Performance, safety, and hardware claims are intentionally scoped. Reproducibility links and claim-level evidence are maintained in [**Engineering Evidence**](./EVIDENCE.md).
