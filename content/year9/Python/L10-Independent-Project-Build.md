---
title: "Lesson 10: Independent Project Build"
description: Build the first working version of your planned Python project.
order: 10
draft: false
---

## Today you will

Build the first working version of your project using your plan from Lesson
9. Get the essential features working before adding optional improvements.

## 🧰 Lost your previous work?

Download the [Year 9 project starter file](/downloads/year9-project-starter.py),
save it with a new filename, and adapt its input, decisions, and repeated
task to match your plan.

## 🔵 Build in stages

### Stage 1: Make one interaction work

Write a short program that asks for one piece of input and displays a
response. Run it before adding more code.

### Stage 2: Add variables and decisions

Store the input in a variable. Use `if`, `elif`, or `else` to respond to the
user's choice.

```python
choice = input("Choose yes or no: ").strip().lower()

if choice == "yes":
    print("You chose yes.")
else:
    print("You chose no.")
```

`.strip()` removes spaces at the ends and `.lower()` makes letter case
consistent. Compare the result with a lowercase value such as `"yes"`. This
is useful for menu choices and other text input, but do not lowercase a name
that you want to display as entered.

Adapt this structure to the rules in your plan.

### Stage 3: Add the loop

Add the loop you planned. Decide what changes during each repetition and
check that the stop condition can be reached.

For a fixed number of repetitions:

```python
for turn in range(3):
    print("Turn", turn + 1)
```

For repetition controlled by a condition:

```python
choice = "continue"

while choice == "continue":
    choice = input("Enter continue or stop: ").strip().lower()
```

The same `.strip().lower()` reminder applies here: both `" STOP "` and
`"Stop"` become `"stop"`.

Do not run a `while` loop until you have checked what will change its
condition.

### Stage 4: Add the remaining features

Finish the normal program flow and make the messages clear. Save your work
regularly.

## 🟠 Checkpoint

Ask your teacher to check the first working version, or show a partner:

- the user can enter information;
- the program makes at least one decision;
- the loop repeats the intended task; and
- the program has a way to finish.

## 🧰 If you get stuck

1. Read the error message and find the line it identifies.
2. Check punctuation, spelling, indentation, and variable names.
3. Temporarily test one small part at a time.
4. Compare the actual result with your plan.
5. Ask for help with the smallest specific problem you can describe.

## 🟣 Extension

Once the essential program works, improve one feature: add clearer
instructions, another outcome, a score or attempt counter, or a more useful
end message. Update your plan if the program's rules change.

## 🧰 Before Asking for Help

- Did I use `==` to compare values, rather than `=`?
- Is every `:` present after an `if`, `elif`, `for`, or `while` line?
- Is the code under each condition and loop indented consistently?
- Did I spell every variable name the same way?
- Did I save my file?

## ✅ Success Criteria

- My program gets input and stores information in variables.
- My program uses selection to respond to the user's input.
- My loop repeats the task in my plan and has a way to stop.
- I have run the program and checked at least one outcome.
