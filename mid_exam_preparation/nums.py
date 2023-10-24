original_list_of_numbers = list(map(int, input().split()))

average_sum = sum(original_list_of_numbers) / len(original_list_of_numbers)

nums_above_average = []

is_length_bigger_than_5 = False
for num in original_list_of_numbers:
    if num > average_sum:
        nums_above_average.append(num)

if len(nums_above_average) == 0:
    print('No')


top_5_nums = []
if len(nums_above_average) > 5:
    is_length_bigger_than_5 = True
    while len(top_5_nums) < 5:
        current_max_value = max(nums_above_average)
        top_5_nums.append(current_max_value)
        nums_above_average.remove(current_max_value)

nums_above_average.sort(reverse=True)
str_nums_above_average = list(map(str, nums_above_average))
str_top_5_nums = list(map(str, top_5_nums))


if is_length_bigger_than_5:
    print(' '.join(str_top_5_nums))
else:
    print(' '. join(str_nums_above_average))




