number_of_plants = int(input())

dict_plant_rarity = {}
dict_plant_rating = {}

for plant in range(number_of_plants):
    plant_info = input().split('<->')
    plant_name = plant_info[0]
    plant_rarity = int(plant_info[1])

    # *
    if plant not in dict_plant_rarity:
        dict_plant_rarity[plant_name] = 0
    dict_plant_rarity[plant_name] = plant_rarity

command = input()

while command != 'Exhibition':
    command_and_plant_info = command.split(': ')
    instruction = command_and_plant_info[0]
    if instruction == 'Rate':
        plant_and_rating = command_and_plant_info[1].split(' - ')
        plant = plant_and_rating[0]
        rating = int(plant_and_rating[1])

        if plant not in dict_plant_rarity:
            print('error')

        if plant in dict_plant_rarity:
            if plant not in dict_plant_rating:
                dict_plant_rating[plant] = []
            dict_plant_rating[plant].append(rating)


    elif instruction == 'Update':
        plant_new_rarity = command_and_plant_info[1].split(' - ')
        plant = plant_new_rarity[0]
        new_rarity = int(plant_new_rarity[1])

        if plant in dict_plant_rarity:
            dict_plant_rarity[plant] = new_rarity
        else:
            print('error')

    elif instruction == 'Reset':
        plant_new_rarity = command_and_plant_info[1].split(' - ')
        plant = plant_new_rarity[0]
        if plant in dict_plant_rating:
            dict_plant_rating[plant] = []
        else:
            print('error')

    command = input()

print('Plants for the exhibition:')

average_rating = 0.00
for plant in dict_plant_rarity:
    if dict_plant_rating[plant]:
        average_rating = sum(dict_plant_rating[plant]) / len(dict_plant_rating[plant])
        print(f'- {plant}; Rarity: {dict_plant_rarity[plant]}; Rating: {average_rating:.2f}')
    else:
        print(f'- {plant}; Rarity: {dict_plant_rarity[plant]}; Rating: {average_rating:.2f}')
