number = int(input())


def perfect_num(n):
    divisors = []
    if n > 0:
        for current_divisor in range(1, n):
            if n % current_divisor == 0:
                divisors.append(current_divisor)
    if sum(divisors) == n:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


perfect_num(number)
