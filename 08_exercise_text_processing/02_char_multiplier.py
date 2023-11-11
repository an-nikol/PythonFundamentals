first_sting, second_string = input().split()

result = 0
# first case
if len(first_sting) > len(second_string):
    # multiplication
    for index in range(len(second_string)):
        result += ord(second_string[index]) * ord(first_sting[index])
    # adding the sum of left symbols
    for index in range(len(second_string), len(first_sting)):
        result += ord(first_sting[index])

# second case
elif len(first_sting) < len(second_string):
    for index in range(len(first_sting)):
        result += ord(second_string[index]) * ord(first_sting[index])
    for index in range(len(first_sting), len(second_string)):
        result += ord(second_string[index])

# third case
elif len(first_sting) == len(second_string):
    for index in range(len(first_sting)):
        result += ord(first_sting[index]) * ord(second_string[index])

print(result)

