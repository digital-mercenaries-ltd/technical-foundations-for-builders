# Chapter 1: Computing foundations

Computers store and transform information by giving meaning to physical states. This chapter builds the lowest-level model needed by the rest of TFB: how those states become bits, numbers, text and files; how processors act on them; and how finite time, memory and storage shape a system.

The aim is recognition, not manual calculation. You should finish these entries able to distinguish a value from its representation, understand why the same bits can mean different things and recognise when a low-level detail may explain high-level behaviour.

## Chapter map

The first pass begins with bits and bytes, then builds toward the number, text, machine, time and performance models that later chapters rely on:

1. [Bits and bytes](#bits-and-bytes)
2. [Integer ranges and overflow](#integer-ranges-and-overflow)
3. [Floating-point approximation](#floating-point-approximation)
4. [Text, Unicode and character encodings](#text-unicode-and-character-encodings)
5. [Processors, memory and persistent storage](#processors-memory-and-persistent-storage)
6. [Operating systems and running programs](#operating-systems-and-running-programs)
7. [Time, clocks, dates and time zones](#time-clocks-dates-and-time-zones)
8. [Latency and throughput](#latency-and-throughput)

Optional explanations of [binary numbers](../further/01-computing-foundations.md#binary-numbers) and [hexadecimal and octal](../further/01-computing-foundations.md#hexadecimal-and-octal) are available as further territory.

## Bits and bytes

*The basic units used to store and move digital information.*

### What they are

A **bit**, short for *binary digit*, has one of two values: `0` or `1`. A **byte** is a group of eight bits, so it has `2⁸`, or 256, possible patterns. If those patterns are interpreted as an [unsigned (non-negative) whole number](../GLOSSARY.md#unsigned-integer), they cover 0 to 255: zero consumes one of the 256 possibilities. The [National Institute of Standards and Technology (NIST) defines a byte as eight bits](https://csrc.nist.gov/glossary/term/byte).

The most useful distinction is between a **container and its interpretation**. Consider this byte:

```text
01000001
```

Read as an unsigned number, it is 65. Read using [UTF-8, a common text encoding](../GLOSSARY.md#utf-8), it represents `A`. In another format it could be part of a colour, machine instruction, compressed file or encrypted message. The bits do not carry that meaning by themselves; a rule such as a number type, text encoding or file format supplies it. The [Unicode Standard's UTF-8 definition](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G7404) also shows why encoded size and visible-character count differ: one [Unicode scalar value](../GLOSSARY.md#unicode-scalar-value) - the basic numbered unit encoded by UTF-8 - requires one to four bytes, and one visible character can contain several scalar values.

### Why a builder needs to know this

Files, memory, databases and network messages expose sizes in bytes. Network transfer rates are commonly expressed in bits per second, while cryptographic key sizes are commonly expressed in bits. Understanding the difference helps you reason about upload limits, storage bills, memory use, text length and values such as a 256-bit encryption key.

The Hypertext Transfer Protocol (HTTP) uses the more precise word [**octet**](../GLOSSARY.md#octet) for an eight-bit byte and defines `Content-Length` as a count of octets ([HTTP Semantics, section 8.6](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.6)). A browser's [`Blob.size`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/size), which describes the size of a raw-data container, reports bytes. These are different interfaces to the same basic unit.

### Pitfalls

- **A character is not a byte.** Counting visible characters does not reliably predict encoded or transmitted size.
- **Bits are not automatically numbers.** Always ask what interpretation or format applies.
- **Bits and bytes are easy to confuse.** Product interfaces commonly use lowercase `b` for bits and uppercase `B` for bytes.
- **MB and MiB are not identical.** `1 MB` is 1,000,000 bytes; `1 MiB` is 1,048,576 bytes. [NIST explains the decimal and binary prefixes](https://physics.nist.gov/cuu/Units/binary.html).

### Related concepts in TFB

- [Binary numbers](../further/01-computing-foundations.md#binary-numbers) - how a bit pattern can represent a quantity.
- [Hexadecimal and octal](../further/01-computing-foundations.md#hexadecimal-and-octal) - compact ways to write groups of bits.
- [Integer ranges and overflow](#integer-ranges-and-overflow) - why a fixed representation cannot hold every whole number.
- [Text, Unicode and character encodings](#text-unicode-and-character-encodings) - how numbers and bytes represent written text.

### Deeper concepts

- Signed integers and two's complement - how bit patterns can represent negative values.
- Bitwise operations and masks - how code reads or changes individual flags.
- Endianness and memory addressing - how multi-byte values are ordered and located.
- Error detection and correction - how added information can reveal or repair corruption.

### Further reading

- [Harvard CS50: Lecture 0 notes](https://cs50.harvard.edu/x/notes/0/) - an accessible introduction to information represented with bits.
- [NIST: Byte](https://csrc.nist.gov/glossary/term/byte) - the concise standards-linked definition.
- [NIST: Prefixes for binary multiples](https://physics.nist.gov/cuu/Units/binary.html) - the difference between units such as MB and MiB.

## Integer ranges and overflow

*A whole number may be unlimited in mathematics but limited in software.*

### What they are

An integer is a whole number. An **integer representation** is a finite set of patterns used to store such numbers. An unsigned field of *n* bits has `2ⁿ` patterns, representing values from `0` through `2ⁿ - 1`. An unsigned eight-bit field therefore stops at `255`; it has no pattern for `256`.

When a calculation produces a result outside the representation's range, **integer overflow** occurs. What happens next depends on the type and interface. Some operations wrap around, some report an error and some languages provide integers that grow until another resource limit is reached. Java, for example, specifies fixed-width integer types and defined wraparound behaviour for ordinary operations, while Python's `int` has unlimited precision at the language level ([Java Language Specification](https://docs.oracle.com/en/java/javase/26/docs/specs/jls/jls-4.html#jls-4.2.2); [Python numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)). A database column, file format or application programming interface can still impose a smaller range.

### Why a builder needs to know this

Ranges appear in counters, identifiers, timestamps, file sizes, database columns and protocol fields. A value can work inside one component and fail, wrap or be rejected when it crosses into another. Ask which representation, range and overflow rule applies at every boundary that handles important quantities.

### Pitfalls

- A value being called an “integer” does not tell you its range.
- Moving a value into a wider type cannot repair overflow that has already occurred.
- A larger range delays a boundary; it does not remove all resource limits.
- Negative values require a signed representation, whose range differs from an unsigned one of the same size.

### Related concepts in TFB

- [Bits and bytes](#bits-and-bytes) - the finite patterns from which integer representations are built.
- [Binary numbers](../further/01-computing-foundations.md#binary-numbers) - how those patterns can express quantities.
- [Floating-point approximation](#floating-point-approximation) - a different compromise for representing numbers.

### Deeper concepts

- Two's complement - the common representation of signed integers.
- Numeric types at system boundaries - how languages, databases and protocols convert or reject values.
- Decimal quantities and money - where range and domain-specific rounding rules meet.

### Further reading

- [Java Language Specification: primitive numeric types](https://docs.oracle.com/en/java/javase/26/docs/specs/jls/jls-4.html#jls-4.2) - a concrete example of fixed ranges and specified overflow behaviour.
- [Python: numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) - a contrasting language-level integer model.

## Floating-point approximation

*A very large range of numbers is represented with finite precision.*

### What it is

A **floating-point** format stores a sign, a significant part and a scale, rather like scientific notation. This allows one fixed-size value to represent both very small and very large numbers, but only a finite selection of them. When the exact result of a calculation is not in that selection, it is rounded to a nearby representable value. The Institute of Electrical and Electronics Engineers (IEEE) 754 standard defines widely used binary and decimal floating-point formats and their arithmetic ([IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/)).

Many everyday decimal fractions have no finite binary representation. In common binary floating-point environments, `0.1 + 0.2` therefore produces the representable value nearest the exact mathematical result, rather than exact `0.3`. Display formatting may hide or reveal the difference; it does not change the stored value. Python's [floating-point tutorial](https://docs.python.org/3/tutorial/floatingpoint.html) works through this representation error.

### Why a builder needs to know this

Floating-point values appear in measurements, graphics, statistics and many programming-language number types. Their approximations can affect equality checks, repeated calculations, totals and values exchanged between components. The useful question is not whether floating point is “accurate”, but whether its range, precision and rounding behaviour suit the decision being made.

### Pitfalls

- Floating point is not random or universally inaccurate. Many values and operations are exact; others require defined rounding.
- “Always compare with a tolerance” is not a complete rule. A suitable tolerance depends on the domain, scale and calculation, and some comparisons must be exact.
- More display digits do not add information that was never stored.
- Decimal or fixed-point representations can preserve chosen base-ten quantities, but they still have ranges and rounding rules.

### Related concepts in TFB

- [Integer ranges and overflow](#integer-ranges-and-overflow) - another consequence of finite numeric representations.
- [Bits and bytes](#bits-and-bytes) - the underlying storage patterns.

### Deeper concepts

- Rounding modes and accumulated error - how a sequence of approximations affects a result.
- Decimal and fixed-point arithmetic - alternatives for domains with base-ten rules.
- Numerical analysis - methods for reasoning about stable calculations.

### Further reading

- [Python: Floating-Point Arithmetic—Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html) - an accessible worked explanation of binary approximation and display.
- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/) - the standard owner's overview of floating-point formats and arithmetic.

## Text, Unicode and character encodings

*Written text passes through several layers before becoming stored bytes.*

### What they are

Unicode assigns a **code point**, written like `U+0041`, to an encoded character. A **character encoding** then defines how numbered text elements are represented for storage or transmission. Unicode Transformation Format 8-bit (UTF-8), for example, uses one to four bytes for each Unicode scalar value ([Unicode Standard, UTF-8 definition](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G7404)).

These layers mean that bytes, code points and visible characters are different units. The letter `é` can be represented as one code point or as `e` followed by a combining accent. Those sequences may look the same while differing internally. Unicode calls a sequence intended to behave as one user-perceived character a **grapheme cluster** ([Unicode text segmentation](https://www.unicode.org/reports/tr29/tr29-47.html#Grapheme_Cluster_Boundaries)). It also defines normalisation forms that can make specified equivalent sequences use a common representation.

### Why a builder needs to know this

Encoding appears at file, network, database and application programming interface boundaries. Text units matter when code limits input length, moves a cursor, truncates a label, compares identifiers or signs a message. A builder needs to ask which encoding a boundary expects and which unit an interface counts.

### Pitfalls

- A byte is not a character, and a code point is not reliably a user-perceived character.
- Unicode is a standard for text elements and related algorithms; UTF-8 is one encoding of Unicode values.
- “Plain text” still has an encoding and usually other conventions, such as line endings.
- Visually identical text can differ as bytes or code points, affecting comparison, search and file names.
- Normalisation is not a universal cleaning operation. Different forms preserve different distinctions.

### Related concepts in TFB

- [Bits and bytes](#bits-and-bytes) - the container used by byte-oriented encodings.
- [Integer ranges and overflow](#integer-ranges-and-overflow) - another example of values being constrained by a representation.

### Deeper concepts

- Text segmentation and normalisation - rules for user-perceived characters and equivalent sequences.
- Internationalisation - bidirectional text, collation, locale-sensitive casing and formatting.
- Security confusables - different characters that can appear deceptively similar.

### Further reading

- [Unicode Standard, Chapter 1](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-1/) - the standard's model of characters, glyphs and text elements.
- [Unicode Standard Annex #29](https://www.unicode.org/reports/tr29/) - maintained rules for grapheme, word and sentence boundaries.
- [Joel Spolsky: The Absolute Minimum Every Software Developer Must Know About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) - a memorable historical introduction, best read alongside the maintained Unicode material.

## Processors, memory and persistent storage

*Running software depends on resources with different jobs and lifetimes.*

### What they are

A **processor**, or central processing unit (CPU), follows machine instructions and performs calculations. It uses **memory**, commonly random-access memory (RAM), as working space for active programs and data. **Persistent storage** retains files and other data across ordinary process and machine restarts. Harvard's [CS50 overview of computer hardware](https://cs50.harvard.edu/ap/2026/curriculum/technology/references/how_computers_work.pdf) gives an accessible first model of these roles.

The boundaries are layered rather than absolute. An operating system normally gives a running program a virtual address space, maps that space to physical memory and can map files into it. It may move memory pages between RAM and backing storage. File writes can also pass through memory buffers before reaching a storage device. The Portable Operating System Interface (POSIX) defines `fsync()` as a request to transfer a file's data to its associated storage device, while leaving some details to the implementation ([POSIX `fsync`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/fsync.html)). A successful high-level “save” therefore needs a documented durability meaning.

### Why a builder needs to know this

This model explains why a program can run out of memory while disk space remains, why a restart loses in-memory state and why storage access can dominate elapsed time. It also exposes a critical production question: at what point would saved data survive a process crash, machine failure or storage failure?

### Pitfalls

- Memory and storage are not interchangeable terms.
- Virtual memory is not merely “extra RAM on disk”; it also provides address translation and isolation.
- Persistent does not mean indestructible. Devices, file systems, operators and sites can fail.
- A returned write operation is not automatically proof that every layer has made the data durable.

### Related concepts in TFB

- [Operating systems and running programs](#operating-systems-and-running-programs) - the software layer that manages these resources.
- [Latency and throughput](#latency-and-throughput) - two ways resource constraints become visible.
- [Bits and bytes](#bits-and-bytes) - the units used to describe memory and storage.

### Deeper concepts

- Virtual memory, paging and memory mapping - how address spaces relate to memory and files.
- Processor and memory caches - faster layers that change performance behaviour.
- File systems, replication and backups - different parts of making data durable and recoverable.

### Further reading

- [CS50: How Computers Work](https://cs50.harvard.edu/ap/2026/curriculum/technology/references/how_computers_work.pdf) - a one-page model of processors, RAM, storage and operating systems.
- [Linux kernel: Memory Management](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html) - operating-system documentation for virtual memory and paging.
- [POSIX: `fsync`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/fsync.html) - the specified persistence request and its implementation boundary.

## Operating systems and running programs

*An operating system turns stored programs into managed running work.*

### What they are

A **program** is stored instructions and associated data. A **process** is a running instance of a program with resources managed by an **operating system**. The operating system manages hardware and supplies common facilities such as files, networking, memory, device access, process creation and permissions. The same program can run as several processes, and one application can use several programs or processes.

A **thread** is one flow of control within a process. Threads normally share their process's memory and resources while retaining their own execution state. The operating system schedules runnable processes and threads onto available processors. This can interleave several flows so that they make progress concurrently; actual simultaneous execution depends on the available processing resources.

```text
stored program -> operating system starts it -> process owns resources
                                            -> one or more threads execute work
```

Microsoft's [processes and threads overview](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads) gives one concrete platform model; the [Portable Operating System Interface (POSIX) thread specification](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html#tag_16_09) defines the corresponding shared-address-space model on POSIX systems.

### Why a builder needs to know this

Deployments start and stop processes. Logs and monitoring report process or thread failures. Resource limits apply to running work, and concurrent threads can change shared memory. The model helps you ask whether a crash affected one process or a whole machine, whether state survives a restart and whether apparently separate work shares failure-prone state.

### Pitfalls

- An application, program and process do not always correspond one-to-one.
- A thread is not an isolated process. Shared memory allows efficient cooperation and creates data-race risks.
- “At the same time” can mean interleaved concurrency or physical parallelism.
- An operating system is not only a graphical desktop. Servers, containers and embedded systems also depend on operating-system services.

### Related concepts in TFB

- [Processors, memory and persistent storage](#processors-memory-and-persistent-storage) - the resources managed for running programs.
- [Latency and throughput](#latency-and-throughput) - measurements affected by scheduling and shared resources.

### Deeper concepts

- Concurrency and synchronisation - coordinating work that can overlap.
- Process isolation, permissions and system calls - boundaries between programs and the operating system.
- Containers and virtual machines - additional ways to package or isolate running workloads.

### Further reading

- [Microsoft: About Processes and Threads](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads) - a clear resource-sharing and scheduling model.
- [POSIX: threads](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html#tag_16_09) - a standards definition of threads within a process.
- [National Institute of Standards and Technology: operating system](https://csrc.nist.gov/glossary/term/operating_system) - a concise definition linked to formal sources.

## Time, clocks, dates and time zones

*Software must distinguish human calendar intent from instants and elapsed time.*

### What they are

An **instant** is one point on a timeline. A **local date and time**, such as 09:00 on a calendar, expresses civil time. A **Coordinated Universal Time (UTC) offset**, such as `+01:00`, relates one local time to UTC for a particular instant. A **time zone**, such as `Europe/London`, is a maintained set of rules mapping local times to offsets across dates. [Request for Comments (RFC) 9557](https://www.rfc-editor.org/rfc/rfc9557.html#section-1.2) explains why an offset alone cannot answer questions such as “what instant is 09:00 here next month?”: regional rules can change.

Software also uses different clocks. A **wall clock** answers “what civil or system time is it?” and can be corrected. A **monotonic clock** measures elapsed time without jumping backwards when the wall clock changes. Use differences between monotonic readings for durations; its arbitrary origin does not represent a calendar timestamp.

For example, `2026-07-17T12:00:00Z` identifies an instant. `2026-07-17T13:00:00+01:00[Europe/London]` preserves local civil intent and the regional rule set. They answer related but different questions.

### Why a builder needs to know this

Dates and clocks appear in appointments, recurring jobs, expiry, retries, billing periods, logs and performance measurements. Before choosing a library type or database column, decide whether the value represents human calendar intent, an observed instant or elapsed time.

### Pitfalls

- A UTC offset is not a time zone. `+01:00` does not say when a region changes its clocks.
- Local times can be repeated or skipped when an offset changes.
- “Every 24 hours” and “at 09:00 every local day” describe different schedules.
- A calendar month is not a fixed number of seconds.
- Wall clocks can be corrected, so they are unsafe for some elapsed-time measurements and relative timeouts.
- Time-zone rules are maintained data, not unchanging laws of nature.

### Related concepts in TFB

- [Integer ranges and overflow](#integer-ranges-and-overflow) - timestamps also use finite representations.
- [Latency and throughput](#latency-and-throughput) - latency requires a defined elapsed-time measurement.

### Deeper concepts

- Ambiguous and nonexistent local times - the effects of offset changes.
- Distributed ordering and clock synchronisation - why machines may disagree about time.
- Calendar systems and leap seconds - additional rules beyond this initial model.

### Further reading

- [RFC 9557: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc9557.html) - distinctions between timestamps, offsets and named time zones.
- [Internet Assigned Numbers Authority: Time zone and daylight saving time data](https://data.iana.org/time-zones/tz-link.html) - the maintained database and its location-based identifiers.
- [Portable Operating System Interface: monotonic-clock timeout guidance](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_clockwait.html) - why elapsed-time measurements should not depend on wall-clock adjustments.

## Latency and throughput

*One measures time per operation; the other measures completed work per unit time.*

### What they are

**Latency** is how long one operation or piece of work takes from a defined start to a defined finish. **Throughput** is how much work completes per unit time. They use different dimensions: milliseconds per request and requests per second, for example.

If one image conversion takes 200 milliseconds, that is latency. If a worker pool completes 50 conversions per second, that is throughput. Adding workers may increase throughput without making one conversion faster; queueing or contention can even increase its latency. The two measures are related by the system and workload, but they are not simple inverses.

Both definitions require boundaries. A useful measurement says where timing begins and ends, what counts as completed work and under what load. [Request for Comments (RFC) 1242's network-device definitions](https://www.rfc-editor.org/rfc/rfc1242.html) are specialised examples of this discipline. Google's [Site Reliability Engineering examples](https://sre.google/sre-book/service-level-objectives/#indicators-in-practice) apply latency and throughput to services and data pipelines.

### Why a builder needs to know this

Calling a system “fast” hides the question that matters. Interactive users often feel latency, while imports, uploads and batch jobs may be constrained by throughput. Both influence capacity and cost, but improving one does not guarantee an improvement in the other.

### Pitfalls

- Latency and throughput are not automatically inverses; parallelism, batching and queues break that intuition.
- An average can hide a slow tail. Percentiles can reveal how often users experience much slower operations.
- Offered work, completed work and theoretical capacity are different quantities.
- A measurement without units, workload and boundaries is not reusable evidence.

### Related concepts in TFB

- [Processors, memory and persistent storage](#processors-memory-and-persistent-storage) - constrained resources influence both measures.
- [Operating systems and running programs](#operating-systems-and-running-programs) - scheduling and shared work affect observed performance.
- [Time, clocks, dates and time zones](#time-clocks-dates-and-time-zones) - latency depends on measuring elapsed time with a suitable clock.

### Deeper concepts

- Capacity, saturation and queueing - how demand changes waiting time and completed work.
- Percentiles and distributions - how to describe experiences hidden by an average.
- Performance testing - producing measurements that represent realistic workloads.

### Further reading

- [Google Site Reliability Engineering: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/#indicators-in-practice) - latency, throughput and distributions in production services.
- [RFC 1242: Benchmarking Terminology](https://www.rfc-editor.org/rfc/rfc1242.html) - precise examples of why measurement boundaries matter.

## Chapter status

The Chapter 1 first pass now contains eight awareness-level entries. Optional number-notation explanations remain in [further territory](../further/01-computing-foundations.md).

[Return to the guide map](../README.md#map-of-the-territory) · [Browse the complete Chapter 1 plan](../OUTLINE.md#1-computing-foundations)
