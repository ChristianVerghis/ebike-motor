# ebike-motor build log

**Update 2026-09-01**: repo scaffolded.

**2026-09-01** — Design converged over a chat session: coreless dual-rotor axial flux (YASA-shaped, no iron) rear hub, plain N-S magnets on steel back plates (Halbach deferred), 12 coil / 14 pole, 240 mm OD, 2 mm gaps, VESC FOC. Ferrite cores rejected (saturate ~0.45 T); laminated M270-35A segments are the phase-2 stator on the same rotors. Wrote PLAN.md (4 phases, ~6 months), BOM.md (~$950–2,000, motor-specific ~$500–800, 3D-print list), docs/design.html (cross-section, coil/pole plan, exploded stack, bike placement).

**2026-09-01 (later)** — Repo created and pushed (ChristianVerghis/ebike-motor). Priced Order 1: Flipsky 75100 Pro V2 $98, Remington 18 AWG 200 °C wire, Fibre Glast System 3000 epoxy $137/qt, Grin V7 regen torque arm $58, N42 30×10×5 magnets ~$2–3.50 ea. Wrote SOURCING.md and cad/back_plate_3mm_steel.dxf (OD 240 / ID 130 / 6×M5 PCD 150) for a SendCutSend quote.

**2026-09-01 (compat review)** — Parts sourced. Cross-check found: (1) 14 single 10 mm magnets/rotor = ~20 % pole coverage → 3 across per pole, 84 + spares; (2) 5 mm magnets over ~19 mm total magnetic gap ≈ 0.4–0.45 T, not 0.6 → FEMM gate: 10 mm stator or stacked magnets; (3) rotor pull ~3 kN not 1–2; (4) N42 Tmax 80 °C → cutback 85 °C / N42H; (5) 2 strands 18 AWG in hand; (6) coreless low inductance vs VESC FOC; (7) System 3000 post-cure vs PETG mould. Budget now ~$1,100–2,200. Donor bike criteria added.

**2026-09-01 (spec confirmed)** — Wrote sim/sizing.py (1-D magnetic circuit + leakage + winding/thermal). Result: 30×10×5 magnets are gap-limited (0.31 T pk with 15 mm stator) → switched to Applied Magnets 1"×1"×3/8" N42 ($5.35, 28 pcs), one per pole radial at r 92–117, stator thinned to 10 mm → 0.49 T pk. 1/2" thick adds <1 %. Winding 30 t × 2×14 AWG (5 lb spool): Kt 0.48, 460 rpm no-load, cruise 45 W Cu, 15 Nm hill 160 W. Peak ~38 Nm at 80 A. Pull ~0.8 kN. Axle → 14 mm hub-motor replacement + Grin V7 14 mm (12 mm hollow shears <80 Nm). Bearings deferred until axle Ø known. DXF jig pins moved to r=85.

## 2026-09-07
- Consolidated conversion-kit research (Flipsky Z8/Z9 rejected; Leaf direct-drive hub + own VESC recommended as Phase 0; TSDZ2 OSF and BBS02 as alternatives) into docs/conversion_kits.md. Phase 0 kit purchase still undecided.

## 2026-09-15
- docs/components.md: master buy list across the motor orders, bike side and tools, ~$1,250–1,750 plus the donor bike.
