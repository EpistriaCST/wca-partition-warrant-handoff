"""Parameter-space probe for honest R^3 rate-arm load-bearing points.

Run from the same directory as r3_wca_harness.py:
    python r3_rate_arm_search.py

It searches for configurations where the intact full controller passes, while
DIRECT rate-arm lesions degrade that same controller.  This is intentionally
stricter than comparing the full controller against a separate level-only model.
"""
from __future__ import annotations

import json, random
from dataclasses import asdict
from pathlib import Path

import r3_wca_harness as r3

FIELDS = {
    "initial_rate": [0.1, 0.2, 0.35, 0.5, 0.8],
    "regime_accel_noise": [0.0, 0.005, 0.02, 0.05],
    "regime_rate_damping": [0.0, 0.005, 0.015, 0.05],
    "obs_every": [10, 20, 40, 80],
    "obs_noise": [0.005, 0.01, 0.02, 0.04],
    "control_margin": [0.002, 0.005, 0.01, 0.02],
    "basin": [0.12, 0.15, 0.25],
    "q_rate": [1e-5, 1e-4, 5e-4, 1e-3],
    "q_level": [1e-6, 1e-5, 1e-4],
    "q_level_only": [1e-6, 1e-5, 1e-4],
}

DIRECT_LESIONS = ["freeze_rate_prediction", "freeze_rate_state", "cut_rate_update"]

def passes(m: r3.RunMetrics, cfg: r3.Config) -> bool:
    return m.basin_occupancy >= cfg.t_basin and m.mean_abs_error <= cfg.t_calib_error

def degraded(m: r3.RunMetrics, full: r3.RunMetrics, cfg: r3.Config) -> bool:
    ratio = m.mean_abs_error / max(full.mean_abs_error, 1e-12)
    return m.basin_occupancy < cfg.t_basin or ratio > cfg.t_rate_lesion_ratio

def evaluate(cfg: r3.Config) -> dict | None:
    full, _ = r3.run_full(cfg)
    if not passes(full, cfg):
        return None
    lesions = {name: r3.run_full(cfg, lesion=name)[0] for name in DIRECT_LESIONS}
    bad = {name: m for name, m in lesions.items() if degraded(m, full, cfg)}
    if not bad:
        return None
    level = r3.run_level_only(cfg)
    return {
        "config": asdict(cfg),
        "full": asdict(full),
        "level_only": asdict(level),
        "lesions": {k: asdict(v) for k, v in lesions.items()},
        "degraded_direct_lesions": list(bad.keys()),
        "ratios": {k: v.mean_abs_error / max(full.mean_abs_error, 1e-12) for k, v in lesions.items()},
    }

def search(samples: int = 300, steps: int = 500, seed: int = 4) -> list[dict]:
    base = asdict(r3.Config())
    rng = random.Random(seed)
    out = []
    keys = list(FIELDS)
    for _ in range(samples):
        kw = dict(base)
        for k in keys:
            kw[k] = rng.choice(FIELDS[k])
        kw["steps"] = steps
        item = evaluate(r3.Config(**kw))
        if item:
            score = max(item["ratios"].values()) + len(item["degraded_direct_lesions"])
            item["score"] = score
            out.append(item)
    out.sort(key=lambda x: x["score"], reverse=True)
    return out

if __name__ == "__main__":
    hits = search()
    Path("/mnt/data/r3_rate_arm_search_results.json").write_text(json.dumps(hits[:20], indent=2), encoding="utf-8")
    print(f"hits: {len(hits)}")
    for h in hits[:5]:
        c = h["config"]
        print("\nscore", round(h["score"], 3), "degraded", h["degraded_direct_lesions"])
        print({k: c[k] for k in list(FIELDS) + ["steps"]})
        print("full", h["full"])
        print("ratios", {k: round(v, 2) for k, v in h["ratios"].items()})
