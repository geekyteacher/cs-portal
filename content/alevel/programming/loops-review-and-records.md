---
title: Records
description: Review loops and learn about records
order: 2
draft: false
---
## Learning goals

1. Review loop choices and identify FOR-loop bugs
2. Define and use records in pseudocode and Python
3. Create and manipulate arrays of records
4. Implement linear search on arrays of records
5. Understand bubble sort for record arrays


## 1. Start with the requirement

1. Which loop is best for validating a bib number between 100 and 999, and why?
2. Spot the bug in Snippet B.

```pseudocode
// Snippet A
REPEAT
    OUTPUT "Enter bib number (100–999): "
    INPUT BibNumber
UNTIL BibNumber >= 100 AND BibNumber <= 999

// Snippet B 
FOR Index ← 1 TO 5
    OUTPUT RunnerNames[Index]
    Index ← Index + 1
NEXT Index

// Snippet C
WHILE NOT EOF("Runners.txt") DO
    READFILE "Runners.txt", LineText
    OUTPUT LineText
ENDWHILE
```


## 2. Defining a record in pseudocode

```pseudocode
TYPE TRunner
    DECLARE Name : STRING
    DECLARE BibNumber : INTEGER
    DECLARE FinishTime : REAL
    DECLARE Category : CHAR
    DECLARE PaidFee : BOOLEAN
ENDTYPE

DECLARE Runner1 : TRunner

Runner1.Name ← "Maya Patel"
Runner1.BibNumber ← 104
Runner1.FinishTime ← 42.35
Runner1.Category ← 'S'
Runner1.PaidFee ← TRUE

IF Runner1.PaidFee = TRUE THEN
    OUTPUT Runner1.Name, " finished in ", Runner1.FinishTime, " mins"
ENDIF
```

Write CAIE pseudocode for the requirement. Assume that `INPUT Mark` supplies
an integer; this algorithm checks the **range**, not whether the input text
can be converted to an integer.

```pseudocode
DECLARE Mark : INTEGER

REPEAT
    OUTPUT "Enter a whole-number mark from 1 to 100"
    INPUT Mark
UNTIL Mark >= 1 AND Mark <= 100

OUTPUT "Mark accepted"
```

The condition after `UNTIL` describes the valid range. The loop ends only
when the condition is true. In an implementation that accepts raw text,
type validation must also be handled before converting the value.

### Analyse the design

- Why are the two range conditions joined with `AND`?
- What happens if the condition uses `OR` instead?
- Why is the prompt inside the loop?
- What happens when the user enters `1` or `100`?

## 3. Implement type and range validation in Python

Download the [validation and verification Python examples](/downloads/validation-and-verification.py).
Open the file and add this code at the bottom, after the existing example
calls. The helper functions `is_integer` and `range_check` are already
defined in the file.

```python
while True:
    entered_text = input("Enter a whole-number mark from 1 to 100: ")

    if not is_integer(entered_text):
        print("That is not a whole number.")
        continue

    mark = int(entered_text)

    if range_check(mark, 1, 100):
        print("Mark accepted")
        break

    print("The mark must be from 1 to 100.")
```

The type check happens before `int()` converts the text. The range check
happens after conversion. `continue` returns to the start of the loop, and
`break` ends it when a valid mark is entered.

Run the program and try text, a decimal, an integer outside the range, and
valid values.

## 4. Design a test set

Complete the expected-result column before testing. Then run the program
with each input and record the actual result.

| Input | Purpose | Expected result | Actual result |
| --- | --- | --- | --- |
| `hello` | Invalid type | Rejected; asks again | |
| `4.5` | Real number, not an integer | Rejected; asks again | |
| `0` | Just below the range | Rejected; asks again | |
| `1` | Lower boundary | Accepted | |
| `50` | Typical valid value | Accepted | |
| `100` | Upper boundary | Accepted | |
| `101` | Just above the range | Rejected; asks again | |

Explain why testing only with `50` would not give enough confidence in the
routine.

## 5. Evaluate validation and verification

Validation checks whether data meets specified rules; it cannot establish
that the data is factually correct. For example, `75` is a valid mark within
the range, but validation cannot tell whether it is the student's actual
mark.

Verification checks that entered data matches its source, for example by
visual checking or double entry. It can help identify transcription errors,
but does not decide whether the source data itself is sensible.

For this requirement, identify:

- one error that the type check can detect;
- one error that the range check can detect;
- one error that validation cannot detect; and
- how a verification method might help with that remaining error.

## Extension: improve the specification

Change the requirement so that the program accepts a mark from `0` to `100`
and allows the user to enter `Q` to quit. Write down the revised rules and
test cases before changing the algorithm.

Consider how your design should handle lowercase `q`, spaces before or after
the input, and input that is neither a mark nor the quit command.

## Check your work

- [ ] I separated the type check from the range check.
- [ ] My pseudocode repeats until the range condition is satisfied.
- [ ] My Python program rejects invalid type and range inputs.
- [ ] I tested boundaries, typical valid data, and invalid data.
- [ ] I can explain what validation and verification each detect.
