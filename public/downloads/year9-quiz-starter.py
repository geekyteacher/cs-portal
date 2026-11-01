print("Welcome to the quiz!")

score = 0

answer = input("What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Not quite.")



print("Your score is", score, "out of 3")
