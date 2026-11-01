---
title: "05 - More Than Two Outcomes"
description: Use if, elif, and else to select between several number-based outcomes.
order: 7
draft: false
---

## Today you will

Use `elif` to make a program choose between more than two outcomes.

By the end, you should be able to:

- describe how Python checks an `if`/`elif`/`else` structure;
- put number conditions in an order that works; and
- write a simple score-band checker.

## Quick check

1. Which operator means less than or equal to?
2. Is `17 >= 17` True or False?
3. What does `int(input("Score: "))` allow the program to do?

## 1. Add another choice

An `if`/`else` structure gives two possible routes. Add `elif` when there
are more conditions to check:

```python
score = int(input("Score: "))

if score >= 80:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Keep practising")
```

Python checks the conditions from top to bottom. It runs the instructions
under the **first true condition**, then skips the remaining choices. If
none of the conditions is true, it runs `else`.

## 2. Why order matters

In the example, `score >= 80` must be checked first. If `score >= 50` came
first, a score of 90 would already match that condition and would never
reach `Excellent`.

For descending score bands, check the highest threshold first.

## 3. Run and test

Run the example with `45`, `72`, and `85`. Then test the boundaries `49`,
`50`, `79`, and `80`.

For a score of 80, the first condition is true, so the result is
`Excellent`. For a score of 65, the first condition is false but the second
is true, so the result is `Pass`.

## 4. Make a score checker

Write a program that asks for a score and displays:

- `Gold` for 90 or more;
- `Silver` for 70 or more but less than 90;
- `Bronze` for 50 or more but less than 70; or
- `Try again` for scores below 50.

Use `if`, `elif`, and `else`. Test 49, 50, 69, 70, 89, and 90.

## Exit check

1. How does Python choose which `elif` block to run?
2. Why should the highest threshold be checked first in the example?
3. What runs if every `if` and `elif` condition is false?

## Answers

### Quick check

1. `<=`
2. True
3. It converts the entered score to an integer so it can be compared.

### Exit check

4. Python checks conditions in order and runs the first block whose
   condition is true.
5. Otherwise, a high score could match a lower threshold first.
6. The `else` block.
