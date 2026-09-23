"""
W_CA Claim 2 -- R^3 rebuild.

Adds the third controller coordinate the thin (x, a_hat) substrate lacked, so a
SAME-DIMENSIONAL mis-governed competitor can be expressed and tested, rather
than only 1-D convenience carves.

Substrate change (the "momentum regime"):
  - the hidden regime parameter a now has VELOCITY: a integrates a drift-rate r,
    and r itself is a slow clamped random walk. Tracking a therefore requires
    estimating both level (a) and rate (r);
  - the controller becomes a 2-state estimator [a_hat, r_hat] with a 2x2
    covariance. The rate estimate keeps the level estimate calibrated while the
    regime moves; the level estimate keeps the plant in basin. This is the
    within-controller maintenance dependency: rate maintains level maintains
    plant;
  - observability is still intermittent and earned: near basin centre cpl(x)->0,
    so the regime is observable only during plant excursions. Between excursions
    only r_hat carries a_hat forward. That is the channel that makes the rate arm
    load-bearing.

DOF labels for carving:  x  (plant)
                         ah (controller level estimate a_hat)
                         rh (controller rate  estimate r_hat)
  (the covariance P is the budget/uncertainty, tracked but not carved -- C3.)

The decisive new carve is the pseudo-unit {x, ah}: a full-dimensional block that
has a plant and a level estimator and stays in basin for a stretch, but whose
calibration is actually sustained by rh, which sits across the imposed boundary.
W_CA must reject it (C2 fails: governance boundary-sourced) while keeping the
whole loop {x, ah, rh}.

Edge-specific lesions (no global switch):
  freeze_rate : cut rh -> ah  (the rate estimate's edge into the level prediction)
  u_zero      : cut ah -> x   (control set to 0)
  freeze_y    : cut x  -> z   (no live measurement; estimator runs prediction-only)

Thresholds are INHERITED unchanged from the R^2 build. No threshold is tuned to
produce a verdict; the regime motion is set so the test is non-vacuous, then the
discrimination falls where it falls.
"""

import numpy as np
from dataclasses import dataclass, field

# inherit the operational thresholds unchanged
from wca_claim2 import THRESH


def psi(x, xb):
    # unstable near 0 (psi'(0)=1); -> 0 for |x|>>xb (regime unobservable off-basin)
    return x * np.exp(-(x / xb) ** 2)


@dataclass
class ParamsR3:
    dt: float = 0.01
    T: float = 120.0
    # regime LEVEL a
    mu_a: float = 1.0
    a_lo: float = 0.45
    a_hi: float = 1.75
    # regime RATE r (the momentum): a integrates r; r is a slow clamped walk
    mu_r: float = 0.0
    sig_r: float = 0.020       # rate-walk volatility (per sqrt-time)
    r_lo: float = -0.06
    r_hi: float = 0.06
    # control / plant
    k: float = 0.20            # damping margin (weak: calibration matters)
    xb: float = 2.0
    x_escape: float = 2.5
    sig_x: float = 0.25        # plant noise: the ONLY excitation source
    # estimator
    P0: float = 0.40
    q_a: float = 0.012         # level process noise
    q_r: float = 0.004         # rate  process noise
    q_inflate: float = 0.03    # extra uncertainty growth when info edge severed
    seed: int = 0

    @property
    def n(self):
        return int(self.T / self.dt)


class SubstrateR3:
    """Plant x; hidden regime (a level, r rate); 2-state EKF controller (a_hat,
    r_hat) with 2x2 covariance P. One Euler-Maruyama + EKF step is the single
    source of truth, shared by run() and any constrained integrator."""

    def __init__(self, p: ParamsR3, linear_stable=False):
        self.p = p
        self.linear_stable = linear_stable   # negative control

    def coupling(self, x):
        if self.linear_stable:
            return 0.0 * x
        return psi(x, self.p.xb)

    def drift_plant(self, x, a, u):
        if self.linear_stable:
            return -1.0 * x + u
        return a * self.coupling(x) + u

    def step(self, x, a, r, a_hat, r_hat, P, h, rng,
             freeze_y=False, u_zero=False, freeze_rate=False):
        p = self.p

        # --- hidden regime: rate walk, level integrates rate ----------------
        r = r + p.sig_r * np.sqrt(h) * rng.standard_normal()
        r = min(max(r, p.r_lo), p.r_hi)
        a = a + r * h
        a = min(max(a, p.a_lo), p.a_hi)

        cpl = self.coupling(x)

        # --- control: acts through the channel it observes (cpl) ------------
        if u_zero:
            u = 0.0
        elif self.linear_stable:
            u = -(a_hat + p.k) * x
        else:
            u = -(a_hat + p.k) * cpl

        dW = np.sqrt(h) * rng.standard_normal()
        dx_true = self.drift_plant(x, a, u) * h + p.sig_x * dW

        # --- 2-state EKF on [a, r] ------------------------------------------
        if not self.linear_stable:
            # prediction. freeze_rate severs rh->ah: drop the r_hat*h term.
            a_pred = a_hat + (0.0 if freeze_rate else r_hat * h)
            r_pred = r_hat
            F = np.array([[1.0, 0.0 if freeze_rate else h],
                          [0.0, 1.0]])
            Q = np.array([[p.q_a * h, 0.0],
                          [0.0, p.q_r * h]])
            Pp = F @ P @ F.T + Q

            if not freeze_y:
                # measurement: predicted plant increment given the estimate
                pred_dx = (a_pred * cpl + u) * h
                innov = dx_true - pred_dx
                H = np.array([[cpl * h, 0.0]])              # dz/d[a,r]
                S = (H @ Pp @ H.T).item() + (p.sig_x ** 2) * h
                K = (Pp @ H.T) / S                          # 2x1
                upd = (K.flatten() * innov)
                a_hat = a_pred + upd[0]
                r_hat = r_pred + upd[1]
                P = (np.eye(2) - K @ H) @ Pp
            else:
                # info edge severed: prediction-only, uncertainty inflates
                a_hat, r_hat = a_pred, r_pred
                P = Pp + np.array([[p.q_inflate * h, 0.0],
                                   [0.0, p.q_inflate * h]])
        else:
            a_hat, r_hat = a_hat, r_hat
            P = P + np.array([[p.q_a * h, 0.0], [0.0, p.q_r * h]])

        x = x + dx_true
        return x, a, r, a_hat, r_hat, P

    def run(self, freeze_y=False, u_zero=False, freeze_rate=False,
            a_perturb=0.0, r0=None, ahat0=None, rng=None):
        p = self.p
        if rng is None:
            rng = np.random.default_rng(p.seed)
        n, dt = p.n, p.dt
        x = 0.0
        a = p.mu_a + a_perturb
        r = p.mu_r if r0 is None else r0
        a_hat = p.mu_a if ahat0 is None else ahat0
        r_hat = p.mu_r
        P = np.array([[p.P0, 0.0], [0.0, p.P0]])

        X = np.empty(n); A = np.empty(n); R = np.empty(n)
        AH = np.empty(n); RH = np.empty(n); TrP = np.empty(n)
        in_basin = np.empty(n, dtype=bool)
        for i in range(n):
            x, a, r, a_hat, r_hat, P = self.step(
                x, a, r, a_hat, r_hat, P, dt, rng, freeze_y, u_zero, freeze_rate)
            X[i] = x; A[i] = a; R[i] = r; AH[i] = a_hat; RH[i] = r_hat
            TrP[i] = P[0, 0] + P[1, 1]
            in_basin[i] = abs(x) <= p.x_escape
        return dict(X=X, A=A, R=R, AH=AH, RH=RH, P=TrP, in_basin=in_basin)


def _basin_frac(res):
    return res["in_basin"].mean()


def _mean_P(res):
    return res["P"].mean()


# ----------------------------------------------------------------------------
# Partitions over {x, ah, rh}. Cross-boundary edge map per block tells the
# evaluator which lesion isolates that block (severs edges from outside-in).
# ----------------------------------------------------------------------------
@dataclass
class Partition:
    name: str
    blocks: list          # list of frozenset of dof labels


P_ORG    = Partition("P_org",    [frozenset({"x", "ah", "rh"})])
P_PSEUDO = Partition("P_pseudo", [frozenset({"x", "ah"}), frozenset({"rh"})])
P_NESTED = Partition("P_nested", [frozenset({"ah", "rh"}), frozenset({"x"})])
P_SPLIT  = Partition("P_split",  [frozenset({"x"}), frozenset({"ah"}), frozenset({"rh"})])


# isolation lesion for a block: which external edges to sever (set those flags)
def isolation_flags(block):
    has_x, has_ah, has_rh = "x" in block, "ah" in block, "rh" in block
    flags = {}
    # rh -> ah edge is external iff the block holds ah but not rh
    if has_ah and not has_rh:
        flags["freeze_rate"] = True
    # x -> z (measurement) edge is external iff the block holds a controller
    # coord but not the plant
    if (has_ah or has_rh) and not has_x:
        flags["freeze_y"] = True
    # ah -> x (control) edge is external iff the block holds the plant but not ah
    if has_x and not has_ah:
        flags["u_zero"] = True
    return flags
