# Made by Connor Hackenberg
# Date Started: 9/28/23
# Program Importance: Create a program asking for their birth month and birth day then tell the user what their Astrological Sign.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11


birthMonth = int(input("Please enter your birth month: "))
birthDay = int(input("Please enter your birth day: "))

# If users month and day math
if birthMonth == 12:
    astro_sign = 'Sagittarius' if (birthDay < 22) else 'Capricorn'

elif birthMonth == 1:
    astro_sign = 'Capricorn' if (birthDay < 20) else 'Aquarius'

elif birthMonth == 2:
    astro_sign = 'Aquarius' if (birthDay < 19) else 'Pisces'

elif birthMonth == 3:
    astro_sign = 'Pisces' if (birthDay < 21) else 'Aries'

elif birthMonth == 4:
    astro_sign = 'Aries' if (birthDay < 20) else 'Taurus'

elif birthMonth == 5:
    astro_sign = 'Taurus' if (birthDay < 21) else 'Gemini'

elif birthMonth == 6:
    astro_sign = 'Gemini' if (birthDay < 21) else 'Cancer'

elif birthMonth == 7:
    astro_sign = 'Cancer' if (birthDay < 23) else 'Leo'

elif birthMonth == 8:
    astro_sign = 'Leo' if (birthDay < 23) else 'Virgo'

elif birthMonth == 9:
    astro_sign = 'Virgo' if (birthDay < 23) else 'Libra'

elif birthMonth == 10:
    astro_sign = 'Libra' if (birthDay < 23) else 'Scorpio'

elif birthMonth == 11:
    astro_sign = 'Scorpio' if (birthDay < 22) else 'Sagittarius'

# Print their astro sign
print("You are a " + astro_sign)


