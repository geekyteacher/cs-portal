---
title: "06 - Cinema Ticket Adviser"
description: Build a guided program that chooses a cinema ticket category from a person's age.
order: 8
draft: false
---

## Today you will

Combine input, integer conversion, variables, and several decisions in one
useful program.

By the end, you should be able to:

- turn a set of age rules into an `if`/`elif`/`else` structure;
- choose an appropriate order for the conditions; and
- test each ticket category.

## Quick check

1. Which comes first when checking descending score bands: `score >= 50` or
   `score >= 80`?
2. What does `elif` do?
3. Which operator includes the boundary value?

## 1. Plan before coding

The cinema uses these ticket rules:

| Age | Ticket |
| --- | --- |
| Under 5 | Free |
| 5 to 17 | Child |
| 18 to 64 | Adult |
| 65 or older | Senior |

Assume the user enters a valid whole-number age. Read the rules from the
youngest group upwards. After a condition is false, the next condition only
needs to check the upper limit for that group.

## 2. Build the program

Read the code and predict the ticket for ages 4, 12, 18, and 70:

```python
age = int(input("Age: "))

if age < 5:
    print("Free ticket")
elif age <= 17:
    print("Child ticket")
elif age <= 64:
    print("Adult ticket")
else:
    print("Senior ticket")
```

Why does `elif age <= 17` represent ages 5 to 17? The earlier test has
already ruled out ages below 5. In the same way, the next test catches ages
18 to 64 because the younger ages have already been handled.

## 3. Run and investigate

Run the code and test one age in each category. Then test the boundaries:
`4`, `5`, `17`, `18`, `64`, and `65`.

If a result is wrong, check the condition order and whether the boundary
uses `<` or `<=`.

## 4. Adapt it

Change the messages to include a ticket price of your choice. Keep the age
rules the same. Test all four categories again.

**Finished early?** Ask for the person's name and include it in the output.

## Exit check

1. Why does the adult condition only need to check `age <= 64`?
2. Which condition handles ages 65 and above?
3. Name the six boundary ages to test.

## Answers

### Quick check

1. `score >= 80`
2. It checks another condition if the preceding condition was false.
3. `>=` or `<=` includes a value equal to the boundary.

### Watch and predict

4. Age 4: free ticket; age 12: child ticket; age 18: adult ticket; age 70:
   senior ticket.

### Exit check

5. The previous conditions have already ruled out ages below 18.
6. The `else` block.
7. 4, 5, 17, 18, 64, and 65.
