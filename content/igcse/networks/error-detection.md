---
title: "2.2 Methods of Error Detection"
description: Explain how parity, checksums, check digits, and ARQ can identify or respond to errors.
type: lesson
order: 5
draft: false
---

## Learning goals

- Explain how a parity bit can be used to detect an error.
- Use a parity block to locate a single-bit error.
- Explain how a checksum and a check digit are used.
- Describe how automatic repeat request (ARQ) responds when data is missing
  or corrupted.
- Distinguish detecting an error from correcting or retransmitting data.

## Quick start

Data can be changed accidentally while it is stored or transmitted.

1. What might happen if one bit changes from `0` to `1`?
2. How could a receiver check whether the data it received is the data that
   was sent?

## Parity checks

A **parity bit** is an extra bit added to a group of data bits. It is chosen
so the total number of `1` bits is either even or odd, depending on the
system.

- With **even parity**, the data bits and parity bit together contain an
  even number of `1`s.
- With **odd parity**, they contain an odd number of `1`s.

### Worked example: even parity

The data bits are `1 0 1 1 0 0 1`. There are four `1`s, so the even-parity
bit is `0`. The complete group still has an even number of `1`s.

If one bit changes during transmission, the receiver may find the parity is
wrong and detect an error. A single parity bit does not identify which bit
changed, and an even number of bit changes may go undetected.

## Parity blocks

A **parity block** arranges groups of bits in rows and uses parity checks
across both rows and columns. If one bit changes, the row and column with
incorrect parity can identify the bit's position. The bit can then be
corrected by changing it to its opposite value.

This method can locate a single-bit error in the block. Do not assume it can
always identify or correct multiple errors.

## Checksums

A **checksum** is a value calculated from a block of data.

1. The sender calculates a checksum from the data.
2. The checksum is sent with the data.
3. The receiver calculates a new checksum from the received data.
4. The receiver compares the calculated value with the one sent.
5. If the values differ, the receiver knows that an error may have occurred.

A checksum can help detect an error; by itself, it does not explain which
bits are wrong or correct the data.

## Check digits

A **check digit** is an extra digit calculated from the other digits in an
identifier, such as a product code. When the code is entered or read, the
check digit is recalculated and compared with the digit received. A mismatch
indicates that the identifier may have been entered or read incorrectly.

Check digits are used to detect common errors in digit sequences. They do
not guarantee detection of every possible error.

## Automatic repeat request (ARQ)

**Automatic repeat request (ARQ)** is a method for requesting that data be
sent again when it is missing or an error is detected. It relies on error
detection and communication between the receiver and sender.

1. The sender transmits a packet.
2. The receiver checks the packet and sends an acknowledgement (**ACK**) if
   it is received successfully.
3. If an error is detected, the receiver may send a negative
   acknowledgement (**NAK**).
4. If the sender does not receive an acknowledgement before a timeout, it
   treats the packet as potentially lost.
5. The sender retransmits the packet when required.

Parity, checksums, and check digits are ways to **detect** an error. ARQ is a
way to respond by requesting retransmission; it does not itself describe how
the data error is detected.

## Compare the methods

| Method | What it checks | What happens when an error is found |
| --- | --- | --- |
| **Parity bit** | Whether a group has an even or odd number of `1` bits, as required by the system. | Indicates that an error may have occurred. |
| **Parity block** | Row and column parity across a block of bits. | Can locate a single-bit error so it can be corrected. |
| **Checksum** | Whether a recalculated value matches the sent value. | Indicates that the data may have changed. |
| **Check digit** | Whether a digit calculated from an identifier matches the check digit. | Indicates a possible data-entry or reading error. |
| **ARQ** | Whether the receiver acknowledges successful receipt. | Requests retransmission after an error or timeout. |

## Practice

### 1. Parity

For each seven-bit group, state the parity bit needed for **even parity**:

1. `1 0 1 1 0 0 1`
2. `0 1 0 0 0 0 0`
3. `1 1 1 1 1 1 1`
4. `0 0 0 0 0 0 0`

### 2. Choose a method

Choose the most suitable method from **parity bit**, **parity block**,
**checksum**, **check digit**, or **ARQ**:

1. A receiver needs to identify the row and column containing one changed
   bit.
2. A product barcode needs an extra digit to help detect an incorrectly
   entered code.
3. A receiver compares a value recalculated from a data block with the value
   sent alongside it.
4. A sender must send a packet again after it receives a NAK or a timeout
   occurs.

### 3. Explain a checksum

Describe how a sender and receiver use a checksum to detect that data may
have changed during transmission.

### 4. Describe ARQ

A packet is corrupted while being transmitted. Describe how error detection
and ARQ can lead to the packet being sent again. Use the terms `ACK`, `NAK`,
and `timeout` where appropriate.

## Homework

Watch the videos that match the error-detection methods:

- [20. Cambridge IGCSE (0478/0984) 2.2 The need for error
  checking](https://youtu.be/ckvEN_JyiKE)
- [21. Cambridge IGCSE (0478/0984) 2.2 Error detection
  methods](https://youtu.be/TEICs3IaKF4)
- [22. Cambridge IGCSE (0478/0984) 2.2 Check
  digits](https://youtu.be/p60du0zr_H0)
- [23. Cambridge IGCSE (0478/0984) 2.2 Automatic Repeat Query
  (ARQ)](https://youtu.be/SqTS3ZIbwIA)

Complete the parity and error-detection questions assigned by your teacher.
Then write a four-step explanation of how a checksum is checked, and a
separate explanation of how ARQ requests a retransmission. Keep detection
and retransmission as distinct steps.

## Exit check

1. What does a parity bit check?
2. What additional information does a parity block use to locate a single
   changed bit?
3. What does a receiver do with a checksum?
4. What is the purpose of a check digit?
5. What can cause an ARQ system to request retransmission?
