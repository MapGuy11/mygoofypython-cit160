# Made by Connor Hackenberg
# Date Started: 10/23/23
# Program Importance: This program will use functions to calculate the volume of a
# different 3D shapes
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

def main():
    print("1. Cube\nCylinder\n3. Sphere\n4. Cone\n")
    option = int(input("What shape would you like cube, cylninder, sphere, or cone? "))


    area = 0
    if option == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        area = areaCube(length, width, height)

def areaCube(l, w, h):
    return l * w * h

def areaCylinder(r, h):
    return 3.14 * (r * r) * h

def areaSphere(r):
    return (4 / 3) * 3.14 * (r * r * r)

def areaCone(r, h):
    return 3.14 * (r * r) * (h / 3)
