---
title: "Lesson 6: Debugging Conditions"
description: Find and correct common syntax and logic errors in Python conditions.
order: 6
draft: false
---

## Today you will

Find errors in decision-making code and explain how you fixed them.

By the end, you should be able to:

- spot common mistakes in comparison operators;
- distinguish assignment `=` from comparison `==`; and
- test a corrected condition with suitable values.

## Starter: spot the problem

Each code example has an error. For each one, write:

1. the line containing the problem;
2. what Python needs instead; and
3. a value you could test after fixing it.

## 1. Mistake: the comparison symbol

```python
age = 15

if age => 12:
    print("Entry")
```

Python uses `>=` for “greater than or equal to”. The order of the symbols
matters.

Correct version:

```python
age = 15

if age >= 12:
    print("Entry")
```

## 2. Mistake: assignment instead of comparison

```python
code = "blue"

if code = "blue":
    print("Access")
```

Use one equals sign `=` to assign a value to a variable. Use two equals
signs `==` to compare two values.

Correct version:

```python
code = "blue"

if code == "blue":
    print("Access")
```

## 3. Mistake: an unfinished compound condition

```python
age = 15

if age >= 12 and:
    print("Entry")
```

`and` needs a condition on both sides. Decide what second rule is required,
then complete the comparison:

```python
age = 15
has_ticket = "yes"

if age >= 12 and has_ticket == "yes":
    print("Entry")
```

## 4. Mistake: a condition that is too broad

This code runs without a syntax error, but does not give the intended
outcome:

```python
score = 85

if score >= 60:
    print("Good")
elif score >= 80:
    print("Excellent")
else:
    print("Keep practising")
```

The first condition is already true for a score of 85, so Python never
checks the `elif`. Put the higher threshold first:

```python
score = 85

if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Keep practising")
```

## 5. Debugging routine

Work through the four examples with a partner:

1. Find the error.
2. Correct the code.
3. Predict the result.
4. Run it and test one value that should pass and one that should not.
5. Explain whether it was a syntax error or a logic error.

### A

```python
if age => 12:
    print("Entry")
```

### B

```python
password = "maple"

if password = "maple":
    print("Match")
```

### C

```python
if age >= 12 and:
    print("Entry")
```

### D

```python
score = 92

if score >= 50:
    print("Pass")
elif score >= 80:
    print("Excellent")
```

## Exit check

1. What is the difference between `=` and `==`?
2. Is an incorrectly ordered `if`/`elif` always a syntax error?
3. Why should you test after fixing code?

## Answers

### Debugging routine

A. Change `=>` to `>=`.
B. Change `=` to `==` in the condition.
C. Add a complete comparison after `and`, for example
   `and has_ticket == "yes"`.
D. Check `score >= 80` before `score >= 50`.

### Exit check

1. A syntax error prevents Python from running the program; a logic error
   lets it run but produces the wrong result.
2. No. The code can run but give the wrong outcome.
3. Testing checks that the correction works for more than one case.
