---
title: "Lesson 2: Tune Movement and Stop at Walls"
description: Reuse the Year 5 maze movement and wall-collision pattern, then tune the step size and make the player face left and right.
order: 2
draft: false
---

## Today you will

Build four-way controls using the Year 5 maze pattern, then tune the
movement so the player can navigate the narrower passages in both levels.

## Starter: predict the movement

In Scratch, X increases to the right and Y increases upwards. Predict what
happens when the player moves:

- right: increase or decrease X?
- left: increase or decrease X?
- up: increase or decrease Y?
- down: increase or decrease Y?

If you need a starting point, download the [sample project with a single maze
and player movement](/downloads/QuickMaze.sb3).

## Reuse the Year 5 pattern

Use the same [movement pattern from Year 5](/year5/programming/maze-collector/L01-Maze-Map-and-Movement)
and [wall-collision pattern from Year 5](/year5/programming/maze-collector/L02-Walls-and-Finish).
Start with a movement step of `5`, then tune it for your mazes.

Choose one wall colour and use it consistently on both backdrops. After
each movement, check whether the player touches that colour; if so, undo
that movement.

```text
When green flag clicked
Go to x: (Level 1 start X) y: (Level 1 start Y)
Forever
    If right arrow pressed? then
        Change x by 5
        If touching wall colour? then
            Change x by -5
    If left arrow pressed? then
        Change x by -5
        If touching wall colour? then
            Change x by 5
    If up arrow pressed? then
        Change y by 5
        If touching wall colour? then
            Change y by -5
    If down arrow pressed? then
        Change y by -5
        If touching wall colour? then
            Change y by 5
```

In Scratch, use four separate `if` blocks inside one `forever` loop. The
collision check must happen immediately after the matching movement. Use
Scratch's `touching color?` block and select your wall colour.

## Tune the step size

Try a step of `2`, `4`, and `6`. Change every movement and matching
wall-check value together. A larger step moves faster, but may jump over
thin walls or make narrow corridors difficult to navigate.

| Step size | How it feels | Can you get through narrow routes? |
| ---: | --- | --- |
| 2 | | |
| 4 | | |
| 6 | | |

Choose one step size that works reliably on both levels.

## Make the player face left and right

If the player costume faces right by default, add this before the movement
loop:

```text
Set rotation style [left-right]
```

In the left-arrow check, point in direction `-90`; in the right-arrow
check, point in direction `90`. If the sprite faces the wrong way, edit or
flip its costume. Keep vertical movement from changing its facing direction.

## Core task

- Add the four arrow-key controls and wall checks.
- Use the same movement step in both maze backdrops.
- Make the player face the direction it moves horizontally.
- Test that the player cannot pass through any wall.

## Test your controls

| Test | Expected result |
| --- | --- |
| Press each arrow key | The player moves in the matching direction |
| Press left or right | The player faces the direction of travel |
| Move slowly into each wall | The player stays on the path |
| Try the narrowest passage | The player can pass without slipping through walls |
| Restart the project | The player returns to the Level 1 start |

## Record your evidence

Record the step size you chose and one test that showed the wall checks
worked. Explain why the same step size needs to be used in the movement and
the reverse movement.

## Exit check

What happens if the movement step is too large for a narrow passage? Why
must the wall check immediately follow the movement?

## Save your work

Save your Scratch project using your teacher's instructions.
