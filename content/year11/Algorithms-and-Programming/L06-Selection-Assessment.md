---
title: "Lesson 6: Selection Checkpoint"
description: "Check your understanding of selection with a short trace and algorithm-design checkpoint."
order: 6
draft: false
---
> [!NOTE]
>
> Complete this short checkpoint independently. Use CAIE pseudocode and show your working.

## What this checks

- Tracing nested selection and compound conditions.
- Writing a clear selection algorithm from a short specification.
- Checking decision boundaries.

## Before you start

> [!TIP]
>
> Read each condition carefully. Check boundary values and make sure every `IF` has a matching `ENDIF`.

## Checkpoint Task 1: Trace the algorithm

Complete the table for each independent run. The table is started for you:
record the result of each condition and the output. The inner condition is
only checked when `Mark >= 50` is `TRUE`.

```pseudocode
DECLARE Mark : INTEGER
DECLARE HasSubmitted : BOOLEAN

INPUT Mark, HasSubmitted

IF Mark >= 50 THEN
    IF HasSubmitted = TRUE THEN
        OUTPUT "Pass"
    ELSE
        OUTPUT "Submission missing"
    ENDIF
ELSE
    OUTPUT "Resit"
ENDIF
```

| Run | `Mark` | `HasSubmitted` | `Mark >= 50` | `HasSubmitted = TRUE` (if checked) | Output |
| --- | ---: | --- | --- | --- | --- |
| 1 | 50 | TRUE |  |  |  |
| 2 | 72 | FALSE |  |  |  |
| 3 | 49 | TRUE |  | Not checked |  |

In an exam, you may be given a trace-table layout. Practise identifying the
variables, conditions and outputs that need columns, even when the table is
not provided.

## Checkpoint Task 2: Design an algorithm

Write CAIE pseudocode that inputs an integer `Age` and outputs:

- `"Invalid age"` when `Age < 0` or `Age > 120`
- `"Child"` when the age is valid and `Age < 16`
- `"Adult"` when the age is valid and `Age >= 16`

Check the invalid-age condition before deciding whether the person is a child
or an adult. Test your algorithm with `-1`, `0`, `15`, `16`, `120` and `121`.
State the expected output for each test.

Copy and complete this trace table for the six required test values. Add rows
if you test any additional ages. If the age is invalid, write `Not checked`
for the category condition.

| `Age` | `Age < 0 OR Age > 120` | `Age < 16` (if valid) | Output |
| ---: | --- | --- | --- |
| -1 |  |  |  |
| 0 |  |  |  |
| 15 |  |  |  |
| 16 |  |  |  |
| 120 |  |  |  |
| 121 |  |  |  |

## Success Check

Before handing in your work, check that:

- Your trace follows the outer and inner conditions in order.
- Your algorithm checks invalid values before assigning a category.
- Your boundaries match the specification exactly.
- Your pseudocode uses clear variable names and correct selection syntax.

## Stretch

Add a message for a child who has permission to attend an event. Use a
compound condition and test both permission values at the age boundary.

## Further Challenge

These are optional extension tasks for students who finish the checkpoint.

### Challenge 1: Ticket pricing

A venue charges:

- Under 12: `$5`
- Age 12 to 17 inclusive: `$8`
- Age 18 to 64 inclusive: `$12`
- Age 65 or over: `$7`

Write pseudocode that inputs an age and outputs the correct price. Reject
invalid ages below `0` or above `120` before calculating the price. Test all
the category boundaries and explain why the order of your conditions matters.

### Challenge 2: Access rules

An online resource grants access if the user is at least 16 and has an
account, or if the user is a teacher. Write the condition using Boolean
variables, `AND`, `OR` and brackets.

1. Write a complete pseudocode algorithm that inputs the three Boolean or
   integer values and outputs `"Access granted"` or `"Access denied"`.
2. Make a truth table or test table covering cases where each route to access
   succeeds and fails.
3. Explain what could go wrong if the brackets around the `AND` condition
   were omitted or placed differently.

## Portfolio Evidence

Record your answers in **Lesson 6: Selection Assessment** in the existing
Teams portfolio.
