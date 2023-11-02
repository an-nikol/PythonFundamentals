command = input()

product_dict = {}
while command != 'statistics':
    product_information = command.split(': ')
    food_key = product_information[0]
    food_value = int(product_information[1])
    if food_key in product_dict:
        product_dict[food_key] += food_value
    else:
        product_dict[food_key] = food_value
    command = input()

count_of_products = len(product_dict)
total_qty = sum(product_dict.values())

print('Products in stock:')

for food_key, food_value in product_dict.items():
    print(f'- {food_key}: {food_value}')

print(f'Total Products: {count_of_products}')
print(f'Total Quantity: {total_qty}')