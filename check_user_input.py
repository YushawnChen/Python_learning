# Invaild the user input
# 1.username is no more than 12 characters
# 2.username must not contain space
# 3.username must not contain digits

username = input("Enter your name: ")

if len(username) >= 12:
    print("Sorry, you need to short the name")
elif username.count(" ") != 0:
    print("Sorry, you can't use space")
elif not username.isalpha():
    print("Sorry, you can't use digits")
else:
    print("Waaah!! Bro, you made it!")