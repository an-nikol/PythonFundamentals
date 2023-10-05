products = input()
qty = int(input())


def final_sum(product_type, purchases):
    if product_type == 'coffee':
        result = purchases * 1.50
        return result
    elif product_type == 'coke':
        result = purchases * 1.40
        return result
    elif product_type == 'water':
        result = purchases * 1.00
        return result
    elif product_type == 'snacks':
        result = purchases * 2.00
        return result


print(f'{final_sum(products, qty):.2f}')
