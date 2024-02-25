import string

def contains_special_character(s):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in s)

string = input("Enter a string: ")

if contains_special_character(string):
    print(f"The string '{string}' contains at least one special character.")
else:
    print(f"The string '{string}' does not contain any special character.")
