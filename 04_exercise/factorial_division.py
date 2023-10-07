import math


def factorial(n1, n2):
    n1_factorial_sum = math.factorial(n1)
    n2_factorial_sum = math.factorial(n2)
    result = n1_factorial_sum / n2_factorial_sum
    print(f'{result:.2f}')


first_number = int(input())
second_number = int(input())
factorial(first_number, second_number)