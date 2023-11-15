# Made by Connor Hackenberg
# Date Started: 11/6/2023
# Program Importance: Will store all of the equations
# for calculating the area of various 3D objects.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
import math

# calc volume of cube
def vol_cube(l):
    volume = l * l * l
    return volume

#calc volume of hemisphere
def vol_hemisphere(r):
    return (2 * math.pi * math.pow(r, 3))/3

# calc volume of pyramid
def vol_pyramid(l, w, h):
    volume = (l * w * h) / 3
    return volume
