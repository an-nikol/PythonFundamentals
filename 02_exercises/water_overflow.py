water_tank_capacity = 255

number_of_times_pouring_in_the_tank = int(input())

current_litters = 0

while True:
    for pour in range(number_of_times_pouring_in_the_tank):
        pouring_litters = int(input())
        current_litters += pouring_litters
        if current_litters > water_tank_capacity:
            current_litters -= pouring_litters
            print('Insufficient capacity!')
    break

print(current_litters)
