original_array = list(map(int, input().split()))

command = input()  # 'End'

while command != 'end':
    command = command.split()
    task = command[0]

    if task == 'swap':
        first_index = int(command[1])
        second_index = int(command[2])
        original_array[first_index], original_array[second_index] = original_array[second_index], \
                                                                    original_array[first_index]
    elif task == 'multiply':
        first_index = int(command[1])
        second_index = int(command[2])
        result = original_array[first_index] * original_array[second_index]
        original_array[first_index] = result
    elif task == 'decrease':
        for num in range(len(original_array)):
            original_array[num] -= 1

    command = input()

str_modified_list = list(map(str, original_array))
print(', '.join(str_modified_list))