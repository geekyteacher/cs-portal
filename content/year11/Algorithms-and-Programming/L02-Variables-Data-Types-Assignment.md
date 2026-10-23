---
title: "Lesson 2: Variables, Data Types & Assignment"
description: "Understand memory locations, data types, and assignment operations in CAIE pseudocode."
order: 2
draft: false
---

> [!NOTE]
>
> Complete the reading and tasks below. Record your work in **Lesson 2** of your **Teams Portfolio Document**.

## Learning Objectives

- Identify and select appropriate elementary data types (`INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`).
- Perform variable declaration and assignment using standard CAIE pseudocode syntax (`<-`).
- Trace variable value updates and swapping logic[cite: 4, 7].

---

## 1. Explanation: Variables & Data Types

A **variable** is a named memory location used to store data that can change during program execution[cite: 5]. Every variable must be declared with a specific **data type**:

| CAIE Data Type | Description | Pseudocode Example |
| --- | --- | --- |
| `INTEGER` | Whole numbers | `DECLARE Age : INTEGER` |
| `REAL` | Numbers with decimal points | `DECLARE Price : REAL` |
| `CHAR` | A single character | `DECLARE Gender : CHAR` |
| `STRING` | A sequence of characters | `DECLARE Name : STRING` |
| `BOOLEAN` | True or False values | `DECLARE Valid : BOOLEAN` |

> [!TIP]
>
> In CAIE Pseudocode, assignment uses the arrow symbol `<-` (e.g., `Age <- 16`), whereas Python uses `=`[cite: 1, 4].

---

## 2. Practical Coding Activity

Run the following code in Python and observe how variable data types behave:

```python
x = 10         # Integer
y = 3.5        # Float / Real
name = "Alex"  # String
is_passed = True # Boolean

# Re-assigning variables
x = x + 5
print("Updated x:", x)
```

## 3. Portfolio Tasks (Submit to Teams)

> [!WARNING]
>
> Copy your answers into Lesson 2 of your Algorithm Design Portfolio in Teams.

1. Data Type Selection: Choose the most suitable CAIE data type for each item:
    - A student's exam score (e.g., 85)
    - A product price (e.g., $19.99)
    - Whether a user is logged in (TRUE/FALSE)
    - A telephone area code (e.g., "020")

2. Algorithm Design (Variable Swap): Write pseudocode that inputs two values into variables A and B, swaps their values using a temporary variable Temp, and outputs the new values.

3. Dry Run Exercise: Trace the final values of P, Q, and R after execution:

```pseudocode
DECLARE P, Q, R : INTEGER
P <- 5
Q <- 12
R <- P + Q
P <- R * 2
Q <- Q - 2
R <- P - Q
```

> [!CHALLENGE]
>
> Extension: Write a Python program that swaps two variables without using a third temporary variable!