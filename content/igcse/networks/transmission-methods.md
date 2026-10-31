---
title: "2.1 Transmission Methods"
description: Compare serial and parallel transmission, and simplex, half-duplex, and full-duplex communication.
type: lesson
order: 3
draft: false
---

## Learning goals

- Describe serial and parallel transmission.
- Compare the advantages and disadvantages of serial and parallel
  transmission.
- Distinguish simplex, half-duplex, and full-duplex communication.
- Select and justify a suitable method for a scenario.

## Quick start

Think of a road with one lane and a road with several lanes.

1. What might be an advantage of sending one item at a time along one path?
2. What might be an advantage of sending several items at the same time?
3. What could go wrong if the items sent on different paths do not arrive
   together?

## Serial and parallel transmission

Serial and parallel describe how bits are sent between devices.

| Method | How it works | Advantages | Disadvantages |
| --- | --- | --- | --- |
| **Serial** | Bits are sent one after another along a single communication path. | Fewer wires are needed. It is suitable for longer distances and avoids the timing problem of separate bits travelling along parallel wires. | With the same signal rate, bits are sent one at a time rather than several at once. |
| **Parallel** | Several bits are sent simultaneously along separate communication paths. | Several bits can be sent in one group, so it can transfer data quickly over short distances. | It needs more wires. Over longer distances, bits can arrive at different times (**bit skew**) and signals on nearby wires can interfere (**crosstalk**). |

### Worked comparison

A computer must send data to a device in another room. Serial transmission is
usually more suitable over a longer distance because it uses fewer wires and
does not rely on several separate bits arriving at exactly the same time.
Parallel transmission may be useful over a short distance when several bits
need to be sent simultaneously.

## Simplex, half-duplex, and full-duplex

These terms describe the direction in which data can travel between two
devices.

| Method | Direction | Example |
| --- | --- | --- |
| **Simplex** | Data travels in one direction only. | A sensor that only sends readings to a computer. |
| **Half-duplex** | Data can travel in both directions, but only one direction at a time. | A push-to-talk radio. |
| **Full-duplex** | Data can travel in both directions at the same time. | A two-way conversation where both people can speak and hear simultaneously. |

Serial/parallel and simplex/duplex describe **different things**. A
connection can be serial and full-duplex, for example.

## Choosing a method for a scenario

When a question asks you to choose a method, use the details in the scenario:

- **Distance:** serial is generally more suitable over longer distances.
- **Number of bits sent at once:** parallel sends several bits
  simultaneously.
- **Direction:** simplex is one-way; half-duplex allows both directions in
  turn; full-duplex allows simultaneous two-way communication.

State the method and link your reason to a detail in the scenario. For
example: “Serial is suitable because the devices are far apart and fewer
communication wires are needed.”

## Practice

### 1. Identify the method

Choose **serial** or **parallel** for each description:

1. Bits are sent one after another along one communication path.
2. Several bits are sent simultaneously along separate paths.
3. A short-distance connection needs to send a group of bits at once.
4. A long-distance connection should avoid problems caused by bits arriving
   at different times.

### 2. Explain the disadvantage

1. Explain how bit skew can cause a problem during parallel transmission.
2. Explain what crosstalk is and why it can affect parallel transmission.

### 3. Identify the direction

Choose **simplex**, **half-duplex**, or **full-duplex**:

1. A sensor sends measurements to a computer but does not receive data.
2. Two radio users take turns speaking.
3. Two people can speak and hear one another at the same time.

### 4. Apply your knowledge

A monitoring system sends information over a long cable to a display. The
display does not send information back.

1. Which direction method is needed?
2. Which transmission method would you recommend: serial or parallel?
3. Justify both choices using details from the scenario.

## Exit check

1. What is the difference between serial and parallel transmission?
2. What is bit skew?
3. What is the difference between half-duplex and full-duplex?
4. Can a connection be both serial and full-duplex? Explain.

## Homework

Watch [18. Cambridge IGCSE (0478/0984) 2.1 Data transmission
methods](https://youtu.be/0cIWq4MZmxw).

Write a short response explaining why serial transmission is generally more
suitable than parallel transmission over a longer distance. Include bit
skew, crosstalk, and the number of communication paths. Then classify one
real communication example as simplex, half-duplex, or full-duplex and
justify your choice.
