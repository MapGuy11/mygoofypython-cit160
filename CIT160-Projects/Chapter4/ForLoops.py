# Made by Connor Hackenberg
# Date Started: 10/9/23
# Program Importance: This program will demonstrate the use of FOR loops.
# and the RANGE function
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
import time

i = 0
while(i < 5):
    print(i)
    i += 1

print()

# same as above using a FOR loop
for i in range(5):
    print(i)

print()


# for loop using a range that doesnt start at 0
for i in range(100, 201):
    print(i)

print()

# count to 51 by 10s
for i in range(0,51,10):
    print(i)

print()

# count down from 10 to 0
for i in range(10,0,-1):
    print(i)
    time.sleep(8)