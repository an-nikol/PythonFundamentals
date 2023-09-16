
while True:
    word = input()
    reversed_word = ''
    if word == 'End':
        break
    elif word == 'SoftUni':
        continue
    else:
        for letter in word:
            reversed_word += letter * 2
        print(reversed_word)
