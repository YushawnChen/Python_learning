def show_balance(balance):
    print(f"Your balance is: {balance:.2f} PLN")

def deposit():
    user_deposit = float(input("Enter amount to be deposited:"))

    if user_deposit <= 0:
        print("Invalid input, please try again")
        return 0
    else:
        return user_deposit


def withdraw(balance):
    user_withdraw = float(input("Enter amount to be withdrawn:"))

    if user_withdraw <= 0:
        print("Invalid input, please try again")
        return 0
    elif user_withdraw > balance:
        print("Insufficient balance!")
        return 0
    else:
        return user_withdraw


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------- Banking -----------")
        print("Press 1 to show your balance")
        print("Press 2 to deposit")
        print("Press 3 to withdraw")
        print("Press 4 to quit")
        print("-------------------------------")
        try:
            user_input = int(input("Enter the function you want(1-4):"))
        except ValueError:
            print("Error, you can only enter the number.")
            continue
        if user_input == 1:
            print("-------------------------------")
            show_balance(balance)
        elif user_input == 2:
            balance += deposit()
        elif user_input == 3:
            balance -= withdraw(balance)
        elif user_input == 4:
            is_running = False
        else:
            print("Invalid input, please try again")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()

