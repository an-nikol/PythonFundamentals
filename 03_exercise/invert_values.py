string_numbers = input()

original_list = string_numbers.split()
strings_to_integers = []
opposite_list = []

# convert a list of strings to integers

for element in original_list:
    strings_to_integers.append(int(element))

for number in strings_to_integers:
    if number > 0:
        opposite_number = -abs(number)
        opposite_list.append(opposite_number)
    elif number <= 0:
        opposite_number = abs(number)
        opposite_list.append(opposite_number)

print(opposite_list)