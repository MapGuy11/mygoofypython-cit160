# Made by Connor Hackenberg
# Date Started: 11/01/2023
# Program Importance: Appending to a file
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


def main():

    # open file for appending
    myFile = open("_Sample.txt", "a")
    myFile.write("\nThis should append a new line!")
    myFile.close()


main()
