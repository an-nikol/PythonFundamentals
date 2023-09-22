number_of_people_in_a_group = int(input())
number_of_days = int(input())

coins_counter = 0

for day in range(1, number_of_days + 1):
    # at the beginning of every tenth day 2 people leave
    if day % 10 == 0:
        number_of_people_in_a_group -= 2
    # at the beginning of every 15th day 5 new people join the group
    if day % 15 == 0:
        number_of_people_in_a_group += 5
    # every third day you organise a party and spend coins for water
    if day % 3 == 0:
        coins_counter -= number_of_people_in_a_group * 3
    # every fifth day you slay a monster and gain coins
    if day % 5 == 0:
        coins_counter += number_of_people_in_a_group * 20
        # if there is a party the same day you spend more money
        if day % 3 == 0:
            coins_counter -= number_of_people_in_a_group * 2

    # coins earned every day
    coins_counter += 50
    # coins spent every day for food
    coins_counter -= number_of_people_in_a_group * 2

coins_per_person = coins_counter // number_of_people_in_a_group
print(f'{number_of_people_in_a_group} companions received {coins_per_person} coins each.')
