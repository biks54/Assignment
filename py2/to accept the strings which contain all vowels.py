def contains_all_vowels(s):
    vowels = set('aeiouAEIOU')
    return all(vowel in s for vowel in vowels)

string = input("Enter a string: ")

if contains_all_vowels(string):
    print(f"The string '{string}' contains all vowels.")
else:
    print(f"The string '{string}' does not contain all vowels.")
