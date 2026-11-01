---
title: "08 - Decision Program Project: Plan and Start"
description: Plan an independent Python program that uses numeric input and selection.
order: 10
draft: false
---

## Today you will

Plan and begin an independent program that uses number comparisons to make
a useful decision.

By the end, you should be able to:

- choose a brief and identify its inputs, rules, and outputs;
- write a rule table before coding; and
- start a program using `int()`, `if`, `elif`, and `else`.

## Quick check

1. What should you test around a boundary of 18?
2. What does `elif` let your program do?
3. What does `int()` do to a whole-number answer from `input()`?

## 1. Choose a project brief

Choose **one** brief. Use the rules as written; do not add extra features
until the basic program works.

### A. Event ticket adviser

Ask for the visitor's age and display the correct ticket group.

| Age | Ticket group |
| --- | --- |
| Under 5 | Free |
| 5 to 17 | Child |
| 18 to 64 | Adult |
| 65 or older | Senior |

### B. School club adviser

Ask for the student's age and recommend the suitable club group.

| Age | Recommendation |
| --- | --- |
| Under 11 | Junior club |
| 11 to 13 | Intermediate club |
| 14 to 16 | Senior club |
| 17 or older | Ask the teacher about other opportunities |

### C. Score checker

Ask for a score out of 100 and display the result.

| Score | Result |
| --- | --- |
| 80 or more | Excellent |
| 60 to 79 | Secure |
| 40 to 59 | Developing |
| Below 40 | Keep practising |

## 2. Plan your program

Before coding, complete these notes:

| Planning question | My answer |
| --- | --- |
| Which brief did I choose? |  |
| What number will the user enter? |  |
| What variable will store it? |  |
| What are the outcomes, in order? |  |
| What are the boundary values I must test? |  |

Write the rules in order from the first condition to the final `else`.
Decide which condition must be checked first so that a value does not match
the wrong outcome.

## 3. Start coding

Use this structure, replacing the comments with your own prompt, conditions,
and messages:

```python
value = int(input("Enter a number: "))

if first_condition:
    print("First outcome")
elif second_condition:
    print("Second outcome")
elif third_condition:
    print("Third outcome")
else:
    print("Final outcome")
```

Run your code after adding each condition. Keep the indentation consistent:
each `print()` belongs inside the condition immediately above it.

## 4. Save your progress

Before the end of the lesson:

- save your program with a clear filename;
- make sure it runs without a syntax error;
- test at least one value for two different outcomes; and
- write down the boundary values you still need to test next lesson.

**Finished early?** Add a friendly message, but do not change the required
rules.

## Exit check

1. Why write a rule table before coding?
2. What must be converted before a number can be compared?
3. What should your `else` represent?

## Answers

1. Test the value below 18, 18, and the value above 18.
2. It checks another condition if the earlier conditions were false.
3. It converts the entered text to a whole number.
4. A rule table makes the outcomes and boundaries clear before writing
   conditions.
5. Use `int()` to convert the entered text.
6. The remaining outcome after every earlier condition has been checked.
