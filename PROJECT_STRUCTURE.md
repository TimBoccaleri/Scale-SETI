# Project structure

```text
Scale_SETI/
  README.md
  LICENSE                     license decision pending
  CITATION.cff                 collection metadata
  CHANGELOG.md
  CONTRIBUTING.md
  PROJECT_STRUCTURE.md
  MANIFEST.sha256              current relative-path hashes
  .gitignore
  concept-paper/              Candidate 1.0 PDF, DOCX, MD and eight figures
  roadmap/                    v1.1 PDF, DOCX and MD
  phase1/
    README.md                 synthetic dry-run instructions
    design/                   v0.3 PDF, DOCX and MD
    figures/                  four original engineering figures
    hardware/bom/             reference bill of materials
    hardware/io/              I/O map
    hardware/wiring/          wiring schedule
    schemas/                  four JSON schemas
    software/                 original validator and scorer
    synthetic-data/           original simulated campaign and scoring outputs
    calibration/              CAL-01 through CAL-07
    acceptance/               preregistration template
  review/                     guide, forms and empty review log template
  docs/
    terminology.md
    SOURCE_INVENTORY.md
    # Detailed import ledger retained privately, outside the public tree.
    VERIFICATION.md
    provenance/               original release manifests and README files
  local-originals/            local-only original downloads; not in clean ZIP
```

There are no historical revisions in this delivery. If retained later, place superseded revisions only under `archive/` and label them clearly. Original duplicate delivery containers belong in local-originals, not the current source tree.

The engineering scripts take explicit input/output paths. The scorer has one explicit CSV string-type fix for compatibility with pandas 3; scoring logic is unchanged. The design Markdown's four image paths were adjusted. Original manifests retain their original path strings as provenance; use the root MANIFEST.sha256 to verify this workspace.

Regenerate the workspace manifest after intentional edits. The manifest excludes itself and local-only backup, scratch and private material.
