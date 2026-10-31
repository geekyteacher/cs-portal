---
title: Mixed Practice and Checkpoint
description: Review and assess processor architecture, assembly language, and bit manipulation.
order: 4
draft: false
---

## Purpose

Use this checkpoint in Double 10 of the [unit plan](./index), after teaching
the three content areas. Allow time to review answers and reteach any weak
areas.

## Retrieval warm-up

Without notes, write:

1. The purpose of the PC, MAR, MDR, CIR, ACC, and IX.
2. The order of the fetch-execute cycle, including `PC -> MAR`.
3. One difference between direct and indirect addressing.
4. The result of one logical operation and one shift.

## Mixed practice

Complete the questions using the instruction set, register names, and
operations specified in the 9618 syllabus.

### A. Processor operation

1. Memory location 100 contains `LDD 200`; memory location 200 contains 37.
   The initial values are `PC = 100` and `ACC = 0`. Trace the fetch,
   decode, operand fetch, and execution. Record changes to PC, MAR, MDR,
   CIR, and ACC.
2. Explain which buses are used during the instruction fetch and the
   operand fetch.
3. A timer sends an interrupt request while a program is running. Describe
   when it can be handled, the purpose of the ISR, and how the interrupted
   program resumes.
4. Explain one advantage and one limitation of adding more processor cores.

### B. Assembly language

Assume `Memory[30] = 0`.

```text
LDM #60
ADD #5
STO 30
CMP #65
JPE DONE
LDM #66
DONE: OUT
END
```

1. Trace the ACC and `Memory[30]` after each instruction.
2. Explain why the `LDM #66` instruction is or is not executed.
3. State the character output by `OUT` using the ASCII value in the ACC.
4. Describe what the first pass and second pass of a two-pass assembler do
   with the label `DONE`.
5. Explain the difference between indexed and indirect addressing.

### C. Bit manipulation

1. Calculate `11010110 XOR 00001111`.
2. Calculate the one-place logical right shift of `10010110`.
3. Use an AND mask to test bit 4 of `10010110` (rightmost bit is bit 0).
   State whether the bit is set.
4. Use an OR mask to set bit 2 of `10010000`.

## Self-assessment

For each area, mark **secure**, **nearly there**, or **need more practice**:

| Area | Self-assessment | My next action |
| --- | --- | --- |
| Processor components, registers, and buses |  |  |
| Fetch-execute cycle and register-transfer notation |  |  |
| Interrupts, peripheral ports, and performance |  |  |
| Assembler, instruction set, and addressing modes |  |  |
| Reading, tracing, writing, and debugging assembly |  |  |
| Logical operations, shifts, and masks |  |  |

## Follow-up

Choose one area marked **nearly there** or **need more practice**. Revisit
the relevant teaching page, complete one additional question, and explain
what you corrected.

## Homework

Finish any unanswered checkpoint question and correct your work in a
different colour using the teacher's feedback or mark scheme.
