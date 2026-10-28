---
title: "Halloween Ghost Catcher Game"
description: Make a Scratch ghost move around the screen, then click it to score points.
order: 1
draft: false
---
## Today’s mission

Make a ghost move around the screen. Then make it react when you click it.

By the end, you should be able to:

- use a `forever` loop to repeat instructions;
- move a sprite to random places;
- use costumes, sounds, and a score variable; and
- test and improve a game.

## 1. Open the project

1. Log in and open **My Stuff**.
2. Click the folder icon, then open **My Studios**.
3. Choose your class studio.
4. Open **Halloween Game 1 Template**.
5. Click **Remix** to create your own copy.

The project already has sprites, backdrops, and some Stage code. **Leave the
existing Stage code in place.**

## 2. Make the ghost move

Click the ghost sprite. Build a script that starts when the green flag is
clicked:

1. Set **Score** to `0`. This block goes before the loop so the score does
   not keep resetting.
2. Add a `forever` loop.
3. Inside the loop, switch to costume `ghost-a`.
4. Glide to a random position over 2 seconds.
5. Turn a random amount between `1` and `90` degrees.
6. Switch to costume `ghost-d`.
7. Glide to another random position over 2 seconds.
8. Turn a random amount between `1` and `90` degrees again.

The `forever` loop repeats the movement, so the ghost keeps moving until the
game stops.

![Scratch blocks that set the score to zero, then forever switch the ghost costume, glide to random positions, and turn a random amount.](/images/halloween-ghost-catcher/ghost-movement.png)

### Text version

```text
When green flag clicked
Set score to 0
Forever
    Switch costume to ghost-a
    Glide for 2 seconds to a random position
    Turn clockwise by a random amount from 1 to 90 degrees
    Switch costume to ghost-d
    Glide for 2 seconds to a random position
    Turn clockwise by a random amount from 1 to 90 degrees
```

## 3. Make the ghost react to a click

Add a second script to the ghost sprite. When clicked, it should make a
sound, change costume, and add one point to **Score**.

![Scratch blocks that play the screech sound, switch to costume ghost-c, increase Score by one, and wait half a second when the ghost is clicked.](/images/halloween-ghost-catcher/ghost-click.png)

### Text version

```text
When this sprite clicked
Start sound screech
Switch costume to ghost-c
Change score by 1
Wait 0.5 seconds
```

## 4. Add the music

Click the **Stage** and add a script to play the creepy music in a loop.

![Scratch blocks that repeat the creepy music forever when the green flag is clicked.](/images/halloween-ghost-catcher/stage-music.png)

### Text version

```text
When green flag clicked
Forever
    Play sound creepy music until done
```

## 5. Test your game

Click the green flag and check:

- Does the ghost move to different places?
- Does the music play?
- What happens when you click the ghost?
- Does the score increase?

If something does not work, check that each script starts with the correct
event block and that the movement blocks are inside the `forever` loop.

## Finished early?

- Right-click the ghost sprite to duplicate it and add more ghosts.
- Change the ghosts’ movement speeds so some are easier to catch than others.
- Try making different ghosts worth different numbers of points.
- Add a countdown: catch 10 ghosts before time runs out. If the timer reaches
  zero, show a **Game Over** message.

## Check your work

Before handing in, check:

- [ ] The score starts at zero.
- [ ] The ghost moves to random places and changes costume.
- [ ] Clicking the ghost plays a sound and increases the score.
- [ ] The Stage music plays.
- [ ] I tested my game with the green flag.

## Hand in your work

Save your project as your teacher has shown you. Use the submission link for
your class at the bottom of this page to send in your work.
