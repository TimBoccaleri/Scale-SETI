# Scale-SETI Project Roadmap and Scope Control
## Publication, Engineering, Review, and Experimental Plan

**Version 1.1**  
**Author:** Tim Boccaleri  
**Date:** September 2026

---

## 1. Purpose

This roadmap prevents scope drift and defines what each Scale-SETI artifact is supposed to accomplish. The project will no longer add material simply because additional detail is possible. Each document has a defined audience, stopping condition, and next action.

The governing rule is:

> **If a new item does not close a defined publication, reproducibility, review, or experimental gap, it does not belong in the current artifact.**

---

## 2. Project Architecture

Scale-SETI is divided into three primary products.

### Product A - Core Concept Paper

**Working title:** *Scale-SETI: A Search for Technological Intelligence Across Physical Scale*

**Purpose:** Present the intellectual contribution, scientific motivation, falsifiable research question, evidence standards, relationship to prior work, and high-level experimental roadmap.

**Primary audience:** physicists, SETI/technosignature researchers, information theorists, experimentalists, reviewers, and potential collaborators.

**Source baseline:** Revision 5 technical-review edition.

**What belongs here:**
- central Scale-SETI hypothesis and search-space framing;
- established science versus speculative extensions;
- minimal scale-coordinate framework;
- relationship to existing SETI, scale-relativity, nanocommunication, and quantum-communication work;
- falsifiability and evidence ladder;
- high-level Phase-1 experimental design;
- major objections and limitations;
- publication-quality references.
- expanded SETI search-space framework: same-scale, down-scale, and up-scale search;
- wall analogy for the shared-boundary concept;
- bidirectional macro/micro model;
- up-scale SETI as a conceptual/distributed-analysis branch distinct from Phase 1.

**What does not belong here:**
- connector pinouts;
- full wiring schedules;
- detailed procurement BOMs;
- calibration worksheets;
- software repository internals;
- fabrication drawings;
- step-by-step bench assembly procedures.

**Target size:** approximately 25-35 pages including references and essential figures.

**Definition of done:**
1. hypothesis is clear and internally consistent;
2. established science is clearly separated from speculation;
3. novelty and prior work are accurately represented;
4. falsifiable experimental proposition is explicit;
5. evidence and failure criteria are defined;
6. major objections are addressed;
7. external reviewers have had an opportunity to critique the work;
8. only changes improving scientific accuracy, clarity, or reviewer response remain.

Once these conditions are met, the document becomes **Scale-SETI Concept Paper 1.0** and is frozen except for corrections or peer-review changes.

### Product B - Phase-1 Technical Design Package

**Purpose:** Allow an independent instrumentation/microfluidics laboratory to reproduce the first controlled experiment without guessing important design decisions.

**Primary audience:** instrumentation engineers, microfluidics researchers, electronics engineers, experimental physicists, software/data engineers, and replication laboratories.

**Current baseline:** Phase-1 Design Package v0.3.

**What belongs here:**
- complete system architecture;
- electrical and fluidic schematics;
- wiring and I/O maps;
- mechanical/fabrication drawings;
- BOM and alternates;
- host/network isolation design;
- software interfaces and schemas;
- calibration procedures;
- control matrix;
- acceptance criteria;
- bring-up procedure;
- troubleshooting and replication instructions;
- release manifests and hashes.

**Definition of done:**
1. all critical components are identified by part number or performance specification;
2. every intentional signal path is documented;
3. every relevant leakage path has a mitigation or measurement plan;
4. all electrical/fluidic interfaces are documented;
5. calibration and acceptance procedures are executable;
6. data schemas and software interfaces are validated;
7. another qualified lab can build the system from the package;
8. unresolved decisions are non-critical or explicitly documented.

When these conditions are met, the design becomes **Phase-1 Technical Design Package 1.0**. Additional features must then be handled through controlled engineering change requests rather than informal expansion.

### Product C - Experimental Results Paper

**Provisional title:** *Scale-SETI Phase I: Experimental Constraints on Information-Bearing Anomalies in Microscopic Communication Interfaces*

**Purpose:** Report actual experimental results, including null results, after the Phase-1 apparatus has passed commissioning and the analysis has been preregistered.

**What belongs here:**
- final apparatus actually used;
- deviations from Design Package 1.0;
- preregistered hypotheses and analysis;
- calibration and acceptance results;
- control results;
- blinded trial results;
- statistics and uncertainty;
- anomaly investigation;
- raw-data availability;
- independent replication status.

This paper does **not** exist until there are real experimental data.

---

## 3. Current Project Status

| Milestone | Status | Notes |
|---|---|---|
| Original idea | Complete | Search for intelligence across physical scale |
| Conceptual hypothesis | Complete | Hierarchical / nonlinear scale framing |
| Scientific framing | Complete | Established science separated from speculation |
| Falsifiability framework | Complete | Challenge-response and control hierarchy defined |
| Formal technical review | Complete | Revision 5 |
| Phase-1 reference architecture | Complete | Known-physics validation bench |
| Engineering control documents | Complete | Through v0.3 |
| Stage-1 implementation choice | Complete | Ion concentration / microfluidic reference channel |
| Dry-run software/data pipeline | Complete | Synthetic campaign demonstrated |
| Fabrication/build release | Next | Close remaining reproducibility gaps |
| External expert review | NEXT | Publication gate before freeze and costly build |
| Concept Paper Candidate 1.0 | Complete | Expanded same-scale/down-scale/up-scale framework; ready for external review |
| Public preprint / DOI | Pending | Zenodo / OSF first |
| Physical prototype | Pending | After design review |
| Commissioning | Pending | Acceptance gates before search experiment |
| Search experiment | Pending | Only after validated baseline |
| Results paper | Pending | Based on real data |

---

## 4. Remaining Work Before External Review

**v1.1 scope boundary:** The up-scale SETI concept belongs to Product A and does not reopen the Phase-1 microscopic engineering scope. Any future distributed up-scale sensor/probe architecture is deferred until after Concept Paper 1.0 review and publication planning.

The project should complete only the engineering items necessary for a competent external reviewer to evaluate reproducibility and failure modes.

### Required Design-Package Closure Items

- dimensioned receiver-cell / flow-cell drawing;
- complete electrical schematic with component values;
- grounding, shielding, and isolation schematic;
- fluidic assembly drawing;
- connector and pin schedule;
- final procurement BOM with quantities, alternates, and performance requirements;
- physical cable-routing and zone-boundary drawing;
- bench assembly procedure;
- bench bring-up sequence;
- troubleshooting matrix;
- acceptance-test procedure and forms;
- list of unresolved engineering assumptions.

These are closure items because they directly affect reproducibility. Anything beyond these should require a specific identified need.

---

## 5. External Technical Review Plan

The goal of external review is criticism, not endorsement. Reviewers should be asked to identify failure modes, prior art, leakage paths, statistical weaknesses, or reproducibility gaps.

### Desired reviewer mix

Seek approximately 5-10 reviewers or contacts, expecting only a subset to respond, across:
- molecular communication;
- microfluidics;
- nanosensors;
- experimental physics;
- instrumentation and low-noise measurement;
- statistics/information theory;
- quantum measurement;
- SETI/technosignatures.

### Questions reviewers should answer

1. Is there a known conventional physical pathway that invalidates the proposed isolation logic?
2. Are the positive, negative, sham, delayed, replay, clock, and network controls sufficient?
3. Are the statistical thresholds and multiple-testing controls defensible?
4. Is important prior work missing?
5. Does any existing literature make the central proposal non-novel?
6. Could another lab reproduce Phase 1 from the design package?
7. Which assumptions require direct measurement before a confirmatory experiment?
8. What result would the reviewer personally consider strong enough to justify escalation?

### Review disposition categories

Each comment should be logged as:
- **Critical** - invalidates a claim, control, or design assumption; must be resolved before release.
- **Major** - materially improves reproducibility, statistics, or scientific framing; normally resolved before release.
- **Minor** - clarity, terminology, formatting, or non-critical implementation improvement.
- **Deferred** - valid but outside the defined scope of Concept Paper 1.0 or Phase-1 Design Package 1.0.
- **Rejected with rationale** - reviewed but not adopted; reasoning documented.

---

## 6. Publication Plan

### Stage 1 - Candidate Release

Create:
- **Scale-SETI Concept Paper - Candidate 1.0**
- **Scale-SETI Phase-1 Technical Design Package - Candidate 1.0**

These are circulated privately for external technical review.

### Stage 2 - Public Preprint and Research Record

After reviewer feedback is incorporated:
- publish Concept Paper 1.0 on a DOI-bearing repository such as Zenodo;
- create an OSF project for protocols, preregistration, datasets, code, and later updates;
- archive Design Package 1.0 and the software/data schemas with versioned release hashes;
- maintain a stable author identity and ORCID.

### Stage 3 - arXiv / scholarly distribution

Attempt an appropriate arXiv submission once the paper has matured and any endorsement/category requirements are addressed. Use the DOI/preprint as the canonical version record if needed.

### Stage 4 - Journal or conference submission

Choose a venue based on what the work has become after technical review. A conceptual methodology paper and an experimental-results paper may require different venues.

---

## 7. Build and Experiment Plan

### Phase 1A - Known-Physics Commissioning

Goal: prove the entire experimental and analysis pipeline using a conventional microscopic communication channel.

Success means:
- transmitter state is recoverable at the receiver;
- bit-error performance meets acceptance criteria;
- challenge generation and sealing work;
- receiver analysis remains blinded;
- blocked/sham controls establish the false-positive floor;
- telemetry captures ordinary leakage channels;
- the full 100-trial commissioning campaign is reproducible.

No claim about another scale is tested in this stage.

### Phase 1B - Stronger Isolation / Alternative Microscopic Interface

Only after Phase 1A passes. Candidate interfaces may include graphene/nanoscale receivers or other microscopic sensing technologies. The protocol should remain fixed while one physical layer is changed at a time.

### Phase 2 - Search Experiment

Only after commissioning and external review. The intentional known information path is removed or blocked while the blinded challenge and receiver infrastructure remains.

Escalation requires preregistered criteria. Passive anomalies are insufficient; reproducible challenge-linked information dependence is the target.

### Phase 3 - Independent Replication

Any serious candidate must be reproduced by independent laboratories using fresh challenges and independently implemented hardware/software.

---

## 8. Scope-Control Rules

Before adding any new section, figure, hardware feature, protocol field, or analysis method, answer the following questions:

1. **Which product does it belong to?** Core paper, design package, or results paper?
2. **Which defined gap does it close?** Publication, reproducibility, control, safety, review, or experimental validity?
3. **Is it required before the next project gate?**
4. **Could it be deferred without weakening the current deliverable?**
5. **Does it introduce a new unvalidated assumption or new testing burden?**

If there is no clear answer to #2 or #3, the item is deferred.

### Formal rule

> **No feature is added to Phase-1 Design Package 1.0 unless it is necessary to reproduce, validate, isolate, analyze, or safely operate the defined Phase-1 experiment.**

---

## 9. Change-Control Process

After Candidate 1.0, all substantive changes receive an identifier:

`SETI-CR-YYYY-NNN`

Each change request records:
- requested change;
- reason;
- artifact affected;
- risk if omitted;
- new assumptions introduced;
- verification required;
- disposition;
- approver/date.

Changes after Design Package 1.0 should produce a controlled minor or major release rather than silently modifying the baseline.

---

## 10. Immediate Next Actions

The next work should be limited to the following sequence:

1. Complete the remaining fabrication/build closure items for the Phase-1 package.
2. Produce **Phase-1 Technical Design Package Candidate 1.0**.
3. Use the completed **Concept Paper Candidate 1.0** as the publication-review baseline; do not expand it except to resolve scientific or reviewer gaps.
4. Build an external-review packet containing both candidate documents plus a one-page reviewer guide.
5. Send the packet to targeted reviewers and log feedback.
6. Resolve Critical and Major review findings.
7. Freeze Concept Paper 1.0 and Design Package 1.0.
8. Publish the concept/preprint and repository record.
9. Only then authorize significant Phase-1 hardware procurement and physical build.

---

## 11. Definition of Project Success

The project is successful even if no unexplained information channel is discovered. Success means the project produces:
- a clearly defined and falsifiable search concept;
- a reproducible experimental methodology;
- a high-quality null result or a reproducible anomaly;
- public data, protocols, and code sufficient for independent scrutiny;
- a clear scientific record separating observation from interpretation.

The project should never define success as obtaining a preferred outcome.

---

## 12. Final Stop Rule

The writing phase ends when the core paper and technical design package meet their definitions of done.

> **At that point, we stop expanding documents and start testing the experiment.**
