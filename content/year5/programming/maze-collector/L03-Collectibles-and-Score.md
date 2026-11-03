---
title: "Lesson 3: Collect Items and Keep Score"
description: Create collectibles and use a Scratch variable to track the player's score.
order: 3
draft: false
---

## Today you will

Add collectible items and use a variable to keep track of how many the
player has collected.

## Starter: trace the score

The score starts at `0`. The player collects one coin, then two more. What
should the score show after each collection?

## Create the score variable

Create a variable called `Score` for all sprites. On the Stage or player,
make a script that sets it to `0` when the green flag is clicked.

```text
When green flag clicked
Set Score to 0
```

Set the score once at the start of the game, not inside the player's
`forever` movement loop.

## Make a collectible

Choose a coin, star, key, or other item sprite. Add a script like this:

```text
When green flag clicked
Show
Forever
    If touching Player? then
        Change Score by 1
        Hide
```

Use Scratch's `touching [Player]?` block. The item hides after collection so
the score only increases once for that item. If the item should reappear,
choose a new position and show it again after a short wait.

## Core task

- Create and reset the `Score` variable.
- Add at least three items to the maze.
- Make each item increase the score once when collected.
- Test that the score resets when you click the green flag.

## Challenge choices

- Make a special item worth more than one point.
- Add a sound or costume effect when an item is collected.
- Make an item appear at a random position, checking that it does not appear
  inside a wall.
- Add a key that the player must collect before the exit can open.
- Display a message when all the items have been collected.

## Test the score

| Test | Expected result |
| --- | --- |
| Click the green flag | Score becomes `0` |
| Touch one item | Score increases by `1` |
| Stay on the same item | Score does not keep increasing |
| Collect three items | Score becomes `3` |
| Restart the game | Score returns to `0` |

## Exit check

Why does the collectible hide after the player touches it? Where should
`Score` be set to `0`?

## Save your work

Save your Scratch project using your teacher's instructions. If you cannot
find the project next lesson, ask your teacher to help you reopen it or make
a fresh copy before you continue.
