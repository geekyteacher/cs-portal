---
title: Iteration
description: Repeat instructions using count-controlled and condition-controlled loops.
order: 3
draft: false
---

# Iteration

## Learning goals

- [ ] Explain why iteration is used.
- [ ] Choose between count-controlled and condition-controlled loops.
- [ ] Trace loop execution and identify termination conditions.
- [ ] Write equivalent loops in Python and CAIE pseudocode.
- [ ] Use nested loops, totals, and counters safely.

## Key ideas

### Why use iteration?

**Iteration** means repeating a set of instructions. It is useful when a task needs the same steps performed several times, such as processing a set of marks or displaying a pattern. A loop makes a program shorter and easier to change than writing the same instructions repeatedly.

### Count-controlled loops

Use a count-controlled loop when the number of repetitions is known. In CAIE pseudocode, `FOR ... TO ... NEXT` repeats for the specified values. In Python, `for` with `range()` is commonly used.

Both examples below repeat ten times, using the values 1 to 10:

```pseudocode
FOR i ← 1 TO 10
    OUTPUT i
NEXT i
```

```python
for i in range(1, 11):
    print(i)
```

In Python, the final value in `range()` is not included. Therefore, `range(1, 11)` produces values from 1 to 10.

> [!TIP]
>
> When translating an inclusive pseudocode range to Python, remember that `range()` excludes its stop value. For example, `FOR i ← 1 TO 10` becomes `range(1, 11)`.

### Condition-controlled loops

Use a condition-controlled loop when repetition depends on a condition rather than a fixed number of repetitions.

A `WHILE` loop checks its condition before each repetition. If the condition is false at the start, the loop body does not run.

```pseudocode
WHILE condition DO
    instructions
ENDWHILE
```

```python
while condition:
    instructions
```

A `REPEAT ... UNTIL` loop checks its condition after each repetition. Its body runs at least once. It stops when the condition becomes true.

```pseudocode
REPEAT
    instructions
UNTIL condition
```

Python has no direct `REPEAT ... UNTIL` structure. A `while` loop can be used to achieve the same behavior, but the first execution must happen before the condition is checked.

```python
instructions
while not condition:
    instructions
```

### Nested loops

A **nested loop** is a loop inside another loop. The inner loop completes all its repetitions for each repetition of the outer loop. Nested loops are useful for tasks such as processing rows and columns.

```pseudocode
FOR row ← 1 TO 2
    FOR column ← 1 TO 3
        OUTPUT row, column
    NEXT column
NEXT row
```

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)
```

### Totals and counters

A **counter** keeps track of how many times something happens. A **running total** accumulates values. Set each variable to an initial value before the loop, then update it inside the loop.

```pseudocode
count ← 0
total ← 0

FOR i ← 1 TO 3
    INPUT number
    count ← count + 1
    total ← total + number
NEXT i

OUTPUT count
OUTPUT total
```

```python
count = 0
total = 0

for i in range(1, 4):
    number = int(input("Enter a number: "))
    count = count + 1
    total = total + number

print(count)
print(total)
```

> [!WARNING]
>
> - **Infinite loop:** A condition-controlled loop never ends because its condition never becomes true or false as needed. Check that a variable used in the condition is updated.
> - **Off-by-one error:** A loop runs one time too many or too few. Check the first and last values, and remember that Python `range()` excludes its stop value.
> - **Incorrect initialization:** A total or counter is not set before the loop begins, so its value is undefined or carried over from earlier work.
> - **Incorrect nesting:** Indentation determines which instructions belong to a loop in Python. In pseudocode, check that each `NEXT` matches the correct `FOR`.

## Worked example

The program inputs three numbers, then displays their total. Trace the values of `number` and `total` after each loop repetition.

### CAIE pseudocode

```pseudocode
total ← 0

FOR i ← 1 TO 3
    INPUT number
    total ← total + number
NEXT i

OUTPUT total
```

### Python

```python
total = 0

for i in range(1, 4):
    number = int(input("Enter a number: "))
    total = total + number

print(total)
```

Suppose the inputs are 4, 7, and 2:

| Repetition | `i` | `number` | `total` after addition |
| --- | --- | --- | --- |
| Start | — | — | 0 |
| 1 | 1 | 4 | 4 |
| 2 | 2 | 7 | 11 |
| 3 | 3 | 2 | 13 |

1. `total` is initialized to 0 before the loop.

2. The loop runs once for each value of `i` from 1 to 3.

3. Each input is added to the existing total.

4. After the third repetition, the program outputs 13.

## Practice

### A. Trace the loops

For each question, write the output in order.

1. **CAIE pseudocode**

    ```pseudocode
   FOR i ← 2 TO 5
       OUTPUT i
   NEXT i
   ```

2. **Python**

   ```python
   total = 0
   for n in range(1, 5):
       total = total + n
   print(total)
   ```

3. **CAIE pseudocode**

    ```pseudocode
   count ← 0
   number ← 3

   WHILE number < 6 DO
       count ← count + 1
       number ← number + 1
   ENDWHILE

   OUTPUT count
   ```

### B. Short answer

Explain one difference between `WHILE ... DO ... ENDWHILE` and `REPEAT ... UNTIL`. When might each be appropriate?

### C. Programming task

Write a program in both Python and CAIE pseudocode that:

- Inputs five numbers.

- Counts how many are greater than 10.

- Calculates and outputs the total of all five numbers.

<details>
<summary>
<h3>Answers</h3>
</summary>
<h4>A. Trace the loops</h4>

1. Output: 2, 3, 4, 5.

2. Output: 10.

3. Output: 3.

<h4>B. Short answer</h4>

A `WHILE` loop checks its condition before the body runs, so the body might run zero times. A `REPEAT ... UNTIL` loop checks after the body, so the body runs at least once. Use `WHILE` when the condition should be checked before starting; use `REPEAT ... UNTIL` when an action must happen at least once, such as asking for input before checking it.

#### C. Programming task: sample solution

**CAIE pseudocode**

```pseudocode
total ← 0
count ← 0

FOR i ← 1 TO 5
    INPUT number
    total ← total + number
    IF number > 10 THEN
        count ← count + 1
    ENDIF
NEXT i

OUTPUT total
OUTPUT count
```

**Python**

```python
total = 0
count = 0

for i in range(1, 6):
    number = int(input("Enter a number: "))
    total = total + number
    if number > 10:
        count = count + 1

print(total)
print(count)
```
</details>