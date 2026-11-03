---
title: "Lesson 2: Add Walls and a Finish"
description: Stop the player passing through maze walls and add a clear finish point.
order: 2
draft: false
---

## Today you will

Add a wall check to your movement and make a clear finish point for the maze.

## Starter: predict the collision

The player moves right by 5. If it touches a wall, what coordinate change
could move it back to where it was?

## Stop at the walls

Use the same wall colour throughout your maze. After each movement, check if
the player is touching that colour. If it is, reverse that movement.

```text
If right arrow pressed? then
    Change x by 5
    If touching wall colour? then
        Change x by -5
```

Repeat the pattern for the other directions:

| Direction | Move first | Move back if touching a wall |
| --- | --- | --- |
| Right | Change X by `5` | Change X by `-5` |
| Left | Change X by `-5` | Change X by `5` |
| Up | Change Y by `5` | Change Y by `-5` |
| Down | Change Y by `-5` | Change Y by `5` |

Use Scratch's `touching color?` sensing block and choose the colour you used
for the walls. Make the collision check inside the matching key condition.

## Test one direction at a time

Move the player slowly towards each wall. If the player slips through, try a
smaller movement step or make sure the collision check happens immediately
after the movement.

## Add a finish

Make the finish easy to see. You could draw a coloured exit area on the
backdrop or add an Exit sprite. For now, test that the player can reach it.
The next lesson will add a win response.

## Core task

- Test each of the four walls.
- Add the matching reverse movement when the player touches a wall.
- Keep the finish area reachable.

## Challenge choices

- Use a separate Exit sprite and place it at the end of the maze.
- Add a sound or speech bubble when the player touches the exit.
- Create a second maze with narrower passages, then check whether the player
  still fits.
- Add a short animation when the player reaches a wall.
- Change the step size and test whether collision remains reliable.

## Before you finish

- Does the player stay inside every wall?
- Can the player still move away from a wall?
- Can the player reach the exit?
- Does the green flag return the player to the start?

## Save your work

Save your Scratch project using your teacher's instructions. If you cannot
find the project next lesson, ask your teacher to help you reopen it or make
a fresh copy before you continue.
