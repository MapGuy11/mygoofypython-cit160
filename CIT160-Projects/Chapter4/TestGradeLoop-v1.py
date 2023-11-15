# Made by Connor Hackenberg
# Date Started: 10/2/23
# Program Importance: This program will average a specific number of test grades for the user.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


numGrades = int(input("How many grades to average: "))
total = 0
counter = 1
# count controlled loop
while counter <= numGrades:
    # running total values
    total += int(input(f"Enter grade for the test"))
    counter += 1

    print(f"Your total is: {total}")
    print (f"Your average is:" {total / numGrades: .2f)