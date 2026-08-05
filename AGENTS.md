# AGENTS.md

## Identity

- Public name: **Technical Foundations for Builders**
- Informal abbreviation: **TFB**
- Volume role: **Volume 1**, focused on trustworthy software systems
- Planned companion: **Technical Leadership for Builders** (TLB), Volume 2
- Separate related project: **Delivery Risk Cube** (DRC)
- GitHub repository: `technical-foundations-for-builders`
- Site identity: use a descriptive name such as `foundationsforbuilders`; do not rely on `tfb` alone.

## Project intent

Build **Technical Foundations for Builders**: a breadth-first map of the computing, engineering, product and operational concepts needed to build trustworthy production software in a world where AI assistance and agentic engineering are normal.

The guide is for founders, solo builders and other self-taught people who can already ship software but have not yet built the broad mental models usually gained through a computer-science education and years of production experience. Its immediate audience includes the non-technical or newly technical “vibe coder”. It should also remain useful to journeyman developers, solopreneurs and sole technical contributors whose experience is deep in some areas but incomplete across the whole production landscape. Technically experienced people using the same tools are better described here as practising agentic engineering.

The goal is awareness and better judgement, not mastery. TFB helps readers discover their unknown unknowns. Once aware of a concept or risk, they are better able to investigate it with AI, documentation or professional help. Readers should learn what a concept is, why it exists, where it fits, when it matters, what evidence would matter and when they need deeper help. Awareness is not proof that a system is correct.

## Project family and audiences

Read [PROJECT_FAMILY.md](PROJECT_FAMILY.md) before changing scope, audience or the relationship between the works.

- **TFB** explains the technical territory beneath trustworthy software systems.
- **TLB** is the planned Volume 2 about carrying the wider technical function of a small organisation.
- **DRC** is a separate project that frames which imbalance or missing evidence deserves attention before the next commitment.

The existing chapter outline and milestones govern TFB Volume 1. Do not add TLB's organisational territory to the current 13-chapter traversal. Give TLB its own outline and execution plan after its audience and promise receive a separate editorial review. DRC may be introduced as a useful lens, but it is not TFB's organising structure.

## Editorial principles

- Be explanation-first, not link-first. Do not turn this into an “awesome” list.
- Prefer durable concepts as the connective tissue, while covering current tools, products, vendors, organisations and schemes when awareness of them is useful to a contemporary builder.
- Cover the territory broadly and keep the initial treatment deliberately shallow.
- Optimise for selective browsing; do not require a fixed or sequential curriculum.
- Teach production thinking: correctness, reliability, security, performance, maintainability, operability, recoverability, and compliance.
- Teach each concept superficially: explain its basic mechanics and use a few headline examples, while omitting obscure detail.
- Use plain language, diagrams where useful, pitfalls, and relevant links embedded throughout the prose.
- Treat AI assistance and agentic engineering as a pervasive contemporary context. Keep their distinctive mechanisms canonical in the dedicated chapter, while explaining material consequences in any chapter where they change behaviour, risk, evidence or responsibility.
- Curate a few strong references instead of collecting every available resource.
- Treat the guide as a maintained living document. Include useful current practice, date material whose accuracy depends on products, organisations, standards or practice, and allow automation to propose currentness updates without delegating editorial judgement to it.
- Use memorable laws, practitioner stories and hacker folklore when they make a mechanism easier to remember. Explain the mechanism plainly and do not make humour carry the factual burden.

## Information architecture

1. **Project family:** `PROJECT_FAMILY.md` defines the distinct promises and boundaries of TFB, TLB and DRC.
2. **Repository overview:** `README.md` explains the purpose and makes the whole territory visible without exposing the complete inventory.
3. **Editorial outline:** `OUTLINE.md` records the canonical home and disclosure tier of retained topics.
4. **First-pass chapter pages:** `chapters/` provides a breadth-first traversal through a deliberately limited selection of properly explained concepts.
5. **Further territory:** `further/` provides optional awareness-level entries that are useful but not required for the first traversal.
6. **Recognition and landscape material:** short mentions, current products, organisations, schemes, laws and cultural terms appear where they make another concept easier to recognise.
7. **Glossary:** `GLOSSARY.md` gives short definitions and links back to canonical entries.

Likely domains include computing, programming, software engineering, architecture and systems, web and networking, data, infrastructure and delivery, security and privacy, operations and reliability, product and analytics, governance and compliance, AI-assisted engineering, and laws and principles.

## Progressive disclosure

Assign each retained candidate one treatment:

1. **First pass:** a complete awareness-level entry on the main traversal.
2. **Further territory:** an optional awareness-level entry for a less immediately necessary or more specific concept.
3. **Recognition only:** a short explanation inside a related entry, including current products, vendor organisations and named schemes where appropriate.
4. **External or omitted:** a link or omission when extra coverage would add more catalogue weight than useful understanding.

Reduce the number of concepts on the first pass, not the quality of their explanations. Concepts do not need equal-sized entries or to sit at the same level of abstraction. Their treatment should reflect what the target reader needs to recognise and understand.

## Repository boundary and publication workflow

- The public repository, `digital-mercenaries-ltd/technical-foundations-for-builders`, is the published guide. It may contain only material that is safe and useful to publish.
- The private companion repository, `digital-mercenaries-ltd/technical-foundations-for-builders-private`, is the research vault and editorial workshop. It holds original source files, raw research notes, unpublished context and other non-public material.
- Use separate local clones. Do not add one repository as a second remote for the other and do not push a private-work branch to the public repository.
- Research starts private by default. Promote its conclusions by writing or revising reader-facing content in the public repository; do not copy raw notes or original reference files automatically.
- If a research note should be public, create a deliberately edited, non-sensitive public version with its own source links and review it before publication.
- The original `Technical Foundations for Founders` reference files are private-only. Do not reintroduce them or a public `research/` directory into this repository.

Sub-agent handoff artefacts for this project belong in the private companion repository's `handoffs/` directory. Do not place them in this public repository or an operating-system temporary directory. Name files `YYYY-MM-DD-<task>-<agent>.md` and retain sources, findings, unresolved questions and the intended next action. Handoffs are working evidence, not a second delivery ledger; GitHub Issues remains authoritative for work status.

## Concept-entry shape

Each concept should normally answer:

1. What is it?
2. How does it work at a basic level? Include only the examples needed to establish a useful initial mental model.
3. Why does a builder need to know about it?
4. Where does it appear?
5. What are its pitfalls and misleading intuitions?
6. Which concepts in TFB are related?
7. Which deeper concepts might the reader encounter next?
8. Where can the reader go deeper? Limit this to a few strong references.

Use standard GitHub Markdown links in a wiki-like way: link relevant terms and sources at the point where they help, rather than collecting all links at the end.

## Agent skills

### Issue tracker

Track work in GitHub Issues for `digital-mercenaries-ltd/technical-foundations-for-builders`. External pull requests are not a request or triage surface. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the standard `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human` and `wontfix` roles. See `docs/agents/triage-labels.md`.

### Domain docs

Treat TFB and the planned TLB as bounded editorial contexts within one project family. The current repository content remains the TFB context until a separate TLB structure is approved. See `docs/agents/domain.md`.

## Writing and editorial delivery

For reusable prose, fetch and follow the [Writing Style Guide SOP](https://app.notion.com/p/3aea4c502b178183bd05dfaf0d4c2b8d). For collaboration, research, progress reporting and completion claims, fetch and follow the [AI Interaction and Collaboration Guide](https://app.notion.com/p/3aea4c502b1781acaa56e800b0ef1c15). Treat both as binding for this personal project unless an explicit project rule conflicts.

TFB is primarily explanatory documentation in the Diátaxis sense. Establish each entry's claim, reader need, mechanism or evidence and consequence before drafting headings. Lead with the substantive point, use one consistent term per concept, name responsible actors, preserve causal distinctions and trade-offs, and remove generic importance claims, repetitive transitions, catalogue prose and recap conclusions. Apply the full editorial rules in `STYLE_GUIDE.md` as the project-specific contract.

For planning and delivery, fetch and adapt [SOP: Adaptive Agentic Software Delivery v1.2](https://app.notion.com/p/3aea4c502b1781a888b1f8e851697813). GitHub Issues are this repository's sole canonical delivery ledger; chat, `PLAN.md`, `WORK_PACKAGES.md` and audits must not become competing live trackers. Keep the long-range chapter map shallow. Elaborate and execute one controlled chapter or reference increment at a time, then stop at its owner-review gate.

Adapt the software-delivery evidence model to editorial work:

- A ready chapter increment states its outcome, reader, included topics, boundaries, dependencies, source requirements, currentness risks, deterministic checks, independent reviewers and stop condition.
- Private cited research precedes public prose. A separate drafter and independent specification and standards reviews provide evaluation outside the implementation context.
- The evidence chain is the GitHub issue, private research commit, public chapter and audit, deterministic documentation checks, external-link results, review findings and public commit.
- Use behaviour-driven development notation only when Given/When/Then genuinely clarifies observable behaviour. Acceptance criteria describe evidence, not drafting tasks.
- Use the Delivery Risk Cube only as a milestone-health prompt: compare breadth, editorial fidelity and production-quality evidence with the next publication commitment. It is not TFB's organising structure or a completion score.
- Mark a chapter issue complete only after owner approval. Do not proceed automatically into the next chapter.

## Scope guardrails

- Do not design this as job training, interview preparation, or an academic CS course.
- Do not assume that a working prototype is production-ready.
- Do not prescribe depth where awareness and a warning sign are sufficient.
- Do not organise the initial guide around tasks, practical paths, or checklists.
- Do not reorganise TFB around the Delivery Risk Cube or treat the cube as a universal lifecycle, maturity model or completion score.
- Do not treat artificial intelligence as relevant only to Chapter 12, or repeat generic AI commentary when it does not materially change a concept.
- Do not absorb general information technology, organisational technology leadership or the whole accidental-chief-technology-officer role into TFB Volume 1; those belong to the planned TLB context.
- Do not begin implementation planning until the project intent and audience are confirmed.

Historical checklists such as the Joel Test may appear as clearly labelled artefacts after their underlying concepts have been explained. They are not TFB's organising structure or proof of readiness.

The initial delivery format is a GitHub repository of Markdown files. Do not introduce a site generator or other publishing system without a demonstrated need.

The original source document is held in the private companion repository.
