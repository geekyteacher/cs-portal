---
title: "Lesson 7: Test and Debug a Quiz"
description: Test another student's quiz, report useful evidence, and fix errors.
order: 7
draft: false
---

## Today you will

Test a partner's quiz systematically, identify errors, and help verify that
any fixes work.

## Testing agreement

Swap programs with a partner. Run only the program they have agreed to share.
Do not change their original file; write down the tests and results first.

## Test the quiz

Use this table to check the program. Add extra tests if you find a problem.

| Test | Input or action | Expected result | Actual result |
| --- | --- | --- | --- |
| Correct answer | Enter a correct answer | Correct feedback and score increases | |
| Incorrect answer | Enter a wrong answer | Incorrect feedback and score stays the same | |
| Final score | Finish the quiz | Score matches correct answers | |
| Replay yes | Choose `yes`, if replay exists | A new quiz starts with a fresh score | |
| Replay no | Choose `no`, if replay exists | The program ends | |
| Capital letters/spaces | Try a different case or extra spaces | Record whether it is accepted | |

For the capitalisation test, first observe what the program does. If the
program is intended to accept variations, the programmer can use
`.strip().lower()` on the answer and compare with a lowercase expected value:

```python
answer = input("Your answer: ").strip().lower()

if answer == "paris":
    print("Correct!")
```

`.strip()` removes spaces from the beginning and end; `.lower()` converts
letters to lowercase. The expected answer must also use lowercase. To count
a correct response, `score += 1` is a shorter form of `score = score + 1`.

## Report a useful bug

For each issue, record:

1. **Input:** what you entered or did.
2. **Expected:** what you thought should happen.
3. **Actual:** what happened instead.
4. **Location:** the question or part of the program where it happened.

Check for:

- a score that does not increase after a correct answer;
- feedback that does not match the answer;
- an incorrect final score;
- spelling or unclear instructions;
- a replay loop that will not stop; and
- a loop that does not ask for updated input.

## Fix and retest

Give the program back to its author with your notes. The author chooses which
suggestions to use, fixes the code, and repeats the failed test. A fix is not
verified until the test now produces its expected result.

If a loop keeps running, use the editor's stop button. Then inspect whether
the loop condition can change and whether the program updates the relevant
variable inside the loop.

## Reflection

Write:

- one bug you found or one test that confirmed the program worked;
- the evidence that helped you identify it; and
- the result after the program was retested.

## Exit check

Why is "I tried it and it seemed fine" weaker evidence than recording the
input, expected result, and actual result?

## Answers

A recorded test makes it clear what was checked and whether the result
matched expectations. It helps another person repeat the test and verify a
fix.
