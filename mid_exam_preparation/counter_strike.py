initial_energy = int(input())

counter_for_won_battles = 0
has_won = True
while True:
    command = input()
    if command == 'End of battle':
        break

    distance = int(command)
    if initial_energy < distance:
        has_won = False
        print(f'Not enough energy! Game ends with {counter_for_won_battles} won battles and {initial_energy} energy')
        break
    initial_energy -= distance
    counter_for_won_battles += 1
    if counter_for_won_battles % 3 == 0:
        initial_energy += counter_for_won_battles

if has_won:
    print(f'Won battles: {counter_for_won_battles}. Energy left: {initial_energy}')