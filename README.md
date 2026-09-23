# W_CA Partition-Warrant Research Handoff

This repository preserves the current state of **closure activation as a partition warrant** (`W_CA`) and makes its unresolved tests available for independent continuation.

The originating research program ended at its present boundary on 22 September 2026. This repository is therefore an archival handoff, not an active laboratory, a claim of validation, or a promise of author support.

## The problem

Many frameworks evaluate persistence, consciousness, integration, agency, or control only after a system boundary has been selected. If several partitions of the same substrate preserve the observables used by the framework, those observables cannot by themselves warrant which partition contains the system being evaluated.

`W_CA` is one candidate for the logically prior partition-warrant slot. It evaluates each subsystem induced by a candidate partition using three proposed activation conditions:

1. **C1 — state-referential constraint:** the corrective target is specified over the subsystem's own state-space coordinates.
2. **C2 — internally governed corrective response:** initiation, targeting, and termination of correction are governed from within the imposed boundary.
3. **C3 — internally viable maintenance budget:** internally governed resources can sustain the corrective dynamics over the operating timescale.

For subsystem `S` under partition `P`, the proposed verdict is

```text
W_CA(P, S) = (tau_0(S), mu*(S), kappa(S))
```

where `tau_0` records activation, `mu*` is a graded maintenance-margin profile, and `kappa` classifies the subsystem as `closed`, `closure-competent`, or `subthreshold`.

`W_CA` is a structural candidate. It is not presented here as unique, generally sufficient, empirically validated across substrate classes, or as a consciousness criterion.

## Current evidence state

| Item | Status | What it supports | What it does not support |
| --- | --- | --- | --- |
| Formal predicate and falsifiers | **Specified** | A partition-relative candidate with explicit non-claims and failure conditions | Empirical adequacy |
| Rejection-mode witness | **Demonstrated at the stated construction** | Uniform negative verdicts where no carve is closure-bearing | Positive selection |
| Single-loop maintained-maintainer witness | **Constructive, bounded result** | Specificity against passive persistence and invariance under the tested frame family | Proper-subclosure admission, multi-candidate discrimination, sensitivity, or joint sufficiency |
| R³ experiments | **Exploratory; method-limited** | Useful lesion, frame-stress, and autonomy diagnostics | A modular autonomous-substrate demonstration |
| RAF route | **Drafted, not deposited or run; not recommended as the main test** | A possible RAF–`W_CA` concordance study | Independent positive selection or a decisive test of `W_CA` |
| Two-module witness | **Specified, not built** | The clearest current design for proper-subclosure admission and non-reduction | Any result until implemented and attacked |
| Stratification mode | **Open** | A stated target involving differential `mu*` profiles across nested closure-bearing partitions | An operational protocol or demonstration |

The detailed claim ledger is in [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md). The prioritized research tasks and failure criteria are in [OPEN_PROBLEMS.md](OPEN_PROBLEMS.md).

## Best point of entry

The highest-value continuation is the [two-module test](experiments/two-module/README.md). It asks whether `W_CA` can admit a genuine proper sub-closure while rejecting a same-dimensional cross-cut rival, and whether it can do so when a minimum-coupling or Markov-blanket-like partition points elsewhere.

That design is intentionally not ready to run. One canonical implementation detail remains unresolved in the recovered materials: the exact deposited C2 enforcement ratio must be recovered and frozen before parameters are chosen. The threshold reported by the single-loop witness is `0.15`, with the negative-carve result invariant across thresholds in `(0, 0.29)`. An exploratory R³ implementation used a blocked-motion fraction, but this repository does not silently promote that later implementation into the canonical rule.

## Repository map

- [`docs/primary/`](docs/primary/) contains Markdown renderings of the formal paper and single-loop witness.
- [`OPEN_PROBLEMS.md`](OPEN_PROBLEMS.md) states the remaining work as testable research tasks.
- [`experiments/two-module/`](experiments/two-module/) contains the preferred next-test specification.
- [`experiments/r3/`](experiments/r3/) preserves exploratory code and result summaries with their limits.
- [`experiments/raf/`](experiments/raf/) preserves the abandoned RAF route as negative methodological work.
- [`docs/SOURCES_AND_PROVENANCE.md`](docs/SOURCES_AND_PROVENANCE.md) records provenance, transformations, and known omissions.

## Primary records

- Charles S. Thomas, *Closure Activation as Partition-Warrant: A Two-Axis Resolution to Metric-Preserving Identity Underdetermination*. DOI: [10.5281/zenodo.20114054](https://doi.org/10.5281/zenodo.20114054)
- Charles S. Thomas, *Closure-Activation Partition-Warrant on a Single-Loop Substrate: A Recursive Maintained-Maintainer Witness for Specificity and Frame-Invariance*. DOI: [10.5281/zenodo.20767308](https://doi.org/10.5281/zenodo.20767308)

## Reuse and attribution

Code is provided under the MIT License. Original documentation and result summaries are provided under CC BY 4.0. See [`LICENSE`](LICENSE) and [`LICENSE-DOCUMENTATION.md`](LICENSE-DOCUMENTATION.md).

If the work is extended, report negative results and changed operationalizations. A failed substrate/evaluator pair should not be rewritten into a success after inspection, and a pass should not be generalized beyond the tested substrate class.
