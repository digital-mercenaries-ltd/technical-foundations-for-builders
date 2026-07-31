---
title: "Foundational Resources, Laws, Heuristics and Mental Models for Agentic Software Delivery"
subtitle: "A project synthesis for agentic SDLC harnesses, delivery-risk work and Technical Foundations for Builders"
date: 2026-07-31
status: working reference
scope: source-first synthesis of prior project discussions
---

# Foundational Resources, Laws, Heuristics and Mental Models for Agentic Software Delivery

## 1. Purpose and scope

This document consolidates the project discussions about the **underlying intellectual resources** for software development: canonical books, bodies of knowledge, architecture methods, named laws, hacker aphorisms, engineering heuristics and general mental models.

Its primary purpose is to support future work on:

- agentic software-development harnesses;
- standard operating procedures for an agentic SDLC;
- prompts, critic agents, quality gates and evaluation rubrics;
- curricula and reference material for *Technical Foundations for Builders*;
- principles and source material relevant to delivery-risk modelling and writing.

It deliberately does **not** organise itself around TFB or the Delivery Risk Cube. Those are downstream structures that may select, summarise or operationalise this material. The centre of gravity here is the source canon and the reusable knowledge contained in it.

The broader project previously expanded this field into a catalogue of roughly **170 works and 28 descriptive columns**. This document is a condensation of the most foundational and repeatedly discussed material rather than a reproduction of that full catalogue.

## 2. Central conclusion from the discussions

There is no single definitive compendium. The practical canon is a **federation of complementary sources**:

1. broad software-engineering books that teach durable judgement;
2. specialised architecture, delivery, operations, security and testing books;
3. collections of named laws and hacker folklore;
4. formal bodies of knowledge and classification schemes;
5. general reasoning and decision-making frameworks;
6. current, domain-specific supplements that update older classics.

The most useful unit for an agentic harness is therefore not “a book” or “a law” in isolation. It is a structured **principle card** containing:

- the rule or model;
- its source and authority;
- the problem it addresses;
- applicability conditions;
- counter-principles and trade-offs;
- common misuse;
- observable evidence;
- tests or questions an agent can apply;
- examples and failure cases.

A mature harness should retrieve and reconcile several such cards rather than blindly apply a slogan.

---

# Part I — The resource canon

## 3. Resource map at a glance

| Resource family | Main contribution | Typical use in an agentic harness |
|---|---|---|
| Pragmatic software craft | Everyday judgement, feedback, adaptability and maintainability | General implementation and review prompts |
| Refactoring and code quality | Change mechanics, code smells and test-supported improvement | Refactoring agents and maintainability critics |
| Domain and enterprise architecture | Boundaries, models, integration and structural patterns | Architecture synthesis and decomposition |
| Distributed systems and data | Consistency, state, replication, messaging and failure | Distributed-systems critic and data-design reviewer |
| Delivery and operations | Flow, deployment, operability and feedback | CI/CD, release and operational-readiness agents |
| Reliability and NFRs | Resilience, performance, observability and capacity | Quality-attribute scenarios and fitness functions |
| Security | Threats, controls and secure design | Threat-modelling and security gates |
| Bodies of knowledge and methods | Coverage taxonomies, views and standard terminology | Retrieval metadata and completeness checks |
| Hacker laws and folklore | Memorable warnings about recurring failure modes | Lightweight critics and review prompts |
| General mental models | Reasoning under uncertainty and trade-offs | Planning, option generation and decision audit |
| Language/platform supplements | Current idioms and ecosystem-specific practice | Implementation specialists and code review |
| Agent frameworks | Orchestration mechanisms rather than engineering wisdom | Execution layer for roles, dialogue and tools |

## 4. Core software-craft books

### 4.1 *The Pragmatic Programmer* — Andrew Hunt and David Thomas

This was repeatedly identified as one of the closest things to a compact software-development canon. Its value is not a single methodology but a repertoire of adaptable behaviours.

Key concepts to extract:

- **tracer bullets**: build a thin, end-to-end path through the real system to learn whether the components actually connect;
- **prototypes versus tracer bullets**: distinguish disposable learning artefacts from production-oriented skeletal paths;
- **DRY**: avoid duplicated knowledge, not merely duplicated text;
- **orthogonality**: minimise unnecessary coupling so that changes remain local;
- **reversibility**: preserve options where uncertainty is high;
- **broken windows**: visible disorder compounds unless addressed;
- **automation**: make repeatable processes executable;
- **design by contract** and explicit expectations;
- **debugging as problem solving**, not blame;
- **knowledge portfolios** and continual learning;
- **pragmatism over dogma**.

Agentic use:

- require a thin end-to-end implementation before broad feature completion;
- ask where knowledge is duplicated across code, configuration, schemas and documentation;
- identify irreversible decisions and create option-preserving alternatives;
- distinguish a learning prototype from a production seed;
- turn repeated manual actions into scripts, checks or pipeline stages.

### 4.2 *Refactoring* — Martin Fowler

The core contribution is a disciplined vocabulary and method for improving internal structure while preserving observable behaviour.

Key concepts:

- code smells as prompts for investigation, not automatic verdicts;
- small, behaviour-preserving transformations;
- tests as a safety net for change;
- naming, decomposition and responsibility movement;
- replacing conditionals and primitive representations with clearer models;
- incremental migration rather than wholesale rewriting.

Agentic use:

- restrict refactoring agents to small, test-backed transformations;
- require pre- and post-change behavioural evidence;
- separate refactoring from feature addition where practicable;
- make the agent explain the smell, the chosen transformation and the expected design improvement.

### 4.3 *Clean Code* — Robert C. Martin

This remains influential for naming, function design, readability and local code hygiene, but the discussions treated classics as **sources of heuristics rather than scripture**. Some prescriptions are context-dependent and should be balanced against performance, language idiom, team conventions and the cost of excessive fragmentation.

Useful extracts:

- intention-revealing names;
- small, cohesive units;
- explicit error handling;
- tests as first-class code;
- reducing hidden side effects;
- maintaining conceptual consistency.

Agentic use:

- use as one reviewer perspective, not a universal style oracle;
- require language- and repository-specific conventions to override generic stylistic advice;
- evaluate readability at the level of the whole change, not merely function length.

### 4.4 *The Mythical Man-Month* — Frederick P. Brooks Jr.

This contributes enduring observations about coordination, conceptual integrity and the limits of adding labour to late projects.

Key principles:

- **Brooks’s Law**: adding people to a late software project can make it later;
- communication paths and onboarding create non-linear coordination costs;
- conceptual integrity matters more than a pile of individually clever features;
- **No Silver Bullet**: no single technique removes the essential complexity of software;
- distinguish **essential** from **accidental** complexity.

Agentic use:

- do not treat more agents as automatically producing better work;
- minimise unnecessary inter-agent communication and hand-offs;
- appoint a coherent architectural authority or explicit decision mechanism;
- identify whether a proposed tool removes accidental work or merely disguises essential difficulty.

## 5. Architecture and domain-modelling canon

### 5.1 *Domain-Driven Design* — Eric Evans

Key contributions:

- ubiquitous language;
- bounded contexts;
- explicit context maps;
- entities, value objects, aggregates, repositories and domain services;
- strategic design before indiscriminate tactical-pattern use;
- model integrity across organisational and system boundaries.

Agentic use:

- require agents to identify domain terms and ambiguous synonyms;
- separate bounded contexts before generating schemas or services;
- reject shared models that collapse materially different meanings;
- make aggregate boundaries correspond to invariants and transaction needs rather than object convenience.

### 5.2 *Patterns of Enterprise Application Architecture* — Martin Fowler

This provides a vocabulary for transaction scripts, domain models, data mapping, service layers, gateways and distribution boundaries.

Agentic use:

- choose patterns based on domain complexity and transaction behaviour;
- distinguish presentation, domain and data responsibilities;
- avoid importing enterprise patterns where a simpler transaction script is sufficient;
- make distribution an explicit cost rather than a fashionable default.

### 5.3 *Enterprise Integration Patterns* — Gregor Hohpe and Bobby Woolf

Key contributions:

- message channels, routers, translators, filters and endpoints;
- correlation, idempotency and message sequencing;
- canonical data models and their trade-offs;
- competing consumers, dead-letter handling and integration observability.

Agentic use:

- model message semantics before selecting a broker;
- identify delivery guarantees, duplicates, ordering and retry behaviour;
- generate explicit failure paths, poison-message handling and operational diagnostics;
- distinguish integration architecture from internal domain design.

### 5.4 *Fundamentals of Software Architecture* — Mark Richards and Neal Ford

The discussions treated this as a modern bridge between classical architecture and contemporary systems.

Key contributions:

- architecture characteristics and trade-offs;
- coupling and cohesion;
- architectural styles as bundles of constraints, not product categories;
- architecture decisions and governance;
- the architect’s role in continuous analysis rather than up-front omniscience.

### 5.5 *Building Evolutionary Architectures* — Neal Ford, Rebecca Parsons and Patrick Kua

Key contribution: architecture should evolve under **fitness functions** that make desired characteristics testable.

Agentic use:

- convert architectural intentions into executable checks;
- monitor coupling, dependency direction, latency, security and operability continuously;
- prefer controlled evolutionary paths to speculative future-proofing.

### 5.6 *Clean Architecture* — Robert C. Martin

Useful ideas include dependency direction, separation of policy from detail and keeping core business rules insulated from volatile delivery mechanisms. These should be applied proportionately; excessive layering can create ceremony and indirection.

### 5.7 Design patterns and pattern languages

The project cited the Gang of Four’s *Design Patterns* and broader pattern-based resources as vocabularies for recurring structures.

Harness rule:

> Retrieve a pattern only after the problem and forces are identified. Never select a pattern from its name alone.

Agents should state:

- the recurring problem;
- the forces and constraints;
- the selected pattern;
- simpler alternatives;
- consequences and likely misuse.

### 5.8 C4 model

The C4 model supplies a pragmatic visual hierarchy:

- system context;
- containers;
- components;
- code, when useful.

Its deeper principle is **audience-appropriate zoom**, not compulsory production of four diagrams. For many teams, context and container views carry most of the value.

Agentic use:

- generate views for a declared audience and question;
- keep element names and relationships consistent across zoom levels;
- link diagrams to repository and deployment evidence;
- distinguish logical containers from infrastructure products.

### 5.9 TOGAF and architecture frameworks

TOGAF contributes process, stakeholder, capability and governance coverage. It is useful as a completeness and organisational-alignment reference, but should not force heavyweight ceremony onto small or exploratory products.

Agentic use:

- retrieve only the relevant viewpoints, artefacts and governance questions;
- tailor process depth to decision cost, regulation and organisational scale;
- avoid generating documents merely because a framework names them.

## 6. Distributed systems, data and microservices

### 6.1 *Designing Data-Intensive Applications* — Martin Kleppmann

This was consistently treated as a central modern resource.

Key contributions:

- data models and query languages;
- storage engines and indexing;
- replication and partitioning;
- transactions and isolation;
- consistency, consensus and distributed failure;
- batch and stream processing;
- derived data and event logs;
- trade-offs rather than vendor recipes.

Agentic use:

- make data ownership, consistency and failure semantics explicit;
- evaluate access patterns before choosing storage technology;
- ask what happens under partitions, retries, concurrent writes and replay;
- separate logical requirements from database marketing categories.

### 6.2 *Building Microservices* — Sam Newman

Useful contributions:

- service boundaries and independent deployability;
- organisational ownership;
- evolutionary decomposition;
- observability, testing and deployment consequences;
- the operational cost of distribution.

Core project stance:

> Microservices are justified by demonstrated needs in scale, ownership, deployment independence, resilience or regulation—not by modernity alone.

A modular monolith is often the safer initial form for an MVP or small team. An agent proposing services should provide evidence that the distribution cost is warranted.

### 6.3 Distributed-systems laws and impossibility results

The project repeatedly identified the following as mandatory background:

- **CAP theorem**;
- the **fallacies of distributed computing**;
- the **Two Generals Problem**;
- the **Byzantine Generals Problem**;
- the **end-to-end principle**;
- consistency and coordination trade-offs;
- the impossibility of assuming exactly-once effects merely because a transport claims exactly-once delivery.

These should function as design critics, not trivia questions.

Typical agent prompts:

- Which network or process failure is being assumed away?
- Where can a duplicate, delayed, reordered or missing message occur?
- Which invariant requires coordination?
- What does the system do when a dependency is slow rather than dead?
- Which end-to-end property cannot be guaranteed by an intermediate layer alone?

## 7. Delivery, DevOps and operational practice

### 7.1 *Continuous Delivery* — Jez Humble and David Farley

Key contributions:

- deployment pipelines;
- build, test and deployment automation;
- keeping software in a releasable state;
- small changes and rapid feedback;
- configuration and environment management;
- progressive confidence through pipeline stages;
- decoupling deployment from release where possible.

The discussions noted that some classic examples predate today’s cloud-native defaults, but the principles remain durable. Modern supplements should update implementation details such as trunk-based development, ephemeral environments, infrastructure as code, supply-chain security and platform engineering.

### 7.2 *Accelerate* — Nicole Forsgren, Jez Humble and Gene Kim

Key contributions:

- empirical connection between delivery capability and organisational performance;
- lead time, deployment frequency, change-failure rate and recovery time as system-level indicators;
- small batches, automation, loosely coupled architecture and learning culture.

Agentic use:

- optimise the delivery system rather than individual coding speed;
- detect local automation that worsens queueing or failure rates elsewhere;
- report flow and outcome measures, not generated lines of code or agent activity.

### 7.3 *The Phoenix Project* — Gene Kim, Kevin Behr and George Spafford

Its chief value is an accessible systems view of flow, constraints, work in progress, unplanned work and the relationship between development and operations.

### 7.4 Google’s *Site Reliability Engineering* resources

Key contributions:

- service-level indicators and objectives;
- error budgets;
- toil reduction;
- monitoring and alerting based on user impact;
- capacity planning;
- incident response and blameless learning;
- balancing reliability with delivery velocity.

Agentic use:

- convert “highly available” into measurable service-level objectives;
- reject alerts without a clear operator action or user consequence;
- distinguish automation that removes toil from automation that conceals instability;
- use error budgets to make reliability-versus-change decisions explicit.

### 7.5 The Twelve-Factor App

The twelve-factor principles remain a compact checklist for deployable services: configuration separation, backing services, stateless processes, disposability, environment parity and logs as event streams. They are not a complete architecture or security standard.

### 7.6 *Release It!* — Michael T. Nygard

This is a core source for production failure and stability patterns.

Key concepts:

- timeouts;
- circuit breakers;
- bulkheads;
- fail-fast behaviour;
- load shedding;
- back pressure;
- cascading failure;
- integration points as risk concentrations;
- production diagnostics and operational visibility.

Agentic use:

- generate explicit slow, partial and overloaded failure scenarios;
- require bounded retries with jitter and budgets;
- inspect resource pools and shared dependencies for blast radius;
- treat operability as part of design, not an afterthought.

## 8. Testing, quality and NFR resources

### 8.1 *xUnit Test Patterns* — Gerard Meszaros

Useful contributions:

- test smells;
- fixture design;
- test doubles and their appropriate use;
- isolation, determinism and maintainability;
- diagnosis of fragile or obscure tests.

Agentic use:

- prevent test-generation agents from maximising test count;
- assess whether tests detect meaningful regressions;
- identify over-mocking, shared fixtures and assertions without clear intent;
- prefer tests aligned to risk and behaviour.

### 8.2 Performance engineering resources

The project cited *Designing for Performance* and broader performance practice. Core principles include:

- measure before optimising;
- define workload and latency distributions;
- distinguish throughput, latency, utilisation and concurrency;
- examine tail latency rather than averages alone;
- test representative data volumes and failure states;
- optimise the bottleneck, not the most visible code.

### 8.3 Security resources

Repeatedly identified foundations include:

- threat-modelling literature;
- OWASP guidance;
- API-security resources;
- *API Security in Action*;
- *OAuth 2 in Action* for IAM-heavy teams.

Agentic use:

- identify assets, actors, trust boundaries, threats and mitigations before generating controls;
- distinguish authentication, authorisation, delegation and identity proofing;
- apply least privilege and secure defaults;
- test abuse cases and privilege escalation, not merely happy-path access;
- treat secrets, logging, dependency risk and software supply chain as first-class concerns.

### 8.4 NFRs as continuous design inputs

A recurring project conclusion was that non-functional requirements must not be left as a late hardening phase. Reliability, security, performance, privacy, accessibility, supportability and operability influence architecture from the beginning.

An agent should translate each important quality attribute into a **scenario**:

- source of stimulus;
- stimulus;
- environment;
- affected artefact;
- desired response;
- measurable response criterion.

This converts vague adjectives into testable design obligations.

## 9. Modern Java and language-specific updating

The project noted that many classics are based on older Java and enterprise conventions. Their conceptual content often remains useful, but language idiom and platform practice require modern supplements.

Resources discussed included:

- *Modern Java in Action*;
- *Practical Modern Java*;
- Java 17-focused handbooks;
- Oracle’s language and release documentation;
- Baeldung’s Java 17 and 21 coverage;
- current material on records, sealed classes, pattern matching, switch expressions, text blocks, virtual threads and modern concurrency.

The important harness principle is broader than Java:

> Separate timeless design guidance from version-sensitive implementation advice.

Every language specialist should receive:

- the repository’s actual compiler/runtime version;
- framework and dependency versions;
- supported deployment environment;
- team conventions;
- compatibility constraints;
- current official documentation where syntax or behaviour may have changed.

## 10. Web compendia and reference collections

### 10.1 Hacker Laws

The `dwmkerr/hacker-laws` repository was repeatedly identified as the closest readily usable index of named software-development laws. Its own warning is important: it explains laws and patterns but does not claim they are universally correct. Application depends on context.

Use it as:

- an index and vocabulary;
- a source of candidate critic rules;
- a starting point for primary-source verification;
- a source of memorable review prompts.

Do not use it as:

- an unqualified rule engine;
- a substitute for source context;
- proof that an aphorism applies to a particular system.

Resource: <https://github.com/dwmkerr/hacker-laws>

### 10.2 The Jargon File

The Jargon File preserves hacker culture, terminology, humour and historical heuristics. Its value is partly conceptual: it exposes recurring ways programmers describe complexity, abstraction, cleverness, failure and culture.

Resource: <https://catb.org/~esr/jargon/html/index.html>

### 10.3 Wikipedia lists and primary sources

Wikipedia’s lists of programming principles, software-development philosophies, cognitive biases and named laws are useful for **discovery**, but each important item should be linked to a primary source or authoritative treatment before being encoded as a high-confidence rule.

### 10.4 Farnam Street and mental-model collections

Mental-model compendia are useful indexes for cross-domain reasoning: inversion, second-order effects, incentives, bottlenecks, feedback loops, compounding, opportunity cost and map–territory distinctions. They should be paired with more rigorous sources where decisions are consequential.

### 10.5 SWEBOK

The IEEE Computer Society’s Software Engineering Body of Knowledge supplies a formal coverage map. Version 4 organises the discipline into 18 knowledge areas and explicitly includes architecture, operations and security.

Resource: <https://www.computer.org/education/bodies-of-knowledge/software-engineering>

SWEBOK is particularly useful for:

- checking whether a curriculum or knowledge base has major omissions;
- tagging resources by software-engineering domain;
- separating foundational knowledge from particular methodologies;
- creating coverage metrics for an agentic corpus.

### 10.6 C4 model

Resource: <https://c4model.com/>

### 10.7 OWASP

Resource: <https://owasp.org/>

### 10.8 Twelve-Factor App

Resource: <https://12factor.net/>

---

# Part II — Laws, aphorisms, heuristics and mental models

## 11. A three-layer taxonomy

A useful taxonomy from the project discussions separates three forms of compressed knowledge.

### Layer A — Aphorisms and slogans

Examples:

- YAGNI;
- KISS;
- DRY;
- WET;
- TIMTOWTDI/TMTOWTDI — “There is more than one way to do it”;
- fail fast;
- make invalid states unrepresentable;
- convention over configuration.

These are memorable and operationally useful, but usually underspecified. They need context and counterweights.

### Layer B — Named laws, principles and impossibility results

Examples:

- Conway’s Law;
- Brooks’s Law;
- CAP theorem;
- Amdahl’s Law;
- Gustafson’s Law;
- Little’s Law;
- Gall’s Law;
- Postel’s Law;
- Greenspun’s Tenth Rule;
- the end-to-end principle;
- the fallacies of distributed computing.

These tend to have clearer claims or source contexts, though their popular paraphrases can still be distorted.

### Layer C — General reasoning tools and mental models

Examples:

- Occam’s razor;
- inversion;
- first-principles reasoning;
- map versus territory;
- feedback loops;
- bottlenecks and constraints;
- incentives;
- opportunity cost;
- second-order effects;
- Pareto distributions;
- Bayesian updating;
- calibration and forecasting;
- reversible versus irreversible decisions.

These are not software-specific, but they often govern the quality of architectural and delivery decisions more than any individual pattern.

## 12. Simplicity, scope and duplication

### 12.1 KISS

Prefer the simplest design that satisfies the actual constraints. “Simple” should be evaluated across the whole lifecycle, not merely by line count or the speed of initial coding.

Agent questions:

- What complexity is essential to the problem?
- Which complexity is introduced by the chosen solution?
- Is the solution simpler for users, developers and operators, or only for its author?
- What is the simplest design that preserves the required future change path?

### 12.2 YAGNI

Do not build speculative capability without evidence that it is required. YAGNI protects against opportunity cost, untested abstractions and future-proofing based on imagined requirements.

Counterweight:

- some irreversible or expensive-to-retrofit qualities must be designed early;
- security, data ownership, regulatory constraints and critical operability cannot always be deferred;
- option-preserving seams may be warranted even when full capability is not.

### 12.3 DRY

DRY concerns duplication of **knowledge**. Two similar code fragments may encode different concepts and should remain separate; one business rule copied into several services is a more serious violation even if the code differs.

Counterweights:

- premature abstraction;
- inappropriate coupling between concepts that merely look similar;
- the Rule of Three or evidence-based consolidation;
- local duplication may be cheaper than a shared dependency.

### 12.4 WET and deliberate duplication

“Write Everything Twice” is a useful counterweight to premature DRY. Delay abstraction until the stable commonality is visible.

### 12.5 TIMTOWTDI

Larry Wall’s Perl maxim, “There is more than one way to do it”, is a reminder that design spaces contain alternatives and that local context matters.

Counterweight:

- too many equally sanctioned ways increase cognitive load and inconsistency;
- a team or platform often benefits from a paved road even when alternatives remain technically possible.

### 12.6 The framework/library heuristic

A recurring observation from the project:

> Libraries and frameworks make the easy things easier; they do not make the intrinsically hard things disappear.

They can remove boilerplate and standardise routine work, but domain ambiguity, distributed consistency, security boundaries, operability and organisational coordination remain. An agent should identify which difficulty is genuinely removed and which is merely hidden behind an abstraction.

## 13. Abstraction, models and architecture

### 13.1 All abstractions leak

An abstraction hides detail only until performance, failure, security or unusual behaviour crosses its boundary.

Agent questions:

- Which hidden implementation details can affect correctness or operations?
- What escape hatch exists when the abstraction fails?
- Is the team capable of diagnosing below the abstraction?

### 13.2 All models are wrong; some are useful

A model is an intentional simplification. Its fitness depends on the decision it supports.

Agent questions:

- What is this model for?
- What does it omit?
- At what scale or condition does it fail?
- Is the audience likely to mistake it for the implementation?

### 13.3 Gall’s Law

A complex system that works is usually found to have evolved from a simple system that worked. Attempts to design a working complex system from scratch are unlikely to succeed.

Operational consequence:

- establish a working skeleton;
- add complexity through observed need;
- preserve the ability to test the system at each stage.

### 13.4 Greenspun’s Tenth Rule

Any sufficiently complicated non-Lisp program tends to contain an ad hoc, informally specified, bug-ridden, slow implementation of part of Lisp.

The deeper warning is that systems often accrete hidden interpreters, rule languages and meta-programming facilities. When a product begins to create its own configuration language, workflow engine or expression evaluator, treat it as a language-design problem with corresponding security, tooling and semantics costs.

### 13.5 Conway’s Law

System communication structures tend to mirror organisational communication structures.

Agentic implications:

- proposed boundaries must be feasible for the owning organisation;
- cross-team dependencies are architectural dependencies;
- an “inverse Conway manoeuvre” can reorganise teams to encourage desired boundaries, but the organisational change is real work;
- adding specialist agents can reproduce the same silo and hand-off problems as human organisations.

### 13.6 Conceptual integrity

A coherent system should feel as though it follows a small number of consistent design ideas. This is threatened by uncontrolled multi-agent generation.

Harness controls:

- a declared architecture and vocabulary;
- decision records;
- ownership of cross-cutting conventions;
- repository-wide checks;
- a final integrator or architecture critic with authority to reject inconsistency.

### 13.7 Postel’s Law, applied cautiously

“Be conservative in what you send, liberal in what you accept” encouraged interoperability, but permissive input handling can create ambiguity, security risk and long-lived compatibility burdens.

Modern counter-principle:

- be explicit, validate inputs, fail clearly and version contracts deliberately;
- tolerate only variations that are safe and semantically unambiguous.

## 14. Change, evolution and reversibility

### 14.1 Reversible and irreversible decisions

Not all decisions deserve equal analysis. Reversible, low-cost decisions should be made quickly and tested. Irreversible, expensive or externally binding decisions require stronger evidence and review.

Potentially high-commitment choices include:

- externally published APIs;
- irreversible data migrations;
- identity and tenancy models;
- regulatory representations;
- strategic vendor lock-in;
- public security guarantees;
- organisational ownership boundaries.

### 14.2 Evolutionary architecture

Prefer designs that can be changed safely under observable constraints. Evolution is not the absence of architecture; it requires:

- modular boundaries;
- migration paths;
- compatibility strategy;
- automated fitness functions;
- feedback from production;
- explicit deprecation and retirement.

### 14.3 Chesterton’s Fence

Do not remove a structure until its purpose is understood. In code and architecture, apparently redundant checks, fields or processes may encode historical failure knowledge.

Agent requirement:

- inspect history, tests, incidents and dependent consumers before deletion;
- state the hypothesised original purpose and the evidence that it no longer applies.

## 15. Distributed-systems reasoning

### 15.1 The fallacies of distributed computing

Never assume that:

- the network is reliable;
- latency is zero;
- bandwidth is infinite;
- the network is secure;
- topology does not change;
- there is one administrator;
- transport cost is zero;
- the network is homogeneous.

A distributed-systems agent should explicitly test every design against these assumptions.

### 15.2 CAP theorem

During a network partition, a distributed data system cannot simultaneously guarantee both linearizable consistency and availability for every request. CAP is not a general instruction to choose two of three at all times; its practical use is to force precise discussion of behaviour under partition.

### 15.3 Two Generals and Byzantine Generals

These problems demonstrate limits on agreement under unreliable communication and, in the Byzantine case, potentially faulty or malicious participants. Their purpose in a harness is to prevent vague promises of perfect coordination.

### 15.4 End-to-end principle

Some properties—correct delivery, security, integrity or transaction outcome—can only be fully established at the endpoints that understand the application semantics. Intermediate layers may help but cannot replace end-to-end verification.

### 15.5 Idempotency, retries and uncertainty

Retries convert transient failure into possible duplication. Every automated workflow should define:

- an idempotency key or deduplication strategy;
- retryable versus terminal errors;
- maximum attempts and time budgets;
- backoff and jitter;
- compensation or reconciliation;
- observable final state.

### 15.6 Little’s Law

For a stable system, average work in progress equals arrival rate multiplied by average time in the system. This connects queues, WIP and lead time.

Delivery implication:

- increasing parallel work without increasing completion capacity lengthens queues and feedback;
- agentic systems should limit concurrent branches and unfinished changes.

### 15.7 Amdahl’s and Gustafson’s laws

Amdahl’s Law limits speed-up when part of the workload remains serial. Gustafson’s Law shows how larger problem sizes can use parallel capacity effectively.

Agentic implication:

- identify serial review, integration, test and decision bottlenecks before adding parallel agents;
- do not optimise the parallelisable generation phase while ignoring a fixed validation bottleneck.

## 16. Delivery, flow and feedback

### 16.1 Tracer bullets and walking skeletons

Both seek an early end-to-end path through the actual system. Their value is integrated learning:

- real interfaces;
- deployment path;
- data flow;
- observability;
- basic user interaction;
- feedback on architectural assumptions.

A feature-complete component that is not integrated gives weaker delivery evidence than a thin vertical slice.

### 16.2 Small batches

Small changes reduce uncertainty, simplify review, shorten feedback and limit blast radius. The harness should:

- cap change size;
- decompose work into independently verifiable slices;
- integrate frequently;
- avoid long-lived speculative branches.

### 16.3 Feedback loops

Every stage should produce evidence for the next decision. Important loops include:

- tests and static analysis during coding;
- preview environments and user feedback;
- telemetry and production behaviour;
- incidents and post-incident learning;
- architecture fitness functions;
- delivery-performance measures.

### 16.4 Bottlenecks and the Theory of Constraints

Improving a non-bottleneck may not improve throughput. In an agentic SDLC, generation can become abundant while clarification, test execution, review, integration or deployment remains scarce.

Agent question:

> What currently limits completed, validated value—not merely activity?

### 16.5 Brooks’s Law for agents

Parallel agents add coordination costs, duplicated exploration, merge conflicts and inconsistent assumptions. Use multiple agents when work can be partitioned with clear contracts or when independent critique is valuable. Do not create an agent organisation merely to imitate a human org chart.

### 16.6 Goodhart’s Law

When a measure becomes a target, it ceases to be a good measure. Dangerous agentic targets include:

- lines of code;
- test count;
- issue throughput;
- token use;
- number of generated alternatives;
- percentage “coverage” without mutation or behavioural quality;
- nominal compliance artefacts.

Prefer balanced outcome measures and periodic metric review.

## 17. Reliability and operational heuristics

### 17.1 Everything fails

Design for components to fail independently, partially and slowly. A binary up/down model is inadequate.

### 17.2 Timeout every remote call

Unbounded waiting consumes resources and turns local degradation into system-wide failure.

### 17.3 Retries need budgets

Retries can amplify load and create retry storms. They require bounded attempts, backoff, jitter and end-to-end time budgets.

### 17.4 Bulkheads and blast-radius control

Separate resource pools, tenants, queues or workloads so that one failure cannot exhaust the whole system.

### 17.5 Circuit breakers and load shedding

Stop sending work to a failing dependency and reject excess demand before the system collapses. Recovery behaviour must be observable and tested.

### 17.6 SLOs and error budgets

Reliability should be expressed as a user-relevant target. The error budget makes the permissible unreliability explicit and provides a decision mechanism for balancing release velocity against stability work.

### 17.7 Observability is a design property

Logs, metrics and traces are not automatically useful. The system should expose enough state to answer operational questions, correlate requests and diagnose failure without reproducing it locally.

## 18. Security and trust heuristics

### 18.1 Least privilege

Every human, service and agent should possess only the permissions needed for its current task and duration.

### 18.2 Complete mediation

Every access to a protected resource should be checked; do not rely on an earlier check remaining valid across context changes.

### 18.3 Secure defaults

The safe state should require less effort than the unsafe state. Optional security controls are often omitted.

### 18.4 Defence in depth

Independent controls reduce reliance on a single perfect mechanism. However, layers should address distinct failure modes rather than duplicate ceremony.

### 18.5 Trust boundaries and confused deputies

Agents that act with tools and credentials can become confused deputies. The harness must preserve:

- user intent;
- resource scope;
- identity of the caller;
- provenance of instructions;
- separation between untrusted content and executable commands;
- explicit approval for high-impact actions.

### 18.6 Assume breach and minimise blast radius

Agent sandboxes, ephemeral credentials, scoped tokens, isolated environments and auditable actions are practical applications.

## 19. General mental models for engineering judgement

### 19.1 Occam’s razor

Prefer the explanation or design that introduces the fewest unsupported assumptions, not merely the fewest components.

### 19.2 Inversion

Instead of asking only how to succeed, ask:

- How would this system fail?
- How would we make the delivery late?
- How could data be corrupted?
- How could an attacker abuse this flow?
- What would make the design impossible to change?

Then remove or control those conditions.

### 19.3 First-principles reasoning

Decompose the problem into constraints and mechanisms rather than copying a fashionable reference architecture. This is particularly important where scale, team size or regulation differs from the source example.

### 19.4 Map and territory

Requirements, diagrams, schemas, tests and metrics are representations. None is the running socio-technical system. Cross-check multiple representations against production evidence.

### 19.5 Second-order effects

Ask what happens after the immediate result:

- Will automation increase incoming demand?
- Will a shared platform become a queue?
- Will permissive compatibility create permanent support obligations?
- Will a local optimisation shift cost to operations or users?

### 19.6 Incentives

Teams and agents optimise what is rewarded and measured. Align success criteria with validated user and system outcomes.

### 19.7 Pareto principle

A small subset of defects, dependencies, workflows or customers often drives a large share of impact. Use evidence to focus attention, but do not assume the exact 80/20 ratio.

### 19.8 Bayesian updating and calibration

Treat architectural beliefs as hypotheses with confidence levels. Update them when tests, user research, incidents or performance measurements arrive.

### 19.9 Cynefin

Classify the decision context:

- **clear**: apply established practice;
- **complicated**: analyse with expertise;
- **complex**: probe safely, observe and adapt;
- **chaotic**: stabilise first;
- **confused/disordered**: decompose or gather context.

Agentic consequence:

- do not use the same planning and validation pattern for every problem;
- complex product or architecture questions need safe experiments rather than false certainty.

### 19.10 Superforecasting principles

Useful habits include decomposition, base rates, explicit probabilities, updating and post-hoc calibration. An architecture agent should distinguish confidence from rhetorical fluency.

## 20. Approximation, creativity and fitness for purpose

A distinctive thread in the project began with famous implementation hacks such as fast inverse square root. The important lesson was not the clever bit manipulation itself. It was the developer’s judgement that an **approximation was sufficient for the actual use case**.

This leads to a general principle:

> Correctness is multidimensional and should be calibrated to the problem, provided non-negotiable safety and integrity constraints are preserved.

An agent should determine:

- required numerical accuracy;
- acceptable probability of error;
- latency and throughput limits;
- hardware and runtime characteristics;
- energy, memory and cost budgets;
- language and compiler behaviour;
- reversibility and detectability of error;
- user consequences;
- regulatory or safety constraints;
- whether approximation error compounds downstream.

This is not permission for careless answers. It is a demand to optimise against the **real objective function** rather than an assumed ideal of maximum precision.

### 20.1 Runtime-aware creativity

Creative implementation depends on awareness of the environment:

- CPU, GPU and vector capabilities;
- memory hierarchy and cache behaviour;
- operating system and runtime;
- language semantics and compiler optimisations;
- available libraries and platform primitives;
- deployment topology;
- data distributions;
- expected scale and workload shape.

A harness seeking inventive solutions must expose these facts to the proposing agents and require validation on the real target environment.

### 20.2 Flexible correctness dimensions

A useful checklist:

| Dimension | Question |
|---|---|
| Functional | Does it produce the required outcome? |
| Numerical | How precise and stable must the result be? |
| Temporal | Must it be correct immediately, eventually or by a deadline? |
| Consistency | Which observers must agree, and when? |
| Availability | What degraded behaviour is acceptable? |
| Safety | What errors are intolerable? |
| Security | What attacker capabilities must be resisted? |
| UX | What imperfection is perceptible or harmful to users? |
| Operational | Can errors be detected, diagnosed and repaired? |
| Economic | Is extra precision worth its compute, delivery and maintenance cost? |

---

# Part III — Turning the canon into an agentic SDLC harness

## 21. Principles are not commandments

The harness should never retrieve a slogan and mechanically enforce it. Most useful principles have a counter-principle:

| Principle | Counterweight or tension |
|---|---|
| DRY | Avoid premature abstraction; tolerate local duplication |
| YAGNI | Preserve options for expensive or irreversible change |
| KISS | Do not externalise complexity onto users or operators |
| Postel’s Law | Strict validation and secure, versioned contracts |
| Decoupling | Excess indirection and distributed complexity |
| Reuse | Coupling, ownership and release coordination |
| Microservices | Modular monolith and operational simplicity |
| Fail fast | Graceful degradation and recovery |
| Automation | Human judgement for ambiguous or high-impact decisions |
| Standardisation | Local optimisation and domain-specific variation |
| Consistency | Availability, latency and autonomy |
| Up-front design | Evolution, experimentation and feedback |
| Speed | Safety, maintainability and operational risk |

The agent’s task is to expose and resolve the tension, not quote whichever slogan supports its first proposal.

## 22. Recommended knowledge representation

Each resource should be decomposed into structured records rather than embedded only as prose chunks.

### 22.1 Principle-card schema

```yaml
id: conways-law
name: Conway's Law
kind: named-law
summary: System structures tend to mirror organisational communication structures.
source:
  primary: "Melvin Conway, 1968"
  secondary: []
problem_addressed:
  - organisational and architectural misalignment
applicability:
  - multi-team systems
  - platform and service boundaries
preconditions:
  - meaningful organisational ownership boundaries
questions:
  - Who owns each component end to end?
  - Which cross-team communications become runtime dependencies?
risks_of_misuse:
  - treating current organisation as immutable
  - forcing one service per team without domain justification
counter_principles:
  - cohesive domain boundaries
  - small-system simplicity
observable_evidence:
  - ownership map
  - dependency graph
  - deployment coordination data
agent_roles:
  - architecture-critic
  - operating-model-critic
confidence: high
```

### 22.2 Resource-card schema

```yaml
id: designing-data-intensive-applications
resource_type: book
title: Designing Data-Intensive Applications
author: Martin Kleppmann
canonicality: foundational-modern
freshness_policy: supplement vendor and implementation details with current documentation
coverage:
  swebok_areas:
    - software-architecture
    - software-design
    - software-engineering-operations
  lifecycle:
    - architecture
    - implementation
    - operations
  concerns:
    - data-models
    - replication
    - partitioning
    - transactions
    - streams
activation:
  use_when:
    - selecting data architecture
    - designing distributed state
  agent_roles:
    - data-architect
    - distributed-systems-critic
```

## 23. Classification dimensions from the prior canon work

The previous catalogue work sought to align columns with established bodies rather than invent arbitrary labels. The following dimensions should be retained.

### 23.1 Domain and lifecycle coverage

Use SWEBOK or a compatible software-engineering taxonomy to classify:

- requirements;
- architecture;
- design;
- construction;
- testing;
- maintenance;
- configuration management;
- engineering management;
- process;
- models and methods;
- quality;
- professional practice;
- economics;
- computing and mathematical foundations;
- operations;
- security.

### 23.2 Cognitive demand — Bloom’s taxonomy

Tag whether a resource or task asks an agent or learner to:

- remember;
- understand;
- apply;
- analyse;
- evaluate;
- create.

This prevents a corpus from confusing recognition of a principle with competent application.

### 23.3 Decision context — Cynefin

Tag the contexts in which the guidance is most useful: clear, complicated, complex or chaotic.

### 23.4 Perspective and interrogatives — Zachman-style dimensions

Useful tags include:

- what: data and things;
- how: functions and processes;
- where: locations and topology;
- who: actors and ownership;
- when: events, timing and lifecycle;
- why: goals, rules and motivation.

The value is completeness of viewpoints, not mandatory production of a full Zachman matrix.

### 23.5 Representation strategy

Examples:

- narrative explanation;
- principle card;
- checklist;
- pattern;
- anti-pattern;
- worked example;
- case study;
- diagram;
- decision table;
- executable test;
- metric or fitness function.

### 23.6 Activation style

How should the knowledge be used?

- always-on guardrail;
- triggered retrieval;
- planning prompt;
- design-generation aid;
- critic or red-team rule;
- deterministic validation;
- post-incident diagnostic;
- teaching material;
- escalation criterion.

### 23.7 Agentic role

Examples:

- requirements analyst;
- product-risk critic;
- architecture synthesiser;
- simplicity critic;
- domain modeller;
- data architect;
- distributed-systems critic;
- security reviewer;
- privacy reviewer;
- test strategist;
- reliability engineer;
- performance engineer;
- delivery-flow reviewer;
- operational-readiness reviewer;
- evidence auditor;
- integrator/editor.

### 23.8 Additional high-value columns

The project’s goals imply several further dimensions:

- authority: primary, canonical secondary, practitioner synthesis or folklore;
- timelessness versus version sensitivity;
- prerequisites;
- scale range;
- team/organisation assumptions;
- regulated or safety-critical relevance;
- reversibility of the decision affected;
- cost of error;
- evidence type;
- counter-principles;
- known controversies;
- suitable deterministic checks;
- required human approval;
- source licence and ingestion rights.

## 24. Agent-role pattern

A strong harness separates proposal, criticism and validation.

### 24.1 Context and intent agent

Produces:

- business outcome;
- users and stakeholders;
- constraints;
- assumptions;
- missing evidence;
- decision horizon;
- reversibility and cost of error.

### 24.2 Architecture synthesiser

Produces one recommended design, alternatives considered, boundaries, data ownership, interfaces, deployment view and key decisions.

### 24.3 Simplicity and scope critic

Applies KISS, YAGNI, DRY/WET, Gall’s Law and essential-versus-accidental complexity.

### 24.4 Distributed-systems critic

Applies network fallacies, CAP, retries, idempotency, ordering, consistency and partial-failure scenarios.

### 24.5 NFR critics

Separate specialists may review:

- security and privacy;
- reliability and recoverability;
- performance and capacity;
- operability and observability;
- accessibility;
- maintainability and evolvability.

### 24.6 Delivery and flow critic

Examines slice size, integration path, deployment pipeline, WIP, feedback latency, release strategy and rollback.

### 24.7 Evidence auditor

Checks that claims are supported by:

- requirements;
- repository evidence;
- tests;
- measurements;
- authoritative documentation;
- explicit assumptions.

### 24.8 Integrator

Resolves conflicts, preserves conceptual integrity and produces a coherent decision record. It must not merely concatenate agent outputs.

## 25. Standard reasoning loop for an agentic SDLC task

1. **State the outcome.** What user or business result is required?
2. **Establish context.** Product stage, team, existing system, runtime, constraints and NFRs.
3. **Classify uncertainty.** Clear, complicated, complex or chaotic; reversible or irreversible.
4. **Retrieve relevant principles.** Include counter-principles and source context.
5. **Generate a small option set.** Include the simplest viable option and at least one materially different alternative where the decision warrants it.
6. **Evaluate trade-offs.** Functional fit, delivery risk, NFRs, organisational fit, cost and future change.
7. **Select one recommendation.** Avoid unranked catalogues.
8. **Design an evidence path.** Tracer bullet, prototype, benchmark, threat model, test or operational experiment.
9. **Implement in small batches.** Keep the system integrated and releasable.
10. **Run deterministic checks.** Tests, static analysis, policy, schema and architecture fitness functions.
11. **Run independent critics.** Critics must cite concrete evidence and cannot approve their own work.
12. **Record the decision.** Context, options, rationale, consequences, assumptions and review trigger.
13. **Observe outcomes.** Production telemetry, user feedback and delivery measures.
14. **Update beliefs and rules.** Refine prompts, examples, fitness functions and principle applicability.

## 26. Prompt pattern for applying principles

```text
Outcome
- State the user and business result.

Context
- Product stage, current architecture, team, runtime, data, integrations and constraints.

Decision
- State the exact decision to be made and its reversibility.

Relevant principles
- Retrieve 3–7 applicable principles and at least one counter-principle for each major tension.

Options
- Produce a small set of materially different options, including the simplest viable one.

Evaluation
- Compare the options against functional fit, delivery risk, quality attributes, organisational fit, operational burden and cost.

Evidence
- Distinguish facts, measurements, assumptions and predictions. State confidence.

Validation
- Define the cheapest test that could falsify the recommendation.

Recommendation
- Choose one option and state why. Record consequences and a review trigger.
```

## 27. Deterministic checks before LLM judgement

Where possible, replace subjective review with executable evidence:

- compilation and type checking;
- unit, integration, contract and end-to-end tests;
- schema compatibility;
- dependency and vulnerability scanning;
- secrets detection;
- licence policy;
- formatting and static analysis;
- architecture dependency rules;
- performance budgets;
- accessibility checks;
- infrastructure policy;
- deployment and rollback verification;
- SLO and alert validation;
- migration rehearsal;
- generated artefact consistency.

LLM review is best used for ambiguity, semantics, trade-offs, missing cases and cross-artifact coherence. It should not substitute for a test the system can run.

## 28. Failure modes of principle-driven agents

### 28.1 Slogan matching

The agent spots “duplication” and invokes DRY without understanding domain meaning.

Control: require problem, applicability, counter-principle and evidence fields.

### 28.2 Cargo-cult architecture

The agent selects microservices, event sourcing, Kubernetes or a pattern because the source material treats it prominently.

Control: require scale, ownership, release, resilience or regulatory justification and compare with a simpler architecture.

### 28.3 Authority laundering

A folklore rule is presented as a theorem, or a book’s opinion as a standard.

Control: tag authority and primary-source provenance.

### 28.4 Stale implementation advice

A durable principle is bundled with obsolete language, cloud or framework guidance.

Control: separate timeless principle records from version-sensitive implementation records and retrieve current official documentation.

### 28.5 Excessive agent society

Many roles create duplicated analysis and integration overhead.

Control: add a role only when it contributes distinct evidence, capability or independent challenge.

### 28.6 Self-review illusion

The same model proposes, critiques and approves a change using the same assumptions.

Control: independent prompts/context, deterministic evidence and human approval for consequential actions.

### 28.7 Documentation theatre

Agents produce comprehensive-looking artefacts without validating the running system.

Control: link claims to code, tests, deployments, telemetry and user evidence.

### 28.8 Metric gaming

The harness optimises issue throughput, test count or agent activity.

Control: measure completed, validated outcomes and review metrics under Goodhart’s Law.

### 28.9 Excessive orthodoxy

The harness suppresses creative approximations or context-specific solutions.

Control: include an alternative-generation role, expose runtime constraints and explicitly assess acceptable correctness rather than maximising every quality dimension.

## 29. Breadth-first learning and activation

The project repeatedly favoured a **breadth-first, spiral approach** over a depth-first curriculum that spends months on one practice before showing the whole delivery system.

A useful sequence is:

1. software craft and pragmatic judgement;
2. requirements, product and domain framing;
3. basic architecture and data;
4. testing and change safety;
5. delivery pipeline and operations;
6. security and IAM;
7. reliability and performance;
8. distributed-systems depth;
9. evolutionary architecture and governance;
10. repeated deeper passes driven by current risks.

The same model applies to agents: perform an initial cross-cutting review of the whole change, then allocate deeper specialists according to risk. Do not run every possible specialist at maximum depth on every task.

---

# Part IV — Suggested prioritisation

## 30. Minimum foundational shelf

For a compact but broad base, the discussions converge on the following cluster.

### General craft and change

1. *The Pragmatic Programmer*
2. *Refactoring*
3. *Clean Code* — used critically, not dogmatically
4. *The Mythical Man-Month*

### Architecture and domain

5. *Domain-Driven Design*
6. *Patterns of Enterprise Application Architecture*
7. *Fundamentals of Software Architecture*
8. *Building Evolutionary Architectures*
9. *Enterprise Integration Patterns*

### Data and distributed systems

10. *Designing Data-Intensive Applications*
11. *Building Microservices*, second edition

### Delivery and operations

12. *Continuous Delivery*
13. *Accelerate*
14. *Release It!*
15. Google’s *Site Reliability Engineering* books

### Testing and security

16. *xUnit Test Patterns*
17. a current threat-modelling resource
18. OWASP’s current application and API-security guidance
19. *API Security in Action*
20. *OAuth 2 in Action* for IAM-heavy work

### Reasoning and judgement

21. *Thinking, Fast and Slow*
22. *Superforecasting*
23. *The Great Mental Models* series
24. *Poor Charlie’s Almanack*

### Compendia and frameworks

25. Hacker Laws
26. The Jargon File
27. SWEBOK
28. C4 model
29. Twelve-Factor App
30. Cynefin

This is not a recommended linear reading order. It is the foundational retrieval shelf from which a curriculum or harness can select according to context.

## 31. First sources to ingest for an agentic corpus

### Priority 1 — High-density general principles

- *The Pragmatic Programmer*;
- Hacker Laws;
- SWEBOK classification;
- *The Mythical Man-Month*;
- C4 and Twelve-Factor primary web guidance.

### Priority 2 — Architecture and system trade-offs

- *Fundamentals of Software Architecture*;
- *Designing Data-Intensive Applications*;
- *Domain-Driven Design*;
- *Release It!*;
- Google SRE.

### Priority 3 — Delivery and validation

- *Continuous Delivery*;
- *Accelerate*;
- *Refactoring*;
- *xUnit Test Patterns*;
- OWASP and threat-modelling guidance.

### Priority 4 — Specialisation

- enterprise integration;
- microservices;
- IAM/API security;
- performance;
- current language and framework documentation;
- regulated-domain guidance.

## 32. Ingestion warning: copyright and transformation

A private or commercial knowledge system should not indiscriminately ingest copyrighted books as redistributable full text. Prefer:

- licensed copies and permitted private use;
- user-authored summaries and principle cards;
- short, attributed quotations where legally permitted;
- bibliographic links and page references;
- public standards and openly licensed material;
- original worked examples;
- retrieval from lawfully accessible source material.

The high-value transformation is not bulk text storage. It is the structured extraction of claims, applicability, counter-principles, examples and executable checks.

---

# Part V — Open questions and next synthesis work

## 33. Gaps identified in the discussions

1. **No single complete compendium.** Hacker Laws and the Jargon File are useful but do not cover the full SDLC, product judgement, NFRs and modern agentic operation.
2. **Classics require modern supplements.** Cloud, microservices, zero-trust security, supply-chain risk, platform engineering and AI-assisted development change implementation practice even where the underlying principles remain durable.
3. **Aphorisms lack applicability metadata.** Most collections state the law but not when it conflicts with another law.
4. **Agentic activation is rarely represented.** Existing bibliographies do not say which role should use a principle, at what stage, with what evidence or test.
5. **Product and business reasoning are under-integrated.** Software-engineering canons often begin after the product decision and underrepresent discovery, value, incentives and commercial constraints.
6. **NFRs are fragmented by speciality.** Reliability, security, privacy, performance, accessibility and operability need a common quality-attribute representation.
7. **Creative approximation is under-specified.** Most standards focus on conformance; they give less help on calibrating sufficient accuracy and exploiting runtime constraints safely.
8. **Evidence quality needs explicit treatment.** A memorable law, empirical finding, formal theorem and practitioner opinion should not carry identical weight.

## 34. Recommended next artefacts

The most valuable follow-on artefacts would be:

- a machine-readable principle-card library;
- a source-to-principle traceability graph;
- a conflict matrix of principle versus counter-principle;
- a SWEBOK-based coverage dashboard;
- role-specific agent prompt packs;
- deterministic architecture and NFR fitness-function templates;
- worked case studies showing principles applied and rejected;
- a freshness policy separating timeless principles from current implementation guidance;
- an evaluation suite containing ambiguous cases where slogan matching produces the wrong result.

## 35. Final synthesis

The project discussions point to a clear foundation for agentic software development:

- build on a **plural canon**, not one methodology;
- retain the compact power of laws and aphorisms, but attach context, exceptions and counter-principles;
- use formal taxonomies such as SWEBOK, Bloom, Cynefin and viewpoint/interrogative models to organise knowledge;
- favour breadth-first coverage followed by risk-driven depth;
- separate timeless principles from version-sensitive implementation advice;
- expose product stage, team, runtime, data, integrations and NFRs before proposing architecture;
- use tracer bullets, small batches and executable evidence to collapse uncertainty;
- treat distributed failure, security, reliability and operability as design inputs;
- calibrate correctness and precision to the real problem rather than maximising every dimension blindly;
- combine generative agents with independent critics, deterministic checks and coherent integration;
- measure completed, validated outcomes rather than agent activity;
- preserve conceptual integrity and keep the simplest architecture that satisfies demonstrated needs.

The resulting harness should behave less like a collection of personas reciting books and more like an engineering institution: it retrieves relevant accumulated wisdom, tests it against context, exposes tensions, produces evidence, records decisions and learns from outcomes.

---

# Appendix A — Compact principle checklist

## Problem and context

- What business or user outcome matters?
- What is known, assumed and uncertain?
- Is the decision reversible?
- What is the cost of error?
- What product stage and team capability apply?

## Simplicity and scope

- Is this required now, or speculative?
- Which complexity is essential?
- Is duplication real knowledge duplication?
- Is an abstraction premature?
- Does a framework hide rather than solve the hard problem?

## Architecture

- Are boundaries aligned to domain and ownership?
- Is distribution justified?
- Which decisions are externally binding?
- What does each model omit?
- Which fitness functions preserve desired characteristics?

## Data and distributed systems

- Who owns each datum?
- What consistency is required?
- What happens under partition, delay, duplication and reordering?
- Are operations idempotent?
- How are migrations, replay and reconciliation handled?

## Delivery

- Is there a thin end-to-end path?
- Are changes small and integrated frequently?
- What is the bottleneck?
- What evidence is produced at each stage?
- Can the change be deployed, observed and rolled back safely?

## NFRs

- Are quality attributes expressed as measurable scenarios?
- What are the SLOs and error budgets?
- What are the security assets and trust boundaries?
- What is the capacity model and expected workload?
- Can operators diagnose partial failure?

## Agentic controls

- Which agent proposes, which criticises and which validates?
- What deterministic checks are available?
- Are permissions least-privileged and actions auditable?
- Is untrusted content isolated from tool instructions?
- Is the final output coherent rather than concatenated?
- What requires human approval?

## Learning

- What result would falsify the recommendation?
- What telemetry or user evidence will be collected?
- When should the decision be reviewed?
- Which principle card or prompt should change based on the outcome?

# Appendix B — Resource links

- Hacker Laws: <https://github.com/dwmkerr/hacker-laws>
- The Jargon File: <https://catb.org/~esr/jargon/html/index.html>
- SWEBOK: <https://www.computer.org/education/bodies-of-knowledge/software-engineering>
- C4 model: <https://c4model.com/>
- Twelve-Factor App: <https://12factor.net/>
- OWASP: <https://owasp.org/>
- Google SRE books: <https://sre.google/books/>
- Refactoring: <https://refactoring.com/>
