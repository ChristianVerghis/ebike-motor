# Bill of materials & budget

Prices are rough USD, mid-2026, hobby quantities. Ranges cover cheap-AliExpress vs. reputable-supplier.

## A. Motor — magnetics & winding

| # | Part | Spec | Qty | Est. | Notes |
|---|---|---|---|---|---|
| 1 | NdFeB block magnets | **N42 1"×1"×3/8"** (25.4×25.4×9.5 mm), Ni-Cu-Ni | 28 (+4 spare) | **$171** @ $5.35 | Applied Magnets. 1 per pole, radial. 54 % pole coverage at mean radius. One batch. (Alt: 3× 30×10×10 metric/pole — not stocked anywhere found) |
| 2 | Steel back plates | 3 mm mild steel, Ø240 / Ø130 ring, cad/back_plate_3mm_steel.dxf | 2 | $30–60 | Laser/waterjet. NOT stainless |
| 3 | Magnet wire | **14 AWG** (1.63 mm) enamelled Cu, 200 °C, **5 lb spool** | 1 | ~$90–110 | 12 coils × 30 turns × **2 strands in hand** ≈ 110 m / 360 ft; 14 AWG ≈ 80 ft/lb |
| 4 | Laminating epoxy, high-Tg | e.g. Sicomin SR1710 or MGS L285 w/ slow hardener | 1 kg kit | $60–90 | Tg ≥ 120 °C. Standard West System will soften |
| 5 | Fibreglass cloth | 200 gsm plain weave, 1 m² | 1 | $15 | Stator disc reinforcement |
| 6 | Kapton tape, fibreglass sleeving, PET braid | — | — | $20 | Coil-to-coil insulation, phase leads |
| 7 | NTC thermistors 10k | glass-bead | 3 | $6 | 2 embedded in coils, 1 spare |
| 8 | Magnet adhesive | Loctite 326 + activator, or 3M DP460 | 1 | $25 | Structural, ≥ 120 °C |
| | **Subtotal A** | | | **$420–520** | |

## B. Motor — mechanical

| # | Part | Spec | Qty | Est. | Notes |
|---|---|---|---|---|---|
| 9 | Axle | **14 mm hub-motor replacement axle**, M14×1.5, 10 mm flats, wire slot (Ebike Solution UK £25 / Amazon–AliExpress $20–30) | 1 | $25–35 | Buy first; bearings sized to its centre diameter (usually 17 or 20 mm → 6003 / 6004). 12 mm hollow axles shear < 80 Nm at the torque arm |
| 10 | Bearings | 6003-2RS (17×35×10) or 6004-2RS (20×42×12) — match axle | 4 (+2) | $15–25 | Order after axle arrives |
| 11 | Aluminium rotor/spoke carriers | 6061, Ø250 × 20 mm blanks | 2 | $60–120 | Machined (lathe) or sent to a CNC shop (~$150–250 if outsourced) |
| 12 | Stator hub | 6061 Ø80 × 40 mm | 1 | $15 | Clamps stator disc to axle |
| 13 | Shim spacers | 12 mm ID, 0.1 / 0.2 / 0.5 mm | set | $12 | Sets the two air gaps |
| 14 | Fasteners | M4/M5 stainless cap screws, Nyloc, thread-locker | — | $25 | |
| 15 | Torque arm | **Grin V7 Regen, 14 mm variant** | 1 | ~$58 | Mandatory for regen; clamps axle flats |
| 16 | Spokes + nipples | 13G/14G stainless, cut to length | 36 + spares | $40 | Length depends on flange dims |
| 17 | Rim | 27.5" double-wall, 36 h | 1 | $40–80 | Or re-use the bike's rim |
| | **Subtotal B** | | | **$250–400** | |

## C. Electrical

| # | Part | Spec | Qty | Est. | Notes |
|---|---|---|---|---|---|
| 18 | Controller | VESC 6-class FOC (Flipsky 75100 / Trampa VESC 6 MkVI / MakerX) | 1 | $90–250 | Sensorless FOC + regen; ≥ 60 A |
| 19 | Battery | 48 V 13S 12–15 Ah Li-ion, downtube or rack, with BMS | 1 | $250–450 | Buy, don't build, for a commuter |
| 20 | Throttle + brake-cutoff levers | Hall thumb throttle, e-brake levers | 1 set | $25–40 | |
| 21 | Display / VESC Bluetooth module | for tuning & data | 1 | $20–35 | |
| 22 | Connectors, fuse, key switch, silicone wire | XT90-S, 12 AWG, 40 A fuse | — | $40 | |
| 23 | Hall sensors (optional) | SS41 / 44E ×3 | 3 | $5 | Sensorless FOC usually fine; add if start-up stutters |
| | **Subtotal C** | | | **$430–820** | |

## D. Tools & consumables (if you don't own them)

| # | Item | Est. | Notes |
|---|---|---|---|
| 24 | 3D printer filament (PETG / ASA / PA-CF) | $40 | jigs, formers, moulds, covers |
| 25 | Vacuum bag + pump (or brake bleeder) | $40–80 | For stator lay-up. Optional but improves fill |
| 26 | Digital scale, calipers, multimeter, clamp meter | $60 | |
| 27 | Cheap oscilloscope (or VESC tool) | $50–100 | Back-EMF check |
| 28 | Spring scale / luggage scale | $15 | Kt measurement |
| 29 | Lathe time / CNC outsourcing | $0–250 | Biggest variable |
| | **Subtotal D** | **$200–600** | |

## Budget summary

| Scenario | Total |
|---|---|
| Lean (own tools, AliExpress, machine own carriers, reuse rim) | **~$1,100** |
| Typical | **~$1,600** |
| Comfortable (Trampa VESC, quality battery, outsourced CNC) | **~$2,000+** |

Roughly half is the battery + controller you'd buy for *any* e-bike. Motor-specific spend is ~$500–800.

## What to 3D print

Print **everything that doesn't carry magnetic or structural load**. Print nothing that sits in the flux path or holds the magnets against the 1–2 kN axial pull.

### Print these (PETG or ASA; PA-CF where noted)
- **Coil winding former** — trapezoidal bobbin matching coil pitch; two-part with a bolt so the finished coil pops off
- **Coil bundling jig** — 12-pocket ring that holds finished coils at exact angular pitch during lay-up
- **Stator lay-up mould** — two-part disc mould, 2–3 mm oversize; release wax; epoxy poured inside. Print smooth (0.12 mm layers) or sand
- **Magnet placement jig** — ring with 14 pockets that locates each magnet on the steel plate while adhesive cures. Print in **PA-CF or PETG ≥ 4 walls**; N-S handling spacer combs too
- **Gap-setting gauges** — 2.0 mm comb feelers for checking the gap all round after assembly
- **Rotor covers / dust shields** — thin ASA discs, non-structural
- **Wire exit strain-relief / axle grommet** — TPU
- **Hall sensor carrier** (if used) — small PCB holder at the stator OD
- **VESC enclosure, battery-cable clips, controller mount**
- **Dyno arm and spring-scale bracket** for Kt tests
- **Prototype rotor carriers** — printed carriers are for **dry-fit / geometry check only, without magnets on both rotors**. Full-coverage rotors pull ~3 kN; do not spin on printed carriers

### Do NOT print
- Rotor back plates (must be steel — flux return path)
- Final rotor/spoke carriers (spoke tension + axial magnetic pull + braking load)
- Axle, stator hub clamp, torque arm
- Anything within 3 mm of a coil at continuous ≥ 90 °C without confirming material Tg (PETG softens ~80 °C; ASA ~100 °C; PA-CF ~150 °C)

### Phase-2 note
If you go to laminated cores later, print the **lamination stacking fixture** and **segment bobbins** (PA-CF). The cores themselves stay steel.
