principal_balance = 0
interest_rate = 0
time = 0
compounding_frequency = 0

while principal_balance <= 0:
    principal_balance = float(input("Enter your principal balance: "))
    if principal_balance <= 0:
         print("Principle can't be less than or equal to zero")


while interest_rate <= 0:
    interest_rate = float(input("Enter your interest rate: "))
    if interest_rate <= 0:
        print("Interest rate can't be less than or equal to zero")


while time <= 0:
    time = int(input("Enter your Time: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

while compounding_frequency <= 0:
    compounding_frequency = int(input("Enter your compounding frequency: "))
    if compounding_frequency <= 0:
        print("Compounding frequency can't be less than or equal to zero")


final_amount = round(principal_balance * pow(1 + interest_rate / 100 / compounding_frequency, time * compounding_frequency), 3)
print(f"If you invest {principal_balance} as your principal at an interest rate of {interest_rate}% for {time} years, you will end up with {final_amount}.")
