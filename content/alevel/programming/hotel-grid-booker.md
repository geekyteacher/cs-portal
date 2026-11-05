---
title: The Hotel Grid Booker
description: Debug a room-booking program using integer input, 2D-list indexing, and state changes.
order: 2
draft: false
---

## The challenge

The hotel booking app is crashing. Guests choose a floor and a room using
ordinary room numbers, but the backend stores its rooms in a Python 2D list.
Debug the program so it checks the right room and saves a booking.

### Learning goals

- Convert text input into integers before using it as a list index.
- Map a room number starting at 1 to a Python list index starting at 0.
- Access and update an item in a 2D list.
- Use a loop and counter to process a row of data.

### Success criteria

- The program checks the selected room without a type or index error.
- Booking an available room changes its status from `"A"` to `"B"`.
- The program displays the updated floor and, in the challenge, counts its available rooms.

## Get the starter running

1. Download the [Hotel Grid Booker starter program](/downloads/hotel-grid-booker-starter.py).
2. Open it in the Python editor you normally use, such as Thonny or VS Code.
3. Run the file. If you use a terminal, run `python3 hotel-grid-booker-starter.py`
   from the folder where you saved it.
4. Enter a floor such as `0` and a room such as `1`. Read the error message
   before changing the code.

You can also copy the starter below into a new Python file named
`hotel-grid-booker.py`.

```python
# Hotel Availability Checker (2D Matrix Backend)
# 3 floors (0, 1, 2), 3 rooms per floor (1, 2, 3)
# 'A' = Available, 'B' = Booked

hotel_grid = [
    ["A", "B", "A"],  # Floor 0 (Ground)
    ["A", "A", "B"],  # Floor 1
    ["B", "B", "A"],  # Floor 2
]

print("=== WELCOME TO GRAND HOTEL BACKEND ===")

target_floor = input("Enter floor number (0, 1, or 2): ")
target_room = input("Enter room number (1 to 3): ")

# Fix the input types and map room numbers to Python's 0-based indexes.
room_index = target_room - 1

status = hotel_grid[target_floor][room_index]

if status == "A":
    print("Room is Available!")
    # Change the selected room from "A" to "B".
else:
    print("Sorry, that room is already taken.")

print("Updated Floor Status:")
print(hotel_grid[target_floor])
```

## 1. Find and fix the crash

Run the starter and inspect the traceback. `input()` returns text, even when
the person types digits. The room calculation tries to subtract `1` from that
text, so Python raises a `TypeError`.

Fix the input and indexing so that:

- both the floor and room values are integers before they are used;
- the room number is converted to a list index (`1` becomes index `0`, `2`
  becomes index `1`, and `3` becomes index `2`); and
- the floor number stays unchanged because the floors are already numbered
  from `0`.

Run the program again. Try floor `0`, room `1`, then floor `1`, room `3`.
Check that each choice inspects the expected position in `hotel_grid`.

> [!TIP]
>
> Convert each value once, as it is entered. The floor is already a
> zero-based index; only the room number needs `- 1`.

## 2. Save the booking

When the selected room is available, add the assignment that changes its
status from `"A"` to `"B"`. The selected room is at
`hotel_grid[target_floor][room_index]`.

Run the program and book floor `0`, room `1`. The updated floor should now be
`["B", "B", "A"]`. Run the program again and choose the same room: it should
report that the room is already taken.

## 3. Fast-finisher challenge: count available rooms

Write a loop that scans the selected floor and prints how many rooms are still
available (`"A"`). Initialize a counter before the loop and increase it for
each available room.

Test your count with at least two floors. Remember that the booking happens
before the count, so the selected floor's updated status should be counted.

> [!CHALLENGE]
>
> Add range checks so a floor outside `0` to `2` or a room outside `1` to `3`
> is rejected with a helpful message rather than selecting the wrong room or
> crashing.

## Check your understanding

1. Why does `input()` need to be converted before it can be used as a list index?
2. Why do we subtract `1` from the room number but not from the floor number?
3. What changes in the grid when a room is booked?
4. What does the available-room counter need to be set to before the loop?

## Answers

### Debugged program

```python
hotel_grid = [
    ["A", "B", "A"],
    ["A", "A", "B"],
    ["B", "B", "A"],
]

print("=== WELCOME TO GRAND HOTEL BACKEND ===")

target_floor = int(input("Enter floor number (0, 1, or 2): "))
target_room = int(input("Enter room number (1 to 3): "))
room_index = target_room - 1

status = hotel_grid[target_floor][room_index]

if status == "A":
    print("Room is Available!")
    hotel_grid[target_floor][room_index] = "B"
else:
    print("Sorry, that room is already taken.")

print("Updated Floor Status:")
print(hotel_grid[target_floor])

available_count = 0
for room_status in hotel_grid[target_floor]:
    if room_status == "A":
        available_count += 1

print("Available rooms on this floor:", available_count)
```

The floor is converted to an integer for indexing. The room is also converted,
then shifted by one because the room labels start at `1` while Python list
indexes start at `0`. The assignment updates the nested list in place. The
counter starts at zero and increases once for each `"A"` on the selected floor.

### Check your understanding

1. `input()` returns a string; list indexes must be integers.
2. Floor labels already match the grid indexes (`0`, `1`, `2`), but room labels
   (`1`, `2`, `3`) are one greater than their indexes (`0`, `1`, `2`).
3. Its `"A"` value is replaced with `"B"`.
4. It must start at `0` before counting available rooms.
