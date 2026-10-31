---
title: Assembly Language
description: Read, trace, write, and debug short assembly-language routines using the CAIE 9618 instruction set.
order: 2
draft: false
---

## Learning goals

- Explain the relationship between assembly language and machine code.
- Describe the two passes of an assembler.
- Recognise the syllabus instruction groups and addressing modes.
- Trace changes to registers and memory.
- Write and debug short assembly-language routines.

## Suggested teaching time

Use this page for Doubles 5–7 in the [unit plan](./index): first learn the
assembler and instruction set, then trace routines, then write and debug
programs.

## 1. Assembly language and the two-pass assembler

Assembly language uses mnemonics and operands to represent machine
instructions in a form that is easier for people to read. The assembler
translates the program into machine code.

In a **two-pass assembler**:

1. **Pass 1** scans the program and records the addresses associated with
   labels.
2. **Pass 2** translates the instructions into machine code, using the
   recorded label addresses to resolve references such as jumps.

An instruction consists of an **opcode** (the operation) and, where needed,
an **operand** (the value, register, or address used by the operation).
Labels identify instruction addresses and are written before a colon.

| Part | Meaning |
| --- | --- |
| **Label** | Optional symbolic name for an instruction address, for example `LOOP:`. |
| **Opcode** | The operation to perform, for example `LDM`, `ADD`, or `JMP`. |
| **Operand** | The value, register, address, or label used by the opcode. Some instructions have no operand. |

For numeric operands, the syllabus notation uses `#` for a decimal number,
`B` for a binary number, and `&` for a hexadecimal number. For example,
`#12`, `B00001100`, and `&0C` represent the same value.

## 2. Instruction groups

The syllabus instruction set includes these groups:

| Group | Instructions and purpose |
| --- | --- |
| **Data movement** | `LDM`, `LDD`, `LDI`, and `LDX` load values into the ACC; `LDR` loads an immediate value into IX; `MOV` copies the ACC to a register; `STO` stores the ACC in memory. |
| **Arithmetic** | `ADD` adds a value to the ACC; `SUB` subtracts a value from the ACC; `INC` and `DEC` add or subtract 1 from a register. |
| **Compare and conditional control** | `CMP` and `CMI` compare the ACC with a value or memory contents; `JPE` and `JPN` jump depending on whether the previous comparison was true or false. |
| **Unconditional control** | `JMP` jumps to an address. `END` returns control to the operating system. |
| **Input and output** | `IN` reads a character and stores its ASCII value in the ACC; `OUT` displays the character whose ASCII value is in the ACC. |

All questions assume one general-purpose register, the **ACC**, is
available. The **IX** is the index register. Use the syllabus instruction
table to check the precise operand form for an instruction.

### Core instruction examples

| Instruction | Effect |
| --- | --- |
| `LDM #5` | Load the immediate value 5 into the ACC. |
| `LDD 200` | Load the contents of memory address 200 into the ACC. |
| `LDI 40` | Use the contents of address 40 as the address to read, then load the contents of that second address into the ACC. |
| `LDX 100` | Add the contents of IX to 100 and load the contents of the calculated address into the ACC. |
| `LDR #3` | Load the immediate value 3 into IX. |
| `MOV IX` | Copy the contents of the ACC into IX. |
| `STO 200` | Store the contents of the ACC at memory address 200. |
| `ADD #2` | Add the immediate value 2 to the ACC. |
| `CMP #5` | Compare the ACC with the immediate value 5. |
| `JPE DONE` | If the previous comparison was true, jump to the instruction labelled `DONE`. |

## 3. Addressing modes

An addressing mode describes how an instruction locates its operand.

| Mode | How the operand is found | Syllabus instruction example |
| --- | --- | --- |
| **Immediate** | The operand is the value in the instruction. | `LDM #12` loads the value 12 into the ACC. |
| **Direct** | The operand gives the memory address containing the value. | `LDD 200` loads the contents of address 200. |
| **Indirect** | The given memory address contains the address of the value. | If `Memory[40] = 200`, `LDI 40` loads `Memory[200]` into the ACC. |
| **Indexed** | The effective address is the given address plus the contents of IX. | If `IX = 3`, `LDX 100` loads `Memory[103]`. |
| **Relative** | The target address is calculated by adding an offset to the PC, rather than using an absolute address. | If the branch is at address 120, the PC has advanced to 121, and the relative offset is `+4`, the target is `121 + 4 = 125`. |

Be precise when tracing indirect and indexed modes: first calculate the
effective address, then read the value stored at that address.

### Worked example: relative addressing

Suppose a conditional branch instruction is stored at address 120. After
fetching it, the PC contains 121, the address of the next instruction. The
branch operand is a relative offset of `+4`.

```text
Target address = PC + offset
               = 121 + 4
               = 125
```

If the branch condition is true, execution continues at address 125; if it
is false, execution continues at address 121. The offset is relative, so
moving the whole routine to another location does not change the distance
from the branch to its target. When tracing an exam example, use the PC
value and offset convention given in the question.

## 4. Trace an assembly routine

When tracing a routine:

1. Read one instruction at a time.
2. Identify the opcode, operand, and addressing mode.
3. Apply its effect to the ACC, IX, or specified memory location.
4. Record updated values before moving to the next instruction.
5. For `CMP` or `CMI`, determine whether the comparison is true; follow
   `JPE` or `JPN` accordingly.

### Worked trace

Assume `Memory[20] = 0` at the start.

```text
LDM #5
ADD #3
STO 20
LDD 20
```

| Instruction | ACC before | Memory[20] before | Effect | ACC after | Memory[20] after |
| --- | ---: | ---: | --- | ---: | ---: |
| `LDM #5` | 0 | 0 | Load immediate value 5. | 5 | 0 |
| `ADD #3` | 5 | 0 | Add 3 to the ACC. | 8 | 0 |
| `STO 20` | 8 | 0 | Store the ACC at address 20. | 8 | 8 |
| `LDD 20` | 8 | 8 | Load the contents of address 20 into the ACC. | 8 | 8 |

## 5. Class practice

1. Label the opcode and operand in `LDM #12`, `STO 200`, and `JPE FINISH`.
2. Trace the worked routine and explain why `STO` does not change the ACC.
3. If `Memory[40] = 200` and `Memory[200] = 17`, trace `LDI 40`.
4. If `IX = 4` and `Memory[104] = 9`, trace `LDX 100`.
5. Trace a compare followed by `JPE` and `JPN`; show which instruction
   executes for both possible comparison results.
6. Write a routine that reads a value, adds a fixed amount, stores the
   result, and outputs a character. Annotate each instruction.
7. Identify and correct errors in a routine with an incorrect memory
   address, a wrong jump target, and a misplaced `END`.
8. Explain what information the first and second assembler passes produce.

## Homework

Trace a short routine set by your teacher, recording ACC, IX, and any memory
locations that change. Then write a routine using at least one data movement
instruction, one arithmetic instruction, and a conditional jump. Annotate
the purpose of each instruction.

## Exit check

1. What happens in each pass of a two-pass assembler?
2. What is the difference between direct and indirect addressing?
3. What value does `LDX 100` use as its effective address?
4. What do `JPE` and `JPN` depend on?
5. Which register stores the character read by `IN`?
