<p align="center">
  <img src="./banner.png" alt="Taha Zarif — Systems & Robotics Software Engineering" width="100%">
</p>

# Taha Zarif

### Systems & Robotics Software Engineer
**C++ / ROS 2 · Embedded / Zephyr RTOS · Privacy-First Windows Systems · Verification-Driven Engineering**

I build systems software across robotics, embedded/real-time systems, and privacy-aware desktop automation. I focus on deterministic behavior, bounded resources, explicit failure handling, reproducible verification, CI, and hardware/software debugging.

My public engineering work includes **11 merged upstream pull requests across 7 external repositories**, including **Zephyr RTOS, Apache NuttX, Robotics Toolbox for Python, Motrix**, and safety-oriented robotics/localization projects.

[**Resume**](./RESUME.md) · [**Engineering Evidence**](./EVIDENCE.md) · [**LinkedIn**](https://www.linkedin.com/in/taha-zarif-bba94b397/) · [**Repositories**](https://github.com/tahazarif10?tab=repositories)

## Open-Source Engineering

**11 upstream pull requests merged across 7 external repositories.** Selected work:

- **[Zephyr RTOS #118971](https://github.com/zephyrproject-rtos/zephyr/pull/118971)** — added `native_sim` coverage for public Bluetooth identity-management APIs through the real host path with a fake HCI driver, covering create/reset/delete/get behavior without mocking host internals.
- **[Robotics Toolbox for Python #667](https://github.com/petercorke/robotics-toolbox-python/pull/667)** — fixed numerical IK convergence ordering so an already-converged initial configuration is accepted before a potentially singular solver update; added regression coverage.
- **[Motrix #2138](https://github.com/agalwood/Motrix/pull/2138)** — restored the macOS Menu Bar Only Dock-state invariant after main-window dismissal and added focused regression coverage.
- **[GPS-Denied UAV Navigation #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28)** — preserved fail-closed localization behavior so invalid/non-finite TDOA data cannot raise confidence or claim a recovery/fusion source.
- **[DQ QuestionBank Core #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) / [#128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128)** — added editor draft autosave/crash recovery and fixed a subtle table round-trip data-preservation bug for ragged and trailing-empty rows.

Additional merged work: **[Zephyr #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636)** · **[Robotics Toolbox #644](https://github.com/petercorke/robotics-toolbox-python/pull/644)** · **[Motrix #1885](https://github.com/agalwood/Motrix/pull/1885)** · **[Apache NuttX #20147](https://github.com/apache/nuttx/pull/20147)** · **[Orchestrator MCP #11](https://github.com/crAK1644/orchestrator-mcp/pull/11)**.

**Zephyr:** two upstream PRs are merged. An application for the **Zephyr Technical Contributor** badge has been submitted and is pending review; it is not presented here as an earned credential until formally approved.

## Featured Engineering

- **[Robotics Control Core](https://github.com/tahazarif10/robotics-control-core)** — C++20 differential-drive planning/control library with occupancy-grid A*, collision-aware path shaping, PID, interpolated-lookahead pure pursuit, SE(2) odometry, deterministic benchmarks, multi-compiler CI, sanitizers, CodeQL, and installable CMake packaging.
- **[Local AI Desktop Copilot](https://github.com/tahazarif10/local-ai-desktop-copilot)** — privacy-first Windows systems foundation with identity-first privacy gates, RAM-only sensing, capability-gated UI Automation, bounded orchestration, provider-isolation measurement, and deterministic failure/recovery verification.
- **[ROS 2 Autonomous Mobile Robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)** — ROS 2 Jazzy/Nav2 integration with lifecycle control, TF/QoS contracts, deterministic rosbag2 replay, diagnostics, fault injection, missing-TF fail-closed behavior, and isolated integration tests.
- **[Embedded RTOS Sensor Hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)** — C/Zephyr RTOS sensor hub with static threads, bounded queues, synchronization, supervision, bounded retry/recovery, fault injection, and **12/12** checked-in Twister cases on `native_sim`.

Additional work: **[Industrial Vision Inspector](https://github.com/tahazarif10/industrial-vision-inspector)** — deterministic Python/OpenCV/PyTorch inspection pipeline with reproducible dataset preparation and evidence-scoped evaluation.

## Industrial / Real-World Engineering

Hands-on work includes Python/PyQt control software with **Delta AS228T-series PLCs over Modbus TCP**, pulse/direction servo motion for CNC saw/clamp axes, millimetre-to-pulse conversion, homing/jog/state logic, limits, alarms, safety interlocks, and physical PLC/I/O debugging.

## Background

Grade 10 student in Mashhad, Iran. **4th place — FIRA RoboWorld Cup 2024**, São Luís, Brazil, with **Kamaan Shahriar Iran** in Cliff Hanger Lightweight (U14). Evidence and additional competition history are documented in [EVIDENCE.md](./EVIDENCE.md#robotics-competition-experience--fira).

## Core Stack

**C · C++20 · Python · C#/.NET · ROS 2 · Nav2 · Zephyr RTOS · OpenCV · PyTorch · Linux · CMake · GitHub Actions · CodeQL · ASan/UBSan · PLC/Modbus/Servo Automation**

---

Performance, safety, hardware, and credential claims are intentionally scoped. Reproducibility links, CI evidence, benchmark boundaries, and the complete upstream contribution record are maintained in [**Engineering Evidence**](./EVIDENCE.md).
