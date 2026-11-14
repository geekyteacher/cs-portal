---
title: "Lesson 8: Tracing and Debugging Algorithms"
description: "Dry-run algorithms, complete trace tables and use test data to find and correct logic errors."
order: 8
draft: false
---

## Learning Objectives

- Dry-run an algorithm step-by-step and record every variable change in a trace table.
- Distinguish between normal, abnormal, extreme, and boundary test data.
- Identify and correct off-by-one and logic errors using boundary test values.

---

## 1. Starter (5 mins — Do this first)

A theme park ride requires riders to be **at least 120 cm** tall and **no taller than 200 cm**.

1. Give **one** height that is **extreme** valid data.
2. Give **one** height that is **abnormal** data.
3. A programmer writes:

```pseudocode
IF Height > 120 AND Height <= 200 THEN
```

Which exact height will fail because of their mistake?

---

## 2. Learn: Dry-Running & Test Data

### Rules for CAIE Trace Tables

In Paper 2, trace tables are marked strictly. Follow these rules:

1. **Work left-to-right, top-to-bottom.** Move down to a new row whenever a loop repeats or a variable is overwritten.
2. **Record initial values first.** Put variables set before a loop (e.g. `Total <- 0`) on the first row.
3. **Only write values when they change** (unless a question specifically asks you to repeat every row).
4. **Record exact outputs.** Put values in the `Output` column at the exact moment `OUTPUT` executes.

### Choosing Test Data

To prove an algorithm works, test both typical inputs and the edges of every condition.

| Test Type | Definition | Example (Rule: `0` to `100` inclusive) |
|------------|------------|-----------------------------------------|
| **Normal** | Typical data the program expects to accept. | `45` |
| **Abnormal** | Invalid data (wrong range or wrong type) that must be rejected. | `-5`, `105`, `"abc"` |
| **Extreme** | The smallest or largest acceptable valid values. | `0` and `100` |
| **Boundary** | An extreme valid value paired with its nearest rejected neighbour. | `-1` and `0` (lower boundary); `100` and `101` (upper boundary) |

> [!NOTE]
> **Decision Boundaries vs Range Boundaries**
>
> If valid marks are `0–100` and a pass is `50+`, there are **two** sets of boundaries to test:
>
> - Valid input edges: `-1`, `0`, `100`, `101`
> - Pass/fail decision edge: `49`, `50`

---

## 3. Guided Practice (We do this together)

Dry-run this algorithm using the test data:

```text
12, 5, 18, 5, 20
```

```pseudocode
DECLARE Num, Count, Special : INTEGER

Special <- 0

FOR Count <- 1 TO 5
    INPUT Num

    IF Num > 10 THEN
        Special <- Special + 1
    ELSE
        Special <- Special - 1
    ENDIF

NEXT Count

OUTPUT Special
```

| Count | Num | Num > 10 | Special | Output |
|---------|---------|------------|---------|---------|
| — | — | — | 0 | — |
| 1 | 12 | TRUE | 1 | — |
| 2 | 5 | FALSE | 0 | — |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| Final | | | | |

1. Complete rows 3, 4, 5, and the final output row.
2. What would the final output be if the condition was changed to:

```pseudocode
IF Num >= 5 THEN
```

---

## 4. Core Practice (Paper / Exam Style)

Complete these tasks on paper.

Show all working clearly.

### Task 1: Trace a `WHILE` Loop with Two Variables

Dry-run the algorithm below using the input sequence:

```text
4, 7, 2, 9, 0
```

```pseudocode
DECLARE X, Y, Result : INTEGER

X <- 1
Result <- 0

INPUT Y

WHILE Y <> 0 DO
    IF Y > X THEN
        Result <- Result + Y
        X <- Y
    ENDIF

    INPUT Y
ENDWHILE

OUTPUT X, Result
```

Draw and complete a trace table with the columns:

```text
X | Y | Y <> 0 | Y > X | Result | Output
```

---

### Task 2: Debug a Broken Exam Algorithm

A program must input **5 temperatures** and output the **lowest** temperature recorded.

Temperatures can be negative (e.g. `-12`).

The student's code below fails on certain inputs.

```pseudocode
DECLARE Temp, Lowest, Counter : INTEGER

Lowest <- 0

FOR Counter <- 1 TO 5
    INPUT Temp

    IF Temp > Lowest THEN
        Lowest <- Temp
    ENDIF

NEXT Counter

OUTPUT Lowest
```

1. Dry-run this broken code using:

   ```text
   -4, -8, -2, -10, -5
   ```

   What does it wrongly output?

2. Explain the **two** logic errors in the code.
   - Look at how `Lowest` is initialised.
   - Look at the `IF` comparison.

3. Write the corrected algorithm.

---

### Task 3: Test Data Table

A school bus booking system accepts a student's Year Group from **Year 7 to Year 11 inclusive**.

Complete the table below.

| Test Type | Test Value | Expected Result (Accept / Reject) | Reason |
|------------|------------|------------------------------------|---------|
| Normal | | | |
| Abnormal (too low) | | | |
| Abnormal (wrong type) | | | |
| Extreme (upper) | | | |
| Boundary pair (lower) | | | |

---

## 5. Support & Scaffolds

> [!TIP]
> **Stuck on Task 1's Trace Table?**
>
> Start with these first two rows:

| X | Y | Y <> 0 | Y > X | Result | Output |
|----|----|---------|---------|---------|---------|
| 1 | 4 | TRUE | TRUE | 4 | — |
| 4 | 7 | TRUE | TRUE | 11 | — |

Notice how `INPUT Y` happens **at the bottom** of the `WHILE` loop.

---

## 6. Stretch (Finished Early?)

Look at Task 2 again.

Why is setting:

```pseudocode
Lowest <- 999
```

a risky fix, even if it works for weather temperatures?

Explain how a programmer should properly initialise `Lowest` when inputting 5 numbers **without assuming a maximum possible value**.