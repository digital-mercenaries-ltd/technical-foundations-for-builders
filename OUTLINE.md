# TFB tiered content outline

Status: Milestone 2 draft for review - 2026-07-17

This is the editorial source of truth for the scope of **Technical Foundations for Builders** (TFB). The [README](README.md) is the short reader-facing map. This file records what belongs on the first pass, what belongs in optional further territory and which names should initially appear for recognition or landscape orientation.

## How to read the outline

The guide intentionally includes material at different levels of abstraction. A binary number, a managed platform, a standards body, an assurance report and a humorous debugging term can all be worth recognising. They do not need equal-sized entries.

- **First pass:** approximately five to eight properly explained entries that form one breadth-first traversal.
- **Further territory:** optional awareness-level entries for important but less immediately necessary or more specific material.
- **Recognition and landscape:** short explanations, examples or asides that introduce current names without requiring a full entry.
- **Go deeper:** external sources for mastery, formal detail or exhaustive variants.

Each durable mechanism has one canonical home. Products, vendors, organisations, standards, schemes, laws and stories may appear beside that mechanism or receive a dated landscape entry when knowing the name is itself useful.

The current planning guardrail is no more than 95 principal entries across the complete first traversal. Raising it requires an explicit editorial review rather than filling every chapter to its local maximum.

## 1. Computing foundations

**Purpose:** show how physical states become information and why representations and finite resources create behaviour that differs from everyday intuition.

### First pass

1. Bits, bytes and representation
2. Integer ranges, overflow and floating-point approximation
3. Text, Unicode and character encodings
4. Processors, memory and persistent storage
5. Operating systems, programs, processes and threads
6. Dates, time zones, clocks, latency and throughput

Bits and bytes, binary numbers, and hexadecimal and octal are the approved Milestone 1 calibration set. The tiering places the latter two in further territory, but their drafted explanations should be preserved when the files are reorganised.

### Further territory

- Binary numbers and positional notation
- Hexadecimal, octal and compact representations
- Boolean logic and bitwise operations
- Decimal quantities, money, rounding and units
- Random numbers, entropy and collision probability
- Processor instructions, registers and system calls
- Files, file systems and platform differences
- Input, output and devices
- Processor and memory caches
- Compression
- Serialisation and data formats
- Endianness and error detection
- Amdahl's Law and limits to speed-up

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Unicode Consortium, Unicode Standard, UTF-8, American Standard Code for Information Interchange (ASCII), International Organization for Standardization (ISO), Institute of Electrical and Electronics Engineers (IEEE), National Institute of Standards and Technology (NIST), decimal and binary prefixes, x86-64, Arm, solid-state drives and object storage.

**Boundary:** number and text representation live here; language type systems live in Chapter 2, database representations in Chapter 5 and cryptographic use in Chapter 9.

## 2. Programming foundations

**Purpose:** explain the structures and runtime rules inside source code so that generated code is not an opaque artefact.

### First pass

1. Source code, programming languages and runtimes
2. Values, types and conversions
3. Variables, state, mutability and side effects
4. Control flow, functions and scope
5. Collections, data structures and algorithmic cost
6. Errors, exceptions, cleanup, debugging and diagnosis
7. Modules, packages and dependencies

### Further territory

- Syntax, semantics and observable behaviour
- Compilers, interpreters and virtual machines
- Iteration and recursion
- Objects, interfaces, composition and inheritance
- Static and dynamic typing, inference and nullability
- Equality, ordering, missing values and special values
- Concurrency, parallelism and asynchronous work
- Resource ownership, cancellation and lifetime
- Parsing limits and hostile inputs
- Reproducible debugging, stack traces, debuggers and minimal examples

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

JavaScript, TypeScript, Python, Java, Kotlin, C#, Go, Rust, Swift, PHP, Ruby, Node.js, Deno, Bun, npm, Python Package Index (PyPI), Maven Central, NuGet, crates.io, integrated development environments and language servers.

**From hacker folklore:** *heisenbug*, *Bohr bug*, *shotgun debugging*, *voodoo programming*, *phase of the moon* and *PEBKAC/PEBCAK* can make debugging behaviours memorable. Explain the real issue—observer effects, hidden state or lack of a causal model—rather than using the joke as the diagnosis.

**Boundary:** language mechanics live here; organising and changing a codebase over time lives in Chapter 3.

## 3. Software engineering

**Purpose:** explain how intent becomes maintainable, testable and recoverable change across a codebase and a team.

### First pass

1. Functional requirements, quality attributes, specifications and invariants
2. Modularity, cohesion, coupling and separation of concerns
3. Abstraction, information hiding and interfaces
4. Testing, verification and evidence
5. Version control, code review, shared ownership and recovery
6. Build automation, continuous integration and fast feedback
7. Refactoring, technical debt, legacy systems and evolutionary replacement

### Further territory

- Library interfaces, in-process contracts and versioning
- Composition, inheritance and dependency injection
- Design patterns and speculative abstraction
- Unit, integration, contract, end-to-end, property, fuzz and mutation testing
- Test doubles, coverage and flaky tests
- Defect tracking and reproducible reports
- Semantic Versioning, manifests and lockfiles
- Documentation and architecture decision records
- Developer experience and work-in-progress limits
- Maintainability, software rot and the second-system effect

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Git, GitHub, GitLab, Bitbucket, pull requests, trunk-based development, conventional commits, GitHub Actions, GitLab CI/CD, Jenkins and common code-quality services.

**Historical practice:** the Joel Test (2000) may appear as a dated field checklist after its underlying ideas have been explained. Joel Spolsky's writing on daily builds, bug reports and rewrites supplies memorable cases, not universal process rules.

**Boundary:** code construction, collaborative change and in-process library interfaces live here; network service contracts live in Chapter 4, deploying the resulting artefact in Chapter 7 and operating it in Chapter 8.

## 4. The Internet, web and application programming interfaces

**Purpose:** explain how browsers, servers and services communicate, and why compatibility and failure remain visible through convenient frameworks.

### First pass

1. The Internet, Internet Protocol, transport, ports and the journey of a request
2. Domain Name System, domain names, Uniform Resource Locators and Uniform Resource Identifiers
3. Hypertext Transfer Protocol, Hypertext Transfer Protocol Secure, Transport Layer Security and certificates
4. Browsers, semantic Hypertext Markup Language, Cascading Style Sheets and JavaScript
5. Client-server systems, network service application programming interfaces and behavioural contracts
6. Cookies, sessions, browser origins and Cross-Origin Resource Sharing
7. Progressive enhancement, capability detection and browser compatibility

### Further territory

- Hypertext Transfer Protocol methods, status codes, headers, caching and content negotiation
- Representational State Transfer, remote procedure calls and GraphQL
- OpenAPI, JSON Schema and generated clients
- Reverse proxies, content delivery networks and gateways
- WebSockets, server-sent events and webhooks
- Browser rendering models, web performance and Core Web Vitals
- Web Platform Baseline, feature policies and compatibility data
- Backward compatibility, deprecation and Hyrum's Law
- Internationalised domain names and protocol registries

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

MDN Web Docs, World Wide Web Consortium (W3C), Web Hypertext Application Technology Working Group (WHATWG), Internet Engineering Task Force (IETF), RFC Editor, Internet Assigned Numbers Authority (IANA), Internet Corporation for Assigned Names and Numbers (ICANN), Chrome, Safari, Firefox, Edge, Chromium, WebKit and Gecko.

**Boundary:** the mechanics of communication live here; distributed coordination and partial failure live in Chapter 6, web attacks in Chapter 9 and interface usability in Chapter 10.

## 5. Data and databases

**Purpose:** explain how systems give information structure, preserve its rules and change it safely under concurrent use.

### First pass

1. Data models, schemas, identifiers and missing values
2. Relational databases, Structured Query Language, keys, relationships and joins
3. Constraints, validation and data integrity
4. Queries, indexes and execution plans
5. Transactions, atomicity, isolation and concurrency control
6. Schema evolution, online migrations and backfills
7. Non-relational databases, consistency and data lifecycle

### Further territory

- Create, read, update and delete operations
- Query selectivity, N+1 problems and connection pools
- Offset and cursor pagination
- Optimistic and pessimistic locking
- Isolation anomalies and write skew
- Eventual consistency and conflict resolution
- Document, key-value, graph, time-series and search stores
- Import, export, retention, archival, deletion and legal holds
- Operational and analytical processing
- Warehouses, lakes, lakehouses and analytical stores
- Event logs, audit trails and change-data capture

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

PostgreSQL, MySQL, MariaDB, SQLite, Microsoft SQL Server, Oracle Database, MongoDB, Redis, DynamoDB, Firestore, Supabase, Elasticsearch, Snowflake, BigQuery, database migrations and object-relational mappers.

**Boundary:** data integrity lives here; replication across distributed components lives in Chapter 6, managed database responsibility in Chapter 7 and backup recovery in Chapter 8.

## 6. Architecture and distributed systems

**Purpose:** show how components and boundaries form a system, and why remote components introduce partial failure and uncertain outcomes.

### First pass

1. System context, boundaries, components and architecture views
2. Monoliths, services, and stateful and stateless components
3. Synchronous calls, asynchronous messages, queues, streams and events
4. Partial failure and the fallacies of distributed computing
5. Deadlines, timeouts, cancellation, retries and idempotency
6. Replication, partitioning, consistency and user-visible intermediate states
7. Load balancing, rate limiting, backpressure, failure domains and graceful degradation

### Further territory

- C4 and Unified Modeling Language notation
- Reference architectures, viewpoints and stakeholder views
- Domain-driven design and bounded contexts
- Event storming and event-driven architecture
- Delivery guarantees, duplicate messages and ordering
- Transactional outbox, sagas and compensating actions
- Sharding, consensus and leader election
- CAP theorem and PACELC
- Distributed caching and cache invalidation
- Circuit breakers, bulkheads, load shedding and retry budgets
- Architecture frameworks including TOGAF, Zachman and ArchiMate

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Kafka, RabbitMQ, Amazon Simple Queue Service, Google Pub/Sub, Redis, content-delivery networks, service meshes and vendor well-architected frameworks.

**Boundary:** language concurrency lives in Chapter 2; database transactions in Chapter 5; deployment topology in Chapter 7; reliability objectives in Chapter 8.

## 7. Infrastructure, cloud and delivery

**Purpose:** explain where software runs, how a tested change becomes a production release and which responsibilities remain when infrastructure is managed by somebody else.

### First pass

1. Development, test, staging and production environments
2. Configuration, secrets delivery and environment parity
3. Physical servers, virtual machines, containers and serverless computing
4. Cloud regions, managed services, shared responsibility and self-hosting
5. Build artefacts, registries and infrastructure as code
6. Continuous delivery, deployment compatibility, rollback and irreversible change
7. Capacity, quotas, pricing, vendor coupling, portability and exit planning

### Further territory

- Virtual networks, subnets, firewalls and load balancers
- Container images, Docker and container registries
- Kubernetes and container orchestration
- Rolling, blue-green, canary and recreate deployments
- Feature flags, dark launches and release control
- Immutable artefacts and release promotion
- Reproducible builds, provenance and software bills of materials
- Graceful shutdown, readiness and old/new version coexistence
- Control planes and data planes
- Infrastructure as a service, platform as a service, functions as a service and backend as a service

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Amazon Web Services, Microsoft Azure, Google Cloud, Cloudflare, Vercel, Netlify, Heroku, Render, Fly.io, Supabase, Firebase, Terraform and OpenTofu.

Named stack profiles such as LAMP, MERN, T3 and Next.js–Vercel–Supabase may receive dated landscape entries. They should show request flow, state, trust boundaries, managed responsibility and coupling rather than act as endorsements.

**Boundary:** architectural decomposition lives in Chapter 6; operating and recovering the deployed system lives in Chapter 8; contracts and vendor assurance live in Chapter 11.

## 8. Operations, reliability and observability

**Purpose:** explain how people know whether production software is useful, respond when it is not and recover without guessing.

### First pass

1. Production readiness, operational ownership and health checks
2. Reliability, availability, durability, service levels and error budgets
3. Logs, metrics, traces and observability
4. Alerting, on-call work and escalation
5. Incident response, severity, timelines and learning reviews
6. Performance, capacity, resource bounds and bottlenecks
7. Backups, restore testing, disaster recovery and continuity

### Further territory

- Structured logging, correlation and trace context
- Metric cardinality, telemetry sampling and sensitive data
- Tail latency, queueing, saturation and load testing
- Runbooks, automation and manual recovery paths
- Redundancy, shared failure domains and failover exercises
- Recovery point and recovery time objectives
- Chaos and resilience testing
- Synthetic monitoring, canaries and post-deployment verification
- Customer support and status communication
- Root-cause analysis, Five Whys and contributing conditions

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

OpenTelemetry, Prometheus, Grafana, Datadog, New Relic, Sentry, Splunk, Elastic, PagerDuty, Opsgenie, status pages and cloud-provider monitoring services.

**Boundary:** designing for partial failure lives in Chapter 6; deployment health in Chapter 7; security incident specifics in Chapter 9; organisational continuity evidence in Chapter 11.

## 9. Security, privacy and identity

**Purpose:** explain how systems establish trust, constrain authority, resist misuse and limit the consequences of failure or compromise.

### First pass

1. Assets, adversaries, attack surfaces and trust boundaries
2. Authentication, authorisation, sessions, identities and least privilege
3. Encryption, hashing, signatures, keys and certificates
4. Input validation, output encoding, interpreters and injection
5. Browser attacks, hostile files, unsafe URLs and server-side requests
6. Dependencies, software supply chains, vulnerabilities and patching
7. Personal data, minimisation, retention, deletion and security incidents

### Further territory

- Threat modelling methods and abuse cases
- Password storage, salts, peppers and multi-factor authentication
- Passkeys and public-key infrastructure
- Authenticated encryption, nonces and key lifecycle
- Cross-site scripting, cross-site request forgery and Content Security Policy
- File upload handling, archive extraction and server-side request forgery
- Secrets management, rotation and sensitive telemetry
- Dependency provenance, signatures, checksums and bills of materials
- Security testing and application-security verification
- Privacy principles, data classification and impact assessments
- Audit logging and forensic evidence

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Open Worldwide Application Security Project (OWASP), OWASP Top 10, OWASP Application Security Verification Standard, NIST, United Kingdom National Cyber Security Centre, Center for Internet Security, Cyber Essentials, common identity providers, password managers, passkeys, Dependabot, Snyk and software composition analysis.

**Boundary:** security mechanisms live here; the legal and assurance categories surrounding them live in Chapter 11.

## 10. Product, experience and analytics

**Purpose:** connect technical work to the people it serves, the evidence used to improve it and the incentives that can distort that evidence.

### First pass

1. Users, customers, stakeholders, problems and Jobs to Be Done
2. Product-market fit, minimum viable products and the prototype-production gap
3. Discovery, delivery, requirements, stories and acceptance criteria
4. User experience, usability, accessibility and capability-aware design
5. Events, product analytics, metrics and trustworthy instrumentation
6. Funnels, activation, retention, cohorts and experiments
7. Prioritisation, opportunity cost, support signals and metric gaming

### Further territory

- Design systems, components, tokens and interaction states
- Internationalisation, localisation, names, addresses and pluralisation
- Web Content Accessibility Guidelines and assistive technology
- Fitts' Law, Hick-Hyman Law and the principle of least astonishment
- Experiment assignment, exposure, statistical uncertainty and stopping rules
- Key performance indicators and North Star metrics
- Network effects, platforms, complementors and ecosystems
- Switching costs, data portability and distribution
- Lightweight usability observation and qualitative research
- Forecasting, work in progress and context switching

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Figma, Storybook, Google Analytics, PostHog, Mixpanel, Amplitude, feature-flag and experimentation platforms, customer-support systems and product-feedback tools.

**Related practitioner stories:** Joel Spolsky's *Iceberg Secret* can illustrate the invisible work beneath a polished demonstration; *Five Worlds* can illustrate that advice depends on product context.

**Boundary:** implementation accessibility belongs here as a user outcome and is cross-linked from Chapter 4; organisational commitments and legal duties live in Chapter 11.

## 11. Governance, compliance and commercial readiness

**Purpose:** explain how an organisation demonstrates control, meets applicable obligations and earns trust beyond a working product.

### First pass

1. Ownership, accountability and risk management
2. Laws, standards, certification schemes, assurance reports and frameworks
3. Policies, controls, evidence, change management and auditability
4. Data-protection roles, agreements and impact assessment
5. Third-party, supplier and concentration risk
6. Open-source licences, intellectual property and contracts
7. Business continuity, customer commitments and due diligence

### Further territory

- Cyber Essentials and Cyber Essentials Plus
- ISO/IEC 27001 and related management-system standards
- System and Organization Controls (SOC) reports, including SOC 2 Types 1 and 2
- Payment Card Industry Data Security Standard
- NIST Cybersecurity Framework, CIS Controls and Cloud Controls Matrix
- United Kingdom and European Union data-protection regimes
- Security questionnaires and customer assurance
- Software bills of materials, SPDX and CycloneDX
- Sector-specific obligations and regulated roles
- Service commitments, remedies and evidence periods

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

International Organization for Standardization, International Electrotechnical Commission, American Institute of Certified Public Accountants, United Kingdom National Cyber Security Centre, Information Commissioner's Office, PCI Security Standards Council, Cloud Security Alliance, regulators, accreditation bodies, certification bodies and independent auditors.

Current schemes and organisations may receive dated entries. Always state whether an item is law, guidance, a standard, a certification scheme, a control framework or an assurance report.

**Boundary:** technical controls live in Chapters 7–9; this chapter explains applicability, governance, evidence and external trust.

## 12. AI-assisted engineering

**Purpose:** explain what changes when probabilistic models participate in engineering, and which conventional responsibilities remain with the builder.

### First pass

1. Models, tokens, context windows and probabilistic output
2. Prompting, context engineering and abstraction matching
3. Code generation, comprehension, ownership and maintenance
4. Agents, tools, permissions, sandboxing and the Model Context Protocol
5. Human oversight, evaluations, independent control and misplaced confidence
6. Prompt injection, data leakage, privacy and provenance
7. Model providers, dependency, cost, latency and conventional engineering controls

### Further territory

- Embeddings and retrieval-augmented generation
- Tool calling, state, memory and durable orchestration
- Agentic application trust boundaries and least privilege
- Model, prompt and evaluation versioning
- Test sets, graders, human evaluation and production feedback
- Reproducibility, model updates and provider drift
- Copyright, licensing and generated-code provenance
- Local models, hosted models and hardware requirements
- AI incident handling and abuse monitoring
- Model API, retrieval and agent stack profiles

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

OpenAI, Anthropic, Google Gemini, Meta Llama, GitHub Copilot, Cursor, Claude Code, Codex, model APIs, local inference runtimes, vector databases and evaluation platforms.

The canonical distinction is not whether AI wrote the code. It is whether the person responsible can independently model, inspect, constrain, verify and recover the system. TFB supplies mechanism awareness and escalation cues, not proof of correctness.

**Boundary:** ordinary programming, testing, security, delivery and operations remain canonical in their earlier chapters and are cross-linked rather than redefined here.

## 13. Laws, heuristics and engineering judgement

**Purpose:** give memorable names to recurring constraints and trade-offs while distinguishing mathematical results, empirical effects, design principles, professional observations and jokes.

### First pass

1. How to use mental models, laws, heuristics and trade-offs
2. Standards, specifications, implementations, documentation and sources of technical truth
3. The law of leaky abstractions
4. System evolution: Gall's Law and Chesterton's Fence
5. Organisations and delivery: Conway's Law and Brooks' Law
6. Measures and incentives: Goodhart's and Campbell's Laws
7. Simplicity, accidental complexity, Don't Repeat Yourself (DRY), Keep It Simple (KISS) and You Aren't Gonna Need It (YAGNI)
8. Local optimisation, system effects, evidence and reversible decisions

### Further territory

- Hanlon's Razor, Murphy's Law and incident interpretation
- Hofstadter's and Parkinson's Laws and estimation uncertainty
- Law of Triviality and bikeshedding
- Law of Conservation of Complexity
- Defaults inherited from another context
- Separating policy from implementation
- Making illegal states impossible
- Law of the Instrument and familiar-tool bias
- Context-sensitive advice and *Five Worlds*
- Speculative generality and *architecture astronauts*

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Hacker Laws, the Jargon File, Joel on Software, Unix philosophy, SOLID, hacker folklore, the Bitter Lesson, *yak shaving*, *cruft*, *kludge*, *spaghetti code*, *bug-compatible*, *quick-and-dirty* and *Real Soon Now*.

Technical laws keep their canonical homes: Amdahl's Law in [Chapter 1](#1-computing-foundations), Hyrum's Law in [Chapter 4](#4-the-internet-web-and-application-programming-interfaces), CAP and PACELC in [Chapter 6](#6-architecture-and-distributed-systems), Kerckhoffs's principle in [Chapter 9](#9-security-privacy-and-identity), and Fitts' and Hick-Hyman Laws in [Chapter 10](#10-product-experience-and-analytics).

Humorous and historical terms are welcome when they help a reader remember a real mechanism. Explain them without sanding off all their personality, but state their scope and do not treat a joke as evidence.

**Boundary:** named results with a clear technical home are taught in that chapter and may be collected here only as cross-links. Chapter 13 supplies cross-cutting judgement rather than becoming a miscellaneous bin.

## Whole-guide dependency spine

The guide supports selective browsing, but the first-pass traversal has a useful dependency direction:

1. Representations and machine limits make programming behaviour intelligible.
2. Programming structures make software-engineering controls intelligible.
3. Networks and data provide the components used by architecture.
4. Architecture explains what infrastructure deploys and operations observes.
5. Security, product and governance apply constraints and purpose across the whole system.
6. AI-assisted engineering reuses all preceding controls rather than replacing them.
7. Laws and judgement provide compact cross-links across every chapter.

Cross-links should allow a reader to enter anywhere without requiring strict sequential study.

## Maintenance rule for living landscape material

Every product, vendor, organisation, protocol status, standard edition or scheme description that can materially change must have a dated note in the private research repository or a `Reviewed: YYYY-MM-DD` marker in its landscape entry. Maintenance should prioritise:

1. correctness of category and responsibility;
2. current status, ownership and deprecation;
3. changed limits, names or product boundaries;
4. broken or superseded references;
5. whether the name still deserves space for the target reader.

Automation may later identify stale review dates and changed links. Human editorial judgement remains responsible for whether a current item still belongs.
