# search contacts by key

phonebook_dict = {}

command = input()

while '-' in command:
    contact_info = command.split('-')
    key = contact_info[0]
    value = contact_info[1]
    phonebook_dict[key] = value

    command = input()

number_of_contacts_to_search = int(command)


for i in range(number_of_contacts_to_search):
    current_contact = input()
    for key, value in phonebook_dict.items():
        if key == current_contact:
            print(f'{key} -> {value}')
    if current_contact not in phonebook_dict:
        print(f'Contact {current_contact} does not exist.')
