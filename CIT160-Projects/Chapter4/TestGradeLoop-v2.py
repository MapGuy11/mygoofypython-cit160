# Made by Connor Hackenberg
# Date Started: 10/2/23
# Program Importance: This program will average a specific number of test grades for the user.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

total = 0
counter = 1
again = "y"

while again == "y":
    total += int(input((f"Enter grade for test {counter}:")))
    again = input("Would you like to enter another:")
    counter = 1

    print(f"Your total is: {total}")
    print (f"Your average is: {total / counter: .2f}")