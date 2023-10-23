# Made by Connor Hackenberg
# Date Started: 10/16/2023
# Program Importance: It it prime? the gameshow........
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

number = int(input("Enter a number please: "))

isPrime = True

for i in range(2, number):
    if number % i == 0:
        print("NOT PRIME loser.")
        break
else:
    print("IS PRIME")