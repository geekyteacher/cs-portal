---
title: "Assembly Language (CAIE 9618)"
description: "Read, trace, write, and debug short assembly-language routines using the CAIE 9618 instruction set."
order: 2
draft: false
---

<!-- ## Quick Navigation
* [1. Starter](#1-starter)
* [2. Quick Reference](#2-quick-reference)
* [3. Guided Practice](#3-guided-practice)
* [4. Core Practice Tasks](#4-core-practice)
* [5. Exit Check](#5-exit-check) -->

## Learning Objectives

- Explain the relationship between assembly language, machine code, and a two-pass assembler.
- Identify the syllabus instruction groups and addressing modes (`Immediate`, `Direct`, `Indirect`, `Indexed`, `Relative`).
- Dry-run and trace changes to registers (`ACC`, `IX`) and main memory.
- Write and debug short CAIE assembly routines.

---

## 1. Starter (5 mins — Forced Recall)

Answer these in your notebook before looking at the notes below:

1. In a Von Neumann CPU, which register holds the intermediate results of arithmetic and logic operations?
2. Which register holds the address of the *next* instruction to be fetched?
3. Why do programmers write in assembly language rather than pure binary machine code?

---

## 2. Learn: How to Read Assembly (The Whiteboard & Postbox Model)

Assembly language replaces binary machine code with human-readable **mnemonics**. Before execution, a **two-pass assembler** translates it:

- **Pass 1:** Scans the code and builds a symbol table mapping labels (e.g., `LOOP:`) to memory addresses.
- **Pass 2:** Translates opcodes and operands into binary machine code, replacing labels with their recorded addresses.

### The Mental Model

- **Accumulator (`ACC`):** Think of this as a **whiteboard on the teacher's desk**. Almost every calculation happens here.
- **Main Memory:** Think of this as a wall of **numbered postboxes** (`100`, `101`, `200`, etc.).
- **Opcode & Operand:** Every instruction has an **Opcode** (the action, e.g., `LDD`) and usually an **Operand** (the target, e.g., `200`).
- **Number Prefixes:**
  - `#` = Denary (`#12`)
  - `B` = Binary (`B00001100`)
  - `&` = Hexadecimal (`&0C`)

### The 5 Addressing Modes (Examiner Favourite)

| Mode | How the CPU finds the data | Example & Effect |
| :--- | :--- | :--- |
| **Immediate** | The operand *is* the actual value. | `LDM #5` → Put the literal number `5` into `ACC`. |
| **Direct** | The operand is the memory address containing the value. | `LDD 200` → Go to address `200`, copy the value into `ACC`. |
| **Indirect** | The address contains a pointer to another address. | `LDI 40` → Look in `40` (finds `200`), then load the value stored at address `200`. |
| **Indexed** | Add the Index Register (`IX`) to the base address. | `LDX 100` (if `IX = 3`) → Effective address = `103`; load `Memory[103]`. |
| **Relative** | Add an offset to the Program Counter (`PC`). | Branch at `120` (PC now `121`) with offset `+4` → Jump to `125`. |

### Core CAIE 9618 Instruction Set

| Group | Mnemonics & Action |
| :--- | :--- |
| **Data Movement** | `LDM #n`, `LDD <addr>`, `LDI <addr>`, `LDX <addr>`, `LDR #n`, `MOV IX`, `STO <addr>` |
| **Arithmetic** | `ADD #n` / `ADD <addr>`, `SUB #n` / `SUB <addr>`, `INC <reg>`, `DEC <reg>` |
| **Compare & Jump** | `CMP #n` / `CMP <addr>`, `CMI <addr>`, `JPE <label>`, `JPN <label>`, `JMP <label>` |
| **I/O & Control** | `IN`, `OUT`, `END` |

---

## 3. Guided Practice: Tracing Together (15 mins)

Never trace assembly in your head. Always build a step-by-step register grid.

Let's trace this routine together assuming `Memory[20] = 0` at the start:

```text
LDM #5
ADD #3
STO 20
LDD 20
```

| Instruction | ACC Before | Memory[20] Before | CPU Action | ACC After | Memory[20] After |
| :--- | :---: | :---: | :--- | :---: | :---: |
| `LDM #5` | 0 | 0 | Load immediate value `5` into `ACC` | **5** | 0 |
| `ADD #3` | 5 | 0 | Add literal `3` to `ACC` | **8** | 0 |
| `STO 20` | 8 | 0 | Copy `ACC` (`8`) into address `20` | 8 | **8** |
| `LDD 20` | 8 | 8 | Load contents of address `20` into `ACC` | **8** | 8 |

*Discussion check:* Why does `STO 20` leave `8` inside `ACC` instead of wiping it to `0`?

---

## 4. Core Practice: Paper Drills (25 mins)

Complete these tasks in your notebook using clean trace tables.

### Task 1: Addressing Mode Workout

Assume the following memory state before *each* separate instruction runs:

- `IX = 4`
- `Memory[40] = 100`
- `Memory[100] = 17`
- `Memory[104] = 99`

State the final value loaded into the `ACC` after executing each single instruction:

1. `LDM #40`
2. `LDD 40`
3. `LDI 40`
4. `LDX 100`

---

### Task 2: Tracing a Conditional Loop

Dry-run the routine below by constructing a trace table with columns for:

- `Instruction`
- `ACC`
- `Memory[50]`
- `Output`

Use ASCII values where:

- `65 = 'A'`
- `66 = 'B'`

Start with:

```text
Memory[50] = 2
```

```text
       LDD 50
LOOP:  CMP #0
       JPE DONE
       SUB #1
       STO 50
       LDM #65
       OUT
       LDD 50
       JMP LOOP

DONE:  LDM #66
       OUT
       END
```

---

### Task 3: Spot the Bugs

A student wrote this routine to read two characters from the keyboard and store the **second** one at address `300`, but it contains **three** errors.

Identify and fix them:

```text
IN
STO #300
IN
LDD 300
```

---

## 5. Stretch (Finished Early?)

Write a complete CAIE assembly routine that:

1. Initialises `IX` to `0`.
2. Loops 4 times to set memory locations:
   - `200`
   - `201`
   - `202`
   - `203`
   
   all to the value `#99`.
3. Ends cleanly with `END`.

---

## 6. Exit Check (5 mins)

Answer from memory before packing up:

1. What is the difference between **Pass 1** and **Pass 2** of a two-pass assembler?
2. What does `LDI 50` do differently from `LDD 50`?
3. Which instruction pair is used to make a conditional decision in CAIE assembly?

[↑ Back to top](#learning-objectives)