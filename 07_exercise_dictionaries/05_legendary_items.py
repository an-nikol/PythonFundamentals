# part of the wanted output directly set in the text of the problem
my_dict = {'shards': 0, 'fragments': 0, 'motes': 0}


is_obtained = False
legendary_item = ''

while not is_obtained:
    item_information = input().split()
    # get the info for the kvps in the correct order
    for idx in range(0, len(item_information), 2):
        value_material = int(item_information[idx])
        key_material = item_information[idx + 1].lower()

        # first, check for the materials of the legendary items
        if key_material == 'shards':
            legendary_item = 'Shadowmourne'
            my_dict['shards'] += value_material
            if my_dict[key_material] >= 250:
                is_obtained = True
                # subtract the used material
                my_dict[key_material] -= 250
                break

        elif key_material == 'fragments':
            legendary_item = 'Valanyr'
            my_dict['fragments'] += value_material
            if my_dict[key_material] >= 250:
                is_obtained = True
                my_dict[key_material] -= 250
                break

        elif key_material == 'motes':
            legendary_item = 'Dragonwrath'
            my_dict['motes'] += value_material
            if my_dict[key_material] >= 250:
                is_obtained = True
                my_dict[key_material] -= 250
                break

            # second, if you receive junk material, create a new kvp in the dict
        else:
            if key_material not in my_dict:
                my_dict[key_material] = 0
            my_dict[key_material] += value_material


print(f'{legendary_item} obtained!')

for key, value in my_dict.items():
    print(f'{key}: {value}')
