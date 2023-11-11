
words = input().split()

for word in words:
    number_of_repetitions = len(word)
    print(f'{word * number_of_repetitions}', end='')