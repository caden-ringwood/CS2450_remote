import random

print("Hello! This is a game to guess your age.")
name = input("What is your name? ")
print('To quit the game, type "exit".')
guessed_ages = set()
correct = False

while not correct:
    # Only guess ages that haven't been guessed yet
    possible_ages = [age for age in range(15, 31) if age not in guessed_ages]
    if not possible_ages:
        print("I've run out of guesses! Are you sure your age is between 15 and 30?")
        break
    guessed_age = random.choice(possible_ages)
    print(f"My guess is {guessed_age}.")
    answer = input("Is it correct? (yes/no): ").strip().lower()
    if answer == "yes":
        print(f"Yay! I guessed it right, {name}.")
        correct = True
    elif answer == "no":
        guessed_ages.add(guessed_age)
        print("Let me try again.")
        if len(guessed_ages) == 16:  # 30 - 15 + 1 = 16 possible ages
            print("I've guessed all possible ages! Are you sure your age is between 15 and 30?")
            break
    elif answer == "exit":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Please answer with 'yes', 'no', or 'exit'.")


