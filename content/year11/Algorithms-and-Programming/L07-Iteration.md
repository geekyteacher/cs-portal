---
title: "Lesson 7: Iteration"
description: "Choose, trace and write count-controlled and condition-controlled loops in CAIE pseudocode."
order: 7
draft: false
---

## Learning Objectives

- Choose between count-controlled (`FOR`) and condition-controlled (`WHILE`, `REPEAT ... UNTIL`) loops.
- Trace loops accurately, identifying exact stopping conditions.
- Write loops in CAIE pseudocode that update variables and terminate cleanly.

---

## 1. Starter (5 mins — Do this first)

Look at the two algorithms below. Without running them, answer the questions in your book.

### Algorithm A

```pseudocode
DECLARE Total, Count : INTEGER
Total <- 10

FOR Count <- 1 TO 3
    Total <- Total - 2
NEXT Count

OUTPUT Total
```

### Algorithm B

```pseudocode
DECLARE Number : INTEGER
Number <- 5

WHILE Number > 0 DO
    OUTPUT Number
ENDWHILE
```

1. What is the final value output by **Algorithm A**?
2. Why will **Algorithm B** never stop running?
3. What single line would fix **Algorithm B**?

---

## 2. Learn: The Three CAIE Loops

**Iteration** repeats a block of instructions. Choosing the right loop depends on whether you know how many repetitions are needed before the loop starts.

| Loop Type | Syntax | When condition is checked | Best used when... |
|------------|----------|--------------------------|-------------------|
| Count-controlled | `FOR ... TO ... NEXT` | Managed automatically by counter | You know the exact number of repetitions before the loop starts. |
| Pre-condition | `WHILE ... DO ... ENDWHILE` | **Before** each repetition | The loop might need to run **zero** times (e.g. checking valid input first). |
| Post-condition | `REPEAT ... UNTIL` | **After** each repetition | The loop must run **at least once** (e.g. a menu or password prompt). |

### Key Rules for CAIE Pseudocode

1. **`FOR` loops include the end value.**  
   `FOR X <- 1 TO 5` runs 5 times (`1, 2, 3, 4, 5`).

   Use `STEP` to count in jumps or backwards:

   ```pseudocode
   FOR X <- 10 TO 2 STEP -2
   ```

   Never manually change the counter inside a `FOR` loop.

2. **`WHILE` vs `REPEAT` logic is opposite.**

   - `WHILE` continues while the condition is **TRUE** (stops when FALSE).
   - `REPEAT ... UNTIL` continues while the condition is **FALSE** (stops when TRUE).

> [!WARNING]
> **The Infinite Loop Trap**
>
> In `WHILE` and `REPEAT` loops, the variable tested in the condition **must** be updated inside the loop body, or the loop will run forever.

---

## 3. Guided Practice (We do this together)

Trace the algorithm below on paper.

Remember: `REPEAT ... UNTIL` checks its condition at the **bottom** of the loop.

```pseudocode
DECLARE Value, Steps : INTEGER

Value <- 20
Steps <- 0

REPEAT
    Value <- Value - 6
    Steps <- Steps + 1
UNTIL Value < 5

OUTPUT Steps, Value
```

| Steps | Value | Value < 5 (Stop?) |
|---------|---------|------------------|
| 0 | 20 | — |
| 1 | 14 | FALSE |

1. Complete the remaining rows of the trace table.
2. What are the two numbers output at the end?
3. If `Value` started at `3` instead of `20`, how many times would this loop run? Why?

---

## 4. Core Practice (Paper / Exam Style)

Complete these tasks in your book or on your worksheet.

**Do not copy the examples. Read the rules carefully.**

### Task 1: Countdown with `FOR`

Write an algorithm using a `FOR` loop that outputs all multiples of 3 from `30` down to `3` (`30, 27, 24 ... 3`).

After the loop finishes, output:

```text
Lift off!
```

### Task 2: Password Lockout (`REPEAT ... UNTIL`)

A security system asks a user to enter a four-digit PIN.

The correct PIN is:

```text
4821
```

Write an algorithm that:

1. Repeatedly asks the user to input a PIN until they enter `4821` **OR** they have made `3` failed attempts.
2. Outputs `"Access Granted"` if they entered the correct PIN.
3. Outputs `"Account Locked"` if all 3 attempts are used.

> **Hint:** You will need a counter variable to track attempts, and `AND` or `OR` in your `UNTIL` condition.

### Task 3: Spot and Fix the Bug

The algorithm below is meant to input numbers until the user types `-1` and output the sum of all numbers entered (**not** including `-1`).

However, it contains **two logic errors**.

```pseudocode
DECLARE Num, Total : INTEGER

Total <- 0

REPEAT
    INPUT Num
    Total <- Total + Num
UNTIL Num = 0

OUTPUT Total
```

1. Identify the two errors.
2. Rewrite the corrected algorithm in CAIE pseudocode.

---

## 5. Support & Scaffolds

> [!TIP]
> **Need a starting point for Task 2?**
>
> Use this structure and fill in the missing logic:

```pseudocode
DECLARE Pin, Attempts : INTEGER

Attempts <- 0

REPEAT
    OUTPUT "Enter PIN:"
    INPUT Pin
    Attempts <- Attempts + 1
UNTIL Pin = _____ OR Attempts = _____

IF Pin = 4821 THEN
    OUTPUT "Access Granted"
ELSE
    // What goes here?
ENDIF
```

---

## 6. Stretch (Finished Early?)

Write an algorithm using a `WHILE` loop that:

1. Inputs a positive integer `N`.
2. Calculates the **factorial** of `N`.
3. Outputs the result.

Example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Ensure your algorithm still outputs `1` if the user enters:

```text
0
```