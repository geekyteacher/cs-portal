---
title: "Assembly Language (CAIE 9618)"
description: "Core instruction set, addressing modes, and register tracing workbook."
order: 2
draft: true
---

## 1. Starter (5 mins — Silent & Independent)

*Close your notes. Write answers in your notebook:*

1. What is the role of the Accumulator (`ACC`) during arithmetic execution?
2. What is the difference between the Program Counter (`PC`) and the Memory Address Register (`MAR`)?
3. Why do we use mnemonics instead of binary machine code?

---

## 2. Quick Reference Dashboard

*Keep this section minimized unless you need a syntax check.*

<details>
<summary><b>Click to expand: Instruction Sets & Assembler Passes</b></summary>

* **Two-Pass Assembler:**
  * **Pass 1:** Scans code, records label addresses in a symbol table.
  * **Pass 2:** Translates mnemonics into machine code, resolves jumps.

* **Instruction Groups:**
  * **Data Movement:** `LDM`, `LDD`, `LDI`, `LDX`, `LDR`, `MOV`, `STO`
  * **Arithmetic:** `ADD`, `SUB`, `INC`, `DEC`
  * **Comparison & Control:** `CMP`, `CMI`, `JPE`, `JPN`, `JMP`, `END`
  * **Input/Output:** `IN`, `OUT`

</details>

<details>
<summary><b>Click to expand: The 5 Addressing Modes Cheat Sheet</b></summary>

* **Immediate (`#`):** Operand is the literal value (e.g., `LDM #12`).
* **Direct:** Operand is the address containing the value (e.g., `LDD 200`).
* **Indirect:** Address gives a pointer to another address (e.g., `LDI 40`).
* **Indexed:** Effective address = Base address + `IX` (e.g., `LDX 100`).
* **Relative:** Target address = `PC` offset (e.g., jump relative to instruction pointer).

</details>

---

## 3. Guided Practice: Tracing Together (Board Work)

*Copy this trace table into your notebook as we model it on the board.*

**Routine:**

```text
LDM #5
ADD #3
STO 20
LDD 20
```

