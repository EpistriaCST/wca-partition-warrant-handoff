# Two-module proper-subclosure test

**Status:** design only; nothing has been built or run.

This is the preferred next experiment because it targets the precise gap left by the single-loop witness: **admit-direction**. The single loop could reject improper carvings but contained no genuine proper sub-closure to admit.

The test uses two independently validated plant–controller maintenance loops joined under three coupling conditions. The evaluator must admit the modular partition, reject same-dimensional cross-cuts, and depart from a computed minimum-coupling partition in the strong-passive-link condition.

Read the full [design specification](design-spec.md) and WCA-01 in the repository's [open-problem register](../../OPEN_PROBLEMS.md).

## Blocking issue before implementation

The current design draft contains a placeholder for the exact canonical C2 enforcement ratio. The single-loop paper records the threshold `0.15` and reports robustness throughout `(0, 0.29)`, but the named deposited source files were not recovered with the local materials.

Do not substitute a convenient new ratio without declaring a new operationalization. Recover and freeze the deposited formula first, or explicitly register the experiment as a test of a revised C2 rule.

## Minimum deliverables

1. A preregistration or timestamped protocol with evaluator, thresholds, candidate partitions, transformation family, seeds, pass/fail/void rules, and planned robustness sweeps.
2. Source code and environment lock file.
3. Raw and summarized outputs for all runs.
4. Independent module-validation results.
5. A comparison against minimum coupling, a Markov-blanket-like partition where definable, and the cross-cut family.
6. A change log identifying every departure from the design specification.
