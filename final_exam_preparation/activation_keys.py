# letters and numbers only
activation_key = input()

command = input()

while command != 'Generate':
    # strings with instructions
    instructions_info = command.split('>>>')
    instruction = instructions_info[0]

    if instruction == 'Contains':
        substring = instructions_info[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif instruction == 'Flip':
        upper_or_lower = instructions_info[1]
        start_idx = int(instructions_info[2])
        end_idx = int(instructions_info[3])
        if upper_or_lower == 'Upper':
            part_to_be_added = activation_key[start_idx:end_idx].upper()
            activation_key = activation_key[:start_idx] + part_to_be_added + activation_key[end_idx:]
            print(f'{activation_key}')

        elif upper_or_lower == 'Lower':
            part_to_be_added = activation_key[start_idx:end_idx].lower()
            activation_key = activation_key[:start_idx] + part_to_be_added + activation_key[end_idx:]
            print(f'{activation_key}')

    elif instruction == 'Slice':
        start_idx = int(instructions_info[1])
        end_idx = int(instructions_info[2])
        part_to_be_deleted = activation_key[start_idx:end_idx]
        activation_key = activation_key.replace(part_to_be_deleted,'')
        print(f'{activation_key}')
    command = input()

print(f'Your activation key is: {activation_key}')
