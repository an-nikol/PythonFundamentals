# adding kvps in dicts

product_information = input().split()

stock_dict = {}

for i in range(0, len(product_information), 2):
    food = product_information[i]
    qty = int(product_information[i + 1])
    # insert a value to the key
    stock_dict[food] = qty

print(stock_dict)