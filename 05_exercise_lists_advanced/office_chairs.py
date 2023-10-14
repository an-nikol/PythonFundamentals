num_of_rooms = int(input())

counter_total_free_chairs = 0

not_enough_chairs = False
for room in range(1, num_of_rooms + 1):
    command = input().split()
    seats_per_room = command[0]
    visitors = int(command[1])
    counter_for_current_seats = 0
    counter_needed_chairs = 0
    # keep track of X's
    for current_seat in seats_per_room:
        counter_for_current_seats += 1

    if counter_for_current_seats < visitors:
        counter_needed_chairs = visitors - counter_for_current_seats
        not_enough_chairs = True
        print(f'{counter_needed_chairs} more chairs needed in room {room}')

    elif counter_for_current_seats > visitors:
        counter_total_free_chairs += counter_for_current_seats - visitors

if not not_enough_chairs:
    print(f'Game On, {counter_total_free_chairs} free chairs left')

