"""
R^3 W_CA battery, GATED on the direct rate-arm lesion degrading the intact full
controller (Charles's precondition). The battery does not run unless the gate
passes AND the specificity control confirms the degradation is regime-tracking
rather than generic fragility.
"""
import numpy as np
from dataclasses import replace
from wca_claim2_r3 import (SubstrateR3, ParamsR3, _basin_frac, _mean_P,
                           P_ORG, P_PSEUDO, P_NESTED, P_SPLIT, isolation_flags, THRESH)

# load-bearing operating point: only sig_x raised (plant must visit the high-cpl
# shoulder) plus the new R^3 regime params (sig_r velocity, q_r, rate clamp).
# Inherited damping k=0.20 kept.
P = replace(ParamsR3(), sig_x=0.55, sig_r=0.10, k=0.10, q_r=0.015, r_lo=-0.20, r_hi=0.20)
NS = 12
B = THRESH["basin_frac"]; PR = THRESH["P_ratio"]; PD = THRESH["pathdep_ratio"]


def avg_basin(sub, **kw):
    return np.mean([_basin_frac(sub.run(rng=np.random.default_rng(s), **kw)) for s in range(NS)])
def avg_P(sub, **kw):
    return np.mean([_mean_P(sub.run(rng=np.random.default_rng(s), **kw)) for s in range(NS)])


def gate(sub):
    intact = avg_basin(sub)
    lesion = avg_basin(sub, freeze_rate=True)
    neg = SubstrateR3(P, linear_stable=True)
    n_intact, n_lesion = avg_basin(neg), avg_basin(neg, freeze_rate=True)
    g = (intact >= B) and (lesion < B)
    spec = ((intact - lesion) >= 0.15) and ((n_intact - n_lesion) < 0.10)
    return g and spec, dict(intact=intact, lesion=lesion, neg_drop=n_intact-n_lesion)


def eval_block(sub, block):
    flags = isolation_flags(block)
    has_x, has_ah = "x" in block, "ah" in block
    dim = len(block)
    if dim == 1:
        return 0, dict(reason="single-coordinate: target/governance/budget external")
    if not has_x:
        # controller-only block: stratification mode (least-developed). Viability
        # is calibration, not basin. Report, do not lean on it.
        P_iso = avg_P(sub, **flags)
        P_starved = avg_P(sub, **{**flags, "freeze_y": True})
        C3 = (P_iso / max(P_starved, 1e-9)) < PR
        return int(False), dict(mode="stratification", note="controller-only; not decisive",
                                C3=C3, P_ratio=P_iso/max(P_starved,1e-9))
    # x-containing block: basin-based C2, budget C3, path-dependent C1
    iso_basin = avg_basin(sub, **flags)
    passive_basin = avg_basin(sub, **{**flags, "u_zero": True})
    C2 = (iso_basin >= B) and (passive_basin < B)
    P_iso = avg_P(sub, **flags)
    P_starved = avg_P(sub, **{**flags, "freeze_y": True})
    C3 = (P_iso / max(P_starved, 1e-9)) < PR
    d = 0.4; resid_thresh = PD * d   # regime-robust C1: calibration-recovery
    def late_terr(off):
        v = []
        for s in range(NS):
            rr = sub.run(ahat0=P.mu_a + off, rng=np.random.default_rng(300 + s), **flags)
            v.append(np.abs(rr["AH"] - rr["A"])[-500:].mean())
        return np.mean(v)
    base_terr = late_terr(0.0); hi = late_terr(+d); lo = late_terr(-d)
    resid = max(hi, lo) - base_terr
    base_basin = avg_basin(sub, **flags)
    C1 = (resid < resid_thresh) and (base_basin >= B)
    tau0 = int(C1 and C2 and C3)
    return tau0, dict(iso_basin=iso_basin, passive_basin=passive_basin, C1=C1, C2=C2, C3=C3,
                      P_ratio=P_iso/max(P_starved,1e-9), resid=resid)


def run_partition(sub, part):
    print(f"  {part.name}:")
    s = 0
    for blk in part.blocks:
        t, d = eval_block(sub, blk)
        s += t
        extra = ""
        if "iso_basin" in d:
            extra = f"iso={d['iso_basin']:.2f} passive={d['passive_basin']:.2f} C1={int(d['C1'])} C2={int(d['C2'])} C3={int(d['C3'])}"
        elif "reason" in d: extra = d["reason"]
        elif "mode" in d:   extra = f"{d['mode']}: C3={int(d['C3'])} (not decisive)"
        print(f"    {set(blk)}: tau0={t}  {extra}")
    return s


def main():
    sub = SubstrateR3(P)
    print("R^3 W_CA BATTERY (gated)")
    print(f"params: sig_x={P.sig_x} sig_r={P.sig_r} k={P.k} q_r={P.q_r} rclamp=±{P.r_hi}")
    print("="*74)
    ok, g = gate(sub)
    print(f"GATE (direct rate lesion vs intact full):")
    print(f"  intact basin={g['intact']:.3f}  rate-lesion basin={g['lesion']:.3f}  "
          f"neg-control drop={g['neg_drop']:.3f}")
    print(f"  -> {'PASS: rate arm load-bearing, battery runs' if ok else 'BLOCKED: rate decorative, battery forbidden'}")
    if not ok:
        print("BATTERY NOT RUN."); return
    print("="*74)
    s_org    = run_partition(sub, P_ORG)
    s_pseudo = run_partition(sub, P_PSEUDO)
    s_nested = run_partition(sub, P_NESTED)
    s_split  = run_partition(sub, P_SPLIT)
    # negative control: full battery on linear-stable substrate must reject org
    neg = SubstrateR3(P, linear_stable=True)
    s_negorg = run_partition(neg, P_ORG)
    print("="*74)
    print(f"sum(tau0): org={s_org} pseudo={s_pseudo} nested={s_nested} split={s_split} | neg-org={s_negorg}")
    win = (s_org == 1) and (s_pseudo == 0) and (s_negorg == 0)
    print("VERDICT:", "SELECTION on the same-dimensional carve -- org crosses, pseudo-unit rejected, neg rejects"
          if win else "NOT a clean same-dimensional selection (see blocks above)")

if __name__ == "__main__":
    main()
