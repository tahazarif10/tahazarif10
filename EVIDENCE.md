# Engineering Evidence

This page links resume claims to public, reproducible evidence. Performance claims are scoped to the exact checked-in fixtures that produced them.

## Robotics Control Core — C++20

Repository: [robotics-control-core](https://github.com/tahazarif10/robotics-control-core)

### Implemented

- occupancy-grid A*
- obstacle inflation and collision-safe path shaping
- PID and interpolated-lookahead pure pursuit
- differential-drive forward/inverse kinematics
- SE(2) odometry
- installable CMake package `robotics::control`
- independent `find_package` consumer verification
- GCC / Clang / MSVC CI
- ASan / UBSan
- CodeQL

### Deterministic v0.2 fixture

| Controller | Waypoints | Steps | Travel | Max cross-track | Final error | Collision-free |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| PID baseline | 26 | 545 | 7.158981 m | 0.063708 m | 0.099468 m | yes |
| Pure pursuit + smoothed path | 5 | 479 | 6.905655 m | 0.052827 m | 0.097605 m | yes |

Evidence:

- [v0.2 PR #7](https://github.com/tahazarif10/robotics-control-core/pull/7)
- [multi-compiler CI](https://github.com/tahazarif10/robotics-control-core/actions/runs/34357410837)
- [CodeQL](https://github.com/tahazarif10/robotics-control-core/actions/runs/34357411019)
- [verification record](https://github.com/tahazarif10/robotics-control-core/blob/main/docs/VERIFICATION.md)

These metrics are deterministic regression-fixture evidence, not hardware-performance claims.

## ROS 2 Autonomous Mobile Robot

Repository: [ros2-autonomous-mobile-robot](https://github.com/tahazarif10/ros2-autonomous-mobile-robot)

### v0.2 — lifecycle control adapter

- C++20 ROS 2 lifecycle node
- consumes `robotics-control-core` at a pinned commit instead of copying algorithms
- converts Path + Odometry inputs
- bounded `cmd_vel`
- safe stop for missing, stale, and non-finite input
- invalid-configuration and lifecycle-transition tests

Evidence:

- [PR #6](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/6)
- [merged-main CI #34380715133](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34380715133)

### v0.3 — deterministic Nav2 integration

Checked-in fixture:

- ROS 2 Jazzy / Ubuntu 24.04
- 6 m × 6 m static map
- start `(-2.0, 0.0)`
- goal `(2.0, 0.0)`
- central obstacle blocks the direct path
- NavFn with A* enabled
- Regulated Pure Pursuit
- explicit `map -> odom -> base_link -> base_scan` ownership
- runtime TF verification
- documented QoS contract
- end-to-end `NavigateToPose` assertion
- final fixture position tolerance ≤ 0.20 m
- collision-clear detour required by the test

Evidence:

- [Nav2 fixture PR #8](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/8)
- [TF/QoS PR #9](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/9)
- [final v0.3 merged-main CI #34386081006](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34386081006)
- [verification record](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/blob/main/docs/VERIFICATION.md)

### v0.4 — replay, observability, fault injection, and CI isolation

Status: **complete**

Verified capabilities:

- lifecycle diagnostics with stable stop reasons and input-age observability
- NaN, stale-odometry, and stale-path fault injection with zero-command safe stop
- real rosbag2 sqlite3 generation from a checked-in source fixture
- same bag replayed twice through the live C++ lifecycle adapter with equal canonical outcomes
- checked-in replay contract: **8 messages**, **1.2 s** recorded span, **2.0×** configured pacing
- bounded replay/controller metrics: wall duration, max linear command, command samples, diagnostic samples
- missing-global-TF fault injection: `bt_navigator` stays non-ACTIVE and no non-zero `cmd_vel` is produced
- concurrent ROS test-graph contamination diagnosed from CI and fixed with test namespaces + serialized Nav2 fixtures, without weakening collision assertions

Evidence:

- [diagnostics/fault injection PR #10](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/10)
- [PR #10 merged-main CI #34388363553](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34388363553)
- [rosbag replay PR #11](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/11)
- [rosbag replay merged-main CI #34389798773](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34389798773)
- [missing-TF + metrics PR #12](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/12)
- [PR #12 CI #34394204856](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34394204856)
- [test-graph isolation PR #13](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/pull/13)
- [final v0.4 merged-main CI #34395404807](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/actions/runs/34395404807)
- [repository verification record](https://github.com/tahazarif10/ros2-autonomous-mobile-robot/blob/main/docs/VERIFICATION.md)

These are deterministic software/system-integration results, not physical safety certification or hardware-performance claims.

## Embedded RTOS Sensor Hub — C / Zephyr

Repository: [embedded-rtos-sensor-hub](https://github.com/tahazarif10/embedded-rtos-sensor-hub)

Baseline:

- Zephyr **v4.4.2** pinned by `west.yml`
- Ubuntu 24.04 hosted CI
- `native_sim/native`
- host GNU toolchain
- ztest/Twister

### v0.1 — bounded RTOS core

Verified capabilities:

- five statically defined threads: two producers, consumer, supervisor, telemetry
- bounded `k_msgq` producer/consumer pipeline
- `k_sem` startup synchronization
- `k_mutex` protected shared metrics
- fixed-size messages and no application data-path heap allocation
- software heartbeat watchdog logic
- queue drop and high-watermark accounting
- deterministic vibration-producer stall injection
- stale transition, de-duplication, and recovery tests

Evidence:

- [PR #1](https://github.com/tahazarif10/embedded-rtos-sensor-hub/pull/1)
- [PR CI #34406892562](https://github.com/tahazarif10/embedded-rtos-sensor-hub/actions/runs/34406892562) — success
- [merged-main CI #34407100161](https://github.com/tahazarif10/embedded-rtos-sensor-hub/actions/runs/34407100161) — success
- 5/5 v0.1 ztest cases passed

### v0.2 — acquisition driver boundary and recovery

Status: **complete**

Verified capabilities:

- abstract bus read boundary used by producer threads
- simulated I2C-style temperature transaction: device `0x48`, register `0x00`
- simulated SPI-style vibration transaction: device `0x01`, register `0x10`
- fixed 32-bit little-endian sample decode
- bounded retry policy with transfer/retry/failed-read metrics
- deterministic transient bus-fault injection
- retry recovery and retry-exhaustion tests
- per-sensor sequence-gap rejection with tracking resynchronization
- timestamp-regression rejection without poisoning the accepted baseline
- normal, producer-stall, and bus-fault hosted `native_sim` builds
- **12/12 Twister test cases passed (100%)** on merged `main`

Evidence:

- [Issue #2](https://github.com/tahazarif10/embedded-rtos-sensor-hub/issues/2)
- [PR #3](https://github.com/tahazarif10/embedded-rtos-sensor-hub/pull/3)
- PR head `6339d60f9c82c6f1317fa2e98e51de5013ad85ab`
- [PR CI #34493289155](https://github.com/tahazarif10/embedded-rtos-sensor-hub/actions/runs/34493289155) — success
- merge commit `156903b57eb5525849094a76ca851349a9b0fc34`
- [merged-main CI #34493673687](https://github.com/tahazarif10/embedded-rtos-sensor-hub/actions/runs/34493673687) — success
- [verification record](https://github.com/tahazarif10/embedded-rtos-sensor-hub/blob/main/docs/VERIFICATION.md)

This is native-simulation software evidence. It does not establish physical I2C/SPI timing, electrical behavior, sensor accuracy, ISR latency, hardware-watchdog behavior, or safety certification.

## Robotics Competition Experience — FIRA

### FIRA RoboWorld Cup 2024 — Brazil

- Event: **FIRA RoboWorld Cup 2024**
- Location: **São Luís, Maranhão, Brazil**
- Dates: **5–9 August 2024**
- Participant: **Taha Zarif**
- Team on participant badge: **Kamaan Shahriar Iran**
- Participant-provided physical event badge confirms attendance.
- Reported competition result: **4th place**. A public official ranking entry for this team/result has not yet been located, so the placement is presented as participant-provided rather than independently verified.
- Official AVIS event page: https://events.avisengine.com/events/fira-2024
- Official FIRA event listing: https://firaworldcup.org/

The current AVIS 2024 event page exists, but its public awards page currently returns **"No awards found for this event."** This is consistent with incomplete historical award/badge data and may explain why the 2024 participant badge is absent from the current "My Badges" dashboard. It does not imply non-participation.

### FIRA Iran

Participant badges supplied for two FIRA Iran competitions:

- **Iran 2026 FIRA Open Competition** — team **Kamaan**, **Air Autonomous Race (U19)**, Tehran, 17–21 July 2026. Team record: [AVIS dashboard](https://events.avisengine.com/dashboard/teams/787559c0-d862-45a4-987f-343b13a0690f). Official event: [Iran 2026 FIRA Open Competition](https://events.avisengine.com/events/iran-2026-fira-open-competition).
- **Iran 2025 FIRA Open Competition** — team **Kamaan 3**, **Cliff Hanger Lightweight (U19)**, Tehran, 15–18 April 2025. Team record: [AVIS dashboard](https://events.avisengine.com/dashboard/teams/dcdcb284-d966-4060-9ae5-48a20081cb94). Official event: [Iran 2025 FIRA Open Competition](https://events.avisengine.com/events/iran-2025-fira-open-competition).
- A **3rd-place national FIRA Iran finish** is included in the resume from the participant-provided competition record. The specific public award-page mapping to the supplied team badges has not yet been independently matched, so this page does not attach the placement to a particular league until that result record is identified.

This competition experience is separate from the software benchmark evidence above and is included as hands-on robotics/aerial-robotics participation.

## Upstream Open-Source Contributions

**6 merged upstream pull requests** verified as of 2026-09-10:

1. Robotics Toolbox for Python — [PR #644](https://github.com/petercorke/robotics-toolbox-python/pull/644) — restored missing distance-transform diagonal.
2. Motrix — [PR #1885](https://github.com/agalwood/Motrix/pull/1885) — restored tray left-click window toggling.
3. DQ QuestionBank Core — [PR #127](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/127) — editor draft autosave/crash recovery.
4. DQ QuestionBank Core — [PR #128](https://github.com/wzsisshadiao-crypto/dq-questionbank-core/pull/128) — preserved table-row shape in editor.
5. Orchestrator MCP — [PR #11](https://github.com/crAK1644/orchestrator-mcp/pull/11) — fixed delegated review-synthesis input.
6. GPS-Denied UAV Navigation — [PR #28](https://github.com/smshagor-dev/UVA-GPS-Denied-Navigation-in-Dynamic-Environments/pull/28) — preserved fail-closed handling for invalid TDOA localization data.

### Currently in upstream review

Not counted as merged achievements:

- Zephyr RTOS — [PR #118636](https://github.com/zephyrproject-rtos/zephyr/pull/118636), Bluetooth HCI documentation/API-reference scope clarification; two human approvals have been observed and the PR remains open.
- Robotics Toolbox for Python — [PR #667](https://github.com/petercorke/robotics-toolbox-python/pull/667), numerical IK pre-step convergence fix with regression test; visible CI is green and the PR remains open.

## Industrial Automation Experience

Public profile summary:

- Python/PyQt control software with Delta AS228T-series PLC over Modbus TCP
- servo motion for CNC saw/clamp axes
- millimetre-to-pulse conversion
- homing and jog
- busy/done state handling
- limits, alarms, readiness and safety interlocks
- pulse/direction motion and PLC I/O debugging on physical machinery

These are experience statements, not public hardware benchmarks.
