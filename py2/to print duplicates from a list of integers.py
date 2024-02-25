def print_duplicates(my_list):
    count_dict = {}
    duplicates = set()

    for num in my_list:
        if num in count_dict:
            count_dict[num] += 1
            duplicates.add(num)
        else:
            count_dict[num] = 1

    if duplicates:
        print("Duplicates in the list:", list(duplicates))
    else:
        print("No duplicates found in the list.")

numbers_list = [1, 2, 3, 4, 2, 7, 8, 1, 9, 3, 5, 6, 5]
print_duplicates(numbers_list)
