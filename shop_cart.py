item = input("What you want to buy:")
price = float(input(f"How much is {item}:"))
quantity = int(input(f"How many {item} you have bought:"))

total = price * quantity

print(f"You have bought {quantity} {item}, cost PLN {total}")