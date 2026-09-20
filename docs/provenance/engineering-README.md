# Scale-SETI Phase-1 v0.3 Engineering Artifacts

This folder supports the Phase-1 Design Package v0.3. The synthetic data are deliberately simulated and are **not experimental evidence**. They exist only to dry-run parsing, scoring, blinding, and archival workflows before hardware commissioning.

## Folders
- `schemas/` JSON Schema definitions for trial, campaign, calibration, and scoring records.
- `data/` deterministic 100-trial synthetic commissioning campaign and scoring outputs.
- `software/score_campaign.py` reference dry-run scorer.
- `assets/` engineering figures used in the design package.

## Dry run
```bash
python software/score_campaign.py --trials data/synthetic_trials_100.csv --out data/recomputed_by_condition.csv --summary data/recomputed_summary.json
```
