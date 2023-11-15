# Made by Connor Hackenberg
# Date Started: 11/01/2023
# Program Importance: This program will demonstrate reading from a file.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

def main():
    # open a file to read
    stateFile = open("us-state-capitals.csv", "r")

    # start reading file 1 line at a time.
    line1 = stateFile.readline()
    line2 = stateFile.readline()

    print(line1)
    print(line2)

    # read rest of file using a loop
    for line in stateFile:
        print(line)






main()