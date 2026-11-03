---
title: "Lesson 1: Design the Maze and Move the Player"
description: Plan a maze and use Scratch coordinates and a forever loop to move a player sprite.
order: 1
draft: false
---

## Today you will

Plan a single-screen maze and make a player sprite move using the arrow keys.

## Starter: be the sprite

Look at a coordinate grid with a start, a finish, and a barrier. On paper,
write which coordinate change would move the sprite in each direction:

- right: increase or decrease X?
- left: increase or decrease X?
- up: increase or decrease Y?
- down: increase or decrease Y?

Remember: in Scratch, X increases to the right and Y increases upwards.

## Plan your maze

The Scratch stage is one screen, **480 steps wide by 360 steps high**. Keep
the maze to one screen so it is large enough to see and play. A simple
planning grid of 8 columns by 6 rows gives you 60 stage steps per square.

On paper, sketch a maze with:

- a clear start;
- a route that can be followed without tiny gaps;
- passages wider than your player's visible sprite; and
- a finish in a different place from the start.

Keep the first maze simple, with only a few turns and dead ends. Leave space
for one enemy to patrol along a straight passage. You can make the maze
harder after the controls work.

## Build four-way movement

Choose a player sprite and a maze backdrop. Put this script on the player:

```text
When green flag clicked
Go to x: (start X) y: (start Y)
Forever
    If right arrow pressed? then
        Change x by 5
    If left arrow pressed? then
        Change x by -5
    If up arrow pressed? then
        Change y by 5
    If down arrow pressed? then
        Change y by -5
```

In Scratch, use four separate `if` blocks inside the same `forever` loop.
Replace `(start X)` and `(start Y)` with the coordinates of your start point.
If the movement feels too fast or too slow, change `5` to a smaller or
larger step and test again.

## Core task

- Make a maze backdrop or choose a suitable backdrop and draw the walls.
- Put the player at the start when the green flag is clicked.
- Make all four arrow keys move the player in the correct direction.
- Test that the player can reach the finish area.

## Challenge choices

Choose one challenge if the core controls work:

- Add or draw costumes so the player faces left and right correctly.
- Add a second pair of costumes and animate the player while moving.
- Add a start screen with the game title and instructions.
- Design a more interesting maze with a dead end or a choice of routes.
- Change the movement step and compare which value feels easiest to control.
- Add a simple enemy sprite and plan a straight corridor where it could
  patrol later.

## Test your controls

| Test | Expected result |
| --- | --- |
| Press right arrow | X increases and the player moves right |
| Press left arrow | X decreases and the player moves left |
| Press up arrow | Y increases and the player moves up |
| Press down arrow | Y decreases and the player moves down |
| Click the green flag again | The player returns to the start |

## Exit check

Which coordinate changes when the player moves up? What does the `forever`
loop make Scratch keep checking?

## Save your work

Save your Scratch project using your teacher's instructions. If you cannot
find the project next lesson, ask your teacher to help you reopen it or make
a fresh copy before you continue.
