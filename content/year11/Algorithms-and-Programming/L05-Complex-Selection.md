---
title: "Lesson 5: Complex Selection & Logical Operators"
description: "Combine conditions using AND, OR, NOT, and CASE structures."
order: 5
draft: false
---

> [!NOTE]
>
> Complete the reading and tasks below. Record your work in **Lesson 5** of your **Teams Portfolio Document**.

## Learning Objectives

- Combine selection conditions using logical operators (`AND`, `OR`, `NOT`).
- Construct multi-branch decisions using `ELSEIF`.
- Express multi-choice logic using `CASE OF...OTHERWISE...ENDCASE` in pseudocode.

---

## 1. Explanation: Compound Conditions

When a decision depends on more than one condition, use **logical operators**:

- `AND`: Both conditions must be `TRUE`.
- `OR`: At least one condition must be `TRUE`.
- `NOT`: Reverses the Boolean outcome.

### Example: CASE Selection

```pseudocode
DECLARE Grade : CHAR
OUTPUT "Enter grade (A-D):"
INPUT Grade

CASE OF Grade
    'A' : OUTPUT "Excellent"
    'B' : OUTPUT "Good"
    'C' : OUTPUT "Satisfactory"
    'D' : OUTPUT "Needs Improvement"
    OTHERWISE OUTPUT "Invalid Grade"
ENDCASE
```

## 2. Practical Coding Activity

Test compound conditions in Python:

```python
score = int(input("Enter score: "))
attendance = float(input("Enter attendance percentage: "))

if score >= 70 and attendance >= 85.0:
    print("Award: Distinction Certificate")
elif score >= 50 or attendance >= 90.0:
    print("Award: Standard Pass")
else:
    print("Award: Re-sit Required")
```

## 3. Portfolio Tasks (Submit to Teams)

> [!WARNING]
>
> Record your answers in **Lesson 5** of your **Algorithm Design Portfolio** in Teams.

1. **Logical Operator Analysis:** Evaluate whether each expression is `TRUE` or `FALSE` when `X = 10`, `Y = 20`, and `Z = 5`:
   - `(X < Y) AND (Y > Z)`
   - `(X = Y) OR (Z < X)`
   - `NOT (Y > X)`

2. **Algorithm Design (Grade Boundaries):** Write pseudocode that inputs a mark out of 100 and outputs a grade according to these rules:
   - `80` or higher: `"Grade A"`
   - `60` to `79`: `"Grade B"`
   - `40` to `59`: `"Grade C"`
   - Below `40`: `"Grade U"`

3. **CASE Structure Conversion:** Convert the following `IF` chain into a `CASE OF` structure in pseudocode:

    ```pseudocode
    IF Choice = 1 THEN
        OUTPUT "Add Record"
    ELSEIF Choice = 2 THEN
        OUTPUT "Delete Record"
    ELSEIF Choice = 3 THEN
        OUTPUT "Search Record"
    ELSE
        OUTPUT "Invalid Choice"
    ENDIF
    ```

> [!CHALLENGE]
>
> Write a Python program that accepts a month number from 1 to 12 and uses selection to print the number of days in that month. Ignore leap years.
