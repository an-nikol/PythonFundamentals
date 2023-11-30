number_of_plants = int(input())

dict_plant_rarity = {}
dict_plant_rating = {}

# store info about the plants
for plant in range(number_of_plants):
    plant_info = input().split('<->')
    plant_name = plant_info[0]
    plant_rarity = int(plant_info[1])
    if plant_name not in dict_plant_rarity:
        dict_plant_rarity[plant_name] = plant_rarity
    # received more than once
    dict_plant_rarity[plant_name] = plant_rarity

command = input()
while command != 'Exhibition':
    command_info = command.split(' - ')
    first_part_info = command_info[0].split(': ')
    instruction = first_part_info[0]

    if instruction == 'Rate':
        curr_plant_name = first_part_info[1]
        rating = int(command_info[1])
        if curr_plant_name in dict_plant_rarity:
            if curr_plant_name not in dict_plant_rating:
                dict_plant_rating[curr_plant_name] = []
            dict_plant_rating[curr_plant_name].append(rating)
        else:
            print('error')

    elif instruction == 'Update':
        curr_plant_name = first_part_info[1]
        new_rarity = int(command_info[1])
        if curr_plant_name in dict_plant_rarity:
            if curr_plant_name in dict_plant_rating:
                dict_plant_rarity[curr_plant_name] = new_rarity
        else:
            print('error')

    elif instruction == 'Reset':
        curr_plant_name = first_part_info[1]
        if curr_plant_name in dict_plant_rarity:
            if curr_plant_name in dict_plant_rating:
                dict_plant_rating[curr_plant_name] = []
        else:
            print('error')

    command = input()

print('Plants for the exhibition:')
for plant in dict_plant_rarity:
    average_rating = 0
    if sum(dict_plant_rating[plant]):
        average_rating = sum(dict_plant_rating[plant]) / len(dict_plant_rating[plant])
    print(f" - {plant}; Rarity: {dict_plant_rarity[plant]}; Rating: {average_rating:.2f}")