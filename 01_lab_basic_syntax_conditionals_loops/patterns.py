number = int(input())

# first half of the triangle
for rows in range(1, number + 1):
    for col in range(rows): # the counting of the stars start from 0 and with the increasing of the rows so do the stars
        print('*', end='')
    print()

# second half of the triangle
for rows in range(number - 1, 0, -1):
    for col in range(rows):
        print('*', end='')
    print()
