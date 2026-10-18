---
title: Variables
description: Store, update, and use data in a program.
order: 1
draft: false
---

## Learning goals

- [ ] Explain what a variable is.
- [ ] Create and update variables in a program.
- [ ] Choose suitable names and data types.
- [ ] Distinguish variables from constants.
- [ ] Use input, output, and type conversion with variables.

## Key ideas

### What is a variable?

> [!NOTE]
>
> A **variable** is a named memory location used to store a value. A program can read that value and, when appropriate, change it while the program runs.

The examples assign a value to `score` and then display it:

```pseudocode
DECLARE score : INTEGER
score ← 12
OUTPUT score
```

```python
score = 12
print(score)
```

Here, `score` is the identifier (name), and `12` is its value.

### Variables and constants

A **variable** can be updated. A **constant** stores a value that should not change during the program. In CAIE pseudocode, use `CONSTANT` to define a constant and its value.

```pseudocode
CONSTANT PassMark = 50
```

Python does not have a special constant declaration. By convention, programmers use uppercase names for values that should not change:

```python
PASS_MARK = 50
```

### Assignment and declaration

**Assignment** stores a value in a variable. In CAIE pseudocode, the arrow `←` means “is assigned the value.” In Python, a single equals sign `=` is used for assignment.

```pseudocode
score ← 12
```

```python
score = 12
```

CAIE pseudocode requires variables to be declared with a data type before use. Python is dynamically typed: a variable is created when a value is assigned, and Python determines its type from that value.

```pseudocode
DECLARE score : INTEGER
score ← 12
```

```python
score = 12
```

### Data types

A data type describes the kind of value a variable can store. Common CAIE types and their Python equivalents are:

| CAIE pseudocode | Python                | Example value   |
| --- | --- | --- |
| `INTEGER` | `int` | `12` |
| `REAL` | `float` | `3.5` |
| `STRING` | `str` | `"Hello"` |
| `CHAR` | `str` (one character) | `"A"` |
| `BOOLEAN` | `bool` | `TRUE` / `True` |

Use a type that suits the information. For example, use an integer for a whole-number count and a string for a person's name.

```pseudocode
DECLARE age : INTEGER
DECLARE temperature : REAL
DECLARE name : STRING
DECLARE initial : CHAR
DECLARE isReady : BOOLEAN
```

```python
age = 14
temperature = 21.5
name = "Amina"
initial = "A"
is_ready = True
```

### Choosing identifier names

An **identifier** is the name given to a variable or constant. Choose names that make the program easier to understand, such as `totalMarks` or `student_name`, rather than unclear names such as `x`.

In Python, names can contain letters, digits, and underscores, but cannot begin with a digit or be a Python keyword. Python distinguishes between uppercase and lowercase letters, so `score` and `Score` are different names. CAIE pseudocode identifiers should also be meaningful and used consistently.

```pseudocode
DECLARE totalMarks : INTEGER
```

```python
total_marks = 0
```

### Input, output, and type conversion

Use `INPUT` and `OUTPUT` in CAIE pseudocode to receive and display values. In Python, use `input()` and `print()`. Python's `input()` returns text, so convert the input when a number is required. Use `int()` for whole numbers and `float()` for decimal numbers.

```pseudocode
DECLARE age : INTEGER
INPUT age
OUTPUT age
```

```python
age = int(input("Enter your age: "))
print(age)
```

### Updating a variable

A variable can be assigned a new value. For example, a counter is often increased by one each time an event occurs.

```pseudocode
count ← count + 1
```

```python
count = count + 1
```

The right side is evaluated first, then the result is stored back in `count`.

> [!WARNING]
>
> - **Using a variable before assigning it:** Give the variable a value before reading or updating it.
> - **Using the wrong data type:** Check that the type suits the value and the operation.
> - **Misspelling a name:** Use the same identifier consistently; Python treats uppercase and lowercase letters as different.

### Common naming and type errors

Check that names follow the language’s rules and that values have the expected type.

| Error | Example | Fix |
| --- | --- | --- |
| Python name starts with a digit | `2ndScore` | `second_score` |
| Spaces or hyphens in a Python name | `total marks` or `total-marks` | `total_marks` |
| Using a Python keyword as a name | `class` or `for` | Choose a descriptive name, such as `class_name` |
| Inconsistent capitalization | `score` and `Score` refer to different names | Use the same capitalization consistently |
| Forgetting to convert Python input | `age = input(...)`; `age + 1` causes a `TypeError` | `age = int(input(...))` |
| Value does not match a CAIE pseudocode type | `DECLARE age : INTEGER`, then `age ← "fourteen"` | Assign an integer value to `age` |

**pseudocode**
```pseudocode
Incorrect:
DECLARE age : STRING
INPUT age
age ← age + 1

Corrected:
DECLARE age : INTEGER
INPUT age
age ← age + 1
```

**python**
```python
Incorrect:
age = input("Enter your age: ")
age + 1

Corrected:
age = int(input("Enter your age: "))
age + 1
```

- **Confusing assignment with comparison:** In Python, `=` assigns a value, while `==` compares two values.

## Worked example

The program asks for a student's name and two whole-number test scores. It calculates and displays their total.

### CAIE pseudocode

```pseudocode
DECLARE studentName : STRING
DECLARE firstScore : INTEGER
DECLARE secondScore : INTEGER
DECLARE total : INTEGER

INPUT studentName
INPUT firstScore
INPUT secondScore

total ← firstScore + secondScore

OUTPUT studentName
OUTPUT total
```

### Python

```python
student_name = input("Enter the student's name: ")
first_score = int(input("Enter the first score: "))
second_score = int(input("Enter the second score: "))

total = first_score + second_score

print(student_name)
print(total)
```

Suppose the inputs are the name `"Kai"` and the scores `18` and `24`:

| Step | Variable or action | Value |
| --- | --- | --- |
| 1 | `studentName` / `student_name` | `"Kai"` |
| 2 | `firstScore` / `first_score` | `18` |
| 3 | `secondScore` / `second_score` | `24` |
| 4 | `total` | `42` |
| 5 | Output | `Kai`, then `42` |

1. The pseudocode declares each variable with an appropriate data type. Python creates each variable when a value is assigned.

2. The name is stored as text. In Python, each score is converted from input text to an integer.

3. The two scores are added, and the result is assigned to `total`.

4. The program outputs the student's name and the total.

## Practice

### A. Trace the variables

Write the value of each variable at the end of each program, then state the output.

1. **CAIE pseudocode**

```pseudocode
DECLARE number : INTEGER
DECLARE result : INTEGER

number ← 6
result ← number + 4
number ← number + 1

OUTPUT number
OUTPUT result
```

2. **Python**

```python
price = 2.5
quantity = 4
total = price * quantity
quantity = quantity + 1
print(total)
print(quantity)
```

3. **CAIE pseudocode**

```pseudocode
DECLARE isOpen : BOOLEAN
DECLARE message : STRING

isOpen ← TRUE
message ← "Ready"

IF isOpen = TRUE THEN
    OUTPUT message
ENDIF
```

### B. Short answer

Explain the difference between a variable and a constant. Give one example of when a constant would be useful.

### C. Programming task

Write a program in both Python and CAIE pseudocode that:

- Inputs a product name, its price, and the quantity purchased.

- Calculates the cost by multiplying the price by the quantity.

- Outputs the product name and the cost.

Use suitable variable names and data types. In Python, convert numeric input to a suitable numeric type.

## Answers

### A. Trace the variables

1. `number` is `7`; `result` is `10`. The program outputs `7`, then `10`.

2. `total` is `10.0`; `quantity` is `5`. The program outputs `10.0`, then `5`.

3. `isOpen` is `TRUE`; `message` is `"Ready"`. The program outputs `Ready`.

### B. Short answer

A variable can be updated while a program runs; a constant is intended to keep the same value. A constant is useful for a value used repeatedly that should remain fixed, such as a tax rate or a pass mark.

### C. Programming task: sample solution

**CAIE pseudocode**

```pseudocode
DECLARE productName : STRING
DECLARE price : REAL
DECLARE quantity : INTEGER
DECLARE cost : REAL

INPUT productName
INPUT price
INPUT quantity

cost ← price * quantity

OUTPUT productName
OUTPUT cost
```

**Python**

```python
product_name = input("Enter the product name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

cost = price * quantity

print(product_name)
print(cost)
```