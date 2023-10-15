initial_schedule = input().split(', ')
schedule = initial_schedule.copy()
line2 = input()
while line2 != 'course start':
    command = line2.split(':')
    if 'Add' in command:
        if command[1] not in schedule:
            schedule.append(command[1])
    elif 'Insert' in command:
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])
    elif 'Remove' in command:
        if command[1] in schedule:
            schedule.remove(command[1])
            if f'{command[1]}-Exercise' in schedule:
                schedule.remove(f'{command[1]}-Exercise')
    elif 'Swap' in command:
        if command[1] in schedule and command[2] in schedule:
            lesson1_i = schedule.index(command[1])
            lesson2_i = schedule.index(command[2])
            schedule[lesson1_i], schedule[lesson2_i] = schedule[lesson2_i], schedule[lesson1_i]
            for lesson_name, lesson_index in zip([command[1], command[2]], [lesson1_i, lesson2_i]):
                if f"{lesson_name}-Exercise" in schedule:
                    schedule.remove(f"{lesson_name}-Exercise")
                    if lesson_index < schedule.index(lesson_name):
                        schedule.insert(schedule.index(lesson_name), f"{lesson_name}-Exercise")
                    else:
                        schedule.insert(schedule.index(lesson_name) + 1, f"{lesson_name}-Exercise")
    elif 'Exercise' in command:
        if command[1] in schedule and f"{command[1]}-Exercise" not in schedule:
            lesson_i = schedule.index(command[1])
            schedule.insert(lesson_i + 1, f'{command[1]}-Exercise')
        elif command[1] not in schedule:
            schedule.append(command[1])
            schedule.append(f'{command[1]}-Exercise')
    line2 = input()
for i, lesson in enumerate(schedule, 1):
    print(f'{i}.{lesson}')