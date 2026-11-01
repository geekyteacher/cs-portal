---
title: "Lesson 6: Improve the Player Experience"
description: Add a welcome, player name, and useful end-of-quiz messages.
order: 6
draft: false
---

## Today you will

Improve how your quiz feels to play by adding a welcome, a player's name, and
a message based on the final score.

## Starter: choose a message

A quiz has five questions. What message should it show for scores of `5`, `4`,
`2`, and `0`? Write down your ideas before looking at the example.

## Welcome the player

Add a welcome and ask for the player's name near the start of your quiz:

```python
print("Welcome to the quiz!")
player_name = input("What is your name? ").strip()
print("Good luck,", player_name)
```

Use `player_name` in a message at the end too.

`.strip()` removes accidental spaces at the start and end of the name. Do
not use `.lower()` on a player's name unless you want to display it entirely
in lowercase.

## Respond to the final score

After the quiz has finished, use `if`, `elif`, and `else` to select one
message. In this example, the maximum score is five:

```python
if score == 5:
    print("Perfect score,", player_name)
elif score >= 3:
    print("Well done,", player_name)
else:
    print("Keep practising,", player_name)
```

Python checks the conditions from top to bottom. Once a condition is true, it
runs that branch and skips the remaining branches. Put the most specific
condition first: if `score >= 3` came before `score == 5`, a score of five
would receive `Well done` instead of `Perfect score`.

## Practice

### Core

Add a welcome, ask for a name, and display a personalised final message.
Make at least two different messages based on the score.

### Supported

If `elif` is new, begin with two outcomes using `if` and `else`. Then add an
`elif` for a middle score range.

### Extension

- Add a short instruction screen before the first question.
- Tell the player how many questions the quiz contains.
- Add a message for a score of zero.
- If you have a replay loop, reset `score` at the start of each new game.

## Test your messages

| Score | Expected message |
| --- | --- |
| 5 | Perfect score |
| 3 | Well done |
| 0 | Keep practising |

Change `score` temporarily to each test value to check the branches. Restore
your quiz so it calculates the score normally.

## Exit check

Why should `score == 5` be checked before `score >= 3`?

## Answers

Because five also satisfies `score >= 3`. Python runs the first true branch,
so the exact perfect-score condition must come first.
