---
title: Compound Conditions and Logic
description: Use Python's and and or operators to combine conditions and make decisions.
order: 4
draft: false
---
## Learning Objectives

By the end of this lesson you should be able to:

- Explain how the logical operators `and` and `or` work.
- Use `and` and `or` to combine conditions in an `if` statement.
- Predict whether a compound condition evaluates to `True` or `False`.

## Prior Knowledge

Before starting this lesson, you should be familiar with:

- `if`, `elif`, and `else` statements.
- Comparison operators such as `>=` and `==`.
- Conditions that evaluate to `True` or `False`.

## Quick Knowledge Check

Before starting, write down or discuss what you remember about `if`, `elif`,
and `else`. Try these without looking anything up:

1. What does an `if` statement do?
2. When would you use `elif` instead of `if`?
3. What happens when none of the `if` or `elif` conditions are true?
4. Trace the code when `score` is `72`. Then change the value to `45`, run it
   again, and explain why the output changes.

```python
score = 72

if score >= 80:
    print("High score")
elif score >= 60:
    print("Good score")
else:
    print("Keep practising")
```

Be ready to explain which condition is checked and why a particular branch
runs. In Python, “else if” is written as `elif`. You will build on this
knowledge by combining conditions in this lesson.

### Overview

So far, you have used `if`, `elif`, and `else` statements to make decisions
based on a single condition.

Real programs often need to check multiple conditions at the same time. For
example:

- A game might check whether a player is level 10 **and** owns a special item.
- A website might check whether a user entered the correct password **and**
  has permission to access a page.
- A cinema might allow entry if someone is old enough **or** accompanied by
  an adult.

Python uses the logical operators `and` and `or` to combine conditions.

### Keywords

| Keyword | Meaning |
| --- | --- |
| `and` | Both conditions must be true. |
| `or` | At least one condition must be true. |
| `True` | A condition is correct. |
| `False` | A condition is not correct. |
| Condition | A test that evaluates to `True` or `False`. |
| Compound condition | Multiple conditions joined together. |

### Using `and`

The `and` operator requires every condition to be true.

```python
age = 14
height = 150

if age >= 12 and height >= 140:
    print("Access Granted")
else:
    print("Access Denied")
```

The user must be 12 or older **and** at least 140 cm tall. If either check
fails, access is denied.

### Using `or`

The `or` operator requires at least one condition to be true.

```python
age = 10
with_adult = "yes"

if age >= 12 or with_adult == "yes":
    print("You may enter")
else:
    print("Entry denied")
```

Only one of the conditions needs to be true.

### Comparing `and` and `or`

| Condition | Result |
| --- | --- |
| `True and True` | `True` |
| `True and False` | `False` |
| `False and True` | `False` |
| `False and False` | `False` |

| Condition | Result |
| --- | --- |
| `True or True` | `True` |
| `True or False` | `True` |
| `False or True` | `True` |
| `False or False` | `False` |

### Worked Example: Theme Park Safety Check

```python
age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

if age >= 12 and height >= 140:
    print("Access Granted! Enjoy the ride!")
else:
    print("Sorry, you do not meet both safety rules.")
```

This program only grants access when both safety requirements have been met.

## Teacher Demonstration

Watch the demonstration first. Before each run, predict the output and explain
which conditions are true.

1. Run the `and` example with `age = 14` and `height = 150`. Both conditions
   are true, so access is granted.
2. Change `height` to `130` and run it again. One condition is false, so access
   is denied. Ask: what would happen if the age check failed instead?
3. Run the `or` example with `age = 10` and `with_adult = "yes"`. The adult
   condition is true, so entry is allowed.
4. Change `with_adult` to `"no"` and run it again. Both conditions are false,
   so entry is denied. Ask: what if the age was 12 instead?

As you demonstrate, trace each comparison as `True` or `False` before
explaining the result of the complete condition. Then let students try a
similar change themselves.

## Practice

If you would like a printed version of the coding scaffolds, use the
[Compound Conditions scaffold worksheet](/downloads/year8-compound-conditions-scaffold.html).
You can also copy a starter below into your Python editor and fill in the gaps.

### Bronze Challenge: Concert Gatekeeper

Write a program that:

1. Asks for a person's age.
2. Asks whether they have a ticket (`yes` or `no`).
3. Uses `and` to check whether they are 18 or older **and** have a ticket.
4. Displays an appropriate message.

Example:

```text
Age: 20
Ticket: yes

Entry Granted
```

Start with this scaffold. Fill in the age limit and the ticket check:

```python
age = int(input("Age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()

if age >= _____ and has_ticket == "_____":
    print("Entry Granted")
else:
    print("Entry Denied")
```

### Silver Challenge: Cinema Special Pass

Write a program that asks for the user's age and whether they are with an
adult. Use `or` to decide whether they can enter.

A customer can enter if they are 12 or older **or** accompanied by an adult.

Example:

```text
Age: 10
With adult? yes

Entry Granted
```

Complete the condition with the operator that allows either requirement to be
true:

```python
age = int(input("Age: "))
with_adult = input("Are you with an adult? (yes/no): ").strip().lower()

if age >= 12 _____ with_adult == "yes":
    print("Entry Granted")
else:
    print("Entry Denied")
```

### Gold Challenge: Secure Vault System

Create a program that asks for a username, password, and security level.

The system should only allow access when:

- The username is `"admin"`.
- The password is `"secret123"`.
- The security level is greater than 5.

Use `and` to check that all three requirements are met.

Fill in the missing values to complete the three checks:

```python
username = input("Username: ")
password = input("Password: ")
security_level = int(input("Security level: "))

if username == "_____" and password == "_____" and security_level > _____:
    print("Access Granted")
else:
    print("Access Denied")
```

Example:

```text
Username: admin
Password: secret123
Security level: 8

Access Granted
```

## Challenge

Create a login system that uses both `and` and `or`.

The username and password must be correct, and the user must have either an
Admin account or a VIP account.

For example, store the checks in variables and group the account options with
parentheses:

```python
username_correct = True
password_correct = True
is_admin = False
is_vip = True

if username_correct and password_correct and (is_admin or is_vip):
    print("Access granted")
else:
    print("Access denied")
```

Can you make the program display different messages depending on why access
was denied?

## Summary

You should now be able to:

- Use `and` to combine conditions that must all be true.
- Use `or` when at least one condition must be true.
- Create compound conditions in `if` statements.
- Build programs that make more realistic decisions.
