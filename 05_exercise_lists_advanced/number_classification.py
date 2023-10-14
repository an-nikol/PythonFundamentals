numbers = list(map(int, input().split(', ')))

list_of_positives = []
list_of_negatives = []
list_of_evens = []
list_of_odds = []

for num in numbers:
    if num >= 0:
        list_of_positives.append(num)
    if num < 0:
        list_of_negatives.append(num)
    if num % 2 == 0:
        list_of_evens.append(num)
    if num % 2 != 0:
        list_of_odds.append(num)

joined_positives = ', '.join(list(map(str, list_of_positives)))
joined_negatives = ', '.join(list(map(str, list_of_negatives)))
joined_evens = ', '.join(list(map(str, list_of_evens)))
joined_odds = ', '.join(list(map(str, list_of_odds)))

print(f'Positive: {joined_positives}')
print(f'Negative: {joined_negatives}')
print(f'Even: {joined_evens}')
print(f'Odd: {joined_odds}')
