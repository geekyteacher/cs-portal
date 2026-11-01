print("Welcome to my program!")

for turn in range(1, 4):
    print("Turn", turn)
    choice = input("Choose A or B: ").strip().lower()

    if choice == "a":
        print("You chose A.")
    elif choice == "b":
        print("You chose B.")
    else:
        print("That choice was not recognised.")

print("The program has finished.")
