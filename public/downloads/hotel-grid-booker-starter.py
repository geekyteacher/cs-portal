# Hotel Availability Checker (2D Matrix Backend)
# 3 floors (0, 1, 2), 3 rooms per floor (1, 2, 3)
# 'A' = Available, 'B' = Booked

hotel_grid = [
    ["A", "B", "A"],  # Floor 0 (Ground)
    ["A", "A", "B"],  # Floor 1
    ["B", "B", "A"],  # Floor 2
]

print("=== WELCOME TO GRAND HOTEL BACKEND ===")

# Run this first, then fix the input types and indexing.
target_floor = input("Enter floor number (0, 1, or 2): ")
target_room = input("Enter room number (1 to 3): ")

# Inputs are strings, and room numbers need to map to Python's 0-based index.
room_index = target_room - 1

status = hotel_grid[target_floor][room_index]

if status == "A":
    print("Room is Available!")
    # TODO: Change this slot from "A" to "B" once it is booked.
else:
    print("Sorry, that room is already taken.")

print("Updated Floor Status:")
print(hotel_grid[target_floor])
