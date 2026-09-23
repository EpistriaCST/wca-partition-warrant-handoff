# R³ exploratory sequence

**Status:** exploratory; informative but not the missing modular witness.

R³ introduced a three-dimensional loop state with a regime level and rate estimate, then applied direct lesions, parameter search, oblique-frame stress tests, and an off-trajectory autonomy probe.

The sequence matters because its intermediate labels can mislead when separated from the later tests:

1. The initial harness reported same-dimensional discrimination at one construction.
2. Parameter search found operating points where direct rate-arm lesions degraded performance, including a candidate with intact basin occupancy `1.000` and mean absolute error about `0.0043`; selected lesions raised error by approximately `2204x`, `5.49x`, and `5.07x` at that point.
3. Robustness testing found neighborhoods with direct rate-arm dependence under the stated thresholds.
4. The oblique-frame replay/projection sweep admitted 60 viable planes and therefore returned `FAILED/UNDECIDED` at that stage.
5. The autonomy probe rejected all 60 as trajectory-huggers: they followed the intact path but did not restore under perturbations internal to their own planes.

The final limit is decisive: these were projection and autonomy stress tests on a single constructed loop, not a new modular physical substrate containing a genuine proper sub-closure and a matched mis-governed rival. They therefore do not close WCA-01.

## Reproduction warning

The scripts are preserved as recovered and several retain paths from the original execution environment, including `/mnt/data`. Run them in a disposable environment and inspect output paths before execution. The generated JSON files and summaries needed to inspect the recorded sequence are included; redundant ZIP bundles are not.

## Suggested reading order

1. `results/r3_wca_summary.txt`
2. `results/r3_rate_arm_search_summary.txt`
3. `results/r3_rate_arm_robustness_summary.txt`
4. `results/r3_oblique_frame_sweep_summary.txt`
5. `results/r3_oblique_autonomy_probe_summary.txt`
