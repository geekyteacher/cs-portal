---
title: Bit Manipulation
description: Apply the logical operations, shifts, and masks required by the CAIE 9618 syllabus.
order: 3
draft: false
---

## Learning goals

- Apply AND, OR, and XOR to binary values.
- Trace the effect of a logical operation on binary values.
- Perform logical, arithmetic, and cyclic shifts.
- Use bit masks to test and set bits.

## Suggested teaching time

Use this page for Doubles 8–9 in the [unit plan](./index): practise the
logical operations first, then compare shift types and apply masks.

## 1. Bitwise logical operations

The syllabus uses **AND**, **OR**, and **XOR**. Each operation is applied to
corresponding bits in two values. In the assembly instruction set, the
result replaces the value in the ACC.

| A | B | AND | OR | XOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

| Operation | Purpose | Worked binary example |
| --- | --- | --- |
| **AND** | Produces 1 only when both corresponding bits are 1. | `10110110 AND 00001111 = 00000110` |
| **OR** | Produces 1 when either or both corresponding bits are 1. | `10110000 OR 00001111 = 10111111` |
| **XOR** | Produces 1 when the corresponding bits are different. | `10110110 XOR 00001111 = 10111001` |

## 2. Shifts

The syllabus includes **logical**, **arithmetic**, and **cyclic** shifts to
the left and right. Apply the shift to the ACC by the number of positions
given. Track bits that leave one end and what enters at the other end.

Use the eight-bit value `10110110` for these examples:

| Shift | Result after shifting one place | What happens |
| --- | --- | --- |
| Logical left | `01101100` | The leftmost bit is discarded and `0` enters at the right. |
| Logical right | `01011011` | The rightmost bit is discarded and `0` enters at the left. |
| Arithmetic left | `01101100` | The leftmost bit is discarded and `0` enters at the right; check for overflow when interpreting a signed value. |
| Arithmetic right | `11011011` | The rightmost bit is discarded and the sign bit is copied into the leftmost position. |
| Cyclic left | `01101101` | The leftmost bit wraps around into the rightmost position. |
| Cyclic right | `01011011` | The rightmost bit wraps around into the leftmost position. |

For arithmetic right shifts, the leftmost bit is treated as the sign bit.
Do not treat arithmetic and logical right shifts as interchangeable.
Repeated shifts apply the same rule once for each position.

## 3. Masks

A **mask** is a bit pattern combined with a value using a logical operation
to work with selected bits.

### Test a bit

To test bit 2 (counting the rightmost bit as bit 0) in `10110110`, use the
mask `00000100` with AND:

```text
  10110110
AND 00000100
  --------
  00000100
```

The result is non-zero, so bit 2 was set. If the result were `00000000`, bit
2 would be clear.

### Set a bit

To set bit 3, use the mask `00001000` with OR:

```text
  10110110
OR  00001000
  --------
  10111110
```

All other bits are unchanged because the mask has `0` in their positions.

## Class practice

1. Complete the truth table for AND, OR, and XOR from memory.
2. Calculate `11001010 AND 00001111`, `11001010 OR 00001111`, and
   `11001010 XOR 00001111`.
3. Starting with `01101001`, calculate one-place logical, arithmetic, and
   cyclic shifts in both directions.
4. Use a mask and AND to test whether bit 5 of `10110110` is set.
5. Use a mask and OR to set bit 1 of `10110000`.
6. Explain why OR is suitable for setting a bit and AND is suitable for
   testing a bit.
7. Describe how bit manipulation could be used to monitor or control a
   device, such as checking a status bit or setting an output bit.

## Homework

Complete a short set of bitwise-operation and shift questions assigned by
your teacher. Include one mask question that tests a bit and one that sets a
bit. Show aligned binary working and state what the result means.

## Exit check

1. In what situation does XOR produce 1?
2. What enters the vacated position in a logical right shift?
3. How does an arithmetic right shift differ from a logical right shift?
4. Which logical operation would you use to test a bit? Which to set one?
