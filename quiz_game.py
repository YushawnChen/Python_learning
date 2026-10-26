questions = (("What is the capital city of France?"),
             ("How many planets are in our solar system?"),
             ("What is the chemical symbol for water?"),
             ("Who wrote the play Romeo and Juliet?"))

options = (("A.Lyon","B.Paris", "C.Shanghai", "D.Fuzhou"),
           ("A.Seven", "B.Nine", "C.Eight", "D.Ten"),
           ("A.H2O", "B.CO2", "C.HO2", "D.H2O2"),
           ("A.Elon Mask", "B.Mark Zuckerberg", "C.Leijun", "D.Charles Dickens"))

answers = (("B"), ("C"), ("A"), ("D"))

guesses = []
question_num = 0
score = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter you answer(A/B/C/D):").upper()
    guesses.append(guess)
    question_num += 1

    if guesses[question_num - 1] == answers[question_num - 1]:
        score += 1
        print(f"You answer {guess} is correct!")
    else:
        print(f"You answer {guess} is incorrect!")


print("---------Congradulation!!--------")
print("Your answer is:", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()
print("Correct answer is:")
for answer in answers:
    print(answer, end = " ")
print()
print(f"Your quiz result is: {score}")


    

