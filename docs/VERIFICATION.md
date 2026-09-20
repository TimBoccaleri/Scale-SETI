# Verification of initial local assembly

- External-review source manifest: all 13 listed files match.
- Engineering source manifest: all 32 non-manifest files match; its own self-hash entry differs. Original manifest preserved unchanged.
- Copies and extracted figure bytes checked against source hashes in IMPORT_LEDGER.csv.
- Four supplied JSON schemas pass Draft 2020-12 schema checks.
- Campaign manifest validates. All 100 synthetic JSONL records satisfy the per-trial scoring schema.
- All 100 synthetic JSONL records fail the normative trial-record schema. This inherited incompatibility is recorded below, without changing the supplied data or schema.
- Recomputed Hamming distances, exact-match flags and rounded bit accuracies agree with all 100 trial records.
- Original scorer failed with pandas 3.0.1 because its bitstring CSV fields were inferred as integers. After explicitly typing the two columns as strings, the scorer runs successfully. Recomputed summary and grouped results match the supplied outputs.
- Synthetic positive-control mean bit accuracy: 99.468752%; control mean: 49.416664%; exact matches in controls: 0.
- Eight concept-paper figure links restored from embedded Word images; four design figure links adjusted. Local Markdown links checked after assembly.

## Limits and inherited issues

These are packaging and synthetic-pipeline checks, not hardware acceptance or evidence for the hypothesis. No calibration measurements were supplied; the calibration schema was checked structurally, not exercised with real calibration records. No preregistration or external review completion is claimed.

The synthetic JSONL uses simplified IDs such as SYN-001 instead of UUIDs; omits campaign_id, protocol_version, raw_receiver_sha256, telemetry_sha256 and score_status; and adds scoring properties disallowed by the normative trial schema. It is useful for scoring dry runs but is not a valid example of a complete normative trial record. This should be resolved in a future engineering revision, not hidden by relabeling or fabricating metadata during workspace assembly.

PDF and DOCX files are copied unchanged. Guide/form PDF variants have identical extracted text; page-layout equivalence is not asserted. A full scientific, citation, Word pagination or PDF layout review is outside this assembly pass. The supplied software is a dry-run reference implementation, not certified acquisition or statistical-analysis software. Third-party references and reviewer affiliations have not been re-researched.
