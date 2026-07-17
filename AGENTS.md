# AGENTS.md

## Identity

- Public name: **Technical Foundations for Builders**
- Informal abbreviation: **TFB**
- GitHub repository: `technical-foundations-for-builders`
- Site identity: use a descriptive name such as `foundationsforbuilders`; do not rely on `tfb` alone.

## Project intent

Build **Technical Foundations for Builders**: a breadth-first map of the computing, engineering, product, and operational concepts needed to build trustworthy production software, with or without AI.

The guide is for founders, solo builders, and other self-taught people who can already ship software but have not yet built the broad mental models usually gained through a computer-science education and years of production experience. Its immediate audience is the non-technical “vibe coder”; technically experienced people using the same tools are better described here as practising agentic engineering.

The goal is awareness and better judgement, not mastery. TFB helps readers discover their unknown unknowns. Once aware of a concept or risk, they are better able to investigate it with AI, documentation or professional help. Readers should learn what a concept is, why it exists, where it fits, when it matters, what evidence would matter and when they need deeper help. Awareness is not proof that a system is correct.

## Editorial principles

- Be explanation-first, not link-first. Do not turn this into an “awesome” list.
- Prefer durable concepts as the connective tissue, while covering current tools, products, vendors, organisations and schemes when awareness of them is useful to a contemporary builder.
- Cover the territory broadly and keep the initial treatment deliberately shallow.
- Optimise for selective browsing; do not require a fixed or sequential curriculum.
- Teach production thinking: correctness, reliability, security, performance, maintainability, operability, recoverability, and compliance.
- Teach each concept superficially: explain its basic mechanics and use a few headline examples, while omitting obscure detail.
- Use plain language, diagrams where useful, pitfalls, and relevant links embedded throughout the prose.
- Be relevant to AI-assisted builders without making AI tooling the centre of the guide.
- Curate a few strong references instead of collecting every available resource.
- Treat the guide as a maintained living document. Date and periodically review material whose accuracy depends on current products, organisations, standards or practice.
- Use memorable laws, practitioner stories and hacker folklore when they make a mechanism easier to remember. Explain the mechanism plainly and do not make humour carry the factual burden.

## Information architecture

1. **Repository overview:** `README.md` explains the purpose and makes the whole territory visible without exposing the complete inventory.
2. **Editorial outline:** `OUTLINE.md` records the canonical home and disclosure tier of retained topics.
3. **First-pass chapter pages:** `chapters/` provides a breadth-first traversal through a deliberately limited selection of properly explained concepts.
4. **Further territory:** `further/` provides optional awareness-level entries that are useful but not required for the first traversal.
5. **Recognition and landscape material:** short mentions, current products, organisations, schemes, laws and cultural terms appear where they make another concept easier to recognise.
6. **Glossary:** `GLOSSARY.md` gives short definitions and links back to canonical entries.

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

Treat this as a single-context repository. Use root-level domain documentation and system-wide architecture decisions if they are added later. See `docs/agents/domain.md`.

## Scope guardrails

- Do not design this as job training, interview preparation, or an academic CS course.
- Do not assume that a working prototype is production-ready.
- Do not prescribe depth where awareness and a warning sign are sufficient.
- Do not organise the initial guide around tasks, practical paths, or checklists.
- Do not begin implementation planning until the project intent and audience are confirmed.

Historical checklists such as the Joel Test may appear as clearly labelled artefacts after their underlying concepts have been explained. They are not TFB's organising structure or proof of readiness.

The initial delivery format is a GitHub repository of Markdown files. Do not introduce a site generator or other publishing system without a demonstrated need.

The original source document is held in the private companion repository.
