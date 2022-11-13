# Camryn echevarria
# 11/12/2022

# guessing random number between 1-10.
import random

print("Hello")

# explain the function of guessing the number

n = random.randrange(1, 10)

guess = int(input("Guess a number between 1 and 10:"))

# generating random number between 1-10
# pick a low number
for number in range(0, 10):
    number_of_guesses = 1

    if guess < n:
        print("Please guess higher")
        guess = int(input("Try Entering again:"))
