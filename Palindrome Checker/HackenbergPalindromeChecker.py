# Made by Connor Hackenberg
# Date Started: 10/24/23
# Program Importance: Write a program that checks whether a given word or phrase is a palindrome or not.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
def is_palindrome(s):
    # remove spaces and make it lowercase because it's easier that way.
    s = s.replace(" ", "").lower()
    # get the length to check the string
    length = len(s)
    # Compare characters from the start and end of the string
    # This will take the string and ensure the loop only runs half the length
    # Then it will compare against the inverse and see if it a palindrome
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

# Ask user for input
user_input = input("Enter a word or phrase to check if it a palindrome: ")

# Decide on previous calculations if the input was a palindrone and output accordingly.
if is_palindrome(user_input):
    print(" Wow! \n You found a palindrome \n :)")
else:
    print(" Sorry, \n it's not a palindrome \n :( ")