---
title: "03 - Numbers as Input"
description: Use integer input to make a program respond to a person's age.
order: 5
draft: false
---

## Today you will

Turn typed input into a number so Python can compare it.

By the end, you should be able to:

- explain why `input()` needs converting before a numeric comparison;
- use `int()` to convert a whole-number answer; and
- write an `if` statement that checks an age.

## Quick check

1. What does `input()` let a user do?
2. Which symbol checks whether two values are equal?
3. Is the answer from `input()` a number or text?

## 1. Predict

Read this code. What do you think it will display if the user enters `14`?

```python
age = int(input("Age: "))

if age >= 13:
    print("You can join the club.")
```

## 2. Run it together

Run the program and enter `14`. Run it again and enter `11`.

`input()` receives what the user types as **text**. The `int()` function
converts that text into a whole number. The program can then compare `age`
with the number `13`.

```python
age = int(input("Age: "))
```

The condition `age >= 13` is true when the age is 13 or more. If it is true,
Python runs the indented line.

## 3. Change the condition

Change the program so that it checks whether the person is under 13:

```python
age = int(input("Age: "))

if age < 13:
    print("Ask an adult before joining.")
```

Test it with `12` and `13`. Notice what happens at the boundary.

## 4. Try it independently

Write a program that asks for a person's age. If the person is 16 or older,
display `You can apply.` Otherwise, display nothing for now.

Test with one age below 16 and one age equal to 16.

> [!NOTE]
>
> Enter a whole number such as `12`. This lesson does not yet handle words
> or decimal numbers entered by mistake.

## Exit check

1. What does `int()` do?
2. Why would `age = input("Age: ")` not be enough for a numeric comparison?
3. What does `age >= 13` mean?

## Answers

### Quick check

1. It lets the user type an answer; Python receives that answer as text.
2. `==`
3. Text. Convert it with `int()` before comparing it as a whole number.

### Exit check

4. `int()` converts a whole-number string to an integer.
5. `input()` returns text, so convert it to an integer before comparing it
   with a number.
6. It checks whether age is greater than or equal to 13.
