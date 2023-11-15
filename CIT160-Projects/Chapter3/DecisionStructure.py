# Connor Hackenberg
# 9-11-2023
# Learning how decisions are made in the world of Python tldr (if statements)
# connorhackenberg.tech
# Mirrored on GitHub github.com/MapGuy11

# ask the user for their age
age = int(input("What is your age? "))

# determine if user is old enough for an adult beverage
if age >= 21:
    print("Lets have a Broken Heels")
    print("Hold my beer ...")
else:
    print("Here's some milk and cookies.")
print ("\n\n")




# ask the user a yes no question and compare strings
answer = input("Is programming fun? (y/n): ")
if answer == "y" or answer == "Y":
    print ("I know right!?")
print("\n\n")


# Use an if statement to compare strings.
girlName = "Mary"
boyName = "Mark"

if girlName > boyName:
    print("Maru is better")
else:
    print("Mark is better")