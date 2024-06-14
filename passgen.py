import random

password_length = 12
characters = "abcde12345"  # Add more characters as needed

password = ""
for _ in range(password_length):
    password += random.choice(characters)

print("Password generated:", password)