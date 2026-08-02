# TFB tiered content outline

Status: Milestone 4 Chapter 3 approved; Chapter 4 in progress - 2026-07-18

This is the editorial source of truth for the scope of **Technical Foundations for Builders** (TFB), Volume 1 of the project family described in [PROJECT_FAMILY.md](PROJECT_FAMILY.md). The [README](README.md) is the short reader-facing map. This file records what belongs on the first pass, what belongs in optional further territory and which names should initially appear for recognition or landscape orientation.

## How to read the outline

The guide intentionally includes material at different levels of abstraction. A binary number, a managed platform, a standards body, an assurance report and a humorous debugging term can all be worth recognising. They do not need equal-sized entries.

- **First pass:** approximately five to eight properly explained entries that form one breadth-first traversal.
- **Further territory:** optional awareness-level entries for important but less immediately necessary or more specific material.
- **Recognition and landscape:** short explanations, examples or asides that introduce current names without requiring a full entry.
- **Go deeper:** external sources for mastery, formal detail or exhaustive variants.

Each durable mechanism has one canonical home. Products, vendors, organisations, standards, schemes, laws and stories may appear beside that mechanism or receive a dated landscape entry when knowing the name is itself useful.

The current approved outline contains 94 principal entries across the complete first traversal, below a planning guardrail of 95. Milestone 3 raised the Milestone 2 count from 91 by splitting three overloaded labels: integer overflow from floating point, time from performance, and error handling from diagnosis. Raising the guardrail itself requires an explicit editorial review rather than filling every chapter to its local maximum.

## Cross-cutting context and boundaries

AI assistance and agentic engineering are a pervasive context for the whole outline. Chapter 12 is the canonical home for distinctive AI mechanisms such as probabilistic output, context, agents, tool permissions, evaluations and prompt injection. Earlier chapters should still explain an agentic consequence when it materially changes behaviour, evidence, responsibility or a likely failure mode. Do not add a mechanical AI subsection when nothing important changes.

The Delivery Risk Cube may be introduced as a decision lens: functional breadth, implementation fidelity and production-quality depth should be shaped by the project's next commitment. It does not replace the chapter taxonomy, create another disclosure tier or turn TFB into a maturity model.

The product and governance chapters establish the interfaces required to understand trustworthy software. Deeper coverage of technology strategy, organisation-wide product ownership, delivery management, workplace information technology, business systems, budgets, sourcing and technical leadership belongs to the planned **Technical Leadership for Builders** Volume 2 and will receive a separate outline.

## 1. Computing foundations

**Purpose:** show how physical states become information and why representations and finite resources create behaviour that differs from everyday intuition.

### First pass

1. Bits, bytes and representation
2. Integer ranges and overflow
3. Floating-point approximation
4. Text, Unicode and character encodings
5. Processors, memory and persistent storage
6. Operating systems and running programs
7. Time, clocks, dates and time zones
8. Latency and throughput

Bits and bytes, binary numbers, and hexadecimal and octal are the approved Milestone 1 calibration set. Milestone 3 keeps bits and bytes here and relocates the latter two entries unchanged to Chapter 1 further territory, leaving links from the first-pass page where they help.

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

Unicode Consortium, Unicode Standard, Unicode Transformation Format 8-bit (UTF-8), American Standard Code for Information Interchange (ASCII), International Organization for Standardization (ISO), Institute of Electrical and Electronics Engineers (IEEE), National Institute of Standards and Technology (NIST), decimal and binary prefixes, x86-64, Arm, solid-state drives and object storage.

**Boundary:** number and text representation live here; language type systems live in Chapter 2, database representations in Chapter 5 and cryptographic use in Chapter 9.

## 2. Programming foundations

**Purpose:** explain the structures and runtime rules inside source code so that generated code is not an opaque artefact.

### First pass

1. Source code, programming languages and runtimes
2. Values, types and conversions
3. Variables, state, mutability and side effects
4. Control flow, functions and scope
5. Collections, data structures and algorithmic cost
6. Modules, packages and dependencies
7. Errors, exceptions and cleanup
8. Debugging and diagnosis

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

**From hacker folklore:** *heisenbug*, *Bohr bug*, *shotgun debugging*, *voodoo programming*, *phase of the moon*, “problem exists between keyboard and chair” (PEBKAC) and “problem exists between chair and keyboard” (PEBCAK) can make debugging behaviours memorable. Explain the real issue—observer effects, hidden state or lack of a causal model—rather than using the joke as the diagnosis.

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
- Software documentation as maintained system evidence: audiences, document types, canonical sources, docs-as-code, ownership, freshness, tested examples and architecture decision records
- Developer experience and work-in-progress limits
- Maintainability, software rot and the second-system effect

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Git, GitHub, GitLab, Bitbucket, pull requests, trunk-based development, conventional commits, GitHub Actions, GitLab continuous integration and continuous delivery (CI/CD), Jenkins and common code-quality services.

Treat *pigs and chickens* as dated Scrum folklore that a reader may still encounter, not as current role terminology or a recommended division between people who are “committed” and “involved”. Explain accountability and participation directly. The metaphor was removed from the Scrum Guide in 2011 after it had been used to create unhelpful barriers and power dynamics. Planning references: the official [Scrum Guide revision history](https://scrumguides.org/revisions.html) and Scrum.org's contemporary explanation of [chickens and pigs](https://www.scrum.org/resources/chickens-and-pigs).

For software documentation, teach the durable distinction between clarity and correctness and between documents serving different readers and purposes. Introduce Diátaxis's tutorials, how-to guides, reference and explanation as one useful diagnostic framework rather than a mandatory directory structure. Introduce docs-as-code, plain language, controlled language and Simplified Technical English (ASD-STE100) for recognition, while making clear that version control or simplified prose does not establish factual accuracy. Planning references: [Diátaxis](https://diataxis.fr/start-here/), [Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/), [Google's documentation chapter in *Software Engineering at Google*](https://abseil.io/resources/swe-book/html/ch10.html), [ISO 24495-1:2023 plain language](https://www.iso.org/standard/78907.html), [ASD-STE100](https://www.asd-ste100.org/) and [GDS guidance on architecture decision records](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html).

For architecture decision records, explain the context, status, decision and consequences, including alternatives only where they clarify the trade-off. Preserve decision history by marking a record superseded rather than silently rewriting it. An ADR records rationale; it is neither a complete architecture description nor proof that the decision was sound.

Possible book-length routes for the curated further-reading guide are [*Docs for Developers: An Engineer's Field Guide to Technical Writing*](https://link.springer.com/book/10.1007/978-1-4842-7217-6) and [*Documenting Software Architectures: Views and Beyond*, second edition](https://www.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/). Select them only after balancing the complete thematic guide.

**Historical practice:** the Joel Test (2000) may appear as a dated field checklist after its underlying ideas have been explained. Joel Spolsky's writing on daily builds, bug reports and rewrites supplies memorable cases, not universal process rules.

**Boundary:** code construction, collaborative change and documentation required to understand or change a software system live here; network service contracts and their machine-readable descriptions live in Chapter 4, deploying the resulting artefact in Chapter 7 and operating it in Chapter 8. Organisation-wide knowledge management, records strategy, documentation staffing, enterprise taxonomy and tooling belong to TLB Volume 2.

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
- OpenAPI, JavaScript Object Notation (JSON) Schema, generated clients and generated interface reference
- Reverse proxies, load balancers, API gateways, content delivery networks, web application firewalls and service meshes
- WebSockets, server-sent events and webhooks
- Browser rendering models, web performance and Core Web Vitals
- Web Platform Baseline, feature policies and compatibility data
- Backward compatibility, deprecation and Hyrum's Law
- Internationalised domain names and protocol registries

### Recognition and landscape

*Landscape selection reviewed: 2026-08-02; verify current status before publication.*

MDN Web Docs, World Wide Web Consortium (W3C), Web Hypertext Application Technology Working Group (WHATWG), Internet Engineering Task Force (IETF), RFC Editor, Internet Assigned Numbers Authority (IANA), Internet Corporation for Assigned Names and Numbers (ICANN), Chrome, Safari, Firefox, Edge, Chromium, WebKit and Gecko.

Teach an API gateway as a runtime boundary that routes API calls and may apply authentication, quotas, rate limits, transformations, observability and lifecycle policy. Distinguish it from a reverse proxy, load balancer, ingress controller, web application firewall, content-delivery network and service mesh; products may combine these roles, but the concepts are not interchangeable. A gateway does not remove the backend's responsibility for authorisation, correct contracts or safe overload behaviour. Recognise [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts), [Google Cloud API Gateway](https://docs.cloud.google.com/api-gateway/docs/architecture-overview) and [Cloudflare API Shield](https://developers.cloudflare.com/api-shield/) as current examples with overlapping but different scopes. Keep API contracts canonical here; place managed-service responsibility in Chapter 7, overload control in Chapter 6 and API security in Chapter 9.

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
5. End-to-end deadlines and time budgets, timeouts, cancellation, retries and idempotency
6. Replication, partitioning, consistency and user-visible intermediate states
7. Load balancing, admission and rate limiting, bounded queues, backpressure, overload collapse, failure domains and graceful degradation

### Further territory

- C4 model context, container, component and code views, and Unified Modeling Language notation
- Reference architectures, viewpoints and stakeholder views
- Domain-driven design and bounded contexts
- Event storming and event-driven architecture
- Delivery guarantees, duplicate messages and ordering
- Transactional outbox, sagas and compensating actions
- Sharding, consensus and leader election
- Consistency, availability and partition tolerance (CAP) theorem, and “partition: availability or consistency; else: latency or consistency” (PACELC)
- Distributed caching and cache invalidation
- Deadline propagation, timeout ordering, circuit breakers, bulkheads, load shedding and retry budgets
- Architecture frameworks including The Open Group Architecture Framework (TOGAF), Zachman and ArchiMate

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

Kafka, RabbitMQ, Amazon Simple Queue Service, Google Pub/Sub, Redis, content-delivery networks, service meshes and vendor well-architected frameworks.

Teach deadlines, cancellation, retries and backpressure as connected controls on finite work rather than isolated patterns. An incoming request has a total time budget; downstream calls consume the remaining budget; expired or cancelled work should stop where possible; bounded queues, admission control and load shedding prevent unbounded accumulation; and retries can amplify the overload they are intended to survive. A call-chain or shrinking-budget diagram may help. Planning references: [gRPC deadlines and deadline propagation](https://grpc.io/docs/guides/deadlines/) and the Amazon Builders' Library on [timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).

**Boundary:** language concurrency lives in Chapter 2; database transactions in Chapter 5; deployment topology in Chapter 7; reliability objectives in Chapter 8.

## 7. Infrastructure, cloud and delivery

**Purpose:** explain where software runs, how a tested change becomes a production release and which responsibilities remain when infrastructure is managed by somebody else.

### First pass

1. Development, test, staging and production environments
2. Configuration, workload identity, secrets delivery and environment parity
3. Physical servers, virtual machines, containers and serverless computing
4. Cloud regions, provider-neutral service primitives, managed services, shared responsibility and self-hosting
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
- Workload identities, short-lived credentials and secrets-manager integration
- Infrastructure as a service, platform as a service, functions as a service and backend as a service
- Open-source foundations, project governance and project-lifecycle signals

### Recognition and landscape

*Landscape selection reviewed: 2026-07-31; verify current status before publication.*

Amazon Web Services, Microsoft Azure, Google Cloud, Cloudflare, Vercel, Netlify, Heroku, Render, Fly.io, Supabase, Firebase, Terraform, OpenTofu, the Linux Foundation, the Cloud Native Computing Foundation (CNCF) and the CNCF Landscape.

Introduce cloud services through a provider-neutral map before naming products: identity and policy; networking and edge; compute; storage and databases; messaging and integration; configuration and secrets; observability and operations; and build and delivery. A compact comparison should help readers translate among Amazon Web Services, Microsoft Azure, Google Cloud, Cloudflare and specialised platforms without implying exact equivalence. Explain that managed services move operational work and change the responsibility boundary; they do not remove responsibility.

For infrastructure as code, cover desired state, dependency graphs, plan or preview, state, drift, idempotence, secret handling, review of destructive changes and the limits of rollback. State may contain sensitive material and is part of the control boundary. Planning references: Terraform's explanations of [state](https://developer.hashicorp.com/terraform/language/state) and [resource drift](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift).

For software-as-a-service products, provide recognition of recurring technical building blocks such as tenants or organisations, roles and entitlements, billing, API keys, webhooks, audit trails, single sign-on and System for Cross-domain Identity Management (SCIM). Route their mechanics to Chapters 4, 5, 9 and 10 rather than creating a second explanation here. Organisation-wide selection, procurement, administration and integration of business software-as-a-service belong to TLB.

For CNCF, explain what a neutral open-source foundation and its project lifecycle can signal without treating inclusion, graduation or landscape placement as proof that a project fits a particular system. Planning references: [CNCF: Who we are](https://www.cncf.io/about/who-we-are/), [CNCF project lifecycle](https://contribute.cncf.io/projects/lifecycle/) and the maintained [CNCF Landscape](https://landscape.cncf.io/).

Named stack profiles such as Linux–Apache–MySQL–PHP (LAMP), MongoDB–Express–React–Node.js (MERN), T3 and Next.js–Vercel–Supabase may receive dated landscape entries. They should show request flow, state, trust boundaries, managed responsibility and coupling rather than act as endorsements.

Use *pets and cattle* only as historical shorthand for unique, manually tended servers versus replaceable members of an automated pool. Pair it with *snowflake server*, *phoenix server* and *immutable server*, and explain the real questions: where state lives, whether an instance can be rebuilt, what replacement depends on and how failure is detected. Do not extend the metaphor to people. Planning references: Randy Bias's history of [pets versus cattle](https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/) and Martin Fowler's [immutable server](https://martinfowler.com/bliki/ImmutableServer.html) entry.

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
- Runbooks, automation and manual recovery paths, including prerequisites, expected observations, stopping conditions, rollback, escalation and rehearsal
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
2. Authentication, authorisation, sessions, account recovery, identities and least privilege
3. Encryption, hashing, signatures, keys and certificates
4. Input validation, output encoding, interpreters and injection
5. Browser attacks, hostile files, unsafe URLs and server-side requests
6. Dependencies, software supply chains, vulnerabilities and patching
7. Personal data, minimisation, retention, deletion and security incidents

### Further territory

- Threat modelling methods and abuse cases
- Human account patterns: passkeys, federated login and generated passwords in platform or independent password managers
- Password policy, password managers, generated passwords and memorable passphrases
- Multi-factor and step-up authentication, assurance levels and phishing resistance
- Account recovery, recovery material, backup authenticators and break-glass access
- Password storage, salts, peppers and password hashing
- Passkeys, security keys, WebAuthn, federation and public-key infrastructure
- Workload identities, service accounts and short-lived credentials
- Authenticated encryption, nonces and key lifecycle
- Cross-site scripting, cross-site request forgery and Content Security Policy
- File upload handling, archive extraction and server-side request forgery
- Secrets management, rotation and sensitive telemetry
- Dependency provenance, attestations, signatures, checksums and bills of materials
- Security testing and application-security verification
- Privacy principles, data classification and impact assessments
- Audit logging and forensic evidence

### Recognition and landscape

*Landscape selection reviewed: 2026-07-31; verify current status before publication.*

Open Worldwide Application Security Project (OWASP), OWASP Top 10, OWASP Application Security Verification Standard, NIST, United Kingdom National Cyber Security Centre, Cybersecurity and Infrastructure Security Agency, FIDO Alliance, WebAuthn, Center for Internet Security, Cyber Essentials, Open Source Security Foundation (OpenSSF), Supply-chain Levels for Software Artifacts (SLSA), common identity providers, federated login, platform and independent password managers, passkeys, Dependabot, Snyk and software composition analysis.

Present human authentication as four practical account patterns: a suitable passkey; an approved federated login; a generated password in a platform password manager for low-consequence accounts; or a generated password in an independent password manager for consequential accounts. Treat the platform/independent boundary as a risk and recovery heuristic rather than an institutional standard or universal product ranking. Teach memorised credentials, MFA and recovery as separate decisions. Keep application and automation credentials under non-human identity and secrets management. Use [xkcd 936, “Password Strength”](https://xkcd.com/936/), as a qualified related observation under passwords and passphrases, not as evidence or a complete password policy. The reader-facing decision reference is [Authentication and credential management](reference/authentication-and-credential-management.md).

Treat OpenSSF as an institution and SLSA as one current framework for reasoning about software-artefact provenance, not as proof that a dependency or build is secure. Planning references: [OpenSSF: About](https://openssf.org/about/) and the versioned [SLSA specification](https://slsa.dev/spec/).

**Boundary:** security mechanisms live here; the legal and assurance categories surrounding them live in Chapter 11. Organisation-wide workforce identity governance, provider approval and joiner-mover-leaver responsibility belong to TLB.

## 10. Product, experience and analytics

**Purpose:** connect technical work to the people it serves, the evidence used to improve it and the incentives that can distort that evidence.

### First pass

1. Users, customers, stakeholders, problems and Jobs to Be Done
2. Product-market fit, minimum viable products and the prototype-production gap
3. Discovery, delivery, requirements, stories, acceptance criteria and behaviour-driven development
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

**Related delivery heuristics:** introduce INVEST as a compact check on user-story quality and SMART as a family of checks on goals, objectives or tasks inside the first-pass discussion of requirements, stories and acceptance criteria. Treat both as prompts for conversation rather than proof that the story or objective is valuable or correct. State which expansion is being used because SMART has several established variants. Planning references: Bill Wake's original [INVEST in Good Stories, and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/) and George T. Doran's 1981 article record, [*There's a S.M.A.R.T. Way to Write Management's Goals and Objectives*](https://openurl.ebsco.com/contentitem/gcd%3A6043491).

**Boundary:** implementation accessibility belongs here as a user outcome and is cross-linked from Chapter 4; organisational commitments and legal duties live in Chapter 11. Organisation-wide product leadership, portfolio management, delivery management and market or business operations belong to TLB Volume 2.

## 11. Governance, compliance and commercial readiness

**Purpose:** explain how an organisation demonstrates control, meets applicable obligations and earns trust beyond a working product.

### First pass

1. Governance, accountability and risk management: objectives, uncertainty, likelihood, consequences, treatment, ownership and residual risk
2. Laws, standards, certification schemes, assurance reports and frameworks
3. Policies, controls, evidence, change management and auditability
4. Data-protection roles, agreements and impact assessment
5. Third-party, supplier and concentration risk
6. Open-source licences, intellectual property and contracts
7. Business continuity, customer commitments and due diligence

### Further territory

- Cyber Essentials and Cyber Essentials Plus
- International Organization for Standardization/International Electrotechnical Commission (ISO/IEC) 27001 and related management-system standards
- System and Organization Controls (SOC) reports, including SOC 2 Types 1 and 2
- Payment Card Industry Data Security Standard
- National Institute of Standards and Technology (NIST) Cybersecurity Framework, Center for Internet Security (CIS) Controls and Cloud Controls Matrix
- United Kingdom and European Union data-protection regimes
- Security questionnaires and customer assurance
- Software bills of materials, Software Package Data Exchange (SPDX) and CycloneDX
- Sector-specific obligations and regulated roles
- Service commitments, remedies and evidence periods
- Capability and maturity models, staged assessments and the evidence behind ratings
- Information-technology service management, service ownership and continual improvement

### Recognition and landscape

*Landscape selection reviewed: 2026-07-31; verify current status before publication.*

International Organization for Standardization, International Electrotechnical Commission, American Institute of Certified Public Accountants, United Kingdom National Cyber Security Centre, Information Commissioner's Office, PCI Security Standards Council, Cloud Security Alliance, CMMI, COBIT, ISO/IEC 38500, ITIL, ISO/IEC 20000, regulators, accreditation bodies, certification bodies and independent auditors.

Teach general risk management as a cross-cutting decision loop. Start with an objective and context; describe a risk scenario as causes, an uncertain event and consequences; assess likelihood, consequence, timing and confidence proportionately; select treatment and preventive, detective or recovery controls; assign an owner; record the residual risk; and monitor whether assumptions and controls remain valid. Distinguish a risk from an issue, threat, vulnerability, hazard and control, and distinguish mitigation, remediation and contingency. Introduce inherent and residual risk, risk acceptance, appetite and tolerance without turning a risk matrix into false precision. Technical chapters supply concrete risks and controls; Chapter 11 owns this general method. Organisation-wide appetite, portfolio aggregation and risk governance belong to TLB. Planning references: [ISO 31000:2018](https://www.iso.org/standard/65694.html), HM Treasury's [Orange Book](https://www.gov.uk/government/publications/orange-book/the-orange-book-management-of-risk-principles-and-concepts) and [NIST SP 800-30 Revision 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final).

Teach maturity and capability models as the durable concept; use CMMI only as a named example and do not imply that a rating proves product quality. Distinguish organisational maturity from capability in an individual practice area, and verify the current level definitions before publication. Planning references: [CMMI levels](https://cmmiinstitute.com/learning/appraisals/levels) and [ISO/IEC 33001 process-assessment concepts](https://www.iso.org/standard/54175.html).

Teach information-technology governance and service management before naming their frameworks. Planning references: [ISO/IEC 38500:2024 governance of IT](https://www.iso.org/standard/81684.html), [ISACA's COBIT overview](https://www.isaca.org/resources/cobit), the [ISO/IEC JTC 1/SC 40 overview of IT service management and ISO/IEC 20000](https://committee.iso.org/home/jtc1sc40) and the official [ITIL framework overview](https://www.peoplecert.org/Organizations/Certifications/ITIL-Corporate-Framework).

Current schemes and organisations may receive dated entries. Always state whether an item is law, guidance, a standard, a certification scheme, a control framework or an assurance report.

**Boundary:** technical controls live in Chapters 7–9; this chapter explains the applicability, governance, evidence and external trust required around a software product. Organisation-wide technology governance, workplace information technology, service management, budgets, sourcing and leadership belong canonically to TLB Volume 2; named frameworks may remain here for recognition where they help a software builder understand an external obligation or assurance request.

## 12. Artificial intelligence-assisted engineering

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
- Artificial intelligence-generated documentation, source grounding, factual verification, tested examples, version scope and sensitive-data control
- Local models, hosted models and hardware requirements
- Artificial intelligence incident handling and abuse monitoring
- Model application programming interface, retrieval and agent stack profiles

### Recognition and landscape

*Landscape selection reviewed: 2026-07-17; verify current status before publication.*

OpenAI, Anthropic, Google Gemini, Meta Llama, GitHub Copilot, Cursor, Claude Code, Codex, model APIs, local inference runtimes, vector databases and evaluation platforms.

The canonical distinction is not whether artificial intelligence wrote the code. It is whether the person responsible can independently model, inspect, constrain, verify and recover the system. TFB supplies mechanism awareness and escalation cues, not proof of correctness.

Apply the same distinction to generated documentation. Artificial intelligence can draft, translate and restructure prose cheaply, but fluency and controlled language do not prove that a claim, command, interface, citation or version is correct. Require a responsible owner, authoritative sources, review against code, configuration, schemas and observed behaviour, testing of commands and examples, and proportionate provenance and disclosure. Planning references: [Microsoft's principles for AI-generated documentation](https://learn.microsoft.com/en-us/principles-for-ai-generated-content) and the [NIST Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1).

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

Hacker Laws, the Jargon File, Joel on Software, Unix philosophy, the single-responsibility, open–closed, Liskov-substitution, interface-segregation and dependency-inversion (SOLID) principles, hacker folklore, the Bitter Lesson, *rubber-duck debugging*, *footgun*, *bus factor*, *yak shaving*, *cruft*, *kludge*, *spaghetti code*, *bug-compatible*, *quick-and-dirty*, *Real Soon Now*, *thundering herd*, *poison message*, *dead-letter queue*, *golden path*, *paved road*, *toil*, *works on my machine*, *Friday deploy*, *dogfooding*, *cargo cult*, *hero culture*, *break glass* and *alert fatigue*.

Technical laws keep their canonical homes: Amdahl's Law in [Chapter 1](#1-computing-foundations), Hyrum's Law in [Chapter 4](#4-the-internet-web-and-application-programming-interfaces), CAP and PACELC in [Chapter 6](#6-architecture-and-distributed-systems), Kerckhoffs's principle in [Chapter 9](#9-security-privacy-and-identity), and Fitts' and Hick-Hyman Laws in [Chapter 10](#10-product-experience-and-analytics).

Humorous and historical terms are welcome when they help a reader remember a real mechanism. Explain them without sanding off all their personality, but state their scope and do not treat a joke as evidence.

Route each retained cultural term to its technical home: for example, *bus factor* to Chapter 3, *thundering herd* and *poison message* to Chapter 6, *pets and cattle* to Chapter 7, *toil* and *alert fatigue* to Chapter 8, and *break glass* to Chapter 9. Chapter 13 provides recognition and cross-links, not duplicate definitions. Retain a term only when a reader is reasonably likely to encounter it and it clarifies a mechanism, a common misunderstanding or a technical conversation. Add it to the glossary when it appears in published prose. Google's [definition of toil](https://sre.google/sre-book/eliminating-toil/) is one planning reference for the operational vocabulary.

**Boundary:** named results with a clear technical home are taught in that chapter and may be collected here only as cross-links. Chapter 13 supplies cross-cutting judgement rather than becoming a miscellaneous bin.

## Reference guides

Reference guides consolidate navigation without becoming additional canonical explanations or an exhaustive bibliography. The Markdown pages are the fuller living references. A later book edition may select concise, prioritised versions as appendices or back matter, but should not reproduce each online page automatically.

### Institutions and sources of authority

Plan a reader-facing index organised by function and domain rather than prestige. Distinguish standards bodies, public authorities, regulators, open-source foundations, framework owners, professional bodies, certification and accreditation bodies, and commercial vendors. Each retained entry should state what the organisation publishes or governs, why a builder may encounter it, what authority it does and does not have, its canonical TFB context and an official source. Apply the living-landscape review rule where ownership, scope or status can change.

### Curated further reading

Plan a thematic guide to the strongest books, courses, standards, specifications and maintained online resources. Use practical priority labels such as **Start here**, **Continue** and **Reference**, with a short explanation of the value, level and limitations of each item. Select from the strongest per-entry reading rather than copying every chapter list or publishing a comprehensive canon. Verify editions, links and current scope before inclusion.

### Authentication and credential management

Maintain a practical decision reference for human account patterns, memorised credentials, MFA, recovery and non-human identities. Label the four-pattern model as a TFB synthesis, distinguish user credential storage from service-side password storage, and retain authoritative links to NIST, NCSC, OWASP and CISA. Keep the canonical explanations in Chapters 7 and 9. The current page is [Authentication and credential management](reference/authentication-and-credential-management.md).

The completed pages live under `reference/` and link back to canonical chapters and entries. Chapter explanations and their local further-reading lists remain authoritative for context; reference guides provide alternative ways to browse them. Select printed back matter only after the chapters are visible, favouring material that benefits from consolidated lookup: the glossary, a compact authentication decision guide, an institutions-and-authorities index and a small thematic further-reading guide. Keep fuller, frequently updated or catalogue-like material online.

## Whole-guide dependency spine

The guide supports selective browsing, but the first-pass traversal has a useful dependency direction:

1. Representations and machine limits make programming behaviour intelligible.
2. Programming structures make software-engineering controls intelligible.
3. Networks and data provide the components used by architecture.
4. Architecture explains what infrastructure deploys and operations observes.
5. Security, product and governance apply constraints and purpose across the whole system.
6. Artificial intelligence-assisted engineering reuses all preceding controls rather than replacing them; its material consequences also appear throughout the earlier chapters.
7. Laws and judgement provide compact cross-links across every chapter.

Cross-links should allow a reader to enter anywhere without requiring strict sequential study.

## Maintenance rule for living landscape material

Every product, vendor, organisation, protocol status, standard edition or scheme description that can materially change must have a dated note in the private research repository or a `Reviewed: YYYY-MM-DD` marker in its landscape entry. Maintenance should prioritise:

1. correctness of category and responsibility;
2. current status, ownership and deprecation;
3. changed limits, names or product boundaries;
4. broken or superseded references;
5. whether the name still deserves space for the target reader.

An automatic maintenance harness may later identify stale review dates, changed links, new editions, renamed products, deprecations and source changes, and may propose bounded updates. Human editorial judgement remains responsible for interpreting the evidence, approving the wording and deciding whether a current item still belongs.
