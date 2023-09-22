n = int(input())

# loop through every number until n
for current_number in range(1, n + 1):
    # convert current number to string
    current_number_to_str = str(number)
    # create a counter for digits before the second for-loop, so that it restarts with each iteration
    digits_sum = 0
    # extract each digit from the number
    for digit in current_number_to_str:
        digits_sum += int(digit)
    # create a bool False in the first for-loop so that it restarts with every new number
    is_special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        # switch the bool to True if the sum is correct
        is_special = True
    # print each number in the sequence
    print(f'{number} -> {is_special}')