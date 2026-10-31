---
title: "Lesson 9: Arrays, Traversal and Accumulation"
description: "Declare and traverse one-dimensional and two-dimensional arrays, then use totalling and counting algorithms."
order: 9
draft: false
---
## Topics in this page

- One-dimensional and two-dimensional arrays
- Reading and writing array values using iteration
- Totalling
- Counting
- Nested iteration

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Explain why an array is useful for storing related values.
- Declare and access one-dimensional and two-dimensional arrays.
- Read from and write to array elements using loops and index variables.
- Use an accumulator to total values and a counter to count items meeting a condition.

## Quick Check

1. What values does `Index` take in this loop?

   ```pseudocode
   FOR Index <- 1 TO 4
       OUTPUT Index
   NEXT Index
   ```

2. Why should `Total` be set to `0` before adding values to it?
3. What is the difference between updating a total and updating a count?

## Learn

### What is an array?

An **array** stores a group of related values under one identifier. Each
element is accessed using an index. The index can start at `0` or `1`;
always use the index range given in the question or declaration.

```pseudocode
DECLARE Scores : ARRAY[1:5] OF INTEGER
```

This declares five integer elements, `Scores[1]` to `Scores[5]`.

Assign or input values into individual elements:

```pseudocode
Scores[1] <- 72
Scores[2] <- 65
INPUT Scores[3]
```

Use an index variable to work through the array:

```pseudocode
DECLARE Index : INTEGER

FOR Index <- 1 TO 5
    OUTPUT Scores[Index]
NEXT Index
```

### Two-dimensional arrays

A two-dimensional array stores values in rows and columns. It needs two
indexes, commonly a row and a column:

```pseudocode
DECLARE Seats : ARRAY[1:3, 1:4] OF BOOLEAN
Seats[2, 3] <- TRUE
```

The value at row 2, column 3 is accessed as `Seats[2, 3]`. A nested loop can
visit every element:

```pseudocode
DECLARE Row, Column : INTEGER

FOR Row <- 1 TO 3
    FOR Column <- 1 TO 4
        OUTPUT Seats[Row, Column]
    NEXT Column
NEXT Row
```

The inner loop processes every column for the current row. The outer loop
then moves to the next row.

### Totalling and counting

A **total** is an accumulator: initialise it before the loop and add each
relevant value to it.

```pseudocode
DECLARE Scores : ARRAY[1:4] OF INTEGER
DECLARE Index, Total : INTEGER

Total <- 0
FOR Index <- 1 TO 4
    INPUT Scores[Index]
    Total <- Total + Scores[Index]
NEXT Index

OUTPUT Total
```

A **count** records how many values meet a condition. Initialise it to `0`
and increase it by `1` when the condition is true:

```pseudocode
DECLARE Index, PassCount : INTEGER
PassCount <- 0

FOR Index <- 1 TO 4
    IF Scores[Index] >= 50 THEN
        PassCount <- PassCount + 1
    ENDIF
NEXT Index

OUTPUT PassCount
```

Do not confuse the value being counted with the counter. `PassCount` increases
by one for each qualifying score; it does not increase by the score itself.

## Guided Practice

The values in `Scores` are `12`, `7`, `15`, and `6`. Trace the total and the
count of values greater than `10`.

```pseudocode
DECLARE Scores : ARRAY[1:4] OF INTEGER
DECLARE Index, Total, Count : INTEGER

Scores[1] <- 12
Scores[2] <- 7
Scores[3] <- 15
Scores[4] <- 6
Total <- 0
Count <- 0

FOR Index <- 1 TO 4
    Total <- Total + Scores[Index]
    IF Scores[Index] > 10 THEN
        Count <- Count + 1
    ENDIF
NEXT Index
```

| `Index` | `Scores[Index]` | `Total` | `Scores[Index] > 10` | `Count` |
| ---: | ---: | ---: | --- | ---: |
| - | - | 0 | - | 0 |
| 1 | 12 |  |  |  |
| 2 | 7 |  |  |  |
| 3 | 15 |  |  |  |
| 4 | 6 |  |  |  |

## Core Practice

Complete both tasks using CAIE pseudocode.

### Task 1: Record and total scores

Declare an integer array to store six scores. Use a loop to input all six
values and calculate their total. Output the total after the loop.

### Task 2: Count temperatures

An array stores the temperatures for seven days. Write an algorithm that
traverses the array and counts how many temperatures are below `10`. Output
the count.

## Support

Use the scaffold for Task 2:

```pseudocode
DECLARE Index, ColdDays : INTEGER
ColdDays <- _____

FOR Index <- _____ TO _____
    IF Temperature[Index] _____ 10 THEN
        ColdDays <- ColdDays + _____
    ENDIF
NEXT Index

OUTPUT ColdDays
```

Check that:

- The array has one element for each day.
- The loop visits every valid index exactly once.
- The count is initialised before the loop.
- The count increases only when the condition is true.

## Stretch

A school records the scores of three students in four subjects using
`Scores[Student, Subject]`.

1. Declare a two-dimensional integer array for these scores.
2. Write nested loops to input every score.
3. Write an algorithm to calculate and output the total score for each
   student.
4. Explain which loop processes the subjects and which loop moves between
   students.

## Homework

Complete any unfinished core task. Then write one sentence explaining when
you would use a one-dimensional array and when you would use a
two-dimensional array.
