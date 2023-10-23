# Made by Connor Hackenberg
# Date Started: 10/16/2023
# Program Importance: Make a vowel counter. a-e-i-o-u
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

while True:
# ask user for input
    sentence = input("Enter a sentence ('quit' to exit): ")
# break out if users types 'quit'
    if sentence == 'quit':
        print("Thanks for playing goodbye!")
        break


# count the number of vowels
    vowelCount = 0
    for char in sentence:
       # print(char)
        if char.lower() in "aeiou":
            vowelCount += 1
            print(char.upper(), end="")
        else:
            print(char.lower(), end="")

    print(f"\nTotal vowels found in the sentence provided: {vowelCount}")