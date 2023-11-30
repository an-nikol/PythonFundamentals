text = input()

command = input()

while command != 'Done':
    command_info = command.split()
    instruction = command_info[0]

    if instruction == 'TakeOdd':
        new_raw_pass = ''
        for idx in range(len(text)):
            if idx % 2 != 0:
                new_raw_pass += text[idx]
        text = new_raw_pass
        print(text)
    elif instruction == 'Cut':
        index = int(command_info[1])
        length = int(command_info[2])
        part_to_be_removed = text[index:index + length]
        text = text.replace(part_to_be_removed, '', 1)
        print(text)

    elif instruction == 'Substitute':
        old_substring = command_info[1]
        new_substring = command_info[2]
        if old_substring in text:
            text = text.replace(old_substring, new_substring)
            print(text)
        else:
            print('Nothing to replace!')

    command = input()

print(f'Your password is: {text}')