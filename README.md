<p align="center">
  <img src="./banner.png" alt="Taha Zarif banner" width="100%">
</p>

# Hi, I'm Taha 👋

[**Public Technical Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/)

I build software around robotics, embedded systems, and real-time applications, with a focus on reliability, deterministic behavior, testing, and debugging.

## Focus

- Robotics & autonomous systems
- Embedded and real-time software
- C++ systems programming
- Hardware/software integration
- Testing, debugging, and root-cause analysis

## Tech

**Languages:** C, C++, Python, C#  
**Platforms & Tools:** Linux, Git, CMake, ROS 2, Zephyr RTOS, Nav2, ztest/Twister, .NET  
**Engineering:** Unit Testing, CI, Fault Injection, Deterministic Regression, Debugging, Software Architecture

## Industrial Engineering Work

Selected hands-on work on CNC and industrial automation systems:

- Developed Python/PyQt control software integrating with a **Delta AS228T-series PLC** over Modbus TCP.
- Implemented and debugged servo-axis motion for saw and clamp mechanisms, including millimetre-to-pulse conversion, homing, jog, busy/done state, limits, alarms, and readiness/safety interlocks.
- Worked across PLC I/O, pulse/direction motion, machine state logic, and hardware/software integration to diagnose real machine behavior rather than only simulated software.

## Robotics Competition Experience

- **FIRA RoboWorld Cup 2024 — São Luís, Brazil** — participant with **Kamaan Shahriar Iran** at the global FIRA competition; participant badge retained. Reported **4th-place finish**.
- **FIRA Iran robotics competition** — national-level **3rd-place finish**.
- **Iran 2026 FIRA Open Competition** — participant with **Kamaan** in **Air Autonomous Race (U19)**, adding hands-on competition exposure to autonomous aerial robotics.
- **Iran 2025 FIRA Open Competition** — participant with **Kamaan 3** in **Cliff Hanger Lightweight (U19)**.

## Featured Work

### [Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)

A middleware-independent C++20 robotics core for differential-drive navigation: deterministic A* planning, obstacle inflation, collision-safe path shaping, PID and interpolated-lookahead pure-pursuit control, forward/inverse kinematics, and SE(2) odometry.

**Public engineering evidence:** installable CMake package, GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, deterministic regression tests, package-consumer verification, and benchmark documentation. In the checked-in v0.2 fixture, pure pursuit reaches the goal collision-free using 5 smoothed waypoints versus the 26-waypoint PID baseline; the repository scopes the metrics as regression evidence rather than hardware claims.

### [ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

A ROS 2 Jazzy / Ubuntu 24.04 autonomous-mobile-robot stack developed through **v0.4**: lifecycle control, deterministic Nav2 integration, observability, fault injection, and rosbag2 replay.

**Public engineering evidence:** hosted `colcon build` / `colcon test` CI; a C++20 lifecycle adapter consuming `robotics-control-core` at a pinned commit; bounded `cmd_vel` and safe-stop behavior for stale/missing/non-finite input; NavFn A* + Regulated Pure Pursuit; runtime TF/QoS verification; diagnostics with stable stop reasons; NaN/stale-input fault injection; a real sqlite3 rosbag replayed twice with equal canonical outcomes; missing-global-TF fail-closed verification; and a diagnosed/fixed concurrent ROS test-graph contamination bug using namespace isolation. All results are scoped to deterministic software fixtures rather than physical hardware.

### [Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)

A C / **Zephyr RTOS 4.4.2** sensor-hub project developed and verified on `native_sim` before hardware qualification.

**Public engineering evidence:** five statically defined RTOS threads; bounded `k_msgq`; `k_sem` startup synchronization; `k_mutex` protected state; software heartbeat supervision; queue drop/high-watermark accounting; a testable acquisition-driver boundary; simulated I2C-style temperature and SPI-style vibration transactions; bounded bus retries with metrics; sequence/timestamp integrity checks; deterministic producer-stall and transient bus-fault injection; normal/stall/bus-fault hosted builds; and **12/12 ztest/Twister cases passing** on merged `main`. Physical bus timing and hardware behavior are intentionally not claimed.

### [Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)

A privacy-first Windows desktop copilot project focused on controlled context sensing, strict privacy boundaries, deterministic behavior, and testable system architecture.

The project includes automated CI, deterministic tests, architecture documentation, privacy constraints, and explicit engineering acceptance criteria.

## Open Source Contributions

I contribute focused fixes and tests to existing projects, with an emphasis on reproducible defects and reviewable changes.

- **Robotics Toolbox for Python** — merged [PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644), restoring a missing distance-transform diagonal.
- **Motrix** — merged [PR #1885](https://github.com/agalwood/Motrix/pull/1885), restoring tray left-click window toggling.
- **DQ QuestionBank Core** — merged [PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) and [PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128), covering editor draft recovery and table-row preservation.
- **Orchestrator MCP** — merged [PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11), fixing delegated review synthesis input.
- **GPS-Denied UAV Navigation** — merged [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28), preserving fail-closed handling for invalid TDOA localization data.

Two additional upstream changes are currently under review: a Zephyr Bluetooth HCI documentation/API-reference clarification and a Robotics Toolbox numerical-IK convergence fix. They are not counted as merged achievements until upstream merges them.

## Currently Building Toward

- Bounded embedded telemetry framing and transport
- Queue-pressure/backpressure testing and recovery
- Physical sensor/bus and hardware-watchdog qualification
- Reproducible hardware timing evidence
- Focused upstream robotics/embedded open-source contributions

I’m particularly interested in software that has to interact reliably with the physical world.
