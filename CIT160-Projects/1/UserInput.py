# Made by Connor Hackenberg
# Date Started: 8/25/2023
# Program Importance: This program will accept user input.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


# Hardcoded Version of Program
hoursWorked = 18
payRate = 13.13
grossPay = hoursWorked * payRate
print ("Your gross pay is hardcoded haha: $" + str(grossPay))

# User Inputed Version of the Program
# Asking user for their hours worked then converting said data to a float.
hoursWorked = float(input("Please enter the hours you have worked: "))
# Asking user for payrate then converting said data to a float.
payRate = float(input("Please enter your pay rate: "))
# Multiplying the two together since they are both floats these works.
grossPay = hoursWorked * payRate
# Printing the answer from the user inputed data and saying grossPay is a string so it will print.
print ("Your gross pay: $" + str(grossPay))

