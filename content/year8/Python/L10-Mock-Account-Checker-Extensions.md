---
title: "Lesson 10: Mock Account Checker — More Outcomes"
description: Extend a fictional account-checking program with roles and clear outcomes.
order: 10
draft: false
---

## Today you will

Extend a mock account checker so that different fictional account types
receive different messages.

By the end, you should be able to:

- combine `and` and `or` with parentheses;
- use `if`, `elif`, and `else` for several outcomes; and
- test that each outcome can be reached.

## Safety reminder

This activity is a **fictional logic simulation**, not real authentication.
Do not enter, store, or share real usernames, passwords, or personal
information. The sample account values are deliberately visible in the
code.

## Starter

Read this code and predict the result:

```python
account_type = "student"
has_pass = True

if has_pass and account_type == "teacher":
    print("Teacher area")
elif has_pass and account_type == "student":
    print("Student area")
else:
    print("No demo access")
```

Which branch runs? What changes if `has_pass` becomes `False`?

## 1. Combine conditions

Parentheses make it clear which options belong together:

```python
has_pass = True
account_type = "student"

if has_pass and (account_type == "teacher" or account_type == "student"):
    print("Recognised demo account")
else:
    print("Unrecognised demo account")
```

The program requires `has_pass` to be true and the account type to match
either allowed label. The parentheses group the two alternatives.

## 2. Add multiple outcomes

Use `elif` to choose a different message for each role:

```python
has_pass = True
account_type = "student"

if has_pass and account_type == "teacher":
    print("Teacher demo area")
elif has_pass and account_type == "student":
    print("Student demo area")
else:
    print("No demo access")
```

The first matching branch runs. If the first condition is false, Python
checks the next `elif`; if neither is true, it runs `else`.

## 3. Test every outcome

Change the values and predict the message before you run the program:

| `has_pass` | `account_type` | Expected message |
| --- | --- | --- |
| `True` | `"teacher"` |  |
| `True` | `"student"` |  |
| `False` | `"student"` |  |
| `True` | `"visitor"` |  |

## 4. Improve the mock program

Create your own fictional role-checking example. It must:

- use made-up role labels such as `"reader"` and `"editor"`;
- use a Boolean variable such as `has_pass`;
- include a compound condition;
- use `if`, `elif`, and `else`; and
- display a different message for each role and for a rejected case.

Keep the sample values in code. Do not turn this classroom model into a
real login system.

## Exit check

1. What do parentheses show in a compound condition?
2. Which branch runs if every condition is false?
3. How will you test that a role is rejected?

## Answers

### Starter

1. The teacher branch displays `Teacher area`.
2. With `has_pass = False`, the `else` branch displays `No demo access`.

### Test every outcome

The outcomes, in row order, are `Teacher demo area`, `Student demo area`,
`No demo access`, and `No demo access`.

### Exit check

1. Parentheses group the role alternatives so either role can match, while
   `has_pass` must also be true.
2. The `else` branch.
3. Use a value that does not match either allowed role, or set `has_pass`
   to `False`.
