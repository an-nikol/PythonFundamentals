# create and search a dict
stock_information = input().split()

stock_dict = {}

for i in range(0, len(stock_information), 2):
    food_key = stock_information[i]
    food_value = int(stock_information[i + 1])
    stock_dict[food_key] = food_value

# search for products in dict
searched_products = input().split()

for current_product in searched_products:
    if current_product in stock_dict:
        print(f'We have {stock_dict[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')