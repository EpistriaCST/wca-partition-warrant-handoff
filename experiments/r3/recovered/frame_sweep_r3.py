"""
R^3 oblique frame sweep -- the binding selection test.

Lifts the R^2 frame sweep off the thin (x, a_hat) plane onto the 3-D
organizational state (x, a_hat, r_hat). A carving frame is an invertible 3x3
basis B; a block is a subspace spanned by a subset of its columns. The NEW
content is the 2-D blocks: same-dimensional competitors to the genuine
sub-structure. Isolating a block freezes the complementary frame coordinate(s)
and evolves the substrate, projecting the org coords back onto the block subspace
each step. The projection is an external governor; if it supplies a non-trivial
share of the block's free motion (enf_frac above tolerance) the block's
correction is boundary-sourced and C2 fails.

PRE-COMMITTED KILL RULES
  KILL: P_org (undivided 3-D loop) fails to cross T0          -> procedure artifact
  KILL: any 2-D (same-dimensional) competitor block crosses T0 -> selection is
        frame-relative; the same-dimensional discrimination does NOT generalize.
PASS: org crosses; every 1-D and 2-D competitor rejects under every frame.

Thresholds inherited unchanged. Run gated: only valid if the battery's gate
(direct rate lesion degrades the intact full controller, specificity clean) has
already passed at this operating point.
"""
import numpy as np
import itertools
from dataclasses import replace
from wca_claim2_r3 import SubstrateR3, ParamsR3, THRESH

P = replace(ParamsR3(), sig_x=0.55, sig_r=0.10, k=0.10, q_r=0.015, r_lo=-0.20, r_hi=0.20)
B_thr = THRESH["basin_frac"]; PR = THRESH["P_ratio"]
PD = THRESH["pathdep_ratio"]; ENF = THRESH["enf_frac"]
NS = 2
COND_MAX = 5.0
ORG = ("x", "ah", "rh")


def run_constrained(sub, Bmat, Binv, free_idx, rng,
                    u_zero=False, freeze_y=False, ahat_off=0.0):
    """Evolve with complement frame-coords frozen. Org coords (x,a_hat,r_hat)
    are projected back onto the block subspace each step; hidden a,r and budget P
    carry unprojected. Returns basin trace, mean trP, |a_hat-a| late, enf_frac."""
    p = sub.p; n = p.n; h = p.dt
    comp_idx = [i for i in range(3) if i not in free_idx]
    x = 0.0; a = p.mu_a; r = p.mu_r
    a_hat = p.mu_a + ahat_off; r_hat = p.mu_r
    Pm = np.array([[p.P0, 0.0], [0.0, p.P0]])
    xi0 = Binv @ np.array([x, a_hat, r_hat])
    frozen = {c: xi0[c] for c in comp_idx}

    in_basin = np.empty(n, dtype=bool)
    TrP = np.empty(n); AH = np.empty(n); A = np.empty(n)
    enf_comp = 0.0; enf_blk = 0.0
    for i in range(n):
        xi_cur = Binv @ np.array([x, a_hat, r_hat])
        x, a, r, a_hat, r_hat, Pm = sub.step(x, a, r, a_hat, r_hat, Pm, h, rng,
                                             freeze_y=freeze_y, u_zero=u_zero)
        xi_unc = Binv @ np.array([x, a_hat, r_hat])
        for c in comp_idx:
            enf_comp += abs(xi_unc[c] - frozen[c])
            xi_unc[c] = frozen[c]
        for f in free_idx:
            enf_blk += abs(xi_unc[f] - xi_cur[f])
        x, a_hat, r_hat = Bmat @ xi_unc
        in_basin[i] = abs(x) <= p.x_escape
        TrP[i] = Pm[0, 0] + Pm[1, 1]; AH[i] = a_hat; A[i] = a
    enf_frac = enf_comp / (enf_comp + enf_blk + 1e-12)
    return dict(basin=in_basin.mean(), trP=TrP.mean(),
                terr=np.abs(AH - A)[-500:].mean(), enf=enf_frac)


def eval_constrained_block(sub, Bmat, Binv, free_idx):
    def avg(metric, **kw):
        return np.mean([metric(run_constrained(sub, Bmat, Binv, free_idx,
                        np.random.default_rng(700 + 13 * s), **kw)) for s in range(NS)])
    iso_basin = avg(lambda r: r["basin"])
    passive_basin = avg(lambda r: r["basin"], u_zero=True)
    enf = avg(lambda r: r["enf"])
    P_iso = avg(lambda r: r["trP"])
    P_starved = avg(lambda r: r["trP"], freeze_y=True)
    # C2 hardened: viable, load-bearing, internally sourced (not boundary-enforced)
    C2 = (iso_basin >= B_thr) and (passive_basin < B_thr) and (enf < ENF)
    C3 = (P_iso / max(P_starved, 1e-9)) < PR
    base = avg(lambda r: r["terr"])
    hi = avg(lambda r: r["terr"], ahat_off=+0.4)
    lo = avg(lambda r: r["terr"], ahat_off=-0.4)
    C1 = (max(hi, lo) - base) < PD * 0.4 and (iso_basin >= B_thr)
    tau0 = int(C1 and C2 and C3)
    return tau0, dict(iso=iso_basin, passive=passive_basin, enf=enf,
                      P_ratio=P_iso / max(P_starved, 1e-9))


def make_frames(n_rot=10, n_shear=4, seed=11):
    rng = np.random.default_rng(seed)
    frames = []
    for _ in range(n_rot):
        Q, _ = np.linalg.qr(rng.standard_normal((3, 3)))   # random rotation, cond=1
        frames.append(Q)
    tries = 0
    while len([f for f in frames]) < n_rot + n_shear and tries < 200:
        tries += 1
        Q, _ = np.linalg.qr(rng.standard_normal((3, 3)))
        S = np.eye(3) + 0.3 * rng.standard_normal((3, 3))   # mild shear
        Bm = Q @ S
        if np.linalg.cond(Bm) <= COND_MAX:
            frames.append(Bm)
    return frames
