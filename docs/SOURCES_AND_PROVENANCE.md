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

## Canonical single-loop source recovery — 23 September 2026

The author supplied the three exact source filenames identified in the deposited single-loop witness. They are preserved unchanged under `experiments/single-loop/src/`.

| Supplied file | SHA-256 | Verification |
| --- | --- | --- |
| `wca_claim2.py` | `e2b88c4c0a1343e30ebe51acf737dd8273ad7e466b945560d8c6953806fc6fce` | Thresholds and implementation structure correspond to the deposited paper; imports and syntax valid. |
| `probes.py` | `c916dbf29d41d0ff08a134fcdc46d0f49f6bc10f9a4149a63e61376bd7cca9f6` | Executed unchanged; all five precommitted probes passed. |
| `frame_sweep.py` | `ca5beab1f9173ee18ce4a6931bf29b4c82d1846c5c4175087777a114fa913d84` | Executed unchanged; organization admitted, all 60 split blocks rejected, minimum enforcement fraction rounded to `0.29`. |

Execution used Python 3.12.14 and NumPy 2.3.5 in a temporary directory. The behavior reproduced the results stated in the witness. The hashes above establish the repository bytes; byte identity with the remote Zenodo file objects was not independently checked because a remote checksum manifest was not available during assembly.

The preserved `wca_claim2.py` contains an inline comment stating that all splits exceed `0.26`; the executed `frame_sweep.py` and deposited paper report a rounded minimum of `0.29`. The operative C2 threshold is `0.15`, so the conservative comment discrepancy does not alter the code path or verdict.

## Primary documents

| Repository path | Source | Transformation |
| --- | --- | --- |
| `docs/primary/closure-activation-as-partition-warrant.md` | `Closure Activation as Partition Warrant.odt` | Converted to GitHub-flavored Markdown with Pandoc; wording not substantively edited. |
| `docs/primary/single-loop-witness.md` | `W_CA Witness.docx` | Converted to GitHub-flavored Markdown with Pandoc; wording not substantively edited. |
| `experiments/two-module/design-spec.md` | `Two_Module_Spec.docx` | Converted to Markdown; an archival status notice and explicit warning about extending the recovered scalar C2 ratio to higher-dimensional modules were added. |
| `experiments/raf/protocol-draft.md` | `WCA_RAF_Preregistration.docx` | Converted to Markdown; an archival notice was added because the draft was neither deposited nor run. |

## Code and results

The RAF files `kin.py`, `raf.py`, and `wca_test.py` are preserved as recovered. Their presence does not convert the undeployed protocol into a preregistration or a result.

The R³ scripts, result JSON files, and summaries are preserved from the research collection. Redundant ZIP bundles were omitted because their contents duplicate the included source, results, and summaries.

### Supplementary R³ recovery — 23 September 2026

Six additional R³ files supplied after initial publication are preserved under `experiments/r3/recovered/`. They form a separate implementation branch rather than replacements for the standalone R³ sequence already documented in the repository.

| Supplied file | SHA-256 | Repository role |
| --- | --- | --- |
| `wca_claim2_r3.py` | `3aa9271bec5d9ce510de3cbf5e4d77ab52ee6414874b3e0b65aa653a28eb3edd` | Three-coordinate substrate and partition definitions; imports thresholds from the recovered canonical `wca_claim2.py`. |
| `battery_r3.py` | `1d2b65aa485ba2c1e5f97642c89f80c955a9969de36c3afdaa33b91ae434a87a` | Gated lesion and partition battery for that branch. |
| `frame_sweep_r3.py` | `3172bdcde00623e0c60d092ee7a2c50ecff572046d5d031aff5915ef3f9dcd6c` | Constrained oblique-frame evaluator for that branch. |
| `sweep_run.py` | `f15d21196ed37e357cf5d12c6d0e201bfdbf6448223a275327362023435956bf` | Twelve-frame, two-seed sweep driver. |
| `sweep_chunk.py` | `443d090aa06a69ddc37d1536c8e9f6a02b5e3e834656fa1adc9403c2e1083120` | Chunkable six-seed sweep driver. |
| `sweep_ns6.csv` | `ab093b5f7daac185cad8a7efa73c88237a770cd3e528f287d5da6abe402b747b` | Recorded six-seed output: one admitted undivided organization and 36 rejected two-dimensional competitor rows across 12 frames. |

After recovery of `wca_claim2.py`, the branch was executed without modifying its files. The gated battery admitted the organization, rejected the same-dimensional pseudo-unit, and rejected the passive negative control. Running `sweep_chunk.py 0 12` regenerated `sweep_ns6.csv` byte-for-byte with SHA-256 `ab093b5f7daac185cad8a7efa73c88237a770cd3e528f287d5da6abe402b747b`.

## Authority

For claims made in the deposited papers, the deposited versions are authoritative. The repository's ledgers and route assessments explain the handoff state; they do not silently amend those deposits.
