# Made by Connor Hackenberg
# Date Started: 10/23/23
# Program Importance: This program will demonstrate the use of functions
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

def main():

    def message(x):
        print(x)

    message("python is cool")


def calc(a, b):
    print(a * b)

calc(10, 20)
calc(5, 25)

def name(fName, lName):
    print(f"Your name is {fName} {lName}")

name("Hackenberg", "Connor")



def futureAge(fName, age):
    newAge = age + 10
    print(f"Hi! {fName}. You will be {newAge} in 10 years.")

futureAge("Connor", 18)


main()