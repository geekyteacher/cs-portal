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
* Asks the user to enter two numbers.
* Adds the two numbers together.
* Displays the result to the screen.


3. **Trace Check:** What is the output of the following sequence if the user inputs `10` then `5`?

```pseudocode
INPUT A
INPUT B
A <- A + 5
B <- B * 2
OUTPUT A + B

```

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

3. **Trace Check Output:** `25` (Calculation: $A = 10 + 5 = 15$, $B = 5 \times 2 = 10$, Output $15 + 10 = 25$).
-->