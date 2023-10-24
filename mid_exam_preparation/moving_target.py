targets = [int(num) for num in input().split()]

while True:
    command = input().split()

    if command[0] == 'Shoot':
        idx = int(command[1])
        power = int(command[2])
        # check for valid input
        if 0 <= idx < len(targets):
            targets[idx] -= power
            if targets[idx] <= 0:
                targets.pop(idx)

    elif command[0] == 'Add':
        idx = int(command[1])
        value = int(command[2])
        # check for valid input
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print('Invalid placement!')
    elif command[0] == 'Strike':
        idx = int(command[1])
        radius = int(command[2])
        start_index = idx - radius
        end_index = idx + radius
        # check for valid input
        if 0 <= idx < len(targets) and  0 <= start_index < len(targets) and 0 <= end_index < len(targets):
            del targets[start_index:end_index + 1]
        else:
            print('Strike missed!')

    elif command[0] == 'End':
        str_targets = [str(num) for num in targets]
        print(f"{'|'.join(str_targets)}")
        break

