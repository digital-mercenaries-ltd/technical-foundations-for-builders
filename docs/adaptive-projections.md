# Adaptive projections

Status: deferred design note - reviewed 2026-08-05

This note records a possible knowledge-product layer built on Technical Foundations for Builders (TFB). It is not a delivery tracker, a new disclosure tier, a replacement for the 13-chapter outline or authority for changing canonical content. [GitHub Issues](https://github.com/digital-mercenaries-ltd/technical-foundations-for-builders/issues) remains the delivery ledger.

## Position

TFB's Markdown entries remain the canonical explanation of each retained concept. Their links already form an implicit graph; a future projection layer would add explicit, typed relationships and create views over that material. A graph or index is a derived navigation and teaching aid, not a second book written by a recommender.

The system could produce a reading route for a person with a particular background, goal, project and uncertainty. It could also help an assistant explain a topic at an appropriate level, avoiding both assumed knowledge and unnecessary repetition. It does not make a larger, poorly curated first pass acceptable. The first traversal remains bounded and each entry retains its own editorial standard.

## Minimum concept model

Keep Markdown as the source of truth until a concrete limitation justifies more structure. If a derived registry is later justified, the smallest useful model is:

| Field or relationship | Use |
| --- | --- |
| Stable concept identifier and canonical home | Prevent duplicate or competing explanations. |
| Treatment tier and entry type | Distinguish first-pass, further territory, recognition and external material; distinguish mechanism, practice, risk, institution, standard, tool and cultural term. |
| Prerequisite and related-concept links | Build an ordered route while retaining useful lateral browsing. |
| Reader need, risk signal and action cue | Explain why a concept appears in a route. |
| Diátaxis mode | Distinguish explanation, tutorial, how-to and reference material without confusing these with learner personas. |
| Terms, acronyms and glossary links | Adapt explanations and provide local definitions consistently. |
| Sources, currentness and confidence | Preserve provenance and identify material that needs review. |

Do not turn every cross-link into a formal prerequisite. A reader may benefit from knowing that two ideas are related without needing one before they can understand the other.

## Projections and learner model

A projection selects a connected subset of approved material, closes over the necessary prerequisites and orders it for a stated purpose. Initial default projections may serve a domain-experienced AI-assisted builder, a graduate from another discipline or a computer-science graduate whose production experience is limited. Those are starting hypotheses, not fixed tracks or claims about a person's competence.

The learner model should record only what helps the current interaction:

- stated goal, project context and immediate concern;
- claimed familiarity and confidence by concept area;
- concepts already read, discussed or demonstrated in this product;
- preferred explanation level and terminology support; and
- uncertainty, evidence source and last review where that affects a recommendation.

Separate a reader's self-report from observed evidence. A short scenario, optional quiz response or authorised repository inspection can calibrate a route, but none proves professional competence. Do not infer a broad capability from code style, a public profile or one correct answer.

## Routing and teaching

Route selection can begin procedurally. A transparent rule can combine consequence, likelihood, dependency leverage, apparent knowledge gap and actionability to identify likely high-return concepts. It should show the user why a concept was selected and let the user defer, remove or reorder it.

An AI assistant is optional. It can conduct a conversational intake, ask calibration questions, explain a concept using the learner model and propose the next step. It must make uncertainty visible, avoid inventing progress records and preserve canonical terminology. It should introduce unfamiliar terms before using acronyms or specialist shorthand.

Presentation features such as glossary previews, acronym expansion and hover definitions can reduce friction. They are enhancements, not substitutes for clear prose, accessible links or a usable non-JavaScript reading experience.

## Project evidence and safeguards

Repository inspection is optional and requires explicit consent. Request only the scope needed for the stated question, use least privilege, explain what will be examined and avoid treating code inspection as proof of a person's knowledge. Keep progress data minimal, user-visible and correctable. Do not require a repository, quiz or persistent profile to read TFB.

Badges or certification are separate, much later propositions. A valid credential needs a defensible competence standard, assessment design, identity and integrity controls, accessibility arrangements, appeals and governance; an AI conversation or automatically inspected repository is insufficient evidence.

## Decision gates

Reconsider this work only when:

1. enough approved entries expose repeated reader-routing and prerequisite needs;
2. the Markdown link structure makes those needs difficult to answer consistently;
3. a small derived registry can be generated and checked without creating a competing authoring workflow; and
4. a bounded prototype can show that a projection improves discovery or comprehension for real readers.

Start with an inspectable index and deterministic route generator. Add a graph store, conversational assistant, GitHub integration, quizzes or credentials only when the previous layer demonstrates a concrete limitation and the relevant privacy, accessibility and evidence requirements are met.
