"""R^3 oblique autonomy probe: trajectory-fit vs autonomous governance.

This script takes the viable-accepted oblique 2D competitors from
r3_oblique_frame_sweep.py and subjects them to off-trajectory perturbations
inside the candidate plane.  A replay-admitted plane is not counted as a bearer
unless perturbations internal to the plane are damped without borrowing the
excluded frame coordinate.

Method limit: this remains a projected-vector-field autonomy stress test, not a
new modular physical substrate.
"""
from __future__ import annotations

import json, math, zipfile
from pathlib import Path
from dataclasses import asdict
from typing import Dict, List, Tuple
import numpy as np

import r3_wca_harness as r3
import r3_oblique_frame_sweep as sweep

OUTDIR = Path('/mnt/data')
INPUT = OUTDIR / 'r3_oblique_frame_sweep_results.json'

# Autonomy probe settings
PERTURB_TIMES = [80, 120, 160, 220, 280]
PERTURB_MAGNITUDES = [0.004, 0.008, 0.012]
HORIZON = 45
RECOVERY_RATIO_T = 0.70       # final deviation must fall below this fraction of initial deviation
MEAN_RECOVERY_RATIO_T = 0.85  # mean tail deviation must be below this fraction of initial deviation
STRICT_RESTORE_FRACTION_T = 0.60  # fraction of perturbations that must restore
DIVERGENCE_CAP = 8.0          # any perturbation above this ratio is counted unstable


def cfg_for(seed: int) -> r3.Config:
    base = asdict(r3.Config())
    base.update(sweep.ROBUST_OP)
    base['seed'] = seed
    return r3.Config(**base)


def regenerate_projector(seed: int, frame_index: int, omit_axis: int) -> Tuple[np.ndarray, float]:
    rng_master = np.random.default_rng(20260620)
    seed_rngs = {}
    for s in sweep.SEEDS:
        seed_rngs[s] = int(rng_master.integers(0, 2**32-1)) + s
    rng = np.random.default_rng(seed_rngs[seed])
    A = None
    for j in range(frame_index + 1):
        A = sweep.random_frame(rng)
    assert A is not None
    P, cond = sweep.plane_projector_from_frame(A, omit_axis)
    # Orthonormal basis for the plane, used to choose perturbation directions.
    vals, vecs = np.linalg.eigh(P)
    U = vecs[:, np.argsort(vals)[-2:]]
    return P, cond, U


def projected_field(z: np.ndarray, a_truth: float, cfg: r3.Config, P: np.ndarray) -> np.ndarray:
    """Autonomous vector field available to the candidate plane.

    Uses the plant/control law and estimator prediction terms, then projects the
    free motion back into the candidate's 2D plane.  No correction from the
    excluded frame coordinate is allowed beyond this projection.
    """
    x, ah, rh = map(float, z)
    dx = (cfg.base_growth + a_truth) * x - (cfg.base_growth + ah + cfg.control_margin) * x
    dah = rh
    drh = -cfg.regime_rate_damping * rh
    return P @ np.array([dx, dah, drh], dtype=float)


def build_reference_path(traj: Dict[str, np.ndarray], P: np.ndarray) -> np.ndarray:
    Z = np.column_stack([traj['x'], traj['a_hat'], traj['rate_hat']])
    Zp = np.empty_like(Z)
    Zp[0] = P @ Z[0]
    for t in range(len(Z) - 1):
        Zp[t + 1] = Zp[t] + P @ (Z[t + 1] - Z[t])
    return Zp


def evolve_candidate(z0: np.ndarray, start_t: int, traj: Dict[str, np.ndarray], cfg: r3.Config, P: np.ndarray) -> np.ndarray:
    zs = [z0.copy()]
    z = z0.copy()
    for k in range(HORIZON):
        t = min(start_t + k, len(traj['a']) - 1)
        dz = projected_field(z, float(traj['a'][t]), cfg, P)
        z = z + cfg.dt * dz
        # Constrain numerical drift back to the candidate plane without using any
        # excluded governance signal.
        z = P @ z
        zs.append(z.copy())
    return np.array(zs)


def probe_plane(row: dict) -> dict:
    seed = int(row['seed'])
    cfg = cfg_for(seed)
    full, traj = r3.run_full(cfg)
    P, cond, U = regenerate_projector(seed, int(row['frame_index']), int(row['omit_axis']))
    Zref = build_reference_path(traj, P)
    perturb_results = []
    restored = 0
    total = 0
    divergent = 0

    for t0 in PERTURB_TIMES:
        if t0 + HORIZON >= len(Zref):
            continue
        for mag in PERTURB_MAGNITUDES:
            for sign in [-1.0, 1.0]:
                for d in range(2):
                    delta = sign * mag * U[:, d]
                    z0 = Zref[t0] + delta
                    cand = evolve_candidate(z0, t0, traj, cfg, P)
                    ref = Zref[t0:t0 + HORIZON + 1]
                    dev = np.linalg.norm(cand - ref, axis=1)
                    init = max(float(dev[0]), 1e-12)
                    final_ratio = float(dev[-1] / init)
                    tail_ratio = float(np.mean(dev[-10:]) / init)
                    min_ratio = float(np.min(dev) / init)
                    max_ratio = float(np.max(dev) / init)
                    is_restored = final_ratio <= RECOVERY_RATIO_T and tail_ratio <= MEAN_RECOVERY_RATIO_T
                    is_divergent = max_ratio >= DIVERGENCE_CAP
                    restored += int(is_restored)
                    divergent += int(is_divergent)
                    total += 1
                    perturb_results.append({
                        't0': t0,
                        'mag': mag,
                        'direction': d,
                        'sign': sign,
                        'initial_dev': init,
                        'final_ratio': final_ratio,
                        'tail_ratio': tail_ratio,
                        'min_ratio': min_ratio,
                        'max_ratio': max_ratio,
                        'restored': is_restored,
                        'divergent': is_divergent,
                    })

    restore_fraction = restored / total if total else 0.0
    diverge_fraction = divergent / total if total else 0.0
    med_final = float(np.median([p['final_ratio'] for p in perturb_results])) if perturb_results else None
    med_tail = float(np.median([p['tail_ratio'] for p in perturb_results])) if perturb_results else None
    p90_max = float(np.quantile([p['max_ratio'] for p in perturb_results], 0.90)) if perturb_results else None

    if restore_fraction >= STRICT_RESTORE_FRACTION_T:
        cls = 'autonomous_candidate_survived'
        mode = 'off_trajectory_restoration'
    else:
        cls = 'trajectory_hugger_rejected'
        mode = 'replay_fit_without_internal_restoration'

    return {
        'seed': seed,
        'frame_index': int(row['frame_index']),
        'omit_axis': int(row['omit_axis']),
        'condition_number': cond,
        'prior_replay_metrics': {k: row[k] for k in ['basin_occupancy','mean_abs_error','enforcement_fraction','covariance_retention','classification'] if k in row},
        'n_perturbations': total,
        'restored': restored,
        'restore_fraction': restore_fraction,
        'divergent': divergent,
        'diverge_fraction': diverge_fraction,
        'median_final_ratio': med_final,
        'median_tail_ratio': med_tail,
        'p90_max_ratio': p90_max,
        'classification': cls,
        'autonomy_mode': mode,
        'perturbation_results': perturb_results,
    }


def main() -> dict:
    data = json.loads(INPUT.read_text())
    accepted_rows = [r for r in data['rows'] if r['classification'] == 'viable_accepted']
    results = [probe_plane(r) for r in accepted_rows]
    counts = {}
    for rrow in results:
        counts[rrow['classification']] = counts.get(rrow['classification'], 0) + 1
    survived = [r for r in results if r['classification'] == 'autonomous_candidate_survived']
    rejected = [r for r in results if r['classification'] == 'trajectory_hugger_rejected']
    summary = {
        'input_viable_accepted_planes': len(accepted_rows),
        'autonomy_probe_settings': {
            'perturb_times': PERTURB_TIMES,
            'perturb_magnitudes': PERTURB_MAGNITUDES,
            'horizon': HORIZON,
            'recovery_ratio_threshold': RECOVERY_RATIO_T,
            'mean_recovery_ratio_threshold': MEAN_RECOVERY_RATIO_T,
            'restore_fraction_threshold': STRICT_RESTORE_FRACTION_T,
            'divergence_cap': DIVERGENCE_CAP,
            'method_limit': 'projected-vector-field perturbation test of replay-admitted oblique planes; not a full modular autonomous substrate',
        },
        'classification_counts': counts,
        'n_survived': len(survived),
        'n_rejected_as_trajectory_huggers': len(rejected),
        'median_restore_fraction': float(np.median([r['restore_fraction'] for r in results])) if results else None,
        'max_restore_fraction': float(np.max([r['restore_fraction'] for r in results])) if results else None,
        'median_final_ratio_over_planes': float(np.median([r['median_final_ratio'] for r in results])) if results else None,
        'median_tail_ratio_over_planes': float(np.median([r['median_tail_ratio'] for r in results])) if results else None,
        'survived_examples': survived[:10],
        'rejected_examples': rejected[:10],
        'rows': results,
    }
    return summary


def write_outputs(results: dict) -> None:
    out_json = OUTDIR / 'r3_oblique_autonomy_probe_results.json'
    out_txt = OUTDIR / 'r3_oblique_autonomy_probe_summary.txt'
    out_zip = OUTDIR / 'r3_oblique_autonomy_probe.zip'
    out_json.write_text(json.dumps(results, indent=2), encoding='utf-8')
    lines = [
        'R^3 oblique autonomy probe: trajectory-fit vs autonomous governance',
        '',
        f"Input viable accepted oblique planes: {results['input_viable_accepted_planes']}",
        f"Classification counts: {results['classification_counts']}",
        f"Rejected as trajectory-huggers: {results['n_rejected_as_trajectory_huggers']}",
        f"Autonomous candidates survived: {results['n_survived']}",
        f"Median restore fraction: {results['median_restore_fraction']}",
        f"Max restore fraction: {results['max_restore_fraction']}",
        f"Median final deviation ratio over planes: {results['median_final_ratio_over_planes']}",
        f"Median tail deviation ratio over planes: {results['median_tail_ratio_over_planes']}",
        '',
        'Verdict: ' + ('PASSED: all replay-admitted oblique planes failed off-trajectory autonomy.' if results['n_survived'] == 0 else 'FAILED/UNDECIDED: at least one replay-admitted oblique plane survived autonomy probing.'),
        '',
        'Interpretation:',
        '  Replay viability is not enough. A plane must restore from perturbations internal to its own 2D coordinates.',
        '  Planes rejected here are trajectory-huggers: they shadow the intact path but do not supply autonomous governance.',
        '',
        'Method limit:',
        f"  {results['autonomy_probe_settings']['method_limit']}",
    ]
    out_txt.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    with zipfile.ZipFile(out_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(__file__, arcname='r3_oblique_autonomy_probe.py')
        zf.write(out_json, arcname='r3_oblique_autonomy_probe_results.json')
        zf.write(out_txt, arcname='r3_oblique_autonomy_probe_summary.txt')
        zf.write(OUTDIR / 'r3_oblique_frame_sweep.py', arcname='r3_oblique_frame_sweep.py')
        zf.write(OUTDIR / 'r3_wca_harness.py', arcname='r3_wca_harness.py')

if __name__ == '__main__':
    res = main()
    write_outputs(res)
    print((OUTDIR / 'r3_oblique_autonomy_probe_summary.txt').read_text())
