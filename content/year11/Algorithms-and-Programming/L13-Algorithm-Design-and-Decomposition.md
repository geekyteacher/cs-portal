---
title: "Lesson 13: Algorithm Design and Decomposition"
description: "Analyse a problem, decompose it and design a tested solution using pseudocode, flowcharts or structure diagrams."
order: 13
draft: false
---
## Topics in this page

- Program development life cycle
- Decomposition and sub-systems
- Inputs, processes, outputs and storage
- Structure diagrams, flowcharts and pseudocode
- Designing, testing and amending algorithms

## Learning Objectives

By the end of this lesson sequence you should be able to:

- Describe the analysis, design, coding and testing stages.
- Break a problem into smaller sub-problems.
- Identify inputs, processes, outputs and storage.
- Select a suitable representation for an algorithm.
- Design and amend an algorithm using suitable test data.

## Quick Check

For a program that calculates the total price of a shopping basket:

1. Name two possible inputs.
2. Name one process.
3. Name one output.
4. What information might need to be stored?

## Learn

### The program development life cycle

| Stage | What happens |
| --- | --- |
| Analysis | Identify the problem, requirements, inputs, processes, outputs and storage. Use abstraction to focus on relevant details and decompose the problem into manageable parts. |
| Design | Plan the solution using structure diagrams, flowcharts and/or pseudocode. |
| Coding | Write program code and test it repeatedly as it is developed. |
| Testing | Use suitable test data to check that the solution works and correct errors. |

The stages support each other. Testing may reveal a problem that requires
changes to the design or code.

### Decomposition

**Decomposition** means breaking a problem into smaller parts, or
sub-systems. Each part should have a clear purpose and connect to the overall
requirements.

For a checkout program, possible parts are:

1. Input item details.
2. Calculate each line total.
3. Add line totals to a basket total.
4. Apply any discount.
5. Display the receipt.

For each part, identify its inputs, processing, outputs and any data that must
be stored.

### Choosing a design method

- A **structure diagram** shows how a system or problem is divided into
  smaller parts.
- A **flowchart** represents the control flow of an algorithm using standard
  symbols.
- **Pseudocode** describes an algorithm in a language-independent, structured
  form.

Use the conventions and symbols specified by the task. Pseudocode needs
precise operators and instructions; for example, write `Score >= 50`, not
“Score is at least 50”.

For Paper 2 algorithm questions, write the solution in pseudocode. Coding
practice is still useful; the syllabus permits pseudocode or Python, Visual
Basic or Java for the 15-mark scenario question.

### From design to testing

After writing an algorithm:

1. Check that every requirement is represented.
2. Check that variables are declared and have suitable data types.
3. Follow sequence, selection and iteration carefully.
4. Use test data and state the expected results.
5. Amend the algorithm if a test reveals a problem.

When asked to amend an existing solution, preserve the parts that already
meet the requirements and change the specific step that causes the problem.

## Guided Practice

Design a program that inputs a student's name and three assessment marks,
calculates the average, and outputs the name and average.

Complete the planning table:

| Category | Possible data |
| --- | --- |
| Inputs |  |
| Processes |  |
| Outputs |  |
| Storage |  |
| Sub-problems |  |

Then write a short pseudocode outline. You do not need to write every
instruction yet.

## Core Practice

### Task: School club booking system

A school needs a program to record bookings for a club. It must collect a
student's name and year group, check that the year group is allowed, store
accepted bookings, and display how many students have booked.

1. List the requirements in your own words.
2. Identify the inputs, processes, outputs and stored data.
3. Decompose the problem into at least four sub-problems.
4. Draw a structure diagram or flowchart for the main parts.
5. Write pseudocode for the booking and counting process.
6. Suggest normal, abnormal, extreme and boundary test data for the year
   group check. State the expected result.
7. Implement one small part of your solution in Python, then amend it after
   testing an invalid year group.

## Support

Use this planning scaffold:

1. **Input:** What does the user provide?
2. **Check:** What rules must the input satisfy?
3. **Process:** What calculations or updates are needed?
4. **Storage:** What values must be remembered?
5. **Output:** What should the user or teacher see?
6. **Test:** What valid and invalid examples will you try?

Start your pseudocode with:

```pseudocode
DECLARE StudentName : STRING
DECLARE YearGroup, BookingCount : INTEGER

BookingCount <- 0
OUTPUT "Enter student name:"
INPUT StudentName
OUTPUT "Enter year group:"
INPUT YearGroup

// Add the range check, storage/update and outputs
```

## Stretch

Choose a familiar system, such as a library loan, canteen order or sports
booking.

- Draw a structure diagram that decomposes the system into sub-systems.
- Identify one requirement that is not relevant to the problem and explain
  why it can be abstracted away.
- Design a flowchart or pseudocode solution for one sub-system.
- Give test data and expected outcomes for the key decision.

## Additional syllabus focus: file handling

Some programs need to keep data after they close. In CAIE pseudocode, a file
is opened in one mode, read from or written to, and then closed.

```pseudocode
DECLARE LineOfText : STRING

OPENFILE "Names.txt" FOR READ
READFILE "Names.txt", LineOfText
CLOSEFILE "Names.txt"
```

To write a line, open the file in `WRITE` mode and use `WRITEFILE`:

```pseudocode
DECLARE LineOfText : STRING

LineOfText <- "Ada Lovelace"
OPENFILE "Names.txt" FOR WRITE
WRITEFILE "Names.txt", LineOfText
CLOSEFILE "Names.txt"
```

`READFILE` and `WRITEFILE` can handle single items of data or a line of text.
Opening a file for writing creates a new file and replaces existing contents,
so use it carefully. Files should be closed when they are no longer needed.
File handling is an additional Paper 2 skill beyond the original 24 lesson
titles.

## Homework

Complete the planning and design for one sub-system in the club booking
scenario. Include inputs, processes, outputs, storage, pseudocode and at
least two test cases with expected results.
