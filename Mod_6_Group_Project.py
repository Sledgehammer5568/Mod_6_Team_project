#Jose Lopez
#11/12/2022

#A game that guesses a random number.

import random
print("This is a game where I choose an unidentified number between 1 and 10 and you must figure out the number i chose!")
numbers= random.randint(1,10)
#GN-Guessed number
GN = int(input("What is your guess?\n"))
while numbers != GN:
    if numbers < GN:
        next_choice = input("You have guessed the wrong number! Would you like to guess again?\nYES\nNO\n")
        if next_choice == "YES":
            print("Guess a lower number!")
            GN = int(input("What is your next guess?\n"))
        elif next_choice == "NO":
            break
        else:
            print("You must decide 'YES' or 'NO'!!!")
    elif numbers > GN:
        next_choice = input("You have guessed the wrong number! Would you like to guess again?\nYES\nNO\n")
        if next_choice == "YES":
            print("Guess a larger number!")
            GN = int(input("What is your next guess\n"))
        elif next_choice == "NO":
            break
        else:
            print("You must decide 'YES' or 'NO'!!!")
if numbers == GN:
    print("You have guessed the correct number!")
else:
    print("This is the end of the program.")
    print("The unidentified number is,",numbers,".")
