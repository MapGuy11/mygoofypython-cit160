# Connor Hackenberg
# 9-18-23
# This program will do store hours. Version #3 yikes Spyke you really like more versions.
# connorhackenberg.tech
# Mirrored on GitHub github.com/MapGuy11


# Wednesday & Thursday 3:00pm - 10:00pm
# Friday & Saturday 12:00pm - 10:00pm
# Sunday 12:00pm - 8:00pm

# print dev/number options for user to pick from
print("Sun - 0\t\t\tThu - 4")
print("Mon - 1\t\t\tFri - 5")
print("Tue - 2\t\t\tSat - 6")
print("Wed - 3")

# ask user for day
dayNum = int(input("What day is it?: "))
hour = int(input("What hour is it (0-24): "))

# set a boolean flag for open
open = False

# determine which day(s) it is
if (dayNum == 3 or dayNum == 4) and (15 <= hour <= 22): open = True

elif (dayNum == 5 or dayNum == 6) and (12 <= hour <= 22): open = True
# If you don't put parentheses it won't test all the conditions.
elif (dayNum == 0) and (12 <= hour <= 20): open = True
# tell user if store is open or closed
if open: print("Store is open!")
else: print("Sorry, store is closed :(")