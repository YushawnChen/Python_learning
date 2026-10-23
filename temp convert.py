unit = input("Is this temperture in celsius or farenheit (C/F): ")
temp = float(input("What is the temperture now?: "))

if unit == "F":
    temp = (temp - 32) * 5/9
    unit = "°C"
    print(f"The temperture is {temp} {unit}")
elif unit == "C":
    temp = temp * 9/5 + 32
    unit = "°F"
    print(f"The temperture is {temp} {unit}")
else:
    print(f"{unit} is a invaild input, please try again.")
             