# TFB project family

Status: editorial direction confirmed - 2026-07-31

This document defines the relationship between **Technical Foundations for Builders** (TFB), the planned **Technical Leadership for Builders** (TLB) companion and the separate **Delivery Risk Cube** (DRC) project. It prevents their audiences and promises from being collapsed into one oversized guide.

## Shared worldview

All three works assume that artificial intelligence (AI) assistance and agentic engineering are normal parts of contemporary software work. They should remain useful as particular models, agents, protocols and products change.

Their common editorial model has three layers:

1. **Durable mechanisms:** the computing, engineering, product and organisational principles that remain applicable across tool generations.
2. **Agentic consequences:** what materially changes when probabilistic models generate artefacts, use tools, retain context, coordinate work or act with delegated authority.
3. **Current landscape:** the models, products, protocols, standards and practices a contemporary builder is likely to encounter, supported by sources and ISO-8601 review dates where needed.

AI is therefore neither an appendix nor a replacement for established engineering. Traditional mechanisms still govern state, latency, coupling, transactions, trust, recovery, cost and accountability. Agentic methods can change how quickly systems are produced, how failures arise and how difficult it is for a responsible person to understand the result.

These are living works. Automation may detect stale review dates, broken links, changed versions, renamed products, updated standards and potentially superseded claims. Human editorial review remains responsible for meaning, selection, accuracy and whether a current item still belongs.

## Volume 1: Technical Foundations for Builders

TFB is the breadth-first map of the concepts needed to understand and build trustworthy production software.

Its primary reader is a capable builder with a real software project but no assumed formal technical education. This includes non-technical or newly technical people building with AI. It should also remain useful to self-taught developers, journeyman engineers, solopreneurs and sole technical contributors who have depth in some areas but gaps elsewhere.

TFB's unit of concern is principally the **software system or service**. It asks:

- How does this mechanism work?
- Where does it appear?
- How can it fail or mislead?
- What evidence would matter?
- When is deeper investigation or experienced help required?

The existing 13-chapter outline is the scope of Volume 1. Product and governance remain necessary interfaces because software must serve people and operate within organisational obligations. TFB does not expand those chapters into a complete guide to running a technical function.

## Volume 2: Technical Leadership for Builders

TLB is the planned companion about carrying the technical function of a small organisation, startup, department or solo venture.

Its reader may be a solopreneur, journeyman developer, founder, operator, sole technical employee, technical lead or accidental chief technology officer. They are responsible for decisions and outcomes beyond the codebase even when no formal technology organisation exists.

TLB's unit of concern is the **organisation's technical capability**. Likely territory includes:

- technology strategy, decision rights and risk appetite;
- product ownership, user research and experience;
- planning, estimation, capacity, delivery and organisational change;
- business systems, internal processes and integration;
- application and service portfolio management, rationalisation and lifecycle;
- workplace information technology, identity, devices and software-as-a-service administration;
- data ownership, governance and organisational analytics;
- security, privacy, compliance and external assurance;
- budgets, total cost, procurement, vendors, contracts and exit planning;
- hiring, outsourcing, key-person risk, continuity and technical leadership.

TLB is not an advanced sequel that requires every reader to finish TFB. The volumes are sibling maps with cross-links. Before TLB drafting begins, give it its own outline, disclosure tiers and execution plan rather than adding its territory to the Volume 1 chapter inventory.

## Separate project: Delivery Risk Cube

DRC is a decision framework for judging whether a project's accumulated evidence and implementation are shaped appropriately for its next commitment.

Its three dimensions are:

1. **Functional breadth:** which user needs, capabilities and journeys have been explored.
2. **Implementation fidelity:** how real, integrated and complete the implementation is.
3. **Production-quality depth:** what evidence exists for security, reliability, performance, operability, recoverability, accessibility, privacy, compliance and other consequential qualities.

The governing question is not “How full is the cube?” or “What percentage complete are we?” It is:

> What shape should this project have before its next commitment?

A proof of concept, product experiment, private pilot, public launch and regulated deployment require different shapes. DRC describes trajectory and imbalance, not a universal lifecycle, maturity ladder or readiness score.

AI is not a fourth DRC axis. Agentic methods affect all three axes: they can expand visible scope rapidly, create an appearance of fidelity and either deepen or conceal the absence of production evidence.

DRC and TFB have complementary roles:

> DRC provides the decision frame; TFB provides many of the underlying explanations.

DRC remains a separate project so that its argument, case studies, assessment method and possible book or coaching tools can develop without reorganising TFB around a delivery framework.

## Editorial boundaries

Use these tests when a topic could fit more than one work:

| Question | Canonical home |
| --- | --- |
| How does a software mechanism behave, fail or become trustworthy? | TFB |
| What must the organisation own, fund, govern or coordinate? | TLB |
| Given the next commitment, which imbalance or missing evidence deserves attention now? | DRC |

Cross-reference rather than duplicate a full explanation. A topic may appear in more than one work from a different unit of concern—for example, technical access control in TFB and organisational joiner-mover-leaver responsibility in TLB—but each treatment must state its boundary.

## Cross-work placement examples

### Architecture decision records

- **TFB canonical treatment:** explain architecture decision records (ADRs) as lightweight, versioned records of a consequential software decision's context, status, decision and consequences. Connect them to architecture, documentation, sources of technical truth and reversible change.
- **TLB treatment:** govern decision rights, thresholds for recording decisions, participation, review, supersession, exceptions and organisational memory. Cross-link to TFB rather than reteaching the record format.
- **DRC use:** accept a relevant ADR as one form of evidence that assumptions and consequences have been considered before a commitment. Its presence does not prove that the decision is correct, and not every decision needs an ADR.

### Wardley mapping

- **TLB canonical home:** teach the durable mechanism of strategic situational awareness: user needs, dependency chains, component evolution, differentiation, sourcing and capability choices. Introduce Wardley mapping as one named method that combines these ideas, while treating positions and movements as contestable models rather than facts. Decide whether the named method receives further-territory or recognition treatment when TLB receives its own editorial outline; do not automatically make it a principal entry.
- **TFB treatment:** recognition or an external cross-reference only where component evolution materially explains an architecture, platform, managed-service, vendor-coupling or exit decision. Do not add Wardley mapping to TFB's 13-chapter first traversal.
- **DRC use:** a Wardley map may supply optional context about dependencies, novelty and strategic movement before the next commitment. It is not a DRC axis, maturity score, risk register or substitute for technical and product evidence.

Planning references: [GDS guidance on architecture decision records](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html), [Wardley Mapping introduction](https://learnwardleymapping.com/introduction) and Simon Wardley's freely available [mapping book](https://learnwardleymapping.com/book/).

### Gartner TIME application-portfolio model

- **TLB canonical home:** teach the durable practice of application portfolio management: maintain an inventory, relate applications to business capabilities and users, assess business, technical and cost fitness, expose dependencies and lifecycle constraints, and make explicit investment and retirement decisions. Introduce Gartner's TIME model—**Tolerate, Invest, Migrate and Eliminate**—as one named categorisation framework, not as an automatic verdict or permanent label. Review decisions as needs, costs, risks and available alternatives change.
- **TFB treatment:** recognition or an external cross-reference from legacy-system evolution, managed services, vendor coupling, portability and exit planning. TFB should explain the technical evidence that makes migration, continued operation or retirement safe, but should not absorb organisation-wide application inventory and portfolio governance.
- **DRC use:** the intended TIME direction can help state the next commitment. DRC can then ask whether the project has an appropriate shape and evidence for that direction—for example, migration compatibility and rollback evidence or elimination, data-retention and dependency-removal evidence. A TIME category is not a DRC axis, maturity level, readiness score or substitute for validating the decision.

Do not infer that **Migrate** means cloud migration or that **Eliminate** means immediate deletion. Migration may replace, consolidate or move a capability, while elimination requires deliberate user, dependency, data, contractual, compliance and recovery decisions. Planning references, reviewed 2026-07-31: [Gartner's public enterprise-applications overview of the TIME method and its fitness dimensions](https://www.gartner.com/en/information-technology/topics/enterprise-apps) and [SAP LeanIX's TIME framework overview](https://www.leanix.net/en/wiki/apm/gartner-time-model).
