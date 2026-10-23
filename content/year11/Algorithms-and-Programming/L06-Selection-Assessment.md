---
title: "Lesson 6: Selection Assessment & Application"
description: "Apply sequence and selection to solve exam-style scenario problems."
order: 6
draft: false
---

> [!NOTE]
>
> Complete this assessment independently. Record your solutions in **Lesson 6** of your **Teams Portfolio Document**.

## Learning Objectives

- Combine sequence, variables, and complex selection in a complete algorithm.
- Trace decision algorithms containing multiple logical branches.
- Write exam-ready pseudocode with clear declarations and appropriate logic.

---

## 1. Exam Context & Guidance

Scenario questions reward precise syntax, logical structure, clear variable declarations, and careful handling of boundary conditions.

> [!TIP]
>
> Check boundary conditions. For example, if a condition uses `>= 18`, test what happens when the value is exactly `18`.

## 2. Assessment Scenario Tasks

### Task 1: Cinema Ticket Pricing System

A local cinema calculates ticket prices based on customer age and whether it is a discount day:

- Standard ticket: **$12.00**
- Children under 12: **$7.00**
- Seniors aged 65 and over: **$8.00**
- Wednesday discount: all tickets receive a **$2.00 discount**.

Write pseudocode for an algorithm that:

1. Prompts for and inputs the customer's `Age` (`INTEGER`) and `IsWednesday` (`BOOLEAN`).
2. Calculates the final ticket price.
3. Outputs the ticket price in a clear message.

### Task 2: Exam Trace Table

Trace the algorithm for each independent run using the test data below:

- Run 1: `Weight = 15`, `IsExpress = TRUE`
- Run 2: `Weight = 4`, `IsExpress = FALSE`

```pseudocode
DECLARE Weight : REAL
DECLARE IsExpress : BOOLEAN
DECLARE Cost : REAL

INPUT Weight, IsExpress

IF Weight > 10 THEN
    Cost <- 20.0
ELSE
    Cost <- 10.0
ENDIF

IF IsExpress = TRUE THEN
    Cost <- Cost + 5.0
ENDIF

OUTPUT Cost
```

| Run | `Weight` | `IsExpress` | `Cost` | `OUTPUT` |
| --- | --- | --- | --- | --- |
| **1** |  |  |  |  |
| **2** |  |  |  |  |

> [!CHALLENGE]
>
> **Task 3 (Extension): Validation Add-On**
>
> Modify your cinema ticket algorithm to check that `Age` is between `1` and `120`, inclusive. If the age is invalid, output an error message instead of calculating a price.
