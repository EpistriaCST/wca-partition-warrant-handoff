# Supplementary recovered R³ branch

**Status:** preserved as supplied; dependency-incomplete; not independently reproduced during repository assembly.

These files implement a three-coordinate R³ construction distinct from the later standalone R³ sequence in the parent directory. The branch consists of:

| File | Function |
| --- | --- |
| `wca_claim2_r3.py` | Defines the stochastic substrate, three organizational coordinates, candidate partitions, and isolation flags. |
| `battery_r3.py` | Gates the partition battery on a load-bearing rate-arm lesion and a specificity control. |
| `frame_sweep_r3.py` | Defines the constrained oblique-frame evaluation. |
| `sweep_run.py` | Runs the twelve-frame sweep with two seeds per condition. |
| `sweep_chunk.py` | Runs selectable frame ranges with six seeds and appends CSV output. |
| `sweep_ns6.csv` | Preserved output from the six-seed driver. |

## Recorded result

The supplied CSV contains one undivided-organization row and 36 same-dimensional competitor rows across twelve frames. The undivided organization has `tau0 = 1`; every competitor row has `tau0 = 0`. This describes the recorded file only. The result was not regenerated during handoff assembly.

## Dependency boundary

`wca_claim2_r3.py` imports `THRESH` from `wca_claim2.py`. That base file is one of the exact sources named by the deposited single-loop witness and remains unrecovered. Consequently, this directory does not satisfy WCA-08 and is not runnable as a self-contained package. Substituting thresholds reconstructed from prose would create a new implementation rather than verify the deposited one.

The supplied Python files pass syntax compilation. No claim is made that this branch precedes, supersedes, or is numerically equivalent to the later standalone R³ code solely on the basis of filenames.
