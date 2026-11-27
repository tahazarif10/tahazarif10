<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Real-Time Robotics, Embedded Systems, and Industrial AI" width="100%">
</p>

# Hi, I'm Taha.

I'm a high-school student building software for the hardware/software boundary: **real-time robotics, embedded systems, industrial automation, and applied AI**.

The work I care about most starts after a demo appears to work: timing, failure modes, edge cases, reproducible tests, bounded resources, safety behavior, and understanding why a system breaks when software meets hardware.

My current theme is simple:

> **Reliable intelligent systems for robots and industrial machines.**

## Current focus

- **Embedded & RTOS:** Zephyr RTOS, Bluetooth host behavior, bounded queues, concurrency, supervision, and fault recovery.
- **Robotics & control:** C/C++, ROS 2, Nav2, planning, odometry, lifecycle behavior, diagnostics, and fail-safe motion.
- **Industrial automation:** PLCs, Modbus TCP, servo motion, homing, interlocks, alarms, and real machine debugging.
- **Applied AI:** computer vision and grounded LLM/RAG systems with explicit evidence boundaries and reproducible evaluation.

## Evidence-first engineering

I try to keep public claims proportional to what the code, tests, CI, and upstream reviews actually prove.

- **12 merged upstream pull requests** across **7 external repositories**.
- Contributions include **Zephyr RTOS**, **Apache NuttX**, **Robotics Toolbox for Python**, **Motrix**, and other real projects.
- Project claims are backed by verification notes, CI runs, regression tests, and scoped performance boundaries.

Full claim-level record: **[Engineering Evidence](./EVIDENCE.md)**.

## Selected upstream contributions

- [Zephyr RTOS #119955](https://github.com/zephyrproject-rtos/zephyr/pull/119955) — reject invalid Bluetooth identities during local OOB lookup.
- [Zephyr RTOS #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971) — add public Bluetooth identity-management API coverage through the real host path.
- [Robotics Toolbox for Python #667](https://github.com/petercorke/robotics-toolbox-python/pull/667) — fix numerical IK convergence ordering before singular solver updates.
- [Apache NuttX #20147](https://github.com/apache/nuttx/pull/20147) — document Python linting/formatting contributor workflow.
- [Motrix #2138](https://github.com/agalwood/Motrix/pull/2138) — restore macOS Menu Bar Only behavior after the main window is dismissed.

## Projects I want people to judge me by

### [Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)
A Zephyr-based sensor hub focused on static resources, bounded message queues, supervision, deterministic fault injection, and Twister tests.

### [Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)
A C++20 differential-drive planning/control library with A*, obstacle inflation, PID, pure pursuit, kinematics, odometry, deterministic benchmarks, sanitizers, and CI.

### [ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)
A ROS 2 / Nav2 stack focused on lifecycle behavior, TF/QoS contracts, replayable tests, diagnostics, stale-input handling, and fail-closed behavior.

### [Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector)
An OpenCV/PyTorch defect-classification pipeline with deterministic data preparation, training/inference CLI, calibration-aware evaluation, and scoped model claims.

### [Grounded LLM Platform](https://github.com/tahazarif10/grounded-llm-platform)
A small RAG platform built around explicit retrieval, provenance, structured outputs, citation validation, abstention, and measurable retrieval evaluation.

### [Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)
A privacy-first Windows systems foundation with bounded sensing, capability-gated UI Automation, orchestration limits, and provider-isolation recovery evidence.

## How I like to work

I prefer small, explainable changes over clever ones. I reproduce a problem before fixing it, add regression tests where practical, and keep demo claims separate from verified behavior.

A bug caused by a timing assumption, encoder edge, servo parameter, protocol detail, or stale state is usually more interesting to me than a polished UI with no hard engineering underneath.

## Tools I use

**C · C++20 · Python · C#/.NET · Zephyr RTOS · ROS 2 · Nav2 · OpenCV · PyTorch · FastAPI · Docker · CMake · GitHub Actions · PLC / Modbus / Servo Automation**

## Robotics background

Robotics is what pulled me into engineering. I competed with **Kamaan Shahriar Iran** at the **FIRA RoboWorld Cup 2024** in São Luís, Brazil, where our team placed **4th in Cliff Hanger Lightweight (U14)**.

---

[Resume](./RESUME.md) · [Engineering Evidence](./EVIDENCE.md) · [LinkedIn](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [Repositories](https://github.com/tahazarif10?tab=repositories)
