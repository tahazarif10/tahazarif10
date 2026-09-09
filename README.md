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

**Languages:** C++, Python, C#  
**Platforms & Tools:** Linux, Git, CMake, ROS 2, .NET, Arduino  
**Engineering:** Unit Testing, CI, Debugging, Software Architecture

## Industrial Engineering Work

Selected hands-on work on CNC and industrial automation systems:

- Developed Python/PyQt control software integrating with a **Delta AS228T-series PLC** over Modbus TCP.
- Implemented and debugged servo-axis motion for saw and clamp mechanisms, including millimetre-to-pulse conversion, homing, jog, busy/done state, limits, alarms, and readiness/safety interlocks.
- Worked across PLC I/O, pulse/direction motion, machine state logic, and hardware/software integration to diagnose real machine behavior rather than only simulated software.

## Featured Work

### [Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)

A middleware-independent C++20 robotics core for differential-drive navigation: deterministic A* planning, obstacle inflation, collision-safe path shaping, PID and interpolated-lookahead pure-pursuit control, forward/inverse kinematics, and SE(2) odometry.

**Public engineering evidence:** installable CMake package, GCC/Clang/MSVC CI, ASan/UBSan, CodeQL, deterministic regression tests, package-consumer verification, benchmark documentation, and a reviewed PR workflow. In the checked-in v0.2 fixture, pure pursuit reaches the goal collision-free using 5 smoothed waypoints versus the 26-waypoint PID baseline; the repository documents the full metrics and scopes them as regression evidence rather than hardware claims.

### [ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

A ROS 2 Jazzy / Ubuntu 24.04 autonomous-mobile-robot stack developed in evidence-driven milestones. v0.3 adds a deterministic Nav2 system fixture on top of the lifecycle control-core adapter.

**Public engineering evidence:** hosted `colcon build` / `colcon test` CI; a C++20 lifecycle adapter consuming `robotics-control-core` at a pinned commit; bounded `cmd_vel` and safe-stop behavior for stale/missing/non-finite input; NavFn A* planning; Regulated Pure Pursuit; a checked-in 6 m × 6 m static-map fixture; explicit `map -> odom -> base_link -> base_scan` ownership; documented QoS contracts; lifecycle-aware navigation-goal submission; and end-to-end assertions for goal success, obstacle clearance, final position tolerance, and a non-trivial detour. All navigation results are explicitly scoped to the deterministic software fixture rather than physical hardware.

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

## Currently Building Toward

- rosbag replay, deterministic fault injection, and navigation observability
- Real-time embedded systems and RTOS work
- Sensor and communication interfaces
- Reproducible simulation and later hardware validation
- Focused upstream robotics/embedded open-source contributions

I’m particularly interested in software that has to interact reliably with the physical world.
