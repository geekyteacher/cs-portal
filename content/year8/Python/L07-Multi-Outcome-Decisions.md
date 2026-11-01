---
title: "Lesson 7: Multi-Outcome Decisions"
description: Use if, elif, and else in the right order to select between several outcomes.
order: 7
draft: false
---

## Today you will

Use `elif` to give a program more than two possible outcomes.

By the end, you should be able to:

- explain how Python checks an `if`/`elif`/`else` structure;
- order numeric conditions from highest threshold to lowest; and
- test values at the score boundaries.

## Starter

Predict the result for a score of 85. Which condition does Python check
first?

```python
score = 85

if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Keep Improving")
```

## 1. How `elif` works

Python checks conditions from top to bottom:

1. It checks the `if` condition.
2. If that is false, it checks the first `elif`.
3. It continues until it finds a true condition.
4. It runs that block and skips the remaining choices.
5. If no condition is true, it runs `else`.

In the starter, a score of 85 matches `score >= 80`, so the output is
`Excellent`.

## 2. Why order matters

Try swapping the two conditions:

```python
if score >= 60:
    print("Good")
elif score >= 80:
    print("Excellent")
```

This still runs, but a score of 85 matches the first condition and never
reaches `Excellent`. For descending score bands, check the highest
threshold first.

## 3. Run and test

Run the working example with these scores:

| Score | Expected outcome |
| ---: | --- |
| 59 | Keep Improving |
| 60 | Good |
| 79 | Good |
| 80 | Excellent |

Then extend the program so it asks the user for a score:

```python
score = int(input("Enter your score: "))

if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Keep Improving")
```

## 4. Make a reward checker

Write a program that asks for a game score and displays:

- `Gold reward` for 100 or more;
- `Silver reward` for 70 or more;
- `Bronze reward` for 40 or more; or
- `Try again` for scores below 40.

Test `39`, `40`, `69`, `70`, `99`, and `100`.

**Finished early?** Add a name input and include the name in each message.

## Exit check

1. What happens when an `elif` condition is true?
2. Why should the highest threshold come first?
3. Which values should be tested around a threshold of 70?

## Answers

### Starter

The output is `Excellent`.

### Run and test

The expected outcomes are `Keep Improving`, `Good`, `Good`, and `Excellent`.

### Exit check

1. It runs that block and skips the remaining branches.
2. Otherwise, a high score can match a lower threshold first.
3. Test 69, 70, and 71.
