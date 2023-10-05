string_numbers = input().split()

absolute_list_values = []

for number in string_numbers:
    converted_number = abs(float(number))
    absolute_list_values.append(converted_number)

print(absolute_list_values)