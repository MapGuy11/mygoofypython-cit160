# Made by Connor Hackenberg
# Date Started: 11/08/2023
# Program Importance: Will use the width statement to open multiple files.
# This program will introduce TRY/EXCEPT exception handling.
# This program will use the SPLIT function to parse records.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

try:
    # open file
    with open("us-state-capitals.csv", "r") as readFile, open("us-state-capitals-2.csv", "w") as writeFile:
        # loop through and read file
        for line in readFile:
           # print(line.rstrip().lstrip())
            record = line.split(",")
            # print(record)
            stateName = record[0]
            stateCapital = record[1]
            writeFile.write(f"{stateName},{stateCapital}\n")
except FileNotFoundError:
    print("File not found")
except NameError:
    print("something is wrong with your syntax")
except:
    print("general error")