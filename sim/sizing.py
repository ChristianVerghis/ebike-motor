"""Analytical sizing of a coreless dual-rotor axial-flux PM motor.
1-D magnetic circuit with back iron on both rotors + empirical leakage factor.
Good to ~10-15 %; FEMM refines. Run: python3 sim/sizing.py
"""
import math
mu0 = 4e-7*math.pi
Br_N42 = 1.30          # T, remanence N42 @ 20C (N42H similar)
rho_cu = 1.72e-8*(1+0.0039*80)  # ohm.m at 100 C
V_bat = 48.0; V_min = 42.0      # 13S nominal / near-empty
Ro, Ri = 0.120, 0.090           # magnet annulus (m)
P = 14                          # poles per rotor
Ncoil = 12
r_m = (Ro+Ri)/2; L_act = Ro-Ri

def B_gap(hm, g_total, cov):
    """hm: magnet thickness per rotor (m); g_total: rotor face to rotor face (m); cov: pole arc coverage"""
    # two magnets in series with the whole non-magnetic gap; back iron ideal
    B1d = Br_N42 * (2*hm) / (2*hm + g_total)
    # leakage/fringing: pole pitch vs total gap (Carter-like empirical)
    tau = 2*math.pi*r_m/P
    k_leak = 1 - 0.5*(g_total+2*hm)/tau          # crude, ok for tau/g > 2
    Bpk = B1d*max(k_leak,0.3)
    # fundamental of a trapezoid-ish wave: B1 = (4/pi)*Bpk*sin(cov*pi/2)
    B1 = 4/math.pi*Bpk*math.sin(cov*math.pi/2)
    return Bpk, B1

def motor(hm, t_stator, gap, cov, turns, strands, awg=18, I_pk=60, I_cont=None):
    g_total = t_stator + 2*gap
    Bpk, B1 = B_gap(hm, g_total, cov)
    # torque: T = (3/2)... use per-coil BLI at both active sides of each coil, fundamental winding factor for 12/14 = 0.933
    kw = 0.933
    # flux linkage per phase fund: lambda = (Ncoil/3)*turns*B1*L_act*(tau_coil ~ 2 r sin(pi/Ncoil)) ... use standard axial flux:
    # Torque = (pi/8)*kw*B1*A_rms_lin... simpler & standard: T = 3/2 * p * psi_pm * Iq, psi_pm from coil flux
    A_coil = L_act * 2*r_m*math.sin(math.pi/Ncoil)   # coil span area at mean radius
    psi_coil = B1*A_coil*turns*kw*(2/math.pi)          # avg link of sinusoidal field over one coil span
    psi_ph = psi_coil*(Ncoil/3)
    Kt = 1.5*(P/2)*psi_ph                              # Nm per A (peak phase current, sinusoidal)
    Ke = Kt                                            # V.s/rad (peak line-neutral / omega_mech)
    Vll_peak_per_krpm = Ke*(2*math.pi*1000/60)*math.sqrt(3)
    rpm_noload = V_min*0.95/(Vll_peak_per_krpm/1000)   # VESC ~95 % modulation
    # copper
    d = 0.127e-3*92**((36-awg)/39); a_str = math.pi*d*d/4; a_cu = a_str*strands
    turn_len = 2*L_act + 2*(2*r_m*math.sin(math.pi/Ncoil)) + 0.02
    R_coil = rho_cu*turns*turn_len/a_cu
    R_ph = R_coil*(Ncoil/3)
    T_pk = Kt*I_pk
    I_cont = I_cont or 15/Kt
    P_cu = 1.5*R_ph*I_cont**2                          # 3-phase loss with peak-current convention
    J_cont = I_cont/math.sqrt(2)/a_cu/1e6
    # fill check: coil window at inner radius
    slot_w_in = 2*Ri*math.sin(math.pi/Ncoil)           # 47 mm at Ri
    cu_area = turns*a_cu*2                             # both sides of coil
    fill = cu_area/(slot_w_in*0.6*t_stator)           # ~60 % of slot width usable, whole stator thickness
    # rotor pull ~ B^2 A/(2mu0) at mid gap (both sides attract each other through the stator)
    F = Bpk**2*(math.pi*(Ro**2-Ri**2))*cov/(2*mu0)
    return dict(hm=hm*1e3, t_st=t_stator*1e3, Bpk=Bpk, B1=B1, Kt=Kt, T_pk=T_pk, rpm_nl=rpm_noload,
                R_ph=R_ph, I_cont=I_cont, P_cu=P_cu, J=J_cont, fill=fill, F_kN=F/1e3, turns=turns, strands=strands)

def row(m):
    return (f"hm={m['hm']:4.0f} st={m['t_st']:4.0f}  Bpk={m['Bpk']:.2f} B1={m['B1']:.2f}  Kt={m['Kt']:.3f} "
            f"Tpk={m['T_pk']:4.1f}Nm  nl={m['rpm_nl']:4.0f}rpm  Rph={m['R_ph']*1e3:4.0f}mΩ  "
            f"Icont={m['I_cont']:4.1f}A Pcu={m['P_cu']:4.0f}W J={m['J']:4.1f}A/mm²  fill={m['fill']:.2f}  F={m['F_kN']:.1f}kN  N={m['turns']}x{m['strands']}")

print("=== magnet thickness / stator thickness sweep (cov 0.65, 2 mm gaps) ===")
for hm in (5e-3, 8e-3, 10e-3):
    for ts in (8e-3, 10e-3, 12e-3, 15e-3):
        Bpk,B1 = B_gap(hm, ts+4e-3, 0.65)
        print(f"hm={hm*1e3:2.0f} mm  stator={ts*1e3:2.0f} mm  Bpk={Bpk:.2f} T  B1={B1:.2f} T")
print()
print("=== candidate designs (target: Tpk≥40 Nm @60 A, no-load ≥ 330 rpm @42 V, J≤12 A/mm², fill≤0.8) ===")
for hm,ts,N,s in [(5e-3,15e-3,45,2),(10e-3,10e-3,35,2),(10e-3,10e-3,30,2),(10e-3,12e-3,32,3),(8e-3,10e-3,34,2)]:
    print(row(motor(hm,ts,2e-3,0.65,N,s)))

print()
print("=== copper-heavy candidates: cruise 8 Nm (25 km/h flat), hill 15 Nm (minutes), peak 40 Nm ===")
for hm,ts,N,s,awg in [(10e-3,10e-3,30,4,18),(10e-3,12e-3,30,5,18),(10e-3,12e-3,30,2,14),(8e-3,10e-3,32,4,18)]:
    m=motor(hm,ts,2e-3,0.65,N,s,awg=awg)
    I8=8/m['Kt']; I15=15/m['Kt']
    P8=1.5*m['R_ph']*I8**2; P15=1.5*m['R_ph']*I15**2
    print(row(m)); print(f"      cruise 8Nm: I={I8:.1f}A Pcu={P8:.0f}W   hill 15Nm: Pcu={P15:.0f}W   awg={awg}")
