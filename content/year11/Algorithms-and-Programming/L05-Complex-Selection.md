---
title: "Lesson 5: Complex Selection & Logical Operators"
description: "Combine conditions using AND, OR, NOT, and CASE structures."
order: 5
draft: false
---

> [!NOTE]
>
> Complete the examples and core tasks. Record your answers in **Lesson 5** of your **Teams Portfolio Document**.

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

### Combining conditions with `AND`, `OR` and `NOT`

```pseudocode
DECLARE Age : INTEGER
DECLARE HasTicket : BOOLEAN
INPUT Age, HasTicket

IF Age >= 18 AND HasTicket = TRUE THEN
    OUTPUT "Entry allowed"
ELSE
    OUTPUT "Entry denied"
ENDIF
```

Both conditions must be true for entry to be allowed. Use brackets to make
the intended grouping clear in longer conditions.

### Multiple branches with `ELSEIF`

Conditions are checked in order. The first true branch runs; later branches
are skipped.

```pseudocode
DECLARE Mark : INTEGER
INPUT Mark

IF Mark >= 80 THEN
    OUTPUT "Grade A"
ELSEIF Mark >= 60 THEN
    OUTPUT "Grade B"
ELSEIF Mark >= 40 THEN
    OUTPUT "Grade C"
ELSE
    OUTPUT "Grade U"
ENDIF
```

Put the most restrictive/highest threshold first. For example, if
`Mark >= 40` came first, marks of 80 or more would be assigned Grade C.

### Nested selection

An `IF` statement can be placed inside another selection when a second
decision is only needed in one branch:

```pseudocode
IF Age >= 18 THEN
    IF HasTicket = TRUE THEN
        OUTPUT "Entry allowed"
    ELSE
        OUTPUT "Ticket required"
    ENDIF
ELSE
    OUTPUT "Minimum age not met"
ENDIF
```

Trace the inner condition only when the outer condition leads into it.

### Multi-way selection with `CASE`

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

Use `CASE` when one value is compared with several possible values. Include
`OTHERWISE` to handle values that do not match a listed case.

## Guided Practice

For `X = 10`, `Y = 20` and `Z = 5`, evaluate:

- `(X < Y) AND (Y > Z)`
- `(X = Y) OR (Z < X)`
- `NOT (Y > X)`

Then trace the grade example with marks `39`, `40`, `60` and `80`.

## Core Practice

Answer algorithm-design questions in **CAIE pseudocode**.

1. **Grade boundaries:** Write an algorithm that inputs a mark out of 100 and
   outputs:
   - `80` or higher: `"Grade A"`
   - `60` to `79`: `"Grade B"`
   - `40` to `59`: `"Grade C"`
   - Below `40`: `"Grade U"`
2. **CASE conversion:** Convert this `IF` chain to a `CASE OF` structure:

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

3. **Nested decision:** Write an algorithm that inputs `Age` and
   `HasPermission`. Output `"Allowed"` only when the person is at least 16
   and has permission. Otherwise, output a message explaining which
   requirement was not met.

## Explore in Python

Translate one of your pseudocode answers into Python and test values at
important boundaries. This is practice; use CAIE pseudocode for Paper 2
algorithm-design answers.

```python
mark = int(input("Enter mark: "))

if mark >= 80:
    print("Grade A")
elif mark >= 60:
    print("Grade B")
elif mark >= 40:
    print("Grade C")
else:
    print("Grade U")
```

## Support

For the grade task:

- Check the highest boundary first.
- Use `ELSEIF` for each additional grade range.
- Use `ELSE` for marks below the final boundary.
- Test `39`, `40`, `59`, `60`, `79` and `80`.

For `CASE`, each branch compares the same selector (`Choice`) with one value.

## Stretch

Write a Python program that inputs a month number from `1` to `12` and uses
selection to output the number of days in that month. Ignore leap years.
Include a message for an invalid month.

## Portfolio Tasks (Submit to Teams)

Record your answers in **Lesson 5** of your **Algorithm Design Portfolio** in
Teams. Include the logical-operator answers and one completed pseudocode
algorithm from the core tasks.
