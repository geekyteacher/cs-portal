---
title: "Lesson 4: Add a Patrol Hazard and Lives"
description: Create a patrol hazard that removes one life per collision, flashes the player, and sends them back to a safe point.
order: 4
draft: false
---

## Today you will

Add a patrol hazard and a `Lives` variable. When the player is caught,
they lose one life, flash, and return to the safe point for their current
level.

## Starter: plan a fair hazard

Look at both maze maps. Mark a straight corridor where a hazard can patrol
without blocking the only route. How can the player get past it?

## Create and reset lives

Create a `Lives` variable for all sprites. When the green flag is clicked,
set `Lives` to `3`. Do not reset lives when the player moves to Level 2.

## Make the patrol

Choose an enemy sprite and a clear patrol route. Use Scratch's glide blocks
to move it between two points:

```text
When green flag clicked
Go to x: (first point X) y: (first point Y)
Forever
    Glide 2 seconds to (second point)
    Glide 2 seconds to (first point)
```

Use matching coordinates for the patrol route on both maze backdrops, so
the same enemy can patrol safely on each level. Keep the route out of walls
and give the player room to get past.

## Detect one collision at a time

On the hazard, check for contact in a loop and wait until the sprites are
apart before checking again:

```text
When green flag clicked
Forever
    If touching Player? then
        Broadcast [Caught] and wait
        Wait until not touching Player
```

On the player, respond to `Caught`:

```text
When I receive [Caught]
Change Lives by -1
If <Lives > 0> then
    If <Level = 1> then
        Go to x: (Level 1 safe reset X) y: (Level 1 safe reset Y)
    Else
        Go to x: (Level 2 safe reset X) y: (Level 2 safe reset Y)
    Repeat 3
        Set [ghost] effect to 50
        Wait 0.1 seconds
        Clear graphic effects
        Wait 0.1 seconds
```

The `wait until not touching` block prevents one long collision from
removing several lives. The player returns to the current level's safe
point and keeps their score. If `Lives` reaches `0`, Lesson 5's game-state
check will show the game-over screen.

## Core task

- Start with `3` lives.
- Make the hazard patrol a safe route.
- Remove exactly one life for each collision.
- Flash and return the player to the current level's safe point.
- Keep the game running while at least one life remains.

## Test the hazard

| Test | Expected result |
| --- | --- |
| Click the green flag | `Lives` becomes `3` |
| Touch the hazard once | `Lives` decreases by `1` |
| Stay in contact briefly | Only one life is lost |
| Touch the hazard again | One more life is lost |
| Lose a life in Level 2 | Player returns to the Level 2 safe point |
| Reach zero lives | Lesson 5 will show the game-over ending |

## Record your evidence

Record one test that proves a single collision removes only one life.
Describe how the player is given a chance to continue.

## Exit check

Why does the hazard wait until the player is no longer touching it? Which
safe point should the player return to on Level 2?

## Save your work

Save your Scratch project using your teacher's instructions.
