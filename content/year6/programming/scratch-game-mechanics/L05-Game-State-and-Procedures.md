---
title: "Lesson 5: Create a Goal and Ending"
description: Use a condition and a custom block to manage a clear win or game-over ending.
order: 5
draft: false
---

## Today you will

Make a clear rule for winning or losing, then put a repeated check into a
reusable custom block.

## Starter: make the rule precise

Write your game's win rule using **if ... then**. For example:

> If `Score` is at least `3`, then the player wins.

If your game uses a different goal, describe exactly what must happen for
the player to win. A player should also be able to tell when the game is
over.

## Add a game state

Create a variable called `Game State`. At the start of the game, set it to
`Playing`. When the player wins or loses, change it to `Won` or `Game over`.
This makes it clear which part of the game should happen next.

For a score-based goal, create a custom block from **My Blocks** called
`check game state`. Add the win condition to its definition:

```text
define check game state
If <Score >= 3> then
    Set Game State to [Won]
    Broadcast [You Win] and wait
    Stop all
```

Call the custom block from a separate loop:

```text
When green flag clicked
Forever
    If <Game State = [Playing]> then
        check game state
```

On the Stage, respond to the message:

```text
When I receive [You Win]
Switch backdrop to [You Win]
```

Create a simple backdrop that tells the player they have won. Use your own
goal in place of `Score >= 3`. For a game-over rule, make a matching
`Game over` message and ending.

The custom block is a procedure: it gives a named set of instructions that
can be called from another script. You can use the same structure for a
different win rule.

## Core task

- Write a clear win condition for your game.
- Add a `Game State` variable and reset it to `Playing` at the start.
- Create a custom block that checks the win condition.
- Show an ending when the player wins.
- Make sure the game does not keep running after the ending.

## Challenge choices

- Add a countdown timer and a game-over ending.
- Add a restart button that resets the score, timer, and game state.
- Add a custom block called `reset game` to keep setup instructions
  together.
- Require two conditions for a win, such as enough points **and** reaching
  the exit.
- Add an ending animation or sound.

## Test the ending

| Test | Expected result |
| --- | --- |
| Start the game | Game State is `Playing` |
| Goal condition is not met | The game continues |
| Goal condition is met | The win message appears |
| After the ending | Gameplay stops |
| Restart, if included | Score and game state reset |

## Record your evidence

Write your win rule in words and record one test showing what happens
before and after the condition is met. Sketch the custom block or describe
the condition and ending. If uploads are available, this is a useful point
to submit a screenshot showing the working game and its win or game-over
rule.

## Exit check

What makes your custom block reusable? How does the player know the game
has ended?

## Save your work

Save your Scratch project using your teacher's instructions.
