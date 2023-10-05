list_of_numbers = list(map(float, input().split()))

list_of_rounded_numbers = []


def round_numbers(number):
    rounded_number = round(number)
    return rounded_number


for current_number in list_of_numbers:
    converted_number = round_numbers(current_number)
    list_of_rounded_numbers.append(converted_number)

print(list_of_rounded_numbers)
