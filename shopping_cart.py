items = []
prices = []
total = 0

while True:
    item = input("Enter the item you want to buy (q to quit): ")
    if item.lower() == "q":
        break
    else:
        items.append(item)
        price = float(input(f"Enter the price of {item}: PLN"))
        prices.append(price)

       
       
print("------- Here's you shopping cart -------")

for item in items:
    print(item, end = ", ")    

print()

for price in prices:
    print(price, end = ", ")
    total += price

print()
print(f"The total amount is {total:.2f}")

        
