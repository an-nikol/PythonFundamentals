health = 100
bitcoins = 0

all_rooms = input().split('|') # ['rat 10', 'bat 20']
counter_rooms = 0
for current_room in all_rooms:
    command = current_room.split() # ['rat','10']
    task = command[0]
    qty = int(command[1])
    counter_rooms += 1
    if task == 'potion':
        if health + qty > 100:
            qty = 100 - health

        if health > 100:
            health = 100

        health += qty
        print(f'You healed for {qty} hp.')
        print(f'Current health: {health} hp.')

    elif task == 'chest':
        bitcoins += qty
        print(f'You found {qty} bitcoins.')
    else:
        health -= qty
        if health <= 0:
            print(f'You died! Killed by {task}.')
            print(f'Best room: {counter_rooms}')
            break
        else:
            print(f'You slayed {task}.')

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

