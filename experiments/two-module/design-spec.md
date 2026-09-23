> **Archival handoff notice (updated 23 September 2026).** This is an unbuilt design, not a preregistration or result. The canonical single-loop C2 source is now recovered: its scalar two-coordinate enforcement fraction uses threshold `0.15`, with the reproduced negative-carve verdict invariant throughout `(0, 0.29)`. The source does not uniquely specify a higher-dimensional generalization. Any module-level norm, coordinate scaling, complement projection, or aggregation rule must therefore be frozen and declared as an extension before implementation.

**Admitting a Proper Sub-Closure Without Labels**

A two-module test specification for the closure-activation partition
warrant (draft for critique)

Charles S. Thomas · ORCID 0009-0007-6330-1053 · September 2026. Nothing
has been built; this is the design to be attacked.

1\. The problem

A single-loop witness (Thomas, 2026; zenodo.20767308) showed the
partition warrant W_CA to be specific: it declines every carving of a
passively stable substrate, and its verdict is invariant under
controller rescaling and monotone time reparametrization. It could not
show the warrant admitting anything by discrimination, because a single
fully coupled loop has exactly one genuine carving. Two things remain
open:

- **Admit-direction.** W_CA must certify a genuine proper sub-closure,
  not only a whole.

- **Discrimination.** It must prefer that carving over an equal-sized
  competitor that matches it on persistence, without access to which
  carving the designer intended.

The main threat here is reduction, more than circularity. If the
admitted carving is always the one with least coupling across its
boundary, W_CA is doing the work of a minimum-cut or Markov-blanket
partition. The design includes a condition where those criteria and W_CA
must come apart.

2\. Substrate

Two modules, each a plant–controller loop of the kind used in the
single-loop witness. In each module, the controller's calibration is
sustained only by the plant's in-basin response. Control and observation
share one channel, and no excitation is injected, so the
plant-to-controller arm is load-bearing. The modules are joined by an
inter-module link of strength κ. Each module also carries a budget pool
that its own in-basin operation regenerates and its controller effort
drains. The pool is what (C3) and the T\* axis read.

|                        |                                                                                                                                                                                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Condition**          | **Construction and purpose**                                                                                                                                                                                                                                 |
| A: weak link           | κ small and passive. The baseline admit/discriminate case.                                                                                                                                                                                                   |
| B: strong passive link | κ large but purely mechanical: it transmits force and carries no calibration or budget. Within each module the maintenance arms are weak but load-bearing. Here the minimum-coupling partition differs from the modular one. This is the non-reduction test. |
| C: shared budget       | The link carries part of each module's budget. Descriptive: each module should come out internally governed but under-resourced (closure-competent).                                                                                                         |

3\. Candidate partitions

All subsystems within a partition have equal dimension.

- **P⁺ (modular):** module 1 \| module 2.

- **P⁻ (cross-cut):** (plant 1, controller 2) \| (plant 2, controller
  1), plus a bounded family of orthogonal mixtures of corresponding
  coordinates across modules (condition number ≤ a pre-set bound).

- **P_mc (minimum coupling):** the equal-size bipartition minimizing
  summed absolute cross-boundary entries of the time-averaged Jacobian.
  Computed, not chosen. It coincides with P⁺ in A and should differ from
  it in B.

4\. The evaluator (frozen before any parameter is set)

The evaluator receives state trajectories and a candidate partition. It
receives no module labels, and it treats every subsystem of every
partition identically.

1.  **Replay lesion.** For subsystem S, record the complement's
    trajectory from an intact run, then rerun with the complement
    replayed open-loop. Its influence on S keeps the same time course
    but no longer responds to S. Any maintenance loop that runs through
    the complement is cut; the input statistics are not. This operation
    is defined for any S and never refers to "arms." *(Proposed here;
    the single-loop witness used designed-arm lesions.)*

2.  **(C2) enforcement.** In the recovered single-loop source, one
    frame coordinate is free and its complement is frozen. The
    enforcement fraction is accumulated motion suppressed in the
    frozen coordinate divided by that suppressed motion plus
    accumulated free motion in the block's own coordinate, with C2
    requiring a value below 0.15. Applying this idea to a
    higher-dimensional S requires a prespecified norm, coordinate
    scaling, complement projection, and time/coordinate aggregation.
    Those choices must be frozen before parameter search and reported
    as an extension of the deposited scalar rule, not as an unchanged
    application.

3.  **(C1) state-referentiality.** The perturbation discriminator:
    recovery trajectories must differ across perturbations targeting
    different aspects of S's own constraint, and must depend on S's
    prior configuration, not only its current state.

4.  **(C3) budget and T\*.** τ₀ is read from (C1) and (C2) under replay.
    The maintenance margin μ\* is read off a graded load series that
    drains S's budget pool. Closed and closure-competent are separated
    by whether the pool sustains enforcement over the operating
    timescale.

5\. Substrate validation (independent of W_CA)

These checks establish on design grounds that the P⁺ modules are genuine
sub-closures, before any verdict is read. If they fail, the run is void.

- Cutting an intra-module arm collapses that module.

- Cutting the inter-module link leaves both modules viable (A and B).

- Restoring a cut arm returns the module to its basin.

6\. Pass and fail

|               |                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| **Criterion** | **Requirement**                                                                                                              |
| Admit         | Both P⁺ subsystems return τ₀ = 1 in A and B, at every nominal setting and in at least 90% of sweep cells.                    |
| Reject        | Every P⁻ subsystem, across the whole cross-cut family and every sweep cell, returns τ₀ = 0. One admission is a fail.         |
| Non-reduction | In B, P_mc ≠ P⁺, W_CA rejects P_mc and admits P⁺. If P_mc = P⁺ in B, condition B is void and must be redesigned, not scored. |
| Invariance    | Verdicts unchanged under controller rescaling, monotone time reparametrization and seeds.                                    |

**Scope of a fail:** this evaluator, this substrate. A fail bears on the
admit-direction of the deposited (C2) rule, not on the warrant as a
whole.

7\. What I'm asking you to attack

1.  Does the replay lesion plus the (C2) ratio reduce to something
    already known: transfer entropy, a blanket partition under
    nonequilibrium conditions, or a minimum-cut criterion? Is condition
    B enough to separate them?

2.  Is the controller in each module doing regulation (second-order
    control of its own first-order dynamics) or only feedback? If the
    latter, the substrate does not instantiate what (C2) is meant to
    capture.

3.  Is the cross-cut family a strong enough competitor? What carving
    would you use to embarrass the warrant?
