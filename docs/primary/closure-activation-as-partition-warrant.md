# Closure Activation as Partition-Warrant: A Two-Axis Resolution to Metric-Preserving Identity Underdetermination

Charles S. Thomas

Epistria, LLC

Companion to "Persistence Without Individuation" (Thomas, 2026c)

CC BY-NC 4.0 © 2026, Charles S. Thomas

## Abstract

Paper 1 establishes that persistence-based frameworks — the Free Energy
Principle, Global Workspace Theory, and adjacent approaches — rely on
batteries of dynamical observables insufficient, on at least one
substrate where the frameworks would naturally apply them, to
individuate the systems they characterize. The supplementary structural
condition Paper 1 §7 calls a partition-warrant must be sensitive to
substrate properties not invariant under the admissible transformation
group of the dynamics. The present paper develops closure activation as
a candidate filling for that slot.

The formal predicate W_CA is partition-evaluative: for each subsystem
under a partition P, it returns a verdict structure (τ₀, μ\*, κ)
recording whether the activation event T₀ has been crossed, the
maintenance margin μ\* under graded perturbation, and the resulting
classification (closed, closure-competent, subthreshold). The activation
conditions — state-referential constraint, internally governed
corrective response, internally viable maintenance budget — are
evaluated relative to the partition's imposed boundary. The predicate's
two-axis structure (binary T₀, scalar T\*) is phase-structured in a way
that distinguishes closure activation from classical autopoietic
operational closure.

W_CA is non-G-invariant at the predicate level: the causal support graph
relative to the imposed boundary is partition-relative and not preserved
under admissible transformations. The predicate operates in three
structural modes — rejection, selection, and stratification — depending
on the substrate's closure-bearing properties under G-related
partitions. Evaluation on the Paper 1 witness yields a rejection-mode
verdict: neither partition is closure-bearing, and the uniform negative
output is the predicate's correctness behavior on a substrate where the
activation conditions cannot be satisfied under any admissible labeling.

Distinctions from optimization-based (Integrated Information Theory),
structural-definitional (Global Workspace Theory),
statistical-structural (Free Energy Principle in nonlinear regimes), and
process-based (autopoietic operational closure) alternatives are
developed structurally and by operational-mode coverage. The route ×
mode cross-tabulation supplies a meta-taxonomy for partition-warrants
more generally. Falsification conditions are stated at predicate,
verdict-structure, and discriminative-scope levels.

In conjunction with Paper 1, the present paper separates three questions
persistence-based frameworks have often conflated: what persists
dynamically, what individuates structurally, and what sustains recursive
closure. The class of closure-bearing systems is a proper subset of the
class of persistence-bearing systems under the battery characterization,
and the structural rarity of closure-bearing organization is a derivable
consequence of the activation conditions' joint stringency.

## 1. Introduction

### 1.1 The underdetermination result and the partition-warrant slot

Paper 1 (Thomas, 2026c) establishes that persistence-based frameworks —
the Free Energy Principle (Friston, 2010; Kirchhoff et al., 2018),
Global Workspace Theory (Baars, 1988; Dehaene & Changeux, 2011), and
adjacent approaches — identify their target substrates as
identity-bearing on the basis of batteries of dynamical observables that
are insufficient, on at least one substrate where the frameworks would
naturally apply them, to individuate the systems they characterize. The
witness construction is two harmonic oscillators coupled in a weak
thermal bath, admitting two substrate partitions related by an
orthogonal transformation in the dynamics' admissible transformation
group. One partition groups the substrate's degrees of freedom by
oscillator index; the other by normal-mode index. An eight-item
persistence/coherence battery — autocorrelation, return statistics,
spectral stability, transport, phase-locking, Kuramoto order parameter,
correlation-matrix coherence, broadcast-access — takes invariant values
on both partitions. The identity-sets they pick out differ. The battery
does not individuate within the transformation group, and any
individuation drawn from the battery alone is incomplete.

Paper 1 §7 names the structural condition this incompleteness implies: a
partition-warrant, defined as a constraint on admissible partitions that
selects among G-equivalent candidates on grounds the battery cannot
supply. The minimum requirement on any such warrant is that it be
sensitive to substrate properties that are not invariant under the
admissible transformation group. Three logical routes are available:
external selection principles imposed from outside the dynamics,
internally generated non-invariant properties not reducible to functions
of (L, 𝒞), or refinements of the transformation group. The existing
literature contains at least four specific proposals occupying this slot
— optimization-based (Integrated Information Theory's exclusion
postulate), structural-definitional (Global Workspace Theory's workspace
architecture), statistical-structural (the Free Energy Principle's
Markov-blanket criterion in nonlinear regimes), and process-based
(autopoietic operational closure and the closure-activation proposal of
the present paper). Paper 1 §7.5 forwards the development of the
closure-activation proposal to the present companion paper.

### 1.2 The charter and the proposal

Paper 1 §7.5 specifies the present paper's task: to develop closure
activation as a candidate partition-warrant and to show what verdict
structure it returns on the witness partitions. The two papers are
companions deposited together, with Paper 1 V2 reflecting the §7.5
wording the present development required. Discharge of the charter
requires four substantive obligations. The first is to specify the
formal predicate W_CA — what kind of object it is, how it evaluates
partitions, and what verdict structure it produces. The second is to
demonstrate that the predicate is non-G-invariant in the sense the
partition-warrant slot requires: sensitive to properties not preserved
under admissible transformations and not reducible to the
battery-internal observables of (L, 𝒞). The third is to evaluate the
predicate on the witness from Paper 1 §3 and report the verdict
structure that evaluation produces. The fourth is to distinguish the
proposed warrant from the alternative candidates surveyed in Paper 1
§7.3, both structurally and in terms of operational behavior across
substrate classes.

The proposal is closure activation, recast from its prior development as
an account of identity-onset events into a partition-evaluative
predicate. The *Mechanism of Identity Onset* paper (Thomas, 2026a)
introduced closure activation as the structural transition by which a
configuration crosses the threshold T₀ of admissible instantiation of
recursive constraint enforcement, with three jointly necessary
conditions and a tripartite classification (closed, closure-competent,
subthreshold) generated by the activation event T₀ and the
sustained-regime threshold T\*. The present paper recasts that structure
as a partition-evaluative warrant: W_CA evaluates whether the imposed
subsystem boundary of a candidate partition yields configurations of the
kind the activation conditions identify as closure-bearing. The
recasting is not a redefinition. The threshold ontology developed in
*Mechanism of Identity Onset* applies without modification; what changes
is the structural role the predicate plays. From an account of how
identity-onset takes place in already-individuated configurations, the
predicate becomes a tool for evaluating whether an imposed partition
individuates closure-bearing structure at all.

The proposal occupies route (ii) in the Paper 1 §7.2 taxonomy: an
internally generated property of the substrate, not reducible to
functions of the dynamical generator and stationary correlation
structure. Its non-G-invariance derives from sensitivity to the causal
support graph relative to the imposed partition boundary — a structural
object that is induced rather than inherent in the substrate, and that
is generally not preserved under admissible transformations even where
the verdict outputs of the predicate happen to coincide. The predicate's
two-axis structure — binary T₀ for the activation event and scalar T\*
for the sustained-regime margin — is phase-structured in a way that
distinguishes closure activation from classical autopoietic operational
closure and from the other route-occupying candidates.

### 1.3 Scope, stakes, and structure

The paper claims that closure activation is a defensible candidate
filling the partition-warrant slot, not that it is the unique correct
filling. Other candidates may be better suited to specific substrate
classes; the structural specification developed here is intended to
support comparative assessment with alternative candidates rather than
to displace them. The paper does not develop the empirical case for
closure activation's discriminative work on closure-bearing substrates;
that work is the task of companion empirical programs, including the
pre-registered anesthesia state-transition program in the corpus
(Thomas, 2026d) and cell-biology operationalization of selection-mode
protocols. Empirical demonstration is appropriately downstream of
structural specification, and the present paper limits itself to the
structural commitments the warrant requires and the falsification
conditions those commitments imply.

The paper is adjacent to broader metaphysical discussions of
individuation and persistence, but its target is narrower: the
methodological problem of partition attribution within persistence-based
frameworks. The literature on the metaphysics of individuation — the
question of what makes a thing one thing as opposed to another, or many
— is engaged here only insofar as the partition-warrant slot is itself
an individuation question by that literature's standards. Whether
closure activation can serve as a metaphysical account of individuation
more broadly is a separate question that this paper does not take up.

The structural achievement the paper enables in conjunction with Paper 1
warrants explicit statement at the outset. The two papers, taken
together, separate three questions the field has often conflated: what
persists dynamically, what individuates structurally, and what sustains
recursive closure. Battery-style observables address the first; the
partition-warrant slot named in Paper 1 §7 makes the second visible as a
question requiring supplementary structural condition; the present
paper's W_CA proposes a candidate filling for the third. The three
questions correspond to distinct structural commitments and admit
independent answers, and the specifications proper to each cannot be
captured by treatments that conflate them. Section 8.7 develops this
decomposition in detail; the present introduction notes it as the
paper's broader methodological contribution beyond the specific warrant
proposal.

The remainder of the paper proceeds as follows. Section 2 reproduces the
threshold structure inherited from *Mechanism of Identity Onset* — the
activation conditions, the threshold events T₀ and T\*, and the
tripartite classification — in the compressed form the partition-warrant
framing requires. Section 3 develops the formal predicate W_CA, its
two-axis structure, and its position in the corpus's three-tier
evaluator hierarchy of W_CA, IMC, and VPR. Section 4 demonstrates the
predicate's non-G-invariance through the gauge-fixing structural framing
and the causal-support-graph specification. Section 5 evaluates the
predicate on the Paper 1 witness and reports the verdict structure as a
rejection-mode case. Section 6 distinguishes closure activation from the
four alternative candidate families surveyed in Paper 1 §7.3, with the
route × mode cross-tabulation supplying a meta-taxonomy for
partition-warrants generally. Section 7 specifies falsification
conditions across predicate, verdict-structure, and discriminative-scope
categories. Section 8 closes with scope and limits, including the
structural achievement the two papers jointly enable.

## 2. Threshold Structure Inherited

The activation predicate developed in this paper builds on the threshold
structure introduced in *Mechanism of Identity Onset* (Thomas, 2026a).
The present section reproduces that structure in the compressed form the
partition-warrant framing requires. The treatment is summary rather than
re-derivation; readers seeking the full structural development of the
activation event, the conditions' joint necessity argument, the
flicker-phase derivation, and the falsification-condition specification
at the activation level should consult the prior paper directly. What
follows is the minimum necessary to support the partition-evaluative
recasting in §3.

### 2.1 The activation event

The activation event T₀ is the structural transition by which a
configuration crosses the threshold of admissible instantiation of
recursive constraint enforcement. Before T₀, a configuration's dynamics
may be coherent, persistent, and statistically organized in any number
of ways, but the configuration's own maintenance dynamics are not yet
defined over its own state in a manner that admits recursive enforcement
of the constraint that individuates it. After T₀, the maintenance
dynamics are admissible inputs to the constraint they maintain, and the
configuration enters the regime in which closure-bearing structure is
possible. The activation event is local and internal to the
configuration: it is a transition in the configuration's own constraint
dynamics, not a relational property bestowed by external configurations.

Three conditions are jointly necessary for activation:

**(C1) State-referential governing constraint.** The constraint that
governs the configuration's maintenance dynamics is defined over the
configuration's own state. The constraint references the configuration's
persistence-relevant variables, not merely a reduced description
applicable to broader classes of system.

**(C2) Internally funded corrective response.** The corrective response
that enforces the constraint is sourced from within the configuration.
The dynamics that maintain constraint satisfaction are not transferred
wholesale from external configurations; they are internal to the
configuration's own organization.

**(C3) Cost-viable maintenance budget.** The energetic and structural
resources required to sustain the corrective response are admissible:
the configuration's maintenance budget is sufficient to support the
dynamics on its own operating timescale.

The three conditions are stated in *Mechanism of Identity Onset* as
joint requirements rather than as fully separated commitments. The
present paper's §3.1 restates them in a form that disentangles
governance and viability — a refinement appropriate to the
partition-evaluative role the predicate plays here. The Mechanism
paper's formulation is sufficient at its level of generality; the
refinement is required for partition-warrant work because the
per-subsystem evaluation §3 develops needs the role-domains to be
separable.

### 2.2 The sustained-regime threshold and the tripartite classification

Activation establishes that closure is possible; closure names the
regime in which that possibility is sustained under perturbation and
cost. The sustained-regime threshold T\* marks the transition from
configurations that have crossed T₀ to configurations whose
post-activation regime is stably maintained: the maintenance budget is
not merely admissible at the activation event but sustainable across the
load profile the configuration faces in its operating environment.

The relationship between T₀ and T\* generates a tripartite
classification of configurations:

A **closed** configuration has crossed both T₀ and T\*: activation has
occurred and the post-activation regime is sustained with positive
maintenance margin under ambient perturbation.

A **closure-competent** configuration has crossed T₀ but not T\*:
activation has occurred and recursive constraint enforcement is
instantiated, but the maintenance budget is insufficient to sustain it
under ambient perturbation. Closure-competent configurations exhibit the
activation signature transiently or under reduced perturbation
conditions, but cannot be sustained on their own resources at the
substrate's operating scale. The class is empirically real and predicted
as a structural feature of substrates approaching the viability
threshold from below; it is the empirical witness of T₀ and T\* being
structurally distinct.

A **subthreshold** configuration has not crossed T₀: there is no
admissible mapping between the configuration's maintenance dynamics and
the constraint they would enforce. The activation predicate does not
apply, and the configuration is not closure-bearing under any extension
of its current dynamical structure.

### 2.3 Flicker, locality, and catalytic closure

The flicker phase is the interval between first recursive closure (T₀
crossing) and stable regime entry (T\* crossing) for configurations
approaching the viability threshold. Flicker corresponds to unstable
temporal occupancy of the activation condition: the configuration
recurrently crosses and uncrosses T₀ as the maintenance budget
oscillates around the cost-viability threshold. Flicker is a
structurally predicted feature of closure-competent configurations, not
a measurement artifact, and its empirical observation is one of the
falsification signatures *Mechanism of Identity Onset* specifies.

The locality of activation is structurally consequential. Activation is
always a transition in the configuration's own constraint dynamics; no
external configuration can cross T₀ on behalf of another. What an
external configuration can do is modify the boundary conditions under
which the first configuration's dynamics operate, reducing the
maintenance cost or increasing the restorative capacity in ways that
allow the configuration's own dynamics to achieve admissible
instantiation under those modified conditions. This is the catalytic
closure case: a configuration crosses T₀ through internally instantiated
activation under catalytically modified boundary conditions, without yet
achieving independent closure.

Catalytically activated configurations are activated but not
independently closed. T₀ has been crossed by the configuration's own
dynamics — the locality of activation forecloses the alternative that
external support could perform closure on behalf of the configuration.
What catalysis enables is internally instantiated closure that is not
yet internally sustained: the post-activation maintenance budget depends
on continued external support until the configuration develops
sufficient internal cost-viability to operate independently. The
structural distinction is therefore between *externally subsidized
viability* — where external support sustains an
already-internally-activated configuration — and *externally
instantiated closure*, which the locality principle rules out by
construction. The catalytic case is the first; the second is
structurally impossible. Appendix C develops the catalytic case as it
bears on the partition-warrant verdict structure for externally
scaffolded systems.

### 2.4 The recasting

The threshold structure summarized above was developed in *Mechanism of
Identity Onset* as an account of identity-onset events for
already-individuated configurations. The structural object the prior
paper specifies is the activation event in the configuration's own
dynamics, with the configuration's individuation taken as given.

The present paper recasts that structure as a partition-evaluative
warrant. The threshold ontology — T₀, T\*, the activation conditions,
the tripartite classification — applies without modification. What
changes is the structural role the predicate plays: from an account of
how identity-onset takes place in already-individuated configurations,
the predicate becomes a tool for evaluating whether an imposed partition
individuates configurations of the kind for which identity-onset is even
structurally possible. The recasting requires (C1)–(C3) to be evaluated
relative to a partition's imposed subsystem boundary — which is the work
of §3 — rather than relative to a configuration's already-given
individuation. The conditions and thresholds are inherited; their
evaluative locus shifts from configuration-internal dynamics to
partition-imposed boundaries on the substrate.

§3 develops this recasting formally and produces the
partition-evaluative predicate W_CA whose verdict structure the
remainder of the paper analyzes.

## 3. Closure Activation as Partition-Warrant

The previous section reproduced the threshold structure of *Mechanism of
Identity Onset* — the activation event T₀, the sustained-regime
threshold T\*, the three jointly necessary conditions for activation,
and the tripartite classification (closed, closure-competent,
subthreshold). That structure was developed as an account of how
identity onset takes place in already-individuated configurations. The
present section recasts it as a partition-evaluative warrant.

A terminological bridge is helpful at the outset. Throughout this
section, "configuration" denotes the object to which the activation
predicate applies; "subsystem" denotes the element of a partition's
image Ind(P). When a partition P is imposed on a substrate, each
subsystem S ∈ Ind(P) is a configuration to which W_CA can be applied.
The two terms refer to the same object viewed from different angles:
configuration-as-such (the activation-predicate frame) and
subsystem-under-partition (the individuation frame).

### 3.1 The formal predicate W_CA

Let P be a partition of the substrate, with Ind(P) the set of subsystems
P induces. The closure-activation predicate W_CA is a
partition-evaluative predicate that returns a structured verdict over
Ind(P), comprising a per-subsystem verdict for each S ∈ Ind(P).

For each subsystem S ∈ Ind(P), W_CA evaluates three jointly necessary
conditions, restated here in a form that disentangles the governance and
viability dimensions of the activation predicate. The three conditions
divide cleanly along structural roles: (C1) concerns target structure,
(C2) concerns governance structure, and (C3) concerns viability
structure. Each role can fail independently of the others, and the
conditions are jointly necessary in the sense that failure in any single
role-domain blocks T₀.

**(C1) State-referential constraint.** The corrective target is
specified over S's own state-space coordinates — those degrees of
freedom of the substrate assigned to S by P. The constraint governing
S's maintenance dynamics is defined relative to the state-space
structure P imposes, not over a reduced description that would apply
equally without that imposed boundary.

**(C2) Internally governed corrective response.** The corrective
dynamics that enforce constraint satisfaction on S are organized and
regulated from within the subsystem boundary P imposes. The dynamics'
control structure — what determines when corrective response is
initiated, how it is targeted, and how it terminates — is sourced
internally to S, not transferred across the imposed boundary.

**(C3) Internally viable maintenance budget.** S possesses sufficient
internally governed resources to sustain the corrective dynamics over
its operating timescale. The energetic and structural resources required
to support the regulation specified in (C2) are drawn from S's own
resource base, in quantities sufficient to maintain the dynamics without
unbounded support from external configurations.

The three conditions separate three distinct evaluative questions: where
the corrective target is specified (C1), where the dynamics enforcing
the target are governed (C2), and whether the resources to sustain those
dynamics are internally available in viable quantity (C3). The earlier
*Mechanism of Identity Onset* formulation collapsed (C2) and (C3) into a
single "internally funded" condition; the present formulation separates
them because a configuration may satisfy (C2) without satisfying (C3) —
its corrective dynamics are internally governed but its resource base is
insufficient to sustain them — and the closure-competent class is
exactly this case.

The three conditions are jointly necessary for activation. A subsystem S
satisfies T₀ iff (C1)–(C3) hold simultaneously. The verdict on S takes
the form:

W_CA(P, S) = (τ₀(S), μ\*(S), κ(S))

where τ₀(S) ∈ {0, 1} records whether T₀ is crossed; μ\*(S) is the
maintenance-margin profile under graded perturbation, defined only when
τ₀(S) = 1; and κ(S) ∈ {closed, closure-competent, subthreshold} is the
classification derived from (τ₀(S), μ\*(S)) per the *Mechanism of
Identity Onset* tripartite scheme.

The partition-level verdict is the tuple of per-subsystem verdicts:

W_CA(P) = ⟨W_CA(P, S) : S ∈ Ind(P)⟩

A partition admits no single binary or scalar reduction; the verdict
structure is irreducibly per-subsystem because the activation conditions
are partition-relative and the substrate's degrees of freedom partition
differently under different P. The aggregate readings of W_CA(P) —
whether the partition is "fully activated," "partially activated," or
"non-activated" — are derived properties of the verdict structure, not
its primary content.

W_CA is not fundamentally a selector among already-valid systems; it is
an evaluator of whether the imposed partition yields closure-bearing
systems at all. The conditions (C1)–(C3) reference the subsystem
boundary that P imposes, and the verdict W_CA(P) is the result of that
evaluation applied subsystem-by-subsystem. Whether the verdict supplies
a unique selection among G-related partitions is a downstream question,
decided by what the verdict structure looks like across the partitions
in question.

### 3.2 The two-axis structure

W_CA is structured around two distinct evaluative axes, with different
dimensionalities and different perturbation-protocol requirements.

**Axis 1: T₀ (binary).** The activation event itself. There is no
partially satisfied activation condition at a given evaluative instant;
flicker regimes correspond instead to unstable temporal occupancy of the
activation condition — recurrent crossings and uncrossings of T₀ in
configurations that have not yet stabilized within the post-activation
regime. The diagnostic signature of crossing is configuration-relative
path-dependent recovery under discriminative perturbation: a closed
configuration's recovery profile depends on which prior configuration
the system was maintaining, not merely on its prior state. The
discriminator is a single perturbation administered under controlled
conditions; the response is read off as a binary verdict on (C1)–(C3).

**Axis 2: T\* (scalar).** The viability of the post-activation regime.
Among configurations satisfying T₀, the maintenance budget admits
varying margins — the resources available to sustain the corrective
dynamics relative to the costs imposed by ambient perturbation. The
diagnostic instrument is a load-graded perturbation series, with the
maintenance-margin profile μ\* read off the response across the series.
The verdict is scalar: μ\*(S) is a real-valued profile bounded below by
zero (closure-competent threshold) and unbounded above.

The two axes are not redundant. T₀ alone cannot distinguish closed from
closure-competent configurations: both have crossed T₀, and the
discriminator returns the same binary verdict. T\* alone cannot
distinguish either from subthreshold configurations: a configuration
that has not crossed T₀ does not admit a coherent maintenance-margin
reading at all. The tripartite classification κ requires both axes by
construction.

The warrant is not merely topological or organizational; it is
phase-structured. Activation and sustained viability are distinct
evaluative dimensions, and a warrant that collapses them into a single
criterion — as classical autopoietic accounts of operational closure
tend to — loses the distinction between systems that have achieved
recursive constraint enforcement and systems that can sustain that
achievement under perturbation. The two-axis structure is the formal
locus of this phase-structured commitment.

### 3.3 Relationship to the Viable Perturbation Regime and the IMC

The two axes specify what W_CA reads off the response to perturbation;
they do not specify what perturbations are admissible to apply. The
latter is governed by the Viable Perturbation Regime (VPR; Thomas,
2026e), the two-dimensional phase diagram developed elsewhere in the
corpus, with axes (perturbation load, perturbation richness). VPR
governs the experimental design space within which W_CA is evaluated.

The geometries operate at different levels. VPR is defined over the
substrate's perturbation environment: load is the IMC-bounded magnitude
of perturbation a configuration can absorb without exiting its viability
region; richness is the structural diversity of the perturbation set,
capturing whether the configuration is probed against a sufficient
variety of constraint-relative challenges. T₀/T\* is defined over the
response: T₀ reads off the path-dependence signature of recovery; T\*
reads off the maintenance margin across the load axis of VPR.

A complete W_CA evaluation requires a perturbation protocol that draws
from VPR's admissible region in two distinct ways. For T₀: a
discriminative perturbation, sufficient to elicit the
configuration-relative recovery signature when present, but bounded
within the configuration's IMC envelope. For T\*: a graded perturbation
series spanning a useful interval along VPR's load axis, with richness
sufficient to probe the configuration against the structural diversity
of perturbation it would face in its operating environment.

The two protocol requirements can be combined into a single regimen — a
graded perturbation series with discriminative perturbations interleaved
at chosen load levels — but they answer different evaluative questions
and must be designed against different protocol constraints. Conflating
the two protocols, or attempting to read both axes off a single
perturbation, loses the binary-then-scalar discipline the warrant
requires.

The relationship to VPR also clarifies the position of W_CA relative to
IMC-governed viability analysis. VPR characterizes the perturbation
environment a configuration faces and the conditions under which its
viability is preserved; the Invariance Maintenance Condition (IMC;
Thomas, 2026b) governs the upper bound on perturbation load that
closure-bearing configurations can absorb without identity loss. Both
presuppose that the subsystem under examination is a configuration to
which IMC-governed analysis applies. W_CA therefore operates upstream of
IMC application: it evaluates whether the imposed subsystem boundary
yields a configuration for which IMC-governed viability analysis is
meaningful at all. IMC is not universally substrate-applicable merely
because a persistent dynamical structure exists; its applicability is
conditioned on the closure-bearing properties that W_CA evaluates. The
three structures are nested rather than competing, with W_CA the
outermost evaluator.

## 4. Non-G-Invariance Demonstration

### 4.1 Structural relationship to Paper 1

The structural relationship between Paper 1 and the present paper can be
stated precisely. Paper 1 establishes metric equivalence classes over
partitions under admissible transformations G — partitions related by
elements of G receive identical values from the persistence/coherence
battery and are therefore indistinguishable at the level of battery
observables. The present paper establishes W_CA as a non-invariant
evaluator over those equivalence classes — a predicate that returns
verdict structures sensitive to features admissible transformations do
not preserve.

The structural homology is to gauge-fixing: a non-invariant criterion
imposed over an equivalence class to recover a unique representative.
The disanalogy is that gauge-fixing in physics is typically
representational — the fixing criterion specifies a coordinate
convention that breaks the gauge symmetry without altering the physical
content of the system — while closure activation fixes by a
dynamical-maintenance criterion. The fixing condition references the
substrate's causal structure rather than a representational choice. The
remainder of this section discharges the formal claim implicit in this
framing.

### 4.2 Causal support and the imposed boundary

W_CA's non-G-invariance follows from the conditions (C1)–(C3) specified
in §3.1. Each condition references the subsystem boundary that the
partition imposes: (C1) requires the corrective target be specified over
the subsystem's own state-space coordinates; (C2) requires the
corrective dynamics be governed from within the imposed boundary; (C3)
requires the resources sustaining those dynamics be drawn from within
the same boundary. The three conditions therefore evaluate properties
that are defined relative to the partition, and a partition
transformation can change the structure being evaluated.

The relevant dependency structure concerns causal support relations
across the imposed subsystem boundary, not merely covariance structure
within a coordinate representation. The causal support graph is not an
additional substrate appended to the dynamics; it is the organization of
maintenance dependency relations induced when the substrate is evaluated
relative to an imposed subsystem boundary. Covariance structure — the
joint statistical dependencies among substrate variables — transforms
covariantly under T ∈ G: Σ ↦ T Σ Tᵀ, and the spectrum, precision-matrix
zero pattern, and other quadratic functionals are preserved or transform
predictably. The causal support graph is a different object. It concerns
which substrate degrees of freedom supply the inputs to which corrective
dynamics, and whether those input flows cross the boundary the partition
imposes. The covariance structure is a property of the joint
distribution; the causal support structure is a property of the
substrate's interaction graph viewed relative to the partition.

For the harmonic-oscillator witness of Paper 1 §3.2, the distinction is
concrete. Under P₁ = {S_A, S_B}, where S_A is the configuration carried
by oscillator-1 coordinates and S_B by oscillator-2 coordinates, the
substrate's coupling term −k(q₁ − q₂)² generates a restoring force on
each oscillator that depends causally on the other's position. The
causal support structure under P₁ has the coupling term crossing the
imposed S_A/S_B boundary: S_A's corrective dynamics depend on inputs
sourced from S_B's degrees of freedom, and vice versa. Under P₂ = {S₊,
S₋}, where S₊ and S₋ are the symmetric and antisymmetric normal-mode
configurations, the coupling term is diagonalized in the rotated
coordinates and the modes are dynamically decoupled in the linearized
regime. The covariance structure under P₂ inherits this decoupling: the
precision-matrix zero pattern is consistent with the apparent
independence of the modes in their own coordinates.

A reader might infer from the rotated-frame decoupling that P₂ satisfies
(C2) — the modes appear internally governed in their own coordinates.
The inference fails because the decoupling concerns trajectory
representation, not maintenance governance. Causal independence of
trajectories does not imply recursive self-maintaining organization. The
transformed coordinates inherit the substrate dynamics but do not
thereby acquire independently funded corrective organization. The bath
coupling, which sources the Langevin damping that provides corrective
response in this substrate, couples to the original coordinates as ξ_i
acting on q_i; in the rotated frame, the bath couples to the normal
modes through the linear combinations Ξ\_± = (ξ₁ ± ξ₂)/√2. The coupling
crosses the P₂ boundary regardless of the coordinate representation:
each normal-mode configuration's corrective dynamics depend causally on
inputs from the bath, which is external to either S₊ or S₋.

The witness substrate therefore exhibits cross-boundary causal support
under both partitions, but for structurally different reasons. Under P₁,
the inter-oscillator coupling provides intra-substrate cross-boundary
support; under P₂, the bath provides external cross-boundary support
that survives the coordinate rotation because it operates on the
partition's actual imposed boundary, not on the rotated coordinate
system. Neither partition satisfies (C2). The witness verdict is
therefore uniform across G-related partitions: τ₀ = 0 for all subsystems
under both P₁ and P₂. The detailed evaluation appears in §5.

The uniformity of the witness verdict across G-related partitions does
not refute the non-G-invariance claim. W_CA's non-G-invariance is
established at the predicate level: the predicate is sensitive to
substrate properties — causal support relations relative to imposed
boundaries — that are not in (L, 𝒞) and that change in structural form
under partition transformations even when their verdict output does not.
Whether the predicate's verdict outputs differ across G-related
partitions on a given substrate depends on whether that substrate
exhibits closure-bearing structure under any of those partitions. The
predicate's discriminative work takes one of three structural modes,
depending on the substrate's closure-bearing properties. These are
sufficiently distinct in their operational signatures to warrant
separate naming.

**Rejection mode.** A substrate with no closure-bearing partition under
any G-equivalent labeling — the harmonic-oscillator witness — yields a
uniform negative verdict across G-related partitions. Non-G-invariance
is preserved at the predicate level but does not manifest at the
verdict-output level, because no partition activates and the predicate's
discriminative work consists of ruling out persistence-only candidates
rather than selecting among closure-bearing ones.

**Selection mode.** A substrate with closure-bearing structure under one
partition and not others — the case where W_CA does the discriminative
work the partition-warrant slot most directly demands — yields
differential T₀ verdicts that demonstrate non-G-invariance at the output
level. The harmonic-oscillator witness does not supply this case, but
closure-bearing substrates discussed in the §5.6 forward-pointer and in
the corpus's empirical companion programs do.

**Stratification mode.** A substrate with closure-bearing structure
under multiple G-related partitions yields differential margin profiles
even where the binary T₀ verdicts coincide, and non-G-invariance
manifests at the scalar axis. This mode is the structural foothold for
nested-identity and coalition-identity phenomena — Volvox-type
distributed systems, multi-level biological organization, and similar
cases where multiple closure-bearing partitions coexist on a single
substrate with differentiated viability profiles. The corpus addresses
these phenomena elsewhere; the present paper notes the structural
availability of the mode and reserves its development.

The three modes correspond to distinct verdict-structure topologies that
follow from the substrate's closure-bearing properties evaluated against
G. Subsequent sections refer to substrates and verdicts by mode.

The non-G-invariance claim therefore holds at the level relevant to the
partition-warrant slot: W_CA can return verdict structures that
distinguish among G-related partitions on substrates where any of those
partitions support closure-bearing structure. The witness's uniform
negative verdict is the appropriate behavior of the predicate on a
substrate where no G-related partition supports closure, and
demonstrates the predicate's correctness on rejection-mode substrates
rather than refuting its non-G-invariance.

### 4.3 Location in the three-route taxonomy

Paper 1 §7.2 identified three logical routes by which a candidate
partition-warrant might break G-invariance: (i) external selection
principles imposed from outside the dynamics, (ii) internally generated
properties not G-invariant and not reducible to functions of (L, 𝒞), and
(iii) refinement of the transformation group itself.

Closure activation occupies route (ii). The activation predicate is
sourced internally — its conditions reference the substrate's dynamics
and the partition's imposed boundary, not an external optimization
criterion or definitional commitment. Its non-G-invariance, established
in §4.2, derives from a property of the substrate (the causal support
graph relative to the imposed boundary) that is not reducible to
functions of the dynamical generator and stationary correlation
structure. It does not refine G; it operates on the same admissible
transformation class while reading off features the class does not
preserve.

Paper 1 §7.3 noted that route (ii) is the home of process-based
warrants, and identified two specific candidates in this family:
autopoietic operational closure and closure activation. Both are
internally generated, both are dynamically defined, and both reference
dependency structures that are not battery-internal. Closure activation
is therefore one of two process-based warrants in the taxonomy as
currently surveyed; the §6 distinctions among warrant families take up
the differentiation among them.

## 5. Evaluation of the Witness Under Closure Activation

### 5.1 The witness substrate

The witness from Paper 1 §3.2 is reproduced minimally for the present
evaluation. The substrate consists of two harmonic oscillators of unit
mass with positions q₁ and q₂ and conjugate momenta p₁ and p₂, natural
frequency ω₀, and linear coupling of strength k, embedded in a weak
thermal bath at inverse temperature β. The system Hamiltonian is

H_sys = ½(p₁² + p₂²) + ½ω₀²(q₁² + q₂²) + ½k(q₁ − q₂)².

The bath provides dissipative coupling through independent Langevin
forcing on each oscillator, with damping coefficient γ and Gaussian
white-noise terms ξ_i satisfying ⟨ξ_i(t) ξ_j(t′)⟩ = 2γβ⁻¹ δ_ij δ(t −
t′). The working regime is k ≪ ω₀² and γ ≪ ω₀.

Two partitions are admissible under the substrate's transformation group
G:

P₁ = {S_A, S_B} groups the substrate's degrees of freedom by oscillator
index, with S_A carried by (q₁, p₁) and S_B by (q₂, p₂).

P₂ = {S₊, S₋} groups the substrate's degrees of freedom by normal-mode
index, with S₊ carried by the symmetric combination (Q₊ = (q₁+q₂)/√2, P₊
= (p₁+p₂)/√2) and S₋ by the antisymmetric combination (Q₋ = (q₁−q₂)/√2,
P₋ = (p₁−p₂)/√2). The two partitions are related by an orthogonal
rotation T ∈ G, and Paper 1 §4 demonstrates that the eight-item
persistence/coherence battery returns identical values on both.

The present section evaluates W_CA on each partition. The conditions
(C1)–(C3) are evaluated in their distinct structural roles per §3.1 —
target structure, governance structure, viability structure. Each
condition fails in its own role-domain and the failures stack rather
than the upstream failure preempting downstream evaluation.

### 5.2 Evaluation under P₁

The per-subsystem evaluation under P₁ proceeds by examining the
activation conditions for S_A and S_B in turn. By the substrate's
reflection symmetry between the two oscillators, the analysis for S_A
applies symmetrically to S_B; the explicit walk-through is given for
S_A, with the symmetric extension noted.

**(C1) Target structure.** The oscillator dynamics do not specify an
internally maintained target state whose deviation recruits corrective
enforcement; the return toward equilibrium is simply the substrate
evolution itself. The Hamiltonian and bath coupling jointly determine
that S_A's trajectory drifts toward q₁ = 0 in expectation, but no
separately specified target — no internally enforced reference state
distinct from the dynamics' own trajectory structure — is part of S_A's
organization. (C1) fails on its own terms: the structural object the
condition presupposes (an internally specified corrective target) is
absent.

**(C2) Governance structure.** Even if a corrective target were
specified, the response that would return S_A toward such a target is
the Langevin damping term −γp₁ + ξ₁(t). The damping coefficient γ and
the noise statistics are properties of the bath; the response is not
organized or regulated from within the S_A boundary. The dissipative
dynamics are governed externally — by the bath's coupling parameters —
and survive any redescription of S_A's internal state. The harmonic
restoring force −ω₀²q₁ is internal to S_A's coordinates but is not
itself a corrective response in the activation sense; it is the
deterministic dynamics specified by the Hamiltonian, not a regulatory
mechanism that monitors and corrects deviation. (C2) fails on its own
terms: there is no internally governed correction.

**(C3) Viability structure.** Even if target and governance were
internally specified, the dissipative dynamics that maintain S_A near
equilibrium are bath-funded, not S_A-funded; their sustainability is a
property of the bath's thermal capacity, not of S_A's internal
resources. (C3) fails on its own terms: there is no internally sustained
budget.

The symmetry of the substrate yields the same evaluation for S_B. The
per-subsystem verdicts are τ₀(S_A) = τ₀(S_B) = 0, with κ(S_A) = κ(S_B) =
subthreshold. The partition-level verdict is

W_CA(P₁) = ⟨(0, −, subthreshold), (0, −, subthreshold)⟩.

The cascade of failures is structurally consistent: each subsystem lacks
an internally specified target, lacks internally governed correction,
and lacks internally sustained budgeting. The three failures are
independent and each is sufficient on its own to block T₀.

### 5.3 Evaluation under P₂

The evaluation under P₂ proceeds analogously for S₊ and S₋. The rotated
coordinates (Q₊, P₊, Q₋, P₋) diagonalize the coupling term in the
linearized regime: the symmetric mode oscillates with frequency ω₀ and
the antisymmetric mode with frequency √(ω₀² + 2k), and in the linear
limit the modes are dynamically independent.

**(C1) Target structure.** A corrective target for S₊ would be defined
over (Q₊, P₊). As with P₁, no separately enforced maintenance constraint
is present; the rotation diagonalizes the dynamics but does not
introduce target structure. The transformed coordinates inherit the
substrate dynamics but do not thereby acquire independently funded
corrective organization. (C1) fails for the same structural reason as
under P₁.

**(C2) Governance structure.** This is the condition where the
rotated-frame analysis requires care. In normal-mode coordinates, the
deterministic dynamics of S₊ and S₋ are decoupled; a reader might infer
that each mode's corrective dynamics are now internal to its own
coordinate frame. The inference fails because the decoupling concerns
trajectory representation, not maintenance governance. Causal
independence of trajectories does not imply recursive self-maintaining
organization. The dissipative response that returns each mode toward
equilibrium is the projection of the Langevin terms onto the rotated
coordinates: the bath couples to (q₁, q₂) with Gaussian white noises ξ₁,
ξ₂, and these project onto the normal modes as Ξ\_± = (ξ₁ ± ξ₂)/√2,
retaining the same noise statistics. The damping coefficient γ continues
to be bath-set; the bath continues to source the corrective response.
The bath governs the dynamics regardless of coordinate choice. (C2)
fails for the same structural reason as under P₁: the corrective
response is not internally governed.

**(C3) Viability structure.** As under P₁, the dissipative dynamics are
bath-funded; no internally sustained budget exists under either
normal-mode subsystem.

The per-subsystem verdicts are τ₀(S₊) = τ₀(S₋) = 0, with κ(S₊) = κ(S₋) =
subthreshold. The partition-level verdict is

W_CA(P₂) = ⟨(0, −, subthreshold), (0, −, subthreshold)⟩.

### 5.4 Verdict structure across the witness

The two partition-level verdicts coincide at the output level: W_CA(P₁)
and W_CA(P₂) have identical tuple values. The witness is a
rejection-mode case per §4.2 — a substrate with no closure-bearing
partition under any G-equivalent labeling, on which W_CA returns a
uniform negative verdict. The structural reasons for the verdict are
partition-dependent in a way the verdict outputs do not record. Under
P₁, the failure cascade tracks the inter-oscillator coupling crossing
the imposed S_A/S_B boundary, layered with bath-mediated dissipation.
Under P₂, the failure cascade tracks the bath coupling crossing the
rotated S₊/S₋ boundary, with the inter-oscillator coupling now
diagonalized in the rotated frame and contributing to the dynamical
structure rather than to cross-boundary support. Both partitions fail
(C1)–(C3); the dependency topology by which the bath supports the
dynamics differs across partitions, and the precise structural reasons
within each condition's failure differ accordingly. The non-G-invariance
of the predicate at the structural level is preserved even where verdict
outputs coincide, exactly as §4.2 anticipated.

The deeper structural reading of the verdict requires care about what
"external" means in this context. The failure is not openness to
external exchange as such; biological closure-bearing systems are
likewise thermodynamically open. The failure is that the corrective
organization is not governed from within the imposed subsystem boundary.
Thermodynamic openness and governance externality are different
structural properties: a cell exchanges energy and materials with its
environment but governs its own corrective response to perturbation; the
harmonic-oscillator-in-bath system exchanges energy with the bath and is
also governed by the bath's parameters in its corrective response. The
activation conditions read off the latter, not the former.

The harmonic oscillator system embedded in a thermal bath is not the
kind of system the activation predicate identifies as closure-bearing.
The substrate persists, in the sense that the stationary distribution
exists and the Langevin dynamics return the system to the support of
that distribution after perturbation; this is the persistence that Paper
1's battery captures. But the substrate does not exhibit recursive
constraint enforcement — it has no internally specified target, no
internally governed correction, and no internally sustained budget.
Persistence and closure are different structural categories, and the
witness is a substrate where the former obtains and the latter does not.

### 5.5 What the evaluation demonstrates about W_CA

The witness evaluation shows that W_CA exhibits the verdict-structure
behavior the partition-warrant slot requires. Three structural points
warrant emphasis.

First, W_CA returns a determinate verdict on both G-related partitions
of a substrate that the persistence/coherence battery cannot
individuate. The battery's invariance across G-related partitions is the
underdetermination Paper 1 §6 establishes; the warrant supplies an
evaluation that does not share that invariance — even where the verdict
outputs coincide in this particular case.

Second, the warrant's verdict on the witness is correctly negative. The
substrate is not closure-bearing; the verdict reflects that.
Battery-style observables identify both P₁ and P₂ as legitimate "system"
partitions under their respective frameworks (Paper 1 §4 demonstrates
this across the framework registers it surveys); W_CA identifies neither
as closure-bearing. The asymmetry between persistence and closure is
exactly the asymmetry that makes a partition-warrant necessary, and
W_CA's null verdict on the witness is the methodological observation
Paper 1 set up: battery-alone individuation is insufficient because some
battery-identified "systems" are not closure-bearing systems at all.

Third, the warrant's discriminative power takes different operational
modes depending on substrate class. The witness exhibits rejection-mode
discrimination: W_CA rules out both G-related partitions as
non-closure-bearing without selecting between them. On substrates
supporting closure-bearing structure under one or more partitions, the
warrant's work shifts into selection mode (differential T₀ verdicts) or
stratification mode (differential margin profiles among closure-bearing
partitions). The witness exhibits the first mode; the other modes
require closure-bearing substrates outside the present paper's scope.

### 5.6 Closure-bearing substrates and forward pointers

The full discriminative power of W_CA is exercised on substrates that
exhibit recursive constraint enforcement under at least one admissible
partition. Biological cells, with their homeostatic regulatory networks
and metabolic dependency structure, are the canonical case: the cell
membrane defines a partition under which corrective dynamics are
internally governed (membrane-localized regulatory feedback) and
resource viability is internally managed (metabolic budget). Cognitive
systems with recursive constraint enforcement on internal states —
systems where a regulatory loop monitors and corrects deviation in
internally specified target variables — are a second class of
candidates. The corpus's empirical companion programs, including the
pre-registered anesthesia state-transition study (Thomas, 2026d), take
up such substrates and develop the protocols for evaluating W_CA on
them.

The present paper establishes the warrant's formal specification and its
correctness behavior on the inherited witness; positive closure-bearing
cases are developed in the companion empirical programs. The witness
evaluation establishes that W_CA discharges the §7.5 charter from Paper
1: the verdict structure on the witness's two G-related partitions is
determinate, structurally informative, and exhibits the
partition-relativity the partition-warrant slot demands.

## 6. Distinction from §7.3 Alternatives

### 6.1 Structural map

Paper 1 §7.3 surveyed four candidate families filling the
partition-warrant slot: optimization-based warrants (Integrated
Information Theory's Φ-maximization), structural-definitional warrants
(Global Workspace Theory's workspace architecture),
statistical-structural warrants (the Free Energy Principle's
Markov-blanket criterion in nonlinear regimes), and process-based
warrants (autopoietic operational closure and the closure-activation
proposal of the present paper). The four families distribute across the
three logical routes specified in Paper 1 §7.2: optimization-based and
structural-definitional warrants occupy route (i) (external selection
principles), statistical-structural and process-based warrants occupy
route (ii) (internally generated non-invariant properties), and no
current candidate occupies route (iii) (refined transformation group).

The route taxonomy locates each warrant by the source of its
discriminative work; the operational mode classification of §4.2 locates
each warrant by its verdict-structure behavior. The two classifications
are orthogonal: a warrant's location in the route taxonomy does not
determine its operational-mode coverage, which depends on the structure
of the warrant's evaluative regime. The cross-tabulation is therefore
informative as a meta-taxonomy of partition-warrants — a structural
classification scheme that locates closure activation among existing
candidates and provides a frame for assessing further candidates the
slot may yet admit. The cross-tabulation reads as follows.
Optimization-based warrants operate primarily in selection mode —
Φ-maximization always selects a maximizing partition when one exists —
and treat rejection mode as ill-posed (no maximization target on
substrates where no partition is closure-bearing).
Structural-definitional warrants operate primarily in selection mode by
architectural fit, with rejection mode straightforward (no partition
exhibits the architecture) and stratification mode largely artificial.
Statistical-structural warrants operate in all three modes in principle,
but their selection work depends on the regime-specific applicability of
the Markov-blanket criterion. Autopoietic operational closure operates
primarily in selection mode, with rejection straightforward and
stratification rare in classical accounts because operational closure is
treated as a binary condition. Closure activation operates naturally in
all three modes, with rejection, selection, and stratification each
producing distinct and informative verdict structures.

This last feature — natural mode coverage — is among the structural
commitments the present paper inherits from the activation-event framing
rather than imports as a virtue claim. The two-axis structure of W_CA
(binary T₀ + scalar T\*) and its phase-structured commitment make all
three operational modes well-defined; warrants without analogous
structure handle some modes only as edge cases or with awkward
extensions. The remaining subsections develop the specific distinctions
warrant family by warrant family.

### 6.2 Distinction from optimization-based warrants

Integrated Information Theory's exclusion postulate is the clearest
example of an optimization-based partition-warrant in the
consciousness-studies literature (Tononi, 2008; Oizumi et al., 2014). Φ
— the system's integrated information — is partition-dependent; the
postulate selects the partition that maximizes Φ and treats the
maximizing partition as constituting the system. The selection mechanism
is route (i): an optimization criterion imposed from outside the
dynamics that picks a representative from each G-equivalence class.

The structural distinctions from closure activation are several.
Φ-maximization is comparative: it selects by relative ranking among
admissible partitions, requiring the warrant to compute Φ across the
partition lattice and identify the maximum. Closure activation is
evaluative: each partition is assessed on its own terms against
(C1)–(C3), and the verdict structure is determined per partition rather
than by inter-partition comparison. The two warrants therefore answer
different questions: Φ-maximization answers "which admissible partition
is most integrated?", closure activation answers "which admissible
partitions, if any, are closure-bearing under their imposed
boundaries?".

The computational character of the warrants differs accordingly. Exact Φ
computation is intractable on any but trivial substrates; the partition
lattice grows combinatorially in system size and Φ requires evaluation
over all possible partitions for the selection step (Oizumi et al.,
2014). Closure activation requires a perturbation protocol that probes
T₀ and T\* for each candidate partition under examination; it does not
require enumeration over the full partition lattice, because verdicts
are partition-evaluative rather than partition-comparative.

Mode coverage differs as well. Optimization-based warrants treat
rejection as downstream of comparative selection rather than as a
primitive evaluative outcome: a substrate where no partition is
closure-bearing still has a Φ-maximizing partition, and rejection
emerges only as a downstream verdict if that partition's Φ falls below a
threshold value separately specified. Closure activation's
rejection-mode behavior — uniform negative verdict on case-1 substrates
— is the predicate's primitive response, not a consequence of having
first selected.

The two warrants are not jointly inconsistent on substrates where both
apply; they answer different questions and could in principle yield
aligned or conflicting verdicts on the same substrate without either
being thereby refuted. The present paper's claim is that closure
activation supplies a partition-evaluative warrant where the
optimization-based slot is occupied by a partition-comparative one, and
that the slot supports both kinds of filling.

### 6.3 Distinction from structural-definitional warrants

Global Workspace Theory invokes an architectural commitment as a
precondition for systemhood: the requirement that a system possess a
workspace structure in which local processing regions broadcast to a
shared integrative space (Baars, 1988; Dehaene & Changeux, 2011). Paper
1 §5.3 noted that this commitment must be either part of the observable
battery (in which case it inherits the underdetermination result of §6)
or external to the battery (in which case it functions as a
partition-warrant in the sense of route (i)). The forced-choice
structure made the warrant function visible; the present discussion
takes the route-(i) reading and locates the structural distinctions from
closure activation.

GWT-as-warrant requires substrate-level architectural specification: a
partition is admissible only if its subsystems exhibit the
broadcast-and-receive topology the framework defines. The architectural
commitment is definitional — it specifies what counts as a system rather
than evaluating whether a candidate partition exhibits some dynamical
property. Closure activation, by contrast, is dynamical-evaluative: it
does not require any specific architectural type and applies to any
substrate where the activation conditions can be probed by perturbation.
The two warrants operate at different levels — GWT at the level of
admissible system types, closure activation at the level of whether a
candidate partition meets the activation conditions regardless of
architectural type.

The substrate scope differs accordingly. GWT-as-warrant is most
naturally applied to substrates with discrete processing regions and
specifiable broadcast topology — neural systems, certain artificial
cognitive architectures, and analogues. Closure activation applies
wherever activation conditions can be evaluated, which includes
substrates without broadcast architecture (single-cell biological
systems, homeostatic regulatory networks without distributed processing,
and so on). On substrates with broadcast architecture, both warrants may
apply and may agree or disagree; on substrates without it,
GWT-as-warrant is silent while closure activation can return a
determinate verdict.

Mode coverage differs in a particular respect: stratification mode is
awkward for GWT-as-warrant. Architectural commitment is typically binary
— either a subsystem has the broadcast topology or it does not — and
grading the strength of that commitment across closure-bearing
partitions is not a natural extension of the framework. Closure
activation's stratification mode reads off margin profiles directly from
the maintenance dynamics, which admits gradation by construction.

### 6.4 Distinction from statistical-structural warrants

The Free Energy Principle characterizes systems through Markov-blanket
structure, with conditional-independence relations between internal and
external states given a set of blanket states (Friston, 2010; Kirchhoff
et al., 2018). Paper 1 §5.2 established that in linear-Gaussian regimes,
the Markov-blanket structure is captured by the precision-matrix zero
pattern, which is a function of (L, 𝒞) and inherits the
underdetermination result. In nonlinear regimes, where higher-order
conditional independencies are not reducible to pairwise correlations,
the Markov-blanket criterion can encode structure not captured by the
battery and may function as a route-(ii) partition-warrant.

The structural distinctions from closure activation operate even where
both warrants are non-G-invariant. The Markov-blanket criterion is
statistical: it identifies partitions by patterns of conditional
independence in the joint distribution. Closure activation reads off the
causal support graph, which concerns dependency in the dynamics'
input-output structure relative to the imposed boundary. These are
different structural objects: a partition can exhibit Markov-blanket
structure (conditional-independence pattern present) without exhibiting
closure-bearing structure (corrective organization governed from
within), and conversely a partition can exhibit closure-bearing
structure with imperfect or non-classical conditional-independence
patterns. The two warrants can therefore disagree on substrates where
both are well-defined.

The descriptive-versus-constitutive distinction is structurally
informative. Markov-blanket identification concerns statistical
separability structure; closure activation concerns maintenance
organization relative to the imposed boundary. These are independent
structural objects, and the same substrate can yield different verdicts
under each.

A regime-dependence asymmetry is also relevant. The FEP Markov-blanket
criterion is regime-dependent in its warrant-eligibility: it is a
route-(i) battery-internal observable in linear-Gaussian regimes and a
route-(ii) warrant only in nonlinear regimes where higher-order
conditional independencies enter. Closure activation operates as a
route-(ii) warrant across regimes, because the causal support graph it
reads off is not reducible to (L, 𝒞) regardless of linearity. The two
warrants therefore have different applicability profiles across
substrate regimes.

### 6.5 Distinction from autopoietic operational closure

The closest neighbor in the warrant taxonomy is autopoietic operational
closure (Maturana & Varela, 1980; Varela, 1979). Both warrants are route
(ii), both are process-based, and both reference dependency structures
internal to the substrate's dynamics rather than statistical or
definitional features. The structural distinctions are accordingly more
subtle, but they are decisive enough to warrant separate development of
closure activation as a distinct candidate.

The phase-structured commitment is the load-bearing distinction.
Classical autopoietic operational closure treats organizational closure
as a single condition: components produce one another in a closed loop,
and this closure is either present or absent in a system at a given
time. Closure activation introduces an explicit two-axis structure: T₀
as the binary activation event and T\* as the scalar viability axis. The
two axes correspond to distinct evaluative dimensions — whether
activation has occurred and how robustly the post-activation regime is
sustained — and the tripartite classification (closed,
closure-competent, subthreshold) is well-defined only across both axes.
Classical autopoiesis collapses these dimensions and loses the
distinction between configurations that have achieved recursive
enforcement and configurations that can sustain it under perturbation.

The cost-viability condition (C3) makes this distinction operative.
Closure activation requires not only that corrective dynamics be
internally governed (C2) but that the resources sustaining those
dynamics be internally viable on the configuration's operating
timescale. A configuration may satisfy C2 without satisfying C3 —
internally governed but resource-inadequate — and the closure-competent
class is exactly this case. Classical autopoiesis lacks an explicit
budget condition and accordingly does not distinguish closed from
closure-competent configurations.

Operationalizability is the second decisive distinction. Closure
activation's verdict structure is read off perturbation response:
configuration-relative path-dependence under discriminative perturbation
for T₀, maintenance-margin profile under graded perturbation for T\*.
The protocol is well-defined and less dependent on prior decomposition
of the substrate into constitutive production relations than
verification of operational closure under classical autopoietic
accounts. Classical autopoiesis has historically been less
operationalized; verifying operational closure on a given substrate
requires identifying the components and their production relations, a
task that is interpretively heavy and substrate-specific. The
activation-conditions formulation factors this work into a perturbation
protocol that does not require prior identification of components,
though it still depends on meaningful access to system dynamics and
interpretive judgment about what counts as discriminative perturbation
in the substrate at hand.

Mode coverage follows: classical autopoietic closure is most naturally a
selection-mode warrant. Stratification is rare in classical accounts
because closure is treated as binary; rejection mode is straightforward
but does not produce structured verdict information beyond the binary
"no closure here." Closure activation's natural three-mode coverage —
with rejection-mode verdicts carrying structural information about
cascade-of-failure modes, selection-mode verdicts producing differential
T₀ verdicts, and stratification-mode verdicts producing differential
margin profiles — extends the warrant's discriminative work
substantially.

The distinctions from autopoietic closure are structural rather than
adversarial. Closure activation can be read as a refinement of the
autopoietic insight that recursive maintenance is the relevant
individuating feature, with explicit phase-structure, explicit budget
conditions, explicit operational protocol, and explicit verdict
structure replacing the classical binary closure judgment. The two
warrants are best understood as occupying the same route-(ii)
process-based slot at different levels of structural articulation, with
closure activation supplying the articulation the partition-warrant role
requires.

## 7. Falsification Conditions

The falsification conditions for W_CA partition into three structural
commitments: predicate-level conditions on the activation specification
itself, verdict-structure conditions on the predicate's behavior across
operational modes, and discriminative-scope conditions on the warrant's
empirical reach. Each is stated with the structural commitment the
predicate makes and the empirical signature that would falsify it.

### 7.1 Predicate-level falsifications

The activation predicate makes three commitments at the level of its
specification, each falsifiable independently of the verdict structures
the predicate produces.

**Joint necessity of (C1)–(C3).** The activation conditions are stated
as jointly necessary for T₀: a configuration crosses T₀ only if all
three conditions hold. If a substrate exhibits closure-bearing
organization on any independent grounds — *independent* here meaning
identified by criteria not reducible to W_CA's own verdict structure: a
homeostatic regulatory network with internally specified setpoints, a
metabolic dependency structure with internally governed corrective
feedback, a cognitive system with recursive constraint enforcement on
internal states — but fails one or more of (C1), (C2), (C3) under
reasonable evaluation, then either the conditions are not jointly
necessary or the independent closure-bearing identification was wrong.
At the current stage of development, adjudication necessarily relies on
independently motivated exemplars of closure-bearing organization rather
than on a fully formalized independence criterion. Empirical signature:
a substrate class on which closure-bearing organization is independently
warranted, but on which W_CA returns τ₀ = 0 under all candidate
partitions.

**Joint sufficiency of (C1)–(C3) for T₀.** A configuration satisfying
all three activation conditions should exhibit the T₀ signature —
configuration-relative path-dependent recovery under discriminative
perturbation. If a substrate satisfies (C1)–(C3) under reasonable
evaluation but fails to produce path-dependent recovery profiles on
appropriate perturbation protocols, the conditions are not jointly
sufficient as the predicate specifies. Empirical signature: a candidate
partition on which (C1)–(C3) hold but recovery from perturbation is
state-only-dependent rather than configuration-relative.

**Structural distinctness of T₀ and T\*.** The two-axis structure
presupposes that the activation event and the sustained-regime threshold
are distinct, with closure-competent configurations the empirical
witness of their distinctness. If, across substrates and protocols, no
empirical or theoretical distinction can be drawn between first
admissible instantiation and sustained satisfiability of the activation
predicate — if every case of T₀ is immediately a case of T\* with no
detectable flicker phase across paradigms and substrates — then the
separation of activation from viability collapses and the two-level
structure reduces to a single threshold event. This condition is
inherited from *Mechanism of Identity Onset* and applies in the present
paper without modification, since the partition-warrant framing depends
on it directly. Empirical signature: configurations that exhibit
T₀-signature recovery but never exhibit closure-competent behavior —
activated but not sustainably viable, T₀-crossed but T\*-uncrossed —
under any perturbation protocol.

### 7.2 Verdict-structure falsifications by mode

The three operational modes specified in §4.2 each carry
verdict-structure commitments that can be falsified empirically.

**Rejection mode.** On rejection-mode substrates — substrates with no
closure-bearing partition under any G-equivalent labeling — W_CA should
return uniform negative verdicts: τ₀(S) = 0 for all subsystems S under
all G-related partitions. If a substrate is independently identified as
non-closure-bearing but produces T₀-signature recovery profiles under
perturbation on one or more partitions, the rejection-mode behavior
fails for that substrate class. Empirical signature: T₀-signature
recovery on substrates where no closure-bearing organization is
independently warranted. Note that the witness is exactly such a
substrate; predictions on the witness are therefore among the immediate
falsification targets.

**Selection mode.** On selection-mode substrates — substrates with
closure-bearing structure under one partition and not under G-related
alternatives — W_CA should return differential T₀ verdicts across
G-related partitions. If a substrate independently identified as
supporting closure-bearing structure under a uniquely specifiable
partition produces uniform T₀ verdicts across all G-related candidates,
the selection-mode behavior fails for that substrate class. Biological
cells and well-individuated regulatory networks are the canonical
selection-mode candidates; failure of differential verdicts on such
substrates would be substantial evidence against the warrant's
discriminative claim. Empirical signature: uniform T₀ verdicts on
substrates where the closure-bearing partition is independently
identifiable.

**Stratification mode.** On stratification-mode substrates — substrates
with closure-bearing structure under multiple G-related partitions —
W_CA should return differential margin profiles even where binary T₀
verdicts coincide. If candidate cases of nested identity (a cell within
a multicellular organism, an individual within a colonial structure)
yield W_CA evaluations that do not differentiate the nested partitions
through margin-profile structure, the stratification-mode behavior fails
for that substrate class. Stratification-mode operationalization is the
least developed of the three modes in the corpus; the present
specification of its falsification condition is structural, with
empirical protocols for nested-identity substrates remaining to be
developed in companion work. Empirical signature: identical μ\* profiles
across G-related partitions on substrates where nested closure-bearing
structure is independently warranted.

### 7.3 Discriminative-scope falsification

The non-G-invariance claim of §4 is established at the predicate level
by structural argument; its empirical reach requires demonstration on at
least one substrate class. If, across all substrate classes accessible
by available perturbation protocols, W_CA returns identical verdicts on
all G-related partitions, then the predicate's non-G-invariance is
empirically vacuous regardless of its structural specification. The
substrate-class non-emptiness condition is therefore a falsification
condition in itself.

The condition is partially testable on existing substrates without
requiring novel experimental development. Biological cells with
well-characterized membrane-localized regulatory feedback are
selection-mode candidates for which selection-mode discriminative
behavior should be empirically demonstrable using available perturbation
protocols. Cognitive systems with explicit homeostatic dynamics on
internal state variables are a second candidate class. The corpus's
pre-registered anesthesia state-transition program (Thomas, 2026d)
operates on substrates where the closure-bearing/non-closure-bearing
distinction can be probed across induction and emergence trajectories,
providing one specific avenue for substrate-class discriminative
testing.

The condition has a structural failure mode worth noting separately. If
the only substrates on which W_CA produces differential verdicts are
substrates where independent closure-bearing identification is itself
contested — if W_CA's discriminative work cannot be demonstrated on
substrates with uncontested closure-bearing identification — then the
warrant's discriminative power is structurally entangled with the very
identifications it is meant to license. Demonstrating discriminative
work on substrates where closure-bearing identification is independently
warranted is therefore essential to the warrant's empirical standing,
and is the primary task of the empirical companion programs.

Cells recur as the canonical exemplar in the present paper for three
structural reasons: their individuation is relatively uncontested across
philosophical and empirical traditions; their regulatory organization is
well-characterized and admits explicit identification of corrective
dynamics, governance structure, and resource budgeting; and their
perturbation structure is experimentally accessible through
well-developed methods in cell biology. Other candidate substrates may
eventually replace or extend the cell as the canonical exemplar, but at
the warrant's current stage of empirical development, biological cells
offer the cleanest combination of uncontested closure-bearing
identification and accessible experimental probe. The recurrence of the
cell example throughout this paper is therefore strategic rather than
incidental.

### 7.4 Note on falsification asymmetries

The three categories of falsification are not equally severe.
Predicate-level falsifications (§7.1) refute the activation
specification itself and would require revision of the predicate or its
conditions. Verdict-structure falsifications (§7.2) refute the
predicate's behavior in specific operational modes and may admit
refinement of mode definitions or substrate-class boundaries without
abandoning the predicate. Discriminative-scope falsifications (§7.3)
refute the warrant's empirical reach, which is the most contingent of
the three commitments and most dependent on the development of companion
empirical programs.

The predicate's structural specification is robust against §7.3 in the
sense that the present paper's arguments do not require empirical
demonstration to stand. The warrant's status as a *candidate*
partition-warrant rests on its structural specification (§3) and its
non-G-invariance (§4); its status as a *demonstrated* partition-warrant
rests on §7.3-style discriminative evidence on appropriate substrate
classes. Paper 2's task is the former; the latter is the work of the
companion programs.

## 8. Scope and Limits

### 8.1 Claims and non-claims of the paper

The paper establishes five structural commitments. First, closure
activation, formalized as the partition-evaluative predicate W_CA with
verdict tuple (τ₀, μ\*, κ) per subsystem, satisfies the slot
requirements for a partition-warrant specified in Paper 1 §7. Second,
the predicate's two-axis structure — binary T₀ for the activation event,
scalar T\* for the sustained-regime threshold — is phase-structured in a
way that distinguishes the warrant from classical autopoietic
operational closure and admits the tripartite classification (closed,
closure-competent, subthreshold) by construction. Third, W_CA is
non-G-invariant at the predicate level: its sensitivity to the causal
support graph relative to the imposed subsystem boundary is not
reducible to functions of the dynamical generator and stationary
correlation structure, and an admissible transformation can change the
structure being evaluated even where verdict outputs coincide. Fourth,
the witness from Paper 1 §3 is a rejection-mode case under W_CA, and the
warrant's uniform negative verdict on its two G-related partitions is
the predicate's correctness behavior on a substrate where no admissible
partition supports closure-bearing structure. Fifth, falsification
conditions are stated at predicate, verdict-structure, and
discriminative-scope levels, with empirical signatures specified.

The paper does not claim uniqueness of closure activation as the warrant
for the partition-warrant slot. Other candidates may be better suited to
other substrate classes, and the present paper's contribution is one
defensible filling of the slot rather than its definitive solution. The
paper does not claim full empirical demonstration of selection-mode and
stratification-mode discriminative behavior; this work is the task of
companion empirical programs and depends on substrate-specific protocol
development. The paper does not claim full operationalization of
stratification-mode protocols; this is the least empirically developed
of the three modes in the current corpus, and the present specification
of its falsification conditions is structural rather than experimentally
instantiated. The paper does not supply an adjudication procedure for
closure-bearing identification independent of W_CA's own verdict
structure; current adjudication relies on independently motivated
exemplars rather than on a fully formalized independence criterion. The
paper does not claim demonstrated joint sufficiency across all substrate
classes; the conditions are stated as jointly necessary, and their joint
sufficiency is a structural commitment whose empirical reach depends on
the companion empirical programs.

### 8.2 Substrate-class scope by mode

The warrant's operational behavior partitions naturally by mode and by
substrate class.

Rejection-mode substrates are those without closure-bearing structure
under any G-equivalent labeling: harmonic-oscillator-style substrates
dissipated by external thermal coupling, simple chemical reaction
networks without internally governed regulatory feedback, abiotic
crystalline structures, and similar systems characterized by external
maintenance through dissipation rather than internal governance. The
witness of Paper 1 §3 is a representative case. The warrant's
contribution on such substrates is to rule them out as closure-bearing
despite battery-level signatures of persistence and coherence.

Selection-mode substrates are those with closure-bearing structure under
one partition and not under G-related alternatives. Biological cells
with well-characterized membrane-localized regulatory feedback are the
canonical case: the partition along the cell membrane selects a
configuration whose corrective dynamics are internally governed and
whose maintenance budget is internally viable; G-related alternatives
that draw partitions across the membrane do not preserve this structure.
Cognitive systems with explicit homeostatic dynamics on internal state
variables — feedback loops monitoring internally specified target
variables and recruiting corrective response — are a second candidate
class. The warrant's contribution on such substrates is to differentiate
the closure-bearing partition from G-related alternatives that the
persistence/coherence battery cannot distinguish.

Stratification-mode substrates are those with closure-bearing structure
under multiple G-related partitions: nested biological organization
(cells within multicellular organisms, individuals within colonial
structures), candidate social-organizational systems with multiple
individuating levels, and similar substrates where multiple
closure-bearing partitions coexist on a single substrate with
differentiated viability profiles. The warrant's contribution on such
substrates is to differentiate the closure-bearing partitions through
margin-profile structure even where binary T₀ verdicts coincide. As
noted in §7.2, stratification-mode operationalization is the least
developed component in the current corpus.

### 8.3 Position in the corpus's evaluator hierarchy

The paper's specification of W_CA implies a structural ordering across
three corpus elements. W_CA evaluates whether a partition's subsystems
are configurations of the kind to which IMC-governed analysis applies —
whether the imposed subsystem boundary yields closure-bearing structure
for which viability bounds are well-defined. The Invariance Maintenance
Condition then governs the upper bound on perturbation load that
closure-bearing configurations can absorb without identity loss. The
Viable Perturbation Regime characterizes the perturbation environment
within which IMC-governed bounds are evaluated and within which the
warrant's perturbation protocols are designed. The three structures are
nested: W_CA upstream of IMC upstream of VPR, with each layer evaluating
the conditions for the next layer's applicability. The warrant is
therefore the outermost evaluator in this stack — IMC analysis
presupposes that the substrate under examination is closure-bearing in
the sense W_CA evaluates, and VPR design presupposes that IMC bounds are
meaningful for the partition under examination.

This ordering is implicit in the corpus's structure but not previously
stated in this form. Its methodological consequence is that IMC-governed
viability analysis is not universally substrate-applicable merely
because a persistent dynamical structure exists; its applicability is
conditioned on the closure-bearing properties W_CA evaluates.

### 8.4 The meta-taxonomy contribution and a structural asymmetry

The route × mode cross-tabulation developed in §6 supplies a
methodological output distinct from the warrant specification itself.
The taxonomy locates each candidate partition-warrant by the source of
its discriminative work (route taxonomy: external selection, internally
generated non-invariant property, refined transformation group) and by
its verdict-structure behavior across substrate classes (rejection,
selection, stratification modes). The two classifications are
orthogonal, and their cross-tabulation provides a frame for locating
closure activation among existing candidates and for assessing further
candidates the slot may yet admit. This frame is independent of whether
closure activation is accepted as the right warrant for any particular
substrate class; it is a structural classification scheme that survives
the displacement of any individual candidate.

A nesting relation between two ontological classes follows from the
warrant's specification, and its acknowledgment matters even though its
full development belongs in separate work. Battery observables in Paper
1's sense characterize dynamical organization broadly — coherence,
persistence, integration across regions of substrate space — and apply
wherever the relevant dynamical structure is well-defined. W_CA's
conditions are more demanding: they require an internally specified
target, internally governed correction, and internally sustained budget
relative to an imposed subsystem boundary. The class of closure-bearing
systems is therefore a proper subset of the class of persistence-bearing
systems under the battery characterization of Paper 1. The structural
rarity of closure-bearing organization, where it obtains, is a derivable
consequence of the activation conditions' joint stringency rather than a
brute fact about the universe or an anthropic selection effect. The
implication that this nesting helps account for the apparent ubiquity of
coherence-like phenomena in nature alongside the comparative rarity of
identity-bearing recursive organization is flagged here and reserved for
development in separate work.

### 8.5 Forward-pointers to companion work

The empirical demonstration of W_CA's selection-mode and
stratification-mode behavior depends on companion programs. The
pre-registered anesthesia state-transition program in the corpus
(Thomas, 2026d) operates on substrates where the
closure-bearing/non-closure-bearing distinction can be probed across
induction and emergence trajectories, providing one specific avenue for
substrate-class discriminative testing. Cell-biology operationalization
of selection-mode protocols on uncontested closure-bearing exemplars is
a second avenue. Stratification-mode protocol development for
nested-identity substrates remains open work, with the present paper
supplying its falsification structure but not its empirical
instantiation.

Several open structural questions are flagged but not addressed in the
present paper, and are forwarded to other components of the corpus or to
future work: scaling properties of the activation conditions across
system size and complexity; nested-level variants relating multiple
partitioning levels on the same substrate; hysteresis structure
governing the gap between nucleation and dissolution thresholds; and
frame-relativity of activation conditions under transformation group
choice. Each is structurally consequential but requires independent
development that exceeds the scope of a partition-warrant specification.

### 8.6 The Paper 1 / Paper 2 sequential structure

The present paper completes the sequential structure announced in Paper
1 §7.5, with revisions to that section's wording reflected in the V2 of
Paper 1 deposited alongside this paper. Paper 1 establishes that
persistence-based frameworks are insufficient to individuate the systems
they characterize without a supplementary partition-warrant condition;
the present paper proposes one specific candidate filling that slot and
develops its formal specification, non-G-invariance, witness verdict
structure, distinctions from alternative candidates, and falsification
conditions. Neither paper depends on the other's substantive proposals
being accepted: the slot may be real even if closure activation is wrong
about its content, and a different proposal may eventually fit the slot
better. What is stable across both papers is the structural finding —
individuation in persistence-based frameworks is not battery-alone, the
supplementary condition admits structural assessment, and candidate
warrants can be compared on the same structural terms.

The research program the two papers jointly enable is the development
and assessment of multiple candidate warrants against substrate classes,
with the present paper supplying one defensible candidate and a
methodological frame within which that candidate and others can be
evaluated. Closure activation's claim to the slot rests on its
structural specification; its empirical standing depends on companion
programs whose results lie outside the scope of the present work. The
warrant is offered as a contribution to that research program rather
than as its conclusion.

### 8.7 The decomposition the two papers jointly enable

The two papers, taken together, separate three questions the field has
often conflated.

What persists dynamically — the question battery-style observables
address, concerning coherence, persistence, integration, and other
dynamical signatures of organized structure. This question is
well-developed in the existing literature and is not in dispute as a
category of inquiry, even where specific frameworks compete on its
operationalization.

What individuates structurally — the question of which subsystem under
what imposed boundary counts as the unit whose persistence the battery
is reading, and how that boundary is selected from the G-equivalence
class of admissible candidates. Paper 1 establishes that this question
is not answered by battery observables alone, and names the
supplementary structural condition required to answer it.

What sustains recursive closure — the question of whether, under a given
imposed boundary, the configuration's maintenance dynamics exhibit the
recursive constraint enforcement that closure-bearing organization
requires. The present paper proposes that this question is structurally
distinct from the first two and addresses it through the activation
predicate W_CA.

The three questions correspond to three distinct structural commitments
and admit independent answers. A substrate may persist without being
individuated, and may be individuated without being closure-bearing —
three nested conditions whose conflation has been the field's
characteristic methodological obstacle, particularly in framing
comparisons between consciousness theories operating at different layers
of this stack. The two papers' contribution is to disentangle the first
two stages and propose a candidate filling for the third; the
architecture of any further work in this direction depends on the
decomposition being in place. Without it, the questions collapse into
one another, and the structural specifications proper to each get
treated as if they belonged to the others.

## References

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge
University Press.

Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical
approaches to conscious processing. *Neuron*, 70(2), 200–227.

Friston, K. (2010). The free-energy principle: a unified brain theory?
*Nature Reviews Neuroscience*, 11(2), 127–138.

Kirchhoff, M., Parr, T., Palacios, E., Friston, K., & Kiverstein, J.
(2018). The Markov blankets of life: autonomy, active inference and the
free energy principle. *Journal of the Royal Society Interface*,
15(138), 20170792.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The
Realization of the Living*. D. Reidel.

Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology
to the mechanisms of consciousness: Integrated Information Theory 3.0.
*PLOS Computational Biology*, 10(5), e1003588.

Thomas, C. S. (2026a). *Closure Activation: The Mechanism of Identity
Onset*. Zenodo. <https://doi.org/10.5281/zenodo.19162300>

Thomas, C. S. (2026b). *The Invariance Maintenance Condition (IMC) V2:
Complete Series*. Zenodo. <https://doi.org/10.5281/zenodo.19042041>

Thomas, C. S. (2026c). *Persistence Without Individuation: A Witness
Model for Metric-Preserving Identity Underdetermination*. Zenodo.
<https://doi.org/10.5281/zenodo.19762405>

Thomas, C. S. (2026d). *A Pre-Registered Two-Stage Empirical Program for
Testing a Three-Surface Decomposition of Recursive Maintenance Cost in
Anesthesia State Transitions*. Zenodo.
<https://doi.org/10.5281/zenodo.18828765>

Thomas, C. S. (2026e). *The Viable Perturbation Regime Concept*. Zenodo.
<https://doi.org/10.5281/zenodo.19421091>

Tononi, G. (2008). Consciousness as integrated information: a
provisional manifesto. *The Biological Bulletin*, 215(3), 216–242.

Varela, F. J. (1979). *Principles of Biological Autonomy*. North
Holland.

## Appendix A. Formal Specification of the Activation Predicate

This appendix supplies the formal apparatus underlying the body-text
specification of W_CA in §3.1, in a register that may be useful for
readers requiring more rigorous statement of the predicate's logical and
set-theoretic structure.

### A.1 Preliminaries

Let Ω denote the substrate's state space and L its dynamical generator.
A partition P of the substrate's degrees of freedom induces a
decomposition

Ω ≅ 𝔇\_{S ∈ Ind(P)} Ω(S),

where 𝔇 denotes the appropriate product, tensor-product, or direct-sum
construction for the substrate class. The partition P imposes a
subsystem boundary around each S, defining its state-space coordinates
as the variables in Ω(S) and its environment as the variables in Ω \\
Ω(S). The admissible transformation group G is specified as in Paper 1
§A.4: the subgroup of substrate transformations preserving (L, 𝒞), where
𝒞 is the stationary correlation structure.

### A.2 The activation predicate

The activation predicate τ₀: Ind(P) → {0, 1} is defined for each S ∈
Ind(P) by:

τ₀(S) = 1 ⟺ (C1)(S) ∧ (C2)(S) ∧ (C3)(S),

where the three conditions are:

(C1)(S): There exists a corrective target T(S) ⊆ Ω(S) — a subset of S's
own state-space coordinates specifying the configuration to be
maintained — and a constraint K(S) over Ω(S) such that K(S) is the
operative target structure governing S's maintenance dynamics.

(C2)(S): There exist corrective dynamics R(S) defined over Ω(S) such
that R(S) acts to restore (T(S), K(S)) under perturbation, and R(S) is
governed from within S — its initiation, targeting, and termination
depend on internal state of Ω(S) and not on transferred control from
configurations outside S.

(C3)(S): The maintenance budget β(S) — the resources required to sustain
R(S) on S's operating timescale τ_S — is internally available: there
exist resource flows within Ω(S) of magnitude ≥ β(S), with
sustainability not contingent on unbounded external subsidization.

Joint necessity is the structural commitment that all three conditions
must hold simultaneously for τ₀(S) = 1. A configuration S satisfying any
strict subset of (C1)–(C3) but not all three has τ₀(S) = 0 and is
classified subthreshold under W_CA.

### A.3 The maintenance margin

For configurations S with τ₀(S) = 1, the maintenance margin μ\*(S) is
treated for the present formalization as the scalar load margin
associated with the maintenance-margin profile discussed in the main
text:

μ\*(S) = sup { λ ≥ 0 : R(S) sustains (T(S), K(S)) under perturbation of
magnitude ≤ λ within VPR's admissible region for S }.

The profile referenced in the main text is the underlying empirical
object — the response of the configuration across the load × richness
space of VPR — from which the scalar μ\*(S) is extracted as the supremal
viable load. A configuration with μ\*(S) \> 0 has crossed T\*; a
configuration with τ₀(S) = 1 and μ\*(S) = 0 is closure-competent.

### A.4 Classification

The classification κ: Ind(P) → {closed, closure-competent, subthreshold}
is determined by:

κ(S) = closed if τ₀(S) = 1 and μ\*(S) \> 0, κ(S) = closure-competent if
τ₀(S) = 1 and μ\*(S) = 0, κ(S) = subthreshold if τ₀(S) = 0.

### A.5 Verdict tuple and partition-level verdict

The per-subsystem verdict tuple is W_CA(P, S) = (τ₀(S), μ\*(S), κ(S))
with μ\*(S) marked unevaluated when τ₀(S) = 0. The partition-level
verdict is

W_CA(P) = ⟨W_CA(P, S) : S ∈ Ind(P)⟩,

an ordered tuple over Ind(P). Aggregate readings (fully activated,
partially activated, non-activated) are derived properties of W_CA(P)
and not its primary content.

### A.6 Operational mode definitions

For a substrate Σ with G-related partitions {P_α}\_{α ∈ A}, where A
indexes the G-equivalence class, Σ is classified by the following
priority rule:

**Rejection mode.** Σ is in rejection mode iff τ₀(S) = 0 for all S ∈
Ind(P_α) and all α ∈ A.

**Selection mode.** Σ is in selection mode iff Σ is not in rejection
mode and there exist α, β ∈ A such that ∑*{S ∈ Ind(P_α)} τ₀(S) ≠ ∑*{S ∈
Ind(P_β)} τ₀(S).

**Stratification mode.** Σ is in stratification mode iff Σ is in neither
rejection nor selection mode and there exist α, β ∈ A with ∑*{S ∈
Ind(P_α)} τ₀(S) = ∑*{S ∈ Ind(P_β)} τ₀(S) \> 0 such that the multisets
{μ\*(S) : S ∈ Ind(P_α), τ₀(S) = 1} and {μ\*(S) : S ∈ Ind(P_β), τ₀(S) =
1} differ.

The priority rule produces mutually exclusive and jointly exhaustive
classifications: rejection is checked first, selection second,
stratification third.

##

## Appendix B. Witness Perturbation Analysis

This appendix develops the perturbation analysis underlying the §5
verdict on the Paper 1 witness. The analysis is structural rather than
experimental; the calculations shown demonstrate that the
configuration-relative path-dependence signature on which T₀ detection
depends is absent for the witness substrate, supporting the §5
conclusion that τ₀ = 0 under both P₁ and P₂.

### B.1 The discriminative perturbation protocol

A discriminative perturbation, in the activation-detection sense, is a
perturbation whose recovery profile reveals whether the configuration's
maintenance dynamics depend on which prior configuration was being
maintained — i.e., whether recovery is configuration-relative or merely
state-relative. The protocol structure is:

1.  Prepare the configuration in a state corresponding to one of two
    distinct prior maintenance regimes (call these regime A and regime
    B).
2.  Apply a perturbation of magnitude δ at time t₁, displacing the
    configuration to a state (q\*, p\*) that is identical between the
    two preparations.
3.  Allow the configuration to recover for time τ_R, yielding final
    state (q_A(t₁ + τ_R), p_A(t₁ + τ_R)) for the regime-A preparation
    and (q_B(t₁ + τ_R), p_B(t₁ + τ_R)) for the regime-B preparation.
4.  Compare. If the recovery profiles depend systematically on prior
    regime (q_A ≠ q_B at all measurement times), the path-dependence
    signature is present. If they coincide ((q_A, p_A)(t) = (q_B,
    p_B)(t) for all t \> t₁), the signature is absent.

The path-dependence signature requires the configuration's maintenance
dynamics to carry memory of the prior regime through the perturbation —
memory that survives the displacement to the common post-perturbation
state. For closure-bearing systems, this memory is encoded in the
maintenance system's reference to the prior configuration; for systems
whose dynamics are state-only-determined, no such memory exists and the
signature is absent.

### B.2 Application under P₁

Under P₁ = {S_A, S_B}, S_A is the configuration carried by (q₁, p₁). The
post-perturbation evolution of S_A is governed by

dq₁/dt = p₁, dp₁/dt = −ω₀²q₁ − k(q₁ − q₂) − γp₁ + ξ₁(t).

The deterministic part of this evolution, conditional on the
post-perturbation state (q₁(t₁), p₁(t₁), q₂(t₁), p₂(t₁)) and on the
realization of bath noise ξ_i(t) for t \> t₁, is uniquely determined.
Critically, no term in the equation of motion references S_A's prior
maintenance regime — the dynamics are Markovian in the joint substrate
state.

Consider preparing S_A under two distinct prior regimes that produce
identical post-perturbation states (q₁, p₁, q₂, p₂)(t₁). By
construction, the equations of motion acting on the configuration after
t₁ are identical for both preparations: the same Hamiltonian, the same
coupling, the same damping, the same statistical bath driving.
Conditional on the noise realization, the recovery trajectories are
identical:

(q_A, p_A, q_B, p_B)*{regime A}(t) = (q_A, p_A, q_B, p_B)*{regime B}(t)
for all t \> t₁.

The recovery is fully determined by the post-perturbation state and the
noise realization; it does not depend on which prior regime produced
that state. The path-dependence signature is therefore absent under P₁,
and τ₀(S_A) = 0. By the substrate's reflection symmetry, τ₀(S_B) = 0 as
well.

### B.3 Application under P₂

Under P₂ = {S₊, S₋}, S₊ is the configuration carried by (Q₊, P₊). The
post-perturbation evolution in normal-mode coordinates is governed by

dQ₊/dt = P₊, dP₊/dt = −ω₀²Q₊ − γP₊ + Ξ₊(t),

with the antisymmetric mode evolving independently:

dQ₋/dt = P₋, dP₋/dt = −(ω₀² + 2k)Q₋ − γP₋ + Ξ₋(t).

The decoupling is exact in the linearized regime. As under P₁, no term
references the configuration's prior maintenance regime; the dynamics
are Markovian in the joint normal-mode state. Conditional on the
post-perturbation state (Q₊, P₊, Q₋, P₋)(t₁) and on the realization of
Ξ\_±(t) for t \> t₁, the recovery trajectory is uniquely determined and
independent of prior regime. The path-dependence signature is absent,
and τ₀(S₊) = τ₀(S₋) = 0.

### B.4 Conclusion of the analysis

The structural reason for the uniform absence of the path-dependence
signature is that the witness substrate's dynamics are Markovian: the
equations of motion conditional on the joint state and on the noise
realization carry no reference to prior regime. A configuration whose
maintenance dynamics encode memory of the configuration being maintained
— a closure-bearing configuration in the activation sense — would be
expected to exhibit effective path-dependence in the configuration
variable, even where the underlying substrate dynamics are themselves
Markovian. The witness substrate has no such layer; its dynamics are
exhausted by the Hamiltonian, the coupling, and the bath. The verdict τ₀
= 0 under both partitions is therefore not a contingent feature of the
parameter regime but a structural property of the substrate.

The maintenance-margin profile μ\* is undefined for both partitions
because τ₀ = 0 forecloses its evaluation. The full verdict tuple under
each partition is W_CA(P_α, S) = (0, undefined, subthreshold) for all S
∈ Ind(P_α) and α ∈ {1, 2}.

# Appendix C. The Catalytic Case

This appendix develops the catalytic-closure case introduced in §2.3 as
it bears on W_CA's verdict structure for externally scaffolded
configurations.

### C.1 Catalytic activation structurally

A configuration C₁ catalyzes the activation of configuration C₂ when
C₁'s presence modifies the boundary conditions under which C₂'s dynamics
operate, in such a way that C₂'s own activation event T₀ becomes
possible where it would not be without C₁. Three structural properties
characterize the catalytic relation.

First, the activation event remains internal to C₂. C₁ does not perform
closure on behalf of C₂; the locality of activation forecloses that
possibility. What C₁ does is alter the cost-viability landscape —
reducing the maintenance cost C₂ must bear, augmenting the restorative
capacity available to C₂'s corrective dynamics, or providing temporary
regulatory inputs that allow C₂'s own regulation to come online — so
that C₂'s dynamics can achieve admissible instantiation of recursive
constraint enforcement under the modified boundary conditions. C₂
crosses T₀ because (C1)–(C3) are locally satisfied under the catalytic
regime; (C3) in particular is satisfied because C₂'s internal resources
are sufficient under the modified conditions, even though they would be
insufficient under unmodified ones.

Second, the post-activation regime depends on C₁'s continued presence. A
catalytically activated C₂ has crossed T₀ and exhibits internally
instantiated closure under modified conditions, but the conditions that
make (C3) locally satisfiable are themselves contingent on C₁. Without
C₁, the boundary conditions revert, and (C3) ceases to hold under the
unmodified regime. The configuration falls back below T\*, but T₀
remains crossed at the level of structural specification: activation,
having occurred, is not unmade by the loss of catalytic support, but the
configuration's classification shifts from closure-competent
(T₀-crossed, T\*-uncrossed) under partitions excluding C₁ toward
subthreshold under sustained removal of C₁.

Third, catalytic dependence is a continuum, not a binary. A
configuration may be fully catalytically dependent (collapse without
C₁), partially dependent (degraded function without C₁ but residual
activation), or transitionally dependent (catalytic support during a
developmental phase, replaced by independent funding once C₂ matures).
The verdict structure W_CA returns reflects this continuum through the
maintenance-margin profile μ\*.

### C.2 Verdict structure on catalyzed configurations

Under a partition P that isolates C₂ (without C₁ in its image), W_CA
returns:

τ₀(C₂) = 1 (activation has occurred internally to C₂ under the catalytic
regime), μ\*(C₂) = 0 or close to 0 (the maintenance budget is not
internally viable without catalytic support), κ(C₂) = closure-competent.

Catalytically activated configurations are therefore classified as
closure-competent under partitions that exclude their catalysts. The
structural distinction relative to the §2.2 closure-competent class is
informative: ordinary closure-competent configurations have crossed T₀
and would benefit from increased internal resources; catalytically
activated configurations have crossed T₀ and are receiving external
resources through the catalytic relation. Both are closure-competent
under W_CA's classification, but the structural reasons for that
classification differ.

Under a partition P' that includes both C₁ and C₂, the verdict depends
on C₁'s own structural status. If C₁ is itself closure-bearing under P',
the joint configuration may exhibit closed-state behavior, with W_CA(P',
{C₁ ∪ C₂}) returning τ₀ = 1 and μ\* \> 0 jointly. If C₁ is not
closure-bearing, the joint configuration may still be classified
closure-competent or subthreshold depending on the specific dynamics.

### C.3 Implications for selection and stratification modes

The catalytic case has consequences for both selection and
stratification modes.

In selection mode, a substrate may admit two G-related partitions P and
P', where P isolates a catalytically activated configuration C₂ and P'
includes C₁. The W_CA verdicts differ structurally: under P, C₂ is
closure-competent; under P', the joint configuration may be closed.
Selection mode discrimination would in this case favor the broader
partition P' as picking out the genuinely closure-bearing configuration,
with the narrower partition P returning a closure-competent verdict that
signals the catalytic dependence. The warrant's verdict structure makes
this discrimination tractable in a way that classical operational
closure does not, because the closure-competent verdict carries
information about external dependency that a binary closed/not-closed
predicate cannot encode.

In stratification mode, substrates supporting nested-identity structure
may exhibit catalytic relations across nested levels. A multicellular
organism's cells stand in catalytic relations to the organism — the
organism provides resource flows, regulatory signals, and structural
scaffolding that cells rely on — but the resulting verdict structure is
more nuanced than a single classification can capture. W_CA may return
closed or closure-competent verdicts on isolated organismal cells
depending on the cell type, the degree of organismal dependence, and the
timescale of evaluation: hepatocytes in primary culture exhibit
different verdict structure from terminally differentiated
cardiomyocytes, and short-timescale evaluation may produce different
classification from long-timescale evaluation. Under partitions
isolating the organism, W_CA may return closed verdicts where the
cellular substrate functions as constitutive infrastructure for the
organism's closure-bearing structure. The stratification-mode reading
captures the joint dependency structure with appropriate per-substrate
calibration.

### C.4 Open structural questions

Two structural questions about the catalytic case remain open and are
flagged for future development.

The first concerns the temporal structure of catalytic dependency.
Catalytic support may be transient (a developmental phase replaced by
independent funding) or sustained (an ongoing relation). W_CA's verdict
structure as currently specified does not formally distinguish these
cases; the maintenance-margin profile μ\* is a snapshot reading, not a
temporal profile. A more refined predicate would carry temporal
information about catalytic dependency dynamics, but this development
exceeds the present paper's scope.

The second concerns frame-relativity of catalytic relations. Whether C₁
catalyzes C₂'s activation may itself be partition-relative, depending on
which configurations are picked out as candidates. Different G-related
partitions may produce different catalytic structures over the same
substrate. The question of how W_CA's verdict structure behaves under
partition transformations involving catalytic relations is structurally
consequential for stratification-mode operationalization but has not
been worked out in the corpus's current state.

##
