---
title: "Lesson 4: Add a Moving Challenge"
description: Add a moving hazard or enemy and use a condition to make contact affect the game.
order: 4
draft: false
---

## Today you will

Add a moving challenge and decide what should happen when it touches the
player.

## Starter: predict the condition

Complete this rule:

> If the player touches the hazard, then __________.

Possible responses include returning to the start, losing a life, losing
points, or ending the game. Choose one response that suits your game.

## Make a patrol

Add an enemy or hazard sprite. Start it at one end of a clear route and
make it move between two points:

```text
When green flag clicked
Go to x: (first point X) y: (first point Y)
Forever
    Glide 2 seconds to (second point)
    Glide 2 seconds to (first point)
```

You can change the travel time to adjust the speed. Make sure the patrol
stays in an area the player can see.

## Respond to contact

Add a separate script to check whether the hazard touches the player:

```text
When green flag clicked
Forever
    If touching Player? then
        Broadcast [Caught]
        Wait until not touching Player
```

On the player, respond to `Caught`. For a simple first version, return the
player to the start:

```text
When I receive [Caught]
Go to x: (start X) y: (start Y)
```

The `wait until not touching` block prevents the hazard from sending the
message continuously while the sprites remain in contact. If you choose a
different penalty, make sure the player has a chance to try again.

## Core task

- Add one hazard or enemy that moves repeatedly.
- Make contact trigger one clear response.
- Test that the hazard follows its route.
- Check that the player can recover and continue.

## Challenge choices

- Use a `Lives` variable and reduce it when the player is caught.
- Add a second hazard with a different route or speed.
- Make the hazard reverse direction when it reaches an edge.
- Add a short invincibility period after the player is caught.
- Add a sound or costume effect when contact happens.

## Test the challenge

| Test | Expected result |
| --- | --- |
| Click the green flag | Hazard starts at its first point |
| Wait and watch | Hazard moves between its two points |
| Touch the hazard | The chosen penalty happens |
| Move away and touch again | A new contact can trigger the response |

## Record your evidence

Record what happens on contact and one test showing that the player can
keep playing. Sketch the hazard or contact blocks, or describe how the
collision is detected and handled. A screenshot is optional.

## Exit check

Why is the contact check in a loop? What problem does `wait until not
touching Player` help prevent?

## Save your work

Save your Scratch project using your teacher's instructions.
