list_of_phones = input().split(', ')

command = input()

while command != 'End':
    type_of_command = command.split(' - ')[0]
    phone = command.split(' - ')[1]
    if type_of_command == 'Add':
        if phone not in list_of_phones:
            list_of_phones.append(phone)
    elif type_of_command == 'Remove':
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif type_of_command == 'Bonus phone':
        old_and_new_phone = phone.split(':')
        old_phone = old_and_new_phone[0]
        new_phone = old_and_new_phone[1]
        if old_phone in list_of_phones:
            idx_of_old_phone = list_of_phones.index(old_phone)
            list_of_phones.insert(idx_of_old_phone + 1, new_phone)
    elif type_of_command == 'Last':
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

    command = input()

print(f"{', '.join(list_of_phones)}")