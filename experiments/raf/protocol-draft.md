> **Archival handoff notice (22 September 2026).** This document was drafted as a preregistration but was not deposited and the experiment was not run. It is preserved as an attempted route. The repository assessment is that it may support a limited RAF–W_CA concordance study, but it does not resolve the proper-subclosure/matched-rival problem and should not be presented as the principal positive-selection test.

**Closure Activation on Autocatalytic Reaction Networks**

A Draft Positive-Selection Protocol for the W_CA Partition Warrant

Charles S. Thomas · Epistria, LLC · ORCID 0009-0007-6330-1053

*Archival draft. This protocol was not deposited and no W_CA evaluation
was run on the substrate class.*

1\. Purpose

Closure Activation as Partition-Warrant (Thomas, 2026; DOI
10.5281/zenodo.20114054) supplies a rejection-mode witness: a substrate
on which W_CA correctly declines to certify persistence-equivalent
partitions as closure-bearing. A positive-selection witness has remained
open: a non-biological substrate on which W_CA returns a closed verdict
on the organization-fixed partition and rejects convenience carves that
the persistence battery cannot tell apart from it.

This document fixes, in advance, the substrate, the carves, the
operationalization of W_CA, the predictions, and the pass/fail/void
criteria for such a test on autocatalytic reaction networks. The
independent warrant for which carve is organization-fixed comes from RAF
theory (reflexively autocatalytic and food-generated sets; Hordijk and
Steel), a formalism developed without reference to W_CA.

**Scope.** A pass is a positive-selection witness on one substrate
class. It does not establish joint sufficiency of (C1)–(C3) in general,
and it does not bear on any consciousness claim. A fail is a direct
result against the predicate-level commitments stated in §7 of the W_CA
paper. The outcome will be reported either way.

2\. Substrate

The substrate is the binary polymer model (Kauffman) run as a flow
reactor under mass-action kinetics.

|                       |                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Element**           | **Specification**                                                                                                             |
| Molecule types        | All binary strings of length 1 to n = 6                                                                                       |
| Food set F            | All strings of length ≤ 2 (6 species), supplied by inflow at concentration 1.0                                                |
| Reactions             | Every ligation a + b → ab and every cleavage ab → a + b with product length ≤ 6                                               |
| Catalysis assignment  | Each molecule catalyzes each reaction independently with probability p = f / \|R\|, f = 3.0; generator seeded by network seed |
| Food catalysis        | Disabled: food molecules are removed from all catalyst sets after assignment                                                  |
| Uncatalyzed reactions | None (k0 = 0): only catalyzed reactions run                                                                                   |
| Reaction rate         | v = kfac · kc · (Σ catalyst concentrations) · (reactant concentrations); kc = 1000; kfac = 1 for ligation, 0.1 for cleavage   |
| Flow                  | Dilution rate φ = 0.1 on all species; food inflow φ · 1.0                                                                     |
| Start state           | Food at 1.0; every species produced by the network's maxRAF seeded at 0.01                                                    |
| Integration           | LSODA, rtol 1e-6, atol 1e-12; burn-in T = 1000; reference = time average over the final 200 time units                        |

**Why food is non-catalytic.** In pilot runs with food catalysis
enabled, steady-state flux was dominated by single reactions catalyzed
by food molecules. Under the reading adopted here, food is environment,
not an external configuration: it may supply material (compatible with
C3) but control sourced from it would be control transferred across the
boundary (a C2 failure). Disabling food catalysis removes that confound
at the substrate level instead of settling it inside the verdict.

**Why no uncatalyzed reactions.** With background reactions enabled,
pilot runs showed dynamic autocatalysis carried by loops containing
uncatalyzed steps. Those loops are not RAFs, so RAF theory would not
supply an independent warrant for them. Setting k0 = 0 keeps the
independent warrant and the dynamics on the same object. The
background-reaction case is retained as an exploratory arm (§9).

3\. What was run before deposit

Full disclosure of pilot work, all on calibration seeds that are
excluded from the test:

- Static RAF analysis (no dynamics) on n = 8 networks, seeds 0–39, and n
  = 6 networks, seeds 0–9. Finding: RAFs appear abruptly near f ≈
  2.4–2.6 for n = 8, and their irreducible sub-RAFs are large,
  non-unique, and weakly overlapping. Sub-RAF carves were therefore
  dropped as candidate organization-fixed partitions.

- Intact-dynamics pilots (no knock-down, no severance) on n = 8, eight
  seeds between 0 and 12, across kc 1 to 1e5, φ 0.01 to 0.1, cleavage
  factor 0.01 to 1. Finding: the graph maxRAF is kinetically inert under
  these settings; almost none of it is realized in the reactor.

- Intact-dynamics pilots on n = 6: a parameter grid on seeds 0 and 2 (φ
  0.01 and 0.1, cleavage factor 0.1 and 1, food inflow 1 and 10), then
  seeds 0–19 under the parameters in §2. Finding: 1 of 20 networks
  sustains a realized autocatalytic system; the rest wash out. Viable
  networks are rare, which the admissibility gate in §4 accounts for.

- A harness check of the verdict code on a hand-built four-reaction toy
  network outside the substrate class.

No knock-down, severance, T\*, or cut-the-loop run has been performed on
any network generated from the substrate class, calibration or test.

4\. Admissibility gate and test networks

Test networks are drawn from seeds 1000, 1001, 1002, … in order. A
network is admissible if, in the intact run from the seeded start:

- its maxRAF contains at least 5 reactions;

- at least 20 non-food species have time-averaged concentration above
  1e-4;

- the non-food/food concentration ratio is at least 0.1; and

- over the second half of the burn-in, total non-food concentration
  never falls below half its mean (sustained oscillation is allowed;
  collapse is not).

The first five admissible networks form the test set. If fewer than five
are found among seeds 1000–1999, the test is VOID (substrate class
inadmissible at these parameters), not failed.

5\. Carves and the independent warrant

Let the realized set be the non-food species with time-averaged
concentration above 1e-4. Let M_r be the maxRAF of the reactions whose
reactants and products all lie in the realized set plus food. All carves
are defined on each test network before any verdict is computed. An
empty carve is skipped and its row does not count.

|           |                                                                                 |                                                 |
|-----------|---------------------------------------------------------------------------------|-------------------------------------------------|
| **Carve** | **Definition**                                                                  | **Independent status**                          |
| S_RAF     | Species produced by M_r                                                         | Organization-fixed: a realized RAF              |
| S_LEN     | Species in S_RAF of length ≤ 4                                                  | Convenience carve (short molecules)             |
| S_LONG    | Species in S_RAF of length ≥ 5                                                  | Convenience carve (long molecules)              |
| S_PER     | Species in S_RAF that are neither reactant nor catalyst for any reaction in M_r | Dead-end by-products; defined only if non-empty |
| S_CORE    | S_RAF minus S_PER                                                               | Defined only if S_PER is non-empty              |

**Persistence battery.** Every carve consists of realized species, so
every carve persists in the intact reactor by construction. The battery
(sustained non-zero concentration under the reference run) is therefore
non-discriminating across all carves. That is the condition under which
a partition warrant is needed.

6\. Operationalization of W_CA

*This operationalization is the author's own. The W_CA paper states
(C1)–(C3) and the two-axis structure but does not specify a
chemical-reaction protocol. Choices made here are part of what is being
tested.*

6.1 Severance

For a carve S, the severed reactor is the intact reactor with two
changes, applied only to reactions that produce at least one species in
S:

- **Material severance (C3).** Any such reaction with a reactant outside
  S ∪ F is disabled.

- **Control severance (C2).** Catalytic contributions from catalysts
  outside S are set to zero.

Reactions that produce no species in S run unchanged. Food inflow is
unchanged.

6.2 Discriminative perturbation (T₀ axis)

From the end state of the intact burn-in, the concentrations of all
species in S are multiplied by ε = 0.5. The severed reactor then runs
for T_rec = 500 (50 residence times). Two quantities are read off over
the final 200 time units:

- **ρ(S):** time-averaged total concentration of S divided by its intact
  reference.

- **r(S):** Pearson correlation, across the species of S, of log10
  concentrations between the recovered and intact time averages (C1:
  return to S's own configuration).

6.3 Verdict

|                          |                                                                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Output**               | **Rule**                                                                                                        |
| τ₀(S) = 1                | ρ(S) ≥ 0.01, i.e., S sustains itself far above the washout floor (≈ e⁻⁵⁰) with outside material and control cut |
| κ(S) = closed            | τ₀ = 1, ρ(S) ≥ 0.5 and r(S) ≥ 0.9                                                                               |
| κ(S) = closure-competent | τ₀ = 1 but not closed (internally governed, insufficient budget)                                                |
| κ(S) = subthreshold      | τ₀ = 0                                                                                                          |

6.4 Maintenance margin (T\* axis)

For S_RAF, the intact reference and the verdict are recomputed at φ ∈
{0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50}. μ\*(S_RAF) is reported
as the profile of ρ across the series, and the margin as the largest φ
at which κ = closed, minus 0.10. A φ at which the intact reactor itself
collapses is recorded as such.

6.5 Cut-the-loop

A keystone link is a single catalysis relation (reaction, catalyst)
inside M_r whose removal empties the RAF restricted to realized
reactions; the lowest-indexed one is used. A control link is one whose
removal shrinks that RAF by at most one reaction; one is drawn with the
network seed. For each, the link is deleted, the intact reactor is rerun
from the seeded start, and the S_RAF verdict is recomputed against the
original reference.

**Stated in advance:** with k0 = 0, keystone deletion makes collapse
close to guaranteed, so the keystone half is a consistency check. The
informative half is the control: W_CA must not reject S_RAF when a
non-essential link is cut.

6.6 Known limitation

The W_CA paper states the T₀ signature as configuration-relative
path-dependent recovery. Here the configuration-relative element is
carried by severance (recovery must run on S's own material and
catalysts) and by r(S). A direct contrast between recovery from
different prior configurations at equal state is not included in the
confirmatory test.

7\. Predictions

|                          |                                                                                               |                             |
|--------------------------|-----------------------------------------------------------------------------------------------|-----------------------------|
| **Carve / condition**    | **Predicted κ**                                                                               | **Counts toward pass/fail** |
| S_RAF                    | closed                                                                                        | Yes                         |
| S_LEN                    | subthreshold                                                                                  | Yes                         |
| S_LONG                   | subthreshold                                                                                  | Yes                         |
| S_PER (if defined)       | subthreshold                                                                                  | Yes                         |
| S_CORE (if defined)      | closed                                                                                        | No: see scratchpad arm, §9  |
| Keystone deletion, S_RAF | subthreshold                                                                                  | Yes                         |
| Control deletion, S_RAF  | τ₀ = 1                                                                                        | Yes                         |
| T\* series, S_RAF        | ρ non-increasing in φ; κ steps closed → closure-competent → subthreshold (or intact collapse) | No: descriptive             |

8\. Pass, fail, void

- **Network pass:** every "Yes" row in §7 holds for that network.

- **PASS:** at least 4 of the 5 test networks pass.

- **FAIL:** 2 or more test networks do not pass.

- **VOID:** fewer than 5 admissible networks in seeds 1000–1999, or a
  numerical failure that prevents a verdict. A void is reported as a
  void, not recast as either outcome.

Which §7 commitment a failure implicates: S_RAF not closed while
RAF-closed and realized is the joint-necessity signature. A convenience
carve returning closed is a discrimination failure. Control deletion
rejecting S_RAF means the verdict is brittle to non-essential structure.

9\. Descriptive and exploratory analyses

These are reported, labeled, and carry no weight in §8.

- **Robustness.** Verdicts for all carves recomputed at ε = 0.2 and ε =
  0.8.

- **T\* profile.** As in §6.4.

- **Scratchpad arm.** Where S_PER is non-empty, W_CA is expected to
  return closed on both S_CORE and S_RAF (core plus by-products) and not
  to select between them. This is the chemical analog of the model
  versus model-plus-scaffolding case left open in the corpus. It is
  pre-registered as an expected non-discrimination. In the single viable
  calibration network S_PER was empty, so this arm may not be estimable.

- **Background-reaction variant.** Rerun with uncatalyzed reactions
  enabled, to examine W_CA on dynamically autocatalytic loops that RAF
  theory does not count. This arm is implemented after the confirmatory
  run and is exploratory only.

10\. Deviations

Any change to code, parameters, thresholds, or seeds after deposit is
reported as a deviation, with reason, alongside results under the
original specification where those can still be computed.

11\. Code

The analysis is fully determined by the three files below, deposited
with this record. The confirmatory run is "python3 wca_test.py run".
SHA-256 hashes at deposit:

|             |                                                                  |
|-------------|------------------------------------------------------------------|
| **File**    | **SHA-256**                                                      |
| raf.py      | e5a5da28297598ef692f0ae1b206aaffba6fc432312906fe8f914126f8e5f899 |
| kin.py      | 26aac1711f37ea3b74cca07a4a6bfcf15d650bb36e7f82b0ca70f88ab944f829 |
| wca_test.py | 6eda30482aba53851f29fa9a4b0c2adcb4daaca85d9cd8c7f5e1d9aa271df198 |

Dependencies: Python 3, NumPy, SciPy.
