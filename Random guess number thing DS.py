import random
n = random.randrange(1,10)
guess = int(input("Guess a number between 1 and 10: "))
while n!= guess:
    if guess < n:
        print("Please guess higher")
        guess = int(input("Enter humber again: "))
    elif guess > n:
        print("please guess lower")
        guess = int(input("enter humber again"))
    else:
        break
print("Guessed right :D")