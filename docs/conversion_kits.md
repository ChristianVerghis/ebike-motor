# Conversion-kit research

Consolidated from design chats 2026-09-02 / 09-03. Question asked: should a bought kit come before the DIY axial-flux motor, and which kits actually teach anything toward the build? Prices USD as checked 2026-09-02.

## Verdict

**Yes, buy a kit first, but a bare direct-drive rear hub run from our own VESC, not a bolt-on booster.** Everything except the hub itself (battery, VESC, torque arm, throttle, e-brakes, wiring, donor bike) moves straight onto the DIY motor later. Proposed as **Phase 0** in PLAN.md (see below) — not yet confirmed, nothing bought.

## Category 1 — bolt-on speed boosters (rejected)

Chain/roller or friction drives with a sealed proprietary controller and a small battery. Teach cable routing and "what 450 W feels like", nothing about motors, FOC, hubs, or regen. Nothing carries forward.

| Product | Price | Notes |
|---|---|---|
| [Flipsky Z9](https://flipsky.net/products/flipsky-z9-bicycle-speed-booster-kit-for-increased-speed-with-48v-5-2ah-9ah-battery-copy) / [Z8](https://flipsky.net/products/z8) | $219–259 | 450 W outrunner, chain + roller on rear wheel, 48 V 5.2 or 9 Ah (≈250 Wh ≈ 12 km assist). [AliExpress spec](https://www.aliexpress.com/i/1005009445601751.html) |
| Rubbee X | ~$500–700 | Friction roller on rear tyre, swappable battery modules |
| Clip | ~$500 | Front-wheel friction drive clamped to fork |
| Skarper | ~$1,500 | Drives a special disc-brake rotor; closed system |
| Add-e, Velogical | $800–1,500 | European roller drives, well made, sealed |

Shared problems: slips in the wet, 250–500 W, proprietary controller, small battery, no reuse path.

## Category 2 — kits that teach something

Ranked by relevance to the axial-flux build.

### 1. Direct-drive rear hub + our own VESC — **recommended**

- [Leaf Bike 26" 48/52 V 1000 W rear motor wheel](https://www.leafbike.com/products/e-bike-hub-motor/26-inch-48v-52v-1000w-rear-electric-hub-motor-wheel-892.html) — **$210** (was $259). Gearless, 135 mm dropouts, Honeywell halls, double-wall rim, 12 ga spokes, freewheel or cassette, 7.3 kg. The Endless Sphere default for tinkering.
- Bench-only alternative: [HPC Bikes 1000 W 48 V front gearless wheel](https://hpcbikes.com/products/1000w-48v-front-gearless-hub-motor-wheel-26) — $80, front / 100 mm dropouts, so not a daily ride.
- Name-brand option: Bafang G062 direct-drive hub, documented [VESC retrofit thread](https://forums.electricbikereview.com/threads/bafang-g062-1000w-vesc-controller-retrofit.55915/). **Avoid geared hubs (e.g. Bafang G310)**: clutch kills regen and the gearbox hides the motor behaviour we want to study.
- Pair with parts already in SOURCING.md: Flipsky 75100 Pro V2.0 ($98), Grin V7 torque arm (~$58), 48 V 13S 12–15 Ah pack ($250–450), plus throttle / e-brake levers / XT90 / fuse / wire (~$60).

What it teaches: VESC detection, FOC tuning, hall vs sensorless, regen, thermal cutback, torque arms, dropout fit. Same architecture as our motor (radial instead of axial) → teardown benchmark for `sim/sizing.py`. Working commuter in a weekend.

Cost of this route ≈ **$600–900**, of which only the hub ($150–250) is not reused.

### 2. Tongsheng TSDZ2B with open-source firmware — teaches controller firmware

- [Electrify Bike TSDZ2B OSF kit](https://electrifybike.com/collections/tongsheng-motors) from $525 (standard 500 W kit $495; both sold out 2026-09-02). Also [Eco Cycles](https://www.eco-ebike.com/collections/tsdz2-open-source-firmware-osf-products), [Amazon](https://www.amazon.com/Tongsheng-Electric-Conversion-Firmware-Tricycle/dp/B0CZ64S2C3).
- Torque-sensing mid-drive, big OSF community. Learn flashing/tuning firmware, torque-sensor and FOC behaviour. Geared + radial, so little transfers to axial flux; only the battery is reused.

### 3. Bafang BBS02B — least learning, most reliable

- [Luna Cycle BBS02 750 W kit](https://lunacycle.com/bafang-bbs02-750w-middrive-kit/) — $470 without battery. Motor, 25 A controller, chainring, throttle, display. $19.95 programming cable tweaks assist curves; controller is closed. Pick only if a dependable commuter matters more than learning.

## Proposed Phase 0 sequence

1. Donor bike + Leaf direct-drive hub + battery + VESC + torque arm. Ride it.
2. Tear down and measure the hub (or buy the $80 HPC front hub as a bench specimen): magnet dims, turns, Kt, phase R → calibrate `sim/sizing.py`.
3. Build the coreless axial-flux motor on the bench with the VESC already tuned.
4. Swap wheels.

## Side idea — frame-mounted "pancake" using the wheel as rotor (phase-3 candidate)

The clip-on commercial drives use the same mounting idea. Rotor = steel + magnet disc bolted to the **6-bolt disc-brake mount** (~160–200 mm usable OD); stator bracket on the **caliper tabs**, which take torque reaction so no torque arm. Coreless makes it feasible: near-zero attraction, so a 2.5–3 mm gap can float with wheel wobble.

Costs: single-sided (air return ≈ half the field; a steel backing plate recovers it but brings back a few hundred N of attraction), smaller diameter (torque ∝ r²), brake-rotor conflict (adapter carrying both discs, non-drive-side mount, or rim-brake bike), IS/post/flat-mount variety. Expect **150–250 W**, a quarter to a third of the hub motor's torque per kg of magnet. Mechanically easier than the hub (no axle, bearings, lacing, dropout fit); rotor disc, coil former, and potting process all carry over.

## Sources

[Flipsky e-bike collection](https://flipsky.net/collections/e-bike) · [Endless Sphere: VESC and Flipsky for e-bikes](https://endless-sphere.com/sphere/threads/vesc-and-flipsky-for-e-bikes.127684/) · [Bafang G062 VESC retrofit](https://forums.electricbikereview.com/threads/bafang-g062-1000w-vesc-controller-retrofit.55915/)
