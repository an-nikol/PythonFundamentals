original_str_all_stops = input()

command = input()
while command != 'Travel':
    travel_info = command.split(':')
    instruction = travel_info[0]
    if instruction == 'Add Stop':
        idx = int(travel_info[1])
        curr_str = travel_info[2]
        # check if idx is valid
        if idx < len(original_str_all_stops):
            original_str_all_stops = original_str_all_stops[:idx] + curr_str + original_str_all_stops[idx:]
        print(original_str_all_stops)

    elif instruction == 'Remove Stop':
        start_idx = int(travel_info[1])
        end_idx = int(travel_info[2])
        if start_idx < len(original_str_all_stops) and end_idx < len(original_str_all_stops):
            removed_part = original_str_all_stops[start_idx:end_idx + 1]
            original_str_all_stops = original_str_all_stops.replace(removed_part, '')
        print(original_str_all_stops)

    elif instruction == 'Switch':
        old_str = travel_info[1]
        new_str = travel_info[2]
        if old_str in original_str_all_stops:
            original_str_all_stops = original_str_all_stops.replace(old_str, new_str)
        print(original_str_all_stops)
    command = input()

print(f'Ready for world tour! Planned stops: {original_str_all_stops}')