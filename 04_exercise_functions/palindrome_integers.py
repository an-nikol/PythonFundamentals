list_of_numbers = input().split(', ')

for current_number in list_of_numbers:
    reversed_num = current_number[::-1]
    if reversed_num == current_number:
        print('True')
    else:
        print('False')
