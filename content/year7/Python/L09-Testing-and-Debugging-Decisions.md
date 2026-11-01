---
title: "07 - Testing and Debugging Decisions"
description: Test decision programs at boundaries and fix errors in their conditions.
order: 9
draft: false
---

## Today you will

Use test data to check that a decision program follows its rules, then
correct a condition that causes the wrong outcome.

By the end, you should be able to:

- choose normal and boundary test values;
- trace an `if`/`elif`/`else` structure; and
- explain how the order of conditions affects the result.

## Quick check

1. What ticket should a 5-year-old receive in the cinema program?
2. What does an `else` block do?
3. Why should you test the ages immediately either side of a boundary?

## 1. Test the boundaries

For the cinema rules, the important boundaries are 5, 18, and 65. Test the
values immediately below, at, and immediately above each one:

| Boundary | Test values |
| --- | --- |
| 5 | 4, 5, 6 |
| 18 | 17, 18, 19 |
| 65 | 64, 65, 66 |

These tests help reveal mistakes such as using `< 5` when the rule should
include age 5, or putting a broad condition before a more specific one.

## 2. Find the bug

This program is meant to use the cinema ticket rules, but one condition is
wrong:

```python
age = int(input("Age: "))

if age < 5:
    print("Free ticket")
elif age >= 5:
    print("Child ticket")
elif age >= 18:
    print("Adult ticket")
else:
    print("Senior ticket")
```

1. Predict the result for ages 4, 18, and 65.
2. Explain why the adult and senior messages are never reached for valid
   ages of 18 or more.
3. Correct the conditions so the program follows the rule table from the
   previous lesson.

## 3. Debug and retest

Replace the faulty conditions with the working cinema structure from
[Cinema Ticket Adviser](/year7/python/l08-cinema-ticket-adviser). Retest all six
boundary ages: `4`, `5`, `17`, `18`, `64`, and `65`.

For each test, record:

| Input age | Expected ticket | Actual ticket | Pass or fix needed? |
| ---: | --- | --- | --- |
| 4 | Free |  |  |
| 5 | Child |  |  |
| 17 | Child |  |  |
| 18 | Adult |  |  |
| 64 | Adult |  |  |
| 65 | Senior |  |  |

## 4. Try another bug

The club accepts students aged 13 and over. A student aged exactly 13 is
rejected by this condition:

```python
if age > 13:
    print("You can join.")
```

Change the operator so age 13 is accepted. Test ages 12, 13, and 14.

## Exit check

1. What is a boundary test?
2. Which condition in the faulty program catches every age of 5 or more?
3. Which operator accepts a value equal to a minimum age?

## Answers

### Quick check

1. A 5-year-old receives a child ticket.
2. It runs when all preceding conditions are false.
3. They check values around the boundary to find errors in the condition.

### Find the bug

4. Age 4 receives a free ticket; ages 18 and 65 receive a child ticket.
   The condition `age >= 5` is true for those ages, so its block runs and
   the later conditions are skipped.
5. Use the ordered tests `age < 5`, `age <= 17`, `age <= 64`, then `else`.
6. Use `age >= 13` so age 13 is accepted.

### Exit check

7. Test values just below, equal to, and just above a rule boundary.
8. The `elif age >= 5` condition.
9. `>=`
