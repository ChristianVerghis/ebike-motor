# ebike-motor

**A from-scratch coreless dual-rotor axial-flux rear hub motor for a commuter e-bike, sized analytically and driven by a VESC.**

## What it is

A design-stage hardware project: a DIY coreless dual-rotor axial-flux (YASA-shaped, no iron) rear hub motor, direct drive, 135 mm dropout. Target ~350 W continuous / 750 W peak, ~40 Nm peak at the wheel, 26–27.5" wheel, 48 V, VESC FOC with regen. The stator is 12 epoxy-potted air coils between two 14-pole NdFeB rotors on steel back plates. A 1-D magnetic-circuit sizing script (`sim/sizing.py`) fixed the geometry and winding on 2026-09-01. Phases 0–3 run design, bench spin, wheel integration and a commute log.

Alongside the motor there is research into off-the-shelf conversion kits (`docs/conversion_kits.md`): which one to buy first as a rideable stepping stone and teardown benchmark, and which ones teach anything toward the build.

Everything in the repo is documentation, analysis and one script. Nothing has been machined or wound yet.

## Why I built it

I wanted to understand an electric machine by designing one end to end rather than buying a hub kit: magnet sizing and the air-gap flux budget, winding a coil count and gauge against copper loss and no-load speed, the axial pull between rotors, magnet temperature limits, epoxy glass transition, and how a low-inductance coreless machine behaves under sensorless FOC. Axial flux was chosen because a bicycle wheel is a large-diameter, low-RPM load, which is exactly the regime a pancake motor prefers, and a coreless stator is buildable on a bench with a 3D printer and no laminations.

## Status

As of 2026-09-15:

- Motor spec confirmed 2026-09-01 with `sim/sizing.py`: geometry, magnet size, winding, Kt/Kv, copper loss and rotor pull are pinned (PLAN.md Phase 0). FEMM cross-check still to do.
- Rotor back-plate DXF drawn (`cad/back_plate_3mm_steel.dxf`); no quote requested.
- Conversion-kit research done (`docs/conversion_kits.md`); a stepping-stone direct-drive hub purchase is proposed but undecided.
- BOM, sourcing and a master components list are priced. **No parts have been purchased.** Everything is design-stage.

## Design summary

Phase-1 targets. Numbers are from `sim/sizing.py` (1-D magnetic circuit with empirical leakage, good to roughly 10–15 %); FEMM is meant to refine them.

| Item | Value | Why |
|---|---|---|
| Topology | Dual-rotor, single coreless stator, no iron | No rotor-stator attraction, forgiving gaps, zero cogging, bench-buildable stator |
| Outer diameter | 240 mm | Torque scales with r²; fits inside 27.5" spokes |
| Poles / coils | 14 poles per rotor / 12 coils (LRK-style, wye) | Winding factor 0.933; ~29 Hz electrical at 250 rpm, no litz needed |
| Magnets | 28× N42 1"×1"×3/8" (25.4×25.4×9.5 mm), one per pole, radial at r 92–117 mm | 9.5 mm magnets across a 10 mm stator give ~0.49 T peak; 5 mm magnets only ~0.31 T |
| Rotor back plates | 3 mm mild steel, OD 240 / ID 130 | Flux return; stainless is non-magnetic |
| Stator | 10 mm epoxy/fibreglass potted disc, 2 mm air gap each side | Thinner stator raises gap flux; 2 mm gaps tolerate wobble |
| Winding | 30 turns × 2 strands 14 AWG per coil | Kt ≈ 0.48 Nm/A, ~460 rpm no-load at 42 V |
| Torque | ~29 Nm at 60 A, ~38 Nm at 80 A phase | VESC motor current max set to 80 A for launches |
| Copper loss | ~45 W at 8 Nm cruise, ~160 W at 15 Nm hill | Hill torque is minutes, not continuous; thermal cutback at 85 °C |
| Axial pull | ~0.8 kN between rotors | Carried rotor-to-rotor through OD bolts, not through the stator |
| Axle | 14 mm hub-motor replacement axle, Grin V7 14 mm torque arm | 12 mm hollow axles shear below 80 Nm at the arm |
| Controller | VESC 6-class FOC (Flipsky 75100 Pro candidate), 48 V 13S | Sensorless FOC and regen; low coreless inductance is the known gotcha |
| Core material | None in phase 1; laminated M270-35A segments in phase 2 | Ferrite saturates at ~0.45 T, rejected; rotors fixed so a cored stator drops in later |
| Magnet pattern | Plain alternating N-S; Halbach deferred | ~80 % of Halbach field, none of the orientation fiddliness |
| Mass | ~5 kg motor (1.3 kg magnets) | Coreless penalty, accepted for phase 1 |

## Layout

| Path | Contents |
|---|---|
| `PLAN.md` | Motor phases 0–3, milestones, timeline, risks |
| `GOALS.md` | Working checklist: Phase 0 design steps, bench motor, wheel and ride, north-star goals |
| `BOM.md` | Motor parts list, budget scenarios, what to 3D print and what not to |
| `SOURCING.md` | Priced supplier list per order (Order 0–3) |
| `build_log.md` | Dated log of decisions and research |
| `project.yml` | Project manifest (name, links, checklist sections) |
| `sim/sizing.py` | Analytical sizing: gap flux, Kt/Kv, copper loss, fill, rotor pull; prints a design sweep |
| `cad/` | `back_plate_3mm_steel.dxf` rotor back plate for laser/waterjet cutting, plus notes |
| `docs/design.html` | Motor diagrams: cross-section, coil/pole plan, exploded stack, bike placement, key numbers |
| `docs/roadmap.html` | Phase 0–3 timeline and where the torque number lands against commercial drives |
| `docs/conversion_kits.md` | Commercial kit research: what to buy first, what teaches anything |
| `docs/components.md` | Master buy list across the motor orders, bike side and tools |

The HTML pages are self-contained (inline SVG, no external assets); open them locally in a browser.

## Run the sizing script

Python 3, standard library only.

```sh
python3 sim/sizing.py
```

It prints a magnet-thickness / stator-thickness sweep of gap flux density, then candidate designs with Kt, peak torque, no-load rpm, phase resistance, continuous current, copper loss, current density, slot fill and rotor pull. Edit the candidate tuples at the bottom of the file to explore other windings.

## License

Code (`sim/`, `cad/`) is released under the MIT License, see [LICENSE](LICENSE). Documentation (`docs/`, this README and the other Markdown files) is licensed under Creative Commons Attribution 4.0 International, see [LICENSE-docs.md](LICENSE-docs.md).
