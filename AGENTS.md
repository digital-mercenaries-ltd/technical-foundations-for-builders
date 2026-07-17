# AGENTS.md

## Identity

- Public name: **Technical Foundations for Builders**
- Informal abbreviation: **TFB**
- GitHub repository: `technical-foundations-for-builders`
- Site identity: use a descriptive name such as `foundationsforbuilders`; do not rely on `tfb` alone.

## Project intent

Build **Technical Foundations for Builders**: a breadth-first map of the computing, engineering, product, and operational concepts needed to build trustworthy production software, with or without AI.

The guide is for founders, solo builders, and other self-taught people who can already ship software but have not yet built the broad mental models usually gained through a computer-science education and years of production experience. Its immediate audience is the non-technical “vibe coder”; technically experienced people using the same tools are better described here as practising agentic engineering.

The goal is awareness and better judgement, not mastery. TFB helps readers discover their unknown unknowns. Once aware of a concept or risk, they are capable of asking AI what they need to learn or how to handle it. Readers should learn what a concept is, why it exists, where it fits, when it matters, and when they need deeper help.

## Editorial principles

- Be explanation-first, not link-first. Do not turn this into an “awesome” list.
- Prefer durable concepts over current tools, vendors, and “vibe coding” terminology.
- Cover the territory broadly and keep the initial treatment deliberately shallow.
- Optimise for selective browsing; do not require a fixed or sequential curriculum.
- Teach production thinking: correctness, reliability, security, performance, maintainability, operability, recoverability, and compliance.
- Teach each concept superficially: explain its basic mechanics and use a few headline examples, while omitting obscure detail.
- Use plain language, diagrams where useful, pitfalls, and relevant links embedded throughout the prose.
- Be relevant to AI-assisted builders without making AI tooling the centre of the guide.
- Curate a few strong references instead of collecting every available resource.

## Information architecture

1. **Repository overview:** `README.md` explains the purpose, maps the territory, and introduces each chapter in plain language.
2. **Chapter pages:** one Markdown file per major section, containing several related concept entries.
3. **Concept entries:** independently understandable sections within chapter pages, connected by wiki-style inline links.
4. **Glossary:** `GLOSSARY.md` gives short definitions and links back to the canonical entries.

Likely domains include computing, programming, software engineering, architecture and systems, web and networking, data, infrastructure and delivery, security and privacy, operations and reliability, product and analytics, governance and compliance, AI-assisted engineering, and laws and principles.

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

## Scope guardrails

- Do not design this as job training, interview preparation, or an academic CS course.
- Do not assume that a working prototype is production-ready.
- Do not prescribe depth where awareness and a warning sign are sufficient.
- Do not organise the initial guide around tasks, practical paths, or checklists.
- Do not begin implementation planning until the project intent and audience are confirmed.

The initial delivery format is a GitHub repository of Markdown files. Do not introduce a site generator or other publishing system without a demonstrated need.

The source document is `Technical Foundations for Founders.pdf` in the project root.
