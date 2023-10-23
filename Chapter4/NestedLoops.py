# Made by Connor Hackenberg
# Date Started: 10/4/23
# Program Importance: This program demonstrates nested loops
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

# Ask user for number of rows and colums.
rows = int(input("Number of rows: "))
colums = int(input("Number of colums: "))

rowCounter = 1
while rowCounter <= rows:

    columCounter = 1
    while columCounter <= colums:
        print("*", end=" ")
        columCounter += 1

    print()
    rowCounter += 1

print()
print()

rowCounter = 1
while rowCounter <= 12:

    columCounter = 1
    while columCounter <= 12:
        print(f"{columCounter * rowCounter:^3}", end=" ")
        columCounter += 1
    print()
    rowCounter += 1

print()
print()

# print out checkerboard

rowCounter = 1
while rowCounter <= 8:

    columCounter = 1
    while columCounter <= 8:

        if (columCounter + rowCounter) % 2 == 0:
            character = "+"
        else:
            character = "-"
        print(f"{character}", end=" ")
        columCounter += 1
    print()
    rowCounter += 1

print()
print()

