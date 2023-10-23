# Made by Connor Hackenberg
# Date Started: 10/16/23
# Program Importance: Do the program from before in class.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

userNum = int(input("How far to go in the sequence? "))
a = 0
b = 1
c = 0

for i in range(0, userNum):
    print(f"A:{a:<5} B: {b:<5} c:{c:<5} ")
    c = a + b
    a = b
    b = c