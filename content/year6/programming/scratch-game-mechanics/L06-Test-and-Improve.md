---
title: "Lesson 6: Test, Debug, and Improve"
description: Use planned tests and peer feedback to find a problem and improve the game.
order: 6
draft: false
---

## Today you will

Test your game systematically, use evidence to find a problem, and make
one improvement.

## Starter: bug or design choice?

A player says, “I keep losing, and I don't know why.” Is this necessarily a
bug, or could the game be too difficult or unclear? What test would help
you find out?

## Plan your tests

Write what should happen before you run each test. Try to include normal
play, an unusual situation, and a restart.

| Test | What I will try | Expected result | Actual result |
| --- | --- | --- | --- |
| Controls | Try each control | Player responds correctly | |
| Interaction | Collect or hit one item | Progress changes once | |
| Challenge | Touch or avoid the hazard | Correct response happens | |
| Goal | Meet or fail the win condition | Correct ending appears | |
| Restart | Start the game again | Values return to their start state | |

Change these tests to match your game. A useful test checks one thing at a
time.

## Peer playtest

Ask a partner to play your game without explaining every step. Watch
carefully and record:

- what they understood straight away;
- where they got stuck or confused;
- whether the controls and challenge felt fair; and
- one suggestion they made.

Give feedback that is kind and specific. “I couldn't tell what the target
was” is more useful than “It's bad.”

## Fix or improve one thing

Choose one problem supported by your tests or the playtest. Make one
change, then repeat the test that revealed the problem.

| Problem or suggestion | Change I made | Test I repeated | Result |
| --- | --- | --- | --- |
| | | | |

If the test still fails, inspect the script that controls that feature.
Check the event block, loop, condition, sprite name, and variable value.

## Challenge choices

- Adjust the movement speed or hazard speed to improve difficulty.
- Add an instruction that would have helped your playtester.
- Test an unusual case, such as restarting while the game is over.
- Ask a second person to test the improved version.
- Make a second change only after the first one has been tested.

## Record your evidence

Keep your completed test table. Record the change and whether the repeated
test passed, and include the playtester's feedback. If you can upload
evidence, this is a useful point to submit the test result and a screenshot
of the improvement. Otherwise, keep the evidence in your project log.

## Exit check

Which test result led to your change? What evidence shows whether the
change helped?

## Save your work

Save your Scratch project and make sure it opens before the showcase next
lesson.
