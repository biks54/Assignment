#Using the in operator
my_list = [1, 2, 3, 4, 5]

# Check if an element exists
element_to_check = 3
if element_to_check in my_list:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")

#Using the not in operator:
    my_list = [1, 2, 3, 4, 5]

# Check if an element does not exist
element_to_check = 6
if element_to_check not in my_list:
    print(f"{element_to_check} does not exist in the list.")
else:
    print(f"{element_to_check} exists in the list.")

#Using the count() method:
my_list = [1, 2, 3, 4, 5]

# Check if an element exists using count
element_to_check = 3
if my_list.count(element_to_check) > 0:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
