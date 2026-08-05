# Milestone 4 Chapter 7 audit

Review snapshot: ready for owner review on 2026-08-03. Current workflow state lives in public issue [#8](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/8).

This audit covers the controlled Chapter 7 increment. The public comparison point is commit `fe695e8`; the private cited research was committed before public drafting at `5f62099`.

## Delivered scope

- Chapter 7 contains exactly the seven approved first-pass entries: environments; configuration, workload identity and secret delivery; compute forms; cloud and managed responsibility; artefacts and infrastructure as code; compatible delivery and recovery; and capacity, cost and coupling.
- The chapter keeps `source → build artefact → release → deployment → runtime → recovery` visible as an evidence chain without presenting it as a universal tool pipeline.
- A provider-neutral functional map and compact scope comparison orient readers to broad clouds, application or edge platforms and managed application backends without implying product equivalence or endorsement.
- Managed services move operational work and change the responsibility boundary; they do not remove the customer's responsibility for configuration, access, data, evidence or outcomes.
- Configuration, workload identity, credentials, authentication, policy authorisation and secrets are distinguished at awareness depth. No secret values, account identifiers or project-specific security details appear in the public chapter.
- Infrastructure as code covers desired state, planning, state, drift, idempotent convergence, sensitive state, destructive change and the limits of configuration rollback.
- Rollback is distinguished from recovery, and portability is treated as a layered property rather than a claim based on one format or container image.
- Chapter 6 remains the home for architecture and distributed failure. Chapters 8, 9 and 11 retain operations and recovery evidence, detailed security and identity mechanics, and contracts and assurance respectively.
- The README, glossary, earlier chapter boundaries and documentation measurement harness now link to or include Chapter 7.

## Grounding and currentness

The private brief separates durable mechanisms from provider and product examples. It uses standards, specifications, original practice sources and first-party documentation, including NIST, the Open Container Initiative, SPIFFE, SLSA, Terraform, Google Site Reliability Engineering and current provider material.

Current provider, platform, foundation and product recognition was reviewed on 2026-08-03. Exact prices, quotas, regions, service limits and contractual terms are deliberately omitted because they must be checked at the decision point.

## Reading-load measurements

Measurements come from `python3 scripts/measure_docs.py`. It counts visible Markdown words while excluding link destinations. Entry prose counts exclude the related-concepts, deeper-concepts and further-reading lists.

| Measure | Chapter 7 |
| --- | ---: |
| Principal entries | 7 |
| Complete page words | 3,766 |
| Estimated complete-page reading time | 19 minutes |
| Shortest entry prose | 286 words |
| Longest entry prose | 456 words |
| Entries outside the 250–500-word prose range | 0 |

## Independent review

A researcher produced the private cited brief. A separate drafter then produced the public chapter. Independent specification, editorial-standards and security-boundary reviewers evaluated the integrated working tree.

The reviews produced six unique actionable groups. All six were corrected and the same reviewers confirmed that no material finding remained.

| Finding | Resolution |
| --- | --- |
| Secret delivery was named without showing its basic mechanism, and identity, credentials and authorisation were blurred. | Distinguished identity, authentication evidence, policy and secret sensitivity; added runtime-scoped injection or controlled retrieval as the compact delivery example. |
| A content digest could be mistaken for proof of trusted origin. | Stated that a digest proves byte identity, while build authority, registry access and provenance supply different evidence. |
| The provider-neutral map did not translate current provider types. | Added a compact, dated comparison of broad clouds, application or edge platforms and managed backends without asserting equivalence. |
| Infrastructure as code omitted idempotence and rollback limits. | Added convergence behaviour and explained why restoring configuration cannot restore deleted data or external state. |
| Software-as-a-service building blocks and the CNCF lifecycle were only named. | Added concise recognition treatment and stated what a lifecycle stage does not prove. |
| Two acronyms were not expanded for a direct-entry reader. | Expanded software development kit and Open Container Initiative in their entries. |

The specification reviewer confirmed that the chapter covers all seven retained entries, preserves the later-chapter boundaries and makes the required evidence, responsibility, rollback and portability distinctions. The standards reviewer found no residual project-family or editorial violation. The security reviewer found no remaining overpromise, secret exposure or Chapter 9 scope leak.

## Verification

Run from the public repository root:

```sh
python3 scripts/check_docs.py
```

Expected result: `Documentation checks passed. Checked 30 Markdown files.`

```sh
python3 scripts/measure_docs.py
```

Expected result: seven chapter measurement lines followed by `Repeated long prose paragraphs: 0`.

```sh
git diff --check
```

Expected result: no output and exit status 0.

```sh
npm_config_cache=/private/tmp/tfb-npm-cache npx --yes markdownlint-cli2@0.23.2 '**/*.md'
```

Expected result: `Summary: 0 issues in 0 files.`

```sh
uv run --with codespell==2.4.3 codespell --skip='.git' --ignore-words-list='crate,fo,nd,te,ba,uptodate,fulfilment,co-ordinate,skelton' .
```

Expected result: no spelling findings and exit status 0.

The 22 distinct external Markdown links in Chapter 7 were requested after correction on 2026-08-03. All 22 returned HTTP status 200 after redirects. The current provider categories were also checked against first-party product documentation.

All deterministic checks above passed before the public commit. The measurement run reported zero repeated long prose paragraphs.

## Gate

The Chapter 7 increment has passed independent specification, standards and security review. It is ready for owner review. Chapter 8 remains deferred until the owner approves this gate.
