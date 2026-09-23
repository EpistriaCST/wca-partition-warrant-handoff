# Supplementary recovered R³ branch

**Status:** preserved as supplied; repository dependency recovered; recorded results independently reproduced on 23 September 2026.

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

The supplied CSV contains one undivided-organization row and 36 same-dimensional competitor rows across twelve frames. The undivided organization has `tau0 = 1`; every competitor row has `tau0 = 0`. After recovery of the canonical base file, `sweep_chunk.py 0 12` regenerated the supplied CSV byte-for-byte, including SHA-256 `ab093b5f7daac185cad8a7efa73c88237a770cd3e528f287d5da6abe402b747b`.

## Dependency boundary

`wca_claim2_r3.py` imports `THRESH` from `wca_claim2.py`. The canonical base file is now preserved under `experiments/single-loop/src/`; this directory remains intentionally non-duplicative rather than self-contained. Run it with that directory on `PYTHONPATH`.

The gated `battery_r3.py` run admitted the organization, rejected the same-dimensional pseudo-unit, and rejected the passive negative control. The supplied Python files pass syntax compilation. No claim is made that this branch precedes, supersedes, or is numerically equivalent to the later standalone R³ code solely on the basis of filenames.
