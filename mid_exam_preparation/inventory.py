inventory = input().split(', ')

command = input()

while command != 'Craft!':
    task = command.split(" - ")[0]
    item = command.split(" - ")[1]

    if task == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif task == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif task == 'Combine Items':
        old_item = item.split(':')[0]
        new_item = item.split(':')[1]
        if old_item in inventory:
            idx_of_old_item = inventory.index(old_item)
            inventory.insert(idx_of_old_item + 1, new_item)
    elif task == 'Renew':
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()

print(f"{', '.join(inventory)}")