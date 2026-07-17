# Chapter 3: Software engineering

Writing code creates behaviour. Software engineering makes that behaviour easier to understand, change and recover as a project grows. It connects intended outcomes to boundaries, evidence, recorded changes and feedback, so that neither a human nor an artificial intelligence (AI) has to rely on plausible-looking code alone.

The starting assumption is that you have a real software project and recognise the programming ideas in [Chapter 2](02-programming-foundations.md). Each entry stands on its own. Together they follow a controlled change from stating its intent through testing, review and integration to the long-term evolution of an existing system.

## Chapter map

The first pass covers:

1. [Functional requirements, quality attributes, specifications and invariants](#functional-requirements-quality-attributes-specifications-and-invariants)
2. [Modularity, cohesion, coupling and separation of concerns](#modularity-cohesion-coupling-and-separation-of-concerns)
3. [Abstraction, information hiding and interfaces](#abstraction-information-hiding-and-interfaces)
4. [Testing, verification and evidence](#testing-verification-and-evidence)
5. [Version control, code review, shared ownership and recovery](#version-control-code-review-shared-ownership-and-recovery)
6. [Build automation, continuous integration and fast feedback](#build-automation-continuous-integration-and-fast-feedback)
7. [Refactoring, technical debt, legacy systems and evolutionary replacement](#refactoring-technical-debt-legacy-systems-and-evolutionary-replacement)

## Functional requirements, quality attributes, specifications and invariants

*A change is easier to build and assess when its intended behaviour and important constraints are visible.*

### What they are

A **functional requirement** states a capability or behaviour the system must provide: for example, “a customer can transfer money between two accounts”. A **quality attribute requirement** describes how well the system must behave or a property it must have, such as security, reliability, accessibility, performance or maintainability. Calling these properties “non-functional” does not make them optional.

A **specification** records expected properties and constraints precisely enough to guide construction and evaluation. It might be prose, examples, acceptance criteria, a definition of permitted data structure, an interface contract or a mathematical description; it need not be one large document. A useful specification separates two questions: would these stated properties meet the real need, and does the built system have those properties?

An **invariant** is a condition that must remain true in every valid state covered by the design. For a transfer, “money is not silently created or lost” is an invariant. Authorised access, an acceptable response time and recovery after failure are quality requirements. Valid amounts and the required effect on both balances belong in the specification. These statements give design and [testing](#testing-verification-and-evidence) something concrete to examine.

Requirements are maintained knowledge, not predictions made once at the start. Discovery can change them, but the change should be explicit so that the implementation and its evidence can change with them.

### Why a builder needs to know this

Builders meet these ideas in feature descriptions, database constraints, interface contracts, test cases, operational targets and security or privacy rules. Without them, a person or AI can produce reasonable code while silently choosing the wrong behaviour, failure policy or trade-off.

Words such as “fast”, “secure”, “scalable” and “user-friendly” name aspirations until the relevant context and acceptable outcome are clearer. A feature list can also omit recovery, compatibility, accessibility and operation. Ask what must happen, what must never happen, under which conditions, and what observation would count as evidence.

### Pitfalls

- **“A requirement must dictate the implementation.”** That can hide the underlying need and exclude better designs.
- **“Passing the examples proves the invariant.”** Examples cover particular cases, not every reachable state.
- **“Formal-looking words make a statement precise.”** Writing `MUST` does not remove ambiguity or make a claim verifiable.
- **“The specification cannot change.”** Learning should update it deliberately rather than leave code and expectations inconsistent.

### Related concepts in TFB

- [Values, types and conversions](02-programming-foundations.md#values-types-and-conversions) - implementation types can express some constraints but do not discover the real requirement.
- [State, mutability and side effects](02-programming-foundations.md#variables-state-mutability-and-side-effects) - invariants constrain which state changes are valid.
- [Latency and throughput](01-computing-foundations.md#latency-and-throughput) - quality requirements need measurable context rather than “fast”.

### Deeper concepts

- Requirements traceability - connecting a claim to design, implementation and evidence as each changes.
- Formal specification and model checking - describing and exploring system behaviours mathematically.
- Acceptance criteria - representative, observable conditions used to discuss whether work meets an expectation.

### Further reading

- [NASA: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) - practical tests for clear, necessary and verifiable requirements.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) - a product-quality model showing that quality has several dimensions.
- [Leslie Lamport: Proving Safety Properties](https://lamport.org/tla/proving-safety.pdf) - a deeper account of invariants and what proving one means.

## Modularity, cohesion, coupling and separation of concerns

*Useful boundaries give a change a comprehensible home and limit what else it can disturb.*

### What they are

**Modularity** divides a system into parts with understandable responsibilities and controlled relationships. A file, folder, class, package or service is not automatically a good module: the important questions are which decisions the boundary contains and what other parts must know about them.

**Cohesion** asks whether the things inside a module belong together. **Coupling** asks how much one module depends on the details or behaviour of another. High cohesion and low coupling are useful directions for judgement, not scores to maximise blindly. A cohesive payment module, for example, might own payment decisions while exposing a narrow way for order code to request a charge. If it also formats email and knows a carrier's private data format, it has unrelated reasons to change.

**Separation of concerns** is a way of reasoning about one important aspect at a time while remembering that the final system must satisfy them together. Security, persistence or user-interface concerns may cross several modules, and one module may participate in several concerns. Separation in thought does not always imply a separate deployed service.

### Why a builder needs to know this

Boundaries influence how far a failure or mistaken change can spread, the context a person or agent must load, what can be tested independently and how many components or people must coordinate. Builders encounter them in [functions and modules](02-programming-foundations.md#modules-packages-and-dependencies), libraries, repositories and networked services.

A useful warning sign is knowledge crossing a boundary: order code reaches into payment storage, two modules depend on each other's internals, or a small change requires edits across many unrelated places. The answer is not necessarily more pieces. The aim is to place related decisions together and make necessary relationships explicit.

### Pitfalls

- **“More modules mean better design.”** Tiny parts can replace internal complexity with navigation, configuration and dependency complexity.
- **“One function does one thing defines cohesion.”** Reasons to change and domain responsibility are more informative than counting tasks.
- **“Removing all duplicated text reduces coupling.”** Similar-looking code can represent concepts that should evolve independently.
- **“A microservice is automatically modular.”** A network boundary can add latency, failure and operational coupling without hiding a coherent decision.

### Related concepts in TFB

- [Control flow, functions and scope](02-programming-foundations.md#control-flow-functions-and-scope) - functions are small boundaries around computation, names and effects.
- [Modules, packages and dependencies](02-programming-foundations.md#modules-packages-and-dependencies) - packaging provides mechanisms; modularity judges the responsibilities and relationships they contain.
- [Abstraction, information hiding and interfaces](#abstraction-information-hiding-and-interfaces) - the next entry explains what a module exposes and conceals.

### Deeper concepts

- Dependency direction and cycles - how relationships constrain which parts can change independently.
- The Law of Demeter - a heuristic for limiting knowledge of distant internals.
- Service boundaries - applying modularity across processes and network failures.

### Further reading

- [D. L. Parnas: On the Criteria To Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623) - the original argument for boundaries around decisions likely to change.
- [Stevens, Myers and Constantine: Structured Design](https://doi.org/10.1147/sj.132.0115) - the foundational cohesion and coupling vocabulary.
- [Edsger W. Dijkstra: On the role of scientific thought](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html) - separation of concerns as a reasoning technique.

## Abstraction, information hiding and interfaces

*A good boundary exposes what callers need while containing knowledge they should not have to carry.*

### What they are

An **abstraction** presents a useful model and set of operations while suppressing details that are irrelevant at that level. It reduces how much a caller must understand at once; it does not remove the underlying mechanism.

**Information hiding** is the design decision to keep particular knowledge behind a boundary, especially decisions likely to change. A language's `private` field can help enforce that decision, but the keyword alone does not create a coherent abstraction.

An **interface** is the part another component is allowed to depend on: operation names, inputs, outputs, errors, effects and behavioural promises. Here the term means an in-process module or library boundary, rather than only a user interface or a network application programming interface.

Consider storage code that offers `save` and `load` operations while hiding whether it uses memory, files or a database. The interface is useful only if callers also know the promises that affect them: whether a successful save is durable, how missing data is represented, which errors can occur and whether simultaneous updates can overwrite each other. Two implementations with identical method names are not interchangeable when these meanings differ.

### Why a builder needs to know this

Builders meet abstractions in language types, libraries, frameworks, database clients, cloud services and AI-generated helper layers. A good abstraction reduces cognitive load and lets an implementation change without forcing every caller to change. A poor one merely renames operations, or hides costs and failures that callers must manage.

Interfaces also create commitments. Once callers depend on observable behaviour or exposed data, changing it may break them even if the implementation becomes internally cleaner. Make the boundary small, but include the behaviour a caller needs to act correctly.

### Pitfalls

- **“A wrapper is an abstraction.”** Another layer may add a name without reducing knowledge or coupling.
- **“Leaky abstractions are useless.”** Lower-level limits sometimes cross a boundary; the abstraction can still handle ordinary reasoning while diagnosis occasionally looks beneath it.
- **“Design for every imagined implementation.”** Speculative flexibility can make the interface harder to understand than the concrete need.
- **“The signature is the whole interface.”** Errors, side effects, ownership, ordering and performance can be observable parts of its contract.

### Related concepts in TFB

- [Errors, exceptions and cleanup](02-programming-foundations.md#errors-exceptions-and-cleanup) - failure and resource ownership need honest representation at an interface.
- [Modularity, cohesion, coupling and separation of concerns](#modularity-cohesion-coupling-and-separation-of-concerns) - modules establish boundaries; interfaces expose selected parts of them.
- [Processors, memory and persistent storage](01-computing-foundations.md#processors-memory-and-persistent-storage) - storage mechanisms illustrate details that an abstraction may hide only up to a point.

### Deeper concepts

- Abstract data types - defining data through permitted operations rather than its representation.
- Design by contract - expressing expectations, guarantees and maintained conditions at a boundary.
- Dependency injection - supplying collaborators from outside a component rather than fixing them internally.

### Further reading

- [Liskov and Zilles: Programming with Abstract Data Types](https://doi.org/10.1145/942572.807045) - abstraction through operations independent of representation.
- [D. L. Parnas: On the Criteria To Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623) - the connection between information hiding and module design.
- [Bertrand Meyer: Introduction to Design by Contract](https://archive.eiffel.com/doc/manuals/technology/contract/) - a deeper model of expectations and guarantees at interfaces.

## Testing, verification and evidence

*A check supports a particular claim under particular conditions; it does not certify the whole system.*

### What they are

A **test** executes or examines something under stated conditions and compares an observation with an expectation. It provides evidence for the claim and conditions it covers. Tests can operate at several boundaries: a small calculation, a component with a real database, a complete user journey or a property exercised across generated inputs.

**Verification** is broader. It asks whether an implementation, artefact or model satisfies specified requirements. Evidence may come from tests, review, automated examination of source code without running it, mathematical reasoning, inspection, demonstrations and observations of a running system. **Validation** asks a different question: whether the result meets the real stakeholder need. A system can implement its [specification](#functional-requirements-quality-attributes-specifications-and-invariants) correctly while that specification describes the wrong thing.

For the money-transfer invariant, small tests can check known amounts, a test of several parts together can exercise the real database transaction, automatically generated input cases can explore a wider range, and review can challenge the failure assumptions. Observation of the running system might later detect a conservation violation. None of these alone proves the whole production system correct; together they support a more explicit claim.

Useful evidence keeps enough context to interpret it: the claim, version, environment, inputs, method and result. A green badge is weak evidence if nobody knows what ran.

### Why a builder needs to know this

Builders use evidence in local test suites, proposed changes, release decisions, security review, incident investigation and compliance. AI can generate both code and tests from the same mistaken assumption, so independent reasoning about what a test establishes is particularly important.

Different techniques expose different classes of defect. Testing remains essential, but a passing run means that the recorded observations matched their expectations in that run. It does not prove that the requirement was right or that every important condition was exercised.

### Pitfalls

- **“Coverage measures correctness.”** It records executed code, not assertion quality, requirement coverage or risk reduction.
- **“Mocks make a test realistic.”** A replacement can remove the interaction whose real behaviour matters.
- **“A failing generated test should be changed until the code passes.”** That can erase evidence instead of correcting behaviour.
- **“Formal verification proves the deployed system correct.”** It proves defined properties of a model under assumptions; hardware, deployment and an incorrect requirement can remain outside the claim.

### Related concepts in TFB

- [Debugging and diagnosis](02-programming-foundations.md#debugging-and-diagnosis) - a failed test supplies a symptom; diagnosis seeks its cause.
- [Time, clocks, dates and time zones](01-computing-foundations.md#time-clocks-dates-and-time-zones) - clock assumptions often make tests unreliable.
- [Floating-point approximation](01-computing-foundations.md#floating-point-approximation) - exact comparisons can encode the wrong expectation for approximate numbers.

### Deeper concepts

- Unit, integration, contract and end-to-end testing - choosing a boundary that matches the claim.
- Property, fuzz and mutation testing - generating cases or changing code to challenge the strength of evidence.
- Formal methods - mathematical models and reasoning about specified properties.

### Further reading

- [Edsger W. Dijkstra: Notes on Structured Programming](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html) - the important limit on what program testing can establish.
- [NASA Systems Engineering Handbook appendices](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) - verification and validation methods, claims and recorded results.
- [How SQLite Is Tested](https://www.sqlite.org/testing.html) - a detailed case showing different tests matched to different risks.

## Version control, code review, shared ownership and recovery

*Recorded, reviewable changes give a project memory and several routes back from a mistake.*

### What they are

**Version control** records project states and changes over time so that collaborators can compare, attribute and recover known versions. In Git, a **commit** is a named snapshot linked into history. Work that has not been committed or saved elsewhere remains outside that protection.

**Code review** gives a proposed change another reasoning surface before or around integration. Finding defects is one purpose; review can also expose assumptions, spread knowledge and keep a local decision consistent with the wider codebase. Small, coherent changes make intent and consequences easier to review, diagnose and reverse than large changes serving several purposes.

**Shared ownership** means responsibility and knowledge should not stop with the original author. It does not require every person to change every component without boundaries. Named ownership can provide accountability but become a bottleneck; broad ownership can spread knowledge but become weak ownership if nobody acts. The important thing is to make responsibility and routes for help explicit.

Recovery takes several forms. You might revert a committed change by recording a new inverse change, restore an earlier file, locate a lost local reference or rebuild a damaged remote. These are different operations. Version control supports source recovery, but it is not a backup of production data, external state or every local artefact.

### Why a builder needs to know this

This is the safety mechanism around everyday change. It appears in local repositories, repository-hosting services, branches, commits, pull or merge requests and review rules. For a solo builder it provides an experiment log; for a team it creates shared technical memory.

Isolating an AI-generated change in a focused commit and proposed review makes its assumptions visible. A reviewer can spot an accidental deletion, automated checks can evaluate the exact result, and a later defect in behaviour that used to work can be reversed while preserving evidence of what happened.

### Pitfalls

- **“Git saves everything automatically.”** It cannot recover work that was never recorded or otherwise saved.
- **“A branch is inherently safe.”** Long-lived branches delay integration and let assumptions diverge.
- **“Approval proves correctness.”** Review is evidence of a process; its value depends on context, time and expertise.
- **“Rewrite shared history to tidy it.”** Overwriting a shared branch's history—often called force-pushing—or resetting it can destroy collaborators' reference points.
- **“Everyone owns it.”** Without explicit responsibility, shared ownership can mean nobody responds.

### Related concepts in TFB

- [Modules, packages and dependencies](02-programming-foundations.md#modules-packages-and-dependencies) - code boundaries influence review scope and ownership.
- [Debugging and diagnosis](02-programming-foundations.md#debugging-and-diagnosis) - history can narrow when and why behaviour that used to work became defective.
- [Testing, verification and evidence](#testing-verification-and-evidence) - human review and automated checks support different claims.

### Deeper concepts

- Branching and integration strategies - different ways of organising concurrent work and shared history.
- Repository permissions and protected branches - controls over who can change important references.
- Backup and disaster recovery - preserving state that version control does not contain.

### Further reading

- [Pro Git: About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control.html) - the purposes and main forms of version control.
- [Git `revert` documentation](https://git-scm.com/docs/git-revert) - recovery by recording an inverse change without erasing shared history.
- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/) - a maintained practitioner guide to review purpose and judgement.
- [Software Engineering at Google: Knowledge Sharing](https://abseil.io/resources/swe-book/html/ch03.html) - approaches to making technical knowledge resilient across a team.

## Build automation, continuous integration and fast feedback

*Repeatable builds and frequent integration turn a change into evidence while its context is still fresh.*

### What they are

A **build** transforms recorded inputs—source, dependencies, configuration and tool instructions—into checked outputs or deployable packages, also called artefacts. **Build automation** records those steps so they can be repeated instead of living only in one person's terminal history. Build instructions and automated workflow definitions are themselves part of the software system and need versioning and review.

**Continuous integration (CI)** is the practice of frequently integrating small changes into the shared primary branch, or **mainline**, and checking the combined result with an automated build and tests. A product labelled “CI” supplies tools; installing it does not establish the practice.

**Fast feedback** shortens the distance between a change and evidence about it. This reduces the number of possible causes when a check fails, limits work built on a faulty assumption and makes correction cheaper. Fast and broad checks involve a trade-off: a quick required check can cover high-value formatting, type and test concerns, while slower sets of browser, performance or security checks run separately.

For example, each proposed change can trigger one recorded workflow that installs dependencies pinned to recorded versions, checks the source, runs fast tests and produces an identifiable artefact. A failure remains visible and blocks integration until corrected or the change is withdrawn. The green result means only that the configured steps passed against those inputs.

### Why a builder needs to know this

Builders meet builds in compiler and package scripts, generated assets, container images and deployment bundles. CI appears as repository checks and shared automated workflows. Together they expose “works on my machine” assumptions and provide a repeatable route from source to [evidence](#testing-verification-and-evidence).

The feedback loop matters more than the product name. Joel Spolsky's 2001 essay [*Daily Builds Are Your Friend*](https://www.joelonsoftware.com/2001/01/27/daily-builds-are-your-friend/) made the edit-build-test and report-fix-retest loops memorable. Its once-per-day schedule and dedicated build-machine details reflect its period; contemporary CI usually aims to report on each integrated change much sooner.

### Pitfalls

- **“A script makes a reproducible build.”** Undeclared tools, hidden manual steps and mutable dependencies can still change the output.
- **“Running tests eventually is continuous integration.”** Delaying integration until a long-lived branch is finished loses the frequent shared feedback.
- **“Every check must block the change immediately.”** Slow or unreliable checks that sometimes fail without a relevant change teach people to bypass or ignore them.
- **“CI means continuous delivery or deployment.”** Integration checks combined changes; later practices address releasability and release.

### Related concepts in TFB

- [Source code, programming languages and runtimes](02-programming-foundations.md#source-code-programming-languages-and-runtimes) - a build records how source becomes an executable form.
- [Modules, packages and dependencies](02-programming-foundations.md#modules-packages-and-dependencies) - dependency resolution is one source of differing build inputs.
- [Version control, code review, shared ownership and recovery](#version-control-code-review-shared-ownership-and-recovery) - CI evaluates recorded changes and their combined state.

### Deeper concepts

- Reproducible builds and artefact provenance - evidence about the exact inputs and process behind an output.
- Continuous delivery and continuous deployment - keeping changes releasable and deciding how they reach users.
- Test selection and parallel execution - balancing feedback speed with breadth.

### Further reading

- [GNU Make overview](https://www.gnu.org/software/make/) - a concrete model of outputs, inputs, dependencies and recorded rules.
- [Martin Fowler: Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) - the practice and its common confusions.
- [DORA: Continuous integration](https://dora.dev/capabilities/continuous-integration/) - the relationship between small batches, mainline integration and rapid feedback.

## Refactoring, technical debt, legacy systems and evolutionary replacement

*Existing software can improve at several scales, from a small structural change to a staged system replacement.*

### What they are

**Refactoring** changes internal structure through small, behaviour-preserving steps so that software becomes easier to understand or modify. A feature, defect fix or rewrite may include refactoring, but changing intended behaviour is not itself refactoring.

**Technical debt** is a metaphor for internal decisions that make future changes cost more. Its “interest” is the additional effort paid when work touches the affected area. Debt can be an informed trade-off, an accidental result of learning or a neglected problem. It is not a precise account balance or a synonym for every defect, old dependency or disliked style.

A **legacy system** is software inherited from earlier work on which people still depend. Age alone does not make it bad. Such a system contains visible code and less visible knowledge: edge cases, compatibility behaviour, data history, integrations and operational workarounds. Michael Feathers's description of legacy code as code without tests is a useful lens on risky change, not its only definition.

**Evolutionary replacement** moves behaviour or data in bounded stages while old and new systems coexist. An invoicing team might first capture current behaviour with tests, extract one rendering boundary, compare old and new output, route a small class of invoices to the replacement and reconcile results before retiring the old path. Local refactoring and system replacement are different scales of controlled change.

### Why a builder needs to know this

Every successful system becomes existing software. These choices appear when adding features to awkward code, upgrading unsupported platforms, moving data, replacing a vendor or responding to security and cost constraints. AI can produce a clean-looking replacement quickly while missing behaviour that exists only in history and operations.

Joel Spolsky's 2000 essay [*Things You Should Never Do, Part I*](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) memorably argues that rewrites discard accumulated knowledge. Its absolute title is rhetoric, not a universal rule. Unsupported technology, unacceptable security boundaries or fundamentally changed requirements can justify replacement; the durable lesson is to find the hidden responsibilities and manage the migration risk.

### Pitfalls

- **“Old means worthless; new means correct.”** Neither age nor appearance supplies evidence.
- **“Refactoring is safe without feedback.”** Tests or another observation mechanism are needed to detect accidental behaviour changes.
- **“Record all debt and the problem is managed.”** A useful decision identifies the affected change cost, priority and owner.
- **“Incremental replacement is automatically low risk.”** It adds temporary routing, compatibility, reconciliation and operating cost, and can stall with two permanent systems.
- **“Replacing code replaces the system.”** Data, users, integrations, operational knowledge and compliance evidence also need migration or an explicit boundary.

### Related concepts in TFB

- [Modularity, cohesion, coupling and separation of concerns](#modularity-cohesion-coupling-and-separation-of-concerns) - good boundaries provide seams for controlled change.
- [Testing, verification and evidence](#testing-verification-and-evidence) - behaviour-preserving change needs evidence about existing and new behaviour.
- [Version control, code review, shared ownership and recovery](#version-control-code-review-shared-ownership-and-recovery) - small recorded changes make evolution easier to examine and reverse.
- [Build automation, continuous integration and fast feedback](#build-automation-continuous-integration-and-fast-feedback) - quick feedback makes staged change practical.

### Deeper concepts

- Characterisation testing - recording observed legacy behaviour before changing it.
- Strangler fig migration - routing selected behaviour to a replacement in stages.
- Lehman's laws of software evolution - observations about long-lived systems adapting to their environments.

### Further reading

- [Martin Fowler: Refactoring](https://refactoring.com/) - the definition and disciplined practice of small behaviour-preserving structural changes.
- [Ward Cunningham: The WyCash Portfolio Management System](https://c2.com/doc/oopsla92.html) - the original debt metaphor in its learning-and-consolidation context.
- [Michael Feathers: *Working Effectively with Legacy Code* sample](https://www.informit.com/content/images/9780131177055/samplepages/0131177052.pdf) - feedback and seams for safer work in difficult code.
- [Martin Fowler: Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) - staged replacement and its transitional cost.

## Chapter status

The approved Chapter 3 first pass covers seven entries. Further territory and current product material remain optional and will be added only where they improve awareness without overloading the main traversal.

[Return to the guide map](../README.md#map-of-the-territory) · [Browse the complete Chapter 3 plan](../OUTLINE.md#3-software-engineering)
