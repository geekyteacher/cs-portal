---
title: "Lesson 4: Selection & Decision Making"
description: "Use IF...THEN...ELSE statements to make decisions in pseudocode and Python."
order: 4
draft: false
---

> [!NOTE]
>
> Read the explanation, complete the tasks, and record your answers in **Lesson 4** of your **Teams Portfolio Document**.

## Learning Objectives

- Explain how selection allows programs to make decisions based on conditions.
- Write single-condition selection statements using `IF...THEN...ELSE...ENDIF`.
- Use comparison operators (`=`, `<>`, `<`, `>`, `<=`, `>=`) in CAIE pseudocode and Python.

---

## 1. Explanation: What is Selection?

**Selection** is a programming construct where the path of execution depends on whether a condition evaluates to `TRUE` or `FALSE`.

In CAIE pseudocode, a two-way selection uses the `IF...THEN...ELSE...ENDIF` structure.

### Comparison Operators

| Operation | CAIE pseudocode | Python |
| --- | --- | --- |
| Equal to | `=` | `==` |
| Not equal to | `<>` | `!=` |
| Greater than | `>` | `>` |
| Less than | `<` | `<` |
| Greater than or equal to | `>=` | `>=` |
| Less than or equal to | `<=` | `<=` |

### Pseudocode Example

```pseudocode
DECLARE Mark : INTEGER
OUTPUT "Enter exam mark:"
INPUT Mark

IF Mark >= 50 THEN
    OUTPUT "Result: Pass"
ELSE
    OUTPUT "Result: Fail"
ENDIF
```

## 2. Practical Coding Activity

Run and test the following code in Python:

```python
mark = int(input("Enter exam mark: "))

if mark >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
```

**Experiment:** Change the condition to check whether the mark is equal to 100 and print `"Perfect Score!"`.

## 3. Portfolio Tasks (Submit to Teams)

> [!WARNING]
>
> Record your answers in **Lesson 4** of your **Algorithm Design Portfolio** in Teams.

1. **Syntax Check:** Identify the syntax error in this pseudocode and rewrite it correctly:

    ```pseudocode
    IF Age > 18
        OUTPUT "Adult"
    END
    ```

2. **Algorithm Design (Pass/Fail Gatekeeper):** Write pseudocode that:
   - Prompts the user to enter their account balance as a `REAL`.
   - Outputs `"Account in Credit"` if the balance is greater than or equal to `0.0`.
   - Otherwise, outputs `"Overdrawn"`.

3. **Dry Run Task:** What is the output of the following pseudocode if the user inputs `28`?

    ```pseudocode
    DECLARE Temp : REAL
    INPUT Temp

    IF Temp <= 0 THEN
        OUTPUT "Freezing"
    ELSE
        IF Temp >= 30 THEN
            OUTPUT "Hot"
        ELSE
            OUTPUT "Moderate"
        ENDIF
    ENDIF
    ```

> [!CHALLENGE]
>
> Write a Python program that inputs a number and outputs whether it is **Even** or **Odd** using the remainder operator `%`.
