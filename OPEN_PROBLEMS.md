# Open problems

The list is ordered by expected information gain, not by ease. Each item is a handoff specification rather than a commitment by the originating author.

## WCA-01 — Admit a proper sub-closure without labels

**Priority:** highest.

**Question:** Can a frozen `W_CA` evaluator admit two genuine modules as proper sub-closures while rejecting an equal-dimensional cross-cut family and a computed minimum-coupling rival?

**Required construction:** Implement the three conditions in [`experiments/two-module/design-spec.md`](experiments/two-module/design-spec.md): weak passive link, strong passive link, and shared budget. Validate the modules independently of `W_CA` using intra-module lesions, inter-module lesions, and rescue.

**Precommitments:**

- recover and freeze the canonical C2 enforcement ratio before parameter search;
- set all thresholds and the permitted transformation family in advance;
- give the evaluator trajectories and candidate partitions but no module labels;
- prespecify the orthogonal/oblique cross-cut family and its condition-number bound;
- compute the minimum-coupling partition rather than choosing it;
- report every nominal setting, sweep cell, seed, void, and failure.

**Pass:** both modular subsystems are admitted in the weak- and strong-passive-link conditions; every cross-cut rival is rejected; the strong-link condition makes the minimum-coupling partition differ from the modular partition; `W_CA` rejects the former and admits the latter; verdicts are invariant under the declared transformations.

**Fail:** any cross-cut rival is admitted, a prevalidated module is rejected, or the non-reduction condition cannot be made valid. The first interpretation should be limited to the frozen evaluator and constructed substrate unless the failure directly targets a predicate-level commitment.

## WCA-02 — Test hostile false positives and joint sufficiency

Construct systems that mimic mutual dependence without being independently closure-bearing: coupled estimators, generic feedback loops, externally replenished controllers, and systems whose apparent maintenance is produced by boundary projection. Attempt to make them satisfy C1–C3.

The critical result is not another favorable witness. It is whether a deliberately adversarial construction can earn `tau_0 = 1` while lacking independently defensible closure-bearing organization.

## WCA-03 — Establish an independent positive substrate

Test a substrate whose organizational boundary is supported on grounds independent of `W_CA`. A biological cell or well-characterized regulatory network is the canonical target in the formal paper, but the experimental protocol must not use `W_CA` itself to establish the ground-truth partition.

Required outputs are the candidate-partition family, independent boundary warrant, intervention design for C1–C3, raw trajectories, negative controls, and all partition-level verdicts.

## WCA-04 — Operationalize stratification mode

Develop a protocol for a substrate with closure-bearing organization at more than one level. The target is not different binary `tau_0` verdicts; it is a principled difference in `mu*` profiles among nested admitted partitions.

The main unresolved issue is comparability. Loads, timescales, and resource margins must be normalized without erasing the scale differences the experiment is intended to detect.

## WCA-05 — Test necessity and sensitivity

Assemble independently warranted closure-bearing exemplars from more than one substrate class and ask whether each satisfies C1, C2, and C3 under reasonable, prespecified operationalizations.

A consistent false negative is evidence against joint necessity or against the selected operationalization. The two must be separated rather than repaired after observing the result.

## WCA-06 — Demonstrate the T0/T* separation

Identify closure-competent cases that cross the activation threshold but cannot sustain the maintenance regime under graded load. The intended evidence is a stable difference between the binary activation verdict and the scalar maintenance-margin profile, including any flicker or hysteresis regime.

If no such cases can be found across suitable paradigms, the two-axis structure may collapse into a single threshold.

## WCA-07 — Specify transformation-group scope

The single-loop witness tests controller rescaling, monotone time reparameterization, and a bounded-condition-number carving family. General work remains on which transformation group `G` is appropriate for a substrate class, how frame bounds are justified, and whether verdict stability survives changes in those choices.

## WCA-08 — Recover and verify the canonical single-loop source package

The single-loop paper names `wca_claim2.py`, `probes.py`, and `frame_sweep.py` as archived source files. Those files were not present in the recovered local research collection used to assemble this handoff. Retrieve them from DOI `10.5281/zenodo.20767308`, verify hashes and outputs, and add them without rewriting history. Until then, this repository contains the paper's account but cannot itself reproduce that witness.
