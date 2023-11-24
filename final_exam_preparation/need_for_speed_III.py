number_of_cars = int(input())

dict_brand_miles = {}
dict_brand_fuel = {}

for car in range(number_of_cars):
    line = input()
    # add cars to dicts
    car_info = line.split('|')
    car_brand, miles, fuel = car_info[0], car_info[1], car_info[2]

    if car_brand not in dict_brand_miles:
        dict_brand_miles[car_brand] = int(miles)

    if car_brand not in dict_brand_fuel:
        dict_brand_fuel[car_brand] = int(fuel)

command = input()

while command != 'Stop':
    instruction_info = command.split(' : ')
    instruction = instruction_info[0]
    car = instruction_info[1]
    max_mileage = 100000

    if instruction == 'Drive':
        distance = int(instruction_info[2])
        used_fuel = int(instruction_info[3])
        if dict_brand_fuel[car] < used_fuel:
            print('Not enough fuel to make that ride')
        else:
            dict_brand_miles[car] += distance
            dict_brand_fuel[car] -= used_fuel
            print(f'{car} driven for {distance} kilometers. {used_fuel} liters of fuel consumed.')

        if dict_brand_miles[car] >= max_mileage:
            del dict_brand_miles[car]
            del dict_brand_fuel[car]
            print(f'Time to sell the {car}!')

    elif instruction == 'Refuel':
        added_fuel = int(instruction_info[2])
        max_tank = 75

        if dict_brand_fuel[car] < max_tank:
            diff_to_max = max_tank - dict_brand_fuel[car]
            if added_fuel > diff_to_max:
                added_fuel = diff_to_max
                dict_brand_fuel[car] += diff_to_max
            else:
                dict_brand_fuel[car] += added_fuel
            print(f'{car} refueled with {added_fuel} liters')

    elif instruction == 'Revert':
        km = int(instruction_info[2])
        minimum_mils = 10000

        dict_brand_miles[car] -= km
        if dict_brand_miles[car] >= minimum_mils:
            print(f'{car} mileage decreased by {km} kilometers')
        else:
            dict_brand_miles[car] = minimum_mils

    command = input()

for car, miles in dict_brand_miles.items():
    print(f'{car} -> Mileage: {miles} kms, Fuel in the tank: {dict_brand_fuel[car]} lt.')