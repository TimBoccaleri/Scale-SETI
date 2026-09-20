# Source inventory and provenance

The current baseline is imported from the supplied source documents and the nested full engineering release inside External Technical Review Packet v0.1.

| Material | Included |
| --- | --- |
| Concept Paper Candidate 1.0 | PDF, DOCX, Markdown; eight figures extracted from DOCX |
| Phase-1 Design Package v0.3 | PDF, DOCX, Markdown; complete supplied engineering artifacts |
| Project Roadmap v1.1 | PDF, DOCX, Markdown |
| External review v0.1 | Guide and form PDF/DOCX and an empty review log template |
| Engineering details | Four figures; BOM, I/O map, wiring schedule; four schemas; two Python scripts; seven synthetic campaign files; CAL-01 through CAL-07; preregistration template |

The detailed import ledger is retained locally with private project administration records. It is excluded from the public repository because it contains local source paths. The root manifest supplies checksums for the published files. The original container ZIP and standalone downloads remain under local-originals in the installed working folder, excluded from the distribution.

Identical paper, roadmap and design copies in overlapping packages were deduplicated. Standalone guide/form PDFs differ in bytes from the packet copies but their extracted text is identical; standalone copies are canonical. Their Word sources are from the packet. This is not a claim that the alternative PDF renderings are visually identical.

The design Markdown's four figure links were adjusted for the organized layout. Concept-paper figure files were recovered byte-for-byte from embedded Word media, matching the sequence and captions to the Markdown references. The scorer now explicitly reads its two bitstring columns as strings to avoid integer inference in pandas 3. No technical claims, data, schemas or scoring formulas were changed.

Original release manifests are preserved in docs/provenance. The engineering manifest's self-entry does not match its own delivered bytes; its other 32 entries verify. All 13 entries in the external-review manifest verify. A fresh root manifest covers the assembled project independently.

No historical revisions were supplied, so an archive folder is unnecessary. Public repository URLs, DOIs, release dates and license grants have not been invented.
