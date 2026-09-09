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

- Built a reproducible **ROS 2 Jazzy / Ubuntu 24.04** AMR workspace and a **C++20 lifecycle control adapter** that consumes `robotics-control-core` at a pinned commit rather than duplicating algorithm code.
- Implemented bounded `geometry_msgs/Twist` output with explicit safe-stop behavior for missing, stale, and non-finite inputs and goal completion.
- Added a deterministic Nav2 fixture using a checked-in 6 m × 6 m map, **NavFn A***, **Regulated Pure Pursuit**, explicit TF ownership, QoS contracts, and end-to-end goal/collision assertions.
- Added runtime diagnostics with stable stop reasons plus fault injection for NaN odometry, stale odometry, and stale paths; verified zero-command fail-closed behavior.
- Generated a real **rosbag2 sqlite3** fixture from checked-in source data and replayed the same bag twice through the live lifecycle adapter with equal canonical outcomes; the fixture contains 8 messages spanning 1.2 s of recorded time at 2.0× configured pacing.
- Verified missing-global-TF behavior by removing the `map -> odom` / `odom -> base_link` provider and asserting that `bt_navigator` never becomes ACTIVE and no non-zero `cmd_vel` is produced.
- Diagnosed and fixed a concurrent ROS test-graph contamination failure without weakening collision assertions by namespace-isolating integration fixtures and serializing Nav2 launch tests.
- GitHub Actions verifies the full `rosdep` / `colcon build` / `colcon test` suite; the final v0.4 merged-main run is public engineering evidence.

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

Zephyr RTOS · real-time embedded systems · sensor/communication interfaces · deterministic fault handling · hardware validation · autonomous navigation and control

---

*Public version intentionally excludes private contact details.*
