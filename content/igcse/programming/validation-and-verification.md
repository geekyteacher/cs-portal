---
title: Validation and Verification
description: Write a data validation routine in CAIE pseudocode, then explore examples in Python.
order: 6
draft: false
---
## Today you will

- explain the difference between validation and verification;
- recognise common validation checks; and
- write and test a validation routine in CAIE pseudocode.

## 1. Validation and verification

**Validation** checks whether data follows rules or is sensible. For example,
a range check can ensure that a mark is between 0 and 100. Passing a
validation check does not prove that the value is correct.

**Verification** checks that data matches its source. For example, someone
could visually compare an entered value with the original, or enter it twice
and compare the two entries. Verification is a process, not a validation
check.

## 2. Read the pseudocode

This algorithm keeps asking for a mark until the value is in the allowed
range:

```pseudocode
DECLARE Mark : INTEGER

REPEAT
    OUTPUT "Enter a mark from 0 to 100"
    INPUT Mark
UNTIL Mark >= 0 AND Mark <= 100

OUTPUT "Mark accepted"
```

The condition after `UNTIL` describes a valid mark. The loop stops when that
condition is `TRUE`. The boundary values `0` and `100` are accepted.

### Trace the algorithm

Suppose the inputs are `-1`, `101`, and then `75`:

1. `-1` is below the range, so the loop repeats.
2. `101` is above the range, so the loop repeats.
3. `75` is in the range, so the loop stops and displays **Mark accepted**.

Trace it again with `0` and `100`. Both are valid boundary values.

## 3. Write your own range check

Write a CAIE pseudocode algorithm that repeatedly asks the user to enter a
menu choice from `1` to `4`. It should accept choices in that range and keep
asking when the choice is outside it.

Your algorithm needs to:

1. declare an integer variable for the choice;
2. ask for and input a choice inside a `REPEAT ... UNTIL` loop;
3. stop when the choice is at least `1` **and** at most `4`; and
4. output a confirmation after a valid choice is entered.

Test your algorithm by tracing these values: `0`, `5`, `1`, and `4`. Which
values should make the loop repeat? Which are valid boundary values?

## 4. Know the validation checks

| Check | What it checks |
| --- | --- |
| Range | A number is between the lower and upper limits, inclusive. |
| Length | Text contains an allowed number of characters. |
| Type | Data is an allowed type, such as an integer or real number. |
| Presence | A value has been entered rather than left blank. |
| Format | Data follows a required pattern, such as `DD/MM/YYYY`. |
| Check digit | A digit is calculated from the other digits to help detect entry errors. |

For each check, ask: **What rule does it enforce? Does passing the check
prove that the data is correct?**

## 5. Compare with Python

The pseudocode routine uses a range check. You can compare it with the
Python examples in the [validation and verification demo](/downloads/validation-and-verification.py).
Download the file and open it in Python. Before running it, predict which
examples will print `True`. Run it, then change the example values at the
bottom of the file and test your predictions.

The Python file includes examples of range, length, type, presence, format,
and check-digit checks. Use it to compare the idea of a validation check in
pseudocode with one way to implement a check in a programming language.

## 6. Consider the limits

These Python examples are deliberately simple. Look at their functions and
discuss what they do **not** guarantee:

- The email check only looks for `@` and `.com`; it does not prove that the
  address exists or is a valid email address.
- The date check checks the `DD/MM/YYYY` pattern, but does not check whether
  the date exists. For example, `31/02/2026` has the right format but is not
  a real date.
- The check-digit function uses one particular set of rules. Other systems
  can use different check-digit algorithms.
- An integer can be a valid whole number but still be outside an allowed
  range.

## Check your understanding

- [ ] I can explain validation and verification and describe the difference.
- [ ] I can identify common types of validation check.
- [ ] I can write a range validation routine using CAIE pseudocode.
- [ ] I can test valid values, invalid values, and boundary values.
