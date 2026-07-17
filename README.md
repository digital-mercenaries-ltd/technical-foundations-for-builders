# Technical Foundations for Builders

**A breadth-first guide to the ideas behind trustworthy modern software.**

Technical Foundations for Builders (TFB) is for people who can build and ship software - often with artificial intelligence (AI) assistance - but have not yet encountered the breadth of concepts that experienced engineers use to reason about it.

The problem TFB addresses is not a shortage of tutorials. It is **not knowing what you do not know**. If you have never heard of safe repetition, protection between simultaneous data changes, limiting the reach of a failure or granting only necessary access, you cannot recognise when those ideas matter or ask useful questions about them. Engineers give these ideas names such as *idempotency*, *transaction isolation*, *blast radius* and *least privilege*.

TFB supplies that missing map. It introduces the major areas of modern computing, teaches the headline mechanics of each concept, explains why builders encounter it, warns about common pitfalls and provides routes to deeper material. It aims for awareness and a useful initial mental model, not detail or mastery.

> **Project status:** Milestone 1 editorial prototype. The outline is deliberately broad, while only the first three entries of Chapter 1 have been drafted. The structure, depth and voice are awaiting review before more content is produced.

## Who this is for

TFB is primarily written for a non-technical or newly technical builder who already has a real project: a founder, operator, domain expert or self-taught developer using AI to create software.

In this guide:

- **Vibe coding** means building software with AI without an established technical background. The phrase is used descriptively, not dismissively.
- **Agentic engineering** means using AI agents as part of an engineering process while bringing existing technical judgement to the work.

Both groups can use TFB, but it is the first group that most needs help exposing blind spots. Once a builder knows that a concept exists, project-aware AI can explain it in the context of their own system, help investigate whether it matters and assist with implementation. That works only after the missing question has become visible.

## What this guide does

Each concept entry is designed to answer:

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

The claims behind this comparison are recorded separately in the compact [alternatives research note](research/project-alternatives.md).

## How to use TFB

Start with the chapter map below. Read the introductions to understand what each area contributes to a modern system, then browse whichever concepts are unfamiliar. The chapters have a sensible order, but they are not a required curriculum.

Follow links as you would in a wiki. A link inside an explanation supplies context at the point where it becomes useful. The **Related concepts**, **Deeper concepts** and **Further reading** sections at the end of an entry offer deliberate next steps.

When a concept appears relevant, give an AI assistant suitable context about your project and ask it to explain where the concept appears, what risks it creates and what evidence would show that it has been handled correctly. Treat that response as the start of an investigation, not proof that the system is sound.

## Map of the territory

The chapters move from the physical representation of information towards the organisational judgement needed to build and operate software:

1. **Foundations:** [Computing foundations](#chapter-1-computing-foundations) explains how information is represented and machines act on it; [Programming foundations](#chapter-2-programming-foundations) explains how people express behaviour as code.
2. **Construction:** [Software engineering](#chapter-3-software-engineering) covers changeable code; [the Internet, web and APIs](#chapter-4-the-internet-web-and-application-programming-interfaces) covers communication; [data and databases](#chapter-5-data-and-databases) covers durable information; [architecture and distributed systems](#chapter-6-architecture-and-distributed-systems) covers components and partial failure.
3. **Production:** [Infrastructure, cloud and delivery](#chapter-7-infrastructure-cloud-and-delivery) covers where software runs; [operations, reliability and observability](#chapter-8-operations-reliability-and-observability) covers keeping it useful; [security, privacy and identity](#chapter-9-security-privacy-and-identity) covers misuse and responsible data handling.
4. **Purpose and accountability:** [Product, experience and analytics](#chapter-10-product-experience-and-analytics) covers usefulness and learning; [governance, compliance and commercial readiness](#chapter-11-governance-compliance-and-commercial-readiness) covers control, evidence and trust.
5. **Modern practice and judgement:** [AI-assisted engineering](#chapter-12-ai-assisted-engineering) covers what changes when AI participates; [laws, heuristics and engineering judgement](#chapter-13-laws-heuristics-and-engineering-judgement) covers compact reasoning tools.

Security, reliability, privacy, cost and maintainability cut across every layer. They are given their own chapters so their ideas can be introduced coherently, not because they happen only at one point in a system.

## Chapter 1: Computing foundations

**Purpose:** build the lowest-level mental model needed by the rest of TFB: how information becomes physical states, how machines represent and transform it, and why finite resources create practical constraints.

You do not need to design a processor or perform arithmetic in binary by hand. You do need enough understanding to recognise why encodings break, numbers overflow, decimal values lose precision, memory differs from storage and apparently small operations can have large performance costs.

The [Chapter 1 prototype](chapters/01-computing-foundations.md) contains the first three completed entries:

1. [Bits and bytes](chapters/01-computing-foundations.md#bits-and-bytes) - the small units from which digital information is built.
2. [Binary numbers](chapters/01-computing-foundations.md#binary-numbers) - representing quantities with two digits.
3. [Hexadecimal and octal](chapters/01-computing-foundations.md#hexadecimal-and-octal) - compact ways to write binary-shaped values.

The planned remainder of the chapter is:

- Boolean values and logic
- Integers, signed numbers and overflow
- Floating-point numbers and precision
- Text, Unicode and character encodings
- Central processing unit (CPU) instructions and execution
- Registers, memory and random-access memory (RAM)
- Persistent storage
- Files and file systems
- Input, output and devices
- Operating systems and system calls
- Programs, processes and threads
- Time and clocks
- Latency and throughput
- Processor and memory caches
- Compression
- Serialisation and data formats

## Chapter 2: Programming foundations

**Purpose:** explain how people express behaviour in software and how source code becomes a running program. This chapter introduces the building blocks that AI-generated code is made from, so a builder can recognise structure, state, dependencies and failure rather than treating code as an opaque result.

The emphasis is not on learning one language's syntax. It is on durable ideas that recur across languages and tools: values have types, control flow selects what happens next, functions package behaviour, state changes over time, data structures shape what operations are easy, and runtimes impose rules that generated code cannot escape.

Planned concepts:

- Source code and programming languages
- Syntax, semantics and behaviour
- Compilers, interpreters and runtimes
- Values and types
- Variables and state
- Expressions and operators
- Conditions, loops and control flow
- Functions, parameters and return values
- Scope and lifetime
- Collections and data structures
- Algorithms and complexity
- Iteration and recursion
- Mutability, immutability and side effects
- Errors and exceptions
- Objects, interfaces and composition
- Modules, packages and dependencies
- Concurrency and asynchronous programming
- Debugging

## Chapter 3: Software engineering

How code is organised and changed by people over time. Planned concepts:

- Functional and non-functional requirements
- Modularity and separation of concerns
- Abstraction and information hiding
- Interfaces and contracts
- Cohesion and coupling
- Composition, inheritance and dependency injection
- Application programming interface (API) design and versioning
- Design patterns
- Automated testing and the testing pyramid
- Version control, branches and merges
- Code review
- Continuous integration
- Refactoring
- Technical debt
- Documentation and architecture decisions
- Maintainability and legacy code

## Chapter 4: The Internet, web and application programming interfaces

How software communicates across networks and how browsers, servers and services meet. Planned concepts:

- The Internet and the web
- Packets and Internet Protocol addresses
- Transmission Control Protocol (TCP), User Datagram Protocol (UDP), ports and sockets
- Domain Name System (DNS)
- Uniform Resource Locators (URLs), Uniform Resource Identifiers (URIs) and domain names
- Hypertext Transfer Protocol (HTTP) requests and responses
- HTTP methods, status codes and headers
- Hypertext Transfer Protocol Secure (HTTPS), Transport Layer Security (TLS) and certificates
- How a browser loads a page
- Hypertext Markup Language (HTML), Cascading Style Sheets (CSS) and JavaScript
- Client-server systems
- APIs, remote procedure calls and representational state transfer (REST)
- GraphQL
- Cookies and sessions
- Same-origin policy and Cross-Origin Resource Sharing (CORS)
- Reverse proxies
- Content delivery networks
- WebSockets and server-sent events
- Webhooks

## Chapter 5: Data and databases

How systems represent, preserve, query and change information. Planned concepts:

- Data models and schemas
- Relational databases and Structured Query Language (SQL)
- Tables, rows, columns and keys
- Relationships and joins
- Normalisation and denormalisation
- Constraints and data integrity
- Create, read, update and delete operations
- Indexes and query planning
- Transactions and atomicity, consistency, isolation and durability (ACID)
- Isolation levels and concurrency control
- Schema migrations
- Non-relational (NoSQL) database families
- Consistency and eventual consistency
- Data import and export
- Data retention and archival
- Online transaction and analytical processing
- Warehouses, lakes and analytics stores
- Event logs and audit trails

## Chapter 6: Architecture and distributed systems

How components are divided, connected and made to behave as one system despite partial failure. Planned concepts:

- System boundaries and components
- Monoliths and modular monoliths
- Services and microservices
- Stateful and stateless components
- Synchronous and asynchronous communication
- Messages, queues and streams
- Events and publish-subscribe systems
- Idempotency
- Timeouts, retries and exponential backoff
- Distributed replication and partitioning
- Sharding
- Designing around network partitions
- Consensus and leader election
- Application and distributed caching
- Load balancing
- Rate limiting and backpressure
- Failure domains and blast radius
- Graceful degradation

## Chapter 7: Infrastructure, cloud and delivery

Where software runs and how changes reach production. Planned concepts:

- Development, test, staging and production environments
- Configuration
- Physical servers and virtual machines
- Containers, images and registries
- Container orchestration and Kubernetes
- Cloud regions and availability zones
- Compute, storage and managed services
- Serverless computing
- Infrastructure as code
- Virtual networks, subnets and firewalls
- Build artefacts
- Continuous delivery and deployment
- Deployment strategies
- Rollback
- Feature flags
- Environment parity
- Artefact repositories and release promotion
- Capacity and cloud cost

## Chapter 8: Operations, reliability and observability

How people keep production systems useful, understandable and recoverable. Planned concepts:

- Production readiness
- Reliability, availability and durability
- Service-level indicators, objectives and agreements
- Monitoring
- Logs, metrics and traces
- Observability
- Health checks
- Alerting and on-call work
- Operational incident response and severity
- Blameless postmortems
- Runbooks
- Capacity planning
- Performance measurement and bottlenecks
- Redundancy and failover
- Backups and restore testing
- Disaster recovery
- Recovery point and recovery time objectives
- Resilience and chaos testing
- Customer support and escalation

## Chapter 9: Security, privacy and identity

How systems resist misuse, limit damage and handle people's data responsibly. Planned concepts:

- Assets, adversaries and attack surfaces
- Threat modelling and trust boundaries
- Authentication and authorisation
- Identities, roles and permissions
- Least privilege
- Secrets management
- Encryption in transit and at rest
- Hashing, salting and password storage
- Keys, certificates and public-key infrastructure
- Input validation and output encoding
- Injection attacks
- Cross-site scripting and request forgery
- Open Worldwide Application Security Project (OWASP) guidance
- Dependency and supply-chain security
- Vulnerability management and patching
- Security testing
- Audit logging
- Personal-data classification, minimisation and deletion
- Privacy and data-protection principles
- Security incident response

## Chapter 10: Product, experience and analytics

Why the software exists, how people experience it and how teams learn whether it is useful. Planned concepts:

- Users, customers and stakeholders
- Problem framing and Jobs to Be Done
- Product-market fit
- Minimum viable products
- Discovery and delivery
- User experience and usability
- Accessibility
- Requirements, stories and acceptance criteria
- Events and product analytics
- Funnels, activation and retention
- Key performance and North Star metrics
- Cohort analysis
- Experiments and A/B (split) testing
- Experiment assignment and exposure
- Feedback and support signals
- Prioritisation and opportunity cost
- Metric gaming and unintended incentives

## Chapter 11: Governance, compliance and commercial readiness

How a software organisation demonstrates control, meets commitments and earns trust beyond the product itself. Planned concepts:

- Ownership and accountability
- Risk management
- Policies, controls and evidence
- Change management
- Access reviews
- Records and auditability
- Data-protection roles and responsibilities
- Third-party and vendor risk
- Open-source licences
- Intellectual property
- Contracts and data-processing agreements
- Security questionnaires
- Service Organization Control 2 (SOC 2) and International Organization for Standardization/International Electrotechnical Commission (ISO/IEC) 27001 at a high level
- Business continuity
- Customer service commitments
- Technical and commercial due diligence

## Chapter 12: AI-assisted engineering

What changes - and what does not - when AI participates in building software. Planned concepts:

- Models, tokens and context windows
- Prompting and context engineering
- Code generation and review
- Agents, tools and the Model Context Protocol
- Permissions and sandboxing
- Human oversight
- Evaluations
- Hallucination and misplaced confidence
- Prompt injection
- Data leakage and privacy
- Non-determinism and reproducibility
- Model and provider dependency
- AI service economics and responsiveness
- Provenance, copyright and licensing
- Generated-code ownership and maintenance
- Why conventional engineering controls still apply

## Chapter 13: Laws, heuristics and engineering judgement

Compact ideas that help experienced engineers reason about trade-offs, organisations and failure. Planned concepts:

- Mental models and trade-offs
- Conway's Law
- Gall's Law
- Brooks' Law
- Goodhart's and Campbell's Laws
- Chesterton's Fence
- Pareto's Principle
- Hanlon's Razor and Murphy's Law
- Hofstadter's and Parkinson's Laws
- The consistency-availability-partition (CAP) theorem and its PACELC extension
- The law of leaky abstractions
- Simplicity and accidental complexity
- Optimising for change and understanding
- Local optimisation and system effects
- Making illegal states impossible
- Separating policy from implementation
- Explicit and implicit behaviour

## Supporting documents

- [Glossary](GLOSSARY.md) - short definitions linked to canonical entries.
- [Style guide](STYLE_GUIDE.md) - the editorial contract for contributors and agents.
- [Execution plan](PLAN.md) - milestones and document lifecycle.
- [Milestone 1 audit](reviews/milestone-1-audit.md) - independent review findings and verification results.
- [Source conversation](Technical%20Foundations%20for%20Founders.md) - the cleaned Markdown reference from which the project emerged.

## Feedback requested for Milestone 1

Before more chapters are drafted, this prototype needs decisions on:

- Does the audience promise describe the intended reader?
- Are the chapter boundaries and order useful?
- Is anything important missing or misplaced in the complete concept map?
- Do the first three entries teach enough without becoming tutorials?
- Is the tone clear without being patronising?
- Are jargon, inline links and further-reading sections handled well?

No later milestone should begin until this feedback has been incorporated.
