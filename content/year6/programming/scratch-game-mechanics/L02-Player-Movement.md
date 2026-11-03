---
title: "Lesson 2: Control the Player"
description: Use a forever loop, keyboard checks, and coordinates to control a player sprite.
order: 2
draft: false
---

## Today you will

Make the player respond to keyboard controls and test whether the controls
feel clear and reliable.

## Starter: predict the coordinates

In Scratch, X increases to the right and Y increases upwards. Complete these
statements in your book:

- To move right, increase or decrease X?
- To move left, increase or decrease X?
- To move up, increase or decrease Y?
- To move down, increase or decrease Y?

## Build keyboard controls

Open the project from Lesson 1 and select the player sprite. Start it at a
useful position when the green flag is clicked.

Use four key checks inside a `forever` loop:

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

The loop repeatedly checks whether a key is being pressed. Without it, the
script would check only once. If the player moves too quickly or slowly,
change the step size and test again.

If your game idea uses a different control, first make the arrow-key
version work, then ask your teacher before adapting it.

## Core task

- Add four-way movement to your player.
- Make the green flag put the player back at the start.
- Check that the player stays visible on the Stage.
- Choose a movement speed that is easy to control.

## Challenge choices

- Add left- and right-facing costumes.
- Animate the player while a key is pressed.
- Make the player stop at the edge of the Stage.
- Compare two movement speeds and record which is easier to control.
- Add a simple boundary or wall and plan how to stop the player crossing
  it next lesson.

## Test the controls

| Test | Expected result |
| --- | --- |
| Press right arrow | X increases and the player moves right |
| Press left arrow | X decreases and the player moves left |
| Press up arrow | Y increases and the player moves up |
| Press down arrow | Y decreases and the player moves down |
| Click the green flag again | The player returns to the start |

## Record your evidence

Record one movement test, its result, and whether you changed the movement
speed. Sketch the key blocks or describe the script in your project log.
You do not need to upload evidence this lesson.

## Exit check

What does the `forever` loop repeatedly check? Which coordinate changes
when the player moves upwards?

## Save your work

Save your Scratch project using your teacher's instructions.
