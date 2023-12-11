command = input()

stock = {}

all_sold_goods = 0

while command != 'Complete':
    command_info = command.split()
    instruction = command_info[0]

    if instruction == 'Receive':
        qty = int(command_info[1])
        food = command_info[2]
        if food not in stock:
            stock[food] = 0
        if qty > 0:
            stock[food] += qty

    elif instruction == 'Sell':
        needed_qty = int(command_info[1])
        sold_food = command_info[2]

        if sold_food not in stock:
            print(f'You do not have any {sold_food}.')
        elif needed_qty > stock[sold_food]:
            print(f"There aren't enough {sold_food}. You sold the last {stock[sold_food]} of them.")
            all_sold_goods += stock[sold_food]
            del stock[sold_food]
        elif needed_qty <= stock[sold_food]:
            stock[sold_food] -= needed_qty
            print(f"You sold {needed_qty} {sold_food}.")
            all_sold_goods += needed_qty
            if stock[sold_food] <= 0:
                del stock[sold_food]
    command = input()

for curr_food in stock:
    print(f'{curr_food}: {stock[curr_food]}')

print(f'All sold: {all_sold_goods} goods')