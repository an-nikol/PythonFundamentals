import re

pattern = r'%([A-Z][a-z]+)%[^\|\$\%\.]*<([\w]+)[^\|\$\%\.]*\|([\d]+)\|[^\|\$\%\.]*([1-9]+[.0-9]*)\$'
total_sum = 0

command = input()
while command != 'end of shift':
    matches = re.search(pattern, command)

    if matches:
        groups = matches.groups()
        name = groups[0]
        product = groups[1]
        qty = int(groups[2])
        price = float(groups[3])

        sum_per_customer = price * qty
        total_sum += sum_per_customer
        print(f"{name}: {product} - {sum_per_customer:.2f}")

    command = input()
print(f'Total income: {total_sum:.2f}')