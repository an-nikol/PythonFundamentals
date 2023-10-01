original_list = input().split()

original_list_to_integers = []
for current_string in original_list:
    original_list_to_integers.append(int(current_string))

count_of_numbers_to_remove = int(input())
for current_removal in range(1, count_of_numbers_to_remove + 1):
    num_to_remove = min(original_list_to_integers)
    original_list_to_integers.remove(num_to_remove)

converted_list_to_strings = []
for current_int in original_list_to_integers:
    converted_list_to_strings.append(str(current_int))

final_result = ', '.join(converted_list_to_strings)
print(final_result)
