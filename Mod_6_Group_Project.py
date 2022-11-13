#David Serna
# 11/10/2022
#
#Description: Input a number between 1-10 to guess the number the code is thinking of
#Problems: code breaks if something else is inputed that isn't 1-10

import random
n = random.randrange(1,10) #can change the range if you want it to be less or more complex.
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
