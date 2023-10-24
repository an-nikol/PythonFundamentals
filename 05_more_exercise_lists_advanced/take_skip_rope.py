string = input()

numbers = []
letters = ''
take_list = []
skip_list = []

final_string = ''

# split the list into numbers and letters
for character in string:
    if character.isdigit():
        numbers.append(int(character))
    else:
        letters += character

# check if nums are even or not
for index, num in enumerate(numbers):
    if index % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)

# iterate over both lists
for take, skip in zip(take_list, skip_list):
    if take == 0:
        letters = letters[skip:]
    elif take != 0:
        final_string += letters[:take]
        letters = letters[skip + take:]

print(final_string)