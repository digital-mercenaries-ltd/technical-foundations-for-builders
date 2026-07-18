# Milestone 4 Chapter 4 audit

Status: reviewed draft ready for owner review - 2026-07-18

This audit covers the second controlled Milestone 4 batch against public issue [#4](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/4). The public comparison point is commit `08de92d`, which records Chapter 3 approval and the Chapter 4 work package.

## Delivered scope

- Chapter 4 contains seven first-pass entries following a request from Internet addressing through names, protected HTTP, browser interpretation, network API contracts, browser state and compatibility.
- A compact request-journey diagram shows the responsibility sequence and explicitly warns that caches, reused connections, intermediaries and HTTP/3 alter the literal path.
- The chapter links to its computing, programming and software-engineering prerequisites without duplicating their canonical explanations.
- Current browser-engine, organisation, OpenAPI and Web Platform Baseline material was reviewed on 2026-07-18 and remains subordinate to durable mechanisms.
- The README, glossary, measurements, navigation and work-package record point to the Chapter 4 concepts.
- Source-linked research was committed and pushed to the private companion repository at commit `dba933a` before public drafting.

## Scope and grounding decision

An independent structure pass confirmed that the approved seven-entry order forms a coherent request journey and does not need another traversal split. The three broadest clusters each retain one centre: how HTTP becomes protected, how the browser's content layers cooperate, and how browser/server state meets the origin boundary. Distributed coordination remains in Chapter 6, deployment in Chapter 7, attacks in Chapter 9 and usability and accessibility outcomes in Chapter 10.

The chapter adds one small diagram because the sequence crosses more boundaries than prose can show as compactly. Its accompanying text supplies the qualification needed by readers who do not parse the diagram visually.

## Reading-load measurements

Measurements come from `python3 scripts/measure_docs.py`. It counts visible Markdown words while excluding link destinations. Reading-time estimates use 200 words per minute and round up. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists.

| Measure | Chapter 4 |
| --- | ---: |
| Principal entries | 7 |
| Complete page words | 4,072 |
| Estimated complete-page reading time | 21 minutes |
| Shortest entry prose | 375 words |
| Longest entry prose | 415 words |
| Entries outside the 250–500-word prose range | 0 |

The page remains below the eight-entry calibration maximum and is comparable in reading load to the approved Chapters 2 and 3. Its linked chapter map and independently grounded entries support selective browsing.

## Lifecycle and review effort

- A bounded private research pass traced durable claims to RFCs, web standards and official documentation and separated dated landscape claims.
- An independent structure pass checked grounding order, bundling, jargon risk, duplication and chapter boundaries.
- A separate drafting pass produced the seven-entry chapter from the fixed research note and approved outline.
- The lead integration pass checked canonical links, terminology, glossary coverage, reading load and public/private separation.
- Separate standards and specification reviews were completed by contributors other than the researcher and drafter.

## Review findings and corrections

The independent reviews produced five unique actionable groups. All five were corrected before publication, giving a pre-publication correction rate of 5/5.

| Finding | Resolution |
| --- | --- |
| The audit had not yet recorded completed review and verification evidence. | Recorded both review outcomes, corrections, observed checks and the ready-for-owner-review gate. |
| Browser URL parsing was described as following both WHATWG and the older general URI syntax. | Distinguished WHATWG browser parsing from RFC 3986's broader URI terminology. |
| The CORS pitfall made authentication and authorisation sound mandatory for public resources. | Qualified the requirement to resources where access is restricted. |
| Current browser-to-engine mappings lacked complete first-party support and initially hid Apple-platform exceptions. | Added dated links to Chrome, Mozilla and Apple documentation at the claim and qualified the mapping by platform. |
| The Web Platform Baseline example risked duplicating its planned further-territory entry. | Compressed it to dated recognition material and left category detail for the optional canonical entry. |

The specification review found no missing or misplaced Chapter 4 concept. Both reviewers confirmed that the seven entries remain at awareness depth, prerequisite links and later-chapter boundaries are clear, the diagram has an accompanying textual explanation, related and deeper concepts are distinguished, and no public/private-boundary violation or duplicated canonical explanation was introduced.

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

Expected result: four chapter measurement lines followed by `Repeated long prose paragraphs: 0`.

```sh
npm_config_cache=/private/tmp/tfb-npm-cache npx --yes markdownlint-cli2@0.23.1 '**/*.md' '#tfb-private/**'
```

Expected result: `Summary: 0 issues in 0 files.`

```sh
UV_CACHE_DIR=/private/tmp/tfb-uv-cache UV_TOOL_DIR=/private/tmp/tfb-uv-tools uvx codespell@2.4.3 --skip='.git,tfb-private' --ignore-words-list='crate,fo,nd,te,ba,uptodate' .
```

Expected result: no spelling findings and exit status 0.

The 29 distinct external Markdown links in Chapter 4 were requested on 2026-07-18. All returned a successful 2xx response after redirects. Example URLs shown as code were excluded because they are teaching examples rather than link targets. This point-in-time availability check is not validation of every factual claim or a guarantee of future availability.

All verification commands above were executed successfully on 2026-07-18. The measurement run reported zero repeated long prose paragraphs, and the documentation checker covered 20 Markdown files.

## Gate

The Chapter 4 batch passed both independent review axes, external-link checking and the verification suite. The owner approved it on 2026-07-18. Chapter 5 may now begin as the next controlled batch.
