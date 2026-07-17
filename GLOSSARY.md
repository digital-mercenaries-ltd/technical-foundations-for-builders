# Glossary

Status: Milestone 4 Chapter 3 approved - 2026-07-18

This alphabetical index defines terms used by the drafted concepts and reader-facing navigation. It will grow with the guide. Definitions stay short and link to a published canonical explanation rather than to an outline placeholder.

## A

### Abstraction

A useful model and set of operations that suppress details irrelevant at that level; see [Abstraction, information hiding and interfaces](chapters/03-software-engineering.md#abstraction-information-hiding-and-interfaces).

### Artificial intelligence (AI)

Software techniques that produce outputs associated with human cognitive work, including the models and agents used to assist software development; see [AI-assisted engineering](README.md#12-ai-assisted-engineering).

## B

### Base (or radix)

The number of digit values used by a positional number system: decimal is base 10, [binary](further/01-computing-foundations.md#binary-numbers) is base 2, octal is base 8 and hexadecimal is base 16.

### Big-O notation

A shorthand for how an algorithm's resource requirements are bounded as its input grows; it does not state an operation's measured speed. See [Collections, data structures and algorithmic cost](chapters/02-programming-foundations.md#collections-data-structures-and-algorithmic-cost).

### Binary

A base-2 positional number system using only `0` and `1`; see [Binary numbers](further/01-computing-foundations.md#binary-numbers).

### Bit

A binary digit with one of two values, `0` or `1`; see [Bits and bytes](chapters/01-computing-foundations.md#bits-and-bytes).

### Byte

A group of eight bits; see [Bits and bytes](chapters/01-computing-foundations.md#bits-and-bytes).

## C

### Central processing unit (CPU)

The processor that follows machine instructions and performs calculations; see [Processors, memory and persistent storage](chapters/01-computing-foundations.md#processors-memory-and-persistent-storage).

### Cohesion

The degree to which the responsibilities inside a module belong together; see [Modularity, cohesion, coupling and separation of concerns](chapters/03-software-engineering.md#modularity-cohesion-coupling-and-separation-of-concerns).

### Continuous integration (CI)

The practice of frequently integrating small changes into a shared primary branch and checking the combined result; see [Build automation, continuous integration and fast feedback](chapters/03-software-engineering.md#build-automation-continuous-integration-and-fast-feedback).

### Coordinated Universal Time (UTC)

The international time standard used as a reference for civil time and offsets; see [Time, clocks, dates and time zones](chapters/01-computing-foundations.md#time-clocks-dates-and-time-zones).

### Coupling

The extent to which one module depends on another module's details or behaviour; see [Modularity, cohesion, coupling and separation of concerns](chapters/03-software-engineering.md#modularity-cohesion-coupling-and-separation-of-concerns).

## E

### Encoding

A defined way of mapping information to another representation, such as mapping Unicode values to bytes with UTF-8; see [Text, Unicode and character encodings](chapters/01-computing-foundations.md#text-unicode-and-character-encodings).

### Exception

A structured mechanism that reports an abnormal condition and changes a program's normal control flow; see [Errors, exceptions and cleanup](chapters/02-programming-foundations.md#errors-exceptions-and-cleanup).

## F

### Floating point

A finite-precision number representation that covers a wide range by storing a significant part and a scale; see [Floating-point approximation](chapters/01-computing-foundations.md#floating-point-approximation).

## H

### Hexadecimal (hex)

A base-16 positional notation using digits `0` to `9` and letters `A` to `F`; see [Hexadecimal and octal](further/01-computing-foundations.md#hexadecimal-and-octal).

## I

### Interface

The operations and behavioural promises that another component is allowed to depend on; see [Abstraction, information hiding and interfaces](chapters/03-software-engineering.md#abstraction-information-hiding-and-interfaces).

### Invariant

A condition that must remain true in every valid state covered by a design; see [Functional requirements, quality attributes, specifications and invariants](chapters/03-software-engineering.md#functional-requirements-quality-attributes-specifications-and-invariants).

## L

### Latency

The elapsed time from a defined start to a defined finish for one operation or piece of work; see [Latency and throughput](chapters/01-computing-foundations.md#latency-and-throughput).

## M

### Module

A unit of code with its own namespace and an interface to other code; see [Modules, packages and dependencies](chapters/02-programming-foundations.md#modules-packages-and-dependencies).

### Modularity

The division of a system into parts with understandable responsibilities and controlled relationships; see [Modularity, cohesion, coupling and separation of concerns](chapters/03-software-engineering.md#modularity-cohesion-coupling-and-separation-of-concerns).

### Mutation

A change to an existing mutable value or location; see [Variables, state, mutability and side effects](chapters/02-programming-foundations.md#variables-state-mutability-and-side-effects).

## N

### National Institute of Standards and Technology (NIST)

A United States standards and measurement agency whose technical glossaries and publications are used throughout TFB; see its role in defining [bits and bytes](chapters/01-computing-foundations.md#bits-and-bytes).

## O

### Octal

A base-8 positional notation using digits `0` to `7`; see [Hexadecimal and octal](further/01-computing-foundations.md#hexadecimal-and-octal).

### Octet

An unambiguous name for an eight-bit byte, commonly used in Internet standards; see [Bits and bytes](chapters/01-computing-foundations.md#bits-and-bytes).

## P

### Portable Operating System Interface (POSIX)

A family of standards for operating-system interfaces. TFB uses it as one source for [process and thread behaviour](chapters/01-computing-foundations.md#operating-systems-and-running-programs) and [clock behaviour](chapters/01-computing-foundations.md#time-clocks-dates-and-time-zones), not as a description of every platform.

### Positional number system

A way of writing numbers in which a digit's value depends on its position, as explained in [Binary numbers](further/01-computing-foundations.md#binary-numbers).

### Process

A running instance of a program with resources managed by an operating system; see [Operating systems and running programs](chapters/01-computing-foundations.md#operating-systems-and-running-programs).

### Progressive disclosure

Presenting a small first view and making additional detail optional so that breadth does not create immediate overwhelm; see [How the guide avoids overwhelm](README.md#how-the-guide-avoids-overwhelm).

## R

### Random-access memory (RAM)

Working memory used by active programs and data; see [Processors, memory and persistent storage](chapters/01-computing-foundations.md#processors-memory-and-persistent-storage).

### Refactoring

Changing software's internal structure through small, behaviour-preserving steps so that it becomes easier to understand or modify; see [Refactoring, technical debt, legacy systems and evolutionary replacement](chapters/03-software-engineering.md#refactoring-technical-debt-legacy-systems-and-evolutionary-replacement).

### Request for Comments (RFC)

A numbered publication in the Internet technical-document series. Some RFCs define standards; others record information, experiments or current practice. Chapter 1 uses RFCs to ground [Internet byte terminology](chapters/01-computing-foundations.md#bits-and-bytes), [time representations](chapters/01-computing-foundations.md#time-clocks-dates-and-time-zones) and [performance measurements](chapters/01-computing-foundations.md#latency-and-throughput).

### Runtime

The environment and services used while a program executes; see [Source code, programming languages and runtimes](chapters/02-programming-foundations.md#source-code-programming-languages-and-runtimes).

## S

### Side effect

An observable change beyond producing a function's result, such as changing shared state or writing to another system; see [Variables, state, mutability and side effects](chapters/02-programming-foundations.md#variables-state-mutability-and-side-effects).

### Specification

A record of expected properties and constraints precise enough to guide construction and evaluation; see [Functional requirements, quality attributes, specifications and invariants](chapters/03-software-engineering.md#functional-requirements-quality-attributes-specifications-and-invariants).

## T

### Technical debt

A metaphor for internal decisions that make future changes cost more; see [Refactoring, technical debt, legacy systems and evolutionary replacement](chapters/03-software-engineering.md#refactoring-technical-debt-legacy-systems-and-evolutionary-replacement).

### Throughput

The amount of completed work per unit time under defined conditions; see [Latency and throughput](chapters/01-computing-foundations.md#latency-and-throughput).

### Time zone

A maintained set of rules mapping local civil times to offsets from Coordinated Universal Time; see [Time, clocks, dates and time zones](chapters/01-computing-foundations.md#time-clocks-dates-and-time-zones).

### Type

A classification that helps determine which values and operations a program permits and how those operations behave; see [Values, types and conversions](chapters/02-programming-foundations.md#values-types-and-conversions).

## U

### Unicode

A standard that assigns numbers to the characters and other text elements used by writing systems; an encoding such as UTF-8 represents those values as bytes. See [Text, Unicode and character encodings](chapters/01-computing-foundations.md#text-unicode-and-character-encodings).

### Unicode scalar value

A numbered unit that Unicode encodings can represent; one visible character may contain more than one scalar value. See [Text, Unicode and character encodings](chapters/01-computing-foundations.md#text-unicode-and-character-encodings).

### Unicode Transformation Format 8-bit (UTF-8)

A variable-length Unicode encoding that uses one to four bytes for each Unicode scalar value; see [Text, Unicode and character encodings](chapters/01-computing-foundations.md#text-unicode-and-character-encodings).

### Unsigned integer

A whole-number representation with no negative values; an unsigned 8-bit integer can represent values from 0 through 255. See [Integer ranges and overflow](chapters/01-computing-foundations.md#integer-ranges-and-overflow).

## V

### Verification

The use of tests, review, analysis or other evidence to assess whether an implementation, artefact or model satisfies specified requirements; see [Testing, verification and evidence](chapters/03-software-engineering.md#testing-verification-and-evidence).

### Version control

A system that records project states and changes so that people can compare, attribute and recover known versions; see [Version control, code review, shared ownership and recovery](chapters/03-software-engineering.md#version-control-code-review-shared-ownership-and-recovery).
