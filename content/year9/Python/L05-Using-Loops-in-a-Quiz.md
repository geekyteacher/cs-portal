---
title: "Lesson 5: Using Loops in a Quiz"
description: Use for and while loops to repeat questions and replay a quiz.
order: 5
draft: false
---

## Today you will

Use repetition to make a quiz easier to extend and replay.

- Use a `for` loop when you know how many times to repeat, or when working
  through a sequence.
- Use a `while` loop when repetition should continue until a condition
  changes.

## Lost your previous work?

Download the [Year 9 quiz starter file](/downloads/year9-quiz-starter.py),
save it with a new filename, and continue from today's task.

## Starter: predict

Without running the code, how many lines are printed? What values does
`number` take?

```python
for number in range(1, 4):
    print("Question", number)
```

## 1. Repeat a set number of times

Run the starter and check your prediction. `range(1, 4)` produces `1`, `2`,
and `3`, so the loop runs three times.

```python
for number in range(1, 4):
    print("Question", number)
```

The loop variable changes on each repetition. The indented code is the part
that repeats.

## 2. Loop through a list of questions

A list stores several values under one name. Each time through the loop,
`question` refers to the next item in the list.

```python
questions = [
    "What is the capital of France?",
    "How many bits are in a byte?",
    "Which device displays a computer's output?",
]

for question in questions:
    print(question)
```

This is a **new idea** if you have not used lists before. First check that
the loop displays all three questions. Then adapt it to your own quiz.

> [!NOTE]
>
> This example displays each question. Checking different answers and keeping
> a score still needs the matching `if` statements and score updates from
> Lesson 4.

## 3. Replay with a `while` loop

A `while` loop checks its condition before each repetition. The program must
ask for a new value inside the loop so the player can eventually choose to
stop.

```python
play_again = "yes"

while play_again == "yes":
    print("Run your quiz here")
    play_again = input("Play again? Enter yes or no: ").strip().lower()

print("Thanks for playing!")
```

### Python Tip reminder: normalise the replay answer

`.strip().lower()` removes spaces from the ends and converts letters to
lowercase. That means inputs such as ` YES ` and `Yes` become `"yes"` and
match the loop condition.

If `play_again` is never updated, the condition remains true and the loop
does not stop. Replace the message with your working quiz before testing the
replay version.

## Practice

### Core: loop through questions

Use the question list above or your own list. Write a `for` loop that displays
every question. Check that each appears once.

### Supported: build it one step at a time

1. Create a list with two question strings.
2. Add `for question in questions:`.
3. Indent `print(question)` underneath it.
4. Run the program and count the output.

### Extension: add replay

Put your quiz inside a `while play_again == "yes":` loop. Ask whether the
player wants to replay after the quiz finishes. Check that entering `no`
stops the program. Use `.strip().lower()` on the replay input so capital
letters and extra spaces do not prevent the expected response.

## Test your loop

| Test | Expected result |
| --- | --- |
| The question list has three items | Three questions are displayed |
| The player enters `yes` to replay | The quiz runs again |
| The player enters `no` to replay | The quiz ends |

## Exit check

When would you choose a `for` loop? When would you choose a `while` loop?

## Answers

The starter prints three lines. `number` takes the values `1`, `2`, and `3`.
A `for` loop suits a known sequence or number of repetitions. A `while` loop
suits repetition that continues until a condition changes.

## Before Asking for Help

- Did I use `==` to compare values, rather than `=`?
- Is every `:` present after an `if`, `for`, or `while` line?
- Is the code inside the loop indented consistently?
- Did I spell every variable name the same way?
- Did I save my file?

## Success Criteria

- I can use a `for` loop to repeat instructions or go through a sequence.
- I can use a `while` loop and update its condition so it can stop.
- I can use a loop to display quiz questions or offer replay.
- I can test that the loop repeats and ends as expected.
