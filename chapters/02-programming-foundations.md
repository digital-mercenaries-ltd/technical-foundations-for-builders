# Chapter 2: Programming foundations

Source code describes intended behaviour under the rules of a programming language, but it does not act alone. An implementation and runtime execute it; values, state, control flow and dependencies determine what happens. This chapter supplies a compact model for looking through generated code instead of treating it as an opaque artefact.

The only starting assumptions are that you can read ordinary text and have seen a software project run. Each entry stands on its own, although the order follows a program from source text through execution and, eventually, failure and diagnosis.

## Chapter map

The first pass covers:

1. [Source code, programming languages and runtimes](#source-code-programming-languages-and-runtimes)
2. [Values, types and conversions](#values-types-and-conversions)
3. [Variables, state, mutability and side effects](#variables-state-mutability-and-side-effects)
4. [Control flow, functions and scope](#control-flow-functions-and-scope)
5. [Collections, data structures and algorithmic cost](#collections-data-structures-and-algorithmic-cost)
6. [Modules, packages and dependencies](#modules-packages-and-dependencies)
7. [Errors, exceptions and cleanup](#errors-exceptions-and-cleanup)
8. [Debugging and diagnosis](#debugging-and-diagnosis)

## Source code, programming languages and runtimes

*The text you edit needs rules, an implementation and a host before it can do anything.*

### What they are

**Source code** is a representation of a program written in a **programming language**. The language defines which arrangements of text are valid—its **syntax**—and what valid arrangements mean—its **semantics**. Source is still text represented as [bits and bytes](01-computing-foundations.md#bits-and-bytes); a language implementation gives that text computational meaning.

An **implementation** translates or executes the program. It might produce machine instructions ahead of time, use an **intermediate form** meant for another program rather than the processor, or mix those approaches. An **interpreter** executes source or an intermediate form; a **virtual machine** provides a software-defined execution environment. These are implementation choices, not permanent categories of language. The same language can have several implementations.

A **runtime** is the environment and services used while a program executes. It may include a language engine, standard library, a service that manages allocated memory, and a service that finds and loads separately organised code. The **host**—such as a browser, server runtime or [operating system](01-computing-foundations.md#operating-systems-and-running-programs)—supplies facilities such as files, network access, clocks and a user interface. JavaScript in a browser and JavaScript in Node.js share a language but do not receive identical host facilities.

```text
source text
    -> parse, check or translate
    -> executable instructions or an intermediate form
    -> runtime plus host environment
    -> values, state and observable effects
```

This pipeline is a map, not a claim that every tool performs every stage separately.

### Why a builder needs to know this

Code can be valid for the wrong language version, runtime, operating system, module system or host. “It is JavaScript” does not tell you whether it can use a browser document, read a server file or run on a particular deployment platform. When generated code fails, identify the language, implementation, runtime version and host before changing the source.

TypeScript shows another important boundary: its ordinary type annotations are removed when JavaScript is emitted. A successful type check is useful evidence about the checked source, but it does not validate untrusted data arriving while the program runs.

### Pitfalls

- **“The source runs directly.”** An implementation and host are present even when tooling hides them.
- **“Compiled means fast or safe; interpreted means slow.”** Translation strategy alone proves neither performance nor correctness.
- **“The language supplies every available function.”** Many useful facilities come from the runtime, host, framework or operating system.
- **“It works here, so it is portable.”** Versions, configuration, dependencies and host facilities can change behaviour.

### Related concepts in TFB

- [Bits and bytes](01-computing-foundations.md#bits-and-bytes) - source text and executable representations are both stored as bytes.

### Deeper concepts

- Compilers, interpreters and virtual machines - the different stages by which implementations execute programs.
- Build artefacts and deployment environments - how translated code reaches its eventual host.

### Further reading

- [ECMAScript: Source Text](https://tc39.es/ecma262/2025/multipage/ecmascript-language-source-code.html) - the standard's formal model of source text.
- [Java Language Specification: Execution](https://docs.oracle.com/javase/specs/jls/se26/html/jls-12.html) - a concrete staged model of compilation, loading, linking and execution.
- [TypeScript: Erased Types](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch#erased-types) - why TypeScript type annotations do not remain as runtime checks.
- [Node.js introduction](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) - an example of a JavaScript runtime and host outside the browser.

## Values, types and conversions

*Programs manipulate values according to rules; labels and conversions do not make those values trustworthy.*

### What they are

A **value** is a piece of information a running program can manipulate: a number, some text, a true-or-false value or a more complex object. A **type** classifies values and helps determine which operations are meaningful and what result or failure an operation can produce. A value's type is not the same as its [byte representation](01-computing-foundations.md#bits-and-bytes).

Types can be checked at different times. Some mismatches are rejected before execution; others are detected while the program runs. Many languages use both approaches. A declared type can describe what the source expects without changing the data that actually arrives from a form, file, database or network response.

A **conversion** produces or interprets a value as another type. The text value `"42"` and the integer value `42` may display alike but support different operations. Parsing the text as an integer can fail. Converting a fractional number to an integer can discard information. A language may perform a conversion explicitly because the code asks for it, or implicitly as part of another operation.

### Why a builder needs to know this

Boundaries between forms, application code, databases and network services are full of conversions. A generated type declaration can make code easier to check, but external data still needs parsing and validation. Even a successful conversion only answers a technical question: parsing `120` as an integer does not prove that 120 is a permitted age, price or quantity.

Pay particular attention to missing values. An absent field, an empty string, zero and a language's special “no value” marker can represent different domain states. Collapsing them can turn “not supplied” into “supplied as zero” or erase a deliberate choice.

### Pitfalls

- **“Adding a type label transforms the data.”** A type claim can describe an assumption without enforcing it at runtime.
- **“Conversion is free and lossless.”** It can reject, round, truncate, overflow or change meaning.
- **“The same operator behaves alike everywhere.”** Operations depend on the language and the types involved.
- **“Successfully parsed means valid.”** Domain rules still apply after technical conversion.

### Related concepts in TFB

- [Bits and bytes](01-computing-foundations.md#bits-and-bytes) - the same stored pattern can receive different interpretations.
- [Integer ranges and overflow](01-computing-foundations.md#integer-ranges-and-overflow), [floating-point approximation](01-computing-foundations.md#floating-point-approximation) and [text encodings](01-computing-foundations.md#text-unicode-and-character-encodings) - representation limits that can make conversions lossy.

### Deeper concepts

- Static and dynamic typing - when type constraints are checked and what evidence they provide.
- Validation and schemas - how software checks that external data meets a required shape and meaning.

### Further reading

- [Python data model: Objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types) - one language's precise distinction between identity, type and value.
- [ECMAScript: Data Types and Values](https://tc39.es/ecma262/2025/multipage/ecmascript-data-types-and-values.html) - the language standard's runtime value model.
- [ECMAScript: Type Conversion](https://tc39.es/ecma262/2025/multipage/abstract-operations.html#sec-type-conversion) - examples of conversions built into language operations.

## Variables, state, mutability and side effects

*Names let code reach values; retained and shared changes make later behaviour depend on earlier events.*

### What they are

A **variable** is a name or location through which a program refers to a value. Assignment can **rebind** a name so that it refers to a different value. This is not always the same as copying or changing the value itself.

**State** is information retained between steps so that later behaviour can depend on what happened earlier. A value is **mutable** if it can be changed after creation; **mutation** changes that existing value or location. If two names refer to the same mutable object, a change made through either name may be visible through the other. This shared reference is called an **alias**.

A **side effect** is an observable change beyond producing a function's result. Examples include changing shared state, writing a file or database row, sending a network request, logging or displaying output. Some effects stay inside the running program; others reach the outside world.

### Why a builder needs to know this

State and effects explain why apparently identical calls can return different results, why order matters and why one test can contaminate another. They also explain why repeating an operation is not automatically safe: retrying code that sends a payment or message may repeat the external effect.

This model is especially useful when reviewing generated changes. A function may look local while mutating an object shared elsewhere, relying on a global cache or reading a clock. Ask not only “what does it return?” but also “what can it read or change?”

### Pitfalls

- **“Assignment copies the whole value.”** It may create another reference to the same mutable object.
- **“A constant name makes its value deeply immutable.”** Some languages prevent rebinding while allowing the referred-to object to change.
- **“A function only affects its return value.”** It may change reachable state or the outside world.
- **“Hidden state is harmless.”** Globals, caches, environment settings and clocks can make behaviour depend on history.
- **“Immutable means nothing beneath it can change.”** An immutable container may still refer to mutable values.

### Related concepts in TFB

- [Values, types and conversions](#values-types-and-conversions) - variables refer to values; they are not another kind of value.

### Deeper concepts

- Pure functions and functional programming - ways to make effects more explicit and reasoning more local.
- Idempotency - designing an operation so that repetition does not multiply its intended effect.
- Concurrency and transactions - managing state when work overlaps or several changes must succeed together.

### Further reading

- [Python: Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding) - how names become associated with objects.
- [Python: Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) - the distinction between rebinding and changing an attribute or item.
- [Racket evaluation model: Effects](https://docs.racket-lang.org/reference/eval-model.html) - a precise distinction between internal and external effects.

## Control flow, functions and scope

*Code does not merely sit in order: rules decide which operation runs, where names are visible and what a call can affect.*

### What they are

**Control flow** is the order in which a program's operations are evaluated. Statements may run in sequence, a condition may choose a branch, a loop may repeat work, and a function call may transfer control to another block before returning. Exceptions, events and callbacks can change the path again.

A **function** packages a computation behind a name or value. A call supplies **arguments**, creates bindings for the function's **parameters**, executes its body and may return a result. Functions create useful boundaries around inputs, outputs, effects and failures, but they do not automatically make code independent or correct.

**Scope** governs where a name can be resolved. A name introduced inside a function is usually local to that function, while code may also see names in enclosing or wider scopes. An inner declaration can **shadow** an outer one by using the same name. Scope is not the same as lifetime: a value may remain reachable after one name goes out of scope, and a returned function can retain access to an enclosing binding.

### Why a builder needs to know this

Control flow tells you which code actually runs, not merely which code appears above or below another line. When a result surprises you, trace the conditions, calls, returns and exceptional paths that could reach it. When a name surprises you, ask which scope supplied it and whether another declaration shadows it.

Generated code often hides important work inside callbacks or helper functions. A familiar-looking condition can also mislead because languages have different rules for treating values as true or false. The condition passing does not prove the underlying domain fact is valid.

### Pitfalls

- **“Code runs from top to bottom once.”** Loops, calls, callbacks, events and exceptions alter the route.
- **“A true condition proves the data is valid.”** Truth-value rules and domain validation answer different questions.
- **“A local variable is temporary and isolated.”** It can refer to shared mutable state or escape through a returned value.
- **“The same name means the same value everywhere.”** Scope and shadowing determine which binding is used.

### Related concepts in TFB

- [Variables, state, mutability and side effects](#variables-state-mutability-and-side-effects) - calls and scopes determine how code reaches and changes state.
- [Errors, exceptions and cleanup](#errors-exceptions-and-cleanup) - exceptions create an alternative control-flow path.

### Deeper concepts

- Iteration and recursion - two ways for a computation to repeat.
- Closures - functions that retain access to bindings from an enclosing scope.
- Asynchronous work - control flow that continues after another operation completes or signals an event.

### Further reading

- [Python: Compound statements](https://docs.python.org/3/reference/compound_stmts.html) - representative rules for conditions, loops, functions and exceptions.
- [Python: Resolution of names](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names) - a formal account of scope and name lookup.
- [ECMAScript: Lexical Environments](https://tc39.es/ecma262/2025/multipage/executable-code-and-execution-contexts.html#sec-lexical-environments) - the standard model behind nested JavaScript scopes.

## Collections, data structures and algorithmic cost

*How values are organised determines both what operations mean and how their cost grows.*

### What they are

A **collection** groups values. A **data structure** organises information so that operations such as finding, inserting, deleting, ordering or taking the next item have defined meanings and costs. A small recognition set covers many ordinary programs:

- a **sequence**, list or array keeps items in order, commonly with access by position;
- a **map** or dictionary associates keys with values;
- a **set** keeps unique members;
- a **stack** removes the most recently added item first;
- a **queue** removes the earliest added item first; and
- a **tree** or **graph** represents hierarchical or general connections.

Names and guarantees vary by language. “Map” does not by itself promise ordering, and “list” can describe different underlying structures.

**Algorithmic cost** describes how the work or memory required by an operation grows as its input grows. **Big-O notation** expresses a bound on that growth. The essential intuition is the difference between work that stays roughly constant, grows with the number of items, or grows much faster because it repeatedly rescans or nests work. Big-O is not a stopwatch reading: it omits constants and many machine and data effects.

### Why a builder needs to know this

Choosing a collection also chooses semantics. If you need uniqueness, key lookup or first-in-first-out processing, a generic list may allow invalid states or require repeated searches. Cost becomes important when small sample data grows or when a loop performs a database or network operation for every item.

Performance claims need their assumptions. A hash map often provides roughly constant-time key lookup when its hash function distributes keys well; poor distribution or another implementation can change that behaviour. Real latency, memory use and clarity still matter alongside the growth model.

### Pitfalls

- **“A list is the default for everything.”** Required ordering, uniqueness and lookup operations may suggest another structure.
- **“O(1) means instantaneous.”** It describes growth under a model, not elapsed time.
- **“The best theoretical bound always wins.”** Data size, memory, locality, implementation overhead and clarity matter.
- **“A short loop is cheap.”** Each iteration may trigger much more work in another system.

### Related concepts in TFB

- [Values, types and conversions](#values-types-and-conversions) - structures organise values and constrain meaningful operations.
- [Variables, state, mutability and side effects](#variables-state-mutability-and-side-effects) - many collections are mutable and may be shared through aliases.

### Deeper concepts

- Algorithms and complexity analysis - more precise models of work, memory and trade-offs.
- Indexes and query planning - data structures and cost models inside databases.
- Queues and graphs - structures with important uses in distributed systems and dependency modelling.

### Further reading

- [National Institute of Standards and Technology (NIST): Data structure](https://www.nist.gov/dads/HTML/dataStructure.html) - a concise definition tied to operations and efficiency.
- [NIST: Big-O notation](https://www.nist.gov/dads/HTML/bigOnotation.html) - the formal meaning behind the growth shorthand.
- [Python tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html) - accessible examples of common collections.
- [Java `HashMap` documentation](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/util/HashMap.html) - a performance promise stated with its assumptions.

## Modules, packages and dependencies

*A project is assembled from units of code, but ecosystem vocabulary and inherited responsibility do not stop at an import statement.*

### What they are

A **module** is a unit of code with its own namespace and an interface to other code. Importing or loading it generally means resolving a name or path, obtaining code and making its exported facilities available.

A **package** is an ecosystem-specific grouping. It might mean a hierarchy of importable modules, an installable distribution or a directory described by package metadata. Do not assume that two ecosystems—or even two tools in one ecosystem—use the word identically.

A **dependency** is code or another component on which your program relies. A **direct dependency** is declared by your project; a **transitive dependency** is brought in by something you depend on. A package manager resolves names and version constraints, retrieves artefacts and installs a graph of dependencies. An import in source and an installable package are related, but they are not necessarily the same unit.

### Why a builder needs to know this

Every dependency expands the code, maintainers, licences, updates and possible failure or compromise paths that the project inherits. Generated code may add a package to solve a small problem without establishing whether it is compatible with the runtime, available in deployment, safe to execute or necessary at all.

An import working on one machine does not prove that dependency resolution is reproducible elsewhere. Search paths, package metadata, runtime versions and previously installed files all affect what is found. Manifests, lockfiles and build controls provide stronger evidence, but they belong to the software-engineering layer rather than changing this basic dependency model.

### Pitfalls

- **“Module and package are universal synonyms.”** Their meanings depend on the language and toolchain.
- **“If the import works, deployment is covered.”** Another environment may resolve or install a different graph.
- **“Only direct dependencies matter.”** Transitive code also executes or influences the build.
- **“Open source means reviewed, safe or maintained.”** Source availability does not prove any of those properties.
- **“Removing an import removes all coupling.”** Formats, runtime interfaces, build plugins and generated artefacts can also create dependencies.

### Related concepts in TFB

- [Source code, programming languages and runtimes](#source-code-programming-languages-and-runtimes) - module loading and package support depend on the implementation and host.
- [Collections, data structures and algorithmic cost](#collections-data-structures-and-algorithmic-cost) - dependencies form a graph rather than a flat list.

### Deeper concepts

- Version constraints, manifests and lockfiles - evidence about the exact dependency graph selected for a build.
- Software supply-chain security - controls for code and artefacts inherited from elsewhere.
- Modularity and interfaces - designing boundaries within a codebase rather than merely packaging files.

### Further reading

- [Python: The import system](https://docs.python.org/3/reference/import.html) - separates searching, loading and name binding.
- [Python Packaging User Guide: Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-packages) - explains the difference between import packages and installable distributions.
- [Node.js: Packages](https://nodejs.org/api/packages.html) - an ecosystem-specific package and module model.
- [npm: Specifying dependencies](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file/) - how one package manager records dependency version ranges.

## Errors, exceptions and cleanup

*Failure can appear at several stages; handling it means choosing an honest outcome and leaving resources in a known state.*

### What they are

An **error** broadly means that something went wrong. Syntax may be rejected while source is parsed; valid code may fail while executing; configuration, input or an unavailable service may violate an assumption without using a language exception at all.

An **exception** is one structured mechanism for reporting an abnormal condition and changing control flow. It carries information and may be handled by an enclosing operation or propagate to its caller. Languages also represent failure with return values, result types, process exit status and other mechanisms, so “error” and “exception” are not synonyms.

Handling is a policy decision. A caller might report a useful failure, choose an alternative, retry when repetition is safe, undo earlier work or let the failure propagate to a boundary that can respond honestly. Catching an exception without restoring a valid state or reporting failure can create a false success.

**Cleanup** releases resources and restores required conditions whether work succeeds or fails. Automatic memory reclamation, often called **garbage collection**, does not guarantee that files, network connections, locks or transactions close at the right moment. Languages provide mechanisms such as `finally` blocks, structured resource scopes or explicit resource ownership so cleanup follows every exit path.

### Why a builder needs to know this

Production software fails at boundaries: input is malformed, services time out, disks fill and assumptions are violated. Code must distinguish an expected failure it can handle from an unexpected one that should remain visible. “No exception” is not proof of correctness; a program can produce the wrong result or omit work and still finish normally.

When reviewing generated error handling, ask what failed, what the caller now believes, which effects already happened and which resources remain open. Reliability comes from an accurate outcome and a recoverable state, not from suppressing red messages.

### Pitfalls

- **“Catching every exception makes the program reliable.”** Broad catches can hide programmer errors and create false success.
- **“Every failure should be retried.”** Repetition may be useless, harmful or duplicative.
- **“Garbage collection handles every resource.”** External resources often require timely, explicit cleanup.
- **“No exception means the operation succeeded.”** Wrong results and missing effects can complete normally.

### Related concepts in TFB

- [Control flow, functions and scope](#control-flow-functions-and-scope) - exceptions propagate through calls and alter the normal path.
- [Variables, state, mutability and side effects](#variables-state-mutability-and-side-effects) - failure handling must account for state already changed and effects already performed.
- [Debugging and diagnosis](#debugging-and-diagnosis) - handling a failure is different from finding its cause.

### Deeper concepts

- Result types and failure contracts - ways interfaces make expected failure explicit.
- Resource ownership and cancellation - deciding which operation must release or stop work.
- Transactions and compensation - preserving consistency across several effects.

### Further reading

- [Python tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) - accessible examples of syntax errors, exceptions and selective handling.
- [Python execution model: Exceptions](https://docs.python.org/3/reference/executionmodel.html#exceptions) - how exceptions change control flow and propagate.
- [Python tutorial: Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions) - why structured cleanup matters across success and failure.

## Debugging and diagnosis

*A symptom is evidence; diagnosis is the work of finding and testing a causal explanation.*

### What they are

**Debugging** is the work of finding and correcting defects. **Diagnosis** is the causal part: explain why the observed behaviour occurred, then test whether the explanation predicts what happens under changed conditions.

An error message or **stack trace** records where a condition was reported and the chain of active calls around it. A debugger can pause execution, step through operations and inspect values. These tools expose evidence; they do not identify the root cause for you. The cause may be earlier input, state, configuration, timing or an interaction with another system.

A compact diagnostic loop is:

1. state the observed symptom and expected behaviour;
2. reproduce it under known conditions, or preserve evidence when reproduction is unsafe;
3. inspect the error, calls, inputs, state and recent changes;
4. form a falsifiable hypothesis about the cause;
5. change one relevant condition or add a targeted observation; and
6. verify that the symptom is gone **and** that the explanation predicts the result.

This is a reasoning model, not a demand to experiment on a live production system. Preserve evidence and control risk before changing conditions.

### Why a builder needs to know this

Changing code until a symptom disappears does not establish what fixed it. Several changes at once can conceal the cause and introduce another defect. Artificial intelligence (AI) can propose hypotheses and observations quickly, but its plausible explanation still needs evidence from the actual program and environment.

Diagnosis also separates an immediate trigger from a system cause. “The user clicked the wrong control” may be accurate yet incomplete if a confusing interface, unsafe default or missing guardrail made the action likely.

### From hacker folklore

A **Bohr bug** is reliably reproducible under known conditions. A **heisenbug** changes or disappears when observation alters timing, memory layout or other execution conditions. The joke points to observer effects and hidden state, not quantum physics.

**Shotgun debugging** means making several undirected changes in the hope that the bug disappears. It is the opposite of controlling variables and testing a causal model.

**PEBKAC**, “problem exists between keyboard and chair”, and its reversed form **PEBCAK**, “problem exists between chair and keyboard”, blame user action. They can be funny among consenting peers, but they are not a root-cause analysis. Describe the action and the system mechanism before reaching for the joke; never use it to belittle the reader.

### Pitfalls

- **“The final line of the error is the root cause.”** It reports a condition; the cause may be earlier or elsewhere.
- **“A disappearing bug is fixed.”** Observation or timing may only have changed its conditions.
- **“The first plausible explanation is enough.”** A diagnosis should make testable predictions.
- **“The user caused it, so the system is fine.”** Human action is part of the causal chain, not a reason to stop investigating.

### Related concepts in TFB

- [Errors, exceptions and cleanup](#errors-exceptions-and-cleanup) - failure mechanisms provide evidence but not the causal conclusion.
- [Variables, state, mutability and side effects](#variables-state-mutability-and-side-effects) - hidden and shared state often explains irreproducible behaviour.
- [Source code, programming languages and runtimes](#source-code-programming-languages-and-runtimes) - evidence must come from the implementation and host that actually ran the code.

### Deeper concepts

- Minimal reproducible examples - reducing a failure while preserving its cause.
- Observability - collecting logs, metrics and traces from running systems.
- Root-cause analysis and incident learning - investigating wider technical and organisational conditions.

### Further reading

- [Python: `traceback`](https://docs.python.org/3/library/traceback.html) - what stack and exception traces contain.
- [Python: `pdb`](https://docs.python.org/3/library/pdb.html) - representative debugger controls and observations.
- [Jargon File: heisenbug](http://www.catb.org/jargon/html/H/heisenbug.html) - the historical debugging term and its mechanism.
- [Jargon File: shotgun debugging](http://www.catb.org/jargon/html/S/shotgun-debugging.html) - the historical term for undirected changes.

## Chapter status

The approved Chapter 2 first pass covers eight concepts. Further territory and current landscape material remain optional and will be added only where they improve recognition without overwhelming the main traversal.

[Return to the guide map](../README.md#map-of-the-territory) · [Browse the complete Chapter 2 plan](../OUTLINE.md#2-programming-foundations)
