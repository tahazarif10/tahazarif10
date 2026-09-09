# Taha Zarif

## Robotics & Embedded Software

**GitHub:** [tahazarif10](https://github.com/tahazarif10)

### Profile

Robotics and embedded-software focused developer with hands-on industrial automation experience spanning CNC control software, PLC I/O, servo motion, safety/readiness state logic, and hardware/software debugging. Builds testable C++ and Python systems with explicit contracts, deterministic regression evidence, CI, and reproducible engineering workflows.

### Selected Industrial Engineering Work

- Developed Python/PyQt control software integrating with **Delta AS228T-series PLCs** over Modbus TCP.
- Implemented and debugged servo-axis control for CNC saw and clamp mechanisms, including millimetre-to-pulse conversion, homing, jog, busy/done states, limits, alarms, and readiness/safety interlocks.
- Worked across PLC I/O, pulse/direction motion, machine state logic, and physical hardware/software integration.

### Selected Project — [robotics-control-core](https://github.com/tahazarif10/robotics-control-core)

- Built a middleware-independent **C++20** navigation/control library for a differential-drive robot.
- Implemented occupancy-grid A*, obstacle inflation, collision-safe path smoothing, PID control, interpolated-lookahead pure pursuit, kinematics, and SE(2) odometry.
- Packaged the library with CMake as reusable target `robotics::control`; verified an independent `find_package` consumer.
- Added GCC/Clang/MSVC CI, warnings-as-errors, ASan/UBSan, CodeQL, Docker, Dependabot, deterministic regression tests, and benchmark evidence.
- On the checked-in v0.2 deterministic fixture, reduced the path representation from 26 to 5 waypoints while remaining collision-free; the pure-pursuit benchmark reached the goal in 479 vs 545 PID-baseline steps with lower measured travel, cross-track error, and final goal error on that fixture.

### Selected Project — [ros2-autonomous-mobile-robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

- Built a reproducible **ROS 2 Jazzy / Ubuntu 24.04** AMR workspace with a differential-drive Xacro model and headless launch verification.
- Added a **C++20 lifecycle control adapter** that consumes `robotics-control-core` at a pinned commit instead of duplicating algorithm code.
- Converts `nav_msgs/Path` and `nav_msgs/Odometry` into the middleware-independent control contract and publishes bounded `geometry_msgs/Twist` commands.
- Implements explicit safe-stop behavior for missing, stale, and non-finite inputs and for goal completion.
- Hosted GitHub Actions CI verifies dependency resolution, `colcon build`, `colcon test`, lifecycle transitions, invalid-configuration rejection, and the earlier Xacro/launch baseline.

### Open Source Contributions

- **Robotics Toolbox for Python** — merged PR #644: restored a missing distance-transform diagonal.
- **Motrix** — merged PR #1885: restored tray left-click window toggling.
- **DQ QuestionBank Core** — merged PRs #127 and #128: editor draft recovery and table-row preservation.
- **Orchestrator MCP** — merged PR #11: fixed delegated review-synthesis input.
- **GPS-Denied UAV Navigation** — merged PR #28: preserved fail-closed handling for invalid TDOA localization data.

### Technical Skills

**Languages:** C++20, Python, C#  
**Systems & Tooling:** Linux, Git, CMake, GitHub Actions, CI/CD, Docker, ROS 2 Jazzy, colcon, ament_cmake  
**Engineering:** Unit Testing, Debugging, Software Architecture, deterministic regression, CodeQL, ASan/UBSan  
**Industrial / Motion:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation, hardware/software integration

### Current Direction

Nav2 integration · localization · real-time embedded systems · sensor/communication interfaces · autonomous navigation and control

---

*Public version intentionally excludes private contact details.*
