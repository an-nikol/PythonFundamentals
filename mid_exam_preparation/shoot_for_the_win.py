targets = list(map(int, input().split()))

counter_for_shot_targets = 0

command = input()
while command != 'End':
    idx = int(command)
    # check for valid input
    if 0 <= idx < len(targets):
        original_value = targets[idx]
        targets[idx] = -1
        counter_for_shot_targets += 1
        for current_target in range(len(targets)):
            if targets[current_target] != -1:
                if targets[current_target] > original_value:
                    targets[current_target] -= original_value
                else:
                    targets[current_target] += original_value

    command = input()

str_targets_state = list(map(str, targets))
print(f"Shot targets: {counter_for_shot_targets} -> {' '.join(str_targets_state)}")