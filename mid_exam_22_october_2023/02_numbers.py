list_of_numbers = list(map(int, input().split()))

command = input()

while command != 'Finish':
    split_lines = command.split()
    type_of_command = split_lines[0]
    value = int(split_lines[1])
    if type_of_command == 'Add':
        # check if it exists?
        list_of_numbers.append(value)
    elif type_of_command == 'Remove':
        # check for valid input
        if value in list_of_numbers:
            list_of_numbers.remove(value)
    elif type_of_command == 'Replace':
        # check for valid input
        if value in list_of_numbers:
            replacement = int(split_lines[2])
            idx_of_value = list_of_numbers.index(value)
            list_of_numbers[idx_of_value] = replacement
    elif type_of_command == 'Collapse':
        list_of_numbers = [num for num in list_of_numbers if num >= value]

    command = input()

str_list_nums = list(map(str, list_of_numbers))

joined_list = ' '.join(str_list_nums)
print(joined_list)
