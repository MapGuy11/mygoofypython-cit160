# Made by Connor Hackenberg
# Date Started: 8/25/2023
# Program Description: This program will demonstrate the use of the string format specifier
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
# Format {Money} into the correct format we want.
money = 13586.74568
print(f"The value is: {money:.2f}")
# Calculate New York Tax and format is correctly.
nyTax = .0825
print(f"{nyTax:.02%}")
# Right Justify {cool}
cool = "--*--"
print(f"{cool:>20}")
# Center Justify {cool}
print(f"{cool:^20}")
# Left Justify {cool}
print(f"{cool:<20}")
quit()