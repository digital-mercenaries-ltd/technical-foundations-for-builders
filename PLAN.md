# Technical Foundations for Builders - Execution Plan

Status: Milestone 3 approved; Milestone 4 in progress - 2026-07-18

## 1. Objective

Create a broad, concise, contextual guide that helps non-technical builders discover the concepts and mental models they do not yet know to ask about.

Technical Foundations for Builders (TFB) should teach each concept superficially enough to establish a useful initial mental model. It should explain basic mechanics and headline examples, then direct the reader to related concepts and stronger resources for depth. It is not a task-oriented manual or a route to mastery.

## 2. Initial delivery architecture

Keep the first version as GitHub-native Markdown:

```text
README.md
AGENTS.md
PLAN.md
STYLE_GUIDE.md
GLOSSARY.md
OUTLINE.md
WORK_PACKAGES.md
chapters/
  01-<chapter-name>.md
  02-<chapter-name>.md
  ...
further/
  01-<chapter-name>.md
  02-<chapter-name>.md
  ...
reviews/
  milestone-<number>-audit.md
scripts/
  check_docs.py
```

`README.md` is the reader-facing map of the guide. It should make the whole territory visible without displaying the complete concept inventory. `OUTLINE.md` is the editorial source of truth for chapter boundaries, disclosure tiers and canonical homes. Each concept has one canonical entry within a first-pass or further-territory chapter file. Other mentions link to that entry instead of duplicating its explanation.

Use standard Markdown links such as `[binary](further/01-computing-foundations.md#binary-numbers)` rather than `[[wikilinks]]`, which GitHub does not render as repository-page links. The editorial experience should feel wiki-like even though the syntax remains GitHub-compatible.

Do not introduce a site generator, database, content management system (CMS), or structured content schema during the first milestones. Reconsider this only if the Markdown repository exposes a concrete limitation.

Raw research notes and original source material live in the separate private companion repository, `digital-mercenaries-ltd/technical-foundations-for-builders-private`. This public repository receives only deliberately edited reader-facing material and non-sensitive review records.

### 2.1 Progressive disclosure

Every retained candidate receives one treatment:

1. **First pass:** a complete awareness-level entry in `chapters/`.
2. **Further territory:** an optional awareness-level entry in `further/`.
3. **Recognition only:** a short explanation within a related entry, including products, organisations, named schemes, laws and jargon where appropriate.
4. **External or omitted:** a link or omission when more TFB coverage would add weight without useful understanding.

The README map, first-pass chapters and further-territory pages are three different browsing depths. External references provide depth beyond TFB; they are not a fourth internal curriculum.

## 3. Editorial unit

Each concept entry uses this default shape:

1. **Concept name and plain-language subtitle**
2. **What it is**
3. **How it works at a basic level**, using only enough detail and headline examples to create a useful mental model
4. **Why a builder needs to know about it**
5. **Where it appears**
6. **Pitfalls and misleading intuitions**
7. **Related concepts in TFB**
8. **Deeper concepts to explore**
9. **Further reading**, limited to a few strong resources

Relevant internal and external links should also be embedded naturally throughout the explanation. The final sections are curated navigation, not an automatic duplicate list of every inline link. Repeating one or two inline sources is acceptable when they are also the strongest routes to deeper understanding; their descriptions should say what further value they provide.

Use a soft initial budget of 250-500 words per concept, excluding resource lists. Milestone 1 showed that this range can support concrete awareness-level teaching; clarity takes priority over a rigid limit.

Concepts do not need equal-sized entries or to occupy the same level of abstraction. Use the full template for durable mechanisms. Use shorter dated landscape items for current products, vendors, organisations, protocols and schemes when name recognition is useful. Use related observations, historical asides and cultural jargon where they make a mechanism memorable.

## 4. Document software development lifecycle

Every content batch moves through the same lifecycle.

### 4.1 Scope

- Define the chapter's purpose and audience assumptions.
- List its concepts and assign one canonical home to each.
- Assign each candidate to first pass, further territory, recognition only, or external/omitted.
- Record dependencies: which concepts must be introduced before others can rely on them.
- Identify boundaries with neighbouring chapters.

### 4.2 Research

- Search for authoritative and accessible sources.
- Prefer standards, specifications, original papers, official documentation, and established teaching material for factual claims.
- Use Wikipedia, the Jargon File, Hacker Laws, respected books and courses, MDN Web Docs, educational vendor material, and strong explanatory articles for orientation and further reading.
- Save concise research notes with source links in the private companion repository; do not copy raw notes or original reference files into the public guide.
- Separate durable mechanism research from time-sensitive landscape research and record ISO 8601 review dates for the latter.

### 4.3 Draft

- Draft from the approved concept template and source notes.
- Introduce the idea before leaning on its jargon.
- Include enough mechanics and examples to teach the headline concept.
- Link terms to their canonical TFB entries as soon as the link helps the reader.

### 4.4 Critique

Run separate reviews for:

- conceptual accuracy;
- ungrounded jargon and hidden prerequisites;
- missing context or relevance;
- excessive depth or unexplained compression;
- redundancy and conflicting definitions;
- missing or weak sources;
- broken narrative flow within the chapter.

The primary critic should not be the agent that wrote the draft.

### 4.5 Integrate

- Resolve review findings through one lead editor.
- Replace repeated explanations with links to canonical entries.
- Update the glossary and cross-links.
- Check chapter boundaries and terminology against the full outline.

### 4.6 Verify

- Validate internal links, external links, and heading anchors.
- Run Markdown linting and spelling checks.
- Check that every entry contains the required editorial elements.
- Check that every retained topic has one tier and canonical home in `OUTLINE.md`.
- Recheck sources for claims that are current, contested, security-sensitive, or easy to misstate.
- Require human approval at each milestone gate before increasing the production batch size.
- Run `python3 scripts/check_docs.py`; the expected result is `Documentation checks passed.`

## 5. Agent and model strategy

### 5.1 Roles

- **Lead editor/orchestrator:** owns the taxonomy, style, canonical definitions, integration, and milestone gate.
- **Structure agents:** independently propose or critique chapter boundaries, topic coverage, ordering, and blind spots.
- **Research agents:** investigate bounded concept clusters and produce cited source notes without drafting final prose.
- **Drafting agents:** write non-overlapping concept ranges from approved briefs and research notes.
- **Critique agents:** review structure, jargon grounding, accuracy, redundancy, and reader relevance independently of the author.
- **Verification agent:** checks references, cross-links, glossary coverage, and conformance to the template.

Assign agents distinct files or concept ranges. Parallel agents should not edit the same chapter file simultaneously. The lead editor integrates their outputs after critique.

### 5.2 Work allocation by capability

Where the execution environment supports model selection:

- Use a high-reasoning model for taxonomy, dependency mapping, difficult technical explanations, conflict resolution, and final integration.
- Use faster, lower-cost models for bounded source collection, glossary extraction, template checks, link classification, and first-pass prose tightening.
- Use deterministic scripts for link checking, Markdown linting, spelling, duplicate-heading detection, and structural audits.

The current built-in sub-agent interface can parallelise work by role but does not expose per-agent model selection. Until that changes, efficiency should come from bounded briefs, parallelism, small context packs, and deterministic automation rather than pretending that different models were selected.

### 5.3 Relevant skills

- **`writing-shape` and `writing-beats`:** useful because they explicitly track which concepts have been grounded before later prose relies on them. Apply this discipline to chapter introductions and concept ordering.
- **`decision-mapping`:** useful only when chapter taxonomy or another consequential decision remains unresolved across sessions. Do not create decision tickets for settled editorial work.
- **`to-prd` and `to-issues`:** useful after Milestone 1 approval if the remaining work is to be divided into independently assignable GitHub issues.
- **`review`:** useful for integration reviews of changes against an approved baseline.
- **`edit-article`:** use selectively for tightening; its default 240-character paragraph constraint is too rigid to govern all TFB prose.
- **[Matt Pocock's `research` skill](https://www.skills.sh/mattpocock/skills/research):** installed and used for source-driven background research. It uses background agents and requires claims to be traced to primary sources.

The external [`documentation-writer`](https://www.skills.sh/github/awesome-copilot/documentation-writer) skill from `github/awesome-copilot` is reputable but centred on Diataxis and task-oriented documentation. TFB is primarily conceptual explanation, so it is not necessary for the initial workflow.

## 6. Milestones

### Milestone 1 - Editorial and structural prototype (complete)

Deliver only enough material to test the form:

- Draft `README.md` containing:
  - the TFB purpose and intended reader;
  - the awareness-first editorial promise;
  - instructions for using TFB with deeper resources or project-aware artificial intelligence;
  - the proposed top-level map;
  - fuller introductions and topic lists for the first two chapters;
  - names and concept lists for every remaining chapter.
- Create the Chapter 1 Markdown page.
- Fully draft only the first three concepts in Chapter 1.
- Create the first `STYLE_GUIDE.md` with the concept template, link rules, source policy, jargon rules, and provisional word budget.
- Seed `GLOSSARY.md` with terms used by the three drafted concepts.
- Run independent structure, reader, technical, and redundancy critiques.
- Verify every included link and factual claim.

Acceptance gate: the user approves or revises the audience promise, chapter granularity, overall coverage, concept depth, tone, entry template, jargon handling, link style, and source quality.

Stop after presenting Milestone 1. Do not draft later chapters until the user approves the revised form.

### Milestone 2 - Tiered outline and editorial system (approved 2026-07-17)

- Apply Milestone 1 feedback and the progressive-disclosure decision.
- Finalise chapter names, boundaries, first-pass selections, further territory and recognition-only landscape material in `OUTLINE.md`.
- Preserve the approved Chapter 1 prototype while using it to calibrate the tiered structure.
- Finalise the style guide, source policy, glossary rules and review rubrics for durable concepts, current landscape material, laws, practitioner stories and hacker folklore.
- Add lightweight automated structural, internal-link, anchor and duplicate-heading checks.
- Record independently assignable, issue-ready batches in `WORK_PACKAGES.md`; publish them to `digital-mercenaries-ltd/technical-foundations-for-builders` after Milestone 2 approval.

Acceptance gate: the user approves or revises the tiering, first-pass selections, treatment of current products and organisations, use of humour and historical material, and the production rules before parallel drafting begins.

### Milestone 3 - First complete first-pass chapter batch

- Finish the Chapter 1 and Chapter 2 first-pass pages through the full document lifecycle.
- Relocate the approved binary and hexadecimal/octal entries unchanged to Chapter 1 further territory and repair their incoming links.
- Do not draft every optional Chapter 1 and Chapter 2 further-territory topic in this milestone.
- Test cross-chapter linking, glossary maintenance, source verification, and integration.
- Measure actual entry length, estimated reading time, conceptual bundling, review effort, duplication, and correction rate.
- Adjust batch size and the editorial template based on evidence.

Acceptance gate: two complete chapters demonstrate a repeatable quality level.

Approved on 2026-07-17. The evidence supports keeping the 250–500-word entry calibration range and eight-entry chapter maximum unchanged. Eight entries is a ceiling, not a target: the next batch starts with one chapter so reading load, terminology and review effort can be checked before broader parallel drafting.

### Milestone 4 - Controlled parallel drafting

- Draft the remaining chapters in small, non-overlapping batches.
- Require research notes before prose for technically sensitive concepts.
- Pair every drafting batch with a different critique agent.
- Integrate only reviewed work into the main branch.
- Pause after each batch for coverage and consistency review; do not wait until the entire guide is drafted.

Acceptance gate: all planned concepts have a reviewed first draft and a canonical home.

### Milestone 5 - Whole-guide integration

- Review the complete guide as one connected mental model.
- Find gaps, unnecessary overlap, contradictory definitions, orphaned concepts, and poorly grounded jargon.
- Complete cross-links and the glossary.
- Recheck source authority, accessibility, durability, and link health.
- Tighten for brevity without removing essential mechanics, context, examples, or pitfalls.

Acceptance gate: the guide is coherent and browsable as a whole, not merely a collection of individually acceptable entries.

### Milestone 6 - Public release

- Complete final editorial, factual, and repository checks.
- Add concise contribution and maintenance guidance.
- Configure continuous link and Markdown checks on pull requests.
- Publish the approved Markdown repository and create an initial tagged release.
- Record deferred ideas separately; do not add a site generator or practical guide layer during release hardening.

Acceptance gate: the public repository accurately represents the approved scope and has a maintainable update process.

## 7. Quality rubric

A concept entry is ready only when:

- a non-technical builder can explain its basic idea after reading it;
- it says why the concept matters and where it appears;
- it includes the minimum mechanics and headline examples needed for understanding;
- it identifies important pitfalls or misleading intuitions;
- jargon is defined, grounded earlier, or linked at first useful mention;
- related and deeper concepts are distinguished;
- further reading is small, relevant, and credible;
- factual claims are supported by suitable sources;
- it does not duplicate another entry's canonical explanation;
- removing more text would damage the reader's initial mental model.

### 7.1 Current landscape item

A product, vendor, organisation, protocol, standard or scheme item is ready only when:

- its category, role and important responsibility boundaries are clear;
- it is connected to the durable concepts it implements, publishes or influences;
- inclusion is orientation rather than an endorsement or popularity claim;
- time-sensitive claims have suitable sources and an ISO-8601 review date;
- commercial claims, comparisons and limitations are attributed appropriately.

### 7.2 Related observation or hacker folklore

A law, maxim, practitioner story or cultural term is ready only when:

- the underlying mechanism is explained in plain language;
- the entry remains understandable without the memorable label or joke;
- important scope, exceptions and evidential status are stated;
- the original source or a reliable history is linked where available;
- humour adds recognition without substituting for diagnosis or belittling the reader.

### 7.3 Historical checklist or case study

A historical artefact is ready only when:

- its origin and date are clear;
- its durable ideas link to their canonical homes;
- dated assumptions and rhetorical absolutes are qualified;
- it is presented as context or a conversation aid, not proof, certification or a universal process.

## 8. Current Milestone 4 action

WP-05 was approved on 2026-07-18. [WP-06](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues/4) has produced a researched and independently reviewed Chapter 4 first-pass draft. Pause for owner review before opening Chapter 5. Continue to defer optional further-territory packages.
