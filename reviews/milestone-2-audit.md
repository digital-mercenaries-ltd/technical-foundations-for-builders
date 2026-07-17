# Milestone 2 audit

Date: 2026-07-17

- Baseline: `2a07e14`

## Scope reviewed

The review covered the reader-facing map, tiered content inventory, disclosure model, chapter boundaries, editorial rules, issue-ready work packages, research-note use and documentation checks. It did not review prose for Chapters 2–13 because that prose has not been drafted.

## Editorial decisions

- TFB may deliberately mix mechanisms, products, vendors, organisations, standards, assurance reports, laws and cultural terms. The treatment varies according to the awareness the target reader needs; the subjects do not receive equal-sized entries by default.
- The README remains a calm map. `OUTLINE.md` holds the complete inventory. First-pass chapter files will contain the main traversal, and `further/` will hold optional awareness-level entries.
- Current products and organisations are legitimate content in a living guide. Time-sensitive landscape material carries an ISO-8601 review date and must be checked before publication.
- Humorous terms such as *PEBKAC/PEBCAK*, *heisenbug* and *yak shaving* may retain their personality. Each use must explain the system behaviour or working habit behind the term and must not substitute blame for diagnosis.
- Joel Spolsky's writing is used as dated practitioner context. The law of leaky abstractions has a canonical place; the Joel Test, evolutionary rewrites, build feedback and related stories support concepts rather than becoming timeless rules.
- The approved Chapter 1 prose remains unchanged. Its three entries are now described as a calibration set: bits and bytes remains on the first pass, while binary and hexadecimal are assigned to further territory for the eventual file reorganisation.

## Standards review

The standards review checked the repository's own editorial contract, canonical ownership, source policy, glossary rules and automated checks.

| Finding | Resolution |
| --- | --- |
| Several concepts had canonical-looking homes in more than one chapter or tier. | Removed duplicate homes for architecture decision records, reproducible builds, responsive design and several named laws. Recognition sections now cross-link named technical laws to their canonical chapters. |
| The glossary linked undrafted terms to planned outline headings. | Removed those seed entries. The glossary now links only to published explanations or reader-facing navigation. |
| The private modern-web research note made current recommendations without a source and verification marker. | Marked it as a preliminary research note, dated the review and added an official-source index. Its code examples and prescriptive defaults still require claim-level checking before publication. |
| Acronyms in the README appeared before a plain expansion. | Expanded OWASP, ISO/IEC and SOC at their first relevant reader-facing uses. |
| The automated check enforced per-chapter counts but not whole-guide first-pass size or landscape review markers. | Added a 95-entry breadth guardrail and a required dated landscape marker for every outline chapter. |

A closure check then found four smaller inconsistencies. It separated in-process library interfaces in Chapter 3 from network service contracts in Chapter 4, removed the second treatment of reversible decisions, expanded HTML, DRY, KISS and YAGNI, and made WP-01 the immediate next action so the plan matches the work-package dependencies.

## Repository boundary

The public repository now contains the guide, contributor instructions, work plan, checks and review records. Original source files and raw research notes are held in the separate private companion repository. The reviewed changes to two research notes were preserved there before their public working copies were removed.

The public remote's existing history predates this boundary and still contains earlier copies of some source and research files. Removing those historical objects would require a separate, explicitly approved history rewrite and coordinated force-push; Milestone 2 does not perform that destructive operation.

The final workflow check also replaced obsolete references to a pending `dml` repository with the existing `digital-mercenaries-ltd/technical-foundations-for-builders` repository. Milestone 2 approval, not repository availability, is the gate for publishing the work packages as issues.

## Specification review

The specification review checked the result against the requested audience, progressive disclosure, contemporary landscape coverage, source-note use and the Milestone 2 deliverables.

| Finding | Resolution |
| --- | --- |
| Thirteen chapters with eight first-pass entries each created an overly uniform 104-entry traversal. | Reduced the traversal to 91 entries: six in Chapter 1, seven in Chapters 2–12 and eight in Chapter 13. Several compound entries were tightened and optional material moved to further territory. |
| Landscape sections lacked a visible maintenance date. | Added a `2026-07-17` selection-review marker to every chapter and a whole-guide living-landscape maintenance rule. |
| The quality rubric described full concepts but not shorter content forms. | Added distinct readiness criteria for current landscape items, related observations, hacker folklore and historical checklists or cases. |
| Some work packages left later scope choices to the drafting agent. | Split Chapter 1 further territory into three bounded packages and gave every later further-territory chapter an explicit package tied to the canonical outline list. |

## Verification

- `python3 scripts/check_docs.py` passes after the review fixes. It checks Markdown links and anchors, duplicate sibling headings, chapter numbering, disclosure sections, first-pass chapter counts, the whole-guide breadth guardrail and dated landscape markers.
- `markdownlint-cli2` 0.23.1 reports 0 issues across the 10 public Markdown files in scope.
- `cspell` with the `en-GB` locale reports only reviewed project names, acronyms, technical terms and code identifiers; one apparent prose error was corrected.
- `OUTLINE.md` contains 91 first-pass entries: 6 in Chapter 1, 7 in Chapters 2–12 and 8 in Chapter 13.
- The private research directory is approximately 236 KB of text material; the source PDF is approximately 799 KB. No bulk site mirrors or large generated assets were added.
- The temporary 63 MB package cache used for Markdown and spelling checks was deleted after verification.
- The working tree was checked for whitespace errors before commit.

## Human approval still required

- Confirm the 91-entry first traversal is selective enough.
- Confirm the assignment of binary and hexadecimal to further territory while retaining their approved prose.
- Revise any first-pass selection or chapter boundary that feels wrong for the target reader.
- Confirm the maintenance burden for dated products, organisations, schemes and standards is acceptable.
- Confirm the Milestone 2 editorial system before Chapter 2 or later chapter prose is drafted.
