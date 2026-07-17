# Milestone 4 Chapter 3 audit

Status: approved - 2026-07-18

This audit covers the first controlled Milestone 4 batch against public issue [#3](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/3). The public comparison point is commit `3563aae`, the approved Milestone 3 publication.

## Delivered scope

- Chapter 3 contains seven first-pass entries covering intent, boundaries, interfaces, evidence, recorded change, integration feedback and evolutionary change.
- The chapter links back to the programming and computing foundations it relies on without duplicating their canonical explanations.
- Joel Spolsky's 2000 and 2001 essays appear as dated practitioner context. Their memorable claims are qualified rather than treated as universal rules.
- The README, glossary, measurements, navigation and work-package record point to the published Chapter 3 concepts.
- Source-linked research was committed and pushed to the private companion repository at commit `4c1721f` before public integration.

## Scope decision

The approved seven-entry shape was retained. In particular, refactoring, technical debt, legacy systems and evolutionary replacement remain one scale-of-change entry. Splitting them would take the complete first traversal from 94 to 95 entries and obscure the useful relationship between small structural improvements and staged system replacement. The entry distinguishes the mechanisms internally without changing the approved outline.

## Reading-load measurements

Measurements come from `python3 scripts/measure_docs.py`. It counts visible Markdown words while excluding link destinations. Reading-time estimates use 200 words per minute and round up. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists.

| Measure | Chapter 3 |
| --- | ---: |
| Principal entries | 7 |
| Complete page words | 3,994 |
| Estimated complete-page reading time | 20 minutes |
| Shortest entry prose | 367 words |
| Longest entry prose | 436 words |
| Entries outside the 250–500-word prose range | 0 |

The page stays below the eight-entry calibration maximum and is comparable in reading load to the approved first two chapters. Its linked chapter map and self-contained entries support selective browsing.

## Lifecycle and review effort

- A bounded private research pass separated durable claims from dated practitioner material and traced them to primary or first-party sources.
- A separate drafting pass produced the seven-entry chapter from that research and the approved outline.
- The lead integration pass checked dependencies, canonical links, glossary terms and reading load.
- Separate standards and specification reviews were completed by contributors other than the drafter.

## Review findings and corrections

The independent reviews produced four unique actionable groups. All four were corrected before publication, giving a pre-publication correction rate of 4/4.

| Finding | Resolution |
| --- | --- |
| The audit still described the reviews as assigned and left the publication gate unresolved. | Recorded both completed review outcomes, corrections and the ready-for-owner-review gate. |
| Several entries assumed incidental engineering jargon, including *blast radius*, *static analysis*, *mainline*, *pipeline*, *gate* and *flaky*. | Replaced incidental terms with plain descriptions or defined the useful term locally; simplified the glossary definition of continuous integration. |
| The chapter footer called the entries approved even though the prose still awaits owner review. | Distinguished the entries selected in the approved outline from the unapproved Chapter 3 draft. |
| External-link verification was performed but not recorded. | Recorded its date, scope, results and the two classes of justified exception below. |

No content-scope finding remained: both reviewers confirmed that the seven selected entries are present at awareness depth, Chapter 2 dependencies are linked without material duplication, and the dated practitioner material remains subordinate to the durable mechanisms. No public/private-boundary violation was found.

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

Expected result: three chapter measurement lines followed by `Repeated long prose paragraphs: 0`.

```sh
npm_config_cache=/private/tmp/tfb-npm-cache npx --yes markdownlint-cli2@0.23.1 '**/*.md' '#tfb-private/**'
```

Expected result: `Summary: 0 issues in 0 files.`

```sh
UV_CACHE_DIR=/private/tmp/tfb-uv-cache UV_TOOL_DIR=/private/tmp/tfb-uv-tools uvx codespell@2.4.3 --skip='.git,tfb-private' --ignore-words-list='crate,fo,nd,te,ba,uptodate' .
```

Expected result: no spelling findings and exit status 0.

The 24 distinct external links in Chapter 3 were requested on 2026-07-18. Twenty-one returned a successful 2xx response after redirects. The two Association for Computing Machinery DOI links redirected to the correct publisher records, whose pages returned `403` to the automated request. The official GNU Make page timed out on repeated HTTP and HTTPS requests. The DOI identifiers and official project URL were retained as stable canonical targets; these three destinations should receive a browser check at the next maintenance pass. This point-in-time availability check is not validation of every factual claim or a guarantee of future availability.

## Gate

The Chapter 3 batch passed independent review and the verification suite. The owner approved it on 2026-07-18 and authorised the Chapter 4 controlled batch.
