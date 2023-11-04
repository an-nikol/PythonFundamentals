command = input()

# create two separate dicts for qty and prices
dict_qty = {}
dict_prices = {}

while command != 'buy':
    current_product = command. split()
    name_product, price, qty = current_product[0], float(current_product[1]), float(current_product[2])

    if name_product not in dict_qty:
        # create a kvp for the qty and prices for each product
        dict_qty[name_product] = 0
        dict_prices[name_product] = 0
    # add the corresponding qty and prices in the two dicts of each product
    dict_qty[name_product] += qty
    dict_prices[name_product] = price
    command = input()

for key, value in dict_qty.items():
    # since the keys are the same in both lists you get the the wanted value by iterating only through one list
    result = value * dict_prices[key]
    print(f'{key} -> {result:.2f}')