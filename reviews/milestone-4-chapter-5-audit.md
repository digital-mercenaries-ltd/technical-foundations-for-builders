# Milestone 4 Chapter 5 audit

Status: reviewed draft ready for owner review - 2026-07-18

This audit covers the third controlled Milestone 4 batch against public issue [#5](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/5). The public comparison point is commit `ab48a1e`, which records Chapter 4 approval, the Chapter 5 work package and the explicit placement of behaviour-driven development in Chapter 10.

## Delivered scope

- Chapter 5 contains the seven approved first-pass entries, moving from data meaning and structure through relational models, integrity, retrieval, concurrency, evolution and storage choices.
- A small order-system example is reused across entries so that each mechanism adds to one mental model rather than introducing a new domain.
- The chapter links to prerequisites in Chapters 1–4 without duplicating their canonical explanations.
- Replication and distributed coordination remain in Chapter 6, managed-database responsibility in Chapter 7, backups and recovery in Chapter 8, database security in Chapter 9, and legal obligations in Chapter 11.
- Current database products are dated recognition material rather than recommendations or substitutes for the durable decision model.
- The README, glossary, measurements, navigation and work-package record point to the Chapter 5 concepts.
- Source-linked research was committed and pushed to the private companion repository at commit `915bdec` before public drafting.

## Scope and grounding decision

An independent structure pass confirmed that the seven-entry order forms a coherent breadth-first model and does not need a split. The final entry remains one culminating decision model based on data shape, access patterns, guarantees and lifecycle obligations rather than a catalogue of database categories or vendors. It states explicitly that lifecycle applies to relational and non-relational stores.

The word *consistency* receives a deliberate boundary. Transaction consistency means preserving declared valid-state rules; isolation concerns overlapping database work; read or replica consistency concerns which committed version a reader may observe. Chapter 5 distinguishes these meanings but leaves replication mechanisms and distributed trade-offs to Chapter 6.

## Reading-load measurements

Measurements come from `python3 scripts/measure_docs.py`. It counts visible Markdown words while excluding link destinations. Reading-time estimates use 200 words per minute and round up. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists.

| Measure | Chapter 5 |
| --- | ---: |
| Principal entries | 7 |
| Complete page words | 4,277 |
| Estimated complete-page reading time | 22 minutes |
| Shortest entry prose | 407 words |
| Longest entry prose | 489 words |
| Entries outside the 250–500-word prose range | 0 |

The page remains below the eight-entry calibration maximum and is comparable in reading load to Chapters 2–4. Its chapter map and independent entries support selective browsing.

## Lifecycle and review effort

- A bounded private research pass traced durable claims to original research, standards and official database documentation.
- An independent structure pass checked order, bundling, jargon, duplication and the Chapter 6–8 boundaries.
- A separate drafting pass produced the seven-entry chapter from the fixed research note and approved outline.
- The lead integration pass checked factual boundaries, canonical links, terminology, glossary coverage, reading load and public/private separation.
- Separate standards and specification reviews were completed by reviewers other than the researcher and drafter.

## Review findings and corrections

The independent reviews produced four unique actionable groups. All four were corrected before publication, giving a pre-publication correction rate of 4/4.

| Finding | Resolution |
| --- | --- |
| The foreign-key definition excluded self-references by saying the referenced key must be in another table. | Clarified that the referenced row may be in the same or another table. |
| The acronym ACID appeared before its expansion. | Introduced atomicity, consistency, isolation and durability before using ACID. |
| JSON recurred across published chapters without a glossary entry. | Added an alphabetised JavaScript Object Notation entry linked to its canonical introduction. |
| The final entry compressed strongly consistent reads, replicas and soft deletion into unexplained jargon. | Replaced or grounded each term in plain language and tightened the entry back below the prose budget. |

The specification reviewer found no other missing or misplaced Chapter 5 requirement. Both reviewers confirmed that the seven entries remain at awareness depth, prerequisite links and later-chapter boundaries are clear, related and deeper concepts are distinguished, and no public/private-boundary violation or duplicated canonical explanation was introduced.

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

```sh
python3 scripts/measure_docs.py
```

Expected result: five chapter measurement lines followed by `Repeated long prose paragraphs: 0`.

```sh
npm_config_cache=/private/tmp/tfb-npm-cache npx --yes markdownlint-cli2@0.23.1 '**/*.md' '#tfb-private/**'
```

Expected result: `Summary: 0 issues in 0 files.`

```sh
UV_CACHE_DIR=/private/tmp/tfb-uv-cache UV_TOOL_DIR=/private/tmp/tfb-uv-tools uvx codespell@2.4.3 --skip='.git,tfb-private' --ignore-words-list='crate,fo,nd,te,ba,uptodate' .
```

Expected result: no spelling findings and exit status 0.

The 22 distinct external Markdown links in Chapter 5 were requested on 2026-07-18. All returned HTTP status 200 after redirects. This point-in-time availability check is not validation of every factual claim or a guarantee of future availability.

All verification commands above were executed successfully on 2026-07-18. The measurement run reported zero repeated long prose paragraphs, and the documentation checker covered 22 Markdown files.

## Gate

The Chapter 5 batch has passed both independent review axes, external-link checking and the verification suite. It is ready for owner review. Chapter 6 remains deferred until that pause has occurred.
