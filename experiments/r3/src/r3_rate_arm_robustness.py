"""Robustness battery for R^3 direct rate-arm load-bearing.

This script does not treat a failing level-only comparator as evidence. It asks
whether direct lesions of the rate arm degrade the same intact full controller
across seeds and nearby operating points.

Run:
    python r3_rate_arm_robustness.py

Outputs:
    /mnt/data/r3_rate_arm_robustness_results.json
    /mnt/data/r3_rate_arm_robustness_summary.txt
"""
from __future__ import annotations

import itertools, json, statistics, random
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Tuple

import r3_wca_harness as r3

DIRECT_LESIONS = ["freeze_rate_prediction", "freeze_rate_state", "cut_rate_update"]

BASE_OP = dict(
    initial_rate=0.8,
    obs_every=20,
    obs_noise=0.005,
    control_margin=0.01,
    basin=0.12,
    regime_accel_noise=0.0,
    regime_rate_damping=0.0,
    q_rate=1e-5,
    q_level=1e-6,
    q_level_only=1e-6,
    steps=350,
)

NEIGHBORHOOD = {
    "initial_rate": [0.5, 0.8, 1.1],
    "obs_every": [10, 20, 40],
    "obs_noise": [0.005, 0.01, 0.02],
    "control_margin": [0.005, 0.01, 0.02],
    "basin": [0.10, 0.12, 0.15],
    "regime_accel_noise": [0.0, 0.005, 0.02],
    "regime_rate_damping": [0.0, 0.005, 0.015],
}

SEEDS = list(range(1, 16))


def passes(m: r3.RunMetrics, cfg: r3.Config) -> bool:
    return m.basin_occupancy >= cfg.t_basin and m.mean_abs_error <= cfg.t_calib_error


def ratio(m: r3.RunMetrics, full: r3.RunMetrics) -> float:
    return m.mean_abs_error / max(full.mean_abs_error, 1e-12)


def degraded(m: r3.RunMetrics, full: r3.RunMetrics, cfg: r3.Config) -> bool:
    return m.basin_occupancy < cfg.t_basin or ratio(m, full) > cfg.t_rate_lesion_ratio


def eval_seed(cfg: r3.Config) -> dict:
    full, _ = r3.run_full(cfg)
    lesions = {name: r3.run_full(cfg, lesion=name)[0] for name in DIRECT_LESIONS}
    return {
        "seed": cfg.seed,
        "full": asdict(full),
        "full_pass": passes(full, cfg),
        "lesions": {name: asdict(m) for name, m in lesions.items()},
        "ratios": {name: ratio(m, full) for name, m in lesions.items()},
        "degraded": {name: degraded(m, full, cfg) for name, m in lesions.items()},
        "all_direct_degraded": all(degraded(m, full, cfg) for m in lesions.values()),
        "any_direct_degraded": any(degraded(m, full, cfg) for m in lesions.values()),
    }


def eval_config(kwargs: dict, seeds: List[int] = SEEDS) -> dict:
    seed_rows = []
    for s in seeds:
        cfg = r3.Config(**{**asdict(r3.Config()), **kwargs, "seed": s})
        seed_rows.append(eval_seed(cfg))
    full_pass_rows = [row for row in seed_rows if row["full_pass"]]
    all_degraded_rows = [row for row in seed_rows if row["full_pass"] and row["all_direct_degraded"]]
    any_degraded_rows = [row for row in seed_rows if row["full_pass"] and row["any_direct_degraded"]]
    per_lesion = {}
    for name in DIRECT_LESIONS:
        valid = [row for row in seed_rows if row["full_pass"]]
        ratios = [row["ratios"][name] for row in valid]
        per_lesion[name] = {
            "degrade_fraction_given_full_pass": (sum(row["degraded"][name] for row in valid) / len(valid)) if valid else 0.0,
            "median_error_ratio_given_full_pass": statistics.median(ratios) if ratios else None,
            "min_error_ratio_given_full_pass": min(ratios) if ratios else None,
            "max_error_ratio_given_full_pass": max(ratios) if ratios else None,
        }
    return {
        "config": kwargs,
        "n_seeds": len(seeds),
        "full_pass_fraction": len(full_pass_rows) / len(seeds),
        "all_direct_degraded_fraction_all_seeds": len(all_degraded_rows) / len(seeds),
        "all_direct_degraded_fraction_given_full_pass": (len(all_degraded_rows) / len(full_pass_rows)) if full_pass_rows else 0.0,
        "any_direct_degraded_fraction_given_full_pass": (len(any_degraded_rows) / len(full_pass_rows)) if full_pass_rows else 0.0,
        "per_lesion": per_lesion,
        "seed_rows": seed_rows,
    }


def grid_neighborhood(limit: int | None = None) -> List[dict]:
    keys = list(NEIGHBORHOOD)
    out = []
    for vals in itertools.product(*(NEIGHBORHOOD[k] for k in keys)):
        kw = dict(BASE_OP)
        kw.update(dict(zip(keys, vals)))
        out.append(kw)
        if limit and len(out) >= limit:
            break
    return out


def score(item: dict) -> Tuple[float, float, float]:
    return (
        item["full_pass_fraction"],
        item["all_direct_degraded_fraction_given_full_pass"],
        min((item["per_lesion"][name]["degrade_fraction_given_full_pass"] for name in DIRECT_LESIONS), default=0),
    )


def main() -> None:
    # 1. exact operating point, many seeds
    exact = eval_config(BASE_OP, SEEDS)

    # 2. neighborhood grid, fewer seeds first for breadth
    breadth_seeds = list(range(1, 6))
    grid = grid_neighborhood()
    rng = random.Random(11)
    grid = rng.sample(grid, min(60, len(grid)))
    grid_rows = [eval_config(kw, breadth_seeds) for kw in grid]
    grid_rows.sort(key=score, reverse=True)

    # 3. retest top candidates on 30 seeds
    retest = [eval_config(row["config"], SEEDS) for row in grid_rows[:8]]
    retest.sort(key=score, reverse=True)

    # 4. identify robust/passable sets
    robust_all = [r for r in retest if r["full_pass_fraction"] >= 0.9 and r["all_direct_degraded_fraction_given_full_pass"] >= 0.9]
    robust_any = [r for r in retest if r["full_pass_fraction"] >= 0.9 and r["any_direct_degraded_fraction_given_full_pass"] >= 0.9]

    results = {
        "criteria": {
            "full_pass": "basin_occupancy >= t_basin and mean_abs_error <= t_calib_error",
            "direct_degrade": "lesion basin falls below t_basin OR lesion/full error ratio exceeds t_rate_lesion_ratio",
            "seeds": SEEDS,
            "direct_lesions": DIRECT_LESIONS,
        },
        "exact_operating_point": exact,
        "top_breadth_candidates_10_seed": grid_rows[:20],
        "top_retested_candidates_15_seed": retest[:20],
        "robust_all_direct_15_seed": robust_all,
        "robust_any_direct_15_seed": robust_any,
    }
    Path("/mnt/data/r3_rate_arm_robustness_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

    lines = []
    lines.append("R^3 direct rate-arm robustness battery")
    lines.append("Criterion: direct lesion of the same full controller, not full-vs-level-only.")
    lines.append("")
    lines.append("Exact operating point:")
    lines.append(str(BASE_OP))
    lines.append(f"  full_pass_fraction: {exact['full_pass_fraction']:.3f}")
    lines.append(f"  all_direct_degraded_fraction_given_full_pass: {exact['all_direct_degraded_fraction_given_full_pass']:.3f}")
    lines.append(f"  any_direct_degraded_fraction_given_full_pass: {exact['any_direct_degraded_fraction_given_full_pass']:.3f}")
    for name in DIRECT_LESIONS:
        p = exact["per_lesion"][name]
        lines.append(f"  {name}: degrade_frac={p['degrade_fraction_given_full_pass']:.3f}, median_ratio={p['median_error_ratio_given_full_pass']:.2f}, min_ratio={p['min_error_ratio_given_full_pass']:.2f}")
    lines.append("")
    lines.append("Best 15-seed retests:")
    for i, row in enumerate(retest[:8], 1):
        lines.append(f"{i}. full_pass={row['full_pass_fraction']:.3f}; all_direct_given_full={row['all_direct_degraded_fraction_given_full_pass']:.3f}; any_direct_given_full={row['any_direct_degraded_fraction_given_full_pass']:.3f}")
        lines.append(f"   config={row['config']}")
        for name in DIRECT_LESIONS:
            p = row["per_lesion"][name]
            lines.append(f"   {name}: degrade_frac={p['degrade_fraction_given_full_pass']:.3f}, median_ratio={p['median_error_ratio_given_full_pass']:.2f}, min_ratio={p['min_error_ratio_given_full_pass']:.2f}")
    lines.append("")
    lines.append(f"robust_all_direct_15_seed_count: {len(robust_all)}")
    lines.append(f"robust_any_direct_15_seed_count: {len(robust_any)}")
    if robust_all:
        lines.append("Verdict: robust all-direct rate-arm load-bearing point found under the stated thresholds.")
    elif robust_any:
        lines.append("Verdict: at least one direct rate-arm dependence is robust, but all-direct dependence is not.")
    else:
        lines.append("Verdict: no robust direct rate-arm load-bearing point found in this neighborhood.")
    Path("/mnt/data/r3_rate_arm_robustness_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
