# Made by Connor Hackenberg
# Date Started: 10/18/2023
# Program Importance: Demonstate the LEN() method and loop through a string.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
userInput = input("Enter a string: ")

# show the variable as the user entered it, in all lower case, an in all upper case.
print(userInput)
print(userInput.lower())
print(userInput.upper())
print(userInput)

print("\n")
# loop through string
for char in userInput:
    print(char)
print()

print(userInput[2])
numChars = len(userInput)
print("\n", numChars)

print()

for i in range(0, numChars):
    print(userInput[i])