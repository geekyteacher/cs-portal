---
title: "Lesson 11: Project Completion and Testing"
description: Finish the project, test its rules and loop, and make one evidence-based improvement.
order: 11
draft: false
---

## Today you will

Complete your project, test the important outcomes, fix errors, and make at
least one improvement based on evidence.

## 🧰 Lost your previous work?

Download the [Year 9 project starter file](/downloads/year9-project-starter.py),
save it with a new filename, and rebuild the core of your program using your
project plan and the steps below.

## 🔵 Finish the core program

Before adding another feature, check that your program:

- accepts the required input;
- stores and uses values in variables;
- makes decisions using selection;
- repeats a meaningful task with a loop;
- reaches its intended ending; and
- explains the result clearly to the user.

If any item is missing, finish it before polishing.

## 🟠 Test your program

Write a test plan that matches your own project's rules.

| Test | Input or action | Expected result | Actual result | Pass? |
| --- | --- | --- | --- | --- |
| Normal case 1 | | | | |
| Normal case 2 | | | | |
| Different decision outcome | | | | |
| Loop repeats | | | | |
| Loop stops | | | | |
| Boundary or unusual input | | | | |

For a quiz, test both a correct and incorrect answer. For a password-attempt
simulation, check the allowed and exhausted attempts. For a theme park
checker, test values on either side of an age or height boundary.

## 🔵 Fix and retest

When a test fails:

1. Record the input, expected result, and actual result.
2. Find the relevant condition or loop.
3. Change one thing at a time.
4. Repeat the failed test.
5. Check that the change did not break a different outcome.

If a loop does not stop, stop the program using the editor's stop button.
Then check the condition and the variable or input that should change it.

## 🟣 Improve one feature

Use a test result or feedback to make one useful improvement. Examples:

- reset a score at the start of a new game;
- make an instruction clearer;
- add feedback for an outcome that was missing;
- correct a loop's stopping condition; or
- make an input comparison more consistent with `.strip().lower()`.

For text choices, `.strip().lower()` removes spaces at the ends and converts
letters to lowercase before comparison. Compare with a lowercase expected
value. If your project keeps a score or attempt count, `score += 1` adds one
and is a shorter form of `score = score + 1`.

Record what you changed and which test shows that it works.

## 🟢 Prepare to showcase

Save your program with a clear filename. Prepare a short explanation of:

- what your program does;
- one decision it makes;
- what its loop repeats and how it stops; and
- one test or improvement you are proud of.

## 🧰 Before Asking for Help

- Did I use `==` to compare values, rather than `=`?
- Is every `:` present after an `if`, `elif`, `for`, or `while` line?
- Is the code under each condition and loop indented consistently?
- Did I spell every variable name the same way?
- Did I save my file?

## ✅ Success Criteria

- My project uses input, variables, and selection.
- My loop repeats a meaningful task and stops when expected.
- I have recorded actual results for normal and boundary or unusual tests.
- I fixed at least one issue or made an improvement based on testing.
