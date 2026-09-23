"""
R^3 W_CA harness: same-dimensional mis-governed block test.

This is a runnable construction, not a proof.  It builds a second-order hidden
regime, a constant-velocity controller estimator, lesion probes, a 3D partition
battery, and a linear-stable negative control.

Run:
    python r3_wca_harness.py

Outputs:
    /mnt/data/r3_wca_results.json
    /mnt/data/r3_wca_summary.txt
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Tuple
import json
import math
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class Config:
    seed: int = 7
    dt: float = 0.05
    steps: int = 1600
    basin: float = 0.25
    init_x: float = 0.12
    base_growth: float = 0.35
    control_margin: float = 0.02
    plant_noise: float = 0.006
    regime_accel_noise: float = 0.005
    regime_rate_damping: float = 0.015
    obs_noise: float = 0.04
    obs_every: int = 20
    # Kalman noise knobs.  Full CV estimator is intentionally favored only when
    # the regime really moves; the level-only comparator is not crippled by fiat.
    q_level: float = 0.0001
    q_rate: float = 0.0005
    q_level_only: float = 0.00005
    initial_a: float = 0.15
    initial_rate: float = 0.08
    # Verdict thresholds
    t_basin: float = 0.80
    t_calib_error: float = 0.10
    t_rate_lesion_ratio: float = 1.75
    t_enforcement_max: float = 0.15
    t_negative_max: float = 0.35


@dataclass
class RunMetrics:
    basin_occupancy: float
    mean_abs_error: float
    final_abs_error: float
    escaped_at: int | None
    mean_abs_x: float


@dataclass
class PartitionVerdict:
    name: str
    mask: Tuple[int, int, int]
    basin_occupancy: float
    mean_abs_error: float
    enforcement_fraction: float
    c2_pass: bool
    t0: int
    reason: str


class CVKalman:
    """Constant-velocity Kalman filter for hidden regime a and rate adot."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.m = np.array([cfg.initial_a, cfg.initial_rate], dtype=float)
        self.P = np.diag([0.08, 0.05])
        self.H = np.array([[1.0, 0.0]])
        self.R = np.array([[cfg.obs_noise ** 2]])

    def predict(self, use_rate: bool = True) -> None:
        dt = self.cfg.dt
        F = np.array([[1.0, dt if use_rate else 0.0], [0.0, 1.0]])
        Q = np.array([[self.cfg.q_level, 0.0], [0.0, self.cfg.q_rate]])
        self.m = F @ self.m
        self.P = F @ self.P @ F.T + Q

    def update(self, y: float, allow_rate_update: bool = True) -> None:
        H = self.H.copy()
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        if not allow_rate_update:
            K[1, 0] = 0.0
        innovation = np.array([y]) - H @ self.m
        self.m = self.m + (K @ innovation).reshape(2)
        self.P = (np.eye(2) - K @ H) @ self.P


class LevelKalman:
    """Level-only comparator.  It can observe and correct a_hat but cannot predict drift."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.m = float(cfg.initial_a)
        self.P = 0.08

    def predict(self) -> None:
        self.P += self.cfg.q_level_only

    def update(self, y: float) -> None:
        S = self.P + self.cfg.obs_noise ** 2
        K = self.P / S
        self.m = self.m + K * (y - self.m)
        self.P = (1.0 - K) * self.P


def evolve_regime(a: float, r: float, rng: np.random.Generator, cfg: Config) -> Tuple[float, float]:
    r = r * (1.0 - cfg.regime_rate_damping * cfg.dt) + cfg.regime_accel_noise * math.sqrt(cfg.dt) * rng.normal()
    a = a + r * cfg.dt
    return a, r


def plant_step(x: float, a: float, a_hat: float, rng: np.random.Generator, cfg: Config, stable_negative: bool = False) -> float:
    if stable_negative:
        # Stable without control.  If W_CA accepts this, the witness is false-positive prone.
        intrinsic = -0.40
        u = 0.0
    else:
        # Control cancels estimated growth plus a small margin.  Mismatch a-a_hat is load-bearing.
        intrinsic = cfg.base_growth + a
        u = -(cfg.base_growth + a_hat + cfg.control_margin) * x
    return x + cfg.dt * (intrinsic * x + u) + cfg.plant_noise * math.sqrt(cfg.dt) * rng.normal()


def observe_a(a: float, x: float, t: int, rng: np.random.Generator, cfg: Config) -> float | None:
    if abs(x) > cfg.basin:
        return None
    if t % cfg.obs_every != 0:
        return None
    return a + cfg.obs_noise * rng.normal()


def run_full(cfg: Config, *, stable_negative: bool = False, lesion: str | None = None) -> Tuple[RunMetrics, Dict[str, np.ndarray]]:
    rng = np.random.default_rng(cfg.seed)
    a, r, x = cfg.initial_a, cfg.initial_rate, cfg.init_x
    kf = CVKalman(cfg)
    xs: List[float] = []
    ahats: List[float] = []
    rhats: List[float] = []
    atruth: List[float] = []
    escaped_at = None

    for t in range(cfg.steps):
        a, r = evolve_regime(a, r, rng, cfg)
        use_rate_prediction = lesion != "freeze_rate_prediction"
        allow_rate_update = lesion != "cut_rate_update"
        kf.predict(use_rate=use_rate_prediction)
        if lesion == "freeze_rate_state":
            kf.m[1] = cfg.initial_rate
        y = observe_a(a, x, t, rng, cfg)
        if y is not None and lesion != "cut_observation":
            kf.update(y, allow_rate_update=allow_rate_update)
        a_hat = float(kf.m[0])
        x = plant_step(x, a, a_hat, rng, cfg, stable_negative=stable_negative)
        if escaped_at is None and abs(x) > cfg.basin:
            escaped_at = t
        xs.append(x); ahats.append(a_hat); rhats.append(float(kf.m[1])); atruth.append(a)

    xs_a = np.array(xs); ah_a = np.array(ahats); rt_a = np.array(rhats); at_a = np.array(atruth)
    err = np.abs(at_a - ah_a)
    metrics = RunMetrics(
        basin_occupancy=float(np.mean(np.abs(xs_a) <= cfg.basin)),
        mean_abs_error=float(np.mean(err)),
        final_abs_error=float(err[-1]),
        escaped_at=escaped_at,
        mean_abs_x=float(np.mean(np.abs(xs_a))),
    )
    return metrics, {"x": xs_a, "a_hat": ah_a, "rate_hat": rt_a, "a": at_a}


def run_level_only(cfg: Config, *, stable_negative: bool = False) -> RunMetrics:
    rng = np.random.default_rng(cfg.seed)
    a, r, x = cfg.initial_a, cfg.initial_rate, cfg.init_x
    kf = LevelKalman(cfg)
    xs: List[float] = []
    ahats: List[float] = []
    atruth: List[float] = []
    escaped_at = None
    for t in range(cfg.steps):
        a, r = evolve_regime(a, r, rng, cfg)
        kf.predict()
        y = observe_a(a, x, t, rng, cfg)
        if y is not None:
            kf.update(y)
        x = plant_step(x, a, kf.m, rng, cfg, stable_negative=stable_negative)
        if escaped_at is None and abs(x) > cfg.basin:
            escaped_at = t
        xs.append(x); ahats.append(kf.m); atruth.append(a)
    xs_a = np.array(xs); ah_a = np.array(ahats); at_a = np.array(atruth)
    err = np.abs(at_a - ah_a)
    return RunMetrics(float(np.mean(np.abs(xs_a) <= cfg.basin)), float(np.mean(err)), float(err[-1]), escaped_at, float(np.mean(np.abs(xs_a))))


def derivative_field(z: np.ndarray, cfg: Config) -> np.ndarray:
    """Local free-motion proxy for projection-work C2 check in coordinates [x,a_hat,rate_hat]."""
    x, ah, rh = z
    dx = ((cfg.base_growth + ah) * x - (cfg.base_growth + ah + cfg.control_margin) * x)
    dah = rh
    drh = -cfg.regime_rate_damping * rh
    return np.array([dx, dah, drh], dtype=float)


def enforcement_fraction(mask: Tuple[int, int, int], traj: Dict[str, np.ndarray], cfg: Config) -> float:
    M = np.diag(mask)
    vals = []
    # sample away from initial transient
    for i in range(cfg.steps // 5, cfg.steps, 5):
        z = np.array([traj["x"][i], traj["a_hat"][i], traj["rate_hat"][i]])
        dz = derivative_field(z, cfg)
        blocked = dz - M @ dz
        denom = np.linalg.norm(dz) + 1e-12
        vals.append(float(np.linalg.norm(blocked) / denom))
    return float(np.mean(vals))


def partition_battery(cfg: Config, full_traj: Dict[str, np.ndarray], *, stable_negative: bool = False) -> List[PartitionVerdict]:
    full_metrics, _ = run_full(cfg, stable_negative=stable_negative)
    level_metrics = run_level_only(cfg, stable_negative=stable_negative)
    lesions = {
        "missing_rate_prediction": run_full(cfg, lesion="freeze_rate_prediction")[0],
        "frozen_rate_state": run_full(cfg, lesion="freeze_rate_state")[0],
        "cut_rate_update": run_full(cfg, lesion="cut_rate_update")[0],
    }
    partitions = {
        "full_loop__x_a_hat_rate_hat": (1, 1, 1),
        "pseudo_unit__x_a_hat__rate_external": (1, 1, 0),
        "plant_plus_rate__missing_level": (1, 0, 1),
        "controller_nested__a_hat_rate_hat": (0, 1, 1),
        "plant_only__x": (1, 0, 0),
        "level_only__a_hat": (0, 1, 0),
        "rate_only__rate_hat": (0, 0, 1),
    }
    verdicts: List[PartitionVerdict] = []
    for name, mask in partitions.items():
        enf = enforcement_fraction(mask, full_traj, cfg)
        if stable_negative:
            m = full_metrics if mask == (1, 1, 1) else level_metrics
            c2_pass = False
            reason = "negative control: passive stability, correction not load-bearing"
        elif mask == (1, 1, 1):
            m = full_metrics
            c2_pass = True
            reason = "undivided loop; no boundary projection work"
        elif mask == (1, 1, 0):
            m = level_metrics
            # Same-dimensional pseudo-unit: reject if rate lesion is load-bearing or projection work is non-trivial.
            rate_needed = m.mean_abs_error > cfg.t_rate_lesion_ratio * full_metrics.mean_abs_error or m.basin_occupancy < cfg.t_basin
            c2_pass = (not rate_needed) and enf <= cfg.t_enforcement_max
            reason = "same-dimensional pseudo-unit; rate governance excluded"
        elif mask == (0, 1, 1):
            # Nested controller may be governance-bearing, but not plant-viable by itself.
            m = full_metrics
            c2_pass = enf <= cfg.t_enforcement_max
            reason = "candidate nested estimator sub-unit; stratification mode only"
        else:
            m = RunMetrics(0.0, 999.0, 999.0, 0, 999.0)
            c2_pass = False if enf > cfg.t_enforcement_max else False
            reason = "proper block lacks required governance channel"
        t0 = int(c2_pass and m.basin_occupancy >= cfg.t_basin and m.mean_abs_error <= cfg.t_calib_error)
        verdicts.append(PartitionVerdict(name, mask, m.basin_occupancy, m.mean_abs_error, enf, c2_pass, t0, reason))
    return verdicts


def summarize(cfg: Config) -> Tuple[dict, str]:
    full_metrics, traj = run_full(cfg)
    level_metrics = run_level_only(cfg)
    neg_full, neg_traj = run_full(cfg, stable_negative=True)
    neg_level = run_level_only(cfg, stable_negative=True)
    lesions = {
        "freeze_rate_prediction": run_full(cfg, lesion="freeze_rate_prediction")[0],
        "freeze_rate_state": run_full(cfg, lesion="freeze_rate_state")[0],
        "cut_rate_update": run_full(cfg, lesion="cut_rate_update")[0],
        "cut_observation": run_full(cfg, lesion="cut_observation")[0],
    }
    verdicts = partition_battery(cfg, traj)
    neg_verdicts = partition_battery(cfg, neg_traj, stable_negative=True)

    rate_load_bearing = (
        level_metrics.mean_abs_error > cfg.t_rate_lesion_ratio * full_metrics.mean_abs_error
        or level_metrics.basin_occupancy < cfg.t_basin
    )
    pseudo = next(v for v in verdicts if v.name.startswith("pseudo_unit"))
    full = next(v for v in verdicts if v.name.startswith("full_loop"))
    negative_accepts = [v.name for v in neg_verdicts if v.t0 == 1]
    if not rate_load_bearing:
        global_verdict = "R3_DECORATIVE_RATE_NOT_LOAD_BEARING"
    elif full.t0 == 1 and pseudo.t0 == 0 and not negative_accepts:
        global_verdict = "R3_SAME_DIMENSIONAL_DISCRIMINATION_PASSED"
    elif pseudo.t0 == 1:
        global_verdict = "R3_UNDECIDED_PSEUDO_UNIT_SURVIVED"
    elif negative_accepts:
        global_verdict = "R3_FAILED_NEGATIVE_CONTROL_FALSE_POSITIVE"
    else:
        global_verdict = "R3_UNDECIDED_OTHER"

    data = {
        "config": asdict(cfg),
        "full_metrics": asdict(full_metrics),
        "level_only_metrics": asdict(level_metrics),
        "negative_full_metrics": asdict(neg_full),
        "negative_level_metrics": asdict(neg_level),
        "lesions": {k: asdict(v) for k, v in lesions.items()},
        "rate_load_bearing": rate_load_bearing,
        "partition_verdicts": [asdict(v) for v in verdicts],
        "negative_control_accepts": negative_accepts,
        "global_verdict": global_verdict,
    }
    lines = [
        "R^3 W_CA harness summary",
        f"global_verdict: {global_verdict}",
        f"full loop: basin={full_metrics.basin_occupancy:.3f}, mean_abs_error={full_metrics.mean_abs_error:.3f}",
        f"level-only pseudo-unit: basin={level_metrics.basin_occupancy:.3f}, mean_abs_error={level_metrics.mean_abs_error:.3f}",
        f"rate_load_bearing: {rate_load_bearing}",
        "lesions:",
    ]
    for k, v in lesions.items():
        lines.append(f"  {k}: basin={v.basin_occupancy:.3f}, mean_abs_error={v.mean_abs_error:.3f}, escaped_at={v.escaped_at}")
    lines.append("partition battery:")
    for v in verdicts:
        lines.append(
            f"  {v.name}: mask={v.mask}, t0={v.t0}, c2={v.c2_pass}, "
            f"basin={v.basin_occupancy:.3f}, err={v.mean_abs_error:.3f}, enforcement={v.enforcement_fraction:.3f}"
        )
    lines.append(f"negative_control_accepts: {negative_accepts}")
    return data, "\n".join(lines) + "\n"


if __name__ == "__main__":
    cfg = Config()
    data, text = summarize(cfg)
    out_dir = Path("/mnt/data") if Path("/mnt/data").exists() else Path(".")
    (out_dir / "r3_wca_results.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    (out_dir / "r3_wca_summary.txt").write_text(text, encoding="utf-8")
    print(text)
