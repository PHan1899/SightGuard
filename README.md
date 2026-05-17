# SightGuard

**Cross-Modal Safety Alignment for Robust Vision-Language Models**

This repository prepares the code and datasets for experiments on reducing the modality gap and improving jailbreak robustness in LLaVA-1.5-7B.

## Project Structure

| Path | Description |
| --- | --- |
| `repos/SaferVLM` | UnsafeConcepts / Bridging-the-Gap codebase |
| `repos/SaferVLM/data/UnsafeConcepts` | UnsafeConcepts metadata and 1567 images |
| `repos/JailBreakV_28K` | JailBreakV-28K codebase |
| `repos/JailBreakV_28K/JailBreakV_28K` | Trimmed JailBreakV report subset |
| `experiment_results_tracking.md` | Experiment result tracking document |

## JailBreakV Report Subset

The report uses a fixed 2000-sample stratified subset from JailBreakV-28K.

| Attack format | Count | Ratio |
| --- | ---: | ---: |
| Template | 740 | 37.0% |
| Persuade | 130 | 6.5% |
| Logic | 30 | 1.5% |
| figstep | 500 | 25.0% |
| SD | 200 | 10.0% |
| SD_typo | 200 | 10.0% |
| typo | 200 | 10.0% |
| Total | 2000 | 100% |

Files:

- Default evaluation CSV: `repos/JailBreakV_28K/JailBreakV_28K/JailBreakV_28K.csv`
- Reproducible subset CSV: `repos/JailBreakV_28K/JailBreakV_28K/JailBreakV_2K_report_subset_seed2024.csv`
- Sampling seed: `2024`

The JailBreakV data directory has been trimmed to contain only images referenced by the 2000-sample subset.

## Suggested Report Title

**SightGuard: Hardening Vision-Language Models Against Cross-Modal Jailbreaks**
