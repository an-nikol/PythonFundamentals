number_of_wagons = int(input())

list_of_wagons = [0] * number_of_wagons

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'add':
        people = int(command[1])
        list_of_wagons[-1] += people
    elif command[0] == 'insert':
        index = int(command[1])
        list_of_wagons[index] += int(command[2])
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        list_of_wagons[index] -= int(command[2])

print(list_of_wagons)