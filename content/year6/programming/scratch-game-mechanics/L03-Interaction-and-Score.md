---
title: "Lesson 3: Add Collectibles and a Bonus Key"
description: Use a score variable for ordinary items and a special key, then plan where they appear on both maze levels.
order: 3
draft: false
---

## Today you will

Add three ordinary collectibles worth one point each and a special key
worth five points. Plan a position for each item on both levels.

## Starter: predict the score

The score starts at `0`. The player collects two ordinary items and then
the bonus key. What should the score show after each collection?

## Create the variables

Create `Score` and `Level` variables for all sprites. When the green flag
is clicked, set `Score` to `0` and `Level` to `1`. The score is reset when
the game starts and again when the player enters Level 2.

## Add ordinary collectibles

Add three item sprites. Put each one on a path in Level 1 and record a
second safe path position for it in Level 2. Use a separate script on each
item:

```text
When green flag clicked
Go to x: (Level 1 item X) y: (Level 1 item Y)
Show
Forever
    If touching Player? then
        Change Score by 1
        Hide
```

When the player reaches Level 2, the same items can reappear at their
Level 2 positions:

```text
When I receive [Level 2]
Go to x: (Level 2 item X) y: (Level 2 item Y)
Show
```

Use the correct player sprite name in the `touching` block. Hiding an item
after it is collected prevents it adding points repeatedly.

## Add the bonus key

Add a different-looking key sprite. Use the same pattern, but change the
score by `5`. Hide it after collection. When Level 2 begins, place it at
its planned Level 2 position and show it again.

```text
When green flag clicked
Go to x: (Level 1 key X) y: (Level 1 key Y)
Show
Forever
    If touching Player? then
        Change Score by 5
        Hide

When I receive [Level 2]
Go to x: (Level 2 key X) y: (Level 2 key Y)
Show
```

Make sure each item position is on a path, not inside a wall.

## Core task

- Create and initialise `Score` and `Level`.
- Add three ordinary items that each add one point.
- Add a special key that adds five points.
- Plan safe item positions on both backdrops.
- Test that each item only adds points once per level.

## Test the score

| Test | Expected result |
| --- | --- |
| Click the green flag | `Score` is `0` and `Level` is `1` |
| Touch an ordinary item | `Score` increases by `1` |
| Stay on an item | It does not keep adding points |
| Touch the bonus key | `Score` increases by `5` |
| Enter Level 2 | Items appear at their Level 2 positions |
| Restart the game | Items return to Level 1 positions and `Score` resets |

## Challenge

Make the bonus key appear at a random safe position in each level. Test
that it never appears inside a wall.

## Record your evidence

Draw or describe one item script. Record your test showing that a normal
item adds one point, the key adds five, and neither can be collected twice
in the same level.

## Exit check

Why does an item hide after collection? What must happen to the items when
the player enters Level 2?

## Save your work

Save your Scratch project using your teacher's instructions.
