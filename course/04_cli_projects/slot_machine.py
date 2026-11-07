# Slot Machine
# 1. Welcome message: Display a welcome message and symbols.
# 2. Show Balance: Display the user's current balance.
# 3. User Input Validation:
#    - Bet amount must be greater than 0.
#    - Bet amount cannot exceed the user's current balance.
#    - Input must be a valid number.
# 4. Show result of spin.
# 5. Payout
# 5. Ask the user if they want to continue.
import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "🌟"]
    return [random.choice(symbols) for x in range(3)]

def print_row(row):
    print("Spainning...")
    print(" ".join(row))

def payout(bet, row):
    if row[0] == row[1] == row[2]:
        print("Congratulations!")
        if row[0] == "🍒":
            return bet * 3
        if row[0] == "🍉":
            return bet * 4
        if row[0] == "🍋":
            return bet * 5
        if row[0] == "🔔":
            return bet * 6
        if row[0] == "🌟":
            return bet * 6
    else:
        return 0
        
def main():
    print("-------------------")
    print("Welcome to slots!!")
    print("Symbol: 🍒 🍉 🍋 🔔 🌟")
    print("-------------------")

    balance = 100

    while balance > 0:
        print(f"Your balance: {balance}")
        bet = input("Place your bet amount: ")
         
        if not bet.isdigit():
            print("You should input a number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        if balance == 0:
            print("Game over! You are out of money.")
            break

        row = spin_row()
        print_row(row)

        winnings = payout(bet, row)
        balance += winnings

        quit = input("Do you want to continue(Y/N):").upper()
        if not quit == "Y":
            break


    print("Thank you!")
    print(f"Your total balance is: {balance}")

if __name__ == '__main__':
    main()
    


