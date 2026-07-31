# Milestone 4 Chapter 6 audit

Status: reviewed draft ready for owner review - 2026-07-31

This audit covers the fourth controlled Milestone 4 batch against public issue [#6](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/6). The public comparison point is commit `3691770`, which records the Chapter 6 work package and a clean Markdown-linting baseline.

## Delivered scope

- Chapter 6 contains the seven approved first-pass entries, moving from system boundaries through component shapes, communication, partial failure, finite-work controls, replicated state and overload control.
- One order-system example connects remote payment, queued fulfilment, replicated reads and honest intermediate states without prescribing a service architecture.
- A compact shrinking-budget diagram makes deadlines, downstream timeouts and remaining response time visible as one finite allowance.
- The chapter links to prerequisites in Chapters 1–5 without duplicating their canonical explanations.
- Language concurrency remains in Chapter 2, database transactions in Chapter 5, infrastructure in Chapter 7, operational evidence in Chapter 8, security in Chapter 9 and organisational architecture governance in TLB.
- Current products are dated recognition examples rather than recommendations or substitutes for the durable mechanisms.
- The README, glossary, measurements, navigation and work-package record point to the Chapter 6 concepts.
- Source-linked research was committed and pushed to the private companion repository at commit `4d6fd9f` before public drafting.

## Scope and grounding decisions

The approved order forms one causal model: name boundaries; decide where components run and keep state; select communication semantics; expect partial failure; bound work and retries; state what replicated readers may observe; and prevent finite capacity from collapsing under accumulated work. The final entry deliberately groups several controls because their value comes from their interaction rather than from a pattern catalogue.

The chapter defines CAP only for behaviour during a network partition and rejects the “pick any two” slogan. It distinguishes that model from ACID valid-state consistency and from product-specific replica-read guarantees. It also treats a timeout as one caller's observation, cancellation as a co-operative signal and idempotency as a receiving-system guarantee over stated operation identity, parameters, concurrency and retention.

## Reading-load measurements

Measurements come from `python3 scripts/measure_docs.py`. It counts visible Markdown words while excluding link destinations. Reading-time estimates use 200 words per minute and round up. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists.

| Measure | Chapter 6 |
| --- | ---: |
| Principal entries | 7 |
| Complete page words | 3,962 |
| Estimated complete-page reading time | 20 minutes |
| Shortest entry prose | 361 words |
| Longest entry prose | 440 words |
| Entries outside the 250–500-word prose range | 0 |

The page remains below the eight-entry calibration maximum and comparable in reading load to the approved construction chapters. Its chapter map and independent entries support selective browsing.

## Lifecycle and review effort

- A bounded private research pass separated durable mechanisms from current product examples and traced high-risk claims to standards, original papers and first-party engineering accounts.
- A separate drafting pass produced the seven-entry chapter from the fixed research note and approved outline.
- The lead integration pass added navigation, glossary definitions, measurements and canonical links without exposing raw research.
- Independent specification and editorial-standards reviews were completed by reviewers other than the researcher and drafter.

## Review findings and corrections

The independent reviews produced five unique actionable groups. All five were corrected before publication, giving a pre-publication correction rate of 5/5.

| Finding | Resolution |
| --- | --- |
| The queue definition implied that every queue uses claim-and-acknowledge semantics. | Defined a queue by pending work and described claim, acknowledgement, removal and redelivery as variable broker semantics. |
| The idempotency example did not state how concurrent uses of an operation key are arbitrated. | Required matching operation parameters and one authoritative receiving-system record; stated that a key alone changes nothing. |
| The CAP sentence overgeneralised availability and left single-copy consistency unexplained. | Scoped availability to requests received by non-failing components and explained the competing promise as behaviour through one current copy. |
| Several acronyms were not grounded for a direct-entry reader. | Expanded artificial intelligence, Request for Comments, atomicity/consistency/isolation/durability and PACELC at first use. |
| Deadline propagation, jitter and load-balancer inputs were worded as automatic or guaranteed. | Recast them as design requirements or probabilistic controls and qualified the possible load-balancer inputs. |

The specification reviewer found no other missing or misplaced Chapter 6 requirement. Both reviewers confirmed that the entries remain at awareness depth, current examples are dated, agentic consequences are mechanism-specific, and no public/private-boundary violation or later-chapter scope leak was introduced.

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

Expected result: six chapter measurement lines followed by `Repeated long prose paragraphs: 0`.

```sh
npm_config_cache=/private/tmp/tfb-npm-cache npx --yes markdownlint-cli2@0.23.2 '**/*.md' '#tfb-private/**'
```

Expected result: `Summary: 0 issues in 0 files.`

```sh
uv run --with codespell==2.4.3 codespell --skip='.git,tfb-private' --ignore-words-list='crate,fo,nd,te,ba,uptodate,fulfilment,co-ordinate,skelton' .
```

Expected result: no spelling findings and exit status 0.

The 22 distinct external Markdown links in Chapter 6 were requested on 2026-07-31. Twenty returned HTTP status 200 after redirects. The ISO standard page and Harvard-hosted *A Note on Distributed Computing* returned HTTP status 403 to the automated client; the research pass confirmed that they are the intended sources, so this status is recorded as an inconclusive automation result rather than a dead link.

All deterministic verification commands above were executed successfully on 2026-07-31. The measurement run reported zero repeated long prose paragraphs.

## Gate

The Chapter 6 batch has passed both independent review axes and the deterministic verification suite. It is ready for owner review. Chapter 7 remains deferred until that pause has occurred.
