---
title: "Lesson 8: Quiz Mini Assessment"
description: Independently plan, build, and test a short Python quiz.
order: 8
draft: false
---

## Today you will

Independently build a short quiz that uses input, variables, selection, and a
loop. Use your own questions and answers.

## Assessment task

Create a quiz with at least three questions. Your program must:

- display a welcome or instructions;
- ask for answers using `input()`;
- store and update a score;
- give correct and incorrect feedback using selection;
- use a loop to repeat a meaningful part of the program; and
- display a final score.

You may use a `for` loop to go through a list of questions, or a
`while` loop to allow the player to replay the quiz.

## Quick Python reminders

- For text answers, `input("Your answer: ").strip().lower()` removes spaces
  at the ends and converts letters to lowercase. Compare it with a lowercase
  expected answer, such as `"paris"`.
- To add one point for a correct answer, write `score += 1`. This is a
  shorter form of `score = score + 1`.
- For a replay response, `.strip().lower()` lets inputs such as ` YES ` and
  `Yes` match `"yes"`.

## Plan before coding

| Planning question | Your plan |
| --- | --- |
| What is the quiz topic? | |
| What are your three or more questions and correct answers? | |
| Which variables will you need? | |
| What will your loop repeat? | |
| What will happen for a correct answer? | |
| What will happen for an incorrect answer? | |
| How will the player see their final score? | |

## Loop support

If you need a reminder, choose the pattern that fits your plan.

### Repeat a known set of questions

```python
questions = ["Question one", "Question two", "Question three"]

for question in questions:
    print(question)
```

This displays the questions. Add your own answer checks and score updates.

### Offer another round

```python
play_again = "yes"

while play_again == "yes":
    # Put the quiz instructions here.
    play_again = input("Play again? Enter yes or no: ").strip().lower()
```

Replace the comment with your quiz. The loop needs to ask for a new
`play_again` value so the player can stop.

## Work independently

Do not copy a complete quiz from another person. You may use the support
patterns above and your own notes. Test the program after writing it.

## Self-check

| Requirement | Complete? | Evidence |
| --- | --- | --- |
| At least three questions | | |
| Input and variables | | |
| Score changes correctly | | |
| Correct and incorrect feedback | | |
| A loop repeats a meaningful part | | |
| Final score is displayed | | |
| Correct and incorrect answers tested | | |

## Answers

This is an independent assessment, so there is no single correct program.
Check each requirement against the completed program and test evidence.
