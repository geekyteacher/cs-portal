---
title: Validation and Verification
description: Design, implement, and test robust data validation, then evaluate what validation can and cannot guarantee.
order: 1
draft: false
---
## Learning goals

- translate a data-entry requirement into validation rules;
- design a validation routine in CAIE pseudocode;
- implement type and range checks in Python; and
- select test data that checks normal, invalid, and boundary cases.

## 1. Start with the requirement

A program asks a user to enter a whole-number mark from `1` to `100`.
It must keep asking until it receives an acceptable value.

Before writing code, identify the rules:

1. The input must represent an integer.
2. The integer must be from `1` to `100`, inclusive.
3. The program must not continue until both rules are satisfied.

These are separate checks. A value can be the right type but outside the
range, or look like a number but not represent an integer.

## 2. Design the range-validation algorithm

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
