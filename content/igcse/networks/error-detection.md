---
title: "2.2 Methods of Error Detection"
description: "Master parity checks, parity blocks, checksums, check digits, and ARQ over a structured 3-session block."
type: lesson
order: 5
draft: false
---

## Learning Goals

- Explain how a parity bit detects single-bit errors.
- Use a parity block (2D parity) to locate and correct a single-bit error.
- Explain how checksums and check digits operate.
- Describe how Automatic Repeat Request (ARQ) handles missing or corrupted data.
- Clearly distinguish *detecting* an error from *correcting* or *retransmitting* it.

---

## Session 1 & 2: The Mechanics of Detection (Monday Double)

### 1. Parity Bits & Their Blind Spots

A **parity bit** is an extra bit added to a binary code to ensure the total number of `1`s is either always **even** (Even Parity) or always **odd** (Odd Parity).

```text
Data Bits:   1 0 1 1 0 0 1
             ↑   ↑ ↑     ↑
           Four 1s

Even Parity Bit = 0

Transmitted Data:
1 0 1 1 0 0 1 0
```

```text
Data Stream:      1   0   1   1   0   0   1
Count of '1's:    1, 3, 4, and 7 are '1's (Total = 4 ones)
Parity Rule:      Even Parity requires an EVEN number of '1's.
Parity Bit:       0  (since 4 is already even)
Transmitted Data: 1  0  1  1  0  0  1  [0]
```

#### The Catch

If **two bits** change during transmission, the parity check may not detect the error.

For example:

```text
Original: 1 0 1 1 0 0 1 0
Received: 1 1 1 1 0 0 0 0
```

Although two bits have changed, the total number of `1`s remains even, so the parity check incorrectly indicates that the data is valid.

> **Key Point:** A single parity bit can detect many transmission errors, but it cannot reliably detect multiple-bit errors.

---

### 2. Parity Blocks (2D Parity)

To locate an error so that it can be corrected, systems can use a **parity block** (two-dimensional parity).

Data is arranged into rows and columns, with parity bits generated for both directions.

```text
                Column Parity
  1  0  1  1  | 1
  0  1  1  0  | 0
  1  1  0  0  | 0
--------------+---
  0  0  1  1  | Overall Check
 Row Parity
```

### How It Corrects Errors

If a single bit changes:

- One row parity check fails.
- One column parity check fails.
- The intersection identifies the incorrect bit.

That bit can then be flipped back to its correct value.

#### Example

If the bit in Row 2, Column 3 changes:

```text
                Column Parity
  1  0  1  1  | 1
  0  1  0  0  | 0   ← Row fails
  1  1  0  0  | 0
--------------+---
  0  0  1  1  |     ↑
              Column fails
```

The failed row and failed column identify the exact location of the error.

> **Key Point:** A parity block can both detect and correct a single-bit error.

---

### 3. Checksums and Check Digits

#### Checksum

A **checksum** is a value calculated from a block of data.

Process:

1. The sender calculates the checksum.
2. The checksum is transmitted with the data.
3. The receiver recalculates the checksum.
4. The two values are compared.

If they differ, an error has occurred during transmission.

```text
Data → Checksum Calculated → Sent
                 ↓
Data → Checksum Recalculated → Compared
```

> Checksums can detect errors but cannot identify exactly where the error occurred.

---

#### Check Digit

A **check digit** is an additional digit added to an identification code.

Examples:

- Barcodes
- ISBN numbers
- National identification systems
- Product codes

The check digit is calculated from the other digits using a mathematical formula.

Example:

```text
1234567X
```

The final character (`X`) is calculated from the preceding digits.

If a user mistypes the code, the calculation usually fails and the error is detected.

> Check digits are primarily used to detect data-entry errors rather than transmission errors.

---

## Session 3: Responding to Errors — ARQ (Wednesday Single)

Detecting an error is only half the process.

**Automatic Repeat Request (ARQ)** combines error detection with acknowledgements and retransmission.

### How ARQ Works

```text
[Sender] --------------------> [Receiver]
   |                               |
   | <---------- ACK --------------|
   |       (Packet OK)             |
   |                               |
   | <---------- NAK --------------|
   |      (Error Detected)         |
   |                               |
   +----- Resend Packet ---------->|
```

A timeout mechanism is also used.

```text
Send Packet
      ↓
Start Timer
      ↓
ACK received?
      ↓
 Yes → Stop
      ↓
 No
      ↓
Timeout Expires
      ↓
Resend Packet
```

### ARQ Process

1. Sender transmits a packet.
2. Sender starts a timeout timer.
3. Receiver checks the packet using parity, a checksum, or another error-detection method.
4. If the packet is correct, the receiver sends an **ACK** (Acknowledgement).
5. If the packet is corrupted, the receiver sends a **NAK** (Negative Acknowledgement).
6. If a NAK is received, the sender retransmits the packet.
7. If no reply is received before the timeout expires, the sender assumes the packet or response was lost and retransmits it.

### Important Exam Point

ARQ does **not** detect errors itself.

ARQ relies on another method such as:

- Parity
- Parity blocks
- Checksums
- CRC (Cyclic Redundancy Check)

ARQ simply manages the retransmission process after an error has been detected.

---

## Exam-Style Core Practice

Complete these questions on paper.

### 1. Parity Calculation

State the even-parity bit required for the 7-bit sequence:

```text
1 1 0 0 1 1 0
```

Explain your answer.

---

### 2. Comparing Methods

Explain why:

- A checksum cannot identify which bit was corrupted.
- A parity block can identify the location of a single-bit error.

---

### 3. ARQ Scenario

A weather satellite transmits data packets to a ground station over a noisy radio link.

Describe the roles of:

- `ACK`
- `NAK`
- Timeout

in ensuring that data arrives correctly.

---

## Exit Check

1. What is the difference between even parity and odd parity?
2. What is the main limitation of a single parity bit?
3. What does a check digit protect against?
4. Does ARQ detect errors itself, or does it rely on another error-detection method? Explain.

---

## Summary Table

| Method | Detect Errors | Locate Errors | Correct Errors | Retransmit Data |
|----------|--------------|--------------|--------------|--------------|
| Parity Bit | ✅ | ❌ | ❌ | ❌ |
| Parity Block (2D) | ✅ | ✅ | ✅ (single-bit) | ❌ |
| Checksum | ✅ | ❌ | ❌ | ❌ |
| Check Digit | ✅ | ❌ | ❌ | ❌ |
| ARQ | ❌ | ❌ | ❌ | ✅ |

> **Remember:** Detection, correction, and retransmission are three different concepts. Exam questions often test whether you can distinguish between them.