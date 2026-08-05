# Chapter 7: Infrastructure, cloud and delivery

Infrastructure is the part of a system that turns source code into a running service for real people. It includes the places software runs, the configuration and authority it receives, the artefacts that are promoted, and the limits imposed by providers and physical resources. A platform can conceal much of this work; it cannot remove the underlying responsibilities.

This chapter follows one distinction that is useful when investigating a release or an incident:

`source → build artefact → release → deployment → runtime → recovery`

**Source** is editable code and configuration. A **build artefact** is a particular output made from it, such as a package, executable, container image or static site bundle. A **release** selects an artefact and target configuration. A **deployment** changes an environment so that the release can run. **Runtime** is the live system, its data, dependencies and traffic. **Recovery** restores a safe or useful state after a failed change or incident. A hosted platform may combine these steps, but it does not make the distinctions disappear.

The focus is where software runs and how it changes. Architectural decomposition belongs in [Chapter 6](06-architecture-and-distributed-systems.md); operating a live service and proving recovery belong in Chapter 8; security and identity mechanics belong in Chapter 9; and supplier contracts and assurance belong in Chapter 11.

## Chapter map

The first pass covers:

1. [Environments are evidence boundaries](#environments-are-evidence-boundaries)
2. [Configuration is not authority](#configuration-is-not-authority)
3. [Compute has layers](#compute-has-layers)
4. [Managed changes the boundary](#managed-changes-the-boundary)
5. [Artefacts make change traceable](#artefacts-make-change-traceable)
6. [Delivery depends on compatibility](#delivery-depends-on-compatibility)
7. [Capacity and coupling have limits](#capacity-and-coupling-have-limits)

## Environments are evidence boundaries

*Development, test, staging and production are separate contexts with different dependencies, data and consequences.*

### What they are

An **environment** is a deliberately separate context in which software runs against particular configuration, identities, data and dependencies. Development supports fast learning. Production serves real users and can create real obligations. Test and staging environments sit between them when they allow a team to examine a defined property before exposing it to production.

The same order application might use test payment credentials locally, a provider sandbox during integration testing and real payment access only in production. Its source code can be identical while addresses, permissions, data volume, traffic and external effects differ. A test result therefore establishes something specific: for example, that the application can authenticate to a payment sandbox. It does not establish that every production permission, dependency or traffic pattern is safe.

The [Twelve-Factor App's dev/prod parity principle](https://12factor.net/dev-prod-parity) is a useful direction: reduce avoidable gaps between development, staging and production. It does not require identical copies. Production-scale data, real customers and every third-party failure cannot safely be recreated elsewhere.

### Why a builder needs to know this

Environment names often appear in deployment screens, URLs, configuration files and incident reports. Knowing what an environment is lets you ask which behaviour a test actually exercised, which data it used and which production property remains untested. AI can generate a plausible local stack and test fixtures rapidly. That increases the risk of mistaking local success for production evidence.

### Pitfalls

- **“Staging is production-like.”** The label says nothing about the properties under test.
- **“Copy production data to test.”** That creates a new privacy, access and retention boundary.
- **“A passing test environment will stay the same.”** Shared environments can change between a result and a release.
- **“An environment is one URL or account.”** One user journey can cross several services with separate configurations.

### Related concepts in TFB

- [Testing, verification and evidence](03-software-engineering.md#testing-verification-and-evidence) - a test has value only relative to the behaviour it establishes.
- [Service APIs and behavioural contracts](04-internet-web-and-apis.md#service-apis-and-behavioural-contracts) - a sandbox and production provider can have materially different contracts.
- [System context, boundaries, components and architecture views](06-architecture-and-distributed-systems.md#system-context-boundaries-components-and-architecture-views) - an environment can contain several system boundaries.

### Deeper concepts

- Test doubles and contract testing - making the scope of an external-integration test explicit.
- Ephemeral preview environments and synthetic data - reducing shared-environment and data-exposure risks.
- Production verification - gathering evidence after a release without treating production as an uncontrolled test bed.

### Further reading

- [The Twelve-Factor App: Dev/prod parity](https://12factor.net/dev-prod-parity) - the original compact account of reducing environmental gaps.
- [Google SRE: Testing for reliability](https://sre.google/sre-book/testing-reliability/) - how a reliability test needs an explicit model of its property.

## Configuration is not authority

*Configuration selects behaviour; workload identity supports authentication; policy determines allowed actions.*

### What it is

**Configuration** tells software which non-secret choices apply in an environment: for example, a service address, a feature setting or a region. A **workload identity** names the running software making a request. A **credential** supplies evidence used to authenticate an identity, while policy authorises that identity to perform stated actions. Some credentials and encryption keys are **secrets** because disclosure could enable impersonation or expose protected data. These values perform different jobs even when software represents them all as strings.

One order-service image can receive a database address as configuration and a platform-issued identity. Policy can allow that identity to connect to one database. If an external service still requires a secret credential, the platform can authenticate the workload and inject the secret only into that runtime, or let it retrieve the secret from a controlled service. The delivery path should make the readers, persistence, lifetime and revocation boundary clear. Storing the value in source, an artefact or a persistent parent-shell environment spreads it beyond the target workload.

Where a platform supports it, prefer platform-issued or federated workload identity and short-lived, narrowly authorised credentials. The [SPIFFE Workload API](https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_api/) illustrates a vendor-neutral way for a workload to obtain cryptographic identity; it is not required for ordinary projects. Keep secrets out of source, artefacts, images, state files and diagnostics.

### Why a builder needs to know this

Configuration appears harmless because it is commonplace, while authority determines what a compromised or mistaken process can do. Configuration parity means that each environment exposes the *shape* of settings and permissions required by the software. It does not mean that development receives production values, data or authority. A developer should not need production access merely to start an application locally.

Agentic build and deployment systems create more processes that may receive authority. An agent able to edit code does not thereby need a broad permanent secret. Identify each pipeline or runtime workload, its stated action and the minimum authority it needs; inspect non-secret identity and audit evidence afterwards.

### Pitfalls

- **“An environment variable solves secrets management.”** It is a transport mechanism that surrounding tooling can inherit, persist or expose.
- **“A secret identifies the process.”** Possession alone does not prove which workload used it or whether it should have its authority.
- **“Same configuration means same values.”** Equal production authority in lower environments is unsafe.
- **“A secret manager makes copies harmless.”** Build logs, images, state and backups can still enlarge the exposure boundary.

### Related concepts in TFB

- [Abstraction, information hiding and interfaces](03-software-engineering.md#abstraction-information-hiding-and-interfaces) - configuration makes environmental variation explicit at an interface.
- [Service APIs and behavioural contracts](04-internet-web-and-apis.md#service-apis-and-behavioural-contracts) - credentials and identity affect who may use an API.
- [Partial failure and the fallacies of distributed computing](06-architecture-and-distributed-systems.md#partial-failure-and-the-fallacies-of-distributed-computing) - identity and configuration delivery are remote dependencies too.

### Deeper concepts

- OpenID Connect federation, service accounts and SPIFFE/SPIRE - ways workloads establish and exchange identity.
- Credential rotation and revocation - limiting the lifetime of compromised authority.
- Policy as code and secret-manager integration - making authority and sensitive delivery reviewable.

### Further reading

- [The Twelve-Factor App: Config](https://12factor.net/config) - separating deploy-varying configuration from code.
- [SPIFFE identity specification](https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/) - a portable workload-identity model.
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) - why identity and policy are a more useful boundary than implicit network location.

## Compute has layers

*Servers, virtual machines, containers and serverless platforms are different arrangements for running code on the same underlying hardware.*

### What they are

Every running program ultimately uses physical hardware. A physical server gives its operator direct control of that hardware. A **virtual machine** (VM) uses a hypervisor to present a virtual computer with its own operating system to a tenant. A **container** packages an application and its user-space dependencies while sharing the host operating-system kernel; it is not a small VM. The [Open Container Initiative image specification](https://github.com/opencontainers/image-spec) defines a portable image format, while its [runtime specification](https://github.com/opencontainers/runtime-spec) describes how a compatible runtime executes a filesystem bundle.

**Serverless** normally means that a provider starts and scales a function or managed runtime in response to requests or events. The builder still supplies code, configuration, permissions, dependency choices and resource bounds; the provider controls more placement and host operation. Long-running work, connections, local files and background effects can behave differently from an always-running process.

### Why a builder needs to know this

These forms change the packaging, isolation, lifecycle and operating work left to the builder. A generated deployment template can conceal its compute assumption. Before accepting one, ask whether the workload needs a persistent process, local state, a long-lived connection, an operating-system capability or a predictable warm runtime. Each answer narrows the suitable form.

### Pitfalls

- **“A container is a security boundary.”** Its isolation depends on the host, runtime and configuration.
- **“Serverless has no servers or operations.”** It still has provider limits, latency, cost, permissions and dependencies.
- **“Stateless requests have no state.”** State has moved to a database, object store, queue, cache or external service.
- **“An instance can always be replaced.”** Its state, configuration, identity and startup dependencies must exist elsewhere first.

### Related concepts in TFB

- [Operating systems and running programs](01-computing-foundations.md#operating-systems-and-running-programs) - a compute form still runs processes with finite resources.
- [Variables, state, mutability and side effects](02-programming-foundations.md#variables-state-mutability-and-side-effects) - replacing a process is safe only when its needed state is elsewhere or recoverable.
- [Monoliths, services, and stateful and stateless components](06-architecture-and-distributed-systems.md#monoliths-services-and-stateful-and-stateless-components) - deployment form and system decomposition are separate decisions.

### Deeper concepts

- Hypervisors, Linux namespaces and cgroups - mechanisms behind VM and container isolation.
- Orchestration, autoscaling, cold starts and graceful shutdown - how platforms manage workload lifecycles.
- Immutable and replaceable infrastructure - treating instances as rebuildable rather than manually unique.

### Further reading

- [NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final) - cloud service models and the shared-resource context.
- [OCI Image Specification](https://github.com/opencontainers/image-spec) - the standard image boundary for containers.
- [AWS Lambda developer guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) - a current serverless example; its limits are product-specific.

## Managed changes the boundary

*Cloud regions and managed services move operational work between customer and provider; they do not make responsibility vanish.*

### What they are

Cloud computing makes pooled computing resources available on demand. A **region** is a provider-defined geographic and operational grouping. Its internal failure boundaries, service availability and data paths are provider-specific. A more durable map is by function: identity and policy; networking and edge; compute; storage and databases; messaging and integration; configuration and secrets; observability and operations; and build and delivery.

A managed database might run in a chosen region and provide a defined combination of patching, backups or replication. The provider operates some layers. The customer still chooses data classification, access policy, schema, client behaviour, retained data, integrations, monitoring and an appropriate service configuration. Self-hosting reverses more of that operational allocation; it does not automatically provide more control or reliability in practice.

**Shared responsibility** is useful only when it names the boundary. For each property, ask who configures it, operates it, supplies evidence for it and bears the consequence if it fails. The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) is a readable provider example, not a universal contract.

Current products can be translated by the scope they bundle. The categories overlap and do not imply equivalent features or guarantees.

| Rough scope | Recognition examples | What the builder assembles |
| --- | --- | --- |
| Broad infrastructure cloud | Amazon Web Services, Microsoft Azure, Google Cloud | Several primitives across the provider-neutral map |
| Application or edge platform | Cloudflare, Vercel, Netlify, Heroku, Render, Fly.io | A selected combination of network, compute, build and delivery functions |
| Managed application backend | Supabase, Firebase | A selected combination of data, identity, storage and integration functions |

Software-as-a-service products often expose tenants or organisations, roles, entitlements, billing, application programming interface keys, webhooks, audit trails, single sign-on and System for Cross-domain Identity Management. These are recurring building blocks, not a second architecture. The Cloud Native Computing Foundation (CNCF) project lifecycle can signal that a project has met defined governance and maturity expectations at a particular stage; inclusion or graduation does not prove that the project fits a system. Landscape reviewed: 2026-08-03.

### Why a builder needs to know this

A provider software development kit or generated configuration can add a dependency before its consequences are visible. Record the provider, region, data types, delegated operations, access path and exit constraints. This makes the decision reviewable without turning the chapter into a product ranking.

### Pitfalls

- **“A region proves residency, legal suitability or recovery independence.”** Check the service, data path and contract.
- **“Managed means secure or compliant.”** The stated layer may still leave access, configuration, data and recovery to the customer.
- **“Products in the same category are equivalent.”** Labels such as gateway, database, edge and serverless often cover different boundaries.
- **“Self-hosted means independent.”** It adds patching, availability, incident and evidence obligations.

### Related concepts in TFB

- [The journey of a request](04-internet-web-and-apis.md#the-internet-internet-protocol-transport-ports-and-the-journey-of-a-request) - networking and edge products sit on the request path.
- [Data models, schemas, identifiers and missing values](05-data-and-databases.md#data-models-schemas-identifiers-and-missing-values) - a managed database still stores product meanings and rules.
- [Controlling overload and containing failure](06-architecture-and-distributed-systems.md#controlling-overload-and-containing-failure) - provider boundaries can be failure and capacity boundaries.

### Deeper concepts

- Availability zones, multi-region design and control/data planes - distinguishing placement from independent operation.
- Virtual networking and service-level agreements - provider-specific network and service commitments.
- Data-processing terms and supplier assurance - the contractual evidence around a technical service.

### Further reading

- [NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final) - durable cloud characteristics and service-model vocabulary.
- [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) - an example of responsibility varying by service.
- [Cloud Native Computing Foundation: Who we are](https://www.cncf.io/about/who-we-are/) - recognition context for a neutral open-source foundation, not a product recommendation.
- [CNCF project lifecycle](https://contribute.cncf.io/projects/lifecycle/) - the defined expectations and limits of lifecycle stages.

## Artefacts make change traceable

*A known build output, controlled registry and reviewable infrastructure definition connect an intended change to the system that receives it.*

### What they are

A **build artefact** is the specific output that runs: a package, executable, container image or static-site bundle. A **registry** stores and serves such artefacts. **Infrastructure as code** (IaC) expresses intended resources in versioned configuration, then uses a tool to compare, plan and apply changes against a real environment. It improves repeatability only when access, the real state and proposed changes are also controlled.

An application build can produce an Open Container Initiative (OCI) image identified by an immutable content digest. A deployment selects that known output rather than rebuilding separately for each environment. The registry's access, retention and integrity controls then matter because it serves the deployed artefact.

With IaC, configuration declares resources and their relationships: perhaps a database, workload identity and application runtime. A plan or preview compares desired configuration, tool state and provider observations before applying a change. [Terraform's state documentation](https://developer.hashicorp.com/terraform/language/state) explains that state records resources it manages. If manual changes diverge from configuration, later reconciliation can replace or destroy resources unexpectedly. State can reveal sensitive operational information, so it is part of the control boundary rather than harmless metadata.

IaC aims for **idempotent** convergence: applying unchanged intent again should not create a second copy of each resource. It cannot make provider operations reversible. Restoring an earlier configuration may recreate infrastructure, but it does not restore deleted data or the former state of an external system.

### Why a builder needs to know this

Source revision, build artefact and deployed release are different identifiers. A Git commit alone does not prove what ran. This distinction helps a builder trace a production change and interrogate generated IaC: what will apply it, under which authority, and what human-readable plan supports it? Preserve non-secret evidence that joins approved source, build, artefact and deployment.

### Pitfalls

- **“The current branch is the deployed system.”** It may not identify the built artefact or target configuration.
- **“`latest` identifies an image.”** A mutable tag can later refer to different content.
- **“A clean plan is safe.”** A plan has a limited model, can become stale and can correctly propose a destructive action.
- **“IaC removes drift and privilege.”** It creates another control path for them.
- **“A digest proves an artefact is trustworthy.”** It proves byte identity. Build authority and registry write access determine who could introduce those bytes; origin and safety need separate provenance evidence.

### Related concepts in TFB

- [Version control, code review, shared ownership and recovery](03-software-engineering.md#version-control-code-review-shared-ownership-and-recovery) - source history is necessary evidence but not the entire release record.
- [Schema evolution, online migrations and backfills](05-data-and-databases.md#schema-evolution-online-migrations-and-backfills) - database changes need evidence and compatible sequencing too.
- [System context, boundaries, components and architecture views](06-architecture-and-distributed-systems.md#system-context-boundaries-components-and-architecture-views) - deployed resources are evidence for a deployment view.

### Deeper concepts

- Reproducible builds, provenance and attestations - linking a build output to its origin.
- Software bills of materials and image signing - inspecting and asserting artefact contents.
- Policy as code, state backends and drift detection - governing infrastructure changes and their records.

### Further reading

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) - the registry interface for OCI artefacts.
- [Terraform: state](https://developer.hashicorp.com/terraform/language/state) - why an IaC tool records managed resources.
- [Terraform: resource drift](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) - how manual changes and declared intent diverge.
- [SLSA specification](https://slsa.dev/spec/v1.1/) - deeper vocabulary for build provenance and supply-chain boundaries.

## Delivery depends on compatibility

*A deployment changes a live system that may contain old code, new code, persistent data and external effects at the same time.*

### What it is

**Continuous delivery** keeps software in a state that can be released safely on demand. **Continuous deployment** automatically releases changes that meet its stated conditions. Neither merely means that a build runs after every commit. Delivery needs evidence that a particular artefact, configuration and sequence of change can coexist with the current running system and data.

Compatibility matters because old and new versions can overlap. An application change that adds a required database column cannot assume that every old process stops before every new process starts. A safer sequence can expand the schema, deploy code that accepts both forms, migrate traffic or data, and remove the old form only afterwards. The sequence is a design property, not a feature supplied by a deployment button.

**Rollback** restores an earlier application or infrastructure version when that reverses the harm. It cannot automatically undo an email, captured charge, destructive migration, external event or incompatible record already written. Those effects require **recovery**: a decision to halt, compensate, reconcile, restore, communicate or make a compatible forward fix. Chapter 8 addresses the evidence and operational work needed to prove recovery.

### Why a builder needs to know this

A green build says only that selected checks passed. A deployment success says that a platform accepted a change. Neither proves that real requests, permissions, dependencies and data are healthy. AI can generate many small changes and trigger them frequently; that makes explicit artefact selection, compatibility and irreversible effects more important, not less.

### Pitfalls

- **“A successful deployment proves the release is healthy.”** It does not establish user-visible behaviour or dependency health.
- **“Rollback is recovery.”** Earlier code cannot reverse every earlier effect.
- **“Canary, rolling or blue-green means safe.”** These rollout patterns change exposure; none removes compatibility work.
- **“A backup makes a release reversible.”** Restore must be tested and reconciled with valid later writes.

### Related concepts in TFB

- [Testing, verification and evidence](03-software-engineering.md#testing-verification-and-evidence) - build checks provide selected evidence, not universal proof.
- [Service APIs and behavioural contracts](04-internet-web-and-apis.md#service-apis-and-behavioural-contracts) - clients and servers can overlap across compatible versions.
- [Schema evolution, online migrations and backfills](05-data-and-databases.md#schema-evolution-online-migrations-and-backfills) - data migrations make old/new compatibility visible.
- [Synchronous calls, asynchronous messages, queues, streams and events](06-architecture-and-distributed-systems.md#synchronous-calls-asynchronous-messages-queues-streams-and-events) - queued work can outlive the version that produced it.

### Deeper concepts

- Progressive delivery, feature flags and dark launches - limiting exposure while gathering defined evidence.
- Expand/contract migrations and release orchestration - sequencing compatible software and data change.
- Readiness checks and compensating actions - recognising when a runtime is ready and what to do with irreversible effects.

### Further reading

- [ContinuousDelivery.com](https://continuousdelivery.com/) - the original definition and rationale for repeatable, low-risk releases.
- [Google SRE: Canarying releases](https://sre.google/workbook/canarying-releases/) - staged exposure and its operational limits.
- [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) - a concrete rollout mechanism whose exact behaviour is not portable to every platform.

## Capacity and coupling have limits

*Cloud resources, provider quotas and commercial terms constrain a system even when it can scale automatically.*

### What they are

Infrastructure is bounded by capacity, provider quota and a commercial model. **Vendor coupling** is the cost of changing a dependency because the application, data, operations, contracts or skills rely on its distinctive behaviour. **Portability** is therefore layered, not binary. An **exit plan** is a tested hypothesis about what must move, be replaced or be accepted if a provider becomes unsuitable.

An application can have enough compute but be limited by database connections, a third-party API rate limit, accelerator capacity, build minutes, function concurrency, egress bandwidth or an account quota. Autoscaling cannot exceed a quota, repair a slower dependency or make an unaffordable demand pattern viable. Prices commonly combine time, requests, storage, data transfer, commitments and support, while the billing unit may not match the unit that creates user value.

A container image can run on more than one platform while its identity model, managed database queries, queues, observability data, export format, network policy and operating procedures remain coupled. A useful first exit hypothesis names the provider-specific services, data export/import route, Domain Name System and identity dependencies, retained backups, alternative operating model, acceptable downtime and expected rework. It need not require a parallel second provider.

### Why a builder needs to know this

Capacity and coupling are technical choices with continuing business consequences. Quotas can block deployment, recovery or traffic handling at the moment demand rises. AI workloads add potentially variable model, tool-call and accelerator consumption. Generated architecture should expose its quota and cost drivers rather than treating a current free tier or default limit as a guarantee. Exact quotas, prices and terms are time-sensitive: check them at the decision point. Reviewed: 2026-08-03.

### Pitfalls

- **“Cloud is elastic.”** Capacity is neither instant, unbounded nor necessarily affordable.
- **“Quotas are only billing controls.”** They can stop traffic handling and recovery.
- **“Avoid proprietary features.”** Avoiding every distinctive service can cost more reliability and attention than the risk it avoids.
- **“A backup is an exit route.”** An opaque format may be neither restorable nor exportable elsewhere.
- **“Multi-cloud is an exit plan.”** It can duplicate complexity and shared application faults without proving a workable move.

### Related concepts in TFB

- [Latency and throughput](01-computing-foundations.md#latency-and-throughput) - throughput and waiting work expose resource limits.
- [Controlling overload and containing failure](06-architecture-and-distributed-systems.md#controlling-overload-and-containing-failure) - dependencies and capacity limits can spread a failure.
- [Data models, schemas, identifiers and missing values](05-data-and-databases.md#data-models-schemas-identifiers-and-missing-values) - portable data needs defined meaning as well as an export format.

### Deeper concepts

- Service quotas, data egress and FinOps - relating provider limits and consumption to workload value.
- Open formats and migration rehearsal - testing an export and move rather than assuming one is possible.
- Business continuity and concentration risk - deciding which provider failures matter to the service.

### Further reading

- [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) - a concrete account and resource-limit model; exact quotas vary by service and region.
- [FinOps Framework](https://www.finops.org/framework/) - a current discipline for connecting technical consumption, cost and value.
- [NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final) - durable vocabulary for cloud service models.

[Previous: Chapter 6 - Architecture and distributed systems](06-architecture-and-distributed-systems.md) · [Return to the guide map](../README.md)
