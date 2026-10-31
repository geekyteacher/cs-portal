---
title: "Lesson 11: Procedures and Functions"
description: "Define and call procedures and functions using parameters, return values and local variables."
order: 11
draft: false
---
## Topics in this page

- Procedures and functions
- Parameters
- Return values
- Local and global variables
- Maintainable algorithms

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Explain why a problem may be divided into subprograms.
- Define and call a procedure with or without parameters.
- Define and call a function that returns a value.
- Distinguish between local and global variables.
- Use meaningful identifiers and appropriate comments.

## Quick Check

1. What does a parameter allow a subprogram to receive?
2. Which is clearer: `x` or `NumberOfTickets`? Why?
3. Does a function return a value, or does a procedure return a value?

## Learn

Subprograms divide a solution into smaller named parts. They can make an
algorithm easier to understand, test and maintain. In the syllabus,
procedures and functions may use up to three parameters.
Their definitions are placed at the start of the code, before the main
program statements.

### Procedures

A **procedure** performs instructions. It may have parameters, but it does not
return a value.

```pseudocode
PROCEDURE ShowTotal(Amount : REAL)
    OUTPUT "Total cost: ", Amount
ENDPROCEDURE
```

Call a procedure using `CALL`:

```pseudocode
CALL ShowTotal(12.50)
```

A procedure with no parameters can be called without brackets:

```pseudocode
PROCEDURE ShowWelcome
    OUTPUT "Welcome"
ENDPROCEDURE

CALL ShowWelcome
```

### Functions

A **function** calculates and returns one value. The function's return type
appears in its definition. Use `RETURN` to give the value back.

```pseudocode
FUNCTION CalculateArea(Length : REAL, Width : REAL) RETURNS REAL
    RETURN Length * Width
ENDFUNCTION
```

Use the function call as part of an expression. Do **not** use `CALL` for a
function:

```pseudocode
Area <- CalculateArea(5.0, 3.0)
OUTPUT Area
```

### Parameters and local variables

A **parameter** is a named input in a subprogram definition. When the
subprogram is called, the argument value is supplied for that parameter. The
argument data type must match the parameter's data type.

A **local variable** is declared inside a subprogram and is used within that
subprogram. A **global variable** is declared outside subprograms and can be
used by the main algorithm and subprograms. Prefer parameters and local
variables where practical, because they make data dependencies clearer and
reduce accidental changes to shared values.

### Useful string operations and library routines

These standard operations can be used as part of expressions:

| Operation | Purpose | Example |
| --- | --- | --- |
| `LENGTH(Text)` | Returns the number of characters. | `LENGTH("Happy Days")` returns `10`. |
| `LCASE(Text)` | Returns the text in lower case. | `LCASE("HELLO")` returns `"hello"`. |
| `UCASE(Text)` | Returns the text in upper case. | `UCASE("Happy")` returns `"HAPPY"`. |
| `SUBSTRING(Text, Start, Length)` | Returns part of a string. | `SUBSTRING("Happy Days", 1, 5)` returns `"Happy"`. |
| `DIV(A, B)` | Returns the integer quotient. | `DIV(10, 3)` returns `3`. |
| `MOD(A, B)` | Returns the remainder. | `MOD(10, 3)` returns `1`. |
| `ROUND(Value, Places)` | Rounds a real number. | `ROUND(3.14159, 2)` returns `3.14`. |
| `RANDOM()` | Returns a random real from 0 to 1 inclusive. | `RANDOM()`. |

For `SUBSTRING`, the start position is generally `1` for the first character.
`DIV` and `MOD` use integer operands. Use parentheses to make complex
expressions clear.

### Maintainable algorithms

Make algorithms easier to read and update by using:

- Meaningful names for variables, constants, arrays, procedures and functions.
- Subprograms for tasks that can be named and reused.
- Short comments that explain a purpose or a non-obvious decision.
- Consistent indentation and clear structure.

Selection and iteration can be nested when a problem needs a decision or a
loop inside another structure. Trace each level carefully; the syllabus
expects no more than three levels of nesting.

## Guided Practice

Complete this function so it returns the larger of two values:

```pseudocode
FUNCTION LargerValue(First : INTEGER, Second : INTEGER) RETURNS INTEGER
    IF First > Second THEN
        RETURN _____
    ELSE
        RETURN _____
    ENDIF
ENDFUNCTION

OUTPUT LargerValue(12, 9)
```

1. Fill in the return values.
2. State the output.
3. Explain why `LargerValue(12, 9)` is used inside `OUTPUT`, rather than with
   `CALL`.

## Core Practice

1. Write a procedure called `DisplayLine` that takes an integer parameter
   `Length` and outputs that many `*` characters.
2. Write a function called `CalculateTotal` with parameters `Price` and
   `Quantity`. It returns `Price * Quantity`.
3. Show how to call each subprogram.
4. Identify one local variable in a subprogram and explain what makes it
   local.

## Support

Use these patterns:

```pseudocode
PROCEDURE ProcedureName(Parameter : INTEGER)
    // instructions
ENDPROCEDURE

CALL ProcedureName(Value)
```

```pseudocode
FUNCTION FunctionName(Parameter : INTEGER) RETURNS INTEGER
    RETURN Result
ENDFUNCTION

Answer <- FunctionName(Value)
```

Remember: use `CALL` for procedures; use a function as part of an expression.

## Stretch

Design a program that calculates the total cost of several items. Decompose
the solution into:

- A procedure that displays instructions.
- A function that calculates the cost for one item.
- A main algorithm that inputs values, calls the subprograms and outputs the
  final total.

Use meaningful names and no more than three parameters in any subprogram.

## Homework

In your own words, explain the difference between a procedure and a function.
Include how each one is called and whether it returns a value.
