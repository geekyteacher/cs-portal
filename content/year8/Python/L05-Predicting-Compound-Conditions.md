---
title: "Lesson 5: Predicting Compound Conditions"
description: Predict, explain, and test the results of Python conditions using and and or.
order: 5
draft: false
---

## Today you will

Work out what a compound condition does before running the program.

By the end, you should be able to:

- decide whether each part of a condition is `True` or `False`;
- explain how `and` and `or` combine those results; and
- predict the output for different values.

## Starter: predict the output

Do not run the code yet. Write down what you think it displays, then explain
why.

```python
age = 10
adult = "yes"

if age >= 12 or adult == "yes":
    print("Entry")
else:
    print("Denied")
```

Decide whether each comparison is true:

1. `age >= 12`
2. `adult == "yes"`
3. What is the result when those comparisons are joined with `or`?

## 1. Remember the rules

| Operator | The whole condition is `True` when... |
| --- | --- |
| `and` | Both conditions are `True`. |
| `or` | At least one condition is `True`. |

For example:

```python
has_ticket = True
old_enough = False

print(has_ticket and old_enough)
print(has_ticket or old_enough)
```

The first result is `False` because both parts are not true. The second is
`True` because at least one part is true.

## 2. Predict, explain, run

For each example:

1. Predict the output without running the code.
2. Write each comparison as `True` or `False`.
3. Explain how `and` or `or` combines the comparisons.
4. Run the program and check your prediction.

### Example A: both rules required

```python
age = 15
has_ticket = "yes"

if age >= 12 and has_ticket == "yes":
    print("Entry")
else:
    print("Denied")
```

### Example B: either rule is enough

```python
age = 10
with_adult = "no"

if age >= 12 or with_adult == "yes":
    print("Entry")
else:
    print("Denied")
```

### Example C: change one value

Change `with_adult` to `"yes"` in Example B. Predict the output before you
run it again. Which part of the condition changed from false to true?

## 3. Try different combinations

Complete the table before running the code:

| `age >= 12` | `with_adult == "yes"` | `and` result | `or` result |
| --- | --- | --- | --- |
| True | True |  |  |
| True | False |  |  |
| False | True |  |  |
| False | False |  |  |

Use the table to explain why an `and` rule can be stricter than an `or` rule.

## 4. Independent practice

Predict the message for each set of values. Show the truth value of both
comparisons.

```python
score = 72
bonus = "yes"

if score >= 80 and bonus == "yes":
    print("Gold")
elif score >= 60 or bonus == "yes":
    print("Silver")
else:
    print("Try again")
```

Test these value pairs:

1. `score = 72`, `bonus = "yes"`
2. `score = 85`, `bonus = "no"`
3. `score = 45`, `bonus = "no"`

## Exit check

1. When is a condition joined with `and` true?
2. When is a condition joined with `or` true?
3. What should you work out before deciding the result of a compound
   condition?

## Answers

### Starter

The output is `Entry`: the age check is false, but the adult check is true;
one true part is enough for `or`.

### Try different combinations

| First value | Second value | `and` result | `or` result |
| --- | --- | --- | --- |
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

### Independent practice

1. `Silver`: the first condition is false, but the `elif` condition is true.
2. `Silver`: the first condition is false, but `score >= 60` is true.
3. `Try again`: both conditions are false.

### Exit check

1. `and` is true only when both parts are true.
2. `or` is true when at least one part is true.
3. Work out whether each comparison is true or false first.
