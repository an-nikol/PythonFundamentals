def find(string, c):
    return [i for i, letter in enumerate(string) if letter == c]


empty_word = ''

command = input()

while command != 'End':
    command_info = command.split()
    current_command = command_info[0]

    # add word to empty str
    if current_command == 'Add':
        word = command_info[1]
        empty_word = empty_word + word
        # upgrade instruction
    elif current_command == 'Upgrade':
        char = command_info[1]
        empty_word = empty_word.replace(char, chr(ord(char) + 1))
    elif current_command == 'Print':
        print(empty_word)
    elif current_command == 'Index':
        char = command_info[1]
        if char in empty_word:
            list_of_indexes = find(empty_word, char)
            print(f"{' '.join(map(str, list_of_indexes))}")
        else:
            print('None')
    # remove instruction
    elif current_command == 'Remove':
        word = command_info[1]
        empty_word = empty_word.replace(word, '')
    command = input()