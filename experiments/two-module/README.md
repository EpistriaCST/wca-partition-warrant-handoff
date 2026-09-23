# Two-module proper-subclosure test

**Status:** design only; nothing has been built or run.

This is the preferred next experiment because it targets the precise gap left by the single-loop witness: **admit-direction**. The single loop could reject improper carvings but contained no genuine proper sub-closure to admit.

The test uses two independently validated plant–controller maintenance loops joined under three coupling conditions. The evaluator must admit the modular partition, reject same-dimensional cross-cuts, and depart from a computed minimum-coupling partition in the strong-passive-link condition.

Read the full [design specification](design-spec.md) and WCA-01 in the repository's [open-problem register](../../OPEN_PROBLEMS.md).

## Remaining issue before implementation

The canonical single-loop C2 calculation is now recovered. For each one-dimensional block in a two-coordinate carving frame, it divides accumulated motion suppressed in the frozen complementary coordinate by that suppressed motion plus accumulated free motion in the block's own coordinate. C2 requires the ratio to be below `0.15`; the reproduced split minimum rounded to `0.29`.

That scalar construction does not uniquely determine a higher-dimensional module rule. Before implementation, freeze the norm, coordinate scaling, complement projection, and time/coordinate aggregation. Treat those choices as an explicit extension of the deposited operationalization, not as its unchanged application.

## Minimum deliverables

1. A preregistration or timestamped protocol with evaluator, thresholds, candidate partitions, transformation family, seeds, pass/fail/void rules, and planned robustness sweeps.
2. Source code and environment lock file.
3. Raw and summarized outputs for all runs.
4. Independent module-validation results.
5. A comparison against minimum coupling, a Markov-blanket-like partition where definable, and the cross-cut family.
6. A change log identifying every departure from the design specification.
