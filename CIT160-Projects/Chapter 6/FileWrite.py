# Made by Connor Hackenberg
# Date Started: 11/01/2023
# Program Importance: Create and write a file
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

def main():

    # create/open a file for writing
    # within the working directory
    myFile = open("_Sample.txt", "w")
    
    # write data to the file
    myFile.write("Hello, Connor!")
    myFile.write("\nIt's a beautiful day in NEPA")

    # Close the file!!!!!!
    myFile.close()

    # create/open a file for writing
    # outside the working directory
    desktopFile = open(r"C:\Users\conno\Desktop\NewFile.txt", "w")
    desktopFile.write("Hello World")
    desktopFile.close()

main()