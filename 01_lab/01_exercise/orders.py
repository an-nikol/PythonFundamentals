number_of_orders = int(input())

total_sum = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    elif 0 > days or days > 31:
        continue
    elif 1 > capsules_needed_per_day or capsules_needed_per_day > 2000:
        continue

    current_sum = (price_per_capsule * capsules_needed_per_day) * days
    total_sum += current_sum
    print(f'The price for the coffee is: ${current_sum:.02f}')

print(f'Total: ${total_sum:.02f}')
