# name  - class

# --QUIZ MASTER--

#TODAY - make a quiz that has several questions
# The questions will be in a list.
# Use a for loop to cycle through them

score = 0
questions = ["What is 2 x 10? ",
             "What is the capital city of England? ",
             "What month is Christmas in? "]

answers = ["20",
           "london",
           "december"]

for i in range(len(questions)):
    answer = input(questions[i]).lower()
    if answer == answers[i]:
        print("Correct! +1 point")
    else:
        print("Wrong!")


