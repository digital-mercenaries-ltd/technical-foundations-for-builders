# Technical Foundations for Builders issue-ready work packages

Status: Milestone 3 approved; Milestone 4 in progress - 2026-07-18

These are bounded drafting and integration batches for publication to the `digital-mercenaries-ltd/technical-foundations-for-builders` GitHub issue tracker after Milestone 2 approval. They are not a required reading order.

Every package must follow [PLAN.md](PLAN.md), [STYLE_GUIDE.md](STYLE_GUIDE.md) and the tier assignments in [OUTLINE.md](OUTLINE.md). Research, drafting and critique should be performed by different agents or contributors where practical.

## Shared definition of done

- Private research notes identify durable claims, current landscape claims and suitable sources; public deliverables contain only edited conclusions and appropriate source links.
- Each topic retains its assigned disclosure tier and canonical home.
- First-pass prose establishes mechanics, relevance and pitfalls without becoming a tutorial.
- Current products, organisations, standards and schemes include an ISO 8601 review date where staleness matters.
- Jargon and historical material explain the mechanism and context behind the memorable name.
- Internal links, anchors and document structure pass `python3 scripts/check_docs.py`.
- A separate reviewer checks accuracy, jargon grounding, redundancy and fit with the target reader.

## Editorial-system package

### WP-00: Integrate Milestone 2 review

**Status:** Complete on 2026-07-17.

**Depends on:** user review of the current milestone.

**Deliverables:** resolve feedback on tiering, chapter boundaries, current landscape coverage and humour; update the outline and style guide; record decisions in a Milestone 2 audit.

## Foundation packages

### WP-01: Complete the Chapter 1 first pass

**Issue:** [#1](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/1)

**Status:** Complete; approved on 2026-07-17.

**Depends on:** WP-00.

**Scope:** preserve the three calibrated explanations; relocate binary and hexadecimal/octal unchanged to the Chapter 1 further-territory page; draft eight first-pass entries covering representation, integer limits, floating point, text, machine resources, running programs, time and performance; repair incoming links; and integrate the page as one mental model.

### WP-02A: Expand Chapter 1 numeric further territory

**Depends on:** WP-01.

**Scope:** after WP-01 has established the page and relocated the approved entries, add Boolean and bitwise operations, decimal money and units, randomness and entropy. Do not redraft binary or hexadecimal notation.

### WP-02B: Draft Chapter 1 machine further territory

**Depends on:** WP-01.

**Scope:** instructions, registers and system calls; files and platform differences; input and output; processor and memory caches.

### WP-02C: Draft Chapter 1 format and performance further territory

**Depends on:** WP-01.

**Scope:** compression; serialisation; endianness; error detection; Amdahl's Law.

### WP-03: Draft the Chapter 2 first pass

**Issue:** [#2](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/2)

**Status:** Complete; approved on 2026-07-17.

**Depends on:** WP-00 and the terminology established by WP-01.

**Scope:** draft eight first-pass entries covering languages and runtimes, values and types, state, control flow and functions, data structures, modules and dependencies, error handling, and diagnosis. Include a compact hacker-folklore debugging aside.

### WP-04: Draft Chapter 2 further territory

**Depends on:** WP-03.

**Scope:** compilation models, recursion, object models, type-system variants, concurrency, asynchronous work, resource lifetime and deeper debugging tools.

## Construction packages

### WP-05: Draft Chapter 3 - software engineering

**Issue:** [#3](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/3)

**Status:** Reviewed draft ready for owner review - 2026-07-18.

**Depends on:** WP-03.

**Scope:** requirements, modularity, abstraction, verification, version control, build feedback, review and evolutionary change. Use Joel Spolsky material as dated practitioner context where assigned.

### WP-06: Draft Chapter 4 - Internet, web and application programming interfaces

**Depends on:** WP-01 and WP-03.

**Scope:** request path, network protocols, Hypertext Transfer Protocol (HTTP), Transport Layer Security (TLS), browser foundations, application programming interfaces, browser state, progressive enhancement and compatibility. Verify current organisations and browser-platform material.

### WP-07: Draft Chapter 5 - data and databases

**Depends on:** WP-03.

**Scope:** schemas, relational data, integrity, queries, transactions, migrations and non-relational models. Protect the boundary with distributed systems and recovery.

### WP-08: Draft Chapter 6 - architecture and distributed systems

**Depends on:** WP-05, WP-06 and WP-07.

**Scope:** boundaries, architecture views, component styles, messaging, partial failure, deadlines, idempotency, consistency and overload control.

## Production packages

### WP-09: Draft Chapter 7 - infrastructure, cloud and delivery

**Depends on:** WP-08.

**Scope:** environments, compute models, cloud and managed services, shared responsibility, artefacts, deployment safety, capacity, cost and exit planning. Include selected dated platform and stack profiles.

### WP-10: Draft Chapter 8 - operations, reliability and observability

**Depends on:** WP-09.

**Scope:** readiness, reliability targets, telemetry, operational response, performance and recovery. Cross-link rather than redefine distributed failure.

### WP-11: Draft Chapter 9 - security, privacy and identity

**Depends on:** WP-06 through WP-10.

**Scope:** trust, identity, access, cryptography, interpreter boundaries, web and file attacks, supply-chain risk, personal data and incident handling. Require security-sensitive primary sources and specialist critique.

## Purpose and accountability packages

### WP-12: Draft Chapter 10 - product, experience and analytics

**Depends on:** WP-05 and WP-06.

**Scope:** product purpose, prototype versus production, discovery, usability, accessibility, responsive design, analytics, experiments, prioritisation and support feedback.

### WP-13: Draft Chapter 11 - governance, compliance and commercial readiness

**Depends on:** WP-09 through WP-12.

**Scope:** accountability, category distinctions, controls and evidence, data-protection governance, third parties, intellectual property, contracts, continuity and assurance. Verify jurisdiction, editions, scope and terminology.

## Modern practice and judgement packages

### WP-14: Draft Chapter 12 - artificial intelligence-assisted engineering

**Depends on:** WP-05 through WP-11.

**Scope:** models, prompting, code generation, agents, tools, permissions, independent evaluation, artificial intelligence-specific attacks, providers and retained engineering responsibility. Date product and protocol landscape material.

### WP-15: Draft Chapter 13 - laws, heuristics and judgement

**Depends on:** the canonical mechanisms in WP-01 through WP-14.

**Scope:** sources of technical truth, leaky abstractions, evolution, organisations, incentives, simplicity and system effects. Collect cross-links to technical laws in their natural chapters. Use Hacker Laws, the Jargon File and Joel Spolsky as qualified source collections and practitioner context.

## Whole-guide packages

### Further-territory packages for Chapters 3–13

Each row is an independently publishable issue. Its exact topic list is the corresponding **Further territory** section in [OUTLINE.md](OUTLINE.md); changing that scope requires an outline change rather than an informal drafting decision.

| Package | Scope | Depends on |
| --- | --- | --- |
| **WP-F03** | Chapter 3 further territory | WP-05 |
| **WP-F04** | Chapter 4 further territory | WP-06 |
| **WP-F05** | Chapter 5 further territory | WP-07 |
| **WP-F06** | Chapter 6 further territory | WP-08 |
| **WP-F07** | Chapter 7 further territory and dated stack profiles | WP-09 |
| **WP-F08** | Chapter 8 further territory | WP-10 |
| **WP-F09** | Chapter 9 further territory | WP-11 |
| **WP-F10** | Chapter 10 further territory | WP-12 |
| **WP-F11** | Chapter 11 further territory and scheme profiles | WP-13 |
| **WP-F12** | Chapter 12 further territory and artificial intelligence landscape profiles | WP-14 |
| **WP-F13** | Chapter 13 further territory, cross-links and cultural asides | WP-15 |

### WP-17: Whole-guide integration and currentness review

**Depends on:** WP-01 through WP-15 and WP-F03 through WP-F13.

**Scope:** check dependency flow, canonical ownership, glossary coverage, repeated definitions, current landscape dates, link health and the size of the first traversal.
