def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    else:
        print("Invalid indices. Please ensure both indices are within the range of the list.")
my_list = list(map(int, input("Enter the elements of the list: ").split()))
index1 = int(input("Enter the first index to swap: "))
index2 = int(input("Enter the second index to swap: "))
swap_elements(my_list, index1, index2)
print("List after swapping elements:", my_list)