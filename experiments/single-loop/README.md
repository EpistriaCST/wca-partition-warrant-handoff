# Canonical single-loop witness

**Status:** author-supplied source package recovered and behaviorally verified on 23 September 2026.

These are the three exact filenames identified in the deposited single-loop witness. The recovered files are preserved unchanged under [`src/`](src/).

| File | Role | SHA-256 |
| --- | --- | --- |
| `wca_claim2.py` | Substrate, partitions, operational predicate, and thresholds | `e2b88c4c0a1343e30ebe51acf737dd8273ad7e466b945560d8c6953806fc6fce` |
| `probes.py` | Five precommitted selection, control, lesion, and invariance probes | `c916dbf29d41d0ff08a134fcdc46d0f49f6bc10f9a4149a63e61376bd7cca9f6` |
| `frame_sweep.py` | Bounded-condition-number carving-frame selection test | `ca5beab1f9173ee18ce4a6931bf29b4c82d1846c5c4175087777a114fa913d84` |

## Verification

The files were executed unchanged in a temporary directory using Python 3.12.14 and NumPy 2.3.5.

`python probes.py` completed successfully. The positive organization was admitted with `tau0 = 1` and `mu* = 0.75`; both split blocks rejected; the passively stable negative control rejected; both directional lesion tests passed; and the coordinate-rescaling and monotone-time-reparameterization checks did not flip the verdict.

`python frame_sweep.py` completed successfully. The undivided organization was admitted, all 60 blocks across 30 admissible frames rejected, and the minimum observed enforcement fraction rounded to `0.29`, reproducing the paper's reported threshold-robust interval `(0, 0.29)`.

One non-operative wording discrepancy remains in the preserved source: the inline `THRESH` comment in `wca_claim2.py` says the splits exceed `0.26`, while the executed `frame_sweep.py` and deposited paper report a rounded minimum of `0.29`. The implemented threshold is `0.15` in either case, so this comment does not change the verdict or the reproduced output.

The author supplied these files as the canonical package. Their hashes are recorded here and in the repository manifest. Byte identity with the remote Zenodo file objects was not independently checked because a remote checksum manifest was not available during assembly.

## Scope

This reproduction supports the deposited single-loop witness on its stated thin two-coordinate substrate. It does not establish proper-subclosure admission, same-dimensional modular discrimination, general sufficiency, or validity outside the tested transformation family.
