list_of_string_numbers = input().split(', ')

list_of_integer_numbers = []

for current_number in list_of_string_numbers:
    current_number_to_integer = int(current_number)
    list_of_integer_numbers.append(current_number_to_integer)

for current_number in list_of_integer_numbers:
    if current_number == 0:
        list_of_integer_numbers.remove(current_number)
        list_of_integer_numbers.append(current_number)

print(list_of_integer_numbers)
