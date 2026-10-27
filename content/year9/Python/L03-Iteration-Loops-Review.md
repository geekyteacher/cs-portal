---
title: "Python Iteration: Loops Review"
description: Refresh your knowledge of for and while loops, debug common errors, and practise using loops in Python.
order: 3
draft: false
---
## Learning Objectives

By the end of this lesson you should be able to:

- Explain when to use a `for` loop and a `while` loop.
- Trace a loop and predict how many times it runs.
- Find and fix common loop errors.
- Use loops to repeat instructions in a small Python program.

## Prior Knowledge

Before starting this lesson, you should know how to:

- Use `print()` and variables in Python.
- Write a basic `if` statement.
- Use `range()` and lists.

## Quick Knowledge Check

Try these without running the code first:

1. How many times does this loop print `Hello`? What values does `i` take?

   ```python
   for i in range(3):
       print("Hello", i)
   ```

2. What line needs to be added to make this `while` loop stop?

   ```python
   x = 1
   while x < 5:
       print(x)
   ```

3. In your own words, what is one difference between a `for` loop and a
   `while` loop?

## Learn

### Choosing a loop

A `for` loop goes through each item in a sequence, such as a list or a string.
`range()` is commonly used when you want to repeat instructions a set number
of times.

A `while` loop repeats **while its condition is true**. Use it when you want
repetition to continue until something changes, such as a correct password
being entered.

### Worked examples

Use `range(3)` to repeat an instruction three times:

```python
for i in range(3):
    print("Hello", i)
```

The values of `i` are `0`, `1`, and `2`, so the loop runs three times.

A `while` loop needs something inside the loop to eventually make its
condition false:

```python
x = 1

while x < 5:
    print(x)
    x = x + 1
```

Here, `x` increases on every turn. When it reaches `5`, `x < 5` is false and
the loop stops.

## Teacher Demonstration

Before running each example, ask students to predict what will happen.

1. Run the `for` loop with `range(3)`. Trace `i` as `0`, `1`, and `2`, and
   count the three repetitions.
2. Show the loop error in Task 1. Ask students what Python expects at the end
   of the `for` line, then add the missing colon and run it.
3. Show the `while` loop in Task 2. Ask what is changing each time around the
   loop. Add `x = x + 1`, then run it and explain why it stops.
4. Run the password example in the Gold task. Demonstrate one incorrect
   password followed by the correct password, and trace how the value of
   `password` changes.

## Practice

### Task 1: Fix the Broken Code

Fix each example and run it in Thonny.

#### Bug A: Missing colon

```python
for i in range(3)
    print("Hello")
```

Add the missing punctuation to the `for` line.

#### Bug B: The infinite loop

```python
x = 1
while x < 5:
    print(x)
```

Add a line inside the loop so that `x` increases each time. Check that the
loop prints `1` to `4` and then stops.

### Task 2: Choose Your Challenge

#### Bronze: The 10-Times Table

Write a `for` loop using `range()` that prints the 10 times table from
`1 x 10 = 10` up to `10 x 10 = 100`.

Your output should follow this pattern:

```text
1 x 10 = 10
2 x 10 = 20
...
10 x 10 = 100
```

#### Silver: Loop Through a Quiz

Use this short quiz question list, or replace it with the questions from your
previous quiz project:

```python
questions = [
    "What does CPU stand for?",
    "How many bits are in a byte?",
    "What does RAM stand for?",
]
```

Write a `for` loop that displays each question exactly once. Your program
should work for the whole list without writing a separate `print()` for each
question. If you finish, ask the user to enter an answer after each question.

#### Gold: The Password Gatekeeper

Write a `while` loop that keeps asking the user to enter a password until they
type `"python9"`. Start by assigning an initial value to `password`, then
update it inside the loop so the condition can eventually become false.
Display `"Access Granted!"` after the loop ends.

Use this starter if helpful:

```python
password = ""

while password != "python9":
    password = input("Enter the password: ")

print("Access Granted!")
```

Finished early? Add an `attempts` counter so the program tells the user how
many guesses they made.

## Summary

You should now be able to:

- Use a `for` loop to go through a sequence or repeat instructions using
  `range()`.
- Use a `while` loop to repeat while a condition remains true.
- Update values inside a loop so it can finish.
- Trace and debug simple loops.
