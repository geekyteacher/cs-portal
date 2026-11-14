---
title: "Lesson 12: Validation and Verification"
description: "Choose validation and verification checks and apply normal, abnormal, extreme and boundary test data."
order: 12
draft: false
---

## Learning Objectives

- Distinguish between validation (checking data reasonableness) and verification (checking data accuracy against a source).
- Identify appropriate validation checks (range, length, type, presence, format, check digit).
- Describe verification methods (visual check, double entry).
- Select rigorous test data: normal, abnormal, extreme, and boundary.

---

## 1. Starter (5 mins — Do this first)

Answer these questions in your book.

1. Does passing a range check (`0` to `100`) prove that the correct student's mark was entered?
2. What is the difference between an **extreme** value and a **boundary** value?
3. Name one verification method used to prevent typing mistakes when entering a new password.

---

## 2. Learn: Data Quality & Testing

### Validation vs Verification

#### Validation

Validation uses automated checks to ensure data is sensible and follows predefined rules.

Common validation checks include:

- **Range check** - e.g. age must be between 11 and 18.
- **Length check** - e.g. password must contain exactly 8 characters.
- **Type check** - e.g. an exam mark must be an integer.
- **Presence check** - e.g. a username cannot be left blank.
- **Format check** - e.g. an email address must contain `@`.
- **Check digit** - e.g. barcode or ISBN validation.

> Validation checks whether data is reasonable, not whether it is correct.

#### Verification

Verification checks whether data has been copied accurately from an original source.

Common verification methods include:

- **Visual check**
  - A user compares the entered data with the original source.
- **Double entry**
  - The user enters the data twice and both entries must match.

> Verification checks accuracy of entry, not validity of the original data.

---

### Test Data Categories

| Test Type | Description |
|------------|------------|
| **Normal** | Typical valid data that should be accepted. |
| **Abnormal** | Invalid data that should be rejected. |
| **Extreme** | The smallest or largest valid values. |
| **Boundary** | An extreme valid value and its nearest invalid neighbour. |

#### Example

If valid ages are from **11 to 18 inclusive**:

| Type | Example |
|--------|--------|
| Normal | `15` |
| Extreme (Lower) | `11` |
| Extreme (Upper) | `18` |
| Boundary (Lower) | `10`, `11` |
| Boundary (Upper) | `18`, `19` |
| Abnormal | `-3`, `"cat"` |

---

## 3. Guided Practice (We do this together)

A youth club accepts an integer age from `11` to `18` inclusive.

The age field is required and users must enter it twice.

Answer the following:

1. Suggest an appropriate validation check for the age range.
2. State one abnormal test value.
3. State the pair of lower boundary test values.
4. Explain why matching double-entry inputs do not prove the entered age is actually true.

---

## 4. Core Practice (Paper / Exam Style)

### Task 1: Validation Matching

Match each rule to the most appropriate validation check.

| Rule | Validation Check |
|--------|--------|
| Username cannot be blank | |
| PIN must contain exactly 4 digits | |
| Age must be between 11 and 18 | |
| Exam mark must be numeric | |
| School email must follow the correct format | |

---

### Task 2: Test Data Table

A program accepts percentages from `0` to `100` inclusive.

It outputs:

```text
Pass
```

for scores of `50` or above.

Create a complete test data table including:

- Normal data
- Abnormal data
- Extreme values
- Input boundaries:
  - `-1`
  - `0`
  - `100`
  - `101`
- Decision boundary values:
  - `49`
  - `50`

Your table should include:

| Test Value | Test Type | Expected Result | Reason |
|------------|------------|------------|------------|
| | | | |

---

### Task 3: Verification Limitations

Explain one limitation of using a **visual check** when transcribing a long handwritten serial number.

Consider:

- Human error.
- Similar-looking characters.
- Fatigue when checking large amounts of data.

---

## 5. Python Implementation (Thonny Lab Check)

Write a Python program that validates a score between `0` and `100`.

```python
score = int(input("Enter score (0-100): "))

while score < 0 or score > 100:
    print("Invalid score. Try again.")
    score = int(input("Enter score (0-100): "))

print("Valid score entered.")
```

Save your program as:

```text
l12_validation.py
```

Upload it to the Teams assignment when complete.

---

## 6. Stretch (Finished Early?)

Check digits are often used to detect data-entry mistakes.

Examples include:

- ISBN numbers
- Credit card numbers
- Product codes
- Barcodes

### Challenge

Design a check-digit system for a four-digit product code where the final digit is calculated using modulo-11 arithmetic.

Your answer should:

1. Explain how the check digit is calculated.
2. Provide a worked example.
3. Show how the system would detect an error such as:

```text
1234
```

being entered as:

```text
1243
```

### Extension

Research a real-world check-digit system such as:

- ISBN-10
- ISBN-13
- EAN-13
- Credit card numbers (Luhn Algorithm)

Compare it with your own design and explain which is likely to detect more errors.