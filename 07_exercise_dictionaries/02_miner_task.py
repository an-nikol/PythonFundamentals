command = input()

my_dict = {}
my_list = []
while command != 'stop':
    my_list.append(command)
    command = input()


for idx in range(0, len(my_list), 2):
    key = my_list[idx]
    value = my_list[idx + 1]
    if key not in my_dict:
        my_dict[key] = int(value)
    else:
        my_dict[key] += int(value)

for key, value in my_dict.items():
    print(f'{key} -> {value}')