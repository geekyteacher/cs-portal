---
title: "Lesson 5: Connect Levels and Manage Game State"
description: Use a reusable custom block to change levels and check the win and game-over conditions, then test and present the game.
order: 5
draft: false
---

## Today you will

Connect both mazes, use a custom block to manage the game state, test the
win and game-over rules, and prepare a short demonstration.

## Starter: make the win rule precise

The player must collect at least three points **and** reach the exit to
complete each level. Reaching the Level 1 exit moves to Level 2; reaching
the Level 2 exit with the score target met wins the game.

## Set up the game state

Create a `Game State` variable for all sprites. On the Stage, when the
green flag is clicked, set `Level` to `1`, `Score` to `0`, `Lives` to `3`,
and `Game State` to `Playing`. Switch the backdrop to `Maze 1`, then
broadcast `Start Game`. The player's existing start script should place it
at the Level 1 start.

```text
When green flag clicked
Set Level to 1
Set Score to 0
Set Lives to 3
Set Game State to [Playing]
Switch backdrop to [Maze 1]
Broadcast [Start Game]
```

Add a second exit position. Make the Exit sprite move to the Level 2 exit
when it receives the `Level 2` message:

```text
When green flag clicked
Go to x: (Level 1 exit X) y: (Level 1 exit Y)

When I receive [Level 2]
Go to x: (Level 2 exit X) y: (Level 2 exit Y)
```

On the Stage, switch backdrops when messages arrive:

```text
When I receive [Level 2]
Switch backdrop to [Maze 2]

When I receive [You Win]
Switch backdrop to [You Win]

When I receive [Game Over]
Switch backdrop to [Game Over]
```

Name the backdrops `Maze 1`, `Maze 2`, `You Win`, and `Game Over`.

## Create the custom block

Select the player sprite. In **My Blocks**, make a custom block called
`check game state`. It handles zero lives, the Level 1 exit, and the Level
2 win:

```text
define check game state
If <Game State = [Playing]> then
    If <Lives = 0> then
        Set Game State to [Game Over]
        Broadcast [Game Over] and wait
        Stop all
    If <<touching Exit?> and <Score >= 3>> then
        If <Level = 1> then
            Set Game State to [Changing Level]
            Set Level to 2
            Set Score to 0
            Broadcast [Level 2] and wait
            Go to x: (Level 2 start X) y: (Level 2 start Y)
            Set Game State to [Playing]
        Else
            Set Game State to [Won]
            Broadcast [You Win] and wait
            Stop all
```

Call the custom block repeatedly while the game is being played:

```text
When I receive [Start Game]
Forever
    check game state
```

The `Level 2` message changes the backdrop, moves the exit, and tells the
items from Lesson 3 to move to their Level 2 positions and reappear. The
player keeps any remaining lives, but the score resets for the new level.
The patrol should stay on a safe route in both mazes.

The custom block is a reusable procedure: the game calls the same named
group of instructions repeatedly instead of copying the win/loss checks
into several scripts.

## Test, improve, and prepare to share

Test each condition before presenting the game:

| Test | Expected result |
| --- | --- |
| Start the game | Level 1, score `0`, lives `3`, and the `Maze 1` backdrop |
| Touch the Level 1 exit with fewer than 3 points | Stay on Level 1 |
| Reach the Level 1 exit with at least 3 points | Switch to Level 2; score resets |
| Enter Level 2 | Player, exit, and items use their Level 2 positions |
| Reach the Level 2 exit with fewer than 3 points | Stay on Level 2 |
| Reach the Level 2 exit with at least 3 points | Show the `You Win` backdrop |
| Lose all 3 lives | Show the `Game Over` backdrop |
| Click the green flag after an ending | Restart from Level 1 with score `0` and lives `3` |

Ask a partner to play without explaining every step. Record one issue or
suggestion, make one improvement, and repeat the test that revealed it.

Prepare to show the two levels and explain one script, such as the wall
check, the bonus key, the life penalty, or `check game state`.

## Core task

- Connect the two maze backdrops with the `Level 2` message.
- Create and call the `check game state` custom block.
- Require at least 3 points and the exit to complete each level.
- Show the correct win or game-over backdrop.
- Test the game, make one improvement, and prepare to demonstrate it.

## Record your evidence

Keep your completed test table. Record the improvement you made and the
result of the repeated test. Be ready to demonstrate your game in class.

## Exit check

Why does the win condition need both `Score >= 3` and touching the exit?
What instructions are reused by `check game state`?

## Save your work

Save your Scratch project using your teacher's instructions. Make sure the
project opens and restarts correctly before you present it.
