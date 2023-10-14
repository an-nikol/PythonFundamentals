current_version = list(map(int, input().split('.')))

first_num = current_version[0]
second_num = current_version[1]
third_num = current_version[2]

current_version[2] = third_num + 1

if current_version[2] > 9:
    current_version[2] = 0
    current_version[1] = second_num + 1

if current_version[1] > 9:
    current_version[1] = 0
    current_version[0] = first_num + 1

current_version = list(map(str, current_version))
print('.'.join(current_version))

