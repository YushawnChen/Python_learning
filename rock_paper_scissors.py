# User need to input their choice (rock, paper, scissors)
# Computer need to generate a random choice in each round
# Need to show user's K/D

choice = ("rock", "paper", "scissors")

import random
running = True
time_round = 0
victory = 0
defeat = 0

user_name = input("Creat your user name:").capitalize()

while running:
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    time_round += 1
    computer_input = random.choice(choice)
   
    while user_input not in choice:
            print(f"please try again, {user_name}. You can only choose rock, paper or scissors.")
            user_input = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_input == computer_input:
            print(f"Player: {user_input}")
            print(f"Computer: {computer_input}")
            print("It is tie!")
    elif user_input == "rock" and computer_input == "scissors":
            print(f"Player: {user_input}")
            print(f"Computer: {computer_input}")
            print(f"{user_name}, you win!")
            victory += 1
    elif user_input == "paper" and computer_input == "rock":
            print(f"Player: {user_input}")
            print(f"Computer: {computer_input}")
            print(f"{user_name}, you win!")
            victory += 1
    elif user_input == "scissors" and computer_input == "paper":
            print(f"Player: {user_input}")
            print(f"Computer: {computer_input}")
            print(f"{user_name}, you win!")
            victory += 1
    else:
            print(f"Player: {user_input}")
            print(f"Computer: {computer_input}")
            print("You loose")
            defeat += 1

    play_again = input("Continue to play? (y/n)):").lower()
    if not play_again == "y":
            running = False
    
print(f"Thank you for playing, {user_name}")
print(f"Your KD is {victory}/{defeat}.")
   
       
    
            