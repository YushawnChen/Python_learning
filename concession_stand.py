menu = {"pizza": 21.89,
        "soda": 6.89,
        "wisemac": 10.99,
        "watermelon": 34.89,
        "cola": 9.99,
        "potato": 7.00}

cart = []
total = 0

print("--------M E N U--------")
for key, value in menu.items():
    print(f"{key:10}: PLN{value:.2f}")
print("-----------------------")

while True:
    food = input("Choose the items you want(q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

print("-------------Cart--------------")

print(f"You have choose: {" ".join(cart)}")

print("-------------Bill--------------")

print(f"You need to pay: PLN{total:.2f}")
    
        



