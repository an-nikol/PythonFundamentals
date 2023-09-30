factor = int(input())
length_of_list = int(input())

list_of_numbers = [factor]

counter = 1
next_number = factor

while counter < length_of_list:
    next_number += factor
    list_of_numbers.append(next_number)
    counter += 1

print(list_of_numbers)