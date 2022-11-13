# Emanuel Ramos
# 11/11/2022
#
# Description: Random number guessing game.
# Problems: if you input something else than a number the program breaks

import random
# explain what the code will do
print("""Let's play a guessing game. I will choose a random number between
1 and 10 and you will have to figure out what my number is.\n""")
input("once ready press 'enter'\n")

# choose a random number between a set of numbers
number = random.randint(1, 10)  # <-- the range can be changed here to make it more complicated or less complicated
# print(number)  # <-- uncomment this function for debugging purposes

# ask the user for their first guess as to what number was chosen
guess = int(input("Guess a number between 1 and 10:\n"))

# number of guesses it took
number_of_guesses = 1

# make a loop that continues to run until they guess the correct number, or they give up
while number != guess:

    # check if the number randomly generated number is less than the users guess
    if number < guess:
        # give the user a choice whether they would like to keep guessing
        try_again = input("Would you like to guess another number? (Y/N)")
        if try_again == "Y":
            # allow the user to guess again and give them a hint that the number is lower
            print("Please guess lower")
            guess = int(input("Guess another number:\n"))
            # add 1 to number of guesses
            number_of_guesses += 1
        # stop the program if the user doesn't want to continue
        elif try_again == "N":
            break
        # account for incorrect input into try_again
        else:
            print("ONLY INPUT (Y/N)!!!")

    # check if the number randomly generated number is greater than the guess
    elif number > guess:
        # give the user a choice whether they would like to keep guessing
        try_again = input("Would you like to guess another number? (Y/N)")
        if try_again == "Y":
            # allow the user to guess again and give them a hint that the number is lower
            print("Please guess higher")
            guess = int(input("Guess another number:\n"))
            # add 1 to number of guesses
            number_of_guesses += 1
        # stop the program if the user doesn't want to continue
        elif try_again == "N":
            break
        # account for incorrect input into try_again
        else:
            print("ONLY INPUT (Y/N)!!!")

    # break the loop if number == guess
    else:
        break
if number == guess:
    # if user finds the answer print that they guessed it right after the loop is broken
    print("You guessed it correctly!!!")
    print("How many tries did it take you:", number_of_guesses)
    input("press 'enter' to finish the programs execution\n")
else:
    # tell the user they exited the game and show them the answer
    print("You have exited from the program")
    print("This was the answer:", number)
    input("press 'enter' to finish the programs execution\n")
