# read user input
number = int(input())

# create an empty list to store the digits of the number
digits = []

# loop through each digit and convert the int to a str, because the digit.append command works only with strings
for i in str(number):
    # adds items to the empty list I created
    digits.append(i)

# sort the list in descending order
digits.sort(reverse=True)

# print the output without square brackets, commas and spaces between the numbers
for item in digits:
    print(item, sep='-foo-',end='')

