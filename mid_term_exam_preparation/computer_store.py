prices_without_taxes = 0
taxes = 0
type_of_customer = ''

is_order_valid = True

while True:
    command = input() # check for special or regular
    if command == 'special' or command == 'regular':
        type_of_customer = command
        break
    current_price = float(command)
    # check for valid input
    if current_price < 0:
        print('Invalid price!')
        continue
    prices_without_taxes += current_price
    taxes += current_price * 0.20

total_price = (prices_without_taxes + taxes)
if total_price == 0:
    is_order_valid = False
    print('Invalid order!')

if is_order_valid:
    if type_of_customer == 'special':
        total_price = (prices_without_taxes + taxes) * 0.90

    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {prices_without_taxes:.2f}$"
          f"\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")






