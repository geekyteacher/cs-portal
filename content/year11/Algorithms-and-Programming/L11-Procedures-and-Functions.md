---
title: "Lesson 11: Procedures and Functions"
description: "Define and call procedures and functions using parameters, return values and local variables."
order: 11
draft: false
---

## Learning Objectives

- Distinguish between procedures (actions) and functions (calculations returning a value).
- Define and call subprograms using up to three parameters.
- Understand the scope difference between local and global variables.
- Use built-in string and library routines (`SUBSTRING`, `LCASE`, `DIV`, `MOD`, `ROUND`).

---

## 1. Starter (5 mins — Do this first)

Answer these questions in your book.

1. What does a parameter allow a subprogram to receive?
2. Which identifier is clearer: `x` or `NumberOfTickets`? Why?
3. Does a **function** return a value, or does a **procedure** return a value?

---

## 2. Learn: Subprograms & Library Routines

### Procedures vs Functions

#### Procedure

A **procedure** performs a set of instructions.

- May accept parameters.
- Does **not** return a value.
- Called using `CALL`.

```pseudocode
PROCEDURE DisplayMessage()
    OUTPUT "Hello"
ENDPROCEDURE

CALL DisplayMessage()
```

#### Function

A **function** calculates and returns a single value.

- Uses `RETURN`.
- Returns a value to the calling code.
- Used inside expressions.
- Never called with `CALL`.

```pseudocode
FUNCTION Square(Number : INTEGER) RETURNS INTEGER
    RETURN Number * Number
ENDFUNCTION

OUTPUT Square(5)
```

---

### Useful CAIE Library Routines

| Routine | Purpose | Example |
|----------|----------|----------|
| `LENGTH(Text)` | Returns the number of characters in a string | `LENGTH("Hello")` → `5` |
| `LCASE(Text)` | Converts text to lowercase | `LCASE("HELLO")` → `"hello"` |
| `UCASE(Text)` | Converts text to uppercase | `UCASE("hello")` → `"HELLO"` |
| `SUBSTRING(Text, Start, Length)` | Extracts part of a string | `SUBSTRING("Computer", 1, 3)` → `"Com"` |
| `DIV(A, B)` | Integer division | `17 DIV 5` → `3` |
| `MOD(A, B)` | Returns the remainder | `17 MOD 5` → `2` |
| `ROUND(Value, Places)` | Rounds a real number | `ROUND(3.14159, 2)` → `3.14` |

---

### Scope

#### Local Variables

Local variables only exist inside the subprogram where they are declared.

```pseudocode
PROCEDURE Example()
    DECLARE Count : INTEGER
    Count <- 1
ENDPROCEDURE
```

The variable `Count` cannot be accessed outside the procedure.

#### Global Variables

Global variables are declared in the main program and can be accessed by multiple subprograms.

```pseudocode
DECLARE Total : INTEGER
Total <- 0
```

In general, using parameters and local variables is preferred because it reduces bugs and makes programs easier to maintain.

---

## 3. Guided Practice (We do this together)

Complete this function so it returns the larger of two integer values.

```pseudocode
FUNCTION LargerValue(First : INTEGER, Second : INTEGER) RETURNS INTEGER
    IF First > Second THEN
        RETURN _____
    ELSE
        RETURN _____
    ENDIF
ENDFUNCTION
```

1. Fill in the missing return statements.
2. Explain why `LargerValue(12, 9)` is written inside an `OUTPUT` statement rather than preceded by `CALL`.

---

## 4. Core Practice (Paper / Exam Style)

### Task 1: Procedure with a Parameter

Write a procedure called `DisplayLine` that:

- Accepts an integer parameter called `Length`.
- Outputs that many `*` characters.

Example:

```text
CALL DisplayLine(5)
```

Output:

```text
*****
```

---

### Task 2: Function with a Return Value

Write a function called `CalculateTotal` that:

- Accepts:
  - `Price` (REAL)
  - `Quantity` (INTEGER)
- Returns:

```text
Price × Quantity
```

---

### Task 3: Calling Subprograms

Show the correct pseudocode required to call:

1. Your `DisplayLine` procedure.
2. Your `CalculateTotal` function.

Demonstrate each being used inside a complete algorithm.

---

## 5. Python Implementation (Thonny Lab Check)

Open Thonny and translate your `CalculateTotal` function into Python.

```python
def calculate_total(price, quantity):
    return price * quantity
```

Test it with several sample inputs.

Save your program as:

```text
l11_subprograms.py
```

Upload it to the Teams assignment when finished.

---

## 6. Stretch (Finished Early?)

Design a modular program for a shopping system that includes:

1. A procedure to display a welcome banner.
2. A function to calculate the total cost of an item.
3. A main routine that:
   - Repeatedly inputs item prices and quantities.
   - Uses the function to calculate each item total.
   - Accumulates a running basket total.
4. Outputs the final basket cost.

### Challenge Extension

Modify your design to:

- Apply a 10% discount when the basket total exceeds 200.
- Use a separate function to calculate the discount.
- Output both the original total and the discounted total.