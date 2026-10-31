---
title: "Lesson 8: Tracing and Debugging Algorithms"
description: "Dry-run algorithms, complete trace tables and use test data to find and correct errors."
order: 8
draft: false
---
## Topics in this page

- Trace tables
- Dry-running algorithms
- Error detection and correction
- Choosing useful test data

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Dry-run an algorithm by following each instruction in order.
- Record variable values and outputs accurately in a trace table.
- Use test data to identify a logic or boundary error.
- Suggest and check a correction.

## Quick Check

Try these without running the code:

1. What are the values of `A` and `B` after these instructions?

   ```pseudocode
   A <- 3
   B <- A + 4
   A <- B - 2
   ```

2. Is the condition `Mark >= 50` TRUE or FALSE when `Mark` is `50`?
3. In a trace table, when should you record a new value for a variable?

## Learn

### What is a dry run?

A **dry run** means working through an algorithm by hand, following its
instructions in order and using given test data. It helps you predict what an
algorithm does without running it on a computer.

A **trace table** is a record of the values that change during a dry run. Use
one column for each important variable, and another for output or a condition
when these help explain what happens.

### A reliable tracing method

1. Read the algorithm once to understand its purpose.
2. List the variables that change and add a column for each.
3. Start with the initial values assigned by the algorithm.
4. Follow each instruction in order. Update a variable only when it is
   assigned a new value.
5. For a decision, evaluate the condition using the current values.
6. For a loop, record the values on every repetition, including the final
   check that causes the loop to stop.
7. Record prompts and output when they occur. Add columns for them when they
   are relevant to the algorithm.

Do not skip a repeated value just because it has not changed. If a variable
keeps its value for an iteration, show that unchanged value in the trace.

### Worked example: total the positive inputs

The algorithm inputs four values, adds only positive values to `Total`, then
outputs the result.

Test data, in input order: `3`, `-2`, `5`, `0`.

```pseudocode
DECLARE Num, Counter, Total : INTEGER
Total <- 0

FOR Counter <- 1 TO 4
    OUTPUT "Enter a number:"
    INPUT Num
    IF Num > 0 THEN
        Total <- Total + Num
    ENDIF
NEXT Counter

OUTPUT Total
```

Trace the prompt, input, condition and variable values in order:

| `Counter` | Prompt | Input `Num` | `Num > 0` | `Total` | Output |
| ---: | --- | ---: | --- | ---: | --- |
| - | - | - | - | 0 | - |
| 1 | Enter a number | 3 | TRUE | 3 | - |
| 2 | Enter a number | -2 | FALSE | 3 | - |
| 3 | Enter a number | 5 | TRUE | 8 | - |
| 4 | Enter a number | 0 | FALSE | 8 | - |
| - | - | - | - | 8 | `8` |

After the loop, the algorithm outputs `8`. Notice that `Total` does not
change when the condition is false.

### Finding errors with tests

An algorithm can be written in valid pseudocode and still produce the wrong
result. To find this kind of **logic error**, choose test data whose expected
result is clear, dry-run the algorithm, and compare the result with what
should happen.

Test more than one situation. For a condition that accepts marks of `50` or
more, useful tests include:

- A value below the boundary, such as `49`.
- The boundary value, `50`.
- A value above the boundary, such as `51`.

The boundary test can reveal whether the algorithm uses `>= 50` or the
incorrect `> 50`.

### Choosing test data

When checking an algorithm, choose test data that checks both expected use
and important edge cases. For an algorithm that accepts an integer mark from
`0` to `100`, inclusive:

| Test-data type | Example | Expected result |
| --- | ---: | --- |
| Normal | `63` | Accepted |
| Abnormal | `-1` or `101` | Rejected |
| Extreme | `0` or `100` | Accepted; these are the smallest and largest acceptable values. |
| Boundary | `-1`, `0`, `100`, and `101` | Check the extreme acceptable values and the nearest rejected values. |

Use the expected result to decide whether the algorithm is correct. Test data
should be selected for the requirements of the particular problem.

## Teacher Demonstration

Model the worked example using a board or projected trace table:

1. Point out the initial value `Total <- 0` before processing any input.
2. Take the test data one value at a time: `3`, `-2`, `5`, `0`.
3. Ask the class to evaluate `Num > 0` before deciding whether `Total` changes.
4. Record each prompt, input, value of `Counter`, condition result and value
   of `Total` for every iteration.
5. Add the final output to the trace after the loop. Ask students to predict
   it before revealing the result.
6. Show the incorrect condition `IF Num >= 0 THEN` and ask which test input
   exposes the error and why.

## Guided Practice

Dry-run this algorithm. The test data is `42`, `75`, `50`, `31`, in that
order.

```pseudocode
DECLARE Mark, Counter, PassCount : INTEGER
PassCount <- 0

FOR Counter <- 1 TO 4
    OUTPUT "Enter a mark:"
    INPUT Mark
    IF Mark >= 50 THEN
        PassCount <- PassCount + 1
    ENDIF
NEXT Counter

OUTPUT PassCount
```

Complete the table. Write `PassCount` on every row, even when it does not
change.

| `Counter` | Prompt | Input `Mark` | `Mark >= 50` | `PassCount` | Output |
| ---: | --- | ---: | --- | ---: | --- |
| - | - | - | - | 0 | - |
| 1 | Enter a mark | 42 |  |  | - |
| 2 | Enter a mark | 75 |  |  | - |
| 3 | Enter a mark | 50 |  |  | - |
| 4 | Enter a mark | 31 |  |  | - |
| - | - | - | - | 2 | `2` |

What value is output? Which input checks the exact boundary?

## Core Practice

Complete both tasks. Show your working in a trace table.

### Task 1: Trace a running total

Dry-run the worked example again with the test data `4`, `6`, `-1`, `8`.
Record the final value of `Total` and the value output by the algorithm.

### Task 2: Find and correct the error

This algorithm should output the largest of three input values, but it does
not work correctly for every set of inputs.

```pseudocode
DECLARE First, Second, Third, Largest : INTEGER
INPUT First, Second, Third

Largest <- First

IF Second > Largest THEN
    Largest <- Second
ENDIF

IF Third > Second THEN
    Largest <- Third
ENDIF

OUTPUT Largest
```

1. Dry-run it using `First = 9`, `Second = 4`, and `Third = 7`.
2. What does the algorithm output? What should it output?
3. Identify the condition that causes the problem and write a correction.
4. Choose another set of test data to check your correction.

## Support

Use the steps below if you get stuck:

1. Write the initial value of `Total` or `PassCount` before the first loop.
2. Copy the next input value into the correct row.
3. Work out the condition using that input.
4. If the condition is TRUE, calculate the new variable value.
5. If it is FALSE, carry the previous value forward.

For Task 2, start your trace like this:

| `First` | `Second` | `Third` | `Largest` | `Second > Largest` | `Third > Second` | Output |
| ---: | ---: | ---: | ---: | --- | --- | ---: |
| 9 | 4 | 7 | 9 |  |  |  |

To find a logic error, test a case where the largest value is not in the same
position as the values you used in your first test.

## Stretch

Design test cases for an algorithm that accepts a mark from `0` to `100`,
inclusive, and outputs `"Pass"` for an accepted mark of `50` or more,
otherwise `"Not yet"`. It should reject marks outside the accepted range.

Include one example of each type:

- Normal data.
- Abnormal data.
- Extreme data.
- Boundary data.

For each test, state whether the input should be accepted and the expected
output. Include the input-range boundary values and the pass-mark boundary
values `49` and `50`. Explain which incorrect comparison operator would be
exposed by testing the pass-mark boundary.

## Portfolio Evidence (Existing Teams Document)

In the existing **Year 11 Algorithm Design Portfolio**, complete the work
under Lessons 10–12. For this combined page, include:

- One completed trace table for an algorithm with a loop and a decision.
- One logic error, test data that reveals it, and a corrected condition.
- Test cases labelled normal, abnormal, extreme and boundary, with expected
  outcomes.

Keep using the existing portfolio and Teams assignment. You do not need to
create a separate submission for this page. The teacher will announce when
the portfolio checkpoint is due.

## Homework

Complete any unfinished core task. Then answer:

1. What information should a trace table record?
2. Why should a trace table include the value of a variable when it has not
   changed?
3. Why is it useful to test a value at the boundary of a condition?
