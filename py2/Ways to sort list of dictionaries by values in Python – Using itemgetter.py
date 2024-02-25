from operator import itemgetter

list_of_dicts = [{'name': 'John', 'age': 25, 'score': 90},
                 {'name': 'Alice', 'age': 22, 'score': 85},
                 {'name': 'Bob', 'age': 30, 'score': 95}]


sorted_list = sorted(list_of_dicts, key=itemgetter('score'))
print("Original List of Dictionaries:")
print(list_of_dicts)
print("Sorted List of Dictionaries by 'score':")
print(sorted_list)
