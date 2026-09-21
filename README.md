<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Systems & Robotics Software Engineering" width="100%">
</p>

# Taha Zarif

### Systems & Robotics Software Engineer
**C++ · ROS 2 · Zephyr RTOS · Embedded Systems · Privacy-First Windows Systems**

I build systems software for robotics, embedded/real-time platforms, and privacy-aware desktop automation, with a focus on deterministic behavior, bounded resources, explicit failure handling, reproducible verification, CI, and hardware/software debugging.

**11 upstream pull requests merged across 7 external repositories**, including **Zephyr RTOS, Apache NuttX, Robotics Toolbox for Python, and Motrix**.

[Resume](./RESUME.md) · [Engineering Evidence](./EVIDENCE.md) · [LinkedIn](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [Repositories](https://github.com/tahazarif10?tab=repositories)

## Selected upstream contributions

- **[Zephyr RTOS #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971)** — added `native_sim` coverage for public Bluetooth identity-management APIs through the real host path with a fake HCI driver.
- **[Robotics Toolbox for Python #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)** — fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before a potentially singular solver update.
- **[Motrix #2138](https://github.com/agalwood/Motrix/pull/2138)** — restored the macOS Menu Bar Only Dock-state invariant after main-window dismissal and added focused regression coverage.

More upstream work: [Zephyr #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636) · [Robotics Toolbox #644](https://github.com/petercorke/robotics-toolbox-python/pull/644) · [Apache NuttX #20147](https://github.com/apache/nuttx/pull/20147) · [Motrix #1885](https://github.com/agalwood/Motrix/pull/1885) · [full evidence](./EVIDENCE.md)

## Featured projects

- **[Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)** — C++20 differential-drive planning/control library with occupancy-grid A*, collision-aware path shaping, PID, pure pursuit, SE(2) odometry, deterministic benchmarks, multi-compiler CI, sanitizers, CodeQL, and installable CMake packaging.
- **[Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)** — privacy-first Windows systems foundation with identity-first privacy gates, RAM-only sensing, bounded orchestration, and deterministic failure/recovery verification.
- **[ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)** — ROS 2 Jazzy/Nav2 stack with lifecycle control, TF/QoS contracts, deterministic rosbag2 replay, diagnostics, fault injection, and fail-closed behavior.
- **[Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)** — C/Zephyr RTOS sensor hub with static threads, bounded queues, supervision, bounded retry/recovery, fault injection, and checked-in Twister coverage.

## Real-world engineering

I also work on Python/PyQt industrial control software with Delta AS-series PLCs over Modbus TCP, pulse/direction servo motion, homing/jog/state logic, limits, alarms, safety interlocks, and physical PLC/I/O debugging.

## Stack

**C · C++20 · Python · C#/.NET · ROS 2 · Nav2 · Zephyr RTOS · OpenCV · PyTorch · Linux · CMake · GitHub Actions · CodeQL · ASan/UBSan · PLC/Modbus/Servo Automation**

---

Grade 10 student in Mashhad, Iran. **4th place — FIRA RoboWorld Cup 2024**, São Luís, Brazil, with **Kamaan Shahriar Iran** in Cliff Hanger Lightweight (U14).

Performance, safety, hardware, and credential claims are intentionally scoped. Reproducibility links and the complete upstream contribution record are maintained in [Engineering Evidence](./EVIDENCE.md).
