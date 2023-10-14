first_line = input().split(', ')
second_line = input().split(', ')
converted_list = []

# check the first line string by string
for first_string in first_line:
    # check the second line string by string
    for second_string in second_line:
        # check if the current first string is in the current second string
        if first_string in second_string:
            converted_list.append(first_string)
            break

print(converted_list)
