# Made by Connor Hackenberg
# Date Started: 10/2/23
# Program Importance: This program will demonstrate the basics of a while loop
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


# count controlled while loop
userNum = int(input("Number please: "))

counter = 1

while counter < userNum:
    print(counter)
    counter += 1

# count controlled while loop step by 10
counter = 10
while counter <= 100:
    print(counter)
    counter += 10