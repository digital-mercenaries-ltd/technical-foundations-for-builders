# Technical Foundations for Builders

**A breadth-first guide to the ideas behind trustworthy modern software.**

Technical Foundations for Builders (TFB) is for people who can build and ship software - often with artificial intelligence (AI) assistance - but have not yet encountered the breadth of concepts that experienced engineers use to reason about it.

The problem TFB addresses is not a shortage of tutorials. It is **not knowing what you do not know**. If you have never heard of safe repetition, protection between simultaneous data changes, limiting the reach of a failure or granting only necessary access, you cannot recognise when those ideas matter or ask useful questions about them. Engineers give these ideas names such as *idempotency*, *transaction isolation*, *blast radius* and *least privilege*.

TFB supplies that missing map. It introduces the major areas of modern computing, teaches the headline mechanics of each concept, explains why builders encounter it, warns about common pitfalls and provides routes to deeper material. It aims for awareness and a useful initial mental model, not detail or mastery.

Awareness is only the beginning. Knowing that authentication matters is different from being able to find a missing authorisation check, repair it safely and prove that the repair works. TFB helps turn vague concerns and invisible constraints into recognisable mechanisms, better questions and clearer signals that deeper investigation or experienced help is required.

> **Project status:** Milestone 2 was approved on 2026-07-17. The complete Chapter 1 and Chapter 2 first-pass drafts are now under Milestone 3 review.

## Who this is for

TFB is primarily written for a non-technical or newly technical builder who already has a real project: a founder, operator, domain expert or self-taught developer using AI to create software.

In this guide:

- **Vibe coding** means building software with AI without an established technical background. The phrase is used descriptively, not dismissively.
- **Agentic engineering** means using AI agents as part of an engineering process while bringing existing technical judgement to the work.

Both groups can use TFB, but it is the first group that most needs help exposing blind spots. Once a builder knows that a concept exists, project-aware AI can help explain where it appears and how to investigate it. AI output is the start of that investigation, not proof that the system is correct.

## What belongs in TFB

TFB is organised around durable concepts, but it is a living guide for contemporary builders rather than a document intended to remain unchanged for decades. Useful awareness also includes current products, vendors, organisations, protocols, standards, assurance schemes, named laws and professional language.

The material therefore appears at different levels:

- a mechanism such as binary representation or database isolation;
- a current technology such as Kubernetes, PostgreSQL or the Model Context Protocol;
- an organisation or source of authority such as the Internet Engineering Task Force or Open Worldwide Application Security Project (OWASP);
- a standard, scheme or report such as Cyber Essentials, International Organization for Standardization/International Electrotechnical Commission (ISO/IEC) 27001 or a System and Organization Controls (SOC) 2 report;
- a memorable law, practitioner story or piece of hacker folklore such as the law of leaky abstractions, *heisenbug* or *yak shaving*.

These subjects do not need equal-sized entries. Their treatment depends on what the target reader needs to understand or recognise now. Time-sensitive material is dated and reviewed as the landscape changes.

## How the guide avoids overwhelm

TFB uses progressive disclosure. The rule is: **reduce the number of concepts on the first pass, not the quality of their explanations.**

1. **Map the territory:** use this README to see the whole field in a short sitting.
2. **Take a first pass:** read a limited set of properly explained concepts in `chapters/`.
3. **Browse further territory:** once those pages are drafted, selectively open optional awareness-level material in `further/` as it becomes relevant.
4. **Go deeper elsewhere:** follow a few strong external resources when awareness is no longer enough.

The [tiered content outline](OUTLINE.md) records which topics belong at each level. It is intentionally more detailed than this page.

## What each concept explains

Each full concept entry is designed to answer:

1. What is it?
2. How does it work at a basic level?
3. Why does a builder need to know about it?
4. Where does it appear?
5. What are its pitfalls and misleading intuitions?
6. What related or deeper concepts come next?
7. Where can the reader learn more?

TFB is not an academic computer-science curriculum, job-training roadmap, certification guide, encyclopaedia or task-by-task production manual. It is an explanation-first map that helps a working builder recognise the territory.

## Why another guide?

A selection of the closest existing resources each solves a useful but different problem:

*Alternatives reviewed: 2026-07-17. Recheck current course and roadmap descriptions when this date becomes stale.*

| Resource | Its centre of gravity | What remains missing for this audience |
| --- | --- | --- |
| [roadmap.sh](https://roadmap.sh/about) | Role- and skill-based learning paths, now including [AI Product Builder](https://roadmap.sh/ai-product-builder) and [Vibe Coding](https://roadmap.sh/vibe-coding) | One unified, non-sequential map for a working builder |
| [Teach Yourself Computer Science](https://teachyourselfcs.com/) | Deep self-study of traditional computer science (CS) subjects, with roughly 100-200 hours recommended per subject | Production, security, product, governance and AI-assisted work at awareness depth |
| [The Massachusetts Institute of Technology's (MIT) Missing Semester](https://missing.csail.mit.edu/) | A compact practical course that now includes packaging, agentic coding, code quality and work beyond code | The wider conceptual and production landscape |
| [Professional Programming](https://github.com/charlax/professional-programming) | A curated professional-development reading list | Short explanations that create awareness before further study |
| [Developer Handbook](https://github.com/mikeroyal/Developer-Handbook/blob/main/README.md) | A broad technology, tool and resource catalogue | Tight editorial compression and a connected mental model |
| [Mercari's production-readiness checklist](https://github.com/mercari/production-readiness-checklist) | Judging whether a microservice is ready for customer traffic | Explanations for readers who do not yet know the checklist vocabulary |
| [System Design](https://github.com/karanpratapsingh/system-design) | Learning scalable architecture and preparing for system-design interviews | An accessible starting point and the surrounding non-architecture domains |
| [roadmap.sh's DevOps roadmap](https://roadmap.sh/devops) | A step-by-step path through infrastructure and delivery skills | The computing, product, governance and judgement surrounding that role |
| [Agents Towards Production](https://github.com/NirDiamant/agents-towards-production) | Code-first tutorials for production generative-AI agents | The conventional engineering foundations those guides often assume |
| [Hacker Laws](https://github.com/dwmkerr/hacker-laws) | A browsable collection of laws, principles and mental models relevant to development | A connected beginner-facing map that explains the foundations beneath those models |

TFB sits between a map, a field guide and a compact conceptual handbook. It complements these projects rather than replacing them. Its contribution is not a larger list of links. It is the selection, explanation and connection of what a builder should at least have heard of.

The public links in the table identify the alternatives being compared. Working notes and original source material remain in the private editorial repository.

## How to use TFB

Start with the chapter map below. Read the introductions to understand what each area contributes to a modern system, then browse whichever concepts are unfamiliar. The chapters have a sensible order, but they are not a required curriculum.

Follow links as you would in a wiki. A link inside an explanation supplies context at the point where it becomes useful. **Related concepts**, **Deeper concepts** and **Further reading** provide deliberate next steps without turning every page into a catalogue.

When a concept appears relevant, give an AI assistant suitable context about your project and ask it to explain where the concept appears, what risks it creates and what evidence would show that it has been handled correctly. Ask where the answer came from. For consequential security, legal, financial, privacy or operational decisions, verify the answer against authoritative sources or experienced help.

## Map of the territory

The chapters move from the physical representation of information towards the organisational judgement needed to build and operate software:

1. **Foundations:** computing and programming explain how information and code behave.
2. **Construction:** software engineering, the web, data and architecture explain how systems are assembled and changed.
3. **Production:** infrastructure, operations and security explain how systems run, fail and recover.
4. **Purpose and accountability:** product and governance explain why systems exist and how trust is demonstrated.
5. **Modern practice and judgement:** AI-assisted engineering and named mental models connect the whole field.

Security, reliability, privacy, cost and maintainability cut across every layer. They receive dedicated chapters so their ideas can be introduced coherently, not because they happen only in one part of a system.

### 1. Computing foundations

Computers store representations of information and transform them using finite resources. This chapter explains bits, number systems, text, processors, memory, storage, operating systems and clocks so that limits such as overflow, encoding failures and latency stop looking arbitrary.

[Read Chapter 1](chapters/01-computing-foundations.md) · [Browse optional Chapter 1 territory](further/01-computing-foundations.md) · [Browse the tiered Chapter 1 plan](OUTLINE.md#1-computing-foundations)

### 2. Programming foundations

Source code gives instructions to runtimes using values, types, state, control flow, functions and data structures. This chapter gives builders enough of that model to recognise the structure of generated code, understand errors and ask causal debugging questions.

[Read Chapter 2](chapters/02-programming-foundations.md) · [Browse the tiered Chapter 2 plan](OUTLINE.md#2-programming-foundations)

### 3. Software engineering

Software engineering is how intent becomes change that can be understood, tested, reviewed and recovered. This chapter covers requirements, modularity, interfaces, testing, version control, build feedback, code review, technical debt and the hidden knowledge that makes whole-system rewrites dangerous.

[Browse the tiered Chapter 3 plan](OUTLINE.md#3-software-engineering)

### 4. The Internet, web and application programming interfaces

Browsers and services communicate through layered protocols and behavioural contracts. This chapter connects Internet Protocol, Domain Name System, Hypertext Transfer Protocol and browser technologies with semantic Hypertext Markup Language (HTML), progressive enhancement, compatibility, application programming interfaces and the organisations that define or document them.

[Browse the tiered Chapter 4 plan](OUTLINE.md#4-the-internet-web-and-application-programming-interfaces)

### 5. Data and databases

Data needs structure, meaning and rules that remain valid as many users and processes change it. This chapter introduces schemas, relational and non-relational databases, constraints, queries, indexes, transactions, migrations, consistency and the lifecycle of stored information.

[Browse the tiered Chapter 5 plan](OUTLINE.md#5-data-and-databases)

### 6. Architecture and distributed systems

Architecture describes consequential boundaries and relationships within a system. Once components communicate over a network, timeouts, retries, duplicated messages, partial failure and uncertain state become normal design concerns rather than rare edge cases.

[Browse the tiered Chapter 6 plan](OUTLINE.md#6-architecture-and-distributed-systems)

### 7. Infrastructure, cloud and delivery

Software runs on physical resources even when a platform hides most of them. This chapter explains environments, servers, containers, cloud regions, managed services, build artefacts, deployment, rollback, shared responsibility, cost and the coupling created by products such as Kubernetes, Vercel or Supabase.

[Browse the tiered Chapter 7 plan](OUTLINE.md#7-infrastructure-cloud-and-delivery)

### 8. Operations, reliability and observability

A deployed system still needs owners, evidence and recovery paths. This chapter covers reliability targets, logs, metrics, traces, health checks, alerting, incidents, performance, capacity, backups and disaster recovery—the work that makes production behaviour understandable rather than surprising.

[Browse the tiered Chapter 8 plan](OUTLINE.md#8-operations-reliability-and-observability)

### 9. Security, privacy and identity

Security is the control of trust, authority and damage. This chapter introduces threat boundaries, authentication, authorisation, least privilege, cryptography, input and output trust, browser and file attacks, supply-chain risk and responsible handling of personal data.

[Browse the tiered Chapter 9 plan](OUTLINE.md#9-security-privacy-and-identity)

### 10. Product, experience and analytics

Technical correctness is not enough if software solves the wrong problem or excludes its users. This chapter connects product discovery, the prototype-production gap, usability, accessibility, responsive design, analytics, experiments, prioritisation, support signals and the incentives hidden inside metrics.

[Browse the tiered Chapter 10 plan](OUTLINE.md#10-product-experience-and-analytics)

### 11. Governance, compliance and commercial readiness

Organisations must show who is responsible, which obligations apply and what evidence supports their claims. This chapter distinguishes laws, standards, certifications, assurance reports and frameworks before orienting readers to examples such as Cyber Essentials, ISO/IEC 27001 and SOC 2.

[Browse the tiered Chapter 11 plan](OUTLINE.md#11-governance-compliance-and-commercial-readiness)

### 12. AI-assisted engineering

AI changes the speed and interface of software creation, not the underlying responsibility for the result. This chapter covers models, prompting, code generation, agents, the Model Context Protocol, permissions, evaluations, independent verification, prompt injection, provider dependency and generated-code ownership.

[Browse the tiered Chapter 12 plan](OUTLINE.md#12-artificial-intelligence-assisted-engineering)

### 13. Laws, heuristics and engineering judgement

Experienced practitioners use compact models to notice recurring patterns in systems and organisations. This chapter separates theorems, empirical effects, design principles, professional observations and jokes while covering leaky abstractions, system evolution, incentives, simplicity, sources of technical truth and memorable hacker folklore.

[Browse the tiered Chapter 13 plan](OUTLINE.md#13-laws-heuristics-and-engineering-judgement)

## Supporting documents

- [Tiered content outline](OUTLINE.md) - canonical chapter boundaries, first-pass selections and further territory.
- [Glossary](GLOSSARY.md) - short definitions linked to canonical entries.
- [Style guide](STYLE_GUIDE.md) - the editorial contract for contributors and agents.
- [Execution plan](PLAN.md) - milestones and document lifecycle.
- [Issue-ready work packages](WORK_PACKAGES.md) - bounded batches for later drafting.
- [Milestone 2 audit](reviews/milestone-2-audit.md) - editorial review findings, resolutions and verification results.
- [Milestone 1 audit](reviews/milestone-1-audit.md) - prototype review findings and verification results.

## Milestone 2 decision

Approved on 2026-07-17:

- use the 94-entry first traversal established during Milestone 3, below the 95-entry planning guardrail;
- move binary and hexadecimal to Chapter 1 further territory without rewriting their approved explanations;
- retain dated landscape material, contemporary products and organisations;
- allow qualified practitioner stories and hacker folklore;
- test actual reading time, conceptual load and entry bundling during Milestone 3 before increasing the production batch size.

Milestone 3 is limited to the Chapter 1 and Chapter 2 first-pass pages plus relocation of the two existing numeric entries. It does not draft all optional further-territory topics.
