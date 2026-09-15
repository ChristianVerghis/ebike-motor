# Plan

## Phase 0 — Design & simulate (weeks 1–4)
- [ ] **Proposed:** buy a direct-drive rear hub kit (Leaf 26" 1000 W, $210) and run it from the 75100 as a rideable stepping stone + teardown benchmark — see [docs/conversion_kits.md](docs/conversion_kits.md). Decide before Order 1
- [x] Pin key dimensions (sim/sizing.py, 2026-09-01): OD 240, 14× 1"×1"×3/8" N42 per rotor at r 92–117, 10 mm stator, 2 mm gaps, 12 coils × 30 t × 2×14 AWG
- [ ] FEMM 2D "unrolled" model at mean radius to confirm sizing.py (expect Bpk ≈ 0.49 T, B1 ≈ 0.46 T, pull ≈ 0.8 kN). Adjust turns ±3 if Kt is off
- [x] 12 coils / 14 poles, 30 turns × 2 strands 14 AWG → Kt ≈ 0.48 Nm/A, ~460 rpm no-load @ 42 V, J ≈ 5 A/mm² at 15 Nm
- [ ] Donor bike: 135 mm QR open dropouts, 26/27.5", disc, Al or steel (Trek FX/Marlin, Sirrus, Giant Escape, Kona Dew, Surly Cross-Check)
- [ ] Thermal budget: coil surface area, copper loss at 15 Nm continuous. Want ≤ 60 W copper loss
- [ ] Order 1: magnets, VESC, wire, epoxy, torque arm (see SOURCING.md)
- [ ] Get SendCutSend quote on cad/back_plate_3mm_steel.dxf; Order 2 mechanical
- [ ] CAD full assembly in FreeCAD/Fusion; export STLs for printed parts

## Phase 1 — Bench motor (weeks 5–12)
- [ ] Print coil-winding jig + coil former; wind 12 coils (count turns, measure R each; reject > 5% outliers)
- [ ] Print stator lay-up mould; lay coils, fibreglass, vacuum-bag/pot in epoxy with 2 embedded NTC thermistors
- [ ] Waterjet/laser 2× steel back plates; glue magnets with printed placement jig; check pole pattern with a Hall sensor
- [ ] Turn aluminium hub carriers; press bearings; assemble on 12 mm axle with shim spacers
- [ ] Spin by hand → check back-EMF waveform on scope (balanced 3-phase, no shorted turns)
- [ ] VESC motor detection; run to 400 rpm; measure Kt with a spring scale + lever arm
- [ ] Dyno-ish: prony brake / bike trainer, log W in vs rpm × torque → efficiency map

## Phase 2 — Wheel integration (weeks 13–18)
- [ ] Machine final spoke-flange carriers (36 h, 3-cross), lace 27.5" rim, true
- [ ] Hollow axle slot for phase + thermistor + hall wires; strain relief
- [ ] Torque arm, dropout fit, cassette clearance
- [ ] 48 V 13S battery pack (buy) + BMS, fuse, key switch, wiring loom
- [ ] VESC tune: current limits, thermal cutback at 90 °C, regen on brake-lever switch
- [ ] Ride tests: flat speed, hill climb, thermal soak, regen feel

## Phase 3 — Commute & iterate (weeks 19–26)
- [ ] 4-week daily-use log (Wh/km, peak coil temp, any noise)
- [ ] Decide: Halbach rotor upgrade and/or laminated cored stator (phase 2 design)

## Timeline
Realistic at evenings + weekends: **6 months** to a ridden commuter, 3 months to first bench spin.

## Risks
- N42 max operating temp 80 °C, coils 2 mm away → VESC thermal cutback at 85 °C, or buy N42H/SH
- Axial pull between rotors ≈ 0.8–1 kN (sizing.py) → shaft/bearing preload design; do not underbuild the hub carrier
- Coreless copper AC loss at 14-pole / 250 rpm ≈ 30 Hz electrical — low, fine. Litz not needed
- Coreless = low inductance; VESC FOC detection is finicky. Detect at half battery voltage, 5–10 A; lower observer gain if it desyncs. Bifilar 30 t helps
- Epoxy glass transition: use ≥ 120 °C Tg resin (e.g. West System 105/206 is NOT enough; use a high-temp laminating epoxy)
- Magnet handling: 28× 1"×1"×3/8" N42 blocks (38 lb pull each) will crush fingers. Print a spacer/handling jig
