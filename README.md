<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Systems & Robotics Software Engineering" width="100%">
</p>

# Taha Zarif

### Systems & Robotics Software Engineer
**Privacy-First Local AI · C++ / ROS 2 · Embedded / RTOS · Production-Grade Verification**

I build testable systems software across robotics, embedded/real-time systems, and privacy-aware desktop automation. My engineering work emphasizes deterministic behavior, bounded resources, explicit failure handling, reproducible verification, CI, and hardware/software debugging.

Currently a Grade 10 student in Mashhad, Iran, with hands-on robotics competition and industrial CNC/PLC experience.

[**Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [**Repositories**](https://github.com/tahazarif10?tab=repositories)

## Featured Engineering

### [Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)
C++20 differential-drive control/navigation library with occupancy-grid A*, collision-safe path shaping, PID, pure pursuit, kinematics, and SE(2) odometry. Verified across GCC, Clang, and MSVC with ASan/UBSan, CodeQL, installable CMake packaging, and deterministic benchmarks.

### [Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)
Privacy-first Windows desktop copilot foundation built around bounded local context sensing, UI Automation, explicit privacy capabilities, deterministic orchestration, fault isolation, and strict Windows/cross-platform verification.

### [ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)
ROS 2 Jazzy/Nav2 system integration with lifecycle control, explicit TF/QoS contracts, stale/non-finite input handling, rosbag2 deterministic replay, diagnostics, fault injection, and fail-closed integration tests.

### [Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)
C/Zephyr RTOS sensor hub with static threads, bounded message queues, synchronization, supervision, bounded bus retries, sequence/timestamp validation, deterministic fault injection, and **12/12 ztest/Twister** cases on `native_sim`.

**Also:** [Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector) — deterministic Python/OpenCV/PyTorch inspection pipeline with classical CV, TinyCNN/ResNet-18 paths, reproducible dataset preparation, metrics, and evidence-scoped evaluation.

## Selected Open-Source Contributions

**8 upstream pull requests merged.** Selected contributions:

- **[Robotics Toolbox for Python #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)** — fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before the solver update; added regression coverage.
- **[GPS-Denied UAV Navigation #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28)** — preserved fail-closed localization behavior for invalid/non-finite TDOA data.
- **[Motrix #1885](https://github.com/agalwood/Motrix/pull/1885)** — restored Windows tray left-click window toggling and strengthened cross-platform regression coverage after maintainer review.
- **[Zephyr RTOS #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636)** — corrected public Bluetooth HCI documentation to clarify the BR/EDR-only scope of status `0x29`.

All merged contributions and claim-level references are documented in [**Engineering Evidence**](./EVIDENCE.md).

## Industrial / Real-World Engineering

Hands-on work includes Python/PyQt control software with **Delta AS228T-series PLCs over Modbus TCP**, pulse/direction servo motion for CNC saw/clamp axes, millimetre-to-pulse conversion, homing/jog/state logic, limits, alarms, safety interlocks, and physical PLC/I/O debugging.

## Robotics

**4th place — FIRA RoboWorld Cup 2024**, São Luís, Brazil, with **Kamaan Shahriar Iran** in Cliff Hanger Lightweight (U14). Additional FIRA competition participation and sourcing are documented in [EVIDENCE.md](./EVIDENCE.md#robotics-competition-experience--fira).

## Core Stack

**C · C++20 · Python · C#/.NET · ROS 2 · Nav2 · Zephyr RTOS · OpenCV · PyTorch · Linux · CMake · GitHub Actions · CodeQL · ASan/UBSan · PLC/Modbus/Servo Automation**

---

Performance, safety, and hardware claims are intentionally scoped. Reproducibility links, CI evidence, benchmark boundaries, and full upstream contribution history are maintained in [**Engineering Evidence**](./EVIDENCE.md).
