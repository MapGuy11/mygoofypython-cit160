# Made by Connor Hackenberg
# Date Started: 10/13/23
# Program Importance: Do a program that Spyke asked us to do on Wednesday.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

numberofTerms = int(input("How far? "))

# First two terms
numberOne = 0
numberTwo = 1
count = 0

# Make sure number is valid. No negative numbers allowed
if numberofTerms <= 0:
    print("This number will not work. Please make it positive. ")
# if there is only one term, it will return numberOne
elif numberofTerms == 1:
    print("The Fibonacci sequence of the numbers up to", numberofTerms, ": ")
    print(numberOne)
# Then we will generate Fibonacci sequence of number
else:
    print("The fibonacci sequence of the numbers is:")
    while count < numberofTerms:
        print(numberOne)
        number = numberOne + numberTwo
        numberOne = numberTwo
        numberTwo = number
        count += 1