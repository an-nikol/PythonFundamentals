def fire(index, dmg):
    # check if index is valid
    warship_ship[index] -= dmg


def repair(index, hp):
    pirate_ship[index] += hp
    if pirate_ship[index] >= max_health_per_section:
        pirate_ship[index] = max_health_per_section


pirate_ship = list(map(int, input().split('>')))
warship_ship = list(map(int, input().split('>')))

max_health_per_section = int(input())

is_stalemate = True
command = input()
while command != 'Retire':
    if command == 'Status':
        sections_that_need_repair = 0
        for section in range(len(pirate_ship)):
            min_hp = max_health_per_section * 0.20
            if pirate_ship[section] < min_hp:
                sections_that_need_repair += 1
        print(f'{sections_that_need_repair} sections need repair.')

    command = command.split()
    task = command[0]

    if task == 'Fire':
        idx = int(command[1])  
        damage = int(command[2])
        # if index is valid, enter the function
        if 0 <= idx < len(warship_ship):
            fire(idx, damage)
            # check if the section is destroyed
            if warship_ship[idx] <= 0:
                is_stalemate = False
                print('You won! The enemy ship has sunken.')
                break

    elif task == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        # check if both indexes are valid
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            # check if section is destroyed
            for curr_section in range(start_index, end_index + 1):
                pirate_ship[curr_section] -= damage
                if pirate_ship[curr_section] <= 0:
                    is_stalemate = False
                    print('You lost! The pirate ship has sunken.')
                    break

    elif task == 'Repair':
        idx = int(command[1])
        health = int(command[2])
        # check if idx is valid
        if 0 <= idx < len(pirate_ship):
            repair(idx, health)

    command = input()

if is_stalemate:
    print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship_ship)}')
