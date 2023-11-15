# Connor Hackenberg
# 9-13-2023
# This program will use nested IF statements to determine if a user qualifies for a loan.
# connorhackenberg.tech
# Mirrored on GitHub github.com/MapGuy11

# longest version follows book
salary = int(input("What is your salary?: "))
yearsWorked = int(input("How many years have you worked?: "))

if salary >= 30000:
    if yearsWorked >= 2:
        print("You qualify for the loan! Congratulations: ")
    else:
        print("You must have been employed at your current job for at least 2 years to qualify")
else:
    print("You must earn $30,000 per year to qualify for this loan.")