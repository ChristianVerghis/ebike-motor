# Goals & working checklist

Working checklist; tick items here. Sections are referenced by project.yml. Details: PLAN.md, SOURCING.md, docs/conversion_kits.md.

## Now — Phase 0 design (PLAN.md Phase 0)
- [ ] FEMM check of sim/sizing.py (Bpk ≈ 0.49 T, pull ≈ 0.8 kN)
- [ ] Decide on the stepping-stone direct-drive hub (Order 0, docs/conversion_kits.md) before Order 1
- [ ] Pick a donor bike: 135 mm QR open dropouts, 26/27.5", disc
- [ ] Order 1: magnets, VESC, wire, epoxy, torque arm
- [ ] SendCutSend quote on cad/back_plate_3mm_steel.dxf; Order 2 mechanical after the axle arrives
- [ ] CAD full assembly; export STLs for the jigs, coil former and stator mould

## Bench motor (PLAN.md Phase 1)
- [ ] Wind 12 coils on the printed former; pot the stator with 2 embedded NTCs
- [ ] Glue 28 magnets on the two back plates with the placement jig; check the pole pattern with a Hall probe
- [ ] Bench spin: 12-coil stator between two 14-pole rotors, > 200 W in, measure Kt / Kv / phase R
- [ ] Prony brake or trainer run: W in vs rpm × torque → efficiency map

## Wheel and ride (PLAN.md Phase 2–3)
- [ ] Lace the 27.5" rim on the final carriers; torque arm; 48 V 13S pack; VESC tune with regen
- [ ] Ride tests: flat speed, hill climb, thermal soak, regen feel

## North-star goals
- [ ] Bench spin of the custom motor
- [ ] Ride: hub laced, 48 V, 25 km/h flat, 350 W sustained < 100 °C
- [ ] Commute 4 weeks daily, regen, no thermal cutouts
- [ ] Phase 2: laminated segmented stator on the same rotors

Non-goals: beating a $150 Bafang on cost or weight.
