---
title: "2.1 Packets and Packet Switching"
description: Describe packet structure and explain how packet switching sends and reassembles data.
type: lesson
order: 2
draft: false
---

## Learning goals

- Describe the structure of a data packet.
- Identify the information contained in a packet header.
- Explain how packet switching sends and reassembles data.

## Quick start

Imagine sending a large photograph to someone over the internet.

1. Why might a network send it as several smaller pieces rather than one
   enormous piece?
2. What information might each piece need so the recipient can put the
   photograph back together?

Write down your ideas before reading on.

## Packet structure

Data is divided into **packets** before it is transmitted. Each packet has
three main parts:

| Part | Purpose |
| --- | --- |
| **Header** | Contains the destination address, the originator's address, and the packet number. |
| **Payload** | Contains part of the data being sent. |
| **Trailer** | Marks the end of the packet. |

The packet number identifies the packet's position in the original data. The
destination and originator addresses identify where the packet is going and
where it came from.

## Packet switching

**Packet switching** is a way of transmitting data in packets across a
network:

1. The original data is divided into packets.
2. Routers use packet information to control the route each packet takes.
3. Different packets may travel along different routes.
4. Packets may arrive at the destination out of order.
5. The receiving device uses packet numbers to put them back into the
   correct order and reassemble the original data.

### Worked example

A message is split into four packets. They arrive in this order: `3, 1, 4, 2`.

The receiving device uses the packet numbers to reorder them as `1, 2, 3, 4`
before reassembling the message from their payloads.

## Practice

### 1. Packet structure

For each item, name the packet part it belongs to: header, payload, or
trailer.

1. The address of the receiving device.
2. The part of an image being sent.
3. The number that identifies the packet's position.
4. The address of the sending device.
5. The part marking the end of the packet.

### 2. Reordering packets

A file is divided into five packets. They arrive in this order:
`2, 5, 1, 4, 3`.

1. Write the order in which the packets should be reassembled.
2. Explain how the receiving device knows the correct order.

### 3. Explain packet switching

In your own words, explain how routers help packets travel from a sender to a
receiver. Include why packets might arrive out of order and how the receiver
reassembles the data.

> [!CHALLENGE]
>
> ### Challenge Yourself: Find the Missing Packet
>
> A file is divided into 100 packets. The receiver gets packets `1` to `56`,
> then `58` to `100`.
>
> Explain how the receiver can detect that a packet is missing, what may
> happen next, and how the missing packet fits into the reassembled file.
> Include enough detail to show how packet numbers help the receiver.
>
> ### Optional stretch questions
>
> Complete these if you finish the main challenge. You can try one or both.
>
> **1. Different routes**
>
> Packet A travels `School → Router X → Router Y → Home`. Packet B travels
> `School → Router Z → Home`.
>
> Why might packets from the same file take different routes?
>
> **2. Evaluate packet switching**
>
> Give two advantages of packet switching compared with sending one large
> block of data, and one possible disadvantage. Explain each point.

**Quality over quantity:** You do not need to answer every stretch question.
A clear explanation with relevant details about packets, routes, or
reassembly is more valuable than rushing through all the questions.

## Exit check

Answer from memory:

1. Name the three parts of a packet.
2. State the three items of information in the packet header specified in
   this lesson.
3. Give one reason packets may arrive out of order.
4. Explain how the receiving device puts the packets back in order.

## Homework

Watch:

- [16. Cambridge IGCSE (0478/0984) 2.1 Packet and packet
  structure](https://www.youtube.com/watch?v=rpOfxVgNsa0&list=PLCiOXwirraUBvcD8XWMzyuzEA-IJG5cH7&index=17)
- [17. Cambridge IGCSE (0478/0984) 2.1 Packet
  switching](https://youtu.be/PVbuTBS4Sqc)

Then, without looking at the page, write a short explanation of packet
switching. Include the three packet parts, the three items of information in
the header, why packets may take different routes, and how the receiver
reassembles them. Check your answer against the page and correct anything
you missed.
