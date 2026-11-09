import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"Chars: {chars}")
print(f"Key: {key}")

#Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = " "

for letters in plain_text:
    index = chars.index(letters)
    cipher_text += key[index]

print(f"The cipher text is: {cipher_text}")

#Decrypt
cipher_text = input("Enter a message to decrypt: ")
plain_text = " "

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]

print(f"The plain text is: {plain_text}")