# Taha Zarif

## Robotics & Embedded Software

**GitHub:** [github.com/tahazarif10](https://github.com/tahazarif10)  
**LinkedIn:** [linkedin.com/in/taha-zarif-bba94b397](https://www.linkedin.com/in/taha-zarif-bba94b397/)  
**Engineering Evidence:** [EVIDENCE.md](./EVIDENCE.md)

### Profile

Robotics and embedded-software focused developer with hands-on industrial automation experience spanning CNC control software, PLC I/O, servo motion, safety/readiness state logic, and hardware/software debugging. Builds testable C/C++ and Python systems with explicit contracts, bounded resources, deterministic regression evidence, CI, and fault-injection workflows.

### Selected Industrial Engineering Work

- Developed Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP.
- Implemented and debugged servo-axis control for CNC saw and clamp mechanisms, including millimetre-to-pulse conversion, homing, jog, busy/done states, limits, alarms, and readiness/safety interlocks.
- Worked across PLC I/O, pulse/direction motion, machine-state logic, and physical hardware/software integration.

### Robotics Competition Experience

- **4th place — FIRA RoboWorld Cup 2024, São Luís, Maranhão, Brazil** — competed with **Kamaan Shahriar Iran** in **Cliff Hanger Lightweight (U14)**. The official AVIS roster lists Taha Zarif as a Youth Member of the team; placement is additionally corroborated by the team coach's public FIRA 2024 award record. See [evidence](./EVIDENCE.md#fira-roboworld-cup-2024--brazil).
- **3rd-place national finish — FIRA Iran robotics competition** — retained as a participant-provided competition result until the exact public award-page mapping is identified.
- **Iran 2026 FIRA Open Competition** — competed with **Kamaan** in **Air Autonomous Race (U19)**.
- **Iran 2025 FIRA Open Competition** — competed with **Kamaan 3** in **Cliff Hanger Lightweight (U19)**.

### Selected Project — [robotics-control-core](https://github.com/tahazarif10/robotics-control-core)

- Built a middleware-independent **C++20** navigation/control library for a differential-drive robot.
- Implemented occupancy-grid A*, obstacle inflation, collision-safe path smoothing, PID control, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry.
- Packaged the library with CMake as reusable target `robotics::control`; verified an independent `find_package` consumer.
- Added GCC/Clang/MSVC CI, warnings-as-errors, ASan/UBSan, CodeQL, Docker, Dependabot, deterministic regression tests, and benchmark evidence.
- On the checked-in v0.2 deterministic fixture, reduced the path representation from 26 to 5 waypoints while remaining collision-free; the pure-pursuit benchmark reached the goal in 479 vs 545 PID-baseline steps with lower measured travel, cross-track error, and final goal error on that fixture.

### Selected Project — [ros2-autonomous-mobile-robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

- Built a reproducible **ROS 2 Jazzy / Ubuntu 24.04** AMR workspace and a **C++20 lifecycle control adapter** consuming `robotics-control-core` at a pinned commit rather than duplicating algorithm code.
- Implemented bounded `geometry_msgs/Twist` output with explicit safe-stop behavior for missing, stale, and non-finite inputs and goal completion.
- Added a deterministic Nav2 fixture using a checked-in 6 m × 6 m map, **NavFn A***, **Regulated Pure Pursuit**, explicit TF ownership, QoS contracts, and end-to-end goal/collision assertions.
- Added runtime diagnostics, NaN/stale-input fault injection, real rosbag2 sqlite3 replay, missing-global-TF fail-closed verification, and namespace-isolated integration tests.

### Selected Project — [embedded-rtos-sensor-hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)

- Built a **C / Zephyr RTOS 4.4.2** sensor hub on `native_sim` with five statically defined threads, a bounded `k_msgq` pipeline, `k_sem` startup synchronization, and `k_mutex` protected state.
- Implemented software heartbeat supervision, queue metrics, a testable acquisition-driver boundary, simulated I2C/SPI transaction contracts, bounded bus retries, sequence/timestamp integrity checks, and deterministic fault injection.
- Expanded the **ztest/Twister** regression suite to **12/12 passing test cases** on merged `main`.
- Evidence is deliberately scoped to native simulation; no physical I2C/SPI timing, electrical behavior, or hardware-watchdog claim is made.

### Open-Source Contributions

**6 merged upstream pull requests** across robotics, desktop software, frontend, orchestration, and localization projects.

- **Robotics Toolbox for Python** — merged [PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644): restored a missing distance-transform diagonal and added regression coverage.
- **Motrix** — merged [PR #1885](https://github.com/agalwood/Motrix/pull/1885): restored tray left-click window toggling and strengthened cross-platform regression tests after maintainer review.
- **DQ QuestionBank Core** — merged [PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) and [PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128): editor draft recovery and table-row preservation.
- **Orchestrator MCP** — merged [PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11): fixed delegated review-synthesis input.
- **GPS-Denied UAV Navigation** — merged [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28): preserved fail-closed handling for invalid TDOA localization data.

Currently under upstream review and **not counted as merged**:

- **Zephyr RTOS** — [PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636), Bluetooth HCI documentation/API-reference scope clarification.
- **Robotics Toolbox for Python** — [PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667), numerical-IK pre-step convergence fix with regression coverage.

### Technical Skills

**Languages:** C, C++20, Python, C#  
**Robotics:** ROS 2 Jazzy, Nav2, TF2, lifecycle nodes, rosbag2, differential-drive navigation, autonomous robotics  
**Embedded / RTOS:** Zephyr RTOS, native_sim, ztest/Twister, `k_msgq`, threads, mutexes, semaphores, bounded retries, fault injection, simulated I2C/SPI driver contracts  
**Systems & Tooling:** Linux, Git, CMake, GitHub Actions, CI/CD, Docker, colcon, ament_cmake  
**Engineering:** Unit/Integration Testing, Debugging, Software Architecture, deterministic regression, fault injection, CodeQL, ASan/UBSan  
**Industrial / Motion:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation, hardware/software integration

### Current Direction

Embedded telemetry transport · backpressure/recovery · physical sensor/bus qualification · hardware watchdogs · autonomous navigation and control · upstream robotics/embedded contributions

---

*Public version intentionally excludes private contact details. Claim-level sources and scope are maintained in [EVIDENCE.md](./EVIDENCE.md).*
