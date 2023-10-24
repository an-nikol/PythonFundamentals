goal_ticket_money = 150
collection_of_items = input().split('|')
budget_before_selling = float(input())

profit_after_selling = 0
list_with_bought_items = []

sum_of_all_new_prices = 0

for item in range(len(collection_of_items)):
    structure_of_items = collection_of_items[item].split('->')
    type_of_item = structure_of_items[0]
    price_of_item = float(structure_of_items[1])

    if type_of_item == 'Clothes':
        if not price_of_item <= 50.00:
            continue
    elif type_of_item == 'Shoes':
        if not price_of_item <= 35.00:
            continue
    elif type_of_item == 'Accessories':
        if not price_of_item <= 20.50:
            continue

    if price_of_item > budget_before_selling:
        continue

    budget_before_selling -= price_of_item
    markup = price_of_item * 0.40
    current_sold_price_item = price_of_item + markup
    list_with_bought_items.append(current_sold_price_item)
    sum_of_all_new_prices += current_sold_price_item
    profit_after_selling += markup


for item in list_with_bought_items:
    print(f'{item:.02f}', end=' ')

final_budget = sum_of_all_new_prices + budget_before_selling
print()
print(f'Profit: {profit_after_selling:.2f}')

if final_budget >= goal_ticket_money:
    print('Hello, France!')
else:
    print('Not enough money.')