**Closure-Activation Partition-Warrant on a Single-Loop Substrate: A
Recursive Maintained-Maintainer Witness for Specificity and
Frame-Invariance**

**Charles S. Thomas**

*Epistria LLC · ORCID: 0009-0007-6330-1053*

19 June 2026

DOI: 10.5281/zenodo.20767308

**Abstract**

We report a constructive witness for closure-activation
partition-warrant (W_CA) on a non-biological single-loop substrate,
built to discharge two recorded vulnerabilities and bounded explicitly
against a third it does not reach. The controller is a genuine
maintained-maintainer rather than a feedback law: its calibration is
sustained only by the plant's in-basin response, control and
observability share one channel, and no excitation is injected, so the
plant-to-controller arm is load-bearing. Boundary lesions confirm mutual
maintenance, since severing either arm collapses both, and the asymmetry
between the deterministic controller collapse and the
regime-path-dependent plant collapse is reported rather than smoothed.
Two claims are established. Specificity: a passively-stable substrate
carrying the same estimator is declined under every carving, discharging
the worry that the warrant certifies mere persistence. Frame-invariance:
the conditions are coordinate-free ratios whose verdict is invariant
under controller-coordinate rescaling and monotone time
reparametrization, where an absolute formulation would flip, which
closes the recorded G-invariance gap. The warrant's rejection of
improper carvings is robust across the full bounded-condition-number
frame family and across the enforcement threshold, so its specificity is
frame- and threshold-robust. Three things are not established and are
stated as such: sensitivity, which is the C₀ problem and remains
untouched; joint sufficiency, since collapse-of-both is necessary but
not sufficient; and discrimination, the selection of a bearer among
several genuine closure-bearing carvings, since a single fully-coupled
loop admits exactly one. The governance criterion is therefore shown
specific but not yet admitting. Demonstrating its admit-direction, and
discrimination with it, requires a modular substrate and is left as a
distinct sub-problem.

**Keywords.** closure activation; partition warrant; W_CA; closure under
maintenance; recursive maintenance; maintained maintainer;
frame-invariance; individuation; specificity; non-biological substrate

**1. Objective**

The partition-evaluative predicate W_CA and its verdict structure are
specified in Closure Activation as Partition-Warrant \[1\]; the present
witness instantiates its selection-mode behavior on a constructed
substrate, the companion-program work that paper forwards. The build is
a soundness and specificity test of a recursive closure-activation
witness on a non-biological substrate. The controller is rebuilt as a
genuine maintained-maintainer: a closed mutual-maintenance loop rather
than a memoryless feedback law. The two ledger items it was meant to
discharge were the isolation-persistence vulnerability, the worry that
W_CA false-positives on systems that persist passively, and the
G-invariance gap, the worry that the verdict depends on the coordinate
frame. It was never intended as a sufficiency proof, and the C₀
sensitivity problem was out of scope from the outset.

**2. Substrate and coupling**

The plant is open-loop unstable and stays viable only while the
controller's estimate of a drifting regime parameter remains calibrated.
The regime is observable only through the in-basin closed-loop response:
control and observability share the ψ channel, so out of basin the
parameter is unobservable and control authority vanishes together.
Excitation is the intrinsic plant noise. No dither is injected, so the
controller earns its information from the plant rather than
manufacturing it, which is what keeps the plant-to-controller arm
load-bearing.

**3. What the witness establishes**

**Specificity.** A linear, passively-stable plant carrying the same
estimator machinery is rejected under every carving. Its correction is
not load-bearing, since the plant stays in basin with control removed,
so C2 fails and τ₀ = 0. This is the isolation-persistence worry
discharged: the predicate declines to certify passive persistence.

**Mutual maintenance.** Both lesions collapse both arms. Severing the
plant-to-controller edge collapses the controller's calibration on every
seed (uncertainty blows up ~30×), and severing the controller-to-plant
edge drives the plant out of basin (occupancy → ~0.03) with calibration
following as observability is lost. The collapse is asymmetric and
reported as such: the controller collapse is deterministic, the plant
collapse under the information lesion is regime-path-dependent, escaping
when the random walk carries the regime past the stale estimate's
competence.

**G-invariance.** The three conditions are stated in coordinate-free
terms, ratios in which a controller-coordinate rescale cancels. The
verdict is invariant under both a controller-coordinate transform and a
monotone time reparametrization. The probe also demonstrates that a
naive absolute-uncertainty threshold would flip under rescaling while
the ratio formulation does not, which is the concrete sense in which the
gap is closed.

**Selection.** Selection is clean against the full family of
bounded-condition-number carvings, not only the trivial axis-aligned
split. This required hardening C2 to recognize the carving projection
itself as external governance: a constrained block is internally
governed only when its boundary is approximately a dynamical invariant,
so the projection does negligible work. Every proper split suppresses at
least 29% of its free motion through the projection, while the undivided
loop suppresses none, so the verdict is invariant to the enforcement
threshold anywhere in (0, 0.29). Selection is therefore frame-robust and
threshold-robust on this substrate.

**4. What the witness does not establish**

**Sensitivity.** One positive and one negative substrate demonstrate
specificity. They do not show that W_CA fires on every genuine
closure-bearer. That is the C₀ problem and it remains untouched.

**Joint sufficiency.** Collapse-both is necessary, not sufficient. Two
coupled estimators could exhibit it without being closure-bearing in the
full sense, so the verdict is taken from the predicate on the
organization-fixed block, not from the symmetry of the loop.

**Multi-candidate selection.** A single fully-coupled maintenance loop
has exactly one closure-bearing carving, itself. The selection apparatus
has been exercised only where the answer is foreordained. Its
discriminating power, the capacity to select among several genuinely
closure-bearing carvings and to admit a proper sub-closure, is untested
here.

**5. The R³ boundary**

The natural next test is a higher-dimensional controller, to check
whether W_CA rejects a full-dimensional but mis-governed competitor
block rather than only lower-dimensional ones. This was attempted with a
constant-velocity estimator carrying both a regime level and a regime
rate.

It came out decorative. A level-only estimator holds basin identically
to the full level-and-rate estimator at every parameter setting tried,
and the rate state in fact degraded tracking, because the rate is only
weakly observable and its noise propagates into the level estimate. Two
structural facts explain this. The plant is forgiving: transient
tracking lag reaches several regime units against a control margin of
0.20 without the plant leaving basin, because the coupling channel
saturates and supplies no restoring force outside it. And the regime is
continuously observed, so a level-only filter tracks with bounded lag
unaided.

The diagnosis generalizes and fixes the stopping point. On a single
fully-coupled maintenance loop the end game is set by coupling alone:
the only boundary that is a dynamical invariant is the whole loop, so
every proper sub-block is rejected regardless of its dimension or how
the coordinates are split. Adding degrees of freedom multiplies
instances of the same rejection rather than producing a new verdict, and
two independent regime parameters would not change this. R³ is therefore
the documented boundary of the present work.

**6. Soundness-sensitive operationalization choices**

These carry the weight and are recorded for audit. The causal-support
graph is proxied by boundary-isolation lesions. The numeric thresholds
are set by hand: basin occupancy 0.80, C3 uncertainty ratio 0.50, C1
path-dependence ratio 0.20, and C2 enforcement fraction 0.15, with
selection invariant to the last anywhere in (0, 0.29). C1 is
operationalized as the persistence of configuration-relative calibration
tracks, normalized by the perturbation that produced them. C3 uses the
intact-over-starved uncertainty ratio, which is the coordinate-free form
that closes the G-invariance gap. The C2 hardening uses projection work
measured in frame coordinates; its specificity is demonstrated, since it
rejects every imposed carving, but its admit-direction is argued rather
than demonstrated, because this substrate contains no genuine nested
sub-closure for it to admit.

**7. Status**

This is a constructive close on the positive-selection open problem for
a single-loop, non-biological substrate, with the isolation-persistence
and G-invariance gaps shut. Multi-candidate selection via a modular
substrate, and the corresponding test of the enforcement criterion's
admit-direction, are a distinct sub-problem. They are recorded as future
work and are not pursued here.

**8. Code and data availability**

The witness is implemented in three files, archived with this deposit.
wca_claim2.py specifies the substrate, the partitions, and the
operational predicate. probes.py implements the probe suite with its
pre-committed kill rules. frame_sweep.py runs the computed selection
test across the carving-frame family.

**References**

\[1\] Thomas, C. S. Closure Activation as Partition-Warrant: A Two-Axis
Resolution to Metric-Preserving Identity Underdetermination. Zenodo,
2026. DOI: 10.5281/zenodo.20114054.
