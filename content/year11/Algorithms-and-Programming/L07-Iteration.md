---
title: "Lesson 7: Iteration"
description: "Choose, trace and write count-controlled and condition-controlled loops in CAIE pseudocode."
order: 7
draft: false
---
## Topics in this page

- Count-controlled iteration
- Condition-controlled iteration
- Loop tracing and practice

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Explain why iteration is used in an algorithm.
- Choose between a count-controlled loop and a condition-controlled loop.
- Trace a loop and predict its output.
- Write loops that update their variables and terminate correctly.

## Quick Check

Try these without running the code:

1. What is the value of `Total` after these instructions?

   ```pseudocode
   DECLARE Total : INTEGER
   Total <- 0
   Total <- Total + 6
   Total <- Total + 4
   ```

2. How many times does this loop output a number? Which numbers?

   ```pseudocode
    DECLARE Counter : INTEGER
    FOR Counter <- 1 TO 4
        OUTPUT Counter
    NEXT Counter
   ```

3. What must eventually happen for a `WHILE` loop to stop?

## Learn

### What is iteration?

**Iteration** means repeating one or more instructions. A loop can make an
algorithm shorter and easier to update than writing the same instructions
many times.

Choose a **count-controlled loop** when the number of repetitions is known.
Choose a **condition-controlled loop** when repetition should continue until
a condition changes or becomes true.

### Count-controlled iteration: `FOR`

A `FOR` loop repeats for a specified range of values. In CAIE pseudocode, the
loop counter takes each value from the start value to the end value,
including the end value.

```pseudocode
DECLARE Counter : INTEGER

FOR Counter <- 1 TO 5
    OUTPUT Counter
NEXT Counter
```

This outputs `1`, `2`, `3`, `4`, and `5`. The loop ends after the final value.

The loop counter changes automatically. Do not assign a new value to the
counter inside the loop unless the task specifically requires it.

The start and end values are included. If the start and end values are equal,
the loop runs once; if the start value is greater than the end value, it does
not run. Use `STEP` to change the increment:

```pseudocode
FOR Counter <- 2 TO 10 STEP 2
    OUTPUT Counter
NEXT Counter
```

This outputs the even numbers from `2` to `10`. The `STEP` value must be an
integer. A negative step can count down.

### Pre-condition loop: `WHILE`

A `WHILE` loop checks its condition before each repetition. It continues while
the condition is `TRUE`. The statements inside the loop must make progress
towards the condition becoming `FALSE`, or the loop may never stop.

```pseudocode
DECLARE Number : INTEGER
Number <- 1

WHILE Number <= 4 DO
    OUTPUT Number
    Number <- Number + 1
ENDWHILE
```

The values output are `1`, `2`, `3`, and `4`. After `Number` becomes `5`, the
condition is false and the loop ends.

### Post-condition loop: `REPEAT ... UNTIL`

A `REPEAT ... UNTIL` loop checks its condition after the loop statements have
run. Therefore, its instructions run at least once.

```pseudocode
DECLARE Number : INTEGER
Number <- 1

REPEAT
    OUTPUT Number
    Number <- Number + 1
UNTIL Number > 4
```

This also outputs `1`, `2`, `3`, and `4`. Notice that the loop stops when the
`UNTIL` condition becomes `TRUE`.

| Loop | When is the condition checked? | Useful when... |
| --- | --- | --- |
| `FOR` | The number of repetitions is managed by the loop counter. | You know how many times to repeat. |
| `WHILE` (pre-condition) | Before each repetition. | The loop may run zero or more times, depending on a condition. |
| `REPEAT ... UNTIL` (post-condition) | After each repetition. | The loop must run at least once. |

### A common loop error

Check that a condition-controlled loop changes something used in its
condition:

```pseudocode
Number <- 1
WHILE Number <= 4 DO
    OUTPUT Number
    Number <- Number + 1
ENDWHILE
```

If `Number <- Number + 1` is missing, `Number` stays at `1`. The condition
stays true, so the loop does not terminate.

## Teacher Demonstration

Before each run, ask students to predict the output and explain the loop's
stopping point.

1. Trace the `FOR` example. Write down each value of `Counter` and check that
   the final value, `5`, is included.
2. Trace the `WHILE` example using a table with columns `Number`, condition
   result, and output. Identify the point where the condition becomes false.
3. Compare it with the `REPEAT ... UNTIL` example. Ask why its condition is
   written as the point to stop, and why its body runs at least once.
4. Remove the update from the `WHILE` example. Ask students to predict what
   happens; restore the update before running to avoid an endless program.

## Guided Practice

Complete the trace table for this algorithm:

```pseudocode
DECLARE Counter : INTEGER
Counter <- 2

WHILE Counter < 8 DO
    OUTPUT Counter
    Counter <- Counter + 2
ENDWHILE
```

| Counter | `Counter < 8` | Output |
| ---: | --- | --- |
| 2 | TRUE | 2 |
| 4 |  |  |
| 6 |  |  |
| 8 |  |  |

Then explain why `8` is not output.

## Core Practice

Complete both tasks. Use CAIE pseudocode and test your work by tracing it.

### Task 1: Count-controlled loop

Write an algorithm that outputs the five times table from `5` to `50`, one
multiple per line. Use a `FOR` loop and a loop counter from `1` to `10`.

### Task 2: Condition-controlled loop

Write an algorithm that repeatedly inputs a number until the user enters `0`.
After the loop, output `"Input complete"`.

Choose either `WHILE` or `REPEAT ... UNTIL`. Make sure the input is updated on
every repetition and that the algorithm handles `0` as the stopping value.

## Support

Use the scaffolds if you need a starting point.

### Task 1 scaffold

```pseudocode
DECLARE Counter : INTEGER

FOR Counter <- 1 TO _____
    OUTPUT Counter * _____
NEXT Counter
```

### Task 2 scaffold using `REPEAT ... UNTIL`

```pseudocode
DECLARE Number : INTEGER

REPEAT
    OUTPUT "Enter a number (0 to stop):"
    INPUT Number
UNTIL Number _____ 0

OUTPUT "Input complete"
```

Check your work:

- Does the loop body run the expected number of times?
- Does the loop condition eventually stop the loop?
- Is the stopping value handled correctly?

## Stretch

Write an algorithm that inputs exactly 5 test scores, adds them to `Total`,
and outputs the total. Use a `FOR` loop and initialise `Total` before the
loop.

Then adapt the algorithm so it keeps inputting scores until a sentinel value
of `-1` is entered. The sentinel should stop the loop but must **not** be
included in the total.

Explain which loop you chose for each version and why.

## Portfolio Evidence (Existing Teams Document)

In the existing **Year 11 Algorithm Design Portfolio**, complete the
iteration work under Lessons 7–9. For this combined page, make sure your
portfolio includes:

- One count-controlled loop and its trace or test evidence.
- One condition-controlled loop and an explanation of how it terminates.

Keep using the existing portfolio and Teams assignment. You do not need to
create a separate submission for this page. The teacher will announce when
the portfolio checkpoint is due.

## Homework

Finish any core task you did not complete in class. Then answer:

1. Give one situation where a `FOR` loop is suitable.
2. Give one situation where a condition-controlled loop is suitable.
3. Explain one way to prevent an unintended infinite loop.
