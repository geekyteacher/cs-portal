---
title: "Lesson 4: Selection & Decision Making"
description: "Use IF...THEN...ELSE statements to make decisions in pseudocode and Python."
order: 4
draft: false
---

> [!NOTE]
>
> Work through the examples and core tasks. Record your answers in **Lesson 4** of your **Teams Portfolio Document**.

## Learning Objectives

- Explain how selection allows programs to make decisions based on conditions.
- Write single-condition selection statements using `IF...THEN...ELSE...ENDIF`.
- Use comparison operators (`=`, `<>`, `<`, `>`, `<=`, `>=`) in CAIE pseudocode and Python.

---

## What is Selection?

**Selection** is a programming construct where the path of execution depends on whether a condition evaluates to `TRUE` or `FALSE`.

In CAIE pseudocode, a two-way selection uses `IF...THEN...ELSE...ENDIF`.
The condition is tested first. If it is true, the statements after `THEN` run;
otherwise, the statements after `ELSE` run.

### Comparison Operators

| Operation | CAIE pseudocode | Python |
| --- | --- | --- |
| Equal to | `=` | `==` |
| Not equal to | `<>` | `!=` |
| Greater than | `>` | `>` |
| Less than | `<` | `<` |
| Greater than or equal to | `>=` | `>=` |
| Less than or equal to | `<=` | `<=` |

### Worked Example: Pass or Fail

```pseudocode
DECLARE Mark : INTEGER
OUTPUT "Enter exam mark:"
INPUT Mark

IF Mark >= 50 THEN
    OUTPUT "Result: Pass"
ELSE
    OUTPUT "Result: Fail"
ENDIF
```

The comparison `Mark >= 50` includes a mark of exactly `50`.

### Boundary Check

Test the condition with `Mark = 49`, `Mark = 50`, and `Mark = 51`:

| Mark | `Mark >= 50` | Output |
| ---: | --- | --- |
| 49 | FALSE | Result: Fail |
| 50 | TRUE | Result: Pass |
| 51 | TRUE | Result: Pass |

The value at the boundary helps check that the comparison operator matches
the rule.

## Guided Practice

An account is in credit when its balance is zero or more. Complete the
algorithm:

```pseudocode
DECLARE Balance : REAL
INPUT Balance

IF Balance _____ 0.0 THEN
    OUTPUT "Account in Credit"
ELSE
    OUTPUT "Overdrawn"
ENDIF
```

Choose the comparison operator that includes a balance of exactly zero.

## Core Practice

Answer in **CAIE pseudocode**.

1. **Fix the syntax:** Identify the missing keywords and rewrite this
   algorithm correctly.

    ```pseudocode
    IF Age > 18
        OUTPUT "Adult"
    ELSE
        OUTPUT "Not an adult"
    END
    ```

2. **Account balance:** Write an algorithm that inputs a balance as a `REAL`.
   Output `"Account in Credit"` if the balance is greater than or equal to
   `0.0`; otherwise, output `"Overdrawn"`.

3. **Trace:** What is output when `Temp` is `28`? Which branch is taken?

    ```pseudocode
    DECLARE Temp : REAL
    INPUT Temp

    IF Temp <= 0 THEN
        OUTPUT "Freezing"
    ELSE
        IF Temp >= 30 THEN
            OUTPUT "Hot"
        ELSE
            OUTPUT "Moderate"
        ENDIF
    ENDIF
    ```

## Explore in Python

After completing the pseudocode, write or run a Python version of the
account-balance task. Test values below, at, and above zero.

## Stretch

Write pseudocode that inputs a whole number and outputs whether it is even or
odd. Use `MOD` to test the remainder after division by `2`.
