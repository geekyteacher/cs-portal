---
title: "04 - Comparing Numbers"
description: Use Python comparison operators to make decisions at important values.
order: 6
draft: false
---

## Today you will

Use numeric comparisons to decide whether values are above, below, or equal
to a boundary.

By the end, you should be able to:

- use `>`, `<`, `>=`, and `<=`;
- explain how `==` compares two values; and
- test a program with values around a boundary.

## Quick check

1. What does `int()` do to the text entered by a user?
2. What does `age >= 13` check?
3. Is age 13 greater than or equal to 13?

## 1. Comparison operators

| Operator | Meaning | Example |
| --- | --- | --- |
| `>` | greater than | `score > 10` |
| `<` | less than | `score < 10` |
| `>=` | greater than or equal to | `age >= 13` |
| `<=` | less than or equal to | `age <= 17` |
| `==` | equal to | `age == 13` |

A comparison is either **True** or **False**. Python uses that result to
decide which instructions to run.

## 2. Watch and predict

For each age, decide whether the message will be displayed:

```python
age = int(input("Age: "))

if age >= 13:
    print("You can join.")
```

Try `12`, `13`, and `14`. The value equal to the boundary is important:
`13 >= 13` is true, while `12 >= 13` is false.

## 3. Run it together

Change the condition to `age > 13` and try `13` again. The `>` operator
means strictly greater than, so age 13 does not pass this test.

Now try a maximum-age check:

```python
age = int(input("Age: "))

if age <= 17:
    print("This group is for ages up to 17.")
```

Test `17` and `18`. `<=` includes the boundary value.

## 4. Practice

For each condition, write whether it is True or False:

1. `12 < 13`
2. `13 < 13`
3. `13 <= 13`
4. `18 > 17`
5. `17 >= 17`

Then write a program that asks for a score and displays `Pass` if the score
is 50 or more. Test it with `49`, `50`, and `51`.

## Exit check

1. Which operator means strictly greater than?
2. What is the difference between `>` and `>=`?
3. What three values should you test around a threshold of 20?

## Answers

### Quick check

1. It converts a whole-number string to an integer.
2. It checks whether age is at least 13.
3. Yes.

### Practice

4. True
5. False
6. True
7. True
8. True

### Exit check

9. `>`
10. `>=` includes a value equal to the boundary; `>` does not.
11. Test 19, 20, and 21.
