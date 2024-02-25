def print_negative_numbers(my_list):
    negative_numbers = [num for num in my_list if num < 0]
    if negative_numbers:
        print("Negative numbers in the list:", negative_numbers)
    else:
        print("No negative numbers in the list.")

num_list = [int(x) for x in input("Enter elements of the list separated by spaces: ").split()]
print_negative_numbers(num_list)
