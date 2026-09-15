# Components — master buy list

One place for everything we are likely to buy for the axial-flux motor and the bike around it. Prices are the ones checked when each line was researched (USD unless noted). Status: ☐ not ordered · ◐ ordered · ☑ in hand. Detailed supplier notes stay in [SOURCING.md](../SOURCING.md); this is the reference view.

## A. Axial-flux motor — Order 1 magnetics & controller (~$450–520)

| Part | Candidate product | Spec | Qty | Est. | Status |
|---|---|---|---|---|---|
| Magnets | Applied Magnets N42 block 1"×1"×3/8" | 25.4×25.4×9.5 mm Ni-Cu-Ni | 32 | $171 | ☐ |
| Controller | **Flipsky 75100 Pro V2.0** (VESC) | 14–84 V, 100 A cont, hall port | 1 | $98 | ☐ |
| Magnet wire | Remington 14 AWG 200 °C, 5 lb spool | polyamide-imide | 1 | $90–110 | ☐ |
| High-temp epoxy | Fibre Glast System 3000, quart | 150 °C post-cure | 1 | $137 | ☐ |
| Hub axle | M14 hub-motor axle, 135 mm | flats + wire slot | 1 | $25–35 | ☐ |
| Torque arm | Grin V7 regen, 14 mm | | 1 | $58 | ☐ |

## B. Axial-flux motor — Order 2 mechanical (~$150–250, after the axle arrives)

| Part | Candidate | Spec | Qty | Est. | Status |
|---|---|---|---|---|---|
| Steel back plates | SendCutSend, `cad/back_plate_3mm_steel.dxf` | 3 mm mild steel | 2 | $25–45 | ☐ |
| Bearings | 6003-2RS or 6004-2RS to match axle centre | ABEC-3+ | 4 (+2) | $15–25 | ☐ |
| 6061 round blanks | OnlineMetals | Ø250×20 ×2, Ø80×40 ×1 | 3 | $60–120 | ☐ |
| Shim set, magnet adhesive, fibreglass 200 gsm, Kapton, 3× NTC 10k, M5 hardware | McMaster / Amazon / Loctite 326 | | | ~$90 | ☐ |

## C. Bike side — Order 3 (~$400–700)

| Part | Candidate | Spec | Qty | Est. | Status |
|---|---|---|---|---|---|
| Battery | 48 V 13S 12–15 Ah pack with BMS (Hailong) | UL-listed cells preferred | 1 | $250–450 | ☐ |
| Donor bike | used hybrid/MTB, 135 mm QR, disc, 26/27.5" (Trek FX/Marlin, Sirrus, Giant Escape, Kona Dew) | | 1 | $150–400 | ☐ |
| Direct-drive learning hub (optional Phase 0) | Leaf 26" 1000 W rear, motor only | | 1 | $210 | ☐ undecided |
| Teardown specimen (optional) | HPC 1000 W 48 V front gearless wheel | magnet grade/count, lamination stack → calibrate sim/sizing.py | 1 | $80 | ☐ |
| Throttle, e-brake levers, fuse, key switch, wiring loom | Amazon / ebikes.ca | | | $60 | ☐ |

## D. Tools & measurement (~$250)

| Tool | Candidate | Why | Est. | Status |
|---|---|---|---|---|
| Digital calipers with depth rod + feeler gauges | Mitutoyo-clone 150 mm, 0.05–1 mm feelers | air gaps, magnet placement, shim stack | $35 | ☐ |
| Luggage scale + 0.5 m lever arm | 50 kg hanging scale | wheel torque = force × arm → Kt | $15 | ☐ |
| IR thermometer / K-type probe | | coil and shell temperature | $25 | ☐ |
| Wheel truing stand | Park TS-8 class | lacing, rotor runout | $60–80 | ☐ |
| Clamp meter or VESC logging | VESC Tool on phone | phase current → Kt | $0 | ☑ (VESC) |
| Hall-effect probe or phone magnetometer | | rotor pole check | $0–20 | ☐ |
| Crimpers for XT/JST, heat gun | | | $40 | ☐ |
| Sound level meter app | phone | dB at 1 m | $0 | ☑ |

## Totals

| Block | Est. |
|---|---|
| A Axial magnetics + VESC (Order 1) | ~$450–520 |
| B Axial mechanical (Order 2) | ~$150–250 |
| C Bike side (Order 3) | ~$400–700 (+ donor bike) |
| D Tools | ~$250 |
| **All of it** | **~$1,250–1,750** (+ donor bike) |
