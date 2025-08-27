import random

print("Hello! This is a game to gess your age.")
name = input("What is your name? ")
gessed_age = random.randint(15, 30)
print(f"Hello, {name}! I guess your age is {gessed_age} years old.")
