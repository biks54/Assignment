from collections import Counter
string = input("Enter a string: ")
word_frequency = Counter(string.split())

print("Word frequencies in the string:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
