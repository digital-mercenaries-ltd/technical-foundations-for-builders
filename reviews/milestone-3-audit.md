# Milestone 3 audit

Status: draft ready for owner review - 2026-07-17

This audit covers the Chapter 1 and Chapter 2 first-pass batch against public issues [#1](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/1) and [#2](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/2). The public comparison point is commit `aae9cb0`, the approved Milestone 2 publication.

## Delivered scope

- Chapter 1 now contains eight first-pass entries.
- The approved binary and hexadecimal/octal entries have one canonical home in Chapter 1 [further territory](../further/01-computing-foundations.md); their prose is unchanged apart from necessary relative-link and page-navigation changes.
- Chapter 2 now contains eight first-pass entries, including separate treatments of error handling and causal diagnosis.
- The README, outline, glossary, work packages and navigation point to the published canonical entries.
- Research notes were written, committed and pushed to the private companion repository before the public drafts were integrated.

## Scope adjustment

Drafting exposed three labels that contained distinct mechanisms and sets of pitfalls:

1. integer ranges and overflow versus floating-point approximation;
2. civil time and clocks versus latency and throughput; and
3. error handling and cleanup versus debugging and diagnosis.

Splitting them raised the complete first traversal from the 91 entries approved at Milestone 2 to 94 entries. This remains below the existing planning guardrail of 95. The split reduces conceptual bundling without adding new subject matter.

## Reading-load measurements

Word counts use the current Markdown text. Reading-time estimates use 200 words per minute and round up. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists so they can be compared with the style guide's 250–500-word calibration range.

| Measure | Chapter 1 | Chapter 2 |
| --- | ---: | ---: |
| Principal entries | 8 | 8 |
| Complete page words | 3,798 | 4,428 |
| Estimated complete-page reading time | 19 minutes | 23 minutes |
| Shortest entry prose | 276 words | 345 words |
| Longest entry prose | 437 words | 477 words |
| Entries outside the 250–500-word prose range | 0 | 0 |

The 42-minute combined first pass is substantial but remains selectively browsable: each page has a linked chapter map, each entry is independently grounded, and optional number notation has moved out of the traversal. Eight entries per chapter is retained as a calibration maximum, not a quota for later chapters.

## Lifecycle and review effort

- Two bounded research passes produced 8,753 words of private, source-linked notes covering durable mechanisms and dated landscape checks.
- One independent structure pass mapped prerequisites and identified the three overloaded labels.
- Two separate drafting passes produced non-overlapping chapter files.
- Two independent review passes checked documented standards and the issue specifications.
- The lead integration pass reconciled navigation, glossary terms, traversal counts and review corrections.

## Review findings and corrections

The standards and specification reviews produced six unique actionable groups after overlapping reports were combined. All six were corrected before this handoff, giving a pre-handoff correction rate of 6/6.

| Finding | Resolution |
| --- | --- |
| Traversal counts still described the approved 91-entry outline after three splits. | Recorded the 94-entry current count and the split rationale while preserving the historical Milestone 2 decision. |
| Glossary links still treated the new Unicode entry as planned and pointed to older canonical homes. | Updated the canonical links and added selected Chapter 1 and Chapter 2 terms. |
| Recurring acronyms and several Chapter 2 terms were not grounded. | Expanded terms at first use, replaced avoidable jargon with plain language and added recurring acronyms to the glossary. |
| Chapter 2's map did not support selective browsing. | Added a linked eight-entry chapter map. |
| Chapter 2 made too few useful links back to Chapter 1. | Linked operating systems, integer limits, floating point and text encodings at their first useful mentions. |
| The required Milestone 3 measurements were absent. | Added this audit with length, reading time, conceptual bundling, review effort, duplication and correction measurements. |

The reviewers found no material scope creep. Manual integration review found no duplicated canonical explanation: Chapter 2 briefly grounds prerequisites for direct visitors and links to the fuller Chapter 1 entries. The binary and hexadecimal/octal explanations have one public canonical copy.

## Verification

Run from the public repository root:

```sh
python3 scripts/check_docs.py
```

Expected result: `Documentation checks passed.`

```sh
git diff --check
```

Expected result: no output and exit status 0.

The 63 distinct external links in the two chapter pages and Chapter 1 further-territory page were also requested on 2026-07-17. All returned a successful response. This is a point-in-time availability check, not proof that every external page will remain unchanged.

## Gate

Milestone 3 is ready for owner review. Issues #1 and #2 should remain open, and Milestone 4 should not begin, until the owner accepts the chapter quality, reading load and three scope splits.
