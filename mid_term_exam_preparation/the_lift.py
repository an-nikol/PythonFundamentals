number_of_people = int(input())
all_people = number_of_people
state_of_the_lift = input().split() # ['0', '0']
max_places_per_wagon = 4

# the final sum of the seats in the lift
total_sum_of_seats_in_lift = sum([int(num) for num in state_of_the_lift])

lift_empty_places = (len(state_of_the_lift) * max_places_per_wagon) - total_sum_of_seats_in_lift

for wagon in range(len(state_of_the_lift)):
    # - seats and + people
    if int(state_of_the_lift[wagon]) < 4 and number_of_people >= 4:
        number_of_people -= max_places_per_wagon - int(state_of_the_lift[wagon])
        state_of_the_lift[wagon] = str(max_places_per_wagon)
    # - seats and - people
    elif int(state_of_the_lift[wagon]) < 4 and number_of_people < 4:
        state_of_the_lift[wagon] = str(int(state_of_the_lift[wagon]) + number_of_people)
        number_of_people = 0
        break


if number_of_people == 0 and lift_empty_places > all_people:
    print("The lift has empty spots!")
    print(" ".join(state_of_the_lift))
elif number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
    print(" ".join(state_of_the_lift))
elif lift_empty_places == all_people and number_of_people == 0:
    print(" ".join(state_of_the_lift))