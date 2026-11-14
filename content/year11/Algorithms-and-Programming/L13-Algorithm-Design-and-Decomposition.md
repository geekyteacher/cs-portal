---
title: "Lesson 13: Algorithm Design and Decomposition"
description: "Analyse a problem, decompose it and design a tested solution using pseudocode, structure diagrams and file handling."
order: 13
draft: false
---

## Learning Objectives

- Describe the program development life cycle stages (Analysis, Design, Coding, Testing).
- Decompose complex problems into manageable sub-systems.
- Select and use structure diagrams, flowcharts, or pseudocode.
- Implement CAIE pseudocode text file handling (`OPENFILE`, `READFILE`, `WRITEFILE`, `CLOSEFILE`).

---

## 1. Starter (5 mins — Do this first)

For an online shopping cart program:

1. Name two inputs.
2. Name one processing step.
3. Name what data must be stored persistently.

---

## 2. Learn: Life Cycle & File Handling

### Program Development Life Cycle

Most software projects follow four key stages:

| Stage | Purpose |
|---------|---------|
| **Analysis** | Identify the problem, requirements, inputs, outputs, processing, and storage needed. |
| **Design** | Plan the solution using pseudocode, flowcharts, structure diagrams, and data structures. |
| **Coding** | Translate the design into a programming language. |
| **Testing** | Check the program works correctly using suitable test data. |

---

### Decomposition

**Decomposition** means breaking a large problem into smaller, manageable parts.

For example, an online shopping system could be decomposed into:

1. User login system.
2. Product catalogue.
3. Shopping basket.
4. Payment processing.
5. Order confirmation.

Benefits of decomposition:

- Makes programs easier to design.
- Makes testing simpler.
- Allows different programmers to work on different parts.
- Makes maintenance easier.

---

### File Handling in CAIE Pseudocode

Files allow data to be stored after a program closes.

#### Reading from a File

```pseudocode
DECLARE LineOfText : STRING

OPENFILE "Data.txt" FOR READ
READFILE "Data.txt", LineOfText
CLOSEFILE "Data.txt"
```

---

#### Writing to a File

```pseudocode
OPENFILE "Data.txt" FOR WRITE
WRITEFILE "Data.txt", "New Record"
CLOSEFILE "Data.txt"
```

> [!WARNING]
> Opening a file using `FOR WRITE` removes any existing contents before writing new data.

---

### Inputs, Processes, Outputs and Storage (IPOS)

When analysing a problem, identify:

| Component | Description |
|------------|-------------|
| **Input** | Data entered into the system. |
| **Process** | Operations performed on the data. |
| **Output** | Information produced by the system. |
| **Storage** | Data retained for future use. |

---

## 3. Guided Practice (We do this together)

A school needs a program that:

- Inputs a student's name.
- Inputs three test marks.
- Calculates the average mark.
- Outputs the student name and average.

Complete an IPOS planning table.

| Category | Examples |
|-----------|----------|
| Inputs | |
| Processes | |
| Outputs | |
| Storage | |

### Extension Question

How could the program be decomposed into separate modules or subprograms?

---

## 4. Core Practice (Paper / Exam Style)

### Club Booking System Scenario

A school needs a program that:

- Records club bookings.
- Stores student names.
- Stores year groups.
- Checks students are in allowed year groups.
- Counts the total number of bookings.
- Stores records for future use.

---

### Task 1: Decomposition

Break the system into at least four sub-systems.

For example:

- Input module
- Validation module
- Storage module
- Reporting module

Explain the purpose of each.

---

### Task 2: Booking Algorithm

Write CAIE pseudocode that:

1. Inputs a student's name.
2. Inputs their year group.
3. Validates that the year group is permitted.
4. Records valid bookings.
5. Maintains a running total of bookings.
6. Outputs the booking count.

---

### Task 3: File Handling

Write pseudocode that saves the final booking count to a file called:

```text
Bookings.txt
```

Use the file-handling commands:

- `OPENFILE`
- `WRITEFILE`
- `CLOSEFILE`

---

## 5. Python Implementation (Thonny Lab Check)

Write a Python program that:

1. Opens a file called `scores.txt` in write mode.
2. Stores three student names.
3. Closes the file.
4. Reopens the file in read mode.
5. Displays the contents on the screen.

Example structure:

```python
file = open("scores.txt", "w")

file.write("Alice\n")
file.write("Ben\n")
file.write("Charlie\n")

file.close()

file = open("scores.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

Save your program as:

```text
l13_files.py
```

Upload it to the Teams assignment when complete.

---

## 6. Stretch (Finished Early?)

Choose a complex real-world system such as:

- Library management system
- Hospital appointment system
- Cinema booking system
- School management system

### Task 1: Structure Diagram

Draw a top-level structure diagram that decomposes the system into at least three major sub-systems.

Example:

```text
Library System
├── Member Management
├── Book Loans
└── Reporting
```

### Task 2: Abstraction

Explain how **abstraction** helps developers focus only on relevant details.

For your chosen system:

- What details would a librarian need to see?
- What details could be hidden from them?
- Why is hiding unnecessary complexity useful?

### Challenge Extension

Extend your structure diagram further by decomposing one of your sub-systems into smaller modules and explaining how they interact.