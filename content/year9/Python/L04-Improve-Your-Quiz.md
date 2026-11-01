---
title: "Lesson 4: Improve Your Quiz"
description: Build a quiz with questions, a score, and correct or incorrect feedback.
order: 4
draft: false
---

## Today you will

Build a simple quiz, then improve it at a pace that suits your experience.

- **Core:** ask three questions, keep a score, and give feedback.
- **Extension:** use a list and a loop to manage more questions, then add a
  replay option.

You can complete the core task without knowing loops or lists.

## Programming is a process

Programming projects are rarely finished perfectly the first time. Real
programmers work through a cycle:

1. **Build** a first version.
2. **Test** it with different inputs.
3. **Fix** any problems they find.
4. **Improve** the program and test again.

Use this cycle as you develop your quiz. A bug is useful information about
what to fix next.

## Lost your previous work?

If you cannot find your quiz, download the [Year 9 quiz starter
file](/downloads/year9-quiz-starter.py), save a copy with a new filename,
and continue from today's task. You can also use it if you are starting
without previous quiz work.

## Starter: inspect a quiz

Read this code. What happens when the user enters `Paris`? What happens if
they enter a different answer?

```python
answer = input("What is the capital of France? ")

if answer == "Paris":
    print("Correct!")
else:
    print("Not quite.")
```

If the player types `paris` or adds a space, this exact comparison will not
match. Python has string methods that can make text answers more consistent.

### Python Tip: `.lower()`

`.lower()` converts letters in a string to lowercase. For example, `"YES"`,
`"Yes"`, and `"yEs"` all become `"yes"`.

### Python Tip: `.strip()`

`.strip()` removes spaces from the beginning and end of a string. For
example, `" Paris "` becomes `"Paris"`.

You can combine them when reading an answer:

```python
answer = input("What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
else:
    print("Not quite.")
```

Use the same lowercase form in your comparison. `.lower()` changes letter
case; `.strip()` removes spaces at the ends. Neither changes spaces inside
the answer.

## Build the core quiz

Start with a score of zero. Ask three questions, check each answer, and add
one point for each correct answer.

```python
score = 0

answer = input("What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Not quite.")

answer = input("How many bits are in a byte? ").strip()
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Not quite.")

answer = input("Which device displays a computer's output? ").strip().lower()
if answer == "monitor":
    print("Correct!")
    score += 1
else:
    print("Not quite.")

print("Your score is", score, "out of 3")
```

Change the questions to a topic you know. Make sure that the expected answer
matches what your program checks.

## Check your understanding

1. Why does `score` start at zero?
2. Which lines increase the score?
3. What happens when an answer is wrong?
4. What would happen if you forgot to increase the score after a correct
   answer?

## Choose your next step

### Core: make the quiz your own

- Write three questions about a topic you know.
- Give correct and incorrect feedback for every question.
- Display the final score out of three.
- Test at least one correct and one incorrect answer.

### Extension: add more questions

Add at least two more questions by following the same pattern. Keep the final
score total accurate.

### Challenge: prepare for using loops

If you already know lists, put question text into a list and write a `for`
loop that displays each question. You do not need to use a list to finish
today's core task; Lesson 5 will introduce the idea for everyone.

If you finish, plan how a player could choose to play the quiz again.

## Exit check

Write one sentence explaining what `score += 1` does.

## Answers

1. Starting at zero means no correct answers have been counted yet.
2. The `score += 1` lines add one point after a correct answer. This is a
   shorter way of writing `score = score + 1`.
3. The `else` branch displays `Not quite.` and does not add a point.
4. The quiz could display a score that is too low, even when an answer was
   correct.

## Success Criteria

- I can ask at least three questions using `input()`.
- I can use a variable to keep score.
- I can use selection to give correct or incorrect feedback.
- I can display the final score.
- **Challenge:** I can use a loop, replay option, or list to extend the quiz.
