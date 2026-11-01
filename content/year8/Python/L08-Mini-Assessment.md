---
title: "Lesson 8: Decision-Making Mini Assessment"
description: Show what you know about predicting, debugging, and writing Python decisions.
order: 8
draft: false
---

## Today you will

Show that you can predict, debug, and write simple programs using
comparisons, compound conditions, and `elif`.

## Assessment instructions

Work independently. Do not run code until you have answered the prediction
questions. For the coding task, test your program after you have written it.

## Part A: Predict the output

For each question, write the output and briefly explain which conditions
are true.

### 1

```python
age = 10
with_adult = "yes"

if age >= 12 or with_adult == "yes":
    print("Entry")
else:
    print("Denied")
```

### 2

```python
score = 85

if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Keep practising")
```

## Part B: Find and fix the errors

Rewrite each example so it runs and checks the intended condition.

### 3

```python
age = 15
if age => 12:
    print("Entry")
```

### 4

```python
ticket = "yes"
if ticket = "yes":
    print("Ready")
```

## Part C: Write conditions

### 5

Write one Python condition that is true when `age` is at least 13 **and**
`has_permission` is `"yes"`.

### 6

Write an `if`/`elif`/`else` structure that displays `High` for a score of
80 or more, `Pass` for a score of 50 or more, and `Try again` otherwise.

## Part D: Coding task — ticket checker

Create a small program that asks for a person's age and whether they have a
ticket. Use this rule:

> Entry is allowed if the person is 12 or older **and** has a ticket.

Your program must:

- store both answers in variables;
- convert the age to an integer;
- use a compound condition with `and`;
- display `Entry allowed` or `Entry denied`; and
- run and test both an allowed and a denied case.

When your teacher asks, show your code and explain what each part of the
condition checks.

## Mark check

Before handing in, check:

- [ ] I predicted both outputs.
- [ ] I corrected the comparison symbols.
- [ ] I wrote conditions using `and` or `or`.
- [ ] My ticket checker uses input, variables, and `and`.
- [ ] I tested more than one set of inputs.

## Answers

1. `Entry`: the age condition is false, but the adult condition is true.
2. `Excellent`
3. Change `=>` to `>=`.
4. Change `=` to `==` in the condition.
5. `if age >= 13 and has_permission == "yes":`
6. For example:

   ```python
   if score >= 80:
       print("High")
   elif score >= 50:
       print("Pass")
   else:
       print("Try again")
   ```

7. Example:

   ```python
   age = int(input("Age: "))
   has_ticket = input("Do you have a ticket? yes/no: ").strip().lower()

   if age >= 12 and has_ticket == "yes":
       print("Entry allowed")
   else:
       print("Entry denied")
   ```
