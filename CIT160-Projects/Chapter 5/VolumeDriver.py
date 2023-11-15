# Made by Connor Hackenberg
# Date Started: 11/6/2023
# Program Importance: Will use the VolumeHelper file to help users
# calculate the volume of various 3D objects.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


import VolumeHelper

def main():
    # display menu to user
    print("VOLUME CALCULATOR")
    print("-----------------")
    print("1. Cube")
    print("2. Hemisphere")
    print("3. Pyramid")
    print("-----------------")

    print()

    # ask user for their choice
    choice = int(input("Pick an object: "))
    print()

# determine which object the user selected and ask appropriate questions
    if choice == 1:
        # cube
        length = float(input("Enter length: "))
        volume = VolumeHelper.vol_cube(length)
        print(f"Cube volume: {volume}")
    elif choice == 2:
        # hemisphere
        radius = float(input("Enter radius: "))
        volume = VolumeHelper.vol_hemisphere(radius)
        print(f"Hemisphere Volume: {volume}")

    elif choice == 3:
        # pyramid
        length = float(input("Enter length:"))
        width = float(input("Enter Width: "))
        height = float(input("Enter Height: "))
        volume = VolumeHelper.vol_pyramid(length,width,height)
        print(f"Pyramid Volume: {volume}")

main()