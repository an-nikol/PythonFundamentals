number_of_lines = int(input())

list_of_positive_numbers = []
list_of_negative_numbers = []

for line in range(1, number_of_lines + 1):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive_numbers.append(current_number)
    else:
        list_of_negative_numbers.append(current_number)

count_of_positive_numbers = len(list_of_positive_numbers)
sum_of_negative_numbers = sum(list_of_negative_numbers)

print(list_of_positive_numbers)
print(list_of_negative_numbers)
print(f'Count of positives: {count_of_positive_numbers}')
print(f'Sum of negatives: {sum_of_negative_numbers}')