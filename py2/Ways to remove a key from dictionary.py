# Method 1: Using del keyword
my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]

# Method 2: Using pop() method
my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
my_dict.pop(key_to_remove, None)

# Method 3: Using dictionary comprehension
my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
my_dict = {key: value for key, value in my_dict.items() if key != key_to_remove}

print("Original Dictionary:")
print(my_dict)
