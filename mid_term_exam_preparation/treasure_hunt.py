treasure_chest = input().split('|')

command = input().split()
stolen_items = []
are_stolen_items = False
while command[0] != 'Yohoho!':
    type_of_command = command[0]
    if type_of_command == 'Loot':
        for item in range(1, len(command)):
            if command[item] not in treasure_chest:
                treasure_chest.insert(0, command[item])

    elif type_of_command == 'Drop':
        idx = int(command[-1])
        if 0 <= idx < len(treasure_chest):
            removed = treasure_chest.pop(idx)
            treasure_chest.append(removed)

    elif type_of_command == 'Steal':
        # if the items are not enough to fulfill the command, take as much as there are
        count_steals = min(int(command[-1]), len(treasure_chest))
        stolen_items = []
        for steal in range(count_steals, 0, -1):
            stolen_items.append(treasure_chest[-steal])
            treasure_chest.remove(treasure_chest[-steal])

        print(f"{', '.join(stolen_items)}")  # print the stolen items

    command = input().split()

if len(treasure_chest) > 0:
    total_treasure_gain = 0
    for item in treasure_chest:
        total_treasure_gain += len(item)

    average_treasure_gain = total_treasure_gain / len(treasure_chest)
    print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
