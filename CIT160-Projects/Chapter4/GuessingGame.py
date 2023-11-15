# Made by Connor Hackenberg
# Date Started: 10/9/23
# Program Importance: This program will generate a random number and ask the user to guess what it is.
# It will also keep track of how many guesses the user had.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

# import the random package
import random

# generate a random number
randNum = random.randint(1, 6)
guestCount = 0
userNum = 0

# loop until the numbers match
while userNum != randNum:
    if guestCount > 0:
        print("Incorrect, guess again.")
    userNum = int(input("Please enter a number (1-6): "))

    if(not 1 <= userNum <= 6):
        print("Invalid Number")
    else:
        guestCount += 1

# display results
print(f"It took you {guestCount} guesses!")