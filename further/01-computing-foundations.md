# Further territory: Computing foundations

These entries support the [Chapter 1 first pass](../chapters/01-computing-foundations.md) without being prerequisites for it. They explain number notations that are useful to recognise when they appear in code, logs and technical documentation.

## Binary numbers

*Writing quantities with two digits instead of ten.*

### What they are

Binary is a [**positional number system in base 2**](../GLOSSARY.md#positional-number-system). It uses only `0` and `1`. Each place is worth twice the place to its right, just as each place in ordinary decimal notation is worth ten times the place to its right.

To read `101101` as an unsigned binary number, add the place values whose digit is `1`:

```text
binary digits:  1   0   1   1   0   1
place values:  32  16   8   4   2   1
included:       32   0   8   4   0   1  = 45
```

Therefore `101101₂` and `45₁₀` are two representations of the same quantity. Leading zeroes do not change the value, so `00101101₂` is also 45, but they can communicate a fixed width of eight bits. [Harvard CS50 introduces the same place-value model](https://cs50.harvard.edu/x/notes/0/#binary).

A fixed group of *n* bits, treated as a non-negative integer, has `2ⁿ` patterns and can represent values from 0 through `2ⁿ - 1`. This is why technical limits and capacities so often appear near powers of two.

### Why a builder needs to know this

Programming languages expose binary notation and operations. Python, for example, uses the prefix `0b`, so decimal 45 can be written as `0b101101` ([Python's integer-literal syntax](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)). Individual bits are also used as on/off flags: several permissions or settings can be packed into one value and manipulated position by position with **bitwise operations**.

The model helps explain integer limits, memory sizes, colour components, permissions, network addressing and the compact hexadecimal notation used in logs and identifiers. You rarely need to convert large values by hand; you need to recognise what the representation implies.

### Pitfalls

- **Digits alone do not reveal the base.** `101` means one hundred and one in decimal but five in binary. Label non-decimal values when context is unclear.
- **A pattern is not automatically unsigned.** A type or format decides whether bits represent an unsigned integer, a signed integer that may be negative, text, flags or something else.
- **Pattern count and maximum value differ by one.** Eight bits have 256 patterns, but the largest unsigned value is 255.
- **Width depends on the executing environment or format.** Python integers can grow to available memory, while JavaScript bitwise operations on ordinary numbers convert values to 32-bit integers ([MDN's bitwise AND description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND#description)).
- **Bitwise and logical operations are different.** One acts on bit positions; the other makes truth-value decisions.

### Related concepts in TFB

- [Bits and bytes](../chapters/01-computing-foundations.md#bits-and-bytes) - the storage units used by the notation.
- [Hexadecimal and octal](#hexadecimal-and-octal) - readable shorthand for grouped binary digits.
- [Integer ranges and overflow](../chapters/01-computing-foundations.md#integer-ranges-and-overflow) - what happens at the boundary of a fixed representation.
- [Values, types and conversions](../chapters/02-programming-foundations.md#values-types-and-conversions) - how programs interpret and convert represented values.
- Planned: Boolean logic and permissions.

### Deeper concepts

- Two's complement and signed integers - how fixed-width binary represents negative values.
- Bit masks, shifts and Boolean algebra - how programs inspect and move individual bit positions.

### Further reading

- [Harvard CS50: Binary](https://cs50.harvard.edu/x/notes/0/#binary) - a visual beginner-level explanation.
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

Hex is a compact human-readable view of binary data. You will see it in logs, identifiers, hashes (fixed-size fingerprints of data), memory tools and communication formats. Cascading Style Sheets (CSS) colours use two hex digits for each red, green and blue component, so `#FF0000` means maximum red with no green or blue ([CSS Color 4 hex notation](https://www.w3.org/TR/css-color-4/#hex-notation)). Internet Protocol version 6 (IPv6) addresses also write their 16-bit pieces in hex ([IPv6 address syntax](https://www.rfc-editor.org/rfc/rfc3986.html#section-3.2.2)).

Octal is less common, but it remains visible in Unix-style permissions because read, write and execute are three on/off choices. Three bits map to one octal digit, so `7` corresponds to binary `111`. The [GNU Coreutils permissions guide](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html) explains how a mode such as `755` represents three permission groups.

### Pitfalls

- **The same digits change value with the base.** `10` is decimal ten, binary two, octal eight or hexadecimal sixteen.
- **Hex text is not raw bytes.** The two text characters `2D` are a printable representation; decoding them as base 16 produces one byte. [Internet standard RFC 4648 defines this base16 mapping](https://www.rfc-editor.org/rfc/rfc4648.html#section-8).
- **Permission modes are not decimal.** Unix mode `755` is octal; reading it as seven hundred and fifty-five gives the wrong model.
- **Leading-zero rules vary by language.** Use explicit prefixes such as `0o` instead of relying on legacy notation.
- **Grouping prevents mistakes.** Convert hex in four-bit groups and octal in three-bit groups rather than applying decimal digit intuition.

### Related concepts in TFB

- [Bits and bytes](../chapters/01-computing-foundations.md#bits-and-bytes) - why two hex digits fit one byte.
- [Binary numbers](#binary-numbers) - the underlying representation being grouped.
- Planned: CSS colours, Unix permissions, IP addresses, hashes and cryptography.

### Deeper concepts

- Base-N encoding versus numeric notation - how printable encodings differ from writing a number in another base.
- Bit masks and permission flags - how grouped bits represent independent choices.
- Byte dumps and endianness - how tools display the order of bytes in memory or files.
- Unicode code-point, universally unique identifier (UUID) and hash notation - common conventions that use hex-shaped text.

### Further reading

- [W3C CSS Color 4: Hex notation](https://www.w3.org/TR/css-color-4/#hex-notation) - a familiar use of byte-sized hex components.
- [GNU Coreutils: Numeric modes](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html) - the practical connection between octal and Unix permissions.

[Return to Chapter 1](../chapters/01-computing-foundations.md) · [Browse the complete Chapter 1 plan](../OUTLINE.md#1-computing-foundations)
