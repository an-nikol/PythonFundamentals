single_string = input()
result = single_string.replace(',', '')
animals = result.split()

for index, item in enumerate(animals[::-1]):
    if animals[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    if item == 'wolf':
        sheep_count = animals[index - 1]
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
        break