# Connor Hackenberg
# 9-13-2023
# This program will demonstrate other relational operators as well as logical operators, and the ELIF
# connorhackenberg.tech
# Mirrored on GitHub github.com/MapGuy11
age = int(input("What is your age?: "))
if age >= 16:
    print("You can drive!")

if age >= 18:
    print("You are an adult")

if age >= 21:
    print("You can have a drink")

print("\n\n")
if age >= 21:
    print("You can have a drink")
elif age >=18:
    print("You are an adult!")
elif age >=16:
    print("You can drive!")
else:
    print("You a young buck.")

print ("\n\n")

# demo the use of a logical operator

age = int(input("What is your age: "))
license = input("Do you have a drivers license (y/n): ")

if age >= 25 and license == "y":
    print("You can rent a car")

if age >= 25 or license == "y":
    print("You can rent a car")
