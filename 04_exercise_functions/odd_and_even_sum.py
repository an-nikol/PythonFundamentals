number = input()


def odd_and_even_digits_sum(string_number):
    sum_even_digits = 0
    sum_odd_digits = 0
    for current_num in string_number:
        str_to_int_num = int(current_num)
        if str_to_int_num % 2 == 0:
            sum_even_digits += str_to_int_num
        else:
            sum_odd_digits += str_to_int_num

    return f'Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}'


print(odd_and_even_digits_sum(number))
