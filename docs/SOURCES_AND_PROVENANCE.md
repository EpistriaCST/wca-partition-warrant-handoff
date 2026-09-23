# Sources and provenance

Repository assembled 22 September 2026 from the author's research files and public deposit metadata.

## R³ archive verification — 23 September 2026

The author supplied the three latest R³ ZIP archives before GitHub publication. Every file in them matched the corresponding repository file byte-for-byte. No experimental source or result was replaced.

| Supplied archive | SHA-256 | Verification |
| --- | --- | --- |
| `r3_wca_build.zip` | `3b52a8e112dacf46a5b093fe0bf3e3a689ad1613b6b364220b04240c5def3ce3` | All three contained files matched. |
| `r3_oblique_frame_sweep.zip` | `bbd819c1e207ab17f54fd5e9081b4ca98ce7f0544f71e51b7b2af39b2dabcc32` | All three contained files matched. |
| `r3_oblique_autonomy_probe.zip` | `cc69ab0eb3939d2143ab5ea1ff2c5af8cb3bd6694f12f9831005e2d3884ac5e8` | All five contained files matched; its duplicate frame-sweep and harness sources also matched the standalone archives. |

The ZIP containers themselves are not committed because they duplicate the included source, JSON outputs, and summaries.

## Primary documents

| Repository path | Source | Transformation |
| --- | --- | --- |
| `docs/primary/closure-activation-as-partition-warrant.md` | `Closure Activation as Partition Warrant.odt` | Converted to GitHub-flavored Markdown with Pandoc; wording not substantively edited. |
| `docs/primary/single-loop-witness.md` | `W_CA Witness.docx` | Converted to GitHub-flavored Markdown with Pandoc; wording not substantively edited. |
| `experiments/two-module/design-spec.md` | `Two_Module_Spec.docx` | Converted to Markdown; an archival status notice and explicit canonical-C2 blocker were added. |
| `experiments/raf/protocol-draft.md` | `WCA_RAF_Preregistration.docx` | Converted to Markdown; an archival notice was added because the draft was neither deposited nor run. |

## Code and results

The RAF files `kin.py`, `raf.py`, and `wca_test.py` are preserved as recovered. Their presence does not convert the undeployed protocol into a preregistration or a result.

The R³ scripts, result JSON files, and summaries are preserved from the research collection. Redundant ZIP bundles were omitted because their contents duplicate the included source, results, and summaries.

### Supplementary R³ recovery — 23 September 2026

Six additional R³ files supplied after initial publication are preserved under `experiments/r3/recovered/`. They form a separate, dependency-incomplete implementation branch rather than replacements for the standalone R³ sequence already documented in the repository.

| Supplied file | SHA-256 | Repository role |
| --- | --- | --- |
| `wca_claim2_r3.py` | `3aa9271bec5d9ce510de3cbf5e4d77ab52ee6414874b3e0b65aa653a28eb3edd` | Three-coordinate substrate and partition definitions; imports thresholds from the absent `wca_claim2.py`. |
| `battery_r3.py` | `1d2b65aa485ba2c1e5f97642c89f80c955a9969de36c3afdaa33b91ae434a87a` | Gated lesion and partition battery for that branch. |
| `frame_sweep_r3.py` | `3172bdcde00623e0c60d092ee7a2c50ecff572046d5d031aff5915ef3f9dcd6c` | Constrained oblique-frame evaluator for that branch. |
| `sweep_run.py` | `f15d21196ed37e357cf5d12c6d0e201bfdbf6448223a275327362023435956bf` | Twelve-frame, two-seed sweep driver. |
| `sweep_chunk.py` | `443d090aa06a69ddc37d1536c8e9f6a02b5e3e834656fa1adc9403c2e1083120` | Chunkable six-seed sweep driver. |
| `sweep_ns6.csv` | `ab093b5f7daac185cad8a7efa73c88237a770cd3e528f287d5da6abe402b747b` | Recorded six-seed output: one admitted undivided organization and 36 rejected two-dimensional competitor rows across 12 frames. |

The Python files pass syntax compilation, and the CSV is structurally consistent with the six-seed driver. The branch was not executed during repository assembly because `wca_claim2_r3.py` depends on the still-unrecovered `wca_claim2.py`. Its recorded output is preserved as supplied, not independently reproduced.

## Known omission

The single-loop witness names three deposited source files: `wca_claim2.py`, `probes.py`, and `frame_sweep.py`. They were not present in the recovered local collection, and the deposit could not be materialized during repository assembly. The recovered `wca_claim2_r3.py` is not the named `wca_claim2.py`; it imports thresholds from that absent file and therefore provides dependency evidence rather than a replacement. Neither of the other two named files was recovered. No replacement was fabricated. The absence remains tracked as WCA-08.

## Authority

For claims made in the deposited papers, the deposited versions are authoritative. The repository's ledgers and route assessments explain the handoff state; they do not silently amend those deposits.
