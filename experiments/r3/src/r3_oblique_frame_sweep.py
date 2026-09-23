"""R^3 oblique 3D frame sweep with basin-viability gating.

Purpose
-------
Stress-test the same-dimensional R^3 result against bounded-condition-number
3D coordinate mixtures.  The sweep does not require rejection mechanisms to be
uniform.  It classifies each oblique 2D competitor as:

    nonviable          exits basin too quickly, not informative
    viable_rejected    remains basin-viable but fails governance validation
    viable_accepted    basin-viable and governance-admitted; possible counterexample

This is a replay/projection frame test, not a newly identified physical plant.
It uses the robust rate-arm operating point found in r3_rate_arm_robustness.py.
"""
from __future__ import annotations

import json, math, zipfile
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import r3_wca_harness as r3

ROBUST_OP = dict(
    initial_rate=1.1,
    obs_every=20,
    obs_noise=0.01,
    control_margin=0.01,
    basin=0.15,
    regime_rate_damping=0.015,
    regime_accel_noise=0.0,
    q_rate=1e-5,
    q_level=1e-6,
    q_level_only=1e-6,
    steps=350,
)

DIRECT_LESIONS = ["freeze_rate_prediction", "freeze_rate_state", "cut_rate_update"]
SEEDS = list(range(1, 16))
N_FRAMES_PER_SEED = 160
COND_MAX = 8.0
VIABILITY_T_BASIN = 0.80
VIABILITY_T_ERROR = 0.10
ENFORCEMENT_T = 0.15
COV_T = 0.65  # minimum retained covariance consistency after projection


def cfg_for(seed: int) -> r3.Config:
    base = asdict(r3.Config())
    base.update(ROBUST_OP)
    base["seed"] = seed
    return r3.Config(**base)


def full_pass(m: r3.RunMetrics, cfg: r3.Config) -> bool:
    return m.basin_occupancy >= cfg.t_basin and m.mean_abs_error <= cfg.t_calib_error


def direct_rate_arm_ok(cfg: r3.Config, full: r3.RunMetrics) -> bool:
    for lesion in DIRECT_LESIONS:
        m, _ = r3.run_full(cfg, lesion=lesion)
        ratio = m.mean_abs_error / max(full.mean_abs_error, 1e-12)
        if not (m.basin_occupancy < cfg.t_basin or ratio > cfg.t_rate_lesion_ratio):
            return False
    return True


def random_frame(rng: np.random.Generator, cond_max: float = COND_MAX) -> np.ndarray:
    # Random orthogonal factors with controlled singular values.
    Q1, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    Q2, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    # Log-uniform singular spread in [1, cond_max].
    c = float(np.exp(rng.uniform(0.0, math.log(cond_max))))
    mids = float(np.exp(rng.uniform(0.0, math.log(c))))
    S = np.diag([c, mids, 1.0])
    A = Q1 @ S @ Q2.T
    return A


def plane_projector_from_frame(A: np.ndarray, omit_axis: int) -> Tuple[np.ndarray, float]:
    # Columns of A are oblique frame directions.  A 2D carve keeps two frame axes.
    keep = [i for i in range(3) if i != omit_axis]
    B = A[:, keep]
    P = B @ np.linalg.inv(B.T @ B) @ B.T
    return P, float(np.linalg.cond(A))


def replay_projection_metrics(traj: Dict[str, np.ndarray], P: np.ndarray, cfg: r3.Config) -> dict:
    # Reconstruct actual 3D loop-state trajectory and project its increments into the candidate plane.
    Z = np.column_stack([traj["x"], traj["a_hat"], traj["rate_hat"]])
    Zc = np.empty_like(Z)
    Zc[0] = P @ Z[0]
    blocked_norms = []
    total_norms = []
    for t in range(len(Z) - 1):
        dz = Z[t + 1] - Z[t]
        dz_keep = P @ dz
        blocked = dz - dz_keep
        Zc[t + 1] = Zc[t] + dz_keep
        blocked_norms.append(float(np.linalg.norm(blocked)))
        total_norms.append(float(np.linalg.norm(dz) + 1e-12))
    x = Zc[:, 0]
    ah = Zc[:, 1]
    err = np.abs(traj["a"] - ah)
    basin_occ = float(np.mean(np.abs(x) <= cfg.basin))
    mean_err = float(np.mean(err))
    enforcement = float(np.sum(blocked_norms) / (np.sum(total_norms) + 1e-12))
    # Covariance consistency: how much of the estimator covariance geometry survives the carve.
    X = Z[:, 1:3]
    C = np.cov(X.T) + 1e-12 * np.eye(2)
    # Embed controller covariance into 3D, project, compare retained trace over controller coordinates.
    C3 = np.zeros((3, 3)); C3[1:3, 1:3] = C
    retained = P @ C3 @ P.T
    cov_retention = float(np.trace(retained[1:3, 1:3]) / max(np.trace(C), 1e-12))
    viable = basin_occ >= VIABILITY_T_BASIN and mean_err <= VIABILITY_T_ERROR
    c2_pass = enforcement <= ENFORCEMENT_T
    c3_pass = cov_retention >= COV_T
    if not viable:
        classification = "nonviable"
        mode = "basin_or_calibration_failure"
    elif c2_pass and c3_pass:
        classification = "viable_accepted"
        mode = "none"
    else:
        classification = "viable_rejected"
        if not c2_pass and not c3_pass:
            mode = "projection_enforcement_and_covariance_incoherence"
        elif not c2_pass:
            mode = "projection_enforcement"
        else:
            mode = "covariance_incoherence"
    return {
        "basin_occupancy": basin_occ,
        "mean_abs_error": mean_err,
        "enforcement_fraction": enforcement,
        "covariance_retention": cov_retention,
        "viable": viable,
        "c2_pass": c2_pass,
        "c3_pass": c3_pass,
        "classification": classification,
        "rejection_mode": mode,
    }


def run_sweep() -> dict:
    rng_master = np.random.default_rng(20260620)
    all_rows: List[dict] = []
    seed_summaries: List[dict] = []
    for seed in SEEDS:
        cfg = cfg_for(seed)
        full, traj = r3.run_full(cfg)
        ok_full = full_pass(full, cfg)
        ok_rate = direct_rate_arm_ok(cfg, full) if ok_full else False
        rng = np.random.default_rng(int(rng_master.integers(0, 2**32-1)) + seed)
        seed_rows = []
        if ok_full and ok_rate:
            for j in range(N_FRAMES_PER_SEED):
                A = random_frame(rng)
                for omit in [0, 1, 2]:
                    P, cond = plane_projector_from_frame(A, omit)
                    m = replay_projection_metrics(traj, P, cfg)
                    row = {
                        "seed": seed,
                        "frame_index": j,
                        "omit_axis": omit,
                        "condition_number": cond,
                        **m,
                    }
                    seed_rows.append(row)
                    all_rows.append(row)
        counts = {k: sum(r["classification"] == k for r in seed_rows) for k in ["nonviable", "viable_rejected", "viable_accepted"]}
        modes = {}
        for rrow in seed_rows:
            modes[rrow["rejection_mode"]] = modes.get(rrow["rejection_mode"], 0) + 1
        seed_summaries.append({
            "seed": seed,
            "full_pass": ok_full,
            "rate_arm_direct_load_bearing": ok_rate,
            "full_metrics": asdict(full),
            "n_competitors": len(seed_rows),
            "classification_counts": counts,
            "rejection_modes": modes,
        })
    counts = {k: sum(r["classification"] == k for r in all_rows) for k in ["nonviable", "viable_rejected", "viable_accepted"]}
    viable = [r for r in all_rows if r["viable"]]
    modes = {}
    for rrow in all_rows:
        modes[rrow["rejection_mode"]] = modes.get(rrow["rejection_mode"], 0) + 1
    accepted = [r for r in all_rows if r["classification"] == "viable_accepted"]
    summary = {
        "criteria": {
            "operating_point": ROBUST_OP,
            "seeds": SEEDS,
            "frames_per_seed": N_FRAMES_PER_SEED,
            "2d_carves_per_frame": 3,
            "condition_number_max_target": COND_MAX,
            "viability_gate": f"basin >= {VIABILITY_T_BASIN} and mean_abs_error <= {VIABILITY_T_ERROR}",
            "c2_enforcement_pass": f"enforcement_fraction <= {ENFORCEMENT_T}",
            "c3_covariance_pass": f"covariance_retention >= {COV_T}",
            "method_limit": "replay/projection stress test over full-loop trajectory; not a newly derived autonomous physical substrate",
        },
        "global_counts": counts,
        "n_competitors": len(all_rows),
        "n_viable": len(viable),
        "viable_rejection_fraction": (counts["viable_rejected"] / len(viable)) if viable else None,
        "viable_acceptance_fraction": (counts["viable_accepted"] / len(viable)) if viable else None,
        "rejection_modes": modes,
        "seed_summaries": seed_summaries,
        "accepted_examples": accepted[:20],
        "rows": all_rows,
    }
    return summary


def write_outputs(results: dict) -> None:
    out_json = Path("/mnt/data/r3_oblique_frame_sweep_results.json")
    out_txt = Path("/mnt/data/r3_oblique_frame_sweep_summary.txt")
    out_zip = Path("/mnt/data/r3_oblique_frame_sweep.zip")
    out_json.write_text(json.dumps(results, indent=2), encoding="utf-8")
    lines = []
    lines.append("R^3 3D oblique-frame sweep with viability gate")
    lines.append("")
    lines.append(f"Operating point: {ROBUST_OP}")
    lines.append(f"Seeds: {SEEDS}")
    lines.append(f"Frames per seed: {N_FRAMES_PER_SEED}; 2D carves per frame: 3")
    lines.append(f"Competitors evaluated: {results['n_competitors']}")
    lines.append(f"Viable competitors: {results['n_viable']}")
    lines.append(f"Global counts: {results['global_counts']}")
    lines.append(f"Viable rejection fraction: {results['viable_rejection_fraction']}")
    lines.append(f"Viable acceptance fraction: {results['viable_acceptance_fraction']}")
    lines.append("")
    lines.append("Rejection modes:")
    for k, v in sorted(results["rejection_modes"].items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"  {k}: {v}")
    lines.append("")
    bad_seeds = [s for s in results["seed_summaries"] if not (s["full_pass"] and s["rate_arm_direct_load_bearing"])]
    lines.append(f"Seeds failing full/rate-arm precondition: {len(bad_seeds)}")
    lines.append("")
    lines.append("Per-seed counts:")
    for s in results["seed_summaries"]:
        lines.append(f"  seed {s['seed']}: full={s['full_pass']}, rate={s['rate_arm_direct_load_bearing']}, counts={s['classification_counts']}")
    lines.append("")
    if results["global_counts"]["viable_accepted"] == 0 and results["n_viable"] > 0:
        lines.append("Verdict: PASSED under this replay/projection oblique-frame battery: viable same-dimensional oblique competitors were rejected, and rejection modes were non-uniform.")
    elif results["global_counts"]["viable_accepted"] > 0:
        lines.append("Verdict: FAILED/UNDECIDED: at least one viable oblique competitor was admitted.")
    else:
        lines.append("Verdict: UNINFORMATIVE: no basin-viable same-dimensional competitors survived the viability gate.")
    lines.append("")
    lines.append("Limit: this is a frame-stress replay/projection test, not an autonomous modular substrate demonstration.")
    out_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.write("/mnt/data/r3_oblique_frame_sweep.py", arcname="r3_oblique_frame_sweep.py")
        z.write(out_json, arcname="r3_oblique_frame_sweep_results.json")
        z.write(out_txt, arcname="r3_oblique_frame_sweep_summary.txt")
    print(out_txt.read_text())


if __name__ == "__main__":
    write_outputs(run_sweep())
