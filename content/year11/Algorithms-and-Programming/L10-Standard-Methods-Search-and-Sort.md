---
title: "Lesson 10: Standard Methods - Statistics, Searching and Sorting"
description: "Trace and write standard algorithms for totals, counts, averages, minimums, maximums, linear search and bubble sort."
order: 10
draft: false
---
## Topics in this page

- Totalling and counting
- Finding minimum and maximum values
- Calculating an average
- Linear search
- Bubble sort

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Recognise and apply the standard algorithms in this page.
- Initialise variables correctly before traversing data.
- Trace a linear search and bubble sort.
- Test algorithms using suitable data, including boundary cases.

## Quick Check

1. Why should a total be initialised before a loop?
2. If an array contains five values with indexes `1` to `5`, what is the
   final index?
3. How can you count how many values are greater than `10`?

## Learn

Use the algorithms below as patterns. In each case, match the array bounds and
data types to the problem.
Unless a task says otherwise, assume the array has already been populated
with the stated test data.

### Finding a maximum and minimum

Initialise the maximum and minimum using the first array element. Then compare
the remaining values. This works even if every value is negative.

```pseudocode
DECLARE Values : ARRAY[1:5] OF INTEGER
DECLARE Index, Largest, Smallest : INTEGER

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

OUTPUT Largest, Smallest
```

### Calculating an average

Add the values to a total, then divide by the number of values. Do not divide
by the final loop-counter value without checking what that value represents.

```pseudocode
DECLARE Values : ARRAY[1:5] OF REAL
DECLARE Index : INTEGER
DECLARE Total, Average : REAL

Total <- 0
FOR Index <- 1 TO 5
    Total <- Total + Values[Index]
NEXT Index

Average <- Total / 5
OUTPUT Average
```

### Linear search

Linear search checks array elements in order until the item is found or there
are no more elements to check.

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

IF Found = TRUE THEN
    OUTPUT "Value found at position ", Index
ELSE
    OUTPUT "Value not found"
ENDIF
```

The `Found` flag records whether a match has occurred. The loop stops when a
match is found or the index moves past the last array element.

### Bubble sort

Bubble sort compares neighbouring values and swaps them if they are in the
wrong order. After each full pass, the largest unsorted value has moved to
the end of the unsorted section.

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

The inner loop ends at `5 - Pass`, so `Index + 1` stays within the array.
`Temp` preserves a value during the swap.

## Guided Practice

### Trace a linear search

Search for `14` in the array `[8, 14, 5, 14]`. Record each tested index and
value. Does this algorithm stop at the first match?

### Trace a bubble-sort pass

Use the values `[6, 2, 5, 1]`. Complete the first pass of bubble sort by
comparing each neighbouring pair from left to right. Record the array after
each comparison.

## Core Practice

Complete the tasks. Use trace tables to show your reasoning.

1. Write an algorithm to find the largest and smallest values in an array of
   eight integers.
2. Write an algorithm to calculate the average of six real numbers stored in
   an array.
3. Trace the linear-search algorithm using `[4, 9, 2, 9, 7]` to search for
   `9`. State the position reported.
4. Trace all passes of bubble sort for `[5, 1, 4, 2]`.

## Support

Use these reminders:

- **Maximum/minimum:** initialise both from the first element, then start the
  loop at the second element.
- **Average:** `Average <- Total / NumberOfValues`.
- **Search:** initialise `Found <- FALSE` and begin at the first valid index.
- **Sort:** compare neighbours; use a temporary variable to swap them.

Complete the search scaffold:

```pseudocode
Found <- FALSE
Index <- 1

WHILE Index <= _____ AND Found = FALSE DO
    IF Values[Index] = SearchValue THEN
        Found <- _____
    ELSE
        Index <- Index + _____
    ENDIF
ENDWHILE
```

## Stretch

1. What happens when the search value occurs more than once? How could you
   adapt the algorithm to count all occurrences?
2. Test the maximum/minimum algorithm with an array containing only negative
   values. Explain why initialising from the first element is safer than
   setting `Largest` to `0`.
3. Choose test data for the bubble sort that includes repeated values. Does
   the algorithm still sort the values into ascending order?

## Homework

Choose one method from this page and write a complete trace for a small test
dataset. Include the initial values, each comparison or update, and the final
output.
