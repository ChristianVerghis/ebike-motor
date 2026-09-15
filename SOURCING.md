# Sourcing — first order (Phase 0 long-lead parts)

Prices checked 2026-09-01, USD, US suppliers unless noted. Buy these now; everything else waits for FEMM results.

## Order 1 — magnetics & controller (≈ $450–520) — **confirmed spec 2026-09-01, sim/sizing.py**

| Part | Supplier | Spec / SKU | Qty | Price | Status |
|---|---|---|---|---|---|
| N42 block 1"×1"×3/8" | [Applied Magnets](https://appliedmagnets.com/n42-neodymium-magnets-1-in-x-1-in-x-3-8-in-rare-earth-block/) (= Magnet4Less) | 25.4×25.4×9.5 mm, Ni-Cu-Ni, ~38 lb pull | **32** (28 + 4 spare), one order | $5.35 ea → **$171** | ☐ |
| VESC controller | [Flipsky 75100 Pro V2.0](https://flipsky.net/products/flipsky-75100-pro-v2-0-with-aluminum-pcb-based-on-vesc-for-electric-skateboard-electric-scooter-ebike-speed-controller) | 14–84 V, 100 A cont / 150 A pk, HALL port | 1 | **$98** (button) / $104 (key) | ☐ |
| Magnet wire **14 AWG** 200 °C | [Remington Industries](https://www.remingtonindustries.com/magnet-wire/) polyamide-imide | **5 lb spool (~400 ft)** | 1 | ~$90–110 (confirm on site) | ☐ |
| High-temp laminating epoxy | [Fibre Glast System 3000](https://www.fibreglast.com/products/high-temp-epoxy-resin-3000) quart | 309 °F service, post-cure 150 °C | 1 | **$137** | ☐ |
| 14 mm hub-motor axle | [Ebike Solution UK](https://ebikesolution.co.uk/products/m14-ebike-axle-for-hub-motors-kits-for-135mm-replacement) £25, or Amazon/AliExpress "hub motor axle 14mm 135mm" | M14×1.5, flats, wire slot | 1 | $25–35 | ☐ |
| Torque arm | [Grin V7 Regen — **14 mm** variant](https://ebikes.ca/shop/electric-bicycle-parts/torque-arms.html) | clamps flats | 1 | ~$58 | ☐ |

## Order 2 — mechanical (≈ $150–250, after the axle arrives)

| Part | Supplier | Spec | Qty | Price | Status |
|---|---|---|---|---|---|
| Steel back plates | [SendCutSend](https://sendcutsend.com/pricing/) — upload `cad/back_plate_3mm_steel.dxf` | 3 mm A36/1008 mild steel | 2 | est. $25–45 (min order $29) | ☐ |
| Bearings | match axle centre Ø: 6003-2RS (17 mm) or 6004-2RS (20 mm) | ABEC-3+ | 4 (+2) | $15–25 | ☐ |
| 6061 round blanks | OnlineMetals / local | Ø250×20 mm ×2, Ø80×40 ×1 | 3 | $60–120 | ☐ |
| Shim set | McMaster / Amazon | ID to match axle, 0.1 / 0.2 / 0.5 mm | 1 set | $12 | ☐ |
| Magnet adhesive | Loctite 326 + 7649 activator, or 3M DP460 | | 1 | $25 | ☐ |
| Fibreglass 200 gsm, Kapton, NTC 10k ×3, M5 hardware | Amazon | | | $50 | ☐ |

## Order 3 — bike side (Phase 2, don't buy yet)
48 V 13S battery ($250–450), throttle + e-brake levers, XT90-S, 40 A fuse, 27.5" 36 h rim + spokes.

## Filament
1 kg PETG (jigs), 1 kg ASA or PA-CF (magnet jig, mould). ~$40.

## Notes
- **Buy all magnets from one lot** — Br variance between lots shows up as torque ripple.
- **Why 1"×1"×3/8" and not 30×10×5:** sim/sizing.py — 5 mm magnets across a 15 mm stator give ~0.31 T peak; 9.5 mm magnets across a 10 mm stator give ~0.49 T. 1"×1"×1/2" ($5.89) adds < 1 % — gap-limited, not worth the 430 g. 30×10×10 metric isn't stocked by any supplier found.
- **Peak torque is ~30 Nm at 60 A phase; set VESC motor current max 80 A for ~40 Nm launches.** Cruise (8 Nm, 25 km/h flat) ≈ 45 W copper loss; 15 Nm hill ≈ 150–170 W — minutes, not continuous.
- **Post-cure**: System 3000 wants ~150 °C. Demould first or print the mould in ASA/PA-CF. Never post-cure with magnets present (N42 irreversibly loses field > 80 °C).
- **Axle is 14 mm, not 12** (12 mm hollow axles shear under 80 Nm at the arm per Grin's testing). Grin V7 comes in a 14 mm variant.
- **Low inductance**: coreless = tens of µH. Expect to raise VESC switching frequency and re-run detection; FOC current ripple is the known coreless gotcha.
- Flipsky 75100 has no dedicated motor-temp port; wire the coil NTC to the VESC's ADC/temp input (documented on VESC forum) or read it via a $5 module. Trampa VESC 6 MkVI ($250+) is the upgrade path if the Flipsky's FOC is noisy at low rpm.
- Magnet Expert ships from the UK; for US delivery K&J or Applied Magnets are faster. Verify exact 30×10×5 or adjust the placement jig to whatever size you get — the design tolerates 25–32 mm × 8–12 mm × 4–6 mm with a re-run of FEMM.
- The 2.5 lb wire spool is comfortably enough for 12 coils × 45 turns plus rewinds.

## Order 0 (proposed, undecided) — stepping-stone hub kit, see docs/conversion_kits.md

| Part | Supplier | Spec | Qty | Price | Status |
|---|---|---|---|---|---|
| Direct-drive rear hub in 26" wheel, motor only | [Leaf Bike 48/52 V 1000 W](https://www.leafbike.com/products/e-bike-hub-motor/26-inch-48v-52v-1000w-rear-electric-hub-motor-wheel-892.html) | gearless, 135 mm, halls, 7.3 kg | 1 | $210 | ☐ |
| Bench teardown specimen (optional) | [HPC 1000 W front gearless wheel](https://hpcbikes.com/products/1000w-48v-front-gearless-hub-motor-wheel-26) | 100 mm front | 1 | $80 | ☐ |
| Throttle, e-brake levers, XT90, fuse, wire | Amazon / ebikes.ca | | | ~$60 | ☐ |

