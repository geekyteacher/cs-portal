---
title: "Lesson 10: Standard Methods - Statistics, Searching and Sorting"
description: "Trace and write standard algorithms for totals, counts, averages, minimums, maximums, linear search and bubble sort."
order: 10
draft: false
---

## Learning Objectives

- Apply standard algorithms for finding minimums, maximums, and averages.
- Trace and implement a linear search using a `Found` flag.
- Trace and execute a bubble sort using neighbour comparisons and a temporary swap variable.
- Test algorithms using edge cases and trace tables.

---

## 1. Starter (5 mins — Do this first)

Answer these questions in your book without running any code.

1. If an array contains five values stored at indexes `1` to `5`, what index is checked last?
2. Why must maximum and minimum variables be initialised using the **first element of the array** (`Values[1]`) rather than starting at `0`?
3. What is the purpose of the temporary `Temp` variable during a swap operation?

---

## 2. Learn: Standard Algorithms

### Minimum, Maximum and Average

#### Minimum and Maximum

Initialise the variables using the **first element of the array**, then start the loop from the second element.

```pseudocode
Largest <- Values[1]
Smallest <- Values[1]

FOR Index <- 2 TO 5
    IF Values[Index] > Largest THEN
        Largest <- Values[Index]
    ENDIF

    IF Values[Index] < Smallest THEN
        Smallest <- Values[Index]
    ENDIF
NEXT Index
```

This ensures the algorithm works correctly even if all values are negative.

#### Average

To calculate an average:

1. Total all values.
2. Divide by the number of values.

```pseudocode
Total <- 0

FOR Index <- 1 TO 5
    Total <- Total + Values[Index]
NEXT Index

Average <- Total / 5
```

---

### Linear Search

Linear search checks each element in turn until:

- The value is found, or
- The end of the array is reached.

A Boolean flag is often used to track whether a match has been found.

```pseudocode
DECLARE Values : ARRAY[1:5] OF INTEGER
DECLARE Index, SearchValue : INTEGER
DECLARE Found : BOOLEAN

INPUT SearchValue

Found <- FALSE
Index <- 1

WHILE Index <= 5 AND Found = FALSE DO
    IF Values[Index] = SearchValue THEN
        Found <- TRUE
    ELSE
        Index <- Index + 1
    ENDIF
ENDWHILE
```

---

### Bubble Sort

Bubble sort compares neighbouring values and swaps them if they are in the wrong order.

A temporary variable is used so that no data is lost during the swap.

```pseudocode
DECLARE Values : ARRAY[1:5] OF INTEGER
DECLARE Pass, Index, Temp : INTEGER

FOR Pass <- 1 TO 4
    FOR Index <- 1 TO 5 - Pass

        IF Values[Index] > Values[Index + 1] THEN
            Temp <- Values[Index]
            Values[Index] <- Values[Index + 1]
            Values[Index + 1] <- Temp
        ENDIF

    NEXT Index
NEXT Pass
```

Notice that the inner loop becomes shorter after each pass because the largest values gradually move to the end of the array.

---

## 3. Guided Practice (We do this together)

### Trace a Linear Search

Search for the target value:

```text
14
```

in the array:

```text
[8, 14, 5, 14]
```

1. Which index does the algorithm find first?
2. Does the standard algorithm stop immediately once the first match is found?

---

### Trace a Bubble Sort Pass

Use the starting array:

```text
[6, 2, 5, 1]
```

Complete the **first pass** of a bubble sort.

Record the array after each comparison and swap.

---

## 4. Core Practice (Paper / Exam Style)

Complete these tasks in your book or on your worksheet.

### Task 1: Maximum and Minimum Algorithm

Write CAIE pseudocode that:

1. Processes an array of eight integers.
2. Finds the largest value.
3. Finds the smallest value.
4. Outputs both values.

---

### Task 2: Average Calculation

Write an algorithm that calculates the average of six real numbers stored in an array.

Output the final average.

---

### Task 3: Linear Search Trace

Trace the linear search algorithm using:

```text
Array: [4, 9, 2, 9, 7]
Search value: 9
```

State the exact position reported by the algorithm.

---

### Task 4: Bubble Sort Trace

Trace every pass of a bubble sort for the array:

```text
[5, 1, 4, 2]
```

Show the state of the array after each pass.

---

## 5. Python Implementation (Thonny Lab Check)

Open Thonny and implement a linear search program.

1. Create a list containing five integer scores.
2. Ask the user to enter a search value.
3. Search through the list using a loop.
4. Output either:
   - The position where the value was found, or
   - `"Value not found"` if it does not exist.
5. Save your program as:

```text
l10_search.py
```

6. Upload it to the Teams assignment.

---

## 6. Stretch (Finished Early?)

Consider what happens if a search value appears multiple times in an array.

For example:

```text
[7, 4, 7, 2, 7]
```

1. What would a standard linear search report?
2. Why does it not find every occurrence?
3. How could you modify the algorithm so it counts **all occurrences** instead of stopping at the first match?
4. Write the pseudocode for your improved solution.

### Challenge Extension

Write an algorithm that:

- Searches an array for a target value.
- Counts how many times the value appears.
- Outputs both:
  - Whether the value exists.
  - The total number of occurrences.