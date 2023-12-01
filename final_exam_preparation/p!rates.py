
dict_city_population = {}
dict_city_gold = {}

command = input()
while command != 'Sail':
    data = command.split('||')
    city, population, gold = data[0], int(data[1]), int(data[2])

    if city not in dict_city_population:
        dict_city_population[city] = population
        dict_city_gold[city] = gold
    else:
        dict_city_population[city] += population
        dict_city_gold[city] += gold

    command = input()

event = input()

while event != 'End':
    event_info = event.split('=>')
    instruction, town = event_info[0], event_info[1]
    if instruction == 'Plunder':
        people = int(event_info[2])
        gold = int(event_info[3])
        dict_city_population[town] -= people
        dict_city_gold[town] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if dict_city_population[town] <= 0 or dict_city_gold[town] <= 0:
            del dict_city_population[town]
            del dict_city_gold[town]
            print(f'{town} has been wiped off the map!')

    elif instruction == 'Prosper':
        gold = int(event_info[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            dict_city_gold[town] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {dict_city_gold[town]} gold.')
    event = input()

if dict_city_population:
    print(f'Ahoy, Captain! There are {len(dict_city_population)} wealthy settlements to go to:')
    for curr_town in dict_city_population:
        print(f'{curr_town} -> Population: {dict_city_population[curr_town]} citizens, Gold: {dict_city_gold[curr_town]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')