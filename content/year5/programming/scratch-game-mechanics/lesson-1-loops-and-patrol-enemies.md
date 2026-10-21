---
title: Loops and Patrol Enemies
description: Use repeat and forever loops to bring a patrolling enemy to life in Scratch.
order: 1
draft: false
---

Games use loops to keep things happening. A game repeatedly checks your controls, moves characters, and looks for collisions. Without loops, those actions would happen only once.

## What is a loop?

A **loop** repeats instructions. Instead of adding the same blocks again and again, put them inside a loop.

Scratch has two useful loops:

- **Repeat** runs the blocks inside it a set number of times, then moves on.
- **Forever** keeps running the blocks inside it until the game or script stops.

Use **repeat** for a task that should happen a certain number of times. Use **forever** for something that needs to keep happening during the game, like an enemy patrol.

## Make a patrol enemy

Choose an enemy sprite. Add these blocks to its script:

1. Start with **when green flag clicked**.
2. Add a **forever** loop.
3. Inside the loop, add **move 3 steps** and **if on edge, bounce**.
4. Add **set rotation style left-right** before the loop so the enemy does not turn upside down.

Click the green flag. Your enemy should patrol across the stage and turn around at each edge. Change the number of steps to change its speed.

## Challenges

### Bronze

Build the patrol script above. Make sure the enemy turns around at both edges of the stage.

### Silver

Add a second costume to the enemy. Inside the forever loop, use **next costume** and **wait 0.2 seconds** so it looks animated as it patrols.

### Gold

Add a player sprite. Make the enemy broadcast a **Game Over** message when it touches the player. Create a receiver script that responds to the message by showing a Game Over message or changing the backdrop.

### Platinum

Add a second enemy with a different speed. Make sure touching either enemy triggers Game Over.

### Extension

Create a patrol route with several turning points instead of bouncing at the stage edges. Try using **repeat** to move between points, and use **forever** to keep repeating the route.

## Reflect

How is a repeat loop different from a forever loop? Which loop did your enemy need, and why? What changed when you adjusted its speed?

## Share and submit

Click **Share** on your Scratch project. Copy the project link from your browser, then submit that link using the course's **Submit Work** link. Check that your shared link opens your game before you submit it.