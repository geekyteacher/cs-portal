---
title: "Lesson 3: Add Interactions and Score"
description: Make sprites respond to the player and use a variable to show progress in the game.
order: 3
draft: false
---

## Today you will

Make an object respond when the player reaches it, then use a variable to
show progress.

## Starter: retrieve your variable knowledge

Your quiz used a variable to store information. For a game, what could a
variable keep track of? Suggest one value that might go up and one that
might go down.

## Create a score

Open your game and create a variable called `Score` for all sprites. Reset
it when the game starts:

```text
When green flag clicked
Set Score to 0
```

Set the score once at the start, not inside the player's movement loop.

## Make an object respond

Choose an item or target sprite. For a collectible, make it disappear after
the player touches it so the same item cannot keep adding points:

```text
When green flag clicked
Show
Forever
    If touching Player? then
        Change Score by 1
        Hide
```

Use the correct player sprite name in the `touching` block. If your game
uses targets rather than collectibles, you could move the target to a new
position instead of hiding it.

The score variable and touch check use ideas you have already met in your
quiz and other Scratch work. The new part is connecting them to a game
interaction.

## Core task

- Reset `Score` to `0` when the game starts.
- Add at least three items or targets.
- Make each interaction change the score exactly once.
- Test that starting again resets the score.

## Challenge choices

- Make a special item worth more than one point.
- Add a sound or visual effect when an item is collected.
- Give a target a different point value.
- Add a message when the player reaches the target score.
- Make a collected item reappear in a different position.

## Test the interaction

| Test | Expected result |
| --- | --- |
| Click the green flag | Score becomes `0` |
| Touch or catch one item | Score increases once |
| Stay on the same item | Score does not keep increasing |
| Collect three items | Score becomes `3` |
| Restart the game | Score returns to `0` |

## Record your evidence

Record one test where the interaction worked and one test that checks it
does not happen repeatedly. Sketch the score and interaction blocks or
describe how they work. Keep the Scratch project saved; a screenshot is
optional.

## Exit check

Why does a collectible hide after it is touched? Where should the score be
reset?

## Save your work

Save your Scratch project using your teacher's instructions.
