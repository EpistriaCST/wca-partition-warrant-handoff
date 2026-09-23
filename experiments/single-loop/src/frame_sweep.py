"""
Frame-sweep selection test for W_CA Claim 2.

Upgrades the split-rejection from an asserted single-DOF argument to a COMPUTED
verdict across the whole family of carving frames. The organizational state of
the loop is the (x, a_hat) plane. A carving frame is any invertible basis
B = [e1 e2]; the two blocks are the two new coordinates. Isolating a block means
freezing the complementary coordinate and evolving the substrate under that
constraint (free step, then project back onto the frozen line).

No metric is fixed. Instead the frame family is swept (bounded condition number
to keep every competitor a genuinely distinct carving) and the verdict's
robustness to the frame is the OUTPUT: if every split rejects under every
admissible frame, the scaling never mattered; if some split survives, that is
the frame-relativity finding and it blocks commitment.

CEILING (stated honestly): on this thin (x, a_hat) substrate every competitor is
a 1-D block, so this tests whether the loop survives being constrained to ANY
line through its organizational state. It does not yet reproduce the witness's
discrimination of a same-dimensional, mis-governed block; that needs the R^3
controller (estimate + drift-rate). This sweep closes the "some oblique carving
sneaks through" gap, not the full sufficiency gap.
"""

import numpy as np
from wca_claim2 import Substrate, Params, THRESH, _basin_frac, _mean_P, w_ca, P_ORG

SEED = 7
N_SEEDS = 3


def unit(theta):
    return np.array([np.cos(theta), np.sin(theta)])


def cond_number(B):
    s = np.linalg.svd(B, compute_uv=False)
    return s[0] / s[1]


def run_constrained(sub, B, Binv, block_idx, rng, freeze_y=False, u_zero=False,
                    a_perturb=0.0):
    """Evolve the substrate with the complementary frame-coordinate frozen.
    block_idx in {0,1} is the coordinate left free. Returns reconstructed-x
    basin trace, P trace, a_hat trace."""
    p = sub.p
    n = p.n
    h = p.dt
    x = 0.0
    a = p.mu_a + a_perturb
    a_hat = p.mu_a
    P = p.P0
    # frozen value of the complementary coordinate, from the initial state
    xi0 = Binv @ np.array([x, a_hat])
    j = 1 - block_idx
    xi_j_frozen = xi0[j]

    X = np.empty(n); PP = np.empty(n); AH = np.empty(n)
    in_basin = np.empty(n, dtype=bool)
    enf_j = 0.0   # accumulated free drift of the FROZEN coordinate (projected away)
    enf_i = 0.0   # accumulated free drift of the block's OWN coordinate
    for i in range(n):
        xi_cur = Binv @ np.array([x, a_hat])
        x, a, a_hat, P = sub.step(x, a, a_hat, P, h, rng, freeze_y, u_zero)
        # free-flow drift in frame coordinates, BEFORE projection
        xi_unc = Binv @ np.array([x, a_hat])
        enf_j += abs(xi_unc[j] - xi_j_frozen)
        enf_i += abs(xi_unc[block_idx] - xi_cur[block_idx])
        # project (x, a_hat) back onto the frozen-complement line
        xi_unc[j] = xi_j_frozen
        x, a_hat = B @ xi_unc
        X[i] = x; PP[i] = P; AH[i] = a_hat
        in_basin[i] = abs(x) <= p.x_escape
    # enforcement fraction: share of free motion suppressed by the boundary
    enf_frac = enf_j / (enf_j + enf_i + 1e-12)
    return dict(X=X, P=PP, AH=AH, in_basin=in_basin, enf_frac=enf_frac)


def eval_block_constrained(sub, B, Binv, block_idx):
    """Compute (C1,C2,C3) for one constrained oblique block, averaged over seeds.

    C2 is hardened: internal governance requires that the block's own dynamics,
    not the imposed carving constraint, keep it on its manifold. The projection
    that defines the constrained block is an external governor; if it suppresses
    a non-trivial share of the free motion (enf_frac above tolerance) the
    correction is sourced across the boundary and C2 fails. enf_frac is 0 only
    when the carving line is a dynamical invariant of the loop, i.e. genuine
    internal governance. The undivided org block has no projection (enf_frac=0).
    """
    def avg(metric, **kw):
        vals = []
        for s in range(N_SEEDS):
            r = run_constrained(sub, B, Binv, block_idx,
                                np.random.default_rng(SEED + 100 * s), **kw)
            vals.append(metric(r))
        return np.mean(vals)

    iso_basin = avg(_basin_frac)
    passive_basin = avg(_basin_frac, u_zero=True)
    enf_frac = avg(lambda r: r["enf_frac"])
    P_intact = avg(_mean_P)
    P_starved = avg(_mean_P, freeze_y=True)

    # C2: correction survives isolation, is load-bearing, AND is internally
    # sourced rather than enforced by the carving boundary.
    C2 = ((iso_basin >= THRESH["basin_frac"])
          and (passive_basin < THRESH["basin_frac"])
          and (enf_frac < THRESH["enf_frac"]))
    # C3: information budget self-sustained (invariant ratio)
    C3 = (P_intact / max(P_starved, 1e-9)) < THRESH["P_ratio"]
    # C1: configuration-relative recovery (invariant ratio)
    d = 0.4
    hi = np.mean([np.mean(run_constrained(sub, B, Binv, block_idx,
                  np.random.default_rng(SEED + 10 + s), a_perturb=+d)["AH"][-500:])
                  for s in range(N_SEEDS)])
    lo = np.mean([np.mean(run_constrained(sub, B, Binv, block_idx,
                  np.random.default_rng(SEED + 20 + s), a_perturb=-d)["AH"][-500:])
                  for s in range(N_SEEDS)])
    recov = abs(hi - lo) / (2 * d)
    C1 = (recov >= THRESH["pathdep_ratio"]) and (iso_basin >= THRESH["basin_frac"])

    tau0 = int(C1 and C2 and C3)
    return tau0, dict(iso_basin=iso_basin, passive_basin=passive_basin,
                      enf_frac=enf_frac,
                      P_ratio=P_intact / max(P_starved, 1e-9), recov=recov)


def make_frames():
    """A family of carving frames with bounded condition number. Each frame is a
    basis (e1, e2) of the (x, a_hat) plane. Includes the axis-aligned split."""
    frames = []
    for th1_deg in range(0, 180, 30):
        for dlt_deg in (50, 70, 90, 110, 130):
            e1 = unit(np.radians(th1_deg))
            e2 = unit(np.radians(th1_deg + dlt_deg))
            B = np.column_stack([e1, e2])
            if cond_number(B) <= 5.0:
                frames.append((th1_deg, dlt_deg, B))
    return frames


def main():
    p = Params()
    sub = Substrate(p)
    print("FRAME-SWEEP SELECTION TEST (thin x,a_hat substrate)")
    print("  P_org (undivided loop) must cross T0; every bounded-condition-number")
    print("  split must reject. Survivor = organization-aligned carving only.")
    print("  KILL: any split block tau0=1 (selection frame-relative -> finding)")
    print("  KILL: P_org tau0=0 under the same params (procedure artifact)")
    print("=" * 74)

    # organization-aligned carving (no split)
    v_org = w_ca(sub, P_ORG, SEED)[0]
    print(f"P_org undivided: tau0={v_org.tau0}  mu*={v_org.mu_star:.2f}  {v_org.kappa}")
    if v_org.tau0 == 0:
        print("  KILL FIRED: organization-aligned carving fails -> procedure artifact.")
        return

    frames = make_frames()
    print(f"swept {len(frames)} frames (cond# <= 5)\n")
    survivors = []
    basin_profile = []
    enf_profile = []
    for th1, dlt, B in frames:
        Binv = np.linalg.inv(B)
        for bi in (0, 1):
            tau0, d = eval_block_constrained(sub, B, Binv, bi)
            basin_profile.append((th1, dlt, bi, d["iso_basin"], tau0))
            enf_profile.append((th1, dlt, bi, d["enf_frac"]))
            tag = "  <-- SURVIVES" if tau0 == 1 else ""
            if tau0 == 1:
                survivors.append((th1, dlt, bi, d))
            print(f"  frame th1={th1:3d} delta={dlt:3d} block{bi}: "
                  f"tau0={tau0}  iso_basin={d['iso_basin']:.2f} "
                  f"passive={d['passive_basin']:.2f} enf={d['enf_frac']:.2f} "
                  f"P_ratio={d['P_ratio']:.2f} recov={d['recov']:.2f}{tag}")

    print("=" * 74)
    # is the failure graded (structured) or uniform (trivial)?
    basins = np.array([b for *_, b, _ in basin_profile])
    enfs = np.array([e for *_, e in enf_profile])
    print(f"iso_basin across splits: min={basins.min():.2f} max={basins.max():.2f} "
          f"std={basins.std():.3f}")
    print(f"enf_frac  across splits: min={enfs.min():.2f} max={enfs.max():.2f}  "
          f"(undivided org = 0.00; gap to split-min is the threshold-robust margin)")
    if survivors:
        print(f"RESULT: KILL FIRED -- {len(survivors)} split block(s) survive. "
              f"Selection is frame-relative on this substrate; do not commit.")
    else:
        print("RESULT: pass -- every bounded-condition-number split rejects; only the")
        print("  organization-aligned carving crosses T0. Splits fail C2 because the")
        print("  carving projection supplies a non-trivial share of their motion")
        print("  (enf_frac >= split-min, well above 0), so their correction is")
        print(f"  boundary-sourced. The verdict is invariant to enf_frac threshold in")
        print(f"  (0, {enfs.min():.2f}). Selection is now frame-robust AND threshold-robust.")
        print("  Ceiling: 1-D competitors only; same-dimensional mis-governed blocks")
        print("  require the R^3 controller and are not tested here.")


if __name__ == "__main__":
    main()
