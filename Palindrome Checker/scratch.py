# Made by Connor Hackenberg
# Date Started: 10/22/23
# Program Importance: Write a program that checks whether a given word or phrase is a palindrome or not.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
user_input = input("Enter a word or phrase to check if it a palindrome: ")
# remove spaces and make it lowercase because it's easier that way.
user_input = user_input.replace(" ", "").lower()

for s in range(int(len(user_input)/2)):
    if s != s[length - i - 1]:
        return False
return True