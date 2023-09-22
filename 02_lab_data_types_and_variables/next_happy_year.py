# find the numbers with only distinct digits
year = int(input())

# set in the beginning the bool to False to create a while not loop
year_is_special = False
while not year_is_special:
    year += 1
    year_to_string = str(year)
    # set the boolean to True so that the while-loop to exit if there are duplicating numbers
    year_is_special = True
    for digit in year_to_string:
        # the count command counts the number of duplicate numbers
        if year_to_string.count(digit) != 1:
            # if there are duplicating numbers exit the for-loop and continue searching
            year_is_special = False
            break
print(year)





