---
title: "Lesson 9: Arrays, Traversal and Accumulation"
description: "Declare and traverse 1D and 2D arrays, and apply totalling and counting algorithms in CAIE pseudocode."
order: 9
draft: false
---

## Learning Objectives

- Explain why an array is used to store related data under a single identifier.
- Declare and access elements in one-dimensional and two-dimensional arrays.
- Write iteration loops to traverse arrays for totalling and counting.
- Translate array traversal logic from pseudocode into Python.

---

## 1. Starter (5 mins — Do this first)

Answer these questions in your book without running any code.

1. What values does `Counter` take in this loop?

```pseudocode
DECLARE Counter : INTEGER

FOR Counter <- 1 TO 3
    OUTPUT Counter
NEXT Counter
```

2. Why must `Total` always be initialised to `0` *before* a loop starts adding numbers to it?

3. In an array declared as:

```pseudocode
DECLARE Marks : ARRAY[1:5] OF INTEGER
```

what is the index of the final element?

---

## 2. Learn: Arrays & Traversal

### What is an Array?

An **array** stores a group of data items of the **same data type** under one name. Each individual item is accessed using an **index number**.

In CAIE pseudocode, array index bounds are declared explicitly:

```pseudocode
DECLARE Scores : ARRAY[1:5] OF INTEGER
```

- **Reading/Writing:**  
  `Scores[1] <- 72` assigns a value to the first element.

  ```pseudocode
  Scores[1] <- 72
  ```

  `INPUT Scores[3]` reads a value directly into the third element.

- **Traversal:**  
  A `FOR` loop is the standard way to visit every element in an array using an index variable.

```pseudocode
DECLARE Index : INTEGER

FOR Index <- 1 TO 5
    OUTPUT Scores[Index]
NEXT Index
```

### Two-Dimensional Arrays

A 2D array stores data in **rows and columns** (like a table or spreadsheet).

It requires two index variables: one for the row and one for the column.

```pseudocode
DECLARE Grid : ARRAY[1:3, 1:4] OF INTEGER

Grid[2, 3] <- 10
```

To traverse a 2D array, use **nested loops**.

```pseudocode
DECLARE Row, Col : INTEGER

FOR Row <- 1 TO 3
    FOR Col <- 1 TO 4
        OUTPUT Grid[Row, Col]
    NEXT Col
NEXT Row
```

### Totalling vs Counting Patterns

#### Accumulating a Total

Initialise the total before the loop starts.

```pseudocode
Total <- 0

FOR Index <- 1 TO 5
    Total <- Total + Scores[Index]
NEXT Index
```

#### Conditional Counting

Initialise the counter before the loop starts.

```pseudocode
PassCount <- 0

FOR Index <- 1 TO 5
    IF Scores[Index] >= 50 THEN
        PassCount <- PassCount + 1
    ENDIF
NEXT Index
```

---

## 3. Guided Practice (We do this together)

Trace the algorithm below.

The array `Scores` contains the values:

```text
[12, 7, 15, 6]
```

Complete the trace table tracking:

- The running total.
- The count of values greater than `10`.

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

| Index | Scores[Index] | Total | Scores[Index] > 10 | Count |
|---------|---------|---------|-------------------|---------|
| — | — | 0 | — | 0 |
| 1 | 12 | 12 | TRUE | 1 |
| 2 | 7 | | | |
| 3 | 15 | | | |
| 4 | 6 | | | |

1. Complete rows 2, 3 and 4 of the table.
2. What are the final values of `Total` and `Count`?

---

## 4. Core Practice (Paper / Exam Style)

Complete these tasks on your worksheet or in your book.

### Task 1: Record and Total Scores

Write a CAIE pseudocode algorithm that:

1. Declares an integer array to store **six** test scores.
2. Uses a `FOR` loop to input all six scores.
3. Calculates the overall total of all six scores.
4. Outputs the final total after the loop finishes.

---

### Task 2: Temperature Threshold Counter

An array called `Temperature` stores daily readings for a seven-day week.

```pseudocode
Temperature[1] ... Temperature[7]
```

Write an algorithm that:

1. Traverses the array.
2. Counts how many temperatures are **below 10**.
3. Outputs the final count with a clear label.

---

### Task 3: Spot the Array Boundary Bug

This algorithm is supposed to process an array of five scores, but it crashes or behaves incorrectly.

```pseudocode
DECLARE Marks : ARRAY[1:5] OF INTEGER
DECLARE Index, Total : INTEGER

Total <- 0

FOR Index <- 0 TO 5
    Total <- Total + Marks[Index]
NEXT Index

OUTPUT Total
```

1. What are the **two** indexing errors in the `FOR` loop range?
2. Rewrite the corrected pseudocode.

---

## 5. Python Implementation (Thonny Lab Check)

Once your pseudocode is written and checked, open Thonny and implement **Task 2** as a Python script.

1. Create a list of 7 integers representing temperatures.
2. Use a `for` loop and an `if` statement to count how many values are `< 10`.
3. Save your script as:

```text
l09_temperatures.py
```

4. Upload it to the Teams assignment when finished.

---

## 6. Stretch (Finished Early?)

A school records exam scores for **3 students** across **4 subjects** using a two-dimensional array:

```pseudocode
Scores[Student, Subject]
```

1. Write the pseudocode declaration for this 2D array.
2. Write nested loops to input every score.
3. Write an algorithm that calculates and outputs the **total score for each student** (summing across all four subjects).

### Challenge Extension

Modify your solution so that it also outputs:

- The highest total score.
- Which student achieved that score.