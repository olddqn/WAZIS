# WAZIS documentation

The canonical description of WAZIS is the [README](../README.md) at the repository root.
Everything in this folder is supporting material. Where a document here disagrees with the
root README or with the code in [`app/`](../app/), the README and the code are correct.

Most of these documents were written in June 2026, in Japanese with English headings. They
are kept as written.

## Start here

- [contract/need-document-v1.md](contract/need-document-v1.md) — the one shape
  WAZIS promises to another system. Current, and matches the code.

- [glossary.md](glossary.md) — terms. Written for the earlier model; many still apply.
- [design/WAZIS_V01_IMPLEMENTATION_PLAN.md](design/WAZIS_V01_IMPLEMENTATION_PLAN.md) — the
  plan the application was built from.
- [future-verification-layer.md](future-verification-layer.md) — a concept kept for later.
  Not implemented, and not the definition of WAZIS.

## design/ — how the application was designed

Read in this order; each step narrows the one before it.

1. [WAZIS_IMPLEMENTATION_FLOOR_REVIEW.md](design/WAZIS_IMPLEMENTATION_FLOOR_REVIEW.md) — the least a web application must do to count as WAZIS.
2. [WAZIS_ISSUE_MODEL_REVIEW.md](design/WAZIS_ISSUE_MODEL_REVIEW.md) — one object, the Entry, in a tree.
3. [WAZIS_MVP_SCREEN_REVIEW.md](design/WAZIS_MVP_SCREEN_REVIEW.md) — three screens and three actions.
4. [WAZIS_MVP_FINAL_ARCHITECTURE_REVIEW.md](design/WAZIS_MVP_FINAL_ARCHITECTURE_REVIEW.md) — consistency check before building.
5. [WAZIS_V01_IMPLEMENTATION_PLAN.md](design/WAZIS_V01_IMPLEMENTATION_PLAN.md) — stack, schema, routes and launch gate.

## reviews/ — the reasoning behind the design

Reviews of the earlier specification and repository:

- [WAZIS_REPOSITORY_REVIEW.md](reviews/WAZIS_REPOSITORY_REVIEW.md)
- [WAZIS_EXPERIMENT_DRIVEN_REVIEW.md](reviews/WAZIS_EXPERIMENT_DRIVEN_REVIEW.md)
- [WAZIS_KERNEL_REVIEW.md](reviews/WAZIS_KERNEL_REVIEW.md)
- [WAZIS_PLATFORM_REVIEW.md](reviews/WAZIS_PLATFORM_REVIEW.md)
- [WAZIS_LAUNCH_REVIEW.md](reviews/WAZIS_LAUNCH_REVIEW.md)

Structure of the idea, and what can be removed from it:

- [WAZIS_DANGO_BOUNDARY_REVIEW.md](reviews/WAZIS_DANGO_BOUNDARY_REVIEW.md)
- [META_LOOP_REVIEW.md](reviews/META_LOOP_REVIEW.md)
- [TRANSFORMATION_REVIEW.md](reviews/TRANSFORMATION_REVIEW.md)
- [STRUCTURAL_CONSOLIDATION_REVIEW.md](reviews/STRUCTURAL_CONSOLIDATION_REVIEW.md)
- [OBJECT_REDUCTION_REVIEW.md](reviews/OBJECT_REDUCTION_REVIEW.md)
- [REALITY_FEEDBACK_INTERPRETATION_REVIEW.md](reviews/REALITY_FEEDBACK_INTERPRETATION_REVIEW.md)

From a Need to something that can be acted on, and Needs that cannot be:

- [FIRST_CLAIM_REVIEW.md](reviews/FIRST_CLAIM_REVIEW.md)
- [GAP_TO_CLAIM_REVIEW.md](reviews/GAP_TO_CLAIM_REVIEW.md)
- [CLAIMABILITY_REVIEW.md](reviews/CLAIMABILITY_REVIEW.md)
- [GAPABILITY_REVIEW.md](reviews/GAPABILITY_REVIEW.md)
- [NON_GAPABLE_NEED_REVIEW.md](reviews/NON_GAPABLE_NEED_REVIEW.md)
- [NEED_MATURATION_REVIEW.md](reviews/NEED_MATURATION_REVIEW.md)
- [SELF_TRANSLATION_REVIEW.md](reviews/SELF_TRANSLATION_REVIEW.md)
- [OPENNESS_RIGHT_REVIEW.md](reviews/OPENNESS_RIGHT_REVIEW.md)

## first-loop/ — looking for a first real Need

Working notes on which real-world need could be carried through one full loop first. They
name existing public organisations as candidates. Nothing in them is an agreement with, or
an endorsement by, any organisation named.

- [QUESTION_001_SELECTION_REVIEW.md](first-loop/QUESTION_001_SELECTION_REVIEW.md)
- [QUESTION_001_FINAL_REVIEW.md](first-loop/QUESTION_001_FINAL_REVIEW.md)
- [INNER_EXPERIMENT_REVIEW.md](first-loop/INNER_EXPERIMENT_REVIEW.md)
- [FIRST_REAL_NEED_DISCOVERY.md](first-loop/FIRST_REAL_NEED_DISCOVERY.md)
- [LOOP_001B_DISCOVERY.md](first-loop/LOOP_001B_DISCOVERY.md)
- [FIRST_ORGANIZATION_DISCOVERY.md](first-loop/FIRST_ORGANIZATION_DISCOVERY.md)
- [MUSUBIE_NEED_DISCOVERY.md](first-loop/MUSUBIE_NEED_DISCOVERY.md)
- [MUSUBIE_NEED_FIRST_REVIEW.md](first-loop/MUSUBIE_NEED_FIRST_REVIEW.md)

## history/ — the earlier model

These describe WAZIS as it was first specified: Question → Discussion → Refinement →
Implementation Candidate. The application does not implement this model.

- [README-phase-m0.md](history/README-phase-m0.md) — the first README.
- [WAZIS_SPEC.md](history/WAZIS_SPEC.md) — the first specification.
- [WAZIS_MVP_PLAN.md](history/WAZIS_MVP_PLAN.md) — the first build plan.
