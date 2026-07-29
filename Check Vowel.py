def is_vowel(ch):
    vowels = "aeiouAEIOU"

    if ch in vowels:
        return True
    else:
        return False

character = input("Enter a character: ")

if len(character) == 1:
    print(is_vowel(character))
else:
    print("Please enter only one character.")