---
title: Selection
description: Make a program choose between actions using conditions.
order: 2
draft: false
---

## Learning goals

- [ ] Explain how selection changes program flow based on conditions.
- [ ] Write conditions using relational operators (`=`, `<>`, `<`, `>`, `<=`, `>=`) and logical operators (`AND`, `OR`, `NOT`).
- [ ] Construct single-choice, dual-choice, and multi-choice selection statements using `IF` statements and `CASE` structures.
- [ ] Implement selection constructs in both CAIE Pseudocode and high-level programming languages (Python, Java, Visual Basic).

---

## Key ideas

Selection is a fundamental control structure that allows a program to choose different execution paths based on whether a given condition evaluates to `TRUE` or `FALSE`. 

Without selection, algorithms would execute line-by-line in a rigid sequence. Selection enables dynamic decision-making, such as validating user input, identifying minimum/maximum values, or controlling access based on specific criteria.

### Comparison and Logical Operators

To form conditions, we compare values using **relational (comparison) operators** and combine them using **logical operators**.

#### Relational Operators
| Operation | CAIE Pseudocode | Python | Java / VB |
| :--- | :---: | :---: | :---: |
| Equal to | `=` | `==` | `==` (Java) / `=` (VB) |
| Not equal to | `<>` | `!=` | `!=` (Java) / `<>` (VB) |
| Less than | `<` | `<` | `<` |
| Greater than | `>` | `>` | `>` |
| Less than or equal to | `<=` | `<=` | `<=` |
| Greater than or equal to | `>=` | `>=` | `>=` |

> **Note:** In CAIE Pseudocode, the single `=` symbol is used for testing equality (e.g., `IF Score = 100 THEN`), while `←` is strictly used for assignment (e.g., `Score ← 100`).

#### Logical Operators
* **`AND`**: Evaluates to `TRUE` only if **both** conditions are true.
* **`OR`**: Evaluates to `TRUE` if **at least one** condition is true.
* **`NOT`**: Inverts the boolean value of a condition (`TRUE` becomes `FALSE`, and vice versa).

---

### The Two Types of Conditional Statements

In the CAIE 0478 syllabus, selection is implemented using two primary structures:

#### 1. `IF...THEN...ELSE...ENDIF` Statements
Used when testing logical conditions or checking ranges of values.

* **Single Choice (`IF...THEN`)**: Executes a block of code only if the condition is `TRUE`.
* **Dual Choice (`IF...THEN...ELSE`)**: Executes one block if the condition is `TRUE`, and an alternative block if it is `FALSE`.
* **Multiple Choice (`IF...THEN...ELSE IF...ELSE`)**: Evaluates multiple conditions sequentially until one is satisfied.

#### 2. `CASE...OF...OTHERWISE...ENDCASE` Statements
Used when a single variable or expression is checked against a set of discrete, known values (e.g., menu choices, grade letters, day numbers).

---

## Language Comparison Matrix

Here is how the main selection constructs look across CAIE Pseudocode and the three official IGCSE languages:

### Dual Choice (If-Else)

::: code-group

```pseudocode [CAIE Pseudocode]
IF Age >= 18 THEN
    OUTPUT "Access granted"
ELSE
    OUTPUT "Access denied"
ENDIF
```

```python [Python]
if age >= 18:
    print("Access granted")
else:
    print("Access denied")
```

```java [Java]
if (age >= 18) {
    System.out.println("Access granted");
} else {
    System.out.println("Access denied");
}
```

```visualbasic [Visual Basic]
If Age >= 18 Then
    Console.WriteLine("Access granted")
Else
    Console.WriteLine("Access denied")
End If
```

:::

### Multi-Value Selection (CASE vs Switch)

::: code-group

```pseudocode [CAIE Pseudocode]
CASE OF Grade
    "A" : OUTPUT "Excellent"
    "B" : OUTPUT "Good"
    "C" : OUTPUT "Satisfactory"
    OTHERWISE OUTPUT "Improvement required"
ENDCASE
```

```python [Python (3.10+)]
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Satisfactory")
    case _:
        print("Improvement required")
```

```java [Java]
switch (grade) {
    case 'A':
        System.out.println("Excellent");
        break;
    case 'B':
        System.out.println("Good");
        break;
    case 'C':
        System.out.println("Satisfactory");
        break;
    default:
        System.out.println("Improvement required");
}
```

```visualbasic [Visual Basic]
Select Case Grade
    Case "A"
        Console.WriteLine("Excellent")
    Case "B"
        Console.WriteLine("Good")
    Case "C"
        Console.WriteLine("Satisfactory")
    Case Else
        Console.WriteLine("Improvement required")
End Select
```

:::

---

## Worked example

### Scenario
A theme park ride has a minimum height requirement of **120 cm** and a maximum weight limit of **100 kg**. 

Write an algorithm that prompts the user for their height and weight, and determines whether they are permitted to board the ride. If they are denied, output a specific reason.

### Pseudocode Solution

```pseudocode
// Prompt and input height and weight
OUTPUT "Enter height in cm: "
INPUT Height

OUTPUT "Enter weight in kg: "
INPUT Weight

// Evaluate conditions using logical operator AND
IF Height >= 120 AND Weight <= 100 THEN
    OUTPUT "Permitted to board the ride."
ELSE IF Height < 120 AND Weight > 100 THEN
    OUTPUT "Rejected: Too short and exceeds weight limit."
ELSE IF Height < 120 THEN
    OUTPUT "Rejected: Does not meet minimum height requirement."
ELSE
    OUTPUT "Rejected: Exceeds maximum weight limit."
ENDIF
```

### Step-by-Step Breakdown

1. **Input Prompts**: The algorithm explicitly prompts the user before each `INPUT` line to ensure clear user interaction.
2. **Combined Logical Test**: The initial `IF` statement uses `AND` to ensure **both** constraints (`Height >= 120` and `Weight <= 100`) are satisfied simultaneously.
3. **Branching Diagnostics**: If the primary check fails, nested `ELSE IF` branches evaluate which specific constraint failed so an appropriate output is generated.
4. **Block Termination**: Every `IF` statement block is explicitly closed with an `ENDIF` matching CAIE exam standards.

---

## Practice

### Quick Check Questions

1. **Syntax Identification**: Identify the mistake in the following CAIE Pseudocode snippet:
   ```pseudocode
   IF Score = 50
       OUTPUT "Halfway there"
   ENDIF
   ```
2. **Operator Logic**: What will be the output of the condition `(Age > 12 OR Weight < 40) AND NOT(VIP = TRUE)` if `Age = 14`, `Weight = 50`, and `VIP = TRUE`?
3. **Structure Choice**: State whether an `IF` statement or a `CASE` statement is more suitable for checking if an exam mark (0–100) falls into grade boundaries (e.g., $\ge 80$ for A*, $\ge 70$ for A). Briefly explain your choice.

---

### Programming & Algorithm Tasks

#### Task 1: Cinema Ticket Pricing (Core)
Write a program (or pseudocode algorithm) that calculates ticket prices based on age:
* Children under 5: **Free** ($0)
* Children aged 5 to 17: **$8**
* Adults aged 18 to 64: **$15**
* Seniors aged 65 and above: **$10**

> **Requirements:** Ensure your program outputs clear prompts, uses appropriate `IF...ELSE IF...ELSE` logic, and handles invalid negative inputs gracefully.

#### Task 2: Calculator Menu (Extension)
Construct an algorithm using a `CASE` statement (or `Select Case` / `switch`) that asks the user to input two real numbers and select an arithmetic operation from a menu:
1. `+` (Add)
2. `-` (Subtract)
3. `*` (Multiply)
4. `/` (Divide)

> **Extension Challenge:** Include a validation check within the division branch to prevent division by zero (`/ 0`).

## IGCSE Exam-Style Questions

### Question 1 (1 mark)

State the output produced by the following algorithm.

```pseudocode
number ← 25

IF number > 20 THEN
    OUTPUT "High"
ENDIF
```

---

### Question 2 (1 mark)

State the output produced by the following algorithm.

```pseudocode
score ← 45

IF score >= 50 THEN
    OUTPUT "Pass"
ELSE
    OUTPUT "Fail"
ENDIF
```

---

### Question 3 (2 marks)

A student enters a temperature into a program.

Write a selection statement that outputs:

```text
Hot
```

when the temperature is greater than 25.

Otherwise output:

```text
Cold
```

Use CAIE pseudocode.

---

### Question 4 (2 marks)

State the condition being tested in the following algorithm:

```pseudocode
IF age >= 16 THEN
    OUTPUT "Can Drive"
ENDIF
```

Explain what happens when:

a) age = 18

b) age = 10

---

### Question 5 (4 marks)

A theme park charges entry based on height.

If a person is 120cm or taller they may ride the rollercoaster.

Otherwise they may not.

Write a complete algorithm using selection to display:

```text
Ride Allowed
```

or

```text
Ride Not Allowed
```

---

## Answers

### Question 1

```text
High
```

(1 marks)

---

### Question 2

```text
Fail
```

(1 marks)

---

### Question 3

```pseudocode
IF temperature > 25 THEN
    OUTPUT "Hot"
ELSE
    OUTPUT "Cold"
ENDIF
```

(2 marks)

---

### Question 4

Condition:

```text
age >= 16
```

a)

```text
Can Drive
```

is displayed.

b)

No output is displayed.

(2 marks)

---

### Question 5

```pseudocode
INPUT height

IF height >= 120 THEN
    OUTPUT "Ride Allowed"
ELSE
    OUTPUT "Ride Not Allowed"
ENDIF
```

(4 marks)