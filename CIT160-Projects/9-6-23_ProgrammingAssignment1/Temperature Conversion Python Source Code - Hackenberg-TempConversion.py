# Made by Connor Hackenberg
# Date Started: 9/6/2023
# Program Importance: Ask user for F temp then convert and print to C temp.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

# Ask User for a Farenheit Temperature.
farenheitTemperature = float(input("Could you please give me a temperature in Farenheit: "))

# Convert the Farenheit Temperature into a Celsius Temperature.
convertedTemperature = 5/9*(farenheitTemperature-32)

# Print to the user what the converted temperature is.
print ("Your Celsius Temperature: " + str(round(convertedTemperature, 2)))
# Format the rhombus stars
# Print each row then go the opposite way.
rhombusStarsRow1 = "*"
rhombusStarsRow2 = "***"
rhombusStarsRow3 = "*****"
rhombusStarsRow4 = "*******"
rhombusStarsRow5 = "*********"
rhombusStarsRow6 = "***********"


# Print a rhombus. Probably Dumb Way - Learning I guess :)
print(f"{rhombusStarsRow1:^20}")
print(f"{rhombusStarsRow2:^20}")
print(f"{rhombusStarsRow3:^20}")
print(f"{rhombusStarsRow4:^20}")
print(f"{rhombusStarsRow5:^20}")
print(f"{rhombusStarsRow6:^20}")
print(f"{rhombusStarsRow5:^20}")
print(f"{rhombusStarsRow4:^20}")
print(f"{rhombusStarsRow3:^20}")
print(f"{rhombusStarsRow2:^20}")
print(f"{rhombusStarsRow1:^20}")
exit()
