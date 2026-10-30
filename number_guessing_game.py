# Use random() to choose an answer
# The guess should be int
# The guess should be in range
# Need to count how many times the users tried

import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)

time_guess = 1
is_runing = True

while is_runing:
    guess = input("Hey, plz enter your guess:")
    time_guess += 1
    if guess.isdigit():
        guess = int(guess)
        if guess > answer:
            print("You almost there! But your answer is too high")
        elif guess < answer:
            print("You almost there! But your answer is too low")
        else:
            print(f"Bro, you made it!! Correct answer is {answer}.")
            print(f"You have tried {time_guess} times.")
            is_runing = False
    else:
        print(f"You answer {guess} should be an integer, which form {lowest_number} to {highest_number}.")



