# convert a list of string numbers to a list of integers
list_of_integer_numbers = list(map(int, input().split()))

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x % 2 == 0), list_of_integer_numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)