def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon = words1.symmetric_difference(words2)
    return uncommon
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = uncommon_words(string1, string2)
print("First String:", string1)
print("Second String:", string2)
print("Uncommon words between the two strings:", result)
