# Phase-1 v0.3

Read the [design document](design/Scale-SETI_Phase1_Design_Package_v0.3.pdf). This is the supplied v0.3 baseline, not a later fabrication/build release.

Hardware artifacts are under `hardware/`; schemas under `schemas/`; calibration forms under `calibration/`; the preregistration template under `acceptance/`; and simulated inputs/outputs under `synthetic-data/`.

## Dry run from this folder

The original scripts require Python, pandas and jsonschema. In an existing Python environment with these dependencies, run from `phase1/`:

```powershell
New-Item -ItemType Directory -Force local-output
python software/validate_records.py --schema schemas/campaign_manifest.schema.json --record synthetic-data/synthetic_campaign_manifest.json
python software/score_campaign.py --trials synthetic-data/synthetic_trials_100.csv --out local-output/recomputed_by_condition.csv --summary local-output/recomputed_summary.json
```

The validator accepts a single JSON record, not a JSONL stream. The import verification separately checked all 100 synthetic records. They pass the scoring-output schema but do not conform to the normative trial-record schema; see the verification report. The scoring-output schema describes per-trial records, not the campaign summary JSON.

Synthetic manifest hardware/software hashes are simulation placeholders. They are not signed records of real apparatus. No hardware calibration or acceptance is claimed. See [verification notes](../docs/VERIFICATION.md).
