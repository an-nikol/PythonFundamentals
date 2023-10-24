list_of_gifts = input().split()

while True:
    line = input()
    if line == 'No Money':
        break
    # split the line into a command[0] and a gift[1]
    command = line.split()
    current_gift = command[1]

    # imply the instructions for each command
    if command[0] == 'OutOfStock':
        # 1) find the name of the gift in the line 2) change its value to 'None'
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == current_gift:
                list_of_gifts[index] = 'None'

    elif command[0] == 'Required':
        # make the index an int
        index = int(command[2])
        # check if the index is valid
        if 0 <= index < len(list_of_gifts):
            # set the index's value to the given gift
            list_of_gifts[index] = current_gift

    elif command[0] == 'JustInCase':
        # the last element of the list
        list_of_gifts[-1] = current_gift

# print each gift of the sequence without None
for gift in list_of_gifts:
    if gift != 'None':
        print(gift, end=' ')
