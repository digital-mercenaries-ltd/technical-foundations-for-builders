# Chapter 1 - Computing foundations

Computers store and transform information by giving meaning to physical states. This chapter builds the lowest-level model needed by the rest of TFB: how those states become bits, numbers, text and files; how processors act on them; and how finite time, memory and storage shape a system.

The aim is recognition, not manual calculation. You should finish these entries able to distinguish a value from its representation, understand why the same bits can mean different things and recognise when a low-level detail may explain high-level behaviour.

## Chapter map

The Milestone 1 prototype contains three completed entries:

1. [Bits and bytes](#bits-and-bytes)
2. [Binary numbers](#binary-numbers)
3. [Hexadecimal and octal](#hexadecimal-and-octal)

Later entries will cover Boolean logic; integers and overflow; floating-point precision; text and Unicode; processors; memory and storage; operating systems; processes and threads; time; latency and throughput; caching; compression; serialisation and data formats.

## Bits and bytes

*The basic units used to store and move digital information.*

### What they are

A **bit**, short for *binary digit*, has one of two values: `0` or `1`. A **byte** is a group of eight bits, so it has `2⁸`, or 256, possible patterns. If those patterns are interpreted as an unsigned whole number, they cover 0 to 255: zero consumes one of the 256 possibilities. [NIST defines a byte as eight bits](https://csrc.nist.gov/glossary/term/byte).

The most useful distinction is between a **container and its interpretation**. Consider this byte:

```text
01000001
```

Read as an unsigned number, it is 65. Read using the UTF-8 text encoding, it represents `A`. In another format it could be part of a colour, machine instruction, compressed file or encrypted message. The bits do not carry that meaning by themselves; a data type, encoding or format supplies it. The [Unicode Standard's UTF-8 definition](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G7404) also shows why a visible character is not necessarily one byte: a Unicode value may require between one and four bytes in UTF-8.

### Why a builder needs to know this

Files, memory, databases and network messages expose sizes in bytes. Network speeds and cryptographic key strengths are often expressed in bits. Understanding the difference helps you reason about upload limits, storage bills, memory use, text length and values such as a 256-bit encryption key.

HTTP uses the more precise word **octet** for an eight-bit byte and defines `Content-Length` as a count of octets ([HTTP Semantics, section 8.6](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.6)). A browser's [`Blob.size`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/size), by contrast, reports bytes. These are different interfaces to the same basic unit.

### Pitfalls

- **A character is not a byte.** Counting visible characters does not reliably predict encoded or transmitted size.
- **Bits are not automatically numbers.** Always ask what interpretation or format applies.
- **Bits and bytes are easy to confuse.** Product interfaces commonly use lowercase `b` for bits and uppercase `B` for bytes.
- **MB and MiB are not identical.** `1 MB` is 1,000,000 bytes; `1 MiB` is 1,048,576 bytes. [NIST explains the decimal and binary prefixes](https://physics.nist.gov/cuu/Units/binary.html).

### Related concepts in TFB

- [Binary numbers](#binary-numbers) - how a bit pattern can represent a quantity.
- [Hexadecimal and octal](#hexadecimal-and-octal) - compact ways to write groups of bits.
- Planned: text encodings, data types, files, network protocols and cryptography.

### Deeper concepts

- Signed integers and two's complement
- Bitwise operations and masks
- Endianness and memory addressing
- Error detection and correction

### Further reading

- [Harvard CS50: Lecture 0 notes](https://cs50.harvard.edu/x/notes/0/) - an accessible introduction to information represented with bits.
- [NIST: Byte](https://csrc.nist.gov/glossary/term/byte) - the concise standards-linked definition.
- [NIST: Prefixes for binary multiples](https://physics.nist.gov/cuu/Units/binary.html) - the difference between units such as MB and MiB.

## Binary numbers

*Writing quantities with two digits instead of ten.*

### What they are

Binary is a **positional number system in base 2**. It uses only `0` and `1`. Each place is worth twice the place to its right, just as each place in ordinary decimal notation is worth ten times the place to its right.

To read `101101` as an unsigned binary number, add the place values whose digit is `1`:

```text
binary digits:  1   0   1   1   0   1
place values:  32  16   8   4   2   1
included:       32   0   8   4   0   1  = 45
```

Therefore `101101₂` and `45₁₀` are two representations of the same quantity. Leading zeroes do not change the value, so `00101101₂` is also 45, but they can communicate a fixed width of eight bits. [Harvard CS50 introduces the same place-value model](https://cs50.harvard.edu/x/notes/0/#binary).

An unsigned field containing *n* bits has `2ⁿ` patterns and can represent values from 0 through `2ⁿ - 1`. This is why technical limits and capacities so often appear near powers of two.

### Why a builder needs to know this

Programming languages expose binary notation and operations. Python, for example, uses the prefix `0b`, so decimal 45 can be written as `0b101101` ([Python's integer-literal syntax](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)). Individual bits are also used as on/off flags: several permissions or settings can be packed into one value and manipulated position by position.

The model helps explain integer limits, memory sizes, colour components, permissions, network masks and the compact hexadecimal notation used in logs and identifiers. You rarely need to convert large values by hand; you need to recognise what the representation implies.

### Pitfalls

- **Digits alone do not reveal the base.** `101` means one hundred and one in decimal but five in binary. Label non-decimal values when context is unclear.
- **A pattern is not automatically unsigned.** A type or format decides whether bits represent a positive number, signed number, text, flags or something else.
- **Pattern count and maximum value differ by one.** Eight bits have 256 patterns, but the largest unsigned value is 255.
- **Width depends on the runtime or format.** Python integers can grow to available memory, while JavaScript bitwise operations on ordinary numbers use 32-bit integers ([MDN's bitwise AND description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND#description)).
- **Bitwise and logical operations are different.** One acts on bit positions; the other makes truth-value decisions.

### Related concepts in TFB

- [Bits and bytes](#bits-and-bytes) - the storage units used by the notation.
- [Hexadecimal and octal](#hexadecimal-and-octal) - readable shorthand for grouped binary digits.
- Planned: Boolean logic, integer overflow, data types and permissions.

### Deeper concepts

- Two's complement and signed integers
- Fixed-width overflow
- Bit masks, shifts and Boolean algebra
- Floating-point representation

### Further reading

- [Harvard CS50: Binary](https://cs50.harvard.edu/x/notes/0/#binary) - a visual beginner-level explanation.
- [Python: Integer literals](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals) - real-world notation for binary, octal and hexadecimal values.
- [MDN: Bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bitwise_operators) - where binary positions appear in JavaScript, including important width rules.

## Hexadecimal and octal

*Compact notations that line up neatly with groups of binary digits.*

### What they are

**Hexadecimal**, usually shortened to **hex**, is base 16. It uses `0` to `9`, then `A` to `F` for values ten to fifteen. **Octal** is base 8 and uses `0` to `7`.

These bases are useful because they align exactly with binary groups. One hex digit represents four bits because `2⁴ = 16`; one octal digit represents three bits because `2³ = 8`.

```text
binary:       0010 1101
hex groups:     2    D    -> 0x2D
decimal:                 45

binary:         101 101
octal groups:     5   5    -> 0o55
decimal:                  45
```

You can check the positional values directly: `0x2D = 2×16 + 13 = 45`, while `0o55 = 5×8 + 5 = 45`. A byte fits exactly into two hex digits, from `00` to `FF`. The prefixes `0x` and `0o` are common programming-language labels for hex and octal; they are not part of the mathematical value. [Python documents `0b`, `0o` and `0x` together](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals).

### Why a builder needs to know this

Hex is a compact human-readable view of binary data. You will see it in logs, identifiers, hashes, memory tools and protocols. CSS colours use two hex digits for each red, green and blue component, so `#FF0000` means maximum red with no green or blue ([CSS Color 4 hex notation](https://www.w3.org/TR/css-color-4/#hex-notation)). IPv6 addresses also write their 16-bit pieces in hex ([URI syntax for IPv6 addresses](https://www.rfc-editor.org/rfc/rfc3986.html#section-3.2.2)).

Octal is less common, but it remains visible in Unix-style permissions because read, write and execute are three on/off choices. Three bits map to one octal digit, so `7` corresponds to binary `111`. The [GNU Coreutils permissions guide](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html) explains how a mode such as `755` represents three permission groups.

### Pitfalls

- **The same digits change value with the base.** `10` is decimal ten, binary two, octal eight or hexadecimal sixteen.
- **Hex text is not raw bytes.** The two text characters `2D` encode a display; decoding them as base 16 produces one byte. [RFC 4648 defines this base16 mapping](https://www.rfc-editor.org/rfc/rfc4648.html#section-8).
- **Permission modes are not decimal.** Unix mode `755` is octal; reading it as seven hundred and fifty-five gives the wrong model.
- **Leading-zero rules vary by language.** Use explicit prefixes such as `0o` instead of relying on legacy notation.
- **Grouping prevents mistakes.** Convert hex in four-bit groups and octal in three-bit groups rather than applying decimal digit intuition.

### Related concepts in TFB

- [Bits and bytes](#bits-and-bytes) - why two hex digits fit one byte.
- [Binary numbers](#binary-numbers) - the underlying representation being grouped.
- Planned: CSS colours, Unix permissions, IP addresses, hashes and cryptography.

### Deeper concepts

- Base-N encoding versus numeric notation
- Bit masks and permission flags
- Byte dumps and endianness
- Unicode code-point, UUID and hash notation

### Further reading

- [RFC 4648: Base16 encoding](https://www.rfc-editor.org/rfc/rfc4648.html#section-8) - the standard mapping between bytes and printable hex.
- [W3C CSS Color 4: Hex notation](https://www.w3.org/TR/css-color-4/#hex-notation) - a familiar use of byte-sized hex components.
- [GNU Coreutils: Numeric modes](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html) - the practical connection between octal and Unix permissions.

## Chapter status

Only the first three concepts are drafted for Milestone 1. The remaining entries will not be written until the structure, depth, voice, links and source choices have been reviewed.
