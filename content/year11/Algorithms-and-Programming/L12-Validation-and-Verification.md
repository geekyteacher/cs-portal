---
title: "Lesson 12: Validation and Verification"
description: "Choose validation and verification checks and apply normal, abnormal, extreme and boundary test data."
order: 12
draft: false
---
## Topics in this page

- Validation checks
- Verification checks
- Test data: normal, abnormal, extreme and boundary

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Explain why input data is validated and verified.
- Identify and choose suitable validation checks.
- Explain visual checking and double-entry verification.
- Select suitable test data and state the expected result.

## Quick Check

1. Does a check that a mark is between 0 and 100 prove that the correct
   student's mark was entered?
2. What is the difference between the largest acceptable value and a value
   just outside the acceptable range?
3. Name one way to check that data has been copied accurately.

## Learn

### Validation and verification are different

**Validation** checks whether data is reasonable and follows specified rules.
It does not prove that the data is correct.

**Verification** checks whether data has been entered or copied accurately
from its source. It does not prove that the original data was correct.

For example, a mark of `76` may pass a range check of `0` to `100` but still
belong to the wrong student. A second check against the original source is
verification.

### Validation checks

| Check | What it checks | Example |
| --- | --- | --- |
| Range | A value is within stated limits. | A mark must be from 0 to 100. |
| Length | A string has an allowed number of characters. | A code must contain 6 characters. |
| Type | A value is the required data type. | A quantity must be an integer. |
| Presence | A required value has been entered. | A surname cannot be blank. |
| Format | Data follows a specified pattern. | A date must follow `DD/MM/YYYY`. |
| Check digit | A digit calculated from other digits is valid. | A barcode check digit is recalculated and compared. |

The suitable checks depend on the rules for the data. A range check cannot,
for example, detect every incorrectly entered value if the wrong value is
still within the allowed range.

### Verification checks

| Check | How it works | Example |
| --- | --- | --- |
| Visual check | A person compares entered data with the original. | Compare a typed address with the paper form. |
| Double entry | Data is entered twice and the two entries are compared. | Type a new password twice; accept only if the entries match. |

These methods help detect copying or typing mistakes. They do not decide
whether the source data itself is valid.

### Selecting test data

Test data is used to check an algorithm or validation rule. State the expected
result for each test.

| Type | Meaning | Example for a mark from 0 to 100 inclusive |
| --- | --- | --- |
| Normal | Typical valid data. | `63` |
| Abnormal | Invalid data that should be rejected. | `-1` or `101` |
| Extreme | The smallest or largest acceptable value. | `0` or `100` |
| Boundary | The extreme acceptable value and the nearest rejected value. | `-1`, `0`, `100`, `101` |

For a pass rule of `Mark >= 50`, also test `49` and `50` to check the pass
boundary. Do not confuse an input-range boundary (`0` and `100`) with a
decision boundary (`49` and `50`).

## Guided Practice

A club accepts an integer age from `11` to `18`, inclusive. The age is
required, and the user is asked to type it twice.

1. Suggest a presence check.
2. Suggest a range check.
3. Give one abnormal value.
4. Give both extreme values.
5. Give one pair of boundary values.
6. Describe how double entry could verify the age.
7. Explain why matching double entries do not prove the age is true.

## Core Practice

### Task 1: Choose validation checks

For each item, choose a suitable check and explain what it would accept or
reject:

1. A username must not be blank.
2. A product code must contain exactly eight characters.
3. A quantity must be a whole number from 1 to 50.
4. A date must be entered in `DD/MM/YYYY` format.
5. A code includes a final check digit.

### Task 2: Select test data

A program accepts a percentage from `0` to `100`, inclusive, and outputs
`"Pass"` for values of `50` or more.

Give normal, abnormal, extreme and boundary test data. State the expected
acceptance or rejection and output for each value. Include the pass threshold
values `49` and `50`.

### Task 3: Verification

Explain when a visual check and a double-entry check would be appropriate.
Give one limitation of each.

## Support

Use these sentence starters:

- “A range check would check that ...”
- “This is validation because ...”
- “Double entry compares ...”
- “This test is boundary data because ...”
- “The expected result should be ...”

For Task 2, organise your test data in this table:

| Test value | Type of test data | Accept or reject? | Expected output |
| ---: | --- | --- | --- |
| 63 | Normal |  |  |
| -1 | Abnormal |  |  |
| 0 | Extreme |  |  |
| -1 and 0 | Boundary |  |  |
| 49 and 50 | Pass threshold |  |  |

## Stretch

A school collects a student ID made of two letters followed by four digits.
The ID is entered twice.

1. Suggest a format check for the ID.
2. Explain how double entry verifies the ID.
3. Explain why both checks may still fail to identify an ID that belongs to
   the wrong student.
4. Propose another check that could improve the process.

## Homework

For a new online account form, give one example each of a validation check and
a verification check. Explain how they differ.
