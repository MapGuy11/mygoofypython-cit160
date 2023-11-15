# Connor Hackenberg
# 9-18-23
# This program will do store hours.
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

# determine which day(s) it is
if dayNum == 3 or dayNum == 4:
    if hour >= 15 and hour <= 22:
        print("open")
    else:
        print("closed")
elif dayNum == 5 or dayNum == 6:
    if hour >= 12 and hour <= 22:
        print("open")
    else:
        print("closed")
elif dayNum == 0:
    if hour >= 12 and hour <= 20:
        print("open")
    else:
        print("closed")
else:
    print("closed")
