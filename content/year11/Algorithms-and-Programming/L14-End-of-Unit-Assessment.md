---
title: "Lesson 14: End-of-Unit Assessment"
description: "Demonstrate algorithm design, tracing, standard-method and data-quality skills in a mixed assessment."
order: 14
draft: false
---
## Assessment Coverage

This assessment samples the algorithm and programming work in this unit:

- Sequence, variables, data types, input and output
- Selection, Boolean logic and iteration
- Trace tables, dry-running, test data and error correction
- One-dimensional and two-dimensional arrays
- Totalling, counting, minimum, maximum and average
- Linear search and bubble sort
- Procedures, functions and parameters
- Validation, verification, design and decomposition
- File handling

## Assessment Conditions

- Complete the assessment independently unless your teacher gives different instructions.
- Use the pseudocode conventions in the syllabus.
- Show trace-table working and state expected outcomes for test data.
- Your teacher will tell you which sections to complete, how much time is
  available and which resources are permitted.

## Section A: Trace and Debug

The test data for `Value` is `6`, `3`, `8`, `2`.

```pseudocode
DECLARE Value, Counter, Total : INTEGER
Total <- 0

FOR Counter <- 1 TO 4
    INPUT Value
    IF Value > 4 THEN
        Total <- Total + Value
    ENDIF
NEXT Counter

OUTPUT Total
```

1. Complete a trace table showing `Counter`, `Value`, the result of
   `Value > 4`, `Total` and the final output.
2. The condition is changed to `Value >= 4`. Which input values change the
   behaviour? What is the new output?

## Section B: Standard Methods

An array contains the values `[14, 5, 9, 5, 12]`, stored at indexes `1` to `5`.

1. State the minimum and maximum values.
2. Calculate the average.
3. Write pseudocode to count how many values equal `5`.
4. Trace a linear search for `9`, recording the index and value checked.
5. Complete the first pass of bubble sort into ascending order.

## Section C: Validation and Verification

A system accepts an integer quantity from `1` to `20`, inclusive.

1. Give one normal, one abnormal, one extreme and one boundary test value.
2. State the expected acceptance or rejection for each.
3. Name one suitable validation check.
4. Describe one verification check and explain what it can detect.

## Section D: Algorithm Design

A sports club stores the names and scores of five players. Design an
algorithm that:

- Inputs each player's name and score.
- Stores the names and scores in suitable arrays.
- Counts how many scores are at least `10`.
- Finds and outputs the highest score and its player's name.
- Outputs the average score.

Use a suitable loop and selection. Declare variables and arrays, initialise
accumulators correctly, and use meaningful identifiers.

## Section E: Subprograms and Files

1. State one difference between a procedure and a function.
2. Write a function with two integer parameters that returns their sum.
3. Write pseudocode to open a text file for reading, read one line into a
   string variable, and close the file.

## Reflection and Next Steps

After the assessment, identify:

1. One topic you can now do confidently.
2. One error or misconception you need to address.
3. One specific question or practice task that would help you improve.

## Follow-up

Your teacher will explain how to review corrections and what evidence to
keep. Do not create a new Teams assignment unless instructed.
