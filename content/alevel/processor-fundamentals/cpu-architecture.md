---
title: CPU Architecture
description: Explain CPU architecture, registers, buses, interrupts, peripherals, and processor performance.
order: 1
draft: false
---

## Learning goals

- Explain the Von Neumann model and stored-program concept.
- Describe the purpose of the CPU components and registers in the syllabus.
- Use register-transfer notation to trace the fetch-execute cycle.
- Explain how interrupts are detected and handled.
- Explain how peripheral ports and processor features affect a computer system.

## Suggested teaching time

Use this page for Doubles 1–4 in the [unit plan](./index): introduce the
architecture and registers, trace the fetch-execute cycle, teach interrupts
and performance, then consolidate with mixed practice.

## 1. The Von Neumann model

In the **Von Neumann model**, program instructions and data are stored in the
same main memory. The processor fetches an instruction, decodes what it means,
and executes it. Unless an instruction changes the flow of control, the
processor continues with the next instruction in sequence.

The **Immediate Access Store (IAS)** is the main memory used to store
instructions and data. The processor contains the Control Unit, Arithmetic
and Logic Unit, and registers that hold values needed during processing.

## 2. Processor components and registers

| Component | Purpose |
| --- | --- |
| **Control Unit (CU)** | Controls and coordinates processor operations. It decodes instructions and sends control signals. |
| **Arithmetic and Logic Unit (ALU)** | Performs arithmetic calculations and logical operations. |
| **System clock** | Produces regular timing pulses that coordinate operations. Clock speed is measured in hertz. |
| **Immediate Access Store (IAS)** | Holds the program instructions and data currently available to the processor. |
| **Registers** | Very fast storage locations in the processor for instructions, addresses, data, and intermediate results. |
| **Cache memory** | Stores frequently or recently used instructions and data so they can be accessed faster than from main memory. |

The syllabus distinguishes **general-purpose** and **special-purpose**
registers. In its assembly-language questions, the **Accumulator (ACC)** is
the only general-purpose register available. The other named registers have
specific roles.

| Register | Purpose |
| --- | --- |
| **Program Counter (PC)** | Holds the address of the next instruction to be fetched. |
| **Memory Address Register (MAR)** | Holds the address of the memory location currently being accessed. |
| **Memory Data Register (MDR)** | Holds data or an instruction being transferred to or from memory. |
| **Current Instruction Register (CIR)** | Holds the instruction currently being decoded and executed. |
| **Accumulator (ACC)** | Holds data for an operation and intermediate or final results. |
| **Index Register (IX)** | Holds an index value used when calculating an indexed address. |
| **Status Register** | Holds status information about processor operations; this can be used by conditional instructions. |

## 3. Buses

The processor uses buses to transfer information between the CPU, memory,
and other components.

| Bus | Information carried | Direction or use |
| --- | --- | --- |
| **Address bus** | The address of the memory location or device being accessed. | Usually from the processor to memory or a device. |
| **Data bus** | Instructions and data. | Bidirectional: information can travel to or from the processor. |
| **Control bus** | Signals such as memory read, memory write, and interrupt signals. | Signals travel in the direction required by the operation. |

## 4. Fetch-execute cycle

The processor repeatedly fetches and executes instructions. The CU decodes
each fetched instruction as part of this process. Register-transfer notation
uses an arrow to show a value being copied or transferred; for example,
`PC -> MAR` means that the contents of the PC are copied to the MAR.

### Fetching an instruction

1. `PC -> MAR`: the address of the next instruction is copied to the MAR.
2. The CU sends a read signal on the control bus. The address travels to
   memory on the address bus.
3. The instruction at that address is transferred from memory on the data
   bus into the MDR.
4. The instruction is copied from the MDR to the CIR.
5. The PC is updated to the address of the next instruction.
6. The CU decodes the instruction in the CIR.

### Executing an instruction

The action depends on the instruction. It may use the ALU, access another
memory location, transfer data to a register, or change which instruction
will be fetched next. For example, an instruction to add a value to the ACC
causes the ALU to perform the addition and the result to be stored in the
ACC. The cycle then repeats.

### Worked trace: `LDD 200`

Assume `PC = 100`, memory location 100 contains `LDD 200`, memory location
200 contains `41`, and `ACC = 0`.

| Stage | Register-transfer notation and bus use | Result |
| --- | --- | --- |
| Fetch address | `PC -> MAR`; address 100 is sent on the address bus. | `MAR = 100` |
| Fetch instruction | Memory read signal; instruction travels on the data bus into `MDR`, then `MDR -> CIR`. | `CIR = LDD 200`; `PC` advances to 101. |
| Decode | The CU decodes `LDD 200` as a direct load from address 200. | The instruction requires a memory read from address 200. |
| Fetch operand | `200 -> MAR`; memory read signal; `Memory[200] -> MDR`. | `MDR = 41` |
| Execute | `MDR -> ACC` | `ACC = 41` |

## 5. Interrupts

An **interrupt** is a signal that requests the processor's attention. It
allows the processor to respond to an event, such as a peripheral requesting
service or a timer reaching a set value, without continuously checking that
device.

An **Interrupt Service Routine (ISR)** is a program that deals with the
interrupt. The processor checks for interrupts at the end of a
fetch-execute cycle, after the current instruction has completed and before
it begins the next cycle. An interrupt that is accepted is therefore
serviced between instructions, rather than part-way through the current
instruction.

1. The processor completes the current instruction.
2. At the end of that fetch-execute cycle, it checks for a pending
   interrupt.
3. If an interrupt is accepted, the processor saves the information needed
   to resume the current program and transfers control to the relevant ISR.
4. The ISR handles the event.
5. The saved state is restored and the processor continues with the next
   instruction in the interrupted program.

Interrupts are used for events that need a response, including input from a
device, timer events, and hardware or software errors. The exact ISR depends
on the event and the system.

## 6. Peripheral ports and performance

Ports provide connections between a computer system and peripheral devices.
The syllabus examples are **USB**, **HDMI**, and **VGA**.

| Port | Typical connection |
| --- | --- |
| **USB** | General peripherals such as keyboards, mice, and storage devices. |
| **HDMI** | A digital display connection, commonly used for a monitor or projector. |
| **VGA** | An analogue video connection to a display. |

Identify the port from the scenario and explain how it enables the relevant
device to connect; do not confuse the port with the processor's internal
buses.

Processor performance depends on several factors:

| Factor | How it can affect performance |
| --- | --- |
| **Processor type** | Different processor designs can complete instructions at different rates. |
| **Number of cores** | More cores can allow more tasks or threads to be processed in parallel when the software supports it. |
| **Bus width** | A wider bus can transfer more bits in one transfer. |
| **Clock speed** | A higher clock speed provides more timing cycles per second, but does not by itself guarantee better overall performance. |
| **Cache memory** | A larger or more effective cache can reduce how often the CPU must wait for slower main memory. |

When comparing systems, explain the effect of each factor in context rather
than assuming that one specification alone determines performance.

## Class practice

1. Draw and label the Von Neumann model, showing the CPU, IAS, and the
   address, data, and control buses.
2. Match each register to its role, then explain why the PC and MAR are
   different.
3. Trace the fetch and execution of `LDM #7` and `ADD #4`, showing relevant
   register transfers.
4. For a memory read, identify the values carried on each bus and which
   registers are involved.
5. Explain how a keyboard interrupt is handled and why the processor does
   not need to keep polling the keyboard.
6. Compare two processors using core count, bus width, clock speed, and
   cache; explain why the faster clock is not the only consideration.
7. Choose USB, HDMI, or VGA for a described peripheral connection and justify
   the choice.

## Homework

Without copying this page, draw the CPU-to-memory data path and describe the
fetch-execute cycle for one instruction. Include the PC, MAR, MDR, CIR, ACC,
and the buses where relevant. Then answer one interrupt question and one
processor-performance comparison question assigned by your teacher.

## Exit check

1. What does the stored-program concept mean?
2. Explain the difference between the MAR and MDR.
3. What does `PC -> MAR` mean?
4. At what point does the processor check for interrupts, and what is an
   ISR for?
5. Give two factors that can affect processor performance and explain their
   effects.
