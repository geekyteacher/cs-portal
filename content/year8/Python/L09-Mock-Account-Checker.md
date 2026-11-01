---
title: "Lesson 9: Mock Account Checker — Plan and Build"
description: Use compound conditions to model a simple fictional account check.
order: 9
draft: false
---

## Today you will

Plan and build a small program that checks fictional account details using
`and`.

By the end, you should be able to:

- identify the inputs and checks a program needs;
- require multiple checks to be true using `and`; and
- test a program with both matching and non-matching details.

## Important: classroom simulation only

This is a simple programming exercise, **not real authentication**. The
fictional names and passcodes are visible in the source code, so this kind
of program is not secure. Do not use a real username, password, or personal
information in your program.

## Starter: trace the checks

Predict the output. Is each comparison true or false?

```python
username = "student"
passcode = "blue7"

if username == "student" and passcode == "blue7":
    print("Mock access granted")
else:
    print("Mock access denied")
```

## 1. Plan the account check

The classroom simulation will:

1. ask for a fictional username;
2. ask for a fictional passcode;
3. compare both answers with the sample values; and
4. display a mock result.

Both comparisons must be true. If either is false, the compound `and`
condition is false.

## 2. Build the basic version

Use only the fictional sample values shown below:

```python
username = input("Fictional username: ").strip()
passcode = input("Fictional passcode: ").strip()

if username == "student" and passcode == "blue7":
    print("Mock access granted")
else:
    print("Mock access denied")
```

Try the matching pair, then change one answer at a time. Predict the result
before each run.

## 3. Explain the result

Complete the table:

| Username matches? | Passcode matches? | Whole `and` condition |
| --- | --- | --- |
| True | True |  |
| True | False |  |
| False | True |  |
| False | False |  |

Why should a correct username with an incorrect passcode be denied?

## 4. Test your check

Run the program with these fictional inputs and record the result:

| Username | Passcode | Expected message |
| --- | --- | --- |
| `student` | `blue7` |  |
| `student` | `wrong` |  |
| `visitor` | `blue7` |  |

Change one value at a time. Explain which comparison changes and why the
whole `and` condition becomes false.

## Exit check

1. Why does the account check use `and`?
2. What happens if only one comparison is true?
3. Why must you use fictional details only?

## Answers

### Starter

The output is `Mock access granted`; both comparisons are true.

### Explain the result

The whole `and` condition is true only in the first row. The other three
combinations produce false.

### Test your check

The expected messages are `Mock access granted`, `Mock access denied`, and
`Mock access denied`.

### Exit check

1. Both comparisons must be true for both details to match.
2. The whole condition is false and the denial branch runs.
3. The program stores expected values in visible source code, so it should
   not be used to protect real accounts or data.
