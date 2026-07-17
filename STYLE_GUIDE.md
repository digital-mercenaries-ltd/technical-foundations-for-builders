# TFB Style Guide

Status: Milestone 2 draft - 2026-07-17

This is the editorial contract for Technical Foundations for Builders (TFB). It applies to human and agent contributors.

## Reader and purpose

Write for a capable adult who has a real software project but no assumed technical education. The reader can investigate and act once they know what to investigate. Our job is to expose the concept, establish a useful initial mental model and show why it matters.

Do not write as if the reader is studying for an examination, changing careers or following a task tutorial. Do not treat a non-technical background as a lack of intelligence.

## Editorial principles

1. **Awareness before mastery.** Make the concept visible and recognisable.
2. **Breadth before depth.** Cover the important territory and stop before obscure detail.
3. **Brevity through compression.** Remove detail, not the context required for meaning.
4. **Context before jargon.** Establish the idea or problem before leaning on its name.
5. **Relevance, not procedure.** Explain why and where; do not turn the entry into a how-to guide.
6. **Mental models over isolated facts.** Connect each concept to the system around it.
7. **Independent but connected entries.** A deep link should be understandable without reading the chapter from the start.
8. **Durable concepts, current references.** Prefer ideas that outlast today's tools.
9. **Useful now, maintainable later.** Include current products, vendors, organisations and schemes when recognising them helps today's reader, and mark time-sensitive material for review.
10. **Progressive disclosure.** Keep the first traversal small without weakening the explanation of what it retains.

## Content layers

TFB deliberately mixes ideas at different levels: binary representation, a managed platform, a standards body and an assurance scheme may all be useful things for the same builder to recognise. Do not force them into equal-sized entries. Assign each retained candidate one treatment in [OUTLINE.md](OUTLINE.md):

1. **First pass:** a complete awareness-level entry on the main breadth-first traversal. Use this when a concept corrects a dangerous intuition, supports several later ideas or regularly affects ordinary production software.
2. **Further territory:** an optional awareness-level entry for material that is important but less necessary on the initial traversal or one layer more specific.
3. **Recognition only:** a short explanation inside a related entry. This often suits a product, vendor, organisation, standard, scheme, named law or cultural term.
4. **External or omitted:** a link or omission when TFB would add catalogue weight without improving the reader's mental model.

The governing rule is: **reduce the number of concepts covered on the first pass, not the quality of their explanation.** “Further” means optional or more specific, not advanced or exhaustive. “Go deeper” means leaving TFB for a small set of strong external resources.

## Voice and language

- Use plain British English, except where a standard term or quoted title uses another spelling.
- Address the reader directly when it makes a sentence clearer.
- Prefer concrete nouns and active verbs.
- Use an unfamiliar technical term only when it is the subject being introduced, has already been grounded, or is linked to a plain-language explanation.
- Avoid “simply”, “just”, “obviously” and similar language that hides difficulty.
- Avoid hype, condescension, academic throat-clearing and jokes that depend on technical knowledge.
- State trade-offs. Do not present a default as a universal law.
- Use acronyms only after writing the name in full. Add the acronym to the glossary if it recurs.
- Allow personality, practitioner language and humour. Explain unfamiliar jokes or jargon, and never rely on them as the factual explanation.

## Concept-entry template

Use this structure by default. Merge adjacent sections when separate headings make a short entry feel mechanical, but retain every editorial function.

```markdown
## Concept name

*Plain-language subtitle or one-sentence orientation.*

### What it is

Define and explain the concept. Include its basic mechanics and one or two headline examples.

### Why a builder needs to know this

Explain the decisions, risks or conversations for which awareness matters.

### Where it appears

Give a small number of representative contexts, not an exhaustive catalogue.

### Pitfalls

Correct the most consequential beginner misunderstandings.

### Related concepts in TFB

- [Existing concept](relative-path.md#anchor) - relationship to this concept.

### Deeper concepts

- Concept name - why it is a logical next layer.

### Further reading

- [Descriptive source title](https://example.com/) - what the source adds.
```

The template defines editorial functions, not a demand that every entry have the same length or level of abstraction. A narrow but important scheme may need a shorter entry than a foundational mechanism. A current product profile may need a dated orientation rather than the full concept template.

## Other content forms

### Current landscape item

Use for a product, vendor, organisation, protocol, framework or scheme whose name a contemporary builder is likely to encounter.

- State what category it belongs to and what responsibility it has.
- Connect it to the durable concepts it implements, publishes or influences.
- Identify important boundaries, incentives or coupling where relevant.
- Add `Reviewed: YYYY-MM-DD` when the description can become stale.
- Do not present inclusion as an endorsement or popularity ranking.

### Related observation

Use for a named law, maxim or practitioner story that makes a mechanism memorable. Explain the underlying idea and its important qualification. The surrounding entry must remain understandable if the observation is removed.

### From hacker folklore

Use for historical jargon or humour, including terms such as *heisenbug*, *yak shaving*, *bikeshedding* and *PEBKAC/PEBCAK*. Give the plain meaning and the real mechanism or behaviour behind the joke. Irreverence is acceptable; using a joke instead of investigating a system or interface failure is not.

### Historical field checklist or case study

Use a dated checklist or case when its original form is part of its value. Explain where it came from, distribute its underlying concepts to their canonical homes and state what has dated or requires qualification. A checklist is a conversation aid, not a certification or proof of readiness.

## Depth and length

The working range is 250-500 words for a normal awareness-level concept entry, excluding the resource lists. It is a calibration range, not a quota. Short landscape items and asides may be much smaller. First-pass chapters should normally contain approximately five to eight principal entries and remain readable in one sitting.

An entry is deep enough when a reader can:

- explain the headline idea in their own words;
- recognise representative examples;
- say why the concept might matter to a project;
- avoid its most important misleading intuition;
- identify what to investigate next.

Stop before derivations, exhaustive variants, historical catalogues, language-specific recipes or implementation instructions unless one is essential to the initial model.

Do not solve breadth by putting every candidate on the first pass. Move optional concepts to further territory, name them briefly for recognition or link externally.

## Examples

Use examples to perform explanatory work. For a representation such as binary, show a small conversion. For an operational concept such as a retry, show the failure pattern it changes. Prefer one worked example over five named examples.

Label conventions clearly. If a sequence could be confused with an everyday decimal number, identify its base or use a standard prefix such as `0b`, `0o` or `0x` after explaining the notation.

## Grounding jargon

Treat knowledge as a dependency graph: an explanation may rely only on ideas the reader is assumed to know, has already met, or can follow through a useful link.

At chapter level:

- State the small set of ordinary ideas assumed at entry.
- Order concepts so that foundational ideas tend to appear first.
- Do not make order mandatory; define enough locally for a direct visitor.

At sentence level:

- Introduce the idea and its name together.
- Link a term at its first useful mention, not every occurrence.
- Do not solve unexplained jargon by linking every other word. Rewrite the sentence first.
- If following a link is required to understand the current sentence, the current sentence is probably too dependent on it.

## Links

Use standard GitHub Markdown links in a wiki-like editorial style.

- Link concepts to their one canonical entry with a relative path and heading anchor.
- Link sources at the claim or explanation they support when that context helps the reader.
- Use descriptive link text; avoid “click here”, raw URLs and repeated links to the same target in one section.
- Prefer stable canonical URLs over search results, mirrors, URL shorteners or tracking links.
- Do not create links to planned headings that do not yet exist.
- Check relative links and heading anchors before review.

The final **Related concepts**, **Deeper concepts** and **Further reading** lists are curated next steps. They should not repeat every inline link.

## Sources

Match the source to the claim:

1. Prefer standards, specifications, original papers, official documentation and first-party material for definitions and factual claims.
2. Prefer established teaching material for accessible explanation.
3. Use Wikipedia and good secondary explainers for orientation or a broader overview, not as automatic proof of every technical claim.
4. Use vendor explainers when the vendor has relevant expertise and the page teaches beyond its product. Avoid sales material disguised as education.
5. Use the original source for a named law, framework or standard when it remains reasonably accessible.

Further reading should usually contain two to four items. Say what each source offers. A short, purposeful list is better than an “awesome” list.

For facts that are current, contested, security-sensitive or easy to misstate, record the research and verification date in a note in the private companion repository using ISO-8601 format.

For current products, vendors, organisations, standards and schemes:

- prefer the maintainer, publisher or responsible organisation for identity, scope and current status;
- use independent evidence for comparative claims, adoption, performance or criticism;
- record a review date in the private research note and on a landscape item when staleness would mislead;
- distinguish a product from its category, a standards body from documentation, and a certification from an assurance report;
- keep historical examples dated rather than silently modernising them.

TFB is a living document. Currentness is a maintenance responsibility, not a reason to omit useful contemporary names.

## Canonical concepts and redundancy

Every concept has one canonical home. When another entry needs the idea:

- give only the local context needed;
- link to the canonical explanation;
- do not silently create a second definition.

If two entries repeatedly need the same explanation, reconsider their boundary or extract a shared foundational concept.

One concept may have examples at several levels. That is not duplication when the canonical mechanism remains in one place and each product, standard or story contributes distinct orientation.

## Glossary

The glossary is an alphabetical index, not a second handbook.

- Use one sentence per term where possible.
- Expand abbreviations.
- Link to the canonical entry.
- Do not introduce claims or examples that belong in the chapter.
- Add a term when readers may encounter it before its full entry or when its meaning is easy to confuse.

## Diagrams

Use a diagram only when it makes a relationship, hierarchy or sequence materially easier to understand. GitHub-rendered Mermaid is acceptable when text labels remain plain and the source is readable. Every diagram needs a short textual explanation for readers who do not parse it visually.

## Agent workflow

- Give research agents bounded concept clusters and require cited private notes before drafting sensitive material.
- Give drafting agents the chapter purpose, audience assumptions, concept dependencies, source note and this guide.
- Do not let parallel agents edit the same chapter file.
- Have a different agent critique the draft for accuracy, grounding, relevance and redundancy.
- Let one lead editor integrate changes and protect canonical definitions.
- Require the outline tier, content form and canonical home in every drafting brief.
- Separate durable claims from current landscape claims so that time-sensitive material can be reviewed independently.

Agent-written prose receives the same factual and editorial review as human-written prose.

## Definition of done

A concept entry is ready when it passes the quality rubric in [PLAN.md](PLAN.md#7-quality-rubric), its links resolve, its important claims are supported and removing more text would damage the reader's initial mental model.
