---
title: "Lesson 4: Create a Win Condition"
description: Make the player win by collecting items and reaching the maze exit.
order: 4
draft: false
---

## Today you will

Add a patrol enemy and use conditions to decide when the player is caught or
has completed the maze.

## Starter: what must be true?

For the player to win, they must collect three items **and** reach the exit.
Can the player win if they do only one of these things?

## Add one patrol enemy

Choose an enemy sprite and place it in a straight corridor. Make it move
between two points using Scratch's **glide** blocks:

```text
When green flag clicked
Go to x: (first point X) y: (first point Y)
Forever
    Glide 2 seconds to (second point)
    Glide 2 seconds to (first point)
```

Add a separate script to check if the enemy touches the player:

```text
When green flag clicked
Forever
    If touching Player? then
        Broadcast [Caught]
        Wait until not touching Player
```

On the player, respond to the message by returning to the start:

```text
When I receive [Caught]
Go to x: (start X) y: (start Y)
```

The score stays the same when the player is caught. Test that the enemy's
route stays inside its corridor and that the player can try again.

## Check for a win

On the Exit sprite, make a script that keeps checking whether the player is
touching the exit and has enough points:

```text
When green flag clicked
Forever
    If <touching Player?> and <Score >= 3> then
        Broadcast [You Win] and wait
        Stop all
```

Use a green flag script on the Stage to respond to the message:

```text
When I receive [You Win]
Switch backdrop to [You Win]
```

You can make a simple `You Win` backdrop with a message. If the win message
does not appear, test the score condition and the exit touch separately.

## Core task

- Add one enemy that patrols between two points.
- Return the player to the start if the enemy touches them.
- Show a win message when the player reaches the exit with at least three
  points.
- Check that reaching the exit with fewer than three points does not win.
- Check that collecting enough items but not reaching the exit does not win.

## Challenge choices

Choose one extension and test it:

- Add a second enemy with a different patrol route.
- Add lives and show a game-over message when they reach zero.
- Add a countdown timer that starts at 30.
- If the timer reaches zero before the player wins, show a `Time's up` screen.
- Add a restart button that starts a new game with the score reset.
- Add a second exit that requires a different score.
- Add a victory sound or animation.

For a timer, keep it separate from the movement script. Make sure the timer
stops changing after the player wins or loses.

## Test the win rule

| Score | At exit? | Expected result |
| --- | --- | --- |
| 2 | Yes | Keep playing; no win yet |
| 3 | No | Keep playing |
| 3 | Yes | Show the win message |

Also test that touching the enemy returns the player to the start.

## Exit check

What happens when the player touches the enemy? Why does the win rule use
`and` between the score check and touching the exit?

## Save your work

Save your Scratch project using your teacher's instructions. If you cannot
find the project next lesson, ask your teacher to help you reopen it or make
a fresh copy before you continue.
