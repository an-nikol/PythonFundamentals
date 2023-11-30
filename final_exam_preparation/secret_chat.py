message = input()

command = input()

while command != 'Reveal':
    command_info = command.split(':|:')
    instruction = command_info[0]

    if instruction == 'InsertSpace':
        idx = int(command_info[1])
        message = message[:idx] + ' ' + message[idx:]
        print(message)
    elif instruction == 'Reverse':
        substring = command_info[1]
        if substring in message:
            # replace only the first occurrence
            message = message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            message = message + reversed_substring
            print(message)
        else:
            print('error')
    elif instruction == 'ChangeAll':
        # replace all occurrences in a string
        substring, replacement = command_info[1], command_info[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)

    command = input()

print(f'You have a new text message: {message}')