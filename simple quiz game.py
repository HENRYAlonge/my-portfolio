#simple quiz game
#store the answer
max_try = 5
Try = 0
score = 0
incorrect = 0

#Ypu csn keep adding questions if you want
questions = { "What is your name": "James bond",
              "What is the capital of canada": "ottawa",
              "Whats 2+2": "4"}

for questions, correct_answer in questions.items():
    answer = input(f"{questions} ")
    if answer == correct_answer:
        score += 1
        print("Correct")
    else:
        Try += 1
        incorrect += 1
        print("Incorrect")

    if Try >= max_try:
        print("Game over")
        break

print("Total score was:",score)
print("Total number of tries was:",Try)
print("Total incorrect was:",incorrect)


