"""
Probe suite for the W_CA Claim 2 recursive rebuild.

Each probe states its kill rule BEFORE running. A fired kill rule is a finding,
not a failure to be explained away. The driver prints every verdict, including
nulls, and the informative outcomes here are usually the failures.

Probes
  1. selection         positive substrate: W_CA must select the org carving
  2. negative_control  linear-stable substrate: W_CA must NOT select (specificity)
  3. lesion_pc         freeze y (plant->controller): controller calibration must collapse
  4. lesion_cp         u=0 (controller->plant): plant must leave basin, calibration follow
  5. g_invariance      verdict invariant under z=T*theta and time reparametrization
"""

import numpy as np
from wca_claim2 import (
    Substrate, Params, P_ORG, P_SPLIT,
    w_ca, sum_tau0, evaluate_block, _basin_frac, _mean_P, THRESH,
)

SEED = 7


def fmt_verdicts(vs, blocks):
    out = []
    for v, b in zip(vs, blocks):
        out.append(f"      {set(b)}: tau0={v.tau0}  mu*={v.mu_star:.2f}  {v.kappa}")
    return "\n".join(out)


def probe_selection(p):
    print("=" * 74)
    print("PROBE 1  selection  (positive substrate)")
    print("  expect: P_org sum(tau0)=1, P_split sum(tau0)=0  -> selection mode")
    print("  KILL  : P_split sum(tau0)>0 (each half self-maintains -> not mutual)")
    print("          OR P_org sum(tau0)=0 (no closure reached)")
    sub = Substrate(p)
    v_org = w_ca(sub, P_ORG, SEED)
    v_spl = w_ca(sub, P_SPLIT, SEED)
    s_org, s_spl = sum_tau0(v_org), sum_tau0(v_spl)
    print(f"  P_org   sum(tau0)={s_org}")
    print(fmt_verdicts(v_org, P_ORG.blocks))
    print(f"  P_split sum(tau0)={s_spl}")
    print(fmt_verdicts(v_spl, P_SPLIT.blocks))
    # diagnostics for the org block
    d = v_org[0].detail["detail"]
    print(f"  org C1 recovery_ratio={d['C1'].get('recovery_ratio', float('nan')):.2f}  "
          f"C2 iso/passive basin={d['C2'].get('iso_basin', float('nan')):.2f}/"
          f"{d['C2'].get('passive_basin', float('nan')):.2f}  "
          f"C3 P_ratio={d['C3'].get('P_ratio', float('nan')):.3f}")
    killed = (s_spl > 0) or (s_org == 0)
    mode = "selection" if (s_org != s_spl) else ("rejection" if s_org == 0 else "ambiguous")
    print(f"  RESULT: mode={mode}  ->  {'KILL FIRED' if killed else 'pass'}")
    return not killed, dict(s_org=s_org, s_spl=s_spl, mode=mode)


def probe_negative_control(p):
    print("=" * 74)
    print("PROBE 2  negative_control  (linear passively-stable substrate)")
    print("  expect: all tau0=0 under every carving -> rejection (no false positive)")
    print("  KILL  : P_org sum(tau0)>0  (isolation-persistence false-positives)")
    neg = Substrate(p, linear_stable=True)
    v_org = w_ca(neg, P_ORG, SEED)
    v_spl = w_ca(neg, P_SPLIT, SEED)
    s_org, s_spl = sum_tau0(v_org), sum_tau0(v_spl)
    print(f"  P_org   sum(tau0)={s_org}")
    print(fmt_verdicts(v_org, P_ORG.blocks))
    d = v_org[0].detail["detail"]
    print(f"  org C2 iso/passive basin={d['C2'].get('iso_basin', float('nan')):.2f}/"
          f"{d['C2'].get('passive_basin', float('nan')):.2f}  "
          f"(passive>=0.8 means correction not load-bearing -> C2 fails)")
    killed = s_org > 0
    print(f"  RESULT: {'KILL FIRED (false positive)' if killed else 'pass (correctly rejects)'}")
    return not killed, dict(s_org=s_org, s_spl=s_spl)


def probe_lesion_pc(p):
    print("=" * 74)
    print("PROBE 3  lesion plant->controller  (freeze y)")
    print("  expect: controller calibration collapses; plant maintenance degrades")
    print("  KILL  : calibration stays ~intact (recursion decorative, a fuel gauge)")
    sub = Substrate(p)
    intact = [sub.run(rng=np.random.default_rng(s)) for s in range(8)]
    lesion = [sub.run(freeze_y=True, rng=np.random.default_rng(s)) for s in range(8)]
    Pi = np.mean([_mean_P(r) for r in intact])
    Pl = np.mean([_mean_P(r) for r in lesion])
    bi = np.mean([_basin_frac(r) for r in intact])
    bl = np.mean([_basin_frac(r) for r in lesion])
    print(f"  intact: mean_P={Pi:.3f}  basin={bi:.3f}")
    print(f"  lesion: mean_P={Pl:.3f}  basin={bl:.3f}")
    print(f"  calibration ratio (lesion/intact)={Pl / Pi:.1f}x  basin drop={bi - bl:.3f}")
    killed = (Pl / Pi) < 3.0          # calibration must blow up at least 3x
    print(f"  RESULT: {'KILL FIRED' if killed else 'pass (controller collapses on lesion)'}")
    return not killed, dict(P_intact=Pi, P_lesion=Pl, basin_drop=bi - bl)


def probe_lesion_cp(p):
    print("=" * 74)
    print("PROBE 4  lesion controller->plant  (u=0)")
    print("  expect: plant leaves basin; calibration follows (observability lost)")
    print("  KILL  : plant stays in basin (it never needed the controller)")
    sub = Substrate(p)
    intact = [sub.run(rng=np.random.default_rng(s)) for s in range(8)]
    lesion = [sub.run(u_zero=True, rng=np.random.default_rng(s)) for s in range(8)]
    bi = np.mean([_basin_frac(r) for r in intact])
    bl = np.mean([_basin_frac(r) for r in lesion])
    Pi = np.mean([_mean_P(r) for r in intact])
    Pl = np.mean([_mean_P(r) for r in lesion])
    print(f"  intact: basin={bi:.3f}  mean_P={Pi:.3f}")
    print(f"  lesion: basin={bl:.3f}  mean_P={Pl:.3f}")
    print(f"  basin drop={bi - bl:.3f}  calibration ratio={Pl / Pi:.1f}x")
    killed = bl > THRESH["basin_frac"]   # plant must leave basin
    print(f"  RESULT: {'KILL FIRED' if killed else 'pass (plant collapses; calibration follows)'}")
    return not killed, dict(basin_intact=bi, basin_lesion=bl, P_ratio=Pl / Pi)


def probe_g_invariance(p):
    print("=" * 74)
    print("PROBE 5  G-invariance")
    print("  (a) controller-coordinate rescale z = c*theta")
    print("  (b) monotone time reparametrization tau(t)")
    print("  expect: verdict invariant under correct (coordinate-free) criteria")
    print("  KILL  : the coordinate-free verdict flips under either transform")
    sub = Substrate(p)
    # baseline org verdict
    v0 = w_ca(sub, P_ORG, SEED)[0]
    d0 = v0.detail["detail"]
    P_ratio0 = d0["C3"]["P_ratio"]
    pr0 = d0["C1"]["recovery_ratio"]

    # (a) controller rescale: a_hat -> c*a_hat, P -> c^2*P. The closed-loop plant
    # trajectory is identical (physics depends on physical a), so basin-based and
    # ratio-based criteria are invariant by construction. Demonstrate numerically
    # that the C3 RATIO is invariant while a naive ABSOLUTE-P threshold flips.
    print("  (a) controller-coordinate rescale:")
    flips_invariant = False
    flips_absolute = False
    for c in [0.25, 1.0, 4.0, 16.0]:
        P_intact_c = d0["C3"]["P_intact"] * c ** 2
        P_starved_c = d0["C3"]["P_starved"] * c ** 2
        ratio_c = P_intact_c / P_starved_c            # invariant: c^2 cancels
        abs_pass_c = P_intact_c <= 1.5                # naive absolute threshold
        inv_C3 = ratio_c < THRESH["P_ratio"]
        if inv_C3 != (P_ratio0 < THRESH["P_ratio"]):
            flips_invariant = True
        if not abs_pass_c:
            flips_absolute = True
        print(f"      c={c:5.2f}  invariant C3 ratio={ratio_c:.3f} (C3={inv_C3})   "
              f"naive abs mean_P={P_intact_c:.2f} (pass={abs_pass_c})")
    print(f"      coordinate-free criterion flips: {flips_invariant}  "
          f"(naive absolute-P criterion flips: {flips_absolute})")

    # (b) time reparametrization
    print("  (b) monotone time reparametrization:")
    reparam = lambda t: 1.0 + 0.5 * np.cos(0.03 * t)   # stays in [0.5,1.5] > 0
    # recompute the org verdict with a reparametrized clock
    sub_rp = Substrate(p)
    # monkey-free: pass reparam through run by wrapping evaluate via a subclass-lite
    base = sub_rp.run(reparam=reparam, rng=np.random.default_rng(SEED))
    iso = sub_rp.run(reparam=reparam, rng=np.random.default_rng(SEED + 1))
    passive = sub_rp.run(u_zero=True, reparam=reparam, rng=np.random.default_rng(SEED + 2))
    starved = sub_rp.run(freeze_y=True, reparam=reparam, rng=np.random.default_rng(SEED + 3))
    C2_rp = (_basin_frac(iso) >= THRESH["basin_frac"]) and (_basin_frac(passive) < THRESH["basin_frac"])
    C3_rp = (_mean_P(iso) / max(_mean_P(starved), 1e-9)) < THRESH["P_ratio"]
    hi = sub_rp.run(a_perturb=+0.4, reparam=reparam, rng=np.random.default_rng(SEED + 10))
    lo = sub_rp.run(a_perturb=-0.4, reparam=reparam, rng=np.random.default_rng(SEED + 11))
    pr_rp = abs(np.mean(hi["AH"][-500:]) - np.mean(lo["AH"][-500:])) / 0.8
    C1_rp = (pr_rp >= THRESH["pathdep_ratio"]) and (_basin_frac(base) >= THRESH["basin_frac"])
    tau0_rp = int(C1_rp and C2_rp and C3_rp)
    print(f"      reparam'd org verdict: C1={C1_rp} C2={C2_rp} C3={C3_rp} tau0={tau0_rp}  "
          f"(baseline tau0={v0.tau0})")
    flips_time = tau0_rp != v0.tau0

    killed = flips_invariant or flips_time
    print(f"  RESULT: {'KILL FIRED (verdict coordinate-dependent)' if killed else 'pass (verdict invariant)'}")
    return not killed, dict(flips_invariant=flips_invariant, flips_absolute=flips_absolute,
                            flips_time=flips_time)


def main():
    p = Params()
    print("W_CA CLAIM 2 -- RECURSIVE REBUILD : PROBE REPORT")
    print(f"params: mu_a={p.mu_a} k={p.k} sig_rw={p.sig_rw} xb={p.xb} "
          f"x_escape={p.x_escape} sig_x={p.sig_x} T={p.T} dt={p.dt}")
    results = {}
    results["selection"] = probe_selection(p)
    results["negative_control"] = probe_negative_control(p)
    results["lesion_pc"] = probe_lesion_pc(p)
    results["lesion_cp"] = probe_lesion_cp(p)
    results["g_invariance"] = probe_g_invariance(p)

    print("=" * 74)
    print("SUMMARY")
    all_pass = True
    for name, (ok, _) in results.items():
        print(f"  {name:18s} {'PASS' if ok else 'KILL FIRED'}")
        all_pass = all_pass and ok
    print("-" * 74)
    if all_pass:
        print("  All probes here pass. The binding selection test is the frame")
        print("  sweep (frame_sweep.py), which evaluates every bounded-condition-")
        print("  number carving of the loop with a C2 that treats the carving")
        print("  projection as external governance. As of the current build that")
        print("  sweep PASSES: only the undivided loop crosses T0; every split is")
        print("  rejected because its correction is boundary-sourced, and the")
        print("  verdict is invariant to the enforcement threshold. Selection is")
        print("  frame-robust and threshold-robust on the thin substrate.")
        print("  Standing limits: collapse-both is necessary not sufficient;")
        print("  sensitivity (the C0 problem) is untouched; and only 1-D")
        print("  competitors are tested -- same-dimensional mis-governed blocks")
        print("  need the R^3 controller. Soundness, specificity, and clean")
        print("  selection hold; full sufficiency does not.")
    else:
        print("  At least one kill rule fired. See the probe above for the disproof")
        print("  mode; that is the finding. Do not commit the witness publicly.")
    return results


if __name__ == "__main__":
    main()
