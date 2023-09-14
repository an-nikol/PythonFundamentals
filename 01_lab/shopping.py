budget = int(input())
total = 0

while True:
    prices = input()
    if prices == 'End':
        print('You bought everything needed.')
        break
    else:
        prices = int(prices)
        total += prices
        if budget < total:
            print('You went in overdraft!')
            break
