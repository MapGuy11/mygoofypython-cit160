# Made by Connor Hackenberg
# Date Started: 8/28/2023
# Program Description: Based on Pearson Revel Chapter 2: Auto-Graded Programming Project 2. This will solve it's issue.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
# Ask user for how many females or males.
numMales = int(input("Enter number of males. "))
numFemales = int(input("Enter number of females. "))
# Calculate the two variables together.
total = numMales + numFemales

percentMale = numMales / total
percentFemale = numFemales / total

print(f"Percent males: {percentMale: .0%}")
print(f"Percent females: {percentFemale: .0%}")
