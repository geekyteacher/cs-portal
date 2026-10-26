---
title: "Lesson 1: Sequence and Algorithms"
description: "Understand the concept of algorithm sequence and execution flow."
order: 1
draft: false
---

> [!NOTE]
> Complete the reading and coding tasks below. Paste your answers into **Lesson 1** of your **Teams Portfolio Document** before the end of the week.

## 🎯 Learning Objectives

- Explain what an algorithm is and why sequence matters.
- Read and trace a simple sequential algorithm.
- Write standard pseudocode for a simple sequential calculation.

---

## 1. Explanation: What is Sequence?

In computer science, **sequence** is the specific order in which instructions are executed. A computer reads instructions from top to bottom, one line at a time. If you swap two lines in a sequence, the program may give an incorrect result or crash.

### Example: Calculating Total Price

```pseudocode
// Sequential pseudocode example
DECLARE Price, Quantity, Total : REAL
OUTPUT "Enter item price:"
INPUT Price
OUTPUT "Enter quantity:"
INPUT Quantity
Total <- Price * Quantity
OUTPUT "Total cost is: ", Total

```

---

## 2. Practice Activity (Trinket / Code)

1. Run and experiment with sequential statements in Python:

```python
# Python equivalent
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print("Total cost is:", total)

```

2. What happens if you move line 3 (`total = price * quantity`) above line 1? Try it in Trinket!

---

## 3. Portfolio Tasks (Submit to Teams)

> [!WARNING]
> Copy your answers into **Lesson 1** of your **Algorithm Design Portfolio** document in Teams.

1. **Definition:** Define the term *Sequence* in your own words.
2. **Algorithm Design:** Write pseudocode that:
* Prompts the user to enter a temperature in Celsius.
* Calculates the temperature in Fahrenheit using: Fahrenheit = (Celsius * 1.8) + 32.
Outputs the calculated temperature in Fahrenheit.


3. **Trace Check:** 

Complete a trace table for the given pseudocode using the test dataset: 4, 12, -3, 8, -1.

```pseudocode
01 DECLARE Num, Count, Total : INTEGER
02 Count ← 0
03 Total ← 0
04 REPEAT
05     INPUT Num
06     IF Num > 0 THEN
07         Total ← Total + Num
08         Count ← Count + 1
09     ENDIF
10 UNTIL Num < 0 OR Count = 5
11 OUTPUT Total, Count

```
**Trace table example** 

| Num | Count | Total | OUTPUT |
|-----|-------|-------|--------|
|     | 0     | 0     |        |
|  4  |       |       |        |
|     |       |       |        |

---

> [!CHALLENGE]
> **Extension 1: Validation & Error Handling**
> Modify your temperature program so that it checks if the entered temperature in Celsius is below absolute zero (`-273.15`). If it is, output `"Error: Invalid temperature"`.
>
> **Extension 2: Algorithmic Efficiency**
> Rewrite the pseudocode to process a batch of 5 temperature inputs in a loop and calculate the average temperature.

---

<!--
## Answers

> [!NOTE]
> Check your answers here after completing your portfolio draft!

1. **Sequence Definition:** The execution of statements one after another in the order they are written.
2. **Pseudocode Answer:**
```pseudocode
DECLARE Num1, Num2, Sum : REAL
OUTPUT "Enter first number:"
INPUT Num1
OUTPUT "Enter second number:"
INPUT Num2
Sum <- Num1 + Num2
OUTPUT "The sum is: ", Sum

```

3. **Trace Check Output:** 

| `Num` | `Count` | `Total` | `OUTPUT` |
| :---: | :---: | :---: | :---: |
| | 0 | 0 | |
| 4 | 1 | 4 | |
| 12 | 2 | 16 | |
| -3 | | | **16, 2** |

*(Explanation: When `-3` is input, `Num > 0` evaluates to FALSE, so `Total` and `Count` do not change. The loop terminates because `Num < 0` is TRUE, outputting `16` and `2`.)*
-->