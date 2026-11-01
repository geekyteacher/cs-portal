---
title: "Lesson 11: End-of-Unit Decision Project"
description: Independently design, code, test, and explain a Python decision program.
order: 11
draft: false
---

## Today you will

Independently create a small decision-making program that follows a set of
rules.

## Choose one project

Choose **one** option. Use the rule table as written, and do not add extra
features until your required program works.

### Option 1: School club access

Ask for an age and whether the student has permission.

| Rule | Outcome |
| --- | --- |
| Age is under 11 | Display `Ask about the junior club` |
| Age is 11 or older and permission is `"yes"` | Display `Club entry approved` |
| Any other case | Display `Ask a teacher` |

### Option 2: Cinema ticket system

Ask for age and whether the person has a ticket.

| Rule | Outcome |
| --- | --- |
| Age is under 12 | Display `Child ticket` |
| Age is 12 or older and has a ticket | Display `Entry approved` |
| Any other case | Display `Ticket required` |

### Option 3: Theme park entry

Ask for age, height in centimetres, and whether an adult is present.

| Rule | Outcome |
| --- | --- |
| Height is under 120 cm | Display `Choose another ride` |
| Height is at least 120 cm and (age is at least 12 or an adult is present) | Display `Entry approved` |
| Any other case | Display `Ask an adult` |

### Option 4: Game achievement checker

Ask for a score and whether the player completed the bonus challenge.

| Rule | Outcome |
| --- | --- |
| Score is at least 100 and bonus is `"yes"` | Display `Master achievement` |
| Score is at least 70 or bonus is `"yes"` | Display `Achievement unlocked` |
| Any other case | Display `Keep playing` |

## Plan before coding

Complete this plan:

| Planning question | My answer |
| --- | --- |
| Which option did I choose? |  |
| What information must the user enter? |  |
| Which inputs must be converted to integers? |  |
| What conditions will I check, in order? |  |
| What should each outcome display? |  |
| Which boundary values will I test? |  |

## Build your program

Use a structure like this, adapting the variable names, conditions, and
messages to your chosen project:

```python
value = int(input("Enter a number: "))
choice = input("Enter yes or no: ").strip().lower()

if first_condition:
    print("First outcome")
elif second_condition:
    print("Second outcome")
else:
    print("Other outcome")
```

Your program must use:

- input stored in variables;
- integer conversion for numeric input;
- at least one compound condition using `and` or `or`;
- `if`, `elif`, and `else`; and
- clear messages for every outcome.

## Test your program

Test each outcome and include values at important boundaries. For example,
if a rule changes at age 12, test 11, 12, and 13.

| Test input(s) | Expected outcome | Actual outcome | Passed? |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

If a test fails, fix the code and repeat the test.

## Submit and explain

Save your program using your teacher's instructions. Be ready to explain:

1. what each input represents;
2. what your compound condition checks;
3. why your conditions are in that order; and
4. one change you made after testing.

## Success criteria

- [ ] My program uses input and variables.
- [ ] Numeric values are converted with `int()`.
- [ ] My program uses a compound condition.
- [ ] My program uses `if`, `elif`, and `else`.
- [ ] Every outcome in the rule table is handled.
- [ ] I tested boundary values and more than one outcome.
- [ ] I can explain how my program makes its decision.

**Finished early?** Add a second test case or improve the output messages.
Only add another feature after all the success criteria are met.
