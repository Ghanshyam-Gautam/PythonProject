#Write a function that gets a list of integers as a parameter.
#The function returns a second list that is otherwise the
# same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original as well as the cut-down list.


def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

original_list = [3, 8, 17, 20, 7, 12, 1, 4]
filtered_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("Even-only list:", filtered_list)