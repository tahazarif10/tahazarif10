# Taha Zarif

## Robotics & Embedded Software

**GitHub:** [tahazarif10](https://github.com/tahazarif10)  
**LinkedIn:** [linkedin.com/in/taha-zarif-bba94b397](https://www.linkedin.com/in/taha-zarif-bba94b397/)  
**Engineering Evidence:** [EVIDENCE.md](./EVIDENCE.md)

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
- Added a deterministic **Nav2 v0.3** system fixture using Nav2 Loopback Simulator, a checked-in 6 m × 6 m static map, NavFn with A* enabled, and Regulated Pure Pursuit.
- Defined and runtime-tested the `map -> odom -> base_link -> base_scan` TF chain and documented the fixture QoS contracts.
- Added an end-to-end `NavigateToPose` test that verifies successful goal completion, obstacle clearance, final position error within 0.20 m, and a non-trivial detour around the central obstacle.
- Hosted GitHub Actions CI verifies dependency resolution, `colcon build`, `colcon test`, lifecycle transitions, invalid-configuration rejection, TF availability, and the deterministic Nav2 fixture. Navigation evidence is explicitly scoped to the checked-in simulation fixture, not hardware performance.

### Open Source Contributions

**6 merged upstream pull requests** across robotics, desktop software, frontend, orchestration, and localization projects.

- **Robotics Toolbox for Python** — merged PR #644: restored a missing distance-transform diagonal.
- **Motrix** — merged PR #1885: restored tray left-click window toggling.
- **DQ QuestionBank Core** — merged PRs #127 and #128: editor draft recovery and table-row preservation.
- **Orchestrator MCP** — merged PR #11: fixed delegated review-synthesis input.
- **GPS-Denied UAV Navigation** — merged PR #28: preserved fail-closed handling for invalid TDOA localization data.

### Technical Skills

**Languages:** C++20, Python, C#  
**Systems & Tooling:** Linux, Git, CMake, GitHub Actions, CI/CD, Docker, ROS 2 Jazzy, Nav2, TF2, colcon, ament_cmake  
**Engineering:** Unit Testing, Debugging, Software Architecture, deterministic regression, CodeQL, ASan/UBSan  
**Industrial / Motion:** PLC, Modbus TCP, servo motion, pulse/direction, CNC automation, hardware/software integration

### Current Direction

rosbag replay · deterministic fault injection · real-time embedded systems · RTOS · sensor/communication interfaces · autonomous navigation and control

---

*Public version intentionally excludes private contact details.*
